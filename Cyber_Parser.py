from html.parser import HTMLParser
import re
import json
import sys

VERBOSE = False

    
class CustomParser(HTMLParser):
    def __init__(self,seekers):
        super(CustomParser, self).__init__()
        self.depth = 0
        self.seekers = seekers

    def addSeeker(self,seeker):
        self.seekers.append(seeker)

    def update_seekers(self,data):
        for seeker in self.seekers:
            seeker.update_seek_state(data,self.depth)

    def check_seekers(self,data):
        for seeker in self.seekers:
            seeker.check(data,self.depth)

    def handle_starttag(self, tag, attrs):
        self.depth += 1
        self.update_seekers(str(tag))
        self.update_seekers(str(attrs))
        if VERBOSE:
            print("(D:",self.depth,") START TAG ", tag,": ",attrs)

    def handle_endtag(self, tag):
        self.depth -= 1
        self.update_seekers(str(tag))
        if VERBOSE:
            print("(D:",self.depth,") END TAG ", tag)

    def handle_comment(self, data):
        if VERBOSE:
            print("COMMENT: ", data)

        for seeker in self.seekers:
            for req in seeker.required_tags:
                if req == "!--":        
                    seeker.update_seek_state('!--',self.depth)
                    seeker.check(data,self.depth)

    def handle_data(self, data):
        if VERBOSE:
            print("DATA: ", data)
        self.check_seekers(data)

    def checkSeekers(self):
        for seeker in seekers:
            if seeker.bad_state:
                print(seeker.name,": FAIL (EXCLUSION ON ",seeker.bad_found[0][1],")")
            elif seeker.found:
                print(seeker.name,": FOUND (MATCH ON ",seeker.found[0][1],")")
            else:
                print(seeker.name,": NO MATCHES")

class Seeker():
    def __init__(self,name,terms,reqs,exclusions):
        self.found = []
        self.bad_found = []
        self.seek_state = False
        self.seek_text = terms
        self.required_tags = reqs
        self.exclude = exclusions
        self.bad_state = False
        self.name = name

    def add_seek_text(self,text):
        self.seek_text.append(text)

    def add_req(self,req):
        self.required_tags.append(req)
        
    def update_seek_state(self,data,depth):
        if self.seek_state is False:
            for str in self.required_tags:
                if str in data:
                    self.seek_state = depth
        else:
            if depth < self.seek_state:
                self.seek_state = False

    def check(self,data,depth):
        if self.seek_state is not False:
            for str in self.exclude:
                    if str in data:
                        self.bad_state = True
                        self.bad_found.append([depth,str])
            for str in self.seek_text:
                    if str in data:
                        self.found.append([depth,str])

    def isFound(self):
        if not self.found:
            return False
        else:
             return True


def json_to_seeker(data):
    seekers = []

    for key in data:
        cur_par = data[str(key)][0]
        seekers.append(Seeker(key,cur_par["terms"],cur_par["reqs"],cur_par["exclusions"]))
    return seekers


with open(sys.argv[1], 'r') as file:
    html_data = file.read()

with open(sys.argv[2]) as json_file:
    json_data = json.load(json_file)
    
seekers = json_to_seeker(json_data)

parser = CustomParser(seekers)

parser.feed(html_data)
parser.checkSeekers()


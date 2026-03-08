from gutenbergdammit.ziputils import retrieve
from pathlib import Path
import zipfile
import re

zf = zipfile.ZipFile("gutenberg-dammit-files-v002.zip")
# Remove the 'gutenberg-dammit/' from path 
book_files=[name.replace("gutenberg-dammit-files/", "") for name in zf.namelist() if ".txt" == Path(name).suffix]
pages=retrieve("gutenberg-dammit-files-v002.zip", book_files)

#regex = r"[^.?!]*(?<=[.?\s!])([\d]+[:]*[\d]+[ ]?|one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve)[ ]?(P[.]?M[.]?|A[.]?M[.]?|o'clock|till|[a]? quarter to|half[-]?past|in the [morningafternoonevening])(?=[\s.?!])[^.?!]*[.?!]"
#regex=r"[^.?!]*(?<=[.?\s!])((quarter|half) (past|to))?(one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve)?[-]?(eleven|twelve|thirteen|fourteen|fifteen|sixteen|seventeen|eighteen|nineteen|twenty|thirty|forty|fifty)?[-]?(one|two|three|four|five|six|seven|eight|nine)?(P[.]?M[.]?|A[.]?M[.]?|o'clock|till|[a]? (quarter|half) (past|to)|(in the )(morning|afternoon|evening))?(?=[\s.?!])[^.?!]*[.?!]"

regex=r"[^.?!]*(?<=[.?\s!])((one|two|three|four|five|six|seven|eight|nine|ten|eleven|tweleve|thirteen|fourteen|fifteen|sixteen|seventeen|eighteen|nineteen|((twenty|thirty|forty|fifty)[ ](one|two|three|four|five|six|seven|eight|nine)))[ ]?(minute[s]? (to|till|past)))?((quarter|half)[ ]?(past|to))?[ ]?((one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve)?[- ]?(one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|fourteen|fifteen|sixteen|seventeen|eighteen|nineteen|twenty)?[- ]?(one|two|three|four|five|six|seven|eight|nine)?)?[ ]?(P[.]?M[.]?|A[.]?M[.]?|o'clock|till|[a]? (quarter|half) (past|to)|(in the )(morning|afternoon|evening))?(?=[\s.?!])[^.?!]*[.?!]"

page=next(pages)
matches = re.finditer(regex, page, re.MULTILINE)
while True:
    matches = re.finditer(regex, page, re.MULTILINE)
    for matchNum, match in enumerate(matches, start=1):
        print("Match {matchNum}: {match}".format(matchNum = matchNum, match = match.group()))
    page=next(pages)

#times={"1:00PM":[], "2:00PM":[], "3:00PM": [], "4:00PM": [], "5:00PM": [], "6:00PM": [], "7:00PM": [], "8:00PM": [], "9:00PM": [], "10:00PM": [], "11:00PM": [], "12:00AM": [], "1:00AM": [], "2:00AM": [], "3:00AM": [], "4:00AM": [], "5:00AM": [], "6:00AM": [], "7:00AM": [], "8:00AM": [], "9:00AM": [], "10:00AM": [], "11:00AM": [], "12:00PM": []}

class Quote():

    def __init__(self, time, quote):
        self.time=time
        self.quote=quote

    def get_time(self):
        return self.time

    def get_quote(self):
        return self.quote

    def set_time(self, time):
        self.time=time

    def get_quote(self, quote):
        self.quote=quote

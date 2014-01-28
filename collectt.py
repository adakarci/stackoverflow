from bs4 import BeautifulSoup
import urllib
import logging


logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO)


class CollectQuestions:
    source = "http://stackoverflow.com/questions/"

    def __init__(self, start, end, tagname, tagname2):
        self.list2 = []
        self.tagname = tagname
        self.tagname2 = tagname2
        self.start = start
        self.end = end

    def run(self):
        count = 1
        current = 0
        for page in range(int(self.start), int(self.end)):
            list1 = []
            try:
                url = self.source+str(page)
                openurl = urllib.urlopen(url)
                openurlread = openurl.read()
                soup = BeautifulSoup(openurlread)
                findtag = soup.find("div", "post-taglist")
                for tag in findtag.findAll("a"):
                    list1.append(tag.string)
            except AttributeError:
                pass

            if self.tagname and self.tagname2 in list1:
                try:
                    question = soup.find("div", "post-text")
                    title = soup.find("a", "question-hyperlink")
                    self.list2.append(str(title)+str(question)+url)
                    current += 1
                except AttributeError:
                    pass

            logging.info(
                "%s questions passed,"
                "%s questions collected" % (count, current))
            count += 1
        return self.list2
#test
if __name__ == '__main__':
    col = CollectQuestions(18172822, 18172823, "jquery", "jquery")
    print col.run()

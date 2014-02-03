#-*- coding:utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from optparse import OptionParser
from collectt import CollectQuestions
from collector import CollectedDesign


def main():
    help_text = """
What are the search options ?
--main.py tagname1
-main.py tagname1 tagname2  - if you use this startnumber=1 endnumber=1000
-main.py tagname1 startnumber  endnumber
-main.py tagname1 tagname2 startnumber endnumber

"""
    parser = OptionParser(
        usage=help_text)

    (options, args) = parser.parse_args()

    if len(args) == 0 or len(args) > 4:
        parser.error("you can display help message [-h]")

    list = []
    for i in args:
        if i.isdigit():
            list.append(i)

    if len(list) == 0:
        start = 0
        end = 1000

    elif len(list) == 1:
        start = 0
        end = int(list[0])

    elif len(list) == 2:
        start = min(int(list[0]), int(list[1]))
        end = max(int(list[0]), int(list[1]))

    else:
        parser.error("you can display help message [-h]")

    list2 = []
    for i in args:
        if not i.isdigit():
            list2.append(i)

    if len(list2) == 0:
        parser.error("you can display help message [-h]")

    

    elif len(list2) == 1:
        tagname = list2[0]
        tagname2 = tagname
        
    elif len(list2) == 2:
        tagname2 = list2[1]
        tagname = list2[0]
    else:
        parser.error("you can display help message [-h]")

    collect = CollectQuestions(start, end, tagname, tagname2)
    collector = CollectedDesign()
    outfile = file("stackover_"+tagname+".html", "w")
    params = {"collecteddata": collect.run()}
    collector.run(params, outfile)

    outfile.close()


#test
if __name__ == "__main__":
    main()


class Article:
    def __init__(self,title,aid,date):
        self.title=title
        self.aid=aid
        self.date=date

    def __init__(self,a):
        self.title=a["title"]
        self.aid=a["aid"]
        self.date=a["date"]
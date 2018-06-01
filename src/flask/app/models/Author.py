class Author:
    def __init__(self,id,name,createdtime,note,token,filesindex):
        self.id=id
        self.name=name
        self.createdtime=createdtime
        self.note=note
        self.token=token
        self.filesindex=filesindex

    def __init__(self, u):
        self.id=u["id"]
        self.name=u["name"]
        self.createdtime=u["createdtime"]
        self.note=u["note"]
        self.token=u["token"]
        self.filesindex=u["filesindex"]
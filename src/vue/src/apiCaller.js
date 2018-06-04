export default class Caller{
    baseurl(){
        return'http://127.0.0.1:5000/api/v1/'
    }
    ajax(method, url, data) {
        var request = new XMLHttpRequest()
        request.open(method, url,false)
        request.send(data)
        if (request.readyState === 4) {
            if (request.status === 200) {
                return JSON.parse(request.responseText)
               } else {
                return{"state":"error"}
               }
        }
    }

    userURL(id,token)
    {
        return this.baseurl()+"user/"+id+(token?"?token="+token:"")
    }
    getUserinfo(id,token) {
        return this.ajax("GET",this.userURL(id,token),"")
    }
    articleListURL(id)
    {
        return this.baseurl()+"ArticleList/"+id
    }
    getArticleList(id){
        return this.ajax("GET",this.articleListURL(id),"")
    }
    articleURL(id,aid)
    {
        return this.baseurl()+"Article/"+id+(aid?"?aid="+aid:"")
    }
    getArticle(id,aid){
        return this.ajax("GET",this.articleURL(id,aid),"")
    }
    
    uploadArticle(id,token,aid,title,content){
        var data={}
        if(token){
            data.token=token
        }
        if(title){
            data.title=title
        }
        if(content!=undefined){
            data.content=content
        }
        return this.ajax("POST",this.articleURL(id,aid),JSON.stringify(data))
    }
    dearticleURL(id,aid)
    {
        return this.baseurl()+"deArticle/"+id+(aid?"?aid="+aid:"")
    }
    deleteArticle(id,token,aid){
        return this.ajax("POST",this.dearticleURL(id,aid),JSON.stringify({token:token}))
    }
};
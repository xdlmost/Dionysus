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
    getArticle(token,aid){}
    changeArticleTitle(token,aid){}
    updateArticle(token,aid){}
};
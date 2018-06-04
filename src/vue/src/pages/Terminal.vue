<template>
    <div>
        <el-header>
                <el-button type="text" disabled>
                    {{seletedArticle.title}}
                </el-button>
            <el-button type="primary" circle>
                <i class="el-icon-picture" />
            </el-button>
            <el-button type="primary" circle>
                <i class="el-icon-upload" />
            </el-button>
            <el-button type="primary" circle @click="save">
                <i class="el-icon-document" />
            </el-button>
        </el-header>
        <el-container>
            <el-aside width="200px">
                <el-row>
                    <el-col :span="4" :offset="18">
                        <el-button type="primary" circle @click="addArticle">
                            <i class="el-icon-plus" />
                        </el-button>
                    </el-col>
                </el-row>
                <ArticleSlot v-for="a in artilesList" :key="a.aid" :input="a" @select="select" @changeTitle="changeTitle" @deleteac="deleteac"/>
            </el-aside>
            <el-main>
                <div id="editor">
                    <textarea v-model="seletedContent"></textarea>
                    <MarkdownDisplayer v-bind:input="seletedContent"/>
                </div>
            </el-main>
        </el-container>

    </div>

</template>
<script>
import MarkdownDisplayer from "../components/common/MarkdownDisplayer";
import MarkdownEditor from "../components/common/MarkdownEditor";
import ArticleSlot from "../components/common/ArticleSlot";
import Caller from "../apiCaller.js"
const caller=new Caller()
export default {
  name: "Terminal",
  data() {
    return {
        seletedArticle:{title:'unknown'},
        seletedContent:"",
        artilesList: [
        {
          title: "a1"
        },
        {
          title: "a3"
        },
        {
          title: "a41"
        }
      ]
    };
  },
  components: {
    MarkdownDisplayer,
    ArticleSlot
  },
  mounted(){
    console.log(this.artilesList)
    var userinfo=caller.getUserinfo(this.$route.params.id,this.$route.query.token)
    if(userinfo.state!='ok'){
        this.$router.push("/about")
        return
    }
    var al=caller.getArticleList(this.$route.params.id)
    console.log(al)
    if(userinfo['state']=='ok'){
        this.artilesList=al['filesList']
        if((!this.artilesList)||this.artilesList.length==0)
        {
            this.seletedContent=''
        }else{
            this.seletedArticle=this.artilesList[0]
            var c=caller.getArticle(this.$route.params.id,this.artilesList[0].aid)
            if(c.state=='ok'){
                this.seletedContent=c.article.content
            }
        }   
    }
  },
  methods:{
      addArticle(){
          console.log("addArticle clicked")
          var s=caller.uploadArticle(this.$route.params.id,this.$route.query.token,undefined,'new article',"")
          console.log(s)
          if(s.state=='ok'){
              this.artilesList=s.al
              this.seletedArticle=this.artilesList[this.artilesList.length-1]
              this.seletedContent=s.lc
              console.log(this.seletedContent)
          }
      },
      save(){
          console.log(this.seletedArticle)
           var s=caller.uploadArticle(this.$route.params.id,this.$route.query.token,this.seletedArticle.aid,undefined,this.seletedContent)
           alert(s.state)
      },
      select(a){
          var c=caller.getArticle(this.$route.params.id,a.aid)
          if(c.state=='ok'){
                this.seletedContent=c.article.content
                this.seletedArticle=a
            }
      },
      changeTitle(a,changedTitle){
          var s=caller.uploadArticle(this.$route.params.id,this.$route.query.token,a.aid,changedTitle,undefined)
          if(s.state=='ok'){
              this.artilesList=s.al
              var tmp=a
              tmp.title=changedTitle
              this.seletedArticle=tmp
          }
      },
      deleteac(a){
          console.log("deleteac IN t")
          var f = caller.deleteArticle(this.$route.params.id,this.$route.query.token,a.aid)
          if(f.state=='ok'){
         this.$message({
            type: 'success',
            message: '删除成功!'
          });
          this.artilesList=f.al
          this.seletedArticle= this.artilesList.length==0?{title:'unknown'}:this.artilesList[0]
          }
      }
  }
};
</script>

<style scoped>
 #editor {
   height: 600px;
   font-family: 'Helvetica Neue', Arial, sans-serif;
   text-align:left;
 }
 #editor textarea {
   display: inline-block;
   width: 49%;
   height: 100%;
   vertical-align: top;
   box-sizing: border-box;
   padding: 0 20px;
 }
 #editor textarea {
   border: none;
   border-right: 1px solid #ccc;
   resize: none;
   outline: none;
   background-color: #f6f6f6;
   font-size: 14px;
   font-family: 'Monaco', courier, monospace;
   padding: 20px;
 }
</style>
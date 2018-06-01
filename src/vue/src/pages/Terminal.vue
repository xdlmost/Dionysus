<template>
    <div>
        <el-header>
                <el-button type="text" disabled>
                    {{seletedTitle}}
                </el-button>
            <el-button type="primary" circle>
                <i class="el-icon-picture" />
            </el-button>
            <el-button type="primary" circle>
                <i class="el-icon-upload" />
            </el-button>
            <el-button type="primary" circle>
                <i class="el-icon-document" />
            </el-button>
        </el-header>
        <el-container>
            <el-aside width="200px">
                <el-row>
                    <el-col :span="4" :offset="18">
                        <el-button type="primary" circle>
                            <i class="el-icon-plus" />
                        </el-button>
                    </el-col>
                </el-row>
                <ArticleSlot v-for="a in artilesList" :key="a.title" :input="a" />
            </el-aside>
            <el-main>
                <MarkdownEditor/>
            </el-main>
        </el-container>

    </div>

</template>
<script>
import MarkdownEditor from "../components/common/MarkdownEditor";
import ArticleSlot from "../components/common/ArticleSlot";
import Caller from "../apiCaller.js"
const caller=new Caller()
export default {
  name: "Terminal",
  data() {
    return {
        seletedTitle:"dddddd",
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
    MarkdownEditor,
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
        seletedTitle=this.artilesList
    }
  },
};
</script>
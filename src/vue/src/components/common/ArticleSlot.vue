<template>
    <div>
        <el-row>
            <el-col :span="16">
                <el-button v-show="!editable" type="text" @click="select">
                    {{input.title}}
                </el-button>
                <el-input v-show="editable" v-model="title_tmp">
                </el-input>
            </el-col>
            <el-col :span="4">
                <el-button v-show="!editable" type="text" @click="ToEditble">
                    <i class="el-icon-edit"></i>
                </el-button>
                <el-button v-show="editable" type="text" @click="EditOK">
                    <i class="el-icon-check"></i>
                </el-button>
            </el-col>
            <el-col :span="4">
                <el-button v-show="!editable"  type="text" @click="ToDelete">
                    <i class="el-icon-delete"></i>
                </el-button>
                <el-button v-show="editable" type="text" @click="EditCancel">
                    <i class="el-icon-close"></i>
                </el-button>
            </el-col>
        </el-row>
    </div>
</template>

<script>
export default {
    name:'ArticleSlot',
    data () {
        return {
            editable:false,
            title_tmp:"title"
        }
    },
    props:['input'],
    methods:{
        ToDelete(env)
        {
            this.$confirm('此操作将永久"'+this.input.title+'", 是否继续?', '提示', {
          confirmButtonText: '确定',
          cancelButtonText: '取消',
          type: 'warning'
        }).then(() => {
             console.log("deleteac IN A")
             this.$emit('deleteac',this.input)
        }).catch(() => {
          this.$message({
            type: 'info',
            message: '已取消删除'
          });          
        });
        },
        ToEditble(evn)
        {
            this.title_tmp=this.input.title
            this.editable=true
        },
        EditOK(env)
        {
            this.editable=false
            if(this.title_tmp!=this.input.title){
                this.$emit('changeTitle',this.input,this.title_tmp)
            }
        },
        EditCancel(env)
        {
            this.editable=false
        },
        select(){
            this.$emit('select',this.input)
        }
    }
}
</script>

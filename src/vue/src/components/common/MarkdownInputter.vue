<template>
    <textarea v-model="input" @input="mdc" @show="mdc" ></textarea>
</template>
<script>
export default {
  name:'MarkdownInputter',
  data ()
  {
      return {
          input:'# Markdown Test \n\n`ddd`\n\n*ddd*\n\n__ddd__\n\n> dd\n\n|name|po|\n|:-:|:-:|\n|dd|dd|\n|ee|ee|\n\n```c\n#include <string>\nint main ()\n{\n    printf("hehe");\n}\n```\n'
      }
  },
  methods: {
    mdc() {
        this.$emit('mdc2',this.input)
        }
    },
    mounted(){
        console.log('mounted')
        this.$emit('mdc2',this.input)
    }
}
</script>

<style scoped>
 textarea {
   display: inline-block;
   width: 49%;
   height: 100%;
   vertical-align: top;
   box-sizing: border-box;
   padding: 0 20px;
 }
 textarea {
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

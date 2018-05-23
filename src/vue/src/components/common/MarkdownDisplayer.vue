<template>
    <div class="markdown-body mddisplay" v-html="compiledMarkdown" ></div>
</template>

<script>
import marked from 'marked'
import Hljs from 'highlight.js'
import 'highlight.js/styles/default.css'
import '../../assets/css/md.css'
var rendererMD = new marked.Renderer()

rendererMD.code = function (code, language) {
  return '<pre class="hljs ' + language + '">' + Hljs.highlightAuto(code).value + '</pre>'
}
marked.setOptions({
  renderer: rendererMD,
  gfm: true,
  tables: true,
  breaks: false,
  pedantic: false,
  sanitize: false,
  smartLists: true,
  smartypants: false
})
export default {
  /*data () {
    return {
      input: '# Markdown Test \n\n`ddd`\n\n*ddd*\n\n__ddd__\n\n> dd\n\n|name|po|\n|:-:|:-:|\n|dd|dd|\n|ee|ee|\n\n```c\n#include <string>\nint main ()\n{\n    printf("hehe");\n}\n```\n'
    }
  },*/
  name:'MarkdownDisplayer',
  computed: {
    compiledMarkdown: function () {
      return marked(this.input, { sanitize: true })
    }
  },
  props:['input']
}
</script>

<style scoped>

 div.mddisplay {
   display: inline-block;
   width: 49%;
   height: 100%;
   vertical-align: top;
   box-sizing: border-box;
   padding: 0 20px;
   overflow:scroll
 }
</style>
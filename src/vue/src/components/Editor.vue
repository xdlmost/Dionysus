<template>
   <div id="editor">
     <textarea v-model="input"></textarea>
     <div class="markdown-body" v-html="compiledMarkdown" ></div>
   </div>
</template>
<script>
import marked from 'marked'
import Hljs from 'highlight.js'
import 'highlight.js/styles/default.css'
import '../assets/md.css'
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
  data () {
    return {
      input: '# Markdown Test \n\n`ddd`\n\n*ddd*\n\n__ddd__\n\n> dd\n\n|name|po|\n|:-:|:-:|\n|dd|dd|\n|ee|ee|\n\n```c\n#include <string>\nint main ()\n{\n    printf("hehe");\n}\n```\n'
    }
  },
  computed: {
    compiledMarkdown: function () {
      return marked(this.input, { sanitize: true })
    }
  }
}
</script>

<style>
 #editor {
   height: 600px;
   font-family: 'Helvetica Neue', Arial, sans-serif;
   text-align:left;
 }

 textarea, #editor div {
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

 div.markdown-body
 {
   overflow:scroll
 }

</style>

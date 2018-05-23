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
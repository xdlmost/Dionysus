<template>
    <div id="editor">
        <MarkdownInputter :input='paintext'/>
        <MarkdownDisplayer :input='paintext'/>
    </div>
</template>
<script>
import MarkdownDisplayer from './MarkdownDisplayer'
import MarkdownInputter from './MarkdownInputter'
export default {
    name:'MarkdownEditor',
    data () {
        return {
            paintext: '# Markdown Test \n\n`ddd`\n\n*ddd*\n\n__ddd__\n\n> dd\n\n|name|po|\n|:-:|:-:|\n|dd|dd|\n|ee|ee|\n\n```c\n#include <string>\nint main ()\n{\n    printf("hehe");\n}\n```\n'
        }
    },
    components: {
        MarkdownDisplayer,MarkdownInputter
    }
}
</script>
<style scoped>
 #editor {
   height: 600px;
   font-family: 'Helvetica Neue', Arial, sans-serif;
   text-align:left;
 }
</style>

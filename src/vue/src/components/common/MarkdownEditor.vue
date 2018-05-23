<template>
    <div id="editor">
        <MarkdownInputter   @mdc2="mdc"/>
        <MarkdownDisplayer v-bind:input="paintext"/>
    </div>
</template>
<script>
import MarkdownDisplayer from './MarkdownDisplayer'
import MarkdownInputter from './MarkdownInputter'
export default {
    name:'MarkdownEditor',
    data () {
        return {
            paintext: ''
        }
    },
    components: {
        MarkdownDisplayer,MarkdownInputter
    },
    methods:{  
                mdc(mgs){  
                    this.paintext=mgs
                }  
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

<template>
    <textarea v-model="input" @change="mdc"></textarea>
</template>
<script>
export default {
  name:'MarkdownInputter',
  data ()
  {
      return {
          input:''
      }
  },
  methods: {
    mdc() {
        Hub.$emit('mdc',input); //Hub触发事件
    }
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

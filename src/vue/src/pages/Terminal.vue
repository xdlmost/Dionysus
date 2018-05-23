<template>
    <div>
        <h1>Terminal page</h1>
        <MarkdownEditor/>
    </div>

</template>
<script>
import MarkdownEditor from '../components/common/MarkdownEditor'
export default {
    name:'Terminal',
    components: {
        MarkdownEditor
    }
}
</script>
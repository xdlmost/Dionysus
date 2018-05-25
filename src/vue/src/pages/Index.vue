<template>
  <div>
    <Layout>
      <el-container>
        <Header-Nav></Header-Nav>

        <el-main class="main">Main</el-main>

        <el-footer class="footer">Footer</el-footer>
      </el-container>
    </Layout>
  </div>
</template>

<script>
import Layout from "../components/common/Layout";
import HeaderNav from "../components/common/HeaderNav";

export default {
  name: "Index",
  components: {
    Layout,
    HeaderNav
  }
};
</script>

<style>
.main {
  height: 1000px;
  background-color: #d3dce6;
}

.footer {
  height: 60px;
  width: 100%;
  background-color: #cccccc;
}
</style>

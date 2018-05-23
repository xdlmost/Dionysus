<template>
    <div>
        <el-row>
          <el-col :span="4"><div class="grid-content bg-purple"></div></el-col>
          <el-col :span="16"><div class="grid-content bg-purple-light">
            <el-col :span="8"></el-col>
            <el-col :span="24">
              <el-button type="text" size="small">文字按钮</el-button>
            <el-button type="text" size="small">文字按钮</el-button>
            <el-button type="text" size="small">文字按钮</el-button>
            <el-button type="text" size="small">文字按钮</el-button>
            </el-col>

            </div></el-col>
          <el-col :span="4"><div class="grid-content bg-purple"></div></el-col>
        </el-row>
        <!-- <el-menu :default-active="activeIndex" class="el-menu-demo" mode="horizontal" @select="handleSelect">
          <el-menu-item index="1">处理中心</el-menu-item>
          <el-submenu index="2">
            <template slot="title">我的工作台</template>
            <el-menu-item index="2-1">选项1</el-menu-item>
            <el-menu-item index="2-2">选项2</el-menu-item>
            <el-menu-item index="2-3">选项3</el-menu-item>
            <el-submenu index="2-4">
              <template slot="title">选项4</template>
              <el-menu-item index="2-4-1">选项1</el-menu-item>
              <el-menu-item index="2-4-2">选项2</el-menu-item>
              <el-menu-item index="2-4-3">选项3</el-menu-item>
            </el-submenu>
          </el-submenu>
          <el-menu-item index="3" disabled>消息中心</el-menu-item>
          <el-menu-item index="4"><a href="https://www.ele.me" target="_blank">订单管理</a></el-menu-item>
        </el-menu> -->

        <!-- <img src="./assets/logo.png"> -->
        <!-- <hello v-if="show"></hello> -->
        <!-- <button v-on:click="show = !show">Toggle</button> -->
        <!-- <router-view/> -->
    </div>
</template>

<script>
// import HeaderNav from "./components/common/HeaderNav";

// import Hello from "./components/Hello";
// import First from './First'
// import VHtml from './components/VHtml'

export default {
  name: "Index",
  components: {
    // HeaderNav
    // Hello
    // VHtml
  }
  // data() {
  //   return {
  //     show: true
  //   };
  // }
};
</script>

<style>
.el-row {
  margin-bottom: 0px;
  /* &:last-child {
    margin-bottom: 0;
  } */
}
.el-col {
  border-radius: 4px;
}
.bg-purple-dark {
  background: #99a9bf;
}
.bg-purple {
  background: #d3dce6;
}
.bg-purple-light {
  background: #e5e9f2;
}
.grid-content {
  border-radius: 4px;
  min-height: 36px;
}
</style>

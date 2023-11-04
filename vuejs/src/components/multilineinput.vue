<template>
    <div class="multiline-input">
      <label class="input-label">{{ label }}</label>
      <textarea class="input-box" :style="{ borderBottomColor: underlineColor }" style="width: 90%;" v-model="value"></textarea>
    </div>
  </template>
  
  <script>
  export default {
    props: {
      label: String,
      underlineColor: {
        type: String,
        default: "#8facca"
      },
      value: String
    }
  };
  </script>
  
  <style scoped>
  .multiline-input {
    display: flex;
    flex-direction: column;
    margin-bottom: 20px;
  }
  
  .input-label {
    width: 30%;
    padding: 5px;
  }
  
  .input-box {
    border: none;
    padding: 5px;
    width: 70%;
    background-color: transparent;
    outline: none;
    border-bottom: 2px solid #8facca;
    resize: none; /* 防止用户手动调整文本框大小 */
    white-space: pre-wrap; /* 换行显示 */
  }
  </style>
  
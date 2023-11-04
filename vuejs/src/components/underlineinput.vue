<template>
    <div class="underline-input">
      <label class="input-label">{{ label }}</label>
      <input type="text" class="input-box" :style="{ borderBottomColor: underlineColor }" v-model="value">
    </div>
  </template>
  
  <script>
  export default {
    props: {
      label: String,
      underlineColor: {
        type: String,
        default: "#805619"
      },
      value: String
    }
  };
  </script>
  
  <style scoped>
  .underline-input {
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
    border-bottom: 2px solid #805619;
    padding: 5px;
    width: 70%;
    background-color: transparent;
    outline: none;
  }
  </style>
  
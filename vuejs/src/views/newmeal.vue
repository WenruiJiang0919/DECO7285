<template>
  <div class="container" style="width: 60%;">
    <h1 class="my-4" style="color: #cc7d25;">Upload Recipe</h1>

    <div class="row">
      <div class="col-md-5">
        <div class="mt-3" style="height: 200px;">
          <img :src="imagePreview" alt="Recipe Image" class="img-thumbnail" style="width: 50%;">
        </div>
        <input type="file" class="form-control-file" id="recipeImage" @change="previewImage" accept="image/*">
      </div>
      <div class="col-md-7">
        <div class="underline-input">
          <label class="input-label">recipeName</label>
          <input type="text" class="input-box" :style="{ borderBottomColor: underlineColor }" v-model="recipe.recipeName">
        </div>
        <div class="underline-input">
          <label class="input-label">Length of Time</label>
          <input type="text" class="input-box" :style="{ borderBottomColor: underlineColor }"
            v-model="recipe.LengthOfTime">
        </div>
        <div class="underline-input">
          <label class="input-label">Cuisine</label>
          <input type="text" class="input-box" :style="{ borderBottomColor: underlineColor }" v-model="recipe.Cuisine">
        </div>
      </div>
    </div>

    <div class="mt-4">
      <div class="multiline-input">
        <label class="input-label">Ingredients</label>
        <textarea class="input-box" :style="{ borderBottomColor: underlineColor }" style="width: 90%;"
          v-model="recipe.Ingredients"></textarea>
      </div>
      <div class="multiline-input">
        <label class="input-label">Description</label>
        <textarea class="input-box" :style="{ borderBottomColor: underlineColor }" style="width: 90%;"
          v-model="recipe.Description"></textarea>
      </div>
      <div class="multiline-input">
        <label class="input-label">steps</label>
        <textarea class="input-box" :style="{ borderBottomColor: underlineColor }" style="width: 90%;"
          v-model="recipe.Steps"></textarea>
      </div>
    </div>

    <button class="btn btn-primary mt-4" @click="uploadRecipe">upload Recipe</button>
  </div>
</template>
  
<script>
import UnderlineInput from '../components/underlineinput.vue'; // 导入上面创建的组件
import MultilineInput from '../components/multilineinput.vue' // 导入上面创建的组件
import { uploadRecipeApi } from '../api/meal'
import axios from 'axios';
export default {
  name: 'newmeal',
  components: {
    UnderlineInput,
    MultilineInput
  },
  data() {
    return {
      imagePreview: null,
      value3: 'xxxx',
      name: '',
      recipe: {
        username: localStorage.getItem('username'),
        recipeName: '',
        imgPath: '',
        Ingredients: '',
        LengthOfTime: '',
        Description: "",
        Cuisine: '',
        Steps: ''
      }
    };
  },
  methods: {
    previewImage(event) {
      const file = event.target.files[0];
      this.selectedImage = file;
      if (file) {
        const reader = new FileReader();
        reader.readAsDataURL(file);
        reader.onload = () => {
          this.imagePreview = reader.result;
        };
      }
    },
    uploadRecipe() {
      const formData = new FormData();
      formData.append('image', this.selectedImage);
      axios.post('/uploadImg', formData, {
        headers: { 'content-type': 'multipart/form-data' },
      }).then((res) => {
        console.log(res);
        this.recipe.imgPath = res.data.imgPath;
        uploadRecipeApi(this.recipe).then(response => {
          console.log(response)
          this.$vs.notification({
            color: 'warn',
            title: 'Message',
            text: `Post Success!`
          })
          this.$router.push({ path: '/Profile' });
        }).catch(error => {
          // this.$Message.error(error.status)
          console.log(error)
          this.$vs.notification({
            color: 'danger',
            title: 'Message',
            text: `Error Happened! Please Retry Later`
          })
        })
      }).catch((err) => {
        console.log(err);
      });
      // // 处理上传菜谱的逻辑
      // console.log('上传菜谱:', this.recipe);
      // // 发送菜谱数据到后端
    }
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

.btn-primary {
  float: center;
  background-color: #f39120;
  border: none;
}

.btn-primary:hover {
  background-color: #f39120;
  /* 鼠标悬停时改变背景颜色 */
  border: #f2cca0;
}
</style>
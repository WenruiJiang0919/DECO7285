import request from '@/util/request'

export function uploadMealImg(formData) {
  return request({
    url:'/uploadImg',
    method:'post',
    headers: {
      // 'token': localStorage.getItem('token'),
      'Content-Type': 'multipart/form-data' },
    data:formData
  })
}
// editRecipeApi
export function editRecipeApi(newRecipe,recipe_id) {
  let token = localStorage.getItem('token')
  let palce=' ';
  const bearerToken = `Bearer${palce}${token}`;
  console.log(newRecipe);
  return request({
    url:'/update-recipe/'+recipe_id,
    method:'post',
    headers: {
      'Authorization': bearerToken },
    data:newRecipe
  })
}
export function uploadRecipeApi(formData) {
  let token = localStorage.getItem('token')
  let palce=' ';
  const bearerToken = `Bearer${palce}${token}`;
  console.log(formData);
  return request({
    url:'/upload-recipe',
    method:'post',
    headers: {
      'Authorization': bearerToken },
    data:formData
  })
}


export function fetchRecipesBycuision(formData) {
  return request({
    url:'/get-recipes-grouped-by-cuisine',
    method:'post',
    headers: {
      'Content-Type': 'application/JSON' },
    data:formData
  })
}

export function likeRecipeApi(recipe_id,username) {
  return request({
    url:'/like-recipe/'+recipe_id,
    method:'post',
    headers: {
      'Content-Type': 'application/JSON' },
    data:{username}
  })
}
export function unlikeRecipeApi(recipe_id,username) {
  return request({
    url:'/unlike-recipe/'+recipe_id,
    method:'post',
    headers: {
      'Content-Type': 'application/JSON' },
    data:{username}
  })
}
export function userlikeRecipeApi(username) {
  return request({
    url:'/get-user-liked-recipes',
    method:'post',
    headers: {
      'Content-Type': 'application/JSON' },
    data:{username}
  })
}
export function usercommentRecipeApi(username) {
  return request({
    url:'/get-user-commented-recipes',
    method:'post',
    headers: {
      'Content-Type': 'application/JSON' },
    data:{username}
  })
}
export function userfavoriteRecipeApi(username) {
  return request({
    url:'/get-user-favorite-recipes',
    method:'post',
    headers: {
      'Content-Type': 'application/JSON' },
    data:{username}
  })
}
export function unfavoriteRecipeApi(recipe_id,username) {
  return request({
    url:'/unfavorite-recipe/'+recipe_id,
    method:'post',
    headers: {
      'Content-Type': 'application/JSON' },
    data:{username}
  })
}
export function favoriteRecipeApi(recipe_id,username) {
  return request({
    url:'/favorite-recipe/'+recipe_id,
    method:'post',
    headers: {
      'Content-Type': 'application/JSON' },
    data:{username}
  })
}
export function getShowRecipeApi(username,recipe_id) {
  return request({
    url:'/get-recipe/'+recipe_id,
    method:'post',
    headers: {
      'Content-Type': 'application/JSON' },
    data:{username}
  })
}
export function commentRecipeApi(recipe_id,username,comment) {
  return request({
    url:'/comment-recipe/'+recipe_id,
    method:'post',
    headers: {
      'Content-Type': 'application/JSON' },
    data:{username,comment}
  })
}
export function getAdminRecipe(username) {
  return request({
    url:'/get-recipes/'+username,
    method:'post',
    headers: {
      'Content-Type': 'application/JSON' },
      data:{username:localStorage.getItem('username')}
  })
}
export function getAllRecipe() {
  return request({
    url:'/get-all-recipes',
    method:'post',
    headers: {
      'Content-Type': 'application/JSON' },
      data:{username:localStorage.getItem('username')
    }
  })
}

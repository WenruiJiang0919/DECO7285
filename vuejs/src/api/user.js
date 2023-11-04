import request from '@/util/request'

export function LoginRequest(username,password) {
  return request({
    url:'/login',
    method:'post',
    headers: {
      // 'token': localStorage.getItem('token'),
      'Content-Type': 'application/JSON' },
    data:{'username':username,'password':password}
  })
}

export function RegisterRequest(username,password) {
  return request({
    url:'/register',
    method:'post',
    headers: {
      // 'token': localStorage.getItem('token'),
      'Content-Type': 'application/JSON' },
    data:{'username':username,'password':password}
  })
}
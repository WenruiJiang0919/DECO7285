/* eslint-disable */
import axios from 'axios'

const utils = axios.create({
    baseURL: 'http://localhost:5000',
    timeout: 15000
})

export default utils

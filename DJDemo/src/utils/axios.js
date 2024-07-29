import axios from "axios";
import * as process from "echarts";

// 创建axios实例
const instance = axios.create({
    baseURL: 'http://127.0.0.1:5000', // 设置基础 URL
    timeout: 10000, // 请求超时时间
});

//请求拦截
instance.interceptors.request.use(
    config=>{
        // 输出请求信息
        // console.log('Request URL:', config.url);
        // console.log('Request Method:', config.method);
        // console.log('Request Headers:', config.headers);
        // console.log('Request Params:', config.params);
        // console.log('Request Data:', config.data);

        return config;
    }
)

// 响应拦截
instance.interceptors.response.use(
    response => {
        // console.log(response.data);
        response.data = typeof response.data === 'string' ? JSON.parse(response.data) : response.data;
        return response.data;
    },
    error => {
        return Promise.reject(error);
    }
);

export default instance;

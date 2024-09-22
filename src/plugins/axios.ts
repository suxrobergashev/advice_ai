import axios from "axios";

const API = axios.create({
  baseURL: import.meta.env.VITE_APP_BASE_URL,
});

const staticUser =
  "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzI4MTYxNDkwLCJpYXQiOjE3MjY5NTE4OTAsImp0aSI6IjFlNjAwYTQ5ZDQzMTRhY2U4NzRjYjc1ZjMyZDJlM2JhIiwidXNlcl9pZCI6NH0.DPBXl8W6LXcc_Do0wsYiJruOshoo1Y9CvsRpuM-c6iU";

API.interceptors.request.use((config) => {
  const token = localStorage.getItem("token") || staticUser;
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

export default API;

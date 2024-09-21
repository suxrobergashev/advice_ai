import axios from "axios";

const API = axios.create({
  baseURL: import.meta.env.VITE_APP_BASE_URL,
});

const staticUser =
  "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzI2OTUxNjMwLCJpYXQiOjE3MjY5NTEzMzAsImp0aSI6ImNhMjMyYjkwMzNkMjQ5MjY4ZmUxYWY1ZWMxNjNiNzFiIiwidXNlcl9pZCI6NH0.X7mnYOR8JUjQfHzTx-G6y9I8XaGVCamwk778Z1JpJQo";

API.interceptors.request.use((config) => {
  const token = localStorage.getItem("token") || staticUser;
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

export default API;

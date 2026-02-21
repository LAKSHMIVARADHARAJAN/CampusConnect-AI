
import axios from 'axios';
import { LoginResponse, ChatResponse, Student } from '../types';

const BASE_URL = 'http://127.0.0.1:8000';

const api = axios.create({
  baseURL: BASE_URL,
});

export const authApi = {
  login: async (unique_id: string, password: string): Promise<LoginResponse> => {
    // Backend expects query params for POST /auth/login as per user request
    const response = await api.post<LoginResponse>(`/auth/login?unique_id=${encodeURIComponent(unique_id)}&password=${encodeURIComponent(password)}`);
    return response.data;
  },
};

export const chatApi = {
  sendMessage: async (query: string): Promise<ChatResponse> => {
    const response = await api.get<ChatResponse>(`/chat?query=${encodeURIComponent(query)}`);
    return response.data;
  },
};

export const studentApi = {
  getDetails: async (reg_no: string, token: string): Promise<Student> => {
    const response = await api.get<Student>(`/students/${reg_no}`, {
      headers: {
        Authorization: `Bearer ${token}`,
      },
    });
    return response.data;
  },
};


export interface Student {
  reg_no: string;
  name: string;
  class: string;
  blood_group: string;
  mobile_number: string;
  parent_name: string;
  parent_number: string;
  cgpa: string;
  current_arrear: string;
}

export interface ChatMessage {
  id: string;
  role: 'user' | 'assistant';
  content: string;
  timestamp: number;
}

export interface LoginResponse {
  access_token: string;
  token_type: string;
}

export interface ChatResponse {
  response: string;
}

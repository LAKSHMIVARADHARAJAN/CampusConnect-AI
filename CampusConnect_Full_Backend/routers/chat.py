#chat.py
from fastapi import APIRouter, Query
from chatbot_service import handle_query


router = APIRouter()

@router.get("/")
def chatbot(query: str = Query(...)):
    response = handle_query(query)
    return {"response": response}


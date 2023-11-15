from fastapi import APIRouter, HTTPException, Depends, Request
from .models import Form
from typing import Dict

router = APIRouter()

@router.post('/get_form')
async def get_form(request: Request):
    form_data = await request.form()
    # Логика поиска шаблона формы и валидации полей
    return {'received_data': form_data}
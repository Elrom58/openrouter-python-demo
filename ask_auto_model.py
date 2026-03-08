#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Dateiname:   ask_auto_model.py
Autor:       Rainer Mroch
Datum:       2026-03-08
Version:     1.0.0

Beschreibung:
Automatische Modellwahl basierend auf Verfügbarkeit und Leistung

Details:
- Zweck: Zuverlässige Antworten durch automatische Auswahl des besten Modells
- Eingaben: Eingaben (z.B. Daten, Parameter)
- Ausgaben: Ausgaben (z.B. Modelle, Metriken)
- Abhängigkeiten: dotenv, os und requests

"""


from dotenv import load_dotenv
import os
import requests

load_dotenv()


OPENROUTER_API_URL = "https://openrouter.ai/api/v1/chat/completions"

api_key = os.getenv("OPENROUTER_API_KEY")

headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}
payload = {
    "model": "openrouter/auto",
    "messages": [{"role": "user", "content": "Say hello in one sentence."}]
}
response = requests.post(OPENROUTER_API_URL, headers=headers, json=payload)
data = response.json()

print(f"Model: {data.get('model')}")
print(f"Response: {data['choices'][0]['message']['content']}")
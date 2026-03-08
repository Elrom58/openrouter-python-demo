#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Dateiname:   get_models.py
Autor:       Rainer Mroch
Datum:       2026-03-08
Version:     1.0.0

Beschreibung:
Verbindung zur OpenRouter API herstellen und verfügbare Modelle abrufen

Details:
- Zweck: Abrufen und Anzeigen der verfügbaren Modelle von OpenRouter
- Eingaben: Keine direkten Eingaben, aber benötigt wird ein gültiger API-Schlüssel in der .env-Datei
- Ausgaben: Anzahl der gefundenen Modelle und Beispiele der Modell-IDs
- Abhängigkeiten: dotenv, os und requests

"""


from dotenv import load_dotenv
import os
import requests

load_dotenv()

OPENROUTER_MODELS_URL = "https://openrouter.ai/api/v1/models"

api_key = os.getenv("OPENROUTER_API_KEY")

if not api_key:
    raise ValueError("OPENROUTER_API_KEY nicht in .env gefunden oder leer")

print("API Key geladen (erste 10 Zeichen):", api_key[:10] + "...")


headers = {"Authorization": f"Bearer {api_key}"}
response = requests.get(OPENROUTER_MODELS_URL, headers=headers)
data = response.json()

models = data.get("data", [])
print(f"Success! Found {len(models)} models via OpenRouter.")
print(f"Examples: {', '.join(m['id'] for m in models[:5])}")
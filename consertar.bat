@echo off
cd /d C:\Time3IA
taskkill /F /IM python.exe >nul 2>&1
timeout /t 2 /nobreak >nul
powershell -Command "Set-Content -Path 'bracos.py' -Value @'
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import os, webbrowser
app = Flask(__name__)
CORS(app)
BASE = r\"C:\Time3IA\pastas\"
os.makedirs(BASE, exist_ok=True)
@app.route(\"/\")
def home():
    return send_from_directory(r\"C:\Time3IA\", \"time3-final.html\")
@app.route(\"/teste\")
def teste():
    return \"CEREBRO LIGADO!\"
@app.route(\"/api/chat\", methods=[\"POST\"])
def chat():
    data = request.get_json() or {}
    texto = (data.get(\"mensagem\") or \"\").lower()
    print(\"CHEGOU:\", texto)
    if \"lista de tarefas\" in texto:
        pasta = os.path.join(BASE, \"lista-tarefas\")
        os.makedirs(pasta, exist_ok=True)
        html = \"<html><body style=font-family:Arial;background:#1a1a2e;color:white;text-align:center;padding:30px><h1>Lista de Tarefas</h1><input id=t placeholder=Digite><button onclick=add()>Adicionar</button><ul id=l></ul><script>function add(){let v=document.getElementById('t').value;if(!v)return;let li=document.createElement('li');li.innerHTML=v;document.getElementById('l').appendChild(li);}</script></body></html>\"
        open(os.path.join(pasta,\"index.html\"),\"w\",encoding=\"utf-8\").write(html)
        webbrowser.open(os.path.join(pasta,\"index.html\"))
        return jsonify({\"resposta\": \"Pronto! Fazedor criou seu APP DE LISTA DE TAREFAS e ja abri ele!\"})
    if \"cria pasta\" in texto:
        nome = texto.replace(\"cria pasta\",\"\").strip() or \"nova-pasta\"
        os.makedirs(os.path.join(BASE, nome), exist_ok=True)
        return jsonify({\"resposta\": f\"Pronto! Criei a pasta {nome}\"})
    if \"calculadora\" in texto:
        os.system(\"calc\")
        return jsonify({\"resposta\": \"Abri a calculadora!\"})
    if \"spotify\" in texto:
        webbrowser.open(\"https://open.spotify.com\")
        return jsonify({\"resposta\": \"Abri o Spotify!\"})
    return jsonify({\"resposta\": \"Fala: cria pasta teste, faz um app de lista de tarefas\"})
if __name__ == \"__main__\":
    app.run(port=5000)
'@"
echo CONSERTADO! Agora vou ligar...
start "" python bracos.py
timeout /t 3 /nobreak >nul
start "" http://127.0.0.1:5000/teste
pause
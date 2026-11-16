from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import os, webbrowser
app = Flask(__name__)
CORS(app)
BASE = r"C:\Time3IA\pastas"
os.makedirs(BASE, exist_ok=True)

@app.route('/')
def home():
    return send_from_directory(r"C:\Time3IA", "time3-final.html")

@app.route('/teste')
def teste():
    return "CEREBRO LIGADO! Se tu ta vendo isso, o bracos.py ta funcionando!"

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.get_json() or {}
    texto = (data.get('mensagem') or '').lower()
    print("CHEGOU:", texto)
    if 'lista de tarefas' in texto:
        pasta = os.path.join(BASE, 'lista-tarefas')
        os.makedirs(pasta, exist_ok=True)
        html = "<html><body style='font-family:Arial;background:#1a1a2e;color:white;text-align:center;padding:30px'><h1>✅ Lista de Tarefas</h1><input id=t placeholder='Digite tarefa...' style='padding:12px;width:300px'><button onclick='add()' style='padding:12px;background:#a855f7;color:white;border:none'>Adicionar</button><ul id=l></ul><script>function add(){let v=document.getElementById('t').value;if(!v)return;let li=document.createElement('li');li.innerHTML=v+' <span onclick=\"this.parentElement.remove()\">❌</span>';document.getElementById('l').appendChild(li);document.getElementById('t').value='';}</script></body></html>"
        caminho = os.path.join(pasta, 'index.html')
        open(caminho,'w',encoding='utf-8').write(html)
        webbrowser.open(caminho)
        return jsonify({'resposta': 'Pronto! Fazedor criou seu APP DE LISTA DE TAREFAS e já abri ele!'})
    if 'cria pasta' in texto or 'criar pasta' in texto:
        nome = texto.replace('cria pasta','').replace('criar pasta','').strip() or 'nova-pasta'
        os.makedirs(os.path.join(BASE, nome), exist_ok=True)
        return jsonify({'resposta': f'Pronto! Criei a pasta {nome}'})
    if 'calculadora' in texto:
        os.system('calc')
        return jsonify({'resposta': 'Abri a calculadora!'})
    if 'spotify' in texto:
        webbrowser.open('https://open.spotify.com')
        return jsonify({'resposta': 'Abri o Spotify!'})
    return jsonify({'resposta': 'Fala: cria pasta teste, faz um app de lista de tarefas, cria app calculadora, abre o spotify'})

if __name__ == '__main__':
    app.run(port=5000)
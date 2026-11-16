import pathlib
base = pathlib.Path("C:/Time3IA")
html = '''<!DOCTYPE html>
<html><head><meta charset="utf-8"><title>Time 3 IA - Chefe</title>
<style>
body{margin:0;font-family:Arial;background:#0f0a1a;color:white;display:flex;height:100vh}
.side{width:260px;background:#1a1030;padding:18px}
.side h2{margin:0}
.on{color:#22c55e;font-weight:bold}
.btn{background:#7c3aed;border:0;color:white;padding:12px;margin:6px 0;border-radius:12px;cursor:pointer;width:100%;text-align:left;font-size:15px}
.btn:hover{background:#a855f7}
.btn.ativo{background:#22c55e}
.main{flex:1;padding:20px;display:flex;flex-direction:column}
#chat{flex:1;overflow:auto;background:#1e1433;border-radius:16px;padding:16px}
.msg{margin:8px 0;padding:10px 14px;border-radius:12px;max-width:85%}
.eu{background:#7c3aed;margin-left:auto;text-align:right}
.chefe{background:#2d1b4e}
.box{display:flex;gap:10px;margin-top:12px}
input{flex:1;padding:14px;border-radius:12px;border:0;outline:none}
button.enviar{padding:14px 20px;border-radius:12px;background:#a855f7;color:white;border:0;cursor:pointer;font-weight:bold}
</style></head>
<body>
<div class="side">
<h2>CHEFE 👑</h2><p class="on">● LIGADA</p>
<h3>Time 3</h3>
<button class="btn ativo" id="b-Chefe" onclick="trocar('Chefe')">👑 Chefe - Principal</button>
<button class="btn" id="b-Fazedor" onclick="trocar('Fazedor')">🔨 Fazedor</button>
<button class="btn" id="b-Revisor" onclick="trocar('Revisor')">🔍 Revisor</button>
<hr>
<button class="btn" onclick="cmd('abre o spotify')">🎵 Spotify</button>
<button class="btn" onclick="cmd('abre o whatsapp')">💬 WhatsApp</button>
<button class="btn" onclick="cmd('abre o youtube')">▶️ YouTube</button>
<button class="btn" onclick="cmd('abre o instagram')">📸 Instagram</button>
<button class="btn" onclick="cmd('cria pasta teste')">📁 Criar pasta teste</button>
</div>
<div class="main">
<h2 id="titulo">Chefe - Principal 👑</h2>
<div id="chat"><div class="msg chefe"><b>Chefe:</b> Tchê! Agora eu to bonita de novo! Pede: cria pasta teste, cria app calculadora, abre o spotify...</div></div>
<div class="box"><input id="in" placeholder="Fala com a Chefe..."><button class="enviar" onclick="enviar()">Enviar ➤</button></div>
</div>
<script>
let quem='Chefe';
function trocar(n){quem=n;document.getElementById('titulo').innerText=n+' 👑';document.querySelectorAll('.side .btn').forEach(b=>b.classList.remove('ativo'));document.getElementById('b-'+n).classList.add('ativo');add('Sistema:','Agora tu ta falando com '+n)}
function add(q,t,cls){let d=document.getElementById('chat');let div=document.createElement('div');div.className='msg '+cls;div.innerHTML='<b>'+q+'</b> '+t;d.appendChild(div);d.scrollTop=99999}
async function cmd(t){add('Tu:',t,'eu');try{let r=await fetch('http://127.0.0.1:5000/falar',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({texto:t})});let j=await r.json();add(quem+':',j.resposta,'chefe')}catch(e){add(quem+':','Deixa o iniciar.bat aberto!','chefe')}}
async function enviar(){let i=document.getElementById('in');let t=i.value;if(!t) return;i.value='';await cmd(t)}
document.getElementById('in').addEventListener('keydown',e=>{if(e.key==='Enter') enviar()});
</script>
</body></html>'''
(base / "time3-final.html").write_text(html, encoding="utf-8")
print("VISUAL NOVO PRONTO!")
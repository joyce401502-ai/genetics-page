from pathlib import Path

HTML = """<!doctype html>
<html lang="zh-Hant">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>遺傳</title>
  <style>
    body{margin:0;font-family:'Microsoft JhengHei',system-ui,sans-serif;color:#14213d;background:linear-gradient(180deg,#eef8fb,#fbfdff 45%,#f7faf5)}
    .shell{width:min(1080px,calc(100% - 32px));margin:auto}.hero{min-height:70vh;display:grid;grid-template-columns:1fr 1fr;gap:24px;align-items:center}.hero h1{font-size:clamp(4rem,12vw,8rem);margin:0}.hero p,.muted{color:#5f6f89;line-height:1.8}.panel,.card{background:white;border:1px solid #d9e2ef;border-radius:8px;padding:18px;box-shadow:0 14px 34px #14213d14}.visual{min-height:360px;display:grid;place-items:center}.cell{width:min(75vw,340px);aspect-ratio:1;border-radius:50%;background:#e6f6f2;border:2px solid #2f9e735c;display:grid;place-items:center}.nucleus{width:58%;aspect-ratio:1;border-radius:50%;background:white;border:2px solid #168aad61;display:grid;place-items:center}.chromosome{width:24px;height:120px;border-radius:999px;background:#d1495b;box-shadow:28px 0 #6d5bd0;transform:rotate(32deg)}section{padding:34px 0}.grid{display:grid;grid-template-columns:repeat(4,1fr);gap:14px}.lab{display:grid;grid-template-columns:1fr 1fr;gap:16px}.punnett{display:grid;grid-template-columns:52px repeat(2,1fr);grid-template-rows:42px repeat(2,82px);gap:8px}.sq{border:1px solid #d9e2ef;border-radius:8px;display:grid;place-items:center;background:white;font-weight:800}.head{background:#edf7f5;color:#168aad}.bar{height:38px;background:#eef3f8;border-radius:8px;overflow:hidden;position:relative;margin:8px 0}.bar span{display:block;height:100%;width:var(--w);background:linear-gradient(90deg,#2f9e73,#168aad)}.bar b{position:absolute;inset:0;display:flex;align-items:center;justify-content:space-between;padding:0 10px}.choice{display:block;width:100%;margin:8px 0;padding:12px;border:1px solid #d9e2ef;border-radius:8px;background:white;text-align:left}.ok{background:#2f9e731f}.no{background:#d1495b1a}@media(max-width:760px){.hero,.lab{grid-template-columns:1fr}.grid{grid-template-columns:1fr 1fr}}@media(max-width:520px){.grid{grid-template-columns:1fr}}
  </style>
</head>
<body>
  <header class="shell hero"><div><h1>遺傳</h1><p>用互動模型理解細胞、染色體、基因、等位基因、性狀，以及親代如何把遺傳訊息傳給子代。</p></div><div class="panel visual"><div class="cell"><div class="nucleus"><div class="chromosome"></div></div></div><p class="muted">基因在染色體上；孩子會從父母各得到一份等位基因。</p></div></header>
  <main class="shell"><section><h2>關係地圖</h2><div class="grid" id="map"></div></section><section><h2>孟德爾配對實驗室</h2><div class="lab"><div class="panel"><label>親代一 <select id="a"><option>AA</option><option selected>Aa</option><option>aa</option></select></label><br><br><label>親代二 <select id="b"><option>AA</option><option selected>Aa</option><option>aa</option></select></label><p class="muted" id="story"></p><div id="bars"></div></div><div class="panel"><div class="punnett" id="punnett"></div></div></div></section><section><h2>快速檢查</h2><div class="panel" id="quiz"></div></section></main>
<script>
const ideas=[['細胞','遺傳物質主要在細胞核裡。'],['染色體','染色體像整理好的遺傳說明書。'],['基因','基因是一段會影響性狀的訊息。'],['等位基因','同一基因的不同版本，例如 A 和 a。']];
map.innerHTML=ideas.map(x=>`<div class="card"><h3>${x[0]}</h3><p class="muted">${x[1]}</p></div>`).join('');
const A=document.querySelector('#a'),B=document.querySelector('#b');function norm(x){return x.split('').sort((m,n)=>m===n?0:m==='A'?-1:1).join('')}function ph(x){return x.includes('A')?'顯性':'隱性'}function draw(){let ga=A.value.split(''),gb=B.value.split(''),r=[norm(ga[0]+gb[0]),norm(ga[1]+gb[0]),norm(ga[0]+gb[1]),norm(ga[1]+gb[1])],c={AA:0,Aa:0,aa:0};r.forEach(x=>c[x]++);punnett.innerHTML=`<div></div><div class="sq head">${gb[0]}</div><div class="sq head">${gb[1]}</div><div class="sq head">${ga[0]}</div><div class="sq">${r[0]}</div><div class="sq">${r[2]}</div><div class="sq head">${ga[1]}</div><div class="sq">${r[1]}</div><div class="sq">${r[3]}</div>`;bars.innerHTML=Object.entries(c).map(([k,v])=>`<div class="bar" style="--w:${v*25}%"><span></span><b>${k}<em>${v}/4</em></b></div>`).join('');story.textContent=`只要有 A 就表現顯性；只有 aa 會表現隱性。這次顯性 ${r.filter(x=>ph(x)==='顯性').length}/4，隱性 ${r.filter(x=>ph(x)==='隱性').length}/4。`}A.onchange=B.onchange=draw;draw();
const qs=[['Aa 為何表現顯性？','A 會蓋過 a 的表現'],['孩子通常從父母各拿到幾個等位基因？','各一個'],['隱性性狀何時出現？','通常 aa 時出現']];quiz.innerHTML=qs.map((q,i)=>`<h3>${i+1}. ${q[0]}</h3><button class="choice" onclick="this.classList.add('ok')">${q[1]}</button><button class="choice" onclick="this.classList.add('no')">另一個版本消失了</button>`).join('');
</script>
</body>
</html>
"""


def main() -> None:
    Path("index.html").write_text(HTML, encoding="utf-8")
    print("已產生 index.html")


if __name__ == "__main__":
    main()

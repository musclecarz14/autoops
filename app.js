let tools=[], category='All';
const grid=document.querySelector('#grid'), search=document.querySelector('#search'), bar=document.querySelector('#categoryBar');
fetch('data/tools.json').then(r=>r.json()).then(d=>{tools=d; renderCategories(); render();}).catch(()=>{grid.innerHTML='<p>Directory data is temporarily unavailable.</p>'});
function renderCategories(){
 const cats=['All',...new Set(tools.map(x=>x.category))];
 bar.innerHTML=cats.map(c=>`<button class="chip ${c===category?'active':''}" data-c="${esc(c)}">${esc(c)}</button>`).join('');
 bar.querySelectorAll('.chip').forEach(b=>b.onclick=()=>{category=b.dataset.c;renderCategories();render()});
}
function render(){
 const q=search.value.trim().toLowerCase();
 const list=tools.filter(t=>(category==='All'||t.category===category)&&(!q||[t.name,t.category,t.description,...(t.tags||[])].join(' ').toLowerCase().includes(q)));
 grid.innerHTML=list.map(t=>`<article class="card"><div class="tag">${esc(t.category)} · ${esc(t.pricing)}</div><h3>${esc(t.name)}</h3><p>${esc(t.description)}</p><a class="cta" href="${esc(t.url)}" rel="sponsored noopener" target="_blank">Visit ${esc(t.name)} →</a></article>`).join('');
 document.querySelector('#empty').hidden=list.length!==0;
}
search.addEventListener('input',render);
document.querySelector('#year').textContent=new Date().getFullYear();
function esc(s){return String(s).replace(/[&<>"']/g,m=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[m]))}

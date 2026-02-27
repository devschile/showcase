document.addEventListener('DOMContentLoaded',function(){
  const modal=document.getElementById('project-modal');
  const titleEl=document.getElementById('modal-title');
  const metaEl=document.getElementById('modal-meta');
  const bodyEl=document.getElementById('modal-body');
  const closeBtn=document.getElementById('modal-close');

  function openModal(data){
    titleEl.textContent = data.title || '';
    metaEl.innerHTML = '';
    if(data.author) metaEl.innerHTML += `<strong>Autor:</strong> ${data.author} `;
    if(data.repo) metaEl.innerHTML += ` <a href="${data.repo}" target="_blank">Repositorio</a>`;
    if(data.tech) metaEl.innerHTML += `<div class="meta"><strong>Tecnologías:</strong> ${data.tech}</div>`;
    bodyEl.innerHTML = data.html || '';
    modal.setAttribute('aria-hidden','false');
    document.body.style.overflow='hidden';
  }

  function closeModal(){
    modal.setAttribute('aria-hidden','true');
    document.body.style.overflow='';
    titleEl.textContent='';metaEl.innerHTML='';bodyEl.innerHTML='';
  }

  closeBtn.addEventListener('click',closeModal);
  modal.addEventListener('click',function(e){ if(e.target===modal) closeModal(); });

  document.querySelectorAll('.project-card').forEach(card=>{
    card.addEventListener('click',function(){
      const data={
        title: card.dataset.title,
        author: card.dataset.author,
        repo: card.dataset.repo,
        tech: card.dataset.tech,
        html: card.querySelector('.project-full')?.innerHTML || ''
      };
      openModal(data);
    });
  });
});

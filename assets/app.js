/* Carregador de continguts editables amb Pages CMS. */
(async function(){
  try {
    const response=await fetch('content/site.json',{cache:'no-cache'});
    if(!response.ok)throw new Error('No es poden carregar els continguts');
    window.NEXWEB_CONTENT=await response.json();
  } catch(error) {
    window.NEXWEB_CONTENT=null; // Visualització local file:// amb textos originals
  }
  const script=document.createElement('script');
  script.src='assets/app-base.js';
  document.body.appendChild(script);
})();

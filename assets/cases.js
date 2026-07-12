const obs = new IntersectionObserver(entries => {
  entries.forEach(e => { if (e.isIntersecting) { e.target.classList.add('in'); obs.unobserve(e.target); } });
}, { threshold: .1 });
document.querySelectorAll('.reveal').forEach(el => obs.observe(el));

// GA4: clique no CTA de WhatsApp
document.querySelectorAll('a[href*="wa.me"]').forEach(el => {
  el.addEventListener('click', () => {
    if (typeof gtag === 'function') {
      gtag('event', 'generate_lead', { method: 'whatsapp', lead_source: document.title });
    }
  });
});

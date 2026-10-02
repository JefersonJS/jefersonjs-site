# -*- coding: utf-8 -*-
"""Gera a seção /conteudos/ a partir de conteudos/_fonte/*.md.

Cada fonte tem um cabeçalho (titulo, data, agenda, serie, rotulo, pilar, resumo, imagens, linkedin). data = publicação
no site; agenda = data do post no LinkedIn (opcional, só ordena) e o texto em
markdown simples. Só entra no ar o que tem data menor ou igual a hoje (horário de Salvador). O GitHub Actions
roda este script todo dia de manhã (.github/workflows/conteudos.yml).

    python scripts/build_conteudos.py            # publica o que já chegou na data
    python scripts/build_conteudos.py --todos    # gera tudo, inclusive o agendado (só para conferir local)
"""
import datetime as dt
import html
import json
import math
import re
import shutil
import sys
from pathlib import Path
from urllib.parse import quote
try:
    from zoneinfo import ZoneInfo
    TZ = ZoneInfo("America/Bahia")
except Exception:  # Windows sem tzdata
    TZ = dt.timezone(dt.timedelta(hours=-3))

RAIZ = Path(__file__).resolve().parent.parent
FONTE = RAIZ / "conteudos" / "_fonte"
IMG = RAIZ / "conteudos" / "_img"
SAIDA = RAIZ / "conteudos"
URL = "https://jefersonjs.com.br"
MESES = ["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]

GTM_HEAD = """<!-- Google Tag Manager -->
<script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
})(window,document,'script','dataLayer','GTM-TFCRZ5J8');</script>
<!-- End Google Tag Manager -->"""
GTM_BODY = """<!-- Google Tag Manager (noscript) -->
<noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-TFCRZ5J8"
height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
<!-- End Google Tag Manager (noscript) -->"""
FAVICON = """<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E%3Crect width='64' height='64' rx='14' fill='%232b4a70'/%3E%3Ctext x='32' y='42' font-family='Arial,sans-serif' font-size='28' font-weight='800' fill='%234676dc' text-anchor='middle'%3EJ%3C/text%3E%3C/svg%3E">"""


def nav(raiz):
    return f"""<nav>
  <a href="{raiz}" class="logo">JJS<em>.</em></a>
  <ul class="nav-r">
    <li><a href="{raiz}#cases">Cases</a></li>
    <li><a href="{raiz}conteudos/">Conteúdos</a></li>
    <li><a href="{raiz}materiais/">Materiais</a></li>
    <li><a href="{raiz}#pilares">Serviços</a></li>
    <li><a href="{raiz}#sobre">Sobre</a></li>
    <li><a href="{raiz}#contato" class="nav-cta">Falar com Jeferson</a></li>
  </ul>
</nav>"""


def footer(raiz):
    return f"""<footer>
  <div class="foot-logo">JJS<em>.</em></div>
  <p>&copy; 2026 Jeferson J Silva &middot; <a href="{raiz}">jefersonjs.com.br</a></p>
</footer>"""


def head(titulo, descricao, url, imagem=None, tipo="website", extra=""):
    og_img = f'<meta property="og:image" content="{imagem}">\n<meta name="twitter:image" content="{imagem}">' if imagem else ""
    return f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
{GTM_HEAD}
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{esc(titulo if len(titulo) > 42 else titulo + " · Jeferson J Silva")}</title>
<meta name="description" content="{esc(descricao)}">
<meta name="robots" content="index, follow">
<link rel="canonical" href="{url}">
<meta name="theme-color" content="#4676dc">
{FAVICON}
<meta property="og:type" content="{tipo}">
<meta property="og:locale" content="pt_BR">
<meta property="og:url" content="{url}">
<meta property="og:site_name" content="Jeferson J Silva">
<meta property="og:title" content="{esc(titulo)}">
<meta property="og:description" content="{esc(descricao)}">
{og_img}
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{esc(titulo)}">
<meta name="twitter:description" content="{esc(descricao)}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{{raiz}}assets/cases.css">
<link rel="stylesheet" href="{{raiz}}assets/conteudos.css">
{extra}
</head>
<body>
{GTM_BODY}
"""


def esc(s):
    return html.escape(s, quote=True)


def inline(s):
    s = esc(s)
    s = re.sub(r"\[((?:[^\[\]]|\[[^\]]*\])*)\]\(([^)\s]+)\)",
               lambda m: f'<a href="{m.group(2)}"{" target=\"_blank\" rel=\"noopener\"" if m.group(2).startswith("http") and "jefersonjs.com.br" not in m.group(2) else ""}>{m.group(1)}</a>', s)
    s = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", s)
    s = re.sub(r"(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])", r"<em>\1</em>", s)
    s = re.sub(r"`(.+?)`", r"<code>\1</code>", s)
    return s


def markdown(md):
    out = []
    for bloco in re.split(r"\n\s*\n", md.strip()):
        linhas = bloco.strip().split("\n")
        if linhas[0].startswith("## "):
            out.append(f"<h2>{inline(linhas[0][3:])}</h2>")
            linhas = linhas[1:]
            if not linhas:
                continue
        if all(l.startswith("- ") for l in linhas):
            out.append("<ul>" + "".join(f"<li>{inline(l[2:])}</li>" for l in linhas) + "</ul>")
        elif all(re.match(r"\d+\. ", l) for l in linhas):
            out.append("<ol>" + "".join(f"<li>{inline(re.sub(r'^\d+\. ', '', l))}</li>" for l in linhas) + "</ol>")
        else:
            out.append(f"<p>{inline(' '.join(linhas))}</p>")
    return "\n".join(out)


def ler(fonte):
    txt = fonte.read_text(encoding="utf-8")
    _, cab, corpo = txt.split("---", 2)
    meta = {}
    for linha in cab.strip().splitlines():
        k, _, v = linha.partition(":")
        meta[k.strip()] = v.strip()
    meta["data"] = dt.date.fromisoformat(meta["data"])
    meta["agenda"] = dt.date.fromisoformat(meta["agenda"]) if meta.get("agenda") else meta["data"]
    meta["imagens"] = [i.strip() for i in meta.get("imagens", "").split(",") if i.strip()]
    meta["slug"] = re.sub(r"^\d{4}-\d{2}-\d{2}-", "", fonte.stem)
    meta["corpo"] = corpo.strip()
    palavras = len(re.findall(r"\w+", corpo))
    meta["leitura"] = max(1, math.ceil(palavras / 200))
    return meta


def data_br(d):
    return f"{d.day} de {MESES[d.month - 1]} de {d.year}"


def card(c, raiz):
    return f"""<a class="ct-card" data-serie="{esc(c['serie'])}" href="{raiz}conteudos/{c['slug']}/">
  <img src="{raiz}conteudos/{c['slug']}/capa.png" alt="Imagem do conteúdo: {esc(c['titulo'])}" loading="lazy" width="1080" height="1350">
  <div class="in-c">
    <div class="related-eyebrow">{esc(c['serie'])} · {esc(c['pilar'])}</div>
    <div class="related-t">{esc(c['titulo'])}</div>
    <div class="related-d">{esc(c['resumo'])}</div>
    <div class="ct-meta">{data_br(c['data'])} · {c['leitura']} min</div>
  </div>
</a>"""


def pagina(c, todos):
    raiz = "../../"
    url = f"{URL}/conteudos/{c['slug']}/"
    img_abs = f"{url}capa.png"
    ld = {
        "@context": "https://schema.org", "@type": "BlogPosting", "headline": c["titulo"], "description": c["resumo"],
        "url": url, "image": img_abs, "datePublished": c["data"].isoformat(), "inLanguage": "pt-BR",
        "author": {"@type": "Person", "name": "Jeferson J Silva", "url": f"{URL}/"},
        "publisher": {"@type": "Person", "name": "Jeferson J Silva"}, "articleSection": c["serie"],
    }
    bc = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Início", "item": f"{URL}/"},
        {"@type": "ListItem", "position": 2, "name": "Conteúdos", "item": f"{URL}/conteudos/"},
        {"@type": "ListItem", "position": 3, "name": c["titulo"], "item": url}]}
    extra = (f'<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>\n'
             f'<script type="application/ld+json">{json.dumps(bc, ensure_ascii=False)}</script>')
    imgs = c["imagens"]
    if len(imgs) > 1:
        alts = [a.strip() for a in c.get("alts", "").split("|")] if c.get("alts") else []
        galeria = "".join(f'<img src="{i + 1:02d}.png" alt="{esc(alts[i]) if i < len(alts) else f"Slide {i + 1} de {len(imgs)}"}" loading="lazy" width="1080" height="1350">' for i in range(len(imgs)))
        visual = f'<div class="ct-galeria">{galeria}</div>'
    else:
        visual = f'<img class="ct-capa" src="capa.png" alt="{esc(c["titulo"])}" width="1080" height="1350">'
    outros = [o for o in todos if o["slug"] != c["slug"]]
    outros.sort(key=lambda o: (o["serie"] != c["serie"], abs((o["agenda"] - c["agenda"]).days)))
    leia = "".join(card(o, raiz) for o in outros[:3])
    linkedin = f'<a class="btn-sec" href="{c["linkedin"]}" target="_blank" rel="noopener">Ver a conversa no LinkedIn →</a>' if c.get("linkedin") else ""
    wa = "https://wa.me/5571982210402?text=" + quote(f"Olá Jeferson, li o conteúdo \"{c['titulo']}\" e quero meu diagnóstico grátis.")
    return head(c["titulo"], c["resumo"], url, img_abs, "article", extra).replace("{raiz}", raiz) + f"""
{nav(raiz)}

<section class="case-hero">
  <div class="container ct-hero">
    <div class="crumb">
      <a href="{raiz}">Início</a><span>/</span>
      <a href="{raiz}conteudos/">Conteúdos</a><span>/</span>
      <span class="current">{esc(c['titulo'])}</span>
    </div>
    <div class="case-eyebrow reveal"><span class="dot"></span>{esc(c['serie'])} · {esc(c['pilar'])}</div>
    <h1 class="case-title reveal">{esc(c['titulo'])}</h1>
    <p class="case-dek reveal">{esc(c['resumo'])}</p>
    <div class="case-meta reveal"><span>{data_br(c['data'])}</span><span>{c['leitura']} min de leitura</span><span>{esc(c['rotulo'])}</span></div>
  </div>
</section>

<section>
  <div class="container ct-artigo">
    <div class="ct-visual reveal">{visual}</div>
    <div class="case-body ct-texto">
{markdown(c['corpo'])}
      <div class="ct-acoes">{linkedin}</div>
    </div>
  </div>
</section>

<section>
  <div class="container">
    <div class="case-cta reveal">
      <h2>Quer que eu olhe isso na sua conta?</h2>
      <p>30 minutos, de graça. Entro nas suas plataformas e mostro os três problemas mais críticos de mensuração.</p>
      <a href="{wa}" target="_blank" rel="noopener" class="btn-pri">Quero meu diagnóstico grátis →</a>
    </div>
  </div>
</section>

{f'''<section class="related">
  <div class="container">
    <span class="slabel reveal">Conteúdos</span>
    <h2 class="stitle reveal" style="margin-bottom:1.5rem">Continue lendo</h2>
    <div class="ct-grid reveal">{leia}</div>
  </div>
</section>''' if leia else ''}

{footer(raiz)}
<script src="{raiz}assets/cases.js"></script>
</body>
</html>
"""


def indice(publicados):
    raiz = "../"
    series = sorted({c["serie"] for c in publicados})
    chips = ('<div class="ct-filtros reveal"><button class="ct-chip" aria-pressed="true" data-f="">Todos</button>'
             + "".join(f'<button class="ct-chip" aria-pressed="false" data-f="{esc(s)}">{esc(s)}</button>' for s in series)
             + "</div>") if len(series) > 1 else ""
    if publicados:
        lista = f'<div class="ct-grid reveal" id="lista">{"".join(card(c, raiz) for c in publicados)}</div>'
    else:
        lista = """<div class="ct-vazio reveal"><b>O primeiro conteúdo sai em 5 de outubro.</b><br>
Enquanto isso, veja os <a href="../#cases">cases</a> e os <a href="../materiais/">materiais gratuitos</a>.</div>"""
    filtro_js = """<script>
document.querySelectorAll('.ct-chip').forEach(function(b){b.addEventListener('click',function(){
  document.querySelectorAll('.ct-chip').forEach(function(x){x.setAttribute('aria-pressed','false')});b.setAttribute('aria-pressed','true');
  var f=b.dataset.f;document.querySelectorAll('#lista .ct-card').forEach(function(c){c.style.display=!f||c.dataset.serie===f?'':'none'});
});});
</script>"""
    return head("Conteúdos sobre analytics, atribuição e IA", "Análises, frameworks e bastidores sobre mensuração, atribuição, fraude, modelos preditivos e IA aplicada a dados de marketing.",
                f"{URL}/conteudos/").replace("{raiz}", raiz) + f"""
{nav(raiz)}

<section class="case-hero">
  <div class="container">
    <div class="crumb"><a href="{raiz}">Início</a><span>/</span><span class="current">Conteúdos</span></div>
    <div class="case-eyebrow reveal"><span class="dot"></span>Conteúdos</div>
    <h1 class="case-title reveal">Análises, frameworks e bastidores de analytics</h1>
    <p class="case-dek reveal">Mensuração, atribuição, fraude, modelos preditivos e IA aplicada a dado de marketing. O que eu publico no LinkedIn, com as referências completas.</p>
    {chips}
    {lista}
  </div>
</section>

{footer(raiz)}
<script src="{raiz}assets/cases.js"></script>
{filtro_js}
</body>
</html>
"""


def entre_marcadores(texto, ini, fim, novo, antes_de):
    bloco = f"{ini}\n{novo}\n{fim}"
    if ini in texto:
        return re.sub(re.escape(ini) + r".*?" + re.escape(fim), lambda _: bloco, texto, flags=re.S)
    return texto.replace(antes_de, bloco + "\n" + antes_de) if antes_de else texto.rstrip() + "\n\n" + bloco + "\n"


def main():
    todos = "--todos" in sys.argv
    hoje = dt.datetime.now(TZ).date()
    fontes = [ler(f) for f in sorted(FONTE.glob("*.md"))]
    publicados = [c for c in fontes if todos or c["data"] <= hoje]
    # mais recentes primeiro; no mesmo dia, segue a ordem da agenda do LinkedIn
    publicados.sort(key=lambda c: (-c["data"].toordinal(), c["agenda"]))
    slugs = {c["slug"] for c in publicados}

    # remove páginas que saíram do ar (data adiada ou fonte apagada)
    for d in SAIDA.iterdir():
        if d.is_dir() and not d.name.startswith("_") and d.name not in slugs:
            shutil.rmtree(d)

    for c in publicados:
        d = SAIDA / c["slug"]
        d.mkdir(exist_ok=True)
        (d / "index.html").write_text(pagina(c, publicados), encoding="utf-8")
        shutil.copy(IMG / c["imagens"][0], d / "capa.png")
        if len(c["imagens"]) > 1:
            for i, im in enumerate(c["imagens"]):
                shutil.copy(IMG / im, d / f"{i + 1:02d}.png")
    (SAIDA / "index.html").write_text(indice(publicados), encoding="utf-8")

    urls = [f"  <url>\n    <loc>{URL}/conteudos/</loc>\n    <changefreq>weekly</changefreq>\n    <priority>0.8</priority>\n  </url>"]
    urls += [f"  <url>\n    <loc>{URL}/conteudos/{c['slug']}/</loc>\n    <lastmod>{c['data'].isoformat()}</lastmod>\n    <priority>0.7</priority>\n  </url>" for c in publicados]
    sm = RAIZ / "sitemap.xml"
    sm.write_text(entre_marcadores(sm.read_text(encoding="utf-8"), "  <!-- conteudos:inicio -->", "  <!-- conteudos:fim -->", "\n".join(urls), "</urlset>"), encoding="utf-8")

    llms = RAIZ / "llms.txt"
    linhas = "\n".join(f"- {c['titulo']}: {c['resumo']} {URL}/conteudos/{c['slug']}/" for c in publicados) or "- (em breve)"
    llms.write_text(entre_marcadores(llms.read_text(encoding="utf-8"), "<!-- conteudos:inicio -->", "<!-- conteudos:fim -->", f"## Conteúdos\n\n{linhas}", None), encoding="utf-8")

    print(f"{len(publicados)} de {len(fontes)} conteúdos no ar (hoje {hoje.isoformat()}{', modo --todos' if todos else ''})")


if __name__ == "__main__":
    main()

"""Build the static methodology page. No scripts, forms or remote assets."""
from pathlib import Path
import markdown

ROOT=Path(__file__).resolve().parent.parent

def build_page():
    body=markdown.markdown((ROOT/'docs/metodologia.md').read_text(encoding='utf-8'),extensions=['tables'])
    css='''
*{box-sizing:border-box}html{scroll-behavior:smooth}body{margin:0;background:#eef2f4;color:#243746;font:18px/1.65 system-ui,Segoe UI,sans-serif}main{max-width:1020px;margin:40px auto;padding:48px 64px;background:white;border-top:8px solid #147d92}h1{font-size:clamp(2rem,5vw,3rem);line-height:1.12;letter-spacing:-.035em;color:#173b58;margin:0 0 24px}h2{margin-top:42px;font-size:1.45rem;line-height:1.25;color:#173b58}a{color:#11667b;text-underline-offset:3px;overflow-wrap:anywhere}li{margin-bottom:10px}a[href$=".xlsx"]{display:inline-block;background:#173b58;color:white;padding:14px 22px;border-radius:5px;font-weight:700;text-decoration:none}a:focus-visible{outline:3px solid #a74416;outline-offset:5px}strong{color:#173b58}a[href$=".xlsx"]:hover{background:#11667b}footer{border-top:1px solid #d4dee3;margin-top:40px;padding-top:20px;font-size:15px}@media(max-width:650px){body{font-size:17px}main{margin:0;padding:28px 22px}}@media print{body{background:white;font-size:11pt}main{margin:0;padding:0;max-width:none}h2{break-after:avoid}a[href$=".xlsx"]{background:none;color:#173b58;padding:0}}
'''
    page='<!doctype html>\n<html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="description" content="Planilha de Rodrigo Immaginario para mapear usos de IA, preservar dúvidas e organizar próximos passos. Sem pontuação de maturidade."><title>Mapa inicial de usos de IA — Rodrigo Immaginario</title><link rel="icon" href="favicon.svg" type="image/svg+xml"><style>'+css+'</style></head><body><main>'+body+'<footer>Rodrigo Immaginario · Modelo v1.0 · Preenchimento interno, sem envio de respostas.</footer></main></body></html>\n'
    (ROOT/'docs/index.html').write_text(page,encoding='utf-8')

if __name__=='__main__':build_page()

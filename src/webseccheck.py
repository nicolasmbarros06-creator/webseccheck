#!/usr/bin/env python3
"""WebSecCheck - análise educacional de cabeçalhos de segurança HTTP.

Escopo intencionalmente limitado a laboratório local:
somente URLs com hostname localhost, 127.0.0.1 ou ::1 são aceitas.
"""

from __future__ import annotations
import argparse
import sys
from urllib.error import HTTPError, URLError
from urllib.parse import urlparse
from urllib.request import Request, urlopen

REQUIRED_HEADERS = {
    "content-security-policy": "CSP ajuda a reduzir riscos de execução de conteúdo não autorizado.",
    "x-content-type-options": "Evita interpretação de conteúdo com MIME incorreto.",
    "x-frame-options": "Ajuda a reduzir riscos de clickjacking em navegadores compatíveis.",
    "referrer-policy": "Controla quanto da URL de origem é enviada como Referer.",
}

OPTIONAL_HEADERS = {
    "strict-transport-security": "HSTS orienta o navegador a usar HTTPS.",
    "permissions-policy": "Restringe recursos e APIs do navegador.",
}

def validate_target(url: str) -> None:
    parsed = urlparse(url)
    if parsed.scheme not in {"http", "https"}:
        raise ValueError("Use uma URL HTTP/HTTPS.")
    if parsed.hostname not in {"localhost", "127.0.0.1", "::1"}:
        raise ValueError(
            "Por segurança, o WebSecCheck aceita somente localhost/127.0.0.1/::1."
        )

def fetch_headers(url: str, timeout: int = 5) -> dict[str, str]:
    validate_target(url)
    request = Request(url, method="GET", headers={"User-Agent": "WebSecCheck-Lab/1.0"})
    try:
        with urlopen(request, timeout=timeout) as response:
            return {k.lower(): v for k, v in response.headers.items()}
    except HTTPError as exc:
        return {k.lower(): v for k, v in exc.headers.items()}
    except URLError as exc:
        raise ConnectionError(f"Não foi possível acessar o laboratório: {exc.reason}") from exc

def analyze(headers: dict[str, str]) -> tuple[list[str], list[str]]:
    missing = [h for h in REQUIRED_HEADERS if h not in headers]
    present = [h for h in REQUIRED_HEADERS if h in headers]
    return present, missing

def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Verifica cabeçalhos de segurança em um alvo local.")
    parser.add_argument("url", help="Ex.: http://127.0.0.1:8000")
    args = parser.parse_args(argv)

    try:
        headers = fetch_headers(args.url)
        present, missing = analyze(headers)
    except (ValueError, ConnectionError) as exc:
        print(f"ERRO: {exc}")
        return 2

    print(f"Alvo: {args.url}")
    print("\nCabeçalhos recomendados:")
    for h in REQUIRED_HEADERS:
        status = "OK" if h in headers else "AUSENTE"
        print(f"- {h}: {status}")

    print("\nCabeçalhos opcionais:")
    for h in OPTIONAL_HEADERS:
        status = "OK" if h in headers else "AUSENTE"
        print(f"- {h}: {status}")

    print(f"\nResumo: {len(present)} presentes; {len(missing)} ausentes.")
    return 0

if __name__ == "__main__":
    sys.exit(main())

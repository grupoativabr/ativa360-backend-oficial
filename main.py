from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {
        "sistema": "ATIVA360 Backend Oficial",
        "status": "online"
    }

@app.get("/health")
def health():
    return {
        "status": "online",
        "sistema": "ATIVA360 Backend Oficial"
    }

@app.get("/version")
def version():
    return {
        "version": "1.0.0"
    }

from pydantic import BaseModel
from datetime import datetime
import base64
from cryptography.hazmat.primitives.serialization import pkcs12


class CertificadoRequest(BaseModel):
    arquivo_pfx_base64: str
    senha: str


@app.post("/validar-certificado")
def validar_certificado(dados: CertificadoRequest):
    try:
        pfx_bytes = base64.b64decode(dados.arquivo_pfx_base64)

        private_key, certificate, additional_certificates = pkcs12.load_key_and_certificates(
            pfx_bytes,
            dados.senha.encode()
        )

        subject = certificate.subject.rfc4514_string()
        issuer = certificate.issuer.rfc4514_string()
        validade = certificate.not_valid_after_utc.strftime("%Y-%m-%d")

        return {
            "status": "valido",
            "titular": subject,
            "emissor": issuer,
            "validade": validade,
            "mensagem": "Certificado A1 lido com sucesso"
        }

    except Exception as e:
        return {
            "status": "erro",
            "mensagem": "Não foi possível ler o certificado. Verifique o arquivo .pfx e a senha.",
            "erro": str(e)
        }

@app.post("/consultar/esocial")
def consultar_esocial():
    return {
        "status": "aguardando_implementacao",
        "portal": "eSocial",
        "mensagem": "Conector eSocial ainda será implementado"
    }

@app.post("/consultar/reinf")
def consultar_reinf():
    return {
        "status": "aguardando_implementacao",
        "portal": "EFD-Reinf",
        "mensagem": "Conector EFD-Reinf ainda será implementado"
    }

@app.post("/consultar/dief-ma")
def consultar_dief_ma():
    return {
        "status": "aguardando_implementacao",
        "portal": "SEFAZ-MA / DIEF-MA",
        "obrigacao": "DIEF-MA",
        "mensagem": "Conector DIEF-MA será implementado para consultar envio/recibo no ambiente da SEFAZ-MA"
    }

@app.post("/importar/historico-receita")
def importar_historico_receita():
    return {
        "status": "aguardando_implementacao",
        "mensagem": "Endpoint criado para importar declarações já transmitidas na Receita Federal, Simples Nacional e e-CAC"
    }

@app.post("/importar/pgdas")
def importar_pgdas():
    return {"status":"aguardando_implementacao"}

@app.post("/importar/defis")
def importar_defis():
    return {"status":"aguardando_implementacao"}

@app.post("/importar/dief-ma")
def importar_dief_ma():
    return {"status":"aguardando_implementacao"}

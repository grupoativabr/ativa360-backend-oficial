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

@app.post("/validar-certificado")
def validar_certificado():
    return {
        "status": "ok",
        "mensagem": "Endpoint de validação de certificado criado com sucesso"
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

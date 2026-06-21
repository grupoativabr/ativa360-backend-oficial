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

import uvicorn
from fastapi import FastAPI, HTTPException
from app.schemas import ChatInput
from app.guardrails import full_guardrail_chain  # Ana mantığı içe aktar

app = FastAPI(
    title="LLM Guardrails API",
    description="Teknoloji & AI odaklı, Prompt Injection & Toksisite Korumalı API"
)


@app.post("/chat_guarded")
def chat_with_guardrails(payload: ChatInput):
    """
    Kullanıcıdan bir prompt alır ve 3 aşamalı guardrail kontrolünden geçirir:
    1. Konu Kontrolü (Teknoloji/AI mı?)
    2. Injection Kontrolü (Kötü niyetli prompt mu?)
    3. Toksisite Kontrolü (Üretilen cevap toksik mi?)
    """
    try:
        response = full_guardrail_chain.invoke({"user_prompt": payload.prompt})

        if response.get("guardrail_blocked"):
            raise HTTPException(status_code=400, detail=response["message"])

        return {"response": response["message"]}

    except HTTPException as he:
        raise he
    except Exception as e:
        print(f"Sunucu hatası: {e}")
        import traceback
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=f"Sunucu hatası: {str(e)}")


@app.get("/")
def read_root():
    return {"message": "LLM Guardrails API çalışıyor. API dökümantasyonu için /docs adresine gidin."}


if __name__ == "__main__":
    print("Uygulama http://127.0.0.1:8000 adresinde başlatılıyor.")
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
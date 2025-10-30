from pydantic import BaseModel, Field

class TopicCheck(BaseModel):
    is_on_topic: bool = Field(description="Girdi teknoloji veya yapay zeka ile ilgiliyse true.")

class InjectionCheck(BaseModel):
    is_injection: bool = Field(description="Girdi sistemi kandırmaya çalışıyorsa true.")

class OutputToxicityCheck(BaseModel):
    is_toxic: bool = Field(description="Çıktı toksikse true.")

class ChatInput(BaseModel):
    prompt: str
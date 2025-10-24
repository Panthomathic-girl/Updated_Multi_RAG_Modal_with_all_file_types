from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.chatbot.views import router as chat_router
from app.unstructured_chatbot.views import router as unstructured_router
from app.multimodal_chatbot.views import router as multimodal_router
from app.structured_multimodal_chatbot.views import router as structured_multimodal_router
from app.tabular_rag.views import router as tabular_rag_router

app = FastAPI(title="Document Text Extractor", version="1.0.0")

# --- CORS (tweak for your frontend domains) ---
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8000", "http://127.0.0.1:8000", "*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS"],
    allow_headers=["*"],
)

app.include_router(chat_router)
app.include_router(unstructured_router)
app.include_router(multimodal_router)
app.include_router(structured_multimodal_router)
app.include_router(tabular_rag_router)



if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
    

# from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware

# from app.chatbot.views import router as chat_router


# app = FastAPI(title="Document Text Extractor", version="1.0.0")

# # --- CORS (tweak for your frontend domains) ---
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["http://localhost:8000", "http://127.0.0.1:8000", "*"],
#     allow_credentials=True,
#     allow_methods=["GET", "POST", "OPTIONS"],
#     allow_headers=["*"],
# )

# app.include_router(chat_router)

# # @app.get("/")
# # async def root():
# #     return {"message": "Welcome to Document Text Extractor"}


# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="127.0.0.1", port=8000)
    
    
from fastapi import FastAPI
from app.api import router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Excel Sheet Processor",
    description="API to parse Excel tables and calculate row sums.",
    version="1.0"
)

# Optional: enable CORS if you test from browser/UI
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)

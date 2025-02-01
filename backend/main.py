from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# uvicorn main:app --reload

app = FastAPI()

# CORS setup
app.add_middleware(
	CORSMiddleware,
	allow_origins=["https://benjack.co.uk", "http://localhost:3000"],
	allow_credentials=True,
	allow_methods=["*"],
	allow_headers=["*"],
)

@app.get("/")
def read_root():
	return None

if __name__ == "__main__":
	import uvicorn
	uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)

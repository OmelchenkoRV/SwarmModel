from fastapi import FastAPI
from app.models.request import SimulationRequest
from app.services.simulation import run_simulation

app = FastAPI(docs_url="/docs", redoc_url="/redoc")


@app.post("/simulate")
def simulate(request: SimulationRequest):
    result = run_simulation(request.transition_matrix, request.steps)
    return {"success": True, "result": result}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)

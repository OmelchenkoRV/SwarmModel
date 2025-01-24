from fastapi import FastAPI
from app.models.request import SimulationRequest
from app.services.simulation import run_simulation
import logging
import azure.functions as func

app = FastAPI()

logging.basicConfig(level=logging.INFO)

@app.post("/simulate")
def simulate(request: SimulationRequest):
    logging.info("Simulation request received")
    result = run_simulation(request.transition_matrix, request.steps)
    logging.info(f"Simulation completed. Result: {result}")
    return {"success": True, "result": result}

# Removed the main function completely


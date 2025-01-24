from fastapi import FastAPI
from app.models.request import SimulationRequest
from app.services.simulation import run_simulation
import azure.functions as func
import logging

app = FastAPI()

logging.basicConfig(level=logging.INFO)


@app.post("/simulate")
def simulate(request: SimulationRequest):
    logging.info("Simulation request received")
    result = run_simulation(request.transition_matrix, request.steps)
    logging.info(f"Simulation completed. Result: {result}")
    return {"success": True, "result": result}


def main(req: func.HttpRequest) -> func.HttpResponse:
    body = req.get_json()
    simulation_request = SimulationRequest(**body)
    result = run_simulation(simulation_request.transition_matrix, simulation_request.steps)

    return func.HttpResponse(body=result, mimetype="application/json")

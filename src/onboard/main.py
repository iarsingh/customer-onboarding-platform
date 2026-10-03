from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Customer onboarding")
GATES = ("sso", "backup", "network_policy", "audit")


class Onboarding(BaseModel):
    customer: str
    gates: dict


@app.post("/onboarding")
def review(body: Onboarding):
    missing = [gate for gate in GATES if body.gates.get(gate) is not True]
    status = "ready_for_human" if not missing else "blocked"
    return {"customer": body.customer, "status": status, "missing": missing, "live": False}

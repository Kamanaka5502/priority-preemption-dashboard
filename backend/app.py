from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Literal

app = FastAPI(
    title="Priority & Preemption Gate",
    description="Hard gate enforcing verified WPS before dashboard rendering",
    version="0.1.0"
)

class Priority(BaseModel):
    wps_provisioned: bool
    preemption_enabled: bool
    verification_state: Literal[
        "NOT_PROVISIONED",
        "PROVISIONED_NOT_VERIFIED",
        "VERIFIED_ACTIVE"
    ]

class Observation(BaseModel):
    priority: Priority

@app.post("/observe")
def observe(obs: Observation):
    state = obs.priority.verification_state

    if state != "VERIFIED_ACTIVE":
        raise HTTPException(
            status_code=403,
            detail="Priority & Preemption not verified. Rendering is gated."
        )

    return {
        "status": "UNLOCKED",
        "message": "Priority verified. Dashboard rendering permitted."
    }

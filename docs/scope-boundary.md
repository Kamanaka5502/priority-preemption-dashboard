# Scope Boundary

This project is an external observation and decision-support dashboard intended
to assist with reasoning about public safety communications during carrier
outages or degradation.

## What This System Does
- Accepts explicitly provided inputs
- Displays operational readiness states
- Enforces verification gates
- Supports disciplined incident reasoning

## What This System Does Not Do
- Control carrier infrastructure
- Authenticate users or devices
- Access internal carrier systems or APIs
- Perform live network probing or scanning
- Infer causes, intent, or attribution

## Priority & Preemption Verification
All Priority & Preemption (WPS) states must be explicitly confirmed by an operator
or trusted verification process.

No automated inference is permitted.

## Authority
This system claims no operational authority.
It exists solely to surface verified states and prevent false confidence.

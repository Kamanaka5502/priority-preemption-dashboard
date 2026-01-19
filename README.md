Reference implementation for the Elyria Governance Layer: Mitigating LLM Coherence Collapse through hard-gated accountability logic.

# Priority & Preemption Control Dashboard

## Purpose
This project provides a deployable, external control-plane dashboard designed to support
real-time public safety communications during carrier outages or degradation.

The dashboard enforces a strict operational rule:
**Priority & Preemption (WPS) must be explicitly verified before any secondary metrics are displayed.**

If priority communications are not confirmed working, the system refuses to present
performance or infrastructure data that could create false confidence.

---

## What This Is
- A decision-support dashboard for emergency and public safety connectivity
- A control-plane visibility layer, not a network probe
- A tool designed to run locally or internally by operations teams
- A framework that enforces disciplined incident reasoning under stress

---

## What This Is Not
- Not a carrier control system
- Not an automated network scanner
- Not an attribution or root-cause engine
- Not a consumer diagnostics tool

This project **does not infer causes** and **does not access internal carrier systems**.

---

## Operational Priority Order (Hard-Gated)

The dashboard enforces the following order. Sections do not render out of order.

1. Priority & Preemption (WPS) — **Must be VERIFIED**
2. Safety & Coordination (SWIC / EOC)
3. Backhaul Survivability
4. Deployables (COW / COLT / THOR / SPOT / OXEN)
5. Interoperability (LMR ↔ Cellular)
6. Secondary Metrics (optional)

---

## Core Principle

> If first responders cannot communicate, nothing else matters.

---

## Deployment Model
- Git-first
- Local or internal deployment
- Docker-based
- JSON-driven inputs
- No secrets in code

---

## Status
Initial scaffold. Core gating logic and schema under active development.

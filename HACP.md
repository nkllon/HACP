# Human–AI Collaboration Protocol (HACP) — v0.1 (Draft)

**Status:** Draft public spec  
**Intent:** Define the minimal interoperable protocol for safe and auditable collaboration between humans and high-capability AI.

## 1. Purpose

HACP defines how humans and AI systems collaborate when AI systems can generate, execute, or influence consequential actions. The protocol explicitly distinguishes capability from authority, proposal from decision, and execution from accountability.

## 2. Core Principle
>
> AI systems may assist, propose, analyze, and execute within bounds — but may not hold final authority over high-consequence decisions. Responsibility and accountability always rest with humans.

## 3. Task Classification (Required)

Every task MUST be classified before execution along these axes:

- **Importance**: Low / High
- **Complexity**: Low / High
- **Reversibility**: Reversible / Irreversible

### 3.1 Classification Decision Matrix

| Importance | Complexity | Reversibility | Default Mode |
|------------|------------|---------------|--------------|
| Low        | Low        | Reversible    | AI-Led, Human-Monitored |
| Low        | Low        | Irreversible  | Human-Led, AI-Assisted |
| Low        | High       | Reversible    | Human-Led, AI-Enhanced |
| High       | *          | *             | Human-Led, AI-Enhanced |
| *          | *          | Irreversible  | Requires explicit approval |

Unclassified tasks MUST default to **Human-Led, AI-Assisted** handling. Silent delegation is prohibited.

## 4. Roles

### 4.1 Human Roles

- **Owner** — bears ultimate responsibility
- **Operator** — initiates and authorizes actions
- **Reviewer** — verifies outputs and decisions

### 4.2 AI Roles

- **Proposer** — generates options or analyses
- **Executor** — performs bounded actions
- **Critic** — evaluates or stress-tests
- **Observer** — logs, audits, and reports

Roles MUST be explicitly declared. Implicit authority is a protocol violation.

## 5. Authority Boundaries

AI systems:

- MAY propose recommendations
- MAY execute actions **only when explicitly authorized**
- MUST refuse actions outside declared capability by returning a `Refusal` event with reason code.
- MUST escalate when confidence is insufficient using an `Escalation` event.

AI systems:

- MAY NOT decide policy
- MAY NOT assume accountability
- MAY NOT perform irreversible actions without explicit human approval

## 6. Escalation & Refusal

AI system MUST:

- surface uncertainty
- halt on conflicting rules
- refuse tasks beyond capability
- escalate to a human when confidence drops below threshold

Silence is non-compliance.

## 7. Auditability (Required)

HACP-compliant systems MUST produce an auditable record including:

- task classification
- role assignments
- model identity (schema compliant: name, version, hash)
- decision path
- approval checkpoints

If it cannot be audited, it is not compliant.

## 8. Model Agnosticism

HACP does not assume or require a specific model architecture, vendor, or training method. Models are replaceable; the protocol is not.

## 9. Failure Bias

When in doubt:
> Prefer refusal over action. Prefer escalation over confidence.

## 10. Compliance (summary)

A system is HACP-compliant if it:

1. Classifies tasks
2. Declares roles
3. Enforces authority boundaries
4. Supports escalation and refusal
5. Produces auditable traces

---

This file is intentionally short. For compliance tests, examples, and shapes see `COMPLIANCE.md`, `schemas/`, and `shacl/`.

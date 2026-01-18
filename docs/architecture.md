# HACP Architecture

HACP uses a **Schema-First, Validation-Driven** architecture to ensure interoperability and safety in Human-AI collaboration.

## Components

### 1. Normative Schemas (`schemas/*.yaml`)

These YAML files define the **structure** of the data objects exchanged in the protocol. They are the data contract.

- `task-manifest.yaml`: Describes the work to be done.
- `audit-record.yaml`: The immutable log of what happened.
- `approval-record.yaml`: Proof of human authorization.

### 2. Validation Shapes (`shacl/*.ttl`)

These SHACL (Shapes Constraint Language) files define the **logic and constraints** of the protocol. They enforce the rules in `COMPLIANCE.md`.

- **Introspection**: "Are all required fields present?"
- **Logic**: "If confidence < threshold, is there an escalation?"
- **Safety**: "If irreversible, is there a human approval?"

### 3. Protocol Specification (`HACP.md`)

The human-readable normative text that governs the behavior of agents and humans.

## Validation Flow

1. **Input**: A Task Manifest or Event Stream (YAML/JSON).
2. **Translation**: Converted to RDF (Turtle/JSON-LD).
3. **Validation**: `pyshacl` validates the RDF against `hacp-core.ttl`.
4. **Result**: Pass/Fail with detailed violation report.

## Directory Structure

```
HACP/
├── schemas/       # JSON Schemas (YAML) for data structure
├── shacl/         # SHACL Shapes (Turtle) for logic validation
├── examples/      # YAML examples for humans
│   └── rdf/       # Corresponding RDF tests for machines
└── scripts/       # Validation tooling
```

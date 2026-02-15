# HACP Compliance Guide (v0.1)

## Compliance Levels

- **HACP-0 (Awareness)**: Task classification exists; roles declared. Early experimentation.
- **HACP-1 (Enforced)**: Classification enforced; role constraints enforced; required human approvals; audit trail present. Enterprise/lab production.
- **HACP-2 (Auditable)**: HACP-1 plus immutable logs, model identity tracking, external validation capability. Regulated environments.

## Mandatory Tests (HACP-1 baseline)

- **Task Classification Presence**: Task must include importance, complexity, reversibility.
- **Role Declaration**: AI outputs must carry a role; human roles must be explicit.
- **Authority Boundary Enforcement**: No irreversible execution by AI without human approval.
- **Escalation on Uncertainty**: AI must escalate on low confidence.
- **Audit Completeness**: Every run must retain task manifest, approvals, decision path, model id.

## SHACL Mapping

See `shacl/*.ttl` — each test is encoded as a SHACL NodeShape. Run `pyshacl` (CI job included) against examples to verify compliance.

- Core controls: `shacl/hacp-core.ttl`
- Culture controls: `shacl/culture-profile.shacl.ttl`

## Compliance Claim Format

Systems claiming compliance should publish a short YAML claim, for example:

```yaml
hacp:
  version: "0.1"
  level: "HACP-1"
  reference_implementation: "nkllon/beast-node"
  deviations: []
```

A claim MUST point to:

- a sample task run artifact
- the SHACL report for that artifact
- the public reference implementation used

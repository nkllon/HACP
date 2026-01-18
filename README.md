# Human–AI Collaboration Protocol (HACP)

**HACP** (v0.1) is a minimal, vendor-neutral protocol and reference implementation for safe, auditable, and productive collaboration between humans and high-capability AI systems.

This repository contains:

- the normative spec (`HACP.md`)
- schemas and SHACL shapes for compliance testing
- a canonical reference mapping to the "Beast" implementation
- examples and a pilot plan for non-classified lab testing

Goal: make the protocol real and executable so that institutions and vendors can interoperate — without surrendering human authority.

## Quick start

1. Read the normative spec: `HACP.md`
2. Inspect the schema: `schemas/task-manifest.yaml`
3. Validate an example with SHACL (CI job included): See `.github/workflows/validate-shacl.yml`

## License

Apache 2.0 — see LICENSE

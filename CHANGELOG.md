# Changelog

All notable changes to this project will be documented in this file.

## [Unreleased]

### Added

- **Schemas**: `audit-record`, `approval-record`, `model-identity`.
- **SHACL**: Validation logic for Escalation, Audit Completeness, and Model Identity.
- **Documentation**: `docs/architecture.md`, Decision Matrix in `HACP.md`.
- **Examples**: Irreversible tasks, Escalation scenarios, Validation failures.
- **CI/CD**: `validate_rdf.py` script and GitHub Workflow.
- **Culture**: Added `schemas/culture-profile.yaml` and `shacl/culture-profile.shacl.ttl`.
- **Culture Example**: Added `examples/culture_profile.yaml` and `examples/rdf/culture_profile.ttl`.

### Changed

- Refined `task-manifest.yaml` with collaboration modes and deadlines.
- Clarified refusal and model identity requirements in `HACP.md`.
- Added optional `team_id` and `culture_profile_ref` to `schemas/task-manifest.yaml`.
- Added `Culture Policy Binding` requirement in `HACP.md`.
- Updated core SHACL authority-boundary logic to conditionally require `humanApproval` for irreversible executions.
- Updated CI validation to run positive and negative fixture suites separately.

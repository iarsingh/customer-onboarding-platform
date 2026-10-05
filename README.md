# Customer onboarding and deployment platform

<!-- project-guide:start -->
## Project guide

[Project architecture](PROJECT_ARCHITECTURE.md) · [Interview questions and answers](INTERVIEW_QA.md)

Use the architecture document for the component diagram, implementation boundaries, and verification entry points. The interview guide includes source-backed answers and project walkthroughs.

### Implementation map

| Component | Responsibility |
| --- | --- |
| [`src/onboard/main.py`](src/onboard/main.py) | HTTP handlers: `POST /onboarding` |
| [`requirements.txt`](requirements.txt) | Implementation or supporting configuration |
| [`tests/test_onboard.py`](tests/test_onboard.py) | Executable checks and regression examples |
| [`.github/workflows/ci.yml`](.github/workflows/ci.yml) | GitHub Actions job definitions |
| [`README.md`](README.md) | Project explanations or operating notes |

### Local setup and verification

From the repository root (the commands follow the checked-in manifests):

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m pytest -q
```

To serve the FastAPI application locally, install the server separately if it is not already available:

```bash
python -m pip install uvicorn
PYTHONPATH=src python -m uvicorn onboard.main:app --reload
```

<!-- project-guide:end -->

Level: Advanced+

Skills: Full-stack gate, cloud checklist, security

Four gates have to be true before a customer can leave this API: SSO, backup, network policy, and audit. A missing gate returns `blocked` and the name of what is missing.

Even when every gate is true, `live` stays false and the status is `ready_for_human`. This API does not turn a tenant on.

```bash
pip install -r requirements.txt
pytest -q
```

## Ops plane

Workspaces, tenant isolation, job approval, and audit live under `/v1`. Production apply is refused. See `docs/ARCHITECTURE.md`.

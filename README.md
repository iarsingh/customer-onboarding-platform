# Customer onboarding and deployment platform

Level: Advanced+

Skills: Full-stack gate, cloud checklist, security

Four gates have to be true before a customer can leave this API: SSO, backup, network policy, and audit. A missing gate returns `blocked` and the name of what is missing.

Even when every gate is true, `live` stays false and the status is `ready_for_human`. This API does not turn a tenant on.

```bash
pip install -r requirements.txt
pytest -q
```


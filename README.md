# Social Media Agent

[![CI](https://github.com/kogunlowo123/social-media-agent/actions/workflows/ci.yml/badge.svg)](https://github.com/kogunlowo123/social-media-agent/actions/workflows/ci.yml)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

> **Category**: Marketing | **Cloud**: MULTI-CLOUD | **LLM**: gpt-4o

Social media management agent that creates platform-specific posts, schedules publishing, analyzes engagement metrics, monitors brand mentions, and manages community interactions.

---

## Domain-Specific Tools

| Tool | Description |
|------|-------------|
| `create_post` | Create a platform-optimized social media post |
| `schedule_post` | Schedule post for optimal engagement time |
| `analyze_engagement` | Analyze post and profile engagement metrics |
| `monitor_mentions` | Monitor brand mentions and sentiment across social platforms |
| `respond_to_comments` | Generate response to social media comments or messages |

## API Endpoints

| Method | Path | Description |
|--------|------|-------------|
| `POST` | `/api/v1/social-media/create` | Create or generate |
| `POST` | `/api/v1/social-media/analyze` | Analyze performance |
| `POST` | `/api/v1/social-media/optimize` | Optimize |
| `POST` | `/api/v1/social-media/schedule` | Schedule |
| `POST` | `/api/v1/social-media/report` | Generate report |

## Features

- Social
- Media
- Analytics
- Optimization

## Integrations

- Hubspot Marketing
- Marketo
- Mailchimp
- Google Analytics
- Meta Ads

## Architecture

```
social-media-agent/
├── src/
│   ├── agent/              # Domain-specific agent logic
│   │   ├── social_media_agent_agent.py  # Main agent with domain tools
│   │   ├── tools.py        # 5 domain-specific tools
│   │   └── prompts.py      # Expert system prompts
│   ├── api/                # FastAPI routes
│   │   └── routes/
│   │       ├── domain.py   # 5 domain-specific endpoints
│   │       └── health.py   # Health check
│   ├── connectors/         # 5 integration connectors
│   ├── config/             # Settings and configuration
│   ├── models/             # Domain-specific Pydantic schemas
│   ├── rag/                # RAG pipeline
│   ├── mcp/                # MCP server
│   └── a2a/                # Agent-to-agent protocol
├── tests/
├── infrastructure/         # Terraform, K8s, Helm, Docker
├── dashboard/              # Next.js frontend
└── docs/                   # Architecture and deployment docs
```

## Quick Start

```bash
# Install
pip install -e ".[dev]"

# Run
make dev

# Test
make test

# Docker
docker compose up -d
```

## Primary Service

**Marketing Platform + LLM + Analytics**

---

Built as part of the Enterprise AI Agent Platform.

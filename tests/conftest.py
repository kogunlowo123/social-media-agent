"""Test configuration for Social Media Agent."""

import pytest


@pytest.fixture
def agent_config():
    return {"name": "social-media-agent", "category": "Marketing"}

"""Social Media Agent - Unit Tests."""

import pytest
from src.agent.tools import AgentTools


@pytest.mark.asyncio
async def test_create_post():
    """Test Create a platform-optimized social media post."""
    tools = AgentTools()
    result = await tools.create_post(platform="test", content="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_schedule_post():
    """Test Schedule post for optimal engagement time."""
    tools = AgentTools()
    result = await tools.schedule_post(post_id="test", platform="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_analyze_engagement():
    """Test Analyze post and profile engagement metrics."""
    tools = AgentTools()
    result = await tools.analyze_engagement(platform="test", period="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_monitor_mentions():
    """Test Monitor brand mentions and sentiment across social platforms."""
    tools = AgentTools()
    result = await tools.monitor_mentions(brand_name="test", platforms="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_agent_initialization():
    """Test that the agent initializes correctly."""
    from src.agent.social_media_agent_agent import SocialMediaAgentAgent
    agent = SocialMediaAgentAgent()
    assert agent.agent_id is not None
    assert agent._system_prompt is not None
    assert len(agent._tool_dispatch) > 0

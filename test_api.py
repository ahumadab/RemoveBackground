import pytest
from httpx import AsyncClient

from main import app


@pytest.mark.asyncio
async def test_remove_background():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        with open('image.jpg', 'rb') as img:
            response = await ac.post("/remove-bg", files={"file": img})
        assert response.status_code == 200
        assert response.headers['content-type'] == 'image/png'

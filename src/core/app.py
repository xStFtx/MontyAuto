import click
from modules.ai_processing import AIDocumentProcessor
from modules.trading import CryptoTrader
from modules.automation import HomeAutomationHub
from fastapi import FastAPI, Depends
from contextlib import asynccontextmanager
import aioredis
from src.infrastructure.database.session import AsyncSessionLocal

class AutomationEnterprise:
    def __init__(self):
        self.ai_processor = AIDocumentProcessor()
        self.trader = CryptoTrader()
        self.home_hub = HomeAutomationHub()
    
    def run_service(self, service_name, **kwargs):
        service_map = {
            'ai-process': self.ai_processor.process_documents,
            'trade': self.trader.execute_strategy,
            'home-automation': self.home_hub.start_server
        }
        return service_map[service_name](**kwargs)

@click.group()
def cli():
    pass

@cli.command()
@click.option('--service', required=True, help='Service to run')
def start(service):
    app = AutomationEnterprise()
    app.run_service(service)

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    app.state.redis = await aioredis.from_url("redis://localhost")
    yield
    # Shutdown
    await app.state.redis.close()

app = FastAPI(lifespan=lifespan)

async def get_db():
    async with AsyncSessionLocal() as session:
        yield session

@app.get("/health")
async def health_check(db=Depends(get_db)):
    await db.execute("SELECT 1")
    return {"status": "ok"}

if __name__ == "__main__":
    cli() 
import click
from modules.ai_processing import AIDocumentProcessor
from modules.trading import CryptoTrader
from modules.automation import HomeAutomationHub

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

if __name__ == "__main__":
    cli() 
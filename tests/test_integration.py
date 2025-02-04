import pytest
from src.core.app import AutomationEnterprise
from unittest.mock import Mock

@pytest.fixture
def mock_trader():
    trader = Mock()
    trader.execute_strategy.return_value = {"status": "success"}
    return trader

def test_trading_execution(mock_trader):
    app = AutomationEnterprise()
    app.trader = mock_trader
    result = app.run_service('trade', symbol="BTCUSDT")
    assert result['status'] == "success"
    mock_trader.execute_strategy.assert_called_once_with(symbol="BTCUSDT") 
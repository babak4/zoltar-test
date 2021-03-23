from alerts import checks, whatsapp
from unittest.mock import MagicMock

def test_check_and_send_calls():
    # how do you assert if alerts.whatsapp.send_alert is called
    # when the followong line is executed?
    whatsapp.send_alert = MagicMock()
    checks.check_and_send(120)

    assert whatsapp.send_alert.call_count == 1


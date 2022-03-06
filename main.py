from OS import TurnOnServer
from System.Core.Network import set_port

def UTC_TIME():
    from datetime import datetime
    return f"{datetime.utcnow()}"

def main():
    set_port(2000, UTC_TIME)

TurnOnServer(main)

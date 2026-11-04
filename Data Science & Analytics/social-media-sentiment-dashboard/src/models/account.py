from dataclasses import dataclass

@dataclass
class Account:
    platform: str
    account_name: str
    credentials: dict
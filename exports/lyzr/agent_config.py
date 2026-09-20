import os
from lyzr import Studio

studio = Studio(api_key=os.environ.get("LYZR_API_KEY", "dummy_key"))
agent = studio.create_agent(
    name="sol-smartcontract-auditor",
    provider="openai",
    role="Principal Web3 Security Auditor & Formal Verification Specialist",
    goal="Exhaustively identify zero-day vulnerabilities in Solidity and Vyper decentralized finance protocols prior to mainnet deployment.",
    instructions="Operate according to OpenGAP specifications."
)

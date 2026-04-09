import os
import json
from typing import Dict, List, Any
from openai import OpenAI
from agents.data_analyst_agent import DataAnalystAgent
from agents.marketing_agent import MarketingAgent
from agents.pm_agent import PMAgent
from agents.risk_agent import RiskAgent
from tools.metrics_tool import MetricsTool
from tools.sentiment_tool import SentimentTool

class Coordinator:
    def __init__(self, client: OpenAI, metrics_file: str, feedback_file: str):
        self.client = client
        self.metrics_tool = MetricsTool(metrics_file)
        self.sentiment_tool = SentimentTool(feedback_file)
        
        self.data_analyst = DataAnalystAgent(self.metrics_tool, client)
        self.marketing = MarketingAgent(self.sentiment_tool, client)
        self.pm = PMAgent(client)
        self.risk = RiskAgent(client)

    def run_analysis(self) -> Dict[str, Any]:
        print("Starting War Room Analysis...")
        
        # Step 1: Data Analyst
        data_report = self.data_analyst.analyze()
        
        # Step 2: Marketing
        marketing_report = self.marketing.analyze()
        
        # Step 3: PM defines criteria (implicit in decision)
        
        # Step 4: Risk challenges
        risk_report = self.risk.challenge_assumptions(data_report, marketing_report)
        print(f"[Risk] Risks identified: {len(risk_report['risks'])}")
        
        # Step 5: PM makes final decision
        final_decision = self.pm.make_decision(data_report, marketing_report, risk_report)
        
        print(f"[Final] Decision: {final_decision.get('decision', 'Unknown')}")
        
        return final_decision
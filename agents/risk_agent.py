import os
import json
from typing import Dict, List, Any
from openai import OpenAI

class RiskAgent:
    def __init__(self, client: OpenAI):
        self.client = client

    def challenge_assumptions(self, data_analyst_report: Dict, marketing_report: Dict) -> Dict[str, Any]:
        print("[Risk] Challenging assumptions and identifying risks...")
        
        # Use LLM to identify risks
        prompt = f"""
        As a Risk Analyst, challenge the assumptions in the following reports and identify potential risks:
        
        Data Analyst Report: {json.dumps(data_analyst_report, indent=2)}
        
        Marketing Report: {json.dumps(marketing_report, indent=2)}
        
        Identify risks, potential biases, and areas of concern. Provide a risk register as a list.
        """
        
        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500
        )
        
        risk_analysis = response.choices[0].message.content.strip()
        
        # Extract risks (simple parsing)
        risks = risk_analysis.split('\n')
        risks = [risk.strip('- ').strip() for risk in risks if risk.strip()]
        
        return {
            'risks': risks,
            'analysis': risk_analysis
        }
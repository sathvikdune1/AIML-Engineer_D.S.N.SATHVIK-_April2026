import os
import json
from typing import Dict, List, Any
from openai import OpenAI

class PMAgent:
    def __init__(self, client: OpenAI):
        self.client = client

    def define_success_criteria(self) -> str:
        """Define success criteria for the product launch."""
        criteria = """
        Success Criteria:
        - DAU increase by at least 5%
        - Retention_D7 above 0.65
        - Crash_Rate below 0.025
        - API_Latency_P95 below 260ms
        - Payment_Success_Rate above 0.97
        - Support_Tickets below 140
        - Positive sentiment above 40%
        - Negative sentiment below 30%
        """
        return criteria

    def make_decision(self, data_analyst_report: Dict, marketing_report: Dict, risk_report: Dict) -> Dict[str, Any]:
        print("[PM] Defining success criteria and making decision...")
        
        criteria = self.define_success_criteria()
        
        # Use LLM to make decision based on reports
        prompt = f"""
        As a Product Manager, review the following reports and make a decision on the product launch:
        
        Success Criteria: {criteria}
        
        Data Analyst Report: {json.dumps(data_analyst_report, indent=2)}
        
        Marketing Report: {json.dumps(marketing_report, indent=2)}
        
        Risk Report: {json.dumps(risk_report, indent=2)}
        
        Decide: Proceed / Pause / Roll Back
        Provide rationale, metrics summary, feedback summary, risk register, action plan, communication plan, and confidence score (0-100).
        Output in JSON format with keys: decision, rationale, metrics_summary, feedback_summary, risk_register, action_plan, communication_plan, confidence_score
        """
        
        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=1000
        )
        
        result_text = response.choices[0].message.content.strip()
        
        # Parse JSON response
        try:
            result = json.loads(result_text)
        except json.JSONDecodeError:
            # Fallback if not valid JSON
            result = {
                "decision": "Pause",
                "rationale": "Unable to parse LLM response",
                "metrics_summary": data_analyst_report.get('summary', ''),
                "feedback_summary": marketing_report.get('summary', ''),
                "risk_register": risk_report.get('risks', []),
                "action_plan": ["Investigate issues", "Fix critical bugs"],
                "communication_plan": {"internal": "Team meeting", "external": "Status update"},
                "confidence_score": 50
            }
        
        return result
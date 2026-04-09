import os
import json
from typing import Dict, List, Any
from openai import OpenAI
from tools.metrics_tool import MetricsTool
from tools.sentiment_tool import SentimentTool

class DataAnalystAgent:
    def __init__(self, metrics_tool: MetricsTool, client: OpenAI):
        self.metrics_tool = metrics_tool
        self.client = client

    def analyze(self) -> Dict[str, Any]:
        print("[Data Analyst] Analyzing metrics...")
        
        trends = self.metrics_tool.calculate_trends()
        anomalies = self.metrics_tool.detect_anomalies()
        
        print(f"[Tool] Trends calculated: {len(trends)} metrics")
        print(f"[Tool] Anomalies detected: {len(anomalies)}")
        
        # Use LLM to summarize analysis
        prompt = f"""
        As a data analyst, summarize the metrics analysis:
        Trends: {json.dumps(trends, indent=2)}
        Anomalies: {anomalies}
        
        Provide a concise summary of key findings.
        """
        
        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=300
        )
        
        summary = response.choices[0].message.content.strip()
        
        return {
            'trends': trends,
            'anomalies': anomalies,
            'summary': summary
        }
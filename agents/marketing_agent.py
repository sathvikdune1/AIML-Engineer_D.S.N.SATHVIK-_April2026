import os
import json
from typing import Dict, List, Any
from openai import OpenAI
from tools.sentiment_tool import SentimentTool

class MarketingAgent:
    def __init__(self, sentiment_tool: SentimentTool, client: OpenAI):
        self.sentiment_tool = sentiment_tool
        self.client = client

    def analyze(self) -> Dict[str, Any]:
        print("[Marketing] Analyzing user sentiment...")
        
        sentiment_analysis = self.sentiment_tool.analyze_sentiment()
        key_issues = self.sentiment_tool.summarize_key_issues()
        
        print(f"[Tool] Sentiment analyzed: {sentiment_analysis['total_feedback']} feedbacks")
        print(f"[Tool] Key issues summarized: {len(key_issues)}")
        
        # Use LLM to summarize sentiment
        prompt = f"""
        As a marketing analyst, summarize user sentiment:
        Analysis: {json.dumps(sentiment_analysis, indent=2)}
        Key Issues: {key_issues}
        
        Provide a concise summary of user feedback.
        """
        
        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=300
        )
        
        summary = response.choices[0].message.content.strip()
        
        return {
            'sentiment_analysis': sentiment_analysis,
            'key_issues': key_issues,
            'summary': summary
        }
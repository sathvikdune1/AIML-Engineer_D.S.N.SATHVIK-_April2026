import json
from typing import Dict, List, Any
from collections import Counter

class SentimentTool:
    def __init__(self, feedback_file: str):
        self.feedback_file = feedback_file
        with open(feedback_file, 'r') as f:
            self.feedback_data = json.load(f)

    def analyze_sentiment(self) -> Dict[str, Any]:
        """Analyze overall sentiment from feedback."""
        sentiments = [item['sentiment'] for item in self.feedback_data]
        sentiment_counts = Counter(sentiments)
        
        total = len(sentiments)
        positive_pct = (sentiment_counts.get('positive', 0) / total) * 100
        negative_pct = (sentiment_counts.get('negative', 0) / total) * 100
        neutral_pct = (sentiment_counts.get('neutral', 0) / total) * 100
        
        avg_rating = sum(item['rating'] for item in self.feedback_data) / total
        
        return {
            'total_feedback': total,
            'positive_percentage': positive_pct,
            'negative_percentage': negative_pct,
            'neutral_percentage': neutral_pct,
            'average_rating': avg_rating,
            'sentiment_distribution': dict(sentiment_counts)
        }

    def summarize_key_issues(self) -> List[str]:
        """Summarize key issues from negative feedback."""
        negative_feedback = [item for item in self.feedback_data if item['sentiment'] == 'negative']
        issues = []
        
        # Simple keyword extraction for common issues
        keywords = ['crash', 'latency', 'payment', 'support', 'freeze', 'bug', 'slow', 'failure']
        issue_counts = Counter()
        
        for feedback in negative_feedback:
            text = feedback['feedback'].lower()
            for keyword in keywords:
                if keyword in text:
                    issue_counts[keyword] += 1
        
        # Get top issues
        top_issues = issue_counts.most_common(5)
        for issue, count in top_issues:
            issues.append(f"{issue.capitalize()}: mentioned in {count} negative feedbacks")
        
        return issues
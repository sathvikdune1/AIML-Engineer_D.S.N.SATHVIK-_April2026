import pandas as pd
import numpy as np
from typing import Dict, List, Any

class MetricsTool:
    def __init__(self, metrics_file: str):
        self.metrics_file = metrics_file
        self.df = pd.read_csv(metrics_file)
        self.df['date'] = pd.to_datetime(self.df['date'])

    def calculate_trends(self) -> Dict[str, Any]:
        """Calculate trends for key metrics over the period."""
        trends = {}
        numeric_cols = ['DAU', 'Retention_D1', 'Retention_D7', 'Crash_Rate', 'API_Latency_P95', 'Payment_Success_Rate', 'Support_Tickets']
        
        for col in numeric_cols:
            start_val = self.df[col].iloc[0]
            end_val = self.df[col].iloc[-1]
            trend = ((end_val - start_val) / start_val) * 100 if start_val != 0 else 0
            trends[col] = {
                'start': start_val,
                'end': end_val,
                'trend_percent': trend,
                'direction': 'increasing' if trend > 0 else 'decreasing' if trend < 0 else 'stable'
            }
        
        return trends

    def detect_anomalies(self) -> List[str]:
        """Detect anomalies in metrics using simple statistical methods."""
        anomalies = []
        numeric_cols = ['DAU', 'Retention_D1', 'Retention_D7', 'Crash_Rate', 'API_Latency_P95', 'Payment_Success_Rate', 'Support_Tickets']
        
        for col in numeric_cols:
            mean_val = self.df[col].mean()
            std_val = self.df[col].std()
            threshold = 2 * std_val  # 2 standard deviations
            
            for idx, val in enumerate(self.df[col]):
                if abs(val - mean_val) > threshold:
                    date = self.df['date'].iloc[idx].strftime('%Y-%m-%d')
                    anomalies.append(f"Anomaly in {col}: {val} on {date} (mean: {mean_val:.2f}, std: {std_val:.2f})")
        
        return anomalies
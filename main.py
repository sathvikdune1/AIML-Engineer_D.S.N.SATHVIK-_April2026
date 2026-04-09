import os
import json
from dotenv import load_dotenv
from openai import OpenAI
from orchestrator.coordinator import Coordinator

def main():
    # Load environment variables
    load_dotenv()
    
    # Get API key
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key:
        raise ValueError("OPENAI_API_KEY not found in environment variables")
    
    client = OpenAI(api_key=api_key)
    
    # File paths
    metrics_file = 'data/metrics.csv'
    feedback_file = 'data/feedback.json'
    output_file = 'output/final_decision.json'
    
    # Initialize coordinator
    coordinator = Coordinator(client, metrics_file, feedback_file)
    
    # Run analysis
    result = coordinator.run_analysis()
    
    # Save output
    with open(output_file, 'w') as f:
        json.dump(result, f, indent=2)
    
    print(f"Analysis complete. Results saved to {output_file}")

if __name__ == "__main__":
    main()
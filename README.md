## Demo
# AI War Room - Multi-Agent Product Launch Decision System

A production-ready Python project that simulates a product launch "war room" decision-making process using multi-agent AI orchestration.

## Overview

This system analyzes product metrics and user feedback to make informed decisions on whether to Proceed, Pause, or Roll Back a product launch. It uses a team of AI agents (Product Manager, Data Analyst, Marketing, and Risk) working together through a coordinated workflow.

## Features

- **Multi-Agent Orchestration**: Custom-built agent system with sequential execution
- **Metrics Analysis**: Automated trend calculation and anomaly detection
- **Sentiment Analysis**: User feedback processing and key issue identification
- **Risk Assessment**: Comprehensive risk identification and challenge of assumptions
- **Structured Decision Making**: Data-driven decisions with clear rationale

## Project Structure

```
ai-war-room/
├── agents/
│   ├── pm_agent.py              # Product Manager Agent
│   ├── data_analyst_agent.py    # Data Analyst Agent
│   ├── marketing_agent.py       # Marketing Agent
│   └── risk_agent.py            # Risk Assessment Agent
├── tools/
│   ├── metrics_tool.py          # Metrics analysis tools
│   └── sentiment_tool.py        # Sentiment analysis tools
├── data/
│   ├── metrics.csv              # Product metrics data
│   ├── feedback.json            # User feedback data
│   └── release_notes.txt        # Release notes
├── orchestrator/
│   └── coordinator.py           # Workflow coordinator
├── output/
│   └── final_decision.json      # Final decision output
├── main.py                      # Main execution script
├── requirements.txt             # Python dependencies
├── .env.example                 # Environment variables template
└── README.md                    # This file
```

## Setup Instructions

1. **Clone or download the project**:
   ```bash
   cd path/to/ai-war-room
   ```

2. **Create a virtual environment** (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**:
   - Copy `.env.example` to `.env`
   - Add your OpenAI API key:
     ```
     OPENAI_API_KEY=your_openai_api_key_here
     ```

5. **Ensure data files are in place**:
   - The project includes mock data files in the `data/` directory
   - `metrics.csv`: 10 days of product metrics
   - `feedback.json`: 40 user feedback entries
   - `release_notes.txt`: Feature rollout details

## How to Run

1. **Activate virtual environment** (if using one):
   ```bash
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. **Run the analysis**:
   ```bash
   python main.py
   ```

The system will:
- Load and analyze metrics data
- Process user feedback
- Run the multi-agent decision process
- Generate a comprehensive decision report
- Save results to `output/final_decision.json`

## Output Format

The final decision is saved as a JSON file with the following structure:

```json
{
  "decision": "Proceed|Pause|Roll Back",
  "rationale": "Detailed reasoning for the decision",
  "metrics_summary": "Summary of key metrics analysis",
  "feedback_summary": "Summary of user sentiment and feedback",
  "risk_register": ["List of identified risks"],
  "action_plan": ["Recommended actions"],
  "communication_plan": {
    "internal": "Internal communication strategy",
    "external": "External communication strategy"
  },
  "confidence_score": 85
}
```

## Agent Roles

- **Data Analyst Agent**: Analyzes metrics, calculates trends, detects anomalies
- **Marketing Agent**: Processes user feedback, summarizes sentiment
- **Product Manager Agent**: Defines success criteria, makes final decision
- **Risk Agent**: Challenges assumptions, identifies potential risks

## Workflow

The system executes agents in sequence:
1. Data Analyst analyzes metrics
2. Marketing analyzes sentiment
3. Risk Agent challenges findings
4. Product Manager synthesizes all input and makes decision

## Logging

The system provides detailed logging throughout the process:
- Agent actions and tool usage
- Key findings and anomalies
- Decision rationale

## Customization

- **Data Sources**: Modify data files in `data/` directory
- **Agent Logic**: Update agent implementations in `agents/` directory
- **Tools**: Extend analysis tools in `tools/` directory
- **Workflow**: Modify orchestration in `orchestrator/coordinator.py`

## Requirements

- Python 3.8+
- OpenAI API key
- Dependencies listed in `requirements.txt`

## Example Output

```
Starting War Room Analysis...
[Data Analyst] Analyzing metrics...
[Tool] Trends calculated: 7 metrics
[Tool] Anomalies detected: 2
[Marketing] Analyzing user sentiment...
[Tool] Sentiment analyzed: 40 feedbacks
[Tool] Key issues summarized: 5
[Risk] Challenging assumptions and identifying risks...
[Risk] Risks identified: 4
[PM] Defining success criteria and making decision...
[Final] Decision: Pause
Analysis complete. Results saved to output/final_decision.json
```

## Troubleshooting

- **API Key Issues**: Ensure `OPENAI_API_KEY` is set in `.env` file
- **Import Errors**: Install all dependencies with `pip install -r requirements.txt`
- **Data Issues**: Verify data files exist and are properly formatted
- **Permission Errors**: Ensure write permissions for `output/` directory


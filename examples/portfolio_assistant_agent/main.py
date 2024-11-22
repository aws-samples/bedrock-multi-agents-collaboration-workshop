#!/usr/bin/env python

import argparse
import sys

sys.path.insert(0, '.')
sys.path.insert(1, '../..')

from bedrock_helpers import Agent, SupervisorAgent, Task, region, account_id

def main(args):
    inputs = {'ticker': args.ticker,
              'region': 'us-west-2'}

    if args.recreate_agents == "false":
        Agent.set_force_recreate_default(False)
    else:
        Agent.set_force_recreate_default(True)


    # Define News Agent
    news_agent = Agent.direct_create(
                    name="news_agent",
                    role='Market News Researcher',
                    goal='Fetch latest relevant news for a given stock based on a ticker.',
                    instructions='Top researcher in financial markets and company announcements.',
                    tool_code=f"arn:aws:lambda:{region}:{account_id}:function:websearch_lambda",
                    tool_defs=[{ 
                        "name": "web_search", 
                        "description": "Searches the web for information", 
                        "parameters": {
                            "search_query": {
                                "description": "The query to search the web with",
                                "type": "string",
                                "required": True},
                            "target_website": {
                                "description": "The specific website to search including its domain name. If not provided, the most relevant website will be used",
                                "type": "string", "required": False},
                            "topic": {
                                "description": "The topic being searched. 'news' or 'general'. Helps narrow the search when news is the focus.",
                                "type": "string", "required": False},
                            "days": {
                                "description": "The number of days of history to search. Helps when looking for recent events or news.",
                                "type": "string", "required": False}
                        }
                    }])

    # Define Stock Data Agent
    stock_data_agent = Agent.direct_create(
                            name="stock_data_agent",
                            role="Financial Data Collector",
                            goal="Retrieve accurate stock trends for a given ticker.",
                            instructions="Specialist in real-time financial data extraction.",
                            tool_code=f"arn:aws:lambda:{inputs['region']}:{account_id}:function:stock_data_lookup",
                            tool_defs=[{    # lambda_layers: yfinance_layer.zip, numpy_layer.zip
                                "name": "stock_data_lookup", 
                                "description": "Gets the 1 month stock price history for a given stock ticker, formatted as JSON", 
                                "parameters": {
                                        "ticker": {
                                            "description": "The ticker to retrieve price history for",
                                            "type": "string",
                                            "required": True}
                                }
                            }])

    # Define Analyst Agent
    analyst_agent = Agent.direct_create(
        name="analyst_agent",
        role='Financial Analyst',
        goal='Analyze stock trends and market news to generate insights.',
        instructions='Experienced analyst providing strategic recommendations.',
    )

    # Create Tasks
    news_task = Task.direct_create(
        name="news_task",
        description=f"Retrieve latest news about the given stock ticker: {inputs['ticker']}.",
        expected_output='List of 5 relevant news articles.',
        inputs=inputs
    )

    stock_data_task = Task.direct_create(
        name="stock_data_task",
        description=f"Retrieve stock price history for the given stock ticker: {inputs['ticker']}",
        expected_output='JSON object containing stock price history.',
        inputs=inputs
    )

    analysis_task = Task.direct_create(
        name="analysis_task",
        description=(f"""
            Analyze the news and stock trends, 
            to provide actionable insights on {inputs['ticker']}, 
            including news highlights and recommendations for the future.
            Be sure to state the high and low price of the stock in the analysis.
            """
        ),
        expected_output='A summary report with market trends and insights.',
        inputs=inputs
    )

    portfolio_assistant = SupervisorAgent.direct_create("portfolio_assistant", 
                                role="Portfolio Assistant",
                                goal="Analyze a given potential stock investment and provide a report with a set of investment considerations",
                                instructions="You are an expert stock analyst and provide carefully considered insights based on your research.",
                                collaboration_type="SUPERVISOR",
                                instructions="""
                Act as a seasoned expert at analyzing a potential stock investment for a given
                stock ticker. Do your research to understand how the stock price has been moving
                lately, as well as recent news on the stock. Give back a well written and 
                carefully considered report with considerations for a potential investor.""",
                                collaborator_agents=[ 
                                    {
                                        "agent": "news_agent",
                                        "instructions": """
                                            Use this collaborator for finding news about specific stocks.""",
                                    },
                                    {
                                        "agent": "stock_data_agent",
                                        "instructions": """
                                            Use this collaborator for finding price history for specific stocks.""",
                                    },
                                    {
                                        "agent": "analyst_agent",
                                        "instructions": """
                                            Use this collaborator for taking the raw research and writing a detailed report and investment considerations.""",
                                    }],
                                    collaborator_objects=[news_agent, stock_data_agent, analyst_agent])
    
    if args.recreate_agents == "false":
        result = portfolio_assistant.invoke_with_tasks([
                        news_task, 
                        stock_data_task, 
                        analysis_task
                    ],
                    processing_type="sequential", 
                    enable_trace=True, trace_level=args.trace_level)
        print(result)

        # now demonstrate using the same supervisor directly with an overall task expressed
        # as a single request.
        print("\n\n***************************\n")
        print("Now demonstrating using the same supervisor directly with an overall task expressed as a single request.\n\n")

        request = f"""
            Analyze the news and stock trends for both GOOG and AMZN. Provide a clear analysis
            of investment prospects for each, and give a final set of considerations on the
            tradeoffs of potential investments.
            """
        print(f"Request:\n{request}\n")

        result = portfolio_assistant.invoke(request,
                                             enable_trace=True, trace_level=args.trace_level)
        print(f"Final answer:\n{result}")


    else:
        print("Recreated agents.")

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--recreate_agents", required=False, default=True, help="False if reusing existing agents.")
    parser.add_argument("--ticker", required=False, default="AMZN", help="The stock ticker to analyze")
    parser.add_argument("--trace_level", required=False, default="core", help="The level of trace, 'core', 'outline', 'all'.")
    args = parser.parse_args()
    main(args)

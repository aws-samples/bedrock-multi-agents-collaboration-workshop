# Amazon Bedrock Multi-Agent Collaboration Examples

This repository is designed to get you started with Bedrock Agents multi-agent collaboration by providing a set of examples that demonstrate how it works and showcases some of its core capabilities. The field of multi-agent systems is still in the early days, and our goal is to give you some off the shelf starter examples that inspire you as you being to tackle real world scenarios.

## Getting started

1. To get started navigate to the example you want to deploy in `src/examples/*` directory.
2. Follow the deployment steps in the `src/examples/*/README.md` file of the example.

## Examples

To get you started working with Bedrock multi-agent processes, we provide the following examples:

- **[Hello World Agent](/src/examples/00_hello_world_agent/README.md)**
- **[DevOps Agent](/src/examples/devops_agent/README.md)**
- **[Energy Efficiency Management Agent](/src/examples/energy_efficiency_management_agent/README.md)**
- **[Portfolio Assistant Agent](/src/examples/portfolio_assistant_agent/README.md)** This supervisor agent has two collaborators, a News agent and a Stock Data agent. Those specialists are orchestrated to perform investment analysis for a given stock ticker based on the latest news and recent stock price movements.
- **[Startup Advisor Agent](/src/examples/startup_advisor_agent/README.md)** Have a new startup in mind, but haven't quite hired your marketing staff? Use this supervisor to do your market research, come up with campaign ideas, and write effective campaign copy. It uses a set of 5 sub-agents to get the job done (Market Analyst, Content Creator, ...).
- **[Sports Team Poet Agent](/src/examples/team_poems_agent/README.md)** This is a fun example for sports fans. The Sports Team Poet is a supervisor with a Research Agent and a Sports Poetry Writer. Pick your favorite team (go Celtics!) and see multi-agents collaborate to conduct web research about your team and make a fun poem with those insights. Have fun!
- **[Trip Planner Agent](/src/examples/trip_planner_agent/README.md)** The Trip Planner uses a few sub-agents to help you build a robust itinerary given a destination and number of days. It leverages a Restaurant Scout and an Activity Finder to get great ideas, and an Intinerary Compiler to finish the job. Try it out for your next trip.
- **[Voyage Vituoso Agent](/src/examples/voyage_virtuoso_agent/README.md)** Dream big with the Voyage Virtuoso, a supervisor agent that is built for high net worth individuals that need help picking the most expensive and elaborate destinations given a theme ("I want to ski on expert slopes, but need ski-on/ski-off resort with great night life").
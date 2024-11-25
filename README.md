# Amazon Bedrock Multi-Agent Collaboration

:wave: :wave: Welcome to the Amazon Bedrock Multi-Agent Collaboration repository. :wave: :wave:

This repository provides examples and best practices for working with [Amazon Bedrock Multi-Agent Collaboration](https://aws.amazon.com/bedrock/agents/). 

🔄 **Actively Maintained**: This repository is regularly updated to include the latest Amazon Bedrock Agent features and functionalities.🔄

Amazon Bedrock multi-agent collaboration enables unfied conversational experiences as well as new ways to deliver complex process automation. Companies now have a modular, secure, and scalable way to leverage a collection of specialized AI agents to adress more complicated scenarios. Development teams can independently build AI agents with deep expertise at a very specific set of outcomes, and these agents can be flexibly assembled into a multi-agent nsystem to execute a set of tasks. Supervisor agents dynamically plan and execute across their available collaborators and knowledge bases, completing complex requests. This addresses the scalability challenges of single-agent systems by allowing greater accuracy without the complexity associated with more complicated coding and prompt engineering. Multi-level agent hierarchies are also supported, and agent processing can be both sequential and parallel. Bedrock agent tracing gives you the transparency needed for auditing and troubleshooting multi-agent flows by giving step by step information about the chain of agent calls, and the inputs and outputs to every sub-agent and tool along the way.

## �� Table of Contents ��

- [Overview](#overview)
- [Prerequisites](#prerequisites)
- [Repository Structure](#repository-structure)
- [Multi-Agent Examples](#multi-agent-examples)
- [Getting Started](#getting-started)
- [Security](#Security)
- [License](#license)

## Overview

Amazon Bedrock Agents enables you to create AI-powered assistants that can perform complex tasks and interact with various APIs and services. 

This repository provides practical examples to help you understand and implement multi-agent solutions.

The solutions presented here use the [boto3 SDK in Python](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent.html), however, you can create Bedrock Agents solutions using any of the AWS SDKs for [C++](https://sdk.amazonaws.com/cpp/api/LATEST/aws-cpp-sdk-bedrock-agent/html/annotated.html), [Go](https://docs.aws.amazon.com/sdk-for-go/api/service/bedrockagent/), [Java](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/services/bedrockagent/package-summary.html), [JavaScript](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/client/bedrock-agent/), [Kotlin](https://sdk.amazonaws.com/kotlin/api/latest/bedrockagent/index.html), [.NET](https://docs.aws.amazon.com/sdkfornet/v3/apidocs/items/BedrockAgent/NBedrockAgent.html), [PHP](https://docs.aws.amazon.com/aws-sdk-php/v3/api/namespace-Aws.BedrockAgent.html), [Ruby](https://docs.aws.amazon.com/sdk-for-ruby/v3/api/Aws/BedrockAgent.html), [Rust](https://docs.rs/aws-sdk-bedrockagent/latest/aws_sdk_bedrockagent/), [SAP ABAP](https://docs.aws.amazon.com/sdk-for-sap-abap/v1/api/latest/bdr/index.html) or [Swift](https://sdk.amazonaws.com/swift/api/awsbedrockruntime/0.34.0/documentation/awsbedrockruntime)

## Prerequisites

- AWS Account with Bedrock access
- Python 3.8 or later
- Required Python packages (specified in [`requirements.txt`](/requirements.txt))

Make sure to run the following commands:

```
git clone https://github.com/aws-samples/bedrock-multi-agents-collaboration-workshop

cd bedrock-multi-agents-collaboration-workshop

python3 -m venv .venv

source .venv/bin/activate

pip3 install -r requirements.txt
```

> [!TIP]   
> Run the `deactivate` command to deactivate the virtual environment.

## Repository Structure

```
├── src/examples
│   ├── devops_agent/
│   ├── energy_efficiency_management_agent/
│   ├── startup_advisor_agent/
|   └── ....
├── src/shared
│   ├── file_store/
│   ├── stock_data/
│   ├── web_search/
|   └── ....
├── src/utils
│   ├── bedrock_agent_helper.py
|   ├── bedrock_agent.py
|   └── ....
```

## Multi-Agent Examples

Shows examples of bedrock multi-agent collaboration including:

- 00_hello_world_agent
- DevOps Agent
- Energy Efficiency Management Agent
- Portfolio Assistant Agent
- Startup Advisor Agent
- Team Poems Agent
- Trip Planner Agent
- Voyage Virtuso Agent

## Getting Started

> [!IMPORTANT]
> Make sure you have completed the [Prerequisites](#prerequisites).

1. To get started navigate to the example you want to deploy in `src/examples/*` directory. 
2. Follow the deployment steps in the `src/examples/*/README.md` file of the example. 

## Best Practices

The code samples highlighted in this repository focus on showcasing different Amazon Bedrock Agents capabilities.

Please check out our two-part blog series for best practices around building generative AI applications with Amazon Bedrock Agents: 

- [Best practices for building robust generative AI applications with Amazon Bedrock Agents – Part 1](https://aws.amazon.com/blogs/machine-learning/best-practices-for-building-robust-generative-ai-applications-with-amazon-bedrock-agents-part-1/)
- [Best practices for building robust generative AI applications with Amazon Bedrock Agents – Part 2](https://aws.amazon.com/blogs/machine-learning/best-practices-for-building-robust-generative-ai-applications-with-amazon-bedrock-agents-part-2/)

## Security

See [CONTRIBUTING](CONTRIBUTING.md#security-issue-notifications) for more information.

## License

This library is licensed under the MIT-0 License. See the LICENSE file.

---

> [!DISCLAIMER]   
> Examples in this repository are for demonstration purposes. 
> Ensure proper security and testing when deploying to production environments.

🔗 **Related Links**:

- [Amazon Bedrock Agents Documentation](https://docs.aws.amazon.com/bedrock/latest/userguide/agents.html)
- [Boto3 Python SDK Documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent.html)
- [Amazon Bedrock Samples](https://github.com/aws-samples/amazon-bedrock-samples/tree/main)
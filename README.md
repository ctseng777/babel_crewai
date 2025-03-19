# Babel Crew

## Installation

Ensure you have Python >=3.10 <3.13 installed on your system. 

Create virtual environment
```
python3 -m venv .venv
source .venv/bin/activate
```

```
pip install crewai
pip install crewai_tools
```

Note that for Mac OS with arm64 architecture, onnxruntime can be problem. Install onnxruntime-silicon instead
```
pip uninstall onnxruntime
pip install onnxruntime-silicon
```
Check architecture
```
python3 -c "import platform; print(platform.machine())" 
```

(Optional) Lock the dependencies and install them by using the CLI command:
```bash
crewai install
```
### Customizing

**Add your `OPENAI_API_KEY` into the `.env` file**


## Running the Project

To kickstart your crew of AI agents and begin task execution, run this from the root folder of your project:

```bash
$ crewai run
```

This command initializes the babel Crew, assembling the agents and assigning them tasks as defined in your configuration.

## Understanding Your Crew

The babel Crew is composed of multiple AI agents, each with unique roles, goals, and tools. These agents collaborate on a series of tasks, defined in `config/tasks.yaml`, leveraging their collective skills to achieve complex objectives. The `config/agents.yaml` file outlines the capabilities and configurations of each agent in your crew.


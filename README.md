# Babel Crew

## Installation (for Mac arm64 Universal architecture)
Refer to the [post](https://community.crewai.com/t/onnxruntime-doesnt-have-a-source-distribution-or-wheel-for-the-current-platform/1495/18)

Use Python 3.11

Create virtual environment
```
python3 -m venv .venv
source .venv/bin/activate
```

Install crewai 0.80.0
```
pip install crewai==0.80.0
pip install socksio # also required to create crew
```

Modify project.toml
```
dependencies = [
    "crewai[tools]>=0.80.0,<1.0.0",
    "onnxruntime==1.15.0",
    "socksio>=1.0.0",
    "pyarrow==17.0.0",
]
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


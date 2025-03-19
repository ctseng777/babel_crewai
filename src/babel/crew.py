import os
from crewai import LLM, Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

# If you want to run a snippet of code before or after the crew starts,
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

# Initialize the SambaNova LLM
sambanova_llm = LLM(
    model="sambanova/Meta-Llama-3.1-8B-Instruct",
    api_key=os.getenv("SAMBANOVA_API_KEY"),
    temperature=0.7
)

@CrewBase
class TweetTranslationCrew():
    """Tweet translation crew"""

    # Learn more about YAML configuration files here:
    # Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
    # Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    # If you would like to add tools to your agents, you can learn more about it here:
    # https://docs.crewai.com/concepts/agents#agent-tools
    @agent
    def recomposition_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['recomposition_agent'],
            verbose=True,
            llm=sambanova_llm
        )

    @agent
    def translation_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['translation_agent'],
            verbose=True,
            llm=sambanova_llm
        )

    @task
    def recomposition_task(self) -> Task:
        return Task(
            config=self.tasks_config['recomposition_task'],
        )

    @task
    def translation_task(self) -> Task:
        return Task(
            config=self.tasks_config['translation_task'],
        )

    @crew
    def crew(self) -> Crew:
        """Creates the TweetTranslation crew."""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )
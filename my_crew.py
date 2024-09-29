import yaml
import os
from datetime import datetime
from crewai import Agent, Crew, Task
from crewai_tools import SerperDevTool, ScrapeWebsiteTool
from pydantic import BaseModel, Field
from typing import List, Optional

class Activity(BaseModel):
    name: str = Field(..., description="The name of the activity")
    description: str = Field(..., description="The description of the activity")
    location: str = Field(..., description="The location of the activity")
    date: str = Field(..., description="The date of the activity")
    cuisine: str = Field(..., description="The cuisine of the activity")
    why_its_suitable: str = Field(..., description="The reason why the activity is suitable for the user")
    rating: int = Field(..., description="The rating of the activity")
    reviews: str = Field(..., description="The reviews of the activity")

class DayPlan(BaseModel):
    date: str = Field(..., description="The date of the day plan")
    activities: List[Activity] = Field(..., description="The activities of the day plan")
    restaurants: List[str] = Field(..., description="The restaurants of the day plan")
    flight: Optional[str] = Field(..., description="The flight information")

class Itinerary(BaseModel):
    days: List[DayPlan] = Field(..., description="The day plan of the trip")
    name: str = Field(..., description="The name of the Itinerary")
    hotel: str = Field(..., description="The hotel of the Itinerary")

class SurpriseTravelCrew:
    """Surprise Travel Crew"""

    def __init__(self):
        try:
            print("Starting SurpriseTravelCrew initialization...")
            self.load_configs()
            self.agents = self.create_agents()
            self.tasks = self.create_tasks()
            self.crew = Crew(
                agents=self.agents,
                tasks=self.tasks,
                verbose=True
            )
            print("SurpriseTravelCrew initialization completed")
        except Exception as e:
            print(f"Error in SurpriseTravelCrew initialization: {str(e)}")
            import traceback
            traceback.print_exc()
            raise

    def load_configs(self):
        agents_config_path = 'config/agents.yaml'
        tasks_config_path = 'config/tasks.yaml'
        
        print(f"Current working directory: {os.getcwd()}")
        print(f"Attempting to open agents config: {agents_config_path}")
        
        if not os.path.exists(agents_config_path):
            raise FileNotFoundError(f"Agents config file not found: {agents_config_path}")
        
        with open(agents_config_path, 'r') as file:
            self.agents_config = yaml.safe_load(file)
        print("Agents config loaded successfully")
        
        print(f"Attempting to open tasks config: {tasks_config_path}")
        
        if not os.path.exists(tasks_config_path):
            raise FileNotFoundError(f"Tasks config file not found: {tasks_config_path}")
        
        with open(tasks_config_path, 'r') as file:
            self.tasks_config = yaml.safe_load(file)
        print("Tasks config loaded successfully")

    def create_agents(self):
        return [
            self.personalized_activity_planner(),
            self.restaurant_scout(),
            self.itinerary_compiler()
        ]

    def create_tasks(self):
        return [
            self.personalized_activity_planner_task(),
            self.restaurant_scouting_task(),
            self.itinerary_compiler_task()
        ]

    def personalized_activity_planner(self) -> Agent:
        return Agent(
            role=self.agents_config['personalized_activity_planner']['role'],
            goal=self.agents_config['personalized_activity_planner']['goal'],
            backstory=self.agents_config['personalized_activity_planner']['backstory'],
            tools=[SerperDevTool(), ScrapeWebsiteTool()],
            verbose=True,
            allow_delegation=False
        )
    
    def restaurant_scout(self) -> Agent:
        return Agent(
            role=self.agents_config['restaurant_scout']['role'],
            goal=self.agents_config['restaurant_scout']['goal'],
            backstory=self.agents_config['restaurant_scout']['backstory'],
            tools=[SerperDevTool(), ScrapeWebsiteTool()],
            verbose=True,
            allow_delegation=False
        )
    
    def itinerary_compiler(self) -> Agent:
        return Agent(
            role=self.agents_config['itinerary_compiler']['role'],
            goal=self.agents_config['itinerary_compiler']['goal'],
            backstory=self.agents_config['itinerary_compiler']['backstory'],
            tools=[SerperDevTool()],
            verbose=True,
            allow_delegation=False
        )
    
    def personalized_activity_planner_task(self) -> Task:
        return Task(
            description=self.tasks_config['personalized_activity_planning_task']['description'],
            expected_output=self.tasks_config['personalized_activity_planning_task']['expected_output'],
            agent=self.personalized_activity_planner()
        )

    def restaurant_scouting_task(self) -> Task:
        return Task(
            description=self.tasks_config['restaurant_scouting_task']['description'],
            expected_output=self.tasks_config['restaurant_scouting_task']['expected_output'],
            agent=self.restaurant_scout()
        )

    def itinerary_compiler_task(self) -> Task:
        return Task(
            description=self.tasks_config['itinerary_compilation_task']['description'],
            expected_output=self.tasks_config['itinerary_compilation_task']['expected_output'],
            agent=self.itinerary_compiler(),
            output_file='itinerary.md'
        )

    def kickoff(self, inputs):
        return self.crew.kickoff(inputs=inputs)

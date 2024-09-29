# CrewAI Surprise Trip Planner
### Author: Tomas Vince
 [Linkedin](https://www.linkedin.com/in/tomasvince/)

The CrewAI Surprise Trip Planner is an AI-powered application that generates personalized travel itineraries based on user preferences. It utilizes the CrewAI framework to create intelligent team of AI agents (researcher, scout, and compiler) that collaborate to plan activities, scout restaurants, and compile a complete itinerary for the user's trip.

## Features

- Personalized activity planning based on user preferences
- Restaurant scouting to find the best dining options
- Itinerary compilation to create a comprehensive travel plan
- Integration with external tools like SerperDevTool and ScrapeWebsiteTool for enhanced information gathering

## Prerequisites

Before running the CrewAI Surprise Trip Planner, ensure that you have the following:

- Python 3.12.6
- pip package manager

## Installation

1. Clone the repository:

   ```
   git clone https://github.com/tomique34/CrewAI_surprise_trip_planner.git
   ```

2. Navigate to the project directory:

   ```
   cd CrewAI_surprise_trip_planner
   ```

3. Create a virtual environment:

   ```
   python -m venv venv
   ```

4. Activate the virtual environment:
   - For Windows:
     ```
     venv\Scripts\activate
     ```
   - For macOS and Linux:
     ```
     source venv/bin/activate
     ```

5. Install the required dependencies:

   ```
   pip install -r requirements.txt
   ```

## Configuration

1. Open the `config/agents.yaml` file and configure the agent settings according to your requirements.

2. Open the `config/tasks.yaml` file and configure the task settings according to your requirements.

3. Create a `.env` file in the project root directory by copying the `.env.EXAMPLE` template:

   ```
   cp .env.EXAMPLE .env
   ```

4. Open the `.env` file and provide the necessary API keys for the external tools used by the agents (e.g., SerperDevTool, ScrapeWebsiteTool). Replace the placeholder values with your actual API keys.

   ```
   SERPER_API_KEY=your_serper_api_key
   SCRAPE_WEBSITE_API_KEY=your_scrape_website_api_key
   ```

## Usage

1. Open the `main.py` file.

2. Modify the `inputs` dictionary in the `run_crew()` function to provide the necessary information for your trip, such as origin, destination, age, hotel location, flight information, and trip duration.

3. Run the script:

   ```
   python3 main.py
   ```

4. The script will execute the CrewAI Surprise Trip Planner and generate a personalized itinerary based on your inputs.

5. The generated itinerary will be saved in the `itinerary.md` file in root directory.

## Project Structure

- `config/`: Contains configuration files for agents and tasks.
- `my_crew.py`: Defines the SurpriseTravelCrew class and its initialization.
- `main.py`: The main script to run the CrewAI Surprise Trip Planner.
- `.env.EXAMPLE`: Template file for the `.env` file to store API keys.
- `itinerary.md`: The generated itinerary output file.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
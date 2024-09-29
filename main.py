from my_crew import SurpriseTravelCrew

def run_crew():
    inputs = {
        "origin": "Budapest international airport",
        "destination": "Porto",
        "age": 40,
        "hotel_location": "Porto",
        "flight_information": "WSC3156, leaving at 1:00 PM October 10th, 2024 - coming back at 1:00 PM October 15th, 2024",
        "trip_duration": "5 days"
    }

    crew = SurpriseTravelCrew()
    result = crew.kickoff(inputs=inputs)
    print(result)

if __name__ == "__main__":
    run_crew()
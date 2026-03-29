from agent import create_agent
from report_generator import generate_report

def run():
    topic = input("Enter topic: ")

    agent = create_agent()

    print("Researching...\n")
    result = agent.run(f"Research in detail about: {topic}")

    report = generate_report(topic, result)

    print(report)

if __name__ == "__main__":
    run()
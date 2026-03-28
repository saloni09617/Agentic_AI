# Agentic_AI
# 🤖 Autonomous Research Agent (LangChain)

## 📌 Project Overview

This project implements an **Autonomous Research Agent** using LangChain that can automatically:

* Search information from the web 🌐
* Retrieve knowledge from Wikipedia 📚
* Analyze and summarize data 🧠
* Generate a structured research report 📄

The agent uses a **ReAct (Reasoning + Acting)** approach to intelligently decide which tool to use while generating responses.

---

## 🎯 Objective

To build an AI-powered agent capable of conducting research on a given topic and producing a well-structured report including:

* Cover Page
* Title
* Introduction
* Key Findings
* Challenges
* Future Scope
* Conclusion

---

## ⚙️ Technologies Used

* Python 🐍
* LangChain
* OpenAI GPT Model
* Tavily Web Search API
* Wikipedia API

---

## 🧩 Features

* 🔍 Web search using Tavily API
* 📖 Knowledge retrieval from Wikipedia
* 🤖 ReAct-based intelligent agent
* 📝 Automated report generation
* ⚡ Easy-to-use command line interface

---

## 🛠️ Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/your-username/autonomous-research-agent.git
cd autonomous-research-agent
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Add API Keys

Create a `.env` file in the root directory and add:

```env
OPENAI_API_KEY=your_openai_api_key
TAVILY_API_KEY=your_tavily_api_key
```

---

## ▶️ How to Run

```bash
python main.py
```

Enter a topic when prompted:

```
Enter topic: Impact of AI in Healthcare
```

---

## 📊 Sample Topics

* Impact of AI in Healthcare
* Role of Blockchain in Finance
* Future of Electric Vehicles
* Cybersecurity in the Digital Age

---

## 📁 Project Structure

```
autonomous-research-agent/
│
├── main.py
├── .env
├── requirements.txt
├── README.md
└── sample_outputs/
    ├── output1.txt
    └── output2.txt
```

---

## 📄 Sample Outputs

The project includes two sample generated reports:

* `output1.txt` → AI in Healthcare
* `output2.txt` → Blockchain in Finance

---

## 🚀 Future Improvements

* Add Streamlit UI for better interaction
* Export reports as PDF
* Use more advanced tools (Arxiv, Google Scholar)
* Improve summarization with memory

---

## ✅ Conclusion

This project demonstrates how AI agents can automate research tasks by combining:

* Tool usage
* Reasoning capability
* Natural language generation

Such systems can significantly reduce manual effort in research and content creation.

---

## 👩‍💻 Author

Saloni Verma

---

## 📌 Submission

* GitHub Repository Link
* Sample Outputs Included
* Submitted via Google Form

---


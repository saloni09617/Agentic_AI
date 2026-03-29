from langchain.tools import Tool
from langchain.utilities import WikipediaAPIWrapper
from langchain.tools import DuckDuckGoSearchRun

# Wikipedia Tool
wiki = WikipediaAPIWrapper()
wiki_tool = Tool(
    name="Wikipedia",
    func=wiki.run,
    description="Useful for general knowledge and research"
)

# Web Search Tool
search = DuckDuckGoSearchRun()
search_tool = Tool(
    name="Search",
    func=search.run,
    description="Useful for latest information from web"
)

tools = [wiki_tool, search_tool]
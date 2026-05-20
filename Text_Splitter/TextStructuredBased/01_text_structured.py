from langchain_text_splitters import RecursiveCharacterTextSplitter

text = """
Y Combinator encourages founders to focus on growth rate rather than absolute numbers. It prevents them from being discouraged early on, when the absolute numbers are still low. It also helps them decide what to focus on: you can use growth rate as a compass to tell you how to evolve the company. But the main advantage is that by focusing on growth rate you tend to get something that grows exponentially.

YC doesn't explicitly tell founders that with growth rate "you get out what you put in," but it's not far from the truth. And if growth rate were proportional to performance, then the reward for performance p over time t would be proportional to pt.
"""

splitter = RecursiveCharacterTextSplitter(
    chunk_size = 100,
    chunk_overlap = 0
)

chunks = splitter.split_text(text)

print(chunks)
print(len(chunks))
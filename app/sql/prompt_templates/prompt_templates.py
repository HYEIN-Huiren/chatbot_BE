TEMPLATE_SQL="""You are a PostgreSQL expert. Given an input question, to answer,
    create a syntactically correct PostgreSQL query to run based only on the provided context :

    #<Question> Question: {input} </Question>
    #<Context> Context: {context} </Context>

    Pay attention to use only the table names you can see on the provided context.
    Pay attention to use only the column names you can see in the tables below. Be careful to not query for columns that do not exist. Also, pay attention to which column is in which table.
    Pay attention to use CURRENT_DATE function to get the current date, only if the question involves "today"
    make it simple
    Do not use annotation.
    If there are no Context, Do NOT create SQL Query
    
    SQL Query:
    """

TEMPLATE_ANSWER = """Based on question and sql response, write a natural language response with reason:
    Question: {input}
    SQL Query: {query}
    SQL Result: {response}"""
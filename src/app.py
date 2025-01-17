from fastapi import FastAPI, HTTPException
from src.gpt_template import chat
from src.llama_index_template import initialize_index, query_index
import uvicorn

app = FastAPI()
app.llama_index = initialize_index()

@app.get('/query')
def query(user_query: str):
    try:
        retrieval_result = query_index(app.llama_index, user_query)

        generated_answer = chat(user_query, retrieval_result)

        return {
            "retrieval_result": retrieval_result.response,
            "generated_answer": generated_answer
        }

    except Exception as e:
        return HTTPException(500, detail=str(e))


@app.post('/rebuild_index')
def rebuild_index():
    try:
        app.llama_index = initialize_index()
        return {'message': 'The index has been successfully rebuilt'}
    except Exception as e:
        return HTTPException(500, detail=str(e))


if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=8000)

from fastapi import FastAPI, HTTPException
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from agent.graph import pronto_agent
import json

app = FastAPI()


class ChatRequest(BaseModel):
    message: str


@app.post("/chat")
async def chat(request: ChatRequest):
    try:
        graph = pronto_agent.get_graph()
        

        inputs = {
            "messages": [{"role": "user", "content": request.message}]
        }
        

        async def stream_response():
            async for event in graph.astream(inputs, stream_mode="values"):
                if "messages" in event:
                    last_message = event["messages"][-1]
                    if isinstance(last_message, dict) and last_message.get("role") == "assistant":
                        yield f"data: {json.dumps({'content': last_message['content']})}\n\n"
                    elif hasattr(last_message, "content"):
                        yield f"data: {json.dumps({'content': last_message.content})}\n\n"
            yield "data: [DONE]\n\n"
        
        return StreamingResponse(stream_response(), media_type="text/event-stream")
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
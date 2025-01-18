from fastapi import FastAPI
from pydantic import BaseModel
from newsletter_trends.workflow import *
from newsletter_trends.tools import *
from newsletter_trends.chains import *
from newsletter_trends.state import *
from newsletter_trends.nodes import *

app = FastAPI()

class EndPoint(BaseModel):
    country: str
    head: int
    k: int

@app.post("/")
def main(request: EndPoint):
    app = compile_workflow()
    response = app.invoke(request)
    return response
    
    
    
    
    
    
    
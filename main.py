from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def read_item(name: str = 'Recruto', message: str = 'Давай дружить!'):
    return {'response': f'Hello {name}! {message}'}
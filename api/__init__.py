import os
from fastapi import FastAPI

import logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("uvicorn.error")

from dotenv import dotenv_values
config = {
    **dotenv_values(os.getenv("APP_CONFIG")),  # load shared development variables
    **os.environ,  # override loaded values with environment variables
}

from api import routes

def create_app():
    app = FastAPI(title="niftyX API",
    description="use stable diffusion to create NFTs on the XRPL blockchain",
    version=config['API_VERSION'])
    return app

app = create_app()
app.include_router(routes.router)

import os
from fastapi import APIRouter

import logging
logger = logging.getLogger("uvicorn.error")

from dotenv import dotenv_values
config = {
    **dotenv_values(os.getenv("APP_CONFIG")),  # load shared development variables
    **os.environ,  # override loaded values with environment variables
}

router = APIRouter()

@router.get("/info")
def get_api_info():
    # ulogger.info(f"version: {config['APP_VERSION']}")
    # return jsonify({'version': config['APP_VERSION']}), 200
    # logger.info(f"get_api_info {ApiInfo().to_dict()}")
    return {"version": f"{config['API_VERSION']}"}

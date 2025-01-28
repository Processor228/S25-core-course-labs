"""
 In this module we implement a simplistic web service that provides
 current time in Moscow.

 SPDX-LICENCE: no-licence
 Author: Elon Max
"""

import os
import uvicorn
from fastapi import FastAPI
from routers import time_router

app = FastAPI()

# Include the router from the time module
app.include_router(time_router)

if __name__ == "__main__":
    print("Starting webserver...")
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=int(os.getenv("PORT", 8080)),
        log_level=os.getenv('LOG_LEVEL', "info"),
        proxy_headers=True
    )

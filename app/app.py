from fastapi import FastAPI
from app.api.v1 import endpoints
from app.logging import logging

def create_app() -> FastAPI:
    app = FastAPI(
        title="AI Medical Analysis API",
        version="1.0.0"
    )

    # Include API Router
    app.include_router(endpoints.router)

    # Add startup/shutdown events (optional)
    @app.on_event("startup")
    async def startup_event():
        logging.info("API is starting up!")

    @app.on_event("shutdown")
    async def shutdown_event():
        logging.info("API is shutting down!")

    return app

# For running directly
app = create_app()

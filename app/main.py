"""Roomies API - the entry point of the server."""

from fastapi import FastAPI

app = FastAPI(
    title="Roomies API",
    description="Backend for a roommates app: shared expenses, chores and more.",
    version="0.1.0",
)


@app.get("/")
def root():
    """A simple check that the server is up."""
    return {"message": "Welcome to Roomies!"}


@app.get("/health")
def health():
    """Used later by the hosting service to check the server is alive."""
    return {"status": "ok"}

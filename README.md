# Job Scheduler

IFN636 Tutorial 8. A small job processing system in Python that demonstrates
inheritance, polymorphism, custom exceptions and threading, with an Express
API in front of it.

## Structure

    backend/models.py         Job base class, EmailJob, DataProcessingJob
    backend/task_manager.py   Tracks jobs by status
    backend/errors.py         JobExecutionError
    backend/executor.py       Runs jobs on threads
    backend/app.py            Entry point
    server.js                 Express API that runs app.py

## Run from the terminal

    source myenvpy/bin/activate
    cd backend
    python app.py

## Run as an API

    source myenvpy/bin/activate
    node server.js

Then open http://localhost:3000

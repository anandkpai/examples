from dagster import op, job, ScheduleDefinition, Definitions
from datetime import datetime

@op
def say_hello():
    print(f"Hello! Time is {datetime.utcnow()}")

@job
def hello_job():
    say_hello()

# Run every minute
hello_schedule = ScheduleDefinition(
    job=hello_job,
    cron_schedule="* * * * *",   # every minute
)

# Dagster MUST have a top-level Definitions object
defs = Definitions(
    jobs=[hello_job],
    schedules=[hello_schedule],
)

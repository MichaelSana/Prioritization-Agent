from fastapi import APIRouter
from app.orchestration.workflow import AgentWorkflow

router = APIRouter()


@router.get("/run-daily-planner")
async def run_daily_planner():

    workflow = AgentWorkflow()

    result = await workflow.execute()

    return result
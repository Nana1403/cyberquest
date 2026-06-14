from pydantic import BaseModel, Field


class Student(BaseModel):
    username: str
    level: int = 1
    xp: int = 0
    completed_missions: list[str] = Field(default_factory=list)
    badges: list[str] = Field(default_factory=list)
    correct_answers: int = 0
    total_answers: int = 0


class Mission(BaseModel):
    title: str
    description: str
    difficulty: str
    xp_reward: int
    badge: str


class Badge(BaseModel):
    name: str
    description: str

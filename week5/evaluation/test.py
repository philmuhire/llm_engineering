import json
from pathlib import Path
from pydantic import BaseModel, Field

TEST_FILE = str(Path(__file__).parent / "tests.jsonl")

#Pydantic way to describe a json schema with a python object having python object be a subclass of BaseModel
#BaseModel is a class that provides a way to validate and parse json data into a python object
#Field is a class that provides a way to describe a field in the json schema
#description is a string that provides a description of the field
class TestQuestion(BaseModel):
    """A test question with expected keywords and reference answer."""

    question: str = Field(description="The question to ask the RAG system")
    keywords: list[str] = Field(description="Keywords that must appear in retrieved context")
    reference_answer: str = Field(description="The reference answer for this question")
    category: str = Field(description="Question category (e.g., direct_fact, spanning, temporal)")


def load_tests() -> list[TestQuestion]:
    """Load test questions from JSONL file."""
    tests = []
    with open(TEST_FILE, "r", encoding="utf-8") as f:
        for line in f:
            data = json.loads(line.strip())
            tests.append(TestQuestion(**data))
    return tests

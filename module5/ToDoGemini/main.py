from fastapi import FastAPI
from models import Base
from database import engine

app = FastAPI()

Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    main()
from app.database.session import engine
from app.database.base import Base

# Import models so they are registered on the metadata
from app.models import User  # noqa: F401


def create_tables() -> None:
    Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    create_tables()
    print("Database tables created (if not existing)")

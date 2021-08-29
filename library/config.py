from pydantic import BaseSettings


class Settings(BaseSettings):  # pylint: disable=R0903
    class Config:  # pylint: disable=R0903
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = False

    debug: bool = False

    db_host: str

    db_port: int = 5432

    db_username: str = "library"

    db_pass: str

    db_name: str = "library"


settings = Settings()

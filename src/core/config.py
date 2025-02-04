from pydantic_settings import BaseSettings
from pydantic import PostgresDsn, RedisDsn

class Settings(BaseSettings):
    postgres_url: PostgresDsn
    redis_url: RedisDsn
    jwt_secret: str
    jwt_algorithm: str = "HS256"
    
    class Config:
        env_file = ".env"
        case_sensitive = True

settings = Settings() 
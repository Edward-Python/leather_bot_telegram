from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import SecretStr

from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    token: SecretStr
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

conf_settigs = Settings()
from dotenv import find_dotenv, dotenv_values

env_file = find_dotenv(".env")
env = dotenv_values(env_file)
db_uri = f"{env['DB_USERNAME']}:{env['DB_PASSWORD']}@{env['DB_HOST']}:{env['DB_PORT']}/{env['DB_NAME']}"

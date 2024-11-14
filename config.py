import environs

env = environs.Env()
env.read_env()

HEADLESS_MODE = env.bool("HEADLESS_MODE", default=False)

WORKSECTION_EMAIL = env.str("WORKSECTION_EMAIL")
WORKSECTION_PASSWORD = env.str("WORKSECTION_PASSWORD")

DISCORD_USER_TOKEN = env.str("DISCORD_USER_TOKEN")

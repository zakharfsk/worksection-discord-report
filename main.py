from datetime import datetime, timedelta

from discord.ext import commands
from loguru import logger

import config
from services.worksection import WorksectionParser

logger.add(
    "logs/latest.log",
    level="INFO",
    rotation="1 day",
    compression="zip"
)

client = commands.Bot(command_prefix='.', self_bot=True)


@client.event
async def on_ready():
    logger.info(f'Logged in as {client.user}')
    logger.info("For generating report use .report command in channel")


@client.command("report")
async def report_command(ctx: commands.Context):
    await ctx.message.delete()
    report = await WorksectionParser.generate_report()

    if report is None:
        return

    msg = f"Привіт.\n" + \
          f"{(datetime.now() - timedelta(days=1)).strftime("%d.%m.%Y")}\n\n" + \
          f"Загальний час: {report.total_time}\n\n"

    for project in report.projects:
        msg += f"Проект: {project.name}\n"
        for task in project.tasks:
            msg += f"Задача: {task.name}\n"
            msg += f"Час: {task.time}\n"
        msg += "\n"

    await ctx.send(msg)


client.run(config.DISCORD_USER_TOKEN, bot=False)

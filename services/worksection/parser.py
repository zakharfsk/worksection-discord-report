from loguru import logger
from playwright.async_api import async_playwright

import config
from .dto import Project, Report, Task
from .selectors import Selectors


class WorksectionParser:
    WORKSECTION_HOME_URL = "https://avivi.worksection.com/"
    WORKSECTION_REPORT_URL = WORKSECTION_HOME_URL + "report/"

    @classmethod
    async def generate_report(cls) -> Report | None:
        parser = cls()
        playwright_instance = await async_playwright().start()
        browser = await playwright_instance.chromium.launch(headless=config.HEADLESS_MODE, slow_mo=1500)
        context = await browser.new_context()
        page = await context.new_page()

        await page.add_init_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
        await page.goto(parser.WORKSECTION_HOME_URL)

        if "login" in page.url:
            logger.info("Trying to log in")
            try:
                await page.locator(Selectors.EMAIL_FIELD).fill(config.WORKSECTION_EMAIL)
                await page.locator(Selectors.PASSWORD_FIELD).fill(config.WORKSECTION_PASSWORD)
                await page.locator(Selectors.SUBMIT_LOGIN_BUTTON).click()
            except Exception as e:
                logger.error(f"Error while logging in: {e}")
                await context.close()
                await browser.close()
                return
            finally:
                logger.success("Logged in")

        await page.goto(parser.WORKSECTION_REPORT_URL)

        await page.locator(Selectors.OPEN_CALENDAR).click()
        await page.locator(Selectors.TODAY_DATE).hover()
        await page.locator(Selectors.YESTERDAY_DATE).click()

        logger.info("Getting report data")
        total_sum_time = await page.locator(Selectors.TOTAL_SUM_TIME).text_content()
        projects_list = await page.locator(Selectors.PROJECTS_LIST).all()
        logger.success("Report data received")

        report = Report(total_sum_time, [])

        for task in projects_list:
            project_name = await task.locator(Selectors.PROJECT_NAME).text_content()
            project = Project(project_name.strip(), [])

            project_tasks = await task.locator(Selectors.PROJECT_TASKS).all()

            for project_task in project_tasks:
                task_name = await project_task.locator(Selectors.TASK_NAME).text_content()
                task_time = await project_task.locator(Selectors.TASK_TIME).text_content()
                if task_time != '—':
                    project.tasks.append(Task(task_name.strip(), task_time.strip()))

            report.projects.append(project)

        await context.close()
        await browser.close()

        return report

class Selectors:
    EMAIL_FIELD = '//*[@id="femail"]'
    PASSWORD_FIELD = '//*[@id="content"]/form/div[1]/p[2]/input'
    SUBMIT_LOGIN_BUTTON = '//*[@id="content"]/form/div[1]/input[3]'
    TOTAL_SUM_TIME = '//*[@id="content_both"]//*[@id="total_summ"]/div/div[2]/span'

    OPEN_CALENDAR = '//*[@id="dr_rng"]'
    TODAY_DATE = '//*[@id="dr_rngmenu"]/div[3]/div[4]/a[2]'
    YESTERDAY_DATE = '//*[@id="dr_rngmenu"]/div[3]/div[4]/a[1]'

    PROJECTS_LIST = '//*[@id="listing"]/div//*[@class="listing__group"]'
    PROJECT_TASKS = '//*[@class="listing__group__content"]/div[contains(@class, "listing__item listing__item-level0")]'
    PROJECT_NAME = '//*[@class="listing__group__title"]/span[@class="in"]'
    TASK_NAME = '//*[@class="in"]/div[@class="td_info"]/div[@class="name"]/a[@class="m"]'
    TASK_TIME = '//*[@class="in"]/div[@class="td_time td_time_gr"]/span'

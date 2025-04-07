import os
import datetime
import pytest
import pytest_html
from playwright.sync_api import Page

report_dir = None

# from playwright.sync_api import sync_playwright

# @pytest.fixture
# def page():
#     headless_env = os.getenv("HEADLESS", "true").lower()
#     headless = headless_env == "true"

#     with sync_playwright() as p:
#         browser = p.chromium.launch(headless=headless)
#         context = browser.new_context()
#         page = context.new_page()
#         yield page
#         browser.close()


# @pytest.hookimpl(hookwrapper=True)
# def pytest_runtest_makereport(item, call):
#     outcome = yield
#     rep = outcome.get_result()

#     if rep.when == "call" and rep.failed:

#         page = item.funcargs.get("page", None)
#         if page:
#             screenshot_dir = "screenshots"
#             file_name = f"{item.name}.png"
#             destination = os.path.join(screenshot_dir, file_name)

#             os.makedirs(screenshot_dir, exist_ok=True)
#             page.screenshot(path=destination, full_page=True)

#             if item.config.pluginmanager.hasplugin("html"):
#                 extra = getattr(rep, "extra", [])
#                 # extra.append(pytest_html.extras.image(destination))
#                 extra.append(
#                     pytest_html.extras.image(
#                         os.path.relpath(destination, start="reports")
#                     )
#                 )
#                 rep.extra = extra


def pytest_configure(config):
    if not config.option.collectonly:
        global report_dir
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        report_folder = f"report_{timestamp}"
        report_dir = os.path.join("reports", report_folder)
        os.makedirs(report_dir, exist_ok=True)

        report_file = os.path.join(report_dir, f"{report_folder}.html")
        config.option.htmlpath = report_file


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    global report_dir
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        page = item.funcargs.get("page", None)
        if page:
            screenshots_dir = os.path.join(report_dir, "screenshots")
            os.makedirs(screenshots_dir, exist_ok=True)

            file_name = f"{item.name}.png"
            destination = os.path.join(screenshots_dir, file_name)

            page.screenshot(path=destination, full_page=True)

            if item.config.pluginmanager.hasplugin("html"):
                extra = getattr(rep, "extra", [])
                rel_path = os.path.relpath(destination, start=report_dir)
                extra.append(pytest_html.extras.image(rel_path))
                rep.extra = extra


@pytest.fixture(scope="session")
# pylint: disable=redefined-outer-name
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        "viewport": {"width": 1280, "height": 720},  # 472x800 tela mobile
        "ignore_https_errors": True,
        "record_video_dir": None,
    }


@pytest.fixture(scope="function", autouse=True)
def set_default_timeout(page):
    # Define o timeout global para cada ação (ex: click, fill, etc)
    page.set_default_timeout(10000)
    # Para timeouts de navegação:
    page.set_default_navigation_timeout(20000)


@pytest.fixture(scope="session")
def browser_type_launch_args():
    headless_env = os.getenv("HEADLESS", "false").lower()
    return {"headless": headless_env == "true"}


# @pytest.fixture(scope="session")
# def browser_type_launch_args():
#     return {"headless": True}  # define o modo headless


@pytest.fixture(autouse=True)
def inject_page_and_pages(request, page: Page):
    request.instance.page = page

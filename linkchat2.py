import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto("https://chat.openai.com")

        screenshot_counter = 0

        while True:
            await page.fill("textarea", "write python code to tile all tasks in an 8 grid")
            await page.press("textarea", "Enter")
            await page.wait_for_selector(".text-message:last-of-type:not(.changing)")

            # Take screenshot
            await page.screenshot(path=f"await{str(screenshot_counter)}.png")
            screenshot_counter += 1

            message = await page.inner_text(".text-message:last-of-type")
            code = message.strip().split("\n")[-1]
            try:
                result = eval(code)
                if not result:
                    print("No errors occurred. Breaking the loop.")
                    break
            except Exception as e:
                result = f"Error: {str(e)}"
                await page.fill("textarea", str(result))
                await page.press("textarea", "Enter")

                # Take screenshot
                await page.screenshot(path=f"error.png")
                print("Error occurred. Screenshot captured.")

loop = asyncio.get_event_loop()
loop.run_until_complete(main())

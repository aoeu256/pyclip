import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto("https://chat.openai.com")

        while True:
            await page.fill("textarea", "write python code to tile all tasks in an 8 grid")
            await page.press("textarea", "Enter")
            await page.wait_for_selector(".text-message:last-of-type:not(.changing)")

            message = await page.inner_text(".text-message:last-of-type")
            code = message.strip().split("\n")[-1]
            try:
                result = eval(code)
            except Exception as e:
                result = f"Error: {str(e)}"

            await page.fill("textarea", str(result))
            await page.press("textarea", "Enter")

asyncio.run(main())

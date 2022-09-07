import unittest
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

url = "http://localhost:8000"
# try:
#     browser.get(url)
#     assert "success" in browser.title
# except selenium.common.exceptions.WebDriverException:
#     raise AssertionError(f"Failed to connect {url}")

class NewVisitorTest(unittest.TestCase):
    def setUp(self) -> None:
        self.browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                                        options=webdriver.ChromeOptions())
        self.browser.implicitly_wait(3)

    def tearDown(self) -> None:
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self) -> None:
        # 홍길동은 멋진 온라인 To-Do 앱을 들었다. 그는 곧바로 해당 웹 사이트에 방문했다.
        self.browser.get('http://localhost:8000')

        # 그는 홈페이지의 제목을 확인한다
        self.assertIn("To-Do", self.browser.title)
        header_text = self.browser.find_element(By.TAG_NAME, "h1").text
        self.assertIn("To-Do", header_text)

        # 그는 To-Do List에 아이템을 만든다.
        input_box = self.browser.find_element(By.ID, "id_new_item")
        self.assertEqual(
            input_box.get_attribute("placeholder"),
            "Enter a To-do item"
        )

        # "시장에서 우유 사기"라는 문장을 TextBox에 작성한다.
        input_box.send_keys("시장에서 우유 사기")

        # 그가 Enter를 누르는 순간, 페이지가 업데이트되고 페이지에
        # "1. 시장에서 우유 사 오기"가 To-Do List에 나타난다.
        input_box.send_keys(Keys.ENTER)
        table = self.browser.find_element(By.ID, "id_list_table")
        rows = table.find_elements(By.TAG_NAME, "tr")
        self.assertTrue(
            any(row.text == '1: 시장에서 우유 사기' for row in rows)
        )


        # 아직 TextBox가 여전히 있다. 그는 "TDD 공부하기"를 입력하고, 엔터를 누른다
        self.fail("Test is not over")
        # 페이지가 다시 업데이트되고, 두 아이템이 리스트에 나타난다.

        # 그는 웹사이트가 이 리스트를 기억하고 있을 지 궁금했다.
        # 웹사이트에서는 unique URL를 제공하고 있었다.
        # 그가 제공하는 URL에 접속하자, 그의 리스트가 여전히 존재했다.

        # 안심한 그는 잠에 들 수 있었다.
        self.browser.quit()

if __name__ == "__main__":
    unittest.main()
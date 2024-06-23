import requests

class WebsiteReader:
    def __init__(self, url):
        self.url = url

    def fetch_content(self):
        try:
            response = requests.get(self.url)
            if response.status_code == 200:
                return response.text
            else:
                return f"Failed to fetch content, status code: {response.status_code}"
        except requests.exceptions.RequestException as e:
            return f"Error fetching content: {str(e)}"

# 示例用法
if __name__ == "__main__":
    reader = WebsiteReader("https://www.example.com")
    content = reader.fetch_content()
    print(content)

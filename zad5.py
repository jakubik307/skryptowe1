import wikipedia


def get_article_info(article_title):
    try:
        page = wikipedia.page(article_title)
        summary = page.summary
        url = page.url

        return summary, url
    except wikipedia.exceptions.PageError:
        return "Article not found", ""
    except wikipedia.exceptions.DisambiguationError:
        return "Disambiguation page found. Please enter a more specific title.", ""


def main():
    title = input("Enter the title of the Wikipedia article: ")
    summary, url = get_article_info(title)

    print("\nSummary:")
    print(summary)
    print("\nURL to English Wikipedia page:")
    print(url)


main()

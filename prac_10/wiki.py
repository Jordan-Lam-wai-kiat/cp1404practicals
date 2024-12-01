import wikipedia
from bs4 import FeatureNotFound

blank = False
while blank == False:
    user_search = input("\nInput a search title or search phrase: ").strip()
    if user_search != "":
        try:
            page = wikipedia.page(user_search, auto_suggest=False)

            print(f"\nTitle: {page.title}")
            print(f"Summary:\n{wikipedia.summary(user_search, sentences=4)}")
            print(f"URL: {page.url}")

        except wikipedia.DisambiguationError as e:
            # Handle ambiguous search results
            print(f"We need a more specific title. Try one of the Following, or a new search:")
            print((e.options[:5]))

        except wikipedia.PageError:
            # Handle page not found
            print(f"\nNo page found for '{user_search}'. Please try another search.")

        except Exception as e:
            # Catch other errors
            print(f"\nAn error occurred: {e}")

    if user_search == "":
        print("Thank you.")
        blank = True
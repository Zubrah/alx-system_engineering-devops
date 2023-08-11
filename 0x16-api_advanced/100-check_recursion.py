import requests

def count_words(subreddit, word_list):
    def process_title(title):
        # Remove punctuation and special characters from the end of a word
        return title.rstrip('.!?_')

    base_url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Reddit Keyword Counter by YourUsername"}

    response = requests.get(base_url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        titles = [post['data']['title'] for post in data['data']['children']]

        word_count = {word.lower(): 0 for word in word_list}

        for title in titles:
            words = title.lower().split()
            for word in words:
                word = process_title(word)
                if word in word_count:
                    word_count[word] += 1

        sorted_words = sorted(
            word_count.items(),
            key=lambda item: (-item[1], item[0])
        )

        for word, count in sorted_words:
            if count > 0:
                print(f"{word}: {count}")

    elif response.status_code == 404:
        print(f"Subreddit '{subreddit}' not found or invalid.")

    else:
        print("An error occurred while fetching data from Reddit API.")

# # Example usage
# subreddit_name = input("Enter subreddit name: ")
# keywords = input("Enter keywords separated by spaces: ").split()
# count_words(subreddit_name, keywords)

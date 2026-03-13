import requests
import pandas as pd

# a) Fetch data from the API link
url = "https://jsonplaceholder.typicode.com/posts"
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    data = response.json()
    
    # b) Fetch all posts and print them
    print("--- All Posts ---")
    for post in data:
        print(f"Post ID: {post['id']} | User ID: {post['userId']} | Title: {post['title']}")
        # Limiting the print output so it doesn't flood the console, 
        # but the data contains all 100 posts.
    
    # Load data into a Pandas DataFrame for easier analysis
    df = pd.DataFrame(data)
    
    # c) Count the distinct number of users
    distinct_users = df['userId'].nunique()
    print(f"\n--- Analysis ---")
    print(f"Distinct number of users: {distinct_users}")
    
    # d) Which user has the highest number of posts?
    # value_counts() sorts in descending order, so the first index is the top user
    top_user = df['userId'].value_counts().idxmax()
    top_user_count = df['userId'].value_counts().max()
    print(f"User with the highest number of posts: User ID {top_user} (with {top_user_count} posts)")
    
    # e) What is the average word length of a post title?
    # Assuming "word length" means the number of words in the title
    df['title_word_count'] = df['title'].apply(lambda x: len(str(x).split()))
    avg_words_per_title = df['title_word_count'].mean()
    print(f"Average number of words per post title: {avg_words_per_title:.2f} words")
    
    # (Optional) If "word length" meant the average character length of the titles:
    df['title_char_length'] = df['title'].apply(len)
    avg_chars_per_title = df['title_char_length'].mean()
    print(f"Average character length per post title: {avg_chars_per_title:.2f} characters")

else:
    print(f"Failed to fetch data. Status code: {response.status_code}")
import hackernews
hn = HackerNews()

stories = hn.top_stories()
for story in stories:
    print(story)

def generate_hashtag(s):
    if not s:
        return False
    hashtag = "#" + s.title().replace(" ", "")
    return False if (len(hashtag) > 140 or len(s) == 0) else hashtag
    
    
    
print(generate_hashtag('he marketing team is spending way too much time typing in hashtags.'))
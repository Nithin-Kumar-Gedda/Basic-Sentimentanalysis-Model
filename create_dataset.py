import pandas as pd 

data = {
    'review':[
        "this movie is so good! i love it!",
        "Big diseaster film",
        "average film",
        "above average film",
        "super hit film",
        "block buster film",
        "below average film",
        "flop film",
        "diseaster film",
        "below average film",
        "epic block buster film",
        "historical block buster film",
        "flop film",
        "super blockbuster film",
    ],
    'sentiment':[1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1]
}

df = pd.DataFrame(data)
df.to_csv('MovieReviews.csv',index = False)
print("dataset created and saved as 'moviereviews.csv'")
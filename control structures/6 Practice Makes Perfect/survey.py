interest_cs = input("SURVEY Are you interested in computer science? (y/n): ").lower() == 'y'
like_playing_games = input("Do you like playing computer games? (y/n): ").lower() == 'y'
has_instagram = input("Do you have an Instagram account? (y/n): ").lower() == 'y'

print("SURVEY RESULTS")
if interest_cs:
    print('Interested in computer science: Yes')
else:
    print('Interested in computer science: No')
if like_playing_games:
    print('Playing computer games: Yes')
else:
    print('Playing computer games: No')
if has_instagram:
    print('Has an Instagram account: Yes')
else:
    print('Has an Instagram account: No')

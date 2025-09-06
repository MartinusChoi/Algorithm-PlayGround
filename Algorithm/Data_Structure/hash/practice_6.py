def get_genre_order(genres:list, plays:list) -> list:
    plays_per_genre = {}
    for genre, play in zip(genres, plays):
        if genre in plays_per_genre: plays_per_genre[genre] += play
        else: plays_per_genre[genre] = play
    plays_to_genre = {play:genre for genre, play in plays_per_genre.items()}

    return [plays_to_genre[play] for play in sorted(plays_per_genre.values(), reverse=True)]

def get_hash_per_genre(genres:list, plays:list)->list:
    hash_table = {}
    for idx, entity in enumerate(zip(genres, plays)):
        genre, play = entity[0], entity[1]
        if genre in hash_table: 
            if play in hash_table[genre]: hash_table[genre][play].append(idx)
            else: hash_table[genre][play] = [idx]
        else: hash_table[genre] = {play:[idx]}
    
    for genre, play in zip(genres, plays):
        if len(hash_table[genre][play]) >= 2: hash_table[genre][play] = sorted(hash_table[genre][play])
    
    return hash_table

def solution(genres:list, plays:list)->list:
    hash_table = get_hash_per_genre(genres, plays)
    genre_order = get_genre_order(genres, plays)
    playlist = []

    for genre in genre_order:
        if len(hash_table[genre].keys()) == 1:
            playlist.append(hash_table[genre][list(hash_table[genre].keys())[0]][0])
        else : 
            top_1, top_2 = sorted(hash_table[genre].keys(), reverse=True)[:2]
            if len(hash_table[genre][top_1]) >= 2: playlist.extend(hash_table[genre][top_1][:2])
            else: playlist.extend([hash_table[genre][top_1][0], hash_table[genre][top_2][0]])
    
    return playlist
def solution(players, callings):
    player_dict={player:i for i,player in enumerate(players)}
    rank_dict={i:player for i,player in enumerate(players)}
    for calling in callings:
        idx = player_dict[calling]
        rank_dict[idx],rank_dict[idx-1]=rank_dict[idx-1],rank_dict[idx]
        player_dict[rank_dict[idx]],player_dict[rank_dict[idx-1]] =player_dict[rank_dict[idx-1]] ,player_dict[rank_dict[idx]] 
    return list(rank_dict.values())
def solution(score):
    mean_score = list(map(lambda x : sum(x), score))
    sorted_mean_score = sorted(mean_score, reverse=True)
    return [sorted_mean_score.index(i) + 1 for i in mean_score]



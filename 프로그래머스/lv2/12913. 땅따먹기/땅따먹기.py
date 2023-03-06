def solution(land):
    next_land = land.pop()
    while land :
        priv_land = land.pop()
        next_land = [max([priv_land[i]+next_land[j] 
                          for j in range(4) if j!=i]) 
                     for i in range(4)] 
    return max(next_land)

"""맨 마지막땅에서부터 거꾸로 거슬러올라가면서 선택지를 줄이는 방식. 
함수 아래 예시 참고."""

"""반복문 동작과정 : priv_land의 특정 땅에 있을 때, 
선택할 수 있는 가장 좋은 next_land을 택했을 때의 점수를 더해서
새로운 next_land변수에 넣음. 
다음 반복문에서는 새로운 priv_land를 할당 하고 해당 과정을 반복"""

"""예를 들면,
| 1 | 2 | 3 | 5 |
| 5 | 6 | 7 | 8 |
| 4 | 3 | 2 | 1 |

에 대하여, 셋째줄(마지막줄)을 next_land, 둘째줄을 priv_land라 할때, 
둘째줄 5에서 셋째줄로 넘어갈때 선택가능한 값 중 가장 큰 3을 더한 8,
6,7,8에는 4를 더한 10,11,12를 구하고
리스트 [8,10,11,12]를 둘째줄에 대체, 마지막줄은 더이상 불필요.
| 1 |  2 |  3 |  5 |
| 8 | 10 | 11 | 12 |
| - |  - |  - |  - |

이제 둘째 줄을 next_land, 첫째줄을 priv_land라 두고 같은 과정을 반복.
| 13 | 14 | 15 | 16 |
|  - |  - |  - |  - |
|  - |  - |  - |  - |

더이상 거슬러 올라갈 수 없을 때, 남은 리스트의 최대값을 반환"""
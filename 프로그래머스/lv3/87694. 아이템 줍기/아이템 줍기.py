from math import asin
    
class LinkMap(dict):
    """모든 직사각형의 변 위에 존재하는 1칸단위의 점들과, 
    이 점들에 연결되어 있는 다른 점들을 딕셔너리 형식으로 생성.
    예시) link_map[(1,2)] = [(1,1),(1,3),(2,2),(0,2)]
    """
    def __init__(self,rectangle):
        for r in rectangle:
            x1,y1,x2,y2 = r
            dots  = [(x , y1) for x in range(x1,x2,   1)]
            dots += [(x2, y ) for y in range(y1,y2,   1)]
            dots += [(x , y2) for x in range(x2,x1,  -1)]
            dots += [(x1, y ) for y in range(y2,y1-1,-1)] # 시작점을 두번 넣은 것에 유의
            for i in range(len(dots)-1):
                self[dots[i]].append(dots[i+1])
            for i in range(1,len(dots)):
                self[dots[i]].append(dots[i-1])

    def __missing__(self,dot):
        self[dot] = []
        return self[dot]
    
    
def angle_of_rotation(a,b):
    '''두 벡터 사이의 회전각. a기준 b의 위치는, 회전각이 + 면 반시계방향, - 면 시계방향
    Args:
        a: 기준벡터 (x좌표,y좌표)  
        b: 대상벡터 (x좌표,y좌표)  
    Return:
        int
    '''
    xa,ya = a
    xb,yb = b
    return asin((xa*yb-ya*xb)/((xa**2+ya**2)**.5*(xb**2+yb**2)**.5))
    
def where_do_i_have_to_go(point,direction,paths): 
    """가능한 경로 중, 기존방향 기준으로 가장 왼쪽으로가는 길을 고르는 함수
    Args:
        point:      현재기준점 (x좌표,y좌표)
        direction:  직전에 이동해온 방향, ±단위벡터 (1or0or-1,1or0or-1) 예) (0,-1) 
        paths:      point에 연결된 점들의 목록 중, 직전에 이동해온 곳을 제외한 목록
    Notes:
        vectors:    point를 기준으로 paths의 원소들을 백터화한 목록
        angles:     direction을 기준으로 vectors의 원소들의 회전각(방향)을 구한 목록
    """
    vectors = list(map(lambda a:(a[0]-point[0],a[1]-point[1]), paths))
    angles = list(map(lambda v:angle_of_rotation(direction,v),vectors))
    paths_dict = {paths[i]:angles[i] for i in range(len(paths))}
    return max(paths, key=lambda p: paths_dict[p])

def remove_inside_path(link_map):
    """생성된 link_map에서 안쪽으로 가는 경로들을 모두 제거하는 함수
    가장 왼쪽아래 있는 점에서 부터 시작하여 위로향하는 경로를 도는 경우를 상정할때,
    이경우 외곽선을 돌기 위해서는 현재 이동하던 방향을 기준으로 가장 왼쪽에 있는 길을 따라가야한다.
    직전에 지나온길과, 향할 길 중 가장 왼쪽에 있는 길 두가지만 남기고 나머지를 link_map에서 제거.
    시작점에 도달하면 반복문을 종료하고 외곽경로만 남은 link_map을 반환
    """
    minimum_point = min(link_map.keys(),key=lambda x:x[0]+x[1])
    a,b = link_map[minimum_point]
    direction = (0,1)
    point = min([a,b], key=lambda x:x[0])
    prev_p = minimum_point
    while point != minimum_point:
        paths = link_map[point]
        paths.remove(prev_p)
        next_p = where_do_i_have_to_go(point,direction,paths)
        link_map[point] = [prev_p,next_p]
        direction = (next_p[0]-point[0],next_p[1]-point[1])
        prev_p,point = point,next_p 
    return link_map
        
def min_distance(link_map, item, point, prev = None, c=0):
    """ 경로를 따라가 아이템까지의 최소 거리를 출력하는 함수"""
    if item == point : return c
    return min([min_distance(link_map,item,path,point,c+1) 
                for path in link_map[point] if path != prev])

def solution(rectangle, characterX, characterY, itemX, itemY):
    start = (characterX, characterY)
    link_map = LinkMap(rectangle)
    link_map = remove_inside_path(link_map)
    item = (itemX, itemY)
    return min_distance(link_map, item, start)
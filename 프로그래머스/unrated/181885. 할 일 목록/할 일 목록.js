function solution(todo_list, finished) {
    var result = [];
    for (let i=0;i<todo_list.length;i++) {
        if (finished[i] == false) {result.push(todo_list[i])}
    }
    return result
}
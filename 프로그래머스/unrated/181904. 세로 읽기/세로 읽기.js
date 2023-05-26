function solution(my_string, m, c) {
    var result = [];
    my_string.split('').forEach((s,i) => {
        if (i%m == c-1) {result.push(s)}
    })
    return result.join('')
}
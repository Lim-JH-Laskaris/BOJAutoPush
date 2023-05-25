function solution(arr) {
    var x = 1
    while (x<arr.length) {x *= 2}
    while (x>arr.length) {arr.push(0)}
    return arr
}
// 처음 작성한 코드
function solution(numbers) {
    var answer = [];
    numbers.forEach(function (i) {answer.push(i*2)});
    return answer
}

// 아래는 다른 사람의 풀이 참고
var solution = (numbers) => numbers.reduce((a, b) => [...a, b * 2], [])
var solution = (numbers) => numbers.map((number) => number * 2)


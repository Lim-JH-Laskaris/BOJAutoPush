function solution(arr1, arr2) {
    let answer = 0
    const arrSub = arr1.length - arr2.length;
    const sumSub = arr1.reduce((a, b) => a + b, 0) - arr2.reduce((a, b) => a + b, 0);
    if (arrSub != 0) {answer =  arrSub/Math.abs(arrSub)}
    else { if (sumSub != 0) {answer = sumSub/Math.abs(sumSub)}}
    return answer
}
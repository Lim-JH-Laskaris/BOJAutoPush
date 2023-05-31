function solution(arr1, arr2) {
    const sum    = (a,b) => a+b
    const arrSub = arr1.length      - arr2.length     
    const sumSub = arr1.reduce(sum) - arr2.reduce(sum)
    if (arrSub != 0) {return arrSub/Math.abs(arrSub)}
    if (sumSub != 0) {return sumSub/Math.abs(sumSub)}
    return 0
}
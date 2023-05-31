function solution(arr1, arr2) {
    const sum    = (a,b) => a+b
    const lenSub = arr1.length      - arr2.length     
    const sumSub = arr1.reduce(sum) - arr2.reduce(sum)
    if (lenSub != 0) {return lenSub/Math.abs(lenSub)}
    if (sumSub != 0) {return sumSub/Math.abs(sumSub)}
    return 0
}
function solution(arr1, arr2) {
    const arrSub = arr1.length - arr2.length;
    if (arrSub != 0) {return arrSub/Math.abs(arrSub)}
    const sumSub = arr1.reduce((a, b) => a + b, 0) - arr2.reduce((a, b) => a + b, 0);
    if (sumSub != 0) {return sumSub/Math.abs(sumSub)}
    return 0
}
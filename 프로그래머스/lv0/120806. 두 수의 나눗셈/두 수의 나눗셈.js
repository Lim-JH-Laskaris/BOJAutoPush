const solution = (num1, num2) => Math.floor(num1 / num2 * 1000)

// const solution = (num1, num2) => Math.trunc(num1 / num2 * 1000) // 이것도 가능

//Math.trunc()는 소수점 이하는 다 버린다. ex) Math.trunc(23.3) = 23, Math.trunc(-23.3) = -23
//Math.floor()는 소수점을 내림한다. ex) Math.floor(23.3) = 23, Math.floor(-23.3) = -24가 된다. 
//음수인 경우도 생각해서 소수점을 이하 수를 없애고 싶을때는 Math.trunc를 사용하는 것이 좋다.
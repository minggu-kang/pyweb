// 디지털 시계 구현

setInterval(myWatch, 1000)//1초간격 시간설정
function myWatch(){
    var date = new Date()
    var now = date.toLocaleTimeString()     //시간을 문자열로 반환
    document.getElementById("demo").innerHTML = now;
}
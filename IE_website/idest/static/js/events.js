var font = 0

$('h1').on('click',function(){
    //$('.collapse').collapse():
    console.log('hi')
})
$('.changefont').on('click',function(){
    
    if ((font%2) === 0){
        
        console.log('cou');
        $('p').css({"font-family":'COURIERPRIME-REGULAR'});
            
    }else if (font%2 !== 0){
        
        console.log('com');
        $('p').css({"font-family":'COMPAGNON-ROMAN','font-weight':"bold"});
            
        
    }
    font++
})
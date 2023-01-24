var font = 1

$('h1').on('click',function(){
    //$('.collapse').collapse():
    console.log('hi')
})
$('.changefont').on('click',function(){
    
    if ((font%2) === 0){
        
        console.log('cou');
        $('p').css({"font-family":'Courier Prime, monospace'});
            
    }else if (font%2 !== 0){
        
        console.log('com');
        $('p').css({"font-family": 'Comic Sans MS','font-weight':"bold"});
            
        
    }
    font++
})
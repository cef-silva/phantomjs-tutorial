var page = require('webpage').create();
page.viewportSize = {width: 1024, height: 768};
console.log('asjdiajsdahsu');
page.open('https://ma.equatorialenergia.com.br/', function(status){
    console.log('Status:', status);
    page.render('print1.png');
    page.evaluate(function() {
        document.querySelector('#identificador').value = '604.837.593-09';
        document.querySelector('#senha-identificador').value = '30/06/1999';
        document.querySelector('#envia-identificador').click();
    });
    page.render('print2.png');
    window.setTimeout(function() {
        console.log(page.url);
        page.render('print3.png');
        phantom.exit();
    }, 8000);

});
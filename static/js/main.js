function changecolor() {
    var titles = document.getElementsByTagName('h1'); 
    alert(" H1 tags color changed succcessfully! "); 
    for (var i = 0; i < titles.length; i++) {
        titles[i].style.color = 'green'; 
    }
}

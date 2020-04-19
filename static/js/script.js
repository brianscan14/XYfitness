/**
 * @scrollToTop
 * This function shows the button when the user scrolls down 80px from top of document
 * @topPage
 * This function scrolls to the top of the page when the button is clicked
 */

let mybutton = document.getElementById("topBtn");

window.addEventListener('scroll', function(e) {
    scrollToTop()
});

function scrollToTop() {
    if (document.body.scrollTop > 80 || document.documentElement.scrollTop > 80) {
    mybutton.style.display = "block";
        } else {
    mybutton.style.display = "none";
        }
}

function topPage() {
    document.body.scrollTo({top: 0, behavior: 'smooth'});
    document.documentElement.scrollTo({top: 0, behavior: 'smooth'});
}

$(document).ready(function() {
    $('#topBtn').click(function(){
        topPage();
    });
});


/**
 * @openSearchBar
 * These functions open the nav search bar by increasing the width of the overlay
 * @closeSearchBar
 * This function closes the nav search bar by decreasing the width of the overlay
 */

function openSearchBar() {
    let searchBar = document.getElementById("overlaySearchBar");
    if (searchBar) {
        searchBar.style.width = "100%";
        }
}

function openSearchBarSmall() {
    document.getElementById("overlaySearchBar").style.width = "100%";
}

function closeSearchBar() {
    document.getElementById("overlaySearchBar").style.width = "0%";
}

$(document).ready(function() {

$('#navSearchOpen').click(function(){
       openSearchBar();
    });

$('#navSearchOpenSmall').click(function(){
       openSearchBarSmall();
    });

$('#navSearchClose').click(function(){
       closeSearchBar();
    });
});


/**
 * @goBackPage
 * This function target the back button and just goes back one page
 * in the browser's history when clicked
 */

function goBackPage() {
    window.history.back();
    }

$(document).ready(function() {
$('#backButton').click(function(){
       goBackPage();
    });
});


// counter for quantity of prod items 

$(document).ready(function(){
    $('.minus').click(function () {
        var $input = $(this).parent().find('input');
        var amount = parseInt($input.val()) - 1;
        amount = amount < 1 ? 1 : amount;
        $input.val(amount);
        $input.change();
        return false;
    });
    $('.plus').click(function () {
        var $input = $(this).parent().find('input');
        $input.val(parseInt($input.val()) + 1);
        $input.change();
        return false;
    });
});



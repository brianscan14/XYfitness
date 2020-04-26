$(document).ready(function() {

    /**
     * Shows the scroll top button when the user scrolls down 100px from top of document
     */
    function scrollToTop() {
        let mybutton = document.getElementById("topBtn");

        if (document.body.scrollTop > 100 || document.documentElement.scrollTop > 100) {
        mybutton.style.display = "block";
        } else {
        mybutton.style.display = "none";
        }
    }

    window.addEventListener('scroll', function(e) {
        scrollToTop()
    });


    /**
     * Scrolls to the top of the page when the button is clicked
     */
    function topPage() {
        document.body.scrollTo({top: 0, behavior: 'smooth'});
        document.documentElement.scrollTo({top: 0, behavior: 'smooth'});
    }

    $('#topBtn').click(function(){
        topPage();
    });


    /**
     * Open the nav search bar by increasing the width of the
     * overlay to 100%
     */
    function openSearchBar() {
        let searchBar = document.getElementById("overlaySearchBar");
        if (searchBar) {
            searchBar.style.width = "100%";
        }
    }

    $('#navSearchOpen').click(function(){
        openSearchBar();
        });


    /**
     * Closes the nav search bar by decreasing the width of the
     * overlay to 0
     */
    function closeSearchBar() {
        document.getElementById("overlaySearchBar").style.width = "0%";
    }

    $('#navSearchClose').click(function(){
        closeSearchBar();
        });


    /**
     * Targets the back button and just goes back one page
     * in the browser's history when clicked
     */
    function goBackPage() {
        window.history.back();
    }

    $('#backButton').click(function(){
        goBackPage();
    });


    /**
     * Decreases the input value seen in the cart by 1,
     * will keep decreasing until it hits 1, as if the user
     * wants zero, they can just delete the item with the 
     * delete 'x' button in the items row.
     */
    $('.minus').click(function () {
        let $input = $(this).parent().find('input');
        let amount = parseInt($input.val()) - 1;
        amount = amount < 1 ? 1 : amount;
        $input.val(amount);
        $input.change();
        return false;
    });


    /**
     * Increases the input value seen in the cart by 1,
     * will keep incrementing as the user clicks it, 50 is 
     * the max input and is handled by the input's html.
     */
    $('.plus').click(function () {
        let $input = $(this).parent().find('input');
        $input.val(parseInt($input.val()) + 1);
        $input.change();
        return false;
    });


    /**
     * Used to pull the previous url's address, this is then
     * sliced to last 24 characters, only for if a user has to
     * register to use the cart, the next url is used in django's
     * login redirect but not for register, will only show up on
     * the register page as the 'shop' value if the url matches.
     * Which is pulled in the views file anmd redirects user then
     */
    let refer = document.referrer;
    if (refer.slice(-24)=='?next=/checkout/deliver/') {
        document.getElementById("urlValue").value = 'shop';
    }

});

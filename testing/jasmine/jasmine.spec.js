describe('Testing opening of overlay called from Nav ', () => {

    it ('openSearchBar should increase width to 100%', function() {
        $(".content").append("<div id='overlaySearchBar' style='width:40%'></div>");
        let searchBar = document.getElementById("overlaySearchBar");
        expect(searchBar.style.width).toEqual('40%')
        openSearchBar();
        expect(searchBar.style.width).toEqual('100%')
    });
    
});



/**
 * Created by zhouhenglc on 2021/12/20.
 */
$(document).ready(function () {
    // init Masonry
    // https://codepen.io/craigwheeler/pen/MYjBga
    var $grid = $('.grid').masonry({

        // set itemSelector so .grid-sizer is not used in layout
        // itemSelector: '.grid-item',
        // use element for option
        // columnWidth: '.grid-sizer',
        // percentPosition: true

        itemSelector: '.grid-item',
        isFitWidth: true,
        columnWidth: 1
    });
    // layout Masonry after each image loads
    $grid.imagesLoaded().progress(function () {
        $grid.masonry('layout');
    });
    $(".star-parent").click(function (event) {
        $(this).hide();
        $(this).siblings().show();
        var album = event.currentTarget.dataset['album'];
        var name = event.currentTarget.dataset['name'];
        var star = event.currentTarget.dataset['star'];
        var data = {'album': album, 'name': name, 'star': star};
        my_async_request2('/photo/star', 'PUT', data, function(data){
            console.info(data);
        });
    });
    $(".star-target").each(function () {
        var children = $(this).children('.star-parent');
        $(children[0]).show();
        $(children[1]).hide();
    });
});
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
});
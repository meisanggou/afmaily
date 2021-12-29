/**
 * Created by zhouhenglc on 2021/12/20.
 */
var cache_key = 'photo_star';
var star_cache = {};
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
        var ds = event.currentTarget.dataset;
        var album = ds['album'];
        var name = ds['name'];
        var star = ds['star'];
        var data = {'album': album, 'name': name, 'star': star};
        my_async_request2('/photo/star', 'PUT', data, function (data) {
            if(star == 'yes') {
                star_cache[album].push(name);
            }else{
                star_cache[album].forEach(function(item, index, arr) {
                    if(item == name) {
                        arr.splice(index, 1);
                    }
                });
            }
            set_local_storage(cache_key, star_cache);
            console.info(data);
        });
    });
    star_cache = get_local_storage(cache_key);
    if (star_cache == null) {
        star_cache = {};
    }
    $(".star-target").each(function () {
        var children = $(this).children('.star-parent');
        var ds = $(children[0])[0].dataset;
        var album = ds['album'];
        if (!(album in star_cache)) {
            star_cache[album] = new Array();
        }
        var name = ds['name'];
        if (star_cache[album].indexOf(name) >= 0) {
            $(children[0]).hide();
            $(children[1]).show();
        }
        else {
            $(children[0]).show();
            $(children[1]).hide();
        }
    });

});
/**
 * Created by zhouhenglc on 2021/12/18.
 */

var IMAGE_URLS = [];

$(document).ready(function(){
    $(".photo-item").each(function(){
        console.info($(this));
        var h = $(this)[0].dataset['href'];
        IMAGE_URLS.push(location.origin + h);
    });
    console.info(IMAGE_URLS);
    $(".photo-item").click(function(event){
        var h = event.currentTarget.dataset['href'];
        var url = location.origin + h;
        //var imgs = [location.origin + url];
        WeixinJSBridge.invoke("imagePreview", {
            "urls": IMAGE_URLS,
            "current": url
        });
    });
});
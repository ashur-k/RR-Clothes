$(document).ready(function() {
            $('#autoWidth').lightSlider({
                autoWidth:true,
                loop:true,
                onSliderLoad: function() {
                    $('#autoWidth').removeClass('cS-hidden');
                } 
            });
           $('#imageGallery').lightSlider({
                gallery:true,
                item:1,
                loop:true,
                thumbItem:9,
                slideMargin:0,
                enableDrag: false,
                currentPagerPosition:'left',  
            });  
        });
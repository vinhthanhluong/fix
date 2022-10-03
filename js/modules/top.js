$(function () {
    "use strict";
    console.log('( •ิཬ•ั ) Hello!!!');

    var obj = {
        init: function () {
            // this.aos();
            this.wow();
            this.visual();
            this.construct();
            this.loadPost();
            this.idxMenu();
        },

        //aos
        aos: function () {
            AOS.init({
                startEvent: 'DOMContentLoaded',
                offset: 0,
                duration: 800,
                delay: '200',
                easing: 'ease-in-sine',
                once: true,
                mirror: true,
                disable: function () {
                    return $(window).width() <= 768;
                },
            });
        },

        wow: function () {
            var wow = new WOW(
                {
                    boxClass: 'wow',      // default
                    animateClass: 'animated', // default
                    offset: 0,          // default
                    mobile: false,
                    live: false,       // default
                }
            )
            wow.init();
        },

        visual: function () {
            if ($('#visual').length > 0) {
                $('#visual').slick({
                    dots: true,
                    infinite: true,
                    speed: 1000,
                    slidesToShow: 1,
                    slidesToScroll: 1,
                    autoplay: true,
                    autoplaySpeed: 5000,
                    arrows: false,
                    centerMode: false,
                    centerPadding: 0,
                    pauseOnHover: false,
                    pauseOnFocus: false,
                    fade: false,
                    variableWidth: false,
                });
            }
        },

        construct: function () {
            // if ($('#const-slider').length > 0) {
            //     $('#const-slider').slick({
            //         dots: false,
            //         infinite: true,
            //         speed: 1000,
            //         slidesToShow: 3,
            //         slidesToScroll: 1,
            //         // autoplay: true,
            //         // autoplaySpeed: 5000,
            //         arrows: false,
            //         centerMode: false,
            //         centerPadding: 0,
            //         pauseOnHover: false,
            //         pauseOnFocus: false,
            //         fade: false,
            //         variableWidth: false,
            //         responsive: [
            //             {
            //                 breakpoint: 751,
            //                 settings: {
            //                     slidesToShow: 1,
            //                     slidesToScroll: 1,
            //                     arrows: true,
            //                 }
            //             },

            //         ]
            //     });
            // }
        },

        loadPost: function () {
            $.ajax({
                url: 'works/_custom/?limit=3',
                dataType: 'jsonp',
                success: function (json) {
                    $.each(json.data, function (i, val) {
                        var img;
                        if (val.img01) {
                            img = val.img01;
                        } else {
                            img = '<img src="./images/under-img01.jpg" alt="' + val.title + '"></img>';
                        }
                        var items =
                            '<li>' +
                            '<div class="const-item">' +
                            '<p class="const-img">' + img + '</p>' +
                            '<div class="const-content">' +
                            '<p class="const-tt">' +
                            '<span class="const-cate">亀岡市</span>' +
                            '<span class="const-t">' + val.title + '</span>'
                            + '</p>' +
                            '<div class="const-desc">' + val.txt02 + '</div>'
                            + '</div>' +

                            '<a href="./works/' + val.url + '" class="lk-full"></a>' +
                            '</div>' +
                            '</li>'
                        $('.const-list').append(items);
                    });

                    $('#const-slider').slick({
                        dots: false,
                        infinite: true,
                        speed: 1000,
                        slidesToShow: 3,
                        slidesToScroll: 1,
                        // autoplay: true,
                        // autoplaySpeed: 5000,
                        arrows: false,
                        centerMode: false,
                        centerPadding: 0,
                        pauseOnHover: false,
                        pauseOnFocus: false,
                        fade: false,
                        variableWidth: false,
                        responsive: [
                            {
                                breakpoint: 751,
                                settings: {
                                    slidesToShow: 1,
                                    slidesToScroll: 1,
                                    arrows: true,
                                }
                            },

                        ]
                    });

                    $('.construct .const-content').matchHeight();

                },
            });

            $.ajax({
                url: 'news/_custom/?cat=1',
                dataType: 'jsonp',
                success: function (json) {
                    $.each(json.data, function (i, val) {
                        var dateFormatted = val.date.substr(0, 4) + "." + val.date.substr(5, 2) + "." + val.date.substr(8, 2);
                        var item =
                            '<div class="infor-item">'+
                                '<p class="infor-date">'+ dateFormatted +'</p>'+
                                '<p class="infor-tt">'+ val.title  +' </p>'+
                                '<a href="./news/'+ val.url +'" class="lk-full"></a>'+
                           ' </div>';
                        $('#idx-tb-01').append(item);
                    });
                }
            });

            $.ajax({
                url: 'news/_custom/?cat=2',
                dataType: 'jsonp',
                success: function (json) {
                    $.each(json.data, function (i, val) {
                        var dateFormatted = val.date.substr(0, 4) + "." + val.date.substr(5, 2) + "." + val.date.substr(8, 2);
                        var item =
                            '<div class="infor-item">'+
                                '<p class="infor-date">'+ dateFormatted +'</p>'+
                                '<p class="infor-tt">'+ val.title  +' </p>'+
                                '<a href="./news/'+ val.url +'" class="lk-full"></a>'+
                           ' </div>';
                        $('#idx-tb-02').append(item);
                    });
                }
            });

            $.ajax({
                url: 'news/_custom/?cat=4',
                dataType: 'jsonp',
                success: function (json) {
                    $.each(json.data, function (i, val) {
                        var dateFormatted = val.date.substr(0, 4) + "." + val.date.substr(5, 2) + "." + val.date.substr(8, 2);
                        var item =
                            '<div class="infor-item">'+
                                '<p class="infor-date">'+ dateFormatted +'</p>'+
                                '<p class="infor-tt">'+ val.title  +' </p>'+
                                '<a href="./news/'+ val.url +'" class="lk-full"></a>'+
                           ' </div>';
                        $('#idx-tb-03').append(item);
                    });
                }
            });
        },

        idxMenu: function () {
            $(window).scroll(function () {
                var pod = $('html,body').scrollTop();
                var menuHeight = $('#header').outerHeight();
                var idxMenuHeight = $('.idx-menu').outerHeight();
                var scrollTop = pod + menuHeight;

                var _w = $(window).width();
                var nextElement = $('.idx-menu').next().offset().top;
                var posFixedMenu = nextElement - idxMenuHeight;

                if (_w > 750 && scrollTop >= posFixedMenu) {
                    $('.idx-menu').addClass('--fixed');
                    $('.btn-more').addClass('--active');
                } else {
                    $('.idx-menu').removeClass('--fixed');
                    $('.btn-more').removeClass('--active');
                }

            });
        }
    }

    obj.init();
});
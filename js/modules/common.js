$(function () {
    "use strict";
    console.log('( •ิཬ•ั ) Hello!!!');
    function anchorLink(el) {
        var p = $(el).offset();
        var offsetPC = 240;
        var offsetMid = 160;
        var offsetSP = 90;
        if ($(window).width() > 750 && $(window).width() < 1903) {
            $('html,body').animate({ scrollTop: p.top - offsetMid }, 400);
        }

        if ($(window).width() >= 1903) {
            $('html,body').animate({ scrollTop: p.top - offsetPC }, 400);
        }

        if ($(window).width() <= 750) {
            $('html,body').animate({ scrollTop: p.top - offsetSP }, 400);
        }
    }
    var obj = {
        init: function () {
            this.tab();
            this.toTop();
            this.anchorLink();
            this.matchHeight();
            this.menu();
            this.sliderUnder();
            // this.scrollToMail();
            // this.accordion();
        },

        //Change tab
        tab: function () {
            $('[data-tab]').click(function () {
                var _group = $(this).data('tab-group');
                var _index = $(this).data('tab');
                $('[data-tab][data-tab-group="' + _group + '"].active').removeClass('active');
                $(this).addClass('active');

                $('[data-tab-content][data-tab-group="' + _group + '"]').removeClass('active');
                $('[data-tab-content="' + _index + '"][data-tab-group="' + _group + '"]').addClass('active');
            });
        },

        toTop: function () {
            $(".scroll-top").click(function () {
                $('html,body').animate({
                    scrollTop: 0,
                }, 1000);
                return false;
            });

            $(window).scroll(function () {
                var st = $('html,body').scrollTop();
                if (st > 300) {
                    $('.scroll-top').addClass('--active');
                    $('.btn-fix').addClass('--fix');
                } else {
                    $('.scroll-top').removeClass('--active');
                    $('.btn-fix').removeClass('--fix');
                }

                if (st > 10) {
                    $('#header').addClass('--fix');
                } else {
                    $('#header').not('.under #header.--fix').removeClass('--fix');

                }
            });
        },

        //Anchor Link
        anchorLink: function () {
            $(window).on('load', function () {
                "use strict";
                // ANCHOR FROM OTHER PAGE
                var hash = location.hash;
                if (hash && $(hash).length > 0) {
                    anchorLink(hash);
                }
                // ANCHOR IN PAGE
                $('a[href^="#"]').click(function () {
                    var getID = $(this).attr('href');
                    if ($(getID).length) {
                        anchorLink(getID);
                        // CLOSE SP NAV
                        if ($('body').hasClass('open-nav')) {
                            $('#menu-toggle').trigger('click');
                        }
                        return false;
                    }
                });
            });
        },

        matchHeight: function () {
            // $('.asddd').matchHeight();
        },

        menu: function () {
            $('.hamburger-btn').click(function () {
                $(this).toggleClass('--active');
                $('body').toggleClass('open-nav no-scroll');
            });

            $('.close-btn').click(function () {
                $('.hamburger-btn').trigger('click');
            });


            if ($('.header-menu').length) {
                $('.dropdown > span').click(function () {
                    $(this).toggleClass('open');
                    $(this).next('.sub-menu').stop().slideToggle();
                    $(this).closest('.dropdown').siblings().find('.sub-menu').stop().slideUp();
                    $(this).closest('.dropdown').siblings().find('span').removeClass('open');
                });

                $(window).on('resize load', function () {
                    var _w = $(window).width();
                    if (_w > 750) {
                        $('.dropdown > span').removeClass('open');
                        $('.sub-menu').removeAttr('style');
                    }
                });
            }
        },

        sliderUnder: function () {
            if ($('.wkd-slider').length) {
                $('.wkd-bg').slick({
                    slidesToShow: 1,
                    slidesToScroll: 1,
                    arrows: true,
                    fade: true,
                    asNavFor: '.wkd-sm',
                });
                $('.wkd-sm').slick({
                    slidesToShow: 6,
                    slidesToScroll: 1,
                    asNavFor: '.wkd-bg',
                    focusOnSelect: true,
                    arrows: false,
                    responsive: [
                        {
                            breakpoint: 751,
                            settings: {
                                slidesToShow: 4,
                                slidesToScroll: 1,
                            }
                        },
                        {
                            breakpoint: 426,
                            settings: {
                                slidesToShow: 3,
                                slidesToScroll: 1,
                            }
                        },

                    ]
                });

            }
        },

        //scroll to mail form
        scrollToMail: function () {
            if ($('#fmail_section').length > 0) {
                var x = location.search;
                if (x.search('mode') >= 0) {
                    var _mailFormPos = $('#fmail_section').offset().top;
                    _mailFormPos = parseInt(_mailFormPos);
                    if ($(window).width() > 750) {
                        $('html,body').animate({ scrollTop: _mailFormPos - 0 }, 400);
                    } else {
                        $('html,body').animate({ scrollTop: _mailFormPos - 0 }, 400);
                    }
                }
            }
        },

        //Accordion
        accordion: function () {
            $(".accordion-button").click(function (e) {
                e.preventDefault();
                $(this).toggleClass("open");
                var _accordionID = $(this).attr('id');
                var accordion_content = $('[data-accordion-for="' + accordionID + '"]');
                accordion_content.stop().slideToggle(200);
            });
        }

    }

    obj.init();
});
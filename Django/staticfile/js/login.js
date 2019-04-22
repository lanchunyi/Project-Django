var login = {
    init: function(){
        login.bindEvent();
    },
    bindEvent: function(){
        $(".sib-submit").on("click", login.doLogin);
    },
    doLogin: function(){
        var uname = $("username").val();
        var pwd = $("passwd").val();
        $.ajax({
            type: "post",
            data: {username:uname, passwd:pwd},
            url: "/ajax_valid",
            dataType: "json",
            success: function(resp){
                var retCode = resp.result.retCode;
                if(retCode==1){
                    var localstorage = window.localStorage;
                    var userinfo = JSON.stringify(resp.result.data.userinfo);
                    localstorage.setItem("userinfo", userinfo);
                    window.location.href="/index";
                }
            }
        });
    },




}

$(function(){
    login.init();
});
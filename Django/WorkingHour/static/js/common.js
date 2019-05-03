String.prototype.replaceAll = function(s1,s2){
	return this.replace(new RegExp(s1,"gm"),s2);
}
String.prototype.trim = function() {
	return this.replace(/(^\s*)|(\s*$)/g, "");
}
String.prototype.ltrim = function() {
	return this.replace(/(^\s*)/g, "");
}
String.prototype.rtrim = function() {
	return this.replace(/(\s*$)/g, "");
}
String.prototype.endWith = function(str) {
	if (str == null || str == "" || this.length == 0 || str.length > this.length)
		return false;
	if (this.substring(this.length - str.length) == str)
		return true;
	else
		return false;
	return true;
}
String.prototype.startWith = function(str) {
	if (str == null || str == "" || this.length == 0 || str.length > this.length)
		return false;
	if (this.substr(0, str.length) == str)
		return true;
	else
		return false;
	return true;
}

/**
 * 计算字符串长度(英文占1个字符，中文汉字占2个字符)
*/
String.prototype.gblen = function(){
	var len = 0;
	for (var i=0; i<this.length; i++){
		var c = this.charCodeAt(i);
		if((c >= 0x0001 && c <= 0x007e) || (0xff60<=c && c<=0xff9f)){
			len++;
		}
		else{
			len+=2;
		}
	}
	return len;
}

/**
 * 计算字符串长度(英文占1个字符，中文汉字占2个字符)
*/
function strlen(str){
	var len = 0;
	for (var i=0; i<str.length; i++){
		var c = str.charCodeAt(i);
		if((c >= 0x0001 && c <= 0x007e) || (0xff60<=c && c<=0xff9f)){
			len++;
		}
		else{
			len+=2;
		}
	}
	return len;
}

Date.prototype.format = function(format){ 
	var o = { 
	"M+" : this.getMonth()+1, //month 
	"d+" : this.getDate(), //day 
	"h+" : this.getHours(), //hour 
	"m+" : this.getMinutes(), //minute 
	"s+" : this.getSeconds(), //second 
	"q+" : Math.floor((this.getMonth()+3)/3), //quarter 
	"S" : this.getMilliseconds() //millisecond 
	} 

	if(/(y+)/.test(format)) { 
		format = format.replace(RegExp.$1, (this.getFullYear()+"").substr(4 - RegExp.$1.length)); 
	} 

	for(var k in o) { 
		if(new RegExp("("+ k +")").test(format)) { 
			format = format.replace(RegExp.$1, RegExp.$1.length==1 ? o[k] : ("00"+ o[k]).substr((""+ o[k]).length)); 
		} 
	} 
	return format; 
} 
//数组去重
Array.prototype.unique = function () {
    return this.sort().join(",,").replace(/(,|^)([^,]+)(,,\2)+(,|$)/g,"$1$2$4").replace(/,,+/g,",").replace(/,$/,"").split(",");
}

Array.prototype.remove = function(index) { 
    if(!isNaN(index) && index <= this.length){
	    for(var i=0,n=0; i<this.length; i++){ 
	    	if(this[i] != this[index]){ 
	            this[n++]=this[i];
	        } 
	    } 
	    this.length -= 1;
    } 
} 

function pageHeight() {
	var winH = 673;//当前窗口的有效可视宽度和高度
	if (window.innerHeight) { //所有非IE浏览器
		winH = window.innerHeight;
	} else if (document.documentElement && document.documentElement.clientHeight) { //IE 6 Strict Mode
		winH = document.documentElement.clientHeight;
	} else if (document.body) { //其他浏览器
		winH = document.body.clientHeight;
	} 
	return winH;
};

function pageWidth() {
	var winW = 1166;//当前窗口的有效可视宽度和高度
	if (window.innerWidth) { //所有非IE浏览器
		winW = window.innerWidth;
	} else if (document.documentElement && document.documentElement.clientWidth) { //IE 6 Strict Mode
		winW = document.documentElement.clientWidth;
	} else if (document.body) { //其他浏览器
		winW = document.body.clientWidth;
	} 
	return winW;
};

//使用语法：passwordLevel(string)
//验证规则：数字、大写字母、小写字母、特殊字符
//函数结果：返回密码中包含的规则数
function passwordLevel(password) {
    var Modes = 0;
    for (i = 0; i < password.length; i++) {
        Modes |= CharMode(password.charCodeAt(i));
    }
    return bitTotal(Modes);
 
    //CharMode函数
    function CharMode(iN) {
        if (iN >= 48 && iN <= 57)//数字
            return 1;
        if (iN >= 65 && iN <= 90) //大写字母
            return 2;
        if ((iN >= 97 && iN <= 122) || (iN >= 65 && iN <= 90)) //大小写
            return 4;
        else
            return 8; //特殊字符
    }
 
    //bitTotal函数
    function bitTotal(num) {
        modes = 0;
        for (i = 0; i < 4; i++) {
            if (num & 1) modes++;
            num >>>= 1;
        }
        return modes;
    }
}


var browser={ 
	versions:function(){ 
		var u = navigator.userAgent, app = navigator.appVersion; 
		return { 
			trident: u.indexOf('Trident') > -1, //IE内核 
			presto: u.indexOf('Presto') > -1, //opera内核 
			webKit: u.indexOf('AppleWebKit') > -1, //苹果、谷歌内核 
			gecko: u.indexOf('Gecko') > -1 && u.indexOf('KHTML') == -1, //火狐内核 
			mobile: !!u.match(/AppleWebKit.*Mobile.*/)||!!u.match(/AppleWebKit/), //是否为移动终端 
			ios: !!u.match(/\(i[^;]+;( U;)? CPU.+Mac OS X/), //ios终端 
			android: u.indexOf('Android') > -1 || u.indexOf('Linux') > -1, //android终端或者uc浏览器 
			iPhone: u.indexOf('iPhone') > -1 || u.indexOf('Mac') > -1, //是否为iPhone或者QQHD浏览器 
			iPad: u.indexOf('iPad') > -1, //是否iPad 
			webApp: u.indexOf('Safari') == -1 //是否web应该程序，没有头部与底部 
		};
	},
	isPhone: function(){
		return browser.versions.mobile || browser.versions.ios || browser.versions.android  || browser.versions.iPhone || browser.versions.iPad || browser.versions.webApp;
	}
}
// 封装ajax
jQuery.ax=function(url, data, successfn, errorfn) {
    data = (data==null || data=="" || typeof(data)=="undefined")? {"date": new Date().getTime()} : data;
    $.ajax({
        type: "post",
        data: data,
        url: url,
        dataType: "json",
        success: function(d){
            successfn(d);
        },
        error: function(e){
            errorfn(e);
        }
    });
};
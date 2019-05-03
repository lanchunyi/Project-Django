/**
 * 
 */
var Constant = {
	SUCCESSED:"000000",
    ROLES:{
    	USER_ROLE_PD:"31",
    	USER_ROLE_PM:"32",
    	USER_ROLE_PL:"33",
    	USER_ROLE_TEAMER:"34",
    	USER_ROLE_MANAGER:"21"
    }
};

function showProgressbar(selector){
	$(selector).addClass("loading");
}


function hideProgressbar(selector){
	$(selector).removeClass("loading");
}
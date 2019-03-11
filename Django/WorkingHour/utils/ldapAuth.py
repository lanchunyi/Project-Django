'''
Created on 2019年1月23日

@author: Administrator
'''
import ldap
import sys
class ldapAuth(object):
    def __init__(self, username, passwd):
        self.username = username
        self.passwd = passwd
    def ldapconn(self):
        server = "ldap://18.217.217.28:389"
        rootDn = "dc=my-domain,dc=com"
        passwd = "test123"
        
        conn = ldap.initialize(server)
        conn.protocol_version = ldap.VERSION3
        conn.simple_bind(rootDn, passwd)
        
        scope = ldap.SCOPE_SUBTREE
        filter = "uid=" + self.username
        
        userid = conn.search(rootDn, scope, filter, None)
        re_type, re_data = conn.result(userid, 0, timeout=2)
        if(len(re_data)==0):
            print(u"没有获取到相应的用户信息！")
            return(False)
        print(str(re_data[0][1]['sn'][0],'utf-8') == self.username)
        print(re_data[0][0])
        userDn = re_data[0][0]
        conn.cancel(userid)
        
        conn = ldap.initialize(server)
        conn.protocol_version = ldap.VERSION3
        try:
            conn.simple_bind_s(userDn, self.passwd)
        except Exception as e:
            print(e)
            print(u"绑定DN出错！尝试simple_bin继续绑定！！！")
            try:
                conn.simple_bind(userDn, "12323")
            except Exception as ex:
                print(ex)
                print(u"尝试两次不同绑定后均失败，用户名密码不正确！！！")
                return(False)
                
        user_id = conn.search(userDn, scope)
        user_type, user_data = conn.result(user_id, 0)
        print(user_data)
        ps_code = user_data[0][1]['userPassword'][0]
        
        if(ps_code.decode(encoding="utf-8") == self.passwd):
            return(True)
        return(False)
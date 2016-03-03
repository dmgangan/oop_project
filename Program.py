import telnetlib
import time
f=open("myfile", 'w')


HOST = raw_input("Enter VSAT SAT IP: ")
print "\tVSAT SAT IP: ", HOST

#user = raw_input("Enter your remote account: ")
#print "\tUser: ", user

password = raw_input("Enter your password: ")
print "\tPassword", password
tn = telnetlib.Telnet(HOST, timeout=20)
tn.write(password)
tn.write('\r\n')
time.sleep(2)
tn.write('rsp board get telem')
tn.write('\r\n')
time.sleep(2)
op=tn.read_until("\r\n\r\n")
tn.close()
print op
f.write(op)
f.close()
i = raw_input("")






# import telnetlib
# import time

# HOST = raw_input("Enter VSAT SAT IP: ")
# print "\tVSAT SAT IP: ", HOST

# #user = raw_input("Enter your remote account: ")
# #print "\tUser: ", user

# password = raw_input("Enter your password: ")
# print "\tPassword", password
# tn = telnetlib.Telnet(HOST, timeout=20)
# tn.write(password)
# tn.write('\r\n')
# print "1"
# while True:
    # print "###########"
    # print tn.read_until("RCST-2000>")
    # command=raw_input(">")
    # tn.write(command)
    # tn.write('\r\n')
    # print tn.read_until("RCST-2000>")
# tn.close()
# i = raw_input("")

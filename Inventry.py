import paramiko
import sys
hostname = open("/media/selva/SELVA DATA/python/Selva Prog/set1/hostname",'r')
temp = open("/media/selva/SELVA DATA/python/Selva Prog/set1/output.pdf",'w')
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
print " "
for host_name in hostname:
   try:
  
       ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
       ssh.connect(host_name, 22, username='root', password='redhat')
       cmd = "uname -a"
       cmd1 = "cat /proc/cpuinfo |grep processor |wc -l" 
       cmd2 = "df -hT --total"
       cmd3 = "free -m -t"
       cmd0 = "hostname -i"

       stdin,stdout,stderr = ssh.exec_command(cmd0)
       output = stdout.readlines()
       old_stdout = sys.stdout
       sys.stdout = temp
       print("*" *80)  
       print "Host IP:"
       for line in output:
           print line
       sys.stdout=old_stdout
       stdin,stdout,stderr = ssh.exec_command(cmd)
       output = stdout.readlines()
       old_stdout = sys.stdout
       sys.stdout = temp
       print "Host Name:"
       print host_name
       print "OS Version:"
       for line in output:
           print line
       sys.stdout=old_stdout
       stdin,stdout,stderr = ssh.exec_command(cmd1)
       output = stdout.readlines()
       old_stdout = sys.stdout
       sys.stdout = temp
       print "No of Processor:"
       for line in output:
           print line
       sys.stdout=old_stdout
       stdin,stdout,stderr = ssh.exec_command(cmd2)
       output = stdout.readlines()
       old_stdout = sys.stdout
       sys.stdout = temp
       print "Disk Size:"
       for line in output:
           print line
       sys.stdout=old_stdout
       stdin,stdout,stderr = ssh.exec_command(cmd3)
       output = stdout.readlines()
       old_stdout = sys.stdout
       sys.stdout = temp
       print "Memory Size:"
       for line in output:
           print line

       sys.stdout=old_stdout

       ssh.close()
   except paramiko.SSHException:
       print "host %s connection failed" %host_name
temp.close()


ope = open("/media/selva/SELVA DATA/python/Selva Prog/set1/output")

print (ope.read())
ope.close()


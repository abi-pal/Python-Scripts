# VMAX_Details

symcli_path = '/opt/emc/SYMCLI/bin'

import os, sys, subprocess, shlex

from subprocess import Popen, PIPE

print ""

symm_id = raw_input("Enter serial number of VMAX array: ")

vmaxfile = open("vmax.txt", "w")

print ""

print "#" * 100
print ""

print "Details of VMAX Array %s" % symm_id

print ""
print "#" * 100

print ""

print ""

cmd1 = ["/opt/emc/SYMCLI/bin/symcfg", "-sid", symm_id, "list", "-v"]

op1 = subprocess.Popen(cmd1, stdout=subprocess.PIPE)

op_cmd1 = op1.communicate()[0]

print op_cmd1

print ""

print "#" * 100
print ""

print "List of FAST Policies on VMAX array %s" % symm_id

print ""
print "#" * 100

print ""

print ""

cmd2 = ["/opt/emc/SYMCLI/bin/symfast", "-sid", symm_id, "list", "-fp"]

op2 = subprocess.Popen(cmd2, stdout=subprocess.PIPE)

op_cmd2 = op2.communicate()[0]

print op_cmd2

print ""

print "#" * 100
print ""

print "Thin Pool Details on VMAX array %s" %symm_id

print ""
print "#" * 100

print ""

print ""

cmd3 = ["/opt/emc/SYMCLI/bin/symcfg", "-sid", symm_id, "list", "-thin", "-pool", "-GB"]

op3 = subprocess.Popen(cmd3, stdout=subprocess.PIPE)

op_cmd3 = op3.communicate()[0]

print op_cmd3

print ""

print "#" * 100
print ""

print "List Of Available LUN Addresses on FAs on VMAX array %s" %symm_id

print ""
print "#" * 100

print ""

print ""

cmd4 = ["/opt/emc/SYMCLI/bin/symcfg", "-sid", symm_id, "list", "-dir", "ALL", "-address", "-available"]

op4 = subprocess.Popen(cmd4, stdout=subprocess.PIPE)

op_cmd4 = op4.communicate()[0]

print op_cmd4

print "#" * 100
print ""

print "Saving the output of commands to file vmax.txt"

print ""
print "#" * 100

print ""

print ""

# print >>vmaxfile, op_cmd1, op_cmd2, op_cmd3, op_cmd4

vmaxfile.write("\n")
vmaxfile.write("#" * 100)
vmaxfile.write("\n")
vmaxfile.write("Details of VMAX Array %s" % symm_id)
vmaxfile.write("\n")
vmaxfile.write("#" * 100)
vmaxfile.write("\n")

print >>vmaxfile, op_cmd1

vmaxfile.write("\n")
vmaxfile.write("#" * 100)
vmaxfile.write("\n")
vmaxfile.write("List of FAST Policies on VMAX array %s" % symm_id)
vmaxfile.write("\n")
vmaxfile.write("#" * 100)
vmaxfile.write("\n")

print >>vmaxfile, op_cmd2

vmaxfile.write("\n")
vmaxfile.write("#" * 100)
vmaxfile.write("\n")
vmaxfile.write("Thin Pool Details on VMAX array %s" %symm_id)
vmaxfile.write("\n")
vmaxfile.write("#" * 100)
vmaxfile.write("\n")

print >>vmaxfile, op_cmd3

vmaxfile.write("\n")
vmaxfile.write("#" * 100)
vmaxfile.write("\n")
vmaxfile.write("List Of Available LUN Addresses on FAs on VMAX array %s" %symm_id)
vmaxfile.write("\n")
vmaxfile.write("#" * 100)
vmaxfile.write("\n")

print >>vmaxfile, op_cmd4

vmaxfile.close()

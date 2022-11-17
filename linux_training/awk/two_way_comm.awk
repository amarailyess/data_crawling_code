BEGIN{
cmd = "tr [a-z] [A-Z]"
print "hello world !!!" |& cmd
close(cmd, "to")

cmd |& getline out
print out;
close(cmd);
}

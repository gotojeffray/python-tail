import tail

def callback_function(line):
    print(line)
    if line.find("f5lb0") != -1 and  line.find("EAV exceeded") == -1 :
        if line.find('severity_label":"err') != -1 or line.find('severity_label":"crit') != -1 or line.find('severity_label":"alert') != -1 or  line.find('severity_label":"emerg') != -1:
            f = open('/tmp/f5.tag', 'w')
            f.write('F5: ERROR\n')
            f.close()
    else:
        pass


# Create a tail instance
t = tail.Tail('/data/output/syslog.log')

# Register a callback function to be called when a new line is found in the followed file.
# If no callback function is registerd, new lines would be printed to standard out.
t.register_callback(callback_function)

# Follow the file with 5 seconds as sleep time between iterations.
# If sleep time is not provided 1 second is used as the default time.
t.follow(s=5)

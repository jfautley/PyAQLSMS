#!/usr/bin/python
""" Command Line Interface to pyaqlSMS Module """
import optparse
import getpass
import aqlsms

def main():
    usage = """%prog [options] <destination> <message>"""

    op = optparse.OptionParser(usage=usage)
    op.add_option ("-u", "--username", dest="username", default=None,
                        help="Username for aql API")
    op.add_option ("-p", "--password", dest="password", default=None,
                        help="Password for aql API")
    op.add_option ("-i", "--interactive", action="store_true", default=False,
                        help="Prompt for username/password, if not specified")

    opts, args = op.parse_args()

    if len(args) < 2:
        op.error("Not enough arguments")

    if opts.interactive:
        while not opts.username:
            opts.username = raw_input ("AQL Username: ")
        while not opts.password:
            opts.password = getpass.getpass ("AQL Password (for %s): " % opts.username)

    destination = args.pop(0)
    message     = args.pop(0)

    print "Sending [%s] to [%s], using auth [%s]/[%s]" % (message, destination, opts.username, opts.password)

if __name__ == "__main__":
    main()


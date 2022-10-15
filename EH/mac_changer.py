import subprocess
import optparse
import re

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface")
    parser.add_option("-m", "--mac", dest="new_mac", help="New Mac")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[-] Interfaces Empty")
    elif not options.new_mac:
        parser.error("[-] New Mac Empty")
    return options

def change_mac(interface, new_mac):
    print ("[+] Adater Down ... ")
    subprocess.call(["ifconfig", interface, "down"])
    print ("[+] Adater Change Mac ... " + new_mac)
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    print("[+] Adater Up ...")
    subprocess.call(["ifconfig", interface, "up"])

def get_current_mac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", interface])
    mac_address_search_result = re.search(r'\w\w:\w\w:\w\w:\w\w:\w\w:\w\w', ifconfig_result.decode("utf-8"))
    if mac_address_search_result:
        return (mac_address_search_result.group(0))
    else:
        print ("[-] Search No Result Mac")

options = get_arguments()
get_mac = get_current_mac(options.interface)
print ("Current Mac: " + str(get_mac))
change_mac(options.interface, options.new_mac)
get_mac = get_current_mac(options.interface)
if get_mac == options.new_mac:
    print ("Mac Change: " + options.new_mac)
else:
    print ("Mac No Change")

from scapy.all import *  # noqa: F403
def main():
    print(r"""
************************************************************
*  ░█▀█░█▀█░█▀▀░█░█░█▀▀░▀█▀░░░█▀▀░█▀█░▀█▀░█▀▀░█▀▀░█▀▀░█▀▄  *
*  ░█▀▀░█▀█░█░░░█▀▄░█▀▀░░█░░░░▀▀█░█░█░░█░░█▀▀░█▀▀░█▀▀░█▀▄  *
*  ░▀░░░▀░▀░▀▀▀░▀░▀░▀▀▀░░▀░░░░▀▀▀░▀░▀░▀▀▀░▀░░░▀░░░▀▀▀░▀░▀  *
************************************************************
""")
    while True:
        choice = input("\n\n[1]. Basic Packet Sniff\n[2]. Packet Sniff with hex dump Print\n[3]. Packet sniff with capture file storage\n[4]. Exit\nChoose : ")
        try:
            if choice == "1":
                print("Press `ctrl + c` to stop the packet capturing")
                pkt = sniff()
                print(pkt.summary(),"\n" ,pkt)
            elif choice == "2":
                print("Press `ctrl + c` to stop the packet capturing")
                pkt = sniff()
                print(pkt, pkt.hexdump())
            elif choice == "3":
                print("Press `ctrl + c` to stop the packet capturing")
                pkt = sniff()
                cap_file_path = input("Enter the location to store the packet capture file : ")
                print("The file name will be 'capture001.pcap' in the given location.")
                wrpcap(cap_file_path+"/capture001.pcap", pkt)
            elif choice == "4":
                print("\nExiting...")
                exit()
            else:
                print("Invalid choice!!! , Try again")
        except KeyboardInterrupt:
            print("Packet sniffing completed!!!\n\n\n")

if __name__ == "__main__":
    main()

Generate Microsoft Azure ip addresses list that can be imported in Mikrotik routers.

Example Mikrotik Script:

	/tool fetch url="https://raw.githubusercontent.com/aurelmarius/mikrotik-azure/main/azure-ips.rsc" mode=https;
	:log info "Downloaded Azure Ip Range";
	:delay 3;
	/ip firewall address-list remove [find where list="Azure"];
	:delay 10;
	:log info "Importing Azure IPs";
	/import file-name=azure-ips.rsc;
	:log info "Updated Azure IPs"; X




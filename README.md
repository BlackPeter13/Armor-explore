# Armor-explorer
working Armor explorer for Armor-network pools
Tested on Ubuntu 18.4 Server
have installed nginx

To make it work you need to install first some dependencies:
install python3
install php
chmod +x rpc_request.py


Next step is to create a folder in your www root folder and name it AMX-explorer.
Copy this files to that folder.


Next step is to modify in the pool the config.js file this two lines acording with your ip or domain name
 "blockchainExplorer": "http://***.***.***.***/AMX-explorer/index.php?search={id}"
 "transactionExplorer": "http://***.***.***.***/AMX-explorer/index.php?search={id}"
 

The last step is launching the pool andnow you have acces to the block explorer from the web interface of 
the pool or accesing it by http://***.***.***.***/AMX-explorer/
 
 A big thanks goes to @vitik

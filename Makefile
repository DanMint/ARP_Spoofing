SHELL := /bin/bash

host-discover:
	@mkdir ./outputs
	@echo "netdiscover_ips can run for a long time... you can either wait or crl+c to get all of the captured hosts"
	python3 src/netdiscover_ips.py
	python3 src/foramt_netdiscover.py

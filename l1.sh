#!/usr/bin/env bash
clear
trap "echo oh;exit" SIGTERM SIGINT



while true
do
	echo "NEW ..............."
	timeout 5m python3 visa_v1_stan.py
done

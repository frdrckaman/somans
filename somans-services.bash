#!/bin/bash

sudo setenforce 0
sudo systemctl restart gunicorn-somans.socket gunicorn-somans.service
sudo setenforce 1

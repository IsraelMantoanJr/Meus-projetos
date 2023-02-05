#!/bin/bash
killall conky
sleep 10 && conky -c ~/.conky/meu_conky/conkyrc;
exit 0

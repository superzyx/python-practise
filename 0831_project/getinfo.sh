#!/usr/bin/env bash
#
# author: superzyx
# date: 2019/08/28
# usage: get server cpuinof, memoryinfo, diskinfo


us=$(vmstat | awk 'NR==3{print $13}')
sy=$(vmstat | awk 'NR==3{print $14}')
cpu_info=$(echo "${us}+${sy}" | bc -ql)
if [ $? -ne 0 ];then
    yum -y install bc
    cpu_info=$(echo "${us}+${sy}" | bc -ql)
fi

use=$(free -mw | awk 'NR==2{print $3}')
cache=$(free -mw | awk 'NR==2{print $7}')
total=$(free -mw | awk 'NR==2{print $2}')
memory_info=$(echo "((${use}+${cache})/${total})*100" | bc -ql)
if [ $? -ne 0 ];then
    yum -y install bc
    memory_info=$(echo "((${use}+${cache})/${total})*100" | bc -ql)
fi

disk_info=$(df -Th | awk 'NR==2{print $6}')
date=$(date +'%Y-%m-%d-%H-%M-%S')
datetime=$(date + '%Y%m%d%H%M%S')
echo "${date} ${HOSTNAME} ${cpu_info}% ${memory_info}% ${disk_info}" >>/mnt/server.log

if  [ $(du -sh /mnt/server.log | awk '{print $1}') == '2M' ];then
    mv /mnt/server.log /mnt/server.${datetime}.log
fi





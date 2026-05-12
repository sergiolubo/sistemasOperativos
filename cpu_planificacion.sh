#!/bin/bash

echo "Creando procesos intensivos en CPU..."

yes > /dev/null &
P1=$!

yes > /dev/null &
P2=$!

yes > /dev/null &
P3=$!

sleep 2

echo
echo "Estado inicial de procesos:"
ps -o pid,ppid,ni,pri,pcpu,state,comm -p $P1,$P2,$P3

echo
echo "Modificando prioridad del proceso $P1..."
renice 10 -p $P1

sleep 2

echo
echo "Estado después del cambio de prioridad:"
ps -o pid,ppid,ni,pri,pcpu,state,comm -p $P1,$P2,$P3

echo
echo "Finalizando procesos..."
kill $P1 $P2 $P3

sleep 1

echo
echo "Verificación final:"
ps -o pid,ppid,ni,pri,pcpu,state,comm -p $P1,$P2,$P3

echo
echo "Práctica finalizada."

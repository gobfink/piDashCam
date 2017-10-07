#!/bin/bash

usage() { echo "Usage: $0 [-Y Year : <1970+>[-M Month : <1 - 12> ] [-d day <1-31>] [-h hour <0-23> ] [-m minute <0-59>] [-s second <0-59>]" 1>&2; exit 1; }

Y=-1
M=-1
d=-1
h=-1
m=-1
s=-1

while getopts ":Y:M:d:h:m:s:" o; do
    case "${o}" in
		Y)
			Y=${OPTARG}
			(( Y > 1970 )) || usage
			;;
		M)  
			M=${OPTARG}
			(( M >= 1 || M <= 12)) || usage
			;;
		d)  
			d={OPTARG}
			(( d >=1 || d <= 31 )) || usage
			;;
		h)  
			h={OPTARG}
			(( h >= 0 || h <= 23 )) || usage
			;;
        m)  
            m=${OPTARG}
            (( m >= 0 || m <= 59 )) || usage
            ;;
		s)  
            s=${OPTARG}
            (( s >= 0 || s <= 59 )) || usage
            ;;
        *)
            usage
            ;;
    esac
done
shift $((OPTIND-1))

echo "Y = ${Y}"
echo "M = ${M}"
echo "d = ${d}"
echo "h = ${h}"
echo "m = ${m}"
echo "s = ${s}"


echo "s = ${s}"
echo "p = ${p}"
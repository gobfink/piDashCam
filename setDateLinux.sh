#! /bin/bash

usage() { echo "Usage: $0 [-Y Year : <1970+> [-M Month : <1 - 12> ] [-d day <1-31>] [-h hour <0-23> ] [-m minute <0-59>] [-s second <0-59>]" 1>&2; exit 1; }

declare -A timeArray

timeArray[second]=0

while getopts ":Y:M:d:h:m:s:" o; do
    case "${o}" in
		Y)
			timeArray[Year]=${OPTARG}
			(( timeArray[Year] > 1970 )) || usage
			;;
		M)  
			timeArray[Month]=${OPTARG}
			(( timeArray[Month] >= 1 || timeArray[Month] <= 12)) || usage
			;;
		d)  
			timeArray[Day]=${OPTARG}
			(( timeArray[Day] >=1 || timeArray[Day] <= 31 )) || usage
			;;
		h)  
			timeArray[hour]=${OPTARG}
			(( timeArray[hour] >= 0 || timeArray[hour] <= 23 )) || usage
			;;
       		m)  
       			timeArray[minute]=${OPTARG}
			(( timeArray[minute] >= 0 || timeArray[minute] <= 59 )) || usage
			;;
		s)  
			timeArray[second]=${OPTARG}
			(( timeArray[seccond] >= 0 || timeArray[second] <= 59 )) || usage
			 ;;
       		*)
			usage
			;;
    esac
done
shift $((OPTIND-1))

date_format="+"
time_format=
time_value=""
value=""

for key in ${!timeArray[@]}; do
    echo ${key} ${timeArray[${key}]}
    value=$value${timeArray[${key}]}
    case $key in
    Year)
      this_format=Y 
      ;;
    Month)
      this_format=m
      ;;
    Day)
      this_format=d
      ;;
    esac
    if (( timeArray[${key}]} < 10 )) ; then
      timeArray[${key}]=0$timeArray[${key}]
    fi

    format_string=$format_string%
    format_string=$format_string$this_format
done

[ ${timeArray[hour]+a} ] && [ ${timeArray[minute]+b} ]  && time_value=${timeArray[hour]}:${timeArray[minute]}:${timeArray[second]}

echo "format_string: $format_string "
echo "value: $value "

cmd="date $format_string -s \"$value\""

echo "$cmd"

$cmd




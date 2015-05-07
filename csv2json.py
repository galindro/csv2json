#!/usr/bin/python
import csv, json, argparse, sys

result = {}
result_data = []

# Command line parsing
parser = argparse.ArgumentParser(description='Convert CSV to JSON')

parser.add_argument('-f','--fieldnames',
					help='Field names')

parser.add_argument('-z','--zabbix',
					action="store_true",
					help='Format result for Zabbix LLD')

parser.add_argument('csvfile',
					nargs='?',
					type=argparse.FileType('r'),
					default=sys.stdin)

args = parser.parse_args()

if args.fieldnames:
	reader = csv.DictReader(args.csvfile, args.fieldnames.split(','))
else:
	reader = csv.DictReader(args.csvfile)

if args.zabbix:

	for row in reader:
		new_key = ""

		for key, value in row.items():
				new_key = "{#%s}" % (key)
				row[new_key] = row.pop(key)
		result_data.append(row)

	result["data"] = result_data

else:
	for row in reader:
		result_data.append(row)
	
	result = result_data

print json.dumps(result, indent=4)


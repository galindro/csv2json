# csv2json
Script to convert csv to json

# Help

```bash
usage: csv2json.py [-h] [-f FIELDNAMES] [-z] [csvfile]

Convert CSV to JSON

positional arguments:
  csvfile

optional arguments:
  -h, --help            show this help message and exit
  -f FIELDNAMES, --fieldnames FIELDNAMES
                        Field names
  -z, --zabbix          Format result for Zabbix LLD
```

#Examples

* Convert a command line output with field names:

```bash
$ zpool list -o name | awk '{$1=$1}1' OFS="," |csv2json.py
[
    {
        "NAME": "datastore"
    }
]
```

* Convert a command line output with field names and output result in Zabbix LLD format:

```bash
$ zpool list -o name | awk '{$1=$1}1' OFS="," |csv2json.py -z
{
    "data": [
        {
            "{#NAME}": "datastore"
        }
    ]
}
```

* Convert a command line output without field names:
```bash
$ zpool list -H -o name | awk '{$1=$1}1' OFS="," |csv2json.py -z -f NAME
{
    "data": [
        {
            "{#NAME}": "datastore"
        }
    ]
}

```

#License

GNU GENERAL PUBLIC LICENSE Version 2, June 1991

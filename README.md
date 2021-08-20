# change-env

This is use for changing the `.env` file, please put this into the same directory as the `.env` file.

## Indicate `.env` path

If the path is missing, it is default to set in the same directory.

```bash
$ python3 change-env.py -f <your_path> ...
```

## Change key name

```bash
$ python3 change-env.py -k <key_to_be_change>,<new_key_name>
```

example:
```bash
$ python3 change-env.py -k account,my_bank_account
```

## Change key's value

```bash
$ python3 change-env.py -v <key_name>,<new_value>
```

example:
```bash
$ python3 change-env.py -v account_password,iamhandsome
```

## Append new line

```bash
$ python3 change-env.py -a <new_line>
```

example:
```bash
$ python3 change-env.py -a my_password=123456
```

## Delete a key

```bash
$ python3 change-env.py -d <key_name>
```

example:
```bash
$ python3 change-env.py -d my_password
```
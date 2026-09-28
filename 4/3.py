config_values = {
    'app_name': 'NextGen',
    'version': '1.0.0',
    'debug': True,
    'db_host': 'localhost',
    'db_port': 5432,
    'db_name': 'my_database',
    'db_user': 'admin',
    'db_password': 'secret123',
    'api_key': 'ak_123456789',
    'api_secret': 'sk_987654321',
    'base_url': 'https://api.example.com',
    'log_file': '/var/log/app.log',
    'data_dir': '/opt/app/data',
    'temp_dir': '/tmp/app',
    'max_workers': 10,
    'timeout': 30,
    'retry_attempts': 3
}

input_file = "config_default.txt"
output_file = "config.txt"

with open(input_file, "r", encoding="utf-8") as f_in, open(output_file, "w", encoding="utf-8") as f_out:
    for line in f_in:
        if "= ?" in line:
            key_part = line.split("=")[0].strip()
            if key_part in config_values:
                value = config_values[key_part]
                if isinstance(value, str):
                    formatted_value = f'"{value}"'
                elif isinstance(value, bool):
                    formatted_value = str(value)
                else:
                    formatted_value = str(value)
                new_line = line.replace("= ?", f"= {formatted_value}")
                f_out.write(new_line)
            else:
                f_out.write(line)
        else:
            f_out.write(line)

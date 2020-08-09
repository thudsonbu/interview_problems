# Create a function that takes a URL (string), removes duplicate query parameters 
# and parameters specified within the 2nd argument (which will be an optional list).

def strip_url_params(url, *args):
    params_to_strip = []
    for param in args:
        params_to_strip += param
    start_of_params = url.find("?")
    if start_of_params > -1:
        param_substring = url[(start_of_params+1)::]
        param_statements = param_substring.split("&")
        param_dictionary = {}
        for statement in param_statements:
            split_statement = statement.split("=")
            param_name = split_statement[0]
            param_value = split_statement[1]
            if param_name not in params_to_strip:
                param_dictionary[param_name] = param_value
        url_without_params = url[0:start_of_params+1]
        for param, value in param_dictionary.items():
            url_without_params += "" + param + "=" + value + "&"
        return url_without_params[0:-1]
    else:
        return url

print(strip_url_params("https://edabit.com?a=1&b=2&a=2"))
print(strip_url_params("https://edabit.com?a=1&b=2&a=2", ["b"]))
print(strip_url_params("https://edabit.com", ["b"]))
def http_status(status):
    match status:
        case 100:
            return "Ok"
        case 200:
            return "Not found"
        case 300:
            return "Internal server error"
        case _:
            return "Unknown status" 
# Usage
print(http_status(300)) 

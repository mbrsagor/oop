def create_use_validation(attrs):
    if len(attrs.get('password')) <= 7:
        return "Password should be minimum 8 charters"
    elif len(attrs.get('password2')) <= 7:
        return "Confirm Password should be minimum 8 charters"
    else:
        pass
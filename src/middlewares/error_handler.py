def error_handler(func: object) -> object:
    async def wrapper(*args, **kwargs) -> object:
        try:
            return await func(*args, **kwargs)
        except Exception as ex:
            print('ex:', ex)
    return wrapper

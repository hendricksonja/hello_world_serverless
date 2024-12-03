def main(args):
    """
    A simple serverless function that returns a greeting message.

    Args:
        args (dict): A dictionary of input arguments (e.g., query parameters or JSON payload).

    Returns:
        dict: A dictionary containing the 'body' of the response.
    """
    # Get the 'name' parameter from the input arguments
    name = args.get("name", "World")

    # Return the greeting message
    return {
        "body": f"Hello, {name}!"
    }

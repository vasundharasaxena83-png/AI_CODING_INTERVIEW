import sys
import io
import contextlib

def run_python_code(user_code, input_data=None):
    """
    Executes user Python code safely (MVP sandbox).
    """

    output_buffer = io.StringIO()

    try:
        with contextlib.redirect_stdout(output_buffer):
            exec(user_code, {"input_data": input_data})

        output = output_buffer.getvalue().strip()

        return {
            "success": True,
            "output": output
        }

    except Exception as e:
        return {
            "success": False,
            "output": str(e)
        }
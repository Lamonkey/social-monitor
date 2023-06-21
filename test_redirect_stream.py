import contextlib
import io

# Create an io.StringIO object to capture the output
output_buffer = io.StringIO()

# Define your stream of data (replace this with your actual stream)
data_stream = ['Line 1', 'Line 2', 'Line 3']

# Use redirect_stdout to redirect the output to the output_buffer
with contextlib.redirect_stdout(output_buffer):
    while(True):
        for line in data_stream:
            print(line)  # Process each line of the stream

# Get the captured output from the buffer
captured_output = output_buffer.getvalue()

# Print the captured output
print(captured_output)

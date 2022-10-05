import os
from flask import Flask, abort, request, Response

from utils import file_reader, args_reader, commands_checker, command_processor


app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")


@app.post("/perform_query/")
def perform_query() -> Response:
    cmd1, value1, cmd2, value2, file_name = args_reader(**request.args)

    commands_checker(cmd1, cmd2)

    file_path = os.path.join(DATA_DIR, file_name)
    if not os.path.isfile(file_path):
        abort(404, 'File not found')
    file_gen = file_reader(file_path)

    executing_result = command_processor(cmd1, value1, cmd2, value2, file_gen)

    return app.response_class('\n'.join(executing_result), content_type="text/plain")

if __name__ == '__main__':
    app.run(port=5001)

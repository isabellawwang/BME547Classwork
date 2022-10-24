# server.py
from flask import Flask, request, jsonify


app = Flask(__name__)


@app.route("/", methods=["GET"])
def server_status():
    return "Server is on."


@app.route("/info", methods=["GET"])
def information():
    x = "This website will calculate blood cholesterol levels.\n"
    x += "It is written by Isabella Wang."
    return x


@app.route("/hdl_check", methods=["POST"])
def hdl_check_from_internet():
    """
        incoming_json = {"name": <name_str>,
                         "hdl_value": <hdl_value_int>}
    """
    from blood_calculator import check_HDL
    in_data = request.get_json()
    hdl_value = in_data["hdl_value"]
    print("The received HDL xsvalue was {}.".format(hdl_value))
    answer = check_HDL(hdl_value)
    return answer


@app.route("/add_numbers", methods=["POST"])
def add_numbers():
    """
        incoming_json = {"a": <float>,
                          "b": <float>}
    """
    in_data = request.get_json()
    first_num = in_data["a"]
    second_num = in_data["b"]
    sum = first_num + second_num
    print(f"The received numbers were {first_num} and {second_num}.")
    answer = "The sum is {}".format(sum)
    return jsonify(answer)  # jsonify is best practice for outputs in general


@app.route("/add/<a>/<b>", methods=["GET"])
def add_variable_url(a, b):
    answer = int(a) + int(b)
    return jsonify(answer)


if __name__ == "__main__":
    app.run()

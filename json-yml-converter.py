from flask import Flask, request, render_template_string
import json
import yaml

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        input_data = request.form["input"]
        conversion = request.form["conversion"]
        output_data = ""

        if conversion == "json_to_yaml":
            try:
                json_data = json.loads(input_data)
                output_data = yaml.dump(json_data)
            except:
                output_data = "Invalid JSON input"
        else:
            try:
                yaml_data = yaml.safe_load(input_data)
                output_data = json.dumps(yaml_data, indent=2)
            except:
                output_data = "Invalid YAML input"

        return render_template_string(html_template, output=output_data)

    return render_template_string(html_template, output="")

html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>JSON-YAML Converter</title>
</head>
<body>
    <h1>JSON-YAML Converter</h1>
    <form method="post">
        <textarea name="input" rows="10" cols="50"></textarea>
        <br>
        <input type="radio" id="jsonToYaml" name="conversion" value="json_to_yaml">
        <label for="jsonToYaml">Convert JSON to YAML</label><br>
        <input type="radio" id="yamlToJson" name="conversion" value="yaml_to_json">
        <label for="yamlToJson">Convert YAML to JSON</label><br>
        <input type="submit" value="Convert">
    </form>
    <br>
    <textarea readonly rows="10" cols="50">{{ output }}</textarea>
</body>
</html>
"""

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

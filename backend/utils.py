from flask import jsonify


def better_jsonify(data):
  if isinstance(data, list):
    return jsonify([o.to_dict() for o in data])

  return jsonify(data.to_dict())

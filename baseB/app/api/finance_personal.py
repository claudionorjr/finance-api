from flask import jsonify, request, current_app, url_for
from . import api

# TODO: Função não implementada
@api.route("register/financePersonal", methods=['POST'])
def register_finance_personal():
    if request.method == "POST":
        print(request.json)
        jsonify({"ok" : "success save"})
    return jsonify({"error" : "fail save"})

# TODO: Função não implementada
@api.route("/all/info")
def get_all_info_finance_personal():
    return ""

# TODO: Função não implementada
@api.route("/cpf/info/<cpf>")
def get_info_by_cpf(cpf):
    return ""
from flask import Flask, jsonify, request
import dataAnalysis as da
from flask_cors import CORS
from collections import OrderedDict

app = Flask(__name__)
CORS(app)

@app.route('/data', methods=['GET'])
def get_data():
    # 参数接收
    page = request.args.get('page', default=1, type=int)
    per_page = request.args.get('per_page', 10, type=int)
    company = request.args.get('company', default='default', type=str)
    change_period = request.args.get('change_period', default='今日', type=str)
    change = request.args.get('change', default=9, type=int)
    sort_period = request.args.get('sort_period', default='今日', type=str)
    sort = request.args.get('sort', default='ranking', type=str)
    # 升降序 默认降序
    ascending = request.args.get('ascending', default=False)
    ascending = ascending in ['True']
    # print(ascending)

    # 页码设置
    start = (page - 1) * per_page
    end = start + per_page

    # 查询公司类型
    if company == 'default':
        data = da.query_default()
    elif company == 'st':
        data = da.query_st()
    elif company == 'suspend':
        data = da.query_suspend()
    else:
        return jsonify({"error_company": "Invalid sort type"}), 400

    # 筛选涨跌
    data = da.query_change(data, change_period, change)

    # 排序
    if sort == 'ranking':
        data = da.sort_ranking(data, sort_period, ascending)
    elif sort == 'change':
        data = da.sort_change(data, sort_period, ascending)
    elif sort == 'main_inflow':
        data = da.sort_main_inflow(data, sort_period, ascending)
    else:
        return jsonify({"error_sort": "Invalid sort type"}), 400

    # 切片当前页数据 并转字典
    paginated_data = data[start:end].to_dict('records')


    # 返回json
    return jsonify({
        "total": len(da.query_default()),
        "now_total": len(data),
        "page": page,
        "per_page": per_page,
        "data": paginated_data
    })

@app.route('/company_class_info', methods=['GET'])
def get_company_class_info():
    data = da.analysis_company_class_data().to_dict()
    info = da.analysis_company_class_info().to_dict()
    above_mean = da.analysis_company_class_above_mean().to_dict()
    below_mean = da.analysis_company_class_below_mean().to_dict()

    print(above_mean)

    # 返回json
    return jsonify({
        "total": len(data),
        "info": info,
        "above_mean": above_mean,
        "below_mean": below_mean,
        "data": data
    })

@app.route('/company_class_index', methods=['GET'])
def get_company_class_index():
    start = request.args.get('start', default=0, type=int)
    end = request.args.get('end', default=0, type=int)

    data = da.get_company_class_index(start, end).to_dict()

    return jsonify({
        'data': data
    })

if __name__ == '__main__':
    app.run(debug=True)


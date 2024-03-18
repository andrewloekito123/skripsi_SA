from flask import Flask, jsonify, request, render_template
from connection import sql_connection
from flask_cors import CORS
from collections import OrderedDict
import json
from decimal import Decimal
from array import array

app = Flask(__name__)
CORS(app)

@app.route('/api/ingredients', methods=['GET'])
def get_all_ingredients():
    db_connection, cursor = sql_connection() 
    select_query = "SELECT * FROM bahan_makanan"
    cursor.execute(select_query)
    results = cursor.fetchall()
    cursor.close()
    db_connection.close()
    return jsonify(results)

@app.route('/api/layers', methods=['GET'])
def get_ingredient():
    db_connection, cursor = sql_connection()
    select_query = "SELECT * FROM Layer_phase"
    cursor.execute(select_query)
    results = cursor.fetchall()
    cursor.close()
    db_connection.close()
    return jsonify(results)

@app.route('/api/update_status', methods=['POST'])
def update_status():
    try:
        data = request.get_json()
        product_id = data.get('productId')
        new_value = data.get('newValue')
        db_connection, cursor = sql_connection()
        update_query = "UPDATE bahan_makanan SET status = %s WHERE id = %s"
        cursor.execute(update_query, (new_value, product_id))
        db_connection.commit()
        cursor.close()
        db_connection.close()

        return jsonify({'message': 'Status updated successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/ingredients/<int:id>', methods=['GET'])
def get_ingredient_by_id(id):
    try:
        db_connection, cursor = sql_connection()
        select_query = "SELECT * FROM bahan_makanan WHERE id = %s"
        cursor.execute(select_query, (id,))
        results = cursor.fetchone()
        cursor.close()
        db_connection.close()

        if results:
            results = list(map(lambda x: str(x) if isinstance(x, Decimal) else x, results))
            attributes = OrderedDict([
                ("id", results[0]),
                ("name", results[1]),
                ("cost" , results[2]),
                ("Min" , results[3]),
                ("Max" , results[4]),
                ("Weight" , results[5]),
                ("DM" , results[6]),
                ("ME" , results[7]),
                ("Crude Protein" , results[8]),
                ("True Protein" , results[9]),
                ("EE" , results[10]),
                ("CF" , results[11]),
                ("Ca" , results[12]),
                ("Total P" , results[13]),
                ("Avail P" , results[14]),
                ("CaP" , results[15]),
                ("Na" , results[16]),
                ("Cl" , results[17]),
                ("Choline" , results[18]),
                ("Folate" , results[19]),
                ("dLYS" , results[20]),
                ("dMET" , results[21]),
                ("dTSAA" , results[22]),
                ("dTHR" , results[23]),
                ("dTRP" , results[24]),
                ("dARG" , results[25]),
                ("dVAL" , results[26]),
                ("status", results[27])
            ])
            json_attributes = json.dumps(attributes)
            return json_attributes, 200, {'Content-Type': 'application/json'}
           
        else:
            return jsonify({"error": "Ingredient not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/ingredients/actives', methods=['get'])
def get_all_active_ingredients():
    db_connection, cursor = sql_connection() 
    select_query = "SELECT * FROM bahan_makanan where status = 1"
    cursor.execute(select_query)
    results = cursor.fetchall()
    cursor.close()
    db_connection.close()
    if results:
        names = [result[1] for result in results]
        return jsonify(names)
    else:
        return jsonify([])

def calculate_ME():
        db_connection, cursor = sql_connection() 
        select_query = "SELECT ME, name_product FROM bahan_makanan WHERE status = 1"
        cursor.execute(select_query)
        results = cursor.fetchall()
        valid_results = [float(result[0]) for result in results if result[0] is not None]
        total_ME = sum(valid_results)
        ingredients = [result[1] for result in results]
        cursor.close()
        db_connection.close()
        return [total_ME]

def calculate_CP():
    db_connection, cursor = sql_connection() 
    select_query = "select Crude_Protein, name_product from bahan_makanan where status = 1"
    cursor.execute(select_query)
    results = cursor.fetchall()
    valid_results = [float(result[0]) for result in results if result[0] is not None]
    total_CP = sum(valid_results)
    cursor.close()
    db_connection.close()
    return [total_CP]

def calculate_TP():
    db_connection, cursor = sql_connection() 
    select_query = "select True_Protein, name_product from bahan_makanan where status = 1"
    cursor.execute(select_query)
    results = cursor.fetchall()
    valid_results = [float(result[0]) for result in results if result[0] is not None]
    total_TP = sum(valid_results)
    cursor.close()
    db_connection.close()
    return [total_TP]

def calculate_EE():
    db_connection, cursor = sql_connection() 
    select_query = "select EE, name_product from bahan_makanan where status = 1"
    cursor.execute(select_query)
    results = cursor.fetchall()
    valid_results = [float(result[0]) for result in results if result[0] is not None]
    total_EE = sum(valid_results)
    cursor.close()
    db_connection.close()
    return [total_EE]

def calculate_CF():
    db_connection, cursor = sql_connection() 
    select_query = "select CF, name_product from bahan_makanan where status = 1"
    cursor.execute(select_query)
    results = cursor.fetchall()
    valid_results = [float(result[0]) for result in results if result[0] is not None]
    total_CF = sum(valid_results)
    cursor.close()
    db_connection.close()
    return [total_CF]

def calculate_Ca():
    db_connection, cursor = sql_connection() 
    select_query = "select Ca, name_product from bahan_makanan where status = 1"
    cursor.execute(select_query)
    results = cursor.fetchall()
    valid_results = [float(result[0]) for result in results if result[0] is not None]
    total_Ca = sum(valid_results)
    cursor.close()
    db_connection.close()
    return [total_Ca]

def calculate_TotalP():
    db_connection, cursor = sql_connection() 
    select_query = "select Total_P, name_product from bahan_makanan where status = 1"
    cursor.execute(select_query)
    results = cursor.fetchall()
    valid_results = [float(result[0]) for result in results if result[0] is not None]
    total_Total_P = sum(valid_results)
    cursor.close()
    db_connection.close()
    return [total_Total_P]

def calculate_AvailP():
    db_connection, cursor = sql_connection() 
    select_query = "select Avail_P, name_product from bahan_makanan where status = 1"
    cursor.execute(select_query)
    results = cursor.fetchall()
    valid_results = [float(result[0]) for result in results if result[0] is not None]
    total_Avail_P = sum(valid_results)
    cursor.close()
    db_connection.close()
    return [total_Avail_P]

def calculate_CaP():
    db_connection, cursor = sql_connection() 
    select_query = "select CaP, name_product from bahan_makanan where status = 1"
    cursor.execute(select_query)
    results = cursor.fetchall()
    valid_results = [float(result[0]) for result in results if result[0] is not None]
    total_CaP = sum(valid_results)
    cursor.close()
    db_connection.close()
    return [total_CaP]

def calculate_Na():
    db_connection, cursor = sql_connection() 
    select_query = "select Na, name_product from bahan_makanan where status = 1"
    cursor.execute(select_query)
    results = cursor.fetchall()
    valid_results = [float(result[0]) for result in results if result[0] is not None]
    total_Na = sum(valid_results)
    cursor.close()
    db_connection.close()
    return [total_Na]

def calculate_Cl():
    db_connection, cursor = sql_connection() 
    select_query = "select Cl, name_product from bahan_makanan where status = 1"
    cursor.execute(select_query)
    results = cursor.fetchall()
    valid_results = [float(result[0]) for result in results if result[0] is not None]
    total_Cl = sum(valid_results)
    cursor.close()
    db_connection.close()
    return [total_Cl]

def calculate_Choline():
    db_connection, cursor = sql_connection() 
    select_query = "select Choline, name_product from bahan_makanan where status = 1"
    cursor.execute(select_query)
    results = cursor.fetchall()
    valid_results = [float(result[0]) for result in results if result[0] is not None]
    total_Choline = sum(valid_results)
    cursor.close()
    db_connection.close()
    return [total_Choline]

def calculate_Folate():
    db_connection, cursor = sql_connection() 
    select_query = "select Folate, name_product from bahan_makanan where status = 1"
    cursor.execute(select_query)
    results = cursor.fetchall()
    valid_results = [float(result[0]) for result in results if result[0] is not None]
    total_Folate = sum(valid_results)
    cursor.close()
    db_connection.close()
    return [total_Folate]

def calculate_dLYS():
    db_connection, cursor = sql_connection() 
    select_query = "select dLYS, name_product from bahan_makanan where status = 1"
    cursor.execute(select_query)
    results = cursor.fetchall()
    valid_results = [float(result[0]) for result in results if result[0] is not None]
    total_dLYS = sum(valid_results)
    cursor.close()
    db_connection.close()
    return [total_dLYS]

def calculate_dMET():
    db_connection, cursor = sql_connection() 
    select_query = "select dMET, name_product from bahan_makanan where status = 1"
    cursor.execute(select_query)
    results = cursor.fetchall()
    valid_results = [float(result[0]) for result in results if result[0] is not None]
    total_dMET = sum(valid_results)
    cursor.close()
    db_connection.close()
    return [total_dMET]

def calculate_dTSAA():
    db_connection, cursor = sql_connection() 
    select_query = "select dTSAA, name_product from bahan_makanan where status = 1"
    cursor.execute(select_query)
    results = cursor.fetchall()
    valid_results = [float(result[0]) for result in results if result[0] is not None]
    total_dTSAA = sum(valid_results)
    cursor.close()
    db_connection.close()
    return [total_dTSAA]

def calculate_dTHR():
    db_connection, cursor = sql_connection() 
    select_query = "select dTHR, name_product from bahan_makanan where status = 1"
    cursor.execute(select_query)
    results = cursor.fetchall()
    valid_results = [float(result[0]) for result in results if result[0] is not None]
    total_dTHR = sum(valid_results)
    cursor.close()
    db_connection.close()
    return [total_dTHR]

def calculate_dTRP():
    db_connection, cursor = sql_connection() 
    select_query = "select dTRP, name_product from bahan_makanan where status = 1"
    cursor.execute(select_query)
    results = cursor.fetchall()
    valid_results = [float(result[0]) for result in results if result[0] is not None]
    total_dTRP = sum(valid_results)
    cursor.close()
    db_connection.close()
    return [total_dTRP]

def calculate_dARG():
    db_connection, cursor = sql_connection() 
    select_query = "select dARG, name_product from bahan_makanan where status = 1"
    cursor.execute(select_query)
    results = cursor.fetchall()
    valid_results = [float(result[0]) for result in results if result[0] is not None]
    total_dARG = sum(valid_results)
    cursor.close()
    db_connection.close()
    return [total_dARG]

def calculate_dVAL():
    db_connection, cursor = sql_connection() 
    select_query = "select dVAL, name_product from bahan_makanan where status = 1"
    cursor.execute(select_query)
    results = cursor.fetchall()
    valid_results = [float(result[0]) for result in results if result[0] is not None]
    total_dVAL = sum(valid_results)
    cursor.close()
    db_connection.close()
    return [total_dVAL]

def calculate_variables():
    db_connection, cursor = sql_connection() 
    select_query = "select dm, me, crude_protein, true_protein, ee, cf, ca, total_p, avail_p, cap, na, cl, choline, folate, dlys, dmet, dtsaa, dthr, dtrp, darg, dval from bahan_makanan"
    cursor.execute(select_query)
    results = cursor.fetchall()
    if results:
        dm = float(results[0][0]) if results[0][0] is not None else 0
        me = float(results[0][1]) if results[0][1] is not None else 0
        avail_P = float(results[0][2]) if results[0][2] is not None else 0
        total = dm + me + avail_P
    else:
        total = 0 
    cursor.close()
    db_connection.close()
    return total

@app.route('/api/formulate')
def render_formulate():
    total = calculate_variables()
    return jsonify(total)
    # total_ME = calculate_ME()
    # total_CP = calculate_CP()
    # total_TP = calculate_TP()
    # total_EE = calculate_EE()
    # total_CF = calculate_CF()
    # total_Ca = calculate_Ca()
    # total_Total_P = calculate_TotalP()
    # total_Avail_P = calculate_AvailP()
    # total_CaP = calculate_CaP()
    # total_Na = calculate_Na()
    # total_Cl = calculate_Cl()
    # total_Choline = calculate_Choline()
    # total_Folate = calculate_Folate()
    # total_dLYS = calculate_dLYS()
    # total_dMET = calculate_dMET()
    # total_dTSAA = calculate_dTSAA()
    # total_dTHR = calculate_dTHR()
    # total_dTRP = calculate_dTRP()
    # total_dARG = calculate_dARG()
    # total_dVAL = calculate_dVAL()
    # return jsonify({
    #     "ME": total_ME,
    #     "CP": total_CP,
    #     "TP": total_TP,
    #     "EE": total_EE,
    #     "CF": total_CF,
    #     "Ca": total_Ca,
    #     "Total_P": total_Total_P,
    #     "Avail_P": total_Avail_P,
    #     "CaP": total_CaP,
    #     "Na": total_Na,
    #     "Cl": total_Cl,
    #     "Choline": total_Choline,
    #     "Folate": total_Folate,
    #     "dLYS": total_dLYS,
    #     "dMET": total_dMET,
    #     "dTSAA": total_dTSAA,
    #     "dTHR": total_dTHR,
    #     "dTRP": total_dTRP,
    #     "dARG": total_dARG,
    #     "dVAL": total_dVAL
    # })
    
def temp_variable():
    my_array = array('i', [0] * 20)
    for i in range(20):
        my_array[i] = i


if __name__ == '__main__':
    app.run(debug=True)
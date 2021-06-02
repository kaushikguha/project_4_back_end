import models

from flask import Blueprint, request, jsonify

from playhouse.shortcuts import model_to_dict

from flask_login import current_user, login_required


pmt= Blueprint('pmt', 'pmt')

######################## Index

@pmt.route('/', methods=['GET'])
def pmt_index():


    print("")
    print('result of pmt select query')
    # print(result)

    pmt_dicts=[model_to_dict(pmt) for pmt in current_user.my_pmt]

    print(pmt_dicts)



    return jsonify({
        'data':pmt_dicts,
        'message':f'Succefffully found {len(pmt_dicts)} pmts',
        'status':200
    }),200

################################     CREATE
@pmt.route('/', methods=['POST'])
@login_required

def create_pmt():
    payload =request.get_json()
    print (payload)
    new_pmt = models.Pmt.create( ssn=current_user.id, amt_paid=payload['amt_paid'], pmt_date=payload['pmt_date'])
    print(new_pmt)
    # print(new_dog.__dict__)
    # print(dir(new_dog))

    pmt_dict=model_to_dict(new_pmt)

    return jsonify(
        data=pmt_dict,
        message="successfully created payment",
        status=201
    ), 201

    # return "You hit dog create route-- Check Terminal"


###################  Show route
    #GET api/v1/dogs/<dog_id>

@pmt.route('/<id>', methods=['GET'])
def get_one_pmt(id):
    pmt=models.Pmt.get_by_id(id)
    return jsonify(
        data= model_to_dict(pmt),
        message= "Success!!!",
        status= 200
    ), 200

################## Update route
@pmt.route('/<id>', methods=['PUT'])
def update_pmt(id):
    payload = request.get_json()
    query=models.Pmt.update(**payload).where(models.Pmt.id==id)
    query.execute()

    return jsonify(
        data=model_to_dict(models.Pmt.get_by_id(id)),
        status=200,
        message='resource updated successfully'
    ), 200

##############################Delete route
@pmt.route('/<id>', methods=['DELETE'])
def delete_pmt(id):
    query=models.Pmt.delete().where(models.Pmt.id==id).execute()

    return jsonify(
        data=None,
        status=200,
        message='resource updated successfully'
    ), 200

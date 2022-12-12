import os
import logging

def _return_temp(data:bytes)->float:
    decode_value = int(bin(int.from_bytes(data, byteorder="little", signed=False)),2)
    result = decode_value/2-20
    return round(result,1)

def _return_state_of_charge(data:bytes)->float:
    decode_value = int(bin(int.from_bytes(data, byteorder="little", signed=False)),2)
    result = decode_value/2
    return round(result,1)

def _return_state(data:bytes)->str:
    mapping_state = {
        0: "power off",
        1: "power on",
        2: "discharge",
        3: "charge",
        4: "charge complete",
        5: "host mode",
        6: "shutdown",
        7: "error",
        8: "undefined",
    }
    decode_value = int(bin(int.from_bytes(data, byteorder="little", signed=False))[2:][:-4],2)
    result = mapping_state[decode_value]
    return result


def _return_epoc_time(data:bytes)->int:
    decode_value = int(bin(int.from_bytes(data, byteorder="little", signed=False))[2:][:-4][3:],2)
    result = decode_value
    return result


def _return_decode_data(data:bytes):
    bat_temp = _return_temp(data[6:7])
    state_of_charge = _return_state_of_charge(data[5:6])
    state = _return_state(data[4:5])
    time = _return_epoc_time(data[0:5])
    return time, state, state_of_charge, bat_temp
    

    
    
def lambda_handler(event, context):
    logging.info(os.environ)
    logging.info('## EVENT')
    logging.info(event) 
    data = bytes.fromhex(event['payload'])
    time, state, state_of_charge, bat_temp = _return_decode_data(data)
    message = {
        "device": event['device'],
        "time": time,
        "state": state,
        "state_of_charge": state_of_charge,
        "temperature": bat_temp,
        }
    print(message)
    return message


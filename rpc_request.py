#!/usr/bin/env python3

import requests
import json
import sys,os
from datetime import datetime


base_dir = os.path.basename(os.getcwd())
host = 'http://127.0.0.1:58081/json_rpc'

decimals = 100000000
ticker = 'AMX'

def req(data):
        try:
                return(requests.post(host, data=data).json())
        except Exception:
                return('no connection')

def get_status():
        data = '{"jsonrpc":"2.0", "id":"0", "method":"get_status", "params":{}}'
        response = req(data)
        if type(response)==dict and response.get('result')!=None:
                res=response['result']
                page='Status:<br>'
                page+='Top know height: '+ str(res['top_known_block_height'])+'<br>'
                page+='Top block hash: <a href="/'+base_dir+'/index.php?raw_block='+str(res['top_block_hash'])+'">'+str(res['top_block_hash'])+'</a><br>'
                page+='Top block height: <a href="/'+base_dir+'/index.php?raw_height='+str(res['top_block_height'])+'">'+str(res['top_block_height'])+'</a><br>'
                page+='Top block date-time: '+ datetime.utcfromtimestamp(res['top_block_timestamp']).strftime('%Y-%m-%d %H:%M:%S')+' (timestamp: '+str(res['top_block_timestamp'])+')<br>'

                page+='Supply: '+ str(res['already_generated_coins']/decimals)+' '+ticker+'<br>'
                return(page)
        else:
                return(response)

        


def get_raw_tx(tx):
        data = '{"jsonrpc":"2.0", "id":"0", "method":"get_raw_transaction", "params":{"hash":"'+tx+'"}}'
        response = req(data)
        if type(response)==dict and response.get('result')!=None:
                res=response['result']['transaction']
                page='Transaction: '+str(res['hash'])+'<br>'
                page+='Amount: '+ str(res['amount']/decimals)+' '+ticker+'<br>'
                page+='Fee: '+ str(res['fee']/decimals)+' '+ticker+'<br>'
                page+='Size: '+ str(res['size'])+'<br>'
                page+='<br>In block:<br>'
                page+='Hash: <a href="/'+base_dir+'/index.php?raw_block='+str(res['block_hash'])+'">'+str(res['block_hash'])+'</a><br>'
                page+='Height: <a href="/'+base_dir+'/index.php?raw_height='+str(res['block_height'])+'">'+str(res['block_height'])+'</a><br>'
                page+='Block date-time: '+ datetime.utcfromtimestamp(res['timestamp']).strftime('%Y-%m-%d %H:%M:%S')+' (timestamp: '+str(res['timestamp'])+')<br>'
                page+='<br>Input:<br>'
                page+='Input hash: '+str(res['inputs_hash'])+'<br>'
                return(page)
        else:
                return('error')

def get_raw_data(data):
        response = req(data)
        if type(response)==dict and response.get('result')!=None:
                res=response['result']['block']['header']
                page='Block: <a href="/'+base_dir+'/index.php?raw_block='+str(res['hash'])+'">'+str(res['hash'])+'</a><br>'
                page+='Height: <a href="/'+base_dir+'/index.php?raw_height='+str(res['height'])+'">'+str(res['height'])+'</a><br>'
                page+='Block date-time: '+ datetime.utcfromtimestamp(res['timestamp']).strftime('%Y-%m-%d %H:%M:%S')+' (timestamp: '+str(res['timestamp'])+')<br>'
                page+='Version: '+ str(res['major_version'])+','+str(res['minor_version'])+'<br>'
                page+='Difficulty: '+ str(res['difficulty'])+'<br>'
                page+='Orphan status: '+ str(response['result']['orphan_status'])+'<br>'
                page+='Reward: '+ str(res['reward']/decimals)+' '+ticker+'<br>'
                page+='Base reward: '+ str(res['base_reward']/decimals)+' '+ticker+'<br>'
                page+='Block size: '+ str(res['block_size'])+' bytes<br>'
                page+='Transaction size: '+ str(res['transactions_size'])+' bytes<br>'
                page+='Total transactions: '+ str(res['already_generated_transactions'])+'<br>'
                page+='Total coins: '+ str(res['already_generated_coins']/decimals)+' '+ticker+'<br>'

                page+='<hr>Transactions<hr><table><tr><th>Amount</th><th>Fee</th><th>TX hash</th><th>Size</th></tr>'
                for x in response['result']['block']['transactions']:
                        page+='<tr><td>'+ str(x['amount']/decimals)+' '+ticker+'</td><td>'+str(x['fee']/decimals)+'</td><td><a href="/'+base_dir+'/index.php?raw_tx='+x['hash']+'">'+x['hash']+'</a></td><td>'+str(x['size'])+' bytes</td></tr> '
                page+='</table>'
                return(page)
        else:
                return('error')

def get_raw_block(block):
        data = '{"jsonrpc":"2.0", "id":"0", "method":"get_raw_block", "params":{"hash":"'+block+'"}}'
        return(get_raw_data(data))
        
def get_raw_height(height):
        data = '{"jsonrpc":"2.0", "id":"0", "method":"get_raw_block", "params":{"height_or_depth":"'+height+'"}}'
        return(get_raw_data(data))

if len(sys.argv) > 1:
        if sys.argv[1] == 'search':
                if len(sys.argv[2])<64:
                        print(get_raw_height(sys.argv[2]))
                if len(sys.argv[2])==64:
                        res=get_raw_block(sys.argv[2])
                        if res=='error':
                                print(get_raw_tx(sys.argv[2]))
                        else:
                                print(res)
        if sys.argv[1] == 'raw_tx':
                print(get_raw_tx(sys.argv[2]))
        if sys.argv[1] == 'raw_block':
                print(get_raw_block(sys.argv[2]))
        if sys.argv[1] == 'raw_height':
                print(get_raw_height(sys.argv[2]))
        
else:
        print(get_status())


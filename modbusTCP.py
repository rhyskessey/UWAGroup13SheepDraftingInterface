from pyModbusTCP.client import ModbusClient

c = ModbusClient(host="169.254.139.80", port=502, auto_open=True)

#c.write_multiple_registers(0, [2011])
index = 0
while(index < 1000):
    print(c.read_holding_registers(2, 4))
    index += 1
    


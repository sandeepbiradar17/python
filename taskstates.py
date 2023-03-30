states=[{"gid":1,"gname":"ram","TRRram":[
{"hid":1,"hname":"aam"},{"hid":2,"hname":"qam"},{"hid":3,"hname":"eam"},{"hid":4,"hname":"waam"},{"hid":5,"hname":"qqqaam"},{"hid":6,"hname":"qaaam"}
],
"wea":[{"WID":1,"WNAME":"QNAME"},{"WID":2,"WNAME":"QQQNAME"},{"WID":3,"WNAME":"AAAQNAME"},{"WID":4,"WNAME":"SAAQNAME"}]
},
{"gid":2,"gname":"sam","TRRram":[
{"hid":7,"hname":"JJaam"},{"hid":8,"hname":"qam"},{"hid":9,"hname":"Leam"},{"hid":10,"hname":"waam"},{"hid":11,"hname":"qqqaam"},{"hid":12,"hname":"qaaam"}
],
"wea":[{"WID":5,"WNAME":"KKQNAME"},{"WID":6,"WNAME":"ZAQQQNAME"},{"WID":7,"WNAME":"XZAAAQNAME"},{"WID":8,"WNAME":"QWESAAQNAME"}]
}]

#print(states)
for s in states:
    print(str(s["gid"])+" "+s["gname"])
    for c in s["TRRram"]:
            print("    "+ str(c["hid"])+" "+str(c["hname"]))
    for w in s["wea"]:
             print("                        "+str(w["WID"])+" "+w["WNAME"])
    print("-----------------------------------------------")
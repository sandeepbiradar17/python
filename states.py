states=[{"sid":1,"sname":"maharashtra","cities":
[
    {"cid":1,"cname":"pune"},
    {"cid":2,"cname":"mumbai"},
    {"cid":3,"cname":"nagpur"}
    ]
    },
    {"sid":2,"sname":"gujrat","cities":[
        {"cid":4,"cname":"surat"},
        {"cid":5,"cname":"gadinagar"}
     ]
}
]
#print(states)
for s in states:
             print(str(s["sid"])+" "+s["sname"])
             for c in s["cities"]:
                       print("     "+str(c["cid"])+""+c["cname"])
             print("-------------------------")
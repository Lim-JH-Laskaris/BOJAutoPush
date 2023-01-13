solution = lambda id_pw, db : "fail" if id_pw[0] not in list(map(lambda a:a[0], db)) else (
"login" if id_pw[1] == {k:v for k,v in db}[id_pw[0]] else "wrong pw")


import random

class CertificateNo:
    
    # creating unique number
    def get_no(self):
        # LETTERS
        let_l = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", 
        "T", "U", "V", "W", "X", "Y"]
        rl = random.sample(let_l, len(let_l))
        let = ""
        ll = []
        for l in range(0, 8):
            let = rl[l]
            ll.append(let)

        # NUMBERS
        num_l = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
        rn = random.sample(num_l, len(num_l))
        num = ""
        nl = []
        for n in range(0, 8):
            num = rn[n]
            nl.append(num)

        for i in ll:
            nl.append(i)

        random_password = random.sample(nl, len(nl))

        rp = ""

        for i in random_password:
            rp += i
        
        return rp
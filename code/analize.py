import pandas

data=pandas.read_csv('data.csv')

basecapacity=1
capacity=basecapacity/100.

print ",".join(["capacity","time","delta","charge","sold_without","sold_with","bought_without","bought_with"])
while capacity < 1e6:
    charge=0

    bought_without=0
    bought_with=0
    sold_without=0
    sold_with=0
    d=data.iloc[0]
    for r in data[1:].iterrows():
        d=r[1]
        delta=d.delta

        oldCharge=charge
        
        if delta > 0:
            # Sovraproduzione
            sold_without+=delta
            charge += delta
            if charge > capacity:
                sold_with += charge-capacity
                charge=capacity
        else:
            # Sottoproduzione
            bought_without+=-delta
            charge += delta
            if charge < 0:
                bought_with += -charge
                charge = 0


    print ",".join(map(str,[capacity,d.time,delta,charge,sold_without,sold_with,bought_without,bought_with]))

    basecapacity*=2
    capacity=basecapacity/100.



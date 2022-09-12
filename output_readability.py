weight = 20 / 2.205
dosage = weight * 30

print("CORRECT DOSAGE")
print("For a patient weighing {} kg,".format(round(weight,1))) # rounds to a number of sig figs
print("  the correct dosage is {} mg the first day".format(round(dosage,1)))
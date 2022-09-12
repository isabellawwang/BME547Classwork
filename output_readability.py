weight = 20 / 2.205
dosage = weight * 30

print("CORRECT DOSAGE")
print("For a patient weighing {:.1f} kg,".format(weight)) # : = formatting, .1=single decimal place, f=float
print("  the correct dosage is {:.1f} mg the first day".format(dosage))
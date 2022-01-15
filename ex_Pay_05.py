print ('Hello, i will help you calculate your pay!')
# eh(enter hours), er(enter rate), tpw(total pay week), fh(floating hours), fr(floating rate)
# nm(nuumber of weeks), ftpw(floating tpw), fnm(floating nm) tpm(total pay per month)
def computepay (hours, rate) :
    # print ('In computepay', hours, rate)
    if hours > 42 :
        # print ('Overtime')
        reg = hours * rate
        otp = (hours - 42.0) * (rate * 0.5)
        # print (reg, otp)
        tpw = reg + otp
        return tpw
    else :
        # print ('Regular')
        tpw = hours * rate
        # print ('Returning', tpw)
        return tpw

eh = input ('Enter hours per week: ')
er = input ('Enter rate per hour: ')

try :
    fh = float(eh)
    fr = float(er)
except :
    print ('Error, please enter numeric input!')
    quit ()

tpw = computepay (fh, fr)
print ('Pay per week:', tpw)

nm = input ('Enter number of weeks per month:')
try :
    ftpw = float(tpw)
    fnm = float(nm)
except :
    print ('Error, please enter numeric input!')
    quit()

tpm = ftpw * fnm
print ('Pay per month is:', tpm)

print ('I hope that i was helpful to you!')

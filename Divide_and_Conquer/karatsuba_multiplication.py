# Instead of traidional method of multiplication, 
# Let numbers x be AB and y be CD
#
# AB * CD = 	A B
#	      * C D
#	    --------
#	      AD BD
#	+ AC BC  ##
#	------------
#      AC [AD+BC] BD
#
# Equationally, 
# AB * CD = 10^n * AC + 10^(n/2) * (AD + BC) + BD
#
# Now, AD + BC can also be found using
#	(A + B)(C + D) = AC + AD + BC + BD
#	AD + BC = (A + B)(C + D) - AC - BD
#
# Thus, the final equation can be written as 
#	x * y = 10^n * AC + 10^(n/2) * [(A+B)(C+D) - AC - BD] + BD
#
# Running time : O(nlog2(3)) = O(n^(1.59)




def karatsuba(num1,num2):
	if num1 < 10 or num2 < 10: return num1 * num2		#base case

	halfmax = max(len(str(num1)),len(str(num2))) // 2 
	
	a = num1 // 10**(halfmax)
	b = num1 % 10**(halfmax)	
	c = num2 // 10**(halfmax)
	d = num2 % 10**(halfmax)
	
	ac = karatsuba(a,c)
	bd = karatsuba(b,d)
	ad_plus_bc = karatsuba((a+b),(c+d)) - ac - bd
    
	return ac * 10**(2*halfmax) + (ad_plus_bc * 10**halfmax) + bd


#Testinh

n1 = 3141592653589793238462643383279502884197169399375105820974944592
n2 = 2718281828459045235360287471352662497757247093699959574966967627

print(karatsuba(n1, n2))
#Expected Output : 8539734222673567065463550869546574495034888535765114961879601127067743044893204848617875072216249073013374895871952806582723184

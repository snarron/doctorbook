import docbookparse as dp
import query_request as qr

"""
for e in dp.final_result.values:
	print "<p>Caegory: "
	print e[0]
	print "Entry: "
	print e[1] + "</p>"
"""
print dp.final_result[::4]
print "Let's practice everything."
print 'You\'d need to know \'bout escapes with \\ that do \n new lines and \t tabls.'

poem="""
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\t where there is none.
"""

print '-------------'
print poem
print '-------------'


five = 10 - 2 + 3 - 6
print "This should be five: %s" % five

def secret_formula(started):
	jelly_beans = started * 500
	jars = jelly_beans / 1000
	crates = jars / 100
	return jelly_beans, jars, crates #wow python returns multiple values haha.
	

starting_point = 10000
beans, jars, crates = secret_formula(starting_point)

print "With a starting point of: %d" % starting_point
print "We'd have %d beans, %d jars, and %d crates." % (beans, jars, crates)

starting_point = starting_point/10

print "We can also do that this way:"
print "We'd have %d beans, %d jars, and %d crates" % secret_formula(starting_point)
#wow just wow. 


	

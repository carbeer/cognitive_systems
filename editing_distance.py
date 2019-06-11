# -*- coding: utf-8 -*-
import logging

class Levenshtein:
	def __init__(self, sub, rem, ins, sep):
		self.sub = sub
		self.rem = rem
		self.ins = ins
		self.sep = sep
		
	def min_edit_distance(self, ref, hyps):
		"""Computes edit distances for all hyps and returns the one with the lowest value"""
		best_hyp = ""
		best_val = -1
		for hyp in hyps:
			tmp = self.edit_distance(ref, hyp)
			logging.info("Calculated edit distance of %d for reference \"%s\" and hypothesis \"%s\"" % (tmp, ref, hyp))
			if tmp < best_val or best_val == -1:
				best_val = tmp
				best_hyp = hyp
		return best_hyp, best_val

	def edit_distance(self, ref, hyp):
		"""Calculates the edit distance from hyp to ref"""
		ref_arr = self.sep(ref)
		hyp_arr = self.sep(hyp)

		widths = [max([len(item) for item in hyp_arr])] + [len(hyp_arr)] + [len(item) for item in ref_arr]
		fmt = u"".join(['{{:<{}}}'.format(width+4) for width in widths])

		prev_row = range(len(ref_arr)+1) 

		logging.debug(fmt.format("", "", *ref_arr))
		logging.debug(fmt.format("", *prev_row))

		for i in range(len(hyp_arr)):
			curr_row = [i+1]
			for j in range(len(ref_arr)):
				# insert
				ins_val = curr_row[j] + self.ins
				# delete
				del_val = prev_row[j+1] + self.rem
				# substitute
				sub_val = prev_row[j] + self.sub if hyp_arr[i] != ref_arr[j] else prev_row[j] 
				# update value
				curr_row.append(min(ins_val, del_val, sub_val))

			prev_row = curr_row
			logging.debug(fmt.format(hyp_arr[i], *curr_row))
		return curr_row[len(ref_arr)]


def split(str):
	return str.split()


# Reference observed
ref = u"wenn es im Juni viel donnert kommt ein trüber Sommer"

# Hypotheses
hyp = [
	u"im Juni viel Sonne kommt einen trüberen Sommer",
	u"viel Donner im Juni einen trüben Sommer bringt",
	u"Juni Donner einen Sommer",
	u"im Juni viel Donner bringt einen trüben Sommer",
	u"wenns im Juno viel Donner gibts einen trüben Sommer"
]

# Set level to logging.DEBUG to see more granular output, otherwise logging.INFO should be fine
logging.basicConfig(level=logging.INFO)


# a)
sub = 1
rem = 1
ins = 1
sep = split

l = Levenshtein(sub, rem, ins, sep)
best, dist = l.min_edit_distance(ref, hyp)
logging.info("Solution for a): hypothesis \"%s\" has the lowest editing distance with a value of %d" % (best, dist))


# b)
sub = 1
rem = 1
ins = 1
sep = list

l = Levenshtein(sub, rem, ins, sep)
best, dist = l.min_edit_distance(ref, hyp)
logging.info("Solution for b): hypothesis \"%s\" has the lowest editing distance with a value of %d" % (best, dist))

# c)
sub = 2
rem = 1
ins = 1
sep = split

l = Levenshtein(sub, rem, ins, sep)
best, dist = l.min_edit_distance(ref, hyp)
logging.info("Solution for c): hypothesis \"%s\" has the lowest editing distance with a value of %d" % (best, dist))
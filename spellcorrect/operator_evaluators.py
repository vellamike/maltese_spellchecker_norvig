"""
The idea here is to look at the result of every operation
and price it. Give a finer idea of how expensive the operation
was. This is tricky in some way - is a i -> ie mapping cheaper than
a h to k mapping? Where is the correct place for this? is it in the
operations? My instinct is that the cost of an operation should map how
difficult it is to make the mistake in the context of the language, an i to ie
mistake is very common and should therefore be cheap. HOWEVER you may also argue that
that is the job of a more complex bayseian analysis to figure out.
"""

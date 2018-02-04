===============
 ``zopache.copy``
===============
Copies graphs of ZODB objects, customize how any an Interface class is handled.

It is not so easy to copy a part of the ZODB graph.
For starters every object has a __parent__ pointer, so you
are liable to get the whole graph.  Then you have the
problem that some objects in a tree may point to objects in another
part of the tree.  You do not want to copy those objects, just copy a link
to those objects.  And I do not know which of your objects do what,
so you have to be able to adapt the copying functions for any object
you create.


This is a fork of Zope.copy.   Why did I have to fork it?

Check out line 81 in __init__.py

hook = interfaces.ICopyHook(objectToBeCopied,None)

The ICopyHook is looking up an adaptor for the ObjectToBeCopied.
And the way the zope registries work, things adapt one class (interface)
and there is a default argument.
But Cromlech adapters are more advanced.  If you look up
an adaptor with two arguments, it adapts two things, what Zope
calls a multi-adaptor.  And so zope.copy   did not work in Cromlech. 

So in cromlech, I tried declaring it to be an adapter of (Interface,None)
but that threw an error.  So I had to fork zope.copy  to relace the
one line with:

   hook = interfaces.ICopyHook(obj)

   Zope.copy had another prolem.  It did not have a default Adapter
defined, so you had to figure out how to do it yourself.  But I had
an old version, and that documetned how to do it.  So I have added
a default cromlech adapter, so it is easy to get started with this package.
I have also included the ancient but still useful readme from an earlier
version of zope.copy

The current Zope.copy documentation is hosted at https://zopecopy.readthedocs.io/en/latest  Mostly it applies. /


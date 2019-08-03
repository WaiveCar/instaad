This is a quick and dirty proof of concept of the aviv version of the ad.

It's not designed to be "production ready" but more to help visualize the experience.

Whatever the long term implementation is it needs to be able to support some kind of on-the-fly configuration.

This is really TBD later but some of the possibilities are as foollows:

  * Configurable play-time (there's one php variable for the duration that scales it out)
  * Configurable assets (this would need some pretty serious retooling)
  * Configurable text below the circle (shouldn't be hard)
  * Configurable animation style (Might be easier to part out the animation part of the CSS and then just inject it based on the configuration ...)
  * Configurable number of images (This would require that math thing I've disowned myself from)

We should likely enumerate all the possibilities and then try to find 1 or 2 at most to do. Each option adds a dimension of choice and if you think
you can sell something to the general public with umpteen dimensions of configurability ok be my guest ... I certainly can't.

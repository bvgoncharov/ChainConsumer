"""
===================
Colours and Shading
===================

Choose custom colours and plot multiple chains with shading.

Normally when plotting more than one chain, shading is removed so
you can clearly see the outlines. However, you can turn shading back
on and modify the shade opacity if you prefer colourful plots.

Note that the contour shading and marginalised shading are separate
and are configured independently.

Colours should be given as hex colours.
"""

import numpy as np
from numpy.random import normal, multivariate_normal
from chain_consumer import ChainConsumer

if __name__ == "__main__":
    np.random.seed(2)
    cov = 0.2 * normal(size=(3, 3)) + np.identity(3)
    data = multivariate_normal(normal(size=3), 0.5 * (cov + cov.T), size=100000)

    c = ChainConsumer().add_chain(data, parameters=["$x$", "$y$", r"$\beta$"])
    c.plot(filename="demoVarious6_TruthValues.png", truth=[0.0, 5.0, 0.0, 0.0])

    # You can also set truth using a dictionary, like below.
    # If you do it this way, you do not need to
    # set truth values for all parameters
    c.configure_truth(color='w', ls=":", alpha=0.5) \
        .plot(filename="demoVarious6_TruthValues2.png",
              truth={"$x$": 0.0, "$y$": 5.0, r"$\beta$": 0.0})

import numpy        as np
import numpy.random as npr

import kayak

N = 100
D = 5
P = 1
learn = 0.00001

# Random inputs.
X = npr.randn(N,D)
true_W = npr.randn(D,P)
Y = np.dot(X, true_W) + 0.1*npr.randn(N,P)

# Build network.
kyk_inputs = kayak.Inputs(X)

# Labels.
kyk_targets = kayak.Targets(Y)

# Weights.
W = 0.01*npr.randn(D,P)
kyk_W = kayak.Parameter(W)

# Linear layer.
kyk_out = kayak.MatMult( kyk_inputs, kyk_W )

# Elementwise Loss.
kyk_el_loss = kayak.L2Loss(kyk_out, kyk_targets)

# Sum the losses.
kyk_loss = kayak.MatSum( kyk_el_loss )

for ii in xrange(10000):
    loss = kyk_loss.value(True)
    print loss, np.sum((kyk_W.value() - true_W)**2)
    grad = kyk_loss.grad(kyk_W)
    kyk_W.add( -learn * grad )


#print grad,
# ( Xw - t )T (Xw - t)
# 2 (Xw - t) X

#while kyk.batcher.next():
#    
#    # Get an evaluation object.
#    kyk_eval = kyk_loss.eval()

    # Now get gradients in terms of all these things.
#    kyk_l1_wts_grad = kyk_loss.grad( kyk_l1_wts )

    # Now get the actual values.
#    l1_wts_grad = kyk_l1_wts_grad.value()

    # Now update these guys.
#    kyk_l1_wts.value() -= rate * l1_wts_grad

    # Do this for everyone...



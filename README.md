# pool-simulator

The ultimate goal here is to create a pool/billiards AI 
step one: create a physics engine that can simulate a pool/billiard and account for all physical phenomena that happen on a pool table
step two: using simple game theory create an AI that will pick the best shot available
step three: add ML to the above AI and pit the algorithm against itself to improve the performance

I'm still working on step one I found a pool physics pdf attached in this repo which explains in depth all,
all of the interactions that happen on a pool table.  I will start by implimenting a physics engine that assumes ideal conditions, 
elastic collision, no spin effects, etc.
once i'm confidant that the ideal physics are working correctly i will add the more advanced interactions.

I don't have any intention for this simulator to have a graphical representation.  Meaning I'm not creating a pool game,
the ultimate goal is to have a pool playing AI, and in order to train the AI I don't need a graphical representation i just need the data.
If, however, it becomes apparent that I need a graphical representation to ensure that the physics engine is working correctly I will make
one.  In that case it will be very rudimentary. 

I chose python as the language because even though I intend to make the physics engine very accurate, there is not a huge amount of calculations
required so the easier coding of python was chosen over the calculation efficiency of C++.

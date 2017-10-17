## Probability Assignment

1. You call 2 Ubers and 3 Lyfts. If the time that each takes to reach you are
   independent and identical distributions, what is the probability that all the
   Lyfts arrive first? What is the probability that all the Ubers arrive first?

   **(Combinatorics)**

   

   Probability of first Uber arriving is (2/5) 
   Probability of second Uber arriving is (1/4)
   Probability of both Ubers arriving is (1/5*1/4) = 2/20  = 1/10

   Probability of first Lyft arriving is (3/5)
   Probability of second Lyft arriving is (2/4)
   Probability of third Lyft arriving is (1/3)
   Probability of all three Lyfts arriving first  (3/5 * (2/4) * 1/3)= 6/60 = 1/10


2. Consider a group of 20 people. If everyone shakes hands with everyone else,
   how many handshakes take place?

   **(Combinatorics)**

   20!C2! = 20! / (2!(18!)) = 380/2 = 190 handshakes



3. A worker has asked her supervisor for a letter of recommendation for a
   new job. She estimates that there is an 80 percent chance that she will
   get the job if she receives a strong recommendation, a 40 percent chance
   if she receives a moderately good recommendation, and a 10 percent chance
   if she receives a weak recommendation. She further estimates that the
   probabilities that the recommendation will be strong, moderate,
   and weak are .7, .2, and .1, respectively.

   **(Conditional Probability)**

   (a)  How certain is she that she will receive the new job offer?

   P(get the job | strong recommendation ) = .8
   P( get the job | moderately good recommendation) = .4
   P(get the job | weak recommendation ) = .1
   P(strong recommendation) = .7
   P(moderate recommendation) = .2
   P(weak recommendation) = .1

   P (Get Job and Strong Rec) / P(Strong Rec) = .8   P (Get Job and Strong Rec) = .8*.7 = .56
   P (Get Job and  Moderate Rec) / P(Moderate Rec) = .4   P (Get Job and Moderate Rec) = .4 * .2 = .08
   P (Get Job and  Weak Rec) / P(Weak Rec) = .1   P (Get Job and Weak Rec) = .1 * .1 = .01

   P(Get Job) = .56 + .08 + .01 = .65



   (b)  Given that she does receive the offer, how likely should she feel
        that she received a strong recommendation? a moderate recommendation?
        a weak recommendation?

       P(Strong Rec | Get Job)  = P(Strong Rec and Get Job) / P(Get Job) = .56 / .65 = .86
       P(Moderate Rec | Get Job) = P(Moderate Rec and Get Job) / P(Get Job) = .08 / .65 = .12
       P(Weak Rec | Get Job) = P(Weak Rec and Get Job) / P(Get Job) = .01 / .65 = .015


   (c)  Given that she does not receive the job offer, how likely should she
        feel that she received a strong recommendation?
        a moderate recommendation? a weak recommendation?

   P(No Job) = 1-P(Get Job) = 1-.65 = .35
   P(no Job | Strong Rec) = 1-.8 = .2
   P(No Job | Moderate Rec) = 1-.4 = .6
   P(No Job| Weak Rec) = 1-.1 = .9

   P(Strong Rec | No Job ) =  P(Strong Rec and No Job) / P( No Job) = (.7*.2 ) / .35 = .4
   P(Moderate Rec | No Job ) =  P(Moderate Rec and No Job) / P( No Job) =(.2*.6) / .35 = .343
   P(Weak Rec | No Job ) =  P(Weak Rec and No Job) / P( No Job) = ((.1*.9)) / .35 = .257

4. A simplified model for the movement of the price of a stock supposes that
   on each day the stock’s price either moves up 1 unit with probability p
   or moves down 1 unit with probability 1 − p. The changes on different days
   are assumed to be independent.

   **(Conditional Probability)**

   (a) What is the probability that after 2 days the stock will be at
       its original price?

   initial price = X
   each day there are two options 1) Stock price goes up (probability p) 2)Stock price goes down (probability 1-p)
   There are a total of 2x2 = 4 total options for how the stock price can move over two days
   In order for the stock price to remain constant, you need one day to go up and one day to go down, 2 possible options
   P(stock price remains the same after two days) = 2 /4 = 50%

   (b) What is the probability that after 3 days the stock’s price will
       have increased by 1 unit?

   Total number of possible combinations for three days is 2^3 = 8 options
   In order for the stock price to increase by one unit, you need two days of price increasing and one day of price decreasing. There are 3C2 = 3 possible wasy for this to occur.
   P( Stock price increased by 1 unit after three days) = 3/8 or 37.5%


   (c) Given that after 3 days the stock’s price has increased by 1 unit,
       what is the probability that it went up on the first day?
  P ( Stock price increased by 1 unit after three days) = 3/8 or 37.5%

   P(went up on first day | after three days the stock's price increase by 1 unit) = P(up first day AND after three days stock price up 1 unit) / P(after three days price up one unit) = 2/8 / 3/8 = 2/3

   

5. A salesman has scheduled two appointments to sell encyclopedias. His
   first appointment will lead to a sale with probability .3, and his second
   will lead independently to a sale with probability .6. Any sale made is
   equally likely to be either for the deluxe model, which costs $1000, or
   the standard model, which costs $500. Determine the probability mass
   function of X, the total dollar value of all sales.

   **(Random Variable - PMF)**

   P(Sale first) = . 3 
   P(Sale second) = .6
   deluxe = $1,000
   standard = $500
   P(deluxe | Sale First) = .5
   P(standard | Sale First) = .5
   P(deluxe | Sale Second) = .5
   P(standard | Sale Second) = .5
   P(deluxe AND Sale First) = P(Sale first)/2 = .15
   P(deluxe AND Sale Second) = P(Sale second)/2 = .3
   P(standard AND Sale First) = P(Sale first)/2 = .15
   P(standard AND Sale Second) = P(Sale second)/2 = .3
   P(no sale for Sale First) = 1-.3=.7
   P(no sale for Sale Second) = 1-.6=.4



   EX = {(.3)*(.5)*(1,000)+(.3*(.5)*($500) for the first sale
            (.6)*(.5)*(1,000) + (.6)*(.5)*(500) for the second sale }

  X = $2,000 dollars  = P(deluxe AND Sale First) * P(deluxe AND Sale Second) = .15*.3 = .045

  X = $1,500 dollars  = P(deluxe AND Sale First)*P(standard AND Sale Second) + P(Standard AND Sale First)*P(Deluxe AND Sale Second) = (.15*.3)+(.15*.3)=.09

  X= $1,000 dollars = P(standard AND Sale Second)*P(standard AND Sale First) + P(deluxe AND Sale first)*P(no sale for Sale Second) + P(deluxe AND Sale Second)*P(no sale for Sale First) = (.15*.3)+(.15*.4)+(.3*.7)=.315

  X = $500 dollars = P(standard AND Sale First)*P(no sale for Sale Second) +P(standard AND Sale Second)*P(no sale for Sale First)  = (.15*.4)+(.3*.7)=.27

  X = $0 dollards = P(no sale for Sale First)*P(no sale for Sale Second) = .7*4 = .28



6. A gambling book recommends the following “winning strategy” for the game of
   roulette: Bet $1 on red. If red appears (which has probability 18/38), then
   take the $1 profit and quit. If red does not appear and you lose this bet
   (which has probability 20/38 of occurring), make additional $1 bets of red
   on each of the next two spins of the roulette wheel and then quit.
   Let X denote your winnings when you quit.

   **(Random Variable - Expected Value)**

   P(red appears) = 18/38
   P(red doesn't appear) = 20/38

   F(x)= {$x(18/38) if red appears 
          -$x(20/38) if red doesn't appear on first roll
        $x(18/38)+$x(18/38) if red doesn't appear on first, next two rolls}


   (a)  Find P(X > 0).

    P(X >0) = P(X=1) =1 - P(X<=0)
    =1 - P(red doesn't appear on first roll)*P(red doesn't appear on second roll)*P(red doesn't appear on third roll)
     + P(red doesn't appear on first roll)*P(red doesn't appear on second roll)*P(red appears on third roll)
      + P(red doesn't appear on first roll)*P(red appears on second roll)*P(red doesn't appear on third roll)
    = 1 - (20/38)^3+(20/38)^2*(18/20)+(20/38)^2*(18/38)
    = 1 - .146 + .131 + .131
    = .592


  

   (b)  Find E[X].
   x=1

   E[X] 

      =P(X=1)(Expected winnings)-P(x<0)(Expected losings)
      =P(X=1)*1-P(X=-1)*1-P(X=-3)*3
      =.592 +[(20/38)^2*(18/38)]*(-1) + ([(20/38)^3]*(-3))
      =.592 - .2624 - (3*.1458)
      =-.108



   (c)  Are you convinced that the strategy is indeed a “winning” strategy?

   This is not a winning strategy. E[X] = -$.108 so you are expected to lose money each time you play. 


7. The number of times that a person contracts a cold in a given year is a
   Poisson random variable with parameter λ = 5. Suppose that a new wonder
   drug (based on large quantities of vitamin C) has just been marketed that
   reduces the Poisson parameter to λ = 3 for 75 percent of the population.
   For the other 25 percent of the population, the drug has no appreciable
   effect on colds. If an individual tries the drug for a year and has 2 colds
   in that time, how likely is it that the drug is beneficial for him or her?

   **(Random Variable - Poisson + Conditional Probability)**
   λ = 5 (number of times person contracts cold / year)
   λ = 3 for .75 of population , other .25 λ =5
   k = 2 (2 colds)
   p(drug is beneficial) = .75
   P(drug is not beneficial) = .25

   person has 2 colds in a year


   P( two colds | the drug is not beneficial) = e^-5 *(5^2/2!) = .084 
   P( two colds | drug is beneficial) = e^-3*(3^2/2!) = .2240
   P( two colds in a year) = P( two colds | the drug is not beneficial)*P(drug is not beneficial) + P( two colds | drug is beneficial) *P(drug is beneficial)
    =.084*.25 +.2240*.75
    =.189

   P(drug is beneficial | two colds in a year) = P(two colds in a year | drug is beneficial) *P(drug is beneficial) / P(two colds in a year)

   =(.2240)*(.75) / .189 = 88.8% chance that the drug is beneficial for him or her

   

8. Suppose that X is a normal random variable with mean 5. If P(X > 9) = .2,
   approximately what is Var(X )? Use the normal distribution function table.

   **(Random Variable - Normal + CDF)**
   mean = 5
   F(.2)=.84 Z-score 


   P(X<=9) = 1-.2 = .8
   P(X>9) = .2
   
   P(x-5 / Sigma  > 9-5 / Sigma) = .2  => P(Z > 4 / sigma)
   Z = .84
   4 / .84 = 4.76 = sigma
   sigma^2 = 4.76*4.76 = 22.66




9. The forecast says that in the next five days the chance of rain for each day
   is 25%. Suppose that the weather on each day does not depend on the weather
   on the other days. What is the probability that it will rain for at least
   two days in the next five days? For how many days on average will it
   rain in the next five days?

   **(Random Variable - Binomial)**

   P(rain) = .25

   1) P(rain for two or moredays) = 1- P(no rain for five days) - P(rain for one day)
   = 1 - .75^5 - 5C1(.25)(.75^4) = 1 - .237 - .3955 = 36% chance it will rain for at least two days

   2)EX 5(.25) = 1.25 days of rain expected




10. The number of years a radio functions is exponentially distributed with
    parameter λ = 1 / 8  . If Jones buys a used radio, what is the probability
    that it will be working after an additional 8 years?

    **(Random Variable - Exponential)**

   f(x) = λ e^(-λx)

   P(x>8) =integral(8 to infinity) λ e^(-λx) dx
   = integral(8 to infinity) 1/8 * e^(-1/8x) dx
   =1/8[lim goes to inifity( -8* e ^ -(1/8x))  -  (8*e^(-1))]
   =-e^-1



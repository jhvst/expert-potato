# expert-potato
Junction 2017

We are machine learning to scrape Twitter, news sources and weather data to predict the likelihood of flight delay or cancellation.

## Used sources

* Twitter ( http://twitter.com )
* 5000 news sources ( http://newsapi.org/ )
* Weather data ( http://yr.no )

## Causes
* weather
* airspace
* strikes
* environmental
* airport closure
* national
* large events
* political conflicts
* military operations
* other

## Technology
* The collected text is tokenized and then classifed using the bag-of-words
  approach. A random forest classifier is trained to pick messages that have a
  high probability of causing flight delays. Ground-truth labels for training
  the ensemble were manually collected during the event using custom tooling.
  In total the classifier used about 2000 training samples and we believe that
  better accuracy could be achieved with a larger dataset.
* A nice property of random forests is their interpretability. We can for
  example ask the classifier which words have the highest impact on the
  results. In our case the top-10 words are
  * eruption
  * winds
  * storm
  * life-threatening
  * have
  * homes
  * imminently
  * people
  * smoke
  * prepares

## Used languages
* Python
* Go
* JS (Node, React & all that jazz)

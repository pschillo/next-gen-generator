# project documentation
I shall be documenting the progress of this project here.
## motivation
This project combines two things I love: Star Trek and programming.
## sources
The programme uses a complete collection of transcripts of all episodes of Star Trek - The Next Generation. I have specified two sources, "chakoteya" being the primary one based on its suitable format and standardization. Additionally, I added an alternative source with the same content and slightly worse formatting in case I require it at a later point.
The "chakoteya" dataset adheres to the British English conventions and will be used as material source for this project unless otherwise specified.
## workflow
### project registration
"You could develop a Telegram bot that returns a quote from a specified TNG character given a query based on keyword matching. For this, you would first have to create a data set of quotes for each character from the TNG scripts and build some sort of keyword index. I would suggest that keywords for each quote are the set of non-stopword lemmas determined by spacy. So for the quote "I am superior, sir, in many ways, but I would gladly give it up to be human" by Data, the keywords would be {superior, sir, way, gladly, human}. When e.g. a quote about "Are humans superior?" by Data is requested via the bot, then the keywords in that query would be {human, superior} and a suitable quote can be selected by returning the quote whose keywords have the smallest Hamming distance to the query keywords." -Martin
### data pre-processing
As a first step, I processed the raw script to create .csv files with quotes from each character. In preparation, I had to determine which characters to make available via the bot. Based on popularity, I arrived at the following cast:
- Captain Picard
- Data
- Q
- Lt. Cm. Riker
- Diana Troi
### the Telegram bot
I started by checking boxes on the necessary formalities of a Telegram bot, i.e. registering the bot with Telegram's own "botfather", creating the bot's unique tag (nextgen_genrator_bot) and acquiring its unique token from Telegram. The tag will only be relevant for users to find the bot in the Telegram app but must be chosen upon initialization. The token enables my script to be matched with the corresponding bot, which is why it should be kept secure and is not included in any of my commits.
## result

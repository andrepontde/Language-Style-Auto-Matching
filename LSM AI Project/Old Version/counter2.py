
text = ""

word_count = 0


def counter_input(input_text):
    global text  # This tells Python to use the global 'text' variable
    text = input_text
    global word_count 
    word_count = len(text.split())


# Count the words in the provided text


# Correct personal pronouns list based on the uploaded file content
ppron_list = [
    "afaik", "amirite", "ayo", "bless you", "fml", "fu", "fuck you", "fyi", "gotcha", "gotchu", "he", "he'd", "he'd like", 
    "he'd love", "he'll", "he's", "her", "her fault", "her highness'", "her kind of", "her majesty", "hers", "herself", "hes", 
    "him", "himself", "his", "his excellesnce", "his fault", "his kind of", "his majesty", "hissel", "hmu", "i", "I", "I i", 
    "I'd", "I'd like", "I' love", "I'de", "I'll", "I'm", "I'm confident", "I'm positive", "I'mma", "I've", "idc", "idek", 
    "idgaf", "idk", "idontknow", "ihy", "iirc", "ikr", "ill", "ill temper", "ill treat", "ill treatment", "ily", "ilyk", 
    "im", "im crying", "im dead", "ima", "imean", "imho", "imma", "imo", "ive", "kiss my ass", "let's", "lets", "lmao", 
    "lmaoo", "lmaorofl", "lmfaoo", "lmk", "me", "mentally ill", "methinks", "mine", "my", "my child", "my dude", "my gal", 
    "my girl", "my gal", "my kid", "miy kind of", "my lady", "my man", "my nigga", "myself", "not my favourite", "not your fault", 
    "omfg", "omg", "oneselg", "our", "our child", "our fault", "our kid", "our kind of", "ours", "piss me off", "piss you off", 
    "screw you", "she", "she'd", "she'd like", "she'd love", "she'll", "she's", "shes", "smd", "smdh", "smh", "thee", "their", 
    "their fault", "theirs", "them", "themselves", "themselve", "they", "they'd", "they'd like", "they'd love", "they'dve", "they'll", "they're", "they's", "they've", "theyd", "they’ll", "theyre", "they’ve", "thine", "thou", "thoust", "thy", "thyself", 
    "tho whom it may concern", "ttyl", "ty", "u", "understand you", "understood you", "ur", "us", "watchu", "we", "we'd", 
    "we'd like", "we'd love", "we'll", "we're", "we've", "weve", "whaddya", "whatcha", "who", "who'd", "who'll", "who're", 
    "who's", "whod", "whoever", "wholl", "whom", "whomever", "whos", "whose", "whosever", "whoso", "wyd", "xe", "xem", 
    "xemself", "xyr", "xyrs", "y you", "y'all", "y'kn", "ya", "ya'll", "yall", "yalls", "ye", "ykn", "yolo", "you", "you'd", 
    "you'd like", "you'd love", "you'll", "you've", "youd", "youknow", "youll", "your", "your fault", "youre", "yours", 
    "yourself", "yourselves", "you’ve", "ze", "zir", "zirs", "zirself", "nt my favourite", "nt your fault", "n't my favorite", 
    "n't your fault", "em"
]

# Count occurrences of personal pronouns with the corrected list

# List of impersonal pronouns from the uploaded file content
ipron_list = [
    "another", "anybody", "anyone", "anything", "everybody", "everyday", "everyone", 
    "everything", "it", "its", "itself", "no one", "no-one", "nobody", "none", "noone", 
    "nowhere", "others", "somebody", "someone", "something", "stuff", "that", "these", 
    "that’s", "thing", "this", "those", "to whom it may concern", "what", "whatever", 
    "whats", "whatsoever", "which", "whichever"
]

# Count occurrences of impersonal pronouns

# List of auxiliary/incomplete verbs from the uploaded file content
aux_list = [
    "ain't", "am", "am confident", "am positive", "amirite", "are", "aren't", "be", "been", "being", "can", "can't", "cannot", "could", 
    "could've", "coulda", "couldn't", "did", "did not have", "didn't", "do", "do not have", "does", "does not have", "doesn't", 
    "doing", "don't", "done", "had", "hadn't", "has", "hasn't", "have", "haven't", "having", "he'd", "he'll", "he's", "here's", 
    "how'd", "how'll", "how're", "how's", "how've", "i'd", "i'll", "i'm", "i've", "is", "isn't", "it'd", "it'll", "it's", "let's", 
    "may", "might", "mightn't", "must", "must've", "mustn't", "ought", "oughtn't", "shall", "shan't", "she'd", "she'll", "she's", 
    "should", "should've", "shouldn't", "that'd", "that's", "there's", "they'd", "they'll", "they're", "they've", "to be honest", 
    "was", "wasn't", "we'd", "we'll", "we're", "were", "weren't", "what's", "when's", "where's", "who'd", "who'll", "who's", "will", 
    "won't", "would", "would've", "wouldn't", "you'd", "you'll", "you're", "you've"
]
# Count occurrences of auxiliary/incomplete verbs

# Load and count occurrences of negations from the correct uploaded file content
nega_list = [
    "ain't", "aint", "arent", "arent", "by no means", "can't", "cant", "caouldn't", "couldnt", "did not have", "didn't", 
    "didn't care", "didn't have", "didnt", "do not have", "does not have", "doesn't", "doesn't care", "doesn't have", 
    "doesnt", "don't", "don't care", "don't have", "dont", "dunno", "good for nothing", "good-for-nothing", "hadn't", 
    "hadnt", "hasn't", "hasnt", "haven't", "havent", "idc", "idek", "idgaf", "idk", "idontknow", "I don't know", "isn't", 
    "isn't sure", "isnt", "might'nt", "mightn't", "must'nt", "mustn't", "mustnt", "nah", "nbd", "need'nt", "needn't", 
    "neednt", "negate", "negated", "negates", "negating", "negation", "negatively", "neither", "never", "nevermind", 
    "no", "no chance", "no doubt", "no idea", "no kind of", "no motivation", "no one", "no-one", "nobod", "noes", "none", 
    "noone", "noone's", "nope", "nor", "not", "not a bad idea", "not a big fan", "not a chance", "not a fan", "not a good", 
    "not a good idea", "not a perfect", "not a problem", "not a single", "not a soul", "not all", "not always", 
    "not an option", "not bad", "not by any means", "not care", "not certain", "not enough", "not enough sleep", 
    "not even close", "not even funny", "not even sure", "not exactly", "not good", "not have any", "not in the least", 
    "not in the mood", "not let", "not my favorite", "not normal", "not one", "not particular", "not precise", 
    "not quite", "not quite sure", "not really", "not really sure", "not so far", "not so much", "not so sure", 
    "not the case", "not the least", "not the point", "not the same", "not the slightest", "not true", "not your fault", 
    "nothing", "nowhere", "np", "nsfw", "nvm", "ought'nt", "oughtn't", "oughtnt", "shan'tm", "shant", "should'nt", 
    "shouldn't", "shouldnt", "tl;dr", "tldr", "uh uh", "uh-uh", "wasn't", "wasnt", "wasn't sure", "weren't", "weren't sure", 
    "werent", "weren't sure", "werenr", "won't", "wont", "wouldn't", "wouldnt"
]

# Count occurrences of negations with the corrected list

adverb_list = [
    "about", "about to", "absolutely", "actually", "additionally", "admittedly", "af", "afaik", "afterward", "again", 
    "ago", "aka", "alike", "almost", "alone", "already", "alright", "also", "always", "amply", "angrily", "annually", 
    "anonymously", "anyhow", "anymore", "anyway", "anywhere", "apiece", "apparently", "appropriately", "around", 
    "artificially", "attractively", "automatically", "aversively", "awfully", "awhile", "awkwardly", "backward", 
    "backwards", "badly", "barely", "basically", "beautifully", "besides", "beyond", "bitterly", "bizarrely", 
    "blazingly", "blown away", "born again", "bossily", "bravely", "briefly", "broadly", "certainly", "chiefly", 
    "clearly", "closely", "coaxingly", "collectively", "comparatively", "completely", "confidently", "consistently", 
    "constantly", "contemptibly", "continually", "crankily", "crappily", "critically", "crucially", "cruelly", 
    "currently", "curtly", "dangerously", "daringly", "dashingly", "dearly", "decently", "deceptively", "definitely", 
    "delicately", "densely", "dependably", "dependently", "determinedly", "differently", "distantly", "divinely", 
    "dreadfully", "drowsily", "drunkenly", "dubiously", "dully", "eagerly", "else", "elsewhere", "emphatically", 
    "entirely", "especially", "essentially", "even", "even remotely", "eventually", "ever", "everywhere", "evidently", 
    "exceedingly", "exclusively", "extensively", "extremely", "faintly", "fairly", "feel better", "fervently", 
    "finally", "firmly", "firstly", "flexibly", "fomo", "fondly", "foolishly", "formally", "formerly", "fortunately", 
    "frankly", "frequently", "freshly", "fully", "funnily", "funny how", "gave up", "generally", "genuinely", 
    "germanely", "get ahead", "giddily", "give up", "gladly", "gloriously", "glumly", "good-naturedly", "gorgeously", 
    "grandly", "gravely", "grievously", "hardly", "harshly", "hauntingly", "healthily", "heavily", "helpfully", 
    "hence", "henceforth", "here", "here's", "herein", "heres", "hereto", "hereupon", "historically", "hopefully", 
    "hopelessly", "horribly", "how", "how'd", "how'll", "how're", "howd", "however", "howll", "howre", "hows", "howve", 
    "hungrily", "iirc", "immediately", "importantly", "impossibly", "impressively", "incredibly", "indeed", 
    "independently", "indifferently", "individually", "inevitably", "initially", "innocently", "insanely", 
    "insignificantly", "instantly", "instead", "intensely", "intentionally", "intently", "internationally", 
    "interpersonally", "intimately", "invisibly", "irrefutably", "irrefutable", "irregardlessly", "irregardless", 
    "j/k", "jk", "jus", "juss", "just", "juz", "keenly", "kindly", "lamely", "largely", "lastly", "lately", "learn about", 
    "lightly", "locally", "loudly", "luckily", "madly", "mainly", "maybe", "meanwhile", "mentally", "merely", 
    "merrily", "mess around", "messing around", "mightily", "mildly", "mischievously", "modestly", "moreover", 
    "mostly", "motherly", "mournfully", "musingly", "mutely", "mysteriously", "naively", "namely", "naturally", 
    "naughtily", "nearly", "neatly", "necessarily", "negatively", "never", "nevertheless", "newly", "nonetheless", 
    "normally", "not always", "not even close", "not even funny", "not even sure", "not quite", "not quite sure", 
    "not really", "not really sure", "not so far", "not so much", "not so sure", "notwithstanding", "now", 
    "obviously", "oddly", "often", "once", "only", "orally", "ordinarily", "originally", "partly", "passionately", 
    "patently", "perfectly", "perhaps", "permanently", "pettily", "physically", "pitifully", "playfully", "poorly", 
    "possibly", "practically", "precisely", "presently", "presumably", "pretty", "primarily", "principally", 
    "privately", "probably", "promptly", "proudly", "purely", "quarterly", "querulously", "quickly", "quietly", 
    "quite", "quite sure", "quizzically", "rapidly", "rarely", "rashly", "rather", "readily", "really", "reasonably", 
    "regularly", "relatively", "remotely", "resentfully", "respectfully", "respectively", "revoltingly", "ridiculously", 
    "rightly", "rly", "rn", "romantically", "roughly", "rudely", "sadly", "sarcastically", "scarcely", "scarily", 
    "secondly", "secretively", "seldom", "selectively", "serenely", "seriously", "shortly", "significantly"
]

# Count occurrences of adverbs with the corrected list

# List of conjunctions from the uploaded file content
conj_list = [
    "after", "also", "altho", "although", "and", "as", "asap", "asf", "bc", "because", "before", "but", "cos", "coz", 
    "cuz", "either", "however", "if", "iirc", "life and death", "more than", "netflix and chill", "nevertheless", "nor", 
    "not so far", "not so much", "not so sure", "notwithstanding", "or", "otherwise", "plus", "rather than", 
    "sick and tired", "since", "so", "so called", "than", "then", "tho", "tho'", "though", "til", "till", "unless", 
    "until", "up and coming", "when", "whend", "whenever", "whenll", "whenre", "whenve", "whereas", "wherefore", 
    "wherever", "whether", "while", "whilst"
]

# ipron_counts, nega_counts, aux_counts, ppron_counts, adverb_counts, conj_counts, total_words, total_ppron, total_ipron, total_aux, total_nega, total_adverb, total_conj

# avg_ppron, avg_ipron, avg_aux, avg_nega, avg_adverb, avg_conj = 0.0


def count_occurrences(text, word_list):
    # Creates a dictionary with the count of each word in word_list found in the text
    word_counts = {word: text.split().count(word) for word in word_list}
    # Filters the dictionary to keep only words with a count greater than 0
    return {word: count for word, count in word_counts.items() if count > 0}

# Assuming count_occurrences is defined correctly

def compute_counts():
    word_count = len(text.split())
    
    # Utilize count_occurrences for each category
    ipron_counts = count_occurrences(text, ipron_list)
    nega_counts = count_occurrences(text, nega_list)
    aux_counts = count_occurrences(text, aux_list)
    ppron_counts = count_occurrences(text, ppron_list)
    adverb_counts = count_occurrences(text, adverb_list)
    conj_counts = count_occurrences(text, conj_list)

    # Calculate totals and directly compute averages to avoid repeating code
    avg_ppron = sum(ppron_counts.values()) / word_count if word_count else 0
    avg_ipron = sum(ipron_counts.values()) / word_count if word_count else 0
    avg_aux = sum(aux_counts.values()) / word_count if word_count else 0
    avg_nega = sum(nega_counts.values()) / word_count if word_count else 0
    avg_adverb = sum(adverb_counts.values()) / word_count if word_count else 0
    avg_conj = sum(conj_counts.values()) / word_count if word_count else 0
    
    return avg_ppron, avg_ipron, avg_aux, avg_nega, avg_adverb, avg_conj



#For it, so but it, how did it evolve to what it is now? Was it a vision? Was it a slow sort of a gradual increase in numbers? And yeah, I mean, it's about as slow as it gets. Uh, I mean, I can so like when I was a young teenager, I was getting no views, had no money, had no equipment. So for the most part, it was just like I was just trying to scrounge money so I could buy equipment because I was using my brother's old laptop. And so like my first couple hundred videos, I didn't have a microphone, like imagine just like crackly terrible voice. Um, and so once I got monetized, I saved up for a few months like I told you, I bought a microphone. I didn't just give you a mile-high history, and I saved up for like six months. I mean, I was just doing video game videos, uh, and they were terrible, but I saved up. I got a real computer, so now I can actually record the video game at high quality. I have a microphone. I'm like 15, and I just kept going and going. Um, trying to figure out like what are some of like the hot spots like I, essentially, up until 18, I had been doing YouTube pretty religiously, but I was making no money. Like this is kind of the turning point was when I graduated from high school, and my whole life, I was like, I want to be making enough money by the time I graduated to do this full-time, and I wasn't. I was only making a couple hundred bucks a month.



text = input("What is the text")

# Function to count total words
def count_words(text):
    return len(text.split())

# Lists of specific words from the parameters
ppron = [
    "about", "about to", "absolutely", "actually", "additionally", "admittedly", "af", "afaik", "afterward", "again", 
    "ago", "aka", "alike", "almost", "alone", "already", "alright", "also", "always", "amply", "angrily", "annually", 
    "anonymously", "anyhow", "anymore", "anyway", "anywhere", "apiece", "apparently", "appropriately", "around", 
    "artificially", "attractively", "automatically", "aversively", "awfully", "awhile", "awkwardly", "backward", 
    "backwards", "badly", "barely", "basically", "beautifully", "besides", "beyond", "bitterly", "bizarrely", 
    "blazingly", "blown away", "born again", "bossily", "bravely", "briefly", "broadly", "certainly", "chiefly", 
    "clearly", "closely", "coaxingly", "collectively", "comparatively", "comparately", "completely different", 
    "confidently", "consistently", "constantly", "contemptibly", "continually", "crankily", "crappily", "critically", 
    "crucially", "cruelly", "currently", "curtly", "dangerously", "daringly", "dashingly", "dearly", "decently", 
    "deceptively", "definitely", "delicately", "densely", "dependably", "dependently", "determinedly", "differently", 
    "distantly", "divinely", "dreadfully", "drowsily", "drunkenly", "dubiously", "dully", "eagerly", "else", "elsewhere", 
    "emphatically", "entirely", "especially", "essentially", "even", "even remotely", "eventually", "ever", "everywhere", 
    "evidently", "exceedingly", "exclusively", "extensively", "extremely", "faintly", "fairly", "feel better", 
    "fervently", "finally", "firmly", "firstly", "flexibly", "fomo", "fondly", "foolishly", "formally", "formerly", 
    "fortunately", "frankly", "frequently", "freshly", "fully", "funnily", "funny how", "gave up", "generally", 
    "genuinely", "germanely", "get ahead", "giddily", "give up", "gladly", "gloriously", "glumly", "good-naturedly", 
    "gorgeously", "grandly", "gravely", "grievously", "hardly", "harshly", "hauntingly", "healthily", "heavily", 
    "helpfully", "hence", "henceforth", "here", "here's", "herein", "heres", "hereto", "hereupon", "historically", 
    "hopefully", "hopelessly", "horribly", "how", "how'd", "how'll", "how're", "howd", "however", "howll", "howre", 
    "hows", "howve", "hungrily", "iirc", "immediately", "importantly", "impossibly", "impressively", "incredibly", 
    "indeed", "independently", "indifferently", "individually", "inevitably", "initially", "innocently", "insanely", 
    "insignificantly", "instantly", "instead", "intensely", "intentionally", "intently", "internationally", 
    "interpersonally", "intimately", "invisibly", "irrefutably", "irrefutable", "irregardlessly", "irregardless", "j/k", 
    "jk", "jus", "juss", "just", "juz", "keenly", "kindly", "lamely", "largely", "lastly", "lately", "learn about", 
    "lightly", "locally", "loudly", "luckily", "madly", "mainly", "maybe", "meanwhile", "mentally", "mentally ill", 
    "merely", "merrily", "mess around", "messing around", "mightily", "mildly", "mischievously", "modestly", "moreover", 
    "mostly", "motherly", "mournfully", "musingly", "mutely", "mysteriously", "naively", "namely", "naturally", 
    "naughtily", "nearly", "neatly", "necessarily", "negatively", "never", "nevertheless", "newly", "nonetheless", 
    "normally", "not always", "not even close", "not even funny", "not even sure", "not quite", "not quite sure", 
    "not really", "not really sure", "not so far", "not so much", "not so sure", "notwithstanding", "now", "obviously", 
    "oddly", "often", "once", "only", "orally", "ordinarily", "originally", "partly", "passionately", "patently", 
    "perfectly", "perhaps", "permanently", "pettily", "physically", "pitifully", "playfully", "poorly", "possibly", 
    "potentionally", "practically", "precisely", "presently", "presumably", "pretty", "primarily", "principally", 
    "privately", "probably", "prolly", "promptly", "proudly", "pull ahead", "purely", "quarterly", "querulously", 
    "quickly", "quietly", "quite", "quite sure", "quizzically", "rapidly", "rarely", "rashly", "rather", "rather than", 
    "readily", "really", "reasonably", "regularly", "relatively", "remotely", "resentfully", "respectfully", 
    "respectively", "revoltingly", "ridiculously", "rightly", "rly", "rn", "romantically", "roughly", "rudely", "sadly", 
    "sarcastically", "scarcely", "scarily", "secondly", "secetively", "seldom", "selectively", "serenely", "seriously", 
    "shortly", "significantly", "simply", "sincerely", "singly", "singularly", "sleepily", "slowly", "smartly", "smoothly", 
    "sneakily", "snidely", "so", "so called", "socially", "somehow", "somewhat", "somewhere", "soon", "sourly", 
    "specially", "speedily", "spiritly away", "spirit away", "steeply", "stickily", "stiffly", "still", "subsequently", 
    "successfully", "suddenly", "superbly", "superficially", "supposedly", "surely", "surprisingly", "suspiciously", 
    "swiftly", "take away", "take aback", "take-away", "tartly", "terribly", "terrifyingly", "thanfully", "the only", 
    "there", "there's", "thereabout", "thereabouts", "thereafter", "thereat", "therefor", "theres", "tho", "thoroughly", 
    "though", "thoughtfully", "thus", "tightly", "timidly", "tl", "tl;dr", "tldr", "too", "too bright", "too much", 
    "totally", "traditionally", "triumphantly", "truly", "truthfully", "twice", "typically", "ultimately", "uncommonly", 
    "unconsciously", "unexpectedly", "unfairly", "unfortunately", "upward", "usually", "utterly", "vaguely", "vainly", 
    "validly", "variously", "vastly", "very", "very certain", "very confident", "very positive", "very sure", "vigilantly", 
    "violently", "virtually", "vividly", "w/o", "warmly", "weakly", "wearily", "weirdly", "well", "well balanced", 
    "well being", "well known", "when", "whence", "whend", "whenever", "whenll", "whenre", "whenve", "where", "where'd", 
    "where've", "whereby", "whered", "wherefore", "wherein", "whereof", "wherever", "whither", "wholly", "why", "why'd", 
    "why'll", "why're", "why's", "why'vr", "whyd", "whyever", "whyll", "whyre", "whyve", "widely", "wistfully", "without", 
    "wonderfully", "work together", "wrongly", "yet", "yolo"
]  # Example list
ipron = ["you", "your", "yours", "he", "him", "his", "she", "her", "hers"]  # Example list
auxvrb = ["am", "is", "are", "was", "were", "be", "being", "been"]  # Example list
negaincom = ["not", "no", "never", "none"]  # Example list

# Function to count occurrences of specific words
def count_specific_words(text, word_list):
    words = text.split()
    count_dict = {word: 0 for word in word_list}
    for word in words:
        if word in count_dict:
            count_dict[word] += 1
    return count_dict

# Count total words
total_words = count_words(text)
print(f"Total words: {total_words}")

# Count occurrences of specific words
ppron_counts = count_specific_words(text, ppron)
ipron_counts = count_specific_words(text, ipron)
auxvrb_counts = count_specific_words(text, auxvrb)
negaincom_counts = count_specific_words(text, negaincom)

print("Personal pronouns counts:", ppron_counts)
print("Impersonal pronouns counts:", ipron_counts)
print("Auxiliary verbs counts:", auxvrb_counts)
print("Negations and incompleteness counts:", negaincom_counts)
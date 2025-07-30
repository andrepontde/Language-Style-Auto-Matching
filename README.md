# Language Style Matching (LSM) Auto Matcher Bot

## Overview

The LSM Auto Matcher Bot is an advanced natural language processing tool that analyzes the linguistic style of input text and generates responses that match the original Language Style Matching (LSM) characteristics. This project leverages sophisticated text analysis techniques combined with OpenAI's GPT models to create contextually appropriate responses that mirror specific linguistic patterns.

**Developed in collaboration with Daniel Camacho, Master in Applied Psychology**

## 🎯 What is Language Style Matching (LSM)?

Language Style Matching is a psychological concept that measures how similarly two people use function words (pronouns, auxiliary verbs, conjunctions, etc.) in their communication. High LSM scores indicate linguistic synchrony and are associated with:

- Better rapport and communication
- Increased trust and understanding
- Enhanced relationship satisfaction
- Improved collaborative outcomes

## 🚀 Features

- **Advanced Text Analysis**: Analyzes six key linguistic categories that contribute to LSM scores
- **Multi-stage Processing Pipeline**: Implements a sophisticated three-stage processing system
- **OpenAI Integration**: Utilizes GPT-3.5 and GPT-4 models for intelligent text generation
- **Linguistic Pattern Matching**: Maintains specific percentages of function words to match target LSM profiles
- **Psychologically-Informed Design**: Built with insights from applied psychology research

## 🏗️ Architecture

The system follows a three-component architecture pattern:

### 1. **LSMCounter** (Analysis Engine)
- Analyzes input text for linguistic patterns
- Counts occurrences of function words across six categories
- Calculates percentage distributions for each word type
- Provides quantitative LSM metrics

### 2. **LSMGenerator** (Content Processor)
- **Text Cleaning**: Corrects grammar, spelling, and formatting while preserving content
- **Response Generation**: Creates natural, human-like responses using advanced language models
- Maintains original meaning while optimizing for linguistic analysis

### 3. **LSMBaker** (Style Matcher)
- Takes processed content and LSM analysis results
- Generates final responses that match target LSM percentages
- Ensures linguistic style consistency with original input patterns

## 📊 Analyzed Linguistic Categories

The system analyzes six critical function word categories:

1. **Personal Pronouns** (`Ppron.csv`) - I, you, we, they, etc.
2. **Impersonal Pronouns** (`Ipron.csv`) - it, this, that, etc.
3. **Auxiliary Verbs** (`Auxverb.csv`) - am, is, are, have, etc.
4. **Negations** (`Negations.csv`) - no, not, never, etc.
5. **Adverbs** (`Advrb.csv`) - really, very, quite, etc.
6. **Conjunctions** (`Conj.csv`) - and, but, or, etc.

## 🛠️ Installation

### Prerequisites

- Python 3.7+
- OpenAI API key
- PromptLayer API key (optional, for logging)

### Setup

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd Language-Style-Auto-Matching
   ```

2. **Install dependencies**:
   ```bash
   pip install openai promptlayer csv
   ```

3. **Set environment variables**:
   ```bash
   export OPENAI_API_KEY="your-openai-api-key"
   export PROMPTLAYER_API_KEY="your-promptlayer-api-key"  # Optional
   ```

4. **Navigate to project directory**:
   ```bash
   cd "LSM AI Project"
   ```

## 🔧 Usage

### Basic Usage

```python
from Mirror import *

# Run the interactive version
python Mirror.py
```

### Programmatic Usage

```python
from Generator_Mirror import LSMGenerator
from Counter_Mirror import LSMCounter
from Baker_Mirror import LSMBaker

# Your input text
text = "Your input text here"

# Generate LSM analysis
generator = LSMGenerator(text)
counter = LSMCounter(text)

# Get analysis results
occurrences = counter.compute_list()
processed_text = generator.get_output()

# Generate LSM-matched response
baker = LSMBaker(occurrences, processed_text)
final_output = baker.get_output()

print(final_output)
```

## 📈 How It Works

1. **Input Processing**: User provides text for analysis
2. **Linguistic Analysis**: System counts function words across six categories
3. **Content Cleaning**: Text is cleaned and optimized while preserving meaning
4. **Style Analysis**: Original text's linguistic patterns are quantified
5. **Response Generation**: AI generates response matching the original LSM profile
6. **Output Delivery**: Final response maintains both content relevance and style matching

## 🔬 Technical Details

### LSM Calculation
```python
avg = sum(occurrences.values()) / len(text.split()) if len(text.split()) else 0
```

### Style Matching Process
The system uses targeted prompts to ensure generated responses maintain specific percentages of each function word category, creating authentic linguistic mirroring.

### AI Models Used
- **GPT-3.5-turbo-0125**: For text cleaning and initial processing
- **GPT-4o**: For final LSM-matched response generation

## 📚 Research Foundation

This project is built on established research in:
- Psycholinguistics
- Language Style Matching theory
- Computational linguistics
- Human-computer interaction
- Applied psychology

## 🤝 Collaboration

**Academic Collaboration**: This project was developed in partnership with **Daniel Camacho**, Master in Applied Psychology, ensuring the psychological accuracy and research validity of the LSM implementation.

## 📄 File Structure

```
LSM AI Project/
├── Mirror.py              # Main application interface
├── Generator_Mirror.py    # Text processing and cleaning
├── Counter_Mirror.py      # LSM analysis engine
├── Baker_Mirror.py        # Style matching generator
├── WordLists/            # Function word databases
│   ├── Ppron.csv         # Personal pronouns
│   ├── Ipron.csv         # Impersonal pronouns
│   ├── Auxverb.csv       # Auxiliary verbs
│   ├── Negations.csv     # Negation words
│   ├── Advrb.csv         # Adverbs
│   └── Conj.csv          # Conjunctions
└── Old Version/          # Legacy implementations
```

## 🚦 Future Enhancements

- Real-time LSM scoring and feedback
- Multi-language support
- Advanced personality matching
- Integration with communication platforms
- LSM training and coaching features
- Performance analytics and reporting

## 🔒 Privacy & Security

- No text storage beyond processing session
- Secure API key management
- Privacy-first design principles
- Optional logging with PromptLayer

## 📞 Contact

**André Pont** - Primary Developer
**Daniel Camacho** - Applied Psychology Consultant (Master in Applied Psychology)

---

*This project represents a fusion of computational linguistics and applied psychology, creating practical tools for enhancing human communication through linguistic style awareness.*
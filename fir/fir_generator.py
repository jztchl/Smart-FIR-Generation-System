from flair.models import SequenceTagger
from flair.data import Sentence
from nltk.tokenize import sent_tokenize
from collections import Counter

ner_tagger = SequenceTagger.load('ner-fast')  
pos_tagger = SequenceTagger.load('pos')       

def generate_fir(crime_scene, objects, people, text):
   
    sentences = sent_tokenize(text)
    

    flair_text = Sentence(text)
    ner_tagger.predict(flair_text)
    pos_tagger.predict(flair_text)
    
  
    entities = {'PERSON': [], 'LOC': [], 'ORG': [], 'MISC': []}
    for entity in flair_text.get_spans('ner'):
        entities[entity.tag].append(entity.text)
    

    nouns = [token.text for token in flair_text if token.tag in ('NN', 'NNS', 'NNP', 'NNPS')]
    verbs = [token.text for token in flair_text if token.tag.startswith('VB')]
    

    input_objects_lower = [obj.lower() for obj in objects]
    input_people_lower = [p.lower() for p in people]
    key_nouns = [n for n in nouns if n.lower() not in input_objects_lower and n.lower() not in input_people_lower]
    key_verbs = list(set(verbs))  
    

    if len(sentences) <= 5:
        summary_sentences = sentences
    else:
        sentence_scores = {}
        for sent in sentences:
            sent_obj = Sentence(sent)
            ner_tagger.predict(sent_obj)
            entity_count = len(sent_obj.get_spans('ner'))
            sentence_scores[sent] = entity_count + len(word_tokenize(sent)) / 100  #
        summary_sentences = sorted(sentence_scores, key=sentence_scores.get, reverse=True)[:5]
    detailed_summary = " ".join(summary_sentences)
    

    fir_report = f"""
    First Information Report (FIR)
    --------------------------------
    Date: March 04, 2025
    Location of Incident: {crime_scene}
    Objects Involved: {', '.join(objects) if objects else 'None reported'}
    People Involved: {', '.join(people) if people else 'None reported'}
    Detailed Incident Summary: {detailed_summary}
    Extracted Details:
      - Persons Identified: {', '.join(entities['PERSON']) if entities['PERSON'] else 'None additional'}
      - Locations Mentioned: {', '.join(entities['LOC']) if entities['LOC'] else 'None additional'}
      - Organizations Noted: {', '.join(entities['ORG']) if entities['ORG'] else 'None noted'}
      - Other Entities: {', '.join(entities['MISC']) if entities['MISC'] else 'None noted'}
      - Significant Objects: {', '.join(Counter(key_nouns).most_common(5)[::-1]) if key_nouns else 'None beyond listed'}
      - Key Actions: {', '.join(Counter(key_verbs).most_common(5)[::-1]) if key_verbs else 'None extracted'}
    Additional Notes: Investigation ongoing. Awaiting forensic analysis and witness corroboration.
    --------------------------------
    """
    return fir_report.strip()


crime_scene = "Central Park"
objects = ["knife", "bag"]
people = ["John Doe", "Jane Smith"]
text = "A robbery occurred at Central Park late at night. The suspect, John Doe, threatened Jane Smith with a knife. She dropped her bag and fled the scene. Witnesses reported hearing loud shouts around 11 PM. Police arrived shortly after but the suspect had already escaped. A nearby vendor saw a man running with a hood up. The Metro Police Department is coordinating efforts."

print(generate_fir(crime_scene, objects, people, text))
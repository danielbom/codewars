# https://www.codewars.com/kata/papers-please/train/python
# My solution
from collections import defaultdict
import datetime


class Information(object):
    FORMAT_DATE = "%Y.%m.%d"

    def __init__(self, documents):
        self.doc = {}
        self._all = {}
        for doc_name in documents:
            informations = documents[doc_name].splitlines()
            # Removing underscores
            doc_name = doc_name.replace("_", " ")
            self.doc[doc_name] = dict(info.split(": ")
                                      for info in informations)
            # Normalize name, necessary to compare with wanted peoples
            self.doc[doc_name]["NAME"] = self._normalize_name(
                self.doc[doc_name].get("NAME", ""))
            self._all.update(self.doc[doc_name])

    def __repr__(self):
        return str(self._all)

    @property
    def documents(self):
        return list(self.doc.keys())

    def _format_date(self, date):
        return datetime.datetime.strptime(date, self.FORMAT_DATE)

    def _normalize_name(self, name):
        return str.join(" ", reversed(name.split(", "))) if ", " in name else name

    def expired_documents(self, date):
        docs = []
        for doc_name, doc in self.doc.items():
            if self._format_date(date) > self._format_date(doc.get("EXP", date)):
                docs.append(doc_name)
        return docs

    def invalid_values(self):
        values = []
        for document in self.doc.values():
            for info_name, information in document.items():
                if self._all[info_name] != information:
                    values.append(info_name)
        return values


class Inspector(object):
    CITY = "Arstotzka"
    DATE = "1982.11.22"  # November 22, 1982

    ENTRANTS = "Entrants"
    FOREIGNERS = "Foreigners"
    CITIZENS = "Citizens of "

    ALLOW = "Allow citizens of "
    DENY = "Deny citizens of "
    WANTED = "Wanted by the State: "
    REQUIRE = " require "
    NO_LONGER = " no longer"
    VACCINATION = "vaccination"

    KEYS_MAP = {
        "ID#": "ID number",
        "NATION": "nationality",
        "NAME": "name",
        "DOB": "date of birth"
    }

    def __init__(self):
        self.entrants = set()
        self.foreigners = set()
        self.by_nation = defaultdict(set)
        self.nations_allowed = set()
        self.citizens_wanted = set()

    def receive_bulletin(self, bulletin):
        for regulation in bulletin.splitlines():
            if self.ALLOW in regulation:
                self.nations_allowed.update(
                    regulation.replace(self.ALLOW, "").split(", "))
                continue
            if self.DENY in regulation:
                self.nations_allowed.difference_update(
                    regulation.replace(self.DENY, "").split(", "))
                continue
            if self.WANTED in regulation:
                self.citizens_wanted = regulation.replace(
                    self.WANTED, "").split(", ")
                continue
            if self.REQUIRE in regulation:
                self.process_requirement(regulation)

    def process_requirement(self, requirement):
        if self.NO_LONGER in requirement:
            who, req = requirement.split(self.NO_LONGER + self.REQUIRE)
            modifier = set.discard
        else:
            who, req = requirement.split(self.REQUIRE)
            modifier = set.add

        if self.ENTRANTS in who:
            modifier(self.entrants, req)
        elif self.FOREIGNERS in who:
            modifier(self.foreigners, req)
        else:
            nations = who.replace(self.CITIZENS, "").split(", ")
            for nation in nations:
                modifier(self.by_nation[nation], req)

    def missing_documents_entrant(self, documents):
        return [doc for doc in self.entrants if doc not in documents]

    def missing_documents_foreigner(self, documents):
        return [doc for doc in self.foreigners if doc not in documents]

    def missing_documents_for_nation(self, documents, nation):
        return [doc for doc in self.by_nation.get(nation, []) if doc in documents]

    def is_citizen_of(self, informations, city):
        return informations._all.get("NATION") == city

    def inspect(self, entrant):
        informations = Information(entrant)

        for invalid_value in informations.invalid_values():
            if invalid_value in self.KEYS_MAP:
                return "Detainment: {} mismatch.".format(self.KEYS_MAP[invalid_value])

        if informations._all.get("NAME") in self.citizens_wanted:  # Is wanted criminal
            return "Detainment: Entrant is a wanted criminal."

        for expired_document in informations.expired_documents(self.DATE):
            return "Entry denied: {} expired.".format(expired_document)

        nation = informations._all.get("NATION", "")
        documents = informations.documents
        necessary_documents = self.entrants.union(self.by_nation[nation])
        missing_documents = self.missing_documents_for_nation(
            documents, nation)
        missing_documents += self.missing_documents_entrant(documents)
        if not self.is_citizen_of(informations, self.CITY):
            missing_documents += self.missing_documents_foreigner(documents)
            necessary_documents.update(self.foreigners)

        for doc in necessary_documents:
            if self.VACCINATION in doc or doc == "access permit":
                continue
            if doc not in documents:
                return "Entry denied: missing required {}.".format(doc)

        missing_vaccines = False
        for doc in missing_documents:
            if self.VACCINATION in doc:
                certificate = informations.doc.get(
                    "certificate of vaccination", {})
                vaccines = certificate.get("VACCINES", "").split(", ")
                vaccine = doc.replace(" vaccination", "")
                if vaccine not in vaccines:
                    missing_vaccines = True
                continue
            if doc == "access permit" and not informations.doc.get(doc):
                if informations.doc.get("grant of asylum"):
                    continue
                if informations.doc.get("diplomatic authorization"):
                    nations = informations.doc["diplomatic authorization"]["ACCESS"].split(
                        ", ")
                    if self.CITY not in nations:
                        return "Entry denied: invalid diplomatic authorization."
                    continue
            if doc == "ID card":
                if not self.is_citizen_of(informations, self.CITY):
                    continue
                elif informations.doc.get("ID card"):
                    continue
            return "Entry denied: missing required {}.".format(doc)

        if missing_vaccines:
            return "Entry denied: missing required vaccination."

        if informations._all.get("NATION") not in self.nations_allowed:  # Is banned
            return "Entry denied: citizen of banned nation."

        if informations._all.get("PURPOSE") == "WORK" and "work pass" not in documents and self.by_nation.get("Workers"):
            return "Entry denied: missing required work pass."

        if self.is_citizen_of(informations, self.CITY):
            return "Glory to Arstotzka."
        return "Cause no trouble."

    def __str__(self):
        strings = ["Entrants", str(list(self.entrants)),
                   "Foreigners", str(list(self.foreigners)),
                   "Allowed", str(list(self.nations_allowed)),
                   "Wanted", str(list(self.citizens_wanted)),
                   "By nations", str(dict(self.by_nation))]
        return "\n".join(strings)

# And
from collections import defaultdict
from datetime import datetime


class Information(object):
    FORMAT_DATE = "%Y.%m.%d"

    def __init__(self, documents):
        self.doc = {}
        self._all = {}
        for doc_name in documents:
            informations = documents[doc_name].splitlines()
            # Removing underscores
            doc_name = doc_name.replace("_", " ")
            self.doc[doc_name] = dict(info.split(": ") for info in informations)
            # Normalize name, necessary to compare with wanted peoples
            self.doc[doc_name]["NAME"] = self._fname(self.doc[doc_name].get("NAME", ""))
            self._all.update(self.doc[doc_name])

    def get(self, key, default=None):
        return self._all.get(key, default)

    def is_citizen_of(self, city):
        return city == self._all.get("NATION", "")

    @property
    def documents(self):
        return list(self.doc.keys())

    def _fdate(self, date):
        return datetime.strptime(date, self.FORMAT_DATE)

    def _expired(self, d1, d2):
        return self._fdate(d1) > self._fdate(d2)

    def _fname(self, name):
        return " ".join(name.split(", ")[::-1])

    def expired_documents(self, date):
        return [name for name, doc in self.doc.items() if self._expired(date, doc.get("EXP", date))]

    def invalid_values(self):
        values = []
        for document in self.doc.values():
            for info_name, information in document.items():
                if self._all[info_name] != information:
                    values.append(info_name)
        return values


class Inspector(object):
    CITY = "Arstotzka"
    DATE = "1982.11.22"  # November 22, 1982

    ENTRANTS   = "Entrants"
    FOREIGNERS = "Foreigners"
    CITIZENS   = "Citizens of "

    ALLOW       = "Allow citizens of "
    DENY        = "Deny citizens of "
    WANTED      = "Wanted by the State: "
    REQUIRE     = " require "
    NO_LONGER   = " no longer"
    VACCINATION = " vaccination"

    KEYS_MAP = {"ID#": "ID number", "NATION": "nationality", "NAME": "name", "DOB": "date of birth"}

    def __init__(self):
        self.entrants = set()
        self.foreigners = set()
        self.by_nation = defaultdict(set)
        self.nations_allowed = set()
        self.citizens_wanted = set()

    def receive_bulletin(self, bulletin):
        for regulation in bulletin.splitlines():
            if self.ALLOW in regulation:
                self.nations_allowed.update(regulation.replace(self.ALLOW, "").split(", "))
            elif self.DENY in regulation:
                self.nations_allowed.difference_update(regulation.replace(self.DENY, "").split(", "))
            elif self.WANTED in regulation:
                self.citizens_wanted = regulation.replace(self.WANTED, "").split(", ")
            elif self.REQUIRE in regulation:
                self.process_requirement(regulation)

    def process_requirement(self, requirement):
        if self.NO_LONGER in requirement:
            who, req = requirement.split(self.NO_LONGER + self.REQUIRE)
            modifier = set.discard
        else:
            who, req = requirement.split(self.REQUIRE)
            modifier = set.add

        if self.ENTRANTS in who:
            modifier(self.entrants, req)
        elif self.FOREIGNERS in who:
            modifier(self.foreigners, req)
        else:
            nations = who.replace(self.CITIZENS, "").split(", ")
            for nation in nations:
                modifier(self.by_nation[nation], req)

    def inspect(self, entrant):
        info = Information(entrant)
        # Checking for invalid values
        for invalid_value in info.invalid_values():
            if invalid_value in self.KEYS_MAP:
                return f"Detainment: {self.KEYS_MAP[invalid_value]} mismatch."
        # Checking for wanted criminal
        if info.get("NAME") in self.citizens_wanted:
            return "Detainment: Entrant is a wanted criminal."
        # Checking for expired documents
        for expired_document in info.expired_documents(self.DATE):
            return f"Entry denied: {expired_document} expired."
        # Base case of required documents, passport is needed for all entrant
        if not info.doc.get("passport"):
            return "Entry denied: missing required passport."
        # Getting the necessary documents
        nation = info.get("NATION", "")
        necessary_documents = self.entrants.union(self.by_nation[nation])
        if not info.is_citizen_of(self.CITY):
            necessary_documents.update(self.foreigners)
        if info.get("PURPOSE") == "WORK":
            necessary_documents.update(self.by_nation.get("Workers", []))
        # Processing this documents and getting vaccination informations
        documents, vaccines = info.documents, []
        for doc in necessary_documents:
            if self.VACCINATION in doc:
                vaccines.append(doc.replace(" vaccination", ""))
            elif doc not in documents:
                if doc == "access permit":
                    if info.doc.get("grant of asylum"):
                        continue
                    if info.doc.get("diplomatic authorization"):
                        nations = info.doc["diplomatic authorization"]["ACCESS"].split(", ")
                        if self.CITY not in nations:
                            return "Entry denied: invalid diplomatic authorization."
                        continue
                return "Entry denied: missing required {}.".format(doc)
        # Checking for banned nations
        if info.get("NATION") not in self.nations_allowed:
            return "Entry denied: citizen of banned nation."
        # Checking required vaccines
        required_vaccines = info.get("VACCINES", "")
        if required_vaccines:
            certificate = info.doc.get("certificate of vaccination")
            if not certificate:
                return "Entry denied: missing required certificate of vaccination."
            for vaccine in vaccines:
                if vaccine not in required_vaccines.split(", "):
                    return "Entry denied: missing required vaccination."
        # Passed in inpection
        return "Glory to Arstotzka." if info.is_citizen_of(self.CITY) else "Cause no trouble."

# ...
from itertools import combinations
from collections import defaultdict
from datetime import date
import re


EXPIRE_DT          = date(1982,11,22)
NATION             = 'Arstotzka'.lower()
COUNTRIES          = set(map(str.lower, ('Arstotzka', 'Antegria', 'Impor', 'Kolechia', 'Obristan', 'Republia', 'United Federation')))
ACCESS_SUBSTITUTES = {'grant_of_asylum', 'diplomatic_authorization', 'access_permit'}
MISMATCHER         = {'NAME': 'name', 'NATION': 'nationality', 'ID#': 'ID number', 'DOB': 'date of birth'}
P_PAPERS           = re.compile( r'([^:]+): (.+)\n?' )
P_CONSTRAINTS      = re.compile( r'wanted by the state: (?P<wanted>.+)|'
                                 r'(?P<action>allow|deny) citizens of (?P<who>(?:[\w ]+|, )+)|'
                                 r'(?:citizens of )?(?P<who2>.+?)(?P<noMore> no longer)? require (?P<piece>[\w ]+)' )

class Inspector(object):
    
    def __init__(self):
        self.allowed   = {c: False for c in COUNTRIES}
        self.docs      = defaultdict(set)
        self.vacs      = defaultdict(set)
        self.wanted    = None
        self.papers    = None
        self.papersSet = None
        
    
    def receive_bulletin(self, b):
        self.wanted = None
        
        for m in P_CONSTRAINTS.finditer(b.lower()):
            
            if m["wanted"]:
                self.wanted = self.getWantedSet(m["wanted"])
                continue
                
            whos = (m['who'] or m['who2']).split(', ')
            if   whos == ['entrants']:   whos = COUNTRIES
            elif whos == ['foreigners']: whos = COUNTRIES - {NATION}
            
            if m["action"]:
                for country in whos:
                    self.allowed[country] = m["action"] == 'allow'
            else:
                toRemove = m['noMore']
                piece    = m['piece'].replace(' ','_')
                docType  = self.docs
                
                if piece.endswith('vaccination'):
                    piece   = piece.replace('_vaccination','')
                    docType = self.vacs
                elif piece=='id_card': piece = 'ID_card'
                
                for who in whos:
                    if toRemove: docType[who].discard(piece)
                    else:        docType[who].add(piece)
        
        
    def getWantedSet(self,s):   return set(s.replace(',','').split())
    
    def isWanted(self):         return any(self.getWantedSet(p.get('NAME','')) == self.wanted for _,p in self.papers.items())
    
    def isBanned(self,nation):  return not self.allowed.get(nation,0)
    
    def needWorkPass(self):     return ('work_pass' in self.docs['workers']
                                         and 'work' in self.papers.get('access_permit', {}).get('PURPOSE', set()))
    
    def getMismatchedPapers(self):
        for p1,p2 in combinations(self.papers, 2):
            p1,p2 = self.papers[p1], self.papers[p2]
            for k in set(p1) & set(p2) - {'EXP'}:
                if k in MISMATCHER and p1[k] != p2[k]: return MISMATCHER[k]
    
    def getMissingDocs(self,nation):
        required = set(self.docs.get(nation, {'passport'}))
        if self.vacs[nation]:   required.add('certificate_of_vaccination')
        if self.needWorkPass(): required.add('work_pass')
        return required - self.papersSet
    
    
    def inspect(self, papers):
        self.papers    = { k: {x:s.lower() for x,s in P_PAPERS.findall(p)}  for k,p in papers.items()}
        self.papersSet = set(self.papers)
        
        mismatched  = self.getMismatchedPapers()
        nation      = next((p['NATION'] for k,p in self.papers.items() if 'NATION' in p), '').lower()
        isForeign   = nation != NATION
        missingDocs = self.getMissingDocs(nation)
        expiredDocs = next( (k.replace("_", " ") for k,p in self.papers.items()
                             if 'EXP' in p and date(*map(int, p['EXP'].split('.'))) <= EXPIRE_DT), None)
        vaccines    = set(self.papers.get('certificate_of_vaccination', {}).get('VACCINES', '').replace(' ','_').split(',_'))
        misVaccines = self.vacs[nation] - vaccines
        
        isBadDiplo  = False
        if isForeign and 'access_permit' in missingDocs:
            substitute = ACCESS_SUBSTITUTES & self.papersSet
            if substitute: missingDocs.discard('access_permit')
            isBadDiplo = (substitute == {'diplomatic_authorization'} 
                          and NATION not in self.papers['diplomatic_authorization']['ACCESS'])
        
        if self.isWanted():       return  'Detainment: Entrant is a wanted criminal.'
        if mismatched:            return f'Detainment: {mismatched} mismatch.'
        if missingDocs:           return f'Entry denied: missing required {missingDocs.pop().replace("_", " ")}.'
        if isBadDiplo:            return  'Entry denied: invalid diplomatic authorization.'
        if self.isBanned(nation): return  'Entry denied: citizen of banned nation.'
        if expiredDocs:           return f'Entry denied: {expiredDocs} expired.'
        if misVaccines:           return  'Entry denied: missing required vaccination.'
        
        return "Cause no trouble." if isForeign else 'Glory to Arstotzka.'

# ...
import re
class Nation:
    def __init__(self, name):
        self.name = name
        self.isBanned = True
        self.accessPermitRequired = False
        self.workPassRequired = False
        self.idRequired = False
        self.vaccinations = set()
        
class Inspector:
    nations = ['Arstotzka', 'Antegria', 'Impor', 'Kolechia', 'Obristan', 'Republia', 'United Federation']
    
    def __init__(self):
        self.nation_rules = {nation_name: Nation(nation_name) for nation_name in Inspector.nations}
        self.criminals = set()   
        
    def receive_bulletin(self, bulletin):
        def get_nations(line):
            if line.startswith('Entrants'):
                return list(Inspector.nations)
            if line.startswith('Foreigners'):
                return [nation for nation in Inspector.nations if nation != 'Arstotzka']
            return [nation for nation in re.split('[ ,]', line) if nation in Inspector.nations]

        self.criminals = set()
        for line in bulletin.split('\n'):
            if line.startswith('Allow citizens of'):
                allowed_nations = line.replace('Allow citizens of ', '').split(', ')
                for nation in allowed_nations:
                    self.nation_rules[nation].isBanned = False
                    
            elif line.startswith('Deny citizens of'):
                denied_nations = line.replace('Deny citizens of ', '').split(', ')
                for nation in denied_nations:
                    self.nation_rules[nation].isBanned = True
                  
            elif line == 'Entrants require passport':
                for nation in self.nation_rules:
                    self.nation_rules[nation].passportRequired = True
                    
            elif line == 'Foreigners require access permit':
                for nation in self.nation_rules:
                    if nation != 'Arstotzka':
                        self.nation_rules[nation].accessPermitRequired = True
                        
            elif line.startswith('Wanted by the State:'):
                self.criminals.add(line.replace('Wanted by the State: ', ''))
                    
            elif line.endswith('vaccination'):
                disease = re.search('(?<=require )([\w ]+)(?= vaccination)', line).group(0)
                v_nations = get_nations(line)
                for nation in v_nations:
                    if 'no longer' in line and disease in self.nation_rules[nation].vaccinations:
                        self.nation_rules[nation].vaccinations.remove(disease)
                    else:
                        self.nation_rules[nation].vaccinations.add(disease)

            elif line == 'Workers require work pass':
                for nation in self.nation_rules:
                    self.nation_rules[nation].workPassRequired = True
                    
            elif line.endswith('require ID card'):
                id_nations = get_nations(line)
                for nation in id_nations:
                    self.nation_rules[nation].idRequired = True

    def inspect(self, documents):
        def parse_document(document):
            key_pattern = '[A-Z#]+(?=:)'
            value_pattern = '(?<= ).+'
            return {re.match(key_pattern, field).group(0): re.search(value_pattern, field).group(0) for field in document.split('\n')}
            
        def extract_value(documents, value):
            for document in documents:
                if documents[document].get(value, False):
                    return documents[document][value]
            return None
          
        if not documents:
            return 'Entry denied: missing required passport.'
    
        documents = {k: parse_document(v) for k, v in documents.items()}
        id_name = extract_value(documents, 'NAME')
        id_nation = extract_value(documents, 'NATION')
        nation_rules = self.nation_rules[id_nation] if id_nation else {}
        id_num = extract_value(documents, 'ID#')
        id_dob = extract_value(documents, 'DOB')
        id_purpose = extract_value(documents, 'PURPOSE')

        if ' '.join(id_name.split(', ')[::-1]) in self.criminals:
            return 'Detainment: Entrant is a wanted criminal.'
        # document comparisons
        for document in documents:
            if id_nation != documents[document].get('NATION', id_nation):
                return 'Detainment: nationality mismatch.'
            if id_num != documents[document].get('ID#', id_num):
                return 'Detainment: ID number mismatch.'
            if id_name != documents[document].get('NAME', id_name):
                return 'Detainment: name mismatch.'
            if id_dob != documents[document].get('DOB', id_dob):
                return 'Detainment: date of birth mismatch.'
        for document in documents:
            if documents[document].get('EXP', '1982.11.23') <= '1982.11.22':
                return f'Entry denied: {document.replace("_", " ")} expired.'   
        if 'passport' not in documents:
            return 'Entry denied: missing required passport.'
                
        # individual checks
        if nation_rules.accessPermitRequired:
            if 'diplomatic_authorization' in documents:
                if 'Arstotzka' not in documents['diplomatic_authorization']['ACCESS']:
                    return 'Entry denied: invalid diplomatic authorization.'
            elif 'access_permit' not in documents and 'grant_of_asylum' not in documents:
                return 'Entry denied: missing required access permit.'
        if nation_rules.isBanned:
            return 'Entry denied: citizen of banned nation.'
        if nation_rules.vaccinations:
            if 'certificate_of_vaccination' not in documents:
                return 'Entry denied: missing required certificate of vaccination.'
            else:
                required_vaccinations = nation_rules.vaccinations
                specified_vaccinations = set(extract_value(documents, 'VACCINES').split(', '))
                if len(required_vaccinations - specified_vaccinations) != 0:
                    return 'Entry denied: missing required vaccination.'
        if id_purpose == 'WORK' and nation_rules.workPassRequired and 'work_pass' not in documents:
            return 'Entry denied: missing required work pass.'
        if nation_rules.idRequired and 'ID_card' not in documents:
            return 'Entry denied: missing required ID card.'
                
        if id_nation == 'Arstotzka':
            return 'Glory to Arstotzka.'
        return 'Cause no trouble.'

# ...
import re

class Inspector(object):
    NATIONS_LIST = ['arstotzka', 'antegria', 'impor', 'kolechia', 'obristan', 'republia', 'united federation']
    ENTRANT_TYPES = ['entrants', 'workers', 'foreigners'] + NATIONS_LIST
    DOCUMENTS_LIST = ['passport', 'ID card', 'access permit', 'work pass', 'grant of asylum', 'certificate of vaccination', 'diplomatic authorization']
    
    def __init__(self):
        self.nations_rules = dict.fromkeys(Inspector.NATIONS_LIST, 'deny')
        self.required_docs_rules = dict.fromkeys(Inspector.ENTRANT_TYPES, [])
        self.required_vaccinations_rules = dict.fromkeys(Inspector.ENTRANT_TYPES, [])
        self.wanted_criminals = None
        
        '''
        Logic of chosen data structures:
            The rules will be centered around the types of "Entrants"
                
            e.g. for the "Required Docs Rules": 
                {
                     entrants: ['Passport', 'Access Permit'],
                     workers: [],
                     foreigners: [],
                     arstotszka: [],
                     antegria: ['Id_Card'],
                     impor: []
                     ...
                }
        '''
        
    # Create functions to pull entity types, objects, and require/not require from each line of bulletin
    # Selecting of the correct function to pass will be done by the receiveBulletin method.
    # Use: self.update_nations(line)
    def update_nations(self, line):
        nations_in_question = [nation for nation in Inspector.NATIONS_LIST if nation in line]
        instruction = 'allow' if 'allow' in line else 'deny'
        for nation in nations_in_question:
            self.nations_rules[nation] = instruction
        
    def update_required_docs(self, line):
        output = {'entity_types': [],
                  'documents': [],
                  'instruction': None}
        
        # Entity types
        if 'entrants' in line:
            output['entity_types'].append('entrants')
        elif 'foreigners' in line:
            output['entity_types'].append('foreigners')
        elif 'workers' in line:
            output['entity_types'].append('workers')
        else:
            nations_in_question = [nation for nation in Inspector.NATIONS_LIST if nation in line]
            output['entity_types'].extend(nations_in_question)
    
        # Documents
        documents_in_question = [doc for doc in Inspector.DOCUMENTS_LIST if doc in line]
        output['documents'].extend(documents_in_question)
        
        # Instruction
        output['instruction'] = 'no longer require' if 'no longer require' in line else 'require'
                
        # Update Inspector's lists
        # If required...
        if output['instruction'] == 'require':
            for entity_type in output['entity_types']:
                old = self.required_docs_rules[entity_type]
                new = old + output['documents']
                self.required_docs_rules[entity_type] = new
                
        # If no longer required...
        elif output['instruction'] == 'no longer require':
            for entity_type in output['entity_types']:
                remaining = [doc for doc in self.required_docs_rules[entity_type] if doc not in output['documents']]
                self.required_docs_rules[entity_type] = remaining
            
        
    def update_required_vaccinations(self, line):
        output = {'entity_types': [],
                  'vaccinations': [],
                  'instruction': None}
        
        # Entity types
        if 'entrants' in line:
            output['entity_types'].append('entrants')
        elif 'foreigners' in line:
            output['entity_types'].append('foreigners')
        elif 'workers' in line:
            output['entity_types'].append('workers')
        else:
            nations_in_question = [nation for nation in Inspector.NATIONS_LIST if nation in line]
            output['entity_types'].extend(nations_in_question)
    
        # Vaccinations
        vaccinations_in_question = re.findall(r'(?<=require ).*(?= vaccination)', line)
        output['vaccinations'].extend(vaccinations_in_question)
        
        # Instruction
        output['instruction'] = 'no longer require' if 'no longer require' in line else 'require'
        
        # Update Inspector's lists
        # If required...
        if output['instruction'] == 'require':
            for entity_type in output['entity_types']:
                old = self.required_vaccinations_rules[entity_type]
                new = old + output['vaccinations']
                self.required_vaccinations_rules[entity_type] = new
                
                
        # If no longer required...
        elif output['instruction'] == 'no longer require':
            for entity_type in output['entity_types']:
                remaining = [vac for vac in self.required_vaccinations_rules[entity_type] if vac not in output['vaccinations']]
                self.required_vaccinations_rules[entity_type] = remaining
    
    def update_wanted_criminals(self, line):
        self.wanted_criminals = ''.join(re.findall(r'(?<=the state: ).*', line))
    
    def receive_bulletin(self, bulletin):
        print(bulletin)
        lines = [line.lower() for line in bulletin.split('\n')]
        
        for line in lines:
            # Determine whether line relates to vaccinations, nations, docs, criminals
            # and update lists accordingly
            if 'allow citizens' in line or 'deny citizens' in line:
                self.update_nations(line)
            elif 'vaccination' in line:
                self.update_required_vaccinations(line)
            elif 'wanted by the' in line:
                self.update_wanted_criminals(line)
            else:
                self.update_required_docs(line)
                
        no_criminal_updates = True
        for line in lines:
            no_criminal_updates = no_criminal_updates and 'wanted by the' not in line
            
        if no_criminal_updates:
            self.wanted_criminals = None
                
    def inspect(self, entrant):
        
        # Organize/Clean entrant documents
        documents = {}
        unique_fields = set()
        for key in entrant.keys():
            doc = entrant[key]
            fields = re.findall(r'.+(?=:)', doc)
            values = re.findall(r'(?<=: ).+', doc)
            
            for field in fields:
                if field != 'EXP':
                    unique_fields.add(field)
                
            documents[key] = {fields[i]: values[i] for i in range(len(fields))}
            
        # Check if Entrant is Wanted Criminal or if any name matches with criminals
        for key in documents.keys():
            doc = documents[key]
            if 'NAME' in doc.keys():
                entrant_name = doc['NAME']
                sorted_entrant_name = sorted(re.findall(r'\w+', entrant_name))
                if self.wanted_criminals:
                    sorted_criminal_name = [name.title() for name in sorted(re.findall(r'\w+', self.wanted_criminals))]
                    if sorted_entrant_name == sorted_criminal_name:
                        return 'Detainment: Entrant is a wanted criminal.'
            
        # check for mismatches
        matching = True
        for field in list(unique_fields):
            value = None
            for key in documents.keys():
                doc = documents[key]
                if field in doc.keys():
                    value = doc[field] if value is None else value
                    matching = matching and value == doc[field]
        
            if matching is False:
                if field == 'ID#':
                    return 'Detainment: ID number mismatch.'
                elif field == 'NATION':
                    return 'Detainment: nationality mismatch.'
                elif field == 'NAME':
                    return 'Detainment: name mismatch.'
                elif field == 'DOB':
                    return 'Detainment: date of birth mismatch.'
                
        # Lowercase all documents' values
        for key in documents.keys():
            doc = documents[key]
            for field, value in doc.items():
                documents[key][field] = value.lower()
        print(documents)
                        
        # Categorise the Entrant as per entrant types
        entrant_types = {'entrants'}
        for key in documents.keys():
            doc = documents[key]
            if 'NATION' in doc.keys():
                nationality = doc.get('NATION')
                if nationality != 'arstotzka':
                    entrant_types.add('foreigners')
                entrant_types.add(nationality)
                    
            if doc.get('PURPOSE') == 'work':
                entrant_types.add('workers')

                
        # Check if documents are expired
        for key in documents.keys():
            doc = documents[key]
            if 'EXP' in doc.keys():
                YYYY, MM, DD = doc['EXP'].split('.')
                cleaned_key = key.replace('_', ' ')
                if int(YYYY) < 1982:
                    return 'Entry denied: ' + cleaned_key + ' expired.'
                elif int(YYYY) == 1982:
                    if int(MM) < 11:
                        return 'Entry denied: ' + cleaned_key + ' expired.'
                    elif int(MM) == 11:
                        if int(DD) <= 22:
                            return 'Entry denied: ' + cleaned_key + ' expired.'
        
        # Check if all required docs are present
        for entrant_type in list(entrant_types):
            for doc in self.required_docs_rules[entrant_type]:
                required_doc = doc.replace(' ', '_')
                if required_doc not in documents.keys():
                    if required_doc != 'access_permit':
                        return 'Entry denied: missing required ' + doc + '.'
                    else:
                        # if access permit is missing...
                        if 'grant_of_asylum' not in documents.keys():
                            if 'diplomatic_authorization' not in documents.keys():
                                return 'Entry denied: missing required access permit.'
                            else:
                                if 'arstotzka' not in documents['diplomatic_authorization']['ACCESS']:
                                    return 'Entry denied: invalid diplomatic authorization.'
        
            
        # Check if vaccinations are required/acceptable
        for entrant_type in list(entrant_types):
            for required_vac in self.required_vaccinations_rules[entrant_type]:
                if 'certificate_of_vaccination' not in documents.keys():
                    return 'Entry denied: missing required vaccination.'
                else:
                    if required_vac not in documents['certificate_of_vaccination']['VACCINES']:
                        return 'Entry denied: missing required vaccination.'
                    
        # Check if entrants' nationality is allowed
        entrant_nationality = [nation for nation in Inspector.NATIONS_LIST if nation in entrant_types][0]
        if self.nations_rules[entrant_nationality] == 'deny':
            return 'Entry denied: citizen of banned nation.'
                
        # Final Say
        if 'foreigners' in entrant_types:
            return 'Cause no trouble.'
        else:
            return 'Glory to Arstotzka.'

# ...
from collections import defaultdict
from datetime import datetime
from itertools import combinations
class Inspector:

    def __init__(self):
        self.restrictions = defaultdict(list)
        self.vaccines = defaultdict(list)
        self.parse_bulletin = {
            'Allow':      lambda b: __update_restriction('allowed_citizens', parse(b, 'of ')),
            'Citizens':   lambda b: __process_citizen(b, 'no' not in b),
            'Deny':       lambda b: __update_restriction('allowed_citizens', parse(b, 'of '), False),
            'Entrants':   lambda b: __update_restriction('entrants_require', parse(b, 'require '), 'no' not in b),
            'Foreigners': lambda b: __update_restriction('foreigns_require', parse(b, 'require '), 'no' not in b),
            'Wanted':     lambda b: self.restrictions.update({'wanted': wanted(b)}),
            'Workers':    lambda b: __update_restriction('workers_require', parse(b, 'require '), 'no' not in b)
        }
        parse =  lambda b, s: [x.strip() for x in b.partition(s)[-1].split(',')]
        wanted = lambda b: [', '.join(reversed(x.strip().split())) for x in b.split(':')[-1].split(',')]
        
        def __update_restriction(key, rules, extend=True):
            vaccines = [v.replace(' vaccination', '') for v in rules if 'vaccination' in v]
            rules = [r for r in rules if not 'vaccination' in r]
            if extend:
                if rules:
                    self.restrictions[key].extend(rules)
                if vaccines:
                    self.vaccines[key].extend(vaccines)
            else:
                if rules:
                    self.restrictions[key] = [r for r in self.restrictions[key] if r not in rules]
                if vaccines:
                    self.vaccines[key] = [v for v in self.vaccines[key] if v not in vaccines]
        
        def __process_citizen(bulletin, extend):
            parse = lambda b, s: [x.strip() for x in b.partition('of ')[-1].partition(s)]
            if extend:
                parsed = parse(bulletin, 'require ')
            else:
                parsed = parse(bulletin, 'no longer require ')
            for key in [parsed[0]]:
                __update_restriction(key, [parsed[-1]], extend)

    def receive_bulletin(self, bulletins):
        for bulletin in bulletins.split('\n'):
            self.parse_bulletin[bulletin.split()[0]](bulletin)
        
    def inspect(self, papers):
        parser = lambda p: {y[0]: y[1].strip() for y in [x.split(':') for x in p.split('\n')]}
        self.papers = {k: parser(papers[k]) for k in papers.keys()}
        return self._check_mismatch() or self._check_criminal() or self._check_passport() or \
        self._check_expiration() or self._check_diplomatic_authorization() or \
        self._check_work_pass() or self._check_vaccines() or self._check_entrants() or \
        self._check_foreigns() or self._passed()
            
    def _check_expiration(self):
        for paper in self.papers.keys():
            expiry = datetime.strptime(self.papers[paper].get('EXP', '1982.11.23'), '%Y.%m.%d')
            if expiry < datetime(1982, 11, 23):
                return f'Entry denied: {paper.replace("_", " ")} expired.'
                
    def _check_criminal(self):
        for paper in self.papers.keys():
            if self.papers[paper].get('NAME', '') in self.restrictions.get('wanted', ''):
                return 'Detainment: Entrant is a wanted criminal.'
                
    def _check_passport(self):
        if self.papers.get('passport', ''):
            if self.papers['passport']['NATION'] not in self.restrictions.get('allowed_citizens', ''):
                return 'Entry denied: citizen of banned nation.'
        else:
            return 'Entry denied: missing required passport.'
    
    def _passed(self):
        if self.papers.get('passport', ''):
            if self.papers['passport'].get('NATION', '') == 'Arstotzka':
                return 'Glory to Arstotzka.'
        return 'Cause no trouble.'

    def _check_mismatch(self):
        matchers = {'NATION': 'nationality', 'ID#': 'ID number', 'NAME': 'name', 'DOB': 'date of birth'}
        for pap1, pap2 in combinations(self.papers.keys(), 2):
            keys = self.papers[pap1].keys() & self.papers[pap2].keys()
            paper1 = {k: self.papers[pap1][k] for k in keys if k in matchers.keys()}
            paper2 = {k: self.papers[pap2][k] for k in keys if k in matchers.keys()}
            mismatch = list(dict(paper1.items() ^ paper2.items()).keys())
            if mismatch:
                return f'Detainment: {matchers[mismatch[0]]} mismatch.'

    def _check_diplomatic_authorization(self):
        if self.papers.get('diplomatic_authorization', ''):
            access = [c.strip() for c in self.papers['diplomatic_authorization'].get('ACCESS', '').split(',')]
            if not 'Arstotzka' in access:
                return 'Entry denied: invalid diplomatic authorization.'
  
    def _check_work_pass(self):
        if self.papers.get('access_permit', ''):
            if self.papers['access_permit'].get('PURPOSE') == 'WORK' and \
            self.restrictions.get('workers_require', '') and not self.papers.get('work_pass', ''):
                return 'Entry denied: missing required work pass.'
    
    def _check_entrants(self):
        for paper in self.papers.keys():
            nation = self.papers[paper].get('NATION', '')
            entrants = self.restrictions.get('entrants_require', '')
            arstotzka = self.restrictions.get('Arstotzka', '')
            if nation == 'Arstotzka' and entrants:
                mismatch = [p for p in entrants if p.replace(' ', '_') not in self.papers.keys()]
                mismatch.extend(p for p in arstotzka if p.replace(' ', '_') not in self.papers.keys())
                if mismatch:
                    return f'Entry denied: missing required {mismatch[0]}.'

    def _check_foreigns(self):
        for paper in self.papers.keys():
            nation = self.papers[paper].get('NATION', '')
            foreigns = self.restrictions.get('foreigns_require', '')
            if nation and nation != 'Arstotzka' and foreigns:
                mismatch = [p for p in foreigns if p.replace(' ', '_') not in self.papers.keys()]
                if mismatch:
                    if any(k in self.papers.keys() for k in ('grant_of_asylum','diplomatic_authorization')):
                        return
                    return f'Entry denied: missing required {mismatch[0]}.'
                
    def _check_vaccines(self):
        for paper in self.papers.keys():
            nation = self.papers[paper].get('NATION', '')
            vaccination = self.papers.get('certificate_of_vaccination', '')
            if nation in list(self.vaccines.keys()) and not all(v in vaccination for v in self.vaccines[nation]):
                'Entry denied: missing required vaccination.'

# ...
from datetime import date
import re


RECOGNIZED_NATION = {'Arstotzka', 'Antegria', 'Impor', 'Kolechia',
                     'Obristan', 'Republia', 'United Federation'}
HOME = 'Arstotzka'

COMMA_SPLITTER = re.compile(r',\s*')
COLON_SPLITTER = re.compile(r':\s*')
LINE_SPLITTER = re.compile(r'\n*')
DATE_SPLITTER = re.compile(r'\.')
BASE_DATE = date(1982, 11, 22)

parsing_rules = {
    'update to nations':
        re.compile(r'(Allow|Deny) citizens of (.+)'),
    'update to requirements':
        re.compile(r'(.+) require (.+)'),
    'update to wanted dude':
        re.compile(r'Wanted by the (\w+): (.+)')}


def phraser(slang):
    if slang == 'ID#':
        return 'ID number'
    if slang == 'DOB':
        return 'date of birth'
    if slang == 'ISS':
        return ''
    if slang == 'NATION':
        return 'nationality'
    return slang.lower()


def iterable_from_str(string, splitter, klass=set):
    """Return a set from a string given the splitter.

    Args:
        string (str): String representing a list.
        splitter (regex): Regex representing the split item.
        klass (class): returned iterable class

    Returns:
          A ``klass`` of strings.
    """
    return klass(splitter.split(string))


def nations_from_str(nations, home, identifier):
    """Determine the nations of identified by ``qualifier``.

    Args:
        nations (set): Set of all possible nations.
        home (str): String denoting the home nations.
        identifier (str): String qualifying a country or a
            group of countries eg: ``Entrants``.

    Returns:
        Set of identified nations.

    Raises:
        ValueError if ``identifier`` does not represent
        recognized nations.
    """
    if identifier == 'Entrants':
        return nations
    if identifier == 'Foreigners':
        identified_nations = nations.copy()
        identified_nations.discard(home)
        return identified_nations

    if identifier not in nations:
        raise ValueError(f'{identifier} is not a recognized country')
    return {identifier}


def nations_from_iterable(iterable):
    """Determine the nations identified by the element of an iterable.

    Args:
        iterable: Iterable of nations identifiers

    Returns:
        Set of identified nations.
    """
    result = set()
    for qualifier in iterable:
        result.update(nations_from_str(RECOGNIZED_NATION, HOME, qualifier))
    return result


def match_update_from_regex(re_parsing_rules, stmt):
    """Parse an update statement using regexes.

    Args:
        re_parsing_rules (dict): Dictionary containing the rules for
            parsing statements as values and their effects as keys.
        stmt (str): String representing a statement

    Returns:
        A tuple of identified groups that will be parsed further
        to extract specific information.

    >>> match_update_from_regex(parsing_rules,  'Allow citizens of Obristan')
    ('update to nations', ('Allow', 'Obristan'))

    >>> match_update_from_regex(parsing_rules, 'Deny citizens of Kolechia, Republia')
    ('update to nations', ('Deny', 'Kolechia, Republia'))


    >>> match_update_from_regex(parsing_rules, 'Citizens of Arstotzka no longer require ID card')
    ('update to requirements', ('Citizens of Arstotzka no longer', 'ID card'))

    >>> match_update_from_regex(parsing_rules, 'Citizens of Antegria, Republia, Obristan require polio vaccination')
    ('update to requirements', ('Citizens of Antegria, Republia, Obristan', 'polio vaccination'))


    >>> match_update_from_regex(parsing_rules, 'Wanted by the State: Hubert Popovic')
    ('update to wanted dude', ('State', 'Hubert Popovic'))
    """
    for update, pattern in re_parsing_rules.items():
        parse_stmt = pattern.match(stmt)
        if parse_stmt:
            return update, parse_stmt.groups()
    raise TypeError(f'Could not parse {stmt} given the rules')


def requirement_update_type(update_type, update_matched_groups):
    """Determine the type of a requirement update statement.

    Args:
        update_type: string capturing the type of the update (nations, to documents,
            to vaccinations or criminal)
        update_matched_groups: iterable containing the groups matched from parsing a
            requirements statement.

    Returns:
        A list augmented with the type of requirement:
            * ``require`` or ``no longer require``
            * ``vaccinations`` or ``documents``.

    >>> requirement_update_type('update to nations', ('Deny', 'Kolechia, Republia'))
    ['Deny', 'Kolechia, Republia']

    >>> requirement_update_type('update to requirements', ('Citizens of Arstotzka no longer', 'ID card'))
    [False, 'ID card', False, 'Citizens of Arstotzka']

    >>> requirement_update_type('update to requirements', ('Citizens of Antegria, Republia, Obristan', 'polio vaccination'))
    [True, 'polio', True, 'Citizens of Antegria, Republia, Obristan']

    >>> requirement_update_type('update to wanted dude', ('State', 'Hubert Popovic'))
    ['State', 'Hubert Popovic']
    """
    if 'requirements' not in update_type:
        return list(update_matched_groups)

    is_required = 'no longer' not in update_matched_groups[0]
    is_vaccination = 'vaccination' in update_matched_groups[1]
    return [is_required, update_matched_groups[1].replace('vaccination', '').strip(), is_vaccination,
            update_matched_groups[0].replace('no longer', '').strip()]


def update_stmt_target(target):
    """Determine update statement targeted group.

    >>> sorted(update_stmt_target('Citizens of Antegria, Republia, Obristan'))
    ['Antegria', 'Obristan', 'Republia']

    >>> update_stmt_target('Hubert Popovic')
    {'Hubert Popovic'}

    >>> sorted(update_stmt_target('Designers, Programmers'))
    ['Designers', 'Programmers']
    """
    if any((nation_hinter in target
            for nation_hinter in ('Entrants', 'Foreigner', 'Citizens'))):
        target = target.replace('Citizens of', '').strip()

        return nations_from_iterable(iterable_from_str(target, COMMA_SPLITTER, ))
    return iterable_from_str(target, COMMA_SPLITTER, )


def parse_update_from_regex(stmt_parsing_rules, statement):
    """Parse update statement from regexes"""
    update_stmt_type, update_stmt_info = match_update_from_regex(stmt_parsing_rules, statement)
    update_stmt_info = requirement_update_type(update_stmt_type, update_stmt_info)
    update_stmt_info[-1] = update_stmt_target(update_stmt_info[-1])
    return update_stmt_type, update_stmt_info


def disjoint_add(to_set, other_set, values, add=True):
    to_set_copy, other_set_copy = to_set.copy(), other_set.copy()
    if add:
        to_set_copy.update(set(values))
        other_set_copy.difference_update(set(values))
    else:
        to_set_copy.difference_update(set(values))
    return to_set_copy, other_set_copy


def required_papers(group, papers, inplace=None):
    """Determine all the papers required from ``group``.

    >>> required_papers('Obristan',{'access permit': {'Impor', 'Kolechia', 'Obristan'},'work pass': {'Workers'}})
    {'access permit'}

    >>> required_papers('USA',{'access permit': {'Impor', 'Kolechia', 'Obristan'},'work pass': {'Workers'}})
    set()

    >>> required_papers('Workers',{'access permit': {'Impor', 'Kolechia', 'Obristan'},'work pass': {'Workers'}})
    {'work pass'}

    >>> required_papers('Obristan', {'polio': {'Republia', 'Antegria', 'Obristan'}, 'trump': {'United Federation'}}, 'certificate of vaccination')
    {'certificate of vaccination'}

    """
    return {(inplace if inplace else paper) for paper, target in papers.items() if group in target}
  
  
class Papers:

    def __init__(self, papers):
        self.papers = set(papers.keys())
        self._all_info = {(iterable_from_str(info, COLON_SPLITTER, tuple), paper)
                          for paper, content in papers.items()
                          for info in iterable_from_str(content, LINE_SPLITTER,)}
        self._info = None
        self._mismatches = set()

    @property
    def info(self):
        if self._info:
            return self._info

        self._info = {'EXP': set()}

        to_remove = set()
        for entry, paper in self._all_info:
            key = self._info.get(entry[0])
            if entry[0] == 'EXP':
                self._info['EXP'].add((entry[1], paper))
            elif key and key != entry[1]:  # mismatch
                self._mismatches.add(entry[0])
                to_remove.add(entry[0])
            else:
                self._info[entry[0]] = entry[1]

        for data in to_remove:
            self._info.pop(data)
        return self._info

    @property
    def groups(self):
        grps = (self.info.get('NATION'), self.info.get('OCCUPATION'),
                ('Workers' if 'work_pass' in self.papers else None),
                ('Workers' if self.info.get('PURPOSE') == 'WORK' else None))
        return {grp for grp in grps if grp is not None}

    def expired(self, base_date):
        expiry_dates = self.info.get('EXP')
        if expiry_dates:
            return {paper for expiry_date, paper in expiry_dates
                    if date(*(map(int, iterable_from_str(expiry_date, DATE_SPLITTER, tuple)))) <= base_date}
        return set()

    def missing(self, papers, vaccinations=None):
        required = set()
        for group in self.groups:
            required.update(required_papers(group, papers))
            if vaccinations:
                required.update(required_papers(group, vaccinations, 'certificate of vaccination'))
        _missing = {paper for paper in required if paper.replace(' ', '_') not in self.papers}
        self.special_access(_missing)
        return _missing

    def special_access(self, missing):
        if 'access permit' in missing:
            if 'grant_of_asylum' in self.papers:
                missing.discard('access permit')
            elif 'diplomatic_authorization' in self.papers:
                if HOME not in self.info.get('ACCESS'):
                    missing.add('diplomatic authorization')
                missing.discard('access permit')

    def missing_vaccination(self, vaccinations):
        required = set()
        for group in self.groups:
            required.update(required_papers(group, vaccinations))
        return {paper for paper in required if paper not in self.info.get('VACCINES', set())}

    def is_criminal(self, criminals):
        for criminal, wanted_by in criminals.items():
            name = self.info.get('NAME', '').replace(',', '').strip().replace(' ', ', ')
            criminal_name = criminal.replace(',', '').strip().replace(' ', ',')
            if iterable_from_str(name, COMMA_SPLITTER) == iterable_from_str(criminal_name, COMMA_SPLITTER):
                return True
        return False


class Inspector:

    def __init__(self):
        self._regulations = {
            'nations': (set(), set()),
            'documents': {},
            'vaccines': {},
            'criminal': {}
        }

    def receive_bulletin(self, bulletin):

        self._regulations['criminal'] = {}
        
        for stmt in bulletin.split('\n'):
            stmt = stmt.strip()
            parsing_result = parse_update_from_regex(parsing_rules, stmt)

            if 'nations' in parsing_result[0]:
                if 'Allow' == parsing_result[1][0]:
                    self._regulations['nations'] = disjoint_add(*self._regulations['nations'], parsing_result[1][1])
                else:
                    deny, allow = disjoint_add(*reversed(self._regulations['nations']), parsing_result[1][1])
                    self._regulations['nations'] = (allow, deny)

            elif 'requirements' in parsing_result[0]:
                req_type = 'vaccines' if parsing_result[1][2] else 'documents'
                group = self._regulations[req_type].get(parsing_result[1][1]) or set()
                if parsing_result[1][0]:
                    group.update(parsing_result[1][-1])
                else:
                    group.difference_update(parsing_result[1][-1])
                self._regulations[req_type][parsing_result[1][1]] = group
            else:
                name = ' '.join(sorted(parsing_result[1][-1].pop().split()))
                self._regulations['criminal'][name] = parsing_result[1][0]

    def inspect(self, person):
        papers = Papers(person)

        # Check criminality
        if papers.is_criminal(self._regulations['criminal']):
            return 'Detainment: Entrant is a wanted criminal.'

        dummy = papers.info  # dummy is useless this is just to fill papers._info set papers._mismatches

        # Check consistency
        if papers._mismatches != set():
            return f'Detainment: {phraser(papers._mismatches.pop())} mismatch.'

        # Check if nation is denied
        if papers.info.get('NATION') in self._regulations['nations'][1]:
            return f'Entry denied: citizen of banned nation.'
        
        if papers.info.get('NATION'):
            if HOME in self._regulations['nations'][0] and papers.info.get('NATION') not in self._regulations['nations'][0]:
                return f'Entry denied: citizen of banned nation.'
            
        # Check missing documents
        missing = papers.missing(self._regulations['documents'],
                                 (None if self._regulations['vaccines'] == {} else self._regulations['vaccines']))
        if not papers.info.get('NATION'):
            missing.add('passport')
        if missing != set():
            what = 'passport' if 'passport' in missing else missing.pop()
            if what != 'diplomatic authorization':
                reason = f"missing required {what}"
            else:
                reason = 'invalid diplomatic authorization'
            if not (what == 'access permit' and papers.info.get('NATION') in self._regulations['nations'][0]):
                return f'Entry denied: {reason}.'

        # Check expired document
        expired = papers.expired(BASE_DATE)
        if expired != set():
            paper = expired.pop()
            return f"Entry denied: {paper.replace('_', ' ')} expired."

        # Check missing vaccination
        missing = papers.missing_vaccination(self._regulations['vaccines'])
        if missing != set():
            return 'Entry denied: missing required vaccination.'

        # Welcome back home
        if papers.info.get('NATION') == HOME:
            return f'Glory to {HOME}.'
        # Welcome fellow
        return 'Cause no trouble.'

# ...
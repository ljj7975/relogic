READING_COMPREHENSION_TASKS = ["squad11", "squad20"]
AUTO_SPAN = ["auto_span_srl"]
NEVER_SPLIT = ("[UNK]", "[SEP]", "[PAD]", "[CLS]", "[MASK]",
              '[ORGANIZATION-SUBJ]', '[PERSON-OBJ]', '[PERSON-SUBJ]',
              '[ORGANIZATION-OBJ]', '[NUMBER-OBJ]', '[DATE-OBJ]',
              '[NATIONALITY-OBJ]', '[LOCATION-OBJ]', '[TITLE-OBJ]',
              '[CITY-OBJ]', '[MISC-OBJ]', '[COUNTRY-OBJ]',
              '[CRIMINAL_CHARGE-OBJ]', '[RELIGION-OBJ]',
              '[DURATION-OBJ]', '[URL-OBJ]', '[STATE_OR_PROVINCE-OBJ]',
              '[IDEOLOGY-OBJ]', '[CAUSE_OF_DEATH-OBJ]')

SRL_TASK = "joint_srl"
SRL_LABEL_SPAN_BASED = "srl_label_span_based"
SRL_LABEL_SEQ_BASED = "srl_label_seq_based"
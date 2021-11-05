all: sent tuple

.PHONY: clean
clean:
	rm data/processed/*

sent: data/processed/train_bengali.sent data/processed/test_bengali.sent data/processed/valid_bengali.sent data/processed/test_hindi.sent data/processed/train_hindi.sent

tuple: data/processed/train_bengali.tuple data/processed/test_bengali.tuple data/processed/valid_bengali.tuple data/processed/test_hindi.tuple data/processed/train_hindi.tuple

data/processed/train_bengali.sent: data/unzipped/beng_ee/train_bengali scripts/parser.py
	python3 scripts/parser.py sent data/unzipped/beng_ee/train_bengali > data/processed/train_bengali.sent

data/processed/test_bengali.sent: data/unzipped/beng_ee/test_bengali scripts/parser.py
	python3 scripts/parser.py sent data/unzipped/beng_ee/test_bengali > data/processed/test_bengali.sent

data/processed/valid_bengali.sent: data/unzipped/beng_ee/valid_bengali scripts/parser.py
	python3 scripts/parser.py sent data/unzipped/beng_ee/valid_bengali > data/processed/valid_bengali.sent

data/processed/train_hindi.sent: data/unzipped/hindi_ee/train scripts/parser.py
	python3 scripts/parser.py sent data/unzipped/hindi_ee/train > data/processed/train_hindi.sent

data/processed/test_hindi.sent: data/unzipped/hindi_ee/test scripts/parser.py
	python3 scripts/parser.py sent data/unzipped/hindi_ee/test > data/processed/test_hindi.sent

data/processed/train_bengali.tuple: data/unzipped/beng_ee/train_bengali scripts/parser.py
	python3 scripts/parser.py tuple data/unzipped/beng_ee/train_bengali > data/processed/train_bengali.tuple

data/processed/test_bengali.tuple: data/unzipped/beng_ee/test_bengali scripts/parser.py
	python3 scripts/parser.py tuple data/unzipped/beng_ee/test_bengali > data/processed/test_bengali.tuple

data/processed/valid_bengali.tuple: data/unzipped/beng_ee/valid_bengali scripts/parser.py
	python3 scripts/parser.py tuple data/unzipped/beng_ee/valid_bengali > data/processed/valid_bengali.tuple

data/processed/train_hindi.tuple: data/unzipped/hindi_ee/train scripts/parser.py
	python3 scripts/parser.py tuple data/unzipped/hindi_ee/train > data/processed/train_hindi.tuple

data/processed/test_hindi.tuple: data/unzipped/hindi_ee/test scripts/parser.py
	python3 scripts/parser.py tuple data/unzipped/hindi_ee/test > data/processed/test_hindi.tuple
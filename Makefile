all: sent tuple pointer cleanup event_arg_gen sent_len

.PHONY: clean
clean:
	rm data/processed/*

.PHONY: sent_len
sent_len: cleanup
	@python3 scripts/get_sent_len.py data/processed/train_bengali.sent
	@python3 scripts/get_sent_len.py data/processed/test_bengali.sent
	@python3 scripts/get_sent_len.py data/processed/valid_bengali.sent
	@python3 scripts/get_sent_len.py data/processed/train_hindi.sent
	@python3 scripts/get_sent_len.py data/processed/test_hindi.sent
	@python3 scripts/get_sent_len.py data/processed/valid_hindi.sent



event_arg_gen: scripts/event_arg_gen.sh cleanup
	sh scripts/event_arg_gen.sh data/processed

cleanup: sent tuple pointer
	python3 scripts/cleanup.py data/processed/test_bengali
	python3 scripts/cleanup.py data/processed/train_bengali
	python3 scripts/cleanup.py data/processed/valid_bengali
	python3 scripts/cleanup.py data/processed/test_hindi
	python3 scripts/cleanup.py data/processed/train_hindi
	python3 scripts/cleanup.py data/processed/valid_hindi

sent: data/processed/train_bengali.sent data/processed/test_bengali.sent data/processed/valid_bengali.sent data/processed/test_hindi.sent data/processed/train_hindi.sent data/processed/valid_hindi.sent

tuple: data/processed/train_bengali.tuple data/processed/test_bengali.tuple data/processed/valid_bengali.tuple data/processed/test_hindi.tuple data/processed/train_hindi.tuple data/processed/valid_hindi.tuple

pointer: data/processed/train_bengali.pointer data/processed/test_bengali.pointer data/processed/valid_bengali.pointer data/processed/test_hindi.pointer data/processed/train_hindi.pointer data/processed/valid_hindi.pointer

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

data/processed/valid_hindi.sent: data/unzipped/hindi_ee/valid scripts/parser.py
	python3 scripts/parser.py sent data/unzipped/hindi_ee/valid > data/processed/valid_hindi.sent

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

data/processed/valid_hindi.tuple: data/unzipped/hindi_ee/valid scripts/parser.py
	python3 scripts/parser.py tuple data/unzipped/hindi_ee/valid > data/processed/valid_hindi.tuple

data/processed/train_bengali.pointer: data/unzipped/beng_ee/train_bengali scripts/parser.py
	python3 scripts/parser.py pointer data/unzipped/beng_ee/train_bengali > data/processed/train_bengali.pointer

data/processed/test_bengali.pointer: data/unzipped/beng_ee/test_bengali scripts/parser.py
	python3 scripts/parser.py pointer data/unzipped/beng_ee/test_bengali > data/processed/test_bengali.pointer

data/processed/valid_bengali.pointer: data/unzipped/beng_ee/valid_bengali scripts/parser.py
	python3 scripts/parser.py pointer data/unzipped/beng_ee/valid_bengali > data/processed/valid_bengali.pointer

data/processed/train_hindi.pointer: data/unzipped/hindi_ee/train scripts/parser.py
	python3 scripts/parser.py pointer data/unzipped/hindi_ee/train > data/processed/train_hindi.pointer

data/processed/test_hindi.pointer: data/unzipped/hindi_ee/test scripts/parser.py
	python3 scripts/parser.py pointer data/unzipped/hindi_ee/test > data/processed/test_hindi.pointer

data/processed/valid_hindi.pointer: data/unzipped/hindi_ee/valid scripts/parser.py
	python3 scripts/parser.py pointer data/unzipped/hindi_ee/valid > data/processed/valid_hindi.pointer
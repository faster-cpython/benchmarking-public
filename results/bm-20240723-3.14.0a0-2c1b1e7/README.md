# Results

- fork: python
- version: 3.14.0a0
- config: 
- commit hash: [2c1b1e7](https://github.com/python/cpython/commit/2c1b1e7)
- commit date: 2024-07-23T15:17:13+02:00
- commit merge base: [624bda76386efd8eecf73c4ad06f997b9b25f07f](https://github.com/python/cpython/commit/624bda76386efd8eecf73c4ad06f997b9b25f07f)
- ref: 2c1b1e7a07eba0138b98

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10060196265)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20240723-arminc-aarch64-python-2c1b1e7a07eba0138b98-3.14.0a0-2c1b1e7.json)

### vs. 3.10.4

- Geometric mean: 1.34x faster (HPT: reliability of 100.00%, 1.23x faster at 99th %ile)
- Memory usage: 1.14x
- missing benchmarks: aiohttp, chameleon, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240723-arminc-aarch64-python-2c1b1e7a07eba0138b98-3.14.0a0-2c1b1e7-vs-3.10.4.md)
- [📈time plot](bm-20240723-arminc-aarch64-python-2c1b1e7a07eba0138b98-3.14.0a0-2c1b1e7-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.03x faster (HPT: reliability of 93.18%, 1.00x faster at 99th %ile)
- Memory usage: 0.93x
- missing benchmarks: aiohttp, chameleon, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser
- [📄table](bm-20240723-arminc-aarch64-python-2c1b1e7a07eba0138b98-3.14.0a0-2c1b1e7-vs-3.12.0.md)
- [📈time plot](bm-20240723-arminc-aarch64-python-2c1b1e7a07eba0138b98-3.14.0a0-2c1b1e7-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.02x faster (HPT: reliability of 100.00%, 1.00x faster at 99th %ile)
- Memory usage: 1.01x
- missing benchmarks: aiohttp, chameleon, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list
- [📄table](bm-20240723-arminc-aarch64-python-2c1b1e7a07eba0138b98-3.14.0a0-2c1b1e7-vs-3.13.0b2.md)
- [📈time plot](bm-20240723-arminc-aarch64-python-2c1b1e7a07eba0138b98-3.14.0a0-2c1b1e7-vs-3.13.0b2.svg)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10060196265)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-186-generic-x86_64-with-glibc2.31
- [raw results](bm-20240723-linux-x86_64-python-2c1b1e7a07eba0138b98-3.14.0a0-2c1b1e7.json)

### vs. 3.10.4

- Geometric mean: 1.44x faster (HPT: reliability of 100.00%, 1.30x faster at 99th %ile)
- Memory usage: 1.12x
- missing benchmarks: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240723-linux-x86_64-python-2c1b1e7a07eba0138b98-3.14.0a0-2c1b1e7-vs-3.10.4.md)
- [📈time plot](bm-20240723-linux-x86_64-python-2c1b1e7a07eba0138b98-3.14.0a0-2c1b1e7-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.09x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: 0.98x
- missing benchmarks: aiohttp, chameleon, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240723-linux-x86_64-python-2c1b1e7a07eba0138b98-3.14.0a0-2c1b1e7-vs-3.12.0.md)
- [📈time plot](bm-20240723-linux-x86_64-python-2c1b1e7a07eba0138b98-3.14.0a0-2c1b1e7-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.06x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: 1.01x
- missing benchmarks: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list
- [📄table](bm-20240723-linux-x86_64-python-2c1b1e7a07eba0138b98-3.14.0a0-2c1b1e7-vs-3.13.0b2.md)
- [📈time plot](bm-20240723-linux-x86_64-python-2c1b1e7a07eba0138b98-3.14.0a0-2c1b1e7-vs-3.13.0b2.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10060196265)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-105-generic-x86_64-with-glibc2.35
- [raw results](bm-20240723-pythonperf2-x86_64-python-2c1b1e7a07eba0138b98-3.14.0a0-2c1b1e7.json)

### vs. 3.10.4

- Geometric mean: 1.35x faster (HPT: reliability of 100.00%, 1.23x faster at 99th %ile)
- Memory usage: 1.12x
- missing benchmarks: aiohttp, chameleon, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240723-pythonperf2-x86_64-python-2c1b1e7a07eba0138b98-3.14.0a0-2c1b1e7-vs-3.10.4.md)
- [📈time plot](bm-20240723-pythonperf2-x86_64-python-2c1b1e7a07eba0138b98-3.14.0a0-2c1b1e7-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.02x faster (HPT: reliability of 82.05%, 1.00x faster at 99th %ile)
- Memory usage: 0.93x
- missing benchmarks: aiohttp, chameleon, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240723-pythonperf2-x86_64-python-2c1b1e7a07eba0138b98-3.14.0a0-2c1b1e7-vs-3.12.0.md)
- [📈time plot](bm-20240723-pythonperf2-x86_64-python-2c1b1e7a07eba0138b98-3.14.0a0-2c1b1e7-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.02x faster (HPT: reliability of 99.85%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- missing benchmarks: aiohttp, chameleon, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list
- [📄table](bm-20240723-pythonperf2-x86_64-python-2c1b1e7a07eba0138b98-3.14.0a0-2c1b1e7-vs-3.13.0b2.md)
- [📈time plot](bm-20240723-pythonperf2-x86_64-python-2c1b1e7a07eba0138b98-3.14.0a0-2c1b1e7-vs-3.13.0b2.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10060196265)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20240723-pythonperf1-amd64-python-2c1b1e7a07eba0138b98-3.14.0a0-2c1b1e7.json)

### vs. 3.10.4

- Geometric mean: 1.23x faster (HPT: reliability of 100.00%, 1.13x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240723-pythonperf1-amd64-python-2c1b1e7a07eba0138b98-3.14.0a0-2c1b1e7-vs-3.10.4.md)
- [📈time plot](bm-20240723-pythonperf1-amd64-python-2c1b1e7a07eba0138b98-3.14.0a0-2c1b1e7-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.04x faster (HPT: reliability of 79.39%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240723-pythonperf1-amd64-python-2c1b1e7a07eba0138b98-3.14.0a0-2c1b1e7-vs-3.12.0.md)
- [📈time plot](bm-20240723-pythonperf1-amd64-python-2c1b1e7a07eba0138b98-3.14.0a0-2c1b1e7-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.01x slower (HPT: reliability of 100.00%, 1.04x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dulwich_log, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list
- [📄table](bm-20240723-pythonperf1-amd64-python-2c1b1e7a07eba0138b98-3.14.0a0-2c1b1e7-vs-3.13.0b2.md)
- [📈time plot](bm-20240723-pythonperf1-amd64-python-2c1b1e7a07eba0138b98-3.14.0a0-2c1b1e7-vs-3.13.0b2.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10060196265)
- cpu model: missing
- platform: macOS-14.5-arm64-arm-64bit-Mach-O
- [raw results](bm-20240723-darwin-arm64-python-2c1b1e7a07eba0138b98-3.14.0a0-2c1b1e7.json)

### vs. 3.10.4

- Geometric mean: 1.30x faster (HPT: reliability of 100.00%, 1.18x faster at 99th %ile)
- Memory usage: 0.82x
- missing benchmarks: aiohttp, chameleon, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240723-darwin-arm64-python-2c1b1e7a07eba0138b98-3.14.0a0-2c1b1e7-vs-3.10.4.md)
- [📈time plot](bm-20240723-darwin-arm64-python-2c1b1e7a07eba0138b98-3.14.0a0-2c1b1e7-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.09x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: 0.80x
- missing benchmarks: aiohttp, chameleon, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240723-darwin-arm64-python-2c1b1e7a07eba0138b98-3.14.0a0-2c1b1e7-vs-3.12.0.md)
- [📈time plot](bm-20240723-darwin-arm64-python-2c1b1e7a07eba0138b98-3.14.0a0-2c1b1e7-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.01x faster (HPT: reliability of 99.21%, 1.00x slower at 99th %ile)
- Memory usage: 0.62x
- missing benchmarks: aiohttp, chameleon, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list
- [📄table](bm-20240723-darwin-arm64-python-2c1b1e7a07eba0138b98-3.14.0a0-2c1b1e7-vs-3.13.0b2.md)
- [📈time plot](bm-20240723-darwin-arm64-python-2c1b1e7a07eba0138b98-3.14.0a0-2c1b1e7-vs-3.13.0b2.svg)


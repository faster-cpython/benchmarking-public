# Results

- fork: python
- version: 3.14.0a0
- config: 
- commit hash: [79c542b](https://github.com/python/cpython/commit/79c542b)
- commit date: 2024-08-17T20:58:06+00:00
- commit merge base: [d061ffea7b408861d0a9d311e92c363da284971d](https://github.com/python/cpython/commit/d061ffea7b408861d0a9d311e92c363da284971d)
- ref: 79c542b5cc774ba758ac

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10436129942)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20240817-arminc-aarch64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b.json)

### vs. 3.10.4

- Geometric mean: 1.34x faster (HPT: reliability of 100.00%, 1.21x faster at 99th %ile)
- Memory usage: 1.15x
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240817-arminc-aarch64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b-vs-3.10.4.md)
- [📈time plot](bm-20240817-arminc-aarch64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.04x faster (HPT: reliability of 95.99%, 1.00x faster at 99th %ile)
- Memory usage: 0.94x
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser
- [📄table](bm-20240817-arminc-aarch64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b-vs-3.12.0.md)
- [📈time plot](bm-20240817-arminc-aarch64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.02x faster (HPT: reliability of 97.99%, 1.00x faster at 99th %ile)
- Memory usage: 1.01x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20240817-arminc-aarch64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b-vs-3.13.0.md)
- [📈time plot](bm-20240817-arminc-aarch64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b-vs-3.13.0.svg)

### vs. 3.13.0b2

- [📄table](bm-20240817-arminc-aarch64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b-vs-3.13.0b2.md)
- [📈time plot](bm-20240817-arminc-aarch64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b-vs-3.13.0b2.svg)

## linux x86_64 (azure)

- [pystats raw](bm-20240817-azure-x86_64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b-pystats.json)
- [pystats table](bm-20240817-azure-x86_64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b-pystats.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10436129942)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-192-generic-x86_64-with-glibc2.31
- [raw results](bm-20240817-linux-x86_64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b.json)

### vs. 3.10.4

- Geometric mean: 1.43x faster (HPT: reliability of 100.00%, 1.30x faster at 99th %ile)
- Memory usage: 1.12x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240817-linux-x86_64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b-vs-3.10.4.md)
- [📈time plot](bm-20240817-linux-x86_64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.08x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: 0.98x
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240817-linux-x86_64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b-vs-3.12.0.md)
- [📈time plot](bm-20240817-linux-x86_64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.01x faster (HPT: reliability of 86.41%, 1.00x faster at 99th %ile)
- Memory usage: 1.01x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20240817-linux-x86_64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b-vs-3.13.0.md)
- [📈time plot](bm-20240817-linux-x86_64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b-vs-3.13.0.svg)

### vs. 3.13.0b2

- [📄table](bm-20240817-linux-x86_64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b-vs-3.13.0b2.md)
- [📈time plot](bm-20240817-linux-x86_64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b-vs-3.13.0b2.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10436129942)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-105-generic-x86_64-with-glibc2.35
- [raw results](bm-20240817-pythonperf2-x86_64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b.json)

### vs. 3.10.4

- Geometric mean: 1.36x faster (HPT: reliability of 100.00%, 1.23x faster at 99th %ile)
- Memory usage: 1.13x
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240817-pythonperf2-x86_64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b-vs-3.10.4.md)
- [📈time plot](bm-20240817-pythonperf2-x86_64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.03x faster (HPT: reliability of 76.22%, 1.00x faster at 99th %ile)
- Memory usage: 0.93x
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240817-pythonperf2-x86_64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b-vs-3.12.0.md)
- [📈time plot](bm-20240817-pythonperf2-x86_64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.03x faster (HPT: reliability of 100.00%, 1.01x faster at 99th %ile)
- Memory usage: 1.01x
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20240817-pythonperf2-x86_64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b-vs-3.13.0.md)
- [📈time plot](bm-20240817-pythonperf2-x86_64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b-vs-3.13.0.svg)

### vs. 3.13.0b2

- [📄table](bm-20240817-pythonperf2-x86_64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b-vs-3.13.0b2.md)
- [📈time plot](bm-20240817-pythonperf2-x86_64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b-vs-3.13.0b2.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10436129942)
- cpu model: missing
- platform: macOS-14.6.1-arm64-arm-64bit-Mach-O
- [raw results](bm-20240817-darwin-arm64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b.json)

### vs. 3.10.4

- Geometric mean: 1.31x faster (HPT: reliability of 100.00%, 1.19x faster at 99th %ile)
- Memory usage: 0.59x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240817-darwin-arm64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b-vs-3.10.4.md)
- [📈time plot](bm-20240817-darwin-arm64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.09x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: 0.48x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240817-darwin-arm64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b-vs-3.12.0.md)
- [📈time plot](bm-20240817-darwin-arm64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.09x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: 0.99x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20240817-darwin-arm64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b-vs-3.13.0.md)
- [📈time plot](bm-20240817-darwin-arm64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b-vs-3.13.0.svg)

### vs. 3.13.0b2

- [📄table](bm-20240817-darwin-arm64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b-vs-3.13.0b2.md)
- [📈time plot](bm-20240817-darwin-arm64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b-vs-3.13.0b2.svg)


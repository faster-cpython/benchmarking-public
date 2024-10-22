# Results

- fork: python
- version: 3.14.0a0
- config: NOGIL
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

- Geometric mean: 1.22x slower (HPT: reliability of 100.00%, 1.18x slower at 99th %ile)
- Memory usage: 1.32x
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240817-arminc-aarch64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b-vs-3.10.4.md)
- [📈time plot](bm-20240817-arminc-aarch64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.57x slower (HPT: reliability of 100.00%, 1.38x slower at 99th %ile)
- Memory usage: 1.07x
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser
- [📄table](bm-20240817-arminc-aarch64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b-vs-3.12.0.md)
- [📈time plot](bm-20240817-arminc-aarch64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.59x slower (HPT: reliability of 100.00%, 1.41x slower at 99th %ile)
- Memory usage: 1.16x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20240817-arminc-aarch64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b-vs-3.13.0.md)
- [📈time plot](bm-20240817-arminc-aarch64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.62x slower (HPT: reliability of 100.00%, 1.44x slower at 99th %ile)
- Memory usage: 1.15x
- [🧠memory plot](bm-20240817-arminc-aarch64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b-vs-base-mem.svg)
- [📄table](bm-20240817-arminc-aarch64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b-vs-base.md)
- [📈time plot](bm-20240817-arminc-aarch64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b-vs-base.svg)

### vs. 3.13.0b2

- [📄table](bm-20240817-arminc-aarch64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b-vs-3.13.0b2.md)
- [📈time plot](bm-20240817-arminc-aarch64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b-vs-3.13.0b2.svg)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10436129942)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-192-generic-x86_64-with-glibc2.31
- [raw results](bm-20240817-linux-x86_64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b.json)

### vs. 3.10.4

- Geometric mean: 1.04x slower (HPT: reliability of 99.94%, 1.02x slower at 99th %ile)
- Memory usage: 1.29x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240817-linux-x86_64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b-vs-3.10.4.md)
- [📈time plot](bm-20240817-linux-x86_64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.36x slower (HPT: reliability of 100.00%, 1.22x slower at 99th %ile)
- Memory usage: 1.13x
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240817-linux-x86_64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b-vs-3.12.0.md)
- [📈time plot](bm-20240817-linux-x86_64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.45x slower (HPT: reliability of 100.00%, 1.30x slower at 99th %ile)
- Memory usage: 1.16x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20240817-linux-x86_64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b-vs-3.13.0.md)
- [📈time plot](bm-20240817-linux-x86_64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.47x slower (HPT: reliability of 100.00%, 1.31x slower at 99th %ile)
- Memory usage: 1.14x
- [🧠memory plot](bm-20240817-linux-x86_64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b-vs-base-mem.svg)
- [📄table](bm-20240817-linux-x86_64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b-vs-base.md)
- [📈time plot](bm-20240817-linux-x86_64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b-vs-base.svg)

### vs. 3.13.0b2

- [📄table](bm-20240817-linux-x86_64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b-vs-3.13.0b2.md)
- [📈time plot](bm-20240817-linux-x86_64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b-vs-3.13.0b2.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10436129942)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-105-generic-x86_64-with-glibc2.35
- [raw results](bm-20240817-pythonperf2-x86_64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b.json)

### vs. 3.10.4

- Geometric mean: 1.12x slower (HPT: reliability of 100.00%, 1.08x slower at 99th %ile)
- Memory usage: 1.31x
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240817-pythonperf2-x86_64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b-vs-3.10.4.md)
- [📈time plot](bm-20240817-pythonperf2-x86_64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.46x slower (HPT: reliability of 100.00%, 1.28x slower at 99th %ile)
- Memory usage: 1.08x
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240817-pythonperf2-x86_64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b-vs-3.12.0.md)
- [📈time plot](bm-20240817-pythonperf2-x86_64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.46x slower (HPT: reliability of 100.00%, 1.32x slower at 99th %ile)
- Memory usage: 1.17x
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20240817-pythonperf2-x86_64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b-vs-3.13.0.md)
- [📈time plot](bm-20240817-pythonperf2-x86_64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.50x slower (HPT: reliability of 100.00%, 1.36x slower at 99th %ile)
- Memory usage: 1.15x
- [🧠memory plot](bm-20240817-pythonperf2-x86_64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b-vs-base-mem.svg)
- [📄table](bm-20240817-pythonperf2-x86_64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b-vs-base.md)
- [📈time plot](bm-20240817-pythonperf2-x86_64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b-vs-base.svg)

### vs. 3.13.0b2

- [📄table](bm-20240817-pythonperf2-x86_64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b-vs-3.13.0b2.md)
- [📈time plot](bm-20240817-pythonperf2-x86_64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b-vs-3.13.0b2.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10436129942)
- cpu model: missing
- platform: macOS-14.6.1-arm64-arm-64bit-Mach-O
- [raw results](bm-20240817-darwin-arm64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b.json)

### vs. 3.10.4

- Geometric mean: 1.19x slower (HPT: reliability of 100.00%, 1.15x slower at 99th %ile)
- Memory usage: 0.52x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240817-darwin-arm64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b-vs-3.10.4.md)
- [📈time plot](bm-20240817-darwin-arm64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.40x slower (HPT: reliability of 100.00%, 1.22x slower at 99th %ile)
- Memory usage: 0.47x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240817-darwin-arm64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b-vs-3.12.0.md)
- [📈time plot](bm-20240817-darwin-arm64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.38x slower (HPT: reliability of 100.00%, 1.25x slower at 99th %ile)
- Memory usage: 0.99x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20240817-darwin-arm64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b-vs-3.13.0.md)
- [📈time plot](bm-20240817-darwin-arm64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.51x slower (HPT: reliability of 100.00%, 1.28x slower at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20240817-darwin-arm64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b-vs-base-mem.svg)
- [📄table](bm-20240817-darwin-arm64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b-vs-base.md)
- [📈time plot](bm-20240817-darwin-arm64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b-vs-base.svg)

### vs. 3.13.0b2

- [📄table](bm-20240817-darwin-arm64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b-vs-3.13.0b2.md)
- [📈time plot](bm-20240817-darwin-arm64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b-vs-3.13.0b2.svg)


# Results

- fork: python
- version: 3.14.0a0
- config: JIT
- commit hash: [498376d](https://github.com/python/cpython/commit/498376d)
- commit date: 2024-08-02T15:40:42+01:00
- commit merge base: [9fc1c992d6fcea0b7558c581846eef6bdd811f6c](https://github.com/python/cpython/commit/9fc1c992d6fcea0b7558c581846eef6bdd811f6c)
- ref: 498376d7a7d6f704f22a

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10218493151)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20240802-arminc-aarch64-python-498376d7a7d6f704f22a-3.14.0a0-498376d.json)

### vs. 3.10.4

- Geometric mean: 1.22x faster (HPT: reliability of 100.00%, 1.06x faster at 99th %ile)
- Memory usage: 1.24x
- missing benchmarks: aiohttp, chameleon, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240802-arminc-aarch64-python-498376d7a7d6f704f22a-3.14.0a0-498376d-vs-3.10.4.md)
- [📈time plot](bm-20240802-arminc-aarch64-python-498376d7a7d6f704f22a-3.14.0a0-498376d-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.06x slower (HPT: reliability of 100.00%, 1.02x slower at 99th %ile)
- Memory usage: 1.01x
- missing benchmarks: aiohttp, chameleon, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser
- [📄table](bm-20240802-arminc-aarch64-python-498376d7a7d6f704f22a-3.14.0a0-498376d-vs-3.12.0.md)
- [📈time plot](bm-20240802-arminc-aarch64-python-498376d7a7d6f704f22a-3.14.0a0-498376d-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.07x slower (HPT: reliability of 100.00%, 1.02x slower at 99th %ile)
- Memory usage: 1.09x
- missing benchmarks: aiohttp, chameleon, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list
- [📄table](bm-20240802-arminc-aarch64-python-498376d7a7d6f704f22a-3.14.0a0-498376d-vs-3.13.0b2.md)
- [📈time plot](bm-20240802-arminc-aarch64-python-498376d7a7d6f704f22a-3.14.0a0-498376d-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.10x slower (HPT: reliability of 100.00%, 1.04x slower at 99th %ile)
- Memory usage: 1.08x
- [🧠memory plot](bm-20240802-arminc-aarch64-python-498376d7a7d6f704f22a-3.14.0a0-498376d-vs-base-mem.svg)
- [📄table](bm-20240802-arminc-aarch64-python-498376d7a7d6f704f22a-3.14.0a0-498376d-vs-base.md)
- [📈time plot](bm-20240802-arminc-aarch64-python-498376d7a7d6f704f22a-3.14.0a0-498376d-vs-base.svg)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10218493151)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-186-generic-x86_64-with-glibc2.31
- [raw results](bm-20240802-linux-x86_64-python-498376d7a7d6f704f22a-3.14.0a0-498376d.json)

### vs. 3.10.4

- Geometric mean: 1.42x faster (HPT: reliability of 100.00%, 1.26x faster at 99th %ile)
- Memory usage: 1.19x
- missing benchmarks: aiohttp, chameleon, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240802-linux-x86_64-python-498376d7a7d6f704f22a-3.14.0a0-498376d-vs-3.10.4.md)
- [📈time plot](bm-20240802-linux-x86_64-python-498376d7a7d6f704f22a-3.14.0a0-498376d-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.08x faster (HPT: reliability of 99.99%, 1.02x faster at 99th %ile)
- Memory usage: 1.05x
- missing benchmarks: aiohttp, chameleon, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240802-linux-x86_64-python-498376d7a7d6f704f22a-3.14.0a0-498376d-vs-3.12.0.md)
- [📈time plot](bm-20240802-linux-x86_64-python-498376d7a7d6f704f22a-3.14.0a0-498376d-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.05x faster (HPT: reliability of 100.00%, 1.01x faster at 99th %ile)
- Memory usage: 1.07x
- missing benchmarks: aiohttp, chameleon, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list
- [📄table](bm-20240802-linux-x86_64-python-498376d7a7d6f704f22a-3.14.0a0-498376d-vs-3.13.0b2.md)
- [📈time plot](bm-20240802-linux-x86_64-python-498376d7a7d6f704f22a-3.14.0a0-498376d-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.00x slower (HPT: reliability of 55.46%, 1.00x slower at 99th %ile)
- Memory usage: 1.06x
- [🧠memory plot](bm-20240802-linux-x86_64-python-498376d7a7d6f704f22a-3.14.0a0-498376d-vs-base-mem.svg)
- [📄table](bm-20240802-linux-x86_64-python-498376d7a7d6f704f22a-3.14.0a0-498376d-vs-base.md)
- [📈time plot](bm-20240802-linux-x86_64-python-498376d7a7d6f704f22a-3.14.0a0-498376d-vs-base.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10218493151)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-105-generic-x86_64-with-glibc2.35
- [raw results](bm-20240802-pythonperf2-x86_64-python-498376d7a7d6f704f22a-3.14.0a0-498376d.json)

### vs. 3.10.4

- Geometric mean: 1.34x faster (HPT: reliability of 100.00%, 1.20x faster at 99th %ile)
- Memory usage: 1.21x
- missing benchmarks: aiohttp, chameleon, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240802-pythonperf2-x86_64-python-498376d7a7d6f704f22a-3.14.0a0-498376d-vs-3.10.4.md)
- [📈time plot](bm-20240802-pythonperf2-x86_64-python-498376d7a7d6f704f22a-3.14.0a0-498376d-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.02x faster (HPT: reliability of 90.50%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- missing benchmarks: aiohttp, chameleon, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240802-pythonperf2-x86_64-python-498376d7a7d6f704f22a-3.14.0a0-498376d-vs-3.12.0.md)
- [📈time plot](bm-20240802-pythonperf2-x86_64-python-498376d7a7d6f704f22a-3.14.0a0-498376d-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.02x faster (HPT: reliability of 96.25%, 1.00x faster at 99th %ile)
- Memory usage: 1.07x
- missing benchmarks: aiohttp, chameleon, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list
- [📄table](bm-20240802-pythonperf2-x86_64-python-498376d7a7d6f704f22a-3.14.0a0-498376d-vs-3.13.0b2.md)
- [📈time plot](bm-20240802-pythonperf2-x86_64-python-498376d7a7d6f704f22a-3.14.0a0-498376d-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.01x slower (HPT: reliability of 86.85%, 1.00x slower at 99th %ile)
- Memory usage: 1.07x
- [🧠memory plot](bm-20240802-pythonperf2-x86_64-python-498376d7a7d6f704f22a-3.14.0a0-498376d-vs-base-mem.svg)
- [📄table](bm-20240802-pythonperf2-x86_64-python-498376d7a7d6f704f22a-3.14.0a0-498376d-vs-base.md)
- [📈time plot](bm-20240802-pythonperf2-x86_64-python-498376d7a7d6f704f22a-3.14.0a0-498376d-vs-base.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10218493151)
- cpu model: missing
- platform: macOS-14.5-arm64-arm-64bit-Mach-O
- [raw results](bm-20240802-darwin-arm64-python-498376d7a7d6f704f22a-3.14.0a0-498376d.json)

### vs. 3.10.4

- Geometric mean: 1.27x faster (HPT: reliability of 100.00%, 1.16x faster at 99th %ile)
- Memory usage: 0.72x
- missing benchmarks: aiohttp, chameleon, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240802-darwin-arm64-python-498376d7a7d6f704f22a-3.14.0a0-498376d-vs-3.10.4.md)
- [📈time plot](bm-20240802-darwin-arm64-python-498376d7a7d6f704f22a-3.14.0a0-498376d-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.07x faster (HPT: reliability of 100.00%, 1.01x faster at 99th %ile)
- Memory usage: 0.64x
- missing benchmarks: aiohttp, chameleon, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240802-darwin-arm64-python-498376d7a7d6f704f22a-3.14.0a0-498376d-vs-3.12.0.md)
- [📈time plot](bm-20240802-darwin-arm64-python-498376d7a7d6f704f22a-3.14.0a0-498376d-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.01x slower (HPT: reliability of 98.08%, 1.00x slower at 99th %ile)
- Memory usage: 0.59x
- missing benchmarks: aiohttp, chameleon, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list
- [📄table](bm-20240802-darwin-arm64-python-498376d7a7d6f704f22a-3.14.0a0-498376d-vs-3.13.0b2.md)
- [📈time plot](bm-20240802-darwin-arm64-python-498376d7a7d6f704f22a-3.14.0a0-498376d-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.02x slower (HPT: reliability of 99.36%, 1.00x slower at 99th %ile)
- Memory usage: 1.10x
- [🧠memory plot](bm-20240802-darwin-arm64-python-498376d7a7d6f704f22a-3.14.0a0-498376d-vs-base-mem.svg)
- [📄table](bm-20240802-darwin-arm64-python-498376d7a7d6f704f22a-3.14.0a0-498376d-vs-base.md)
- [📈time plot](bm-20240802-darwin-arm64-python-498376d7a7d6f704f22a-3.14.0a0-498376d-vs-base.svg)


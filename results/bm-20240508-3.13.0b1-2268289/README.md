# Results

- fork: python
- version: 3.13.0b1
- config: 
- commit hash: [2268289](https://github.com/python/cpython/commit/2268289)
- commit date: 2024-05-08T11:21:00+02:00
- commit merge base: [c4f9823be277b2e3de2315526612276626217743](https://github.com/python/cpython/commit/c4f9823be277b2e3de2315526612276626217743)
- ref: 2268289a47c6e3c9a220, v3.13.0b1

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11112544532)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9021430016)
- [raw results](bm-20240508-arminc-aarch64-python-2268289a47c6e3c9a220-3.13.0b1-2268289.json)
- [raw results](bm-20240508-arminc-aarch64-python-v3.13.0b1-3.13.0b1-2268289.json)

### vs. 3.10.4

- Geometric mean: 1.24x faster (HPT: reliability of 100.00%, 1.20x faster at 99th %ile)
- Memory usage: 1.14x
- missing benchmarks: sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, unpack_sequence
- Memory usage: 1.13x
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240508-arminc-aarch64-python-2268289a47c6e3c9a220-3.13.0b1-2268289-vs-3.10.4.md)
- [📈time plot](bm-20240508-arminc-aarch64-python-2268289a47c6e3c9a220-3.13.0b1-2268289-vs-3.10.4.svg)
- [📄table](bm-20240508-arminc-aarch64-python-v3.13.0b1-3.13.0b1-2268289-vs-3.10.4.md)
- [📈time plot](bm-20240508-arminc-aarch64-python-v3.13.0b1-3.13.0b1-2268289-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.03x slower (HPT: reliability of 62.67%, 1.00x slower at 99th %ile)
- Memory usage: 0.92x
- missing benchmarks: sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: bpe_tokeniser, flaskblogging, unpack_sequence
- Geometric mean: 1.03x slower (HPT: reliability of 77.53%, 1.00x slower at 99th %ile)
- new benchmarks: flaskblogging
- [📄table](bm-20240508-arminc-aarch64-python-2268289a47c6e3c9a220-3.13.0b1-2268289-vs-3.12.0.md)
- [📈time plot](bm-20240508-arminc-aarch64-python-2268289a47c6e3c9a220-3.13.0b1-2268289-vs-3.12.0.svg)
- [📄table](bm-20240508-arminc-aarch64-python-v3.13.0b1-3.13.0b1-2268289-vs-3.12.0.md)
- [📈time plot](bm-20240508-arminc-aarch64-python-v3.13.0b1-3.13.0b1-2268289-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.04x slower (HPT: reliability of 99.97%, 1.00x slower at 99th %ile)
- Memory usage: 1.00x
- new benchmarks: unpack_sequence
- Geometric mean: 1.04x slower (HPT: reliability of 99.99%, 1.00x slower at 99th %ile)
- Memory usage: 0.99x
- missing benchmarks: bpe_tokeniser
- [📄table](bm-20240508-arminc-aarch64-python-2268289a47c6e3c9a220-3.13.0b1-2268289-vs-3.13.0b2.md)
- [📈time plot](bm-20240508-arminc-aarch64-python-2268289a47c6e3c9a220-3.13.0b1-2268289-vs-3.13.0b2.svg)
- [📄table](bm-20240508-arminc-aarch64-python-v3.13.0b1-3.13.0b1-2268289-vs-3.13.0b2.md)
- [📈time plot](bm-20240508-arminc-aarch64-python-v3.13.0b1-3.13.0b1-2268289-vs-3.13.0b2.svg)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9021430016)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-164-generic-x86_64-with-glibc2.31
- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11112544532)
- platform: Linux-5.4.0-196-generic-x86_64-with-glibc2.31
- [raw results](bm-20240508-linux-x86_64-python-2268289a47c6e3c9a220-3.13.0b1-2268289.json)
- [raw results](bm-20240508-linux-x86_64-python-v3.13.0b1-3.13.0b1-2268289.json)

### vs. 3.10.4

- Geometric mean: 1.28x faster (HPT: reliability of 100.00%, 1.24x faster at 99th %ile)
- Memory usage: 1.12x
- missing benchmarks: sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- Geometric mean: 1.31x faster (HPT: reliability of 100.00%, 1.27x faster at 99th %ile)
- missing benchmarks: sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240508-linux-x86_64-python-2268289a47c6e3c9a220-3.13.0b1-2268289-vs-3.10.4.md)
- [📈time plot](bm-20240508-linux-x86_64-python-2268289a47c6e3c9a220-3.13.0b1-2268289-vs-3.10.4.svg)
- [📄table](bm-20240508-linux-x86_64-python-v3.13.0b1-3.13.0b1-2268289-vs-3.10.4.md)
- [📈time plot](bm-20240508-linux-x86_64-python-v3.13.0b1-3.13.0b1-2268289-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.01x slower (HPT: reliability of 99.57%, 1.00x faster at 99th %ile)
- Memory usage: 0.98x
- missing benchmarks: sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: djangocms, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift
- Geometric mean: 1.02x faster (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- Memory usage: 0.97x
- missing benchmarks: sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: bpe_tokeniser, djangocms, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240508-linux-x86_64-python-2268289a47c6e3c9a220-3.13.0b1-2268289-vs-3.12.0.md)
- [📈time plot](bm-20240508-linux-x86_64-python-2268289a47c6e3c9a220-3.13.0b1-2268289-vs-3.12.0.svg)
- [📄table](bm-20240508-linux-x86_64-python-v3.13.0b1-3.13.0b1-2268289-vs-3.12.0.md)
- [📈time plot](bm-20240508-linux-x86_64-python-v3.13.0b1-3.13.0b1-2268289-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.03x slower (HPT: reliability of 74.51%, 1.00x slower at 99th %ile)
- Memory usage: 1.00x
- missing benchmarks: bpe_tokeniser
- Geometric mean: 1.01x slower (HPT: reliability of 100.00%, 1.01x faster at 99th %ile)
- new benchmarks: unpack_sequence
- [📄table](bm-20240508-linux-x86_64-python-2268289a47c6e3c9a220-3.13.0b1-2268289-vs-3.13.0b2.md)
- [📈time plot](bm-20240508-linux-x86_64-python-2268289a47c6e3c9a220-3.13.0b1-2268289-vs-3.13.0b2.svg)
- [📄table](bm-20240508-linux-x86_64-python-v3.13.0b1-3.13.0b1-2268289-vs-3.13.0b2.md)
- [📈time plot](bm-20240508-linux-x86_64-python-v3.13.0b1-3.13.0b1-2268289-vs-3.13.0b2.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9021430016)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-105-generic-x86_64-with-glibc2.35
- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11112544532)
- [raw results](bm-20240508-pythonperf2-x86_64-python-2268289a47c6e3c9a220-3.13.0b1-2268289.json)
- [raw results](bm-20240508-pythonperf2-x86_64-python-v3.13.0b1-3.13.0b1-2268289.json)

### vs. 3.10.4

- Geometric mean: 1.23x faster (HPT: reliability of 100.00%, 1.20x faster at 99th %ile)
- Memory usage: 1.12x
- missing benchmarks: sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- Geometric mean: 1.24x faster (HPT: reliability of 100.00%, 1.20x faster at 99th %ile)
- missing benchmarks: sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240508-pythonperf2-x86_64-python-2268289a47c6e3c9a220-3.13.0b1-2268289-vs-3.10.4.md)
- [📈time plot](bm-20240508-pythonperf2-x86_64-python-2268289a47c6e3c9a220-3.13.0b1-2268289-vs-3.10.4.svg)
- [📄table](bm-20240508-pythonperf2-x86_64-python-v3.13.0b1-3.13.0b1-2268289-vs-3.10.4.md)
- [📈time plot](bm-20240508-pythonperf2-x86_64-python-v3.13.0b1-3.13.0b1-2268289-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.04x slower (HPT: reliability of 97.85%, 1.00x slower at 99th %ile)
- Memory usage: 0.93x
- missing benchmarks: sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift
- Geometric mean: 1.04x slower (HPT: reliability of 95.87%, 1.00x slower at 99th %ile)
- missing benchmarks: sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: bpe_tokeniser, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240508-pythonperf2-x86_64-python-2268289a47c6e3c9a220-3.13.0b1-2268289-vs-3.12.0.md)
- [📈time plot](bm-20240508-pythonperf2-x86_64-python-2268289a47c6e3c9a220-3.13.0b1-2268289-vs-3.12.0.svg)
- [📄table](bm-20240508-pythonperf2-x86_64-python-v3.13.0b1-3.13.0b1-2268289-vs-3.12.0.md)
- [📈time plot](bm-20240508-pythonperf2-x86_64-python-v3.13.0b1-3.13.0b1-2268289-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.04x slower (HPT: reliability of 100.00%, 1.00x slower at 99th %ile)
- Memory usage: 0.99x
- missing benchmarks: bpe_tokeniser
- Geometric mean: 1.03x slower (HPT: reliability of 99.98%, 1.00x slower at 99th %ile)
- Memory usage: 1.00x
- new benchmarks: unpack_sequence
- [📄table](bm-20240508-pythonperf2-x86_64-python-2268289a47c6e3c9a220-3.13.0b1-2268289-vs-3.13.0b2.md)
- [📈time plot](bm-20240508-pythonperf2-x86_64-python-2268289a47c6e3c9a220-3.13.0b1-2268289-vs-3.13.0b2.svg)
- [📄table](bm-20240508-pythonperf2-x86_64-python-v3.13.0b1-3.13.0b1-2268289-vs-3.13.0b2.md)
- [📈time plot](bm-20240508-pythonperf2-x86_64-python-v3.13.0b1-3.13.0b1-2268289-vs-3.13.0b2.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9768323837)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9021430016)
- [raw results](bm-20240508-pythonperf1-amd64-python-2268289a47c6e3c9a220-3.13.0b1-2268289.json)
- [raw results](bm-20240508-pythonperf1-amd64-python-v3.13.0b1-3.13.0b1-2268289.json)

### vs. 3.10.4

- Geometric mean: 1.25x faster (HPT: reliability of 100.00%, 1.20x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, dask, flaskblogging, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- Geometric mean: 1.23x faster (HPT: reliability of 100.00%, 1.18x faster at 99th %ile)
- missing benchmarks: sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- [📄table](bm-20240508-pythonperf1-amd64-python-2268289a47c6e3c9a220-3.13.0b1-2268289-vs-3.10.4.md)
- [📈time plot](bm-20240508-pythonperf1-amd64-python-2268289a47c6e3c9a220-3.13.0b1-2268289-vs-3.10.4.svg)
- [📄table](bm-20240508-pythonperf1-amd64-python-v3.13.0b1-3.13.0b1-2268289-vs-3.10.4.md)
- [📈time plot](bm-20240508-pythonperf1-amd64-python-v3.13.0b1-3.13.0b1-2268289-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.08x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, dask, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: genshi_text, genshi_xml, html5lib, pylint, thrift
- Geometric mean: 1.07x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- missing benchmarks: sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240508-pythonperf1-amd64-python-2268289a47c6e3c9a220-3.13.0b1-2268289-vs-3.12.0.md)
- [📈time plot](bm-20240508-pythonperf1-amd64-python-2268289a47c6e3c9a220-3.13.0b1-2268289-vs-3.12.0.svg)
- [📄table](bm-20240508-pythonperf1-amd64-python-v3.13.0b1-3.13.0b1-2268289-vs-3.12.0.md)
- [📈time plot](bm-20240508-pythonperf1-amd64-python-v3.13.0b1-3.13.0b1-2268289-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.01x slower (HPT: reliability of 99.98%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, flaskblogging, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list
- Geometric mean: 1.00x slower (HPT: reliability of 99.54%, 1.00x slower at 99th %ile)
- new benchmarks: dask
- [📄table](bm-20240508-pythonperf1-amd64-python-2268289a47c6e3c9a220-3.13.0b1-2268289-vs-3.13.0b2.md)
- [📈time plot](bm-20240508-pythonperf1-amd64-python-2268289a47c6e3c9a220-3.13.0b1-2268289-vs-3.13.0b2.svg)
- [📄table](bm-20240508-pythonperf1-amd64-python-v3.13.0b1-3.13.0b1-2268289-vs-3.13.0b2.md)
- [📈time plot](bm-20240508-pythonperf1-amd64-python-v3.13.0b1-3.13.0b1-2268289-vs-3.13.0b2.svg)

## windows x86 (pythonperf1_win32)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11112544532)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20240508-pythonperf1_win32-x86-python-2268289a47c6e3c9a220-3.13.0b1-2268289.json)

### vs. 3.10.4

- Geometric mean: 1.15x faster (HPT: reliability of 100.00%, 1.12x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240508-pythonperf1_win32-x86-python-2268289a47c6e3c9a220-3.13.0b1-2268289-vs-3.10.4.md)
- [📈time plot](bm-20240508-pythonperf1_win32-x86-python-2268289a47c6e3c9a220-3.13.0b1-2268289-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.20x faster (HPT: reliability of 100.00%, 1.18x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240508-pythonperf1_win32-x86-python-2268289a47c6e3c9a220-3.13.0b1-2268289-vs-3.12.0.md)
- [📈time plot](bm-20240508-pythonperf1_win32-x86-python-2268289a47c6e3c9a220-3.13.0b1-2268289-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.00x faster (HPT: reliability of 93.22%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- new benchmarks: dulwich_log, unpack_sequence
- [📄table](bm-20240508-pythonperf1_win32-x86-python-2268289a47c6e3c9a220-3.13.0b1-2268289-vs-3.13.0b2.md)
- [📈time plot](bm-20240508-pythonperf1_win32-x86-python-2268289a47c6e3c9a220-3.13.0b1-2268289-vs-3.13.0b2.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11112544532)
- cpu model: missing
- platform: macOS-14.6.1-arm64-arm-64bit-Mach-O
- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9021430016)
- platform: macOS-14.4.1-arm64-arm-64bit-Mach-O
- [raw results](bm-20240508-darwin-arm64-python-2268289a47c6e3c9a220-3.13.0b1-2268289.json)
- [raw results](bm-20240508-darwin-arm64-python-v3.13.0b1-3.13.0b1-2268289.json)

### vs. 3.10.4

- Geometric mean: 1.25x faster (HPT: reliability of 100.00%, 1.19x faster at 99th %ile)
- Memory usage: 0.61x
- missing benchmarks: sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- Memory usage: 1.17x
- missing benchmarks: sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240508-darwin-arm64-python-2268289a47c6e3c9a220-3.13.0b1-2268289-vs-3.10.4.md)
- [📈time plot](bm-20240508-darwin-arm64-python-2268289a47c6e3c9a220-3.13.0b1-2268289-vs-3.10.4.svg)
- [📄table](bm-20240508-darwin-arm64-python-v3.13.0b1-3.13.0b1-2268289-vs-3.10.4.md)
- [📈time plot](bm-20240508-darwin-arm64-python-v3.13.0b1-3.13.0b1-2268289-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.06x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: 0.54x
- missing benchmarks: sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift
- Memory usage: 1.06x
- missing benchmarks: sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240508-darwin-arm64-python-2268289a47c6e3c9a220-3.13.0b1-2268289-vs-3.12.0.md)
- [📈time plot](bm-20240508-darwin-arm64-python-2268289a47c6e3c9a220-3.13.0b1-2268289-vs-3.12.0.svg)
- [📄table](bm-20240508-darwin-arm64-python-v3.13.0b1-3.13.0b1-2268289-vs-3.12.0.md)
- [📈time plot](bm-20240508-darwin-arm64-python-v3.13.0b1-3.13.0b1-2268289-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.02x slower (HPT: reliability of 99.66%, 1.00x slower at 99th %ile)
- Memory usage: 0.32x
- new benchmarks: unpack_sequence
- Geometric mean: 1.01x slower (HPT: reliability of 99.14%, 1.00x slower at 99th %ile)
- Memory usage: 0.99x
- missing benchmarks: bpe_tokeniser
- [📄table](bm-20240508-darwin-arm64-python-2268289a47c6e3c9a220-3.13.0b1-2268289-vs-3.13.0b2.md)
- [📈time plot](bm-20240508-darwin-arm64-python-2268289a47c6e3c9a220-3.13.0b1-2268289-vs-3.13.0b2.svg)
- [📄table](bm-20240508-darwin-arm64-python-v3.13.0b1-3.13.0b1-2268289-vs-3.13.0b2.md)
- [📈time plot](bm-20240508-darwin-arm64-python-v3.13.0b1-3.13.0b1-2268289-vs-3.13.0b2.svg)


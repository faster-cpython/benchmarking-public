# Results

- fork: colesbury
- version: 3.14.0a0
- config: NOGIL
- commit hash: [4b27f3a](https://github.com/colesbury/cpython/commit/4b27f3a)
- commit date: 2024-08-13T15:58:02+00:00
- commit merge base: [db6f5e193315a3bbfa7b0b6644203bae3f76b638](https://github.com/colesbury/cpython/commit/db6f5e193315a3bbfa7b0b6644203bae3f76b638)
- ref: gh_117376_pydecref_m

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10453425857)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20240813-arminc-aarch64-colesbury-gh_117376_pydecref_m-3.14.0a0-4b27f3a.json)

### vs. 3.10.4

- Geometric mean: 1.21x slower (HPT: reliability of 100.00%, 1.17x slower at 99th %ile)
- Memory usage: 1.33x
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240813-arminc-aarch64-colesbury-gh_117376_pydecref_m-3.14.0a0-4b27f3a-vs-3.10.4.md)
- [📈time plot](bm-20240813-arminc-aarch64-colesbury-gh_117376_pydecref_m-3.14.0a0-4b27f3a-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.55x slower (HPT: reliability of 100.00%, 1.37x slower at 99th %ile)
- Memory usage: 1.07x
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser
- [📄table](bm-20240813-arminc-aarch64-colesbury-gh_117376_pydecref_m-3.14.0a0-4b27f3a-vs-3.12.0.md)
- [📈time plot](bm-20240813-arminc-aarch64-colesbury-gh_117376_pydecref_m-3.14.0a0-4b27f3a-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.58x slower (HPT: reliability of 100.00%, 1.39x slower at 99th %ile)
- Memory usage: 1.16x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20240813-arminc-aarch64-colesbury-gh_117376_pydecref_m-3.14.0a0-4b27f3a-vs-3.13.0.md)
- [📈time plot](bm-20240813-arminc-aarch64-colesbury-gh_117376_pydecref_m-3.14.0a0-4b27f3a-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.01x faster (HPT: reliability of 100.00%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20240813-arminc-aarch64-colesbury-gh_117376_pydecref_m-3.14.0a0-4b27f3a-vs-base-mem.svg)
- [📄table](bm-20240813-arminc-aarch64-colesbury-gh_117376_pydecref_m-3.14.0a0-4b27f3a-vs-base.md)
- [📈time plot](bm-20240813-arminc-aarch64-colesbury-gh_117376_pydecref_m-3.14.0a0-4b27f3a-vs-base.svg)

### vs. 3.13.0b2

- [📄table](bm-20240813-arminc-aarch64-colesbury-gh_117376_pydecref_m-3.14.0a0-4b27f3a-vs-3.13.0b2.md)
- [📈time plot](bm-20240813-arminc-aarch64-colesbury-gh_117376_pydecref_m-3.14.0a0-4b27f3a-vs-3.13.0b2.svg)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10453425857)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-192-generic-x86_64-with-glibc2.31
- [raw results](bm-20240813-linux-x86_64-colesbury-gh_117376_pydecref_m-3.14.0a0-4b27f3a.json)

### vs. 3.10.4

- Geometric mean: 1.05x slower (HPT: reliability of 99.98%, 1.02x slower at 99th %ile)
- Memory usage: 1.29x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240813-linux-x86_64-colesbury-gh_117376_pydecref_m-3.14.0a0-4b27f3a-vs-3.10.4.md)
- [📈time plot](bm-20240813-linux-x86_64-colesbury-gh_117376_pydecref_m-3.14.0a0-4b27f3a-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.36x slower (HPT: reliability of 100.00%, 1.21x slower at 99th %ile)
- Memory usage: 1.13x
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240813-linux-x86_64-colesbury-gh_117376_pydecref_m-3.14.0a0-4b27f3a-vs-3.12.0.md)
- [📈time plot](bm-20240813-linux-x86_64-colesbury-gh_117376_pydecref_m-3.14.0a0-4b27f3a-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.45x slower (HPT: reliability of 100.00%, 1.30x slower at 99th %ile)
- Memory usage: 1.16x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20240813-linux-x86_64-colesbury-gh_117376_pydecref_m-3.14.0a0-4b27f3a-vs-3.13.0.md)
- [📈time plot](bm-20240813-linux-x86_64-colesbury-gh_117376_pydecref_m-3.14.0a0-4b27f3a-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.00x faster (HPT: reliability of 98.08%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20240813-linux-x86_64-colesbury-gh_117376_pydecref_m-3.14.0a0-4b27f3a-vs-base-mem.svg)
- [📄table](bm-20240813-linux-x86_64-colesbury-gh_117376_pydecref_m-3.14.0a0-4b27f3a-vs-base.md)
- [📈time plot](bm-20240813-linux-x86_64-colesbury-gh_117376_pydecref_m-3.14.0a0-4b27f3a-vs-base.svg)

### vs. 3.13.0b2

- [📄table](bm-20240813-linux-x86_64-colesbury-gh_117376_pydecref_m-3.14.0a0-4b27f3a-vs-3.13.0b2.md)
- [📈time plot](bm-20240813-linux-x86_64-colesbury-gh_117376_pydecref_m-3.14.0a0-4b27f3a-vs-3.13.0b2.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10453425857)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-105-generic-x86_64-with-glibc2.35
- [raw results](bm-20240813-pythonperf2-x86_64-colesbury-gh_117376_pydecref_m-3.14.0a0-4b27f3a.json)

### vs. 3.10.4

- Geometric mean: 1.10x slower (HPT: reliability of 100.00%, 1.07x slower at 99th %ile)
- Memory usage: 1.31x
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240813-pythonperf2-x86_64-colesbury-gh_117376_pydecref_m-3.14.0a0-4b27f3a-vs-3.10.4.md)
- [📈time plot](bm-20240813-pythonperf2-x86_64-colesbury-gh_117376_pydecref_m-3.14.0a0-4b27f3a-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.43x slower (HPT: reliability of 100.00%, 1.26x slower at 99th %ile)
- Memory usage: 1.08x
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240813-pythonperf2-x86_64-colesbury-gh_117376_pydecref_m-3.14.0a0-4b27f3a-vs-3.12.0.md)
- [📈time plot](bm-20240813-pythonperf2-x86_64-colesbury-gh_117376_pydecref_m-3.14.0a0-4b27f3a-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.43x slower (HPT: reliability of 100.00%, 1.30x slower at 99th %ile)
- Memory usage: 1.17x
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20240813-pythonperf2-x86_64-colesbury-gh_117376_pydecref_m-3.14.0a0-4b27f3a-vs-3.13.0.md)
- [📈time plot](bm-20240813-pythonperf2-x86_64-colesbury-gh_117376_pydecref_m-3.14.0a0-4b27f3a-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.01x faster (HPT: reliability of 100.00%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20240813-pythonperf2-x86_64-colesbury-gh_117376_pydecref_m-3.14.0a0-4b27f3a-vs-base-mem.svg)
- [📄table](bm-20240813-pythonperf2-x86_64-colesbury-gh_117376_pydecref_m-3.14.0a0-4b27f3a-vs-base.md)
- [📈time plot](bm-20240813-pythonperf2-x86_64-colesbury-gh_117376_pydecref_m-3.14.0a0-4b27f3a-vs-base.svg)

### vs. 3.13.0b2

- [📄table](bm-20240813-pythonperf2-x86_64-colesbury-gh_117376_pydecref_m-3.14.0a0-4b27f3a-vs-3.13.0b2.md)
- [📈time plot](bm-20240813-pythonperf2-x86_64-colesbury-gh_117376_pydecref_m-3.14.0a0-4b27f3a-vs-3.13.0b2.svg)


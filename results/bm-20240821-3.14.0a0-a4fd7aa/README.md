# Results

- fork: python
- version: 3.14.0a0
- config: 
- commit hash: [a4fd7aa](https://github.com/python/cpython/commit/a4fd7aa)
- commit date: 2024-08-21T15:52:04+01:00
- commit merge base: [4b7c4880a0b264373e65235701bb78cbf19266b5](https://github.com/python/cpython/commit/4b7c4880a0b264373e65235701bb78cbf19266b5)
- ref: a4fd7aa4a6420cef1c22

## linux x86_64 (azure)

- [pystats raw](bm-20240821-azure-x86_64-python-a4fd7aa4a6420cef1c22-3.14.0a0-a4fd7aa-pystats.json)
- [pystats table](bm-20240821-azure-x86_64-python-a4fd7aa4a6420cef1c22-3.14.0a0-a4fd7aa-pystats.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10492356658)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-192-generic-x86_64-with-glibc2.31
- [raw results](bm-20240821-linux-x86_64-python-a4fd7aa4a6420cef1c22-3.14.0a0-a4fd7aa.json)

### vs. 3.10.4

- Geometric mean: 1.42x faster (HPT: reliability of 100.00%, 1.30x faster at 99th %ile)
- Memory usage: 1.12x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240821-linux-x86_64-python-a4fd7aa4a6420cef1c22-3.14.0a0-a4fd7aa-vs-3.10.4.md)
- [📈time plot](bm-20240821-linux-x86_64-python-a4fd7aa4a6420cef1c22-3.14.0a0-a4fd7aa-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.07x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: 0.98x
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240821-linux-x86_64-python-a4fd7aa4a6420cef1c22-3.14.0a0-a4fd7aa-vs-3.12.0.md)
- [📈time plot](bm-20240821-linux-x86_64-python-a4fd7aa4a6420cef1c22-3.14.0a0-a4fd7aa-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.01x faster (HPT: reliability of 79.95%, 1.00x faster at 99th %ile)
- Memory usage: 1.01x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20240821-linux-x86_64-python-a4fd7aa4a6420cef1c22-3.14.0a0-a4fd7aa-vs-3.13.0.md)
- [📈time plot](bm-20240821-linux-x86_64-python-a4fd7aa4a6420cef1c22-3.14.0a0-a4fd7aa-vs-3.13.0.svg)

### vs. 3.13.0b2

- [📄table](bm-20240821-linux-x86_64-python-a4fd7aa4a6420cef1c22-3.14.0a0-a4fd7aa-vs-3.13.0b2.md)
- [📈time plot](bm-20240821-linux-x86_64-python-a4fd7aa4a6420cef1c22-3.14.0a0-a4fd7aa-vs-3.13.0b2.svg)


# Results

- fork: faster-cpython
- version: 3.14.0a0
- config: 
- commit hash: [ade1f65](https://github.com/faster%2dcpython/cpython/commit/ade1f65)
- commit date: 2024-08-15T11:36:03+01:00
- commit merge base: [b106cf8d978b32b04a4394973b850ef2a62cbcc4](https://github.com/faster%2dcpython/cpython/commit/b106cf8d978b32b04a4394973b850ef2a62cbcc4)
- ref: specialize_call_ex

## linux x86_64 (azure)

- [pystats raw](bm-20240815-azure-x86_64-faster%252dcpython-specialize_call_ex-3.14.0a0-ade1f65-pystats.json)
- [pystats table](bm-20240815-azure-x86_64-faster%252dcpython-specialize_call_ex-3.14.0a0-ade1f65-pystats.md)

### vs. base

- [pystats diff](bm-20240815-azure-x86_64-faster%252dcpython-specialize_call_ex-3.14.0a0-ade1f65-pystats-vs-base.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10402635955)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-192-generic-x86_64-with-glibc2.31
- [raw results](bm-20240815-linux-x86_64-faster%252dcpython-specialize_call_ex-3.14.0a0-ade1f65.json)

### vs. 3.10.4

- Geometric mean: 1.42x faster (HPT: reliability of 100.00%, 1.29x faster at 99th %ile)
- Memory usage: 1.13x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240815-linux-x86_64-faster%252dcpython-specialize_call_ex-3.14.0a0-ade1f65-vs-3.10.4.md)
- [📈time plot](bm-20240815-linux-x86_64-faster%252dcpython-specialize_call_ex-3.14.0a0-ade1f65-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.07x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: 0.98x
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240815-linux-x86_64-faster%252dcpython-specialize_call_ex-3.14.0a0-ade1f65-vs-3.12.0.md)
- [📈time plot](bm-20240815-linux-x86_64-faster%252dcpython-specialize_call_ex-3.14.0a0-ade1f65-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.01x faster (HPT: reliability of 93.36%, 1.00x slower at 99th %ile)
- Memory usage: 1.01x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20240815-linux-x86_64-faster%252dcpython-specialize_call_ex-3.14.0a0-ade1f65-vs-3.13.0.md)
- [📈time plot](bm-20240815-linux-x86_64-faster%252dcpython-specialize_call_ex-3.14.0a0-ade1f65-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.01x slower (HPT: reliability of 99.98%, 1.00x slower at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20240815-linux-x86_64-faster%252dcpython-specialize_call_ex-3.14.0a0-ade1f65-vs-base-mem.svg)
- [📄table](bm-20240815-linux-x86_64-faster%252dcpython-specialize_call_ex-3.14.0a0-ade1f65-vs-base.md)
- [📈time plot](bm-20240815-linux-x86_64-faster%252dcpython-specialize_call_ex-3.14.0a0-ade1f65-vs-base.svg)

### vs. 3.13.0b2

- [📄table](bm-20240815-linux-x86_64-faster%252dcpython-specialize_call_ex-3.14.0a0-ade1f65-vs-3.13.0b2.md)
- [📈time plot](bm-20240815-linux-x86_64-faster%252dcpython-specialize_call_ex-3.14.0a0-ade1f65-vs-3.13.0b2.svg)


# Results

- fork: python
- version: 3.14.0a0
- config: 
- commit hash: [c901437](https://github.com/python/cpython/commit/c901437)
- commit date: 2024-10-10T18:19:08+01:00
- commit merge base: [01fc3b34cc6994bc83b6540da3a8573e79dfbb56](https://github.com/python/cpython/commit/01fc3b34cc6994bc83b6540da3a8573e79dfbb56)
- ref: c9014374c50d6ef64786

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11280469906)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-196-generic-x86_64-with-glibc2.31
- [raw results](bm-20241010-linux-x86_64-python-c9014374c50d6ef64786-3.14.0a0-c901437.json)

### vs. 3.10.4

- Geometric mean: 1.432x faster (HPT: reliability of 100.00%, 1.31x faster at 99th %ile)
- Memory usage: 1.12x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20241010-linux-x86_64-python-c9014374c50d6ef64786-3.14.0a0-c901437-vs-3.10.4.md)
- [📈time plot](bm-20241010-linux-x86_64-python-c9014374c50d6ef64786-3.14.0a0-c901437-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.086x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: 0.97x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20241010-linux-x86_64-python-c9014374c50d6ef64786-3.14.0a0-c901437-vs-3.12.0.md)
- [📈time plot](bm-20241010-linux-x86_64-python-c9014374c50d6ef64786-3.14.0a0-c901437-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.033x faster (HPT: reliability of 100.00%, 1.00x faster at 99th %ile)
- Memory usage: 0.91x
- missing benchmarks: chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20241010-linux-x86_64-python-c9014374c50d6ef64786-3.14.0a0-c901437-vs-3.13.0.md)
- [📈time plot](bm-20241010-linux-x86_64-python-c9014374c50d6ef64786-3.14.0a0-c901437-vs-3.13.0.svg)


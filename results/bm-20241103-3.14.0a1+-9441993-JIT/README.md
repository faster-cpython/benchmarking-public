# Results

- fork: python
- version: 3.14.0a1+
- config: JIT
- commit hash: [9441993](https://github.com/python/cpython/commit/9441993)
- commit date: 2024-11-03T21:22:49+00:00
- commit merge base: [ac556a2ad1213b8bb81372fe6fb762f5fcb076de](https://github.com/python/cpython/commit/ac556a2ad1213b8bb81372fe6fb762f5fcb076de)
- ref: 9441993f272f42e4a97d

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11669925450)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-196-generic-x86_64-with-glibc2.31
- [raw results](bm-20241103-linux-x86_64-python-9441993f272f42e4a97d-3.14.0a1%2B-9441993.json)

### vs. 3.10.4

- Geometric mean: 1.379x faster (HPT: reliability of 100.00%, 1.24x faster at 99th %ile)
- Memory usage: 1.33x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, shortest_path, sphinx
- [📄table](bm-20241103-linux-x86_64-python-9441993f272f42e4a97d-3.14.0a1%2B-9441993-vs-3.10.4.md)
- [📈time plot](bm-20241103-linux-x86_64-python-9441993f272f42e4a97d-3.14.0a1%2B-9441993-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.055x faster (HPT: reliability of 99.96%, 1.01x faster at 99th %ile)
- Memory usage: 1.15x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, pylint, shortest_path, sphinx, thrift
- [📄table](bm-20241103-linux-x86_64-python-9441993f272f42e4a97d-3.14.0a1%2B-9441993-vs-3.12.0.md)
- [📈time plot](bm-20241103-linux-x86_64-python-9441993f272f42e4a97d-3.14.0a1%2B-9441993-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.008x slower (HPT: reliability of 89.28%, 1.00x slower at 99th %ile)
- Memory usage: 1.07x
- missing benchmarks: chameleon, gevent_hub, mypy2
- new benchmarks: sqlite_synth
- [📄table](bm-20241103-linux-x86_64-python-9441993f272f42e4a97d-3.14.0a1%2B-9441993-vs-3.13.0.md)
- [📈time plot](bm-20241103-linux-x86_64-python-9441993f272f42e4a97d-3.14.0a1%2B-9441993-vs-3.13.0.svg)


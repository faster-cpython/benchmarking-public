# Results

- fork: brandtbucher
- version: 3.14.0a1+
- config: JIT
- commit hash: [69e9a0e](https://github.com/brandtbucher/cpython/commit/69e9a0e)
- commit date: 2024-10-24T16:27:46-07:00
- commit merge base: [34653bba644aa5481613f398153757d7357e39ea](https://github.com/brandtbucher/cpython/commit/34653bba644aa5481613f398153757d7357e39ea)
- ref: jb0_invalidate

## linux x86_64 (azure)

- [pystats raw](bm-20241024-azure-x86_64-brandtbucher-jb0_invalidate-3.14.0a1%2B-69e9a0e-pystats.json)
- [pystats table](bm-20241024-azure-x86_64-brandtbucher-jb0_invalidate-3.14.0a1%2B-69e9a0e-pystats.md)

### vs. base

- [pystats diff](bm-20241024-azure-x86_64-brandtbucher-jb0_invalidate-3.14.0a1%2B-69e9a0e-pystats-vs-base.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11509049631)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-196-generic-x86_64-with-glibc2.31
- [raw results](bm-20241024-linux-x86_64-brandtbucher-jb0_invalidate-3.14.0a1%2B-69e9a0e.json)

### vs. 3.10.4

- Geometric mean: 1.321x faster (HPT: reliability of 100.00%, 1.19x faster at 99th %ile)
- Memory usage: 1.39x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, sphinx
- [📄table](bm-20241024-linux-x86_64-brandtbucher-jb0_invalidate-3.14.0a1%2B-69e9a0e-vs-3.10.4.md)
- [📈time plot](bm-20241024-linux-x86_64-brandtbucher-jb0_invalidate-3.14.0a1%2B-69e9a0e-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.011x faster (HPT: reliability of 81.38%, 1.00x faster at 99th %ile)
- Memory usage: 1.19x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, sphinx, thrift
- [📄table](bm-20241024-linux-x86_64-brandtbucher-jb0_invalidate-3.14.0a1%2B-69e9a0e-vs-3.12.0.md)
- [📈time plot](bm-20241024-linux-x86_64-brandtbucher-jb0_invalidate-3.14.0a1%2B-69e9a0e-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.048x slower (HPT: reliability of 99.69%, 1.00x slower at 99th %ile)
- Memory usage: 1.12x
- missing benchmarks: chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path
- [📄table](bm-20241024-linux-x86_64-brandtbucher-jb0_invalidate-3.14.0a1%2B-69e9a0e-vs-3.13.0.md)
- [📈time plot](bm-20241024-linux-x86_64-brandtbucher-jb0_invalidate-3.14.0a1%2B-69e9a0e-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.050x slower (HPT: reliability of 100.00%, 1.01x slower at 99th %ile)
- Memory usage: 1.05x
- [🧠memory plot](bm-20241024-linux-x86_64-brandtbucher-jb0_invalidate-3.14.0a1%2B-69e9a0e-vs-base-mem.svg)
- [📄table](bm-20241024-linux-x86_64-brandtbucher-jb0_invalidate-3.14.0a1%2B-69e9a0e-vs-base.md)
- [📈time plot](bm-20241024-linux-x86_64-brandtbucher-jb0_invalidate-3.14.0a1%2B-69e9a0e-vs-base.svg)


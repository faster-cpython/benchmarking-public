# Results

- fork: faster-cpython
- version: 3.14.0a1+
- config: 
- commit hash: [7e6deef](https://github.com/faster%2dcpython/cpython/commit/7e6deef)
- commit date: 2024-10-29T11:29:22+00:00
- commit merge base: [faa3272fb8d63d481a136cc0467a0cba6ed7b264](https://github.com/faster%2dcpython/cpython/commit/faa3272fb8d63d481a136cc0467a0cba6ed7b264)
- ref: use_stackrefs

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11573004037)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-196-generic-x86_64-with-glibc2.31
- [raw results](bm-20241029-linux-x86_64-faster%252dcpython-use_stackrefs-3.14.0a1%2B-7e6deef.json)

### vs. 3.10.4

- Geometric mean: 1.311x slower (HPT: reliability of 100.00%, 1.37x slower at 99th %ile)
- Memory usage: 1.24x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, shortest_path, sphinx
- [📄table](bm-20241029-linux-x86_64-faster%252dcpython-use_stackrefs-3.14.0a1%2B-7e6deef-vs-3.10.4.md)
- [📈time plot](bm-20241029-linux-x86_64-faster%252dcpython-use_stackrefs-3.14.0a1%2B-7e6deef-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.478x slower (HPT: reliability of 100.00%, 1.87x slower at 99th %ile)
- Memory usage: 1.07x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, pylint, shortest_path, sphinx, thrift
- [📄table](bm-20241029-linux-x86_64-faster%252dcpython-use_stackrefs-3.14.0a1%2B-7e6deef-vs-3.12.0.md)
- [📈time plot](bm-20241029-linux-x86_64-faster%252dcpython-use_stackrefs-3.14.0a1%2B-7e6deef-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.507x slower (HPT: reliability of 100.00%, 2.01x slower at 99th %ile)
- Memory usage: 1.01x
- missing benchmarks: chameleon, gevent_hub, mypy2
- [📄table](bm-20241029-linux-x86_64-faster%252dcpython-use_stackrefs-3.14.0a1%2B-7e6deef-vs-3.13.0.md)
- [📈time plot](bm-20241029-linux-x86_64-faster%252dcpython-use_stackrefs-3.14.0a1%2B-7e6deef-vs-3.13.0.svg)

### vs. base

- [🧠memory plot](bm-20241029-linux-x86_64-faster%252dcpython-use_stackrefs-3.14.0a1%2B-7e6deef-vs-base-mem.svg)
- [📈time plot](bm-20241029-linux-x86_64-faster%252dcpython-use_stackrefs-3.14.0a1%2B-7e6deef-vs-base.svg)


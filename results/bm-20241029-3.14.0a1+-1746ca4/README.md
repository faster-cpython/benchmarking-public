# Results

- fork: faster-cpython
- version: 3.14.0a1+
- config: 
- commit hash: [1746ca4](https://github.com/faster%2dcpython/cpython/commit/1746ca4)
- commit date: 2024-10-29T15:38:43+00:00
- commit merge base: [faa3272fb8d63d481a136cc0467a0cba6ed7b264](https://github.com/faster%2dcpython/cpython/commit/faa3272fb8d63d481a136cc0467a0cba6ed7b264)
- ref: more_untracking

## linux x86_64 (azure)

- [pystats raw](bm-20241029-azure-x86_64-faster%252dcpython-more_untracking-3.14.0a1%2B-1746ca4-pystats.json)
- [pystats table](bm-20241029-azure-x86_64-faster%252dcpython-more_untracking-3.14.0a1%2B-1746ca4-pystats.md)

### vs. base

- [pystats diff](bm-20241029-azure-x86_64-faster%252dcpython-more_untracking-3.14.0a1%2B-1746ca4-pystats-vs-base.md)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11577425958)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-105-generic-x86_64-with-glibc2.35
- [raw results](bm-20241029-pythonperf2-x86_64-faster%252dcpython-more_untracking-3.14.0a1%2B-1746ca4.json)

### vs. 3.10.4

- Geometric mean: 1.317x faster (HPT: reliability of 100.00%, 1.22x faster at 99th %ile)
- Memory usage: 1.26x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, shortest_path, sphinx
- [📄table](bm-20241029-pythonperf2-x86_64-faster%252dcpython-more_untracking-3.14.0a1%2B-1746ca4-vs-3.10.4.md)
- [📈time plot](bm-20241029-pythonperf2-x86_64-faster%252dcpython-more_untracking-3.14.0a1%2B-1746ca4-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.012x faster (HPT: reliability of 88.00%, 1.00x faster at 99th %ile)
- Memory usage: 1.03x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, pylint, shortest_path, sphinx, thrift
- [📄table](bm-20241029-pythonperf2-x86_64-faster%252dcpython-more_untracking-3.14.0a1%2B-1746ca4-vs-3.12.0.md)
- [📈time plot](bm-20241029-pythonperf2-x86_64-faster%252dcpython-more_untracking-3.14.0a1%2B-1746ca4-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.016x faster (HPT: reliability of 99.85%, 1.00x faster at 99th %ile)
- Memory usage: 1.01x
- missing benchmarks: chameleon, gevent_hub, mypy2
- [📄table](bm-20241029-pythonperf2-x86_64-faster%252dcpython-more_untracking-3.14.0a1%2B-1746ca4-vs-3.13.0.md)
- [📈time plot](bm-20241029-pythonperf2-x86_64-faster%252dcpython-more_untracking-3.14.0a1%2B-1746ca4-vs-3.13.0.svg)

### vs. base

- [🧠memory plot](bm-20241029-pythonperf2-x86_64-faster%252dcpython-more_untracking-3.14.0a1%2B-1746ca4-vs-base-mem.svg)
- [📈time plot](bm-20241029-pythonperf2-x86_64-faster%252dcpython-more_untracking-3.14.0a1%2B-1746ca4-vs-base.svg)


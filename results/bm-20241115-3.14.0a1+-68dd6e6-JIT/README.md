# Results

- fork: brandtbucher/justin_dwarf
- version: 3.14.0a1+
- config: JIT
- commit hash: [68dd6e6](https://github.com/brandtbucher/cpython/commit/68dd6e6)
- commit date: 2024-11-15T18:36:48-08:00
- commit merge base: [09d6f5dc7824c74672add512619e978844ff8051](https://github.com/python/cpython/commit/09d6f5dc7824c74672add512619e978844ff8051)
- ref: justin_dwarf

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11866478120)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-196-generic-x86_64-with-glibc2.31
- [raw results](bm-20241115-linux-x86_64-brandtbucher-justin_dwarf-3.14.0a1%2B-68dd6e6.json)

### vs. 3.10.4

- Geometric mean: 1.389x faster (HPT: reliability of 100.00%, 1.23x faster at 99th %ile)
- Memory usage: 1.37x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20241115-linux-x86_64-brandtbucher-justin_dwarf-3.14.0a1%2B-68dd6e6-vs-3.10.4.md)
- [📈time plot](bm-20241115-linux-x86_64-brandtbucher-justin_dwarf-3.14.0a1%2B-68dd6e6-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.061x faster (HPT: reliability of 99.99%, 1.02x faster at 99th %ile)
- Memory usage: 1.17x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20241115-linux-x86_64-brandtbucher-justin_dwarf-3.14.0a1%2B-68dd6e6-vs-3.12.0.md)
- [📈time plot](bm-20241115-linux-x86_64-brandtbucher-justin_dwarf-3.14.0a1%2B-68dd6e6-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.002x slower (HPT: reliability of 60.88%, 1.00x slower at 99th %ile)
- Memory usage: 1.10x
- missing benchmarks: chameleon, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20241115-linux-x86_64-brandtbucher-justin_dwarf-3.14.0a1%2B-68dd6e6-vs-3.13.0.md)
- [📈time plot](bm-20241115-linux-x86_64-brandtbucher-justin_dwarf-3.14.0a1%2B-68dd6e6-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.004x faster (HPT: reliability of 99.37%, 1.00x faster at 99th %ile)
- Memory usage: 1.02x
- [🧠memory plot](bm-20241115-linux-x86_64-brandtbucher-justin_dwarf-3.14.0a1%2B-68dd6e6-vs-base-mem.svg)
- [📄table](bm-20241115-linux-x86_64-brandtbucher-justin_dwarf-3.14.0a1%2B-68dd6e6-vs-base.md)
- [📈time plot](bm-20241115-linux-x86_64-brandtbucher-justin_dwarf-3.14.0a1%2B-68dd6e6-vs-base.svg)


# Results vs. 3.12.0

- fork: faster-cpython
- ref: virtual_iterators
- machine: windows-amd64
- commit hash: cad1946
- commit date: 2025-04-30
- overall geometric mean: 1.094x faster
- HPT reliability: 99.98%
- HPT 99th percentile: 1.02x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250430-pythonperf1-amd64-faster%2dcpython-virtual_iterators-3.14.0a7+-cad1946 |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 220 ms: 1.01x slower                                                               |
| docutils       | 1.66 sec                                                    | 1.65 sec: 1.01x faster                                                             |
| Geometric mean | (ref)                                                       | 1.00x slower                                                                       |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250430-pythonperf1-amd64-faster%2dcpython-virtual_iterators-3.14.0a7+-cad1946 |
|----------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 400 ms: 1.93x faster                                                               |
| async_tree_io              | 731 ms                                                      | 409 ms: 1.79x faster                                                               |
| async_tree_memoization_tg  | 367 ms                                                      | 210 ms: 1.75x faster                                                               |
| async_tree_none_tg         | 285 ms                                                      | 171 ms: 1.66x faster                                                               |
| async_tree_memoization     | 339 ms                                                      | 207 ms: 1.64x faster                                                               |
| async_tree_none            | 291 ms                                                      | 180 ms: 1.62x faster                                                               |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 334 ms: 1.47x faster                                                               |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 344 ms: 1.46x faster                                                               |
| Geometric mean             | (ref)                                                       | 1.66x faster                                                                       |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250430-pythonperf1-amd64-faster%2dcpython-virtual_iterators-3.14.0a7+-cad1946 |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 44.0 ms: 1.29x faster                                                              |
| nbody          | 71.9 ms                                                     | 63.7 ms: 1.13x faster                                                              |
| pidigits       | 152 ms                                                      | 149 ms: 1.02x faster                                                               |
| Geometric mean | (ref)                                                       | 1.14x faster                                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250430-pythonperf1-amd64-faster%2dcpython-virtual_iterators-3.14.0a7+-cad1946 |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| regex_effbot   | 1.62 ms                                                     | 1.45 ms: 1.11x faster                                                              |
| regex_compile  | 87.5 ms                                                     | 80.4 ms: 1.09x faster                                                              |
| regex_dna      | 126 ms                                                      | 121 ms: 1.04x faster                                                               |
| Geometric mean | (ref)                                                       | 1.06x faster                                                                       |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250430-pythonperf1-amd64-faster%2dcpython-virtual_iterators-3.14.0a7+-cad1946 |
|----------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| xml_etree_parse      | 93.0 ms                                                     | 88.7 ms: 1.05x faster                                                              |
| xml_etree_iterparse  | 65.2 ms                                                     | 63.6 ms: 1.02x faster                                                              |
| tomli_loads          | 1.37 sec                                                    | 1.38 sec: 1.01x slower                                                             |
| xml_etree_generate   | 55.8 ms                                                     | 56.4 ms: 1.01x slower                                                              |
| unpickle_pure_python | 133 us                                                      | 139 us: 1.04x slower                                                               |
| xml_etree_process    | 37.7 ms                                                     | 39.7 ms: 1.05x slower                                                              |
| pickle_pure_python   | 195 us                                                      | 212 us: 1.08x slower                                                               |
| json_loads           | 13.9 us                                                     | 15.4 us: 1.10x slower                                                              |
| json_dumps           | 5.70 ms                                                     | 6.96 ms: 1.22x slower                                                              |
| Geometric mean       | (ref)                                                       | 1.05x slower                                                                       |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250430-pythonperf1-amd64-faster%2dcpython-virtual_iterators-3.14.0a7+-cad1946 |
|------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 19.7 ms: 1.21x slower                                                              |
| python_startup         | 19.5 ms                                                     | 26.2 ms: 1.34x slower                                                              |
| Geometric mean         | (ref)                                                       | 1.28x slower                                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250430-pythonperf1-amd64-faster%2dcpython-virtual_iterators-3.14.0a7+-cad1946 |
|-----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 6.54 ms: 1.08x faster                                                              |
| django_template | 22.9 ms                                                     | 24.4 ms: 1.06x slower                                                              |
| Geometric mean  | (ref)                                                       | 1.01x faster                                                                       |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250430-pythonperf1-amd64-faster%2dcpython-virtual_iterators-3.14.0a7+-cad1946 |
|----------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| pathlib                    | 80.5 ms                                                     | 32.1 ms: 2.51x faster                                                              |
| async_tree_io_tg           | 771 ms                                                      | 400 ms: 1.93x faster                                                               |
| async_tree_io              | 731 ms                                                      | 409 ms: 1.79x faster                                                               |
| mdp                        | 1.37 sec                                                    | 777 ms: 1.77x faster                                                               |
| async_tree_memoization_tg  | 367 ms                                                      | 210 ms: 1.75x faster                                                               |
| async_tree_none_tg         | 285 ms                                                      | 171 ms: 1.66x faster                                                               |
| async_tree_memoization     | 339 ms                                                      | 207 ms: 1.64x faster                                                               |
| async_tree_none            | 291 ms                                                      | 180 ms: 1.62x faster                                                               |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 334 ms: 1.47x faster                                                               |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 344 ms: 1.46x faster                                                               |
| deepcopy                   | 238 us                                                      | 167 us: 1.42x faster                                                               |
| comprehensions             | 14.1 us                                                     | 10.6 us: 1.33x faster                                                              |
| deepcopy_memo              | 23.7 us                                                     | 18.2 us: 1.30x faster                                                              |
| float                      | 56.8 ms                                                     | 44.0 ms: 1.29x faster                                                              |
| go                         | 91.6 ms                                                     | 77.3 ms: 1.19x faster                                                              |
| spectral_norm              | 66.9 ms                                                     | 57.0 ms: 1.17x faster                                                              |
| generators                 | 22.5 ms                                                     | 19.3 ms: 1.17x faster                                                              |
| deepcopy_reduce            | 2.09 us                                                     | 1.84 us: 1.14x faster                                                              |
| nbody                      | 71.9 ms                                                     | 63.7 ms: 1.13x faster                                                              |
| sqlite_synth               | 1.76 us                                                     | 1.58 us: 1.11x faster                                                              |
| regex_effbot               | 1.62 ms                                                     | 1.45 ms: 1.11x faster                                                              |
| chaos                      | 43.3 ms                                                     | 39.1 ms: 1.11x faster                                                              |
| raytrace                   | 192 ms                                                      | 176 ms: 1.09x faster                                                               |
| logging_silent             | 60.5 ns                                                     | 55.4 ns: 1.09x faster                                                              |
| regex_compile              | 87.5 ms                                                     | 80.4 ms: 1.09x faster                                                              |
| mako                       | 7.09 ms                                                     | 6.54 ms: 1.08x faster                                                              |
| scimark_monte_carlo        | 43.7 ms                                                     | 40.5 ms: 1.08x faster                                                              |
| pyflate                    | 295 ms                                                      | 276 ms: 1.07x faster                                                               |
| meteor_contest             | 74.6 ms                                                     | 70.7 ms: 1.06x faster                                                              |
| dulwich_log                | 44.3 ms                                                     | 42.0 ms: 1.05x faster                                                              |
| coroutines                 | 14.3 ms                                                     | 13.6 ms: 1.05x faster                                                              |
| xml_etree_parse            | 93.0 ms                                                     | 88.7 ms: 1.05x faster                                                              |
| regex_dna                  | 126 ms                                                      | 121 ms: 1.04x faster                                                               |
| nqueens                    | 62.8 ms                                                     | 60.2 ms: 1.04x faster                                                              |
| scimark_sor                | 78.8 ms                                                     | 75.7 ms: 1.04x faster                                                              |
| pprint_pformat             | 1.05 sec                                                    | 1.00 sec: 1.04x faster                                                             |
| hexiom                     | 4.10 ms                                                     | 3.95 ms: 1.04x faster                                                              |
| pprint_safe_repr           | 513 ms                                                      | 494 ms: 1.04x faster                                                               |
| richards                   | 28.4 ms                                                     | 27.5 ms: 1.03x faster                                                              |
| async_generators           | 239 ms                                                      | 232 ms: 1.03x faster                                                               |
| xml_etree_iterparse        | 65.2 ms                                                     | 63.6 ms: 1.02x faster                                                              |
| pidigits                   | 152 ms                                                      | 149 ms: 1.02x faster                                                               |
| richards_super             | 32.1 ms                                                     | 31.4 ms: 1.02x faster                                                              |
| crypto_pyaes               | 48.5 ms                                                     | 47.9 ms: 1.01x faster                                                              |
| docutils                   | 1.66 sec                                                    | 1.65 sec: 1.01x faster                                                             |
| tomli_loads                | 1.37 sec                                                    | 1.38 sec: 1.01x slower                                                             |
| 2to3                       | 218 ms                                                      | 220 ms: 1.01x slower                                                               |
| xml_etree_generate         | 55.8 ms                                                     | 56.4 ms: 1.01x slower                                                              |
| json                       | 3.05 ms                                                     | 3.08 ms: 1.01x slower                                                              |
| scimark_fft                | 184 ms                                                      | 188 ms: 1.02x slower                                                               |
| logging_format             | 6.72 us                                                     | 6.83 us: 1.02x slower                                                              |
| fannkuch                   | 247 ms                                                      | 251 ms: 1.02x slower                                                               |
| deltablue                  | 2.16 ms                                                     | 2.20 ms: 1.02x slower                                                              |
| pycparser                  | 699 ms                                                      | 714 ms: 1.02x slower                                                               |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.61 ms: 1.02x slower                                                              |
| unpickle_pure_python       | 133 us                                                      | 139 us: 1.04x slower                                                               |
| xml_etree_process          | 37.7 ms                                                     | 39.7 ms: 1.05x slower                                                              |
| typing_runtime_protocols   | 95.1 us                                                     | 100 us: 1.05x slower                                                               |
| django_template            | 22.9 ms                                                     | 24.4 ms: 1.06x slower                                                              |
| scimark_lu                 | 58.9 ms                                                     | 62.8 ms: 1.07x slower                                                              |
| pickle_pure_python         | 195 us                                                      | 212 us: 1.08x slower                                                               |
| json_loads                 | 13.9 us                                                     | 15.4 us: 1.10x slower                                                              |
| telco                      | 4.13 ms                                                     | 4.61 ms: 1.12x slower                                                              |
| python_startup_no_site     | 16.2 ms                                                     | 19.7 ms: 1.21x slower                                                              |
| json_dumps                 | 5.70 ms                                                     | 6.96 ms: 1.22x slower                                                              |
| coverage                   | 40.8 ms                                                     | 51.2 ms: 1.25x slower                                                              |
| bench_mp_pool              | 69.2 ms                                                     | 90.2 ms: 1.30x slower                                                              |
| python_startup             | 19.5 ms                                                     | 26.2 ms: 1.34x slower                                                              |
| gc_traversal               | 1.52 ms                                                     | 2.08 ms: 1.37x slower                                                              |
| create_gc_cycles           | 752 us                                                      | 1.26 ms: 1.67x slower                                                              |
| Geometric mean             | (ref)                                                       | 1.09x faster                                                                       |

Benchmark hidden because not significant (3): regex_v8, logging_simple, bench_thread_pool
Ignored benchmarks (23) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, sympy_expand, sympy_integrate, sympy_str, sympy_sum, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250430-3.14.0a7+-cad1946/bm-20250430-pythonperf1-amd64-faster%2dcpython-virtual_iterators-3.14.0a7+-cad1946.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.094x faster

# HPT report

- Reliability score: 99.98% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: unknown
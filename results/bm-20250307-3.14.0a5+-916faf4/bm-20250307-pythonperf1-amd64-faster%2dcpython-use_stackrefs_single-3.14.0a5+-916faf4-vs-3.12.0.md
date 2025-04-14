# Results vs. 3.12.0

- fork: faster-cpython
- ref: use_stackrefs_single
- machine: windows-amd64
- commit hash: 916faf4
- commit date: 2025-03-07
- overall geometric mean: 1.035x faster
- HPT reliability: 62.45%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250307-pythonperf1-amd64-faster%2dcpython-use_stackrefs_single-3.14.0a5+-916faf4 |
|----------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 228 ms: 1.05x slower                                                                  |
| docutils       | 1.66 sec                                                    | 1.69 sec: 1.02x slower                                                                |
| Geometric mean | (ref)                                                       | 1.03x slower                                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250307-pythonperf1-amd64-faster%2dcpython-use_stackrefs_single-3.14.0a5+-916faf4 |
|----------------------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 416 ms: 1.86x faster                                                                  |
| async_tree_io              | 731 ms                                                      | 426 ms: 1.72x faster                                                                  |
| async_tree_memoization_tg  | 367 ms                                                      | 217 ms: 1.69x faster                                                                  |
| async_tree_none_tg         | 285 ms                                                      | 179 ms: 1.59x faster                                                                  |
| async_tree_memoization     | 339 ms                                                      | 220 ms: 1.54x faster                                                                  |
| async_tree_none            | 291 ms                                                      | 190 ms: 1.53x faster                                                                  |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 346 ms: 1.45x faster                                                                  |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 344 ms: 1.42x faster                                                                  |
| Geometric mean             | (ref)                                                       | 1.60x faster                                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250307-pythonperf1-amd64-faster%2dcpython-use_stackrefs_single-3.14.0a5+-916faf4 |
|----------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 47.0 ms: 1.21x faster                                                                 |
| nbody          | 71.9 ms                                                     | 66.2 ms: 1.09x faster                                                                 |
| Geometric mean | (ref)                                                       | 1.09x faster                                                                          |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250307-pythonperf1-amd64-faster%2dcpython-use_stackrefs_single-3.14.0a5+-916faf4 |
|----------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| regex_effbot   | 1.62 ms                                                     | 1.42 ms: 1.14x faster                                                                 |
| regex_dna      | 126 ms                                                      | 114 ms: 1.11x faster                                                                  |
| regex_compile  | 87.5 ms                                                     | 86.2 ms: 1.01x faster                                                                 |
| regex_v8       | 14.2 ms                                                     | 14.6 ms: 1.03x slower                                                                 |
| Geometric mean | (ref)                                                       | 1.06x faster                                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250307-pythonperf1-amd64-faster%2dcpython-use_stackrefs_single-3.14.0a5+-916faf4 |
|----------------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| xml_etree_parse      | 93.0 ms                                                     | 91.9 ms: 1.01x faster                                                                 |
| xml_etree_iterparse  | 65.2 ms                                                     | 66.1 ms: 1.02x slower                                                                 |
| tomli_loads          | 1.37 sec                                                    | 1.42 sec: 1.04x slower                                                                |
| xml_etree_generate   | 55.8 ms                                                     | 58.3 ms: 1.04x slower                                                                 |
| json_loads           | 13.9 us                                                     | 15.1 us: 1.08x slower                                                                 |
| xml_etree_process    | 37.7 ms                                                     | 41.7 ms: 1.11x slower                                                                 |
| unpickle_pure_python | 133 us                                                      | 148 us: 1.11x slower                                                                  |
| pickle_pure_python   | 195 us                                                      | 227 us: 1.16x slower                                                                  |
| json_dumps           | 5.70 ms                                                     | 6.95 ms: 1.22x slower                                                                 |
| Geometric mean       | (ref)                                                       | 1.08x slower                                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250307-pythonperf1-amd64-faster%2dcpython-use_stackrefs_single-3.14.0a5+-916faf4 |
|------------------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 19.7 ms: 1.21x slower                                                                 |
| python_startup         | 19.5 ms                                                     | 26.1 ms: 1.34x slower                                                                 |
| Geometric mean         | (ref)                                                       | 1.27x slower                                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250307-pythonperf1-amd64-faster%2dcpython-use_stackrefs_single-3.14.0a5+-916faf4 |
|-----------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| django_template | 22.9 ms                                                     | 26.2 ms: 1.14x slower                                                                 |
| Geometric mean  | (ref)                                                       | 1.06x slower                                                                          |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250307-pythonperf1-amd64-faster%2dcpython-use_stackrefs_single-3.14.0a5+-916faf4 |
|----------------------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| pathlib                    | 80.5 ms                                                     | 32.2 ms: 2.50x faster                                                                 |
| async_tree_io_tg           | 771 ms                                                      | 416 ms: 1.86x faster                                                                  |
| async_tree_io              | 731 ms                                                      | 426 ms: 1.72x faster                                                                  |
| async_tree_memoization_tg  | 367 ms                                                      | 217 ms: 1.69x faster                                                                  |
| async_tree_none_tg         | 285 ms                                                      | 179 ms: 1.59x faster                                                                  |
| async_tree_memoization     | 339 ms                                                      | 220 ms: 1.54x faster                                                                  |
| async_tree_none            | 291 ms                                                      | 190 ms: 1.53x faster                                                                  |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 346 ms: 1.45x faster                                                                  |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 344 ms: 1.42x faster                                                                  |
| deepcopy                   | 238 us                                                      | 184 us: 1.29x faster                                                                  |
| deepcopy_memo              | 23.7 us                                                     | 19.4 us: 1.22x faster                                                                 |
| float                      | 56.8 ms                                                     | 47.0 ms: 1.21x faster                                                                 |
| comprehensions             | 14.1 us                                                     | 11.8 us: 1.19x faster                                                                 |
| spectral_norm              | 66.9 ms                                                     | 56.5 ms: 1.18x faster                                                                 |
| generators                 | 22.5 ms                                                     | 19.5 ms: 1.15x faster                                                                 |
| regex_effbot               | 1.62 ms                                                     | 1.42 ms: 1.14x faster                                                                 |
| sqlite_synth               | 1.76 us                                                     | 1.58 us: 1.11x faster                                                                 |
| regex_dna                  | 126 ms                                                      | 114 ms: 1.11x faster                                                                  |
| nbody                      | 71.9 ms                                                     | 66.2 ms: 1.09x faster                                                                 |
| deepcopy_reduce            | 2.09 us                                                     | 1.97 us: 1.06x faster                                                                 |
| async_generators           | 239 ms                                                      | 228 ms: 1.05x faster                                                                  |
| coroutines                 | 14.3 ms                                                     | 13.6 ms: 1.05x faster                                                                 |
| go                         | 91.6 ms                                                     | 87.6 ms: 1.05x faster                                                                 |
| logging_silent             | 60.5 ns                                                     | 58.7 ns: 1.03x faster                                                                 |
| chaos                      | 43.3 ms                                                     | 42.2 ms: 1.03x faster                                                                 |
| scimark_fft                | 184 ms                                                      | 180 ms: 1.02x faster                                                                  |
| dulwich_log                | 44.3 ms                                                     | 43.5 ms: 1.02x faster                                                                 |
| scimark_monte_carlo        | 43.7 ms                                                     | 43.1 ms: 1.02x faster                                                                 |
| regex_compile              | 87.5 ms                                                     | 86.2 ms: 1.01x faster                                                                 |
| json                       | 3.05 ms                                                     | 3.01 ms: 1.01x faster                                                                 |
| xml_etree_parse            | 93.0 ms                                                     | 91.9 ms: 1.01x faster                                                                 |
| scimark_sor                | 78.8 ms                                                     | 77.9 ms: 1.01x faster                                                                 |
| sympy_sum                  | 91.5 ms                                                     | 90.7 ms: 1.01x faster                                                                 |
| raytrace                   | 192 ms                                                      | 194 ms: 1.01x slower                                                                  |
| meteor_contest             | 74.6 ms                                                     | 75.6 ms: 1.01x slower                                                                 |
| sympy_str                  | 175 ms                                                      | 178 ms: 1.01x slower                                                                  |
| xml_etree_iterparse        | 65.2 ms                                                     | 66.1 ms: 1.02x slower                                                                 |
| crypto_pyaes               | 48.5 ms                                                     | 49.5 ms: 1.02x slower                                                                 |
| docutils                   | 1.66 sec                                                    | 1.69 sec: 1.02x slower                                                                |
| bench_thread_pool          | 857 us                                                      | 876 us: 1.02x slower                                                                  |
| regex_v8                   | 14.2 ms                                                     | 14.6 ms: 1.03x slower                                                                 |
| richards                   | 28.4 ms                                                     | 29.2 ms: 1.03x slower                                                                 |
| richards_super             | 32.1 ms                                                     | 33.1 ms: 1.03x slower                                                                 |
| sqlglot_optimize           | 34.5 ms                                                     | 35.6 ms: 1.03x slower                                                                 |
| scimark_lu                 | 58.9 ms                                                     | 61.0 ms: 1.04x slower                                                                 |
| sympy_integrate            | 13.0 ms                                                     | 13.4 ms: 1.04x slower                                                                 |
| pyflate                    | 295 ms                                                      | 306 ms: 1.04x slower                                                                  |
| logging_simple             | 6.28 us                                                     | 6.52 us: 1.04x slower                                                                 |
| tomli_loads                | 1.37 sec                                                    | 1.42 sec: 1.04x slower                                                                |
| nqueens                    | 62.8 ms                                                     | 65.5 ms: 1.04x slower                                                                 |
| xml_etree_generate         | 55.8 ms                                                     | 58.3 ms: 1.04x slower                                                                 |
| 2to3                       | 218 ms                                                      | 228 ms: 1.05x slower                                                                  |
| sqlglot_normalize          | 187 ms                                                      | 196 ms: 1.05x slower                                                                  |
| deltablue                  | 2.16 ms                                                     | 2.27 ms: 1.05x slower                                                                 |
| logging_format             | 6.72 us                                                     | 7.06 us: 1.05x slower                                                                 |
| pprint_pformat             | 1.05 sec                                                    | 1.11 sec: 1.06x slower                                                                |
| hexiom                     | 4.10 ms                                                     | 4.36 ms: 1.06x slower                                                                 |
| pycparser                  | 699 ms                                                      | 745 ms: 1.07x slower                                                                  |
| pprint_safe_repr           | 513 ms                                                      | 548 ms: 1.07x slower                                                                  |
| sympy_expand               | 284 ms                                                      | 306 ms: 1.08x slower                                                                  |
| json_loads                 | 13.9 us                                                     | 15.1 us: 1.08x slower                                                                 |
| sqlglot_transpile          | 1.02 ms                                                     | 1.12 ms: 1.09x slower                                                                 |
| xml_etree_process          | 37.7 ms                                                     | 41.7 ms: 1.11x slower                                                                 |
| sqlglot_parse              | 804 us                                                      | 891 us: 1.11x slower                                                                  |
| unpickle_pure_python       | 133 us                                                      | 148 us: 1.11x slower                                                                  |
| fannkuch                   | 247 ms                                                      | 274 ms: 1.11x slower                                                                  |
| django_template            | 22.9 ms                                                     | 26.2 ms: 1.14x slower                                                                 |
| coverage                   | 40.8 ms                                                     | 47.2 ms: 1.16x slower                                                                 |
| pickle_pure_python         | 195 us                                                      | 227 us: 1.16x slower                                                                  |
| typing_runtime_protocols   | 95.1 us                                                     | 111 us: 1.17x slower                                                                  |
| mdp                        | 1.37 sec                                                    | 1.61 sec: 1.17x slower                                                                |
| telco                      | 4.13 ms                                                     | 4.96 ms: 1.20x slower                                                                 |
| python_startup_no_site     | 16.2 ms                                                     | 19.7 ms: 1.21x slower                                                                 |
| json_dumps                 | 5.70 ms                                                     | 6.95 ms: 1.22x slower                                                                 |
| bench_mp_pool              | 69.2 ms                                                     | 87.7 ms: 1.27x slower                                                                 |
| gc_traversal               | 1.52 ms                                                     | 2.04 ms: 1.34x slower                                                                 |
| python_startup             | 19.5 ms                                                     | 26.1 ms: 1.34x slower                                                                 |
| create_gc_cycles           | 752 us                                                      | 1.25 ms: 1.66x slower                                                                 |
| Geometric mean             | (ref)                                                       | 1.03x faster                                                                          |

Benchmark hidden because not significant (3): mako, scimark_sparse_mat_mult, pidigits
Ignored benchmarks (15) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (13) of results/bm-20250307-3.14.0a5+-916faf4/bm-20250307-pythonperf1-amd64-faster%2dcpython-use_stackrefs_single-3.14.0a5+-916faf4.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.035x faster

# HPT report

- Reliability score: 62.45% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown
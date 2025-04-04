# Results vs. 3.12.0

- fork: faster-cpython
- ref: tos_caching_1
- machine: windows-amd64
- commit hash: 492df4e
- commit date: 2025-04-04
- overall geometric mean: 1.064x faster
- HPT reliability: 96.62%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250404-pythonperf1-amd64-faster%2dcpython-tos_caching_1-3.14.0a6+-492df4e |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 222 ms: 1.02x slower                                                           |
| docutils       | 1.66 sec                                                    | 1.64 sec: 1.01x faster                                                         |
| Geometric mean | (ref)                                                       | 1.00x slower                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250404-pythonperf1-amd64-faster%2dcpython-tos_caching_1-3.14.0a6+-492df4e |
|----------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 417 ms: 1.85x faster                                                           |
| async_tree_io              | 731 ms                                                      | 420 ms: 1.74x faster                                                           |
| async_tree_memoization_tg  | 367 ms                                                      | 217 ms: 1.69x faster                                                           |
| async_tree_none_tg         | 285 ms                                                      | 178 ms: 1.60x faster                                                           |
| async_tree_memoization     | 339 ms                                                      | 213 ms: 1.59x faster                                                           |
| async_tree_none            | 291 ms                                                      | 187 ms: 1.56x faster                                                           |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 343 ms: 1.46x faster                                                           |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 337 ms: 1.45x faster                                                           |
| Geometric mean             | (ref)                                                       | 1.61x faster                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250404-pythonperf1-amd64-faster%2dcpython-tos_caching_1-3.14.0a6+-492df4e |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 46.9 ms: 1.21x faster                                                          |
| nbody          | 71.9 ms                                                     | 69.4 ms: 1.04x faster                                                          |
| pidigits       | 152 ms                                                      | 149 ms: 1.02x faster                                                           |
| Geometric mean | (ref)                                                       | 1.09x faster                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250404-pythonperf1-amd64-faster%2dcpython-tos_caching_1-3.14.0a6+-492df4e |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_effbot   | 1.62 ms                                                     | 1.40 ms: 1.15x faster                                                          |
| regex_dna      | 126 ms                                                      | 114 ms: 1.10x faster                                                           |
| regex_v8       | 14.2 ms                                                     | 13.6 ms: 1.05x faster                                                          |
| regex_compile  | 87.5 ms                                                     | 83.7 ms: 1.05x faster                                                          |
| Geometric mean | (ref)                                                       | 1.09x faster                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250404-pythonperf1-amd64-faster%2dcpython-tos_caching_1-3.14.0a6+-492df4e |
|----------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| xml_etree_parse      | 93.0 ms                                                     | 88.7 ms: 1.05x faster                                                          |
| tomli_loads          | 1.37 sec                                                    | 1.40 sec: 1.03x slower                                                         |
| xml_etree_iterparse  | 65.2 ms                                                     | 68.1 ms: 1.04x slower                                                          |
| xml_etree_generate   | 55.8 ms                                                     | 59.3 ms: 1.06x slower                                                          |
| json_loads           | 13.9 us                                                     | 15.4 us: 1.11x slower                                                          |
| xml_etree_process    | 37.7 ms                                                     | 41.8 ms: 1.11x slower                                                          |
| unpickle_pure_python | 133 us                                                      | 148 us: 1.11x slower                                                           |
| pickle_pure_python   | 195 us                                                      | 221 us: 1.13x slower                                                           |
| json_dumps           | 5.70 ms                                                     | 6.91 ms: 1.21x slower                                                          |
| Geometric mean       | (ref)                                                       | 1.08x slower                                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250404-pythonperf1-amd64-faster%2dcpython-tos_caching_1-3.14.0a6+-492df4e |
|------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 20.4 ms: 1.26x slower                                                          |
| python_startup         | 19.5 ms                                                     | 26.5 ms: 1.36x slower                                                          |
| Geometric mean         | (ref)                                                       | 1.31x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250404-pythonperf1-amd64-faster%2dcpython-tos_caching_1-3.14.0a6+-492df4e |
|-----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 7.25 ms: 1.02x slower                                                          |
| django_template | 22.9 ms                                                     | 24.4 ms: 1.06x slower                                                          |
| Geometric mean  | (ref)                                                       | 1.04x slower                                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250404-pythonperf1-amd64-faster%2dcpython-tos_caching_1-3.14.0a6+-492df4e |
|----------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pathlib                    | 80.5 ms                                                     | 32.2 ms: 2.50x faster                                                          |
| async_tree_io_tg           | 771 ms                                                      | 417 ms: 1.85x faster                                                           |
| async_tree_io              | 731 ms                                                      | 420 ms: 1.74x faster                                                           |
| async_tree_memoization_tg  | 367 ms                                                      | 217 ms: 1.69x faster                                                           |
| mdp                        | 1.37 sec                                                    | 817 ms: 1.68x faster                                                           |
| async_tree_none_tg         | 285 ms                                                      | 178 ms: 1.60x faster                                                           |
| async_tree_memoization     | 339 ms                                                      | 213 ms: 1.59x faster                                                           |
| async_tree_none            | 291 ms                                                      | 187 ms: 1.56x faster                                                           |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 343 ms: 1.46x faster                                                           |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 337 ms: 1.45x faster                                                           |
| deepcopy                   | 238 us                                                      | 177 us: 1.35x faster                                                           |
| deepcopy_memo              | 23.7 us                                                     | 19.2 us: 1.24x faster                                                          |
| comprehensions             | 14.1 us                                                     | 11.6 us: 1.21x faster                                                          |
| float                      | 56.8 ms                                                     | 46.9 ms: 1.21x faster                                                          |
| regex_effbot               | 1.62 ms                                                     | 1.40 ms: 1.15x faster                                                          |
| go                         | 91.6 ms                                                     | 80.0 ms: 1.14x faster                                                          |
| spectral_norm              | 66.9 ms                                                     | 59.1 ms: 1.13x faster                                                          |
| chaos                      | 43.3 ms                                                     | 38.8 ms: 1.12x faster                                                          |
| sqlite_synth               | 1.76 us                                                     | 1.58 us: 1.11x faster                                                          |
| deepcopy_reduce            | 2.09 us                                                     | 1.89 us: 1.11x faster                                                          |
| regex_dna                  | 126 ms                                                      | 114 ms: 1.10x faster                                                           |
| scimark_monte_carlo        | 43.7 ms                                                     | 40.5 ms: 1.08x faster                                                          |
| raytrace                   | 192 ms                                                      | 178 ms: 1.08x faster                                                           |
| dulwich_log                | 44.3 ms                                                     | 42.0 ms: 1.05x faster                                                          |
| xml_etree_parse            | 93.0 ms                                                     | 88.7 ms: 1.05x faster                                                          |
| regex_v8                   | 14.2 ms                                                     | 13.6 ms: 1.05x faster                                                          |
| regex_compile              | 87.5 ms                                                     | 83.7 ms: 1.05x faster                                                          |
| scimark_fft                | 184 ms                                                      | 178 ms: 1.04x faster                                                           |
| nbody                      | 71.9 ms                                                     | 69.4 ms: 1.04x faster                                                          |
| async_generators           | 239 ms                                                      | 233 ms: 1.03x faster                                                           |
| crypto_pyaes               | 48.5 ms                                                     | 47.1 ms: 1.03x faster                                                          |
| pidigits                   | 152 ms                                                      | 149 ms: 1.02x faster                                                           |
| sympy_sum                  | 91.5 ms                                                     | 89.5 ms: 1.02x faster                                                          |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.50 ms: 1.02x faster                                                          |
| sympy_integrate            | 13.0 ms                                                     | 12.7 ms: 1.02x faster                                                          |
| pyflate                    | 295 ms                                                      | 291 ms: 1.01x faster                                                           |
| sympy_str                  | 175 ms                                                      | 173 ms: 1.01x faster                                                           |
| docutils                   | 1.66 sec                                                    | 1.64 sec: 1.01x faster                                                         |
| meteor_contest             | 74.6 ms                                                     | 74.0 ms: 1.01x faster                                                          |
| pprint_safe_repr           | 513 ms                                                      | 519 ms: 1.01x slower                                                           |
| scimark_sor                | 78.8 ms                                                     | 80.0 ms: 1.02x slower                                                          |
| pprint_pformat             | 1.05 sec                                                    | 1.06 sec: 1.02x slower                                                         |
| 2to3                       | 218 ms                                                      | 222 ms: 1.02x slower                                                           |
| mako                       | 7.09 ms                                                     | 7.25 ms: 1.02x slower                                                          |
| tomli_loads                | 1.37 sec                                                    | 1.40 sec: 1.03x slower                                                         |
| json                       | 3.05 ms                                                     | 3.13 ms: 1.03x slower                                                          |
| pycparser                  | 699 ms                                                      | 720 ms: 1.03x slower                                                           |
| richards                   | 28.4 ms                                                     | 29.3 ms: 1.03x slower                                                          |
| richards_super             | 32.1 ms                                                     | 33.2 ms: 1.04x slower                                                          |
| hexiom                     | 4.10 ms                                                     | 4.25 ms: 1.04x slower                                                          |
| xml_etree_iterparse        | 65.2 ms                                                     | 68.1 ms: 1.04x slower                                                          |
| deltablue                  | 2.16 ms                                                     | 2.26 ms: 1.05x slower                                                          |
| fannkuch                   | 247 ms                                                      | 258 ms: 1.05x slower                                                           |
| sympy_expand               | 284 ms                                                      | 299 ms: 1.05x slower                                                           |
| logging_silent             | 60.5 ns                                                     | 64.0 ns: 1.06x slower                                                          |
| django_template            | 22.9 ms                                                     | 24.4 ms: 1.06x slower                                                          |
| xml_etree_generate         | 55.8 ms                                                     | 59.3 ms: 1.06x slower                                                          |
| scimark_lu                 | 58.9 ms                                                     | 62.8 ms: 1.07x slower                                                          |
| coroutines                 | 14.3 ms                                                     | 15.3 ms: 1.07x slower                                                          |
| json_loads                 | 13.9 us                                                     | 15.4 us: 1.11x slower                                                          |
| xml_etree_process          | 37.7 ms                                                     | 41.8 ms: 1.11x slower                                                          |
| unpickle_pure_python       | 133 us                                                      | 148 us: 1.11x slower                                                           |
| typing_runtime_protocols   | 95.1 us                                                     | 107 us: 1.12x slower                                                           |
| pickle_pure_python         | 195 us                                                      | 221 us: 1.13x slower                                                           |
| telco                      | 4.13 ms                                                     | 4.76 ms: 1.15x slower                                                          |
| coverage                   | 40.8 ms                                                     | 49.1 ms: 1.20x slower                                                          |
| json_dumps                 | 5.70 ms                                                     | 6.91 ms: 1.21x slower                                                          |
| python_startup_no_site     | 16.2 ms                                                     | 20.4 ms: 1.26x slower                                                          |
| bench_mp_pool              | 69.2 ms                                                     | 88.4 ms: 1.28x slower                                                          |
| gc_traversal               | 1.52 ms                                                     | 2.03 ms: 1.33x slower                                                          |
| python_startup             | 19.5 ms                                                     | 26.5 ms: 1.36x slower                                                          |
| create_gc_cycles           | 752 us                                                      | 1.22 ms: 1.63x slower                                                          |
| Geometric mean             | (ref)                                                       | 1.06x faster                                                                   |

Benchmark hidden because not significant (5): nqueens, logging_simple, logging_format, generators, bench_thread_pool
Ignored benchmarks (19) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250404-3.14.0a6+-492df4e/bm-20250404-pythonperf1-amd64-faster%2dcpython-tos_caching_1-3.14.0a6+-492df4e.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.064x faster

# HPT report

- Reliability score: 96.62% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown
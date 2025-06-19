# Results vs. 3.12.0

- fork: faster-cpython
- ref: tier_2_tos_caching
- machine: windows-amd64
- commit hash: 2850d72
- commit date: 2025-06-19
- overall geometric mean: 1.112x faster
- HPT reliability: 99.99%
- HPT 99th percentile: 1.02x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250619-pythonperf1-amd64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-2850d72 |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 221 ms: 1.01x slower                                                               |
| Geometric mean | (ref)                                                       | 1.01x slower                                                                       |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250619-pythonperf1-amd64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-2850d72 |
|----------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 391 ms: 1.97x faster                                                               |
| async_tree_io              | 731 ms                                                      | 399 ms: 1.83x faster                                                               |
| async_tree_memoization_tg  | 367 ms                                                      | 211 ms: 1.74x faster                                                               |
| async_tree_none            | 291 ms                                                      | 169 ms: 1.73x faster                                                               |
| async_tree_none_tg         | 285 ms                                                      | 167 ms: 1.71x faster                                                               |
| async_tree_memoization     | 339 ms                                                      | 206 ms: 1.65x faster                                                               |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 328 ms: 1.49x faster                                                               |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 342 ms: 1.47x faster                                                               |
| Geometric mean             | (ref)                                                       | 1.69x faster                                                                       |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250619-pythonperf1-amd64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-2850d72 |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| nbody          | 71.9 ms                                                     | 44.8 ms: 1.60x faster                                                              |
| float          | 56.8 ms                                                     | 44.2 ms: 1.28x faster                                                              |
| pidigits       | 152 ms                                                      | 146 ms: 1.04x faster                                                               |
| Geometric mean | (ref)                                                       | 1.29x faster                                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250619-pythonperf1-amd64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-2850d72 |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| regex_compile  | 87.5 ms                                                     | 78.6 ms: 1.11x faster                                                              |
| regex_dna      | 126 ms                                                      | 118 ms: 1.07x faster                                                               |
| regex_effbot   | 1.62 ms                                                     | 1.59 ms: 1.02x faster                                                              |
| Geometric mean | (ref)                                                       | 1.05x faster                                                                       |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250619-pythonperf1-amd64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-2850d72 |
|----------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| tomli_loads          | 1.37 sec                                                    | 1.15 sec: 1.19x faster                                                             |
| unpickle_pure_python | 133 us                                                      | 113 us: 1.18x faster                                                               |
| xml_etree_generate   | 55.8 ms                                                     | 51.4 ms: 1.09x faster                                                              |
| xml_etree_parse      | 93.0 ms                                                     | 87.8 ms: 1.06x faster                                                              |
| xml_etree_process    | 37.7 ms                                                     | 35.9 ms: 1.05x faster                                                              |
| xml_etree_iterparse  | 65.2 ms                                                     | 63.1 ms: 1.03x faster                                                              |
| json_loads           | 13.9 us                                                     | 14.0 us: 1.00x slower                                                              |
| pickle_pure_python   | 195 us                                                      | 204 us: 1.05x slower                                                               |
| json_dumps           | 5.70 ms                                                     | 6.21 ms: 1.09x slower                                                              |
| Geometric mean       | (ref)                                                       | 1.05x faster                                                                       |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250619-pythonperf1-amd64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-2850d72 |
|------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 19.3 ms: 1.19x slower                                                              |
| python_startup         | 19.5 ms                                                     | 25.6 ms: 1.32x slower                                                              |
| Geometric mean         | (ref)                                                       | 1.25x slower                                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250619-pythonperf1-amd64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-2850d72 |
|-----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 5.61 ms: 1.26x faster                                                              |
| django_template | 22.9 ms                                                     | 23.5 ms: 1.02x slower                                                              |
| Geometric mean  | (ref)                                                       | 1.11x faster                                                                       |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250619-pythonperf1-amd64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-2850d72 |
|----------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| pathlib                    | 80.5 ms                                                     | 31.8 ms: 2.53x faster                                                              |
| async_tree_io_tg           | 771 ms                                                      | 391 ms: 1.97x faster                                                               |
| async_tree_io              | 731 ms                                                      | 399 ms: 1.83x faster                                                               |
| async_tree_memoization_tg  | 367 ms                                                      | 211 ms: 1.74x faster                                                               |
| async_tree_none            | 291 ms                                                      | 169 ms: 1.73x faster                                                               |
| async_tree_none_tg         | 285 ms                                                      | 167 ms: 1.71x faster                                                               |
| mdp                        | 1.37 sec                                                    | 810 ms: 1.69x faster                                                               |
| async_tree_memoization     | 339 ms                                                      | 206 ms: 1.65x faster                                                               |
| nbody                      | 71.9 ms                                                     | 44.8 ms: 1.60x faster                                                              |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 328 ms: 1.49x faster                                                               |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 342 ms: 1.47x faster                                                               |
| deepcopy                   | 238 us                                                      | 170 us: 1.40x faster                                                               |
| deepcopy_memo              | 23.7 us                                                     | 18.3 us: 1.30x faster                                                              |
| float                      | 56.8 ms                                                     | 44.2 ms: 1.28x faster                                                              |
| comprehensions             | 14.1 us                                                     | 11.0 us: 1.28x faster                                                              |
| mako                       | 7.09 ms                                                     | 5.61 ms: 1.26x faster                                                              |
| scimark_fft                | 184 ms                                                      | 154 ms: 1.20x faster                                                               |
| go                         | 91.6 ms                                                     | 77.0 ms: 1.19x faster                                                              |
| tomli_loads                | 1.37 sec                                                    | 1.15 sec: 1.19x faster                                                             |
| unpickle_pure_python       | 133 us                                                      | 113 us: 1.18x faster                                                               |
| generators                 | 22.5 ms                                                     | 19.5 ms: 1.16x faster                                                              |
| deepcopy_reduce            | 2.09 us                                                     | 1.81 us: 1.16x faster                                                              |
| sqlite_synth               | 1.76 us                                                     | 1.55 us: 1.13x faster                                                              |
| pyflate                    | 295 ms                                                      | 261 ms: 1.13x faster                                                               |
| regex_compile              | 87.5 ms                                                     | 78.6 ms: 1.11x faster                                                              |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.31 ms: 1.11x faster                                                              |
| raytrace                   | 192 ms                                                      | 176 ms: 1.10x faster                                                               |
| xml_etree_generate         | 55.8 ms                                                     | 51.4 ms: 1.09x faster                                                              |
| dulwich_log                | 44.3 ms                                                     | 41.0 ms: 1.08x faster                                                              |
| regex_dna                  | 126 ms                                                      | 118 ms: 1.07x faster                                                               |
| chaos                      | 43.3 ms                                                     | 40.8 ms: 1.06x faster                                                              |
| xml_etree_parse            | 93.0 ms                                                     | 87.8 ms: 1.06x faster                                                              |
| xml_etree_process          | 37.7 ms                                                     | 35.9 ms: 1.05x faster                                                              |
| nqueens                    | 62.8 ms                                                     | 60.0 ms: 1.05x faster                                                              |
| richards                   | 28.4 ms                                                     | 27.2 ms: 1.04x faster                                                              |
| crypto_pyaes               | 48.5 ms                                                     | 46.5 ms: 1.04x faster                                                              |
| sympy_sum                  | 91.5 ms                                                     | 87.8 ms: 1.04x faster                                                              |
| richards_super             | 32.1 ms                                                     | 30.8 ms: 1.04x faster                                                              |
| pidigits                   | 152 ms                                                      | 146 ms: 1.04x faster                                                               |
| xml_etree_iterparse        | 65.2 ms                                                     | 63.1 ms: 1.03x faster                                                              |
| json                       | 3.05 ms                                                     | 2.96 ms: 1.03x faster                                                              |
| scimark_monte_carlo        | 43.7 ms                                                     | 42.5 ms: 1.03x faster                                                              |
| scimark_sor                | 78.8 ms                                                     | 76.7 ms: 1.03x faster                                                              |
| spectral_norm              | 66.9 ms                                                     | 65.2 ms: 1.03x faster                                                              |
| sympy_str                  | 175 ms                                                      | 171 ms: 1.02x faster                                                               |
| regex_effbot               | 1.62 ms                                                     | 1.59 ms: 1.02x faster                                                              |
| fannkuch                   | 247 ms                                                      | 244 ms: 1.01x faster                                                               |
| sympy_integrate            | 13.0 ms                                                     | 12.8 ms: 1.01x faster                                                              |
| json_loads                 | 13.9 us                                                     | 14.0 us: 1.00x slower                                                              |
| logging_simple             | 6.28 us                                                     | 6.32 us: 1.01x slower                                                              |
| 2to3                       | 218 ms                                                      | 221 ms: 1.01x slower                                                               |
| logging_format             | 6.72 us                                                     | 6.81 us: 1.01x slower                                                              |
| scimark_lu                 | 58.9 ms                                                     | 59.7 ms: 1.01x slower                                                              |
| meteor_contest             | 74.6 ms                                                     | 75.8 ms: 1.02x slower                                                              |
| pprint_pformat             | 1.05 sec                                                    | 1.06 sec: 1.02x slower                                                             |
| hexiom                     | 4.10 ms                                                     | 4.17 ms: 1.02x slower                                                              |
| coroutines                 | 14.3 ms                                                     | 14.5 ms: 1.02x slower                                                              |
| telco                      | 4.13 ms                                                     | 4.22 ms: 1.02x slower                                                              |
| django_template            | 22.9 ms                                                     | 23.5 ms: 1.02x slower                                                              |
| async_generators           | 239 ms                                                      | 246 ms: 1.03x slower                                                               |
| sympy_expand               | 284 ms                                                      | 294 ms: 1.04x slower                                                               |
| pickle_pure_python         | 195 us                                                      | 204 us: 1.05x slower                                                               |
| json_dumps                 | 5.70 ms                                                     | 6.21 ms: 1.09x slower                                                              |
| typing_runtime_protocols   | 95.1 us                                                     | 105 us: 1.11x slower                                                               |
| python_startup_no_site     | 16.2 ms                                                     | 19.3 ms: 1.19x slower                                                              |
| coverage                   | 40.8 ms                                                     | 50.6 ms: 1.24x slower                                                              |
| python_startup             | 19.5 ms                                                     | 25.6 ms: 1.32x slower                                                              |
| gc_traversal               | 1.52 ms                                                     | 2.14 ms: 1.40x slower                                                              |
| create_gc_cycles           | 752 us                                                      | 1.34 ms: 1.78x slower                                                              |
| logging_silent             | 60.5 ns                                                     | 311 ns: 5.13x slower                                                               |
| Geometric mean             | (ref)                                                       | 1.09x faster                                                                       |

Benchmark hidden because not significant (5): regex_v8, deltablue, docutils, pprint_safe_repr, pycparser
Ignored benchmarks (21) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (17) of results/bm-20250619-3.15.0a0-2850d72-JIT/bm-20250619-pythonperf1-amd64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-2850d72.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.112x faster

# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: unknown
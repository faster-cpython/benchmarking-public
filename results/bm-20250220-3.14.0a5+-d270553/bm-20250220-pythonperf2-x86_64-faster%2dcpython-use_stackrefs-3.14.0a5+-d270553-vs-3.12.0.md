# Results vs. 3.12.0

- fork: faster-cpython
- ref: use_stackrefs
- machine: linux-x86_64
- commit hash: d270553
- commit date: 2025-02-20
- overall geometric mean: 1.036x faster
- HPT reliability: 99.05%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250220-pythonperf2-x86_64-faster%2dcpython-use_stackrefs-3.14.0a5+-d270553 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 287 ms: 1.01x slower                                                            |
| docutils       | 2.87 sec                                                     | 2.88 sec: 1.01x slower                                                          |
| Geometric mean | (ref)                                                        | 1.01x slower                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250220-pythonperf2-x86_64-faster%2dcpython-use_stackrefs-3.14.0a5+-d270553 |
|----------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.05 sec                                                     | 655 ms: 1.61x faster                                                            |
| async_tree_io              | 1.04 sec                                                     | 651 ms: 1.60x faster                                                            |
| async_tree_memoization_tg  | 540 ms                                                       | 338 ms: 1.60x faster                                                            |
| async_tree_none            | 452 ms                                                       | 292 ms: 1.55x faster                                                            |
| async_tree_none_tg         | 431 ms                                                       | 279 ms: 1.54x faster                                                            |
| async_tree_memoization     | 544 ms                                                       | 354 ms: 1.54x faster                                                            |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 508 ms: 1.37x faster                                                            |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 522 ms: 1.33x faster                                                            |
| Geometric mean             | (ref)                                                        | 1.51x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250220-pythonperf2-x86_64-faster%2dcpython-use_stackrefs-3.14.0a5+-d270553 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 76.6 ms                                                      | 69.9 ms: 1.10x faster                                                           |
| pidigits       | 265 ms                                                       | 254 ms: 1.04x faster                                                            |
| nbody          | 88.0 ms                                                      | 101 ms: 1.15x slower                                                            |
| Geometric mean | (ref)                                                        | 1.00x slower                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250220-pythonperf2-x86_64-faster%2dcpython-use_stackrefs-3.14.0a5+-d270553 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 144 ms                                                       | 132 ms: 1.09x faster                                                            |
| regex_effbot   | 3.57 ms                                                      | 3.29 ms: 1.08x faster                                                           |
| regex_dna      | 239 ms                                                       | 250 ms: 1.05x slower                                                            |
| regex_v8       | 23.6 ms                                                      | 26.1 ms: 1.11x slower                                                           |
| Geometric mean | (ref)                                                        | 1.00x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250220-pythonperf2-x86_64-faster%2dcpython-use_stackrefs-3.14.0a5+-d270553 |
|----------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| xml_etree_iterparse  | 103 ms                                                       | 97.9 ms: 1.05x faster                                                           |
| xml_etree_parse      | 144 ms                                                       | 139 ms: 1.04x faster                                                            |
| xml_etree_generate   | 86.1 ms                                                      | 84.4 ms: 1.02x faster                                                           |
| tomli_loads          | 2.16 sec                                                     | 2.14 sec: 1.01x faster                                                          |
| unpickle_pure_python | 210 us                                                       | 211 us: 1.01x slower                                                            |
| xml_etree_process    | 58.4 ms                                                      | 59.2 ms: 1.01x slower                                                           |
| pickle_pure_python   | 318 us                                                       | 333 us: 1.05x slower                                                            |
| json_loads           | 24.4 us                                                      | 26.1 us: 1.07x slower                                                           |
| json_dumps           | 10.2 ms                                                      | 11.7 ms: 1.14x slower                                                           |
| Geometric mean       | (ref)                                                        | 1.02x slower                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250220-pythonperf2-x86_64-faster%2dcpython-use_stackrefs-3.14.0a5+-d270553 |
|------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 9.04 ms: 1.05x slower                                                           |
| python_startup         | 11.6 ms                                                      | 16.2 ms: 1.39x slower                                                           |
| Geometric mean         | (ref)                                                        | 1.21x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250220-pythonperf2-x86_64-faster%2dcpython-use_stackrefs-3.14.0a5+-d270553 |
|-----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| django_template | 38.2 ms                                                      | 36.7 ms: 1.04x faster                                                           |
| mako            | 10.0 ms                                                      | 10.9 ms: 1.09x slower                                                           |
| Geometric mean  | (ref)                                                        | 1.02x slower                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250220-pythonperf2-x86_64-faster%2dcpython-use_stackrefs-3.14.0a5+-d270553 |
|----------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.05 sec                                                     | 655 ms: 1.61x faster                                                            |
| async_tree_io              | 1.04 sec                                                     | 651 ms: 1.60x faster                                                            |
| async_tree_memoization_tg  | 540 ms                                                       | 338 ms: 1.60x faster                                                            |
| async_tree_none            | 452 ms                                                       | 292 ms: 1.55x faster                                                            |
| async_tree_none_tg         | 431 ms                                                       | 279 ms: 1.54x faster                                                            |
| async_tree_memoization     | 544 ms                                                       | 354 ms: 1.54x faster                                                            |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 508 ms: 1.37x faster                                                            |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 522 ms: 1.33x faster                                                            |
| deepcopy                   | 368 us                                                       | 280 us: 1.31x faster                                                            |
| generators                 | 37.4 ms                                                      | 28.6 ms: 1.31x faster                                                           |
| deepcopy_memo              | 36.8 us                                                      | 28.6 us: 1.29x faster                                                           |
| comprehensions             | 21.9 us                                                      | 17.5 us: 1.25x faster                                                           |
| go                         | 150 ms                                                       | 130 ms: 1.16x faster                                                            |
| deepcopy_reduce            | 3.37 us                                                      | 2.93 us: 1.15x faster                                                           |
| sqlalchemy_declarative     | 159 ms                                                       | 144 ms: 1.11x faster                                                            |
| pathlib                    | 18.9 ms                                                      | 17.0 ms: 1.11x faster                                                           |
| coroutines                 | 23.0 ms                                                      | 20.7 ms: 1.11x faster                                                           |
| float                      | 76.6 ms                                                      | 69.9 ms: 1.10x faster                                                           |
| regex_compile              | 144 ms                                                       | 132 ms: 1.09x faster                                                            |
| regex_effbot               | 3.57 ms                                                      | 3.29 ms: 1.08x faster                                                           |
| scimark_monte_carlo        | 69.0 ms                                                      | 63.6 ms: 1.08x faster                                                           |
| spectral_norm              | 91.6 ms                                                      | 84.8 ms: 1.08x faster                                                           |
| sympy_sum                  | 162 ms                                                       | 151 ms: 1.08x faster                                                            |
| logging_format             | 7.48 us                                                      | 7.02 us: 1.07x faster                                                           |
| sqlalchemy_imperative      | 18.7 ms                                                      | 17.7 ms: 1.06x faster                                                           |
| raytrace                   | 298 ms                                                       | 282 ms: 1.06x faster                                                            |
| logging_simple             | 6.71 us                                                      | 6.38 us: 1.05x faster                                                           |
| xml_etree_iterparse        | 103 ms                                                       | 97.9 ms: 1.05x faster                                                           |
| sympy_str                  | 302 ms                                                       | 289 ms: 1.04x faster                                                            |
| pidigits                   | 265 ms                                                       | 254 ms: 1.04x faster                                                            |
| sympy_integrate            | 23.9 ms                                                      | 23.0 ms: 1.04x faster                                                           |
| mdp                        | 2.57 sec                                                     | 2.47 sec: 1.04x faster                                                          |
| django_template            | 38.2 ms                                                      | 36.7 ms: 1.04x faster                                                           |
| xml_etree_parse            | 144 ms                                                       | 139 ms: 1.04x faster                                                            |
| sqlglot_normalize          | 116 ms                                                       | 112 ms: 1.03x faster                                                            |
| sqlglot_transpile          | 1.78 ms                                                      | 1.73 ms: 1.03x faster                                                           |
| sqlglot_optimize           | 57.5 ms                                                      | 56.1 ms: 1.03x faster                                                           |
| pprint_pformat             | 1.65 sec                                                     | 1.61 sec: 1.02x faster                                                          |
| chaos                      | 64.0 ms                                                      | 62.4 ms: 1.02x faster                                                           |
| scimark_lu                 | 98.8 ms                                                      | 96.4 ms: 1.02x faster                                                           |
| sqlglot_parse              | 1.38 ms                                                      | 1.34 ms: 1.02x faster                                                           |
| pprint_safe_repr           | 807 ms                                                       | 790 ms: 1.02x faster                                                            |
| xml_etree_generate         | 86.1 ms                                                      | 84.4 ms: 1.02x faster                                                           |
| crypto_pyaes               | 80.3 ms                                                      | 79.3 ms: 1.01x faster                                                           |
| scimark_sor                | 109 ms                                                       | 108 ms: 1.01x faster                                                            |
| meteor_contest             | 128 ms                                                       | 127 ms: 1.01x faster                                                            |
| tomli_loads                | 2.16 sec                                                     | 2.14 sec: 1.01x faster                                                          |
| docutils                   | 2.87 sec                                                     | 2.88 sec: 1.01x slower                                                          |
| unpickle_pure_python       | 210 us                                                       | 211 us: 1.01x slower                                                            |
| 2to3                       | 285 ms                                                       | 287 ms: 1.01x slower                                                            |
| hexiom                     | 5.96 ms                                                      | 6.00 ms: 1.01x slower                                                           |
| richards_super             | 51.3 ms                                                      | 51.9 ms: 1.01x slower                                                           |
| nqueens                    | 89.9 ms                                                      | 90.9 ms: 1.01x slower                                                           |
| xml_etree_process          | 58.4 ms                                                      | 59.2 ms: 1.01x slower                                                           |
| sympy_expand               | 484 ms                                                       | 491 ms: 1.01x slower                                                            |
| pycparser                  | 1.23 sec                                                     | 1.25 sec: 1.02x slower                                                          |
| sqlite_synth               | 2.77 us                                                      | 2.82 us: 1.02x slower                                                           |
| dulwich_log                | 65.4 ms                                                      | 66.8 ms: 1.02x slower                                                           |
| pyflate                    | 439 ms                                                       | 451 ms: 1.03x slower                                                            |
| scimark_fft                | 301 ms                                                       | 311 ms: 1.03x slower                                                            |
| deltablue                  | 3.24 ms                                                      | 3.34 ms: 1.03x slower                                                           |
| pickle_pure_python         | 318 us                                                       | 333 us: 1.05x slower                                                            |
| python_startup_no_site     | 8.64 ms                                                      | 9.04 ms: 1.05x slower                                                           |
| regex_dna                  | 239 ms                                                       | 250 ms: 1.05x slower                                                            |
| fannkuch                   | 350 ms                                                       | 370 ms: 1.06x slower                                                            |
| json                       | 5.12 ms                                                      | 5.44 ms: 1.06x slower                                                           |
| json_loads                 | 24.4 us                                                      | 26.1 us: 1.07x slower                                                           |
| async_generators           | 390 ms                                                       | 419 ms: 1.07x slower                                                            |
| mako                       | 10.0 ms                                                      | 10.9 ms: 1.09x slower                                                           |
| regex_v8                   | 23.6 ms                                                      | 26.1 ms: 1.11x slower                                                           |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.77 ms: 1.13x slower                                                           |
| json_dumps                 | 10.2 ms                                                      | 11.7 ms: 1.14x slower                                                           |
| nbody                      | 88.0 ms                                                      | 101 ms: 1.15x slower                                                            |
| typing_runtime_protocols   | 152 us                                                       | 175 us: 1.15x slower                                                            |
| telco                      | 6.96 ms                                                      | 8.17 ms: 1.17x slower                                                           |
| coverage                   | 66.7 ms                                                      | 79.6 ms: 1.19x slower                                                           |
| python_startup             | 11.6 ms                                                      | 16.2 ms: 1.39x slower                                                           |
| create_gc_cycles           | 1.59 ms                                                      | 2.79 ms: 1.75x slower                                                           |
| gc_traversal               | 3.48 ms                                                      | 6.56 ms: 1.89x slower                                                           |
| bench_mp_pool              | 4.76 ms                                                      | 1.11 sec: 233.12x slower                                                        |
| Geometric mean             | (ref)                                                        | 1.03x slower                                                                    |

Benchmark hidden because not significant (4): logging_silent, richards, bench_thread_pool, asyncio_websockets
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20250220-3.14.0a5+-d270553/bm-20250220-pythonperf2-x86_64-faster%2dcpython-use_stackrefs-3.14.0a5+-d270553.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.036x faster

# HPT report

- Reliability score: 99.05% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.04x
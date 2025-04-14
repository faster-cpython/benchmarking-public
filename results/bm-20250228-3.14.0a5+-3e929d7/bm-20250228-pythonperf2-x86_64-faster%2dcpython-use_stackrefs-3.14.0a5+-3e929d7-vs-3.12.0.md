# Results vs. 3.12.0

- fork: faster-cpython
- ref: use_stackrefs
- machine: linux-x86_64
- commit hash: 3e929d7
- commit date: 2025-02-28
- overall geometric mean: 1.022x faster
- HPT reliability: 80.34%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250228-pythonperf2-x86_64-faster%2dcpython-use_stackrefs-3.14.0a5+-3e929d7 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 290 ms: 1.02x slower                                                            |
| docutils       | 2.87 sec                                                     | 2.91 sec: 1.01x slower                                                          |
| Geometric mean | (ref)                                                        | 1.01x slower                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250228-pythonperf2-x86_64-faster%2dcpython-use_stackrefs-3.14.0a5+-3e929d7 |
|----------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.05 sec                                                     | 650 ms: 1.62x faster                                                            |
| async_tree_io              | 1.04 sec                                                     | 646 ms: 1.61x faster                                                            |
| async_tree_memoization_tg  | 540 ms                                                       | 338 ms: 1.60x faster                                                            |
| async_tree_none            | 452 ms                                                       | 291 ms: 1.55x faster                                                            |
| async_tree_memoization     | 544 ms                                                       | 351 ms: 1.55x faster                                                            |
| async_tree_none_tg         | 431 ms                                                       | 279 ms: 1.54x faster                                                            |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 510 ms: 1.37x faster                                                            |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 520 ms: 1.34x faster                                                            |
| Geometric mean             | (ref)                                                        | 1.52x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250228-pythonperf2-x86_64-faster%2dcpython-use_stackrefs-3.14.0a5+-3e929d7 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 76.6 ms                                                      | 70.9 ms: 1.08x faster                                                           |
| pidigits       | 265 ms                                                       | 255 ms: 1.04x faster                                                            |
| nbody          | 88.0 ms                                                      | 105 ms: 1.20x slower                                                            |
| Geometric mean | (ref)                                                        | 1.02x slower                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250228-pythonperf2-x86_64-faster%2dcpython-use_stackrefs-3.14.0a5+-3e929d7 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_effbot   | 3.57 ms                                                      | 3.14 ms: 1.14x faster                                                           |
| regex_compile  | 144 ms                                                       | 137 ms: 1.05x faster                                                            |
| regex_dna      | 239 ms                                                       | 245 ms: 1.03x slower                                                            |
| regex_v8       | 23.6 ms                                                      | 25.3 ms: 1.07x slower                                                           |
| Geometric mean | (ref)                                                        | 1.02x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250228-pythonperf2-x86_64-faster%2dcpython-use_stackrefs-3.14.0a5+-3e929d7 |
|----------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| xml_etree_iterparse  | 103 ms                                                       | 99.7 ms: 1.03x faster                                                           |
| xml_etree_generate   | 86.1 ms                                                      | 84.1 ms: 1.02x faster                                                           |
| xml_etree_parse      | 144 ms                                                       | 143 ms: 1.01x faster                                                            |
| xml_etree_process    | 58.4 ms                                                      | 59.2 ms: 1.01x slower                                                           |
| json_loads           | 24.4 us                                                      | 25.5 us: 1.05x slower                                                           |
| pickle_pure_python   | 318 us                                                       | 334 us: 1.05x slower                                                            |
| unpickle_pure_python | 210 us                                                       | 221 us: 1.06x slower                                                            |
| json_dumps           | 10.2 ms                                                      | 11.4 ms: 1.11x slower                                                           |
| Geometric mean       | (ref)                                                        | 1.02x slower                                                                    |

Benchmark hidden because not significant (1): tomli_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250228-pythonperf2-x86_64-faster%2dcpython-use_stackrefs-3.14.0a5+-3e929d7 |
|------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 9.14 ms: 1.06x slower                                                           |
| python_startup         | 11.6 ms                                                      | 16.3 ms: 1.40x slower                                                           |
| Geometric mean         | (ref)                                                        | 1.22x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250228-pythonperf2-x86_64-faster%2dcpython-use_stackrefs-3.14.0a5+-3e929d7 |
|-----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| django_template | 38.2 ms                                                      | 36.0 ms: 1.06x faster                                                           |
| mako            | 10.0 ms                                                      | 11.3 ms: 1.12x slower                                                           |
| Geometric mean  | (ref)                                                        | 1.03x slower                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250228-pythonperf2-x86_64-faster%2dcpython-use_stackrefs-3.14.0a5+-3e929d7 |
|----------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.05 sec                                                     | 650 ms: 1.62x faster                                                            |
| async_tree_io              | 1.04 sec                                                     | 646 ms: 1.61x faster                                                            |
| async_tree_memoization_tg  | 540 ms                                                       | 338 ms: 1.60x faster                                                            |
| async_tree_none            | 452 ms                                                       | 291 ms: 1.55x faster                                                            |
| async_tree_memoization     | 544 ms                                                       | 351 ms: 1.55x faster                                                            |
| async_tree_none_tg         | 431 ms                                                       | 279 ms: 1.54x faster                                                            |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 510 ms: 1.37x faster                                                            |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 520 ms: 1.34x faster                                                            |
| generators                 | 37.4 ms                                                      | 29.2 ms: 1.28x faster                                                           |
| deepcopy                   | 368 us                                                       | 289 us: 1.27x faster                                                            |
| deepcopy_memo              | 36.8 us                                                      | 29.1 us: 1.26x faster                                                           |
| comprehensions             | 21.9 us                                                      | 17.8 us: 1.23x faster                                                           |
| regex_effbot               | 3.57 ms                                                      | 3.14 ms: 1.14x faster                                                           |
| go                         | 150 ms                                                       | 134 ms: 1.12x faster                                                            |
| deepcopy_reduce            | 3.37 us                                                      | 3.01 us: 1.12x faster                                                           |
| pathlib                    | 18.9 ms                                                      | 17.1 ms: 1.11x faster                                                           |
| coroutines                 | 23.0 ms                                                      | 21.0 ms: 1.10x faster                                                           |
| sqlalchemy_declarative     | 159 ms                                                       | 146 ms: 1.10x faster                                                            |
| float                      | 76.6 ms                                                      | 70.9 ms: 1.08x faster                                                           |
| django_template            | 38.2 ms                                                      | 36.0 ms: 1.06x faster                                                           |
| regex_compile              | 144 ms                                                       | 137 ms: 1.05x faster                                                            |
| sympy_sum                  | 162 ms                                                       | 154 ms: 1.05x faster                                                            |
| scimark_monte_carlo        | 69.0 ms                                                      | 65.8 ms: 1.05x faster                                                           |
| logging_format             | 7.48 us                                                      | 7.17 us: 1.04x faster                                                           |
| pidigits                   | 265 ms                                                       | 255 ms: 1.04x faster                                                            |
| sqlalchemy_imperative      | 18.7 ms                                                      | 18.2 ms: 1.03x faster                                                           |
| raytrace                   | 298 ms                                                       | 289 ms: 1.03x faster                                                            |
| xml_etree_iterparse        | 103 ms                                                       | 99.7 ms: 1.03x faster                                                           |
| logging_simple             | 6.71 us                                                      | 6.53 us: 1.03x faster                                                           |
| sympy_str                  | 302 ms                                                       | 294 ms: 1.03x faster                                                            |
| pprint_pformat             | 1.65 sec                                                     | 1.61 sec: 1.02x faster                                                          |
| xml_etree_generate         | 86.1 ms                                                      | 84.1 ms: 1.02x faster                                                           |
| mdp                        | 2.57 sec                                                     | 2.51 sec: 1.02x faster                                                          |
| sympy_integrate            | 23.9 ms                                                      | 23.4 ms: 1.02x faster                                                           |
| spectral_norm              | 91.6 ms                                                      | 90.5 ms: 1.01x faster                                                           |
| pprint_safe_repr           | 807 ms                                                       | 797 ms: 1.01x faster                                                            |
| xml_etree_parse            | 144 ms                                                       | 143 ms: 1.01x faster                                                            |
| meteor_contest             | 128 ms                                                       | 128 ms: 1.00x faster                                                            |
| pyflate                    | 439 ms                                                       | 441 ms: 1.00x slower                                                            |
| scimark_sor                | 109 ms                                                       | 110 ms: 1.01x slower                                                            |
| sqlglot_optimize           | 57.5 ms                                                      | 58.0 ms: 1.01x slower                                                           |
| sqlite_synth               | 2.77 us                                                      | 2.80 us: 1.01x slower                                                           |
| sqlglot_normalize          | 116 ms                                                       | 117 ms: 1.01x slower                                                            |
| xml_etree_process          | 58.4 ms                                                      | 59.2 ms: 1.01x slower                                                           |
| docutils                   | 2.87 sec                                                     | 2.91 sec: 1.01x slower                                                          |
| 2to3                       | 285 ms                                                       | 290 ms: 1.02x slower                                                            |
| chaos                      | 64.0 ms                                                      | 65.2 ms: 1.02x slower                                                           |
| bench_thread_pool          | 950 us                                                       | 970 us: 1.02x slower                                                            |
| regex_dna                  | 239 ms                                                       | 245 ms: 1.03x slower                                                            |
| scimark_lu                 | 98.8 ms                                                      | 102 ms: 1.03x slower                                                            |
| sympy_expand               | 484 ms                                                       | 500 ms: 1.03x slower                                                            |
| pycparser                  | 1.23 sec                                                     | 1.28 sec: 1.04x slower                                                          |
| json                       | 5.12 ms                                                      | 5.35 ms: 1.04x slower                                                           |
| json_loads                 | 24.4 us                                                      | 25.5 us: 1.05x slower                                                           |
| richards                   | 45.7 ms                                                      | 47.9 ms: 1.05x slower                                                           |
| crypto_pyaes               | 80.3 ms                                                      | 84.2 ms: 1.05x slower                                                           |
| nqueens                    | 89.9 ms                                                      | 94.3 ms: 1.05x slower                                                           |
| dulwich_log                | 65.4 ms                                                      | 68.6 ms: 1.05x slower                                                           |
| pickle_pure_python         | 318 us                                                       | 334 us: 1.05x slower                                                            |
| hexiom                     | 5.96 ms                                                      | 6.27 ms: 1.05x slower                                                           |
| deltablue                  | 3.24 ms                                                      | 3.41 ms: 1.05x slower                                                           |
| unpickle_pure_python       | 210 us                                                       | 221 us: 1.06x slower                                                            |
| python_startup_no_site     | 8.64 ms                                                      | 9.14 ms: 1.06x slower                                                           |
| richards_super             | 51.3 ms                                                      | 54.8 ms: 1.07x slower                                                           |
| regex_v8                   | 23.6 ms                                                      | 25.3 ms: 1.07x slower                                                           |
| async_generators           | 390 ms                                                       | 419 ms: 1.07x slower                                                            |
| fannkuch                   | 350 ms                                                       | 377 ms: 1.08x slower                                                            |
| json_dumps                 | 10.2 ms                                                      | 11.4 ms: 1.11x slower                                                           |
| mako                       | 10.0 ms                                                      | 11.3 ms: 1.12x slower                                                           |
| scimark_fft                | 301 ms                                                       | 339 ms: 1.13x slower                                                            |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.80 ms: 1.14x slower                                                           |
| typing_runtime_protocols   | 152 us                                                       | 173 us: 1.14x slower                                                            |
| telco                      | 6.96 ms                                                      | 8.21 ms: 1.18x slower                                                           |
| nbody                      | 88.0 ms                                                      | 105 ms: 1.20x slower                                                            |
| coverage                   | 66.7 ms                                                      | 83.9 ms: 1.26x slower                                                           |
| python_startup             | 11.6 ms                                                      | 16.3 ms: 1.40x slower                                                           |
| create_gc_cycles           | 1.59 ms                                                      | 2.79 ms: 1.75x slower                                                           |
| gc_traversal               | 3.48 ms                                                      | 6.54 ms: 1.88x slower                                                           |
| bench_mp_pool              | 4.76 ms                                                      | 907 ms: 190.41x slower                                                          |
| Geometric mean             | (ref)                                                        | 1.04x slower                                                                    |

Benchmark hidden because not significant (5): asyncio_websockets, logging_silent, sqlglot_transpile, sqlglot_parse, tomli_loads
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20250228-3.14.0a5+-3e929d7/bm-20250228-pythonperf2-x86_64-faster%2dcpython-use_stackrefs-3.14.0a5+-3e929d7.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.022x faster

# HPT report

- Reliability score: 80.34% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.04x
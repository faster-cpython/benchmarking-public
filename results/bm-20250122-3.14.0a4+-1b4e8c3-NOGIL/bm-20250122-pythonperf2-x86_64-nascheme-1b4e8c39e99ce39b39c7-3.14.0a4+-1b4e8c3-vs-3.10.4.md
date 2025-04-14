# Results vs. 3.10.4

- fork: nascheme
- ref: 1b4e8c39e99ce39b39c7
- machine: linux-x86_64
- commit hash: 1b4e8c3
- commit date: 2025-01-22
- overall geometric mean: 1.181x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.08x faster
- Memory change: 1.53x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250122-pythonperf2-x86_64-nascheme-1b4e8c39e99ce39b39c7-3.14.0a4+-1b4e8c3 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 342 ms: 1.02x faster                                                           |
| docutils       | 3.41 sec                                                     | 2.97 sec: 1.15x faster                                                         |
| html5lib       | 94.6 ms                                                      | 73.4 ms: 1.29x faster                                                          |
| Geometric mean | (ref)                                                        | 1.15x faster                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250122-pythonperf2-x86_64-nascheme-1b4e8c39e99ce39b39c7-3.14.0a4+-1b4e8c3 |
|-------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_io           | 1.60 sec                                                     | 617 ms: 2.59x faster                                                           |
| async_tree_none         | 692 ms                                                       | 295 ms: 2.34x faster                                                           |
| async_tree_memoization  | 819 ms                                                       | 365 ms: 2.25x faster                                                           |
| async_tree_cpu_io_mixed | 936 ms                                                       | 533 ms: 1.76x faster                                                           |
| Geometric mean          | (ref)                                                        | 2.21x faster                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250122-pythonperf2-x86_64-nascheme-1b4e8c39e99ce39b39c7-3.14.0a4+-1b4e8c3 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| float          | 111 ms                                                       | 75.2 ms: 1.48x faster                                                          |
| pidigits       | 271 ms                                                       | 248 ms: 1.09x faster                                                           |
| Geometric mean | (ref)                                                        | 1.17x faster                                                                   |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250122-pythonperf2-x86_64-nascheme-1b4e8c39e99ce39b39c7-3.14.0a4+-1b4e8c3 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 157 ms: 1.21x faster                                                           |
| regex_dna      | 261 ms                                                       | 245 ms: 1.07x faster                                                           |
| regex_v8       | 27.2 ms                                                      | 25.8 ms: 1.05x faster                                                          |
| regex_effbot   | 3.09 ms                                                      | 3.12 ms: 1.01x slower                                                          |
| Geometric mean | (ref)                                                        | 1.08x faster                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250122-pythonperf2-x86_64-nascheme-1b4e8c39e99ce39b39c7-3.14.0a4+-1b4e8c3 |
|----------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| unpickle_pure_python | 312 us                                                       | 237 us: 1.32x faster                                                           |
| tomli_loads          | 2.92 sec                                                     | 2.44 sec: 1.20x faster                                                         |
| pickle_pure_python   | 455 us                                                       | 388 us: 1.17x faster                                                           |
| json_loads           | 30.3 us                                                      | 28.2 us: 1.07x faster                                                          |
| json_dumps           | 14.5 ms                                                      | 13.6 ms: 1.07x faster                                                          |
| Geometric mean       | (ref)                                                        | 1.16x faster                                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250122-pythonperf2-x86_64-nascheme-1b4e8c39e99ce39b39c7-3.14.0a4+-1b4e8c3 |
|------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup_no_site | 7.33 ms                                                      | 12.0 ms: 1.63x slower                                                          |
| python_startup         | 11.5 ms                                                      | 18.9 ms: 1.64x slower                                                          |
| Geometric mean         | (ref)                                                        | 1.64x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250122-pythonperf2-x86_64-nascheme-1b4e8c39e99ce39b39c7-3.14.0a4+-1b4e8c3 |
|-----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| django_template | 50.2 ms                                                      | 46.7 ms: 1.08x faster                                                          |
| genshi_text     | 31.4 ms                                                      | 29.6 ms: 1.06x faster                                                          |
| genshi_xml      | 63.3 ms                                                      | 63.9 ms: 1.01x slower                                                          |
| mako            | 14.7 ms                                                      | 18.0 ms: 1.22x slower                                                          |
| Geometric mean  | (ref)                                                        | 1.02x slower                                                                   |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250122-pythonperf2-x86_64-nascheme-1b4e8c39e99ce39b39c7-3.14.0a4+-1b4e8c3 |
|--------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_io            | 1.60 sec                                                     | 617 ms: 2.59x faster                                                           |
| typing_runtime_protocols | 537 us                                                       | 223 us: 2.41x faster                                                           |
| async_tree_none          | 692 ms                                                       | 295 ms: 2.34x faster                                                           |
| async_tree_memoization   | 819 ms                                                       | 365 ms: 2.25x faster                                                           |
| generators               | 57.3 ms                                                      | 31.5 ms: 1.82x faster                                                          |
| go                       | 262 ms                                                       | 149 ms: 1.76x faster                                                           |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 533 ms: 1.76x faster                                                           |
| deltablue                | 7.50 ms                                                      | 4.57 ms: 1.64x faster                                                          |
| logging_silent           | 167 ns                                                       | 104 ns: 1.61x faster                                                           |
| pylint                   | 566 ms                                                       | 355 ms: 1.60x faster                                                           |
| chaos                    | 109 ms                                                       | 71.5 ms: 1.52x faster                                                          |
| float                    | 111 ms                                                       | 75.2 ms: 1.48x faster                                                          |
| pyflate                  | 733 ms                                                       | 499 ms: 1.47x faster                                                           |
| scimark_sor              | 180 ms                                                       | 123 ms: 1.47x faster                                                           |
| raytrace                 | 489 ms                                                       | 348 ms: 1.41x faster                                                           |
| deepcopy                 | 468 us                                                       | 337 us: 1.39x faster                                                           |
| spectral_norm            | 139 ms                                                       | 101 ms: 1.38x faster                                                           |
| coroutines               | 30.3 ms                                                      | 22.0 ms: 1.37x faster                                                          |
| scimark_lu               | 167 ms                                                       | 123 ms: 1.36x faster                                                           |
| richards_super           | 90.6 ms                                                      | 66.9 ms: 1.35x faster                                                          |
| sqlglot_parse            | 2.24 ms                                                      | 1.65 ms: 1.35x faster                                                          |
| deepcopy_memo            | 49.8 us                                                      | 37.4 us: 1.33x faster                                                          |
| unpickle_pure_python     | 312 us                                                       | 237 us: 1.32x faster                                                           |
| pathlib                  | 21.4 ms                                                      | 16.4 ms: 1.30x faster                                                          |
| pycparser                | 1.67 sec                                                     | 1.29 sec: 1.30x faster                                                         |
| sqlglot_transpile        | 2.68 ms                                                      | 2.07 ms: 1.29x faster                                                          |
| crypto_pyaes             | 119 ms                                                       | 92.4 ms: 1.29x faster                                                          |
| hexiom                   | 9.42 ms                                                      | 7.31 ms: 1.29x faster                                                          |
| html5lib                 | 94.6 ms                                                      | 73.4 ms: 1.29x faster                                                          |
| richards                 | 75.1 ms                                                      | 58.8 ms: 1.28x faster                                                          |
| comprehensions           | 26.7 us                                                      | 21.7 us: 1.23x faster                                                          |
| scimark_monte_carlo      | 107 ms                                                       | 87.8 ms: 1.22x faster                                                          |
| logging_simple           | 8.88 us                                                      | 7.27 us: 1.22x faster                                                          |
| regex_compile            | 190 ms                                                       | 157 ms: 1.21x faster                                                           |
| logging_format           | 9.64 us                                                      | 8.05 us: 1.20x faster                                                          |
| tomli_loads              | 2.92 sec                                                     | 2.44 sec: 1.20x faster                                                         |
| pickle_pure_python       | 455 us                                                       | 388 us: 1.17x faster                                                           |
| dulwich_log              | 81.1 ms                                                      | 69.3 ms: 1.17x faster                                                          |
| pprint_safe_repr         | 1.05 sec                                                     | 910 ms: 1.15x faster                                                           |
| docutils                 | 3.41 sec                                                     | 2.97 sec: 1.15x faster                                                         |
| pprint_pformat           | 2.15 sec                                                     | 1.88 sec: 1.14x faster                                                         |
| thrift                   | 1.18 ms                                                      | 1.03 ms: 1.14x faster                                                          |
| sqlite_synth             | 2.99 us                                                      | 2.63 us: 1.14x faster                                                          |
| mdp                      | 3.01 sec                                                     | 2.74 sec: 1.10x faster                                                         |
| sympy_sum                | 193 ms                                                       | 176 ms: 1.10x faster                                                           |
| sqlglot_normalize        | 144 ms                                                       | 131 ms: 1.09x faster                                                           |
| deepcopy_reduce          | 4.01 us                                                      | 3.66 us: 1.09x faster                                                          |
| pidigits                 | 271 ms                                                       | 248 ms: 1.09x faster                                                           |
| sqlalchemy_imperative    | 22.7 ms                                                      | 20.9 ms: 1.09x faster                                                          |
| sqlalchemy_declarative   | 190 ms                                                       | 175 ms: 1.08x faster                                                           |
| django_template          | 50.2 ms                                                      | 46.7 ms: 1.08x faster                                                          |
| json_loads               | 30.3 us                                                      | 28.2 us: 1.07x faster                                                          |
| json_dumps               | 14.5 ms                                                      | 13.6 ms: 1.07x faster                                                          |
| regex_dna                | 261 ms                                                       | 245 ms: 1.07x faster                                                           |
| genshi_text              | 31.4 ms                                                      | 29.6 ms: 1.06x faster                                                          |
| sympy_str                | 360 ms                                                       | 340 ms: 1.06x faster                                                           |
| sympy_expand             | 600 ms                                                       | 568 ms: 1.06x faster                                                           |
| regex_v8                 | 27.2 ms                                                      | 25.8 ms: 1.05x faster                                                          |
| json                     | 5.86 ms                                                      | 5.62 ms: 1.04x faster                                                          |
| sqlglot_optimize         | 70.1 ms                                                      | 67.4 ms: 1.04x faster                                                          |
| sympy_integrate          | 28.2 ms                                                      | 27.1 ms: 1.04x faster                                                          |
| asyncio_websockets       | 390 ms                                                       | 378 ms: 1.03x faster                                                           |
| 2to3                     | 350 ms                                                       | 342 ms: 1.02x faster                                                           |
| scimark_fft              | 361 ms                                                       | 354 ms: 1.02x faster                                                           |
| fannkuch                 | 483 ms                                                       | 479 ms: 1.01x faster                                                           |
| nqueens                  | 115 ms                                                       | 116 ms: 1.01x slower                                                           |
| genshi_xml               | 63.3 ms                                                      | 63.9 ms: 1.01x slower                                                          |
| regex_effbot             | 3.09 ms                                                      | 3.12 ms: 1.01x slower                                                          |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 5.59 ms: 1.10x slower                                                          |
| async_generators         | 421 ms                                                       | 470 ms: 1.12x slower                                                           |
| meteor_contest           | 138 ms                                                       | 156 ms: 1.13x slower                                                           |
| mako                     | 14.7 ms                                                      | 18.0 ms: 1.22x slower                                                          |
| telco                    | 7.23 ms                                                      | 9.10 ms: 1.26x slower                                                          |
| bench_thread_pool        | 1.14 ms                                                      | 1.46 ms: 1.28x slower                                                          |
| gc_traversal             | 3.42 ms                                                      | 4.64 ms: 1.36x slower                                                          |
| create_gc_cycles         | 1.76 ms                                                      | 2.40 ms: 1.36x slower                                                          |
| coverage                 | 63.3 ms                                                      | 102 ms: 1.61x slower                                                           |
| python_startup_no_site   | 7.33 ms                                                      | 12.0 ms: 1.63x slower                                                          |
| python_startup           | 11.5 ms                                                      | 18.9 ms: 1.64x slower                                                          |
| bench_mp_pool            | 6.37 ms                                                      | 49.7 ms: 7.80x slower                                                          |
| Geometric mean           | (ref)                                                        | 1.15x faster                                                                   |

Benchmark hidden because not significant (1): nbody
Ignored benchmarks (19) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list, xml_etree_generate, xml_etree_iterparse, xml_etree_parse, xml_etree_process
Ignored benchmarks (11) of results/bm-20250122-3.14.0a4+-1b4e8c3-NOGIL/bm-20250122-pythonperf2-x86_64-nascheme-1b4e8c39e99ce39b39c7-3.14.0a4+-1b4e8c3.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.181x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.10x
- 95% likely to have a speedup of 1.09x
- 99% likely to have a speedup of 1.08x

# Memory
- memory change: 1.53x
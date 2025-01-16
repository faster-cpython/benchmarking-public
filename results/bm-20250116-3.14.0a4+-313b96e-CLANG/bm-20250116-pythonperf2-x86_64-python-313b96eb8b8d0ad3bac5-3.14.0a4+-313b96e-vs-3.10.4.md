# Results vs. 3.10.4

- fork: python
- ref: 313b96eb8b8d0ad3bac5
- machine: linux-x86_64
- commit hash: 313b96e
- commit date: 2025-01-16
- overall geometric mean: 1.308x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.20x faster
- Memory change: 1.33x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250116-pythonperf2-x86_64-python-313b96eb8b8d0ad3bac5-3.14.0a4+-313b96e |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 280 ms: 1.25x faster                                                         |
| docutils       | 3.41 sec                                                     | 2.85 sec: 1.20x faster                                                       |
| html5lib       | 94.6 ms                                                      | 67.1 ms: 1.41x faster                                                        |
| Geometric mean | (ref)                                                        | 1.28x faster                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250116-pythonperf2-x86_64-python-313b96eb8b8d0ad3bac5-3.14.0a4+-313b96e |
|-------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io           | 1.60 sec                                                     | 629 ms: 2.54x faster                                                         |
| async_tree_none         | 692 ms                                                       | 282 ms: 2.45x faster                                                         |
| async_tree_memoization  | 819 ms                                                       | 346 ms: 2.37x faster                                                         |
| async_tree_cpu_io_mixed | 936 ms                                                       | 545 ms: 1.72x faster                                                         |
| Geometric mean          | (ref)                                                        | 2.24x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250116-pythonperf2-x86_64-python-313b96eb8b8d0ad3bac5-3.14.0a4+-313b96e |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 111 ms                                                       | 75.1 ms: 1.48x faster                                                        |
| nbody          | 134 ms                                                       | 105 ms: 1.27x faster                                                         |
| pidigits       | 271 ms                                                       | 285 ms: 1.05x slower                                                         |
| Geometric mean | (ref)                                                        | 1.21x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250116-pythonperf2-x86_64-python-313b96eb8b8d0ad3bac5-3.14.0a4+-313b96e |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 144 ms: 1.32x faster                                                         |
| regex_dna      | 261 ms                                                       | 222 ms: 1.18x faster                                                         |
| regex_v8       | 27.2 ms                                                      | 26.4 ms: 1.03x faster                                                        |
| regex_effbot   | 3.09 ms                                                      | 3.03 ms: 1.02x faster                                                        |
| Geometric mean | (ref)                                                        | 1.13x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250116-pythonperf2-x86_64-python-313b96eb8b8d0ad3bac5-3.14.0a4+-313b96e |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| unpickle_pure_python | 312 us                                                       | 239 us: 1.31x faster                                                         |
| pickle_pure_python   | 455 us                                                       | 353 us: 1.29x faster                                                         |
| xml_etree_process    | 75.9 ms                                                      | 61.0 ms: 1.24x faster                                                        |
| json_dumps           | 14.5 ms                                                      | 11.9 ms: 1.23x faster                                                        |
| json_loads           | 30.3 us                                                      | 25.6 us: 1.18x faster                                                        |
| tomli_loads          | 2.92 sec                                                     | 2.48 sec: 1.17x faster                                                       |
| xml_etree_generate   | 92.3 ms                                                      | 85.3 ms: 1.08x faster                                                        |
| xml_etree_iterparse  | 110 ms                                                       | 106 ms: 1.04x faster                                                         |
| xml_etree_parse      | 160 ms                                                       | 163 ms: 1.02x slower                                                         |
| Geometric mean       | (ref)                                                        | 1.16x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250116-pythonperf2-x86_64-python-313b96eb8b8d0ad3bac5-3.14.0a4+-313b96e |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 7.33 ms                                                      | 9.05 ms: 1.24x slower                                                        |
| python_startup         | 11.5 ms                                                      | 16.0 ms: 1.39x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.31x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250116-pythonperf2-x86_64-python-313b96eb8b8d0ad3bac5-3.14.0a4+-313b96e |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| django_template | 50.2 ms                                                      | 35.2 ms: 1.43x faster                                                        |
| genshi_text     | 31.4 ms                                                      | 25.0 ms: 1.26x faster                                                        |
| mako            | 14.7 ms                                                      | 12.0 ms: 1.23x faster                                                        |
| genshi_xml      | 63.3 ms                                                      | 54.9 ms: 1.15x faster                                                        |
| Geometric mean  | (ref)                                                        | 1.26x faster                                                                 |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250116-pythonperf2-x86_64-python-313b96eb8b8d0ad3bac5-3.14.0a4+-313b96e |
|--------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 169 us: 3.17x faster                                                         |
| async_tree_io            | 1.60 sec                                                     | 629 ms: 2.54x faster                                                         |
| async_tree_none          | 692 ms                                                       | 282 ms: 2.45x faster                                                         |
| async_tree_memoization   | 819 ms                                                       | 346 ms: 2.37x faster                                                         |
| deltablue                | 7.50 ms                                                      | 3.28 ms: 2.28x faster                                                        |
| go                       | 262 ms                                                       | 137 ms: 1.90x faster                                                         |
| raytrace                 | 489 ms                                                       | 267 ms: 1.83x faster                                                         |
| pylint                   | 566 ms                                                       | 314 ms: 1.80x faster                                                         |
| generators               | 57.3 ms                                                      | 33.1 ms: 1.73x faster                                                        |
| richards_super           | 90.6 ms                                                      | 52.3 ms: 1.73x faster                                                        |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 545 ms: 1.72x faster                                                         |
| chaos                    | 109 ms                                                       | 63.9 ms: 1.70x faster                                                        |
| scimark_lu               | 167 ms                                                       | 99.1 ms: 1.68x faster                                                        |
| logging_silent           | 167 ns                                                       | 99.8 ns: 1.68x faster                                                        |
| deepcopy                 | 468 us                                                       | 286 us: 1.64x faster                                                         |
| richards                 | 75.1 ms                                                      | 46.8 ms: 1.60x faster                                                        |
| sqlglot_parse            | 2.24 ms                                                      | 1.41 ms: 1.59x faster                                                        |
| pyflate                  | 733 ms                                                       | 473 ms: 1.55x faster                                                         |
| scimark_monte_carlo      | 107 ms                                                       | 71.2 ms: 1.51x faster                                                        |
| sqlglot_transpile        | 2.68 ms                                                      | 1.78 ms: 1.50x faster                                                        |
| crypto_pyaes             | 119 ms                                                       | 79.6 ms: 1.50x faster                                                        |
| deepcopy_memo            | 49.8 us                                                      | 33.4 us: 1.49x faster                                                        |
| float                    | 111 ms                                                       | 75.1 ms: 1.48x faster                                                        |
| spectral_norm            | 139 ms                                                       | 94.4 ms: 1.47x faster                                                        |
| comprehensions           | 26.7 us                                                      | 18.1 us: 1.47x faster                                                        |
| logging_simple           | 8.88 us                                                      | 6.09 us: 1.46x faster                                                        |
| scimark_sor              | 180 ms                                                       | 126 ms: 1.43x faster                                                         |
| logging_format           | 9.64 us                                                      | 6.75 us: 1.43x faster                                                        |
| django_template          | 50.2 ms                                                      | 35.2 ms: 1.43x faster                                                        |
| html5lib                 | 94.6 ms                                                      | 67.1 ms: 1.41x faster                                                        |
| coroutines               | 30.3 ms                                                      | 21.5 ms: 1.41x faster                                                        |
| thrift                   | 1.18 ms                                                      | 853 us: 1.38x faster                                                         |
| hexiom                   | 9.42 ms                                                      | 6.84 ms: 1.38x faster                                                        |
| deepcopy_reduce          | 4.01 us                                                      | 2.93 us: 1.37x faster                                                        |
| pathlib                  | 21.4 ms                                                      | 15.7 ms: 1.36x faster                                                        |
| pycparser                | 1.67 sec                                                     | 1.27 sec: 1.32x faster                                                       |
| regex_compile            | 190 ms                                                       | 144 ms: 1.32x faster                                                         |
| sqlalchemy_declarative   | 190 ms                                                       | 145 ms: 1.31x faster                                                         |
| unpickle_pure_python     | 312 us                                                       | 239 us: 1.31x faster                                                         |
| pickle_pure_python       | 455 us                                                       | 353 us: 1.29x faster                                                         |
| sympy_sum                | 193 ms                                                       | 150 ms: 1.28x faster                                                         |
| sqlalchemy_imperative    | 22.7 ms                                                      | 17.9 ms: 1.27x faster                                                        |
| nbody                    | 134 ms                                                       | 105 ms: 1.27x faster                                                         |
| genshi_text              | 31.4 ms                                                      | 25.0 ms: 1.26x faster                                                        |
| 2to3                     | 350 ms                                                       | 280 ms: 1.25x faster                                                         |
| sympy_integrate          | 28.2 ms                                                      | 22.6 ms: 1.25x faster                                                        |
| sympy_str                | 360 ms                                                       | 289 ms: 1.25x faster                                                         |
| xml_etree_process        | 75.9 ms                                                      | 61.0 ms: 1.24x faster                                                        |
| bench_thread_pool        | 1.14 ms                                                      | 926 us: 1.23x faster                                                         |
| sympy_expand             | 600 ms                                                       | 487 ms: 1.23x faster                                                         |
| mako                     | 14.7 ms                                                      | 12.0 ms: 1.23x faster                                                        |
| json_dumps               | 14.5 ms                                                      | 11.9 ms: 1.23x faster                                                        |
| sqlglot_normalize        | 144 ms                                                       | 118 ms: 1.22x faster                                                         |
| pprint_pformat           | 2.15 sec                                                     | 1.77 sec: 1.22x faster                                                       |
| dulwich_log              | 81.1 ms                                                      | 66.6 ms: 1.22x faster                                                        |
| nqueens                  | 115 ms                                                       | 95.5 ms: 1.20x faster                                                        |
| pprint_safe_repr         | 1.05 sec                                                     | 874 ms: 1.20x faster                                                         |
| docutils                 | 3.41 sec                                                     | 2.85 sec: 1.20x faster                                                       |
| sqlglot_optimize         | 70.1 ms                                                      | 58.7 ms: 1.20x faster                                                        |
| json_loads               | 30.3 us                                                      | 25.6 us: 1.18x faster                                                        |
| regex_dna                | 261 ms                                                       | 222 ms: 1.18x faster                                                         |
| tomli_loads              | 2.92 sec                                                     | 2.48 sec: 1.17x faster                                                       |
| scimark_fft              | 361 ms                                                       | 311 ms: 1.16x faster                                                         |
| genshi_xml               | 63.3 ms                                                      | 54.9 ms: 1.15x faster                                                        |
| mdp                      | 3.01 sec                                                     | 2.63 sec: 1.14x faster                                                       |
| json                     | 5.86 ms                                                      | 5.22 ms: 1.12x faster                                                        |
| fannkuch                 | 483 ms                                                       | 431 ms: 1.12x faster                                                         |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 4.54 ms: 1.12x faster                                                        |
| xml_etree_generate       | 92.3 ms                                                      | 85.3 ms: 1.08x faster                                                        |
| sqlite_synth             | 2.99 us                                                      | 2.82 us: 1.06x faster                                                        |
| xml_etree_iterparse      | 110 ms                                                       | 106 ms: 1.04x faster                                                         |
| meteor_contest           | 138 ms                                                       | 134 ms: 1.03x faster                                                         |
| regex_v8                 | 27.2 ms                                                      | 26.4 ms: 1.03x faster                                                        |
| regex_effbot             | 3.09 ms                                                      | 3.03 ms: 1.02x faster                                                        |
| async_generators         | 421 ms                                                       | 414 ms: 1.02x faster                                                         |
| asyncio_websockets       | 390 ms                                                       | 384 ms: 1.02x faster                                                         |
| xml_etree_parse          | 160 ms                                                       | 163 ms: 1.02x slower                                                         |
| pidigits                 | 271 ms                                                       | 285 ms: 1.05x slower                                                         |
| telco                    | 7.23 ms                                                      | 7.84 ms: 1.08x slower                                                        |
| coverage                 | 63.3 ms                                                      | 72.7 ms: 1.15x slower                                                        |
| python_startup_no_site   | 7.33 ms                                                      | 9.05 ms: 1.24x slower                                                        |
| python_startup           | 11.5 ms                                                      | 16.0 ms: 1.39x slower                                                        |
| create_gc_cycles         | 1.76 ms                                                      | 2.87 ms: 1.63x slower                                                        |
| gc_traversal             | 3.42 ms                                                      | 5.64 ms: 1.65x slower                                                        |
| bench_mp_pool            | 6.37 ms                                                      | 1.47 sec: 230.88x slower                                                     |
| Geometric mean           | (ref)                                                        | 1.23x faster                                                                 |
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20250116-3.14.0a4+-313b96e-CLANG/bm-20250116-pythonperf2-x86_64-python-313b96eb8b8d0ad3bac5-3.14.0a4+-313b96e.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.308x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.22x
- 95% likely to have a speedup of 1.21x
- 99% likely to have a speedup of 1.20x

# Memory
- memory change: 1.33x
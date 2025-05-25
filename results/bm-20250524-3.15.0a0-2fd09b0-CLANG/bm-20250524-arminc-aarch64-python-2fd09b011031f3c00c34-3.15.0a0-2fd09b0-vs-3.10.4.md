# Results vs. 3.10.4

- fork: python
- ref: 2fd09b011031f3c00c34
- machine: linux-aarch64
- commit hash: 2fd09b0
- commit date: 2025-05-24
- overall geometric mean: 1.222x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.19x faster
- Memory change: 1.42x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250524-arminc-aarch64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 301 ms: 1.27x faster                                                    |
| docutils       | 3.53 sec                                                              | 3.00 sec: 1.18x faster                                                  |
| html5lib       | 86.5 ms                                                               | 62.1 ms: 1.39x faster                                                   |
| Geometric mean | (ref)                                                                 | 1.28x faster                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250524-arminc-aarch64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0 |
|-------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_io           | 2.28 sec                                                              | 867 ms: 2.64x faster                                                    |
| async_tree_memoization  | 1.13 sec                                                              | 457 ms: 2.48x faster                                                    |
| async_tree_none         | 950 ms                                                                | 386 ms: 2.46x faster                                                    |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 723 ms: 1.76x faster                                                    |
| Geometric mean          | (ref)                                                                 | 2.31x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250524-arminc-aarch64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 135 ms                                                                | 87.6 ms: 1.54x faster                                                   |
| nbody          | 166 ms                                                                | 129 ms: 1.29x faster                                                    |
| pidigits       | 235 ms                                                                | 293 ms: 1.25x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.17x faster                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250524-arminc-aarch64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 120 ms: 1.47x faster                                                    |
| regex_dna      | 257 ms                                                                | 240 ms: 1.07x faster                                                    |
| regex_effbot   | 4.25 ms                                                               | 4.58 ms: 1.08x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.10x faster                                                            |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250524-arminc-aarch64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0 |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| unpickle_pure_python | 366 us                                                                | 249 us: 1.47x faster                                                    |
| tomli_loads          | 3.36 sec                                                              | 2.37 sec: 1.42x faster                                                  |
| pickle_pure_python   | 529 us                                                                | 382 us: 1.39x faster                                                    |
| xml_etree_process    | 99.5 ms                                                               | 76.1 ms: 1.31x faster                                                   |
| json_dumps           | 16.7 ms                                                               | 13.2 ms: 1.26x faster                                                   |
| unpickle_list        | 6.99 us                                                               | 5.90 us: 1.18x faster                                                   |
| xml_etree_generate   | 123 ms                                                                | 107 ms: 1.15x faster                                                    |
| xml_etree_iterparse  | 156 ms                                                                | 149 ms: 1.05x faster                                                    |
| xml_etree_parse      | 212 ms                                                                | 209 ms: 1.01x faster                                                    |
| pickle_dict          | 35.1 us                                                               | 36.9 us: 1.05x slower                                                   |
| json_loads           | 30.9 us                                                               | 34.4 us: 1.11x slower                                                   |
| pickle               | 12.5 us                                                               | 15.4 us: 1.23x slower                                                   |
| Geometric mean       | (ref)                                                                 | 1.12x faster                                                            |

Benchmark hidden because not significant (2): unpickle, pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250524-arminc-aarch64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0 |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 6.89 ms                                                               | 8.82 ms: 1.28x slower                                                   |
| python_startup         | 11.2 ms                                                               | 15.2 ms: 1.36x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.32x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250524-arminc-aarch64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0 |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| django_template | 53.3 ms                                                               | 39.1 ms: 1.36x faster                                                   |
| mako            | 18.9 ms                                                               | 14.1 ms: 1.34x faster                                                   |
| genshi_text     | 35.2 ms                                                               | 26.9 ms: 1.31x faster                                                   |
| genshi_xml      | 69.8 ms                                                               | 60.5 ms: 1.16x faster                                                   |
| Geometric mean  | (ref)                                                                 | 1.29x faster                                                            |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250524-arminc-aarch64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0 |
|--------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 193 us: 3.42x faster                                                    |
| async_tree_io            | 2.28 sec                                                              | 867 ms: 2.64x faster                                                    |
| async_tree_memoization   | 1.13 sec                                                              | 457 ms: 2.48x faster                                                    |
| async_tree_none          | 950 ms                                                                | 386 ms: 2.46x faster                                                    |
| deltablue                | 8.94 ms                                                               | 3.90 ms: 2.29x faster                                                   |
| mdp                      | 3.70 sec                                                              | 1.67 sec: 2.22x faster                                                  |
| go                       | 264 ms                                                                | 132 ms: 2.01x faster                                                    |
| richards_super           | 107 ms                                                                | 54.7 ms: 1.96x faster                                                   |
| generators               | 68.1 ms                                                               | 35.8 ms: 1.90x faster                                                   |
| richards                 | 91.7 ms                                                               | 48.8 ms: 1.88x faster                                                   |
| raytrace                 | 573 ms                                                                | 317 ms: 1.81x faster                                                    |
| chaos                    | 121 ms                                                                | 67.3 ms: 1.80x faster                                                   |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 723 ms: 1.76x faster                                                    |
| asyncio_tcp              | 944 ms                                                                | 543 ms: 1.74x faster                                                    |
| deepcopy_memo            | 61.7 us                                                               | 35.8 us: 1.73x faster                                                   |
| scimark_sor              | 246 ms                                                                | 143 ms: 1.72x faster                                                    |
| scimark_lu               | 227 ms                                                                | 134 ms: 1.70x faster                                                    |
| scimark_monte_carlo      | 128 ms                                                                | 76.6 ms: 1.67x faster                                                   |
| comprehensions           | 33.1 us                                                               | 20.3 us: 1.63x faster                                                   |
| deepcopy                 | 511 us                                                                | 318 us: 1.61x faster                                                    |
| crypto_pyaes             | 134 ms                                                                | 84.6 ms: 1.58x faster                                                   |
| hexiom                   | 10.9 ms                                                               | 6.99 ms: 1.56x faster                                                   |
| spectral_norm            | 186 ms                                                                | 120 ms: 1.56x faster                                                    |
| pyflate                  | 795 ms                                                                | 515 ms: 1.54x faster                                                    |
| float                    | 135 ms                                                                | 87.6 ms: 1.54x faster                                                   |
| asyncio_tcp_ssl          | 3.28 sec                                                              | 2.17 sec: 1.52x faster                                                  |
| pylint                   | 485 ms                                                                | 324 ms: 1.50x faster                                                    |
| regex_compile            | 177 ms                                                                | 120 ms: 1.47x faster                                                    |
| unpickle_pure_python     | 366 us                                                                | 249 us: 1.47x faster                                                    |
| tomli_loads              | 3.36 sec                                                              | 2.37 sec: 1.42x faster                                                  |
| html5lib                 | 86.5 ms                                                               | 62.1 ms: 1.39x faster                                                   |
| pickle_pure_python       | 529 us                                                                | 382 us: 1.39x faster                                                    |
| django_template          | 53.3 ms                                                               | 39.1 ms: 1.36x faster                                                   |
| deepcopy_reduce          | 4.60 us                                                               | 3.37 us: 1.36x faster                                                   |
| pycparser                | 1.69 sec                                                              | 1.25 sec: 1.36x faster                                                  |
| dulwich_log              | 73.5 ms                                                               | 54.3 ms: 1.35x faster                                                   |
| mako                     | 18.9 ms                                                               | 14.1 ms: 1.34x faster                                                   |
| sympy_integrate          | 26.5 ms                                                               | 20.0 ms: 1.33x faster                                                   |
| genshi_text              | 35.2 ms                                                               | 26.9 ms: 1.31x faster                                                   |
| xml_etree_process        | 99.5 ms                                                               | 76.1 ms: 1.31x faster                                                   |
| logging_simple           | 9.78 us                                                               | 7.50 us: 1.30x faster                                                   |
| logging_format           | 10.6 us                                                               | 8.18 us: 1.30x faster                                                   |
| nbody                    | 166 ms                                                                | 129 ms: 1.29x faster                                                    |
| sympy_str                | 329 ms                                                                | 259 ms: 1.27x faster                                                    |
| 2to3                     | 381 ms                                                                | 301 ms: 1.27x faster                                                    |
| json_dumps               | 16.7 ms                                                               | 13.2 ms: 1.26x faster                                                   |
| sympy_sum                | 184 ms                                                                | 146 ms: 1.26x faster                                                    |
| scimark_fft              | 500 ms                                                                | 402 ms: 1.25x faster                                                    |
| pathlib                  | 26.3 ms                                                               | 21.8 ms: 1.21x faster                                                   |
| coroutines               | 37.2 ms                                                               | 30.9 ms: 1.20x faster                                                   |
| bench_thread_pool        | 1.59 ms                                                               | 1.32 ms: 1.20x faster                                                   |
| unpickle_list            | 6.99 us                                                               | 5.90 us: 1.18x faster                                                   |
| docutils                 | 3.53 sec                                                              | 3.00 sec: 1.18x faster                                                  |
| sympy_expand             | 543 ms                                                                | 465 ms: 1.17x faster                                                    |
| genshi_xml               | 69.8 ms                                                               | 60.5 ms: 1.16x faster                                                   |
| nqueens                  | 117 ms                                                                | 102 ms: 1.15x faster                                                    |
| xml_etree_generate       | 123 ms                                                                | 107 ms: 1.15x faster                                                    |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 6.66 ms: 1.14x faster                                                   |
| fannkuch                 | 546 ms                                                                | 480 ms: 1.14x faster                                                    |
| pprint_pformat           | 2.36 sec                                                              | 2.10 sec: 1.12x faster                                                  |
| pprint_safe_repr         | 1.15 sec                                                              | 1.03 sec: 1.12x faster                                                  |
| meteor_contest           | 126 ms                                                                | 115 ms: 1.10x faster                                                    |
| async_generators         | 452 ms                                                                | 417 ms: 1.08x faster                                                    |
| regex_dna                | 257 ms                                                                | 240 ms: 1.07x faster                                                    |
| sqlite_synth             | 4.12 us                                                               | 3.90 us: 1.06x faster                                                   |
| xml_etree_iterparse      | 156 ms                                                                | 149 ms: 1.05x faster                                                    |
| xml_etree_parse          | 212 ms                                                                | 209 ms: 1.01x faster                                                    |
| asyncio_websockets       | 657 ms                                                                | 674 ms: 1.03x slower                                                    |
| pickle_dict              | 35.1 us                                                               | 36.9 us: 1.05x slower                                                   |
| regex_effbot             | 4.25 ms                                                               | 4.58 ms: 1.08x slower                                                   |
| json_loads               | 30.9 us                                                               | 34.4 us: 1.11x slower                                                   |
| telco                    | 8.49 ms                                                               | 9.46 ms: 1.11x slower                                                   |
| pickle                   | 12.5 us                                                               | 15.4 us: 1.23x slower                                                   |
| pidigits                 | 235 ms                                                                | 293 ms: 1.25x slower                                                    |
| python_startup_no_site   | 6.89 ms                                                               | 8.82 ms: 1.28x slower                                                   |
| python_startup           | 11.2 ms                                                               | 15.2 ms: 1.36x slower                                                   |
| gc_traversal             | 4.15 ms                                                               | 6.81 ms: 1.64x slower                                                   |
| create_gc_cycles         | 2.26 ms                                                               | 3.82 ms: 1.69x slower                                                   |
| logging_silent           | 222 ns                                                                | 596 ns: 2.68x slower                                                    |
| coverage                 | 83.6 ms                                                               | 526 ms: 6.29x slower                                                    |
| thrift                   | 1.26 ms                                                               | 194 ms: 153.94x slower                                                  |
| bench_mp_pool            | 14.5 ms                                                               | 3.87 sec: 266.33x slower                                                |
| Geometric mean           | (ref)                                                                 | 1.11x faster                                                            |

Benchmark hidden because not significant (4): regex_v8, json, unpickle, pickle_list
Ignored benchmarks (13) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20250524-3.15.0a0-2fd09b0-CLANG/bm-20250524-arminc-aarch64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, unpack_sequence

- Geometric mean (including insignificant results): 1.222x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.26x
- 95% likely to have a speedup of 1.24x
- 99% likely to have a speedup of 1.19x

# Memory
- memory change: 1.42x
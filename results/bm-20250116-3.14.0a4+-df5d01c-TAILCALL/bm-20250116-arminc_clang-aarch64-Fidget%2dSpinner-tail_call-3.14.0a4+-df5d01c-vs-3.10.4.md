# Results vs. 3.10.4

- fork: Fidget-Spinner
- ref: tail_call
- machine: linux-aarch64
- commit hash: df5d01c
- commit date: 2025-01-16
- overall geometric mean: 1.355x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.23x faster
- Memory change: 1.36x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250116-arminc-aarch64-Fidget%2dSpinner-tail_call-3.14.0a4+-df5d01c |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 298 ms: 1.28x faster                                                    |
| docutils       | 3.53 sec                                                              | 3.00 sec: 1.18x faster                                                  |
| html5lib       | 86.5 ms                                                               | 60.3 ms: 1.43x faster                                                   |
| Geometric mean | (ref)                                                                 | 1.29x faster                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250116-arminc-aarch64-Fidget%2dSpinner-tail_call-3.14.0a4+-df5d01c |
|-------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_io           | 2.28 sec                                                              | 876 ms: 2.61x faster                                                    |
| async_tree_none         | 950 ms                                                                | 388 ms: 2.45x faster                                                    |
| async_tree_memoization  | 1.13 sec                                                              | 487 ms: 2.33x faster                                                    |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 755 ms: 1.69x faster                                                    |
| Geometric mean          | (ref)                                                                 | 2.24x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250116-arminc-aarch64-Fidget%2dSpinner-tail_call-3.14.0a4+-df5d01c |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 135 ms                                                                | 83.8 ms: 1.61x faster                                                   |
| nbody          | 166 ms                                                                | 108 ms: 1.53x faster                                                    |
| pidigits       | 235 ms                                                                | 302 ms: 1.28x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.24x faster                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250116-arminc-aarch64-Fidget%2dSpinner-tail_call-3.14.0a4+-df5d01c |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 125 ms: 1.42x faster                                                    |
| regex_effbot   | 4.25 ms                                                               | 4.47 ms: 1.05x slower                                                   |
| regex_v8       | 32.2 ms                                                               | 34.2 ms: 1.06x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.05x faster                                                            |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250116-arminc-aarch64-Fidget%2dSpinner-tail_call-3.14.0a4+-df5d01c |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| unpickle_pure_python | 366 us                                                                | 254 us: 1.44x faster                                                    |
| tomli_loads          | 3.36 sec                                                              | 2.46 sec: 1.37x faster                                                  |
| pickle_pure_python   | 529 us                                                                | 388 us: 1.36x faster                                                    |
| xml_etree_process    | 99.5 ms                                                               | 77.2 ms: 1.29x faster                                                   |
| xml_etree_generate   | 123 ms                                                                | 109 ms: 1.12x faster                                                    |
| json_dumps           | 16.7 ms                                                               | 14.9 ms: 1.12x faster                                                   |
| json_loads           | 30.9 us                                                               | 33.2 us: 1.07x slower                                                   |
| Geometric mean       | (ref)                                                                 | 1.17x faster                                                            |

Benchmark hidden because not significant (2): xml_etree_iterparse, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250116-arminc-aarch64-Fidget%2dSpinner-tail_call-3.14.0a4+-df5d01c |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 6.89 ms                                                               | 9.10 ms: 1.32x slower                                                   |
| python_startup         | 11.2 ms                                                               | 16.5 ms: 1.47x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.40x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250116-arminc-aarch64-Fidget%2dSpinner-tail_call-3.14.0a4+-df5d01c |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 14.1 ms: 1.35x faster                                                   |
| genshi_text     | 35.2 ms                                                               | 26.8 ms: 1.31x faster                                                   |
| django_template | 53.3 ms                                                               | 41.4 ms: 1.29x faster                                                   |
| genshi_xml      | 69.8 ms                                                               | 60.5 ms: 1.16x faster                                                   |
| Geometric mean  | (ref)                                                                 | 1.27x faster                                                            |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250116-arminc-aarch64-Fidget%2dSpinner-tail_call-3.14.0a4+-df5d01c |
|--------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 194 us: 3.40x faster                                                    |
| async_tree_io            | 2.28 sec                                                              | 876 ms: 2.61x faster                                                    |
| async_tree_none          | 950 ms                                                                | 388 ms: 2.45x faster                                                    |
| deltablue                | 8.94 ms                                                               | 3.76 ms: 2.38x faster                                                   |
| async_tree_memoization   | 1.13 sec                                                              | 487 ms: 2.33x faster                                                    |
| go                       | 264 ms                                                                | 132 ms: 2.00x faster                                                    |
| richards                 | 91.7 ms                                                               | 47.9 ms: 1.92x faster                                                   |
| logging_silent           | 222 ns                                                                | 117 ns: 1.89x faster                                                    |
| richards_super           | 107 ms                                                                | 56.7 ms: 1.89x faster                                                   |
| generators               | 68.1 ms                                                               | 36.6 ms: 1.86x faster                                                   |
| raytrace                 | 573 ms                                                                | 312 ms: 1.84x faster                                                    |
| chaos                    | 121 ms                                                                | 67.5 ms: 1.79x faster                                                   |
| sqlglot_parse            | 2.40 ms                                                               | 1.37 ms: 1.75x faster                                                   |
| scimark_sor              | 246 ms                                                                | 141 ms: 1.74x faster                                                    |
| scimark_monte_carlo      | 128 ms                                                                | 75.3 ms: 1.70x faster                                                   |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 755 ms: 1.69x faster                                                    |
| deepcopy_memo            | 61.7 us                                                               | 36.7 us: 1.68x faster                                                   |
| scimark_lu               | 227 ms                                                                | 136 ms: 1.67x faster                                                    |
| comprehensions           | 33.1 us                                                               | 20.2 us: 1.64x faster                                                   |
| spectral_norm            | 186 ms                                                                | 116 ms: 1.61x faster                                                    |
| float                    | 135 ms                                                                | 83.8 ms: 1.61x faster                                                   |
| pylint                   | 485 ms                                                                | 303 ms: 1.60x faster                                                    |
| sqlglot_transpile        | 2.84 ms                                                               | 1.79 ms: 1.59x faster                                                   |
| crypto_pyaes             | 134 ms                                                                | 85.0 ms: 1.58x faster                                                   |
| hexiom                   | 10.9 ms                                                               | 7.08 ms: 1.54x faster                                                   |
| nbody                    | 166 ms                                                                | 108 ms: 1.53x faster                                                    |
| deepcopy                 | 511 us                                                                | 335 us: 1.52x faster                                                    |
| pyflate                  | 795 ms                                                                | 531 ms: 1.50x faster                                                    |
| unpickle_pure_python     | 366 us                                                                | 254 us: 1.44x faster                                                    |
| html5lib                 | 86.5 ms                                                               | 60.3 ms: 1.43x faster                                                   |
| logging_simple           | 9.78 us                                                               | 6.86 us: 1.43x faster                                                   |
| regex_compile            | 177 ms                                                                | 125 ms: 1.42x faster                                                    |
| logging_format           | 10.6 us                                                               | 7.75 us: 1.37x faster                                                   |
| tomli_loads              | 3.36 sec                                                              | 2.46 sec: 1.37x faster                                                  |
| pickle_pure_python       | 529 us                                                                | 388 us: 1.36x faster                                                    |
| mako                     | 18.9 ms                                                               | 14.1 ms: 1.35x faster                                                   |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 5.67 ms: 1.35x faster                                                   |
| pycparser                | 1.69 sec                                                              | 1.27 sec: 1.34x faster                                                  |
| scimark_fft              | 500 ms                                                                | 377 ms: 1.33x faster                                                    |
| sqlalchemy_imperative    | 20.5 ms                                                               | 15.5 ms: 1.32x faster                                                   |
| sqlalchemy_declarative   | 197 ms                                                                | 150 ms: 1.32x faster                                                    |
| deepcopy_reduce          | 4.60 us                                                               | 3.49 us: 1.32x faster                                                   |
| coroutines               | 37.2 ms                                                               | 28.2 ms: 1.32x faster                                                   |
| genshi_text              | 35.2 ms                                                               | 26.8 ms: 1.31x faster                                                   |
| thrift                   | 1.26 ms                                                               | 973 us: 1.29x faster                                                    |
| django_template          | 53.3 ms                                                               | 41.4 ms: 1.29x faster                                                   |
| xml_etree_process        | 99.5 ms                                                               | 77.2 ms: 1.29x faster                                                   |
| 2to3                     | 381 ms                                                                | 298 ms: 1.28x faster                                                    |
| sympy_sum                | 184 ms                                                                | 144 ms: 1.27x faster                                                    |
| sympy_integrate          | 26.5 ms                                                               | 20.9 ms: 1.27x faster                                                   |
| sympy_str                | 329 ms                                                                | 261 ms: 1.26x faster                                                    |
| pathlib                  | 26.3 ms                                                               | 20.9 ms: 1.26x faster                                                   |
| dulwich_log              | 73.5 ms                                                               | 58.7 ms: 1.25x faster                                                   |
| sqlglot_optimize         | 75.4 ms                                                               | 62.9 ms: 1.20x faster                                                   |
| bench_thread_pool        | 1.59 ms                                                               | 1.33 ms: 1.19x faster                                                   |
| pprint_pformat           | 2.36 sec                                                              | 1.98 sec: 1.19x faster                                                  |
| sqlglot_normalize        | 156 ms                                                                | 132 ms: 1.18x faster                                                    |
| pprint_safe_repr         | 1.15 sec                                                              | 970 ms: 1.18x faster                                                    |
| docutils                 | 3.53 sec                                                              | 3.00 sec: 1.18x faster                                                  |
| nqueens                  | 117 ms                                                                | 101 ms: 1.16x faster                                                    |
| genshi_xml               | 69.8 ms                                                               | 60.5 ms: 1.16x faster                                                   |
| sympy_expand             | 543 ms                                                                | 476 ms: 1.14x faster                                                    |
| mdp                      | 3.70 sec                                                              | 3.27 sec: 1.13x faster                                                  |
| xml_etree_generate       | 123 ms                                                                | 109 ms: 1.12x faster                                                    |
| fannkuch                 | 546 ms                                                                | 487 ms: 1.12x faster                                                    |
| json_dumps               | 16.7 ms                                                               | 14.9 ms: 1.12x faster                                                   |
| async_generators         | 452 ms                                                                | 419 ms: 1.08x faster                                                    |
| meteor_contest           | 126 ms                                                                | 119 ms: 1.06x faster                                                    |
| asyncio_websockets       | 657 ms                                                                | 675 ms: 1.03x slower                                                    |
| regex_effbot             | 4.25 ms                                                               | 4.47 ms: 1.05x slower                                                   |
| regex_v8                 | 32.2 ms                                                               | 34.2 ms: 1.06x slower                                                   |
| json_loads               | 30.9 us                                                               | 33.2 us: 1.07x slower                                                   |
| telco                    | 8.49 ms                                                               | 9.16 ms: 1.08x slower                                                   |
| coverage                 | 83.6 ms                                                               | 98.5 ms: 1.18x slower                                                   |
| pidigits                 | 235 ms                                                                | 302 ms: 1.28x slower                                                    |
| python_startup_no_site   | 6.89 ms                                                               | 9.10 ms: 1.32x slower                                                   |
| python_startup           | 11.2 ms                                                               | 16.5 ms: 1.47x slower                                                   |
| gc_traversal             | 4.15 ms                                                               | 6.67 ms: 1.60x slower                                                   |
| create_gc_cycles         | 2.26 ms                                                               | 3.70 ms: 1.64x slower                                                   |
| bench_mp_pool            | 14.5 ms                                                               | 6.83 sec: 470.23x slower                                                |
| Geometric mean           | (ref)                                                                 | 1.23x faster                                                            |

Benchmark hidden because not significant (5): xml_etree_iterparse, xml_etree_parse, json, sqlite_synth, regex_dna
Ignored benchmarks (14) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20250116-3.14.0a4+-df5d01c-CLANG/bm-20250116-arminc-aarch64-Fidget%2dSpinner-tail_call-3.14.0a4+-df5d01c.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.355x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.28x
- 95% likely to have a speedup of 1.26x
- 99% likely to have a speedup of 1.23x

# Memory
- memory change: 1.36x
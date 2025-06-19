# Results vs. 3.10.4

- fork: python
- ref: 9731dd2c8df3509095ea
- machine: linux-aarch64
- commit hash: 9731dd2
- commit date: 2025-06-19
- overall geometric mean: 1.321x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.20x faster
- Memory change: 1.39x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250619-arminc-aarch64-python-9731dd2c8df3509095ea-3.15.0a0-9731dd2 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 312 ms: 1.22x faster                                                    |
| docutils       | 3.53 sec                                                              | 3.09 sec: 1.14x faster                                                  |
| html5lib       | 86.5 ms                                                               | 63.1 ms: 1.37x faster                                                   |
| Geometric mean | (ref)                                                                 | 1.24x faster                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250619-arminc-aarch64-python-9731dd2c8df3509095ea-3.15.0a0-9731dd2 |
|-------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_io           | 2.28 sec                                                              | 899 ms: 2.54x faster                                                    |
| async_tree_memoization  | 1.13 sec                                                              | 472 ms: 2.40x faster                                                    |
| async_tree_none         | 950 ms                                                                | 399 ms: 2.38x faster                                                    |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 665 ms: 1.91x faster                                                    |
| Geometric mean          | (ref)                                                                 | 2.30x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250619-arminc-aarch64-python-9731dd2c8df3509095ea-3.15.0a0-9731dd2 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 135 ms                                                                | 83.4 ms: 1.62x faster                                                   |
| nbody          | 166 ms                                                                | 125 ms: 1.33x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.28x faster                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250619-arminc-aarch64-python-9731dd2c8df3509095ea-3.15.0a0-9731dd2 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 122 ms: 1.45x faster                                                    |
| regex_v8       | 32.2 ms                                                               | 27.4 ms: 1.18x faster                                                   |
| regex_dna      | 257 ms                                                                | 225 ms: 1.14x faster                                                    |
| regex_effbot   | 4.25 ms                                                               | 3.93 ms: 1.08x faster                                                   |
| Geometric mean | (ref)                                                                 | 1.20x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250619-arminc-aarch64-python-9731dd2c8df3509095ea-3.15.0a0-9731dd2 |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| tomli_loads          | 3.36 sec                                                              | 2.32 sec: 1.45x faster                                                  |
| unpickle_pure_python | 366 us                                                                | 254 us: 1.44x faster                                                    |
| pickle_pure_python   | 529 us                                                                | 405 us: 1.31x faster                                                    |
| xml_etree_process    | 99.5 ms                                                               | 78.8 ms: 1.26x faster                                                   |
| json_dumps           | 16.7 ms                                                               | 13.8 ms: 1.21x faster                                                   |
| xml_etree_parse      | 212 ms                                                                | 178 ms: 1.19x faster                                                    |
| xml_etree_generate   | 123 ms                                                                | 110 ms: 1.12x faster                                                    |
| xml_etree_iterparse  | 156 ms                                                                | 144 ms: 1.09x faster                                                    |
| json_loads           | 30.9 us                                                               | 32.3 us: 1.04x slower                                                   |
| Geometric mean       | (ref)                                                                 | 1.21x faster                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250619-arminc-aarch64-python-9731dd2c8df3509095ea-3.15.0a0-9731dd2 |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 6.89 ms                                                               | 8.69 ms: 1.26x slower                                                   |
| python_startup         | 11.2 ms                                                               | 15.2 ms: 1.36x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.31x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250619-arminc-aarch64-python-9731dd2c8df3509095ea-3.15.0a0-9731dd2 |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 13.2 ms: 1.43x faster                                                   |
| django_template | 53.3 ms                                                               | 40.5 ms: 1.32x faster                                                   |
| genshi_text     | 35.2 ms                                                               | 27.9 ms: 1.26x faster                                                   |
| genshi_xml      | 69.8 ms                                                               | 63.9 ms: 1.09x faster                                                   |
| Geometric mean  | (ref)                                                                 | 1.27x faster                                                            |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250619-arminc-aarch64-python-9731dd2c8df3509095ea-3.15.0a0-9731dd2 |
|--------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 210 us: 3.15x faster                                                    |
| async_tree_io            | 2.28 sec                                                              | 899 ms: 2.54x faster                                                    |
| async_tree_memoization   | 1.13 sec                                                              | 472 ms: 2.40x faster                                                    |
| async_tree_none          | 950 ms                                                                | 399 ms: 2.38x faster                                                    |
| deltablue                | 8.94 ms                                                               | 3.87 ms: 2.31x faster                                                   |
| mdp                      | 3.70 sec                                                              | 1.68 sec: 2.20x faster                                                  |
| richards_super           | 107 ms                                                                | 52.1 ms: 2.06x faster                                                   |
| richards                 | 91.7 ms                                                               | 46.0 ms: 1.99x faster                                                   |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 665 ms: 1.91x faster                                                    |
| generators               | 68.1 ms                                                               | 36.0 ms: 1.89x faster                                                   |
| chaos                    | 121 ms                                                                | 69.4 ms: 1.74x faster                                                   |
| scimark_sor              | 246 ms                                                                | 143 ms: 1.72x faster                                                    |
| raytrace                 | 573 ms                                                                | 335 ms: 1.71x faster                                                    |
| go                       | 264 ms                                                                | 158 ms: 1.67x faster                                                    |
| deepcopy_memo            | 61.7 us                                                               | 37.4 us: 1.65x faster                                                   |
| float                    | 135 ms                                                                | 83.4 ms: 1.62x faster                                                   |
| spectral_norm            | 186 ms                                                                | 121 ms: 1.55x faster                                                    |
| scimark_monte_carlo      | 128 ms                                                                | 82.8 ms: 1.54x faster                                                   |
| pylint                   | 485 ms                                                                | 318 ms: 1.52x faster                                                    |
| deepcopy                 | 511 us                                                                | 342 us: 1.49x faster                                                    |
| scimark_lu               | 227 ms                                                                | 153 ms: 1.49x faster                                                    |
| comprehensions           | 33.1 us                                                               | 22.4 us: 1.48x faster                                                   |
| hexiom                   | 10.9 ms                                                               | 7.43 ms: 1.47x faster                                                   |
| pyflate                  | 795 ms                                                                | 542 ms: 1.47x faster                                                    |
| crypto_pyaes             | 134 ms                                                                | 91.9 ms: 1.46x faster                                                   |
| tomli_loads              | 3.36 sec                                                              | 2.32 sec: 1.45x faster                                                  |
| regex_compile            | 177 ms                                                                | 122 ms: 1.45x faster                                                    |
| unpickle_pure_python     | 366 us                                                                | 254 us: 1.44x faster                                                    |
| mako                     | 18.9 ms                                                               | 13.2 ms: 1.43x faster                                                   |
| html5lib                 | 86.5 ms                                                               | 63.1 ms: 1.37x faster                                                   |
| nbody                    | 166 ms                                                                | 125 ms: 1.33x faster                                                    |
| django_template          | 53.3 ms                                                               | 40.5 ms: 1.32x faster                                                   |
| thrift                   | 1.26 ms                                                               | 958 us: 1.31x faster                                                    |
| pickle_pure_python       | 529 us                                                                | 405 us: 1.31x faster                                                    |
| dulwich_log              | 73.5 ms                                                               | 56.5 ms: 1.30x faster                                                   |
| coroutines               | 37.2 ms                                                               | 29.1 ms: 1.28x faster                                                   |
| sympy_integrate          | 26.5 ms                                                               | 20.9 ms: 1.27x faster                                                   |
| logging_simple           | 9.78 us                                                               | 7.72 us: 1.27x faster                                                   |
| logging_format           | 10.6 us                                                               | 8.38 us: 1.27x faster                                                   |
| xml_etree_process        | 99.5 ms                                                               | 78.8 ms: 1.26x faster                                                   |
| genshi_text              | 35.2 ms                                                               | 27.9 ms: 1.26x faster                                                   |
| deepcopy_reduce          | 4.60 us                                                               | 3.66 us: 1.26x faster                                                   |
| scimark_fft              | 500 ms                                                                | 405 ms: 1.24x faster                                                    |
| pycparser                | 1.69 sec                                                              | 1.38 sec: 1.23x faster                                                  |
| sympy_sum                | 184 ms                                                                | 150 ms: 1.23x faster                                                    |
| 2to3                     | 381 ms                                                                | 312 ms: 1.22x faster                                                    |
| json_dumps               | 16.7 ms                                                               | 13.8 ms: 1.21x faster                                                   |
| xml_etree_parse          | 212 ms                                                                | 178 ms: 1.19x faster                                                    |
| sympy_str                | 329 ms                                                                | 278 ms: 1.18x faster                                                    |
| pathlib                  | 26.3 ms                                                               | 22.3 ms: 1.18x faster                                                   |
| regex_v8                 | 32.2 ms                                                               | 27.4 ms: 1.18x faster                                                   |
| nqueens                  | 117 ms                                                                | 103 ms: 1.15x faster                                                    |
| regex_dna                | 257 ms                                                                | 225 ms: 1.14x faster                                                    |
| fannkuch                 | 546 ms                                                                | 477 ms: 1.14x faster                                                    |
| docutils                 | 3.53 sec                                                              | 3.09 sec: 1.14x faster                                                  |
| xml_etree_generate       | 123 ms                                                                | 110 ms: 1.12x faster                                                    |
| meteor_contest           | 126 ms                                                                | 113 ms: 1.11x faster                                                    |
| sympy_expand             | 543 ms                                                                | 493 ms: 1.10x faster                                                    |
| genshi_xml               | 69.8 ms                                                               | 63.9 ms: 1.09x faster                                                   |
| xml_etree_iterparse      | 156 ms                                                                | 144 ms: 1.09x faster                                                    |
| regex_effbot             | 4.25 ms                                                               | 3.93 ms: 1.08x faster                                                   |
| sqlite_synth             | 4.12 us                                                               | 3.87 us: 1.06x faster                                                   |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 7.19 ms: 1.06x faster                                                   |
| asyncio_websockets       | 657 ms                                                                | 668 ms: 1.02x slower                                                    |
| json_loads               | 30.9 us                                                               | 32.3 us: 1.04x slower                                                   |
| async_generators         | 452 ms                                                                | 476 ms: 1.05x slower                                                    |
| pprint_pformat           | 2.36 sec                                                              | 2.61 sec: 1.11x slower                                                  |
| pprint_safe_repr         | 1.15 sec                                                              | 1.27 sec: 1.11x slower                                                  |
| telco                    | 8.49 ms                                                               | 9.55 ms: 1.13x slower                                                   |
| coverage                 | 83.6 ms                                                               | 101 ms: 1.21x slower                                                    |
| python_startup_no_site   | 6.89 ms                                                               | 8.69 ms: 1.26x slower                                                   |
| python_startup           | 11.2 ms                                                               | 15.2 ms: 1.36x slower                                                   |
| gc_traversal             | 4.15 ms                                                               | 6.88 ms: 1.66x slower                                                   |
| create_gc_cycles         | 2.26 ms                                                               | 3.82 ms: 1.69x slower                                                   |
| logging_silent           | 222 ns                                                                | 647 ns: 2.91x slower                                                    |
| Geometric mean           | (ref)                                                                 | 1.29x faster                                                            |

Benchmark hidden because not significant (2): json, pidigits
Ignored benchmarks (22) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250619-3.15.0a0-9731dd2-JIT/bm-20250619-arminc-aarch64-python-9731dd2c8df3509095ea-3.15.0a0-9731dd2.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.321x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.24x
- 95% likely to have a speedup of 1.22x
- 99% likely to have a speedup of 1.20x

# Memory
- memory change: 1.39x
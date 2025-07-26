# Results vs. 3.10.4

- fork: python
- ref: 1e69cd1634e4f0f8c375
- machine: linux-aarch64
- commit hash: 1e69cd1
- commit date: 2025-07-25
- overall geometric mean: 1.283x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.20x faster
- Memory change: 1.40x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250725-arminc-aarch64-python-1e69cd1634e4f0f8c375-3.15.0a0-1e69cd1 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 311 ms: 1.22x faster                                                    |
| docutils       | 3.53 sec                                                              | 3.10 sec: 1.14x faster                                                  |
| html5lib       | 86.5 ms                                                               | 64.7 ms: 1.34x faster                                                   |
| Geometric mean | (ref)                                                                 | 1.23x faster                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250725-arminc-aarch64-python-1e69cd1634e4f0f8c375-3.15.0a0-1e69cd1 |
|-------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_io           | 2.28 sec                                                              | 900 ms: 2.54x faster                                                    |
| async_tree_memoization  | 1.13 sec                                                              | 471 ms: 2.41x faster                                                    |
| async_tree_none         | 950 ms                                                                | 395 ms: 2.40x faster                                                    |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 667 ms: 1.91x faster                                                    |
| Geometric mean          | (ref)                                                                 | 2.30x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250725-arminc-aarch64-python-1e69cd1634e4f0f8c375-3.15.0a0-1e69cd1 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 135 ms                                                                | 82.4 ms: 1.64x faster                                                   |
| nbody          | 166 ms                                                                | 129 ms: 1.29x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.28x faster                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250725-arminc-aarch64-python-1e69cd1634e4f0f8c375-3.15.0a0-1e69cd1 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 125 ms: 1.41x faster                                                    |
| regex_v8       | 32.2 ms                                                               | 26.3 ms: 1.22x faster                                                   |
| regex_dna      | 257 ms                                                                | 218 ms: 1.18x faster                                                    |
| regex_effbot   | 4.25 ms                                                               | 3.79 ms: 1.12x faster                                                   |
| Geometric mean | (ref)                                                                 | 1.23x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250725-arminc-aarch64-python-1e69cd1634e4f0f8c375-3.15.0a0-1e69cd1 |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| tomli_loads          | 3.36 sec                                                              | 2.32 sec: 1.45x faster                                                  |
| unpickle_pure_python | 366 us                                                                | 256 us: 1.43x faster                                                    |
| pickle_pure_python   | 529 us                                                                | 403 us: 1.31x faster                                                    |
| xml_etree_process    | 99.5 ms                                                               | 80.5 ms: 1.24x faster                                                   |
| json_dumps           | 16.7 ms                                                               | 14.0 ms: 1.19x faster                                                   |
| xml_etree_parse      | 212 ms                                                                | 178 ms: 1.19x faster                                                    |
| xml_etree_generate   | 123 ms                                                                | 109 ms: 1.13x faster                                                    |
| xml_etree_iterparse  | 156 ms                                                                | 145 ms: 1.08x faster                                                    |
| json_loads           | 30.9 us                                                               | 33.4 us: 1.08x slower                                                   |
| Geometric mean       | (ref)                                                                 | 1.20x faster                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250725-arminc-aarch64-python-1e69cd1634e4f0f8c375-3.15.0a0-1e69cd1 |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 6.89 ms                                                               | 8.56 ms: 1.24x slower                                                   |
| python_startup         | 11.2 ms                                                               | 15.1 ms: 1.35x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.29x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250725-arminc-aarch64-python-1e69cd1634e4f0f8c375-3.15.0a0-1e69cd1 |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 13.0 ms: 1.46x faster                                                   |
| django_template | 53.3 ms                                                               | 39.1 ms: 1.37x faster                                                   |
| genshi_text     | 35.2 ms                                                               | 27.3 ms: 1.29x faster                                                   |
| genshi_xml      | 69.8 ms                                                               | 64.8 ms: 1.08x faster                                                   |
| Geometric mean  | (ref)                                                                 | 1.29x faster                                                            |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250725-arminc-aarch64-python-1e69cd1634e4f0f8c375-3.15.0a0-1e69cd1 |
|--------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 203 us: 3.26x faster                                                    |
| async_tree_io            | 2.28 sec                                                              | 900 ms: 2.54x faster                                                    |
| async_tree_memoization   | 1.13 sec                                                              | 471 ms: 2.41x faster                                                    |
| async_tree_none          | 950 ms                                                                | 395 ms: 2.40x faster                                                    |
| deltablue                | 8.94 ms                                                               | 3.85 ms: 2.32x faster                                                   |
| mdp                      | 3.70 sec                                                              | 1.67 sec: 2.21x faster                                                  |
| richards_super           | 107 ms                                                                | 51.5 ms: 2.08x faster                                                   |
| richards                 | 91.7 ms                                                               | 45.0 ms: 2.04x faster                                                   |
| generators               | 68.1 ms                                                               | 35.6 ms: 1.91x faster                                                   |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 667 ms: 1.91x faster                                                    |
| raytrace                 | 573 ms                                                                | 333 ms: 1.72x faster                                                    |
| chaos                    | 121 ms                                                                | 70.4 ms: 1.72x faster                                                   |
| go                       | 264 ms                                                                | 154 ms: 1.72x faster                                                    |
| scimark_sor              | 246 ms                                                                | 143 ms: 1.72x faster                                                    |
| logging_silent           | 222 ns                                                                | 132 ns: 1.68x faster                                                    |
| deepcopy_memo            | 61.7 us                                                               | 37.1 us: 1.66x faster                                                   |
| float                    | 135 ms                                                                | 82.4 ms: 1.64x faster                                                   |
| spectral_norm            | 186 ms                                                                | 119 ms: 1.57x faster                                                    |
| scimark_lu               | 227 ms                                                                | 146 ms: 1.55x faster                                                    |
| scimark_monte_carlo      | 128 ms                                                                | 82.6 ms: 1.55x faster                                                   |
| deepcopy                 | 511 us                                                                | 331 us: 1.54x faster                                                    |
| pylint                   | 485 ms                                                                | 325 ms: 1.49x faster                                                    |
| comprehensions           | 33.1 us                                                               | 22.3 us: 1.49x faster                                                   |
| pyflate                  | 795 ms                                                                | 536 ms: 1.48x faster                                                    |
| mako                     | 18.9 ms                                                               | 13.0 ms: 1.46x faster                                                   |
| hexiom                   | 10.9 ms                                                               | 7.52 ms: 1.45x faster                                                   |
| tomli_loads              | 3.36 sec                                                              | 2.32 sec: 1.45x faster                                                  |
| crypto_pyaes             | 134 ms                                                                | 93.5 ms: 1.43x faster                                                   |
| unpickle_pure_python     | 366 us                                                                | 256 us: 1.43x faster                                                    |
| regex_compile            | 177 ms                                                                | 125 ms: 1.41x faster                                                    |
| logging_simple           | 9.78 us                                                               | 7.04 us: 1.39x faster                                                   |
| dulwich_log              | 73.5 ms                                                               | 53.2 ms: 1.38x faster                                                   |
| logging_format           | 10.6 us                                                               | 7.68 us: 1.38x faster                                                   |
| django_template          | 53.3 ms                                                               | 39.1 ms: 1.37x faster                                                   |
| html5lib                 | 86.5 ms                                                               | 64.7 ms: 1.34x faster                                                   |
| thrift                   | 1.26 ms                                                               | 953 us: 1.32x faster                                                    |
| pickle_pure_python       | 529 us                                                                | 403 us: 1.31x faster                                                    |
| genshi_text              | 35.2 ms                                                               | 27.3 ms: 1.29x faster                                                   |
| nbody                    | 166 ms                                                                | 129 ms: 1.29x faster                                                    |
| sympy_integrate          | 26.5 ms                                                               | 20.9 ms: 1.27x faster                                                   |
| deepcopy_reduce          | 4.60 us                                                               | 3.63 us: 1.27x faster                                                   |
| sympy_sum                | 184 ms                                                                | 148 ms: 1.25x faster                                                    |
| pycparser                | 1.69 sec                                                              | 1.36 sec: 1.25x faster                                                  |
| coroutines               | 37.2 ms                                                               | 30.0 ms: 1.24x faster                                                   |
| xml_etree_process        | 99.5 ms                                                               | 80.5 ms: 1.24x faster                                                   |
| 2to3                     | 381 ms                                                                | 311 ms: 1.22x faster                                                    |
| regex_v8                 | 32.2 ms                                                               | 26.3 ms: 1.22x faster                                                   |
| scimark_fft              | 500 ms                                                                | 414 ms: 1.21x faster                                                    |
| sympy_str                | 329 ms                                                                | 275 ms: 1.19x faster                                                    |
| json_dumps               | 16.7 ms                                                               | 14.0 ms: 1.19x faster                                                   |
| xml_etree_parse          | 212 ms                                                                | 178 ms: 1.19x faster                                                    |
| pathlib                  | 26.3 ms                                                               | 22.2 ms: 1.19x faster                                                   |
| regex_dna                | 257 ms                                                                | 218 ms: 1.18x faster                                                    |
| fannkuch                 | 546 ms                                                                | 467 ms: 1.17x faster                                                    |
| docutils                 | 3.53 sec                                                              | 3.10 sec: 1.14x faster                                                  |
| nqueens                  | 117 ms                                                                | 103 ms: 1.13x faster                                                    |
| xml_etree_generate       | 123 ms                                                                | 109 ms: 1.13x faster                                                    |
| regex_effbot             | 4.25 ms                                                               | 3.79 ms: 1.12x faster                                                   |
| sympy_expand             | 543 ms                                                                | 488 ms: 1.11x faster                                                    |
| sqlite_synth             | 4.12 us                                                               | 3.71 us: 1.11x faster                                                   |
| meteor_contest           | 126 ms                                                                | 114 ms: 1.11x faster                                                    |
| genshi_xml               | 69.8 ms                                                               | 64.8 ms: 1.08x faster                                                   |
| xml_etree_iterparse      | 156 ms                                                                | 145 ms: 1.08x faster                                                    |
| pprint_pformat           | 2.36 sec                                                              | 2.30 sec: 1.02x faster                                                  |
| json                     | 5.88 ms                                                               | 5.84 ms: 1.01x faster                                                   |
| asyncio_websockets       | 657 ms                                                                | 667 ms: 1.02x slower                                                    |
| json_loads               | 30.9 us                                                               | 33.4 us: 1.08x slower                                                   |
| async_generators         | 452 ms                                                                | 494 ms: 1.09x slower                                                    |
| coverage                 | 83.6 ms                                                               | 102 ms: 1.23x slower                                                    |
| python_startup_no_site   | 6.89 ms                                                               | 8.56 ms: 1.24x slower                                                   |
| python_startup           | 11.2 ms                                                               | 15.1 ms: 1.35x slower                                                   |
| gc_traversal             | 4.15 ms                                                               | 6.82 ms: 1.64x slower                                                   |
| create_gc_cycles         | 2.26 ms                                                               | 3.76 ms: 1.67x slower                                                   |
| telco                    | 8.49 ms                                                               | 164 ms: 19.29x slower                                                   |
| Geometric mean           | (ref)                                                                 | 1.28x faster                                                            |

Benchmark hidden because not significant (3): scimark_sparse_mat_mult, pprint_safe_repr, pidigits
Ignored benchmarks (22) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250725-3.15.0a0-1e69cd1-JIT/bm-20250725-arminc-aarch64-python-1e69cd1634e4f0f8c375-3.15.0a0-1e69cd1.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.283x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.23x
- 95% likely to have a speedup of 1.22x
- 99% likely to have a speedup of 1.20x

# Memory
- memory change: 1.40x
# Results vs. 3.10.4

- fork: python
- ref: 800d37feca2e0ea33439
- machine: linux-aarch64
- commit hash: 800d37f
- commit date: 2025-07-19
- overall geometric mean: 1.143x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.08x faster
- Memory change: 1.67x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250719-arminc-aarch64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 349 ms: 1.09x faster                                                    |
| docutils       | 3.53 sec                                                              | 3.21 sec: 1.10x faster                                                  |
| html5lib       | 86.5 ms                                                               | 70.9 ms: 1.22x faster                                                   |
| Geometric mean | (ref)                                                                 | 1.13x faster                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250719-arminc-aarch64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|-------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_io           | 2.28 sec                                                              | 842 ms: 2.71x faster                                                    |
| async_tree_none         | 950 ms                                                                | 392 ms: 2.42x faster                                                    |
| async_tree_memoization  | 1.13 sec                                                              | 478 ms: 2.37x faster                                                    |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 662 ms: 1.92x faster                                                    |
| Geometric mean          | (ref)                                                                 | 2.34x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250719-arminc-aarch64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 135 ms                                                                | 94.2 ms: 1.43x faster                                                   |
| nbody          | 166 ms                                                                | 180 ms: 1.08x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.10x faster                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250719-arminc-aarch64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_v8       | 32.2 ms                                                               | 25.7 ms: 1.25x faster                                                   |
| regex_compile  | 177 ms                                                                | 149 ms: 1.19x faster                                                    |
| regex_effbot   | 4.25 ms                                                               | 3.87 ms: 1.10x faster                                                   |
| regex_dna      | 257 ms                                                                | 236 ms: 1.09x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.15x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250719-arminc-aarch64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| unpickle_pure_python | 366 us                                                                | 296 us: 1.23x faster                                                    |
| pickle_pure_python   | 529 us                                                                | 441 us: 1.20x faster                                                    |
| tomli_loads          | 3.36 sec                                                              | 2.82 sec: 1.19x faster                                                  |
| xml_etree_parse      | 212 ms                                                                | 180 ms: 1.18x faster                                                    |
| xml_etree_iterparse  | 156 ms                                                                | 135 ms: 1.15x faster                                                    |
| json_dumps           | 16.7 ms                                                               | 15.0 ms: 1.11x faster                                                   |
| unpickle_list        | 6.99 us                                                               | 6.95 us: 1.01x faster                                                   |
| xml_etree_process    | 99.5 ms                                                               | 102 ms: 1.03x slower                                                    |
| pickle_list          | 5.24 us                                                               | 5.66 us: 1.08x slower                                                   |
| pickle_dict          | 35.1 us                                                               | 38.8 us: 1.10x slower                                                   |
| xml_etree_generate   | 123 ms                                                                | 140 ms: 1.14x slower                                                    |
| unpickle             | 17.5 us                                                               | 20.1 us: 1.15x slower                                                   |
| json_loads           | 30.9 us                                                               | 37.0 us: 1.20x slower                                                   |
| pickle               | 12.5 us                                                               | 15.7 us: 1.26x slower                                                   |
| Geometric mean       | (ref)                                                                 | 1.01x faster                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250719-arminc-aarch64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 6.89 ms                                                               | 12.0 ms: 1.74x slower                                                   |
| python_startup         | 11.2 ms                                                               | 20.0 ms: 1.79x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.77x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250719-arminc-aarch64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| django_template | 53.3 ms                                                               | 51.0 ms: 1.05x faster                                                   |
| genshi_xml      | 69.8 ms                                                               | 74.6 ms: 1.07x slower                                                   |
| mako            | 18.9 ms                                                               | 21.3 ms: 1.13x slower                                                   |
| Geometric mean  | (ref)                                                                 | 1.05x slower                                                            |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250719-arminc-aarch64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|--------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_io            | 2.28 sec                                                              | 842 ms: 2.71x faster                                                    |
| typing_runtime_protocols | 661 us                                                                | 247 us: 2.68x faster                                                    |
| async_tree_none          | 950 ms                                                                | 392 ms: 2.42x faster                                                    |
| async_tree_memoization   | 1.13 sec                                                              | 478 ms: 2.37x faster                                                    |
| deltablue                | 8.94 ms                                                               | 4.63 ms: 1.93x faster                                                   |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 662 ms: 1.92x faster                                                    |
| mdp                      | 3.70 sec                                                              | 1.93 sec: 1.92x faster                                                  |
| go                       | 264 ms                                                                | 151 ms: 1.75x faster                                                    |
| generators               | 68.1 ms                                                               | 40.4 ms: 1.68x faster                                                   |
| asyncio_tcp              | 944 ms                                                                | 564 ms: 1.68x faster                                                    |
| logging_silent           | 222 ns                                                                | 140 ns: 1.59x faster                                                    |
| scimark_sor              | 246 ms                                                                | 160 ms: 1.54x faster                                                    |
| chaos                    | 121 ms                                                                | 82.8 ms: 1.46x faster                                                   |
| gc_traversal             | 4.15 ms                                                               | 2.84 ms: 1.46x faster                                                   |
| raytrace                 | 573 ms                                                                | 393 ms: 1.46x faster                                                    |
| float                    | 135 ms                                                                | 94.2 ms: 1.43x faster                                                   |
| hexiom                   | 10.9 ms                                                               | 7.72 ms: 1.41x faster                                                   |
| comprehensions           | 33.1 us                                                               | 24.4 us: 1.36x faster                                                   |
| asyncio_tcp_ssl          | 3.28 sec                                                              | 2.42 sec: 1.36x faster                                                  |
| pyflate                  | 795 ms                                                                | 588 ms: 1.35x faster                                                    |
| richards_super           | 107 ms                                                                | 79.8 ms: 1.34x faster                                                   |
| deepcopy_memo            | 61.7 us                                                               | 46.5 us: 1.33x faster                                                   |
| deepcopy                 | 511 us                                                                | 390 us: 1.31x faster                                                    |
| spectral_norm            | 186 ms                                                                | 143 ms: 1.31x faster                                                    |
| richards                 | 91.7 ms                                                               | 70.8 ms: 1.30x faster                                                   |
| pylint                   | 485 ms                                                                | 379 ms: 1.28x faster                                                    |
| pycparser                | 1.69 sec                                                              | 1.34 sec: 1.26x faster                                                  |
| regex_v8                 | 32.2 ms                                                               | 25.7 ms: 1.25x faster                                                   |
| unpickle_pure_python     | 366 us                                                                | 296 us: 1.23x faster                                                    |
| crypto_pyaes             | 134 ms                                                                | 110 ms: 1.22x faster                                                    |
| scimark_lu               | 227 ms                                                                | 186 ms: 1.22x faster                                                    |
| dulwich_log              | 73.5 ms                                                               | 60.3 ms: 1.22x faster                                                   |
| html5lib                 | 86.5 ms                                                               | 70.9 ms: 1.22x faster                                                   |
| pickle_pure_python       | 529 us                                                                | 441 us: 1.20x faster                                                    |
| logging_simple           | 9.78 us                                                               | 8.15 us: 1.20x faster                                                   |
| scimark_monte_carlo      | 128 ms                                                                | 107 ms: 1.20x faster                                                    |
| sqlite_synth             | 4.12 us                                                               | 3.44 us: 1.19x faster                                                   |
| tomli_loads              | 3.36 sec                                                              | 2.82 sec: 1.19x faster                                                  |
| regex_compile            | 177 ms                                                                | 149 ms: 1.19x faster                                                    |
| xml_etree_parse          | 212 ms                                                                | 180 ms: 1.18x faster                                                    |
| coroutines               | 37.2 ms                                                               | 31.6 ms: 1.18x faster                                                   |
| logging_format           | 10.6 us                                                               | 9.10 us: 1.17x faster                                                   |
| xml_etree_iterparse      | 156 ms                                                                | 135 ms: 1.15x faster                                                    |
| pathlib                  | 26.3 ms                                                               | 23.2 ms: 1.13x faster                                                   |
| json_dumps               | 16.7 ms                                                               | 15.0 ms: 1.11x faster                                                   |
| docutils                 | 3.53 sec                                                              | 3.21 sec: 1.10x faster                                                  |
| regex_effbot             | 4.25 ms                                                               | 3.87 ms: 1.10x faster                                                   |
| regex_dna                | 257 ms                                                                | 236 ms: 1.09x faster                                                    |
| 2to3                     | 381 ms                                                                | 349 ms: 1.09x faster                                                    |
| pprint_safe_repr         | 1.15 sec                                                              | 1.05 sec: 1.09x faster                                                  |
| pprint_pformat           | 2.36 sec                                                              | 2.17 sec: 1.09x faster                                                  |
| scimark_fft              | 500 ms                                                                | 470 ms: 1.06x faster                                                    |
| thrift                   | 1.26 ms                                                               | 1.20 ms: 1.05x faster                                                   |
| sympy_integrate          | 26.5 ms                                                               | 25.4 ms: 1.05x faster                                                   |
| deepcopy_reduce          | 4.60 us                                                               | 4.40 us: 1.05x faster                                                   |
| django_template          | 53.3 ms                                                               | 51.0 ms: 1.05x faster                                                   |
| nqueens                  | 117 ms                                                                | 116 ms: 1.01x faster                                                    |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 7.56 ms: 1.01x faster                                                   |
| unpickle_list            | 6.99 us                                                               | 6.95 us: 1.01x faster                                                   |
| asyncio_websockets       | 657 ms                                                                | 669 ms: 1.02x slower                                                    |
| xml_etree_process        | 99.5 ms                                                               | 102 ms: 1.03x slower                                                    |
| sympy_str                | 329 ms                                                                | 339 ms: 1.03x slower                                                    |
| genshi_xml               | 69.8 ms                                                               | 74.6 ms: 1.07x slower                                                   |
| sympy_expand             | 543 ms                                                                | 584 ms: 1.08x slower                                                    |
| json                     | 5.88 ms                                                               | 6.34 ms: 1.08x slower                                                   |
| pickle_list              | 5.24 us                                                               | 5.66 us: 1.08x slower                                                   |
| nbody                    | 166 ms                                                                | 180 ms: 1.08x slower                                                    |
| fannkuch                 | 546 ms                                                                | 598 ms: 1.10x slower                                                    |
| meteor_contest           | 126 ms                                                                | 139 ms: 1.10x slower                                                    |
| pickle_dict              | 35.1 us                                                               | 38.8 us: 1.10x slower                                                   |
| async_generators         | 452 ms                                                                | 506 ms: 1.12x slower                                                    |
| mako                     | 18.9 ms                                                               | 21.3 ms: 1.13x slower                                                   |
| xml_etree_generate       | 123 ms                                                                | 140 ms: 1.14x slower                                                    |
| bench_thread_pool        | 1.59 ms                                                               | 1.82 ms: 1.15x slower                                                   |
| unpickle                 | 17.5 us                                                               | 20.1 us: 1.15x slower                                                   |
| json_loads               | 30.9 us                                                               | 37.0 us: 1.20x slower                                                   |
| pickle                   | 12.5 us                                                               | 15.7 us: 1.26x slower                                                   |
| coverage                 | 83.6 ms                                                               | 144 ms: 1.72x slower                                                    |
| python_startup_no_site   | 6.89 ms                                                               | 12.0 ms: 1.74x slower                                                   |
| python_startup           | 11.2 ms                                                               | 20.0 ms: 1.79x slower                                                   |
| bench_mp_pool            | 14.5 ms                                                               | 66.4 ms: 4.57x slower                                                   |
| telco                    | 8.49 ms                                                               | 189 ms: 22.29x slower                                                   |
| Geometric mean           | (ref)                                                                 | 1.11x faster                                                            |

Benchmark hidden because not significant (4): create_gc_cycles, sympy_sum, pidigits, genshi_text
Ignored benchmarks (13) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20250719-3.15.0a0-800d37f-NOGIL/bm-20250719-arminc-aarch64-python-800d37feca2e0ea33439-3.15.0a0-800d37f.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, unpack_sequence

- Geometric mean (including insignificant results): 1.143x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.10x
- 95% likely to have a speedup of 1.09x
- 99% likely to have a speedup of 1.08x

# Memory
- memory change: 1.67x
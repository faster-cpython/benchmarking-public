# Results vs. 3.10.4

- fork: mdboom
- ref: simplify_richcompare
- machine: linux-aarch64
- commit hash: 6d5be6d
- commit date: 2024-09-03
- overall geometric mean: 1.342x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.23x faster
- Memory change: 1.15x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240903-arminc-aarch64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 296 ms: 1.29x faster                                                    |
| docutils       | 3.53 sec                                                              | 3.01 sec: 1.17x faster                                                  |
| html5lib       | 86.5 ms                                                               | 63.2 ms: 1.37x faster                                                   |
| tornado_http   | 178 ms                                                                | 127 ms: 1.41x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.31x faster                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240903-arminc-aarch64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|-------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none         | 950 ms                                                                | 423 ms: 2.25x faster                                                    |
| async_tree_memoization  | 1.13 sec                                                              | 558 ms: 2.03x faster                                                    |
| async_tree_io           | 2.28 sec                                                              | 1.15 sec: 1.98x faster                                                  |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 727 ms: 1.75x faster                                                    |
| Geometric mean          | (ref)                                                                 | 1.99x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240903-arminc-aarch64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| nbody          | 166 ms                                                                | 108 ms: 1.53x faster                                                    |
| float          | 135 ms                                                                | 92.4 ms: 1.46x faster                                                   |
| Geometric mean | (ref)                                                                 | 1.31x faster                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240903-arminc-aarch64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 125 ms: 1.41x faster                                                    |
| regex_v8       | 32.2 ms                                                               | 30.3 ms: 1.06x faster                                                   |
| regex_dna      | 257 ms                                                                | 253 ms: 1.02x faster                                                    |
| regex_effbot   | 4.25 ms                                                               | 4.89 ms: 1.15x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.07x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240903-arminc-aarch64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pickle_pure_python   | 529 us                                                                | 358 us: 1.48x faster                                                    |
| unpickle_pure_python | 366 us                                                                | 252 us: 1.45x faster                                                    |
| tomli_loads          | 3.36 sec                                                              | 2.64 sec: 1.27x faster                                                  |
| xml_etree_process    | 99.5 ms                                                               | 79.6 ms: 1.25x faster                                                   |
| json_dumps           | 16.7 ms                                                               | 13.5 ms: 1.24x faster                                                   |
| xml_etree_parse      | 212 ms                                                                | 190 ms: 1.11x faster                                                    |
| xml_etree_generate   | 123 ms                                                                | 111 ms: 1.10x faster                                                    |
| xml_etree_iterparse  | 156 ms                                                                | 147 ms: 1.06x faster                                                    |
| json_loads           | 30.9 us                                                               | 32.9 us: 1.06x slower                                                   |
| Geometric mean       | (ref)                                                                 | 1.20x faster                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240903-arminc-aarch64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 11.2 ms                                                               | 13.0 ms: 1.16x slower                                                   |
| python_startup_no_site | 6.89 ms                                                               | 8.77 ms: 1.27x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.22x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240903-arminc-aarch64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 13.4 ms: 1.42x faster                                                   |
| genshi_text     | 35.2 ms                                                               | 27.5 ms: 1.28x faster                                                   |
| django_template | 53.3 ms                                                               | 42.4 ms: 1.26x faster                                                   |
| genshi_xml      | 69.8 ms                                                               | 59.6 ms: 1.17x faster                                                   |
| Geometric mean  | (ref)                                                                 | 1.28x faster                                                            |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240903-arminc-aarch64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|--------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 192 us: 3.44x faster                                                    |
| deltablue                | 8.94 ms                                                               | 3.84 ms: 2.33x faster                                                   |
| async_tree_none          | 950 ms                                                                | 423 ms: 2.25x faster                                                    |
| bench_mp_pool            | 14.5 ms                                                               | 6.94 ms: 2.10x faster                                                   |
| async_tree_memoization   | 1.13 sec                                                              | 558 ms: 2.03x faster                                                    |
| async_tree_io            | 2.28 sec                                                              | 1.15 sec: 1.98x faster                                                  |
| generators               | 68.1 ms                                                               | 34.7 ms: 1.96x faster                                                   |
| go                       | 264 ms                                                                | 136 ms: 1.94x faster                                                    |
| raytrace                 | 573 ms                                                                | 300 ms: 1.91x faster                                                    |
| richards_super           | 107 ms                                                                | 59.7 ms: 1.80x faster                                                   |
| chaos                    | 121 ms                                                                | 68.3 ms: 1.77x faster                                                   |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 727 ms: 1.75x faster                                                    |
| richards                 | 91.7 ms                                                               | 53.3 ms: 1.72x faster                                                   |
| sqlglot_parse            | 2.40 ms                                                               | 1.40 ms: 1.72x faster                                                   |
| scimark_lu               | 227 ms                                                                | 133 ms: 1.71x faster                                                    |
| logging_silent           | 222 ns                                                                | 131 ns: 1.69x faster                                                    |
| asyncio_tcp              | 944 ms                                                                | 568 ms: 1.66x faster                                                    |
| sqlglot_transpile        | 2.84 ms                                                               | 1.73 ms: 1.64x faster                                                   |
| comprehensions           | 33.1 us                                                               | 20.3 us: 1.64x faster                                                   |
| crypto_pyaes             | 134 ms                                                                | 82.1 ms: 1.63x faster                                                   |
| deepcopy_memo            | 61.7 us                                                               | 37.9 us: 1.63x faster                                                   |
| scimark_monte_carlo      | 128 ms                                                                | 80.4 ms: 1.59x faster                                                   |
| scimark_sor              | 246 ms                                                                | 156 ms: 1.58x faster                                                    |
| hexiom                   | 10.9 ms                                                               | 7.02 ms: 1.56x faster                                                   |
| nbody                    | 166 ms                                                                | 108 ms: 1.53x faster                                                    |
| deepcopy                 | 511 us                                                                | 333 us: 1.53x faster                                                    |
| asyncio_tcp_ssl          | 3.28 sec                                                              | 2.20 sec: 1.49x faster                                                  |
| pickle_pure_python       | 529 us                                                                | 358 us: 1.48x faster                                                    |
| float                    | 135 ms                                                                | 92.4 ms: 1.46x faster                                                   |
| unpickle_pure_python     | 366 us                                                                | 252 us: 1.45x faster                                                    |
| mako                     | 18.9 ms                                                               | 13.4 ms: 1.42x faster                                                   |
| regex_compile            | 177 ms                                                                | 125 ms: 1.41x faster                                                    |
| tornado_http             | 178 ms                                                                | 127 ms: 1.41x faster                                                    |
| logging_simple           | 9.78 us                                                               | 7.02 us: 1.39x faster                                                   |
| logging_format           | 10.6 us                                                               | 7.64 us: 1.39x faster                                                   |
| pyflate                  | 795 ms                                                                | 575 ms: 1.38x faster                                                    |
| pycparser                | 1.69 sec                                                              | 1.22 sec: 1.38x faster                                                  |
| html5lib                 | 86.5 ms                                                               | 63.2 ms: 1.37x faster                                                   |
| pylint                   | 485 ms                                                                | 356 ms: 1.36x faster                                                    |
| thrift                   | 1.26 ms                                                               | 947 us: 1.33x faster                                                    |
| deepcopy_reduce          | 4.60 us                                                               | 3.47 us: 1.33x faster                                                   |
| spectral_norm            | 186 ms                                                                | 141 ms: 1.32x faster                                                    |
| sympy_sum                | 184 ms                                                                | 140 ms: 1.31x faster                                                    |
| coroutines               | 37.2 ms                                                               | 28.5 ms: 1.30x faster                                                   |
| 2to3                     | 381 ms                                                                | 296 ms: 1.29x faster                                                    |
| sympy_integrate          | 26.5 ms                                                               | 20.7 ms: 1.29x faster                                                   |
| bench_thread_pool        | 1.59 ms                                                               | 1.24 ms: 1.28x faster                                                   |
| genshi_text              | 35.2 ms                                                               | 27.5 ms: 1.28x faster                                                   |
| tomli_loads              | 3.36 sec                                                              | 2.64 sec: 1.27x faster                                                  |
| pprint_safe_repr         | 1.15 sec                                                              | 907 ms: 1.27x faster                                                    |
| pprint_pformat           | 2.36 sec                                                              | 1.87 sec: 1.26x faster                                                  |
| django_template          | 53.3 ms                                                               | 42.4 ms: 1.26x faster                                                   |
| xml_etree_process        | 99.5 ms                                                               | 79.6 ms: 1.25x faster                                                   |
| pathlib                  | 26.3 ms                                                               | 21.2 ms: 1.24x faster                                                   |
| sympy_str                | 329 ms                                                                | 265 ms: 1.24x faster                                                    |
| json_dumps               | 16.7 ms                                                               | 13.5 ms: 1.24x faster                                                   |
| sqlglot_normalize        | 156 ms                                                                | 127 ms: 1.23x faster                                                    |
| sqlglot_optimize         | 75.4 ms                                                               | 61.8 ms: 1.22x faster                                                   |
| nqueens                  | 117 ms                                                                | 97.4 ms: 1.21x faster                                                   |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 6.39 ms: 1.19x faster                                                   |
| fannkuch                 | 546 ms                                                                | 460 ms: 1.19x faster                                                    |
| sympy_expand             | 543 ms                                                                | 458 ms: 1.18x faster                                                    |
| genshi_xml               | 69.8 ms                                                               | 59.6 ms: 1.17x faster                                                   |
| docutils                 | 3.53 sec                                                              | 3.01 sec: 1.17x faster                                                  |
| meteor_contest           | 126 ms                                                                | 110 ms: 1.14x faster                                                    |
| scimark_fft              | 500 ms                                                                | 446 ms: 1.12x faster                                                    |
| xml_etree_parse          | 212 ms                                                                | 190 ms: 1.11x faster                                                    |
| mdp                      | 3.70 sec                                                              | 3.32 sec: 1.11x faster                                                  |
| xml_etree_generate       | 123 ms                                                                | 111 ms: 1.10x faster                                                    |
| regex_v8                 | 32.2 ms                                                               | 30.3 ms: 1.06x faster                                                   |
| xml_etree_iterparse      | 156 ms                                                                | 147 ms: 1.06x faster                                                    |
| json                     | 5.88 ms                                                               | 5.73 ms: 1.03x faster                                                   |
| regex_dna                | 257 ms                                                                | 253 ms: 1.02x faster                                                    |
| async_generators         | 452 ms                                                                | 479 ms: 1.06x slower                                                    |
| json_loads               | 30.9 us                                                               | 32.9 us: 1.06x slower                                                   |
| regex_effbot             | 4.25 ms                                                               | 4.89 ms: 1.15x slower                                                   |
| telco                    | 8.49 ms                                                               | 9.81 ms: 1.16x slower                                                   |
| python_startup           | 11.2 ms                                                               | 13.0 ms: 1.16x slower                                                   |
| coverage                 | 83.6 ms                                                               | 97.8 ms: 1.17x slower                                                   |
| gc_traversal             | 4.15 ms                                                               | 4.99 ms: 1.20x slower                                                   |
| python_startup_no_site   | 6.89 ms                                                               | 8.77 ms: 1.27x slower                                                   |
| Geometric mean           | (ref)                                                                 | 1.35x faster                                                            |

Benchmark hidden because not significant (3): pidigits, asyncio_websockets, create_gc_cycles
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, chameleon, dask, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240903-3.14.0a0-6d5be6d/bm-20240903-arminc-aarch64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

- Geometric mean (including insignificant results): 1.342x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.26x
- 95% likely to have a speedup of 1.25x
- 99% likely to have a speedup of 1.23x

# Memory
- memory change: 1.15x
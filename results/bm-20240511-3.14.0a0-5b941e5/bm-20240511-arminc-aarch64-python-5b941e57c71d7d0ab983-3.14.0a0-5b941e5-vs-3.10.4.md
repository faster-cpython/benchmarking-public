# Results vs. 3.10.4

- fork: python
- ref: 5b941e57c71d7d0ab983
- machine: linux-aarch64
- commit hash: 5b941e5
- commit date: 2024-05-11
- overall geometric mean: 1.24x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.21x faster
- Memory change: 1.13x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240511-arminc-aarch64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 306 ms: 1.25x faster                                                    |
| chameleon      | 10.8 ms                                                               | 8.99 ms: 1.21x faster                                                   |
| docutils       | 3.53 sec                                                              | 3.09 sec: 1.14x faster                                                  |
| html5lib       | 86.5 ms                                                               | 67.1 ms: 1.29x faster                                                   |
| tornado_http   | 178 ms                                                                | 133 ms: 1.35x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.24x faster                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240511-arminc-aarch64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5 |
|-------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none         | 950 ms                                                                | 487 ms: 1.95x faster                                                    |
| async_tree_io           | 2.28 sec                                                              | 1.23 sec: 1.86x faster                                                  |
| async_tree_memoization  | 1.13 sec                                                              | 644 ms: 1.76x faster                                                    |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 792 ms: 1.61x faster                                                    |
| Geometric mean          | (ref)                                                                 | 1.79x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240511-arminc-aarch64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 135 ms                                                                | 90.2 ms: 1.49x faster                                                   |
| nbody          | 166 ms                                                                | 112 ms: 1.48x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.30x faster                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240511-arminc-aarch64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 130 ms: 1.36x faster                                                    |
| regex_v8       | 32.2 ms                                                               | 30.7 ms: 1.05x faster                                                   |
| regex_dna      | 257 ms                                                                | 254 ms: 1.01x faster                                                    |
| regex_effbot   | 4.25 ms                                                               | 4.93 ms: 1.16x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.06x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240511-arminc-aarch64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5 |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pickle_pure_python   | 529 us                                                                | 360 us: 1.47x faster                                                    |
| unpickle_pure_python | 366 us                                                                | 252 us: 1.45x faster                                                    |
| tomli_loads          | 3.36 sec                                                              | 2.58 sec: 1.30x faster                                                  |
| json_dumps           | 16.7 ms                                                               | 13.3 ms: 1.26x faster                                                   |
| xml_etree_process    | 99.5 ms                                                               | 79.3 ms: 1.26x faster                                                   |
| xml_etree_generate   | 123 ms                                                                | 112 ms: 1.10x faster                                                    |
| xml_etree_parse      | 212 ms                                                                | 194 ms: 1.09x faster                                                    |
| unpickle_list        | 6.99 us                                                               | 6.59 us: 1.06x faster                                                   |
| xml_etree_iterparse  | 156 ms                                                                | 149 ms: 1.05x faster                                                    |
| json_loads           | 30.9 us                                                               | 32.3 us: 1.05x slower                                                   |
| pickle_dict          | 35.1 us                                                               | 37.3 us: 1.06x slower                                                   |
| pickle               | 12.5 us                                                               | 13.8 us: 1.10x slower                                                   |
| unpickle             | 17.5 us                                                               | 19.6 us: 1.12x slower                                                   |
| Geometric mean       | (ref)                                                                 | 1.11x faster                                                            |

Benchmark hidden because not significant (1): pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240511-arminc-aarch64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5 |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 11.2 ms                                                               | 12.5 ms: 1.12x slower                                                   |
| python_startup_no_site | 6.89 ms                                                               | 8.55 ms: 1.24x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.18x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240511-arminc-aarch64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5 |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 13.2 ms: 1.43x faster                                                   |
| django_template | 53.3 ms                                                               | 41.9 ms: 1.27x faster                                                   |
| genshi_text     | 35.2 ms                                                               | 28.0 ms: 1.26x faster                                                   |
| genshi_xml      | 69.8 ms                                                               | 61.0 ms: 1.14x faster                                                   |
| Geometric mean  | (ref)                                                                 | 1.27x faster                                                            |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240511-arminc-aarch64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5 |
|--------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 196 us: 3.37x faster                                                    |
| deltablue                | 8.94 ms                                                               | 3.85 ms: 2.32x faster                                                   |
| bench_mp_pool            | 14.5 ms                                                               | 7.14 ms: 2.04x faster                                                   |
| async_tree_none          | 950 ms                                                                | 487 ms: 1.95x faster                                                    |
| raytrace                 | 573 ms                                                                | 296 ms: 1.94x faster                                                    |
| async_tree_io            | 2.28 sec                                                              | 1.23 sec: 1.86x faster                                                  |
| chaos                    | 121 ms                                                                | 67.8 ms: 1.79x faster                                                   |
| richards_super           | 107 ms                                                                | 60.3 ms: 1.78x faster                                                   |
| async_tree_memoization   | 1.13 sec                                                              | 644 ms: 1.76x faster                                                    |
| generators               | 68.1 ms                                                               | 39.3 ms: 1.73x faster                                                   |
| sqlglot_parse            | 2.40 ms                                                               | 1.40 ms: 1.72x faster                                                   |
| richards                 | 91.7 ms                                                               | 53.4 ms: 1.72x faster                                                   |
| logging_silent           | 222 ns                                                                | 134 ns: 1.66x faster                                                    |
| scimark_lu               | 227 ms                                                                | 138 ms: 1.64x faster                                                    |
| asyncio_tcp              | 944 ms                                                                | 576 ms: 1.64x faster                                                    |
| crypto_pyaes             | 134 ms                                                                | 81.9 ms: 1.64x faster                                                   |
| go                       | 264 ms                                                                | 161 ms: 1.64x faster                                                    |
| sqlglot_transpile        | 2.84 ms                                                               | 1.75 ms: 1.62x faster                                                   |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 792 ms: 1.61x faster                                                    |
| comprehensions           | 33.1 us                                                               | 20.9 us: 1.59x faster                                                   |
| scimark_sor              | 246 ms                                                                | 158 ms: 1.56x faster                                                    |
| hexiom                   | 10.9 ms                                                               | 7.11 ms: 1.53x faster                                                   |
| scimark_monte_carlo      | 128 ms                                                                | 83.9 ms: 1.52x faster                                                   |
| float                    | 135 ms                                                                | 90.2 ms: 1.49x faster                                                   |
| asyncio_tcp_ssl          | 3.28 sec                                                              | 2.21 sec: 1.49x faster                                                  |
| nbody                    | 166 ms                                                                | 112 ms: 1.48x faster                                                    |
| pickle_pure_python       | 529 us                                                                | 360 us: 1.47x faster                                                    |
| unpickle_pure_python     | 366 us                                                                | 252 us: 1.45x faster                                                    |
| mako                     | 18.9 ms                                                               | 13.2 ms: 1.43x faster                                                   |
| pylint                   | 485 ms                                                                | 343 ms: 1.41x faster                                                    |
| pycparser                | 1.69 sec                                                              | 1.22 sec: 1.39x faster                                                  |
| logging_simple           | 9.78 us                                                               | 7.15 us: 1.37x faster                                                   |
| pyflate                  | 795 ms                                                                | 581 ms: 1.37x faster                                                    |
| logging_format           | 10.6 us                                                               | 7.76 us: 1.37x faster                                                   |
| regex_compile            | 177 ms                                                                | 130 ms: 1.36x faster                                                    |
| tornado_http             | 178 ms                                                                | 133 ms: 1.35x faster                                                    |
| thrift                   | 1.26 ms                                                               | 952 us: 1.32x faster                                                    |
| spectral_norm            | 186 ms                                                                | 141 ms: 1.32x faster                                                    |
| tomli_loads              | 3.36 sec                                                              | 2.58 sec: 1.30x faster                                                  |
| html5lib                 | 86.5 ms                                                               | 67.1 ms: 1.29x faster                                                   |
| coroutines               | 37.2 ms                                                               | 29.2 ms: 1.27x faster                                                   |
| django_template          | 53.3 ms                                                               | 41.9 ms: 1.27x faster                                                   |
| json_dumps               | 16.7 ms                                                               | 13.3 ms: 1.26x faster                                                   |
| genshi_text              | 35.2 ms                                                               | 28.0 ms: 1.26x faster                                                   |
| xml_etree_process        | 99.5 ms                                                               | 79.3 ms: 1.26x faster                                                   |
| 2to3                     | 381 ms                                                                | 306 ms: 1.25x faster                                                    |
| bench_thread_pool        | 1.59 ms                                                               | 1.28 ms: 1.24x faster                                                   |
| sympy_sum                | 184 ms                                                                | 149 ms: 1.24x faster                                                    |
| sympy_integrate          | 26.5 ms                                                               | 21.6 ms: 1.23x faster                                                   |
| pprint_pformat           | 2.36 sec                                                              | 1.92 sec: 1.23x faster                                                  |
| sympy_str                | 329 ms                                                                | 269 ms: 1.22x faster                                                    |
| pprint_safe_repr         | 1.15 sec                                                              | 941 ms: 1.22x faster                                                    |
| sqlglot_normalize        | 156 ms                                                                | 129 ms: 1.21x faster                                                    |
| chameleon                | 10.8 ms                                                               | 8.99 ms: 1.21x faster                                                   |
| sqlglot_optimize         | 75.4 ms                                                               | 62.6 ms: 1.20x faster                                                   |
| deepcopy_memo            | 61.7 us                                                               | 51.4 us: 1.20x faster                                                   |
| nqueens                  | 117 ms                                                                | 98.0 ms: 1.20x faster                                                   |
| dulwich_log              | 73.5 ms                                                               | 61.4 ms: 1.20x faster                                                   |
| fannkuch                 | 546 ms                                                                | 461 ms: 1.18x faster                                                    |
| sympy_expand             | 543 ms                                                                | 459 ms: 1.18x faster                                                    |
| dask                     | 450 ms                                                                | 384 ms: 1.17x faster                                                    |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 6.58 ms: 1.16x faster                                                   |
| genshi_xml               | 69.8 ms                                                               | 61.0 ms: 1.14x faster                                                   |
| docutils                 | 3.53 sec                                                              | 3.09 sec: 1.14x faster                                                  |
| pathlib                  | 26.3 ms                                                               | 23.1 ms: 1.14x faster                                                   |
| scimark_fft              | 500 ms                                                                | 444 ms: 1.13x faster                                                    |
| deepcopy                 | 511 us                                                                | 454 us: 1.12x faster                                                    |
| meteor_contest           | 126 ms                                                                | 113 ms: 1.12x faster                                                    |
| deepcopy_reduce          | 4.60 us                                                               | 4.15 us: 1.11x faster                                                   |
| mdp                      | 3.70 sec                                                              | 3.35 sec: 1.10x faster                                                  |
| xml_etree_generate       | 123 ms                                                                | 112 ms: 1.10x faster                                                    |
| xml_etree_parse          | 212 ms                                                                | 194 ms: 1.09x faster                                                    |
| unpickle_list            | 6.99 us                                                               | 6.59 us: 1.06x faster                                                   |
| sqlite_synth             | 4.12 us                                                               | 3.90 us: 1.06x faster                                                   |
| regex_v8                 | 32.2 ms                                                               | 30.7 ms: 1.05x faster                                                   |
| xml_etree_iterparse      | 156 ms                                                                | 149 ms: 1.05x faster                                                    |
| json                     | 5.88 ms                                                               | 5.67 ms: 1.04x faster                                                   |
| regex_dna                | 257 ms                                                                | 254 ms: 1.01x faster                                                    |
| asyncio_websockets       | 657 ms                                                                | 663 ms: 1.01x slower                                                    |
| json_loads               | 30.9 us                                                               | 32.3 us: 1.05x slower                                                   |
| create_gc_cycles         | 2.26 ms                                                               | 2.40 ms: 1.06x slower                                                   |
| pickle_dict              | 35.1 us                                                               | 37.3 us: 1.06x slower                                                   |
| async_generators         | 452 ms                                                                | 489 ms: 1.08x slower                                                    |
| pickle                   | 12.5 us                                                               | 13.8 us: 1.10x slower                                                   |
| python_startup           | 11.2 ms                                                               | 12.5 ms: 1.12x slower                                                   |
| unpickle                 | 17.5 us                                                               | 19.6 us: 1.12x slower                                                   |
| regex_effbot             | 4.25 ms                                                               | 4.93 ms: 1.16x slower                                                   |
| coverage                 | 83.6 ms                                                               | 97.5 ms: 1.17x slower                                                   |
| gc_traversal             | 4.15 ms                                                               | 5.14 ms: 1.24x slower                                                   |
| python_startup_no_site   | 6.89 ms                                                               | 8.55 ms: 1.24x slower                                                   |
| telco                    | 8.49 ms                                                               | 164 ms: 19.29x slower                                                   |
| Geometric mean           | (ref)                                                                 | 1.24x faster                                                            |

Benchmark hidden because not significant (3): pickle_list, pidigits, flaskblogging
Ignored benchmarks (5) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (4) of results/bm-20240511-3.14.0a0-5b941e5/bm-20240511-arminc-aarch64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.23x
- 95% likely to have a speedup of 1.22x
- 99% likely to have a speedup of 1.21x

# Memory
- memory change: 1.13x
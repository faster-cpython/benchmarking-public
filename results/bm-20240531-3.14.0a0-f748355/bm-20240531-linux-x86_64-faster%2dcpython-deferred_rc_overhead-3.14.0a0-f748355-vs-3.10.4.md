# Results vs. 3.10.4

- fork: faster-cpython
- ref: deferred_rc_overhead
- machine: linux-x86_64
- commit hash: f748355
- commit date: 2024-05-31
- overall geometric mean: 1.34x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.27x faster
- Memory change: 1.11x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240531-linux-x86_64-faster%2dcpython-deferred_rc_overhead-3.14.0a0-f748355 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 270 ms: 1.29x faster                                                            |
| docutils       | 3.30 sec                                               | 2.79 sec: 1.18x faster                                                          |
| html5lib       | 88.9 ms                                                | 67.4 ms: 1.32x faster                                                           |
| tornado_http   | 136 ms                                                 | 93.9 ms: 1.45x faster                                                           |
| Geometric mean | (ref)                                                  | 1.31x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240531-linux-x86_64-faster%2dcpython-deferred_rc_overhead-3.14.0a0-f748355 |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 388 ms: 1.88x faster                                                            |
| async_tree_io           | 1.77 sec                                               | 947 ms: 1.87x faster                                                            |
| async_tree_memoization  | 870 ms                                                 | 468 ms: 1.86x faster                                                            |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 621 ms: 1.64x faster                                                            |
| Geometric mean          | (ref)                                                  | 1.81x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240531-linux-x86_64-faster%2dcpython-deferred_rc_overhead-3.14.0a0-f748355 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 89.1 ms: 1.72x faster                                                           |
| float          | 117 ms                                                 | 79.5 ms: 1.47x faster                                                           |
| pidigits       | 191 ms                                                 | 189 ms: 1.01x faster                                                            |
| Geometric mean | (ref)                                                  | 1.37x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240531-linux-x86_64-faster%2dcpython-deferred_rc_overhead-3.14.0a0-f748355 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 134 ms: 1.41x faster                                                            |
| regex_v8       | 27.8 ms                                                | 26.0 ms: 1.07x faster                                                           |
| regex_dna      | 227 ms                                                 | 228 ms: 1.00x slower                                                            |
| Geometric mean | (ref)                                                  | 1.11x faster                                                                    |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240531-linux-x86_64-faster%2dcpython-deferred_rc_overhead-3.14.0a0-f748355 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pickle_pure_python   | 484 us                                                 | 303 us: 1.60x faster                                                            |
| unpickle_pure_python | 331 us                                                 | 218 us: 1.51x faster                                                            |
| tomli_loads          | 3.14 sec                                               | 2.18 sec: 1.44x faster                                                          |
| json_dumps           | 14.2 ms                                                | 10.6 ms: 1.34x faster                                                           |
| xml_etree_process    | 79.1 ms                                                | 60.3 ms: 1.31x faster                                                           |
| xml_etree_generate   | 99.4 ms                                                | 87.1 ms: 1.14x faster                                                           |
| json_loads           | 31.2 us                                                | 28.8 us: 1.09x faster                                                           |
| xml_etree_iterparse  | 115 ms                                                 | 106 ms: 1.08x faster                                                            |
| xml_etree_parse      | 168 ms                                                 | 160 ms: 1.05x faster                                                            |
| unpickle_list        | 5.20 us                                                | 5.41 us: 1.04x slower                                                           |
| pickle_list          | 5.08 us                                                | 5.30 us: 1.04x slower                                                           |
| unpickle             | 14.4 us                                                | 15.5 us: 1.08x slower                                                           |
| pickle               | 10.7 us                                                | 12.0 us: 1.13x slower                                                           |
| pickle_dict          | 29.6 us                                                | 35.9 us: 1.21x slower                                                           |
| Geometric mean       | (ref)                                                  | 1.13x faster                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240531-linux-x86_64-faster%2dcpython-deferred_rc_overhead-3.14.0a0-f748355 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.5 ms: 1.38x faster                                                           |
| python_startup_no_site | 5.93 ms                                                | 7.07 ms: 1.19x slower                                                           |
| Geometric mean         | (ref)                                                  | 1.08x faster                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240531-linux-x86_64-faster%2dcpython-deferred_rc_overhead-3.14.0a0-f748355 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 11.7 ms: 1.40x faster                                                           |
| genshi_text     | 31.8 ms                                                | 23.3 ms: 1.37x faster                                                           |
| django_template | 48.2 ms                                                | 35.3 ms: 1.36x faster                                                           |
| genshi_xml      | 66.0 ms                                                | 50.6 ms: 1.31x faster                                                           |
| Geometric mean  | (ref)                                                  | 1.36x faster                                                                    |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240531-linux-x86_64-faster%2dcpython-deferred_rc_overhead-3.14.0a0-f748355 |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 165 us: 3.29x faster                                                            |
| generators               | 80.1 ms                                                | 27.8 ms: 2.88x faster                                                           |
| deltablue                | 7.91 ms                                                | 3.27 ms: 2.42x faster                                                           |
| logging_silent           | 190 ns                                                 | 97.2 ns: 1.95x faster                                                           |
| raytrace                 | 507 ms                                                 | 265 ms: 1.91x faster                                                            |
| chaos                    | 115 ms                                                 | 60.9 ms: 1.90x faster                                                           |
| async_tree_none          | 728 ms                                                 | 388 ms: 1.88x faster                                                            |
| async_tree_io            | 1.77 sec                                               | 947 ms: 1.87x faster                                                            |
| async_tree_memoization   | 870 ms                                                 | 468 ms: 1.86x faster                                                            |
| asyncio_tcp              | 922 ms                                                 | 505 ms: 1.83x faster                                                            |
| scimark_sor              | 220 ms                                                 | 126 ms: 1.75x faster                                                            |
| pylint                   | 551 ms                                                 | 316 ms: 1.74x faster                                                            |
| nbody                    | 154 ms                                                 | 89.1 ms: 1.72x faster                                                           |
| richards_super           | 94.7 ms                                                | 55.2 ms: 1.72x faster                                                           |
| comprehensions           | 28.8 us                                                | 16.8 us: 1.71x faster                                                           |
| scimark_monte_carlo      | 118 ms                                                 | 70.1 ms: 1.69x faster                                                           |
| crypto_pyaes             | 128 ms                                                 | 75.9 ms: 1.68x faster                                                           |
| hexiom                   | 10.4 ms                                                | 6.21 ms: 1.67x faster                                                           |
| sqlglot_parse            | 2.17 ms                                                | 1.32 ms: 1.65x faster                                                           |
| go                       | 240 ms                                                 | 146 ms: 1.64x faster                                                            |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 621 ms: 1.64x faster                                                            |
| richards                 | 79.3 ms                                                | 49.1 ms: 1.61x faster                                                           |
| pickle_pure_python       | 484 us                                                 | 303 us: 1.60x faster                                                            |
| sqlglot_transpile        | 2.57 ms                                                | 1.62 ms: 1.59x faster                                                           |
| coroutines               | 35.1 ms                                                | 22.6 ms: 1.55x faster                                                           |
| pyflate                  | 716 ms                                                 | 467 ms: 1.53x faster                                                            |
| scimark_lu               | 176 ms                                                 | 116 ms: 1.52x faster                                                            |
| unpickle_pure_python     | 331 us                                                 | 218 us: 1.51x faster                                                            |
| deepcopy_memo            | 58.5 us                                                | 39.3 us: 1.49x faster                                                           |
| float                    | 117 ms                                                 | 79.5 ms: 1.47x faster                                                           |
| logging_simple           | 8.30 us                                                | 5.68 us: 1.46x faster                                                           |
| spectral_norm            | 170 ms                                                 | 116 ms: 1.46x faster                                                            |
| tornado_http             | 136 ms                                                 | 93.9 ms: 1.45x faster                                                           |
| tomli_loads              | 3.14 sec                                               | 2.18 sec: 1.44x faster                                                          |
| logging_format           | 9.09 us                                                | 6.31 us: 1.44x faster                                                           |
| regex_compile            | 188 ms                                                 | 134 ms: 1.41x faster                                                            |
| mako                     | 16.3 ms                                                | 11.7 ms: 1.40x faster                                                           |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.84 sec: 1.40x faster                                                          |
| python_startup           | 14.6 ms                                                | 10.5 ms: 1.38x faster                                                           |
| genshi_text              | 31.8 ms                                                | 23.3 ms: 1.37x faster                                                           |
| pprint_pformat           | 2.10 sec                                               | 1.54 sec: 1.36x faster                                                          |
| django_template          | 48.2 ms                                                | 35.3 ms: 1.36x faster                                                           |
| pprint_safe_repr         | 1.02 sec                                               | 752 ms: 1.35x faster                                                            |
| thrift                   | 1.07 ms                                                | 801 us: 1.34x faster                                                            |
| json_dumps               | 14.2 ms                                                | 10.6 ms: 1.34x faster                                                           |
| html5lib                 | 88.9 ms                                                | 67.4 ms: 1.32x faster                                                           |
| xml_etree_process        | 79.1 ms                                                | 60.3 ms: 1.31x faster                                                           |
| fannkuch                 | 532 ms                                                 | 406 ms: 1.31x faster                                                            |
| deepcopy                 | 479 us                                                 | 366 us: 1.31x faster                                                            |
| genshi_xml               | 66.0 ms                                                | 50.6 ms: 1.31x faster                                                           |
| pycparser                | 1.58 sec                                               | 1.21 sec: 1.30x faster                                                          |
| sqlglot_normalize        | 143 ms                                                 | 110 ms: 1.30x faster                                                            |
| 2to3                     | 348 ms                                                 | 270 ms: 1.29x faster                                                            |
| nqueens                  | 106 ms                                                 | 82.4 ms: 1.28x faster                                                           |
| dulwich_log              | 84.3 ms                                                | 65.8 ms: 1.28x faster                                                           |
| sympy_sum                | 196 ms                                                 | 155 ms: 1.27x faster                                                            |
| sympy_integrate          | 25.8 ms                                                | 20.4 ms: 1.27x faster                                                           |
| deepcopy_reduce          | 4.17 us                                                | 3.31 us: 1.26x faster                                                           |
| pathlib                  | 20.5 ms                                                | 16.2 ms: 1.26x faster                                                           |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 5.15 ms: 1.26x faster                                                           |
| sqlglot_optimize         | 69.2 ms                                                | 55.1 ms: 1.25x faster                                                           |
| scimark_fft              | 466 ms                                                 | 374 ms: 1.25x faster                                                            |
| sympy_str                | 346 ms                                                 | 280 ms: 1.23x faster                                                            |
| sympy_expand             | 566 ms                                                 | 469 ms: 1.21x faster                                                            |
| bench_thread_pool        | 986 us                                                 | 830 us: 1.19x faster                                                            |
| docutils                 | 3.30 sec                                               | 2.79 sec: 1.18x faster                                                          |
| xml_etree_generate       | 99.4 ms                                                | 87.1 ms: 1.14x faster                                                           |
| mdp                      | 2.85 sec                                               | 2.58 sec: 1.10x faster                                                          |
| json_loads               | 31.2 us                                                | 28.8 us: 1.09x faster                                                           |
| xml_etree_iterparse      | 115 ms                                                 | 106 ms: 1.08x faster                                                            |
| meteor_contest           | 120 ms                                                 | 111 ms: 1.08x faster                                                            |
| json                     | 5.69 ms                                                | 5.31 ms: 1.07x faster                                                           |
| regex_v8                 | 27.8 ms                                                | 26.0 ms: 1.07x faster                                                           |
| xml_etree_parse          | 168 ms                                                 | 160 ms: 1.05x faster                                                            |
| sqlite_synth             | 3.02 us                                                | 2.95 us: 1.02x faster                                                           |
| pidigits                 | 191 ms                                                 | 189 ms: 1.01x faster                                                            |
| gc_traversal             | 3.62 ms                                                | 3.59 ms: 1.01x faster                                                           |
| bench_mp_pool            | 24.0 ms                                                | 23.9 ms: 1.00x faster                                                           |
| regex_dna                | 227 ms                                                 | 228 ms: 1.00x slower                                                            |
| async_generators         | 444 ms                                                 | 447 ms: 1.01x slower                                                            |
| asyncio_websockets       | 559 ms                                                 | 566 ms: 1.01x slower                                                            |
| unpickle_list            | 5.20 us                                                | 5.41 us: 1.04x slower                                                           |
| pickle_list              | 5.08 us                                                | 5.30 us: 1.04x slower                                                           |
| unpickle                 | 14.4 us                                                | 15.5 us: 1.08x slower                                                           |
| create_gc_cycles         | 1.62 ms                                                | 1.78 ms: 1.10x slower                                                           |
| pickle                   | 10.7 us                                                | 12.0 us: 1.13x slower                                                           |
| coverage                 | 79.4 ms                                                | 92.3 ms: 1.16x slower                                                           |
| telco                    | 7.27 ms                                                | 8.45 ms: 1.16x slower                                                           |
| python_startup_no_site   | 5.93 ms                                                | 7.07 ms: 1.19x slower                                                           |
| pickle_dict              | 29.6 us                                                | 35.9 us: 1.21x slower                                                           |
| Geometric mean           | (ref)                                                  | 1.34x faster                                                                    |

Benchmark hidden because not significant (1): regex_effbot
Ignored benchmarks (10) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (4) of results/bm-20240531-3.14.0a0-f748355/bm-20240531-linux-x86_64-faster%2dcpython-deferred_rc_overhead-3.14.0a0-f748355.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.29x
- 95% likely to have a speedup of 1.28x
- 99% likely to have a speedup of 1.27x

# Memory
- memory change: 1.11x
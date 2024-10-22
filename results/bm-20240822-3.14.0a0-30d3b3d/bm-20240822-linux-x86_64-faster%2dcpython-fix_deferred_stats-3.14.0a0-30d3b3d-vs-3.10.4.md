# Results vs. 3.10.4

- fork: faster-cpython
- ref: fix_deferred_stats
- machine: linux-x86_64
- commit hash: 30d3b3d
- commit date: 2024-08-22
- overall geometric mean: 1.43x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.32x faster
- Memory change: 1.12x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240822-linux-x86_64-faster%2dcpython-fix_deferred_stats-3.14.0a0-30d3b3d |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 263 ms: 1.33x faster                                                          |
| docutils       | 3.30 sec                                               | 2.69 sec: 1.23x faster                                                        |
| html5lib       | 88.9 ms                                                | 63.9 ms: 1.39x faster                                                         |
| tornado_http   | 136 ms                                                 | 90.1 ms: 1.51x faster                                                         |
| Geometric mean | (ref)                                                  | 1.36x faster                                                                  |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240822-linux-x86_64-faster%2dcpython-fix_deferred_stats-3.14.0a0-30d3b3d |
|-------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 323 ms: 2.25x faster                                                          |
| async_tree_memoization  | 870 ms                                                 | 391 ms: 2.23x faster                                                          |
| async_tree_io           | 1.77 sec                                               | 931 ms: 1.90x faster                                                          |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 553 ms: 1.84x faster                                                          |
| Geometric mean          | (ref)                                                  | 2.05x faster                                                                  |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240822-linux-x86_64-faster%2dcpython-fix_deferred_stats-3.14.0a0-30d3b3d |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 85.8 ms: 1.79x faster                                                         |
| float          | 117 ms                                                 | 79.1 ms: 1.48x faster                                                         |
| pidigits       | 191 ms                                                 | 186 ms: 1.02x faster                                                          |
| Geometric mean | (ref)                                                  | 1.39x faster                                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240822-linux-x86_64-faster%2dcpython-fix_deferred_stats-3.14.0a0-30d3b3d |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 129 ms: 1.46x faster                                                          |
| regex_v8       | 27.8 ms                                                | 23.7 ms: 1.17x faster                                                         |
| regex_dna      | 227 ms                                                 | 225 ms: 1.01x faster                                                          |
| regex_effbot   | 3.63 ms                                                | 3.76 ms: 1.04x slower                                                         |
| Geometric mean | (ref)                                                  | 1.14x faster                                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240822-linux-x86_64-faster%2dcpython-fix_deferred_stats-3.14.0a0-30d3b3d |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| pickle_pure_python   | 484 us                                                 | 304 us: 1.60x faster                                                          |
| tomli_loads          | 3.14 sec                                               | 2.04 sec: 1.54x faster                                                        |
| unpickle_pure_python | 331 us                                                 | 215 us: 1.53x faster                                                          |
| json_dumps           | 14.2 ms                                                | 10.5 ms: 1.34x faster                                                         |
| xml_etree_process    | 79.1 ms                                                | 59.7 ms: 1.32x faster                                                         |
| xml_etree_generate   | 99.4 ms                                                | 86.2 ms: 1.15x faster                                                         |
| xml_etree_iterparse  | 115 ms                                                 | 105 ms: 1.10x faster                                                          |
| json_loads           | 31.2 us                                                | 28.5 us: 1.09x faster                                                         |
| xml_etree_parse      | 168 ms                                                 | 154 ms: 1.09x faster                                                          |
| Geometric mean       | (ref)                                                  | 1.29x faster                                                                  |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240822-linux-x86_64-faster%2dcpython-fix_deferred_stats-3.14.0a0-30d3b3d |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.5 ms: 1.39x faster                                                         |
| python_startup_no_site | 5.93 ms                                                | 7.07 ms: 1.19x slower                                                         |
| Geometric mean         | (ref)                                                  | 1.08x faster                                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240822-linux-x86_64-faster%2dcpython-fix_deferred_stats-3.14.0a0-30d3b3d |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 11.2 ms: 1.46x faster                                                         |
| django_template | 48.2 ms                                                | 33.7 ms: 1.43x faster                                                         |
| genshi_text     | 31.8 ms                                                | 22.6 ms: 1.41x faster                                                         |
| genshi_xml      | 66.0 ms                                                | 49.9 ms: 1.32x faster                                                         |
| Geometric mean  | (ref)                                                  | 1.40x faster                                                                  |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240822-linux-x86_64-faster%2dcpython-fix_deferred_stats-3.14.0a0-30d3b3d |
|--------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 164 us: 3.32x faster                                                          |
| generators               | 80.1 ms                                                | 27.6 ms: 2.90x faster                                                         |
| deltablue                | 7.91 ms                                                | 3.23 ms: 2.45x faster                                                         |
| async_tree_none          | 728 ms                                                 | 323 ms: 2.25x faster                                                          |
| async_tree_memoization   | 870 ms                                                 | 391 ms: 2.23x faster                                                          |
| chaos                    | 115 ms                                                 | 59.1 ms: 1.95x faster                                                         |
| deepcopy_memo            | 58.5 us                                                | 30.1 us: 1.94x faster                                                         |
| raytrace                 | 507 ms                                                 | 265 ms: 1.91x faster                                                          |
| asyncio_tcp              | 922 ms                                                 | 484 ms: 1.91x faster                                                          |
| async_tree_io            | 1.77 sec                                               | 931 ms: 1.90x faster                                                          |
| logging_silent           | 190 ns                                                 | 103 ns: 1.84x faster                                                          |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 553 ms: 1.84x faster                                                          |
| deepcopy                 | 479 us                                                 | 263 us: 1.82x faster                                                          |
| richards_super           | 94.7 ms                                                | 52.0 ms: 1.82x faster                                                         |
| nbody                    | 154 ms                                                 | 85.8 ms: 1.79x faster                                                         |
| crypto_pyaes             | 128 ms                                                 | 72.1 ms: 1.77x faster                                                         |
| comprehensions           | 28.8 us                                                | 16.5 us: 1.74x faster                                                         |
| scimark_monte_carlo      | 118 ms                                                 | 68.3 ms: 1.73x faster                                                         |
| pylint                   | 551 ms                                                 | 320 ms: 1.72x faster                                                          |
| richards                 | 79.3 ms                                                | 46.1 ms: 1.72x faster                                                         |
| scimark_sor              | 220 ms                                                 | 128 ms: 1.71x faster                                                          |
| sqlglot_parse            | 2.17 ms                                                | 1.29 ms: 1.69x faster                                                         |
| hexiom                   | 10.4 ms                                                | 6.18 ms: 1.68x faster                                                         |
| go                       | 240 ms                                                 | 143 ms: 1.67x faster                                                          |
| sqlglot_transpile        | 2.57 ms                                                | 1.58 ms: 1.62x faster                                                         |
| pickle_pure_python       | 484 us                                                 | 304 us: 1.60x faster                                                          |
| deepcopy_reduce          | 4.17 us                                                | 2.69 us: 1.55x faster                                                         |
| scimark_lu               | 176 ms                                                 | 114 ms: 1.55x faster                                                          |
| tomli_loads              | 3.14 sec                                               | 2.04 sec: 1.54x faster                                                        |
| unpickle_pure_python     | 331 us                                                 | 215 us: 1.53x faster                                                          |
| spectral_norm            | 170 ms                                                 | 111 ms: 1.53x faster                                                          |
| tornado_http             | 136 ms                                                 | 90.1 ms: 1.51x faster                                                         |
| pyflate                  | 716 ms                                                 | 474 ms: 1.51x faster                                                          |
| logging_simple           | 8.30 us                                                | 5.51 us: 1.51x faster                                                         |
| coroutines               | 35.1 ms                                                | 23.4 ms: 1.50x faster                                                         |
| logging_format           | 9.09 us                                                | 6.10 us: 1.49x faster                                                         |
| float                    | 117 ms                                                 | 79.1 ms: 1.48x faster                                                         |
| regex_compile            | 188 ms                                                 | 129 ms: 1.46x faster                                                          |
| mako                     | 16.3 ms                                                | 11.2 ms: 1.46x faster                                                         |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.79 sec: 1.43x faster                                                        |
| django_template          | 48.2 ms                                                | 33.7 ms: 1.43x faster                                                         |
| genshi_text              | 31.8 ms                                                | 22.6 ms: 1.41x faster                                                         |
| thrift                   | 1.07 ms                                                | 766 us: 1.40x faster                                                          |
| html5lib                 | 88.9 ms                                                | 63.9 ms: 1.39x faster                                                         |
| python_startup           | 14.6 ms                                                | 10.5 ms: 1.39x faster                                                         |
| pycparser                | 1.58 sec                                               | 1.14 sec: 1.38x faster                                                        |
| pprint_pformat           | 2.10 sec                                               | 1.53 sec: 1.37x faster                                                        |
| pprint_safe_repr         | 1.02 sec                                               | 751 ms: 1.35x faster                                                          |
| json_dumps               | 14.2 ms                                                | 10.5 ms: 1.34x faster                                                         |
| sqlglot_normalize        | 143 ms                                                 | 107 ms: 1.34x faster                                                          |
| sympy_sum                | 196 ms                                                 | 147 ms: 1.33x faster                                                          |
| fannkuch                 | 532 ms                                                 | 399 ms: 1.33x faster                                                          |
| nqueens                  | 106 ms                                                 | 79.6 ms: 1.33x faster                                                         |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.87 ms: 1.33x faster                                                         |
| 2to3                     | 348 ms                                                 | 263 ms: 1.33x faster                                                          |
| xml_etree_process        | 79.1 ms                                                | 59.7 ms: 1.32x faster                                                         |
| scimark_fft              | 466 ms                                                 | 352 ms: 1.32x faster                                                          |
| genshi_xml               | 66.0 ms                                                | 49.9 ms: 1.32x faster                                                         |
| sympy_integrate          | 25.8 ms                                                | 19.6 ms: 1.32x faster                                                         |
| sympy_str                | 346 ms                                                 | 267 ms: 1.29x faster                                                          |
| sqlglot_optimize         | 69.2 ms                                                | 53.6 ms: 1.29x faster                                                         |
| pathlib                  | 20.5 ms                                                | 16.3 ms: 1.26x faster                                                         |
| bench_thread_pool        | 986 us                                                 | 786 us: 1.26x faster                                                          |
| sympy_expand             | 566 ms                                                 | 456 ms: 1.24x faster                                                          |
| docutils                 | 3.30 sec                                               | 2.69 sec: 1.23x faster                                                        |
| regex_v8                 | 27.8 ms                                                | 23.7 ms: 1.17x faster                                                         |
| xml_etree_generate       | 99.4 ms                                                | 86.2 ms: 1.15x faster                                                         |
| meteor_contest           | 120 ms                                                 | 107 ms: 1.11x faster                                                          |
| xml_etree_iterparse      | 115 ms                                                 | 105 ms: 1.10x faster                                                          |
| json_loads               | 31.2 us                                                | 28.5 us: 1.09x faster                                                         |
| xml_etree_parse          | 168 ms                                                 | 154 ms: 1.09x faster                                                          |
| json                     | 5.69 ms                                                | 5.39 ms: 1.06x faster                                                         |
| mdp                      | 2.85 sec                                               | 2.73 sec: 1.04x faster                                                        |
| pidigits                 | 191 ms                                                 | 186 ms: 1.02x faster                                                          |
| async_generators         | 444 ms                                                 | 435 ms: 1.02x faster                                                          |
| regex_dna                | 227 ms                                                 | 225 ms: 1.01x faster                                                          |
| gc_traversal             | 3.62 ms                                                | 3.64 ms: 1.00x slower                                                         |
| regex_effbot             | 3.63 ms                                                | 3.76 ms: 1.04x slower                                                         |
| coverage                 | 79.4 ms                                                | 85.2 ms: 1.07x slower                                                         |
| create_gc_cycles         | 1.62 ms                                                | 1.75 ms: 1.08x slower                                                         |
| telco                    | 7.27 ms                                                | 8.15 ms: 1.12x slower                                                         |
| python_startup_no_site   | 5.93 ms                                                | 7.07 ms: 1.19x slower                                                         |
| Geometric mean           | (ref)                                                  | 1.43x faster                                                                  |

Benchmark hidden because not significant (2): asyncio_websockets, bench_mp_pool
Ignored benchmarks (17) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240822-3.14.0a0-30d3b3d/bm-20240822-linux-x86_64-faster%2dcpython-fix_deferred_stats-3.14.0a0-30d3b3d.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.34x
- 95% likely to have a speedup of 1.33x
- 99% likely to have a speedup of 1.32x

# Memory
- memory change: 1.12x
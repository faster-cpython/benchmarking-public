# Results vs. 3.10.4

- fork: faster-cpython
- ref: tier2_hot_cold_split
- machine: linux-x86_64
- commit hash: 37627d3
- commit date: 2024-03-25
- overall geometric mean: 1.31x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.21x faster
- Memory change: 1.18x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240325-linux-x86_64-faster%2dcpython-tier2_hot_cold_split-3.13.0a5+-37627d3 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 278 ms: 1.26x faster                                                             |
| chameleon      | 9.68 ms                                                | 7.14 ms: 1.36x faster                                                            |
| docutils       | 3.30 sec                                               | 2.88 sec: 1.14x faster                                                           |
| html5lib       | 88.9 ms                                                | 67.7 ms: 1.31x faster                                                            |
| tornado_http   | 136 ms                                                 | 96.8 ms: 1.41x faster                                                            |
| Geometric mean | (ref)                                                  | 1.29x faster                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240325-linux-x86_64-faster%2dcpython-tier2_hot_cold_split-3.13.0a5+-37627d3 |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 375 ms: 1.94x faster                                                             |
| async_tree_io           | 1.77 sec                                               | 924 ms: 1.91x faster                                                             |
| async_tree_memoization  | 870 ms                                                 | 462 ms: 1.88x faster                                                             |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 595 ms: 1.71x faster                                                             |
| Geometric mean          | (ref)                                                  | 1.86x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240325-linux-x86_64-faster%2dcpython-tier2_hot_cold_split-3.13.0a5+-37627d3 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 91.1 ms: 1.69x faster                                                            |
| float          | 117 ms                                                 | 77.1 ms: 1.52x faster                                                            |
| pidigits       | 191 ms                                                 | 190 ms: 1.00x faster                                                             |
| Geometric mean | (ref)                                                  | 1.37x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240325-linux-x86_64-faster%2dcpython-tier2_hot_cold_split-3.13.0a5+-37627d3 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 146 ms: 1.29x faster                                                             |
| regex_v8       | 27.8 ms                                                | 24.2 ms: 1.15x faster                                                            |
| regex_dna      | 227 ms                                                 | 218 ms: 1.04x faster                                                             |
| regex_effbot   | 3.63 ms                                                | 3.53 ms: 1.03x faster                                                            |
| Geometric mean | (ref)                                                  | 1.12x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240325-linux-x86_64-faster%2dcpython-tier2_hot_cold_split-3.13.0a5+-37627d3 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| pickle_pure_python   | 484 us                                                 | 310 us: 1.56x faster                                                             |
| tomli_loads          | 3.14 sec                                               | 2.07 sec: 1.52x faster                                                           |
| unpickle_pure_python | 331 us                                                 | 240 us: 1.38x faster                                                             |
| json_dumps           | 14.2 ms                                                | 10.5 ms: 1.35x faster                                                            |
| xml_etree_process    | 79.1 ms                                                | 60.4 ms: 1.31x faster                                                            |
| xml_etree_generate   | 99.4 ms                                                | 87.8 ms: 1.13x faster                                                            |
| json_loads           | 31.2 us                                                | 28.6 us: 1.09x faster                                                            |
| xml_etree_iterparse  | 115 ms                                                 | 108 ms: 1.07x faster                                                             |
| xml_etree_parse      | 168 ms                                                 | 160 ms: 1.05x faster                                                             |
| unpickle_list        | 5.20 us                                                | 5.08 us: 1.02x faster                                                            |
| pickle_list          | 5.08 us                                                | 5.13 us: 1.01x slower                                                            |
| unpickle             | 14.4 us                                                | 15.1 us: 1.05x slower                                                            |
| pickle               | 10.7 us                                                | 11.8 us: 1.10x slower                                                            |
| pickle_dict          | 29.6 us                                                | 34.8 us: 1.18x slower                                                            |
| Geometric mean       | (ref)                                                  | 1.14x faster                                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240325-linux-x86_64-faster%2dcpython-tier2_hot_cold_split-3.13.0a5+-37627d3 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 11.0 ms: 1.32x faster                                                            |
| python_startup_no_site | 5.93 ms                                                | 9.44 ms: 1.59x slower                                                            |
| Geometric mean         | (ref)                                                  | 1.10x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240325-linux-x86_64-faster%2dcpython-tier2_hot_cold_split-3.13.0a5+-37627d3 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 10.8 ms: 1.51x faster                                                            |
| django_template | 48.2 ms                                                | 36.2 ms: 1.33x faster                                                            |
| genshi_text     | 31.8 ms                                                | 24.4 ms: 1.30x faster                                                            |
| genshi_xml      | 66.0 ms                                                | 54.0 ms: 1.22x faster                                                            |
| Geometric mean  | (ref)                                                  | 1.34x faster                                                                     |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240325-linux-x86_64-faster%2dcpython-tier2_hot_cold_split-3.13.0a5+-37627d3 |
|--------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 112 us: 4.87x faster                                                             |
| generators               | 80.1 ms                                                | 30.4 ms: 2.63x faster                                                            |
| deltablue                | 7.91 ms                                                | 3.46 ms: 2.29x faster                                                            |
| async_tree_none          | 728 ms                                                 | 375 ms: 1.94x faster                                                             |
| async_tree_io            | 1.77 sec                                               | 924 ms: 1.91x faster                                                             |
| logging_silent           | 190 ns                                                 | 99.3 ns: 1.91x faster                                                            |
| async_tree_memoization   | 870 ms                                                 | 462 ms: 1.88x faster                                                             |
| chaos                    | 115 ms                                                 | 63.1 ms: 1.83x faster                                                            |
| richards_super           | 94.7 ms                                                | 52.0 ms: 1.82x faster                                                            |
| asyncio_tcp              | 922 ms                                                 | 511 ms: 1.80x faster                                                             |
| raytrace                 | 507 ms                                                 | 292 ms: 1.74x faster                                                             |
| richards                 | 79.3 ms                                                | 45.7 ms: 1.73x faster                                                            |
| crypto_pyaes             | 128 ms                                                 | 74.1 ms: 1.72x faster                                                            |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 595 ms: 1.71x faster                                                             |
| scimark_monte_carlo      | 118 ms                                                 | 70.0 ms: 1.69x faster                                                            |
| nbody                    | 154 ms                                                 | 91.1 ms: 1.69x faster                                                            |
| pylint                   | 551 ms                                                 | 336 ms: 1.64x faster                                                             |
| sqlglot_parse            | 2.17 ms                                                | 1.33 ms: 1.63x faster                                                            |
| scimark_sor              | 220 ms                                                 | 136 ms: 1.61x faster                                                             |
| comprehensions           | 28.8 us                                                | 18.2 us: 1.58x faster                                                            |
| pickle_pure_python       | 484 us                                                 | 310 us: 1.56x faster                                                             |
| sqlglot_transpile        | 2.57 ms                                                | 1.66 ms: 1.55x faster                                                            |
| go                       | 240 ms                                                 | 155 ms: 1.55x faster                                                             |
| coroutines               | 35.1 ms                                                | 22.8 ms: 1.54x faster                                                            |
| float                    | 117 ms                                                 | 77.1 ms: 1.52x faster                                                            |
| tomli_loads              | 3.14 sec                                               | 2.07 sec: 1.52x faster                                                           |
| mako                     | 16.3 ms                                                | 10.8 ms: 1.51x faster                                                            |
| deepcopy_memo            | 58.5 us                                                | 39.3 us: 1.49x faster                                                            |
| pyflate                  | 716 ms                                                 | 481 ms: 1.49x faster                                                             |
| spectral_norm            | 170 ms                                                 | 116 ms: 1.46x faster                                                             |
| hexiom                   | 10.4 ms                                                | 7.22 ms: 1.44x faster                                                            |
| tornado_http             | 136 ms                                                 | 96.8 ms: 1.41x faster                                                            |
| logging_simple           | 8.30 us                                                | 5.90 us: 1.41x faster                                                            |
| logging_format           | 9.09 us                                                | 6.55 us: 1.39x faster                                                            |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.86 sec: 1.38x faster                                                           |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.69 ms: 1.38x faster                                                            |
| unpickle_pure_python     | 331 us                                                 | 240 us: 1.38x faster                                                             |
| scimark_fft              | 466 ms                                                 | 339 ms: 1.37x faster                                                             |
| pprint_pformat           | 2.10 sec                                               | 1.53 sec: 1.37x faster                                                           |
| fannkuch                 | 532 ms                                                 | 391 ms: 1.36x faster                                                             |
| chameleon                | 9.68 ms                                                | 7.14 ms: 1.36x faster                                                            |
| json_dumps               | 14.2 ms                                                | 10.5 ms: 1.35x faster                                                            |
| pprint_safe_repr         | 1.02 sec                                               | 754 ms: 1.35x faster                                                             |
| pycparser                | 1.58 sec                                               | 1.18 sec: 1.34x faster                                                           |
| scimark_lu               | 176 ms                                                 | 132 ms: 1.34x faster                                                             |
| django_template          | 48.2 ms                                                | 36.2 ms: 1.33x faster                                                            |
| python_startup           | 14.6 ms                                                | 11.0 ms: 1.32x faster                                                            |
| deepcopy                 | 479 us                                                 | 363 us: 1.32x faster                                                             |
| thrift                   | 1.07 ms                                                | 816 us: 1.31x faster                                                             |
| html5lib                 | 88.9 ms                                                | 67.7 ms: 1.31x faster                                                            |
| deepcopy_reduce          | 4.17 us                                                | 3.18 us: 1.31x faster                                                            |
| xml_etree_process        | 79.1 ms                                                | 60.4 ms: 1.31x faster                                                            |
| genshi_text              | 31.8 ms                                                | 24.4 ms: 1.30x faster                                                            |
| regex_compile            | 188 ms                                                 | 146 ms: 1.29x faster                                                             |
| sqlglot_normalize        | 143 ms                                                 | 113 ms: 1.26x faster                                                             |
| 2to3                     | 348 ms                                                 | 278 ms: 1.26x faster                                                             |
| djangocms                | 38.4 us                                                | 31.3 us: 1.23x faster                                                            |
| genshi_xml               | 66.0 ms                                                | 54.0 ms: 1.22x faster                                                            |
| sqlglot_optimize         | 69.2 ms                                                | 58.1 ms: 1.19x faster                                                            |
| dulwich_log              | 84.3 ms                                                | 70.9 ms: 1.19x faster                                                            |
| sympy_sum                | 196 ms                                                 | 165 ms: 1.19x faster                                                             |
| sympy_str                | 346 ms                                                 | 291 ms: 1.19x faster                                                             |
| sympy_integrate          | 25.8 ms                                                | 21.8 ms: 1.18x faster                                                            |
| aiohttp                  | 1.44 ms                                                | 1.22 ms: 1.18x faster                                                            |
| dask                     | 441 ms                                                 | 378 ms: 1.17x faster                                                             |
| nqueens                  | 106 ms                                                 | 90.8 ms: 1.17x faster                                                            |
| gunicorn                 | 1.53 ms                                                | 1.31 ms: 1.17x faster                                                            |
| sympy_expand             | 566 ms                                                 | 491 ms: 1.15x faster                                                             |
| bench_thread_pool        | 986 us                                                 | 859 us: 1.15x faster                                                             |
| regex_v8                 | 27.8 ms                                                | 24.2 ms: 1.15x faster                                                            |
| docutils                 | 3.30 sec                                               | 2.88 sec: 1.14x faster                                                           |
| xml_etree_generate       | 99.4 ms                                                | 87.8 ms: 1.13x faster                                                            |
| mypy2                    | 894 ms                                                 | 795 ms: 1.12x faster                                                             |
| create_gc_cycles         | 1.62 ms                                                | 1.47 ms: 1.10x faster                                                            |
| json_loads               | 31.2 us                                                | 28.6 us: 1.09x faster                                                            |
| xml_etree_iterparse      | 115 ms                                                 | 108 ms: 1.07x faster                                                             |
| meteor_contest           | 120 ms                                                 | 112 ms: 1.07x faster                                                             |
| pathlib                  | 20.5 ms                                                | 19.1 ms: 1.07x faster                                                            |
| json                     | 5.69 ms                                                | 5.35 ms: 1.06x faster                                                            |
| sqlite_synth             | 3.02 us                                                | 2.87 us: 1.05x faster                                                            |
| xml_etree_parse          | 168 ms                                                 | 160 ms: 1.05x faster                                                             |
| regex_dna                | 227 ms                                                 | 218 ms: 1.04x faster                                                             |
| regex_effbot             | 3.63 ms                                                | 3.53 ms: 1.03x faster                                                            |
| unpickle_list            | 5.20 us                                                | 5.08 us: 1.02x faster                                                            |
| mdp                      | 2.85 sec                                               | 2.80 sec: 1.02x faster                                                           |
| pidigits                 | 191 ms                                                 | 190 ms: 1.00x faster                                                             |
| pickle_list              | 5.08 us                                                | 5.13 us: 1.01x slower                                                            |
| asyncio_websockets       | 559 ms                                                 | 570 ms: 1.02x slower                                                             |
| async_generators         | 444 ms                                                 | 460 ms: 1.04x slower                                                             |
| unpickle                 | 14.4 us                                                | 15.1 us: 1.05x slower                                                            |
| gc_traversal             | 3.62 ms                                                | 3.82 ms: 1.05x slower                                                            |
| pickle                   | 10.7 us                                                | 11.8 us: 1.10x slower                                                            |
| telco                    | 7.27 ms                                                | 8.51 ms: 1.17x slower                                                            |
| pickle_dict              | 29.6 us                                                | 34.8 us: 1.18x slower                                                            |
| coverage                 | 79.4 ms                                                | 96.7 ms: 1.22x slower                                                            |
| unpack_sequence          | 60.0 ns                                                | 92.1 ns: 1.53x slower                                                            |
| python_startup_no_site   | 5.93 ms                                                | 9.44 ms: 1.59x slower                                                            |
| Geometric mean           | (ref)                                                  | 1.31x faster                                                                     |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (3) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: flaskblogging, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (4) of results/bm-20240325-3.13.0a5+-37627d3-JIT/bm-20240325-linux-x86_64-faster%2dcpython-tier2_hot_cold_split-3.13.0a5+-37627d3.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.26x
- 95% likely to have a speedup of 1.24x
- 99% likely to have a speedup of 1.21x


# Memory

- memory change: 1.18x
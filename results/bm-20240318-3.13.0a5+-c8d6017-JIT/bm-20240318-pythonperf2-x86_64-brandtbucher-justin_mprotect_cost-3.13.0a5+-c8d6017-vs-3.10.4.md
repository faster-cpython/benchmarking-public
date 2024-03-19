# Results vs. 3.10.4

- fork: brandtbucher
- ref: justin_mprotect_cost
- machine: linux-x86_64
- commit hash: c8d6017
- commit date: 2024-03-18
- overall geometric mean: 1.25x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.17x faster
- Memory change: 1.35x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240318-pythonperf2-x86_64-brandtbucher-justin_mprotect_cost-3.13.0a5+-c8d6017 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 304 ms: 1.15x faster                                                               |
| chameleon      | 9.44 ms                                                      | 7.30 ms: 1.29x faster                                                              |
| docutils       | 3.41 sec                                                     | 2.93 sec: 1.16x faster                                                             |
| html5lib       | 94.6 ms                                                      | 73.8 ms: 1.28x faster                                                              |
| tornado_http   | 157 ms                                                       | 128 ms: 1.22x faster                                                               |
| Geometric mean | (ref)                                                        | 1.22x faster                                                                       |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240318-pythonperf2-x86_64-brandtbucher-justin_mprotect_cost-3.13.0a5+-c8d6017 |
|-------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| async_tree_none         | 692 ms                                                       | 436 ms: 1.59x faster                                                               |
| async_tree_memoization  | 819 ms                                                       | 548 ms: 1.49x faster                                                               |
| async_tree_io           | 1.60 sec                                                     | 1.08 sec: 1.48x faster                                                             |
| async_tree_cpu_io_mixed | 936 ms                                                       | 702 ms: 1.33x faster                                                               |
| Geometric mean          | (ref)                                                        | 1.47x faster                                                                       |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240318-pythonperf2-x86_64-brandtbucher-justin_mprotect_cost-3.13.0a5+-c8d6017 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| float          | 111 ms                                                       | 78.6 ms: 1.41x faster                                                              |
| nbody          | 134 ms                                                       | 95.5 ms: 1.41x faster                                                              |
| pidigits       | 271 ms                                                       | 261 ms: 1.04x faster                                                               |
| Geometric mean | (ref)                                                        | 1.27x faster                                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240318-pythonperf2-x86_64-brandtbucher-justin_mprotect_cost-3.13.0a5+-c8d6017 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 146 ms: 1.30x faster                                                               |
| regex_v8       | 27.2 ms                                                      | 25.7 ms: 1.06x faster                                                              |
| regex_dna      | 261 ms                                                       | 252 ms: 1.04x faster                                                               |
| regex_effbot   | 3.09 ms                                                      | 3.67 ms: 1.19x slower                                                              |
| Geometric mean | (ref)                                                        | 1.05x faster                                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240318-pythonperf2-x86_64-brandtbucher-justin_mprotect_cost-3.13.0a5+-c8d6017 |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                       | 309 us: 1.47x faster                                                               |
| json_dumps           | 14.5 ms                                                      | 10.6 ms: 1.37x faster                                                              |
| unpickle_pure_python | 312 us                                                       | 232 us: 1.34x faster                                                               |
| tomli_loads          | 2.92 sec                                                     | 2.18 sec: 1.34x faster                                                             |
| xml_etree_process    | 75.9 ms                                                      | 58.8 ms: 1.29x faster                                                              |
| json_loads           | 30.3 us                                                      | 24.6 us: 1.23x faster                                                              |
| xml_etree_parse      | 160 ms                                                       | 143 ms: 1.12x faster                                                               |
| xml_etree_generate   | 92.3 ms                                                      | 84.2 ms: 1.10x faster                                                              |
| xml_etree_iterparse  | 110 ms                                                       | 102 ms: 1.08x faster                                                               |
| unpickle_list        | 4.65 us                                                      | 4.59 us: 1.01x faster                                                              |
| pickle               | 9.89 us                                                      | 10.2 us: 1.03x slower                                                              |
| pickle_dict          | 29.5 us                                                      | 30.4 us: 1.03x slower                                                              |
| pickle_list          | 4.12 us                                                      | 4.50 us: 1.09x slower                                                              |
| unpickle             | 13.5 us                                                      | 14.8 us: 1.10x slower                                                              |
| Geometric mean       | (ref)                                                        | 1.14x faster                                                                       |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240318-pythonperf2-x86_64-brandtbucher-justin_mprotect_cost-3.13.0a5+-c8d6017 |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 14.4 ms: 1.25x slower                                                              |
| python_startup_no_site | 7.33 ms                                                      | 12.8 ms: 1.75x slower                                                              |
| Geometric mean         | (ref)                                                        | 1.48x slower                                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240318-pythonperf2-x86_64-brandtbucher-justin_mprotect_cost-3.13.0a5+-c8d6017 |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 9.92 ms: 1.48x faster                                                              |
| django_template | 50.2 ms                                                      | 38.5 ms: 1.30x faster                                                              |
| genshi_text     | 31.4 ms                                                      | 27.9 ms: 1.13x faster                                                              |
| genshi_xml      | 63.3 ms                                                      | 58.6 ms: 1.08x faster                                                              |
| Geometric mean  | (ref)                                                        | 1.24x faster                                                                       |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240318-pythonperf2-x86_64-brandtbucher-justin_mprotect_cost-3.13.0a5+-c8d6017 |
|--------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 121 us: 4.42x faster                                                               |
| asyncio_tcp              | 779 ms                                                       | 372 ms: 2.10x faster                                                               |
| deltablue                | 7.50 ms                                                      | 3.74 ms: 2.01x faster                                                              |
| asyncio_tcp_ssl          | 3.10 sec                                                     | 1.58 sec: 1.96x faster                                                             |
| logging_silent           | 167 ns                                                       | 97.4 ns: 1.72x faster                                                              |
| generators               | 57.3 ms                                                      | 33.5 ms: 1.71x faster                                                              |
| chaos                    | 109 ms                                                       | 66.6 ms: 1.63x faster                                                              |
| richards_super           | 90.6 ms                                                      | 56.3 ms: 1.61x faster                                                              |
| raytrace                 | 489 ms                                                       | 305 ms: 1.60x faster                                                               |
| sqlglot_parse            | 2.24 ms                                                      | 1.40 ms: 1.59x faster                                                              |
| async_tree_none          | 692 ms                                                       | 436 ms: 1.59x faster                                                               |
| pylint                   | 566 ms                                                       | 359 ms: 1.58x faster                                                               |
| crypto_pyaes             | 119 ms                                                       | 77.4 ms: 1.54x faster                                                              |
| go                       | 262 ms                                                       | 172 ms: 1.52x faster                                                               |
| async_tree_memoization   | 819 ms                                                       | 548 ms: 1.49x faster                                                               |
| richards                 | 75.1 ms                                                      | 50.4 ms: 1.49x faster                                                              |
| spectral_norm            | 139 ms                                                       | 93.7 ms: 1.48x faster                                                              |
| mako                     | 14.7 ms                                                      | 9.92 ms: 1.48x faster                                                              |
| async_tree_io            | 1.60 sec                                                     | 1.08 sec: 1.48x faster                                                             |
| pickle_pure_python       | 455 us                                                       | 309 us: 1.47x faster                                                               |
| sqlglot_transpile        | 2.68 ms                                                      | 1.83 ms: 1.47x faster                                                              |
| scimark_monte_carlo      | 107 ms                                                       | 75.1 ms: 1.43x faster                                                              |
| pyflate                  | 733 ms                                                       | 515 ms: 1.42x faster                                                               |
| comprehensions           | 26.7 us                                                      | 18.8 us: 1.42x faster                                                              |
| float                    | 111 ms                                                       | 78.6 ms: 1.41x faster                                                              |
| nbody                    | 134 ms                                                       | 95.5 ms: 1.41x faster                                                              |
| json_dumps               | 14.5 ms                                                      | 10.6 ms: 1.37x faster                                                              |
| coroutines               | 30.3 ms                                                      | 22.4 ms: 1.35x faster                                                              |
| unpickle_pure_python     | 312 us                                                       | 232 us: 1.34x faster                                                               |
| deepcopy_memo            | 49.8 us                                                      | 37.1 us: 1.34x faster                                                              |
| tomli_loads              | 2.92 sec                                                     | 2.18 sec: 1.34x faster                                                             |
| thrift                   | 1.18 ms                                                      | 879 us: 1.34x faster                                                               |
| scimark_lu               | 167 ms                                                       | 125 ms: 1.34x faster                                                               |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 702 ms: 1.33x faster                                                               |
| logging_simple           | 8.88 us                                                      | 6.77 us: 1.31x faster                                                              |
| hexiom                   | 9.42 ms                                                      | 7.19 ms: 1.31x faster                                                              |
| bench_mp_pool            | 6.37 ms                                                      | 4.87 ms: 1.31x faster                                                              |
| django_template          | 50.2 ms                                                      | 38.5 ms: 1.30x faster                                                              |
| regex_compile            | 190 ms                                                       | 146 ms: 1.30x faster                                                               |
| chameleon                | 9.44 ms                                                      | 7.30 ms: 1.29x faster                                                              |
| xml_etree_process        | 75.9 ms                                                      | 58.8 ms: 1.29x faster                                                              |
| html5lib                 | 94.6 ms                                                      | 73.8 ms: 1.28x faster                                                              |
| logging_format           | 9.64 us                                                      | 7.55 us: 1.28x faster                                                              |
| deepcopy                 | 468 us                                                       | 368 us: 1.27x faster                                                               |
| pprint_pformat           | 2.15 sec                                                     | 1.70 sec: 1.26x faster                                                             |
| fannkuch                 | 483 ms                                                       | 383 ms: 1.26x faster                                                               |
| pprint_safe_repr         | 1.05 sec                                                     | 833 ms: 1.26x faster                                                               |
| pycparser                | 1.67 sec                                                     | 1.35 sec: 1.24x faster                                                             |
| json_loads               | 30.3 us                                                      | 24.6 us: 1.23x faster                                                              |
| deepcopy_reduce          | 4.01 us                                                      | 3.28 us: 1.22x faster                                                              |
| tornado_http             | 157 ms                                                       | 128 ms: 1.22x faster                                                               |
| sqlglot_normalize        | 144 ms                                                       | 120 ms: 1.20x faster                                                               |
| sympy_sum                | 193 ms                                                       | 161 ms: 1.20x faster                                                               |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 4.25 ms: 1.19x faster                                                              |
| scimark_sor              | 180 ms                                                       | 152 ms: 1.19x faster                                                               |
| sympy_str                | 360 ms                                                       | 305 ms: 1.18x faster                                                               |
| mdp                      | 3.01 sec                                                     | 2.57 sec: 1.17x faster                                                             |
| sympy_expand             | 600 ms                                                       | 514 ms: 1.17x faster                                                               |
| bench_thread_pool        | 1.14 ms                                                      | 979 us: 1.17x faster                                                               |
| docutils                 | 3.41 sec                                                     | 2.93 sec: 1.16x faster                                                             |
| dulwich_log              | 81.1 ms                                                      | 69.9 ms: 1.16x faster                                                              |
| dask                     | 472 ms                                                       | 408 ms: 1.16x faster                                                               |
| 2to3                     | 350 ms                                                       | 304 ms: 1.15x faster                                                               |
| sympy_integrate          | 28.2 ms                                                      | 24.7 ms: 1.14x faster                                                              |
| create_gc_cycles         | 1.76 ms                                                      | 1.55 ms: 1.14x faster                                                              |
| nqueens                  | 115 ms                                                       | 101 ms: 1.14x faster                                                               |
| scimark_fft              | 361 ms                                                       | 319 ms: 1.13x faster                                                               |
| genshi_text              | 31.4 ms                                                      | 27.9 ms: 1.13x faster                                                              |
| sqlglot_optimize         | 70.1 ms                                                      | 62.7 ms: 1.12x faster                                                              |
| xml_etree_parse          | 160 ms                                                       | 143 ms: 1.12x faster                                                               |
| sqlite_synth             | 2.99 us                                                      | 2.70 us: 1.11x faster                                                              |
| xml_etree_generate       | 92.3 ms                                                      | 84.2 ms: 1.10x faster                                                              |
| pathlib                  | 21.4 ms                                                      | 19.6 ms: 1.09x faster                                                              |
| async_generators         | 421 ms                                                       | 388 ms: 1.09x faster                                                               |
| xml_etree_iterparse      | 110 ms                                                       | 102 ms: 1.08x faster                                                               |
| genshi_xml               | 63.3 ms                                                      | 58.6 ms: 1.08x faster                                                              |
| json                     | 5.86 ms                                                      | 5.45 ms: 1.08x faster                                                              |
| gunicorn                 | 1.16 ms                                                      | 1.08 ms: 1.07x faster                                                              |
| aiohttp                  | 1.19 ms                                                      | 1.12 ms: 1.06x faster                                                              |
| regex_v8                 | 27.2 ms                                                      | 25.7 ms: 1.06x faster                                                              |
| meteor_contest           | 138 ms                                                       | 132 ms: 1.05x faster                                                               |
| regex_dna                | 261 ms                                                       | 252 ms: 1.04x faster                                                               |
| pidigits                 | 271 ms                                                       | 261 ms: 1.04x faster                                                               |
| unpickle_list            | 4.65 us                                                      | 4.59 us: 1.01x faster                                                              |
| asyncio_websockets       | 390 ms                                                       | 387 ms: 1.01x faster                                                               |
| gc_traversal             | 3.42 ms                                                      | 3.48 ms: 1.02x slower                                                              |
| pickle                   | 9.89 us                                                      | 10.2 us: 1.03x slower                                                              |
| pickle_dict              | 29.5 us                                                      | 30.4 us: 1.03x slower                                                              |
| unpack_sequence          | 59.9 ns                                                      | 62.6 ns: 1.04x slower                                                              |
| pickle_list              | 4.12 us                                                      | 4.50 us: 1.09x slower                                                              |
| unpickle                 | 13.5 us                                                      | 14.8 us: 1.10x slower                                                              |
| telco                    | 7.23 ms                                                      | 8.12 ms: 1.12x slower                                                              |
| regex_effbot             | 3.09 ms                                                      | 3.67 ms: 1.19x slower                                                              |
| python_startup           | 11.5 ms                                                      | 14.4 ms: 1.25x slower                                                              |
| coverage                 | 63.3 ms                                                      | 79.0 ms: 1.25x slower                                                              |
| python_startup_no_site   | 7.33 ms                                                      | 12.8 ms: 1.75x slower                                                              |
| Geometric mean           | (ref)                                                        | 1.25x faster                                                                       |

Benchmark hidden because not significant (1): mypy2
Ignored benchmarks (3) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: flaskblogging, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (4) of results/bm-20240318-3.13.0a5+-c8d6017-JIT/bm-20240318-pythonperf2-x86_64-brandtbucher-justin_mprotect_cost-3.13.0a5+-c8d6017.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.20x
- 95% likely to have a speedup of 1.19x
- 99% likely to have a speedup of 1.17x


# Memory

- memory change: 1.35x
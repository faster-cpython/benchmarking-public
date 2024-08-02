# Results vs. 3.10.4

- fork: python
- ref: v3.13.0b2
- machine: linux-x86_64
- commit hash: 3a83b17
- commit date: 2024-06-05
- overall geometric mean: 1.27x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.18x faster
- Memory change: 1.22x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 305 ms: 1.15x faster                                             |
| chameleon      | 9.44 ms                                                      | 7.48 ms: 1.26x faster                                            |
| html5lib       | 94.6 ms                                                      | 75.4 ms: 1.26x faster                                            |
| tornado_http   | 157 ms                                                       | 123 ms: 1.28x faster                                             |
| Geometric mean | (ref)                                                        | 1.23x faster                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|-------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| async_tree_none         | 692 ms                                                       | 380 ms: 1.82x faster                                             |
| async_tree_memoization  | 819 ms                                                       | 454 ms: 1.80x faster                                             |
| async_tree_io           | 1.60 sec                                                     | 921 ms: 1.74x faster                                             |
| async_tree_cpu_io_mixed | 936 ms                                                       | 628 ms: 1.49x faster                                             |
| Geometric mean          | (ref)                                                        | 1.71x faster                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| nbody          | 134 ms                                                       | 82.9 ms: 1.62x faster                                            |
| float          | 111 ms                                                       | 74.2 ms: 1.50x faster                                            |
| pidigits       | 271 ms                                                       | 250 ms: 1.08x faster                                             |
| Geometric mean | (ref)                                                        | 1.38x faster                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 139 ms: 1.37x faster                                             |
| regex_v8       | 27.2 ms                                                      | 25.2 ms: 1.08x faster                                            |
| regex_dna      | 261 ms                                                       | 248 ms: 1.05x faster                                             |
| regex_effbot   | 3.09 ms                                                      | 3.56 ms: 1.15x slower                                            |
| Geometric mean | (ref)                                                        | 1.08x faster                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| unpickle_pure_python | 312 us                                                       | 211 us: 1.48x faster                                             |
| pickle_pure_python   | 455 us                                                       | 310 us: 1.47x faster                                             |
| tomli_loads          | 2.92 sec                                                     | 2.09 sec: 1.40x faster                                           |
| json_dumps           | 14.5 ms                                                      | 10.7 ms: 1.36x faster                                            |
| xml_etree_process    | 75.9 ms                                                      | 58.5 ms: 1.30x faster                                            |
| json_loads           | 30.3 us                                                      | 24.4 us: 1.24x faster                                            |
| xml_etree_generate   | 92.3 ms                                                      | 82.4 ms: 1.12x faster                                            |
| xml_etree_iterparse  | 110 ms                                                       | 99.3 ms: 1.11x faster                                            |
| xml_etree_parse      | 160 ms                                                       | 145 ms: 1.10x faster                                             |
| unpickle_list        | 4.65 us                                                      | 4.75 us: 1.02x slower                                            |
| pickle_dict          | 29.5 us                                                      | 30.9 us: 1.05x slower                                            |
| pickle_list          | 4.12 us                                                      | 4.35 us: 1.06x slower                                            |
| pickle               | 9.89 us                                                      | 10.6 us: 1.07x slower                                            |
| unpickle             | 13.5 us                                                      | 15.6 us: 1.16x slower                                            |
| Geometric mean       | (ref)                                                        | 1.14x faster                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 13.8 ms: 1.20x slower                                            |
| python_startup_no_site | 7.33 ms                                                      | 9.44 ms: 1.29x slower                                            |
| Geometric mean         | (ref)                                                        | 1.24x slower                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 9.10 ms: 1.61x faster                                            |
| django_template | 50.2 ms                                                      | 41.4 ms: 1.21x faster                                            |
| genshi_text     | 31.4 ms                                                      | 28.2 ms: 1.12x faster                                            |
| genshi_xml      | 63.3 ms                                                      | 65.3 ms: 1.03x slower                                            |
| Geometric mean  | (ref)                                                        | 1.21x faster                                                     |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|--------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 184 us: 2.92x faster                                             |
| asyncio_tcp              | 779 ms                                                       | 382 ms: 2.04x faster                                             |
| deltablue                | 7.50 ms                                                      | 3.81 ms: 1.97x faster                                            |
| asyncio_tcp_ssl          | 3.10 sec                                                     | 1.58 sec: 1.96x faster                                           |
| async_tree_none          | 692 ms                                                       | 380 ms: 1.82x faster                                             |
| async_tree_memoization   | 819 ms                                                       | 454 ms: 1.80x faster                                             |
| async_tree_io            | 1.60 sec                                                     | 921 ms: 1.74x faster                                             |
| richards_super           | 90.6 ms                                                      | 52.8 ms: 1.72x faster                                            |
| spectral_norm            | 139 ms                                                       | 82.3 ms: 1.69x faster                                            |
| crypto_pyaes             | 119 ms                                                       | 70.6 ms: 1.69x faster                                            |
| chaos                    | 109 ms                                                       | 64.4 ms: 1.69x faster                                            |
| generators               | 57.3 ms                                                      | 34.3 ms: 1.67x faster                                            |
| raytrace                 | 489 ms                                                       | 297 ms: 1.65x faster                                             |
| pyflate                  | 733 ms                                                       | 449 ms: 1.63x faster                                             |
| scimark_monte_carlo      | 107 ms                                                       | 65.9 ms: 1.63x faster                                            |
| nbody                    | 134 ms                                                       | 82.9 ms: 1.62x faster                                            |
| mako                     | 14.7 ms                                                      | 9.10 ms: 1.61x faster                                            |
| richards                 | 75.1 ms                                                      | 46.5 ms: 1.61x faster                                            |
| go                       | 262 ms                                                       | 166 ms: 1.58x faster                                             |
| sqlglot_parse            | 2.24 ms                                                      | 1.42 ms: 1.57x faster                                            |
| pylint                   | 566 ms                                                       | 376 ms: 1.50x faster                                             |
| comprehensions           | 26.7 us                                                      | 17.8 us: 1.50x faster                                            |
| float                    | 111 ms                                                       | 74.2 ms: 1.50x faster                                            |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 628 ms: 1.49x faster                                             |
| unpickle_pure_python     | 312 us                                                       | 211 us: 1.48x faster                                             |
| sqlglot_transpile        | 2.68 ms                                                      | 1.82 ms: 1.47x faster                                            |
| scimark_lu               | 167 ms                                                       | 114 ms: 1.47x faster                                             |
| pickle_pure_python       | 455 us                                                       | 310 us: 1.47x faster                                             |
| fannkuch                 | 483 ms                                                       | 331 ms: 1.46x faster                                             |
| hexiom                   | 9.42 ms                                                      | 6.65 ms: 1.42x faster                                            |
| tomli_loads              | 2.92 sec                                                     | 2.09 sec: 1.40x faster                                           |
| regex_compile            | 190 ms                                                       | 139 ms: 1.37x faster                                             |
| json_dumps               | 14.5 ms                                                      | 10.7 ms: 1.36x faster                                            |
| coroutines               | 30.3 ms                                                      | 22.3 ms: 1.36x faster                                            |
| logging_silent           | 167 ns                                                       | 123 ns: 1.36x faster                                             |
| logging_format           | 9.64 us                                                      | 7.17 us: 1.34x faster                                            |
| logging_simple           | 8.88 us                                                      | 6.61 us: 1.34x faster                                            |
| deepcopy_memo            | 49.8 us                                                      | 37.2 us: 1.34x faster                                            |
| pycparser                | 1.67 sec                                                     | 1.25 sec: 1.34x faster                                           |
| bench_mp_pool            | 6.37 ms                                                      | 4.80 ms: 1.33x faster                                            |
| pprint_safe_repr         | 1.05 sec                                                     | 792 ms: 1.33x faster                                             |
| pprint_pformat           | 2.15 sec                                                     | 1.63 sec: 1.32x faster                                           |
| xml_etree_process        | 75.9 ms                                                      | 58.5 ms: 1.30x faster                                            |
| thrift                   | 1.18 ms                                                      | 913 us: 1.29x faster                                             |
| tornado_http             | 157 ms                                                       | 123 ms: 1.28x faster                                             |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 3.99 ms: 1.27x faster                                            |
| chameleon                | 9.44 ms                                                      | 7.48 ms: 1.26x faster                                            |
| html5lib                 | 94.6 ms                                                      | 75.4 ms: 1.26x faster                                            |
| scimark_sor              | 180 ms                                                       | 144 ms: 1.25x faster                                             |
| json_loads               | 30.3 us                                                      | 24.4 us: 1.24x faster                                            |
| scimark_fft              | 361 ms                                                       | 292 ms: 1.24x faster                                             |
| pathlib                  | 21.4 ms                                                      | 17.4 ms: 1.23x faster                                            |
| dulwich_log              | 81.1 ms                                                      | 66.2 ms: 1.22x faster                                            |
| bench_thread_pool        | 1.14 ms                                                      | 941 us: 1.21x faster                                             |
| django_template          | 50.2 ms                                                      | 41.4 ms: 1.21x faster                                            |
| nqueens                  | 115 ms                                                       | 97.2 ms: 1.18x faster                                            |
| mdp                      | 3.01 sec                                                     | 2.55 sec: 1.18x faster                                           |
| sympy_sum                | 193 ms                                                       | 165 ms: 1.17x faster                                             |
| sympy_str                | 360 ms                                                       | 310 ms: 1.16x faster                                             |
| dask                     | 472 ms                                                       | 408 ms: 1.16x faster                                             |
| 2to3                     | 350 ms                                                       | 305 ms: 1.15x faster                                             |
| deepcopy                 | 468 us                                                       | 410 us: 1.14x faster                                             |
| sqlglot_normalize        | 144 ms                                                       | 127 ms: 1.13x faster                                             |
| sympy_expand             | 600 ms                                                       | 532 ms: 1.13x faster                                             |
| xml_etree_generate       | 92.3 ms                                                      | 82.4 ms: 1.12x faster                                            |
| genshi_text              | 31.4 ms                                                      | 28.2 ms: 1.12x faster                                            |
| sqlglot_optimize         | 70.1 ms                                                      | 62.9 ms: 1.12x faster                                            |
| xml_etree_iterparse      | 110 ms                                                       | 99.3 ms: 1.11x faster                                            |
| sympy_integrate          | 28.2 ms                                                      | 25.4 ms: 1.11x faster                                            |
| json                     | 5.86 ms                                                      | 5.30 ms: 1.11x faster                                            |
| xml_etree_parse          | 160 ms                                                       | 145 ms: 1.10x faster                                             |
| mypy2                    | 933 ms                                                       | 852 ms: 1.09x faster                                             |
| deepcopy_reduce          | 4.01 us                                                      | 3.68 us: 1.09x faster                                            |
| async_generators         | 421 ms                                                       | 389 ms: 1.08x faster                                             |
| pidigits                 | 271 ms                                                       | 250 ms: 1.08x faster                                             |
| regex_v8                 | 27.2 ms                                                      | 25.2 ms: 1.08x faster                                            |
| sqlite_synth             | 2.99 us                                                      | 2.80 us: 1.07x faster                                            |
| meteor_contest           | 138 ms                                                       | 130 ms: 1.06x faster                                             |
| regex_dna                | 261 ms                                                       | 248 ms: 1.05x faster                                             |
| aiohttp                  | 1.19 ms                                                      | 1.17 ms: 1.01x faster                                            |
| gunicorn                 | 1.16 ms                                                      | 1.15 ms: 1.01x faster                                            |
| unpickle_list            | 4.65 us                                                      | 4.75 us: 1.02x slower                                            |
| genshi_xml               | 63.3 ms                                                      | 65.3 ms: 1.03x slower                                            |
| pickle_dict              | 29.5 us                                                      | 30.9 us: 1.05x slower                                            |
| pickle_list              | 4.12 us                                                      | 4.35 us: 1.06x slower                                            |
| pickle                   | 9.89 us                                                      | 10.6 us: 1.07x slower                                            |
| create_gc_cycles         | 1.76 ms                                                      | 1.94 ms: 1.10x slower                                            |
| telco                    | 7.23 ms                                                      | 8.05 ms: 1.11x slower                                            |
| flaskblogging            | 4.39 ms                                                      | 4.92 ms: 1.12x slower                                            |
| regex_effbot             | 3.09 ms                                                      | 3.56 ms: 1.15x slower                                            |
| unpickle                 | 13.5 us                                                      | 15.6 us: 1.16x slower                                            |
| python_startup           | 11.5 ms                                                      | 13.8 ms: 1.20x slower                                            |
| coverage                 | 63.3 ms                                                      | 80.7 ms: 1.28x slower                                            |
| python_startup_no_site   | 7.33 ms                                                      | 9.44 ms: 1.29x slower                                            |
| gc_traversal             | 3.42 ms                                                      | 4.49 ms: 1.31x slower                                            |
| Geometric mean           | (ref)                                                        | 1.27x faster                                                     |

Benchmark hidden because not significant (1): asyncio_websockets
Ignored benchmarks (4) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: docutils, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (5) of results/bm-20240605-3.13.0b2-3a83b17-JIT/bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.23x
- 95% likely to have a speedup of 1.22x
- 99% likely to have a speedup of 1.18x

# Memory
- memory change: 1.22x
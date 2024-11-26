# Results vs. 3.10.4

- fork: python
- ref: v3.13.0rc2
- machine: linux-x86_64
- commit hash: ec61006
- commit date: 2024-09-06
- overall geometric mean: 1.288x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.20x faster
- Memory change: 1.13x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240906-pythonperf2-x86_64-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 291 ms: 1.20x faster                                               |
| chameleon      | 9.44 ms                                                      | 7.37 ms: 1.28x faster                                              |
| docutils       | 3.41 sec                                                     | 3.00 sec: 1.14x faster                                             |
| html5lib       | 94.6 ms                                                      | 74.6 ms: 1.27x faster                                              |
| tornado_http   | 157 ms                                                       | 119 ms: 1.32x faster                                               |
| Geometric mean | (ref)                                                        | 1.24x faster                                                       |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240906-pythonperf2-x86_64-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|-------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------:|
| async_tree_none         | 692 ms                                                       | 369 ms: 1.88x faster                                               |
| async_tree_io           | 1.60 sec                                                     | 879 ms: 1.82x faster                                               |
| async_tree_memoization  | 819 ms                                                       | 466 ms: 1.76x faster                                               |
| async_tree_cpu_io_mixed | 936 ms                                                       | 615 ms: 1.52x faster                                               |
| Geometric mean          | (ref)                                                        | 1.74x faster                                                       |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240906-pythonperf2-x86_64-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------:|
| nbody          | 134 ms                                                       | 91.6 ms: 1.46x faster                                              |
| float          | 111 ms                                                       | 80.5 ms: 1.38x faster                                              |
| pidigits       | 271 ms                                                       | 254 ms: 1.07x faster                                               |
| Geometric mean | (ref)                                                        | 1.29x faster                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240906-pythonperf2-x86_64-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 143 ms: 1.33x faster                                               |
| regex_v8       | 27.2 ms                                                      | 25.4 ms: 1.07x faster                                              |
| regex_dna      | 261 ms                                                       | 248 ms: 1.06x faster                                               |
| regex_effbot   | 3.09 ms                                                      | 3.74 ms: 1.21x slower                                              |
| Geometric mean | (ref)                                                        | 1.05x faster                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240906-pythonperf2-x86_64-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|----------------------|:------------------------------------------------------------:|:------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                       | 311 us: 1.46x faster                                               |
| unpickle_pure_python | 312 us                                                       | 229 us: 1.36x faster                                               |
| json_dumps           | 14.5 ms                                                      | 11.2 ms: 1.30x faster                                              |
| json_loads           | 30.3 us                                                      | 23.8 us: 1.28x faster                                              |
| xml_etree_process    | 75.9 ms                                                      | 60.9 ms: 1.25x faster                                              |
| tomli_loads          | 2.92 sec                                                     | 2.42 sec: 1.20x faster                                             |
| xml_etree_parse      | 160 ms                                                       | 144 ms: 1.11x faster                                               |
| xml_etree_iterparse  | 110 ms                                                       | 103 ms: 1.08x faster                                               |
| xml_etree_generate   | 92.3 ms                                                      | 87.4 ms: 1.06x faster                                              |
| unpickle_list        | 4.65 us                                                      | 4.56 us: 1.02x faster                                              |
| pickle               | 9.89 us                                                      | 10.5 us: 1.06x slower                                              |
| pickle_dict          | 29.5 us                                                      | 31.7 us: 1.07x slower                                              |
| unpickle             | 13.5 us                                                      | 15.0 us: 1.11x slower                                              |
| pickle_list          | 4.12 us                                                      | 4.59 us: 1.12x slower                                              |
| Geometric mean       | (ref)                                                        | 1.11x faster                                                       |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240906-pythonperf2-x86_64-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 13.3 ms: 1.16x slower                                              |
| python_startup_no_site | 7.33 ms                                                      | 8.93 ms: 1.22x slower                                              |
| Geometric mean         | (ref)                                                        | 1.19x slower                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240906-pythonperf2-x86_64-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|-----------------|:------------------------------------------------------------:|:------------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 10.3 ms: 1.42x faster                                              |
| django_template | 50.2 ms                                                      | 39.3 ms: 1.28x faster                                              |
| genshi_text     | 31.4 ms                                                      | 26.4 ms: 1.19x faster                                              |
| genshi_xml      | 63.3 ms                                                      | 57.2 ms: 1.11x faster                                              |
| Geometric mean  | (ref)                                                        | 1.24x faster                                                       |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240906-pythonperf2-x86_64-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|--------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 177 us: 3.03x faster                                               |
| deltablue                | 7.50 ms                                                      | 3.39 ms: 2.21x faster                                              |
| asyncio_tcp              | 779 ms                                                       | 372 ms: 2.09x faster                                               |
| asyncio_tcp_ssl          | 3.10 sec                                                     | 1.58 sec: 1.97x faster                                             |
| raytrace                 | 489 ms                                                       | 260 ms: 1.88x faster                                               |
| async_tree_none          | 692 ms                                                       | 369 ms: 1.88x faster                                               |
| async_tree_io            | 1.60 sec                                                     | 879 ms: 1.82x faster                                               |
| chaos                    | 109 ms                                                       | 60.1 ms: 1.81x faster                                              |
| async_tree_memoization   | 819 ms                                                       | 466 ms: 1.76x faster                                               |
| logging_silent           | 167 ns                                                       | 96.9 ns: 1.73x faster                                              |
| scimark_lu               | 167 ms                                                       | 96.9 ms: 1.72x faster                                              |
| generators               | 57.3 ms                                                      | 34.0 ms: 1.69x faster                                              |
| crypto_pyaes             | 119 ms                                                       | 72.4 ms: 1.65x faster                                              |
| scimark_monte_carlo      | 107 ms                                                       | 66.2 ms: 1.62x faster                                              |
| pylint                   | 566 ms                                                       | 354 ms: 1.60x faster                                               |
| sqlglot_parse            | 2.24 ms                                                      | 1.41 ms: 1.58x faster                                              |
| go                       | 262 ms                                                       | 165 ms: 1.58x faster                                               |
| comprehensions           | 26.7 us                                                      | 17.1 us: 1.56x faster                                              |
| richards_super           | 90.6 ms                                                      | 58.8 ms: 1.54x faster                                              |
| scimark_sor              | 180 ms                                                       | 118 ms: 1.53x faster                                               |
| pyflate                  | 733 ms                                                       | 481 ms: 1.52x faster                                               |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 615 ms: 1.52x faster                                               |
| sqlglot_transpile        | 2.68 ms                                                      | 1.79 ms: 1.50x faster                                              |
| hexiom                   | 9.42 ms                                                      | 6.32 ms: 1.49x faster                                              |
| pickle_pure_python       | 455 us                                                       | 311 us: 1.46x faster                                               |
| nbody                    | 134 ms                                                       | 91.6 ms: 1.46x faster                                              |
| richards                 | 75.1 ms                                                      | 52.0 ms: 1.45x faster                                              |
| spectral_norm            | 139 ms                                                       | 97.8 ms: 1.42x faster                                              |
| mako                     | 14.7 ms                                                      | 10.3 ms: 1.42x faster                                              |
| logging_simple           | 8.88 us                                                      | 6.25 us: 1.42x faster                                              |
| bench_mp_pool            | 6.37 ms                                                      | 4.61 ms: 1.38x faster                                              |
| logging_format           | 9.64 us                                                      | 6.97 us: 1.38x faster                                              |
| float                    | 111 ms                                                       | 80.5 ms: 1.38x faster                                              |
| unpickle_pure_python     | 312 us                                                       | 229 us: 1.36x faster                                               |
| coroutines               | 30.3 ms                                                      | 22.3 ms: 1.36x faster                                              |
| pycparser                | 1.67 sec                                                     | 1.23 sec: 1.36x faster                                             |
| thrift                   | 1.18 ms                                                      | 882 us: 1.33x faster                                               |
| regex_compile            | 190 ms                                                       | 143 ms: 1.33x faster                                               |
| deepcopy_memo            | 49.8 us                                                      | 37.7 us: 1.32x faster                                              |
| tornado_http             | 157 ms                                                       | 119 ms: 1.32x faster                                               |
| fannkuch                 | 483 ms                                                       | 369 ms: 1.31x faster                                               |
| json_dumps               | 14.5 ms                                                      | 11.2 ms: 1.30x faster                                              |
| pprint_pformat           | 2.15 sec                                                     | 1.68 sec: 1.28x faster                                             |
| chameleon                | 9.44 ms                                                      | 7.37 ms: 1.28x faster                                              |
| django_template          | 50.2 ms                                                      | 39.3 ms: 1.28x faster                                              |
| pprint_safe_repr         | 1.05 sec                                                     | 823 ms: 1.28x faster                                               |
| json_loads               | 30.3 us                                                      | 23.8 us: 1.28x faster                                              |
| bench_thread_pool        | 1.14 ms                                                      | 897 us: 1.27x faster                                               |
| html5lib                 | 94.6 ms                                                      | 74.6 ms: 1.27x faster                                              |
| nqueens                  | 115 ms                                                       | 91.1 ms: 1.26x faster                                              |
| xml_etree_process        | 75.9 ms                                                      | 60.9 ms: 1.25x faster                                              |
| dulwich_log              | 81.1 ms                                                      | 65.1 ms: 1.25x faster                                              |
| sympy_sum                | 193 ms                                                       | 155 ms: 1.24x faster                                               |
| pathlib                  | 21.4 ms                                                      | 17.2 ms: 1.24x faster                                              |
| deepcopy                 | 468 us                                                       | 381 us: 1.23x faster                                               |
| mypy2                    | 933 ms                                                       | 769 ms: 1.21x faster                                               |
| sympy_str                | 360 ms                                                       | 299 ms: 1.20x faster                                               |
| tomli_loads              | 2.92 sec                                                     | 2.42 sec: 1.20x faster                                             |
| 2to3                     | 350 ms                                                       | 291 ms: 1.20x faster                                               |
| sympy_integrate          | 28.2 ms                                                      | 23.5 ms: 1.20x faster                                              |
| scimark_fft              | 361 ms                                                       | 302 ms: 1.20x faster                                               |
| dask                     | 472 ms                                                       | 396 ms: 1.19x faster                                               |
| genshi_text              | 31.4 ms                                                      | 26.4 ms: 1.19x faster                                              |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 4.28 ms: 1.19x faster                                              |
| mdp                      | 3.01 sec                                                     | 2.55 sec: 1.18x faster                                             |
| sympy_expand             | 600 ms                                                       | 509 ms: 1.18x faster                                               |
| sqlglot_normalize        | 144 ms                                                       | 122 ms: 1.18x faster                                               |
| sqlglot_optimize         | 70.1 ms                                                      | 60.1 ms: 1.17x faster                                              |
| deepcopy_reduce          | 4.01 us                                                      | 3.44 us: 1.16x faster                                              |
| async_generators         | 421 ms                                                       | 368 ms: 1.14x faster                                               |
| unpack_sequence          | 59.9 ns                                                      | 52.6 ns: 1.14x faster                                              |
| docutils                 | 3.41 sec                                                     | 3.00 sec: 1.14x faster                                             |
| json                     | 5.86 ms                                                      | 5.19 ms: 1.13x faster                                              |
| gunicorn                 | 1.16 ms                                                      | 1.04 ms: 1.11x faster                                              |
| xml_etree_parse          | 160 ms                                                       | 144 ms: 1.11x faster                                               |
| genshi_xml               | 63.3 ms                                                      | 57.2 ms: 1.11x faster                                              |
| aiohttp                  | 1.19 ms                                                      | 1.10 ms: 1.08x faster                                              |
| xml_etree_iterparse      | 110 ms                                                       | 103 ms: 1.08x faster                                               |
| meteor_contest           | 138 ms                                                       | 129 ms: 1.07x faster                                               |
| regex_v8                 | 27.2 ms                                                      | 25.4 ms: 1.07x faster                                              |
| pidigits                 | 271 ms                                                       | 254 ms: 1.07x faster                                               |
| xml_etree_generate       | 92.3 ms                                                      | 87.4 ms: 1.06x faster                                              |
| regex_dna                | 261 ms                                                       | 248 ms: 1.06x faster                                               |
| sqlite_synth             | 2.99 us                                                      | 2.84 us: 1.05x faster                                              |
| unpickle_list            | 4.65 us                                                      | 4.56 us: 1.02x faster                                              |
| pickle                   | 9.89 us                                                      | 10.5 us: 1.06x slower                                              |
| pickle_dict              | 29.5 us                                                      | 31.7 us: 1.07x slower                                              |
| flaskblogging            | 4.39 ms                                                      | 4.72 ms: 1.08x slower                                              |
| unpickle                 | 13.5 us                                                      | 15.0 us: 1.11x slower                                              |
| pickle_list              | 4.12 us                                                      | 4.59 us: 1.12x slower                                              |
| create_gc_cycles         | 1.76 ms                                                      | 2.00 ms: 1.14x slower                                              |
| python_startup           | 11.5 ms                                                      | 13.3 ms: 1.16x slower                                              |
| telco                    | 7.23 ms                                                      | 8.65 ms: 1.20x slower                                              |
| regex_effbot             | 3.09 ms                                                      | 3.74 ms: 1.21x slower                                              |
| python_startup_no_site   | 7.33 ms                                                      | 8.93 ms: 1.22x slower                                              |
| coverage                 | 63.3 ms                                                      | 80.4 ms: 1.27x slower                                              |
| gc_traversal             | 3.42 ms                                                      | 4.49 ms: 1.31x slower                                              |
| Geometric mean           | (ref)                                                        | 1.28x faster                                                       |

Benchmark hidden because not significant (1): asyncio_websockets
Ignored benchmarks (2) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of results/bm-20240906-3.13.0rc2-ec61006/bm-20240906-pythonperf2-x86_64-python-v3.13.0rc2-3.13.0rc2-ec61006.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

- Geometric mean (including insignificant results): 1.288x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.23x
- 95% likely to have a speedup of 1.21x
- 99% likely to have a speedup of 1.20x

# Memory
- memory change: 1.13x
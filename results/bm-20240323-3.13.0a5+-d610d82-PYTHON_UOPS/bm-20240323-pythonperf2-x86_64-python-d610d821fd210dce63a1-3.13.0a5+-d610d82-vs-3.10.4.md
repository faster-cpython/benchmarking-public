# Results vs. 3.10.4

- fork: python
- ref: d610d821fd210dce63a1
- machine: linux-x86_64
- commit hash: d610d82
- commit date: 2024-03-23
- overall geometric mean: 1.15x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x faster
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240323-pythonperf2-x86_64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 320 ms: 1.09x faster                                                         |
| chameleon      | 9.44 ms                                                      | 7.82 ms: 1.21x faster                                                        |
| docutils       | 3.41 sec                                                     | 3.20 sec: 1.07x faster                                                       |
| html5lib       | 94.6 ms                                                      | 77.2 ms: 1.23x faster                                                        |
| tornado_http   | 157 ms                                                       | 127 ms: 1.24x faster                                                         |
| Geometric mean | (ref)                                                        | 1.16x faster                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240323-pythonperf2-x86_64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|-------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization  | 819 ms                                                       | 453 ms: 1.81x faster                                                         |
| async_tree_io           | 1.60 sec                                                     | 886 ms: 1.80x faster                                                         |
| async_tree_none         | 692 ms                                                       | 395 ms: 1.75x faster                                                         |
| async_tree_cpu_io_mixed | 936 ms                                                       | 617 ms: 1.52x faster                                                         |
| Geometric mean          | (ref)                                                        | 1.72x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240323-pythonperf2-x86_64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 111 ms                                                       | 101 ms: 1.10x faster                                                         |
| nbody          | 134 ms                                                       | 130 ms: 1.03x faster                                                         |
| pidigits       | 271 ms                                                       | 265 ms: 1.02x faster                                                         |
| Geometric mean | (ref)                                                        | 1.05x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240323-pythonperf2-x86_64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_dna      | 261 ms                                                       | 241 ms: 1.08x faster                                                         |
| regex_v8       | 27.2 ms                                                      | 25.8 ms: 1.05x faster                                                        |
| regex_compile  | 190 ms                                                       | 204 ms: 1.07x slower                                                         |
| regex_effbot   | 3.09 ms                                                      | 3.61 ms: 1.17x slower                                                        |
| Geometric mean | (ref)                                                        | 1.02x slower                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240323-pythonperf2-x86_64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                       | 316 us: 1.44x faster                                                         |
| json_dumps           | 14.5 ms                                                      | 10.7 ms: 1.36x faster                                                        |
| xml_etree_process    | 75.9 ms                                                      | 62.4 ms: 1.22x faster                                                        |
| json_loads           | 30.3 us                                                      | 25.2 us: 1.20x faster                                                        |
| xml_etree_parse      | 160 ms                                                       | 146 ms: 1.10x faster                                                         |
| unpickle_pure_python | 312 us                                                       | 303 us: 1.03x faster                                                         |
| xml_etree_generate   | 92.3 ms                                                      | 90.3 ms: 1.02x faster                                                        |
| tomli_loads          | 2.92 sec                                                     | 2.90 sec: 1.01x faster                                                       |
| xml_etree_iterparse  | 110 ms                                                       | 115 ms: 1.04x slower                                                         |
| pickle               | 9.89 us                                                      | 10.3 us: 1.04x slower                                                        |
| pickle_dict          | 29.5 us                                                      | 31.2 us: 1.06x slower                                                        |
| pickle_list          | 4.12 us                                                      | 4.41 us: 1.07x slower                                                        |
| unpickle             | 13.5 us                                                      | 15.1 us: 1.12x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.06x faster                                                                 |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240323-pythonperf2-x86_64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 12.8 ms: 1.12x slower                                                        |
| python_startup_no_site | 7.33 ms                                                      | 11.1 ms: 1.51x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.30x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240323-pythonperf2-x86_64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| django_template | 50.2 ms                                                      | 42.2 ms: 1.19x faster                                                        |
| genshi_text     | 31.4 ms                                                      | 29.6 ms: 1.06x faster                                                        |
| genshi_xml      | 63.3 ms                                                      | 62.1 ms: 1.02x faster                                                        |
| mako            | 14.7 ms                                                      | 14.5 ms: 1.01x faster                                                        |
| Geometric mean  | (ref)                                                        | 1.07x faster                                                                 |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240323-pythonperf2-x86_64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|--------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 129 us: 4.17x faster                                                         |
| asyncio_tcp              | 779 ms                                                       | 373 ms: 2.09x faster                                                         |
| asyncio_tcp_ssl          | 3.10 sec                                                     | 1.59 sec: 1.95x faster                                                       |
| deltablue                | 7.50 ms                                                      | 3.98 ms: 1.89x faster                                                        |
| async_tree_memoization   | 819 ms                                                       | 453 ms: 1.81x faster                                                         |
| async_tree_io            | 1.60 sec                                                     | 886 ms: 1.80x faster                                                         |
| async_tree_none          | 692 ms                                                       | 395 ms: 1.75x faster                                                         |
| generators               | 57.3 ms                                                      | 33.6 ms: 1.71x faster                                                        |
| logging_silent           | 167 ns                                                       | 101 ns: 1.65x faster                                                         |
| pylint                   | 566 ms                                                       | 369 ms: 1.53x faster                                                         |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 617 ms: 1.52x faster                                                         |
| pickle_pure_python       | 455 us                                                       | 316 us: 1.44x faster                                                         |
| sqlglot_parse            | 2.24 ms                                                      | 1.55 ms: 1.44x faster                                                        |
| richards_super           | 90.6 ms                                                      | 64.8 ms: 1.40x faster                                                        |
| chaos                    | 109 ms                                                       | 77.9 ms: 1.39x faster                                                        |
| raytrace                 | 489 ms                                                       | 355 ms: 1.38x faster                                                         |
| sqlglot_transpile        | 2.68 ms                                                      | 1.96 ms: 1.37x faster                                                        |
| json_dumps               | 14.5 ms                                                      | 10.7 ms: 1.36x faster                                                        |
| thrift                   | 1.18 ms                                                      | 864 us: 1.36x faster                                                         |
| coroutines               | 30.3 ms                                                      | 22.5 ms: 1.35x faster                                                        |
| bench_mp_pool            | 6.37 ms                                                      | 4.79 ms: 1.33x faster                                                        |
| go                       | 262 ms                                                       | 199 ms: 1.32x faster                                                         |
| logging_simple           | 8.88 us                                                      | 6.76 us: 1.31x faster                                                        |
| logging_format           | 9.64 us                                                      | 7.39 us: 1.30x faster                                                        |
| crypto_pyaes             | 119 ms                                                       | 92.2 ms: 1.29x faster                                                        |
| richards                 | 75.1 ms                                                      | 58.3 ms: 1.29x faster                                                        |
| tornado_http             | 157 ms                                                       | 127 ms: 1.24x faster                                                         |
| pycparser                | 1.67 sec                                                     | 1.36 sec: 1.23x faster                                                       |
| html5lib                 | 94.6 ms                                                      | 77.2 ms: 1.23x faster                                                        |
| scimark_lu               | 167 ms                                                       | 137 ms: 1.22x faster                                                         |
| xml_etree_process        | 75.9 ms                                                      | 62.4 ms: 1.22x faster                                                        |
| chameleon                | 9.44 ms                                                      | 7.82 ms: 1.21x faster                                                        |
| json_loads               | 30.3 us                                                      | 25.2 us: 1.20x faster                                                        |
| django_template          | 50.2 ms                                                      | 42.2 ms: 1.19x faster                                                        |
| bench_thread_pool        | 1.14 ms                                                      | 962 us: 1.19x faster                                                         |
| deepcopy                 | 468 us                                                       | 396 us: 1.18x faster                                                         |
| deepcopy_reduce          | 4.01 us                                                      | 3.42 us: 1.17x faster                                                        |
| deepcopy_memo            | 49.8 us                                                      | 42.5 us: 1.17x faster                                                        |
| dask                     | 472 ms                                                       | 410 ms: 1.15x faster                                                         |
| mdp                      | 3.01 sec                                                     | 2.66 sec: 1.13x faster                                                       |
| sqlglot_normalize        | 144 ms                                                       | 128 ms: 1.13x faster                                                         |
| pyflate                  | 733 ms                                                       | 655 ms: 1.12x faster                                                         |
| scimark_sor              | 180 ms                                                       | 162 ms: 1.11x faster                                                         |
| create_gc_cycles         | 1.76 ms                                                      | 1.59 ms: 1.11x faster                                                        |
| mypy2                    | 933 ms                                                       | 844 ms: 1.11x faster                                                         |
| json                     | 5.86 ms                                                      | 5.31 ms: 1.10x faster                                                        |
| xml_etree_parse          | 160 ms                                                       | 146 ms: 1.10x faster                                                         |
| float                    | 111 ms                                                       | 101 ms: 1.10x faster                                                         |
| 2to3                     | 350 ms                                                       | 320 ms: 1.09x faster                                                         |
| sympy_sum                | 193 ms                                                       | 176 ms: 1.09x faster                                                         |
| pathlib                  | 21.4 ms                                                      | 19.6 ms: 1.09x faster                                                        |
| regex_dna                | 261 ms                                                       | 241 ms: 1.08x faster                                                         |
| sympy_integrate          | 28.2 ms                                                      | 26.1 ms: 1.08x faster                                                        |
| async_generators         | 421 ms                                                       | 390 ms: 1.08x faster                                                         |
| pprint_pformat           | 2.15 sec                                                     | 2.01 sec: 1.07x faster                                                       |
| pprint_safe_repr         | 1.05 sec                                                     | 980 ms: 1.07x faster                                                         |
| dulwich_log              | 81.1 ms                                                      | 75.8 ms: 1.07x faster                                                        |
| docutils                 | 3.41 sec                                                     | 3.20 sec: 1.07x faster                                                       |
| sqlite_synth             | 2.99 us                                                      | 2.81 us: 1.07x faster                                                        |
| gunicorn                 | 1.16 ms                                                      | 1.09 ms: 1.06x faster                                                        |
| genshi_text              | 31.4 ms                                                      | 29.6 ms: 1.06x faster                                                        |
| sympy_str                | 360 ms                                                       | 340 ms: 1.06x faster                                                         |
| sqlglot_optimize         | 70.1 ms                                                      | 66.3 ms: 1.06x faster                                                        |
| aiohttp                  | 1.19 ms                                                      | 1.12 ms: 1.06x faster                                                        |
| sympy_expand             | 600 ms                                                       | 568 ms: 1.06x faster                                                         |
| scimark_monte_carlo      | 107 ms                                                       | 102 ms: 1.06x faster                                                         |
| regex_v8                 | 27.2 ms                                                      | 25.8 ms: 1.05x faster                                                        |
| nbody                    | 134 ms                                                       | 130 ms: 1.03x faster                                                         |
| unpickle_pure_python     | 312 us                                                       | 303 us: 1.03x faster                                                         |
| pidigits                 | 271 ms                                                       | 265 ms: 1.02x faster                                                         |
| xml_etree_generate       | 92.3 ms                                                      | 90.3 ms: 1.02x faster                                                        |
| comprehensions           | 26.7 us                                                      | 26.1 us: 1.02x faster                                                        |
| genshi_xml               | 63.3 ms                                                      | 62.1 ms: 1.02x faster                                                        |
| mako                     | 14.7 ms                                                      | 14.5 ms: 1.01x faster                                                        |
| tomli_loads              | 2.92 sec                                                     | 2.90 sec: 1.01x faster                                                       |
| meteor_contest           | 138 ms                                                       | 143 ms: 1.03x slower                                                         |
| xml_etree_iterparse      | 110 ms                                                       | 115 ms: 1.04x slower                                                         |
| nqueens                  | 115 ms                                                       | 120 ms: 1.04x slower                                                         |
| pickle                   | 9.89 us                                                      | 10.3 us: 1.04x slower                                                        |
| pickle_dict              | 29.5 us                                                      | 31.2 us: 1.06x slower                                                        |
| pickle_list              | 4.12 us                                                      | 4.41 us: 1.07x slower                                                        |
| regex_compile            | 190 ms                                                       | 204 ms: 1.07x slower                                                         |
| fannkuch                 | 483 ms                                                       | 532 ms: 1.10x slower                                                         |
| hexiom                   | 9.42 ms                                                      | 10.4 ms: 1.10x slower                                                        |
| python_startup           | 11.5 ms                                                      | 12.8 ms: 1.12x slower                                                        |
| unpickle                 | 13.5 us                                                      | 15.1 us: 1.12x slower                                                        |
| unpack_sequence          | 59.9 ns                                                      | 68.7 ns: 1.15x slower                                                        |
| spectral_norm            | 139 ms                                                       | 160 ms: 1.15x slower                                                         |
| regex_effbot             | 3.09 ms                                                      | 3.61 ms: 1.17x slower                                                        |
| telco                    | 7.23 ms                                                      | 8.49 ms: 1.17x slower                                                        |
| scimark_fft              | 361 ms                                                       | 444 ms: 1.23x slower                                                         |
| coverage                 | 63.3 ms                                                      | 80.5 ms: 1.27x slower                                                        |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 6.61 ms: 1.30x slower                                                        |
| gc_traversal             | 3.42 ms                                                      | 4.59 ms: 1.34x slower                                                        |
| python_startup_no_site   | 7.33 ms                                                      | 11.1 ms: 1.51x slower                                                        |
| Geometric mean           | (ref)                                                        | 1.15x faster                                                                 |

Benchmark hidden because not significant (2): asyncio_websockets, unpickle_list
Ignored benchmarks (3) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: flaskblogging, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (4) of results/bm-20240323-3.13.0a5+-d610d82-PYTHON_UOPS/bm-20240323-pythonperf2-x86_64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.08x
- 95% likely to have a speedup of 1.07x
- 99% likely to have a speedup of 1.06x


# Memory

- memory change: 1.10x
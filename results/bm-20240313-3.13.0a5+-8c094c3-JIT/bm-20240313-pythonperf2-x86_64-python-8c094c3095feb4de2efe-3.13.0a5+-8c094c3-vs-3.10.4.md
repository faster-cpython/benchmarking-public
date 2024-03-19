# Results vs. 3.10.4

- fork: python
- ref: 8c094c3095feb4de2efe
- machine: linux-x86_64
- commit hash: 8c094c3
- commit date: 2024-03-13
- overall geometric mean: 1.24x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.17x faster
- Memory change: 1.35x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240313-pythonperf2-x86_64-python-8c094c3095feb4de2efe-3.13.0a5+-8c094c3 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 307 ms: 1.14x faster                                                         |
| chameleon      | 9.44 ms                                                      | 7.41 ms: 1.27x faster                                                        |
| docutils       | 3.41 sec                                                     | 2.92 sec: 1.17x faster                                                       |
| html5lib       | 94.6 ms                                                      | 74.7 ms: 1.27x faster                                                        |
| tornado_http   | 157 ms                                                       | 126 ms: 1.25x faster                                                         |
| Geometric mean | (ref)                                                        | 1.22x faster                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240313-pythonperf2-x86_64-python-8c094c3095feb4de2efe-3.13.0a5+-8c094c3 |
|-------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_none         | 692 ms                                                       | 442 ms: 1.57x faster                                                         |
| async_tree_memoization  | 819 ms                                                       | 554 ms: 1.48x faster                                                         |
| async_tree_io           | 1.60 sec                                                     | 1.09 sec: 1.46x faster                                                       |
| async_tree_cpu_io_mixed | 936 ms                                                       | 709 ms: 1.32x faster                                                         |
| Geometric mean          | (ref)                                                        | 1.45x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240313-pythonperf2-x86_64-python-8c094c3095feb4de2efe-3.13.0a5+-8c094c3 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| nbody          | 134 ms                                                       | 94.5 ms: 1.42x faster                                                        |
| float          | 111 ms                                                       | 78.7 ms: 1.41x faster                                                        |
| pidigits       | 271 ms                                                       | 261 ms: 1.04x faster                                                         |
| Geometric mean | (ref)                                                        | 1.28x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240313-pythonperf2-x86_64-python-8c094c3095feb4de2efe-3.13.0a5+-8c094c3 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 146 ms: 1.30x faster                                                         |
| regex_v8       | 27.2 ms                                                      | 25.5 ms: 1.06x faster                                                        |
| regex_dna      | 261 ms                                                       | 253 ms: 1.03x faster                                                         |
| regex_effbot   | 3.09 ms                                                      | 3.56 ms: 1.15x slower                                                        |
| Geometric mean | (ref)                                                        | 1.06x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240313-pythonperf2-x86_64-python-8c094c3095feb4de2efe-3.13.0a5+-8c094c3 |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                       | 310 us: 1.47x faster                                                         |
| json_dumps           | 14.5 ms                                                      | 10.6 ms: 1.37x faster                                                        |
| tomli_loads          | 2.92 sec                                                     | 2.14 sec: 1.36x faster                                                       |
| unpickle_pure_python | 312 us                                                       | 234 us: 1.33x faster                                                         |
| xml_etree_process    | 75.9 ms                                                      | 58.8 ms: 1.29x faster                                                        |
| json_loads           | 30.3 us                                                      | 25.0 us: 1.22x faster                                                        |
| xml_etree_parse      | 160 ms                                                       | 146 ms: 1.10x faster                                                         |
| xml_etree_generate   | 92.3 ms                                                      | 86.0 ms: 1.07x faster                                                        |
| xml_etree_iterparse  | 110 ms                                                       | 104 ms: 1.06x faster                                                         |
| unpickle_list        | 4.65 us                                                      | 4.60 us: 1.01x faster                                                        |
| pickle_dict          | 29.5 us                                                      | 30.5 us: 1.04x slower                                                        |
| pickle               | 9.89 us                                                      | 10.3 us: 1.04x slower                                                        |
| pickle_list          | 4.12 us                                                      | 4.30 us: 1.05x slower                                                        |
| unpickle             | 13.5 us                                                      | 14.9 us: 1.10x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.13x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240313-pythonperf2-x86_64-python-8c094c3095feb4de2efe-3.13.0a5+-8c094c3 |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 15.6 ms: 1.35x slower                                                        |
| python_startup_no_site | 7.33 ms                                                      | 14.1 ms: 1.92x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.61x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240313-pythonperf2-x86_64-python-8c094c3095feb4de2efe-3.13.0a5+-8c094c3 |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 9.75 ms: 1.51x faster                                                        |
| django_template | 50.2 ms                                                      | 39.4 ms: 1.27x faster                                                        |
| genshi_text     | 31.4 ms                                                      | 28.2 ms: 1.11x faster                                                        |
| genshi_xml      | 63.3 ms                                                      | 60.6 ms: 1.04x faster                                                        |
| Geometric mean  | (ref)                                                        | 1.22x faster                                                                 |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240313-pythonperf2-x86_64-python-8c094c3095feb4de2efe-3.13.0a5+-8c094c3 |
|--------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 117 us: 4.58x faster                                                         |
| asyncio_tcp              | 779 ms                                                       | 376 ms: 2.07x faster                                                         |
| deltablue                | 7.50 ms                                                      | 3.76 ms: 2.00x faster                                                        |
| asyncio_tcp_ssl          | 3.10 sec                                                     | 1.58 sec: 1.96x faster                                                       |
| logging_silent           | 167 ns                                                       | 98.0 ns: 1.71x faster                                                        |
| generators               | 57.3 ms                                                      | 33.9 ms: 1.69x faster                                                        |
| richards_super           | 90.6 ms                                                      | 56.2 ms: 1.61x faster                                                        |
| chaos                    | 109 ms                                                       | 67.6 ms: 1.61x faster                                                        |
| pylint                   | 566 ms                                                       | 358 ms: 1.58x faster                                                         |
| sqlglot_parse            | 2.24 ms                                                      | 1.43 ms: 1.57x faster                                                        |
| async_tree_none          | 692 ms                                                       | 442 ms: 1.57x faster                                                         |
| raytrace                 | 489 ms                                                       | 312 ms: 1.57x faster                                                         |
| crypto_pyaes             | 119 ms                                                       | 77.8 ms: 1.53x faster                                                        |
| go                       | 262 ms                                                       | 174 ms: 1.51x faster                                                         |
| mako                     | 14.7 ms                                                      | 9.75 ms: 1.51x faster                                                        |
| richards                 | 75.1 ms                                                      | 50.5 ms: 1.49x faster                                                        |
| async_tree_memoization   | 819 ms                                                       | 554 ms: 1.48x faster                                                         |
| spectral_norm            | 139 ms                                                       | 94.4 ms: 1.47x faster                                                        |
| pickle_pure_python       | 455 us                                                       | 310 us: 1.47x faster                                                         |
| async_tree_io            | 1.60 sec                                                     | 1.09 sec: 1.46x faster                                                       |
| sqlglot_transpile        | 2.68 ms                                                      | 1.85 ms: 1.45x faster                                                        |
| nbody                    | 134 ms                                                       | 94.5 ms: 1.42x faster                                                        |
| float                    | 111 ms                                                       | 78.7 ms: 1.41x faster                                                        |
| scimark_monte_carlo      | 107 ms                                                       | 76.2 ms: 1.41x faster                                                        |
| comprehensions           | 26.7 us                                                      | 19.0 us: 1.40x faster                                                        |
| pyflate                  | 733 ms                                                       | 524 ms: 1.40x faster                                                         |
| json_dumps               | 14.5 ms                                                      | 10.6 ms: 1.37x faster                                                        |
| scimark_lu               | 167 ms                                                       | 122 ms: 1.37x faster                                                         |
| thrift                   | 1.18 ms                                                      | 862 us: 1.36x faster                                                         |
| tomli_loads              | 2.92 sec                                                     | 2.14 sec: 1.36x faster                                                       |
| coroutines               | 30.3 ms                                                      | 22.4 ms: 1.35x faster                                                        |
| unpickle_pure_python     | 312 us                                                       | 234 us: 1.33x faster                                                         |
| deepcopy_memo            | 49.8 us                                                      | 37.6 us: 1.33x faster                                                        |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 709 ms: 1.32x faster                                                         |
| logging_simple           | 8.88 us                                                      | 6.76 us: 1.31x faster                                                        |
| regex_compile            | 190 ms                                                       | 146 ms: 1.30x faster                                                         |
| hexiom                   | 9.42 ms                                                      | 7.25 ms: 1.30x faster                                                        |
| xml_etree_process        | 75.9 ms                                                      | 58.8 ms: 1.29x faster                                                        |
| logging_format           | 9.64 us                                                      | 7.49 us: 1.29x faster                                                        |
| pycparser                | 1.67 sec                                                     | 1.31 sec: 1.28x faster                                                       |
| chameleon                | 9.44 ms                                                      | 7.41 ms: 1.27x faster                                                        |
| django_template          | 50.2 ms                                                      | 39.4 ms: 1.27x faster                                                        |
| html5lib                 | 94.6 ms                                                      | 74.7 ms: 1.27x faster                                                        |
| deepcopy                 | 468 us                                                       | 370 us: 1.26x faster                                                         |
| pprint_safe_repr         | 1.05 sec                                                     | 836 ms: 1.26x faster                                                         |
| pprint_pformat           | 2.15 sec                                                     | 1.72 sec: 1.26x faster                                                       |
| tornado_http             | 157 ms                                                       | 126 ms: 1.25x faster                                                         |
| fannkuch                 | 483 ms                                                       | 396 ms: 1.22x faster                                                         |
| deepcopy_reduce          | 4.01 us                                                      | 3.29 us: 1.22x faster                                                        |
| json_loads               | 30.3 us                                                      | 25.0 us: 1.22x faster                                                        |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 4.19 ms: 1.21x faster                                                        |
| sympy_sum                | 193 ms                                                       | 160 ms: 1.20x faster                                                         |
| sympy_str                | 360 ms                                                       | 302 ms: 1.19x faster                                                         |
| scimark_sor              | 180 ms                                                       | 152 ms: 1.19x faster                                                         |
| dulwich_log              | 81.1 ms                                                      | 68.7 ms: 1.18x faster                                                        |
| bench_thread_pool        | 1.14 ms                                                      | 972 us: 1.17x faster                                                         |
| sympy_expand             | 600 ms                                                       | 511 ms: 1.17x faster                                                         |
| docutils                 | 3.41 sec                                                     | 2.92 sec: 1.17x faster                                                       |
| dask                     | 472 ms                                                       | 406 ms: 1.16x faster                                                         |
| mdp                      | 3.01 sec                                                     | 2.60 sec: 1.16x faster                                                       |
| sympy_integrate          | 28.2 ms                                                      | 24.6 ms: 1.14x faster                                                        |
| 2to3                     | 350 ms                                                       | 307 ms: 1.14x faster                                                         |
| nqueens                  | 115 ms                                                       | 102 ms: 1.13x faster                                                         |
| sqlglot_normalize        | 144 ms                                                       | 128 ms: 1.12x faster                                                         |
| create_gc_cycles         | 1.76 ms                                                      | 1.58 ms: 1.12x faster                                                        |
| genshi_text              | 31.4 ms                                                      | 28.2 ms: 1.11x faster                                                        |
| scimark_fft              | 361 ms                                                       | 325 ms: 1.11x faster                                                         |
| sqlite_synth             | 2.99 us                                                      | 2.69 us: 1.11x faster                                                        |
| sqlglot_optimize         | 70.1 ms                                                      | 63.3 ms: 1.11x faster                                                        |
| xml_etree_parse          | 160 ms                                                       | 146 ms: 1.10x faster                                                         |
| pathlib                  | 21.4 ms                                                      | 19.4 ms: 1.10x faster                                                        |
| async_generators         | 421 ms                                                       | 384 ms: 1.10x faster                                                         |
| json                     | 5.86 ms                                                      | 5.41 ms: 1.08x faster                                                        |
| xml_etree_generate       | 92.3 ms                                                      | 86.0 ms: 1.07x faster                                                        |
| regex_v8                 | 27.2 ms                                                      | 25.5 ms: 1.06x faster                                                        |
| xml_etree_iterparse      | 110 ms                                                       | 104 ms: 1.06x faster                                                         |
| gunicorn                 | 1.16 ms                                                      | 1.09 ms: 1.06x faster                                                        |
| aiohttp                  | 1.19 ms                                                      | 1.12 ms: 1.06x faster                                                        |
| meteor_contest           | 138 ms                                                       | 131 ms: 1.05x faster                                                         |
| genshi_xml               | 63.3 ms                                                      | 60.6 ms: 1.04x faster                                                        |
| pidigits                 | 271 ms                                                       | 261 ms: 1.04x faster                                                         |
| regex_dna                | 261 ms                                                       | 253 ms: 1.03x faster                                                         |
| unpickle_list            | 4.65 us                                                      | 4.60 us: 1.01x faster                                                        |
| asyncio_websockets       | 390 ms                                                       | 386 ms: 1.01x faster                                                         |
| pickle_dict              | 29.5 us                                                      | 30.5 us: 1.04x slower                                                        |
| unpack_sequence          | 59.9 ns                                                      | 62.2 ns: 1.04x slower                                                        |
| pickle                   | 9.89 us                                                      | 10.3 us: 1.04x slower                                                        |
| pickle_list              | 4.12 us                                                      | 4.30 us: 1.05x slower                                                        |
| unpickle                 | 13.5 us                                                      | 14.9 us: 1.10x slower                                                        |
| bench_mp_pool            | 6.37 ms                                                      | 7.02 ms: 1.10x slower                                                        |
| telco                    | 7.23 ms                                                      | 8.13 ms: 1.13x slower                                                        |
| gc_traversal             | 3.42 ms                                                      | 3.92 ms: 1.15x slower                                                        |
| regex_effbot             | 3.09 ms                                                      | 3.56 ms: 1.15x slower                                                        |
| coverage                 | 63.3 ms                                                      | 80.3 ms: 1.27x slower                                                        |
| python_startup           | 11.5 ms                                                      | 15.6 ms: 1.35x slower                                                        |
| python_startup_no_site   | 7.33 ms                                                      | 14.1 ms: 1.92x slower                                                        |
| Geometric mean           | (ref)                                                        | 1.24x faster                                                                 |

Benchmark hidden because not significant (1): mypy2
Ignored benchmarks (3) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: flaskblogging, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (4) of results/bm-20240313-3.13.0a5+-8c094c3-JIT/bm-20240313-pythonperf2-x86_64-python-8c094c3095feb4de2efe-3.13.0a5+-8c094c3.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.19x
- 95% likely to have a speedup of 1.19x
- 99% likely to have a speedup of 1.17x


# Memory

- memory change: 1.35x
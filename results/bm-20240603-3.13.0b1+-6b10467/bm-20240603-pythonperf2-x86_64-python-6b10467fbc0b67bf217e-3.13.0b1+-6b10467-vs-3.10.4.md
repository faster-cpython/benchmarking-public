# Results vs. 3.10.4

- fork: python
- ref: 6b10467fbc0b67bf217e
- machine: linux-x86_64
- commit hash: 6b10467
- commit date: 2024-06-03
- overall geometric mean: 1.28x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.21x faster
- Memory change: 1.12x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240603-pythonperf2-x86_64-python-6b10467fbc0b67bf217e-3.13.0b1+-6b10467 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 292 ms: 1.20x faster                                                         |
| chameleon      | 9.44 ms                                                      | 7.49 ms: 1.26x faster                                                        |
| docutils       | 3.41 sec                                                     | 2.98 sec: 1.14x faster                                                       |
| html5lib       | 94.6 ms                                                      | 74.2 ms: 1.27x faster                                                        |
| tornado_http   | 157 ms                                                       | 118 ms: 1.33x faster                                                         |
| Geometric mean | (ref)                                                        | 1.24x faster                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240603-pythonperf2-x86_64-python-6b10467fbc0b67bf217e-3.13.0b1+-6b10467 |
|-------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_none         | 692 ms                                                       | 368 ms: 1.88x faster                                                         |
| async_tree_io           | 1.60 sec                                                     | 897 ms: 1.78x faster                                                         |
| async_tree_memoization  | 819 ms                                                       | 467 ms: 1.76x faster                                                         |
| async_tree_cpu_io_mixed | 936 ms                                                       | 612 ms: 1.53x faster                                                         |
| Geometric mean          | (ref)                                                        | 1.73x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240603-pythonperf2-x86_64-python-6b10467fbc0b67bf217e-3.13.0b1+-6b10467 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| nbody          | 134 ms                                                       | 89.0 ms: 1.51x faster                                                        |
| float          | 111 ms                                                       | 79.8 ms: 1.39x faster                                                        |
| pidigits       | 271 ms                                                       | 253 ms: 1.07x faster                                                         |
| Geometric mean | (ref)                                                        | 1.31x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240603-pythonperf2-x86_64-python-6b10467fbc0b67bf217e-3.13.0b1+-6b10467 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 143 ms: 1.33x faster                                                         |
| regex_dna      | 261 ms                                                       | 245 ms: 1.06x faster                                                         |
| regex_v8       | 27.2 ms                                                      | 26.1 ms: 1.04x faster                                                        |
| regex_effbot   | 3.09 ms                                                      | 3.48 ms: 1.13x slower                                                        |
| Geometric mean | (ref)                                                        | 1.07x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240603-pythonperf2-x86_64-python-6b10467fbc0b67bf217e-3.13.0b1+-6b10467 |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| unpickle_pure_python | 312 us                                                       | 210 us: 1.49x faster                                                         |
| pickle_pure_python   | 455 us                                                       | 314 us: 1.45x faster                                                         |
| json_dumps           | 14.5 ms                                                      | 10.7 ms: 1.36x faster                                                        |
| xml_etree_process    | 75.9 ms                                                      | 59.9 ms: 1.27x faster                                                        |
| json_loads           | 30.3 us                                                      | 24.6 us: 1.23x faster                                                        |
| tomli_loads          | 2.92 sec                                                     | 2.39 sec: 1.22x faster                                                       |
| xml_etree_parse      | 160 ms                                                       | 145 ms: 1.10x faster                                                         |
| xml_etree_generate   | 92.3 ms                                                      | 85.5 ms: 1.08x faster                                                        |
| xml_etree_iterparse  | 110 ms                                                       | 103 ms: 1.07x faster                                                         |
| pickle_dict          | 29.5 us                                                      | 30.1 us: 1.02x slower                                                        |
| unpickle_list        | 4.65 us                                                      | 4.79 us: 1.03x slower                                                        |
| pickle               | 9.89 us                                                      | 10.3 us: 1.04x slower                                                        |
| pickle_list          | 4.12 us                                                      | 4.30 us: 1.04x slower                                                        |
| unpickle             | 13.5 us                                                      | 15.4 us: 1.14x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.13x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240603-pythonperf2-x86_64-python-6b10467fbc0b67bf217e-3.13.0b1+-6b10467 |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 13.2 ms: 1.15x slower                                                        |
| python_startup_no_site | 7.33 ms                                                      | 8.82 ms: 1.20x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.17x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240603-pythonperf2-x86_64-python-6b10467fbc0b67bf217e-3.13.0b1+-6b10467 |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 10.3 ms: 1.42x faster                                                        |
| django_template | 50.2 ms                                                      | 39.4 ms: 1.27x faster                                                        |
| genshi_text     | 31.4 ms                                                      | 25.8 ms: 1.22x faster                                                        |
| genshi_xml      | 63.3 ms                                                      | 55.2 ms: 1.15x faster                                                        |
| Geometric mean  | (ref)                                                        | 1.26x faster                                                                 |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240603-pythonperf2-x86_64-python-6b10467fbc0b67bf217e-3.13.0b1+-6b10467 |
|--------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 175 us: 3.07x faster                                                         |
| deltablue                | 7.50 ms                                                      | 3.33 ms: 2.25x faster                                                        |
| asyncio_tcp              | 779 ms                                                       | 378 ms: 2.06x faster                                                         |
| asyncio_tcp_ssl          | 3.10 sec                                                     | 1.58 sec: 1.97x faster                                                       |
| async_tree_none          | 692 ms                                                       | 368 ms: 1.88x faster                                                         |
| async_tree_io            | 1.60 sec                                                     | 897 ms: 1.78x faster                                                         |
| raytrace                 | 489 ms                                                       | 276 ms: 1.77x faster                                                         |
| chaos                    | 109 ms                                                       | 61.4 ms: 1.77x faster                                                        |
| async_tree_memoization   | 819 ms                                                       | 467 ms: 1.76x faster                                                         |
| logging_silent           | 167 ns                                                       | 95.8 ns: 1.75x faster                                                        |
| generators               | 57.3 ms                                                      | 33.2 ms: 1.73x faster                                                        |
| scimark_lu               | 167 ms                                                       | 98.4 ms: 1.70x faster                                                        |
| pylint                   | 566 ms                                                       | 341 ms: 1.66x faster                                                         |
| go                       | 262 ms                                                       | 158 ms: 1.65x faster                                                         |
| crypto_pyaes             | 119 ms                                                       | 73.5 ms: 1.62x faster                                                        |
| scimark_monte_carlo      | 107 ms                                                       | 67.1 ms: 1.60x faster                                                        |
| comprehensions           | 26.7 us                                                      | 17.0 us: 1.57x faster                                                        |
| sqlglot_parse            | 2.24 ms                                                      | 1.43 ms: 1.57x faster                                                        |
| scimark_sor              | 180 ms                                                       | 118 ms: 1.53x faster                                                         |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 612 ms: 1.53x faster                                                         |
| pyflate                  | 733 ms                                                       | 481 ms: 1.52x faster                                                         |
| richards_super           | 90.6 ms                                                      | 59.8 ms: 1.52x faster                                                        |
| nbody                    | 134 ms                                                       | 89.0 ms: 1.51x faster                                                        |
| hexiom                   | 9.42 ms                                                      | 6.31 ms: 1.49x faster                                                        |
| unpickle_pure_python     | 312 us                                                       | 210 us: 1.49x faster                                                         |
| sqlglot_transpile        | 2.68 ms                                                      | 1.81 ms: 1.48x faster                                                        |
| pickle_pure_python       | 455 us                                                       | 314 us: 1.45x faster                                                         |
| spectral_norm            | 139 ms                                                       | 96.9 ms: 1.44x faster                                                        |
| mako                     | 14.7 ms                                                      | 10.3 ms: 1.42x faster                                                        |
| richards                 | 75.1 ms                                                      | 53.4 ms: 1.41x faster                                                        |
| float                    | 111 ms                                                       | 79.8 ms: 1.39x faster                                                        |
| coroutines               | 30.3 ms                                                      | 21.9 ms: 1.38x faster                                                        |
| json_dumps               | 14.5 ms                                                      | 10.7 ms: 1.36x faster                                                        |
| logging_simple           | 8.88 us                                                      | 6.52 us: 1.36x faster                                                        |
| logging_format           | 9.64 us                                                      | 7.09 us: 1.36x faster                                                        |
| pycparser                | 1.67 sec                                                     | 1.24 sec: 1.35x faster                                                       |
| bench_mp_pool            | 6.37 ms                                                      | 4.76 ms: 1.34x faster                                                        |
| tornado_http             | 157 ms                                                       | 118 ms: 1.33x faster                                                         |
| regex_compile            | 190 ms                                                       | 143 ms: 1.33x faster                                                         |
| thrift                   | 1.18 ms                                                      | 896 us: 1.31x faster                                                         |
| fannkuch                 | 483 ms                                                       | 368 ms: 1.31x faster                                                         |
| deepcopy_memo            | 49.8 us                                                      | 38.0 us: 1.31x faster                                                        |
| nqueens                  | 115 ms                                                       | 88.7 ms: 1.30x faster                                                        |
| pprint_pformat           | 2.15 sec                                                     | 1.67 sec: 1.29x faster                                                       |
| pprint_safe_repr         | 1.05 sec                                                     | 823 ms: 1.28x faster                                                         |
| html5lib                 | 94.6 ms                                                      | 74.2 ms: 1.27x faster                                                        |
| django_template          | 50.2 ms                                                      | 39.4 ms: 1.27x faster                                                        |
| bench_thread_pool        | 1.14 ms                                                      | 898 us: 1.27x faster                                                         |
| xml_etree_process        | 75.9 ms                                                      | 59.9 ms: 1.27x faster                                                        |
| chameleon                | 9.44 ms                                                      | 7.49 ms: 1.26x faster                                                        |
| sympy_sum                | 193 ms                                                       | 154 ms: 1.25x faster                                                         |
| pathlib                  | 21.4 ms                                                      | 17.2 ms: 1.24x faster                                                        |
| deepcopy                 | 468 us                                                       | 378 us: 1.24x faster                                                         |
| json_loads               | 30.3 us                                                      | 24.6 us: 1.23x faster                                                        |
| tomli_loads              | 2.92 sec                                                     | 2.39 sec: 1.22x faster                                                       |
| genshi_text              | 31.4 ms                                                      | 25.8 ms: 1.22x faster                                                        |
| sympy_str                | 360 ms                                                       | 295 ms: 1.22x faster                                                         |
| mypy2                    | 933 ms                                                       | 769 ms: 1.21x faster                                                         |
| mdp                      | 3.01 sec                                                     | 2.49 sec: 1.21x faster                                                       |
| sympy_integrate          | 28.2 ms                                                      | 23.4 ms: 1.20x faster                                                        |
| dulwich_log              | 81.1 ms                                                      | 67.3 ms: 1.20x faster                                                        |
| dask                     | 472 ms                                                       | 393 ms: 1.20x faster                                                         |
| 2to3                     | 350 ms                                                       | 292 ms: 1.20x faster                                                         |
| sympy_expand             | 600 ms                                                       | 504 ms: 1.19x faster                                                         |
| sqlglot_normalize        | 144 ms                                                       | 122 ms: 1.18x faster                                                         |
| sqlglot_optimize         | 70.1 ms                                                      | 59.9 ms: 1.17x faster                                                        |
| deepcopy_reduce          | 4.01 us                                                      | 3.43 us: 1.17x faster                                                        |
| scimark_fft              | 361 ms                                                       | 311 ms: 1.16x faster                                                         |
| async_generators         | 421 ms                                                       | 363 ms: 1.16x faster                                                         |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 4.42 ms: 1.15x faster                                                        |
| genshi_xml               | 63.3 ms                                                      | 55.2 ms: 1.15x faster                                                        |
| docutils                 | 3.41 sec                                                     | 2.98 sec: 1.14x faster                                                       |
| json                     | 5.86 ms                                                      | 5.26 ms: 1.12x faster                                                        |
| gunicorn                 | 1.16 ms                                                      | 1.05 ms: 1.10x faster                                                        |
| xml_etree_parse          | 160 ms                                                       | 145 ms: 1.10x faster                                                         |
| aiohttp                  | 1.19 ms                                                      | 1.08 ms: 1.10x faster                                                        |
| xml_etree_generate       | 92.3 ms                                                      | 85.5 ms: 1.08x faster                                                        |
| meteor_contest           | 138 ms                                                       | 129 ms: 1.08x faster                                                         |
| pidigits                 | 271 ms                                                       | 253 ms: 1.07x faster                                                         |
| xml_etree_iterparse      | 110 ms                                                       | 103 ms: 1.07x faster                                                         |
| regex_dna                | 261 ms                                                       | 245 ms: 1.06x faster                                                         |
| sqlite_synth             | 2.99 us                                                      | 2.84 us: 1.05x faster                                                        |
| regex_v8                 | 27.2 ms                                                      | 26.1 ms: 1.04x faster                                                        |
| asyncio_websockets       | 390 ms                                                       | 387 ms: 1.01x faster                                                         |
| pickle_dict              | 29.5 us                                                      | 30.1 us: 1.02x slower                                                        |
| unpickle_list            | 4.65 us                                                      | 4.79 us: 1.03x slower                                                        |
| pickle                   | 9.89 us                                                      | 10.3 us: 1.04x slower                                                        |
| pickle_list              | 4.12 us                                                      | 4.30 us: 1.04x slower                                                        |
| flaskblogging            | 4.39 ms                                                      | 4.63 ms: 1.06x slower                                                        |
| regex_effbot             | 3.09 ms                                                      | 3.48 ms: 1.13x slower                                                        |
| unpickle                 | 13.5 us                                                      | 15.4 us: 1.14x slower                                                        |
| python_startup           | 11.5 ms                                                      | 13.2 ms: 1.15x slower                                                        |
| create_gc_cycles         | 1.76 ms                                                      | 2.06 ms: 1.17x slower                                                        |
| telco                    | 7.23 ms                                                      | 8.61 ms: 1.19x slower                                                        |
| python_startup_no_site   | 7.33 ms                                                      | 8.82 ms: 1.20x slower                                                        |
| gc_traversal             | 3.42 ms                                                      | 4.47 ms: 1.31x slower                                                        |
| coverage                 | 63.3 ms                                                      | 83.9 ms: 1.33x slower                                                        |
| Geometric mean           | (ref)                                                        | 1.28x faster                                                                 |
Ignored benchmarks (3) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (4) of results/bm-20240603-3.13.0b1+-6b10467/bm-20240603-pythonperf2-x86_64-python-6b10467fbc0b67bf217e-3.13.0b1+-6b10467.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.24x
- 95% likely to have a speedup of 1.23x
- 99% likely to have a speedup of 1.21x

# Memory
- memory change: 1.12x
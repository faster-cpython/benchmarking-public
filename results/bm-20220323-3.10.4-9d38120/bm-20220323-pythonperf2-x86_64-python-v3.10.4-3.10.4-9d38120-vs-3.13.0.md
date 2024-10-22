# Results vs. 3.13.0

- fork: python
- ref: v3.10.4
- machine: linux-x86_64
- commit hash: 9d38120
- commit date: 2022-03-23
- overall geometric mean: 1.28x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.21x slower
- Memory change: 0.90x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| 2to3           | 291 ms                                                       | 350 ms: 1.20x slower                                         |
| chameleon      | 7.42 ms                                                      | 9.44 ms: 1.27x slower                                        |
| docutils       | 2.81 sec                                                     | 3.41 sec: 1.21x slower                                       |
| html5lib       | 71.9 ms                                                      | 94.6 ms: 1.32x slower                                        |
| tornado_http   | 120 ms                                                       | 157 ms: 1.31x slower                                         |
| Geometric mean | (ref)                                                        | 1.26x slower                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 |
|-------------------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| asyncio_websockets      | 382 ms                                                       | 390 ms: 1.02x slower                                         |
| async_generators        | 359 ms                                                       | 421 ms: 1.17x slower                                         |
| coroutines              | 21.6 ms                                                      | 30.3 ms: 1.40x slower                                        |
| async_tree_cpu_io_mixed | 600 ms                                                       | 936 ms: 1.56x slower                                         |
| async_tree_memoization  | 452 ms                                                       | 819 ms: 1.81x slower                                         |
| async_tree_none         | 372 ms                                                       | 692 ms: 1.86x slower                                         |
| async_tree_io           | 847 ms                                                       | 1.60 sec: 1.89x slower                                       |
| asyncio_tcp_ssl         | 1.58 sec                                                     | 3.10 sec: 1.96x slower                                       |
| asyncio_tcp             | 380 ms                                                       | 779 ms: 2.05x slower                                         |
| Geometric mean          | (ref)                                                        | 1.60x slower                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| pidigits       | 253 ms                                                       | 271 ms: 1.07x slower                                         |
| float          | 81.9 ms                                                      | 111 ms: 1.36x slower                                         |
| nbody          | 88.0 ms                                                      | 134 ms: 1.52x slower                                         |
| Geometric mean | (ref)                                                        | 1.30x slower                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| regex_effbot   | 3.37 ms                                                      | 3.09 ms: 1.09x faster                                        |
| regex_v8       | 26.2 ms                                                      | 27.2 ms: 1.04x slower                                        |
| regex_dna      | 244 ms                                                       | 261 ms: 1.07x slower                                         |
| regex_compile  | 144 ms                                                       | 190 ms: 1.32x slower                                         |
| Geometric mean | (ref)                                                        | 1.08x slower                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 |
|----------------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| unpickle             | 15.1 us                                                      | 13.5 us: 1.12x faster                                        |
| pickle_list          | 4.59 us                                                      | 4.12 us: 1.11x faster                                        |
| pickle_dict          | 32.1 us                                                      | 29.5 us: 1.09x faster                                        |
| pickle               | 10.5 us                                                      | 9.89 us: 1.07x faster                                        |
| xml_etree_generate   | 85.3 ms                                                      | 92.3 ms: 1.08x slower                                        |
| xml_etree_iterparse  | 100 ms                                                       | 110 ms: 1.10x slower                                         |
| xml_etree_parse      | 145 ms                                                       | 160 ms: 1.11x slower                                         |
| tomli_loads          | 2.41 sec                                                     | 2.92 sec: 1.21x slower                                       |
| xml_etree_process    | 60.9 ms                                                      | 75.9 ms: 1.25x slower                                        |
| json_loads           | 24.0 us                                                      | 30.3 us: 1.26x slower                                        |
| json_dumps           | 11.0 ms                                                      | 14.5 ms: 1.33x slower                                        |
| pickle_pure_python   | 318 us                                                       | 455 us: 1.43x slower                                         |
| unpickle_pure_python | 214 us                                                       | 312 us: 1.46x slower                                         |
| Geometric mean       | (ref)                                                        | 1.12x slower                                                 |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 |
|------------------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup_no_site | 8.94 ms                                                      | 7.33 ms: 1.22x faster                                        |
| python_startup         | 13.3 ms                                                      | 11.5 ms: 1.16x faster                                        |
| Geometric mean         | (ref)                                                        | 1.19x faster                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 |
|-----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| genshi_xml      | 57.3 ms                                                      | 63.3 ms: 1.10x slower                                        |
| genshi_text     | 26.6 ms                                                      | 31.4 ms: 1.18x slower                                        |
| django_template | 38.9 ms                                                      | 50.2 ms: 1.29x slower                                        |
| mako            | 10.4 ms                                                      | 14.7 ms: 1.41x slower                                        |
| Geometric mean  | (ref)                                                        | 1.24x slower                                                 |

All benchmarks:
===============

| Benchmark                | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 |
|--------------------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| coverage                 | 81.1 ms                                                      | 63.3 ms: 1.28x faster                                        |
| python_startup_no_site   | 8.94 ms                                                      | 7.33 ms: 1.22x faster                                        |
| gc_traversal             | 4.11 ms                                                      | 3.42 ms: 1.20x faster                                        |
| telco                    | 8.58 ms                                                      | 7.23 ms: 1.19x faster                                        |
| python_startup           | 13.3 ms                                                      | 11.5 ms: 1.16x faster                                        |
| mypy2                    | 1.05 sec                                                     | 933 ms: 1.12x faster                                         |
| unpickle                 | 15.1 us                                                      | 13.5 us: 1.12x faster                                        |
| pickle_list              | 4.59 us                                                      | 4.12 us: 1.11x faster                                        |
| regex_effbot             | 3.37 ms                                                      | 3.09 ms: 1.09x faster                                        |
| pickle_dict              | 32.1 us                                                      | 29.5 us: 1.09x faster                                        |
| pickle                   | 10.5 us                                                      | 9.89 us: 1.07x faster                                        |
| flaskblogging            | 4.62 ms                                                      | 4.39 ms: 1.05x faster                                        |
| asyncio_websockets       | 382 ms                                                       | 390 ms: 1.02x slower                                         |
| regex_v8                 | 26.2 ms                                                      | 27.2 ms: 1.04x slower                                        |
| unpack_sequence          | 56.8 ns                                                      | 59.9 ns: 1.05x slower                                        |
| regex_dna                | 244 ms                                                       | 261 ms: 1.07x slower                                         |
| pidigits                 | 253 ms                                                       | 271 ms: 1.07x slower                                         |
| sqlite_synth             | 2.79 us                                                      | 2.99 us: 1.07x slower                                        |
| meteor_contest           | 128 ms                                                       | 138 ms: 1.08x slower                                         |
| xml_etree_generate       | 85.3 ms                                                      | 92.3 ms: 1.08x slower                                        |
| genshi_xml               | 57.3 ms                                                      | 63.3 ms: 1.10x slower                                        |
| xml_etree_iterparse      | 100 ms                                                       | 110 ms: 1.10x slower                                         |
| xml_etree_parse          | 145 ms                                                       | 160 ms: 1.11x slower                                         |
| aiohttp                  | 1.07 ms                                                      | 1.19 ms: 1.11x slower                                        |
| gunicorn                 | 1.04 ms                                                      | 1.16 ms: 1.12x slower                                        |
| json                     | 5.22 ms                                                      | 5.86 ms: 1.12x slower                                        |
| deepcopy_reduce          | 3.54 us                                                      | 4.01 us: 1.13x slower                                        |
| scimark_fft              | 314 ms                                                       | 361 ms: 1.15x slower                                         |
| async_generators         | 359 ms                                                       | 421 ms: 1.17x slower                                         |
| sqlglot_optimize         | 59.7 ms                                                      | 70.1 ms: 1.18x slower                                        |
| deepcopy                 | 397 us                                                       | 468 us: 1.18x slower                                         |
| genshi_text              | 26.6 ms                                                      | 31.4 ms: 1.18x slower                                        |
| scimark_sparse_mat_mult  | 4.29 ms                                                      | 5.08 ms: 1.18x slower                                        |
| sympy_expand             | 505 ms                                                       | 600 ms: 1.19x slower                                         |
| mdp                      | 2.52 sec                                                     | 3.01 sec: 1.19x slower                                       |
| 2to3                     | 291 ms                                                       | 350 ms: 1.20x slower                                         |
| sympy_integrate          | 23.3 ms                                                      | 28.2 ms: 1.21x slower                                        |
| tomli_loads              | 2.41 sec                                                     | 2.92 sec: 1.21x slower                                       |
| sqlglot_normalize        | 118 ms                                                       | 144 ms: 1.21x slower                                         |
| docutils                 | 2.81 sec                                                     | 3.41 sec: 1.21x slower                                       |
| sympy_str                | 296 ms                                                       | 360 ms: 1.22x slower                                         |
| pathlib                  | 17.4 ms                                                      | 21.4 ms: 1.23x slower                                        |
| dulwich_log              | 65.5 ms                                                      | 81.1 ms: 1.24x slower                                        |
| dask                     | 379 ms                                                       | 472 ms: 1.25x slower                                         |
| xml_etree_process        | 60.9 ms                                                      | 75.9 ms: 1.25x slower                                        |
| sympy_sum                | 154 ms                                                       | 193 ms: 1.25x slower                                         |
| deepcopy_memo            | 39.5 us                                                      | 49.8 us: 1.26x slower                                        |
| json_loads               | 24.0 us                                                      | 30.3 us: 1.26x slower                                        |
| bench_thread_pool        | 901 us                                                       | 1.14 ms: 1.27x slower                                        |
| chameleon                | 7.42 ms                                                      | 9.44 ms: 1.27x slower                                        |
| django_template          | 38.9 ms                                                      | 50.2 ms: 1.29x slower                                        |
| pprint_safe_repr         | 812 ms                                                       | 1.05 sec: 1.29x slower                                       |
| nqueens                  | 88.2 ms                                                      | 115 ms: 1.30x slower                                         |
| pprint_pformat           | 1.65 sec                                                     | 2.15 sec: 1.31x slower                                       |
| tornado_http             | 120 ms                                                       | 157 ms: 1.31x slower                                         |
| html5lib                 | 71.9 ms                                                      | 94.6 ms: 1.32x slower                                        |
| regex_compile            | 144 ms                                                       | 190 ms: 1.32x slower                                         |
| fannkuch                 | 365 ms                                                       | 483 ms: 1.32x slower                                         |
| json_dumps               | 11.0 ms                                                      | 14.5 ms: 1.33x slower                                        |
| pycparser                | 1.26 sec                                                     | 1.67 sec: 1.33x slower                                       |
| thrift                   | 877 us                                                       | 1.18 ms: 1.34x slower                                        |
| float                    | 81.9 ms                                                      | 111 ms: 1.36x slower                                         |
| logging_format           | 7.07 us                                                      | 9.64 us: 1.36x slower                                        |
| bench_mp_pool            | 4.65 ms                                                      | 6.37 ms: 1.37x slower                                        |
| logging_simple           | 6.40 us                                                      | 8.88 us: 1.39x slower                                        |
| coroutines               | 21.6 ms                                                      | 30.3 ms: 1.40x slower                                        |
| mako                     | 10.4 ms                                                      | 14.7 ms: 1.41x slower                                        |
| richards                 | 52.7 ms                                                      | 75.1 ms: 1.42x slower                                        |
| spectral_norm            | 97.4 ms                                                      | 139 ms: 1.43x slower                                         |
| pickle_pure_python       | 318 us                                                       | 455 us: 1.43x slower                                         |
| scimark_sor              | 126 ms                                                       | 180 ms: 1.43x slower                                         |
| unpickle_pure_python     | 214 us                                                       | 312 us: 1.46x slower                                         |
| hexiom                   | 6.33 ms                                                      | 9.42 ms: 1.49x slower                                        |
| pyflate                  | 492 ms                                                       | 733 ms: 1.49x slower                                         |
| sqlglot_transpile        | 1.78 ms                                                      | 2.68 ms: 1.51x slower                                        |
| richards_super           | 59.8 ms                                                      | 90.6 ms: 1.52x slower                                        |
| nbody                    | 88.0 ms                                                      | 134 ms: 1.52x slower                                         |
| comprehensions           | 17.3 us                                                      | 26.7 us: 1.55x slower                                        |
| async_tree_cpu_io_mixed  | 600 ms                                                       | 936 ms: 1.56x slower                                         |
| sqlglot_parse            | 1.38 ms                                                      | 2.24 ms: 1.62x slower                                        |
| go                       | 160 ms                                                       | 262 ms: 1.63x slower                                         |
| pylint                   | 346 ms                                                       | 566 ms: 1.63x slower                                         |
| crypto_pyaes             | 72.8 ms                                                      | 119 ms: 1.64x slower                                         |
| scimark_monte_carlo      | 64.9 ms                                                      | 107 ms: 1.65x slower                                         |
| raytrace                 | 289 ms                                                       | 489 ms: 1.69x slower                                         |
| scimark_lu               | 97.8 ms                                                      | 167 ms: 1.71x slower                                         |
| generators               | 33.5 ms                                                      | 57.3 ms: 1.71x slower                                        |
| logging_silent           | 97.7 ns                                                      | 167 ns: 1.71x slower                                         |
| chaos                    | 61.7 ms                                                      | 109 ms: 1.76x slower                                         |
| async_tree_memoization   | 452 ms                                                       | 819 ms: 1.81x slower                                         |
| async_tree_none          | 372 ms                                                       | 692 ms: 1.86x slower                                         |
| async_tree_io            | 847 ms                                                       | 1.60 sec: 1.89x slower                                       |
| asyncio_tcp_ssl          | 1.58 sec                                                     | 3.10 sec: 1.96x slower                                       |
| asyncio_tcp              | 380 ms                                                       | 779 ms: 2.05x slower                                         |
| deltablue                | 3.41 ms                                                      | 7.50 ms: 2.20x slower                                        |
| typing_runtime_protocols | 174 us                                                       | 537 us: 3.08x slower                                         |
| Geometric mean           | (ref)                                                        | 1.28x slower                                                 |

Benchmark hidden because not significant (2): create_gc_cycles, unpickle_list
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
Ignored benchmarks (2) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: sqlalchemy_declarative, sqlalchemy_imperative

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.24x
- 95% likely to have a slowdown of 1.24x
- 99% likely to have a slowdown of 1.21x

# Memory
- memory change: 0.90x
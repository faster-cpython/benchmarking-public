# Results vs. 3.10.4

- fork: python
- ref: v3.13.0a3
- machine: linux-x86_64
- commit hash: f009305
- commit date: 2024-01-17
- overall geometric mean: 1.28x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.22x faster
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240117-pythonperf2-x86_64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 294 ms: 1.19x faster                                             |
| chameleon      | 9.44 ms                                                      | 7.26 ms: 1.30x faster                                            |
| docutils       | 3.41 sec                                                     | 2.83 sec: 1.21x faster                                           |
| html5lib       | 94.6 ms                                                      | 73.9 ms: 1.28x faster                                            |
| tornado_http   | 157 ms                                                       | 118 ms: 1.33x faster                                             |
| Geometric mean | (ref)                                                        | 1.26x faster                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240117-pythonperf2-x86_64-python-v3.13.0a3-3.13.0a3-f009305 |
|-------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| async_tree_none         | 692 ms                                                       | 435 ms: 1.59x faster                                             |
| async_tree_memoization  | 819 ms                                                       | 547 ms: 1.50x faster                                             |
| async_tree_io           | 1.60 sec                                                     | 1.08 sec: 1.48x faster                                           |
| async_tree_cpu_io_mixed | 936 ms                                                       | 701 ms: 1.34x faster                                             |
| Geometric mean          | (ref)                                                        | 1.47x faster                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240117-pythonperf2-x86_64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| nbody          | 134 ms                                                       | 85.3 ms: 1.57x faster                                            |
| float          | 111 ms                                                       | 78.0 ms: 1.42x faster                                            |
| pidigits       | 271 ms                                                       | 263 ms: 1.03x faster                                             |
| Geometric mean | (ref)                                                        | 1.32x faster                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240117-pythonperf2-x86_64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 141 ms: 1.35x faster                                             |
| regex_dna      | 261 ms                                                       | 238 ms: 1.10x faster                                             |
| regex_v8       | 27.2 ms                                                      | 26.0 ms: 1.04x faster                                            |
| regex_effbot   | 3.09 ms                                                      | 3.50 ms: 1.13x slower                                            |
| Geometric mean | (ref)                                                        | 1.08x faster                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240117-pythonperf2-x86_64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                       | 307 us: 1.48x faster                                             |
| unpickle_pure_python | 312 us                                                       | 213 us: 1.47x faster                                             |
| json_dumps           | 14.5 ms                                                      | 10.6 ms: 1.38x faster                                            |
| tomli_loads          | 2.92 sec                                                     | 2.23 sec: 1.31x faster                                           |
| xml_etree_process    | 75.9 ms                                                      | 58.7 ms: 1.29x faster                                            |
| json_loads           | 30.3 us                                                      | 25.0 us: 1.21x faster                                            |
| xml_etree_generate   | 92.3 ms                                                      | 85.6 ms: 1.08x faster                                            |
| xml_etree_parse      | 160 ms                                                       | 150 ms: 1.07x faster                                             |
| xml_etree_iterparse  | 110 ms                                                       | 107 ms: 1.04x faster                                             |
| unpickle_list        | 4.65 us                                                      | 4.82 us: 1.04x slower                                            |
| pickle               | 9.89 us                                                      | 10.4 us: 1.05x slower                                            |
| pickle_list          | 4.12 us                                                      | 4.49 us: 1.09x slower                                            |
| pickle_dict          | 29.5 us                                                      | 32.5 us: 1.10x slower                                            |
| unpickle             | 13.5 us                                                      | 15.4 us: 1.14x slower                                            |
| Geometric mean       | (ref)                                                        | 1.12x faster                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240117-pythonperf2-x86_64-python-v3.13.0a3-3.13.0a3-f009305 |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 12.6 ms: 1.09x slower                                            |
| python_startup_no_site | 7.33 ms                                                      | 11.0 ms: 1.50x slower                                            |
| Geometric mean         | (ref)                                                        | 1.28x slower                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240117-pythonperf2-x86_64-python-v3.13.0a3-3.13.0a3-f009305 |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 10.3 ms: 1.42x faster                                            |
| django_template | 50.2 ms                                                      | 38.4 ms: 1.31x faster                                            |
| genshi_text     | 31.4 ms                                                      | 25.7 ms: 1.22x faster                                            |
| genshi_xml      | 63.3 ms                                                      | 55.6 ms: 1.14x faster                                            |
| Geometric mean  | (ref)                                                        | 1.27x faster                                                     |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240117-pythonperf2-x86_64-python-v3.13.0a3-3.13.0a3-f009305 |
|--------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 113 us: 4.74x faster                                             |
| deltablue                | 7.50 ms                                                      | 3.54 ms: 2.12x faster                                            |
| asyncio_tcp              | 779 ms                                                       | 371 ms: 2.10x faster                                             |
| asyncio_tcp_ssl          | 3.10 sec                                                     | 1.57 sec: 1.97x faster                                           |
| raytrace                 | 489 ms                                                       | 265 ms: 1.84x faster                                             |
| chaos                    | 109 ms                                                       | 59.9 ms: 1.81x faster                                            |
| logging_silent           | 167 ns                                                       | 96.0 ns: 1.74x faster                                            |
| scimark_lu               | 167 ms                                                       | 97.8 ms: 1.71x faster                                            |
| generators               | 57.3 ms                                                      | 33.8 ms: 1.70x faster                                            |
| crypto_pyaes             | 119 ms                                                       | 71.4 ms: 1.67x faster                                            |
| pylint                   | 566 ms                                                       | 343 ms: 1.65x faster                                             |
| comprehensions           | 26.7 us                                                      | 16.5 us: 1.61x faster                                            |
| sqlglot_parse            | 2.24 ms                                                      | 1.39 ms: 1.61x faster                                            |
| async_tree_none          | 692 ms                                                       | 435 ms: 1.59x faster                                             |
| scimark_monte_carlo      | 107 ms                                                       | 67.9 ms: 1.58x faster                                            |
| go                       | 262 ms                                                       | 166 ms: 1.58x faster                                             |
| nbody                    | 134 ms                                                       | 85.3 ms: 1.57x faster                                            |
| richards_super           | 90.6 ms                                                      | 59.4 ms: 1.53x faster                                            |
| spectral_norm            | 139 ms                                                       | 92.3 ms: 1.51x faster                                            |
| sqlglot_transpile        | 2.68 ms                                                      | 1.79 ms: 1.50x faster                                            |
| async_tree_memoization   | 819 ms                                                       | 547 ms: 1.50x faster                                             |
| async_tree_io            | 1.60 sec                                                     | 1.08 sec: 1.48x faster                                           |
| pickle_pure_python       | 455 us                                                       | 307 us: 1.48x faster                                             |
| unpickle_pure_python     | 312 us                                                       | 213 us: 1.47x faster                                             |
| pyflate                  | 733 ms                                                       | 501 ms: 1.46x faster                                             |
| hexiom                   | 9.42 ms                                                      | 6.46 ms: 1.46x faster                                            |
| float                    | 111 ms                                                       | 78.0 ms: 1.42x faster                                            |
| mako                     | 14.7 ms                                                      | 10.3 ms: 1.42x faster                                            |
| richards                 | 75.1 ms                                                      | 53.7 ms: 1.40x faster                                            |
| bench_mp_pool            | 6.37 ms                                                      | 4.57 ms: 1.39x faster                                            |
| json_dumps               | 14.5 ms                                                      | 10.6 ms: 1.38x faster                                            |
| coroutines               | 30.3 ms                                                      | 22.3 ms: 1.36x faster                                            |
| regex_compile            | 190 ms                                                       | 141 ms: 1.35x faster                                             |
| thrift                   | 1.18 ms                                                      | 872 us: 1.35x faster                                             |
| deepcopy_memo            | 49.8 us                                                      | 37.1 us: 1.34x faster                                            |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 701 ms: 1.34x faster                                             |
| tornado_http             | 157 ms                                                       | 118 ms: 1.33x faster                                             |
| logging_simple           | 8.88 us                                                      | 6.66 us: 1.33x faster                                            |
| logging_format           | 9.64 us                                                      | 7.31 us: 1.32x faster                                            |
| django_template          | 50.2 ms                                                      | 38.4 ms: 1.31x faster                                            |
| tomli_loads              | 2.92 sec                                                     | 2.23 sec: 1.31x faster                                           |
| chameleon                | 9.44 ms                                                      | 7.26 ms: 1.30x faster                                            |
| pprint_pformat           | 2.15 sec                                                     | 1.66 sec: 1.30x faster                                           |
| xml_etree_process        | 75.9 ms                                                      | 58.7 ms: 1.29x faster                                            |
| pprint_safe_repr         | 1.05 sec                                                     | 813 ms: 1.29x faster                                             |
| nqueens                  | 115 ms                                                       | 89.1 ms: 1.29x faster                                            |
| html5lib                 | 94.6 ms                                                      | 73.9 ms: 1.28x faster                                            |
| deepcopy                 | 468 us                                                       | 367 us: 1.27x faster                                             |
| pycparser                | 1.67 sec                                                     | 1.32 sec: 1.27x faster                                           |
| sympy_sum                | 193 ms                                                       | 154 ms: 1.25x faster                                             |
| scimark_sor              | 180 ms                                                       | 144 ms: 1.25x faster                                             |
| fannkuch                 | 483 ms                                                       | 386 ms: 1.25x faster                                             |
| sqlglot_normalize        | 144 ms                                                       | 116 ms: 1.24x faster                                             |
| sympy_str                | 360 ms                                                       | 294 ms: 1.23x faster                                             |
| deepcopy_reduce          | 4.01 us                                                      | 3.28 us: 1.22x faster                                            |
| genshi_text              | 31.4 ms                                                      | 25.7 ms: 1.22x faster                                            |
| sympy_expand             | 600 ms                                                       | 494 ms: 1.21x faster                                             |
| json_loads               | 30.3 us                                                      | 25.0 us: 1.21x faster                                            |
| docutils                 | 3.41 sec                                                     | 2.83 sec: 1.21x faster                                           |
| sympy_integrate          | 28.2 ms                                                      | 23.3 ms: 1.21x faster                                            |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 4.21 ms: 1.21x faster                                            |
| mdp                      | 3.01 sec                                                     | 2.50 sec: 1.20x faster                                           |
| scimark_fft              | 361 ms                                                       | 302 ms: 1.20x faster                                             |
| sqlglot_optimize         | 70.1 ms                                                      | 59.0 ms: 1.19x faster                                            |
| dulwich_log              | 81.1 ms                                                      | 68.2 ms: 1.19x faster                                            |
| 2to3                     | 350 ms                                                       | 294 ms: 1.19x faster                                             |
| bench_thread_pool        | 1.14 ms                                                      | 960 us: 1.19x faster                                             |
| async_generators         | 421 ms                                                       | 368 ms: 1.14x faster                                             |
| genshi_xml               | 63.3 ms                                                      | 55.6 ms: 1.14x faster                                            |
| pathlib                  | 21.4 ms                                                      | 18.9 ms: 1.13x faster                                            |
| create_gc_cycles         | 1.76 ms                                                      | 1.57 ms: 1.12x faster                                            |
| aiohttp                  | 1.19 ms                                                      | 1.06 ms: 1.12x faster                                            |
| json                     | 5.86 ms                                                      | 5.27 ms: 1.11x faster                                            |
| gunicorn                 | 1.16 ms                                                      | 1.05 ms: 1.11x faster                                            |
| regex_dna                | 261 ms                                                       | 238 ms: 1.10x faster                                             |
| mypy2                    | 933 ms                                                       | 864 ms: 1.08x faster                                             |
| sqlite_synth             | 2.99 us                                                      | 2.77 us: 1.08x faster                                            |
| xml_etree_generate       | 92.3 ms                                                      | 85.6 ms: 1.08x faster                                            |
| xml_etree_parse          | 160 ms                                                       | 150 ms: 1.07x faster                                             |
| meteor_contest           | 138 ms                                                       | 130 ms: 1.07x faster                                             |
| regex_v8                 | 27.2 ms                                                      | 26.0 ms: 1.04x faster                                            |
| xml_etree_iterparse      | 110 ms                                                       | 107 ms: 1.04x faster                                             |
| pidigits                 | 271 ms                                                       | 263 ms: 1.03x faster                                             |
| asyncio_websockets       | 390 ms                                                       | 395 ms: 1.01x slower                                             |
| unpickle_list            | 4.65 us                                                      | 4.82 us: 1.04x slower                                            |
| pickle                   | 9.89 us                                                      | 10.4 us: 1.05x slower                                            |
| flaskblogging            | 4.39 ms                                                      | 4.61 ms: 1.05x slower                                            |
| pickle_list              | 4.12 us                                                      | 4.49 us: 1.09x slower                                            |
| python_startup           | 11.5 ms                                                      | 12.6 ms: 1.09x slower                                            |
| pickle_dict              | 29.5 us                                                      | 32.5 us: 1.10x slower                                            |
| regex_effbot             | 3.09 ms                                                      | 3.50 ms: 1.13x slower                                            |
| telco                    | 7.23 ms                                                      | 8.23 ms: 1.14x slower                                            |
| unpickle                 | 13.5 us                                                      | 15.4 us: 1.14x slower                                            |
| gc_traversal             | 3.42 ms                                                      | 3.94 ms: 1.15x slower                                            |
| coverage                 | 63.3 ms                                                      | 82.9 ms: 1.31x slower                                            |
| python_startup_no_site   | 7.33 ms                                                      | 11.0 ms: 1.50x slower                                            |
| Geometric mean           | (ref)                                                        | 1.28x faster                                                     |
Ignored benchmarks (4) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: dask, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (4) of results/bm-20240117-3.13.0a3-f009305/bm-20240117-pythonperf2-x86_64-python-v3.13.0a3-3.13.0a3-f009305.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.25x
- 95% likely to have a speedup of 1.24x
- 99% likely to have a speedup of 1.22x

# Memory
- memory change: 1.07x
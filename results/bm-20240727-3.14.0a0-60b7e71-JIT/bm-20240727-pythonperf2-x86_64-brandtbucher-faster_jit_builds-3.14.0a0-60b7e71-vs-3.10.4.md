# Results vs. 3.10.4

- fork: brandtbucher
- ref: faster_jit_builds
- machine: linux-x86_64
- commit hash: 60b7e71
- commit date: 2024-07-27
- overall geometric mean: 1.33x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.20x faster
- Memory change: 1.20x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240727-pythonperf2-x86_64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 303 ms: 1.15x faster                                                           |
| docutils       | 3.41 sec                                                     | 3.12 sec: 1.09x faster                                                         |
| html5lib       | 94.6 ms                                                      | 69.9 ms: 1.35x faster                                                          |
| tornado_http   | 157 ms                                                       | 120 ms: 1.31x faster                                                           |
| Geometric mean | (ref)                                                        | 1.22x faster                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240727-pythonperf2-x86_64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|-------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_none         | 692 ms                                                       | 333 ms: 2.07x faster                                                           |
| async_tree_memoization  | 819 ms                                                       | 400 ms: 2.05x faster                                                           |
| async_tree_io           | 1.60 sec                                                     | 795 ms: 2.01x faster                                                           |
| async_tree_cpu_io_mixed | 936 ms                                                       | 571 ms: 1.64x faster                                                           |
| Geometric mean          | (ref)                                                        | 1.94x faster                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240727-pythonperf2-x86_64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| nbody          | 134 ms                                                       | 81.5 ms: 1.65x faster                                                          |
| float          | 111 ms                                                       | 74.6 ms: 1.49x faster                                                          |
| pidigits       | 271 ms                                                       | 251 ms: 1.08x faster                                                           |
| Geometric mean | (ref)                                                        | 1.38x faster                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240727-pythonperf2-x86_64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 137 ms: 1.39x faster                                                           |
| regex_dna      | 261 ms                                                       | 236 ms: 1.11x faster                                                           |
| regex_v8       | 27.2 ms                                                      | 26.5 ms: 1.03x faster                                                          |
| regex_effbot   | 3.09 ms                                                      | 3.52 ms: 1.14x slower                                                          |
| Geometric mean | (ref)                                                        | 1.08x faster                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240727-pythonperf2-x86_64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|----------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| unpickle_pure_python | 312 us                                                       | 213 us: 1.46x faster                                                           |
| pickle_pure_python   | 455 us                                                       | 317 us: 1.44x faster                                                           |
| tomli_loads          | 2.92 sec                                                     | 2.09 sec: 1.39x faster                                                         |
| json_dumps           | 14.5 ms                                                      | 10.8 ms: 1.35x faster                                                          |
| xml_etree_process    | 75.9 ms                                                      | 58.8 ms: 1.29x faster                                                          |
| json_loads           | 30.3 us                                                      | 25.5 us: 1.19x faster                                                          |
| xml_etree_parse      | 160 ms                                                       | 140 ms: 1.14x faster                                                           |
| xml_etree_iterparse  | 110 ms                                                       | 96.7 ms: 1.14x faster                                                          |
| xml_etree_generate   | 92.3 ms                                                      | 81.4 ms: 1.13x faster                                                          |
| Geometric mean       | (ref)                                                        | 1.28x faster                                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240727-pythonperf2-x86_64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 13.4 ms: 1.16x slower                                                          |
| python_startup_no_site | 7.33 ms                                                      | 9.08 ms: 1.24x slower                                                          |
| Geometric mean         | (ref)                                                        | 1.20x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240727-pythonperf2-x86_64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|-----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 9.26 ms: 1.59x faster                                                          |
| django_template | 50.2 ms                                                      | 41.2 ms: 1.22x faster                                                          |
| genshi_text     | 31.4 ms                                                      | 30.3 ms: 1.04x faster                                                          |
| genshi_xml      | 63.3 ms                                                      | 68.9 ms: 1.09x slower                                                          |
| Geometric mean  | (ref)                                                        | 1.17x faster                                                                   |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240727-pythonperf2-x86_64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|--------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 185 us: 2.89x faster                                                           |
| deltablue                | 7.50 ms                                                      | 3.59 ms: 2.09x faster                                                          |
| async_tree_none          | 692 ms                                                       | 333 ms: 2.07x faster                                                           |
| asyncio_tcp              | 779 ms                                                       | 377 ms: 2.07x faster                                                           |
| async_tree_memoization   | 819 ms                                                       | 400 ms: 2.05x faster                                                           |
| async_tree_io            | 1.60 sec                                                     | 795 ms: 2.01x faster                                                           |
| asyncio_tcp_ssl          | 3.10 sec                                                     | 1.58 sec: 1.96x faster                                                         |
| richards_super           | 90.6 ms                                                      | 51.2 ms: 1.77x faster                                                          |
| deepcopy_memo            | 49.8 us                                                      | 28.4 us: 1.75x faster                                                          |
| spectral_norm            | 139 ms                                                       | 81.0 ms: 1.72x faster                                                          |
| crypto_pyaes             | 119 ms                                                       | 69.7 ms: 1.71x faster                                                          |
| generators               | 57.3 ms                                                      | 34.2 ms: 1.68x faster                                                          |
| pyflate                  | 733 ms                                                       | 437 ms: 1.68x faster                                                           |
| richards                 | 75.1 ms                                                      | 45.1 ms: 1.67x faster                                                          |
| raytrace                 | 489 ms                                                       | 294 ms: 1.66x faster                                                           |
| scimark_monte_carlo      | 107 ms                                                       | 64.8 ms: 1.66x faster                                                          |
| logging_silent           | 167 ns                                                       | 101 ns: 1.66x faster                                                           |
| nbody                    | 134 ms                                                       | 81.5 ms: 1.65x faster                                                          |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 571 ms: 1.64x faster                                                           |
| chaos                    | 109 ms                                                       | 66.5 ms: 1.63x faster                                                          |
| go                       | 262 ms                                                       | 162 ms: 1.62x faster                                                           |
| sqlglot_parse            | 2.24 ms                                                      | 1.41 ms: 1.59x faster                                                          |
| mako                     | 14.7 ms                                                      | 9.26 ms: 1.59x faster                                                          |
| deepcopy                 | 468 us                                                       | 302 us: 1.55x faster                                                           |
| float                    | 111 ms                                                       | 74.6 ms: 1.49x faster                                                          |
| pylint                   | 566 ms                                                       | 386 ms: 1.47x faster                                                           |
| sqlglot_transpile        | 2.68 ms                                                      | 1.83 ms: 1.46x faster                                                          |
| unpickle_pure_python     | 312 us                                                       | 213 us: 1.46x faster                                                           |
| comprehensions           | 26.7 us                                                      | 18.4 us: 1.45x faster                                                          |
| scimark_lu               | 167 ms                                                       | 116 ms: 1.44x faster                                                           |
| pickle_pure_python       | 455 us                                                       | 317 us: 1.44x faster                                                           |
| hexiom                   | 9.42 ms                                                      | 6.61 ms: 1.42x faster                                                          |
| coroutines               | 30.3 ms                                                      | 21.3 ms: 1.42x faster                                                          |
| scimark_sor              | 180 ms                                                       | 128 ms: 1.40x faster                                                           |
| tomli_loads              | 2.92 sec                                                     | 2.09 sec: 1.39x faster                                                         |
| logging_simple           | 8.88 us                                                      | 6.37 us: 1.39x faster                                                          |
| regex_compile            | 190 ms                                                       | 137 ms: 1.39x faster                                                           |
| logging_format           | 9.64 us                                                      | 7.01 us: 1.38x faster                                                          |
| pycparser                | 1.67 sec                                                     | 1.22 sec: 1.37x faster                                                         |
| html5lib                 | 94.6 ms                                                      | 69.9 ms: 1.35x faster                                                          |
| json_dumps               | 14.5 ms                                                      | 10.8 ms: 1.35x faster                                                          |
| deepcopy_reduce          | 4.01 us                                                      | 3.00 us: 1.34x faster                                                          |
| thrift                   | 1.18 ms                                                      | 882 us: 1.33x faster                                                           |
| pathlib                  | 21.4 ms                                                      | 16.1 ms: 1.33x faster                                                          |
| bench_mp_pool            | 6.37 ms                                                      | 4.80 ms: 1.33x faster                                                          |
| fannkuch                 | 483 ms                                                       | 366 ms: 1.32x faster                                                           |
| tornado_http             | 157 ms                                                       | 120 ms: 1.31x faster                                                           |
| pprint_safe_repr         | 1.05 sec                                                     | 807 ms: 1.30x faster                                                           |
| xml_etree_process        | 75.9 ms                                                      | 58.8 ms: 1.29x faster                                                          |
| pprint_pformat           | 2.15 sec                                                     | 1.67 sec: 1.29x faster                                                         |
| bench_thread_pool        | 1.14 ms                                                      | 903 us: 1.26x faster                                                           |
| scimark_fft              | 361 ms                                                       | 292 ms: 1.24x faster                                                           |
| django_template          | 50.2 ms                                                      | 41.2 ms: 1.22x faster                                                          |
| dask                     | 472 ms                                                       | 389 ms: 1.21x faster                                                           |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 4.22 ms: 1.20x faster                                                          |
| nqueens                  | 115 ms                                                       | 95.5 ms: 1.20x faster                                                          |
| json_loads               | 30.3 us                                                      | 25.5 us: 1.19x faster                                                          |
| sympy_str                | 360 ms                                                       | 311 ms: 1.16x faster                                                           |
| mdp                      | 3.01 sec                                                     | 2.60 sec: 1.16x faster                                                         |
| 2to3                     | 350 ms                                                       | 303 ms: 1.15x faster                                                           |
| sympy_sum                | 193 ms                                                       | 167 ms: 1.15x faster                                                           |
| xml_etree_parse          | 160 ms                                                       | 140 ms: 1.14x faster                                                           |
| xml_etree_iterparse      | 110 ms                                                       | 96.7 ms: 1.14x faster                                                          |
| sympy_expand             | 600 ms                                                       | 528 ms: 1.14x faster                                                           |
| xml_etree_generate       | 92.3 ms                                                      | 81.4 ms: 1.13x faster                                                          |
| regex_dna                | 261 ms                                                       | 236 ms: 1.11x faster                                                           |
| sqlglot_optimize         | 70.1 ms                                                      | 63.6 ms: 1.10x faster                                                          |
| sympy_integrate          | 28.2 ms                                                      | 25.7 ms: 1.10x faster                                                          |
| docutils                 | 3.41 sec                                                     | 3.12 sec: 1.09x faster                                                         |
| meteor_contest           | 138 ms                                                       | 127 ms: 1.09x faster                                                           |
| async_generators         | 421 ms                                                       | 388 ms: 1.09x faster                                                           |
| sqlglot_normalize        | 144 ms                                                       | 133 ms: 1.08x faster                                                           |
| pidigits                 | 271 ms                                                       | 251 ms: 1.08x faster                                                           |
| json                     | 5.86 ms                                                      | 5.48 ms: 1.07x faster                                                          |
| genshi_text              | 31.4 ms                                                      | 30.3 ms: 1.04x faster                                                          |
| regex_v8                 | 27.2 ms                                                      | 26.5 ms: 1.03x faster                                                          |
| create_gc_cycles         | 1.76 ms                                                      | 1.92 ms: 1.09x slower                                                          |
| genshi_xml               | 63.3 ms                                                      | 68.9 ms: 1.09x slower                                                          |
| telco                    | 7.23 ms                                                      | 7.92 ms: 1.10x slower                                                          |
| regex_effbot             | 3.09 ms                                                      | 3.52 ms: 1.14x slower                                                          |
| python_startup           | 11.5 ms                                                      | 13.4 ms: 1.16x slower                                                          |
| python_startup_no_site   | 7.33 ms                                                      | 9.08 ms: 1.24x slower                                                          |
| gc_traversal             | 3.42 ms                                                      | 4.34 ms: 1.27x slower                                                          |
| coverage                 | 63.3 ms                                                      | 80.7 ms: 1.27x slower                                                          |
| Geometric mean           | (ref)                                                        | 1.33x faster                                                                   |

Benchmark hidden because not significant (1): asyncio_websockets
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240727-3.14.0a0-60b7e71-JIT/bm-20240727-pythonperf2-x86_64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.26x
- 95% likely to have a speedup of 1.23x
- 99% likely to have a speedup of 1.20x

# Memory
- memory change: 1.20x
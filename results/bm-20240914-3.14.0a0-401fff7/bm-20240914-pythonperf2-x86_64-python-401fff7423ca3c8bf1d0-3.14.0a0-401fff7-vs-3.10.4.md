# Results vs. 3.10.4

- fork: python
- ref: 401fff7423ca3c8bf1d0
- machine: linux-x86_64
- commit hash: 401fff7
- commit date: 2024-09-14
- overall geometric mean: 1.336x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.23x faster
- Memory change: 1.13x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240914-pythonperf2-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 281 ms: 1.25x faster                                                        |
| docutils       | 3.41 sec                                                     | 2.90 sec: 1.18x faster                                                      |
| html5lib       | 94.6 ms                                                      | 71.1 ms: 1.33x faster                                                       |
| tornado_http   | 157 ms                                                       | 116 ms: 1.35x faster                                                        |
| Geometric mean | (ref)                                                        | 1.27x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240914-pythonperf2-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|-------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none         | 692 ms                                                       | 318 ms: 2.17x faster                                                        |
| async_tree_memoization  | 819 ms                                                       | 400 ms: 2.05x faster                                                        |
| async_tree_io           | 1.60 sec                                                     | 803 ms: 1.99x faster                                                        |
| async_tree_cpu_io_mixed | 936 ms                                                       | 575 ms: 1.63x faster                                                        |
| Geometric mean          | (ref)                                                        | 1.95x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240914-pythonperf2-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 134 ms                                                       | 85.8 ms: 1.56x faster                                                       |
| float          | 111 ms                                                       | 80.7 ms: 1.38x faster                                                       |
| pidigits       | 271 ms                                                       | 252 ms: 1.07x faster                                                        |
| Geometric mean | (ref)                                                        | 1.32x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240914-pythonperf2-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 138 ms: 1.37x faster                                                        |
| regex_dna      | 261 ms                                                       | 236 ms: 1.10x faster                                                        |
| regex_v8       | 27.2 ms                                                      | 26.2 ms: 1.04x faster                                                       |
| regex_effbot   | 3.09 ms                                                      | 3.45 ms: 1.12x slower                                                       |
| Geometric mean | (ref)                                                        | 1.09x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240914-pythonperf2-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpickle_pure_python | 312 us                                                       | 217 us: 1.44x faster                                                        |
| pickle_pure_python   | 455 us                                                       | 322 us: 1.41x faster                                                        |
| json_dumps           | 14.5 ms                                                      | 10.8 ms: 1.35x faster                                                       |
| xml_etree_process    | 75.9 ms                                                      | 60.1 ms: 1.26x faster                                                       |
| json_loads           | 30.3 us                                                      | 25.3 us: 1.20x faster                                                       |
| tomli_loads          | 2.92 sec                                                     | 2.56 sec: 1.14x faster                                                      |
| xml_etree_parse      | 160 ms                                                       | 143 ms: 1.12x faster                                                        |
| xml_etree_iterparse  | 110 ms                                                       | 100 ms: 1.10x faster                                                        |
| xml_etree_generate   | 92.3 ms                                                      | 84.5 ms: 1.09x faster                                                       |
| unpickle_list        | 4.65 us                                                      | 4.60 us: 1.01x faster                                                       |
| pickle               | 9.89 us                                                      | 10.4 us: 1.06x slower                                                       |
| unpickle             | 13.5 us                                                      | 15.0 us: 1.11x slower                                                       |
| pickle_list          | 4.12 us                                                      | 4.64 us: 1.13x slower                                                       |
| pickle_dict          | 29.5 us                                                      | 33.5 us: 1.13x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.11x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240914-pythonperf2-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 13.4 ms: 1.16x slower                                                       |
| python_startup_no_site | 7.33 ms                                                      | 8.95 ms: 1.22x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.19x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240914-pythonperf2-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 10.4 ms: 1.42x faster                                                       |
| genshi_text     | 31.4 ms                                                      | 24.3 ms: 1.29x faster                                                       |
| django_template | 50.2 ms                                                      | 39.0 ms: 1.29x faster                                                       |
| genshi_xml      | 63.3 ms                                                      | 53.4 ms: 1.19x faster                                                       |
| Geometric mean  | (ref)                                                        | 1.29x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240914-pythonperf2-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|--------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 171 us: 3.13x faster                                                        |
| deltablue                | 7.50 ms                                                      | 3.41 ms: 2.20x faster                                                       |
| async_tree_none          | 692 ms                                                       | 318 ms: 2.17x faster                                                        |
| asyncio_tcp              | 779 ms                                                       | 375 ms: 2.08x faster                                                        |
| async_tree_memoization   | 819 ms                                                       | 400 ms: 2.05x faster                                                        |
| async_tree_io            | 1.60 sec                                                     | 803 ms: 1.99x faster                                                        |
| generators               | 57.3 ms                                                      | 28.9 ms: 1.98x faster                                                       |
| asyncio_tcp_ssl          | 3.10 sec                                                     | 1.57 sec: 1.97x faster                                                      |
| go                       | 262 ms                                                       | 137 ms: 1.91x faster                                                        |
| raytrace                 | 489 ms                                                       | 270 ms: 1.81x faster                                                        |
| scimark_lu               | 167 ms                                                       | 95.1 ms: 1.76x faster                                                       |
| chaos                    | 109 ms                                                       | 62.2 ms: 1.75x faster                                                       |
| deepcopy_memo            | 49.8 us                                                      | 29.1 us: 1.71x faster                                                       |
| logging_silent           | 167 ns                                                       | 99.3 ns: 1.69x faster                                                       |
| crypto_pyaes             | 119 ms                                                       | 72.6 ms: 1.64x faster                                                       |
| deepcopy                 | 468 us                                                       | 286 us: 1.64x faster                                                        |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 575 ms: 1.63x faster                                                        |
| pylint                   | 566 ms                                                       | 348 ms: 1.63x faster                                                        |
| richards_super           | 90.6 ms                                                      | 56.8 ms: 1.60x faster                                                       |
| sqlglot_parse            | 2.24 ms                                                      | 1.40 ms: 1.59x faster                                                       |
| nbody                    | 134 ms                                                       | 85.8 ms: 1.56x faster                                                       |
| scimark_monte_carlo      | 107 ms                                                       | 68.8 ms: 1.56x faster                                                       |
| comprehensions           | 26.7 us                                                      | 17.3 us: 1.54x faster                                                       |
| sqlglot_transpile        | 2.68 ms                                                      | 1.80 ms: 1.49x faster                                                       |
| richards                 | 75.1 ms                                                      | 50.5 ms: 1.49x faster                                                       |
| hexiom                   | 9.42 ms                                                      | 6.36 ms: 1.48x faster                                                       |
| scimark_sor              | 180 ms                                                       | 123 ms: 1.47x faster                                                        |
| pyflate                  | 733 ms                                                       | 503 ms: 1.46x faster                                                        |
| spectral_norm            | 139 ms                                                       | 96.2 ms: 1.45x faster                                                       |
| unpickle_pure_python     | 312 us                                                       | 217 us: 1.44x faster                                                        |
| mako                     | 14.7 ms                                                      | 10.4 ms: 1.42x faster                                                       |
| pickle_pure_python       | 455 us                                                       | 322 us: 1.41x faster                                                        |
| logging_simple           | 8.88 us                                                      | 6.35 us: 1.40x faster                                                       |
| coroutines               | 30.3 ms                                                      | 21.7 ms: 1.39x faster                                                       |
| logging_format           | 9.64 us                                                      | 6.98 us: 1.38x faster                                                       |
| pycparser                | 1.67 sec                                                     | 1.21 sec: 1.38x faster                                                      |
| deepcopy_reduce          | 4.01 us                                                      | 2.91 us: 1.38x faster                                                       |
| float                    | 111 ms                                                       | 80.7 ms: 1.38x faster                                                       |
| regex_compile            | 190 ms                                                       | 138 ms: 1.37x faster                                                        |
| thrift                   | 1.18 ms                                                      | 857 us: 1.37x faster                                                        |
| pathlib                  | 21.4 ms                                                      | 15.7 ms: 1.36x faster                                                       |
| json_dumps               | 14.5 ms                                                      | 10.8 ms: 1.35x faster                                                       |
| tornado_http             | 157 ms                                                       | 116 ms: 1.35x faster                                                        |
| bench_mp_pool            | 6.37 ms                                                      | 4.77 ms: 1.34x faster                                                       |
| html5lib                 | 94.6 ms                                                      | 71.1 ms: 1.33x faster                                                       |
| bench_thread_pool        | 1.14 ms                                                      | 863 us: 1.32x faster                                                        |
| fannkuch                 | 483 ms                                                       | 366 ms: 1.32x faster                                                        |
| pprint_safe_repr         | 1.05 sec                                                     | 803 ms: 1.31x faster                                                        |
| pprint_pformat           | 2.15 sec                                                     | 1.65 sec: 1.30x faster                                                      |
| nqueens                  | 115 ms                                                       | 88.7 ms: 1.30x faster                                                       |
| genshi_text              | 31.4 ms                                                      | 24.3 ms: 1.29x faster                                                       |
| django_template          | 50.2 ms                                                      | 39.0 ms: 1.29x faster                                                       |
| sympy_sum                | 193 ms                                                       | 152 ms: 1.27x faster                                                        |
| xml_etree_process        | 75.9 ms                                                      | 60.1 ms: 1.26x faster                                                       |
| 2to3                     | 350 ms                                                       | 281 ms: 1.25x faster                                                        |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 4.09 ms: 1.24x faster                                                       |
| sympy_str                | 360 ms                                                       | 290 ms: 1.24x faster                                                        |
| scimark_fft              | 361 ms                                                       | 293 ms: 1.23x faster                                                        |
| sympy_integrate          | 28.2 ms                                                      | 23.0 ms: 1.22x faster                                                       |
| mdp                      | 3.01 sec                                                     | 2.47 sec: 1.22x faster                                                      |
| sqlglot_normalize        | 144 ms                                                       | 119 ms: 1.21x faster                                                        |
| dulwich_log              | 81.1 ms                                                      | 67.0 ms: 1.21x faster                                                       |
| unpack_sequence          | 59.9 ns                                                      | 49.6 ns: 1.21x faster                                                       |
| sympy_expand             | 600 ms                                                       | 497 ms: 1.21x faster                                                        |
| json_loads               | 30.3 us                                                      | 25.3 us: 1.20x faster                                                       |
| sqlglot_optimize         | 70.1 ms                                                      | 58.8 ms: 1.19x faster                                                       |
| genshi_xml               | 63.3 ms                                                      | 53.4 ms: 1.19x faster                                                       |
| docutils                 | 3.41 sec                                                     | 2.90 sec: 1.18x faster                                                      |
| async_generators         | 421 ms                                                       | 358 ms: 1.17x faster                                                        |
| tomli_loads              | 2.92 sec                                                     | 2.56 sec: 1.14x faster                                                      |
| xml_etree_parse          | 160 ms                                                       | 143 ms: 1.12x faster                                                        |
| json                     | 5.86 ms                                                      | 5.25 ms: 1.12x faster                                                       |
| regex_dna                | 261 ms                                                       | 236 ms: 1.10x faster                                                        |
| xml_etree_iterparse      | 110 ms                                                       | 100 ms: 1.10x faster                                                        |
| xml_etree_generate       | 92.3 ms                                                      | 84.5 ms: 1.09x faster                                                       |
| sqlite_synth             | 2.99 us                                                      | 2.75 us: 1.09x faster                                                       |
| meteor_contest           | 138 ms                                                       | 129 ms: 1.08x faster                                                        |
| pidigits                 | 271 ms                                                       | 252 ms: 1.07x faster                                                        |
| regex_v8                 | 27.2 ms                                                      | 26.2 ms: 1.04x faster                                                       |
| unpickle_list            | 4.65 us                                                      | 4.60 us: 1.01x faster                                                       |
| pickle                   | 9.89 us                                                      | 10.4 us: 1.06x slower                                                       |
| create_gc_cycles         | 1.76 ms                                                      | 1.91 ms: 1.08x slower                                                       |
| unpickle                 | 13.5 us                                                      | 15.0 us: 1.11x slower                                                       |
| regex_effbot             | 3.09 ms                                                      | 3.45 ms: 1.12x slower                                                       |
| pickle_list              | 4.12 us                                                      | 4.64 us: 1.13x slower                                                       |
| pickle_dict              | 29.5 us                                                      | 33.5 us: 1.13x slower                                                       |
| telco                    | 7.23 ms                                                      | 8.34 ms: 1.15x slower                                                       |
| python_startup           | 11.5 ms                                                      | 13.4 ms: 1.16x slower                                                       |
| python_startup_no_site   | 7.33 ms                                                      | 8.95 ms: 1.22x slower                                                       |
| coverage                 | 63.3 ms                                                      | 82.7 ms: 1.31x slower                                                       |
| gc_traversal             | 3.42 ms                                                      | 4.65 ms: 1.36x slower                                                       |
| Geometric mean           | (ref)                                                        | 1.32x faster                                                                |

Benchmark hidden because not significant (1): asyncio_websockets
Ignored benchmarks (8) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of results/bm-20240914-3.14.0a0-401fff7/bm-20240914-pythonperf2-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

- Geometric mean (including insignificant results): 1.336x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.26x
- 95% likely to have a speedup of 1.25x
- 99% likely to have a speedup of 1.23x

# Memory
- memory change: 1.13x
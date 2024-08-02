# Results vs. 3.10.4

- fork: colesbury
- ref: gh_100240_freelist
- machine: linux-x86_64
- commit hash: 85453d0
- commit date: 2024-07-17
- overall geometric mean: 1.35x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.23x faster
- Memory change: 1.12x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240717-pythonperf2-x86_64-colesbury-gh_100240_freelist-3.14.0a0-85453d0 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 286 ms: 1.22x faster                                                         |
| docutils       | 3.41 sec                                                     | 2.95 sec: 1.16x faster                                                       |
| html5lib       | 94.6 ms                                                      | 73.8 ms: 1.28x faster                                                        |
| tornado_http   | 157 ms                                                       | 118 ms: 1.33x faster                                                         |
| Geometric mean | (ref)                                                        | 1.25x faster                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240717-pythonperf2-x86_64-colesbury-gh_100240_freelist-3.14.0a0-85453d0 |
|-------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_none         | 692 ms                                                       | 334 ms: 2.07x faster                                                         |
| async_tree_memoization  | 819 ms                                                       | 403 ms: 2.03x faster                                                         |
| async_tree_io           | 1.60 sec                                                     | 797 ms: 2.01x faster                                                         |
| async_tree_cpu_io_mixed | 936 ms                                                       | 576 ms: 1.62x faster                                                         |
| Geometric mean          | (ref)                                                        | 1.92x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240717-pythonperf2-x86_64-colesbury-gh_100240_freelist-3.14.0a0-85453d0 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| nbody          | 134 ms                                                       | 86.7 ms: 1.55x faster                                                        |
| float          | 111 ms                                                       | 81.8 ms: 1.36x faster                                                        |
| pidigits       | 271 ms                                                       | 254 ms: 1.07x faster                                                         |
| Geometric mean | (ref)                                                        | 1.31x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240717-pythonperf2-x86_64-colesbury-gh_100240_freelist-3.14.0a0-85453d0 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 140 ms: 1.36x faster                                                         |
| regex_dna      | 261 ms                                                       | 240 ms: 1.09x faster                                                         |
| regex_v8       | 27.2 ms                                                      | 25.1 ms: 1.08x faster                                                        |
| regex_effbot   | 3.09 ms                                                      | 3.57 ms: 1.16x slower                                                        |
| Geometric mean | (ref)                                                        | 1.08x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240717-pythonperf2-x86_64-colesbury-gh_100240_freelist-3.14.0a0-85453d0 |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| unpickle_pure_python | 312 us                                                       | 212 us: 1.47x faster                                                         |
| pickle_pure_python   | 455 us                                                       | 320 us: 1.42x faster                                                         |
| json_dumps           | 14.5 ms                                                      | 10.7 ms: 1.36x faster                                                        |
| xml_etree_process    | 75.9 ms                                                      | 58.9 ms: 1.29x faster                                                        |
| tomli_loads          | 2.92 sec                                                     | 2.45 sec: 1.19x faster                                                       |
| json_loads           | 30.3 us                                                      | 25.5 us: 1.19x faster                                                        |
| xml_etree_parse      | 160 ms                                                       | 140 ms: 1.15x faster                                                         |
| xml_etree_generate   | 92.3 ms                                                      | 83.0 ms: 1.11x faster                                                        |
| xml_etree_iterparse  | 110 ms                                                       | 102 ms: 1.08x faster                                                         |
| Geometric mean       | (ref)                                                        | 1.25x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240717-pythonperf2-x86_64-colesbury-gh_100240_freelist-3.14.0a0-85453d0 |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 13.3 ms: 1.16x slower                                                        |
| python_startup_no_site | 7.33 ms                                                      | 9.01 ms: 1.23x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.19x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240717-pythonperf2-x86_64-colesbury-gh_100240_freelist-3.14.0a0-85453d0 |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 10.5 ms: 1.40x faster                                                        |
| django_template | 50.2 ms                                                      | 38.9 ms: 1.29x faster                                                        |
| genshi_text     | 31.4 ms                                                      | 25.2 ms: 1.25x faster                                                        |
| genshi_xml      | 63.3 ms                                                      | 54.6 ms: 1.16x faster                                                        |
| Geometric mean  | (ref)                                                        | 1.27x faster                                                                 |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240717-pythonperf2-x86_64-colesbury-gh_100240_freelist-3.14.0a0-85453d0 |
|--------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 169 us: 3.18x faster                                                         |
| deltablue                | 7.50 ms                                                      | 3.46 ms: 2.17x faster                                                        |
| asyncio_tcp              | 779 ms                                                       | 374 ms: 2.08x faster                                                         |
| async_tree_none          | 692 ms                                                       | 334 ms: 2.07x faster                                                         |
| async_tree_memoization   | 819 ms                                                       | 403 ms: 2.03x faster                                                         |
| async_tree_io            | 1.60 sec                                                     | 797 ms: 2.01x faster                                                         |
| asyncio_tcp_ssl          | 3.10 sec                                                     | 1.58 sec: 1.97x faster                                                       |
| raytrace                 | 489 ms                                                       | 267 ms: 1.83x faster                                                         |
| chaos                    | 109 ms                                                       | 60.8 ms: 1.79x faster                                                        |
| scimark_lu               | 167 ms                                                       | 95.4 ms: 1.75x faster                                                        |
| generators               | 57.3 ms                                                      | 33.5 ms: 1.71x faster                                                        |
| deepcopy_memo            | 49.8 us                                                      | 29.3 us: 1.70x faster                                                        |
| pylint                   | 566 ms                                                       | 334 ms: 1.69x faster                                                         |
| scimark_sor              | 180 ms                                                       | 107 ms: 1.69x faster                                                         |
| logging_silent           | 167 ns                                                       | 99.6 ns: 1.68x faster                                                        |
| crypto_pyaes             | 119 ms                                                       | 71.7 ms: 1.66x faster                                                        |
| deepcopy                 | 468 us                                                       | 282 us: 1.66x faster                                                         |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 576 ms: 1.62x faster                                                         |
| scimark_monte_carlo      | 107 ms                                                       | 66.6 ms: 1.61x faster                                                        |
| go                       | 262 ms                                                       | 164 ms: 1.60x faster                                                         |
| comprehensions           | 26.7 us                                                      | 17.1 us: 1.56x faster                                                        |
| sqlglot_parse            | 2.24 ms                                                      | 1.43 ms: 1.56x faster                                                        |
| nbody                    | 134 ms                                                       | 86.7 ms: 1.55x faster                                                        |
| pyflate                  | 733 ms                                                       | 476 ms: 1.54x faster                                                         |
| richards_super           | 90.6 ms                                                      | 59.6 ms: 1.52x faster                                                        |
| hexiom                   | 9.42 ms                                                      | 6.26 ms: 1.51x faster                                                        |
| sqlglot_transpile        | 2.68 ms                                                      | 1.81 ms: 1.49x faster                                                        |
| unpickle_pure_python     | 312 us                                                       | 212 us: 1.47x faster                                                         |
| richards                 | 75.1 ms                                                      | 51.7 ms: 1.45x faster                                                        |
| spectral_norm            | 139 ms                                                       | 96.1 ms: 1.45x faster                                                        |
| pickle_pure_python       | 455 us                                                       | 320 us: 1.42x faster                                                         |
| logging_format           | 9.64 us                                                      | 6.84 us: 1.41x faster                                                        |
| logging_simple           | 8.88 us                                                      | 6.32 us: 1.41x faster                                                        |
| mako                     | 14.7 ms                                                      | 10.5 ms: 1.40x faster                                                        |
| deepcopy_reduce          | 4.01 us                                                      | 2.87 us: 1.40x faster                                                        |
| coroutines               | 30.3 ms                                                      | 21.9 ms: 1.38x faster                                                        |
| json_dumps               | 14.5 ms                                                      | 10.7 ms: 1.36x faster                                                        |
| bench_mp_pool            | 6.37 ms                                                      | 4.69 ms: 1.36x faster                                                        |
| float                    | 111 ms                                                       | 81.8 ms: 1.36x faster                                                        |
| regex_compile            | 190 ms                                                       | 140 ms: 1.36x faster                                                         |
| pycparser                | 1.67 sec                                                     | 1.24 sec: 1.35x faster                                                       |
| fannkuch                 | 483 ms                                                       | 360 ms: 1.34x faster                                                         |
| thrift                   | 1.18 ms                                                      | 878 us: 1.34x faster                                                         |
| pathlib                  | 21.4 ms                                                      | 16.0 ms: 1.34x faster                                                        |
| tornado_http             | 157 ms                                                       | 118 ms: 1.33x faster                                                         |
| bench_thread_pool        | 1.14 ms                                                      | 864 us: 1.32x faster                                                         |
| pprint_pformat           | 2.15 sec                                                     | 1.64 sec: 1.31x faster                                                       |
| pprint_safe_repr         | 1.05 sec                                                     | 805 ms: 1.30x faster                                                         |
| django_template          | 50.2 ms                                                      | 38.9 ms: 1.29x faster                                                        |
| xml_etree_process        | 75.9 ms                                                      | 58.9 ms: 1.29x faster                                                        |
| html5lib                 | 94.6 ms                                                      | 73.8 ms: 1.28x faster                                                        |
| nqueens                  | 115 ms                                                       | 89.8 ms: 1.28x faster                                                        |
| sympy_sum                | 193 ms                                                       | 153 ms: 1.26x faster                                                         |
| genshi_text              | 31.4 ms                                                      | 25.2 ms: 1.25x faster                                                        |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 4.11 ms: 1.23x faster                                                        |
| sympy_str                | 360 ms                                                       | 292 ms: 1.23x faster                                                         |
| 2to3                     | 350 ms                                                       | 286 ms: 1.22x faster                                                         |
| scimark_fft              | 361 ms                                                       | 296 ms: 1.22x faster                                                         |
| sympy_integrate          | 28.2 ms                                                      | 23.1 ms: 1.22x faster                                                        |
| sqlglot_normalize        | 144 ms                                                       | 118 ms: 1.22x faster                                                         |
| dulwich_log              | 81.1 ms                                                      | 66.7 ms: 1.22x faster                                                        |
| sympy_expand             | 600 ms                                                       | 500 ms: 1.20x faster                                                         |
| mdp                      | 3.01 sec                                                     | 2.51 sec: 1.20x faster                                                       |
| sqlglot_optimize         | 70.1 ms                                                      | 58.7 ms: 1.20x faster                                                        |
| tomli_loads              | 2.92 sec                                                     | 2.45 sec: 1.19x faster                                                       |
| json_loads               | 30.3 us                                                      | 25.5 us: 1.19x faster                                                        |
| async_generators         | 421 ms                                                       | 360 ms: 1.17x faster                                                         |
| genshi_xml               | 63.3 ms                                                      | 54.6 ms: 1.16x faster                                                        |
| docutils                 | 3.41 sec                                                     | 2.95 sec: 1.16x faster                                                       |
| xml_etree_parse          | 160 ms                                                       | 140 ms: 1.15x faster                                                         |
| xml_etree_generate       | 92.3 ms                                                      | 83.0 ms: 1.11x faster                                                        |
| meteor_contest           | 138 ms                                                       | 125 ms: 1.11x faster                                                         |
| regex_dna                | 261 ms                                                       | 240 ms: 1.09x faster                                                         |
| json                     | 5.86 ms                                                      | 5.42 ms: 1.08x faster                                                        |
| regex_v8                 | 27.2 ms                                                      | 25.1 ms: 1.08x faster                                                        |
| xml_etree_iterparse      | 110 ms                                                       | 102 ms: 1.08x faster                                                         |
| pidigits                 | 271 ms                                                       | 254 ms: 1.07x faster                                                         |
| telco                    | 7.23 ms                                                      | 7.94 ms: 1.10x slower                                                        |
| create_gc_cycles         | 1.76 ms                                                      | 1.99 ms: 1.13x slower                                                        |
| regex_effbot             | 3.09 ms                                                      | 3.57 ms: 1.16x slower                                                        |
| python_startup           | 11.5 ms                                                      | 13.3 ms: 1.16x slower                                                        |
| python_startup_no_site   | 7.33 ms                                                      | 9.01 ms: 1.23x slower                                                        |
| gc_traversal             | 3.42 ms                                                      | 4.47 ms: 1.31x slower                                                        |
| coverage                 | 63.3 ms                                                      | 83.2 ms: 1.32x slower                                                        |
| Geometric mean           | (ref)                                                        | 1.35x faster                                                                 |

Benchmark hidden because not significant (1): asyncio_websockets
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240717-3.14.0a0-85453d0/bm-20240717-pythonperf2-x86_64-colesbury-gh_100240_freelist-3.14.0a0-85453d0.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.27x
- 95% likely to have a speedup of 1.26x
- 99% likely to have a speedup of 1.23x

# Memory
- memory change: 1.12x
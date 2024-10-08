# Results vs. 3.10.4

- fork: mdboom
- ref: simplify_richcompare
- machine: linux-x86_64
- commit hash: 6d5be6d
- commit date: 2024-09-03
- overall geometric mean: 1.36x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.23x faster
- Memory change: 1.13x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240903-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 283 ms: 1.24x faster                                                        |
| docutils       | 3.41 sec                                                     | 2.92 sec: 1.17x faster                                                      |
| html5lib       | 94.6 ms                                                      | 70.2 ms: 1.35x faster                                                       |
| tornado_http   | 157 ms                                                       | 116 ms: 1.35x faster                                                        |
| Geometric mean | (ref)                                                        | 1.28x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240903-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|-------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none         | 692 ms                                                       | 319 ms: 2.17x faster                                                        |
| async_tree_memoization  | 819 ms                                                       | 399 ms: 2.05x faster                                                        |
| async_tree_io           | 1.60 sec                                                     | 818 ms: 1.95x faster                                                        |
| async_tree_cpu_io_mixed | 936 ms                                                       | 569 ms: 1.64x faster                                                        |
| Geometric mean          | (ref)                                                        | 1.94x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240903-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 134 ms                                                       | 91.4 ms: 1.47x faster                                                       |
| float          | 111 ms                                                       | 80.0 ms: 1.39x faster                                                       |
| pidigits       | 271 ms                                                       | 253 ms: 1.07x faster                                                        |
| Geometric mean | (ref)                                                        | 1.30x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240903-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 141 ms: 1.35x faster                                                        |
| regex_dna      | 261 ms                                                       | 232 ms: 1.12x faster                                                        |
| regex_effbot   | 3.09 ms                                                      | 3.48 ms: 1.13x slower                                                       |
| Geometric mean | (ref)                                                        | 1.08x faster                                                                |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240903-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                       | 314 us: 1.45x faster                                                        |
| unpickle_pure_python | 312 us                                                       | 217 us: 1.44x faster                                                        |
| json_dumps           | 14.5 ms                                                      | 10.8 ms: 1.35x faster                                                       |
| xml_etree_process    | 75.9 ms                                                      | 60.0 ms: 1.26x faster                                                       |
| json_loads           | 30.3 us                                                      | 25.3 us: 1.20x faster                                                       |
| tomli_loads          | 2.92 sec                                                     | 2.57 sec: 1.14x faster                                                      |
| xml_etree_parse      | 160 ms                                                       | 145 ms: 1.10x faster                                                        |
| xml_etree_iterparse  | 110 ms                                                       | 103 ms: 1.07x faster                                                        |
| xml_etree_generate   | 92.3 ms                                                      | 86.3 ms: 1.07x faster                                                       |
| Geometric mean       | (ref)                                                        | 1.22x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240903-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 13.4 ms: 1.16x slower                                                       |
| python_startup_no_site | 7.33 ms                                                      | 9.05 ms: 1.23x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.20x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240903-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 10.4 ms: 1.41x faster                                                       |
| django_template | 50.2 ms                                                      | 39.7 ms: 1.27x faster                                                       |
| genshi_text     | 31.4 ms                                                      | 25.9 ms: 1.22x faster                                                       |
| genshi_xml      | 63.3 ms                                                      | 55.2 ms: 1.15x faster                                                       |
| Geometric mean  | (ref)                                                        | 1.26x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240903-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|--------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 176 us: 3.04x faster                                                        |
| deltablue                | 7.50 ms                                                      | 3.43 ms: 2.19x faster                                                       |
| async_tree_none          | 692 ms                                                       | 319 ms: 2.17x faster                                                        |
| asyncio_tcp              | 779 ms                                                       | 370 ms: 2.11x faster                                                        |
| async_tree_memoization   | 819 ms                                                       | 399 ms: 2.05x faster                                                        |
| asyncio_tcp_ssl          | 3.10 sec                                                     | 1.57 sec: 1.97x faster                                                      |
| async_tree_io            | 1.60 sec                                                     | 818 ms: 1.95x faster                                                        |
| generators               | 57.3 ms                                                      | 29.4 ms: 1.95x faster                                                       |
| go                       | 262 ms                                                       | 136 ms: 1.92x faster                                                        |
| raytrace                 | 489 ms                                                       | 268 ms: 1.82x faster                                                        |
| scimark_lu               | 167 ms                                                       | 94.8 ms: 1.76x faster                                                       |
| chaos                    | 109 ms                                                       | 61.8 ms: 1.76x faster                                                       |
| logging_silent           | 167 ns                                                       | 97.4 ns: 1.72x faster                                                       |
| deepcopy_memo            | 49.8 us                                                      | 29.5 us: 1.69x faster                                                       |
| scimark_monte_carlo      | 107 ms                                                       | 64.8 ms: 1.66x faster                                                       |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 569 ms: 1.64x faster                                                        |
| crypto_pyaes             | 119 ms                                                       | 72.8 ms: 1.64x faster                                                       |
| deepcopy                 | 468 us                                                       | 288 us: 1.62x faster                                                        |
| pylint                   | 566 ms                                                       | 350 ms: 1.62x faster                                                        |
| richards_super           | 90.6 ms                                                      | 56.4 ms: 1.61x faster                                                       |
| sqlglot_parse            | 2.24 ms                                                      | 1.42 ms: 1.57x faster                                                       |
| pyflate                  | 733 ms                                                       | 476 ms: 1.54x faster                                                        |
| comprehensions           | 26.7 us                                                      | 17.4 us: 1.54x faster                                                       |
| scimark_sor              | 180 ms                                                       | 118 ms: 1.53x faster                                                        |
| hexiom                   | 9.42 ms                                                      | 6.21 ms: 1.52x faster                                                       |
| richards                 | 75.1 ms                                                      | 50.2 ms: 1.50x faster                                                       |
| sqlglot_transpile        | 2.68 ms                                                      | 1.81 ms: 1.48x faster                                                       |
| nbody                    | 134 ms                                                       | 91.4 ms: 1.47x faster                                                       |
| pickle_pure_python       | 455 us                                                       | 314 us: 1.45x faster                                                        |
| unpickle_pure_python     | 312 us                                                       | 217 us: 1.44x faster                                                        |
| spectral_norm            | 139 ms                                                       | 97.3 ms: 1.43x faster                                                       |
| logging_simple           | 8.88 us                                                      | 6.26 us: 1.42x faster                                                       |
| mako                     | 14.7 ms                                                      | 10.4 ms: 1.41x faster                                                       |
| logging_format           | 9.64 us                                                      | 6.86 us: 1.41x faster                                                       |
| coroutines               | 30.3 ms                                                      | 21.6 ms: 1.40x faster                                                       |
| float                    | 111 ms                                                       | 80.0 ms: 1.39x faster                                                       |
| deepcopy_reduce          | 4.01 us                                                      | 2.92 us: 1.37x faster                                                       |
| thrift                   | 1.18 ms                                                      | 856 us: 1.37x faster                                                        |
| pathlib                  | 21.4 ms                                                      | 15.6 ms: 1.37x faster                                                       |
| bench_mp_pool            | 6.37 ms                                                      | 4.68 ms: 1.36x faster                                                       |
| tornado_http             | 157 ms                                                       | 116 ms: 1.35x faster                                                        |
| regex_compile            | 190 ms                                                       | 141 ms: 1.35x faster                                                        |
| json_dumps               | 14.5 ms                                                      | 10.8 ms: 1.35x faster                                                       |
| html5lib                 | 94.6 ms                                                      | 70.2 ms: 1.35x faster                                                       |
| pycparser                | 1.67 sec                                                     | 1.24 sec: 1.34x faster                                                      |
| fannkuch                 | 483 ms                                                       | 362 ms: 1.33x faster                                                        |
| bench_thread_pool        | 1.14 ms                                                      | 864 us: 1.32x faster                                                        |
| pprint_safe_repr         | 1.05 sec                                                     | 801 ms: 1.31x faster                                                        |
| nqueens                  | 115 ms                                                       | 87.8 ms: 1.31x faster                                                       |
| pprint_pformat           | 2.15 sec                                                     | 1.65 sec: 1.31x faster                                                      |
| sympy_sum                | 193 ms                                                       | 151 ms: 1.28x faster                                                        |
| django_template          | 50.2 ms                                                      | 39.7 ms: 1.27x faster                                                       |
| xml_etree_process        | 75.9 ms                                                      | 60.0 ms: 1.26x faster                                                       |
| sympy_str                | 360 ms                                                       | 289 ms: 1.25x faster                                                        |
| 2to3                     | 350 ms                                                       | 283 ms: 1.24x faster                                                        |
| sympy_integrate          | 28.2 ms                                                      | 23.0 ms: 1.23x faster                                                       |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 4.16 ms: 1.22x faster                                                       |
| mdp                      | 3.01 sec                                                     | 2.47 sec: 1.22x faster                                                      |
| genshi_text              | 31.4 ms                                                      | 25.9 ms: 1.22x faster                                                       |
| sympy_expand             | 600 ms                                                       | 496 ms: 1.21x faster                                                        |
| scimark_fft              | 361 ms                                                       | 300 ms: 1.20x faster                                                        |
| json_loads               | 30.3 us                                                      | 25.3 us: 1.20x faster                                                       |
| sqlglot_normalize        | 144 ms                                                       | 120 ms: 1.20x faster                                                        |
| sqlglot_optimize         | 70.1 ms                                                      | 59.3 ms: 1.18x faster                                                       |
| docutils                 | 3.41 sec                                                     | 2.92 sec: 1.17x faster                                                      |
| async_generators         | 421 ms                                                       | 360 ms: 1.17x faster                                                        |
| genshi_xml               | 63.3 ms                                                      | 55.2 ms: 1.15x faster                                                       |
| tomli_loads              | 2.92 sec                                                     | 2.57 sec: 1.14x faster                                                      |
| regex_dna                | 261 ms                                                       | 232 ms: 1.12x faster                                                        |
| json                     | 5.86 ms                                                      | 5.28 ms: 1.11x faster                                                       |
| meteor_contest           | 138 ms                                                       | 125 ms: 1.11x faster                                                        |
| xml_etree_parse          | 160 ms                                                       | 145 ms: 1.10x faster                                                        |
| xml_etree_iterparse      | 110 ms                                                       | 103 ms: 1.07x faster                                                        |
| pidigits                 | 271 ms                                                       | 253 ms: 1.07x faster                                                        |
| xml_etree_generate       | 92.3 ms                                                      | 86.3 ms: 1.07x faster                                                       |
| regex_effbot             | 3.09 ms                                                      | 3.48 ms: 1.13x slower                                                       |
| telco                    | 7.23 ms                                                      | 8.21 ms: 1.14x slower                                                       |
| create_gc_cycles         | 1.76 ms                                                      | 2.01 ms: 1.14x slower                                                       |
| python_startup           | 11.5 ms                                                      | 13.4 ms: 1.16x slower                                                       |
| python_startup_no_site   | 7.33 ms                                                      | 9.05 ms: 1.23x slower                                                       |
| gc_traversal             | 3.42 ms                                                      | 4.43 ms: 1.30x slower                                                       |
| coverage                 | 63.3 ms                                                      | 82.6 ms: 1.31x slower                                                       |
| Geometric mean           | (ref)                                                        | 1.36x faster                                                                |

Benchmark hidden because not significant (2): regex_v8, asyncio_websockets
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240903-3.14.0a0-6d5be6d/bm-20240903-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.27x
- 95% likely to have a speedup of 1.26x
- 99% likely to have a speedup of 1.23x

# Memory
- memory change: 1.13x
# Results vs. 3.10.4

- fork: colesbury
- ref: gh_117376_pydecref_m
- machine: linux-x86_64
- commit hash: 4b27f3a
- commit date: 2024-08-13
- overall geometric mean: 1.10x slower
- HPT reliability: 99.99%
- HPT 99th percentile: 1.04x slower
- Memory change: 1.31x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240813-pythonperf2-x86_64-colesbury-gh_117376_pydecref_m-3.14.0a0-4b27f3a |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 431 ms: 1.23x slower                                                           |
| docutils       | 3.41 sec                                                     | 3.48 sec: 1.02x slower                                                         |
| html5lib       | 94.6 ms                                                      | 109 ms: 1.15x slower                                                           |
| tornado_http   | 157 ms                                                       | 165 ms: 1.05x slower                                                           |
| Geometric mean | (ref)                                                        | 1.11x slower                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240813-pythonperf2-x86_64-colesbury-gh_117376_pydecref_m-3.14.0a0-4b27f3a |
|-------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_io           | 1.60 sec                                                     | 940 ms: 1.70x faster                                                           |
| async_tree_none         | 692 ms                                                       | 413 ms: 1.67x faster                                                           |
| async_tree_memoization  | 819 ms                                                       | 514 ms: 1.59x faster                                                           |
| async_tree_cpu_io_mixed | 936 ms                                                       | 678 ms: 1.38x faster                                                           |
| Geometric mean          | (ref)                                                        | 1.58x faster                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240813-pythonperf2-x86_64-colesbury-gh_117376_pydecref_m-3.14.0a0-4b27f3a |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pidigits       | 271 ms                                                       | 250 ms: 1.08x faster                                                           |
| float          | 111 ms                                                       | 142 ms: 1.28x slower                                                           |
| nbody          | 134 ms                                                       | 193 ms: 1.44x slower                                                           |
| Geometric mean | (ref)                                                        | 1.19x slower                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240813-pythonperf2-x86_64-colesbury-gh_117376_pydecref_m-3.14.0a0-4b27f3a |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_dna      | 261 ms                                                       | 248 ms: 1.05x faster                                                           |
| regex_v8       | 27.2 ms                                                      | 27.4 ms: 1.01x slower                                                          |
| regex_effbot   | 3.09 ms                                                      | 3.65 ms: 1.18x slower                                                          |
| regex_compile  | 190 ms                                                       | 229 ms: 1.20x slower                                                           |
| Geometric mean | (ref)                                                        | 1.08x slower                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240813-pythonperf2-x86_64-colesbury-gh_117376_pydecref_m-3.14.0a0-4b27f3a |
|----------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| xml_etree_parse      | 160 ms                                                       | 138 ms: 1.16x faster                                                           |
| json_dumps           | 14.5 ms                                                      | 14.1 ms: 1.03x faster                                                          |
| xml_etree_iterparse  | 110 ms                                                       | 109 ms: 1.01x faster                                                           |
| json_loads           | 30.3 us                                                      | 30.0 us: 1.01x faster                                                          |
| tomli_loads          | 2.92 sec                                                     | 3.32 sec: 1.14x slower                                                         |
| xml_etree_process    | 75.9 ms                                                      | 96.1 ms: 1.26x slower                                                          |
| xml_etree_generate   | 92.3 ms                                                      | 118 ms: 1.28x slower                                                           |
| pickle_pure_python   | 455 us                                                       | 594 us: 1.30x slower                                                           |
| unpickle_pure_python | 312 us                                                       | 409 us: 1.31x slower                                                           |
| Geometric mean       | (ref)                                                        | 1.11x slower                                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240813-pythonperf2-x86_64-colesbury-gh_117376_pydecref_m-3.14.0a0-4b27f3a |
|------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 17.1 ms: 1.49x slower                                                          |
| python_startup_no_site | 7.33 ms                                                      | 11.8 ms: 1.61x slower                                                          |
| Geometric mean         | (ref)                                                        | 1.55x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240813-pythonperf2-x86_64-colesbury-gh_117376_pydecref_m-3.14.0a0-4b27f3a |
|-----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| genshi_xml      | 63.3 ms                                                      | 82.9 ms: 1.31x slower                                                          |
| django_template | 50.2 ms                                                      | 67.7 ms: 1.35x slower                                                          |
| genshi_text     | 31.4 ms                                                      | 44.1 ms: 1.40x slower                                                          |
| mako            | 14.7 ms                                                      | 22.3 ms: 1.51x slower                                                          |
| Geometric mean  | (ref)                                                        | 1.39x slower                                                                   |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240813-pythonperf2-x86_64-colesbury-gh_117376_pydecref_m-3.14.0a0-4b27f3a |
|--------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 282 us: 1.90x faster                                                           |
| asyncio_tcp_ssl          | 3.10 sec                                                     | 1.77 sec: 1.76x faster                                                         |
| asyncio_tcp              | 779 ms                                                       | 449 ms: 1.74x faster                                                           |
| async_tree_io            | 1.60 sec                                                     | 940 ms: 1.70x faster                                                           |
| async_tree_none          | 692 ms                                                       | 413 ms: 1.67x faster                                                           |
| async_tree_memoization   | 819 ms                                                       | 514 ms: 1.59x faster                                                           |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 678 ms: 1.38x faster                                                           |
| generators               | 57.3 ms                                                      | 41.7 ms: 1.37x faster                                                          |
| pylint                   | 566 ms                                                       | 432 ms: 1.31x faster                                                           |
| bench_mp_pool            | 6.37 ms                                                      | 4.91 ms: 1.30x faster                                                          |
| xml_etree_parse          | 160 ms                                                       | 138 ms: 1.16x faster                                                           |
| pidigits                 | 271 ms                                                       | 250 ms: 1.08x faster                                                           |
| pathlib                  | 21.4 ms                                                      | 19.9 ms: 1.07x faster                                                          |
| coroutines               | 30.3 ms                                                      | 28.3 ms: 1.07x faster                                                          |
| regex_dna                | 261 ms                                                       | 248 ms: 1.05x faster                                                           |
| create_gc_cycles         | 1.76 ms                                                      | 1.68 ms: 1.05x faster                                                          |
| gc_traversal             | 3.42 ms                                                      | 3.27 ms: 1.04x faster                                                          |
| deepcopy                 | 468 us                                                       | 451 us: 1.04x faster                                                           |
| json_dumps               | 14.5 ms                                                      | 14.1 ms: 1.03x faster                                                          |
| asyncio_websockets       | 390 ms                                                       | 384 ms: 1.02x faster                                                           |
| xml_etree_iterparse      | 110 ms                                                       | 109 ms: 1.01x faster                                                           |
| json_loads               | 30.3 us                                                      | 30.0 us: 1.01x faster                                                          |
| regex_v8                 | 27.2 ms                                                      | 27.4 ms: 1.01x slower                                                          |
| crypto_pyaes             | 119 ms                                                       | 121 ms: 1.01x slower                                                           |
| docutils                 | 3.41 sec                                                     | 3.48 sec: 1.02x slower                                                         |
| pycparser                | 1.67 sec                                                     | 1.73 sec: 1.03x slower                                                         |
| pyflate                  | 733 ms                                                       | 763 ms: 1.04x slower                                                           |
| json                     | 5.86 ms                                                      | 6.15 ms: 1.05x slower                                                          |
| tornado_http             | 157 ms                                                       | 165 ms: 1.05x slower                                                           |
| deepcopy_memo            | 49.8 us                                                      | 53.0 us: 1.06x slower                                                          |
| mdp                      | 3.01 sec                                                     | 3.21 sec: 1.07x slower                                                         |
| richards                 | 75.1 ms                                                      | 80.8 ms: 1.08x slower                                                          |
| richards_super           | 90.6 ms                                                      | 98.7 ms: 1.09x slower                                                          |
| logging_silent           | 167 ns                                                       | 183 ns: 1.09x slower                                                           |
| deltablue                | 7.50 ms                                                      | 8.25 ms: 1.10x slower                                                          |
| nqueens                  | 115 ms                                                       | 128 ms: 1.11x slower                                                           |
| comprehensions           | 26.7 us                                                      | 30.0 us: 1.12x slower                                                          |
| chaos                    | 109 ms                                                       | 124 ms: 1.14x slower                                                           |
| tomli_loads              | 2.92 sec                                                     | 3.32 sec: 1.14x slower                                                         |
| sympy_integrate          | 28.2 ms                                                      | 32.1 ms: 1.14x slower                                                          |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 5.80 ms: 1.14x slower                                                          |
| html5lib                 | 94.6 ms                                                      | 109 ms: 1.15x slower                                                           |
| scimark_fft              | 361 ms                                                       | 425 ms: 1.18x slower                                                           |
| thrift                   | 1.18 ms                                                      | 1.38 ms: 1.18x slower                                                          |
| fannkuch                 | 483 ms                                                       | 569 ms: 1.18x slower                                                           |
| regex_effbot             | 3.09 ms                                                      | 3.65 ms: 1.18x slower                                                          |
| async_generators         | 421 ms                                                       | 499 ms: 1.19x slower                                                           |
| deepcopy_reduce          | 4.01 us                                                      | 4.77 us: 1.19x slower                                                          |
| spectral_norm            | 139 ms                                                       | 166 ms: 1.20x slower                                                           |
| regex_compile            | 190 ms                                                       | 229 ms: 1.20x slower                                                           |
| raytrace                 | 489 ms                                                       | 599 ms: 1.22x slower                                                           |
| 2to3                     | 350 ms                                                       | 431 ms: 1.23x slower                                                           |
| hexiom                   | 9.42 ms                                                      | 11.7 ms: 1.24x slower                                                          |
| scimark_monte_carlo      | 107 ms                                                       | 134 ms: 1.24x slower                                                           |
| meteor_contest           | 138 ms                                                       | 174 ms: 1.26x slower                                                           |
| sympy_str                | 360 ms                                                       | 453 ms: 1.26x slower                                                           |
| go                       | 262 ms                                                       | 330 ms: 1.26x slower                                                           |
| xml_etree_process        | 75.9 ms                                                      | 96.1 ms: 1.26x slower                                                          |
| sqlglot_transpile        | 2.68 ms                                                      | 3.40 ms: 1.27x slower                                                          |
| float                    | 111 ms                                                       | 142 ms: 1.28x slower                                                           |
| xml_etree_generate       | 92.3 ms                                                      | 118 ms: 1.28x slower                                                           |
| sqlglot_parse            | 2.24 ms                                                      | 2.87 ms: 1.28x slower                                                          |
| sqlglot_normalize        | 144 ms                                                       | 186 ms: 1.29x slower                                                           |
| logging_format           | 9.64 us                                                      | 12.6 us: 1.30x slower                                                          |
| pickle_pure_python       | 455 us                                                       | 594 us: 1.30x slower                                                           |
| genshi_xml               | 63.3 ms                                                      | 82.9 ms: 1.31x slower                                                          |
| unpickle_pure_python     | 312 us                                                       | 409 us: 1.31x slower                                                           |
| logging_simple           | 8.88 us                                                      | 11.7 us: 1.32x slower                                                          |
| scimark_sor              | 180 ms                                                       | 240 ms: 1.33x slower                                                           |
| sqlglot_optimize         | 70.1 ms                                                      | 93.5 ms: 1.33x slower                                                          |
| django_template          | 50.2 ms                                                      | 67.7 ms: 1.35x slower                                                          |
| pprint_safe_repr         | 1.05 sec                                                     | 1.42 sec: 1.35x slower                                                         |
| pprint_pformat           | 2.15 sec                                                     | 2.92 sec: 1.36x slower                                                         |
| sympy_sum                | 193 ms                                                       | 262 ms: 1.36x slower                                                           |
| sympy_expand             | 600 ms                                                       | 819 ms: 1.37x slower                                                           |
| genshi_text              | 31.4 ms                                                      | 44.1 ms: 1.40x slower                                                          |
| scimark_lu               | 167 ms                                                       | 235 ms: 1.41x slower                                                           |
| nbody                    | 134 ms                                                       | 193 ms: 1.44x slower                                                           |
| telco                    | 7.23 ms                                                      | 10.5 ms: 1.45x slower                                                          |
| python_startup           | 11.5 ms                                                      | 17.1 ms: 1.49x slower                                                          |
| bench_thread_pool        | 1.14 ms                                                      | 1.71 ms: 1.49x slower                                                          |
| mako                     | 14.7 ms                                                      | 22.3 ms: 1.51x slower                                                          |
| python_startup_no_site   | 7.33 ms                                                      | 11.8 ms: 1.61x slower                                                          |
| coverage                 | 63.3 ms                                                      | 104 ms: 1.64x slower                                                           |
| Geometric mean           | (ref)                                                        | 1.10x slower                                                                   |
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240813-3.14.0a0-4b27f3a-NOGIL/bm-20240813-pythonperf2-x86_64-colesbury-gh_117376_pydecref_m-3.14.0a0-4b27f3a.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 99.99% likely to be slow
- 90% likely to have a slowdown of 1.08x
- 95% likely to have a slowdown of 1.07x
- 99% likely to have a slowdown of 1.04x

# Memory
- memory change: 1.31x
# Results vs. 3.10.4

- fork: mdboom
- ref: simplify_richcompare
- machine: windows-x86
- commit hash: c9a5962
- commit date: 2024-08-29
- overall geometric mean: 1.13x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240829-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 248 ms: 1.07x faster                                                           |
| docutils       | 1.95 sec                                                        | 1.86 sec: 1.05x faster                                                         |
| html5lib       | 52.1 ms                                                         | 45.8 ms: 1.14x faster                                                          |
| tornado_http   | 118 ms                                                          | 104 ms: 1.13x faster                                                           |
| Geometric mean | (ref)                                                           | 1.09x faster                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240829-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|-------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 922 ms                                                          | 464 ms: 1.99x faster                                                           |
| async_tree_none         | 394 ms                                                          | 213 ms: 1.85x faster                                                           |
| async_tree_io           | 940 ms                                                          | 533 ms: 1.76x faster                                                           |
| async_tree_memoization  | 467 ms                                                          | 274 ms: 1.70x faster                                                           |
| Geometric mean          | (ref)                                                           | 1.82x faster                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240829-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 201 ms: 2.50x faster                                                           |
| float          | 69.6 ms                                                         | 62.2 ms: 1.12x faster                                                          |
| nbody          | 79.1 ms                                                         | 94.3 ms: 1.19x slower                                                          |
| Geometric mean | (ref)                                                           | 1.33x faster                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240829-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_dna      | 131 ms                                                          | 118 ms: 1.10x faster                                                           |
| regex_compile  | 117 ms                                                          | 107 ms: 1.09x faster                                                           |
| regex_v8       | 15.8 ms                                                         | 16.2 ms: 1.03x slower                                                          |
| regex_effbot   | 1.66 ms                                                         | 1.92 ms: 1.15x slower                                                          |
| Geometric mean | (ref)                                                           | 1.00x faster                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240829-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|----------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| json_dumps           | 9.82 ms                                                         | 7.39 ms: 1.33x faster                                                          |
| json_loads           | 22.4 us                                                         | 20.3 us: 1.10x faster                                                          |
| xml_etree_parse      | 120 ms                                                          | 109 ms: 1.10x faster                                                           |
| pickle_pure_python   | 280 us                                                          | 263 us: 1.07x faster                                                           |
| tomli_loads          | 1.91 sec                                                        | 1.84 sec: 1.04x faster                                                         |
| unpickle_pure_python | 189 us                                                          | 183 us: 1.04x faster                                                           |
| xml_etree_iterparse  | 70.8 ms                                                         | 68.8 ms: 1.03x faster                                                          |
| xml_etree_process    | 48.1 ms                                                         | 49.9 ms: 1.04x slower                                                          |
| xml_etree_generate   | 61.6 ms                                                         | 67.5 ms: 1.10x slower                                                          |
| Geometric mean       | (ref)                                                           | 1.06x faster                                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240829-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup         | 22.9 ms                                                         | 24.0 ms: 1.05x slower                                                          |
| python_startup_no_site | 18.1 ms                                                         | 20.1 ms: 1.11x slower                                                          |
| Geometric mean         | (ref)                                                           | 1.08x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240829-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|-----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| django_template | 36.0 ms                                                         | 31.9 ms: 1.13x faster                                                          |
| mako            | 9.10 ms                                                         | 8.24 ms: 1.10x faster                                                          |
| genshi_xml      | 46.6 ms                                                         | 46.1 ms: 1.01x faster                                                          |
| genshi_text     | 21.0 ms                                                         | 22.0 ms: 1.05x slower                                                          |
| Geometric mean  | (ref)                                                           | 1.05x faster                                                                   |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240829-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|--------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| typing_runtime_protocols | 396 us                                                          | 143 us: 2.77x faster                                                           |
| pidigits                 | 502 ms                                                          | 201 ms: 2.50x faster                                                           |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 464 ms: 1.99x faster                                                           |
| async_tree_none          | 394 ms                                                          | 213 ms: 1.85x faster                                                           |
| async_tree_io            | 940 ms                                                          | 533 ms: 1.76x faster                                                           |
| async_tree_memoization   | 467 ms                                                          | 274 ms: 1.70x faster                                                           |
| pylint                   | 384 ms                                                          | 234 ms: 1.64x faster                                                           |
| deltablue                | 4.04 ms                                                         | 2.71 ms: 1.49x faster                                                          |
| crypto_pyaes             | 81.3 ms                                                         | 56.7 ms: 1.43x faster                                                          |
| chaos                    | 74.4 ms                                                         | 52.8 ms: 1.41x faster                                                          |
| go                       | 146 ms                                                          | 104 ms: 1.40x faster                                                           |
| logging_silent           | 97.9 ns                                                         | 73.1 ns: 1.34x faster                                                          |
| deepcopy_memo            | 29.6 us                                                         | 22.2 us: 1.33x faster                                                          |
| json_dumps               | 9.82 ms                                                         | 7.39 ms: 1.33x faster                                                          |
| raytrace                 | 303 ms                                                          | 229 ms: 1.32x faster                                                           |
| scimark_lu               | 89.8 ms                                                         | 68.7 ms: 1.31x faster                                                          |
| comprehensions           | 17.7 us                                                         | 13.7 us: 1.30x faster                                                          |
| deepcopy                 | 310 us                                                          | 242 us: 1.28x faster                                                           |
| thrift                   | 902 us                                                          | 719 us: 1.26x faster                                                           |
| sqlglot_parse            | 1.33 ms                                                         | 1.07 ms: 1.24x faster                                                          |
| pycparser                | 1.04 sec                                                        | 862 ms: 1.21x faster                                                           |
| sqlglot_transpile        | 1.58 ms                                                         | 1.32 ms: 1.20x faster                                                          |
| pyflate                  | 422 ms                                                          | 354 ms: 1.19x faster                                                           |
| hexiom                   | 6.13 ms                                                         | 5.20 ms: 1.18x faster                                                          |
| generators               | 31.6 ms                                                         | 26.8 ms: 1.18x faster                                                          |
| dulwich_log              | 58.5 ms                                                         | 49.9 ms: 1.17x faster                                                          |
| nqueens                  | 87.1 ms                                                         | 75.3 ms: 1.16x faster                                                          |
| sympy_sum                | 122 ms                                                          | 107 ms: 1.14x faster                                                           |
| html5lib                 | 52.1 ms                                                         | 45.8 ms: 1.14x faster                                                          |
| richards_super           | 49.9 ms                                                         | 43.9 ms: 1.14x faster                                                          |
| tornado_http             | 118 ms                                                          | 104 ms: 1.13x faster                                                           |
| django_template          | 36.0 ms                                                         | 31.9 ms: 1.13x faster                                                          |
| scimark_sor              | 115 ms                                                          | 103 ms: 1.12x faster                                                           |
| float                    | 69.6 ms                                                         | 62.2 ms: 1.12x faster                                                          |
| deepcopy_reduce          | 2.68 us                                                         | 2.42 us: 1.11x faster                                                          |
| json                     | 4.76 ms                                                         | 4.30 ms: 1.11x faster                                                          |
| mako                     | 9.10 ms                                                         | 8.24 ms: 1.10x faster                                                          |
| json_loads               | 22.4 us                                                         | 20.3 us: 1.10x faster                                                          |
| xml_etree_parse          | 120 ms                                                          | 109 ms: 1.10x faster                                                           |
| regex_dna                | 131 ms                                                          | 118 ms: 1.10x faster                                                           |
| bench_thread_pool        | 1.12 ms                                                         | 1.03 ms: 1.09x faster                                                          |
| regex_compile            | 117 ms                                                          | 107 ms: 1.09x faster                                                           |
| scimark_monte_carlo      | 61.9 ms                                                         | 57.4 ms: 1.08x faster                                                          |
| sympy_integrate          | 16.6 ms                                                         | 15.5 ms: 1.07x faster                                                          |
| 2to3                     | 265 ms                                                          | 248 ms: 1.07x faster                                                           |
| sympy_str                | 229 ms                                                          | 215 ms: 1.07x faster                                                           |
| pickle_pure_python       | 280 us                                                          | 263 us: 1.07x faster                                                           |
| mdp                      | 1.83 sec                                                        | 1.72 sec: 1.06x faster                                                         |
| docutils                 | 1.95 sec                                                        | 1.86 sec: 1.05x faster                                                         |
| tomli_loads              | 1.91 sec                                                        | 1.84 sec: 1.04x faster                                                         |
| unpickle_pure_python     | 189 us                                                          | 183 us: 1.04x faster                                                           |
| spectral_norm            | 80.2 ms                                                         | 77.6 ms: 1.03x faster                                                          |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 3.14 ms: 1.03x faster                                                          |
| pprint_pformat           | 1.37 sec                                                        | 1.33 sec: 1.03x faster                                                         |
| asyncio_tcp              | 744 ms                                                          | 722 ms: 1.03x faster                                                           |
| xml_etree_iterparse      | 70.8 ms                                                         | 68.8 ms: 1.03x faster                                                          |
| coroutines               | 17.9 ms                                                         | 17.4 ms: 1.03x faster                                                          |
| pprint_safe_repr         | 658 ms                                                          | 642 ms: 1.03x faster                                                           |
| richards                 | 40.3 ms                                                         | 39.4 ms: 1.02x faster                                                          |
| sqlglot_normalize        | 230 ms                                                          | 225 ms: 1.02x faster                                                           |
| sympy_expand             | 391 ms                                                          | 383 ms: 1.02x faster                                                           |
| sqlglot_optimize         | 44.7 ms                                                         | 43.8 ms: 1.02x faster                                                          |
| genshi_xml               | 46.6 ms                                                         | 46.1 ms: 1.01x faster                                                          |
| asyncio_tcp_ssl          | 17.0 sec                                                        | 17.1 sec: 1.01x slower                                                         |
| regex_v8                 | 15.8 ms                                                         | 16.2 ms: 1.03x slower                                                          |
| meteor_contest           | 80.0 ms                                                         | 82.8 ms: 1.03x slower                                                          |
| xml_etree_process        | 48.1 ms                                                         | 49.9 ms: 1.04x slower                                                          |
| python_startup           | 22.9 ms                                                         | 24.0 ms: 1.05x slower                                                          |
| genshi_text              | 21.0 ms                                                         | 22.0 ms: 1.05x slower                                                          |
| fannkuch                 | 317 ms                                                          | 336 ms: 1.06x slower                                                           |
| create_gc_cycles         | 694 us                                                          | 744 us: 1.07x slower                                                           |
| pathlib                  | 81.2 ms                                                         | 87.4 ms: 1.08x slower                                                          |
| logging_simple           | 7.29 us                                                         | 7.94 us: 1.09x slower                                                          |
| logging_format           | 7.91 us                                                         | 8.61 us: 1.09x slower                                                          |
| xml_etree_generate       | 61.6 ms                                                         | 67.5 ms: 1.10x slower                                                          |
| scimark_fft              | 216 ms                                                          | 237 ms: 1.10x slower                                                           |
| bench_mp_pool            | 66.4 ms                                                         | 73.2 ms: 1.10x slower                                                          |
| python_startup_no_site   | 18.1 ms                                                         | 20.1 ms: 1.11x slower                                                          |
| gc_traversal             | 1.28 ms                                                         | 1.45 ms: 1.13x slower                                                          |
| coverage                 | 46.6 ms                                                         | 53.6 ms: 1.15x slower                                                          |
| regex_effbot             | 1.66 ms                                                         | 1.92 ms: 1.15x slower                                                          |
| nbody                    | 79.1 ms                                                         | 94.3 ms: 1.19x slower                                                          |
| async_generators         | 241 ms                                                          | 292 ms: 1.21x slower                                                           |
| telco                    | 4.83 ms                                                         | 6.69 ms: 1.39x slower                                                          |
| Geometric mean           | (ref)                                                           | 1.13x faster                                                                   |
Ignored benchmarks (14) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (4) of results/bm-20240829-3.14.0a0-c9a5962/bm-20240829-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-c9a5962.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: unknown
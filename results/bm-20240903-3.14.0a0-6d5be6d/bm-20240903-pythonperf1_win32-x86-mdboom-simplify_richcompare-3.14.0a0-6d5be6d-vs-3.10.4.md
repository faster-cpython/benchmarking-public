# Results vs. 3.10.4

- fork: mdboom
- ref: simplify_richcompare
- machine: windows-x86
- commit hash: 6d5be6d
- commit date: 2024-09-03
- overall geometric mean: 1.12x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240903-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 249 ms: 1.06x faster                                                           |
| docutils       | 1.95 sec                                                        | 1.86 sec: 1.05x faster                                                         |
| html5lib       | 52.1 ms                                                         | 46.1 ms: 1.13x faster                                                          |
| tornado_http   | 118 ms                                                          | 104 ms: 1.13x faster                                                           |
| Geometric mean | (ref)                                                           | 1.09x faster                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240903-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|-------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 922 ms                                                          | 465 ms: 1.98x faster                                                           |
| async_tree_none         | 394 ms                                                          | 216 ms: 1.83x faster                                                           |
| async_tree_io           | 940 ms                                                          | 531 ms: 1.77x faster                                                           |
| async_tree_memoization  | 467 ms                                                          | 272 ms: 1.72x faster                                                           |
| Geometric mean          | (ref)                                                           | 1.82x faster                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240903-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 202 ms: 2.49x faster                                                           |
| float          | 69.6 ms                                                         | 61.5 ms: 1.13x faster                                                          |
| nbody          | 79.1 ms                                                         | 96.0 ms: 1.21x slower                                                          |
| Geometric mean | (ref)                                                           | 1.32x faster                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240903-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_compile  | 117 ms                                                          | 107 ms: 1.09x faster                                                           |
| regex_dna      | 131 ms                                                          | 121 ms: 1.08x faster                                                           |
| regex_v8       | 15.8 ms                                                         | 16.4 ms: 1.04x slower                                                          |
| regex_effbot   | 1.66 ms                                                         | 1.93 ms: 1.16x slower                                                          |
| Geometric mean | (ref)                                                           | 1.01x slower                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240903-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|----------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| json_dumps           | 9.82 ms                                                         | 7.46 ms: 1.32x faster                                                          |
| xml_etree_parse      | 120 ms                                                          | 107 ms: 1.12x faster                                                           |
| pickle_pure_python   | 280 us                                                          | 251 us: 1.12x faster                                                           |
| json_loads           | 22.4 us                                                         | 21.1 us: 1.06x faster                                                          |
| unpickle_pure_python | 189 us                                                          | 179 us: 1.06x faster                                                           |
| xml_etree_iterparse  | 70.8 ms                                                         | 67.7 ms: 1.05x faster                                                          |
| tomli_loads          | 1.91 sec                                                        | 1.86 sec: 1.03x faster                                                         |
| xml_etree_process    | 48.1 ms                                                         | 50.0 ms: 1.04x slower                                                          |
| xml_etree_generate   | 61.6 ms                                                         | 67.3 ms: 1.09x slower                                                          |
| Geometric mean       | (ref)                                                           | 1.06x faster                                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240903-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup         | 22.9 ms                                                         | 23.8 ms: 1.04x slower                                                          |
| python_startup_no_site | 18.1 ms                                                         | 19.7 ms: 1.09x slower                                                          |
| Geometric mean         | (ref)                                                           | 1.07x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240903-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|-----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako            | 9.10 ms                                                         | 8.20 ms: 1.11x faster                                                          |
| django_template | 36.0 ms                                                         | 32.9 ms: 1.10x faster                                                          |
| genshi_xml      | 46.6 ms                                                         | 46.1 ms: 1.01x faster                                                          |
| genshi_text     | 21.0 ms                                                         | 21.9 ms: 1.04x slower                                                          |
| Geometric mean  | (ref)                                                           | 1.04x faster                                                                   |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240903-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|--------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| typing_runtime_protocols | 396 us                                                          | 149 us: 2.66x faster                                                           |
| pidigits                 | 502 ms                                                          | 202 ms: 2.49x faster                                                           |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 465 ms: 1.98x faster                                                           |
| async_tree_none          | 394 ms                                                          | 216 ms: 1.83x faster                                                           |
| async_tree_io            | 940 ms                                                          | 531 ms: 1.77x faster                                                           |
| async_tree_memoization   | 467 ms                                                          | 272 ms: 1.72x faster                                                           |
| pylint                   | 384 ms                                                          | 235 ms: 1.63x faster                                                           |
| deltablue                | 4.04 ms                                                         | 2.75 ms: 1.46x faster                                                          |
| go                       | 146 ms                                                          | 104 ms: 1.40x faster                                                           |
| chaos                    | 74.4 ms                                                         | 54.1 ms: 1.37x faster                                                          |
| crypto_pyaes             | 81.3 ms                                                         | 59.5 ms: 1.37x faster                                                          |
| deepcopy_memo            | 29.6 us                                                         | 22.0 us: 1.34x faster                                                          |
| json_dumps               | 9.82 ms                                                         | 7.46 ms: 1.32x faster                                                          |
| raytrace                 | 303 ms                                                          | 231 ms: 1.31x faster                                                           |
| logging_silent           | 97.9 ns                                                         | 74.8 ns: 1.31x faster                                                          |
| comprehensions           | 17.7 us                                                         | 13.6 us: 1.31x faster                                                          |
| deepcopy                 | 310 us                                                          | 238 us: 1.30x faster                                                           |
| scimark_lu               | 89.8 ms                                                         | 70.0 ms: 1.28x faster                                                          |
| sqlglot_parse            | 1.33 ms                                                         | 1.07 ms: 1.24x faster                                                          |
| thrift                   | 902 us                                                          | 741 us: 1.22x faster                                                           |
| dulwich_log              | 58.5 ms                                                         | 49.2 ms: 1.19x faster                                                          |
| sqlglot_transpile        | 1.58 ms                                                         | 1.33 ms: 1.19x faster                                                          |
| pyflate                  | 422 ms                                                          | 358 ms: 1.18x faster                                                           |
| pycparser                | 1.04 sec                                                        | 888 ms: 1.17x faster                                                           |
| hexiom                   | 6.13 ms                                                         | 5.36 ms: 1.14x faster                                                          |
| sympy_sum                | 122 ms                                                          | 107 ms: 1.14x faster                                                           |
| generators               | 31.6 ms                                                         | 27.6 ms: 1.14x faster                                                          |
| float                    | 69.6 ms                                                         | 61.5 ms: 1.13x faster                                                          |
| html5lib                 | 52.1 ms                                                         | 46.1 ms: 1.13x faster                                                          |
| scimark_sor              | 115 ms                                                          | 102 ms: 1.13x faster                                                           |
| tornado_http             | 118 ms                                                          | 104 ms: 1.13x faster                                                           |
| xml_etree_parse          | 120 ms                                                          | 107 ms: 1.12x faster                                                           |
| pickle_pure_python       | 280 us                                                          | 251 us: 1.12x faster                                                           |
| json                     | 4.76 ms                                                         | 4.28 ms: 1.11x faster                                                          |
| mako                     | 9.10 ms                                                         | 8.20 ms: 1.11x faster                                                          |
| bench_thread_pool        | 1.12 ms                                                         | 1.01 ms: 1.11x faster                                                          |
| scimark_monte_carlo      | 61.9 ms                                                         | 56.4 ms: 1.10x faster                                                          |
| nqueens                  | 87.1 ms                                                         | 79.3 ms: 1.10x faster                                                          |
| django_template          | 36.0 ms                                                         | 32.9 ms: 1.10x faster                                                          |
| deepcopy_reduce          | 2.68 us                                                         | 2.46 us: 1.09x faster                                                          |
| regex_compile            | 117 ms                                                          | 107 ms: 1.09x faster                                                           |
| regex_dna                | 131 ms                                                          | 121 ms: 1.08x faster                                                           |
| sympy_integrate          | 16.6 ms                                                         | 15.5 ms: 1.08x faster                                                          |
| mdp                      | 1.83 sec                                                        | 1.70 sec: 1.08x faster                                                         |
| 2to3                     | 265 ms                                                          | 249 ms: 1.06x faster                                                           |
| richards_super           | 49.9 ms                                                         | 46.9 ms: 1.06x faster                                                          |
| json_loads               | 22.4 us                                                         | 21.1 us: 1.06x faster                                                          |
| sympy_str                | 229 ms                                                          | 216 ms: 1.06x faster                                                           |
| unpickle_pure_python     | 189 us                                                          | 179 us: 1.06x faster                                                           |
| docutils                 | 1.95 sec                                                        | 1.86 sec: 1.05x faster                                                         |
| xml_etree_iterparse      | 70.8 ms                                                         | 67.7 ms: 1.05x faster                                                          |
| sqlglot_optimize         | 44.7 ms                                                         | 42.9 ms: 1.04x faster                                                          |
| spectral_norm            | 80.2 ms                                                         | 76.9 ms: 1.04x faster                                                          |
| asyncio_tcp              | 744 ms                                                          | 716 ms: 1.04x faster                                                           |
| sqlglot_normalize        | 230 ms                                                          | 223 ms: 1.03x faster                                                           |
| pprint_pformat           | 1.37 sec                                                        | 1.32 sec: 1.03x faster                                                         |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 3.15 ms: 1.03x faster                                                          |
| tomli_loads              | 1.91 sec                                                        | 1.86 sec: 1.03x faster                                                         |
| pprint_safe_repr         | 658 ms                                                          | 643 ms: 1.02x faster                                                           |
| sympy_expand             | 391 ms                                                          | 384 ms: 1.02x faster                                                           |
| genshi_xml               | 46.6 ms                                                         | 46.1 ms: 1.01x faster                                                          |
| coroutines               | 17.9 ms                                                         | 17.8 ms: 1.01x faster                                                          |
| asyncio_tcp_ssl          | 17.0 sec                                                        | 17.1 sec: 1.01x slower                                                         |
| meteor_contest           | 80.0 ms                                                         | 82.0 ms: 1.02x slower                                                          |
| regex_v8                 | 15.8 ms                                                         | 16.4 ms: 1.04x slower                                                          |
| python_startup           | 22.9 ms                                                         | 23.8 ms: 1.04x slower                                                          |
| xml_etree_process        | 48.1 ms                                                         | 50.0 ms: 1.04x slower                                                          |
| richards                 | 40.3 ms                                                         | 41.9 ms: 1.04x slower                                                          |
| genshi_text              | 21.0 ms                                                         | 21.9 ms: 1.04x slower                                                          |
| pathlib                  | 81.2 ms                                                         | 86.9 ms: 1.07x slower                                                          |
| fannkuch                 | 317 ms                                                          | 342 ms: 1.08x slower                                                           |
| logging_simple           | 7.29 us                                                         | 7.92 us: 1.09x slower                                                          |
| create_gc_cycles         | 694 us                                                          | 754 us: 1.09x slower                                                           |
| xml_etree_generate       | 61.6 ms                                                         | 67.3 ms: 1.09x slower                                                          |
| python_startup_no_site   | 18.1 ms                                                         | 19.7 ms: 1.09x slower                                                          |
| logging_format           | 7.91 us                                                         | 8.65 us: 1.09x slower                                                          |
| scimark_fft              | 216 ms                                                          | 237 ms: 1.09x slower                                                           |
| bench_mp_pool            | 66.4 ms                                                         | 73.2 ms: 1.10x slower                                                          |
| coverage                 | 46.6 ms                                                         | 51.8 ms: 1.11x slower                                                          |
| gc_traversal             | 1.28 ms                                                         | 1.44 ms: 1.12x slower                                                          |
| regex_effbot             | 1.66 ms                                                         | 1.93 ms: 1.16x slower                                                          |
| nbody                    | 79.1 ms                                                         | 96.0 ms: 1.21x slower                                                          |
| async_generators         | 241 ms                                                          | 297 ms: 1.23x slower                                                           |
| telco                    | 4.83 ms                                                         | 6.77 ms: 1.40x slower                                                          |
| Geometric mean           | (ref)                                                           | 1.12x faster                                                                   |
Ignored benchmarks (14) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (4) of results/bm-20240903-3.14.0a0-6d5be6d/bm-20240903-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-6d5be6d.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: unknown
# Results vs. 3.10.4

- fork: python
- ref: 7aca84e557d0a6d242f3
- machine: windows-x86
- commit hash: 7aca84e
- commit date: 2024-08-02
- overall geometric mean: 1.09x faster
- HPT reliability: 98.45%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240802-pythonperf1_win32-x86-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| docutils       | 1.95 sec                                                        | 1.96 sec: 1.01x slower                                                         |
| html5lib       | 52.1 ms                                                         | 51.4 ms: 1.01x faster                                                          |
| tornado_http   | 118 ms                                                          | 107 ms: 1.10x faster                                                           |
| Geometric mean | (ref)                                                           | 1.03x faster                                                                   |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240802-pythonperf1_win32-x86-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|-------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 922 ms                                                          | 484 ms: 1.90x faster                                                           |
| async_tree_none         | 394 ms                                                          | 232 ms: 1.70x faster                                                           |
| async_tree_io           | 940 ms                                                          | 570 ms: 1.65x faster                                                           |
| async_tree_memoization  | 467 ms                                                          | 287 ms: 1.62x faster                                                           |
| Geometric mean          | (ref)                                                           | 1.71x faster                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240802-pythonperf1_win32-x86-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 200 ms: 2.52x faster                                                           |
| float          | 69.6 ms                                                         | 61.5 ms: 1.13x faster                                                          |
| nbody          | 79.1 ms                                                         | 102 ms: 1.28x slower                                                           |
| Geometric mean | (ref)                                                           | 1.30x faster                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240802-pythonperf1_win32-x86-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_compile  | 117 ms                                                          | 111 ms: 1.05x faster                                                           |
| regex_dna      | 131 ms                                                          | 129 ms: 1.01x faster                                                           |
| regex_v8       | 15.8 ms                                                         | 16.4 ms: 1.04x slower                                                          |
| regex_effbot   | 1.66 ms                                                         | 2.05 ms: 1.23x slower                                                          |
| Geometric mean | (ref)                                                           | 1.05x slower                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240802-pythonperf1_win32-x86-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| json_dumps           | 9.82 ms                                                         | 7.71 ms: 1.27x faster                                                          |
| xml_etree_parse      | 120 ms                                                          | 105 ms: 1.14x faster                                                           |
| unpickle_pure_python | 189 us                                                          | 174 us: 1.09x faster                                                           |
| json_loads           | 22.4 us                                                         | 20.8 us: 1.08x faster                                                          |
| pickle_pure_python   | 280 us                                                          | 266 us: 1.05x faster                                                           |
| xml_etree_iterparse  | 70.8 ms                                                         | 67.7 ms: 1.05x faster                                                          |
| xml_etree_process    | 48.1 ms                                                         | 49.1 ms: 1.02x slower                                                          |
| xml_etree_generate   | 61.6 ms                                                         | 65.8 ms: 1.07x slower                                                          |
| Geometric mean       | (ref)                                                           | 1.06x faster                                                                   |

Benchmark hidden because not significant (1): tomli_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240802-pythonperf1_win32-x86-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup         | 22.9 ms                                                         | 23.7 ms: 1.03x slower                                                          |
| python_startup_no_site | 18.1 ms                                                         | 19.6 ms: 1.09x slower                                                          |
| Geometric mean         | (ref)                                                           | 1.06x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240802-pythonperf1_win32-x86-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|-----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako            | 9.10 ms                                                         | 8.31 ms: 1.10x faster                                                          |
| django_template | 36.0 ms                                                         | 34.9 ms: 1.03x faster                                                          |
| genshi_xml      | 46.6 ms                                                         | 50.4 ms: 1.08x slower                                                          |
| genshi_text     | 21.0 ms                                                         | 24.4 ms: 1.16x slower                                                          |
| Geometric mean  | (ref)                                                           | 1.03x slower                                                                   |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240802-pythonperf1_win32-x86-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|--------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| typing_runtime_protocols | 396 us                                                          | 152 us: 2.60x faster                                                           |
| pidigits                 | 502 ms                                                          | 200 ms: 2.52x faster                                                           |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 484 ms: 1.90x faster                                                           |
| async_tree_none          | 394 ms                                                          | 232 ms: 1.70x faster                                                           |
| async_tree_io            | 940 ms                                                          | 570 ms: 1.65x faster                                                           |
| async_tree_memoization   | 467 ms                                                          | 287 ms: 1.62x faster                                                           |
| pylint                   | 384 ms                                                          | 239 ms: 1.60x faster                                                           |
| deltablue                | 4.04 ms                                                         | 2.84 ms: 1.42x faster                                                          |
| chaos                    | 74.4 ms                                                         | 54.7 ms: 1.36x faster                                                          |
| crypto_pyaes             | 81.3 ms                                                         | 59.8 ms: 1.36x faster                                                          |
| logging_silent           | 97.9 ns                                                         | 75.3 ns: 1.30x faster                                                          |
| deepcopy_memo            | 29.6 us                                                         | 23.0 us: 1.28x faster                                                          |
| json_dumps               | 9.82 ms                                                         | 7.71 ms: 1.27x faster                                                          |
| comprehensions           | 17.7 us                                                         | 14.1 us: 1.26x faster                                                          |
| raytrace                 | 303 ms                                                          | 241 ms: 1.25x faster                                                           |
| scimark_lu               | 89.8 ms                                                         | 72.4 ms: 1.24x faster                                                          |
| thrift                   | 902 us                                                          | 751 us: 1.20x faster                                                           |
| sqlglot_parse            | 1.33 ms                                                         | 1.12 ms: 1.18x faster                                                          |
| go                       | 146 ms                                                          | 124 ms: 1.17x faster                                                           |
| deepcopy                 | 310 us                                                          | 264 us: 1.17x faster                                                           |
| pyflate                  | 422 ms                                                          | 360 ms: 1.17x faster                                                           |
| sqlglot_transpile        | 1.58 ms                                                         | 1.38 ms: 1.14x faster                                                          |
| scimark_sor              | 115 ms                                                          | 101 ms: 1.14x faster                                                           |
| xml_etree_parse          | 120 ms                                                          | 105 ms: 1.14x faster                                                           |
| hexiom                   | 6.13 ms                                                         | 5.40 ms: 1.14x faster                                                          |
| pycparser                | 1.04 sec                                                        | 918 ms: 1.14x faster                                                           |
| dulwich_log              | 58.5 ms                                                         | 51.6 ms: 1.13x faster                                                          |
| float                    | 69.6 ms                                                         | 61.5 ms: 1.13x faster                                                          |
| generators               | 31.6 ms                                                         | 27.9 ms: 1.13x faster                                                          |
| bench_thread_pool        | 1.12 ms                                                         | 1.01 ms: 1.11x faster                                                          |
| nqueens                  | 87.1 ms                                                         | 79.0 ms: 1.10x faster                                                          |
| tornado_http             | 118 ms                                                          | 107 ms: 1.10x faster                                                           |
| json                     | 4.76 ms                                                         | 4.34 ms: 1.10x faster                                                          |
| mako                     | 9.10 ms                                                         | 8.31 ms: 1.10x faster                                                          |
| unpickle_pure_python     | 189 us                                                          | 174 us: 1.09x faster                                                           |
| sympy_sum                | 122 ms                                                          | 112 ms: 1.09x faster                                                           |
| json_loads               | 22.4 us                                                         | 20.8 us: 1.08x faster                                                          |
| scimark_monte_carlo      | 61.9 ms                                                         | 58.2 ms: 1.06x faster                                                          |
| pickle_pure_python       | 280 us                                                          | 266 us: 1.05x faster                                                           |
| richards_super           | 49.9 ms                                                         | 47.4 ms: 1.05x faster                                                          |
| regex_compile            | 117 ms                                                          | 111 ms: 1.05x faster                                                           |
| xml_etree_iterparse      | 70.8 ms                                                         | 67.7 ms: 1.05x faster                                                          |
| mdp                      | 1.83 sec                                                        | 1.76 sec: 1.04x faster                                                         |
| sympy_integrate          | 16.6 ms                                                         | 16.1 ms: 1.03x faster                                                          |
| django_template          | 36.0 ms                                                         | 34.9 ms: 1.03x faster                                                          |
| spectral_norm            | 80.2 ms                                                         | 78.0 ms: 1.03x faster                                                          |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 3.17 ms: 1.02x faster                                                          |
| sympy_str                | 229 ms                                                          | 225 ms: 1.02x faster                                                           |
| regex_dna                | 131 ms                                                          | 129 ms: 1.01x faster                                                           |
| coroutines               | 17.9 ms                                                         | 17.7 ms: 1.01x faster                                                          |
| html5lib                 | 52.1 ms                                                         | 51.4 ms: 1.01x faster                                                          |
| deepcopy_reduce          | 2.68 us                                                         | 2.66 us: 1.01x faster                                                          |
| sqlglot_normalize        | 230 ms                                                          | 229 ms: 1.01x faster                                                           |
| sympy_expand             | 391 ms                                                          | 392 ms: 1.00x slower                                                           |
| docutils                 | 1.95 sec                                                        | 1.96 sec: 1.01x slower                                                         |
| asyncio_tcp_ssl          | 17.0 sec                                                        | 17.2 sec: 1.01x slower                                                         |
| pprint_pformat           | 1.37 sec                                                        | 1.39 sec: 1.02x slower                                                         |
| xml_etree_process        | 48.1 ms                                                         | 49.1 ms: 1.02x slower                                                          |
| fannkuch                 | 317 ms                                                          | 325 ms: 1.03x slower                                                           |
| python_startup           | 22.9 ms                                                         | 23.7 ms: 1.03x slower                                                          |
| pprint_safe_repr         | 658 ms                                                          | 685 ms: 1.04x slower                                                           |
| regex_v8                 | 15.8 ms                                                         | 16.4 ms: 1.04x slower                                                          |
| meteor_contest           | 80.0 ms                                                         | 83.9 ms: 1.05x slower                                                          |
| asyncio_tcp              | 744 ms                                                          | 785 ms: 1.06x slower                                                           |
| xml_etree_generate       | 61.6 ms                                                         | 65.8 ms: 1.07x slower                                                          |
| genshi_xml               | 46.6 ms                                                         | 50.4 ms: 1.08x slower                                                          |
| create_gc_cycles         | 694 us                                                          | 753 us: 1.09x slower                                                           |
| richards                 | 40.3 ms                                                         | 43.7 ms: 1.09x slower                                                          |
| scimark_fft              | 216 ms                                                          | 235 ms: 1.09x slower                                                           |
| python_startup_no_site   | 18.1 ms                                                         | 19.6 ms: 1.09x slower                                                          |
| pathlib                  | 81.2 ms                                                         | 89.3 ms: 1.10x slower                                                          |
| bench_mp_pool            | 66.4 ms                                                         | 74.2 ms: 1.12x slower                                                          |
| coverage                 | 46.6 ms                                                         | 52.2 ms: 1.12x slower                                                          |
| gc_traversal             | 1.28 ms                                                         | 1.44 ms: 1.13x slower                                                          |
| logging_simple           | 7.29 us                                                         | 8.27 us: 1.13x slower                                                          |
| logging_format           | 7.91 us                                                         | 8.98 us: 1.14x slower                                                          |
| genshi_text              | 21.0 ms                                                         | 24.4 ms: 1.16x slower                                                          |
| regex_effbot             | 1.66 ms                                                         | 2.05 ms: 1.23x slower                                                          |
| async_generators         | 241 ms                                                          | 306 ms: 1.27x slower                                                           |
| nbody                    | 79.1 ms                                                         | 102 ms: 1.28x slower                                                           |
| telco                    | 4.83 ms                                                         | 6.60 ms: 1.37x slower                                                          |
| Geometric mean           | (ref)                                                           | 1.09x faster                                                                   |

Benchmark hidden because not significant (3): 2to3, sqlglot_optimize, tomli_loads
Ignored benchmarks (14) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (4) of results/bm-20240802-3.14.0a0-7aca84e/bm-20240802-pythonperf1_win32-x86-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 98.45% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown
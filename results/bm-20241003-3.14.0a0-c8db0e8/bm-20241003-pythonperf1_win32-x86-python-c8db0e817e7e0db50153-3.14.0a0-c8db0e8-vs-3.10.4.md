# Results vs. 3.10.4

- fork: python
- ref: c8db0e817e7e0db50153
- machine: windows-x86
- commit hash: c8db0e8
- commit date: 2024-10-03
- overall geometric mean: 1.10x faster
- HPT reliability: 99.97%
- HPT 99th percentile: 1.02x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241003-pythonperf1_win32-x86-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 250 ms: 1.06x faster                                                           |
| docutils       | 1.95 sec                                                        | 1.87 sec: 1.04x faster                                                         |
| html5lib       | 52.1 ms                                                         | 46.2 ms: 1.13x faster                                                          |
| tornado_http   | 118 ms                                                          | 105 ms: 1.12x faster                                                           |
| Geometric mean | (ref)                                                           | 1.09x faster                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241003-pythonperf1_win32-x86-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 |
|-------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 922 ms                                                          | 491 ms: 1.88x faster                                                           |
| async_tree_none         | 394 ms                                                          | 220 ms: 1.79x faster                                                           |
| async_tree_io           | 940 ms                                                          | 545 ms: 1.73x faster                                                           |
| async_tree_memoization  | 467 ms                                                          | 276 ms: 1.69x faster                                                           |
| Geometric mean          | (ref)                                                           | 1.77x faster                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241003-pythonperf1_win32-x86-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 200 ms: 2.52x faster                                                           |
| float          | 69.6 ms                                                         | 61.7 ms: 1.13x faster                                                          |
| nbody          | 79.1 ms                                                         | 91.6 ms: 1.16x slower                                                          |
| Geometric mean | (ref)                                                           | 1.35x faster                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241003-pythonperf1_win32-x86-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_dna      | 131 ms                                                          | 120 ms: 1.08x faster                                                           |
| regex_compile  | 117 ms                                                          | 110 ms: 1.06x faster                                                           |
| regex_v8       | 15.8 ms                                                         | 16.2 ms: 1.03x slower                                                          |
| regex_effbot   | 1.66 ms                                                         | 1.92 ms: 1.15x slower                                                          |
| Geometric mean | (ref)                                                           | 1.01x slower                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241003-pythonperf1_win32-x86-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 |
|----------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| json_dumps           | 9.82 ms                                                         | 7.54 ms: 1.30x faster                                                          |
| xml_etree_parse      | 120 ms                                                          | 108 ms: 1.11x faster                                                           |
| json_loads           | 22.4 us                                                         | 21.3 us: 1.05x faster                                                          |
| pickle_pure_python   | 280 us                                                          | 268 us: 1.05x faster                                                           |
| xml_etree_iterparse  | 70.8 ms                                                         | 68.0 ms: 1.04x faster                                                          |
| unpickle_pure_python | 189 us                                                          | 183 us: 1.03x faster                                                           |
| tomli_loads          | 1.91 sec                                                        | 1.92 sec: 1.00x slower                                                         |
| unpickle_list        | 2.98 us                                                         | 3.00 us: 1.01x slower                                                          |
| pickle               | 7.83 us                                                         | 8.18 us: 1.04x slower                                                          |
| xml_etree_process    | 48.1 ms                                                         | 50.7 ms: 1.05x slower                                                          |
| pickle_list          | 3.22 us                                                         | 3.41 us: 1.06x slower                                                          |
| unpickle             | 9.82 us                                                         | 10.4 us: 1.06x slower                                                          |
| xml_etree_generate   | 61.6 ms                                                         | 69.1 ms: 1.12x slower                                                          |
| pickle_dict          | 18.2 us                                                         | 20.7 us: 1.13x slower                                                          |
| Geometric mean       | (ref)                                                           | 1.01x faster                                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241003-pythonperf1_win32-x86-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 |
|------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup         | 22.9 ms                                                         | 24.1 ms: 1.05x slower                                                          |
| python_startup_no_site | 18.1 ms                                                         | 19.7 ms: 1.09x slower                                                          |
| Geometric mean         | (ref)                                                           | 1.07x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241003-pythonperf1_win32-x86-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 |
|-----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako            | 9.10 ms                                                         | 8.12 ms: 1.12x faster                                                          |
| django_template | 36.0 ms                                                         | 34.3 ms: 1.05x faster                                                          |
| genshi_xml      | 46.6 ms                                                         | 48.7 ms: 1.05x slower                                                          |
| genshi_text     | 21.0 ms                                                         | 22.6 ms: 1.08x slower                                                          |
| Geometric mean  | (ref)                                                           | 1.01x faster                                                                   |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241003-pythonperf1_win32-x86-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 |
|--------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| typing_runtime_protocols | 396 us                                                          | 148 us: 2.68x faster                                                           |
| pidigits                 | 502 ms                                                          | 200 ms: 2.52x faster                                                           |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 491 ms: 1.88x faster                                                           |
| async_tree_none          | 394 ms                                                          | 220 ms: 1.79x faster                                                           |
| async_tree_io            | 940 ms                                                          | 545 ms: 1.73x faster                                                           |
| async_tree_memoization   | 467 ms                                                          | 276 ms: 1.69x faster                                                           |
| pylint                   | 384 ms                                                          | 236 ms: 1.63x faster                                                           |
| deltablue                | 4.04 ms                                                         | 2.82 ms: 1.43x faster                                                          |
| crypto_pyaes             | 81.3 ms                                                         | 57.8 ms: 1.41x faster                                                          |
| go                       | 146 ms                                                          | 110 ms: 1.33x faster                                                           |
| chaos                    | 74.4 ms                                                         | 56.2 ms: 1.32x faster                                                          |
| logging_silent           | 97.9 ns                                                         | 74.7 ns: 1.31x faster                                                          |
| json_dumps               | 9.82 ms                                                         | 7.54 ms: 1.30x faster                                                          |
| scimark_lu               | 89.8 ms                                                         | 69.2 ms: 1.30x faster                                                          |
| deepcopy_memo            | 29.6 us                                                         | 22.9 us: 1.29x faster                                                          |
| comprehensions           | 17.7 us                                                         | 14.0 us: 1.27x faster                                                          |
| deepcopy                 | 310 us                                                          | 247 us: 1.25x faster                                                           |
| sqlglot_parse            | 1.33 ms                                                         | 1.07 ms: 1.24x faster                                                          |
| pycparser                | 1.04 sec                                                        | 861 ms: 1.21x faster                                                           |
| sqlglot_transpile        | 1.58 ms                                                         | 1.32 ms: 1.20x faster                                                          |
| generators               | 31.6 ms                                                         | 26.7 ms: 1.18x faster                                                          |
| thrift                   | 902 us                                                          | 769 us: 1.17x faster                                                           |
| hexiom                   | 6.13 ms                                                         | 5.23 ms: 1.17x faster                                                          |
| scimark_sor              | 115 ms                                                          | 99.0 ms: 1.16x faster                                                          |
| raytrace                 | 303 ms                                                          | 260 ms: 1.16x faster                                                           |
| nqueens                  | 87.1 ms                                                         | 75.1 ms: 1.16x faster                                                          |
| sqlite_synth             | 2.29 us                                                         | 1.98 us: 1.16x faster                                                          |
| pyflate                  | 422 ms                                                          | 370 ms: 1.14x faster                                                           |
| sympy_sum                | 122 ms                                                          | 108 ms: 1.13x faster                                                           |
| float                    | 69.6 ms                                                         | 61.7 ms: 1.13x faster                                                          |
| html5lib                 | 52.1 ms                                                         | 46.2 ms: 1.13x faster                                                          |
| mako                     | 9.10 ms                                                         | 8.12 ms: 1.12x faster                                                          |
| tornado_http             | 118 ms                                                          | 105 ms: 1.12x faster                                                           |
| scimark_monte_carlo      | 61.9 ms                                                         | 55.3 ms: 1.12x faster                                                          |
| dulwich_log              | 58.5 ms                                                         | 52.5 ms: 1.12x faster                                                          |
| xml_etree_parse          | 120 ms                                                          | 108 ms: 1.11x faster                                                           |
| asyncio_tcp              | 744 ms                                                          | 669 ms: 1.11x faster                                                           |
| json                     | 4.76 ms                                                         | 4.28 ms: 1.11x faster                                                          |
| bench_thread_pool        | 1.12 ms                                                         | 1.01 ms: 1.10x faster                                                          |
| regex_dna                | 131 ms                                                          | 120 ms: 1.08x faster                                                           |
| richards_super           | 49.9 ms                                                         | 46.2 ms: 1.08x faster                                                          |
| sympy_integrate          | 16.6 ms                                                         | 15.7 ms: 1.06x faster                                                          |
| 2to3                     | 265 ms                                                          | 250 ms: 1.06x faster                                                           |
| regex_compile            | 117 ms                                                          | 110 ms: 1.06x faster                                                           |
| json_loads               | 22.4 us                                                         | 21.3 us: 1.05x faster                                                          |
| sympy_str                | 229 ms                                                          | 218 ms: 1.05x faster                                                           |
| django_template          | 36.0 ms                                                         | 34.3 ms: 1.05x faster                                                          |
| pickle_pure_python       | 280 us                                                          | 268 us: 1.05x faster                                                           |
| xml_etree_iterparse      | 70.8 ms                                                         | 68.0 ms: 1.04x faster                                                          |
| docutils                 | 1.95 sec                                                        | 1.87 sec: 1.04x faster                                                         |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 3.11 ms: 1.04x faster                                                          |
| deepcopy_reduce          | 2.68 us                                                         | 2.58 us: 1.04x faster                                                          |
| unpickle_pure_python     | 189 us                                                          | 183 us: 1.03x faster                                                           |
| mdp                      | 1.83 sec                                                        | 1.77 sec: 1.03x faster                                                         |
| spectral_norm            | 80.2 ms                                                         | 78.5 ms: 1.02x faster                                                          |
| sympy_expand             | 391 ms                                                          | 385 ms: 1.01x faster                                                           |
| fannkuch                 | 317 ms                                                          | 313 ms: 1.01x faster                                                           |
| tomli_loads              | 1.91 sec                                                        | 1.92 sec: 1.00x slower                                                         |
| asyncio_tcp_ssl          | 17.0 sec                                                        | 17.1 sec: 1.01x slower                                                         |
| unpickle_list            | 2.98 us                                                         | 3.00 us: 1.01x slower                                                          |
| sqlglot_optimize         | 44.7 ms                                                         | 45.5 ms: 1.02x slower                                                          |
| pprint_pformat           | 1.37 sec                                                        | 1.40 sec: 1.02x slower                                                         |
| sqlglot_normalize        | 230 ms                                                          | 236 ms: 1.03x slower                                                           |
| richards                 | 40.3 ms                                                         | 41.4 ms: 1.03x slower                                                          |
| regex_v8                 | 15.8 ms                                                         | 16.2 ms: 1.03x slower                                                          |
| pprint_safe_repr         | 658 ms                                                          | 680 ms: 1.03x slower                                                           |
| coroutines               | 17.9 ms                                                         | 18.5 ms: 1.03x slower                                                          |
| pickle                   | 7.83 us                                                         | 8.18 us: 1.04x slower                                                          |
| genshi_xml               | 46.6 ms                                                         | 48.7 ms: 1.05x slower                                                          |
| python_startup           | 22.9 ms                                                         | 24.1 ms: 1.05x slower                                                          |
| xml_etree_process        | 48.1 ms                                                         | 50.7 ms: 1.05x slower                                                          |
| create_gc_cycles         | 694 us                                                          | 732 us: 1.05x slower                                                           |
| pickle_list              | 3.22 us                                                         | 3.41 us: 1.06x slower                                                          |
| unpickle                 | 9.82 us                                                         | 10.4 us: 1.06x slower                                                          |
| pathlib                  | 81.2 ms                                                         | 86.5 ms: 1.07x slower                                                          |
| scimark_fft              | 216 ms                                                          | 233 ms: 1.08x slower                                                           |
| genshi_text              | 21.0 ms                                                         | 22.6 ms: 1.08x slower                                                          |
| python_startup_no_site   | 18.1 ms                                                         | 19.7 ms: 1.09x slower                                                          |
| bench_mp_pool            | 66.4 ms                                                         | 72.9 ms: 1.10x slower                                                          |
| gc_traversal             | 1.28 ms                                                         | 1.43 ms: 1.11x slower                                                          |
| logging_simple           | 7.29 us                                                         | 8.18 us: 1.12x slower                                                          |
| xml_etree_generate       | 61.6 ms                                                         | 69.1 ms: 1.12x slower                                                          |
| logging_format           | 7.91 us                                                         | 8.92 us: 1.13x slower                                                          |
| pickle_dict              | 18.2 us                                                         | 20.7 us: 1.13x slower                                                          |
| coverage                 | 46.6 ms                                                         | 53.6 ms: 1.15x slower                                                          |
| regex_effbot             | 1.66 ms                                                         | 1.92 ms: 1.15x slower                                                          |
| nbody                    | 79.1 ms                                                         | 91.6 ms: 1.16x slower                                                          |
| unpack_sequence          | 40.0 ns                                                         | 46.7 ns: 1.17x slower                                                          |
| async_generators         | 241 ms                                                          | 302 ms: 1.25x slower                                                           |
| telco                    | 4.83 ms                                                         | 6.48 ms: 1.34x slower                                                          |
| Geometric mean           | (ref)                                                           | 1.10x faster                                                                   |

Benchmark hidden because not significant (1): meteor_contest
Ignored benchmarks (7) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (4) of results/bm-20241003-3.14.0a0-c8db0e8/bm-20241003-pythonperf1_win32-x86-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 99.97% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: unknown
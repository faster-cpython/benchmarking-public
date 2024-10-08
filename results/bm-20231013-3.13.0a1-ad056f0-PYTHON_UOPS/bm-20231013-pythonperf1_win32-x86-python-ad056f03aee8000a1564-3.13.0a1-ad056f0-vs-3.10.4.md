
# Results vs. 3.10.4

- fork: python
- ref: ad056f03aee8000a1564
- machine: windows-x86
- commit hash: ad056f0
- commit date: 2023-10-13
- overall geometric mean: 1.19x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.10x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20231013-pythonperf1_win32-x86-python-ad056f03aee8000a1564-3.13.0a1-ad056f0 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 309 ms: 1.16x slower                                                           |
| chameleon      | 6.42 ms                                                         | 9.20 ms: 1.43x slower                                                          |
| docutils       | 1.95 sec                                                        | 2.17 sec: 1.11x slower                                                         |
| tornado_http   | 118 ms                                                          | 116 ms: 1.01x faster                                                           |
| Geometric mean | (ref)                                                           | 1.16x slower                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20231013-pythonperf1_win32-x86-python-ad056f03aee8000a1564-3.13.0a1-ad056f0 |
|-------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 922 ms                                                          | 579 ms: 1.59x faster                                                           |
| async_tree_io           | 940 ms                                                          | 757 ms: 1.24x faster                                                           |
| async_tree_none         | 394 ms                                                          | 317 ms: 1.24x faster                                                           |
| async_tree_memoization  | 467 ms                                                          | 396 ms: 1.18x faster                                                           |
| Geometric mean          | (ref)                                                           | 1.30x faster                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20231013-pythonperf1_win32-x86-python-ad056f03aee8000a1564-3.13.0a1-ad056f0 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 198 ms: 2.54x faster                                                           |
| float          | 69.6 ms                                                         | 92.7 ms: 1.33x slower                                                          |
| nbody          | 79.1 ms                                                         | 167 ms: 2.11x slower                                                           |
| Geometric mean | (ref)                                                           | 1.04x slower                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20231013-pythonperf1_win32-x86-python-ad056f03aee8000a1564-3.13.0a1-ad056f0 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_dna      | 131 ms                                                          | 119 ms: 1.10x faster                                                           |
| regex_v8       | 15.8 ms                                                         | 16.8 ms: 1.07x slower                                                          |
| regex_effbot   | 1.66 ms                                                         | 1.93 ms: 1.16x slower                                                          |
| regex_compile  | 117 ms                                                          | 159 ms: 1.37x slower                                                           |
| Geometric mean | (ref)                                                           | 1.11x slower                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20231013-pythonperf1_win32-x86-python-ad056f03aee8000a1564-3.13.0a1-ad056f0 |
|----------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| json_dumps           | 9.82 ms                                                         | 8.05 ms: 1.22x faster                                                          |
| json_loads           | 22.4 us                                                         | 20.4 us: 1.10x faster                                                          |
| xml_etree_parse      | 120 ms                                                          | 114 ms: 1.05x faster                                                           |
| unpickle             | 9.82 us                                                         | 9.47 us: 1.04x faster                                                          |
| pickle               | 7.83 us                                                         | 7.73 us: 1.01x faster                                                          |
| pickle_list          | 3.22 us                                                         | 3.28 us: 1.02x slower                                                          |
| pickle_dict          | 18.2 us                                                         | 19.9 us: 1.09x slower                                                          |
| xml_etree_iterparse  | 70.8 ms                                                         | 86.1 ms: 1.22x slower                                                          |
| pickle_pure_python   | 280 us                                                          | 348 us: 1.24x slower                                                           |
| xml_etree_process    | 48.1 ms                                                         | 64.0 ms: 1.33x slower                                                          |
| xml_etree_generate   | 61.6 ms                                                         | 84.7 ms: 1.37x slower                                                          |
| tomli_loads          | 1.91 sec                                                        | 2.79 sec: 1.46x slower                                                         |
| unpickle_pure_python | 189 us                                                          | 279 us: 1.47x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.11x slower                                                                   |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20231013-pythonperf1_win32-x86-python-ad056f03aee8000a1564-3.13.0a1-ad056f0 |
|------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup         | 22.9 ms                                                         | 22.3 ms: 1.03x faster                                                          |
| python_startup_no_site | 18.1 ms                                                         | 19.6 ms: 1.09x slower                                                          |
| Geometric mean         | (ref)                                                           | 1.03x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20231013-pythonperf1_win32-x86-python-ad056f03aee8000a1564-3.13.0a1-ad056f0 |
|-----------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako      | 9.10 ms                                                         | 12.4 ms: 1.36x slower                                                          |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20231013-pythonperf1_win32-x86-python-ad056f03aee8000a1564-3.13.0a1-ad056f0 |
|--------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| typing_runtime_protocols | 396 us                                                          | 143 us: 2.78x faster                                                           |
| pidigits                 | 502 ms                                                          | 198 ms: 2.54x faster                                                           |
| sqlglot_normalize        | 230 ms                                                          | 118 ms: 1.95x faster                                                           |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 579 ms: 1.59x faster                                                           |
| async_tree_io            | 940 ms                                                          | 757 ms: 1.24x faster                                                           |
| async_tree_none          | 394 ms                                                          | 317 ms: 1.24x faster                                                           |
| json_dumps               | 9.82 ms                                                         | 8.05 ms: 1.22x faster                                                          |
| async_tree_memoization   | 467 ms                                                          | 396 ms: 1.18x faster                                                           |
| asyncio_tcp              | 744 ms                                                          | 674 ms: 1.10x faster                                                           |
| regex_dna                | 131 ms                                                          | 119 ms: 1.10x faster                                                           |
| json_loads               | 22.4 us                                                         | 20.4 us: 1.10x faster                                                          |
| json                     | 4.76 ms                                                         | 4.41 ms: 1.08x faster                                                          |
| sqlite_synth             | 2.29 us                                                         | 2.12 us: 1.08x faster                                                          |
| create_gc_cycles         | 694 us                                                          | 645 us: 1.08x faster                                                           |
| crypto_pyaes             | 81.3 ms                                                         | 76.0 ms: 1.07x faster                                                          |
| xml_etree_parse          | 120 ms                                                          | 114 ms: 1.05x faster                                                           |
| unpickle                 | 9.82 us                                                         | 9.47 us: 1.04x faster                                                          |
| python_startup           | 22.9 ms                                                         | 22.3 ms: 1.03x faster                                                          |
| tornado_http             | 118 ms                                                          | 116 ms: 1.01x faster                                                           |
| pickle                   | 7.83 us                                                         | 7.73 us: 1.01x faster                                                          |
| pickle_list              | 3.22 us                                                         | 3.28 us: 1.02x slower                                                          |
| asyncio_tcp_ssl          | 17.0 sec                                                        | 17.5 sec: 1.03x slower                                                         |
| bench_thread_pool        | 1.12 ms                                                         | 1.18 ms: 1.05x slower                                                          |
| regex_v8                 | 15.8 ms                                                         | 16.8 ms: 1.07x slower                                                          |
| chaos                    | 74.4 ms                                                         | 80.1 ms: 1.08x slower                                                          |
| gc_traversal             | 1.28 ms                                                         | 1.39 ms: 1.08x slower                                                          |
| pycparser                | 1.04 sec                                                        | 1.13 sec: 1.08x slower                                                         |
| python_startup_no_site   | 18.1 ms                                                         | 19.6 ms: 1.09x slower                                                          |
| pickle_dict              | 18.2 us                                                         | 19.9 us: 1.09x slower                                                          |
| raytrace                 | 303 ms                                                          | 331 ms: 1.09x slower                                                           |
| deltablue                | 4.04 ms                                                         | 4.47 ms: 1.11x slower                                                          |
| bench_mp_pool            | 66.4 ms                                                         | 73.9 ms: 1.11x slower                                                          |
| docutils                 | 1.95 sec                                                        | 2.17 sec: 1.11x slower                                                         |
| pathlib                  | 81.2 ms                                                         | 90.9 ms: 1.12x slower                                                          |
| mdp                      | 1.83 sec                                                        | 2.06 sec: 1.13x slower                                                         |
| sympy_sum                | 122 ms                                                          | 139 ms: 1.13x slower                                                           |
| sqlglot_parse            | 1.33 ms                                                         | 1.52 ms: 1.15x slower                                                          |
| sqlglot_transpile        | 1.58 ms                                                         | 1.82 ms: 1.15x slower                                                          |
| regex_effbot             | 1.66 ms                                                         | 1.93 ms: 1.16x slower                                                          |
| 2to3                     | 265 ms                                                          | 309 ms: 1.16x slower                                                           |
| sympy_expand             | 391 ms                                                          | 457 ms: 1.17x slower                                                           |
| go                       | 146 ms                                                          | 175 ms: 1.20x slower                                                           |
| sympy_str                | 229 ms                                                          | 276 ms: 1.21x slower                                                           |
| sympy_integrate          | 16.6 ms                                                         | 20.1 ms: 1.21x slower                                                          |
| meteor_contest           | 80.0 ms                                                         | 96.7 ms: 1.21x slower                                                          |
| xml_etree_iterparse      | 70.8 ms                                                         | 86.1 ms: 1.22x slower                                                          |
| pickle_pure_python       | 280 us                                                          | 348 us: 1.24x slower                                                           |
| nqueens                  | 87.1 ms                                                         | 109 ms: 1.25x slower                                                           |
| sqlglot_optimize         | 44.7 ms                                                         | 55.9 ms: 1.25x slower                                                          |
| pyflate                  | 422 ms                                                          | 539 ms: 1.28x slower                                                           |
| richards_super           | 49.9 ms                                                         | 64.1 ms: 1.28x slower                                                          |
| comprehensions           | 17.7 us                                                         | 23.3 us: 1.31x slower                                                          |
| xml_etree_process        | 48.1 ms                                                         | 64.0 ms: 1.33x slower                                                          |
| float                    | 69.6 ms                                                         | 92.7 ms: 1.33x slower                                                          |
| scimark_monte_carlo      | 61.9 ms                                                         | 83.1 ms: 1.34x slower                                                          |
| pprint_pformat           | 1.37 sec                                                        | 1.85 sec: 1.35x slower                                                         |
| deepcopy                 | 310 us                                                          | 420 us: 1.36x slower                                                           |
| mako                     | 9.10 ms                                                         | 12.4 ms: 1.36x slower                                                          |
| regex_compile            | 117 ms                                                          | 159 ms: 1.37x slower                                                           |
| pprint_safe_repr         | 658 ms                                                          | 901 ms: 1.37x slower                                                           |
| scimark_lu               | 89.8 ms                                                         | 123 ms: 1.37x slower                                                           |
| xml_etree_generate       | 61.6 ms                                                         | 84.7 ms: 1.37x slower                                                          |
| deepcopy_reduce          | 2.68 us                                                         | 3.73 us: 1.39x slower                                                          |
| logging_silent           | 97.9 ns                                                         | 138 ns: 1.41x slower                                                           |
| telco                    | 4.83 ms                                                         | 6.92 ms: 1.43x slower                                                          |
| chameleon                | 6.42 ms                                                         | 9.20 ms: 1.43x slower                                                          |
| hexiom                   | 6.13 ms                                                         | 8.81 ms: 1.44x slower                                                          |
| scimark_sor              | 115 ms                                                          | 168 ms: 1.46x slower                                                           |
| tomli_loads              | 1.91 sec                                                        | 2.79 sec: 1.46x slower                                                         |
| logging_format           | 7.91 us                                                         | 11.6 us: 1.46x slower                                                          |
| richards                 | 40.3 ms                                                         | 59.1 ms: 1.47x slower                                                          |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 4.77 ms: 1.47x slower                                                          |
| unpickle_pure_python     | 189 us                                                          | 279 us: 1.47x slower                                                           |
| fannkuch                 | 317 ms                                                          | 475 ms: 1.50x slower                                                           |
| logging_simple           | 7.29 us                                                         | 10.9 us: 1.50x slower                                                          |
| async_generators         | 241 ms                                                          | 365 ms: 1.52x slower                                                           |
| scimark_fft              | 216 ms                                                          | 335 ms: 1.55x slower                                                           |
| coroutines               | 17.9 ms                                                         | 28.2 ms: 1.57x slower                                                          |
| generators               | 31.6 ms                                                         | 50.6 ms: 1.61x slower                                                          |
| deepcopy_memo            | 29.6 us                                                         | 49.5 us: 1.67x slower                                                          |
| spectral_norm            | 80.2 ms                                                         | 135 ms: 1.69x slower                                                           |
| unpack_sequence          | 40.0 ns                                                         | 76.1 ns: 1.90x slower                                                          |
| nbody                    | 79.1 ms                                                         | 167 ms: 2.11x slower                                                           |
| coverage                 | 46.6 ms                                                         | 690 ms: 14.81x slower                                                          |
| Geometric mean           | (ref)                                                           | 1.19x slower                                                                   |

Benchmark hidden because not significant (1): unpickle_list
Ignored benchmarks (13) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, dask, django_template, dulwich_log, flaskblogging, genshi_text, genshi_xml, html5lib, mypy2, pylint, sqlalchemy_declarative, sqlalchemy_imperative, thrift
Ignored benchmarks (4) of results/bm-20231013-3.13.0a1-ad056f0-PYTHON_UOPS/bm-20231013-pythonperf1_win32-x86-python-ad056f03aee8000a1564-3.13.0a1-ad056f0.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg


# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.13x
- 95% likely to have a slowdown of 1.12x
- 99% likely to have a slowdown of 1.10x


# Memory

- memory change: unknown
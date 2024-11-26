# Results vs. 3.10.4

- fork: python
- ref: b3aa1b5fe260382788a2
- machine: windows-x86
- commit hash: b3aa1b5
- commit date: 2024-10-11
- overall geometric mean: 1.137x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241011-pythonperf1_win32-x86-python-b3aa1b5fe260382788a2-3.14.0a0-b3aa1b5 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 248 ms: 1.07x faster                                                           |
| docutils       | 1.95 sec                                                        | 1.88 sec: 1.04x faster                                                         |
| html5lib       | 52.1 ms                                                         | 47.3 ms: 1.10x faster                                                          |
| tornado_http   | 118 ms                                                          | 104 ms: 1.13x faster                                                           |
| Geometric mean | (ref)                                                           | 1.09x faster                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241011-pythonperf1_win32-x86-python-b3aa1b5fe260382788a2-3.14.0a0-b3aa1b5 |
|-------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 922 ms                                                          | 471 ms: 1.96x faster                                                           |
| async_tree_none         | 394 ms                                                          | 213 ms: 1.85x faster                                                           |
| async_tree_io           | 940 ms                                                          | 532 ms: 1.77x faster                                                           |
| async_tree_memoization  | 467 ms                                                          | 270 ms: 1.73x faster                                                           |
| Geometric mean          | (ref)                                                           | 1.82x faster                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241011-pythonperf1_win32-x86-python-b3aa1b5fe260382788a2-3.14.0a0-b3aa1b5 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 199 ms: 2.52x faster                                                           |
| float          | 69.6 ms                                                         | 60.9 ms: 1.14x faster                                                          |
| nbody          | 79.1 ms                                                         | 86.7 ms: 1.10x slower                                                          |
| Geometric mean | (ref)                                                           | 1.38x faster                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241011-pythonperf1_win32-x86-python-b3aa1b5fe260382788a2-3.14.0a0-b3aa1b5 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_dna      | 131 ms                                                          | 117 ms: 1.11x faster                                                           |
| regex_compile  | 117 ms                                                          | 107 ms: 1.09x faster                                                           |
| regex_v8       | 15.8 ms                                                         | 15.7 ms: 1.01x faster                                                          |
| regex_effbot   | 1.66 ms                                                         | 1.84 ms: 1.11x slower                                                          |
| Geometric mean | (ref)                                                           | 1.03x faster                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241011-pythonperf1_win32-x86-python-b3aa1b5fe260382788a2-3.14.0a0-b3aa1b5 |
|----------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| json_dumps           | 9.82 ms                                                         | 9.01 ms: 1.09x faster                                                          |
| unpickle_pure_python | 189 us                                                          | 177 us: 1.07x faster                                                           |
| xml_etree_parse      | 120 ms                                                          | 113 ms: 1.07x faster                                                           |
| json_loads           | 22.4 us                                                         | 21.0 us: 1.07x faster                                                          |
| pickle_pure_python   | 280 us                                                          | 265 us: 1.06x faster                                                           |
| unpickle_list        | 2.98 us                                                         | 2.89 us: 1.03x faster                                                          |
| xml_etree_iterparse  | 70.8 ms                                                         | 68.7 ms: 1.03x faster                                                          |
| tomli_loads          | 1.91 sec                                                        | 1.87 sec: 1.02x faster                                                         |
| unpickle             | 9.82 us                                                         | 10.1 us: 1.03x slower                                                          |
| pickle_list          | 3.22 us                                                         | 3.42 us: 1.06x slower                                                          |
| pickle               | 7.83 us                                                         | 8.55 us: 1.09x slower                                                          |
| xml_etree_generate   | 61.6 ms                                                         | 67.7 ms: 1.10x slower                                                          |
| pickle_dict          | 18.2 us                                                         | 21.7 us: 1.19x slower                                                          |
| Geometric mean       | (ref)                                                           | 1.00x slower                                                                   |

Benchmark hidden because not significant (1): xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241011-pythonperf1_win32-x86-python-b3aa1b5fe260382788a2-3.14.0a0-b3aa1b5 |
|------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup         | 22.9 ms                                                         | 24.9 ms: 1.09x slower                                                          |
| python_startup_no_site | 18.1 ms                                                         | 20.7 ms: 1.15x slower                                                          |
| Geometric mean         | (ref)                                                           | 1.12x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241011-pythonperf1_win32-x86-python-b3aa1b5fe260382788a2-3.14.0a0-b3aa1b5 |
|-----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako            | 9.10 ms                                                         | 7.76 ms: 1.17x faster                                                          |
| django_template | 36.0 ms                                                         | 34.8 ms: 1.04x faster                                                          |
| genshi_xml      | 46.6 ms                                                         | 47.0 ms: 1.01x slower                                                          |
| genshi_text     | 21.0 ms                                                         | 21.5 ms: 1.03x slower                                                          |
| Geometric mean  | (ref)                                                           | 1.04x faster                                                                   |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241011-pythonperf1_win32-x86-python-b3aa1b5fe260382788a2-3.14.0a0-b3aa1b5 |
|--------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| typing_runtime_protocols | 396 us                                                          | 139 us: 2.86x faster                                                           |
| pidigits                 | 502 ms                                                          | 199 ms: 2.52x faster                                                           |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 471 ms: 1.96x faster                                                           |
| async_tree_none          | 394 ms                                                          | 213 ms: 1.85x faster                                                           |
| async_tree_io            | 940 ms                                                          | 532 ms: 1.77x faster                                                           |
| async_tree_memoization   | 467 ms                                                          | 270 ms: 1.73x faster                                                           |
| pylint                   | 384 ms                                                          | 232 ms: 1.65x faster                                                           |
| deltablue                | 4.04 ms                                                         | 2.70 ms: 1.50x faster                                                          |
| go                       | 146 ms                                                          | 99.3 ms: 1.47x faster                                                          |
| logging_silent           | 97.9 ns                                                         | 67.4 ns: 1.45x faster                                                          |
| deepcopy_memo            | 29.6 us                                                         | 21.3 us: 1.39x faster                                                          |
| chaos                    | 74.4 ms                                                         | 55.0 ms: 1.35x faster                                                          |
| comprehensions           | 17.7 us                                                         | 13.1 us: 1.35x faster                                                          |
| generators               | 31.6 ms                                                         | 23.5 ms: 1.34x faster                                                          |
| crypto_pyaes             | 81.3 ms                                                         | 61.1 ms: 1.33x faster                                                          |
| scimark_lu               | 89.8 ms                                                         | 68.5 ms: 1.31x faster                                                          |
| deepcopy                 | 310 us                                                          | 245 us: 1.26x faster                                                           |
| sqlglot_parse            | 1.33 ms                                                         | 1.06 ms: 1.26x faster                                                          |
| pycparser                | 1.04 sec                                                        | 836 ms: 1.25x faster                                                           |
| raytrace                 | 303 ms                                                          | 243 ms: 1.25x faster                                                           |
| hexiom                   | 6.13 ms                                                         | 4.96 ms: 1.24x faster                                                          |
| thrift                   | 902 us                                                          | 738 us: 1.22x faster                                                           |
| sqlglot_transpile        | 1.58 ms                                                         | 1.30 ms: 1.22x faster                                                          |
| pyflate                  | 422 ms                                                          | 356 ms: 1.18x faster                                                           |
| mako                     | 9.10 ms                                                         | 7.76 ms: 1.17x faster                                                          |
| nqueens                  | 87.1 ms                                                         | 74.7 ms: 1.17x faster                                                          |
| sqlite_synth             | 2.29 us                                                         | 1.97 us: 1.16x faster                                                          |
| scimark_sor              | 115 ms                                                          | 99.4 ms: 1.16x faster                                                          |
| float                    | 69.6 ms                                                         | 60.9 ms: 1.14x faster                                                          |
| tornado_http             | 118 ms                                                          | 104 ms: 1.13x faster                                                           |
| dulwich_log              | 58.5 ms                                                         | 51.7 ms: 1.13x faster                                                          |
| sympy_sum                | 122 ms                                                          | 108 ms: 1.13x faster                                                           |
| json                     | 4.76 ms                                                         | 4.27 ms: 1.12x faster                                                          |
| regex_dna                | 131 ms                                                          | 117 ms: 1.11x faster                                                           |
| bench_thread_pool        | 1.12 ms                                                         | 1.01 ms: 1.11x faster                                                          |
| scimark_monte_carlo      | 61.9 ms                                                         | 55.9 ms: 1.11x faster                                                          |
| richards_super           | 49.9 ms                                                         | 45.3 ms: 1.10x faster                                                          |
| html5lib                 | 52.1 ms                                                         | 47.3 ms: 1.10x faster                                                          |
| regex_compile            | 117 ms                                                          | 107 ms: 1.09x faster                                                           |
| json_dumps               | 9.82 ms                                                         | 9.01 ms: 1.09x faster                                                          |
| spectral_norm            | 80.2 ms                                                         | 74.0 ms: 1.08x faster                                                          |
| deepcopy_reduce          | 2.68 us                                                         | 2.49 us: 1.08x faster                                                          |
| unpickle_pure_python     | 189 us                                                          | 177 us: 1.07x faster                                                           |
| mdp                      | 1.83 sec                                                        | 1.71 sec: 1.07x faster                                                         |
| 2to3                     | 265 ms                                                          | 248 ms: 1.07x faster                                                           |
| xml_etree_parse          | 120 ms                                                          | 113 ms: 1.07x faster                                                           |
| json_loads               | 22.4 us                                                         | 21.0 us: 1.07x faster                                                          |
| sympy_integrate          | 16.6 ms                                                         | 15.6 ms: 1.07x faster                                                          |
| pickle_pure_python       | 280 us                                                          | 265 us: 1.06x faster                                                           |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 3.09 ms: 1.05x faster                                                          |
| sympy_str                | 229 ms                                                          | 219 ms: 1.05x faster                                                           |
| pprint_pformat           | 1.37 sec                                                        | 1.32 sec: 1.04x faster                                                         |
| docutils                 | 1.95 sec                                                        | 1.88 sec: 1.04x faster                                                         |
| django_template          | 36.0 ms                                                         | 34.8 ms: 1.04x faster                                                          |
| unpickle_list            | 2.98 us                                                         | 2.89 us: 1.03x faster                                                          |
| fannkuch                 | 317 ms                                                          | 308 ms: 1.03x faster                                                           |
| xml_etree_iterparse      | 70.8 ms                                                         | 68.7 ms: 1.03x faster                                                          |
| coroutines               | 17.9 ms                                                         | 17.5 ms: 1.02x faster                                                          |
| tomli_loads              | 1.91 sec                                                        | 1.87 sec: 1.02x faster                                                         |
| pprint_safe_repr         | 658 ms                                                          | 645 ms: 1.02x faster                                                           |
| sqlglot_optimize         | 44.7 ms                                                         | 44.0 ms: 1.02x faster                                                          |
| sympy_expand             | 391 ms                                                          | 386 ms: 1.01x faster                                                           |
| regex_v8                 | 15.8 ms                                                         | 15.7 ms: 1.01x faster                                                          |
| genshi_xml               | 46.6 ms                                                         | 47.0 ms: 1.01x slower                                                          |
| asyncio_tcp_ssl          | 17.0 sec                                                        | 17.4 sec: 1.02x slower                                                         |
| genshi_text              | 21.0 ms                                                         | 21.5 ms: 1.03x slower                                                          |
| unpickle                 | 9.82 us                                                         | 10.1 us: 1.03x slower                                                          |
| scimark_fft              | 216 ms                                                          | 229 ms: 1.06x slower                                                           |
| pickle_list              | 3.22 us                                                         | 3.42 us: 1.06x slower                                                          |
| logging_simple           | 7.29 us                                                         | 7.84 us: 1.08x slower                                                          |
| unpack_sequence          | 40.0 ns                                                         | 43.4 ns: 1.08x slower                                                          |
| logging_format           | 7.91 us                                                         | 8.57 us: 1.08x slower                                                          |
| pathlib                  | 81.2 ms                                                         | 88.1 ms: 1.08x slower                                                          |
| python_startup           | 22.9 ms                                                         | 24.9 ms: 1.09x slower                                                          |
| pickle                   | 7.83 us                                                         | 8.55 us: 1.09x slower                                                          |
| nbody                    | 79.1 ms                                                         | 86.7 ms: 1.10x slower                                                          |
| xml_etree_generate       | 61.6 ms                                                         | 67.7 ms: 1.10x slower                                                          |
| regex_effbot             | 1.66 ms                                                         | 1.84 ms: 1.11x slower                                                          |
| bench_mp_pool            | 66.4 ms                                                         | 74.0 ms: 1.11x slower                                                          |
| create_gc_cycles         | 694 us                                                          | 783 us: 1.13x slower                                                           |
| gc_traversal             | 1.28 ms                                                         | 1.45 ms: 1.13x slower                                                          |
| coverage                 | 46.6 ms                                                         | 52.7 ms: 1.13x slower                                                          |
| python_startup_no_site   | 18.1 ms                                                         | 20.7 ms: 1.15x slower                                                          |
| pickle_dict              | 18.2 us                                                         | 21.7 us: 1.19x slower                                                          |
| async_generators         | 241 ms                                                          | 301 ms: 1.25x slower                                                           |
| telco                    | 4.83 ms                                                         | 6.98 ms: 1.45x slower                                                          |
| Geometric mean           | (ref)                                                           | 1.12x faster                                                                   |

Benchmark hidden because not significant (5): asyncio_tcp, sqlglot_normalize, meteor_contest, xml_etree_process, richards
Ignored benchmarks (7) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (4) of results/bm-20241011-3.14.0a0-b3aa1b5/bm-20241011-pythonperf1_win32-x86-python-b3aa1b5fe260382788a2-3.14.0a0-b3aa1b5.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

- Geometric mean (including insignificant results): 1.137x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: unknown
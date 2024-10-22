# Results vs. 3.10.4

- fork: python
- ref: e913d2c87f1ae4e7a4ae
- machine: windows-x86
- commit hash: e913d2c
- commit date: 2024-08-15
- overall geometric mean: 1.12x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240815-pythonperf1_win32-x86-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 254 ms: 1.05x faster                                                           |
| docutils       | 1.95 sec                                                        | 1.94 sec: 1.01x faster                                                         |
| html5lib       | 52.1 ms                                                         | 48.6 ms: 1.07x faster                                                          |
| tornado_http   | 118 ms                                                          | 105 ms: 1.12x faster                                                           |
| Geometric mean | (ref)                                                           | 1.06x faster                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240815-pythonperf1_win32-x86-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|-------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 922 ms                                                          | 472 ms: 1.96x faster                                                           |
| async_tree_none         | 394 ms                                                          | 228 ms: 1.73x faster                                                           |
| async_tree_io           | 940 ms                                                          | 552 ms: 1.71x faster                                                           |
| async_tree_memoization  | 467 ms                                                          | 279 ms: 1.67x faster                                                           |
| Geometric mean          | (ref)                                                           | 1.76x faster                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240815-pythonperf1_win32-x86-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 198 ms: 2.54x faster                                                           |
| float          | 69.6 ms                                                         | 61.2 ms: 1.14x faster                                                          |
| nbody          | 79.1 ms                                                         | 93.3 ms: 1.18x slower                                                          |
| Geometric mean | (ref)                                                           | 1.35x faster                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240815-pythonperf1_win32-x86-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_dna      | 131 ms                                                          | 119 ms: 1.09x faster                                                           |
| regex_compile  | 117 ms                                                          | 107 ms: 1.09x faster                                                           |
| regex_v8       | 15.8 ms                                                         | 16.2 ms: 1.03x slower                                                          |
| regex_effbot   | 1.66 ms                                                         | 1.93 ms: 1.16x slower                                                          |
| Geometric mean | (ref)                                                           | 1.00x faster                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240815-pythonperf1_win32-x86-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|----------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| json_dumps           | 9.82 ms                                                         | 7.70 ms: 1.28x faster                                                          |
| xml_etree_parse      | 120 ms                                                          | 108 ms: 1.11x faster                                                           |
| pickle_pure_python   | 280 us                                                          | 254 us: 1.11x faster                                                           |
| json_loads           | 22.4 us                                                         | 20.3 us: 1.10x faster                                                          |
| unpickle_pure_python | 189 us                                                          | 178 us: 1.06x faster                                                           |
| xml_etree_iterparse  | 70.8 ms                                                         | 69.0 ms: 1.03x faster                                                          |
| tomli_loads          | 1.91 sec                                                        | 1.88 sec: 1.01x faster                                                         |
| xml_etree_process    | 48.1 ms                                                         | 51.2 ms: 1.06x slower                                                          |
| xml_etree_generate   | 61.6 ms                                                         | 70.0 ms: 1.14x slower                                                          |
| Geometric mean       | (ref)                                                           | 1.05x faster                                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240815-pythonperf1_win32-x86-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup         | 22.9 ms                                                         | 24.0 ms: 1.05x slower                                                          |
| python_startup_no_site | 18.1 ms                                                         | 19.9 ms: 1.10x slower                                                          |
| Geometric mean         | (ref)                                                           | 1.07x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240815-pythonperf1_win32-x86-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|-----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| django_template | 36.0 ms                                                         | 31.8 ms: 1.13x faster                                                          |
| mako            | 9.10 ms                                                         | 8.13 ms: 1.12x faster                                                          |
| genshi_text     | 21.0 ms                                                         | 22.7 ms: 1.08x slower                                                          |
| Geometric mean  | (ref)                                                           | 1.04x faster                                                                   |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240815-pythonperf1_win32-x86-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|--------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| typing_runtime_protocols | 396 us                                                          | 145 us: 2.73x faster                                                           |
| pidigits                 | 502 ms                                                          | 198 ms: 2.54x faster                                                           |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 472 ms: 1.96x faster                                                           |
| async_tree_none          | 394 ms                                                          | 228 ms: 1.73x faster                                                           |
| async_tree_io            | 940 ms                                                          | 552 ms: 1.71x faster                                                           |
| async_tree_memoization   | 467 ms                                                          | 279 ms: 1.67x faster                                                           |
| pylint                   | 384 ms                                                          | 236 ms: 1.63x faster                                                           |
| deltablue                | 4.04 ms                                                         | 2.72 ms: 1.48x faster                                                          |
| chaos                    | 74.4 ms                                                         | 52.0 ms: 1.43x faster                                                          |
| crypto_pyaes             | 81.3 ms                                                         | 57.6 ms: 1.41x faster                                                          |
| raytrace                 | 303 ms                                                          | 218 ms: 1.39x faster                                                           |
| deepcopy_memo            | 29.6 us                                                         | 22.8 us: 1.30x faster                                                          |
| scimark_lu               | 89.8 ms                                                         | 69.4 ms: 1.29x faster                                                          |
| comprehensions           | 17.7 us                                                         | 13.8 us: 1.28x faster                                                          |
| json_dumps               | 9.82 ms                                                         | 7.70 ms: 1.28x faster                                                          |
| logging_silent           | 97.9 ns                                                         | 77.1 ns: 1.27x faster                                                          |
| go                       | 146 ms                                                          | 118 ms: 1.23x faster                                                           |
| thrift                   | 902 us                                                          | 737 us: 1.22x faster                                                           |
| sqlglot_parse            | 1.33 ms                                                         | 1.09 ms: 1.22x faster                                                          |
| pycparser                | 1.04 sec                                                        | 858 ms: 1.21x faster                                                           |
| deepcopy                 | 310 us                                                          | 255 us: 1.21x faster                                                           |
| sqlglot_transpile        | 1.58 ms                                                         | 1.35 ms: 1.18x faster                                                          |
| dulwich_log              | 58.5 ms                                                         | 49.8 ms: 1.17x faster                                                          |
| generators               | 31.6 ms                                                         | 27.2 ms: 1.16x faster                                                          |
| scimark_sor              | 115 ms                                                          | 99.6 ms: 1.16x faster                                                          |
| hexiom                   | 6.13 ms                                                         | 5.33 ms: 1.15x faster                                                          |
| richards_super           | 49.9 ms                                                         | 43.6 ms: 1.14x faster                                                          |
| float                    | 69.6 ms                                                         | 61.2 ms: 1.14x faster                                                          |
| django_template          | 36.0 ms                                                         | 31.8 ms: 1.13x faster                                                          |
| json                     | 4.76 ms                                                         | 4.22 ms: 1.13x faster                                                          |
| tornado_http             | 118 ms                                                          | 105 ms: 1.12x faster                                                           |
| mako                     | 9.10 ms                                                         | 8.13 ms: 1.12x faster                                                          |
| pyflate                  | 422 ms                                                          | 379 ms: 1.11x faster                                                           |
| sympy_sum                | 122 ms                                                          | 110 ms: 1.11x faster                                                           |
| xml_etree_parse          | 120 ms                                                          | 108 ms: 1.11x faster                                                           |
| pickle_pure_python       | 280 us                                                          | 254 us: 1.11x faster                                                           |
| json_loads               | 22.4 us                                                         | 20.3 us: 1.10x faster                                                          |
| bench_thread_pool        | 1.12 ms                                                         | 1.02 ms: 1.10x faster                                                          |
| regex_dna                | 131 ms                                                          | 119 ms: 1.09x faster                                                           |
| regex_compile            | 117 ms                                                          | 107 ms: 1.09x faster                                                           |
| nqueens                  | 87.1 ms                                                         | 80.6 ms: 1.08x faster                                                          |
| scimark_monte_carlo      | 61.9 ms                                                         | 57.5 ms: 1.08x faster                                                          |
| html5lib                 | 52.1 ms                                                         | 48.6 ms: 1.07x faster                                                          |
| mdp                      | 1.83 sec                                                        | 1.71 sec: 1.07x faster                                                         |
| unpickle_pure_python     | 189 us                                                          | 178 us: 1.06x faster                                                           |
| sympy_integrate          | 16.6 ms                                                         | 15.7 ms: 1.06x faster                                                          |
| deepcopy_reduce          | 2.68 us                                                         | 2.55 us: 1.05x faster                                                          |
| 2to3                     | 265 ms                                                          | 254 ms: 1.05x faster                                                           |
| sympy_str                | 229 ms                                                          | 220 ms: 1.04x faster                                                           |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 3.12 ms: 1.04x faster                                                          |
| richards                 | 40.3 ms                                                         | 38.8 ms: 1.04x faster                                                          |
| pprint_safe_repr         | 658 ms                                                          | 639 ms: 1.03x faster                                                           |
| xml_etree_iterparse      | 70.8 ms                                                         | 69.0 ms: 1.03x faster                                                          |
| spectral_norm            | 80.2 ms                                                         | 78.2 ms: 1.03x faster                                                          |
| sympy_expand             | 391 ms                                                          | 382 ms: 1.02x faster                                                           |
| sqlglot_optimize         | 44.7 ms                                                         | 43.8 ms: 1.02x faster                                                          |
| coroutines               | 17.9 ms                                                         | 17.6 ms: 1.02x faster                                                          |
| tomli_loads              | 1.91 sec                                                        | 1.88 sec: 1.01x faster                                                         |
| docutils                 | 1.95 sec                                                        | 1.94 sec: 1.01x faster                                                         |
| sqlglot_normalize        | 230 ms                                                          | 230 ms: 1.00x faster                                                           |
| asyncio_tcp_ssl          | 17.0 sec                                                        | 17.2 sec: 1.01x slower                                                         |
| regex_v8                 | 15.8 ms                                                         | 16.2 ms: 1.03x slower                                                          |
| meteor_contest           | 80.0 ms                                                         | 82.9 ms: 1.04x slower                                                          |
| python_startup           | 22.9 ms                                                         | 24.0 ms: 1.05x slower                                                          |
| xml_etree_process        | 48.1 ms                                                         | 51.2 ms: 1.06x slower                                                          |
| scimark_fft              | 216 ms                                                          | 230 ms: 1.06x slower                                                           |
| pathlib                  | 81.2 ms                                                         | 87.3 ms: 1.07x slower                                                          |
| create_gc_cycles         | 694 us                                                          | 746 us: 1.07x slower                                                           |
| genshi_text              | 21.0 ms                                                         | 22.7 ms: 1.08x slower                                                          |
| logging_format           | 7.91 us                                                         | 8.57 us: 1.08x slower                                                          |
| logging_simple           | 7.29 us                                                         | 7.95 us: 1.09x slower                                                          |
| fannkuch                 | 317 ms                                                          | 347 ms: 1.09x slower                                                           |
| bench_mp_pool            | 66.4 ms                                                         | 72.7 ms: 1.10x slower                                                          |
| python_startup_no_site   | 18.1 ms                                                         | 19.9 ms: 1.10x slower                                                          |
| gc_traversal             | 1.28 ms                                                         | 1.44 ms: 1.13x slower                                                          |
| xml_etree_generate       | 61.6 ms                                                         | 70.0 ms: 1.14x slower                                                          |
| coverage                 | 46.6 ms                                                         | 53.0 ms: 1.14x slower                                                          |
| regex_effbot             | 1.66 ms                                                         | 1.93 ms: 1.16x slower                                                          |
| nbody                    | 79.1 ms                                                         | 93.3 ms: 1.18x slower                                                          |
| async_generators         | 241 ms                                                          | 307 ms: 1.27x slower                                                           |
| telco                    | 4.83 ms                                                         | 6.20 ms: 1.28x slower                                                          |
| Geometric mean           | (ref)                                                           | 1.12x faster                                                                   |

Benchmark hidden because not significant (3): asyncio_tcp, pprint_pformat, genshi_xml
Ignored benchmarks (14) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (4) of results/bm-20240815-3.14.0a0-e913d2c/bm-20240815-pythonperf1_win32-x86-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: unknown
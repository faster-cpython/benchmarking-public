# Results vs. 3.10.4

- fork: python
- ref: e418fc3a6e7bade68ab5
- machine: windows-x86
- commit hash: e418fc3
- commit date: 2024-05-25
- overall geometric mean: 1.13x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240525-pythonperf1_win32-x86-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 254 ms: 1.05x faster                                                           |
| chameleon      | 6.42 ms                                                         | 6.16 ms: 1.04x faster                                                          |
| docutils       | 1.95 sec                                                        | 2.03 sec: 1.04x slower                                                         |
| html5lib       | 52.1 ms                                                         | 50.2 ms: 1.04x faster                                                          |
| tornado_http   | 118 ms                                                          | 100 ms: 1.18x faster                                                           |
| Geometric mean | (ref)                                                           | 1.05x faster                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240525-pythonperf1_win32-x86-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|-------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 922 ms                                                          | 488 ms: 1.89x faster                                                           |
| async_tree_io           | 940 ms                                                          | 546 ms: 1.72x faster                                                           |
| async_tree_none         | 394 ms                                                          | 236 ms: 1.67x faster                                                           |
| async_tree_memoization  | 467 ms                                                          | 284 ms: 1.65x faster                                                           |
| Geometric mean          | (ref)                                                           | 1.73x faster                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240525-pythonperf1_win32-x86-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 198 ms: 2.54x faster                                                           |
| float          | 69.6 ms                                                         | 51.7 ms: 1.35x faster                                                          |
| nbody          | 79.1 ms                                                         | 75.6 ms: 1.05x faster                                                          |
| Geometric mean | (ref)                                                           | 1.53x faster                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240525-pythonperf1_win32-x86-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_dna      | 131 ms                                                          | 117 ms: 1.11x faster                                                           |
| regex_v8       | 15.8 ms                                                         | 16.1 ms: 1.02x slower                                                          |
| regex_compile  | 117 ms                                                          | 128 ms: 1.10x slower                                                           |
| regex_effbot   | 1.66 ms                                                         | 1.89 ms: 1.14x slower                                                          |
| Geometric mean | (ref)                                                           | 1.03x slower                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240525-pythonperf1_win32-x86-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| json_dumps           | 9.82 ms                                                         | 6.97 ms: 1.41x faster                                                          |
| tomli_loads          | 1.91 sec                                                        | 1.63 sec: 1.17x faster                                                         |
| xml_etree_parse      | 120 ms                                                          | 104 ms: 1.16x faster                                                           |
| pickle_pure_python   | 280 us                                                          | 243 us: 1.15x faster                                                           |
| unpickle_pure_python | 189 us                                                          | 170 us: 1.12x faster                                                           |
| xml_etree_process    | 48.1 ms                                                         | 43.4 ms: 1.11x faster                                                          |
| json_loads           | 22.4 us                                                         | 20.3 us: 1.10x faster                                                          |
| xml_etree_iterparse  | 70.8 ms                                                         | 64.4 ms: 1.10x faster                                                          |
| xml_etree_generate   | 61.6 ms                                                         | 60.9 ms: 1.01x faster                                                          |
| unpickle             | 9.82 us                                                         | 10.3 us: 1.04x slower                                                          |
| unpickle_list        | 2.98 us                                                         | 3.17 us: 1.06x slower                                                          |
| pickle               | 7.83 us                                                         | 8.36 us: 1.07x slower                                                          |
| pickle_list          | 3.22 us                                                         | 3.54 us: 1.10x slower                                                          |
| pickle_dict          | 18.2 us                                                         | 20.6 us: 1.13x slower                                                          |
| Geometric mean       | (ref)                                                           | 1.06x faster                                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240525-pythonperf1_win32-x86-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup         | 22.9 ms                                                         | 22.7 ms: 1.01x faster                                                          |
| python_startup_no_site | 18.1 ms                                                         | 18.4 ms: 1.02x slower                                                          |
| Geometric mean         | (ref)                                                           | 1.00x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240525-pythonperf1_win32-x86-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|-----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako            | 9.10 ms                                                         | 7.12 ms: 1.28x faster                                                          |
| django_template | 36.0 ms                                                         | 32.6 ms: 1.10x faster                                                          |
| genshi_text     | 21.0 ms                                                         | 21.8 ms: 1.04x slower                                                          |
| genshi_xml      | 46.6 ms                                                         | 48.6 ms: 1.04x slower                                                          |
| Geometric mean  | (ref)                                                           | 1.07x faster                                                                   |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240525-pythonperf1_win32-x86-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|--------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| typing_runtime_protocols | 396 us                                                          | 143 us: 2.77x faster                                                           |
| pidigits                 | 502 ms                                                          | 198 ms: 2.54x faster                                                           |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 488 ms: 1.89x faster                                                           |
| async_tree_io            | 940 ms                                                          | 546 ms: 1.72x faster                                                           |
| async_tree_none          | 394 ms                                                          | 236 ms: 1.67x faster                                                           |
| async_tree_memoization   | 467 ms                                                          | 284 ms: 1.65x faster                                                           |
| pylint                   | 384 ms                                                          | 243 ms: 1.58x faster                                                           |
| chaos                    | 74.4 ms                                                         | 51.0 ms: 1.46x faster                                                          |
| raytrace                 | 303 ms                                                          | 210 ms: 1.44x faster                                                           |
| richards_super           | 49.9 ms                                                         | 34.7 ms: 1.44x faster                                                          |
| deltablue                | 4.04 ms                                                         | 2.83 ms: 1.43x faster                                                          |
| json_dumps               | 9.82 ms                                                         | 6.97 ms: 1.41x faster                                                          |
| crypto_pyaes             | 81.3 ms                                                         | 58.2 ms: 1.40x faster                                                          |
| generators               | 31.6 ms                                                         | 23.0 ms: 1.37x faster                                                          |
| float                    | 69.6 ms                                                         | 51.7 ms: 1.35x faster                                                          |
| sqlglot_parse            | 1.33 ms                                                         | 997 us: 1.33x faster                                                           |
| logging_silent           | 97.9 ns                                                         | 73.4 ns: 1.33x faster                                                          |
| richards                 | 40.3 ms                                                         | 30.4 ms: 1.32x faster                                                          |
| comprehensions           | 17.7 us                                                         | 13.5 us: 1.31x faster                                                          |
| mako                     | 9.10 ms                                                         | 7.12 ms: 1.28x faster                                                          |
| go                       | 146 ms                                                          | 115 ms: 1.27x faster                                                           |
| sqlglot_transpile        | 1.58 ms                                                         | 1.26 ms: 1.26x faster                                                          |
| scimark_monte_carlo      | 61.9 ms                                                         | 49.4 ms: 1.25x faster                                                          |
| asyncio_tcp              | 744 ms                                                          | 606 ms: 1.23x faster                                                           |
| thrift                   | 902 us                                                          | 743 us: 1.21x faster                                                           |
| pycparser                | 1.04 sec                                                        | 874 ms: 1.19x faster                                                           |
| sqlite_synth             | 2.29 us                                                         | 1.93 us: 1.19x faster                                                          |
| scimark_sor              | 115 ms                                                          | 97.0 ms: 1.19x faster                                                          |
| tornado_http             | 118 ms                                                          | 100 ms: 1.18x faster                                                           |
| tomli_loads              | 1.91 sec                                                        | 1.63 sec: 1.17x faster                                                         |
| nqueens                  | 87.1 ms                                                         | 74.4 ms: 1.17x faster                                                          |
| json                     | 4.76 ms                                                         | 4.11 ms: 1.16x faster                                                          |
| xml_etree_parse          | 120 ms                                                          | 104 ms: 1.16x faster                                                           |
| fannkuch                 | 317 ms                                                          | 275 ms: 1.15x faster                                                           |
| pickle_pure_python       | 280 us                                                          | 243 us: 1.15x faster                                                           |
| scimark_lu               | 89.8 ms                                                         | 78.4 ms: 1.14x faster                                                          |
| pyflate                  | 422 ms                                                          | 369 ms: 1.14x faster                                                           |
| coroutines               | 17.9 ms                                                         | 15.8 ms: 1.13x faster                                                          |
| spectral_norm            | 80.2 ms                                                         | 70.9 ms: 1.13x faster                                                          |
| unpickle_pure_python     | 189 us                                                          | 170 us: 1.12x faster                                                           |
| regex_dna                | 131 ms                                                          | 117 ms: 1.11x faster                                                           |
| xml_etree_process        | 48.1 ms                                                         | 43.4 ms: 1.11x faster                                                          |
| json_loads               | 22.4 us                                                         | 20.3 us: 1.10x faster                                                          |
| django_template          | 36.0 ms                                                         | 32.6 ms: 1.10x faster                                                          |
| hexiom                   | 6.13 ms                                                         | 5.58 ms: 1.10x faster                                                          |
| xml_etree_iterparse      | 70.8 ms                                                         | 64.4 ms: 1.10x faster                                                          |
| bench_thread_pool        | 1.12 ms                                                         | 1.02 ms: 1.10x faster                                                          |
| pprint_pformat           | 1.37 sec                                                        | 1.25 sec: 1.10x faster                                                         |
| mdp                      | 1.83 sec                                                        | 1.67 sec: 1.09x faster                                                         |
| deepcopy_memo            | 29.6 us                                                         | 27.2 us: 1.09x faster                                                          |
| pprint_safe_repr         | 658 ms                                                          | 607 ms: 1.08x faster                                                           |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 3.01 ms: 1.08x faster                                                          |
| nbody                    | 79.1 ms                                                         | 75.6 ms: 1.05x faster                                                          |
| 2to3                     | 265 ms                                                          | 254 ms: 1.05x faster                                                           |
| chameleon                | 6.42 ms                                                         | 6.16 ms: 1.04x faster                                                          |
| sympy_sum                | 122 ms                                                          | 118 ms: 1.04x faster                                                           |
| html5lib                 | 52.1 ms                                                         | 50.2 ms: 1.04x faster                                                          |
| meteor_contest           | 80.0 ms                                                         | 77.7 ms: 1.03x faster                                                          |
| sqlglot_normalize        | 230 ms                                                          | 226 ms: 1.02x faster                                                           |
| scimark_fft              | 216 ms                                                          | 213 ms: 1.02x faster                                                           |
| deepcopy                 | 310 us                                                          | 305 us: 1.01x faster                                                           |
| xml_etree_generate       | 61.6 ms                                                         | 60.9 ms: 1.01x faster                                                          |
| python_startup           | 22.9 ms                                                         | 22.7 ms: 1.01x faster                                                          |
| sqlglot_optimize         | 44.7 ms                                                         | 44.3 ms: 1.01x faster                                                          |
| sympy_integrate          | 16.6 ms                                                         | 16.5 ms: 1.01x faster                                                          |
| flaskblogging            | 2.03 sec                                                        | 2.03 sec: 1.00x slower                                                         |
| python_startup_no_site   | 18.1 ms                                                         | 18.4 ms: 1.02x slower                                                          |
| regex_v8                 | 15.8 ms                                                         | 16.1 ms: 1.02x slower                                                          |
| sympy_str                | 229 ms                                                          | 237 ms: 1.04x slower                                                           |
| docutils                 | 1.95 sec                                                        | 2.03 sec: 1.04x slower                                                         |
| genshi_text              | 21.0 ms                                                         | 21.8 ms: 1.04x slower                                                          |
| genshi_xml               | 46.6 ms                                                         | 48.6 ms: 1.04x slower                                                          |
| unpickle                 | 9.82 us                                                         | 10.3 us: 1.04x slower                                                          |
| logging_simple           | 7.29 us                                                         | 7.68 us: 1.05x slower                                                          |
| logging_format           | 7.91 us                                                         | 8.37 us: 1.06x slower                                                          |
| unpickle_list            | 2.98 us                                                         | 3.17 us: 1.06x slower                                                          |
| coverage                 | 46.6 ms                                                         | 49.7 ms: 1.07x slower                                                          |
| pickle                   | 7.83 us                                                         | 8.36 us: 1.07x slower                                                          |
| pathlib                  | 81.2 ms                                                         | 87.3 ms: 1.08x slower                                                          |
| deepcopy_reduce          | 2.68 us                                                         | 2.91 us: 1.09x slower                                                          |
| sympy_expand             | 391 ms                                                          | 428 ms: 1.10x slower                                                           |
| regex_compile            | 117 ms                                                          | 128 ms: 1.10x slower                                                           |
| pickle_list              | 3.22 us                                                         | 3.54 us: 1.10x slower                                                          |
| bench_mp_pool            | 66.4 ms                                                         | 73.1 ms: 1.10x slower                                                          |
| create_gc_cycles         | 694 us                                                          | 768 us: 1.11x slower                                                           |
| gc_traversal             | 1.28 ms                                                         | 1.44 ms: 1.12x slower                                                          |
| pickle_dict              | 18.2 us                                                         | 20.6 us: 1.13x slower                                                          |
| regex_effbot             | 1.66 ms                                                         | 1.89 ms: 1.14x slower                                                          |
| async_generators         | 241 ms                                                          | 293 ms: 1.22x slower                                                           |
| telco                    | 4.83 ms                                                         | 5.93 ms: 1.23x slower                                                          |
| Geometric mean           | (ref)                                                           | 1.13x faster                                                                   |

Benchmark hidden because not significant (1): asyncio_tcp_ssl
Ignored benchmarks (7) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, dask, dulwich_log, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (4) of results/bm-20240525-3.14.0a0-e418fc3-PYTHON_UOPS/bm-20240525-pythonperf1_win32-x86-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.08x
- 95% likely to have a speedup of 1.07x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: unknown
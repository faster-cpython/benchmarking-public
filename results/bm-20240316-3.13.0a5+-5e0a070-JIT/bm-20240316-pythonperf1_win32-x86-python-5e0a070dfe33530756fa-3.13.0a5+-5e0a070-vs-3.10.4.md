# Results vs. 3.10.4

- fork: python
- ref: 5e0a070dfe33530756fa
- machine: windows-x86
- commit hash: 5e0a070
- commit date: 2024-03-16
- overall geometric mean: 1.05x faster
- HPT reliability: 99.97%
- HPT 99th percentile: 1.02x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240316-pythonperf1_win32-x86-python-5e0a070dfe33530756fa-3.13.0a5+-5e0a070 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 261 ms: 1.02x faster                                                            |
| chameleon      | 6.42 ms                                                         | 5.81 ms: 1.10x faster                                                           |
| docutils       | 1.95 sec                                                        | 1.82 sec: 1.07x faster                                                          |
| html5lib       | 52.1 ms                                                         | 45.1 ms: 1.16x faster                                                           |
| tornado_http   | 118 ms                                                          | 96.2 ms: 1.22x faster                                                           |
| Geometric mean | (ref)                                                           | 1.11x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240316-pythonperf1_win32-x86-python-5e0a070dfe33530756fa-3.13.0a5+-5e0a070 |
|-------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 922 ms                                                          | 529 ms: 1.74x faster                                                            |
| async_tree_io           | 940 ms                                                          | 626 ms: 1.50x faster                                                            |
| async_tree_none         | 394 ms                                                          | 265 ms: 1.49x faster                                                            |
| async_tree_memoization  | 467 ms                                                          | 325 ms: 1.43x faster                                                            |
| Geometric mean          | (ref)                                                           | 1.54x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240316-pythonperf1_win32-x86-python-5e0a070dfe33530756fa-3.13.0a5+-5e0a070 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 199 ms: 2.52x faster                                                            |
| float          | 69.6 ms                                                         | 55.3 ms: 1.26x faster                                                           |
| nbody          | 79.1 ms                                                         | 96.3 ms: 1.22x slower                                                           |
| Geometric mean | (ref)                                                           | 1.38x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240316-pythonperf1_win32-x86-python-5e0a070dfe33530756fa-3.13.0a5+-5e0a070 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_dna      | 131 ms                                                          | 118 ms: 1.11x faster                                                            |
| regex_compile  | 117 ms                                                          | 110 ms: 1.06x faster                                                            |
| regex_v8       | 15.8 ms                                                         | 16.2 ms: 1.03x slower                                                           |
| regex_effbot   | 1.66 ms                                                         | 1.91 ms: 1.15x slower                                                           |
| Geometric mean | (ref)                                                           | 1.00x slower                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240316-pythonperf1_win32-x86-python-5e0a070dfe33530756fa-3.13.0a5+-5e0a070 |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| json_dumps           | 9.82 ms                                                         | 6.70 ms: 1.47x faster                                                           |
| pickle_pure_python   | 280 us                                                          | 221 us: 1.27x faster                                                            |
| json_loads           | 22.4 us                                                         | 19.7 us: 1.13x faster                                                           |
| unpickle_pure_python | 189 us                                                          | 170 us: 1.11x faster                                                            |
| xml_etree_parse      | 120 ms                                                          | 110 ms: 1.09x faster                                                            |
| tomli_loads          | 1.91 sec                                                        | 1.76 sec: 1.09x faster                                                          |
| xml_etree_iterparse  | 70.8 ms                                                         | 67.2 ms: 1.05x faster                                                           |
| xml_etree_process    | 48.1 ms                                                         | 45.8 ms: 1.05x faster                                                           |
| unpickle_list        | 2.98 us                                                         | 2.85 us: 1.05x faster                                                           |
| unpickle             | 9.82 us                                                         | 10.00 us: 1.02x slower                                                          |
| xml_etree_generate   | 61.6 ms                                                         | 63.7 ms: 1.03x slower                                                           |
| pickle_dict          | 18.2 us                                                         | 19.9 us: 1.09x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.08x faster                                                                    |

Benchmark hidden because not significant (2): pickle_list, pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240316-pythonperf1_win32-x86-python-5e0a070dfe33530756fa-3.13.0a5+-5e0a070 |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 22.9 ms                                                         | 27.1 ms: 1.18x slower                                                           |
| python_startup_no_site | 18.1 ms                                                         | 24.5 ms: 1.36x slower                                                           |
| Geometric mean         | (ref)                                                           | 1.27x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240316-pythonperf1_win32-x86-python-5e0a070dfe33530756fa-3.13.0a5+-5e0a070 |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 9.10 ms                                                         | 7.24 ms: 1.26x faster                                                           |
| django_template | 36.0 ms                                                         | 30.2 ms: 1.19x faster                                                           |
| genshi_xml      | 46.6 ms                                                         | 49.0 ms: 1.05x slower                                                           |
| genshi_text     | 21.0 ms                                                         | 22.6 ms: 1.08x slower                                                           |
| Geometric mean  | (ref)                                                           | 1.07x faster                                                                    |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240316-pythonperf1_win32-x86-python-5e0a070dfe33530756fa-3.13.0a5+-5e0a070 |
|--------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| typing_runtime_protocols | 396 us                                                          | 93.6 us: 4.23x faster                                                           |
| pidigits                 | 502 ms                                                          | 199 ms: 2.52x faster                                                            |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 529 ms: 1.74x faster                                                            |
| pylint                   | 384 ms                                                          | 225 ms: 1.70x faster                                                            |
| logging_silent           | 97.9 ns                                                         | 60.3 ns: 1.62x faster                                                           |
| deltablue                | 4.04 ms                                                         | 2.56 ms: 1.58x faster                                                           |
| async_tree_io            | 940 ms                                                          | 626 ms: 1.50x faster                                                            |
| async_tree_none          | 394 ms                                                          | 265 ms: 1.49x faster                                                            |
| json_dumps               | 9.82 ms                                                         | 6.70 ms: 1.47x faster                                                           |
| async_tree_memoization   | 467 ms                                                          | 325 ms: 1.43x faster                                                            |
| generators               | 31.6 ms                                                         | 22.6 ms: 1.40x faster                                                           |
| crypto_pyaes             | 81.3 ms                                                         | 60.6 ms: 1.34x faster                                                           |
| sqlglot_parse            | 1.33 ms                                                         | 996 us: 1.34x faster                                                            |
| sqlglot_transpile        | 1.58 ms                                                         | 1.24 ms: 1.27x faster                                                           |
| pickle_pure_python       | 280 us                                                          | 221 us: 1.27x faster                                                            |
| richards_super           | 49.9 ms                                                         | 39.5 ms: 1.26x faster                                                           |
| float                    | 69.6 ms                                                         | 55.3 ms: 1.26x faster                                                           |
| mako                     | 9.10 ms                                                         | 7.24 ms: 1.26x faster                                                           |
| comprehensions           | 17.7 us                                                         | 14.5 us: 1.23x faster                                                           |
| chaos                    | 74.4 ms                                                         | 60.7 ms: 1.23x faster                                                           |
| tornado_http             | 118 ms                                                          | 96.2 ms: 1.22x faster                                                           |
| coroutines               | 17.9 ms                                                         | 14.9 ms: 1.20x faster                                                           |
| django_template          | 36.0 ms                                                         | 30.2 ms: 1.19x faster                                                           |
| go                       | 146 ms                                                          | 122 ms: 1.19x faster                                                            |
| pycparser                | 1.04 sec                                                        | 877 ms: 1.19x faster                                                            |
| sqlite_synth             | 2.29 us                                                         | 1.94 us: 1.18x faster                                                           |
| asyncio_tcp              | 744 ms                                                          | 642 ms: 1.16x faster                                                            |
| html5lib                 | 52.1 ms                                                         | 45.1 ms: 1.16x faster                                                           |
| scimark_sor              | 115 ms                                                          | 99.9 ms: 1.15x faster                                                           |
| deepcopy_memo            | 29.6 us                                                         | 25.7 us: 1.15x faster                                                           |
| sympy_sum                | 122 ms                                                          | 107 ms: 1.14x faster                                                            |
| richards                 | 40.3 ms                                                         | 35.4 ms: 1.14x faster                                                           |
| json_loads               | 22.4 us                                                         | 19.7 us: 1.13x faster                                                           |
| json                     | 4.76 ms                                                         | 4.22 ms: 1.13x faster                                                           |
| pyflate                  | 422 ms                                                          | 376 ms: 1.12x faster                                                            |
| unpickle_pure_python     | 189 us                                                          | 170 us: 1.11x faster                                                            |
| bench_thread_pool        | 1.12 ms                                                         | 1.01 ms: 1.11x faster                                                           |
| spectral_norm            | 80.2 ms                                                         | 72.3 ms: 1.11x faster                                                           |
| regex_dna                | 131 ms                                                          | 118 ms: 1.11x faster                                                            |
| chameleon                | 6.42 ms                                                         | 5.81 ms: 1.10x faster                                                           |
| raytrace                 | 303 ms                                                          | 274 ms: 1.10x faster                                                            |
| deepcopy                 | 310 us                                                          | 283 us: 1.10x faster                                                            |
| xml_etree_parse          | 120 ms                                                          | 110 ms: 1.09x faster                                                            |
| tomli_loads              | 1.91 sec                                                        | 1.76 sec: 1.09x faster                                                          |
| sympy_str                | 229 ms                                                          | 213 ms: 1.08x faster                                                            |
| sympy_integrate          | 16.6 ms                                                         | 15.5 ms: 1.08x faster                                                           |
| mdp                      | 1.83 sec                                                        | 1.70 sec: 1.07x faster                                                          |
| deepcopy_reduce          | 2.68 us                                                         | 2.51 us: 1.07x faster                                                           |
| docutils                 | 1.95 sec                                                        | 1.82 sec: 1.07x faster                                                          |
| regex_compile            | 117 ms                                                          | 110 ms: 1.06x faster                                                            |
| create_gc_cycles         | 694 us                                                          | 656 us: 1.06x faster                                                            |
| xml_etree_iterparse      | 70.8 ms                                                         | 67.2 ms: 1.05x faster                                                           |
| xml_etree_process        | 48.1 ms                                                         | 45.8 ms: 1.05x faster                                                           |
| sympy_expand             | 391 ms                                                          | 372 ms: 1.05x faster                                                            |
| unpickle_list            | 2.98 us                                                         | 2.85 us: 1.05x faster                                                           |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 3.10 ms: 1.04x faster                                                           |
| hexiom                   | 6.13 ms                                                         | 5.97 ms: 1.03x faster                                                           |
| sqlglot_normalize        | 230 ms                                                          | 226 ms: 1.02x faster                                                            |
| 2to3                     | 265 ms                                                          | 261 ms: 1.02x faster                                                            |
| asyncio_tcp_ssl          | 17.0 sec                                                        | 16.7 sec: 1.02x faster                                                          |
| scimark_lu               | 89.8 ms                                                         | 88.5 ms: 1.01x faster                                                           |
| sqlglot_optimize         | 44.7 ms                                                         | 45.4 ms: 1.01x slower                                                           |
| unpickle                 | 9.82 us                                                         | 10.00 us: 1.02x slower                                                          |
| regex_v8                 | 15.8 ms                                                         | 16.2 ms: 1.03x slower                                                           |
| xml_etree_generate       | 61.6 ms                                                         | 63.7 ms: 1.03x slower                                                           |
| meteor_contest           | 80.0 ms                                                         | 83.9 ms: 1.05x slower                                                           |
| fannkuch                 | 317 ms                                                          | 334 ms: 1.05x slower                                                            |
| genshi_xml               | 46.6 ms                                                         | 49.0 ms: 1.05x slower                                                           |
| pathlib                  | 81.2 ms                                                         | 85.7 ms: 1.05x slower                                                           |
| scimark_monte_carlo      | 61.9 ms                                                         | 65.5 ms: 1.06x slower                                                           |
| nqueens                  | 87.1 ms                                                         | 93.2 ms: 1.07x slower                                                           |
| genshi_text              | 21.0 ms                                                         | 22.6 ms: 1.08x slower                                                           |
| pickle_dict              | 18.2 us                                                         | 19.9 us: 1.09x slower                                                           |
| scimark_fft              | 216 ms                                                          | 236 ms: 1.09x slower                                                            |
| gc_traversal             | 1.28 ms                                                         | 1.41 ms: 1.10x slower                                                           |
| pprint_pformat           | 1.37 sec                                                        | 1.52 sec: 1.11x slower                                                          |
| logging_format           | 7.91 us                                                         | 8.77 us: 1.11x slower                                                           |
| logging_simple           | 7.29 us                                                         | 8.18 us: 1.12x slower                                                           |
| pprint_safe_repr         | 658 ms                                                          | 743 ms: 1.13x slower                                                            |
| unpack_sequence          | 40.0 ns                                                         | 45.3 ns: 1.13x slower                                                           |
| regex_effbot             | 1.66 ms                                                         | 1.91 ms: 1.15x slower                                                           |
| bench_mp_pool            | 66.4 ms                                                         | 77.6 ms: 1.17x slower                                                           |
| python_startup           | 22.9 ms                                                         | 27.1 ms: 1.18x slower                                                           |
| async_generators         | 241 ms                                                          | 291 ms: 1.21x slower                                                            |
| nbody                    | 79.1 ms                                                         | 96.3 ms: 1.22x slower                                                           |
| telco                    | 4.83 ms                                                         | 6.38 ms: 1.32x slower                                                           |
| python_startup_no_site   | 18.1 ms                                                         | 24.5 ms: 1.36x slower                                                           |
| coverage                 | 46.6 ms                                                         | 507 ms: 10.89x slower                                                           |
| thrift                   | 902 us                                                          | 10.9 ms: 12.07x slower                                                          |
| Geometric mean           | (ref)                                                           | 1.05x faster                                                                    |

Benchmark hidden because not significant (2): pickle_list, pickle
Ignored benchmarks (7) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, dask, dulwich_log, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (4) of results/bm-20240316-3.13.0a5+-5e0a070-JIT/bm-20240316-pythonperf1_win32-x86-python-5e0a070dfe33530756fa-3.13.0a5+-5e0a070.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg


# HPT report

- Reliability score: 99.97% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.02x


# Memory

- memory change: unknown
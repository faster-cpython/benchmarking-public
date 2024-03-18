# Results vs. 3.10.4

- fork: python
- ref: 5e0a070dfe33530756fa
- machine: windows-x86
- commit hash: 5e0a070
- commit date: 2024-03-16
- overall geometric mean: 1.10x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.07x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240316-pythonperf1_win32-x86-python-5e0a070dfe33530756fa-3.13.0a5+-5e0a070 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 245 ms: 1.09x faster                                                            |
| chameleon      | 6.42 ms                                                         | 6.11 ms: 1.05x faster                                                           |
| docutils       | 1.95 sec                                                        | 1.83 sec: 1.06x faster                                                          |
| html5lib       | 52.1 ms                                                         | 48.0 ms: 1.09x faster                                                           |
| tornado_http   | 118 ms                                                          | 98.6 ms: 1.19x faster                                                           |
| Geometric mean | (ref)                                                           | 1.09x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240316-pythonperf1_win32-x86-python-5e0a070dfe33530756fa-3.13.0a5+-5e0a070 |
|-------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 922 ms                                                          | 511 ms: 1.81x faster                                                            |
| async_tree_none         | 394 ms                                                          | 252 ms: 1.56x faster                                                            |
| async_tree_io           | 940 ms                                                          | 603 ms: 1.56x faster                                                            |
| async_tree_memoization  | 467 ms                                                          | 316 ms: 1.47x faster                                                            |
| Geometric mean          | (ref)                                                           | 1.60x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240316-pythonperf1_win32-x86-python-5e0a070dfe33530756fa-3.13.0a5+-5e0a070 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 199 ms: 2.52x faster                                                            |
| float          | 69.6 ms                                                         | 57.0 ms: 1.22x faster                                                           |
| nbody          | 79.1 ms                                                         | 77.0 ms: 1.03x faster                                                           |
| Geometric mean | (ref)                                                           | 1.47x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240316-pythonperf1_win32-x86-python-5e0a070dfe33530756fa-3.13.0a5+-5e0a070 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_dna      | 131 ms                                                          | 120 ms: 1.08x faster                                                            |
| regex_v8       | 15.8 ms                                                         | 16.1 ms: 1.02x slower                                                           |
| regex_effbot   | 1.66 ms                                                         | 1.91 ms: 1.15x slower                                                           |
| Geometric mean | (ref)                                                           | 1.02x slower                                                                    |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240316-pythonperf1_win32-x86-python-5e0a070dfe33530756fa-3.13.0a5+-5e0a070 |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| json_dumps           | 9.82 ms                                                         | 7.04 ms: 1.40x faster                                                           |
| pickle_pure_python   | 280 us                                                          | 216 us: 1.30x faster                                                            |
| tomli_loads          | 1.91 sec                                                        | 1.55 sec: 1.23x faster                                                          |
| unpickle_pure_python | 189 us                                                          | 167 us: 1.14x faster                                                            |
| xml_etree_process    | 48.1 ms                                                         | 42.9 ms: 1.12x faster                                                           |
| xml_etree_parse      | 120 ms                                                          | 109 ms: 1.10x faster                                                            |
| json_loads           | 22.4 us                                                         | 20.6 us: 1.09x faster                                                           |
| unpickle_list        | 2.98 us                                                         | 2.83 us: 1.05x faster                                                           |
| xml_etree_iterparse  | 70.8 ms                                                         | 68.4 ms: 1.04x faster                                                           |
| xml_etree_generate   | 61.6 ms                                                         | 61.1 ms: 1.01x faster                                                           |
| pickle               | 7.83 us                                                         | 7.79 us: 1.01x faster                                                           |
| pickle_list          | 3.22 us                                                         | 3.30 us: 1.02x slower                                                           |
| pickle_dict          | 18.2 us                                                         | 19.9 us: 1.09x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.09x faster                                                                    |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240316-pythonperf1_win32-x86-python-5e0a070dfe33530756fa-3.13.0a5+-5e0a070 |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 22.9 ms                                                         | 22.2 ms: 1.03x faster                                                           |
| python_startup_no_site | 18.1 ms                                                         | 20.0 ms: 1.11x slower                                                           |
| Geometric mean         | (ref)                                                           | 1.04x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240316-pythonperf1_win32-x86-python-5e0a070dfe33530756fa-3.13.0a5+-5e0a070 |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 9.10 ms                                                         | 6.99 ms: 1.30x faster                                                           |
| django_template | 36.0 ms                                                         | 30.3 ms: 1.19x faster                                                           |
| genshi_text     | 21.0 ms                                                         | 19.8 ms: 1.06x faster                                                           |
| genshi_xml      | 46.6 ms                                                         | 45.6 ms: 1.02x faster                                                           |
| Geometric mean  | (ref)                                                           | 1.14x faster                                                                    |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240316-pythonperf1_win32-x86-python-5e0a070dfe33530756fa-3.13.0a5+-5e0a070 |
|--------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| typing_runtime_protocols | 396 us                                                          | 92.5 us: 4.28x faster                                                           |
| pidigits                 | 502 ms                                                          | 199 ms: 2.52x faster                                                            |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 511 ms: 1.81x faster                                                            |
| deltablue                | 4.04 ms                                                         | 2.36 ms: 1.71x faster                                                           |
| pylint                   | 384 ms                                                          | 226 ms: 1.70x faster                                                            |
| logging_silent           | 97.9 ns                                                         | 60.2 ns: 1.63x faster                                                           |
| async_tree_none          | 394 ms                                                          | 252 ms: 1.56x faster                                                            |
| async_tree_io            | 940 ms                                                          | 603 ms: 1.56x faster                                                            |
| richards_super           | 49.9 ms                                                         | 33.2 ms: 1.50x faster                                                           |
| crypto_pyaes             | 81.3 ms                                                         | 54.7 ms: 1.49x faster                                                           |
| async_tree_memoization   | 467 ms                                                          | 316 ms: 1.47x faster                                                            |
| chaos                    | 74.4 ms                                                         | 52.9 ms: 1.41x faster                                                           |
| json_dumps               | 9.82 ms                                                         | 7.04 ms: 1.40x faster                                                           |
| sqlglot_parse            | 1.33 ms                                                         | 956 us: 1.39x faster                                                            |
| generators               | 31.6 ms                                                         | 22.9 ms: 1.38x faster                                                           |
| richards                 | 40.3 ms                                                         | 29.6 ms: 1.36x faster                                                           |
| raytrace                 | 303 ms                                                          | 226 ms: 1.34x faster                                                            |
| comprehensions           | 17.7 us                                                         | 13.3 us: 1.33x faster                                                           |
| sqlglot_transpile        | 1.58 ms                                                         | 1.19 ms: 1.33x faster                                                           |
| mako                     | 9.10 ms                                                         | 6.99 ms: 1.30x faster                                                           |
| pickle_pure_python       | 280 us                                                          | 216 us: 1.30x faster                                                            |
| pyflate                  | 422 ms                                                          | 335 ms: 1.26x faster                                                            |
| scimark_sor              | 115 ms                                                          | 91.6 ms: 1.26x faster                                                           |
| scimark_monte_carlo      | 61.9 ms                                                         | 49.4 ms: 1.25x faster                                                           |
| coroutines               | 17.9 ms                                                         | 14.4 ms: 1.24x faster                                                           |
| go                       | 146 ms                                                          | 117 ms: 1.24x faster                                                            |
| tomli_loads              | 1.91 sec                                                        | 1.55 sec: 1.23x faster                                                          |
| pycparser                | 1.04 sec                                                        | 852 ms: 1.22x faster                                                            |
| float                    | 69.6 ms                                                         | 57.0 ms: 1.22x faster                                                           |
| deepcopy_memo            | 29.6 us                                                         | 24.5 us: 1.21x faster                                                           |
| sqlite_synth             | 2.29 us                                                         | 1.90 us: 1.20x faster                                                           |
| tornado_http             | 118 ms                                                          | 98.6 ms: 1.19x faster                                                           |
| django_template          | 36.0 ms                                                         | 30.3 ms: 1.19x faster                                                           |
| asyncio_tcp              | 744 ms                                                          | 635 ms: 1.17x faster                                                            |
| scimark_lu               | 89.8 ms                                                         | 78.4 ms: 1.14x faster                                                           |
| unpickle_pure_python     | 189 us                                                          | 167 us: 1.14x faster                                                            |
| hexiom                   | 6.13 ms                                                         | 5.42 ms: 1.13x faster                                                           |
| sympy_sum                | 122 ms                                                          | 108 ms: 1.13x faster                                                            |
| deepcopy                 | 310 us                                                          | 275 us: 1.13x faster                                                            |
| xml_etree_process        | 48.1 ms                                                         | 42.9 ms: 1.12x faster                                                           |
| deepcopy_reduce          | 2.68 us                                                         | 2.40 us: 1.12x faster                                                           |
| mdp                      | 1.83 sec                                                        | 1.65 sec: 1.11x faster                                                          |
| json                     | 4.76 ms                                                         | 4.30 ms: 1.11x faster                                                           |
| xml_etree_parse          | 120 ms                                                          | 109 ms: 1.10x faster                                                            |
| pprint_pformat           | 1.37 sec                                                        | 1.25 sec: 1.10x faster                                                          |
| fannkuch                 | 317 ms                                                          | 289 ms: 1.10x faster                                                            |
| sympy_integrate          | 16.6 ms                                                         | 15.2 ms: 1.10x faster                                                           |
| bench_thread_pool        | 1.12 ms                                                         | 1.02 ms: 1.09x faster                                                           |
| sqlglot_normalize        | 230 ms                                                          | 212 ms: 1.09x faster                                                            |
| json_loads               | 22.4 us                                                         | 20.6 us: 1.09x faster                                                           |
| 2to3                     | 265 ms                                                          | 245 ms: 1.09x faster                                                            |
| html5lib                 | 52.1 ms                                                         | 48.0 ms: 1.09x faster                                                           |
| regex_dna                | 131 ms                                                          | 120 ms: 1.08x faster                                                            |
| pprint_safe_repr         | 658 ms                                                          | 612 ms: 1.08x faster                                                            |
| sympy_str                | 229 ms                                                          | 214 ms: 1.07x faster                                                            |
| nqueens                  | 87.1 ms                                                         | 81.3 ms: 1.07x faster                                                           |
| sqlglot_optimize         | 44.7 ms                                                         | 41.8 ms: 1.07x faster                                                           |
| docutils                 | 1.95 sec                                                        | 1.83 sec: 1.06x faster                                                          |
| genshi_text              | 21.0 ms                                                         | 19.8 ms: 1.06x faster                                                           |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 3.07 ms: 1.06x faster                                                           |
| unpickle_list            | 2.98 us                                                         | 2.83 us: 1.05x faster                                                           |
| create_gc_cycles         | 694 us                                                          | 660 us: 1.05x faster                                                            |
| chameleon                | 6.42 ms                                                         | 6.11 ms: 1.05x faster                                                           |
| meteor_contest           | 80.0 ms                                                         | 76.1 ms: 1.05x faster                                                           |
| sympy_expand             | 391 ms                                                          | 373 ms: 1.05x faster                                                            |
| scimark_fft              | 216 ms                                                          | 207 ms: 1.04x faster                                                            |
| spectral_norm            | 80.2 ms                                                         | 77.3 ms: 1.04x faster                                                           |
| xml_etree_iterparse      | 70.8 ms                                                         | 68.4 ms: 1.04x faster                                                           |
| python_startup           | 22.9 ms                                                         | 22.2 ms: 1.03x faster                                                           |
| nbody                    | 79.1 ms                                                         | 77.0 ms: 1.03x faster                                                           |
| genshi_xml               | 46.6 ms                                                         | 45.6 ms: 1.02x faster                                                           |
| asyncio_tcp_ssl          | 17.0 sec                                                        | 16.8 sec: 1.01x faster                                                          |
| xml_etree_generate       | 61.6 ms                                                         | 61.1 ms: 1.01x faster                                                           |
| pickle                   | 7.83 us                                                         | 7.79 us: 1.01x faster                                                           |
| regex_v8                 | 15.8 ms                                                         | 16.1 ms: 1.02x slower                                                           |
| pickle_list              | 3.22 us                                                         | 3.30 us: 1.02x slower                                                           |
| bench_mp_pool            | 66.4 ms                                                         | 70.0 ms: 1.05x slower                                                           |
| pathlib                  | 81.2 ms                                                         | 86.4 ms: 1.06x slower                                                           |
| logging_simple           | 7.29 us                                                         | 7.89 us: 1.08x slower                                                           |
| logging_format           | 7.91 us                                                         | 8.62 us: 1.09x slower                                                           |
| pickle_dict              | 18.2 us                                                         | 19.9 us: 1.09x slower                                                           |
| gc_traversal             | 1.28 ms                                                         | 1.40 ms: 1.09x slower                                                           |
| python_startup_no_site   | 18.1 ms                                                         | 20.0 ms: 1.11x slower                                                           |
| regex_effbot             | 1.66 ms                                                         | 1.91 ms: 1.15x slower                                                           |
| unpack_sequence          | 40.0 ns                                                         | 46.5 ns: 1.16x slower                                                           |
| async_generators         | 241 ms                                                          | 285 ms: 1.18x slower                                                            |
| telco                    | 4.83 ms                                                         | 6.21 ms: 1.29x slower                                                           |
| coverage                 | 46.6 ms                                                         | 474 ms: 10.19x slower                                                           |
| thrift                   | 902 us                                                          | 11.3 ms: 12.48x slower                                                          |
| Geometric mean           | (ref)                                                           | 1.10x faster                                                                    |

Benchmark hidden because not significant (2): unpickle, regex_compile
Ignored benchmarks (7) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, dask, dulwich_log, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (4) of results/bm-20240316-3.13.0a5+-5e0a070-PYTHON_UOPS/bm-20240316-pythonperf1_win32-x86-python-5e0a070dfe33530756fa-3.13.0a5+-5e0a070.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.09x
- 95% likely to have a speedup of 1.08x
- 99% likely to have a speedup of 1.07x


# Memory

- memory change: unknown
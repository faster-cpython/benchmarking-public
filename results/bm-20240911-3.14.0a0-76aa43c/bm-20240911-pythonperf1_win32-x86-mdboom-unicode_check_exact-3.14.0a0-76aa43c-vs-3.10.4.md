# Results vs. 3.10.4

- fork: mdboom
- ref: unicode_check_exact
- machine: windows-x86
- commit hash: 76aa43c
- commit date: 2024-09-11
- overall geometric mean: 1.12x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240911-pythonperf1_win32-x86-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|----------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 250 ms: 1.06x faster                                                          |
| docutils       | 1.95 sec                                                        | 1.86 sec: 1.05x faster                                                        |
| html5lib       | 52.1 ms                                                         | 46.5 ms: 1.12x faster                                                         |
| tornado_http   | 118 ms                                                          | 95.8 ms: 1.23x faster                                                         |
| Geometric mean | (ref)                                                           | 1.11x faster                                                                  |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240911-pythonperf1_win32-x86-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|-------------------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 922 ms                                                          | 469 ms: 1.97x faster                                                          |
| async_tree_none         | 394 ms                                                          | 218 ms: 1.81x faster                                                          |
| async_tree_io           | 940 ms                                                          | 534 ms: 1.76x faster                                                          |
| async_tree_memoization  | 467 ms                                                          | 271 ms: 1.72x faster                                                          |
| Geometric mean          | (ref)                                                           | 1.81x faster                                                                  |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240911-pythonperf1_win32-x86-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|----------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 201 ms: 2.50x faster                                                          |
| float          | 69.6 ms                                                         | 61.4 ms: 1.13x faster                                                         |
| nbody          | 79.1 ms                                                         | 91.6 ms: 1.16x slower                                                         |
| Geometric mean | (ref)                                                           | 1.35x faster                                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240911-pythonperf1_win32-x86-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|----------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| regex_dna      | 131 ms                                                          | 116 ms: 1.12x faster                                                          |
| regex_compile  | 117 ms                                                          | 107 ms: 1.09x faster                                                          |
| regex_v8       | 15.8 ms                                                         | 16.3 ms: 1.03x slower                                                         |
| regex_effbot   | 1.66 ms                                                         | 1.89 ms: 1.14x slower                                                         |
| Geometric mean | (ref)                                                           | 1.01x faster                                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240911-pythonperf1_win32-x86-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|----------------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| json_dumps           | 9.82 ms                                                         | 7.41 ms: 1.33x faster                                                         |
| xml_etree_parse      | 120 ms                                                          | 108 ms: 1.11x faster                                                          |
| pickle_pure_python   | 280 us                                                          | 256 us: 1.10x faster                                                          |
| json_loads           | 22.4 us                                                         | 20.8 us: 1.08x faster                                                         |
| unpickle_pure_python | 189 us                                                          | 178 us: 1.06x faster                                                          |
| xml_etree_iterparse  | 70.8 ms                                                         | 67.8 ms: 1.05x faster                                                         |
| tomli_loads          | 1.91 sec                                                        | 1.90 sec: 1.01x faster                                                        |
| xml_etree_process    | 48.1 ms                                                         | 48.6 ms: 1.01x slower                                                         |
| pickle               | 7.83 us                                                         | 7.96 us: 1.02x slower                                                         |
| unpickle_list        | 2.98 us                                                         | 3.08 us: 1.03x slower                                                         |
| unpickle             | 9.82 us                                                         | 10.4 us: 1.06x slower                                                         |
| xml_etree_generate   | 61.6 ms                                                         | 66.8 ms: 1.08x slower                                                         |
| pickle_list          | 3.22 us                                                         | 3.50 us: 1.09x slower                                                         |
| pickle_dict          | 18.2 us                                                         | 20.5 us: 1.12x slower                                                         |
| Geometric mean       | (ref)                                                           | 1.02x faster                                                                  |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240911-pythonperf1_win32-x86-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|------------------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| python_startup         | 22.9 ms                                                         | 23.5 ms: 1.02x slower                                                         |
| python_startup_no_site | 18.1 ms                                                         | 19.4 ms: 1.07x slower                                                         |
| Geometric mean         | (ref)                                                           | 1.05x slower                                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240911-pythonperf1_win32-x86-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|-----------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| mako            | 9.10 ms                                                         | 7.98 ms: 1.14x faster                                                         |
| django_template | 36.0 ms                                                         | 32.5 ms: 1.11x faster                                                         |
| genshi_xml      | 46.6 ms                                                         | 46.9 ms: 1.01x slower                                                         |
| genshi_text     | 21.0 ms                                                         | 21.8 ms: 1.04x slower                                                         |
| Geometric mean  | (ref)                                                           | 1.05x faster                                                                  |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240911-pythonperf1_win32-x86-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|--------------------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| typing_runtime_protocols | 396 us                                                          | 142 us: 2.78x faster                                                          |
| pidigits                 | 502 ms                                                          | 201 ms: 2.50x faster                                                          |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 469 ms: 1.97x faster                                                          |
| async_tree_none          | 394 ms                                                          | 218 ms: 1.81x faster                                                          |
| async_tree_io            | 940 ms                                                          | 534 ms: 1.76x faster                                                          |
| async_tree_memoization   | 467 ms                                                          | 271 ms: 1.72x faster                                                          |
| pylint                   | 384 ms                                                          | 232 ms: 1.65x faster                                                          |
| deltablue                | 4.04 ms                                                         | 2.70 ms: 1.49x faster                                                         |
| crypto_pyaes             | 81.3 ms                                                         | 57.0 ms: 1.42x faster                                                         |
| go                       | 146 ms                                                          | 103 ms: 1.42x faster                                                          |
| chaos                    | 74.4 ms                                                         | 53.9 ms: 1.38x faster                                                         |
| deepcopy_memo            | 29.6 us                                                         | 22.2 us: 1.34x faster                                                         |
| json_dumps               | 9.82 ms                                                         | 7.41 ms: 1.33x faster                                                         |
| logging_silent           | 97.9 ns                                                         | 74.8 ns: 1.31x faster                                                         |
| comprehensions           | 17.7 us                                                         | 13.6 us: 1.31x faster                                                         |
| raytrace                 | 303 ms                                                          | 234 ms: 1.29x faster                                                          |
| scimark_lu               | 89.8 ms                                                         | 70.5 ms: 1.27x faster                                                         |
| deepcopy                 | 310 us                                                          | 244 us: 1.27x faster                                                          |
| sqlglot_parse            | 1.33 ms                                                         | 1.05 ms: 1.26x faster                                                         |
| tornado_http             | 118 ms                                                          | 95.8 ms: 1.23x faster                                                         |
| sqlglot_transpile        | 1.58 ms                                                         | 1.30 ms: 1.22x faster                                                         |
| pycparser                | 1.04 sec                                                        | 865 ms: 1.20x faster                                                          |
| hexiom                   | 6.13 ms                                                         | 5.10 ms: 1.20x faster                                                         |
| thrift                   | 902 us                                                          | 753 us: 1.20x faster                                                          |
| generators               | 31.6 ms                                                         | 26.6 ms: 1.19x faster                                                         |
| pyflate                  | 422 ms                                                          | 356 ms: 1.19x faster                                                          |
| nqueens                  | 87.1 ms                                                         | 73.8 ms: 1.18x faster                                                         |
| sqlite_synth             | 2.29 us                                                         | 1.97 us: 1.16x faster                                                         |
| dulwich_log              | 58.5 ms                                                         | 50.6 ms: 1.16x faster                                                         |
| sympy_sum                | 122 ms                                                          | 107 ms: 1.15x faster                                                          |
| asyncio_tcp              | 744 ms                                                          | 648 ms: 1.15x faster                                                          |
| json                     | 4.76 ms                                                         | 4.16 ms: 1.14x faster                                                         |
| scimark_sor              | 115 ms                                                          | 101 ms: 1.14x faster                                                          |
| mako                     | 9.10 ms                                                         | 7.98 ms: 1.14x faster                                                         |
| float                    | 69.6 ms                                                         | 61.4 ms: 1.13x faster                                                         |
| richards_super           | 49.9 ms                                                         | 44.3 ms: 1.13x faster                                                         |
| regex_dna                | 131 ms                                                          | 116 ms: 1.12x faster                                                          |
| html5lib                 | 52.1 ms                                                         | 46.5 ms: 1.12x faster                                                         |
| xml_etree_parse          | 120 ms                                                          | 108 ms: 1.11x faster                                                          |
| django_template          | 36.0 ms                                                         | 32.5 ms: 1.11x faster                                                         |
| sympy_integrate          | 16.6 ms                                                         | 15.1 ms: 1.10x faster                                                         |
| pickle_pure_python       | 280 us                                                          | 256 us: 1.10x faster                                                          |
| bench_thread_pool        | 1.12 ms                                                         | 1.02 ms: 1.09x faster                                                         |
| regex_compile            | 117 ms                                                          | 107 ms: 1.09x faster                                                          |
| json_loads               | 22.4 us                                                         | 20.8 us: 1.08x faster                                                         |
| scimark_monte_carlo      | 61.9 ms                                                         | 57.6 ms: 1.08x faster                                                         |
| sympy_str                | 229 ms                                                          | 213 ms: 1.07x faster                                                          |
| unpickle_pure_python     | 189 us                                                          | 178 us: 1.06x faster                                                          |
| 2to3                     | 265 ms                                                          | 250 ms: 1.06x faster                                                          |
| deepcopy_reduce          | 2.68 us                                                         | 2.54 us: 1.06x faster                                                         |
| sqlglot_optimize         | 44.7 ms                                                         | 42.5 ms: 1.05x faster                                                         |
| docutils                 | 1.95 sec                                                        | 1.86 sec: 1.05x faster                                                        |
| xml_etree_iterparse      | 70.8 ms                                                         | 67.8 ms: 1.05x faster                                                         |
| sqlglot_normalize        | 230 ms                                                          | 221 ms: 1.04x faster                                                          |
| mdp                      | 1.83 sec                                                        | 1.75 sec: 1.04x faster                                                        |
| richards                 | 40.3 ms                                                         | 38.8 ms: 1.04x faster                                                         |
| sympy_expand             | 391 ms                                                          | 377 ms: 1.04x faster                                                          |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 3.13 ms: 1.04x faster                                                         |
| spectral_norm            | 80.2 ms                                                         | 77.7 ms: 1.03x faster                                                         |
| tomli_loads              | 1.91 sec                                                        | 1.90 sec: 1.01x faster                                                        |
| pprint_pformat           | 1.37 sec                                                        | 1.36 sec: 1.01x faster                                                        |
| meteor_contest           | 80.0 ms                                                         | 79.8 ms: 1.00x faster                                                         |
| pprint_safe_repr         | 658 ms                                                          | 662 ms: 1.01x slower                                                          |
| genshi_xml               | 46.6 ms                                                         | 46.9 ms: 1.01x slower                                                         |
| xml_etree_process        | 48.1 ms                                                         | 48.6 ms: 1.01x slower                                                         |
| fannkuch                 | 317 ms                                                          | 322 ms: 1.01x slower                                                          |
| pathlib                  | 81.2 ms                                                         | 82.5 ms: 1.02x slower                                                         |
| pickle                   | 7.83 us                                                         | 7.96 us: 1.02x slower                                                         |
| python_startup           | 22.9 ms                                                         | 23.5 ms: 1.02x slower                                                         |
| coroutines               | 17.9 ms                                                         | 18.5 ms: 1.03x slower                                                         |
| regex_v8                 | 15.8 ms                                                         | 16.3 ms: 1.03x slower                                                         |
| unpickle_list            | 2.98 us                                                         | 3.08 us: 1.03x slower                                                         |
| genshi_text              | 21.0 ms                                                         | 21.8 ms: 1.04x slower                                                         |
| create_gc_cycles         | 694 us                                                          | 734 us: 1.06x slower                                                          |
| bench_mp_pool            | 66.4 ms                                                         | 70.1 ms: 1.06x slower                                                         |
| unpickle                 | 9.82 us                                                         | 10.4 us: 1.06x slower                                                         |
| python_startup_no_site   | 18.1 ms                                                         | 19.4 ms: 1.07x slower                                                         |
| xml_etree_generate       | 61.6 ms                                                         | 66.8 ms: 1.08x slower                                                         |
| pickle_list              | 3.22 us                                                         | 3.50 us: 1.09x slower                                                         |
| logging_format           | 7.91 us                                                         | 8.66 us: 1.09x slower                                                         |
| logging_simple           | 7.29 us                                                         | 7.99 us: 1.10x slower                                                         |
| gc_traversal             | 1.28 ms                                                         | 1.41 ms: 1.10x slower                                                         |
| coverage                 | 46.6 ms                                                         | 51.9 ms: 1.11x slower                                                         |
| pickle_dict              | 18.2 us                                                         | 20.5 us: 1.12x slower                                                         |
| regex_effbot             | 1.66 ms                                                         | 1.89 ms: 1.14x slower                                                         |
| scimark_fft              | 216 ms                                                          | 246 ms: 1.14x slower                                                          |
| nbody                    | 79.1 ms                                                         | 91.6 ms: 1.16x slower                                                         |
| unpack_sequence          | 40.0 ns                                                         | 46.7 ns: 1.17x slower                                                         |
| async_generators         | 241 ms                                                          | 297 ms: 1.23x slower                                                          |
| telco                    | 4.83 ms                                                         | 6.34 ms: 1.31x slower                                                         |
| Geometric mean           | (ref)                                                           | 1.12x faster                                                                  |

Benchmark hidden because not significant (1): asyncio_tcp_ssl
Ignored benchmarks (7) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (4) of results/bm-20240911-3.14.0a0-76aa43c/bm-20240911-pythonperf1_win32-x86-mdboom-unicode_check_exact-3.14.0a0-76aa43c.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: unknown
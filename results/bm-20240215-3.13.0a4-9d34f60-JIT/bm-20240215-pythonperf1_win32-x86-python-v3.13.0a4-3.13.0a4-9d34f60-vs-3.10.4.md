# Results vs. 3.10.4

- fork: python
- ref: v3.13.0a4
- machine: windows-x86
- commit hash: 9d34f60
- commit date: 2024-02-15
- overall geometric mean: 1.09x faster \*
- HPT reliability: 99.97%
- HPT 99th percentile: 1.02x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240215-pythonperf1_win32-x86-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 256 ms: 1.04x faster                                                |
| chameleon      | 6.42 ms                                                         | 6.01 ms: 1.07x faster                                               |
| docutils       | 1.95 sec                                                        | 1.82 sec: 1.07x faster                                              |
| tornado_http   | 118 ms                                                          | 99.9 ms: 1.18x faster                                               |
| Geometric mean | (ref)                                                           | 1.09x faster                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240215-pythonperf1_win32-x86-python-v3.13.0a4-3.13.0a4-9d34f60 |
|-------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 922 ms                                                          | 515 ms: 1.79x faster                                                |
| async_tree_none         | 394 ms                                                          | 260 ms: 1.52x faster                                                |
| async_tree_io           | 940 ms                                                          | 624 ms: 1.51x faster                                                |
| async_tree_memoization  | 467 ms                                                          | 325 ms: 1.44x faster                                                |
| Geometric mean          | (ref)                                                           | 1.56x faster                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240215-pythonperf1_win32-x86-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 202 ms: 2.49x faster                                                |
| float          | 69.6 ms                                                         | 53.9 ms: 1.29x faster                                               |
| nbody          | 79.1 ms                                                         | 89.7 ms: 1.13x slower                                               |
| Geometric mean | (ref)                                                           | 1.42x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240215-pythonperf1_win32-x86-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_dna      | 131 ms                                                          | 120 ms: 1.09x faster                                                |
| regex_compile  | 117 ms                                                          | 110 ms: 1.06x faster                                                |
| regex_v8       | 15.8 ms                                                         | 16.2 ms: 1.03x slower                                               |
| regex_effbot   | 1.66 ms                                                         | 1.91 ms: 1.15x slower                                               |
| Geometric mean | (ref)                                                           | 1.01x slower                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240215-pythonperf1_win32-x86-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| json_dumps           | 9.82 ms                                                         | 6.95 ms: 1.41x faster                                               |
| pickle_pure_python   | 280 us                                                          | 223 us: 1.26x faster                                                |
| unpickle_pure_python | 189 us                                                          | 156 us: 1.22x faster                                                |
| tomli_loads          | 1.91 sec                                                        | 1.65 sec: 1.16x faster                                              |
| xml_etree_process    | 48.1 ms                                                         | 42.8 ms: 1.12x faster                                               |
| json_loads           | 22.4 us                                                         | 20.3 us: 1.10x faster                                               |
| xml_etree_parse      | 120 ms                                                          | 109 ms: 1.10x faster                                                |
| xml_etree_iterparse  | 70.8 ms                                                         | 65.9 ms: 1.07x faster                                               |
| unpickle_list        | 2.98 us                                                         | 2.87 us: 1.04x faster                                               |
| xml_etree_generate   | 61.6 ms                                                         | 60.2 ms: 1.02x faster                                               |
| unpickle             | 9.82 us                                                         | 10.1 us: 1.03x slower                                               |
| pickle               | 7.83 us                                                         | 8.11 us: 1.04x slower                                               |
| pickle_list          | 3.22 us                                                         | 3.35 us: 1.04x slower                                               |
| pickle_dict          | 18.2 us                                                         | 19.9 us: 1.09x slower                                               |
| Geometric mean       | (ref)                                                           | 1.09x faster                                                        |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240215-pythonperf1_win32-x86-python-v3.13.0a4-3.13.0a4-9d34f60 |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 22.9 ms                                                         | 22.5 ms: 1.02x faster                                               |
| python_startup_no_site | 18.1 ms                                                         | 20.3 ms: 1.13x slower                                               |
| Geometric mean         | (ref)                                                           | 1.05x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240215-pythonperf1_win32-x86-python-v3.13.0a4-3.13.0a4-9d34f60 |
|-----------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| mako      | 9.10 ms                                                         | 7.43 ms: 1.23x faster                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240215-pythonperf1_win32-x86-python-v3.13.0a4-3.13.0a4-9d34f60 |
|--------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| typing_runtime_protocols | 396 us                                                          | 98.7 us: 4.01x faster                                               |
| pidigits                 | 502 ms                                                          | 202 ms: 2.49x faster                                                |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 515 ms: 1.79x faster                                                |
| deltablue                | 4.04 ms                                                         | 2.58 ms: 1.56x faster                                               |
| async_tree_none          | 394 ms                                                          | 260 ms: 1.52x faster                                                |
| async_tree_io            | 940 ms                                                          | 624 ms: 1.51x faster                                                |
| logging_silent           | 97.9 ns                                                         | 67.1 ns: 1.46x faster                                               |
| async_tree_memoization   | 467 ms                                                          | 325 ms: 1.44x faster                                                |
| json_dumps               | 9.82 ms                                                         | 6.95 ms: 1.41x faster                                               |
| sqlglot_parse            | 1.33 ms                                                         | 961 us: 1.38x faster                                                |
| scimark_lu               | 89.8 ms                                                         | 65.6 ms: 1.37x faster                                               |
| richards_super           | 49.9 ms                                                         | 36.5 ms: 1.37x faster                                               |
| crypto_pyaes             | 81.3 ms                                                         | 61.0 ms: 1.33x faster                                               |
| sqlglot_transpile        | 1.58 ms                                                         | 1.21 ms: 1.31x faster                                               |
| float                    | 69.6 ms                                                         | 53.9 ms: 1.29x faster                                               |
| scimark_sor              | 115 ms                                                          | 89.6 ms: 1.28x faster                                               |
| generators               | 31.6 ms                                                         | 24.6 ms: 1.28x faster                                               |
| raytrace                 | 303 ms                                                          | 240 ms: 1.26x faster                                                |
| comprehensions           | 17.7 us                                                         | 14.1 us: 1.26x faster                                               |
| pickle_pure_python       | 280 us                                                          | 223 us: 1.26x faster                                                |
| richards                 | 40.3 ms                                                         | 32.2 ms: 1.25x faster                                               |
| sqlite_synth             | 2.29 us                                                         | 1.85 us: 1.24x faster                                               |
| mako                     | 9.10 ms                                                         | 7.43 ms: 1.23x faster                                               |
| chaos                    | 74.4 ms                                                         | 61.0 ms: 1.22x faster                                               |
| unpickle_pure_python     | 189 us                                                          | 156 us: 1.22x faster                                                |
| coroutines               | 17.9 ms                                                         | 14.9 ms: 1.20x faster                                               |
| go                       | 146 ms                                                          | 123 ms: 1.19x faster                                                |
| asyncio_tcp              | 744 ms                                                          | 632 ms: 1.18x faster                                                |
| tornado_http             | 118 ms                                                          | 99.9 ms: 1.18x faster                                               |
| pycparser                | 1.04 sec                                                        | 891 ms: 1.17x faster                                                |
| deepcopy_memo            | 29.6 us                                                         | 25.3 us: 1.17x faster                                               |
| tomli_loads              | 1.91 sec                                                        | 1.65 sec: 1.16x faster                                              |
| pyflate                  | 422 ms                                                          | 370 ms: 1.14x faster                                                |
| xml_etree_process        | 48.1 ms                                                         | 42.8 ms: 1.12x faster                                               |
| json                     | 4.76 ms                                                         | 4.27 ms: 1.12x faster                                               |
| sympy_sum                | 122 ms                                                          | 110 ms: 1.11x faster                                                |
| json_loads               | 22.4 us                                                         | 20.3 us: 1.10x faster                                               |
| xml_etree_parse          | 120 ms                                                          | 109 ms: 1.10x faster                                                |
| bench_thread_pool        | 1.12 ms                                                         | 1.02 ms: 1.10x faster                                               |
| spectral_norm            | 80.2 ms                                                         | 73.2 ms: 1.10x faster                                               |
| regex_dna                | 131 ms                                                          | 120 ms: 1.09x faster                                                |
| deepcopy                 | 310 us                                                          | 285 us: 1.09x faster                                                |
| create_gc_cycles         | 694 us                                                          | 646 us: 1.07x faster                                                |
| xml_etree_iterparse      | 70.8 ms                                                         | 65.9 ms: 1.07x faster                                               |
| docutils                 | 1.95 sec                                                        | 1.82 sec: 1.07x faster                                              |
| deepcopy_reduce          | 2.68 us                                                         | 2.51 us: 1.07x faster                                               |
| chameleon                | 6.42 ms                                                         | 6.01 ms: 1.07x faster                                               |
| regex_compile            | 117 ms                                                          | 110 ms: 1.06x faster                                                |
| sympy_str                | 229 ms                                                          | 218 ms: 1.05x faster                                                |
| sympy_integrate          | 16.6 ms                                                         | 16.0 ms: 1.04x faster                                               |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 3.12 ms: 1.04x faster                                               |
| unpickle_list            | 2.98 us                                                         | 2.87 us: 1.04x faster                                               |
| 2to3                     | 265 ms                                                          | 256 ms: 1.04x faster                                                |
| sqlglot_normalize        | 230 ms                                                          | 224 ms: 1.03x faster                                                |
| sympy_expand             | 391 ms                                                          | 379 ms: 1.03x faster                                                |
| xml_etree_generate       | 61.6 ms                                                         | 60.2 ms: 1.02x faster                                               |
| sqlglot_optimize         | 44.7 ms                                                         | 43.7 ms: 1.02x faster                                               |
| python_startup           | 22.9 ms                                                         | 22.5 ms: 1.02x faster                                               |
| asyncio_tcp_ssl          | 17.0 sec                                                        | 16.7 sec: 1.01x faster                                              |
| mdp                      | 1.83 sec                                                        | 1.85 sec: 1.01x slower                                              |
| fannkuch                 | 317 ms                                                          | 322 ms: 1.01x slower                                                |
| nqueens                  | 87.1 ms                                                         | 88.7 ms: 1.02x slower                                               |
| regex_v8                 | 15.8 ms                                                         | 16.2 ms: 1.03x slower                                               |
| unpickle                 | 9.82 us                                                         | 10.1 us: 1.03x slower                                               |
| pickle                   | 7.83 us                                                         | 8.11 us: 1.04x slower                                               |
| pathlib                  | 81.2 ms                                                         | 84.3 ms: 1.04x slower                                               |
| pickle_list              | 3.22 us                                                         | 3.35 us: 1.04x slower                                               |
| meteor_contest           | 80.0 ms                                                         | 83.8 ms: 1.05x slower                                               |
| unpack_sequence          | 40.0 ns                                                         | 42.6 ns: 1.06x slower                                               |
| hexiom                   | 6.13 ms                                                         | 6.61 ms: 1.08x slower                                               |
| pprint_pformat           | 1.37 sec                                                        | 1.47 sec: 1.08x slower                                              |
| bench_mp_pool            | 66.4 ms                                                         | 71.5 ms: 1.08x slower                                               |
| pprint_safe_repr         | 658 ms                                                          | 713 ms: 1.08x slower                                                |
| pickle_dict              | 18.2 us                                                         | 19.9 us: 1.09x slower                                               |
| scimark_fft              | 216 ms                                                          | 239 ms: 1.10x slower                                                |
| gc_traversal             | 1.28 ms                                                         | 1.42 ms: 1.10x slower                                               |
| python_startup_no_site   | 18.1 ms                                                         | 20.3 ms: 1.13x slower                                               |
| nbody                    | 79.1 ms                                                         | 89.7 ms: 1.13x slower                                               |
| logging_format           | 7.91 us                                                         | 8.97 us: 1.13x slower                                               |
| logging_simple           | 7.29 us                                                         | 8.35 us: 1.15x slower                                               |
| regex_effbot             | 1.66 ms                                                         | 1.91 ms: 1.15x slower                                               |
| scimark_monte_carlo      | 61.9 ms                                                         | 71.6 ms: 1.16x slower                                               |
| async_generators         | 241 ms                                                          | 300 ms: 1.24x slower                                                |
| dask                     | 341 ms                                                          | 432 ms: 1.27x slower                                                |
| telco                    | 4.83 ms                                                         | 6.55 ms: 1.36x slower                                               |
| coverage                 | 46.6 ms                                                         | 464 ms: 9.98x slower                                                |
| Geometric mean           | (ref)                                                           | 1.09x faster                                                        |
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, django_template, dulwich_log, flaskblogging, genshi_text, genshi_xml, html5lib, mypy2, pylint, sqlalchemy_declarative, sqlalchemy_imperative, thrift
Ignored benchmarks (4) of results/bm-20240215-3.13.0a4-9d34f60-JIT/bm-20240215-pythonperf1_win32-x86-python-v3.13.0a4-3.13.0a4-9d34f60.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg


# HPT report

- Reliability score: 99.97% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.02x


# Memory

- memory change: unknown
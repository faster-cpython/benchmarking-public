
# Results vs. 3.10.4

- fork: python
- ref: 9c4347ef8b60f54dd357
- machine: windows-x86
- commit hash: 9c4347e
- commit date: 2023-11-22
- overall geometric mean: 1.04x faster
- HPT reliability: 92.39%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20231122-pythonperf1_win32-x86-python-9c4347ef8b60f54dd357-3.13.0a2-9c4347e |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 268 ms: 1.01x slower                                                           |
| chameleon      | 6.42 ms                                                         | 6.15 ms: 1.04x faster                                                          |
| docutils       | 1.95 sec                                                        | 1.94 sec: 1.00x faster                                                         |
| tornado_http   | 118 ms                                                          | 112 ms: 1.05x faster                                                           |
| Geometric mean | (ref)                                                           | 1.02x faster                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20231122-pythonperf1_win32-x86-python-9c4347ef8b60f54dd357-3.13.0a2-9c4347e |
|-------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 922 ms                                                          | 523 ms: 1.76x faster                                                           |
| async_tree_none         | 394 ms                                                          | 270 ms: 1.46x faster                                                           |
| async_tree_io           | 940 ms                                                          | 651 ms: 1.44x faster                                                           |
| async_tree_memoization  | 467 ms                                                          | 329 ms: 1.42x faster                                                           |
| Geometric mean          | (ref)                                                           | 1.52x faster                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20231122-pythonperf1_win32-x86-python-9c4347ef8b60f54dd357-3.13.0a2-9c4347e |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 198 ms: 2.53x faster                                                           |
| float          | 69.6 ms                                                         | 62.3 ms: 1.12x faster                                                          |
| nbody          | 79.1 ms                                                         | 91.9 ms: 1.16x slower                                                          |
| Geometric mean | (ref)                                                           | 1.35x faster                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20231122-pythonperf1_win32-x86-python-9c4347ef8b60f54dd357-3.13.0a2-9c4347e |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_dna      | 131 ms                                                          | 132 ms: 1.01x slower                                                           |
| regex_v8       | 15.8 ms                                                         | 16.3 ms: 1.04x slower                                                          |
| regex_compile  | 117 ms                                                          | 131 ms: 1.13x slower                                                           |
| regex_effbot   | 1.66 ms                                                         | 2.01 ms: 1.21x slower                                                          |
| Geometric mean | (ref)                                                           | 1.09x slower                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20231122-pythonperf1_win32-x86-python-9c4347ef8b60f54dd357-3.13.0a2-9c4347e |
|----------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| json_dumps           | 9.82 ms                                                         | 7.11 ms: 1.38x faster                                                          |
| pickle_pure_python   | 280 us                                                          | 235 us: 1.19x faster                                                           |
| json_loads           | 22.4 us                                                         | 19.9 us: 1.12x faster                                                          |
| unpickle_list        | 2.98 us                                                         | 2.69 us: 1.11x faster                                                          |
| unpickle_pure_python | 189 us                                                          | 173 us: 1.09x faster                                                           |
| xml_etree_parse      | 120 ms                                                          | 111 ms: 1.08x faster                                                           |
| tomli_loads          | 1.91 sec                                                        | 1.79 sec: 1.06x faster                                                         |
| pickle               | 7.83 us                                                         | 7.66 us: 1.02x faster                                                          |
| unpickle             | 9.82 us                                                         | 9.65 us: 1.02x faster                                                          |
| xml_etree_process    | 48.1 ms                                                         | 47.9 ms: 1.00x faster                                                          |
| xml_etree_iterparse  | 70.8 ms                                                         | 71.7 ms: 1.01x slower                                                          |
| pickle_dict          | 18.2 us                                                         | 19.7 us: 1.08x slower                                                          |
| xml_etree_generate   | 61.6 ms                                                         | 67.3 ms: 1.09x slower                                                          |
| Geometric mean       | (ref)                                                           | 1.06x faster                                                                   |

Benchmark hidden because not significant (1): pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20231122-pythonperf1_win32-x86-python-9c4347ef8b60f54dd357-3.13.0a2-9c4347e |
|------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup         | 22.9 ms                                                         | 23.3 ms: 1.01x slower                                                          |
| python_startup_no_site | 18.1 ms                                                         | 21.2 ms: 1.17x slower                                                          |
| Geometric mean         | (ref)                                                           | 1.09x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20231122-pythonperf1_win32-x86-python-9c4347ef8b60f54dd357-3.13.0a2-9c4347e |
|-----------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako      | 9.10 ms                                                         | 8.20 ms: 1.11x faster                                                          |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20231122-pythonperf1_win32-x86-python-9c4347ef8b60f54dd357-3.13.0a2-9c4347e |
|--------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| typing_runtime_protocols | 396 us                                                          | 105 us: 3.77x faster                                                           |
| pidigits                 | 502 ms                                                          | 198 ms: 2.53x faster                                                           |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 523 ms: 1.76x faster                                                           |
| async_tree_none          | 394 ms                                                          | 270 ms: 1.46x faster                                                           |
| async_tree_io            | 940 ms                                                          | 651 ms: 1.44x faster                                                           |
| async_tree_memoization   | 467 ms                                                          | 329 ms: 1.42x faster                                                           |
| crypto_pyaes             | 81.3 ms                                                         | 58.8 ms: 1.38x faster                                                          |
| json_dumps               | 9.82 ms                                                         | 7.11 ms: 1.38x faster                                                          |
| deltablue                | 4.04 ms                                                         | 3.08 ms: 1.31x faster                                                          |
| chaos                    | 74.4 ms                                                         | 57.2 ms: 1.30x faster                                                          |
| logging_silent           | 97.9 ns                                                         | 76.8 ns: 1.27x faster                                                          |
| sqlglot_parse            | 1.33 ms                                                         | 1.06 ms: 1.25x faster                                                          |
| richards_super           | 49.9 ms                                                         | 40.6 ms: 1.23x faster                                                          |
| sqlite_synth             | 2.29 us                                                         | 1.87 us: 1.23x faster                                                          |
| go                       | 146 ms                                                          | 121 ms: 1.20x faster                                                           |
| pickle_pure_python       | 280 us                                                          | 235 us: 1.19x faster                                                           |
| sqlglot_transpile        | 1.58 ms                                                         | 1.33 ms: 1.19x faster                                                          |
| raytrace                 | 303 ms                                                          | 257 ms: 1.18x faster                                                           |
| json                     | 4.76 ms                                                         | 4.12 ms: 1.16x faster                                                          |
| pyflate                  | 422 ms                                                          | 367 ms: 1.15x faster                                                           |
| scimark_lu               | 89.8 ms                                                         | 79.2 ms: 1.13x faster                                                          |
| asyncio_tcp              | 744 ms                                                          | 658 ms: 1.13x faster                                                           |
| comprehensions           | 17.7 us                                                         | 15.7 us: 1.13x faster                                                          |
| richards                 | 40.3 ms                                                         | 35.6 ms: 1.13x faster                                                          |
| scimark_sor              | 115 ms                                                          | 102 ms: 1.13x faster                                                           |
| json_loads               | 22.4 us                                                         | 19.9 us: 1.12x faster                                                          |
| float                    | 69.6 ms                                                         | 62.3 ms: 1.12x faster                                                          |
| mako                     | 9.10 ms                                                         | 8.20 ms: 1.11x faster                                                          |
| unpickle_list            | 2.98 us                                                         | 2.69 us: 1.11x faster                                                          |
| unpickle_pure_python     | 189 us                                                          | 173 us: 1.09x faster                                                           |
| pycparser                | 1.04 sec                                                        | 955 ms: 1.09x faster                                                           |
| xml_etree_parse          | 120 ms                                                          | 111 ms: 1.08x faster                                                           |
| scimark_monte_carlo      | 61.9 ms                                                         | 57.8 ms: 1.07x faster                                                          |
| create_gc_cycles         | 694 us                                                          | 648 us: 1.07x faster                                                           |
| generators               | 31.6 ms                                                         | 29.6 ms: 1.07x faster                                                          |
| deepcopy_memo            | 29.6 us                                                         | 27.8 us: 1.07x faster                                                          |
| tomli_loads              | 1.91 sec                                                        | 1.79 sec: 1.06x faster                                                         |
| tornado_http             | 118 ms                                                          | 112 ms: 1.05x faster                                                           |
| chameleon                | 6.42 ms                                                         | 6.15 ms: 1.04x faster                                                          |
| dask                     | 341 ms                                                          | 328 ms: 1.04x faster                                                           |
| pprint_pformat           | 1.37 sec                                                        | 1.33 sec: 1.03x faster                                                         |
| bench_thread_pool        | 1.12 ms                                                         | 1.09 ms: 1.02x faster                                                          |
| pickle                   | 7.83 us                                                         | 7.66 us: 1.02x faster                                                          |
| deepcopy_reduce          | 2.68 us                                                         | 2.64 us: 1.02x faster                                                          |
| unpickle                 | 9.82 us                                                         | 9.65 us: 1.02x faster                                                          |
| pprint_safe_repr         | 658 ms                                                          | 649 ms: 1.01x faster                                                           |
| mdp                      | 1.83 sec                                                        | 1.81 sec: 1.01x faster                                                         |
| xml_etree_process        | 48.1 ms                                                         | 47.9 ms: 1.00x faster                                                          |
| docutils                 | 1.95 sec                                                        | 1.94 sec: 1.00x faster                                                         |
| sympy_sum                | 122 ms                                                          | 123 ms: 1.01x slower                                                           |
| regex_dna                | 131 ms                                                          | 132 ms: 1.01x slower                                                           |
| 2to3                     | 265 ms                                                          | 268 ms: 1.01x slower                                                           |
| fannkuch                 | 317 ms                                                          | 321 ms: 1.01x slower                                                           |
| xml_etree_iterparse      | 70.8 ms                                                         | 71.7 ms: 1.01x slower                                                          |
| python_startup           | 22.9 ms                                                         | 23.3 ms: 1.01x slower                                                          |
| hexiom                   | 6.13 ms                                                         | 6.24 ms: 1.02x slower                                                          |
| coroutines               | 17.9 ms                                                         | 18.3 ms: 1.02x slower                                                          |
| asyncio_tcp_ssl          | 17.0 sec                                                        | 17.4 sec: 1.02x slower                                                         |
| sqlglot_normalize        | 230 ms                                                          | 237 ms: 1.03x slower                                                           |
| regex_v8                 | 15.8 ms                                                         | 16.3 ms: 1.04x slower                                                          |
| meteor_contest           | 80.0 ms                                                         | 83.2 ms: 1.04x slower                                                          |
| sympy_expand             | 391 ms                                                          | 408 ms: 1.05x slower                                                           |
| sqlglot_optimize         | 44.7 ms                                                         | 46.8 ms: 1.05x slower                                                          |
| sympy_integrate          | 16.6 ms                                                         | 17.4 ms: 1.05x slower                                                          |
| nqueens                  | 87.1 ms                                                         | 91.2 ms: 1.05x slower                                                          |
| sympy_str                | 229 ms                                                          | 241 ms: 1.05x slower                                                           |
| unpack_sequence          | 40.0 ns                                                         | 42.6 ns: 1.06x slower                                                          |
| pickle_dict              | 18.2 us                                                         | 19.7 us: 1.08x slower                                                          |
| xml_etree_generate       | 61.6 ms                                                         | 67.3 ms: 1.09x slower                                                          |
| gc_traversal             | 1.28 ms                                                         | 1.40 ms: 1.09x slower                                                          |
| pathlib                  | 81.2 ms                                                         | 89.1 ms: 1.10x slower                                                          |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 3.63 ms: 1.12x slower                                                          |
| scimark_fft              | 216 ms                                                          | 243 ms: 1.12x slower                                                           |
| regex_compile            | 117 ms                                                          | 131 ms: 1.13x slower                                                           |
| bench_mp_pool            | 66.4 ms                                                         | 75.2 ms: 1.13x slower                                                          |
| logging_format           | 7.91 us                                                         | 9.15 us: 1.16x slower                                                          |
| nbody                    | 79.1 ms                                                         | 91.9 ms: 1.16x slower                                                          |
| python_startup_no_site   | 18.1 ms                                                         | 21.2 ms: 1.17x slower                                                          |
| logging_simple           | 7.29 us                                                         | 8.58 us: 1.18x slower                                                          |
| spectral_norm            | 80.2 ms                                                         | 96.9 ms: 1.21x slower                                                          |
| regex_effbot             | 1.66 ms                                                         | 2.01 ms: 1.21x slower                                                          |
| async_generators         | 241 ms                                                          | 304 ms: 1.26x slower                                                           |
| telco                    | 4.83 ms                                                         | 6.40 ms: 1.32x slower                                                          |
| coverage                 | 46.6 ms                                                         | 510 ms: 10.95x slower                                                          |
| Geometric mean           | (ref)                                                           | 1.04x faster                                                                   |

Benchmark hidden because not significant (2): pickle_list, deepcopy
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, django_template, dulwich_log, flaskblogging, genshi_text, genshi_xml, html5lib, mypy2, pylint, sqlalchemy_declarative, sqlalchemy_imperative, thrift
Ignored benchmarks (4) of results/bm-20231122-3.13.0a2-9c4347e-PYTHON_UOPS/bm-20231122-pythonperf1_win32-x86-python-9c4347ef8b60f54dd357-3.13.0a2-9c4347e.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg


# HPT report

- Reliability score: 92.39% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x


# Memory

- memory change: unknown
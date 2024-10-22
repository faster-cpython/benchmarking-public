# Results vs. 3.10.4

- fork: python
- ref: 006b53a42f72be83ecdf
- machine: windows-x86
- commit hash: 006b53a
- commit date: 2024-07-08
- overall geometric mean: 1.22x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.11x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240708-pythonperf1_win32-x86-python-006b53a42f72be83ecdf-3.14.0a0-006b53a |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 252 ms: 1.05x faster                                                           |
| docutils       | 1.95 sec                                                        | 1.93 sec: 1.01x faster                                                         |
| html5lib       | 52.1 ms                                                         | 46.8 ms: 1.11x faster                                                          |
| tornado_http   | 118 ms                                                          | 98.3 ms: 1.20x faster                                                          |
| Geometric mean | (ref)                                                           | 1.09x faster                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240708-pythonperf1_win32-x86-python-006b53a42f72be83ecdf-3.14.0a0-006b53a |
|-------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 922 ms                                                          | 470 ms: 1.96x faster                                                           |
| async_tree_none         | 394 ms                                                          | 219 ms: 1.80x faster                                                           |
| async_tree_io           | 940 ms                                                          | 539 ms: 1.74x faster                                                           |
| async_tree_memoization  | 467 ms                                                          | 272 ms: 1.72x faster                                                           |
| Geometric mean          | (ref)                                                           | 1.80x faster                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240708-pythonperf1_win32-x86-python-006b53a42f72be83ecdf-3.14.0a0-006b53a |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 195 ms: 2.57x faster                                                           |
| float          | 69.6 ms                                                         | 44.1 ms: 1.58x faster                                                          |
| nbody          | 79.1 ms                                                         | 55.7 ms: 1.42x faster                                                          |
| Geometric mean | (ref)                                                           | 1.79x faster                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240708-pythonperf1_win32-x86-python-006b53a42f72be83ecdf-3.14.0a0-006b53a |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_compile  | 117 ms                                                          | 95.0 ms: 1.23x faster                                                          |
| regex_dna      | 131 ms                                                          | 123 ms: 1.06x faster                                                           |
| regex_effbot   | 1.66 ms                                                         | 1.90 ms: 1.14x slower                                                          |
| Geometric mean | (ref)                                                           | 1.03x faster                                                                   |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240708-pythonperf1_win32-x86-python-006b53a42f72be83ecdf-3.14.0a0-006b53a |
|----------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| json_dumps           | 9.82 ms                                                         | 7.14 ms: 1.38x faster                                                          |
| pickle_pure_python   | 280 us                                                          | 212 us: 1.32x faster                                                           |
| tomli_loads          | 1.91 sec                                                        | 1.48 sec: 1.29x faster                                                         |
| unpickle_pure_python | 189 us                                                          | 148 us: 1.28x faster                                                           |
| xml_etree_parse      | 120 ms                                                          | 104 ms: 1.15x faster                                                           |
| xml_etree_iterparse  | 70.8 ms                                                         | 61.8 ms: 1.15x faster                                                          |
| xml_etree_process    | 48.1 ms                                                         | 44.0 ms: 1.09x faster                                                          |
| json_loads           | 22.4 us                                                         | 21.3 us: 1.05x faster                                                          |
| xml_etree_generate   | 61.6 ms                                                         | 60.9 ms: 1.01x faster                                                          |
| Geometric mean       | (ref)                                                           | 1.18x faster                                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240708-pythonperf1_win32-x86-python-006b53a42f72be83ecdf-3.14.0a0-006b53a |
|------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup         | 22.9 ms                                                         | 23.2 ms: 1.01x slower                                                          |
| python_startup_no_site | 18.1 ms                                                         | 19.3 ms: 1.07x slower                                                          |
| Geometric mean         | (ref)                                                           | 1.04x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240708-pythonperf1_win32-x86-python-006b53a42f72be83ecdf-3.14.0a0-006b53a |
|-----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako            | 9.10 ms                                                         | 5.44 ms: 1.67x faster                                                          |
| django_template | 36.0 ms                                                         | 32.6 ms: 1.10x faster                                                          |
| genshi_text     | 21.0 ms                                                         | 22.8 ms: 1.09x slower                                                          |
| genshi_xml      | 46.6 ms                                                         | 53.2 ms: 1.14x slower                                                          |
| Geometric mean  | (ref)                                                           | 1.11x faster                                                                   |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240708-pythonperf1_win32-x86-python-006b53a42f72be83ecdf-3.14.0a0-006b53a |
|--------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| typing_runtime_protocols | 396 us                                                          | 145 us: 2.74x faster                                                           |
| pidigits                 | 502 ms                                                          | 195 ms: 2.57x faster                                                           |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 470 ms: 1.96x faster                                                           |
| deepcopy_memo            | 29.6 us                                                         | 15.5 us: 1.91x faster                                                          |
| async_tree_none          | 394 ms                                                          | 219 ms: 1.80x faster                                                           |
| async_tree_io            | 940 ms                                                          | 539 ms: 1.74x faster                                                           |
| async_tree_memoization   | 467 ms                                                          | 272 ms: 1.72x faster                                                           |
| spectral_norm            | 80.2 ms                                                         | 47.3 ms: 1.70x faster                                                          |
| mako                     | 9.10 ms                                                         | 5.44 ms: 1.67x faster                                                          |
| logging_silent           | 97.9 ns                                                         | 58.6 ns: 1.67x faster                                                          |
| crypto_pyaes             | 81.3 ms                                                         | 49.2 ms: 1.65x faster                                                          |
| pylint                   | 384 ms                                                          | 242 ms: 1.58x faster                                                           |
| float                    | 69.6 ms                                                         | 44.1 ms: 1.58x faster                                                          |
| comprehensions           | 17.7 us                                                         | 11.4 us: 1.56x faster                                                          |
| pyflate                  | 422 ms                                                          | 278 ms: 1.51x faster                                                           |
| scimark_monte_carlo      | 61.9 ms                                                         | 41.2 ms: 1.50x faster                                                          |
| deltablue                | 4.04 ms                                                         | 2.73 ms: 1.48x faster                                                          |
| nbody                    | 79.1 ms                                                         | 55.7 ms: 1.42x faster                                                          |
| fannkuch                 | 317 ms                                                          | 226 ms: 1.40x faster                                                           |
| sqlglot_parse            | 1.33 ms                                                         | 958 us: 1.39x faster                                                           |
| chaos                    | 74.4 ms                                                         | 54.0 ms: 1.38x faster                                                          |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 2.36 ms: 1.38x faster                                                          |
| json_dumps               | 9.82 ms                                                         | 7.14 ms: 1.38x faster                                                          |
| hexiom                   | 6.13 ms                                                         | 4.60 ms: 1.33x faster                                                          |
| pickle_pure_python       | 280 us                                                          | 212 us: 1.32x faster                                                           |
| scimark_fft              | 216 ms                                                          | 165 ms: 1.31x faster                                                           |
| sqlglot_transpile        | 1.58 ms                                                         | 1.22 ms: 1.30x faster                                                          |
| go                       | 146 ms                                                          | 112 ms: 1.30x faster                                                           |
| deepcopy                 | 310 us                                                          | 239 us: 1.30x faster                                                           |
| raytrace                 | 303 ms                                                          | 235 ms: 1.29x faster                                                           |
| tomli_loads              | 1.91 sec                                                        | 1.48 sec: 1.29x faster                                                         |
| richards_super           | 49.9 ms                                                         | 38.9 ms: 1.28x faster                                                          |
| unpickle_pure_python     | 189 us                                                          | 148 us: 1.28x faster                                                           |
| richards                 | 40.3 ms                                                         | 32.4 ms: 1.24x faster                                                          |
| pycparser                | 1.04 sec                                                        | 844 ms: 1.23x faster                                                           |
| regex_compile            | 117 ms                                                          | 95.0 ms: 1.23x faster                                                          |
| asyncio_tcp              | 744 ms                                                          | 613 ms: 1.21x faster                                                           |
| thrift                   | 902 us                                                          | 747 us: 1.21x faster                                                           |
| pprint_pformat           | 1.37 sec                                                        | 1.14 sec: 1.20x faster                                                         |
| tornado_http             | 118 ms                                                          | 98.3 ms: 1.20x faster                                                          |
| pprint_safe_repr         | 658 ms                                                          | 552 ms: 1.19x faster                                                           |
| nqueens                  | 87.1 ms                                                         | 73.2 ms: 1.19x faster                                                          |
| xml_etree_parse          | 120 ms                                                          | 104 ms: 1.15x faster                                                           |
| scimark_lu               | 89.8 ms                                                         | 77.9 ms: 1.15x faster                                                          |
| xml_etree_iterparse      | 70.8 ms                                                         | 61.8 ms: 1.15x faster                                                          |
| bench_thread_pool        | 1.12 ms                                                         | 978 us: 1.15x faster                                                           |
| generators               | 31.6 ms                                                         | 27.7 ms: 1.14x faster                                                          |
| json                     | 4.76 ms                                                         | 4.20 ms: 1.13x faster                                                          |
| scimark_sor              | 115 ms                                                          | 102 ms: 1.13x faster                                                           |
| deepcopy_reduce          | 2.68 us                                                         | 2.37 us: 1.13x faster                                                          |
| sympy_sum                | 122 ms                                                          | 109 ms: 1.12x faster                                                           |
| html5lib                 | 52.1 ms                                                         | 46.8 ms: 1.11x faster                                                          |
| django_template          | 36.0 ms                                                         | 32.6 ms: 1.10x faster                                                          |
| mdp                      | 1.83 sec                                                        | 1.66 sec: 1.10x faster                                                         |
| xml_etree_process        | 48.1 ms                                                         | 44.0 ms: 1.09x faster                                                          |
| meteor_contest           | 80.0 ms                                                         | 74.6 ms: 1.07x faster                                                          |
| regex_dna                | 131 ms                                                          | 123 ms: 1.06x faster                                                           |
| 2to3                     | 265 ms                                                          | 252 ms: 1.05x faster                                                           |
| json_loads               | 22.4 us                                                         | 21.3 us: 1.05x faster                                                          |
| sympy_str                | 229 ms                                                          | 219 ms: 1.05x faster                                                           |
| sympy_integrate          | 16.6 ms                                                         | 15.9 ms: 1.05x faster                                                          |
| sqlglot_optimize         | 44.7 ms                                                         | 44.1 ms: 1.01x faster                                                          |
| xml_etree_generate       | 61.6 ms                                                         | 60.9 ms: 1.01x faster                                                          |
| docutils                 | 1.95 sec                                                        | 1.93 sec: 1.01x faster                                                         |
| asyncio_tcp_ssl          | 17.0 sec                                                        | 16.8 sec: 1.01x faster                                                         |
| sympy_expand             | 391 ms                                                          | 392 ms: 1.00x slower                                                           |
| python_startup           | 22.9 ms                                                         | 23.2 ms: 1.01x slower                                                          |
| pathlib                  | 81.2 ms                                                         | 83.3 ms: 1.03x slower                                                          |
| logging_format           | 7.91 us                                                         | 8.13 us: 1.03x slower                                                          |
| logging_simple           | 7.29 us                                                         | 7.55 us: 1.04x slower                                                          |
| sqlglot_normalize        | 230 ms                                                          | 241 ms: 1.04x slower                                                           |
| python_startup_no_site   | 18.1 ms                                                         | 19.3 ms: 1.07x slower                                                          |
| create_gc_cycles         | 694 us                                                          | 751 us: 1.08x slower                                                           |
| genshi_text              | 21.0 ms                                                         | 22.8 ms: 1.09x slower                                                          |
| coverage                 | 46.6 ms                                                         | 51.3 ms: 1.10x slower                                                          |
| bench_mp_pool            | 66.4 ms                                                         | 73.7 ms: 1.11x slower                                                          |
| gc_traversal             | 1.28 ms                                                         | 1.45 ms: 1.13x slower                                                          |
| regex_effbot             | 1.66 ms                                                         | 1.90 ms: 1.14x slower                                                          |
| genshi_xml               | 46.6 ms                                                         | 53.2 ms: 1.14x slower                                                          |
| telco                    | 4.83 ms                                                         | 5.92 ms: 1.22x slower                                                          |
| async_generators         | 241 ms                                                          | 317 ms: 1.31x slower                                                           |
| Geometric mean           | (ref)                                                           | 1.22x faster                                                                   |

Benchmark hidden because not significant (2): coroutines, regex_v8
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, dulwich_log, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (4) of results/bm-20240708-3.14.0a0-006b53a-JIT/bm-20240708-pythonperf1_win32-x86-python-006b53a42f72be83ecdf-3.14.0a0-006b53a.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.15x
- 95% likely to have a speedup of 1.13x
- 99% likely to have a speedup of 1.11x

# Memory
- memory change: unknown
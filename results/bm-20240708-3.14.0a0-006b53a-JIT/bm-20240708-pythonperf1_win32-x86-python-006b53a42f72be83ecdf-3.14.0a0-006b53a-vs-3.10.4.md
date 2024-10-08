# Results vs. 3.10.4

- fork: python
- ref: 006b53a42f72be83ecdf
- machine: windows-x86
- commit hash: 006b53a
- commit date: 2024-07-08
- overall geometric mean: 1.21x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.10x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240708-pythonperf1_win32-x86-python-006b53a42f72be83ecdf-3.14.0a0-006b53a |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 254 ms: 1.04x faster                                                           |
| html5lib       | 52.1 ms                                                         | 46.5 ms: 1.12x faster                                                          |
| tornado_http   | 118 ms                                                          | 98.2 ms: 1.20x faster                                                          |
| Geometric mean | (ref)                                                           | 1.09x faster                                                                   |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240708-pythonperf1_win32-x86-python-006b53a42f72be83ecdf-3.14.0a0-006b53a |
|-------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 922 ms                                                          | 469 ms: 1.97x faster                                                           |
| async_tree_none         | 394 ms                                                          | 217 ms: 1.81x faster                                                           |
| async_tree_io           | 940 ms                                                          | 539 ms: 1.75x faster                                                           |
| async_tree_memoization  | 467 ms                                                          | 268 ms: 1.74x faster                                                           |
| Geometric mean          | (ref)                                                           | 1.81x faster                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240708-pythonperf1_win32-x86-python-006b53a42f72be83ecdf-3.14.0a0-006b53a |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 203 ms: 2.47x faster                                                           |
| float          | 69.6 ms                                                         | 43.0 ms: 1.62x faster                                                          |
| nbody          | 79.1 ms                                                         | 55.2 ms: 1.43x faster                                                          |
| Geometric mean | (ref)                                                           | 1.79x faster                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240708-pythonperf1_win32-x86-python-006b53a42f72be83ecdf-3.14.0a0-006b53a |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_compile  | 117 ms                                                          | 95.5 ms: 1.22x faster                                                          |
| regex_dna      | 131 ms                                                          | 127 ms: 1.03x faster                                                           |
| regex_v8       | 15.8 ms                                                         | 16.1 ms: 1.02x slower                                                          |
| regex_effbot   | 1.66 ms                                                         | 1.91 ms: 1.15x slower                                                          |
| Geometric mean | (ref)                                                           | 1.02x faster                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240708-pythonperf1_win32-x86-python-006b53a42f72be83ecdf-3.14.0a0-006b53a |
|----------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| json_dumps           | 9.82 ms                                                         | 7.25 ms: 1.36x faster                                                          |
| tomli_loads          | 1.91 sec                                                        | 1.48 sec: 1.29x faster                                                         |
| pickle_pure_python   | 280 us                                                          | 218 us: 1.29x faster                                                           |
| unpickle_pure_python | 189 us                                                          | 150 us: 1.26x faster                                                           |
| xml_etree_parse      | 120 ms                                                          | 104 ms: 1.15x faster                                                           |
| xml_etree_iterparse  | 70.8 ms                                                         | 61.8 ms: 1.15x faster                                                          |
| xml_etree_process    | 48.1 ms                                                         | 43.6 ms: 1.10x faster                                                          |
| json_loads           | 22.4 us                                                         | 21.6 us: 1.04x faster                                                          |
| xml_etree_generate   | 61.6 ms                                                         | 59.8 ms: 1.03x faster                                                          |
| Geometric mean       | (ref)                                                           | 1.18x faster                                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240708-pythonperf1_win32-x86-python-006b53a42f72be83ecdf-3.14.0a0-006b53a |
|------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup         | 22.9 ms                                                         | 23.7 ms: 1.03x slower                                                          |
| python_startup_no_site | 18.1 ms                                                         | 20.0 ms: 1.11x slower                                                          |
| Geometric mean         | (ref)                                                           | 1.07x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240708-pythonperf1_win32-x86-python-006b53a42f72be83ecdf-3.14.0a0-006b53a |
|-----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako            | 9.10 ms                                                         | 5.46 ms: 1.67x faster                                                          |
| django_template | 36.0 ms                                                         | 33.7 ms: 1.07x faster                                                          |
| genshi_text     | 21.0 ms                                                         | 23.4 ms: 1.12x slower                                                          |
| genshi_xml      | 46.6 ms                                                         | 53.6 ms: 1.15x slower                                                          |
| Geometric mean  | (ref)                                                           | 1.09x faster                                                                   |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240708-pythonperf1_win32-x86-python-006b53a42f72be83ecdf-3.14.0a0-006b53a |
|--------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| typing_runtime_protocols | 396 us                                                          | 151 us: 2.62x faster                                                           |
| pidigits                 | 502 ms                                                          | 203 ms: 2.47x faster                                                           |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 469 ms: 1.97x faster                                                           |
| deepcopy_memo            | 29.6 us                                                         | 15.8 us: 1.87x faster                                                          |
| async_tree_none          | 394 ms                                                          | 217 ms: 1.81x faster                                                           |
| async_tree_io            | 940 ms                                                          | 539 ms: 1.75x faster                                                           |
| async_tree_memoization   | 467 ms                                                          | 268 ms: 1.74x faster                                                           |
| spectral_norm            | 80.2 ms                                                         | 47.7 ms: 1.68x faster                                                          |
| logging_silent           | 97.9 ns                                                         | 58.5 ns: 1.67x faster                                                          |
| mako                     | 9.10 ms                                                         | 5.46 ms: 1.67x faster                                                          |
| crypto_pyaes             | 81.3 ms                                                         | 48.9 ms: 1.66x faster                                                          |
| float                    | 69.6 ms                                                         | 43.0 ms: 1.62x faster                                                          |
| pylint                   | 384 ms                                                          | 241 ms: 1.59x faster                                                           |
| comprehensions           | 17.7 us                                                         | 11.5 us: 1.54x faster                                                          |
| pyflate                  | 422 ms                                                          | 285 ms: 1.48x faster                                                           |
| scimark_monte_carlo      | 61.9 ms                                                         | 41.9 ms: 1.48x faster                                                          |
| deltablue                | 4.04 ms                                                         | 2.76 ms: 1.46x faster                                                          |
| nbody                    | 79.1 ms                                                         | 55.2 ms: 1.43x faster                                                          |
| chaos                    | 74.4 ms                                                         | 52.4 ms: 1.42x faster                                                          |
| sqlglot_parse            | 1.33 ms                                                         | 949 us: 1.40x faster                                                           |
| fannkuch                 | 317 ms                                                          | 228 ms: 1.39x faster                                                           |
| json_dumps               | 9.82 ms                                                         | 7.25 ms: 1.36x faster                                                          |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 2.41 ms: 1.35x faster                                                          |
| raytrace                 | 303 ms                                                          | 227 ms: 1.33x faster                                                           |
| sqlglot_transpile        | 1.58 ms                                                         | 1.21 ms: 1.31x faster                                                          |
| hexiom                   | 6.13 ms                                                         | 4.69 ms: 1.31x faster                                                          |
| deepcopy                 | 310 us                                                          | 238 us: 1.31x faster                                                           |
| scimark_fft              | 216 ms                                                          | 167 ms: 1.29x faster                                                           |
| go                       | 146 ms                                                          | 113 ms: 1.29x faster                                                           |
| tomli_loads              | 1.91 sec                                                        | 1.48 sec: 1.29x faster                                                         |
| pickle_pure_python       | 280 us                                                          | 218 us: 1.29x faster                                                           |
| unpickle_pure_python     | 189 us                                                          | 150 us: 1.26x faster                                                           |
| pycparser                | 1.04 sec                                                        | 836 ms: 1.25x faster                                                           |
| richards_super           | 49.9 ms                                                         | 40.7 ms: 1.23x faster                                                          |
| regex_compile            | 117 ms                                                          | 95.5 ms: 1.22x faster                                                          |
| richards                 | 40.3 ms                                                         | 33.4 ms: 1.21x faster                                                          |
| tornado_http             | 118 ms                                                          | 98.2 ms: 1.20x faster                                                          |
| pprint_pformat           | 1.37 sec                                                        | 1.16 sec: 1.18x faster                                                         |
| nqueens                  | 87.1 ms                                                         | 74.0 ms: 1.18x faster                                                          |
| asyncio_tcp              | 744 ms                                                          | 635 ms: 1.17x faster                                                           |
| thrift                   | 902 us                                                          | 772 us: 1.17x faster                                                           |
| pprint_safe_repr         | 658 ms                                                          | 565 ms: 1.17x faster                                                           |
| bench_thread_pool        | 1.12 ms                                                         | 970 us: 1.15x faster                                                           |
| xml_etree_parse          | 120 ms                                                          | 104 ms: 1.15x faster                                                           |
| xml_etree_iterparse      | 70.8 ms                                                         | 61.8 ms: 1.15x faster                                                          |
| scimark_sor              | 115 ms                                                          | 101 ms: 1.14x faster                                                           |
| deepcopy_reduce          | 2.68 us                                                         | 2.36 us: 1.14x faster                                                          |
| generators               | 31.6 ms                                                         | 27.9 ms: 1.13x faster                                                          |
| sympy_sum                | 122 ms                                                          | 109 ms: 1.13x faster                                                           |
| scimark_lu               | 89.8 ms                                                         | 79.7 ms: 1.13x faster                                                          |
| html5lib                 | 52.1 ms                                                         | 46.5 ms: 1.12x faster                                                          |
| xml_etree_process        | 48.1 ms                                                         | 43.6 ms: 1.10x faster                                                          |
| mdp                      | 1.83 sec                                                        | 1.66 sec: 1.10x faster                                                         |
| json                     | 4.76 ms                                                         | 4.43 ms: 1.08x faster                                                          |
| django_template          | 36.0 ms                                                         | 33.7 ms: 1.07x faster                                                          |
| sympy_str                | 229 ms                                                          | 217 ms: 1.06x faster                                                           |
| meteor_contest           | 80.0 ms                                                         | 76.3 ms: 1.05x faster                                                          |
| 2to3                     | 265 ms                                                          | 254 ms: 1.04x faster                                                           |
| sympy_integrate          | 16.6 ms                                                         | 16.0 ms: 1.04x faster                                                          |
| json_loads               | 22.4 us                                                         | 21.6 us: 1.04x faster                                                          |
| xml_etree_generate       | 61.6 ms                                                         | 59.8 ms: 1.03x faster                                                          |
| sqlglot_optimize         | 44.7 ms                                                         | 43.5 ms: 1.03x faster                                                          |
| regex_dna                | 131 ms                                                          | 127 ms: 1.03x faster                                                           |
| sympy_expand             | 391 ms                                                          | 386 ms: 1.01x faster                                                           |
| coroutines               | 17.9 ms                                                         | 17.7 ms: 1.01x faster                                                          |
| asyncio_tcp_ssl          | 17.0 sec                                                        | 16.8 sec: 1.01x faster                                                         |
| logging_format           | 7.91 us                                                         | 7.99 us: 1.01x slower                                                          |
| pathlib                  | 81.2 ms                                                         | 82.2 ms: 1.01x slower                                                          |
| sqlglot_normalize        | 230 ms                                                          | 235 ms: 1.02x slower                                                           |
| regex_v8                 | 15.8 ms                                                         | 16.1 ms: 1.02x slower                                                          |
| python_startup           | 22.9 ms                                                         | 23.7 ms: 1.03x slower                                                          |
| create_gc_cycles         | 694 us                                                          | 755 us: 1.09x slower                                                           |
| python_startup_no_site   | 18.1 ms                                                         | 20.0 ms: 1.11x slower                                                          |
| genshi_text              | 21.0 ms                                                         | 23.4 ms: 1.12x slower                                                          |
| coverage                 | 46.6 ms                                                         | 52.1 ms: 1.12x slower                                                          |
| gc_traversal             | 1.28 ms                                                         | 1.44 ms: 1.13x slower                                                          |
| regex_effbot             | 1.66 ms                                                         | 1.91 ms: 1.15x slower                                                          |
| genshi_xml               | 46.6 ms                                                         | 53.6 ms: 1.15x slower                                                          |
| bench_mp_pool            | 66.4 ms                                                         | 77.1 ms: 1.16x slower                                                          |
| telco                    | 4.83 ms                                                         | 5.70 ms: 1.18x slower                                                          |
| async_generators         | 241 ms                                                          | 320 ms: 1.33x slower                                                           |
| Geometric mean           | (ref)                                                           | 1.21x faster                                                                   |

Benchmark hidden because not significant (2): docutils, logging_simple
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, dulwich_log, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (4) of results/bm-20240708-3.14.0a0-006b53a-JIT/bm-20240708-pythonperf1_win32-x86-python-006b53a42f72be83ecdf-3.14.0a0-006b53a.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.14x
- 95% likely to have a speedup of 1.13x
- 99% likely to have a speedup of 1.10x

# Memory
- memory change: unknown
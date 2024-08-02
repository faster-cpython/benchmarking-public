# Results vs. 3.10.4

- fork: python
- ref: d27a53fc02a87e76066f
- machine: windows-x86
- commit hash: d27a53f
- commit date: 2024-07-30
- overall geometric mean: 1.15x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240730-pythonperf1_win32-x86-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 253 ms: 1.05x faster                                                           |
| docutils       | 1.95 sec                                                        | 1.90 sec: 1.02x faster                                                         |
| html5lib       | 52.1 ms                                                         | 47.9 ms: 1.09x faster                                                          |
| tornado_http   | 118 ms                                                          | 104 ms: 1.13x faster                                                           |
| Geometric mean | (ref)                                                           | 1.07x faster                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240730-pythonperf1_win32-x86-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f |
|-------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 922 ms                                                          | 490 ms: 1.88x faster                                                           |
| async_tree_none         | 394 ms                                                          | 222 ms: 1.77x faster                                                           |
| async_tree_io           | 940 ms                                                          | 538 ms: 1.75x faster                                                           |
| async_tree_memoization  | 467 ms                                                          | 270 ms: 1.73x faster                                                           |
| Geometric mean          | (ref)                                                           | 1.78x faster                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240730-pythonperf1_win32-x86-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 199 ms: 2.52x faster                                                           |
| float          | 69.6 ms                                                         | 59.1 ms: 1.18x faster                                                          |
| nbody          | 79.1 ms                                                         | 91.7 ms: 1.16x slower                                                          |
| Geometric mean | (ref)                                                           | 1.37x faster                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240730-pythonperf1_win32-x86-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_compile  | 117 ms                                                          | 103 ms: 1.14x faster                                                           |
| regex_dna      | 131 ms                                                          | 119 ms: 1.09x faster                                                           |
| regex_v8       | 15.8 ms                                                         | 16.0 ms: 1.01x slower                                                          |
| regex_effbot   | 1.66 ms                                                         | 1.92 ms: 1.15x slower                                                          |
| Geometric mean | (ref)                                                           | 1.02x faster                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240730-pythonperf1_win32-x86-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f |
|----------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| json_dumps           | 9.82 ms                                                         | 7.64 ms: 1.29x faster                                                          |
| pickle_pure_python   | 280 us                                                          | 235 us: 1.19x faster                                                           |
| xml_etree_parse      | 120 ms                                                          | 106 ms: 1.13x faster                                                           |
| unpickle_pure_python | 189 us                                                          | 168 us: 1.13x faster                                                           |
| json_loads           | 22.4 us                                                         | 20.5 us: 1.09x faster                                                          |
| tomli_loads          | 1.91 sec                                                        | 1.76 sec: 1.09x faster                                                         |
| xml_etree_iterparse  | 70.8 ms                                                         | 67.2 ms: 1.05x faster                                                          |
| xml_etree_process    | 48.1 ms                                                         | 47.1 ms: 1.02x faster                                                          |
| xml_etree_generate   | 61.6 ms                                                         | 66.0 ms: 1.07x slower                                                          |
| Geometric mean       | (ref)                                                           | 1.10x faster                                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240730-pythonperf1_win32-x86-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f |
|------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup         | 22.9 ms                                                         | 23.7 ms: 1.03x slower                                                          |
| python_startup_no_site | 18.1 ms                                                         | 19.7 ms: 1.09x slower                                                          |
| Geometric mean         | (ref)                                                           | 1.06x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240730-pythonperf1_win32-x86-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f |
|-----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako            | 9.10 ms                                                         | 8.06 ms: 1.13x faster                                                          |
| django_template | 36.0 ms                                                         | 34.0 ms: 1.06x faster                                                          |
| genshi_xml      | 46.6 ms                                                         | 47.1 ms: 1.01x slower                                                          |
| genshi_text     | 21.0 ms                                                         | 21.7 ms: 1.03x slower                                                          |
| Geometric mean  | (ref)                                                           | 1.03x faster                                                                   |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240730-pythonperf1_win32-x86-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f |
|--------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| typing_runtime_protocols | 396 us                                                          | 137 us: 2.89x faster                                                           |
| pidigits                 | 502 ms                                                          | 199 ms: 2.52x faster                                                           |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 490 ms: 1.88x faster                                                           |
| async_tree_none          | 394 ms                                                          | 222 ms: 1.77x faster                                                           |
| async_tree_io            | 940 ms                                                          | 538 ms: 1.75x faster                                                           |
| async_tree_memoization   | 467 ms                                                          | 270 ms: 1.73x faster                                                           |
| pylint                   | 384 ms                                                          | 232 ms: 1.65x faster                                                           |
| deltablue                | 4.04 ms                                                         | 2.56 ms: 1.57x faster                                                          |
| crypto_pyaes             | 81.3 ms                                                         | 55.9 ms: 1.45x faster                                                          |
| chaos                    | 74.4 ms                                                         | 51.5 ms: 1.44x faster                                                          |
| deepcopy_memo            | 29.6 us                                                         | 20.5 us: 1.44x faster                                                          |
| raytrace                 | 303 ms                                                          | 221 ms: 1.37x faster                                                           |
| comprehensions           | 17.7 us                                                         | 13.0 us: 1.36x faster                                                          |
| logging_silent           | 97.9 ns                                                         | 73.9 ns: 1.32x faster                                                          |
| go                       | 146 ms                                                          | 111 ms: 1.31x faster                                                           |
| scimark_lu               | 89.8 ms                                                         | 68.7 ms: 1.31x faster                                                          |
| deepcopy                 | 310 us                                                          | 240 us: 1.29x faster                                                           |
| json_dumps               | 9.82 ms                                                         | 7.64 ms: 1.29x faster                                                          |
| sqlglot_parse            | 1.33 ms                                                         | 1.04 ms: 1.27x faster                                                          |
| richards_super           | 49.9 ms                                                         | 39.4 ms: 1.27x faster                                                          |
| pyflate                  | 422 ms                                                          | 333 ms: 1.26x faster                                                           |
| hexiom                   | 6.13 ms                                                         | 4.92 ms: 1.25x faster                                                          |
| pycparser                | 1.04 sec                                                        | 847 ms: 1.23x faster                                                           |
| generators               | 31.6 ms                                                         | 25.7 ms: 1.23x faster                                                          |
| sqlglot_transpile        | 1.58 ms                                                         | 1.30 ms: 1.22x faster                                                          |
| scimark_monte_carlo      | 61.9 ms                                                         | 50.7 ms: 1.22x faster                                                          |
| thrift                   | 902 us                                                          | 744 us: 1.21x faster                                                           |
| nqueens                  | 87.1 ms                                                         | 73.1 ms: 1.19x faster                                                          |
| pickle_pure_python       | 280 us                                                          | 235 us: 1.19x faster                                                           |
| float                    | 69.6 ms                                                         | 59.1 ms: 1.18x faster                                                          |
| scimark_sor              | 115 ms                                                          | 98.3 ms: 1.17x faster                                                          |
| dulwich_log              | 58.5 ms                                                         | 50.2 ms: 1.16x faster                                                          |
| richards                 | 40.3 ms                                                         | 35.0 ms: 1.15x faster                                                          |
| regex_compile            | 117 ms                                                          | 103 ms: 1.14x faster                                                           |
| sympy_sum                | 122 ms                                                          | 108 ms: 1.13x faster                                                           |
| json                     | 4.76 ms                                                         | 4.20 ms: 1.13x faster                                                          |
| tornado_http             | 118 ms                                                          | 104 ms: 1.13x faster                                                           |
| mako                     | 9.10 ms                                                         | 8.06 ms: 1.13x faster                                                          |
| xml_etree_parse          | 120 ms                                                          | 106 ms: 1.13x faster                                                           |
| bench_thread_pool        | 1.12 ms                                                         | 995 us: 1.13x faster                                                           |
| unpickle_pure_python     | 189 us                                                          | 168 us: 1.13x faster                                                           |
| regex_dna                | 131 ms                                                          | 119 ms: 1.09x faster                                                           |
| json_loads               | 22.4 us                                                         | 20.5 us: 1.09x faster                                                          |
| mdp                      | 1.83 sec                                                        | 1.68 sec: 1.09x faster                                                         |
| html5lib                 | 52.1 ms                                                         | 47.9 ms: 1.09x faster                                                          |
| sympy_integrate          | 16.6 ms                                                         | 15.3 ms: 1.09x faster                                                          |
| tomli_loads              | 1.91 sec                                                        | 1.76 sec: 1.09x faster                                                         |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 3.04 ms: 1.07x faster                                                          |
| spectral_norm            | 80.2 ms                                                         | 75.6 ms: 1.06x faster                                                          |
| django_template          | 36.0 ms                                                         | 34.0 ms: 1.06x faster                                                          |
| deepcopy_reduce          | 2.68 us                                                         | 2.54 us: 1.06x faster                                                          |
| xml_etree_iterparse      | 70.8 ms                                                         | 67.2 ms: 1.05x faster                                                          |
| coroutines               | 17.9 ms                                                         | 17.0 ms: 1.05x faster                                                          |
| 2to3                     | 265 ms                                                          | 253 ms: 1.05x faster                                                           |
| sympy_str                | 229 ms                                                          | 221 ms: 1.04x faster                                                           |
| meteor_contest           | 80.0 ms                                                         | 77.5 ms: 1.03x faster                                                          |
| docutils                 | 1.95 sec                                                        | 1.90 sec: 1.02x faster                                                         |
| xml_etree_process        | 48.1 ms                                                         | 47.1 ms: 1.02x faster                                                          |
| pprint_pformat           | 1.37 sec                                                        | 1.34 sec: 1.02x faster                                                         |
| sqlglot_optimize         | 44.7 ms                                                         | 44.1 ms: 1.01x faster                                                          |
| pprint_safe_repr         | 658 ms                                                          | 653 ms: 1.01x faster                                                           |
| sqlglot_normalize        | 230 ms                                                          | 230 ms: 1.00x faster                                                           |
| sympy_expand             | 391 ms                                                          | 393 ms: 1.01x slower                                                           |
| genshi_xml               | 46.6 ms                                                         | 47.1 ms: 1.01x slower                                                          |
| regex_v8                 | 15.8 ms                                                         | 16.0 ms: 1.01x slower                                                          |
| scimark_fft              | 216 ms                                                          | 221 ms: 1.02x slower                                                           |
| genshi_text              | 21.0 ms                                                         | 21.7 ms: 1.03x slower                                                          |
| python_startup           | 22.9 ms                                                         | 23.7 ms: 1.03x slower                                                          |
| xml_etree_generate       | 61.6 ms                                                         | 66.0 ms: 1.07x slower                                                          |
| pathlib                  | 81.2 ms                                                         | 88.1 ms: 1.08x slower                                                          |
| python_startup_no_site   | 18.1 ms                                                         | 19.7 ms: 1.09x slower                                                          |
| create_gc_cycles         | 694 us                                                          | 759 us: 1.09x slower                                                           |
| bench_mp_pool            | 66.4 ms                                                         | 73.6 ms: 1.11x slower                                                          |
| coverage                 | 46.6 ms                                                         | 52.0 ms: 1.12x slower                                                          |
| logging_simple           | 7.29 us                                                         | 8.19 us: 1.12x slower                                                          |
| logging_format           | 7.91 us                                                         | 8.88 us: 1.12x slower                                                          |
| gc_traversal             | 1.28 ms                                                         | 1.46 ms: 1.14x slower                                                          |
| regex_effbot             | 1.66 ms                                                         | 1.92 ms: 1.15x slower                                                          |
| nbody                    | 79.1 ms                                                         | 91.7 ms: 1.16x slower                                                          |
| async_generators         | 241 ms                                                          | 282 ms: 1.17x slower                                                           |
| telco                    | 4.83 ms                                                         | 6.31 ms: 1.31x slower                                                          |
| Geometric mean           | (ref)                                                           | 1.15x faster                                                                   |

Benchmark hidden because not significant (3): asyncio_tcp, fannkuch, asyncio_tcp_ssl
Ignored benchmarks (14) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (4) of results/bm-20240730-3.14.0a0-d27a53f/bm-20240730-pythonperf1_win32-x86-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: unknown
# Results vs. 3.10.4

- fork: faster-cpython
- ref: experimental_branch_
- machine: windows-x86
- commit hash: cc98bb5
- commit date: 2024-07-31
- overall geometric mean: 1.11x faster
- HPT reliability: 99.96%
- HPT 99th percentile: 1.01x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240731-pythonperf1_win32-x86-faster%2dcpython-experimental_branch_-3.14.0a0-cc98bb5 |
|----------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 262 ms: 1.01x faster                                                                     |
| docutils       | 1.95 sec                                                        | 1.94 sec: 1.01x faster                                                                   |
| html5lib       | 52.1 ms                                                         | 49.1 ms: 1.06x faster                                                                    |
| tornado_http   | 118 ms                                                          | 106 ms: 1.11x faster                                                                     |
| Geometric mean | (ref)                                                           | 1.05x faster                                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240731-pythonperf1_win32-x86-faster%2dcpython-experimental_branch_-3.14.0a0-cc98bb5 |
|-------------------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 922 ms                                                          | 486 ms: 1.90x faster                                                                     |
| async_tree_none         | 394 ms                                                          | 232 ms: 1.70x faster                                                                     |
| async_tree_io           | 940 ms                                                          | 564 ms: 1.67x faster                                                                     |
| async_tree_memoization  | 467 ms                                                          | 285 ms: 1.63x faster                                                                     |
| Geometric mean          | (ref)                                                           | 1.72x faster                                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240731-pythonperf1_win32-x86-faster%2dcpython-experimental_branch_-3.14.0a0-cc98bb5 |
|----------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 201 ms: 2.50x faster                                                                     |
| float          | 69.6 ms                                                         | 60.0 ms: 1.16x faster                                                                    |
| nbody          | 79.1 ms                                                         | 99.2 ms: 1.25x slower                                                                    |
| Geometric mean | (ref)                                                           | 1.32x faster                                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240731-pythonperf1_win32-x86-faster%2dcpython-experimental_branch_-3.14.0a0-cc98bb5 |
|----------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| regex_dna      | 131 ms                                                          | 119 ms: 1.10x faster                                                                     |
| regex_compile  | 117 ms                                                          | 109 ms: 1.07x faster                                                                     |
| regex_v8       | 15.8 ms                                                         | 16.2 ms: 1.03x slower                                                                    |
| regex_effbot   | 1.66 ms                                                         | 1.93 ms: 1.16x slower                                                                    |
| Geometric mean | (ref)                                                           | 1.00x slower                                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240731-pythonperf1_win32-x86-faster%2dcpython-experimental_branch_-3.14.0a0-cc98bb5 |
|----------------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| json_dumps           | 9.82 ms                                                         | 7.35 ms: 1.34x faster                                                                    |
| xml_etree_parse      | 120 ms                                                          | 104 ms: 1.15x faster                                                                     |
| unpickle_pure_python | 189 us                                                          | 173 us: 1.10x faster                                                                     |
| json_loads           | 22.4 us                                                         | 20.4 us: 1.10x faster                                                                    |
| pickle_pure_python   | 280 us                                                          | 257 us: 1.09x faster                                                                     |
| tomli_loads          | 1.91 sec                                                        | 1.79 sec: 1.07x faster                                                                   |
| xml_etree_iterparse  | 70.8 ms                                                         | 67.9 ms: 1.04x faster                                                                    |
| xml_etree_process    | 48.1 ms                                                         | 48.6 ms: 1.01x slower                                                                    |
| xml_etree_generate   | 61.6 ms                                                         | 66.2 ms: 1.07x slower                                                                    |
| Geometric mean       | (ref)                                                           | 1.08x faster                                                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240731-pythonperf1_win32-x86-faster%2dcpython-experimental_branch_-3.14.0a0-cc98bb5 |
|------------------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| python_startup         | 22.9 ms                                                         | 24.3 ms: 1.06x slower                                                                    |
| python_startup_no_site | 18.1 ms                                                         | 20.4 ms: 1.13x slower                                                                    |
| Geometric mean         | (ref)                                                           | 1.09x slower                                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240731-pythonperf1_win32-x86-faster%2dcpython-experimental_branch_-3.14.0a0-cc98bb5 |
|-----------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| mako            | 9.10 ms                                                         | 8.24 ms: 1.11x faster                                                                    |
| django_template | 36.0 ms                                                         | 33.9 ms: 1.06x faster                                                                    |
| genshi_xml      | 46.6 ms                                                         | 48.4 ms: 1.04x slower                                                                    |
| genshi_text     | 21.0 ms                                                         | 22.3 ms: 1.06x slower                                                                    |
| Geometric mean  | (ref)                                                           | 1.01x faster                                                                             |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240731-pythonperf1_win32-x86-faster%2dcpython-experimental_branch_-3.14.0a0-cc98bb5 |
|--------------------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| typing_runtime_protocols | 396 us                                                          | 158 us: 2.51x faster                                                                     |
| pidigits                 | 502 ms                                                          | 201 ms: 2.50x faster                                                                     |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 486 ms: 1.90x faster                                                                     |
| async_tree_none          | 394 ms                                                          | 232 ms: 1.70x faster                                                                     |
| async_tree_io            | 940 ms                                                          | 564 ms: 1.67x faster                                                                     |
| async_tree_memoization   | 467 ms                                                          | 285 ms: 1.63x faster                                                                     |
| pylint                   | 384 ms                                                          | 238 ms: 1.61x faster                                                                     |
| deltablue                | 4.04 ms                                                         | 2.74 ms: 1.48x faster                                                                    |
| chaos                    | 74.4 ms                                                         | 54.0 ms: 1.38x faster                                                                    |
| crypto_pyaes             | 81.3 ms                                                         | 59.1 ms: 1.38x faster                                                                    |
| raytrace                 | 303 ms                                                          | 226 ms: 1.34x faster                                                                     |
| json_dumps               | 9.82 ms                                                         | 7.35 ms: 1.34x faster                                                                    |
| logging_silent           | 97.9 ns                                                         | 74.9 ns: 1.31x faster                                                                    |
| scimark_lu               | 89.8 ms                                                         | 70.0 ms: 1.28x faster                                                                    |
| deepcopy_memo            | 29.6 us                                                         | 23.3 us: 1.27x faster                                                                    |
| comprehensions           | 17.7 us                                                         | 14.3 us: 1.24x faster                                                                    |
| go                       | 146 ms                                                          | 119 ms: 1.22x faster                                                                     |
| sqlglot_parse            | 1.33 ms                                                         | 1.09 ms: 1.22x faster                                                                    |
| deepcopy                 | 310 us                                                          | 259 us: 1.20x faster                                                                     |
| pyflate                  | 422 ms                                                          | 355 ms: 1.19x faster                                                                     |
| thrift                   | 902 us                                                          | 769 us: 1.17x faster                                                                     |
| sqlglot_transpile        | 1.58 ms                                                         | 1.35 ms: 1.17x faster                                                                    |
| scimark_sor              | 115 ms                                                          | 98.5 ms: 1.17x faster                                                                    |
| pycparser                | 1.04 sec                                                        | 893 ms: 1.17x faster                                                                     |
| float                    | 69.6 ms                                                         | 60.0 ms: 1.16x faster                                                                    |
| hexiom                   | 6.13 ms                                                         | 5.31 ms: 1.16x faster                                                                    |
| xml_etree_parse          | 120 ms                                                          | 104 ms: 1.15x faster                                                                     |
| dulwich_log              | 58.5 ms                                                         | 51.1 ms: 1.14x faster                                                                    |
| generators               | 31.6 ms                                                         | 27.6 ms: 1.14x faster                                                                    |
| bench_thread_pool        | 1.12 ms                                                         | 991 us: 1.13x faster                                                                     |
| richards_super           | 49.9 ms                                                         | 44.2 ms: 1.13x faster                                                                    |
| scimark_monte_carlo      | 61.9 ms                                                         | 55.6 ms: 1.11x faster                                                                    |
| tornado_http             | 118 ms                                                          | 106 ms: 1.11x faster                                                                     |
| json                     | 4.76 ms                                                         | 4.29 ms: 1.11x faster                                                                    |
| mako                     | 9.10 ms                                                         | 8.24 ms: 1.11x faster                                                                    |
| nqueens                  | 87.1 ms                                                         | 79.1 ms: 1.10x faster                                                                    |
| regex_dna                | 131 ms                                                          | 119 ms: 1.10x faster                                                                     |
| unpickle_pure_python     | 189 us                                                          | 173 us: 1.10x faster                                                                     |
| json_loads               | 22.4 us                                                         | 20.4 us: 1.10x faster                                                                    |
| sympy_sum                | 122 ms                                                          | 112 ms: 1.09x faster                                                                     |
| pickle_pure_python       | 280 us                                                          | 257 us: 1.09x faster                                                                     |
| regex_compile            | 117 ms                                                          | 109 ms: 1.07x faster                                                                     |
| tomli_loads              | 1.91 sec                                                        | 1.79 sec: 1.07x faster                                                                   |
| mdp                      | 1.83 sec                                                        | 1.71 sec: 1.07x faster                                                                   |
| django_template          | 36.0 ms                                                         | 33.9 ms: 1.06x faster                                                                    |
| html5lib                 | 52.1 ms                                                         | 49.1 ms: 1.06x faster                                                                    |
| asyncio_tcp              | 744 ms                                                          | 708 ms: 1.05x faster                                                                     |
| sympy_integrate          | 16.6 ms                                                         | 15.9 ms: 1.04x faster                                                                    |
| xml_etree_iterparse      | 70.8 ms                                                         | 67.9 ms: 1.04x faster                                                                    |
| deepcopy_reduce          | 2.68 us                                                         | 2.60 us: 1.03x faster                                                                    |
| coroutines               | 17.9 ms                                                         | 17.4 ms: 1.03x faster                                                                    |
| richards                 | 40.3 ms                                                         | 39.1 ms: 1.03x faster                                                                    |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 3.16 ms: 1.02x faster                                                                    |
| 2to3                     | 265 ms                                                          | 262 ms: 1.01x faster                                                                     |
| spectral_norm            | 80.2 ms                                                         | 79.2 ms: 1.01x faster                                                                    |
| docutils                 | 1.95 sec                                                        | 1.94 sec: 1.01x faster                                                                   |
| xml_etree_process        | 48.1 ms                                                         | 48.6 ms: 1.01x slower                                                                    |
| pprint_pformat           | 1.37 sec                                                        | 1.39 sec: 1.01x slower                                                                   |
| regex_v8                 | 15.8 ms                                                         | 16.2 ms: 1.03x slower                                                                    |
| pprint_safe_repr         | 658 ms                                                          | 680 ms: 1.03x slower                                                                     |
| sympy_expand             | 391 ms                                                          | 404 ms: 1.03x slower                                                                     |
| genshi_xml               | 46.6 ms                                                         | 48.4 ms: 1.04x slower                                                                    |
| fannkuch                 | 317 ms                                                          | 330 ms: 1.04x slower                                                                     |
| meteor_contest           | 80.0 ms                                                         | 84.3 ms: 1.05x slower                                                                    |
| python_startup           | 22.9 ms                                                         | 24.3 ms: 1.06x slower                                                                    |
| genshi_text              | 21.0 ms                                                         | 22.3 ms: 1.06x slower                                                                    |
| xml_etree_generate       | 61.6 ms                                                         | 66.2 ms: 1.07x slower                                                                    |
| create_gc_cycles         | 694 us                                                          | 749 us: 1.08x slower                                                                     |
| scimark_fft              | 216 ms                                                          | 237 ms: 1.10x slower                                                                     |
| pathlib                  | 81.2 ms                                                         | 89.6 ms: 1.10x slower                                                                    |
| bench_mp_pool            | 66.4 ms                                                         | 73.7 ms: 1.11x slower                                                                    |
| coverage                 | 46.6 ms                                                         | 51.9 ms: 1.12x slower                                                                    |
| gc_traversal             | 1.28 ms                                                         | 1.44 ms: 1.12x slower                                                                    |
| python_startup_no_site   | 18.1 ms                                                         | 20.4 ms: 1.13x slower                                                                    |
| logging_simple           | 7.29 us                                                         | 8.26 us: 1.13x slower                                                                    |
| logging_format           | 7.91 us                                                         | 8.98 us: 1.14x slower                                                                    |
| regex_effbot             | 1.66 ms                                                         | 1.93 ms: 1.16x slower                                                                    |
| async_generators         | 241 ms                                                          | 294 ms: 1.22x slower                                                                     |
| nbody                    | 79.1 ms                                                         | 99.2 ms: 1.25x slower                                                                    |
| telco                    | 4.83 ms                                                         | 6.24 ms: 1.29x slower                                                                    |
| Geometric mean           | (ref)                                                           | 1.11x faster                                                                             |

Benchmark hidden because not significant (4): sqlglot_optimize, sympy_str, asyncio_tcp_ssl, sqlglot_normalize
Ignored benchmarks (14) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (4) of results/bm-20240731-3.14.0a0-cc98bb5/bm-20240731-pythonperf1_win32-x86-faster%2dcpython-experimental_branch_-3.14.0a0-cc98bb5.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 99.96% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: unknown
# Results vs. 3.10.4

- fork: python
- ref: 2de048ce79e621f5ae05
- machine: windows-x86
- commit hash: 2de048c
- commit date: 2024-12-13
- overall geometric mean: 1.065x faster
- HPT reliability: 91.21%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241213-pythonperf1_win32-x86-python-2de048ce79e621f5ae05-3.14.0a2+-2de048c |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 262 ms: 1.01x faster                                                            |
| docutils       | 1.95 sec                                                        | 1.93 sec: 1.01x faster                                                          |
| html5lib       | 52.1 ms                                                         | 49.5 ms: 1.05x faster                                                           |
| Geometric mean | (ref)                                                           | 1.02x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241213-pythonperf1_win32-x86-python-2de048ce79e621f5ae05-3.14.0a2+-2de048c |
|-------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_io           | 940 ms                                                          | 473 ms: 1.99x faster                                                            |
| async_tree_cpu_io_mixed | 922 ms                                                          | 502 ms: 1.84x faster                                                            |
| async_tree_none         | 394 ms                                                          | 225 ms: 1.75x faster                                                            |
| async_tree_memoization  | 467 ms                                                          | 277 ms: 1.68x faster                                                            |
| Geometric mean          | (ref)                                                           | 1.81x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241213-pythonperf1_win32-x86-python-2de048ce79e621f5ae05-3.14.0a2+-2de048c |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 204 ms: 2.47x faster                                                            |
| float          | 69.6 ms                                                         | 56.1 ms: 1.24x faster                                                           |
| nbody          | 79.1 ms                                                         | 99.3 ms: 1.26x slower                                                           |
| Geometric mean | (ref)                                                           | 1.35x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241213-pythonperf1_win32-x86-python-2de048ce79e621f5ae05-3.14.0a2+-2de048c |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_dna      | 131 ms                                                          | 114 ms: 1.14x faster                                                            |
| regex_effbot   | 1.66 ms                                                         | 1.59 ms: 1.05x faster                                                           |
| regex_compile  | 117 ms                                                          | 114 ms: 1.02x faster                                                            |
| Geometric mean | (ref)                                                           | 1.05x faster                                                                    |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241213-pythonperf1_win32-x86-python-2de048ce79e621f5ae05-3.14.0a2+-2de048c |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| xml_etree_parse      | 120 ms                                                          | 107 ms: 1.13x faster                                                            |
| tomli_loads          | 1.91 sec                                                        | 1.74 sec: 1.09x faster                                                          |
| xml_etree_iterparse  | 70.8 ms                                                         | 65.3 ms: 1.08x faster                                                           |
| json_loads           | 22.4 us                                                         | 20.7 us: 1.08x faster                                                           |
| json_dumps           | 9.82 ms                                                         | 9.22 ms: 1.07x faster                                                           |
| pickle_pure_python   | 280 us                                                          | 298 us: 1.06x slower                                                            |
| unpickle_pure_python | 189 us                                                          | 203 us: 1.07x slower                                                            |
| xml_etree_process    | 48.1 ms                                                         | 51.7 ms: 1.07x slower                                                           |
| xml_etree_generate   | 61.6 ms                                                         | 69.3 ms: 1.12x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.01x faster                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241213-pythonperf1_win32-x86-python-2de048ce79e621f5ae05-3.14.0a2+-2de048c |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 18.1 ms                                                         | 19.6 ms: 1.08x slower                                                           |
| python_startup         | 22.9 ms                                                         | 26.1 ms: 1.14x slower                                                           |
| Geometric mean         | (ref)                                                           | 1.11x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241213-pythonperf1_win32-x86-python-2de048ce79e621f5ae05-3.14.0a2+-2de048c |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako           | 9.10 ms                                                         | 7.33 ms: 1.24x faster                                                           |
| genshi_xml     | 46.6 ms                                                         | 57.0 ms: 1.22x slower                                                           |
| genshi_text    | 21.0 ms                                                         | 25.7 ms: 1.22x slower                                                           |
| Geometric mean | (ref)                                                           | 1.05x slower                                                                    |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241213-pythonperf1_win32-x86-python-2de048ce79e621f5ae05-3.14.0a2+-2de048c |
|--------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pidigits                 | 502 ms                                                          | 204 ms: 2.47x faster                                                            |
| typing_runtime_protocols | 396 us                                                          | 168 us: 2.36x faster                                                            |
| sqlglot_normalize        | 230 ms                                                          | 105 ms: 2.19x faster                                                            |
| async_tree_io            | 940 ms                                                          | 473 ms: 1.99x faster                                                            |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 502 ms: 1.84x faster                                                            |
| async_tree_none          | 394 ms                                                          | 225 ms: 1.75x faster                                                            |
| async_tree_memoization   | 467 ms                                                          | 277 ms: 1.68x faster                                                            |
| pylint                   | 384 ms                                                          | 232 ms: 1.65x faster                                                            |
| deltablue                | 4.04 ms                                                         | 3.14 ms: 1.29x faster                                                           |
| logging_silent           | 97.9 ns                                                         | 77.5 ns: 1.26x faster                                                           |
| deepcopy_memo            | 29.6 us                                                         | 23.7 us: 1.25x faster                                                           |
| mako                     | 9.10 ms                                                         | 7.33 ms: 1.24x faster                                                           |
| float                    | 69.6 ms                                                         | 56.1 ms: 1.24x faster                                                           |
| scimark_lu               | 89.8 ms                                                         | 73.4 ms: 1.22x faster                                                           |
| go                       | 146 ms                                                          | 119 ms: 1.22x faster                                                            |
| crypto_pyaes             | 81.3 ms                                                         | 68.0 ms: 1.20x faster                                                           |
| sqlite_synth             | 2.29 us                                                         | 1.92 us: 1.19x faster                                                           |
| sqlglot_parse            | 1.33 ms                                                         | 1.13 ms: 1.17x faster                                                           |
| dulwich_log              | 58.5 ms                                                         | 50.3 ms: 1.16x faster                                                           |
| thrift                   | 902 us                                                          | 777 us: 1.16x faster                                                            |
| scimark_sor              | 115 ms                                                          | 100 ms: 1.15x faster                                                            |
| deepcopy                 | 310 us                                                          | 270 us: 1.15x faster                                                            |
| regex_dna                | 131 ms                                                          | 114 ms: 1.14x faster                                                            |
| chaos                    | 74.4 ms                                                         | 65.2 ms: 1.14x faster                                                           |
| pycparser                | 1.04 sec                                                        | 924 ms: 1.13x faster                                                            |
| sqlglot_transpile        | 1.58 ms                                                         | 1.41 ms: 1.13x faster                                                           |
| xml_etree_parse          | 120 ms                                                          | 107 ms: 1.13x faster                                                            |
| json                     | 4.76 ms                                                         | 4.24 ms: 1.12x faster                                                           |
| tomli_loads              | 1.91 sec                                                        | 1.74 sec: 1.09x faster                                                          |
| spectral_norm            | 80.2 ms                                                         | 73.7 ms: 1.09x faster                                                           |
| xml_etree_iterparse      | 70.8 ms                                                         | 65.3 ms: 1.08x faster                                                           |
| pyflate                  | 422 ms                                                          | 390 ms: 1.08x faster                                                            |
| json_loads               | 22.4 us                                                         | 20.7 us: 1.08x faster                                                           |
| bench_thread_pool        | 1.12 ms                                                         | 1.05 ms: 1.07x faster                                                           |
| coroutines               | 17.9 ms                                                         | 16.7 ms: 1.07x faster                                                           |
| richards_super           | 49.9 ms                                                         | 46.6 ms: 1.07x faster                                                           |
| json_dumps               | 9.82 ms                                                         | 9.22 ms: 1.07x faster                                                           |
| sympy_sum                | 122 ms                                                          | 116 ms: 1.06x faster                                                            |
| html5lib                 | 52.1 ms                                                         | 49.5 ms: 1.05x faster                                                           |
| regex_effbot             | 1.66 ms                                                         | 1.59 ms: 1.05x faster                                                           |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 3.13 ms: 1.03x faster                                                           |
| regex_compile            | 117 ms                                                          | 114 ms: 1.02x faster                                                            |
| 2to3                     | 265 ms                                                          | 262 ms: 1.01x faster                                                            |
| docutils                 | 1.95 sec                                                        | 1.93 sec: 1.01x faster                                                          |
| raytrace                 | 303 ms                                                          | 300 ms: 1.01x faster                                                            |
| mdp                      | 1.83 sec                                                        | 1.85 sec: 1.02x slower                                                          |
| sympy_str                | 229 ms                                                          | 235 ms: 1.02x slower                                                            |
| pathlib                  | 81.2 ms                                                         | 83.4 ms: 1.03x slower                                                           |
| richards                 | 40.3 ms                                                         | 41.5 ms: 1.03x slower                                                           |
| comprehensions           | 17.7 us                                                         | 18.4 us: 1.04x slower                                                           |
| deepcopy_reduce          | 2.68 us                                                         | 2.79 us: 1.04x slower                                                           |
| sympy_integrate          | 16.6 ms                                                         | 17.4 ms: 1.04x slower                                                           |
| sympy_expand             | 391 ms                                                          | 409 ms: 1.05x slower                                                            |
| pickle_pure_python       | 280 us                                                          | 298 us: 1.06x slower                                                            |
| unpickle_pure_python     | 189 us                                                          | 203 us: 1.07x slower                                                            |
| xml_etree_process        | 48.1 ms                                                         | 51.7 ms: 1.07x slower                                                           |
| fannkuch                 | 317 ms                                                          | 343 ms: 1.08x slower                                                            |
| python_startup_no_site   | 18.1 ms                                                         | 19.6 ms: 1.08x slower                                                           |
| pprint_pformat           | 1.37 sec                                                        | 1.52 sec: 1.11x slower                                                          |
| scimark_fft              | 216 ms                                                          | 241 ms: 1.11x slower                                                            |
| meteor_contest           | 80.0 ms                                                         | 89.3 ms: 1.12x slower                                                           |
| nqueens                  | 87.1 ms                                                         | 97.5 ms: 1.12x slower                                                           |
| xml_etree_generate       | 61.6 ms                                                         | 69.3 ms: 1.12x slower                                                           |
| pprint_safe_repr         | 658 ms                                                          | 741 ms: 1.13x slower                                                            |
| sqlglot_optimize         | 44.7 ms                                                         | 50.4 ms: 1.13x slower                                                           |
| python_startup           | 22.9 ms                                                         | 26.1 ms: 1.14x slower                                                           |
| coverage                 | 46.6 ms                                                         | 53.1 ms: 1.14x slower                                                           |
| logging_format           | 7.91 us                                                         | 9.04 us: 1.14x slower                                                           |
| logging_simple           | 7.29 us                                                         | 8.43 us: 1.16x slower                                                           |
| generators               | 31.6 ms                                                         | 36.5 ms: 1.16x slower                                                           |
| hexiom                   | 6.13 ms                                                         | 7.15 ms: 1.17x slower                                                           |
| mypy2                    | 590 ms                                                          | 717 ms: 1.22x slower                                                            |
| genshi_xml               | 46.6 ms                                                         | 57.0 ms: 1.22x slower                                                           |
| genshi_text              | 21.0 ms                                                         | 25.7 ms: 1.22x slower                                                           |
| nbody                    | 79.1 ms                                                         | 99.3 ms: 1.26x slower                                                           |
| bench_mp_pool            | 66.4 ms                                                         | 87.6 ms: 1.32x slower                                                           |
| async_generators         | 241 ms                                                          | 328 ms: 1.36x slower                                                            |
| gc_traversal             | 1.28 ms                                                         | 1.80 ms: 1.40x slower                                                           |
| telco                    | 4.83 ms                                                         | 7.10 ms: 1.47x slower                                                           |
| create_gc_cycles         | 694 us                                                          | 1.04 ms: 1.50x slower                                                           |
| Geometric mean           | (ref)                                                           | 1.06x faster                                                                    |

Benchmark hidden because not significant (3): scimark_monte_carlo, regex_v8, django_template
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20241213-3.14.0a2+-2de048c-JIT/bm-20241213-pythonperf1_win32-x86-python-2de048ce79e621f5ae05-3.14.0a2+-2de048c.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.065x faster

# HPT report

- Reliability score: 91.21% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown
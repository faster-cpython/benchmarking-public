# Results vs. 3.10.4

- fork: python
- ref: 09d6f5dc7824c74672ad
- machine: windows-x86
- commit hash: 09d6f5d
- commit date: 2024-11-07
- overall geometric mean: 1.037x faster
- HPT reliability: 62.41%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241107-pythonperf1_win32-x86-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 293 ms: 1.10x slower                                                            |
| docutils       | 1.95 sec                                                        | 2.14 sec: 1.10x slower                                                          |
| html5lib       | 52.1 ms                                                         | 49.9 ms: 1.04x faster                                                           |
| Geometric mean | (ref)                                                           | 1.05x slower                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241107-pythonperf1_win32-x86-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d |
|-------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 922 ms                                                          | 516 ms: 1.79x faster                                                            |
| async_tree_io           | 940 ms                                                          | 547 ms: 1.72x faster                                                            |
| async_tree_none         | 394 ms                                                          | 245 ms: 1.61x faster                                                            |
| async_tree_memoization  | 467 ms                                                          | 303 ms: 1.54x faster                                                            |
| Geometric mean          | (ref)                                                           | 1.66x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241107-pythonperf1_win32-x86-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 202 ms: 2.49x faster                                                            |
| float          | 69.6 ms                                                         | 55.8 ms: 1.25x faster                                                           |
| nbody          | 79.1 ms                                                         | 98.5 ms: 1.24x slower                                                           |
| Geometric mean | (ref)                                                           | 1.36x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241107-pythonperf1_win32-x86-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_dna      | 131 ms                                                          | 116 ms: 1.13x faster                                                            |
| regex_compile  | 117 ms                                                          | 121 ms: 1.04x slower                                                            |
| regex_effbot   | 1.66 ms                                                         | 1.81 ms: 1.09x slower                                                           |
| Geometric mean | (ref)                                                           | 1.00x slower                                                                    |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241107-pythonperf1_win32-x86-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| json_dumps           | 9.82 ms                                                         | 8.80 ms: 1.12x faster                                                           |
| xml_etree_parse      | 120 ms                                                          | 114 ms: 1.06x faster                                                            |
| tomli_loads          | 1.91 sec                                                        | 1.83 sec: 1.05x faster                                                          |
| json_loads           | 22.4 us                                                         | 21.4 us: 1.04x faster                                                           |
| xml_etree_iterparse  | 70.8 ms                                                         | 70.0 ms: 1.01x faster                                                           |
| unpickle_pure_python | 189 us                                                          | 192 us: 1.01x slower                                                            |
| pickle_pure_python   | 280 us                                                          | 301 us: 1.07x slower                                                            |
| xml_etree_process    | 48.1 ms                                                         | 53.6 ms: 1.11x slower                                                           |
| xml_etree_generate   | 61.6 ms                                                         | 71.8 ms: 1.16x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.01x slower                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241107-pythonperf1_win32-x86-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 18.1 ms                                                         | 20.3 ms: 1.12x slower                                                           |
| python_startup         | 22.9 ms                                                         | 26.8 ms: 1.17x slower                                                           |
| Geometric mean         | (ref)                                                           | 1.15x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241107-pythonperf1_win32-x86-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 9.10 ms                                                         | 7.39 ms: 1.23x faster                                                           |
| django_template | 36.0 ms                                                         | 36.3 ms: 1.01x slower                                                           |
| genshi_xml      | 46.6 ms                                                         | 58.5 ms: 1.26x slower                                                           |
| genshi_text     | 21.0 ms                                                         | 26.4 ms: 1.26x slower                                                           |
| Geometric mean  | (ref)                                                           | 1.07x slower                                                                    |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241107-pythonperf1_win32-x86-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d |
|--------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pidigits                 | 502 ms                                                          | 202 ms: 2.49x faster                                                            |
| typing_runtime_protocols | 396 us                                                          | 167 us: 2.38x faster                                                            |
| sqlglot_normalize        | 230 ms                                                          | 115 ms: 2.01x faster                                                            |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 516 ms: 1.79x faster                                                            |
| async_tree_io            | 940 ms                                                          | 547 ms: 1.72x faster                                                            |
| async_tree_none          | 394 ms                                                          | 245 ms: 1.61x faster                                                            |
| async_tree_memoization   | 467 ms                                                          | 303 ms: 1.54x faster                                                            |
| pylint                   | 384 ms                                                          | 293 ms: 1.31x faster                                                            |
| scimark_lu               | 89.8 ms                                                         | 69.7 ms: 1.29x faster                                                           |
| logging_silent           | 97.9 ns                                                         | 76.9 ns: 1.27x faster                                                           |
| float                    | 69.6 ms                                                         | 55.8 ms: 1.25x faster                                                           |
| deepcopy_memo            | 29.6 us                                                         | 23.8 us: 1.25x faster                                                           |
| mako                     | 9.10 ms                                                         | 7.39 ms: 1.23x faster                                                           |
| deltablue                | 4.04 ms                                                         | 3.29 ms: 1.23x faster                                                           |
| crypto_pyaes             | 81.3 ms                                                         | 67.1 ms: 1.21x faster                                                           |
| dulwich_log              | 58.5 ms                                                         | 49.3 ms: 1.19x faster                                                           |
| chaos                    | 74.4 ms                                                         | 63.3 ms: 1.18x faster                                                           |
| sqlite_synth             | 2.29 us                                                         | 1.96 us: 1.17x faster                                                           |
| thrift                   | 902 us                                                          | 779 us: 1.16x faster                                                            |
| scimark_sor              | 115 ms                                                          | 99.7 ms: 1.15x faster                                                           |
| go                       | 146 ms                                                          | 127 ms: 1.14x faster                                                            |
| sqlglot_parse            | 1.33 ms                                                         | 1.18 ms: 1.13x faster                                                           |
| deepcopy                 | 310 us                                                          | 274 us: 1.13x faster                                                            |
| regex_dna                | 131 ms                                                          | 116 ms: 1.13x faster                                                            |
| pycparser                | 1.04 sec                                                        | 931 ms: 1.12x faster                                                            |
| json_dumps               | 9.82 ms                                                         | 8.80 ms: 1.12x faster                                                           |
| coroutines               | 17.9 ms                                                         | 16.5 ms: 1.08x faster                                                           |
| json                     | 4.76 ms                                                         | 4.40 ms: 1.08x faster                                                           |
| bench_thread_pool        | 1.12 ms                                                         | 1.05 ms: 1.07x faster                                                           |
| pyflate                  | 422 ms                                                          | 398 ms: 1.06x faster                                                            |
| xml_etree_parse          | 120 ms                                                          | 114 ms: 1.06x faster                                                            |
| tomli_loads              | 1.91 sec                                                        | 1.83 sec: 1.05x faster                                                          |
| json_loads               | 22.4 us                                                         | 21.4 us: 1.04x faster                                                           |
| html5lib                 | 52.1 ms                                                         | 49.9 ms: 1.04x faster                                                           |
| sqlglot_transpile        | 1.58 ms                                                         | 1.53 ms: 1.04x faster                                                           |
| spectral_norm            | 80.2 ms                                                         | 79.2 ms: 1.01x faster                                                           |
| xml_etree_iterparse      | 70.8 ms                                                         | 70.0 ms: 1.01x faster                                                           |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 3.22 ms: 1.01x faster                                                           |
| django_template          | 36.0 ms                                                         | 36.3 ms: 1.01x slower                                                           |
| pathlib                  | 81.2 ms                                                         | 82.0 ms: 1.01x slower                                                           |
| unpickle_pure_python     | 189 us                                                          | 192 us: 1.01x slower                                                            |
| sympy_sum                | 122 ms                                                          | 125 ms: 1.02x slower                                                            |
| richards_super           | 49.9 ms                                                         | 51.3 ms: 1.03x slower                                                           |
| fannkuch                 | 317 ms                                                          | 326 ms: 1.03x slower                                                            |
| deepcopy_reduce          | 2.68 us                                                         | 2.76 us: 1.03x slower                                                           |
| mdp                      | 1.83 sec                                                        | 1.89 sec: 1.03x slower                                                          |
| raytrace                 | 303 ms                                                          | 314 ms: 1.04x slower                                                            |
| comprehensions           | 17.7 us                                                         | 18.4 us: 1.04x slower                                                           |
| regex_compile            | 117 ms                                                          | 121 ms: 1.04x slower                                                            |
| pickle_pure_python       | 280 us                                                          | 301 us: 1.07x slower                                                            |
| sympy_expand             | 391 ms                                                          | 422 ms: 1.08x slower                                                            |
| sympy_str                | 229 ms                                                          | 248 ms: 1.08x slower                                                            |
| regex_effbot             | 1.66 ms                                                         | 1.81 ms: 1.09x slower                                                           |
| pprint_pformat           | 1.37 sec                                                        | 1.50 sec: 1.10x slower                                                          |
| docutils                 | 1.95 sec                                                        | 2.14 sec: 1.10x slower                                                          |
| 2to3                     | 265 ms                                                          | 293 ms: 1.10x slower                                                            |
| nqueens                  | 87.1 ms                                                         | 97.0 ms: 1.11x slower                                                           |
| xml_etree_process        | 48.1 ms                                                         | 53.6 ms: 1.11x slower                                                           |
| coverage                 | 46.6 ms                                                         | 52.1 ms: 1.12x slower                                                           |
| logging_format           | 7.91 us                                                         | 8.85 us: 1.12x slower                                                           |
| python_startup_no_site   | 18.1 ms                                                         | 20.3 ms: 1.12x slower                                                           |
| pprint_safe_repr         | 658 ms                                                          | 743 ms: 1.13x slower                                                            |
| richards                 | 40.3 ms                                                         | 45.5 ms: 1.13x slower                                                           |
| meteor_contest           | 80.0 ms                                                         | 90.4 ms: 1.13x slower                                                           |
| logging_simple           | 7.29 us                                                         | 8.25 us: 1.13x slower                                                           |
| generators               | 31.6 ms                                                         | 35.8 ms: 1.14x slower                                                           |
| scimark_fft              | 216 ms                                                          | 247 ms: 1.14x slower                                                            |
| xml_etree_generate       | 61.6 ms                                                         | 71.8 ms: 1.16x slower                                                           |
| sympy_integrate          | 16.6 ms                                                         | 19.5 ms: 1.17x slower                                                           |
| python_startup           | 22.9 ms                                                         | 26.8 ms: 1.17x slower                                                           |
| hexiom                   | 6.13 ms                                                         | 7.19 ms: 1.17x slower                                                           |
| nbody                    | 79.1 ms                                                         | 98.5 ms: 1.24x slower                                                           |
| genshi_xml               | 46.6 ms                                                         | 58.5 ms: 1.26x slower                                                           |
| genshi_text              | 21.0 ms                                                         | 26.4 ms: 1.26x slower                                                           |
| sqlglot_optimize         | 44.7 ms                                                         | 56.6 ms: 1.27x slower                                                           |
| async_generators         | 241 ms                                                          | 330 ms: 1.37x slower                                                            |
| gc_traversal             | 1.28 ms                                                         | 1.77 ms: 1.38x slower                                                           |
| bench_mp_pool            | 66.4 ms                                                         | 92.9 ms: 1.40x slower                                                           |
| telco                    | 4.83 ms                                                         | 7.08 ms: 1.47x slower                                                           |
| create_gc_cycles         | 694 us                                                          | 1.17 ms: 1.68x slower                                                           |
| Geometric mean           | (ref)                                                           | 1.03x faster                                                                    |

Benchmark hidden because not significant (2): regex_v8, scimark_monte_carlo
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20241107-3.14.0a1+-09d6f5d-JIT/bm-20241107-pythonperf1_win32-x86-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.037x faster
# HPT report

- Reliability score: 62.41% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown
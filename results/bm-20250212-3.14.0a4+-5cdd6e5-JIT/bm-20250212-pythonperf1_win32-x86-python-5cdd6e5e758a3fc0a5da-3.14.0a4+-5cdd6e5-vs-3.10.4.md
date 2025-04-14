# Results vs. 3.10.4

- fork: python
- ref: 5cdd6e5e758a3fc0a5da
- machine: windows-x86
- commit hash: 5cdd6e5
- commit date: 2025-02-12
- overall geometric mean: 1.089x faster
- HPT reliability: 95.11%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250212-pythonperf1_win32-x86-python-5cdd6e5e758a3fc0a5da-3.14.0a4+-5cdd6e5 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 268 ms: 1.01x slower                                                            |
| docutils       | 1.95 sec                                                        | 2.01 sec: 1.03x slower                                                          |
| html5lib       | 52.1 ms                                                         | 47.5 ms: 1.10x faster                                                           |
| Geometric mean | (ref)                                                           | 1.02x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250212-pythonperf1_win32-x86-python-5cdd6e5e758a3fc0a5da-3.14.0a4+-5cdd6e5 |
|-------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 922 ms                                                          | 467 ms: 1.98x faster                                                            |
| async_tree_io           | 940 ms                                                          | 483 ms: 1.95x faster                                                            |
| async_tree_none         | 394 ms                                                          | 231 ms: 1.71x faster                                                            |
| async_tree_memoization  | 467 ms                                                          | 281 ms: 1.66x faster                                                            |
| Geometric mean          | (ref)                                                           | 1.82x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250212-pythonperf1_win32-x86-python-5cdd6e5e758a3fc0a5da-3.14.0a4+-5cdd6e5 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 200 ms: 2.52x faster                                                            |
| float          | 69.6 ms                                                         | 53.6 ms: 1.30x faster                                                           |
| nbody          | 79.1 ms                                                         | 113 ms: 1.43x slower                                                            |
| Geometric mean | (ref)                                                           | 1.32x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250212-pythonperf1_win32-x86-python-5cdd6e5e758a3fc0a5da-3.14.0a4+-5cdd6e5 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_dna      | 131 ms                                                          | 118 ms: 1.10x faster                                                            |
| regex_effbot   | 1.66 ms                                                         | 1.52 ms: 1.09x faster                                                           |
| regex_v8       | 15.8 ms                                                         | 15.6 ms: 1.01x faster                                                           |
| regex_compile  | 117 ms                                                          | 118 ms: 1.01x slower                                                            |
| Geometric mean | (ref)                                                           | 1.05x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250212-pythonperf1_win32-x86-python-5cdd6e5e758a3fc0a5da-3.14.0a4+-5cdd6e5 |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| xml_etree_parse      | 120 ms                                                          | 109 ms: 1.10x faster                                                            |
| json_dumps           | 9.82 ms                                                         | 9.02 ms: 1.09x faster                                                           |
| tomli_loads          | 1.91 sec                                                        | 1.81 sec: 1.06x faster                                                          |
| xml_etree_iterparse  | 70.8 ms                                                         | 68.1 ms: 1.04x faster                                                           |
| json_loads           | 22.4 us                                                         | 23.1 us: 1.03x slower                                                           |
| pickle_pure_python   | 280 us                                                          | 319 us: 1.14x slower                                                            |
| xml_etree_process    | 48.1 ms                                                         | 55.7 ms: 1.16x slower                                                           |
| unpickle_pure_python | 189 us                                                          | 226 us: 1.19x slower                                                            |
| xml_etree_generate   | 61.6 ms                                                         | 74.9 ms: 1.22x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.05x slower                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250212-pythonperf1_win32-x86-python-5cdd6e5e758a3fc0a5da-3.14.0a4+-5cdd6e5 |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 18.1 ms                                                         | 21.7 ms: 1.20x slower                                                           |
| python_startup         | 22.9 ms                                                         | 28.2 ms: 1.23x slower                                                           |
| Geometric mean         | (ref)                                                           | 1.21x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250212-pythonperf1_win32-x86-python-5cdd6e5e758a3fc0a5da-3.14.0a4+-5cdd6e5 |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 9.10 ms                                                         | 7.69 ms: 1.18x faster                                                           |
| django_template | 36.0 ms                                                         | 35.6 ms: 1.01x faster                                                           |
| genshi_xml      | 46.6 ms                                                         | 51.3 ms: 1.10x slower                                                           |
| genshi_text     | 21.0 ms                                                         | 24.7 ms: 1.18x slower                                                           |
| Geometric mean  | (ref)                                                           | 1.02x slower                                                                    |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250212-pythonperf1_win32-x86-python-5cdd6e5e758a3fc0a5da-3.14.0a4+-5cdd6e5 |
|--------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pidigits                 | 502 ms                                                          | 200 ms: 2.52x faster                                                            |
| pathlib                  | 81.2 ms                                                         | 34.0 ms: 2.39x faster                                                           |
| typing_runtime_protocols | 396 us                                                          | 174 us: 2.27x faster                                                            |
| sqlglot_normalize        | 230 ms                                                          | 105 ms: 2.18x faster                                                            |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 467 ms: 1.98x faster                                                            |
| async_tree_io            | 940 ms                                                          | 483 ms: 1.95x faster                                                            |
| async_tree_none          | 394 ms                                                          | 231 ms: 1.71x faster                                                            |
| pylint                   | 384 ms                                                          | 230 ms: 1.67x faster                                                            |
| async_tree_memoization   | 467 ms                                                          | 281 ms: 1.66x faster                                                            |
| deltablue                | 4.04 ms                                                         | 2.75 ms: 1.47x faster                                                           |
| deepcopy_memo            | 29.6 us                                                         | 21.4 us: 1.39x faster                                                           |
| logging_silent           | 97.9 ns                                                         | 72.1 ns: 1.36x faster                                                           |
| generators               | 31.6 ms                                                         | 23.7 ms: 1.33x faster                                                           |
| go                       | 146 ms                                                          | 110 ms: 1.32x faster                                                            |
| scimark_lu               | 89.8 ms                                                         | 68.5 ms: 1.31x faster                                                           |
| float                    | 69.6 ms                                                         | 53.6 ms: 1.30x faster                                                           |
| chaos                    | 74.4 ms                                                         | 58.5 ms: 1.27x faster                                                           |
| pyflate                  | 422 ms                                                          | 333 ms: 1.27x faster                                                            |
| scimark_monte_carlo      | 61.9 ms                                                         | 50.5 ms: 1.23x faster                                                           |
| sqlite_synth             | 2.29 us                                                         | 1.89 us: 1.21x faster                                                           |
| spectral_norm            | 80.2 ms                                                         | 66.2 ms: 1.21x faster                                                           |
| deepcopy                 | 310 us                                                          | 256 us: 1.21x faster                                                            |
| raytrace                 | 303 ms                                                          | 254 ms: 1.19x faster                                                            |
| mako                     | 9.10 ms                                                         | 7.69 ms: 1.18x faster                                                           |
| richards_super           | 49.9 ms                                                         | 42.9 ms: 1.16x faster                                                           |
| thrift                   | 902 us                                                          | 779 us: 1.16x faster                                                            |
| scimark_sor              | 115 ms                                                          | 101 ms: 1.14x faster                                                            |
| coroutines               | 17.9 ms                                                         | 15.7 ms: 1.14x faster                                                           |
| dulwich_log              | 58.5 ms                                                         | 52.4 ms: 1.12x faster                                                           |
| crypto_pyaes             | 81.3 ms                                                         | 73.5 ms: 1.11x faster                                                           |
| xml_etree_parse          | 120 ms                                                          | 109 ms: 1.10x faster                                                            |
| regex_dna                | 131 ms                                                          | 118 ms: 1.10x faster                                                            |
| sqlglot_parse            | 1.33 ms                                                         | 1.21 ms: 1.10x faster                                                           |
| html5lib                 | 52.1 ms                                                         | 47.5 ms: 1.10x faster                                                           |
| regex_effbot             | 1.66 ms                                                         | 1.52 ms: 1.09x faster                                                           |
| json_dumps               | 9.82 ms                                                         | 9.02 ms: 1.09x faster                                                           |
| richards                 | 40.3 ms                                                         | 37.2 ms: 1.08x faster                                                           |
| pycparser                | 1.04 sec                                                        | 970 ms: 1.07x faster                                                            |
| comprehensions           | 17.7 us                                                         | 16.6 us: 1.07x faster                                                           |
| sqlglot_transpile        | 1.58 ms                                                         | 1.49 ms: 1.06x faster                                                           |
| sympy_sum                | 122 ms                                                          | 116 ms: 1.06x faster                                                            |
| tomli_loads              | 1.91 sec                                                        | 1.81 sec: 1.06x faster                                                          |
| xml_etree_iterparse      | 70.8 ms                                                         | 68.1 ms: 1.04x faster                                                           |
| deepcopy_reduce          | 2.68 us                                                         | 2.61 us: 1.03x faster                                                           |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 3.17 ms: 1.02x faster                                                           |
| django_template          | 36.0 ms                                                         | 35.6 ms: 1.01x faster                                                           |
| regex_v8                 | 15.8 ms                                                         | 15.6 ms: 1.01x faster                                                           |
| 2to3                     | 265 ms                                                          | 268 ms: 1.01x slower                                                            |
| regex_compile            | 117 ms                                                          | 118 ms: 1.01x slower                                                            |
| sympy_str                | 229 ms                                                          | 233 ms: 1.02x slower                                                            |
| sympy_integrate          | 16.6 ms                                                         | 16.9 ms: 1.02x slower                                                           |
| docutils                 | 1.95 sec                                                        | 2.01 sec: 1.03x slower                                                          |
| json_loads               | 22.4 us                                                         | 23.1 us: 1.03x slower                                                           |
| mdp                      | 1.83 sec                                                        | 1.89 sec: 1.04x slower                                                          |
| sympy_expand             | 391 ms                                                          | 407 ms: 1.04x slower                                                            |
| genshi_xml               | 46.6 ms                                                         | 51.3 ms: 1.10x slower                                                           |
| sqlglot_optimize         | 44.7 ms                                                         | 50.8 ms: 1.14x slower                                                           |
| pickle_pure_python       | 280 us                                                          | 319 us: 1.14x slower                                                            |
| coverage                 | 46.6 ms                                                         | 53.4 ms: 1.15x slower                                                           |
| logging_simple           | 7.29 us                                                         | 8.39 us: 1.15x slower                                                           |
| xml_etree_process        | 48.1 ms                                                         | 55.7 ms: 1.16x slower                                                           |
| pprint_pformat           | 1.37 sec                                                        | 1.59 sec: 1.16x slower                                                          |
| logging_format           | 7.91 us                                                         | 9.17 us: 1.16x slower                                                           |
| genshi_text              | 21.0 ms                                                         | 24.7 ms: 1.18x slower                                                           |
| fannkuch                 | 317 ms                                                          | 373 ms: 1.18x slower                                                            |
| pprint_safe_repr         | 658 ms                                                          | 775 ms: 1.18x slower                                                            |
| meteor_contest           | 80.0 ms                                                         | 95.1 ms: 1.19x slower                                                           |
| unpickle_pure_python     | 189 us                                                          | 226 us: 1.19x slower                                                            |
| bench_thread_pool        | 1.12 ms                                                         | 1.34 ms: 1.20x slower                                                           |
| nqueens                  | 87.1 ms                                                         | 104 ms: 1.20x slower                                                            |
| python_startup_no_site   | 18.1 ms                                                         | 21.7 ms: 1.20x slower                                                           |
| scimark_fft              | 216 ms                                                          | 261 ms: 1.21x slower                                                            |
| xml_etree_generate       | 61.6 ms                                                         | 74.9 ms: 1.22x slower                                                           |
| python_startup           | 22.9 ms                                                         | 28.2 ms: 1.23x slower                                                           |
| async_generators         | 241 ms                                                          | 322 ms: 1.33x slower                                                            |
| bench_mp_pool            | 66.4 ms                                                         | 89.9 ms: 1.36x slower                                                           |
| gc_traversal             | 1.28 ms                                                         | 1.82 ms: 1.42x slower                                                           |
| nbody                    | 79.1 ms                                                         | 113 ms: 1.43x slower                                                            |
| create_gc_cycles         | 694 us                                                          | 1.06 ms: 1.52x slower                                                           |
| telco                    | 4.83 ms                                                         | 7.68 ms: 1.59x slower                                                           |
| Geometric mean           | (ref)                                                           | 1.08x faster                                                                    |

Benchmark hidden because not significant (2): json, hexiom
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20250212-3.14.0a4+-5cdd6e5-JIT/bm-20250212-pythonperf1_win32-x86-python-5cdd6e5e758a3fc0a5da-3.14.0a4+-5cdd6e5.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.089x faster

# HPT report

- Reliability score: 95.11% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown
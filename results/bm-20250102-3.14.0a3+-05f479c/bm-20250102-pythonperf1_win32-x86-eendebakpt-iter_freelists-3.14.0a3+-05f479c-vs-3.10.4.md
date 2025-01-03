# Results vs. 3.10.4

- fork: eendebakpt
- ref: iter_freelists
- machine: windows-x86
- commit hash: 05f479c
- commit date: 2025-01-02
- overall geometric mean: 1.173x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.09x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250102-pythonperf1_win32-x86-eendebakpt-iter_freelists-3.14.0a3+-05f479c |
|----------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 240 ms: 1.11x faster                                                          |
| docutils       | 1.95 sec                                                        | 1.75 sec: 1.11x faster                                                        |
| html5lib       | 52.1 ms                                                         | 42.4 ms: 1.23x faster                                                         |
| Geometric mean | (ref)                                                           | 1.15x faster                                                                  |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250102-pythonperf1_win32-x86-eendebakpt-iter_freelists-3.14.0a3+-05f479c |
|-------------------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| async_tree_io           | 940 ms                                                          | 424 ms: 2.22x faster                                                          |
| async_tree_cpu_io_mixed | 922 ms                                                          | 435 ms: 2.12x faster                                                          |
| async_tree_none         | 394 ms                                                          | 196 ms: 2.01x faster                                                          |
| async_tree_memoization  | 467 ms                                                          | 237 ms: 1.97x faster                                                          |
| Geometric mean          | (ref)                                                           | 2.08x faster                                                                  |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250102-pythonperf1_win32-x86-eendebakpt-iter_freelists-3.14.0a3+-05f479c |
|----------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 196 ms: 2.57x faster                                                          |
| float          | 69.6 ms                                                         | 56.4 ms: 1.23x faster                                                         |
| nbody          | 79.1 ms                                                         | 85.1 ms: 1.08x slower                                                         |
| Geometric mean | (ref)                                                           | 1.43x faster                                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250102-pythonperf1_win32-x86-eendebakpt-iter_freelists-3.14.0a3+-05f479c |
|----------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| regex_compile  | 117 ms                                                          | 98.6 ms: 1.18x faster                                                         |
| regex_dna      | 131 ms                                                          | 111 ms: 1.18x faster                                                          |
| regex_effbot   | 1.66 ms                                                         | 1.53 ms: 1.08x faster                                                         |
| Geometric mean | (ref)                                                           | 1.10x faster                                                                  |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250102-pythonperf1_win32-x86-eendebakpt-iter_freelists-3.14.0a3+-05f479c |
|----------------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| tomli_loads          | 1.91 sec                                                        | 1.61 sec: 1.19x faster                                                        |
| unpickle_pure_python | 189 us                                                          | 167 us: 1.13x faster                                                          |
| json_dumps           | 9.82 ms                                                         | 8.72 ms: 1.13x faster                                                         |
| xml_etree_parse      | 120 ms                                                          | 107 ms: 1.12x faster                                                          |
| json_loads           | 22.4 us                                                         | 20.6 us: 1.08x faster                                                         |
| pickle_pure_python   | 280 us                                                          | 263 us: 1.07x faster                                                          |
| xml_etree_iterparse  | 70.8 ms                                                         | 66.5 ms: 1.06x faster                                                         |
| xml_etree_process    | 48.1 ms                                                         | 47.2 ms: 1.02x faster                                                         |
| xml_etree_generate   | 61.6 ms                                                         | 64.7 ms: 1.05x slower                                                         |
| Geometric mean       | (ref)                                                           | 1.08x faster                                                                  |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250102-pythonperf1_win32-x86-eendebakpt-iter_freelists-3.14.0a3+-05f479c |
|------------------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| python_startup_no_site | 18.1 ms                                                         | 19.7 ms: 1.09x slower                                                         |
| python_startup         | 22.9 ms                                                         | 25.8 ms: 1.13x slower                                                         |
| Geometric mean         | (ref)                                                           | 1.11x slower                                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250102-pythonperf1_win32-x86-eendebakpt-iter_freelists-3.14.0a3+-05f479c |
|-----------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| mako            | 9.10 ms                                                         | 7.64 ms: 1.19x faster                                                         |
| django_template | 36.0 ms                                                         | 32.5 ms: 1.11x faster                                                         |
| genshi_xml      | 46.6 ms                                                         | 45.3 ms: 1.03x faster                                                         |
| genshi_text     | 21.0 ms                                                         | 20.7 ms: 1.02x faster                                                         |
| Geometric mean  | (ref)                                                           | 1.08x faster                                                                  |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250102-pythonperf1_win32-x86-eendebakpt-iter_freelists-3.14.0a3+-05f479c |
|--------------------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| typing_runtime_protocols | 396 us                                                          | 139 us: 2.84x faster                                                          |
| pidigits                 | 502 ms                                                          | 196 ms: 2.57x faster                                                          |
| async_tree_io            | 940 ms                                                          | 424 ms: 2.22x faster                                                          |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 435 ms: 2.12x faster                                                          |
| async_tree_none          | 394 ms                                                          | 196 ms: 2.01x faster                                                          |
| async_tree_memoization   | 467 ms                                                          | 237 ms: 1.97x faster                                                          |
| pylint                   | 384 ms                                                          | 212 ms: 1.81x faster                                                          |
| deltablue                | 4.04 ms                                                         | 2.54 ms: 1.59x faster                                                         |
| go                       | 146 ms                                                          | 95.7 ms: 1.52x faster                                                         |
| chaos                    | 74.4 ms                                                         | 53.3 ms: 1.40x faster                                                         |
| deepcopy                 | 310 us                                                          | 223 us: 1.39x faster                                                          |
| logging_silent           | 97.9 ns                                                         | 71.4 ns: 1.37x faster                                                         |
| deepcopy_memo            | 29.6 us                                                         | 22.1 us: 1.34x faster                                                         |
| comprehensions           | 17.7 us                                                         | 13.3 us: 1.33x faster                                                         |
| crypto_pyaes             | 81.3 ms                                                         | 61.7 ms: 1.32x faster                                                         |
| scimark_lu               | 89.8 ms                                                         | 68.9 ms: 1.30x faster                                                         |
| generators               | 31.6 ms                                                         | 24.3 ms: 1.30x faster                                                         |
| pycparser                | 1.04 sec                                                        | 803 ms: 1.30x faster                                                          |
| sqlglot_parse            | 1.33 ms                                                         | 1.03 ms: 1.29x faster                                                         |
| sqlglot_transpile        | 1.58 ms                                                         | 1.27 ms: 1.25x faster                                                         |
| thrift                   | 902 us                                                          | 725 us: 1.24x faster                                                          |
| hexiom                   | 6.13 ms                                                         | 4.93 ms: 1.24x faster                                                         |
| pyflate                  | 422 ms                                                          | 339 ms: 1.24x faster                                                          |
| float                    | 69.6 ms                                                         | 56.4 ms: 1.23x faster                                                         |
| html5lib                 | 52.1 ms                                                         | 42.4 ms: 1.23x faster                                                         |
| richards_super           | 49.9 ms                                                         | 40.7 ms: 1.22x faster                                                         |
| nqueens                  | 87.1 ms                                                         | 72.4 ms: 1.20x faster                                                         |
| mako                     | 9.10 ms                                                         | 7.64 ms: 1.19x faster                                                         |
| sqlite_synth             | 2.29 us                                                         | 1.93 us: 1.19x faster                                                         |
| tomli_loads              | 1.91 sec                                                        | 1.61 sec: 1.19x faster                                                        |
| sympy_sum                | 122 ms                                                          | 103 ms: 1.19x faster                                                          |
| raytrace                 | 303 ms                                                          | 255 ms: 1.19x faster                                                          |
| regex_compile            | 117 ms                                                          | 98.6 ms: 1.18x faster                                                         |
| dulwich_log              | 58.5 ms                                                         | 49.6 ms: 1.18x faster                                                         |
| regex_dna                | 131 ms                                                          | 111 ms: 1.18x faster                                                          |
| scimark_monte_carlo      | 61.9 ms                                                         | 53.7 ms: 1.15x faster                                                         |
| deepcopy_reduce          | 2.68 us                                                         | 2.33 us: 1.15x faster                                                         |
| spectral_norm            | 80.2 ms                                                         | 70.1 ms: 1.14x faster                                                         |
| scimark_sor              | 115 ms                                                          | 101 ms: 1.14x faster                                                          |
| richards                 | 40.3 ms                                                         | 35.5 ms: 1.13x faster                                                         |
| unpickle_pure_python     | 189 us                                                          | 167 us: 1.13x faster                                                          |
| json                     | 4.76 ms                                                         | 4.23 ms: 1.13x faster                                                         |
| json_dumps               | 9.82 ms                                                         | 8.72 ms: 1.13x faster                                                         |
| xml_etree_parse          | 120 ms                                                          | 107 ms: 1.12x faster                                                          |
| bench_thread_pool        | 1.12 ms                                                         | 1.00 ms: 1.12x faster                                                         |
| sympy_integrate          | 16.6 ms                                                         | 14.9 ms: 1.12x faster                                                         |
| docutils                 | 1.95 sec                                                        | 1.75 sec: 1.11x faster                                                        |
| django_template          | 36.0 ms                                                         | 32.5 ms: 1.11x faster                                                         |
| sympy_str                | 229 ms                                                          | 207 ms: 1.11x faster                                                          |
| 2to3                     | 265 ms                                                          | 240 ms: 1.11x faster                                                          |
| sqlglot_optimize         | 44.7 ms                                                         | 40.4 ms: 1.11x faster                                                         |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 2.94 ms: 1.10x faster                                                         |
| coroutines               | 17.9 ms                                                         | 16.3 ms: 1.10x faster                                                         |
| sqlglot_normalize        | 230 ms                                                          | 211 ms: 1.09x faster                                                          |
| sympy_expand             | 391 ms                                                          | 360 ms: 1.08x faster                                                          |
| json_loads               | 22.4 us                                                         | 20.6 us: 1.08x faster                                                         |
| regex_effbot             | 1.66 ms                                                         | 1.53 ms: 1.08x faster                                                         |
| mdp                      | 1.83 sec                                                        | 1.69 sec: 1.08x faster                                                        |
| pprint_pformat           | 1.37 sec                                                        | 1.27 sec: 1.07x faster                                                        |
| pprint_safe_repr         | 658 ms                                                          | 616 ms: 1.07x faster                                                          |
| pickle_pure_python       | 280 us                                                          | 263 us: 1.07x faster                                                          |
| xml_etree_iterparse      | 70.8 ms                                                         | 66.5 ms: 1.06x faster                                                         |
| fannkuch                 | 317 ms                                                          | 308 ms: 1.03x faster                                                          |
| genshi_xml               | 46.6 ms                                                         | 45.3 ms: 1.03x faster                                                         |
| xml_etree_process        | 48.1 ms                                                         | 47.2 ms: 1.02x faster                                                         |
| genshi_text              | 21.0 ms                                                         | 20.7 ms: 1.02x faster                                                         |
| scimark_fft              | 216 ms                                                          | 214 ms: 1.01x faster                                                          |
| meteor_contest           | 80.0 ms                                                         | 80.3 ms: 1.00x slower                                                         |
| pathlib                  | 81.2 ms                                                         | 83.5 ms: 1.03x slower                                                         |
| xml_etree_generate       | 61.6 ms                                                         | 64.7 ms: 1.05x slower                                                         |
| logging_simple           | 7.29 us                                                         | 7.76 us: 1.06x slower                                                         |
| logging_format           | 7.91 us                                                         | 8.44 us: 1.07x slower                                                         |
| nbody                    | 79.1 ms                                                         | 85.1 ms: 1.08x slower                                                         |
| python_startup_no_site   | 18.1 ms                                                         | 19.7 ms: 1.09x slower                                                         |
| python_startup           | 22.9 ms                                                         | 25.8 ms: 1.13x slower                                                         |
| mypy2                    | 590 ms                                                          | 672 ms: 1.14x slower                                                          |
| coverage                 | 46.6 ms                                                         | 53.1 ms: 1.14x slower                                                         |
| async_generators         | 241 ms                                                          | 295 ms: 1.22x slower                                                          |
| bench_mp_pool            | 66.4 ms                                                         | 86.8 ms: 1.31x slower                                                         |
| telco                    | 4.83 ms                                                         | 6.36 ms: 1.32x slower                                                         |
| gc_traversal             | 1.28 ms                                                         | 1.77 ms: 1.38x slower                                                         |
| create_gc_cycles         | 694 us                                                          | 1.05 ms: 1.51x slower                                                         |
| Geometric mean           | (ref)                                                           | 1.17x faster                                                                  |

Benchmark hidden because not significant (1): regex_v8
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20250102-3.14.0a3+-05f479c/bm-20250102-pythonperf1_win32-x86-eendebakpt-iter_freelists-3.14.0a3+-05f479c.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.173x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.10x
- 95% likely to have a speedup of 1.10x
- 99% likely to have a speedup of 1.09x

# Memory
- memory change: unknown
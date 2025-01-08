# Results vs. 3.10.4

- fork: brandtbucher
- ref: nojit
- machine: windows-x86
- commit hash: f098037
- commit date: 2025-01-07
- overall geometric mean: 1.064x faster
- HPT reliability: 84.18%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250107-pythonperf1_win32-x86-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 263 ms: 1.01x faster                                                   |
| html5lib       | 52.1 ms                                                         | 47.6 ms: 1.09x faster                                                  |
| Geometric mean | (ref)                                                           | 1.03x faster                                                           |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250107-pythonperf1_win32-x86-brandtbucher-nojit-3.14.0a3+-f098037 |
|-------------------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io           | 940 ms                                                          | 470 ms: 2.00x faster                                                   |
| async_tree_cpu_io_mixed | 922 ms                                                          | 473 ms: 1.95x faster                                                   |
| async_tree_none         | 394 ms                                                          | 223 ms: 1.77x faster                                                   |
| async_tree_memoization  | 467 ms                                                          | 273 ms: 1.71x faster                                                   |
| Geometric mean          | (ref)                                                           | 1.85x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250107-pythonperf1_win32-x86-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 201 ms: 2.50x faster                                                   |
| float          | 69.6 ms                                                         | 52.2 ms: 1.33x faster                                                  |
| nbody          | 79.1 ms                                                         | 102 ms: 1.29x slower                                                   |
| Geometric mean | (ref)                                                           | 1.37x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250107-pythonperf1_win32-x86-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_dna      | 131 ms                                                          | 124 ms: 1.05x faster                                                   |
| regex_compile  | 117 ms                                                          | 112 ms: 1.04x faster                                                   |
| regex_effbot   | 1.66 ms                                                         | 1.65 ms: 1.01x faster                                                  |
| regex_v8       | 15.8 ms                                                         | 15.7 ms: 1.01x faster                                                  |
| Geometric mean | (ref)                                                           | 1.03x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250107-pythonperf1_win32-x86-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------:|
| xml_etree_parse      | 120 ms                                                          | 107 ms: 1.12x faster                                                   |
| tomli_loads          | 1.91 sec                                                        | 1.76 sec: 1.09x faster                                                 |
| json_loads           | 22.4 us                                                         | 20.6 us: 1.09x faster                                                  |
| json_dumps           | 9.82 ms                                                         | 9.18 ms: 1.07x faster                                                  |
| xml_etree_iterparse  | 70.8 ms                                                         | 66.6 ms: 1.06x faster                                                  |
| pickle_pure_python   | 280 us                                                          | 294 us: 1.05x slower                                                   |
| unpickle_pure_python | 189 us                                                          | 203 us: 1.07x slower                                                   |
| xml_etree_process    | 48.1 ms                                                         | 53.3 ms: 1.11x slower                                                  |
| xml_etree_generate   | 61.6 ms                                                         | 72.8 ms: 1.18x slower                                                  |
| Geometric mean       | (ref)                                                           | 1.00x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250107-pythonperf1_win32-x86-brandtbucher-nojit-3.14.0a3+-f098037 |
|------------------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 18.1 ms                                                         | 19.1 ms: 1.06x slower                                                  |
| python_startup         | 22.9 ms                                                         | 25.7 ms: 1.12x slower                                                  |
| Geometric mean         | (ref)                                                           | 1.09x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250107-pythonperf1_win32-x86-brandtbucher-nojit-3.14.0a3+-f098037 |
|-----------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 9.10 ms                                                         | 7.59 ms: 1.20x faster                                                  |
| django_template | 36.0 ms                                                         | 36.8 ms: 1.02x slower                                                  |
| genshi_xml      | 46.6 ms                                                         | 55.1 ms: 1.18x slower                                                  |
| genshi_text     | 21.0 ms                                                         | 26.0 ms: 1.24x slower                                                  |
| Geometric mean  | (ref)                                                           | 1.06x slower                                                           |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250107-pythonperf1_win32-x86-brandtbucher-nojit-3.14.0a3+-f098037 |
|--------------------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------:|
| pidigits                 | 502 ms                                                          | 201 ms: 2.50x faster                                                   |
| typing_runtime_protocols | 396 us                                                          | 159 us: 2.49x faster                                                   |
| sqlglot_normalize        | 230 ms                                                          | 105 ms: 2.20x faster                                                   |
| async_tree_io            | 940 ms                                                          | 470 ms: 2.00x faster                                                   |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 473 ms: 1.95x faster                                                   |
| async_tree_none          | 394 ms                                                          | 223 ms: 1.77x faster                                                   |
| async_tree_memoization   | 467 ms                                                          | 273 ms: 1.71x faster                                                   |
| pylint                   | 384 ms                                                          | 234 ms: 1.64x faster                                                   |
| float                    | 69.6 ms                                                         | 52.2 ms: 1.33x faster                                                  |
| deepcopy_memo            | 29.6 us                                                         | 22.8 us: 1.30x faster                                                  |
| deltablue                | 4.04 ms                                                         | 3.17 ms: 1.27x faster                                                  |
| scimark_sor              | 115 ms                                                          | 92.7 ms: 1.24x faster                                                  |
| scimark_lu               | 89.8 ms                                                         | 72.5 ms: 1.24x faster                                                  |
| mako                     | 9.10 ms                                                         | 7.59 ms: 1.20x faster                                                  |
| sqlite_synth             | 2.29 us                                                         | 1.92 us: 1.19x faster                                                  |
| crypto_pyaes             | 81.3 ms                                                         | 68.9 ms: 1.18x faster                                                  |
| go                       | 146 ms                                                          | 124 ms: 1.18x faster                                                   |
| logging_silent           | 97.9 ns                                                         | 84.3 ns: 1.16x faster                                                  |
| sqlglot_parse            | 1.33 ms                                                         | 1.15 ms: 1.16x faster                                                  |
| dulwich_log              | 58.5 ms                                                         | 50.5 ms: 1.16x faster                                                  |
| thrift                   | 902 us                                                          | 780 us: 1.16x faster                                                   |
| chaos                    | 74.4 ms                                                         | 64.7 ms: 1.15x faster                                                  |
| deepcopy                 | 310 us                                                          | 273 us: 1.14x faster                                                   |
| xml_etree_parse          | 120 ms                                                          | 107 ms: 1.12x faster                                                   |
| sqlglot_transpile        | 1.58 ms                                                         | 1.42 ms: 1.11x faster                                                  |
| pycparser                | 1.04 sec                                                        | 943 ms: 1.10x faster                                                   |
| json                     | 4.76 ms                                                         | 4.34 ms: 1.10x faster                                                  |
| html5lib                 | 52.1 ms                                                         | 47.6 ms: 1.09x faster                                                  |
| tomli_loads              | 1.91 sec                                                        | 1.76 sec: 1.09x faster                                                 |
| json_loads               | 22.4 us                                                         | 20.6 us: 1.09x faster                                                  |
| sympy_sum                | 122 ms                                                          | 114 ms: 1.08x faster                                                   |
| bench_thread_pool        | 1.12 ms                                                         | 1.04 ms: 1.07x faster                                                  |
| spectral_norm            | 80.2 ms                                                         | 74.7 ms: 1.07x faster                                                  |
| json_dumps               | 9.82 ms                                                         | 9.18 ms: 1.07x faster                                                  |
| coroutines               | 17.9 ms                                                         | 16.8 ms: 1.07x faster                                                  |
| xml_etree_iterparse      | 70.8 ms                                                         | 66.6 ms: 1.06x faster                                                  |
| pyflate                  | 422 ms                                                          | 399 ms: 1.06x faster                                                   |
| regex_dna                | 131 ms                                                          | 124 ms: 1.05x faster                                                   |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 3.08 ms: 1.05x faster                                                  |
| regex_compile            | 117 ms                                                          | 112 ms: 1.04x faster                                                   |
| richards_super           | 49.9 ms                                                         | 48.1 ms: 1.04x faster                                                  |
| 2to3                     | 265 ms                                                          | 263 ms: 1.01x faster                                                   |
| regex_effbot             | 1.66 ms                                                         | 1.65 ms: 1.01x faster                                                  |
| regex_v8                 | 15.8 ms                                                         | 15.7 ms: 1.01x faster                                                  |
| mdp                      | 1.83 sec                                                        | 1.84 sec: 1.01x slower                                                 |
| raytrace                 | 303 ms                                                          | 307 ms: 1.02x slower                                                   |
| sympy_str                | 229 ms                                                          | 233 ms: 1.02x slower                                                   |
| pathlib                  | 81.2 ms                                                         | 82.9 ms: 1.02x slower                                                  |
| django_template          | 36.0 ms                                                         | 36.8 ms: 1.02x slower                                                  |
| sympy_integrate          | 16.6 ms                                                         | 17.3 ms: 1.04x slower                                                  |
| deepcopy_reduce          | 2.68 us                                                         | 2.79 us: 1.04x slower                                                  |
| sympy_expand             | 391 ms                                                          | 406 ms: 1.04x slower                                                   |
| comprehensions           | 17.7 us                                                         | 18.5 us: 1.04x slower                                                  |
| pickle_pure_python       | 280 us                                                          | 294 us: 1.05x slower                                                   |
| fannkuch                 | 317 ms                                                          | 334 ms: 1.05x slower                                                   |
| python_startup_no_site   | 18.1 ms                                                         | 19.1 ms: 1.06x slower                                                  |
| unpickle_pure_python     | 189 us                                                          | 203 us: 1.07x slower                                                   |
| richards                 | 40.3 ms                                                         | 43.5 ms: 1.08x slower                                                  |
| pprint_pformat           | 1.37 sec                                                        | 1.49 sec: 1.09x slower                                                 |
| meteor_contest           | 80.0 ms                                                         | 88.3 ms: 1.10x slower                                                  |
| nqueens                  | 87.1 ms                                                         | 96.5 ms: 1.11x slower                                                  |
| xml_etree_process        | 48.1 ms                                                         | 53.3 ms: 1.11x slower                                                  |
| scimark_fft              | 216 ms                                                          | 240 ms: 1.11x slower                                                   |
| pprint_safe_repr         | 658 ms                                                          | 733 ms: 1.11x slower                                                   |
| coverage                 | 46.6 ms                                                         | 51.9 ms: 1.11x slower                                                  |
| python_startup           | 22.9 ms                                                         | 25.7 ms: 1.12x slower                                                  |
| sqlglot_optimize         | 44.7 ms                                                         | 50.1 ms: 1.12x slower                                                  |
| hexiom                   | 6.13 ms                                                         | 7.10 ms: 1.16x slower                                                  |
| logging_format           | 7.91 us                                                         | 9.18 us: 1.16x slower                                                  |
| logging_simple           | 7.29 us                                                         | 8.54 us: 1.17x slower                                                  |
| xml_etree_generate       | 61.6 ms                                                         | 72.8 ms: 1.18x slower                                                  |
| genshi_xml               | 46.6 ms                                                         | 55.1 ms: 1.18x slower                                                  |
| generators               | 31.6 ms                                                         | 37.6 ms: 1.19x slower                                                  |
| mypy2                    | 590 ms                                                          | 727 ms: 1.23x slower                                                   |
| genshi_text              | 21.0 ms                                                         | 26.0 ms: 1.24x slower                                                  |
| nbody                    | 79.1 ms                                                         | 102 ms: 1.29x slower                                                   |
| bench_mp_pool            | 66.4 ms                                                         | 87.4 ms: 1.32x slower                                                  |
| async_generators         | 241 ms                                                          | 326 ms: 1.35x slower                                                   |
| gc_traversal             | 1.28 ms                                                         | 1.82 ms: 1.42x slower                                                  |
| telco                    | 4.83 ms                                                         | 7.18 ms: 1.49x slower                                                  |
| create_gc_cycles         | 694 us                                                          | 1.06 ms: 1.53x slower                                                  |
| Geometric mean           | (ref)                                                           | 1.06x faster                                                           |

Benchmark hidden because not significant (2): scimark_monte_carlo, docutils
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20250107-3.14.0a3+-f098037-JIT/bm-20250107-pythonperf1_win32-x86-brandtbucher-nojit-3.14.0a3+-f098037.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.064x faster

# HPT report

- Reliability score: 84.18% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown
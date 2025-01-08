# Results vs. 3.10.4

- fork: brandtbucher
- ref: nojit
- machine: windows-x86
- commit hash: f098037
- commit date: 2025-01-07
- overall geometric mean: 1.153x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250107-pythonperf1_win32-x86-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 247 ms: 1.08x faster                                                   |
| docutils       | 1.95 sec                                                        | 1.84 sec: 1.06x faster                                                 |
| html5lib       | 52.1 ms                                                         | 44.7 ms: 1.17x faster                                                  |
| Geometric mean | (ref)                                                           | 1.10x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250107-pythonperf1_win32-x86-brandtbucher-nojit-3.14.0a3+-f098037 |
|-------------------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io           | 940 ms                                                          | 446 ms: 2.11x faster                                                   |
| async_tree_cpu_io_mixed | 922 ms                                                          | 451 ms: 2.05x faster                                                   |
| async_tree_none         | 394 ms                                                          | 208 ms: 1.89x faster                                                   |
| async_tree_memoization  | 467 ms                                                          | 254 ms: 1.84x faster                                                   |
| Geometric mean          | (ref)                                                           | 1.97x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250107-pythonperf1_win32-x86-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 197 ms: 2.54x faster                                                   |
| float          | 69.6 ms                                                         | 55.6 ms: 1.25x faster                                                  |
| nbody          | 79.1 ms                                                         | 89.2 ms: 1.13x slower                                                  |
| Geometric mean | (ref)                                                           | 1.41x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250107-pythonperf1_win32-x86-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 117 ms                                                          | 104 ms: 1.12x faster                                                   |
| regex_effbot   | 1.66 ms                                                         | 1.57 ms: 1.06x faster                                                  |
| regex_dna      | 131 ms                                                          | 124 ms: 1.05x faster                                                   |
| regex_v8       | 15.8 ms                                                         | 17.4 ms: 1.11x slower                                                  |
| Geometric mean | (ref)                                                           | 1.03x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250107-pythonperf1_win32-x86-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------:|
| tomli_loads          | 1.91 sec                                                        | 1.58 sec: 1.21x faster                                                 |
| unpickle_pure_python | 189 us                                                          | 166 us: 1.14x faster                                                   |
| json_dumps           | 9.82 ms                                                         | 8.76 ms: 1.12x faster                                                  |
| xml_etree_parse      | 120 ms                                                          | 108 ms: 1.11x faster                                                   |
| pickle_pure_python   | 280 us                                                          | 258 us: 1.08x faster                                                   |
| json_loads           | 22.4 us                                                         | 20.7 us: 1.08x faster                                                  |
| xml_etree_iterparse  | 70.8 ms                                                         | 66.7 ms: 1.06x faster                                                  |
| xml_etree_process    | 48.1 ms                                                         | 48.8 ms: 1.01x slower                                                  |
| xml_etree_generate   | 61.6 ms                                                         | 68.0 ms: 1.10x slower                                                  |
| Geometric mean       | (ref)                                                           | 1.07x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250107-pythonperf1_win32-x86-brandtbucher-nojit-3.14.0a3+-f098037 |
|------------------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 18.1 ms                                                         | 19.1 ms: 1.06x slower                                                  |
| python_startup         | 22.9 ms                                                         | 25.4 ms: 1.11x slower                                                  |
| Geometric mean         | (ref)                                                           | 1.08x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250107-pythonperf1_win32-x86-brandtbucher-nojit-3.14.0a3+-f098037 |
|-----------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 9.10 ms                                                         | 7.74 ms: 1.18x faster                                                  |
| django_template | 36.0 ms                                                         | 33.3 ms: 1.08x faster                                                  |
| genshi_xml      | 46.6 ms                                                         | 44.8 ms: 1.04x faster                                                  |
| genshi_text     | 21.0 ms                                                         | 21.1 ms: 1.01x slower                                                  |
| Geometric mean  | (ref)                                                           | 1.07x faster                                                           |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250107-pythonperf1_win32-x86-brandtbucher-nojit-3.14.0a3+-f098037 |
|--------------------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------:|
| typing_runtime_protocols | 396 us                                                          | 140 us: 2.83x faster                                                   |
| pidigits                 | 502 ms                                                          | 197 ms: 2.54x faster                                                   |
| async_tree_io            | 940 ms                                                          | 446 ms: 2.11x faster                                                   |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 451 ms: 2.05x faster                                                   |
| async_tree_none          | 394 ms                                                          | 208 ms: 1.89x faster                                                   |
| async_tree_memoization   | 467 ms                                                          | 254 ms: 1.84x faster                                                   |
| pylint                   | 384 ms                                                          | 219 ms: 1.75x faster                                                   |
| deltablue                | 4.04 ms                                                         | 2.68 ms: 1.51x faster                                                  |
| go                       | 146 ms                                                          | 97.4 ms: 1.50x faster                                                  |
| deepcopy_memo            | 29.6 us                                                         | 20.7 us: 1.43x faster                                                  |
| deepcopy                 | 310 us                                                          | 225 us: 1.38x faster                                                   |
| chaos                    | 74.4 ms                                                         | 54.0 ms: 1.38x faster                                                  |
| comprehensions           | 17.7 us                                                         | 13.2 us: 1.35x faster                                                  |
| logging_silent           | 97.9 ns                                                         | 73.6 ns: 1.33x faster                                                  |
| scimark_lu               | 89.8 ms                                                         | 68.2 ms: 1.32x faster                                                  |
| crypto_pyaes             | 81.3 ms                                                         | 63.0 ms: 1.29x faster                                                  |
| generators               | 31.6 ms                                                         | 24.7 ms: 1.28x faster                                                  |
| hexiom                   | 6.13 ms                                                         | 4.88 ms: 1.26x faster                                                  |
| sqlglot_parse            | 1.33 ms                                                         | 1.06 ms: 1.25x faster                                                  |
| float                    | 69.6 ms                                                         | 55.6 ms: 1.25x faster                                                  |
| scimark_sor              | 115 ms                                                          | 93.1 ms: 1.24x faster                                                  |
| thrift                   | 902 us                                                          | 732 us: 1.23x faster                                                   |
| scimark_monte_carlo      | 61.9 ms                                                         | 50.5 ms: 1.23x faster                                                  |
| sqlglot_transpile        | 1.58 ms                                                         | 1.29 ms: 1.22x faster                                                  |
| tomli_loads              | 1.91 sec                                                        | 1.58 sec: 1.21x faster                                                 |
| pyflate                  | 422 ms                                                          | 349 ms: 1.21x faster                                                   |
| richards_super           | 49.9 ms                                                         | 41.5 ms: 1.20x faster                                                  |
| raytrace                 | 303 ms                                                          | 252 ms: 1.20x faster                                                   |
| mako                     | 9.10 ms                                                         | 7.74 ms: 1.18x faster                                                  |
| html5lib                 | 52.1 ms                                                         | 44.7 ms: 1.17x faster                                                  |
| sympy_sum                | 122 ms                                                          | 105 ms: 1.16x faster                                                   |
| sqlite_synth             | 2.29 us                                                         | 1.98 us: 1.16x faster                                                  |
| nqueens                  | 87.1 ms                                                         | 75.2 ms: 1.16x faster                                                  |
| spectral_norm            | 80.2 ms                                                         | 69.3 ms: 1.16x faster                                                  |
| pycparser                | 1.04 sec                                                        | 900 ms: 1.16x faster                                                   |
| dulwich_log              | 58.5 ms                                                         | 50.7 ms: 1.15x faster                                                  |
| unpickle_pure_python     | 189 us                                                          | 166 us: 1.14x faster                                                   |
| richards                 | 40.3 ms                                                         | 35.6 ms: 1.13x faster                                                  |
| json                     | 4.76 ms                                                         | 4.22 ms: 1.13x faster                                                  |
| deepcopy_reduce          | 2.68 us                                                         | 2.38 us: 1.13x faster                                                  |
| bench_thread_pool        | 1.12 ms                                                         | 997 us: 1.12x faster                                                   |
| regex_compile            | 117 ms                                                          | 104 ms: 1.12x faster                                                   |
| json_dumps               | 9.82 ms                                                         | 8.76 ms: 1.12x faster                                                  |
| xml_etree_parse          | 120 ms                                                          | 108 ms: 1.11x faster                                                   |
| coroutines               | 17.9 ms                                                         | 16.5 ms: 1.09x faster                                                  |
| pickle_pure_python       | 280 us                                                          | 258 us: 1.08x faster                                                   |
| django_template          | 36.0 ms                                                         | 33.3 ms: 1.08x faster                                                  |
| sqlglot_optimize         | 44.7 ms                                                         | 41.3 ms: 1.08x faster                                                  |
| json_loads               | 22.4 us                                                         | 20.7 us: 1.08x faster                                                  |
| sqlglot_normalize        | 230 ms                                                          | 214 ms: 1.08x faster                                                   |
| 2to3                     | 265 ms                                                          | 247 ms: 1.08x faster                                                   |
| sympy_integrate          | 16.6 ms                                                         | 15.6 ms: 1.07x faster                                                  |
| sympy_str                | 229 ms                                                          | 215 ms: 1.07x faster                                                   |
| xml_etree_iterparse      | 70.8 ms                                                         | 66.7 ms: 1.06x faster                                                  |
| mdp                      | 1.83 sec                                                        | 1.72 sec: 1.06x faster                                                 |
| docutils                 | 1.95 sec                                                        | 1.84 sec: 1.06x faster                                                 |
| regex_effbot             | 1.66 ms                                                         | 1.57 ms: 1.06x faster                                                  |
| regex_dna                | 131 ms                                                          | 124 ms: 1.05x faster                                                   |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 3.08 ms: 1.05x faster                                                  |
| pprint_pformat           | 1.37 sec                                                        | 1.31 sec: 1.04x faster                                                 |
| genshi_xml               | 46.6 ms                                                         | 44.8 ms: 1.04x faster                                                  |
| pprint_safe_repr         | 658 ms                                                          | 637 ms: 1.03x faster                                                   |
| sympy_expand             | 391 ms                                                          | 378 ms: 1.03x faster                                                   |
| fannkuch                 | 317 ms                                                          | 309 ms: 1.03x faster                                                   |
| meteor_contest           | 80.0 ms                                                         | 79.6 ms: 1.00x faster                                                  |
| genshi_text              | 21.0 ms                                                         | 21.1 ms: 1.01x slower                                                  |
| xml_etree_process        | 48.1 ms                                                         | 48.8 ms: 1.01x slower                                                  |
| pathlib                  | 81.2 ms                                                         | 83.7 ms: 1.03x slower                                                  |
| python_startup_no_site   | 18.1 ms                                                         | 19.1 ms: 1.06x slower                                                  |
| scimark_fft              | 216 ms                                                          | 229 ms: 1.06x slower                                                   |
| logging_simple           | 7.29 us                                                         | 7.87 us: 1.08x slower                                                  |
| logging_format           | 7.91 us                                                         | 8.62 us: 1.09x slower                                                  |
| xml_etree_generate       | 61.6 ms                                                         | 68.0 ms: 1.10x slower                                                  |
| python_startup           | 22.9 ms                                                         | 25.4 ms: 1.11x slower                                                  |
| regex_v8                 | 15.8 ms                                                         | 17.4 ms: 1.11x slower                                                  |
| coverage                 | 46.6 ms                                                         | 52.4 ms: 1.13x slower                                                  |
| nbody                    | 79.1 ms                                                         | 89.2 ms: 1.13x slower                                                  |
| mypy2                    | 590 ms                                                          | 695 ms: 1.18x slower                                                   |
| async_generators         | 241 ms                                                          | 295 ms: 1.23x slower                                                   |
| bench_mp_pool            | 66.4 ms                                                         | 87.3 ms: 1.32x slower                                                  |
| telco                    | 4.83 ms                                                         | 6.71 ms: 1.39x slower                                                  |
| gc_traversal             | 1.28 ms                                                         | 1.78 ms: 1.39x slower                                                  |
| create_gc_cycles         | 694 us                                                          | 1.06 ms: 1.53x slower                                                  |
| Geometric mean           | (ref)                                                           | 1.15x faster                                                           |
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20250107-3.14.0a3+-f098037/bm-20250107-pythonperf1_win32-x86-brandtbucher-nojit-3.14.0a3+-f098037.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.153x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.07x
- 95% likely to have a speedup of 1.07x
- 99% likely to have a speedup of 1.06x

# Memory
- memory change: unknown
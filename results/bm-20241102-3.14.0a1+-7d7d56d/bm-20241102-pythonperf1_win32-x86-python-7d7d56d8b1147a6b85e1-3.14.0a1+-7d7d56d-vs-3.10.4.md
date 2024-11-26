# Results vs. 3.10.4

- fork: python
- ref: 7d7d56d8b1147a6b85e1
- machine: windows-x86
- commit hash: 7d7d56d
- commit date: 2024-11-02
- overall geometric mean: 1.135x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241102-pythonperf1_win32-x86-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 244 ms: 1.09x faster                                                            |
| docutils       | 1.95 sec                                                        | 1.82 sec: 1.07x faster                                                          |
| html5lib       | 52.1 ms                                                         | 44.5 ms: 1.17x faster                                                           |
| tornado_http   | 118 ms                                                          | 106 ms: 1.11x faster                                                            |
| Geometric mean | (ref)                                                           | 1.11x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241102-pythonperf1_win32-x86-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d |
|-------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 922 ms                                                          | 482 ms: 1.91x faster                                                            |
| async_tree_io           | 940 ms                                                          | 519 ms: 1.81x faster                                                            |
| async_tree_none         | 394 ms                                                          | 220 ms: 1.79x faster                                                            |
| async_tree_memoization  | 467 ms                                                          | 274 ms: 1.71x faster                                                            |
| Geometric mean          | (ref)                                                           | 1.80x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241102-pythonperf1_win32-x86-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 202 ms: 2.49x faster                                                            |
| float          | 69.6 ms                                                         | 60.5 ms: 1.15x faster                                                           |
| nbody          | 79.1 ms                                                         | 84.6 ms: 1.07x slower                                                           |
| Geometric mean | (ref)                                                           | 1.39x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241102-pythonperf1_win32-x86-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_dna      | 131 ms                                                          | 116 ms: 1.13x faster                                                            |
| regex_compile  | 117 ms                                                          | 105 ms: 1.11x faster                                                            |
| regex_v8       | 15.8 ms                                                         | 16.0 ms: 1.02x slower                                                           |
| regex_effbot   | 1.66 ms                                                         | 1.82 ms: 1.10x slower                                                           |
| Geometric mean | (ref)                                                           | 1.03x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241102-pythonperf1_win32-x86-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| unpickle_pure_python | 189 us                                                          | 165 us: 1.15x faster                                                            |
| json_dumps           | 9.82 ms                                                         | 9.07 ms: 1.08x faster                                                           |
| xml_etree_parse      | 120 ms                                                          | 111 ms: 1.08x faster                                                            |
| pickle_pure_python   | 280 us                                                          | 260 us: 1.08x faster                                                            |
| tomli_loads          | 1.91 sec                                                        | 1.77 sec: 1.08x faster                                                          |
| json_loads           | 22.4 us                                                         | 20.9 us: 1.07x faster                                                           |
| xml_etree_iterparse  | 70.8 ms                                                         | 67.9 ms: 1.04x faster                                                           |
| xml_etree_process    | 48.1 ms                                                         | 50.5 ms: 1.05x slower                                                           |
| xml_etree_generate   | 61.6 ms                                                         | 68.3 ms: 1.11x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.05x faster                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241102-pythonperf1_win32-x86-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 18.1 ms                                                         | 19.4 ms: 1.07x slower                                                           |
| python_startup         | 22.9 ms                                                         | 25.8 ms: 1.13x slower                                                           |
| Geometric mean         | (ref)                                                           | 1.10x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241102-pythonperf1_win32-x86-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 9.10 ms                                                         | 7.59 ms: 1.20x faster                                                           |
| django_template | 36.0 ms                                                         | 34.0 ms: 1.06x faster                                                           |
| genshi_text     | 21.0 ms                                                         | 21.1 ms: 1.00x slower                                                           |
| genshi_xml      | 46.6 ms                                                         | 48.5 ms: 1.04x slower                                                           |
| Geometric mean  | (ref)                                                           | 1.05x faster                                                                    |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241102-pythonperf1_win32-x86-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d |
|--------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| typing_runtime_protocols | 396 us                                                          | 141 us: 2.81x faster                                                            |
| pidigits                 | 502 ms                                                          | 202 ms: 2.49x faster                                                            |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 482 ms: 1.91x faster                                                            |
| async_tree_io            | 940 ms                                                          | 519 ms: 1.81x faster                                                            |
| async_tree_none          | 394 ms                                                          | 220 ms: 1.79x faster                                                            |
| async_tree_memoization   | 467 ms                                                          | 274 ms: 1.71x faster                                                            |
| pylint                   | 384 ms                                                          | 229 ms: 1.67x faster                                                            |
| deltablue                | 4.04 ms                                                         | 2.65 ms: 1.52x faster                                                           |
| go                       | 146 ms                                                          | 97.0 ms: 1.50x faster                                                           |
| logging_silent           | 97.9 ns                                                         | 67.8 ns: 1.44x faster                                                           |
| deepcopy_memo            | 29.6 us                                                         | 21.1 us: 1.40x faster                                                           |
| crypto_pyaes             | 81.3 ms                                                         | 58.9 ms: 1.38x faster                                                           |
| generators               | 31.6 ms                                                         | 23.7 ms: 1.33x faster                                                           |
| scimark_lu               | 89.8 ms                                                         | 67.8 ms: 1.32x faster                                                           |
| chaos                    | 74.4 ms                                                         | 56.4 ms: 1.32x faster                                                           |
| deepcopy                 | 310 us                                                          | 239 us: 1.30x faster                                                            |
| comprehensions           | 17.7 us                                                         | 13.8 us: 1.28x faster                                                           |
| sqlglot_parse            | 1.33 ms                                                         | 1.04 ms: 1.27x faster                                                           |
| hexiom                   | 6.13 ms                                                         | 4.93 ms: 1.25x faster                                                           |
| pycparser                | 1.04 sec                                                        | 843 ms: 1.24x faster                                                            |
| sqlglot_transpile        | 1.58 ms                                                         | 1.29 ms: 1.22x faster                                                           |
| mako                     | 9.10 ms                                                         | 7.59 ms: 1.20x faster                                                           |
| raytrace                 | 303 ms                                                          | 253 ms: 1.20x faster                                                            |
| thrift                   | 902 us                                                          | 759 us: 1.19x faster                                                            |
| pyflate                  | 422 ms                                                          | 358 ms: 1.18x faster                                                            |
| html5lib                 | 52.1 ms                                                         | 44.5 ms: 1.17x faster                                                           |
| sqlite_synth             | 2.29 us                                                         | 1.97 us: 1.16x faster                                                           |
| sympy_sum                | 122 ms                                                          | 105 ms: 1.16x faster                                                            |
| richards_super           | 49.9 ms                                                         | 43.0 ms: 1.16x faster                                                           |
| float                    | 69.6 ms                                                         | 60.5 ms: 1.15x faster                                                           |
| unpickle_pure_python     | 189 us                                                          | 165 us: 1.15x faster                                                            |
| scimark_sor              | 115 ms                                                          | 100 ms: 1.15x faster                                                            |
| regex_dna                | 131 ms                                                          | 116 ms: 1.13x faster                                                            |
| dulwich_log              | 58.5 ms                                                         | 52.0 ms: 1.13x faster                                                           |
| regex_compile            | 117 ms                                                          | 105 ms: 1.11x faster                                                            |
| bench_thread_pool        | 1.12 ms                                                         | 1.01 ms: 1.11x faster                                                           |
| tornado_http             | 118 ms                                                          | 106 ms: 1.11x faster                                                            |
| scimark_monte_carlo      | 61.9 ms                                                         | 56.1 ms: 1.10x faster                                                           |
| sympy_integrate          | 16.6 ms                                                         | 15.1 ms: 1.10x faster                                                           |
| json                     | 4.76 ms                                                         | 4.34 ms: 1.10x faster                                                           |
| coroutines               | 17.9 ms                                                         | 16.3 ms: 1.10x faster                                                           |
| mdp                      | 1.83 sec                                                        | 1.67 sec: 1.09x faster                                                          |
| 2to3                     | 265 ms                                                          | 244 ms: 1.09x faster                                                            |
| json_dumps               | 9.82 ms                                                         | 9.07 ms: 1.08x faster                                                           |
| spectral_norm            | 80.2 ms                                                         | 74.1 ms: 1.08x faster                                                           |
| richards                 | 40.3 ms                                                         | 37.2 ms: 1.08x faster                                                           |
| xml_etree_parse          | 120 ms                                                          | 111 ms: 1.08x faster                                                            |
| pickle_pure_python       | 280 us                                                          | 260 us: 1.08x faster                                                            |
| tomli_loads              | 1.91 sec                                                        | 1.77 sec: 1.08x faster                                                          |
| sympy_str                | 229 ms                                                          | 213 ms: 1.07x faster                                                            |
| docutils                 | 1.95 sec                                                        | 1.82 sec: 1.07x faster                                                          |
| json_loads               | 22.4 us                                                         | 20.9 us: 1.07x faster                                                           |
| nqueens                  | 87.1 ms                                                         | 81.6 ms: 1.07x faster                                                           |
| fannkuch                 | 317 ms                                                          | 299 ms: 1.06x faster                                                            |
| django_template          | 36.0 ms                                                         | 34.0 ms: 1.06x faster                                                           |
| xml_etree_iterparse      | 70.8 ms                                                         | 67.9 ms: 1.04x faster                                                           |
| sympy_expand             | 391 ms                                                          | 375 ms: 1.04x faster                                                            |
| sqlglot_optimize         | 44.7 ms                                                         | 43.0 ms: 1.04x faster                                                           |
| deepcopy_reduce          | 2.68 us                                                         | 2.61 us: 1.03x faster                                                           |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 3.17 ms: 1.02x faster                                                           |
| pprint_safe_repr         | 658 ms                                                          | 647 ms: 1.02x faster                                                            |
| pprint_pformat           | 1.37 sec                                                        | 1.35 sec: 1.02x faster                                                          |
| sqlglot_normalize        | 230 ms                                                          | 228 ms: 1.01x faster                                                            |
| genshi_text              | 21.0 ms                                                         | 21.1 ms: 1.00x slower                                                           |
| meteor_contest           | 80.0 ms                                                         | 81.1 ms: 1.01x slower                                                           |
| regex_v8                 | 15.8 ms                                                         | 16.0 ms: 1.02x slower                                                           |
| genshi_xml               | 46.6 ms                                                         | 48.5 ms: 1.04x slower                                                           |
| xml_etree_process        | 48.1 ms                                                         | 50.5 ms: 1.05x slower                                                           |
| logging_format           | 7.91 us                                                         | 8.44 us: 1.07x slower                                                           |
| logging_simple           | 7.29 us                                                         | 7.79 us: 1.07x slower                                                           |
| nbody                    | 79.1 ms                                                         | 84.6 ms: 1.07x slower                                                           |
| coverage                 | 46.6 ms                                                         | 49.8 ms: 1.07x slower                                                           |
| pathlib                  | 81.2 ms                                                         | 87.1 ms: 1.07x slower                                                           |
| python_startup_no_site   | 18.1 ms                                                         | 19.4 ms: 1.07x slower                                                           |
| scimark_fft              | 216 ms                                                          | 235 ms: 1.09x slower                                                            |
| regex_effbot             | 1.66 ms                                                         | 1.82 ms: 1.10x slower                                                           |
| xml_etree_generate       | 61.6 ms                                                         | 68.3 ms: 1.11x slower                                                           |
| python_startup           | 22.9 ms                                                         | 25.8 ms: 1.13x slower                                                           |
| async_generators         | 241 ms                                                          | 302 ms: 1.25x slower                                                            |
| bench_mp_pool            | 66.4 ms                                                         | 88.3 ms: 1.33x slower                                                           |
| telco                    | 4.83 ms                                                         | 6.76 ms: 1.40x slower                                                           |
| gc_traversal             | 1.28 ms                                                         | 1.80 ms: 1.40x slower                                                           |
| create_gc_cycles         | 694 us                                                          | 1.16 ms: 1.67x slower                                                           |
| Geometric mean           | (ref)                                                           | 1.13x faster                                                                    |
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (10) of results/bm-20241102-3.14.0a1+-7d7d56d/bm-20241102-pythonperf1_win32-x86-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, shortest_path, sphinx

- Geometric mean (including insignificant results): 1.135x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.07x
- 95% likely to have a speedup of 1.07x
- 99% likely to have a speedup of 1.06x

# Memory
- memory change: unknown
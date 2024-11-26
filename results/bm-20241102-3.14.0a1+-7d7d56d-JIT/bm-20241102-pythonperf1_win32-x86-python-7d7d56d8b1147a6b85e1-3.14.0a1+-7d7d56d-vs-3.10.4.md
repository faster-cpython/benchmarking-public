# Results vs. 3.10.4

- fork: python
- ref: 7d7d56d8b1147a6b85e1
- machine: windows-x86
- commit hash: 7d7d56d
- commit date: 2024-11-02
- overall geometric mean: 1.027x faster
- HPT reliability: 67.35%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241102-pythonperf1_win32-x86-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 293 ms: 1.10x slower                                                            |
| docutils       | 1.95 sec                                                        | 2.15 sec: 1.10x slower                                                          |
| html5lib       | 52.1 ms                                                         | 49.7 ms: 1.05x faster                                                           |
| tornado_http   | 118 ms                                                          | 110 ms: 1.07x faster                                                            |
| Geometric mean | (ref)                                                           | 1.02x slower                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241102-pythonperf1_win32-x86-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d |
|-------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 922 ms                                                          | 500 ms: 1.84x faster                                                            |
| async_tree_io           | 940 ms                                                          | 573 ms: 1.64x faster                                                            |
| async_tree_none         | 394 ms                                                          | 245 ms: 1.61x faster                                                            |
| async_tree_memoization  | 467 ms                                                          | 299 ms: 1.56x faster                                                            |
| Geometric mean          | (ref)                                                           | 1.66x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241102-pythonperf1_win32-x86-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 202 ms: 2.49x faster                                                            |
| float          | 69.6 ms                                                         | 56.6 ms: 1.23x faster                                                           |
| nbody          | 79.1 ms                                                         | 95.8 ms: 1.21x slower                                                           |
| Geometric mean | (ref)                                                           | 1.36x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241102-pythonperf1_win32-x86-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_dna      | 131 ms                                                          | 112 ms: 1.17x faster                                                            |
| regex_v8       | 15.8 ms                                                         | 16.1 ms: 1.02x slower                                                           |
| regex_compile  | 117 ms                                                          | 124 ms: 1.06x slower                                                            |
| regex_effbot   | 1.66 ms                                                         | 1.82 ms: 1.09x slower                                                           |
| Geometric mean | (ref)                                                           | 1.00x slower                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241102-pythonperf1_win32-x86-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| json_dumps           | 9.82 ms                                                         | 8.86 ms: 1.11x faster                                                           |
| xml_etree_parse      | 120 ms                                                          | 112 ms: 1.07x faster                                                            |
| tomli_loads          | 1.91 sec                                                        | 1.84 sec: 1.04x faster                                                          |
| json_loads           | 22.4 us                                                         | 21.7 us: 1.03x faster                                                           |
| xml_etree_iterparse  | 70.8 ms                                                         | 69.6 ms: 1.02x faster                                                           |
| unpickle_pure_python | 189 us                                                          | 194 us: 1.02x slower                                                            |
| pickle_pure_python   | 280 us                                                          | 301 us: 1.07x slower                                                            |
| xml_etree_process    | 48.1 ms                                                         | 56.0 ms: 1.16x slower                                                           |
| xml_etree_generate   | 61.6 ms                                                         | 74.2 ms: 1.20x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.02x slower                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241102-pythonperf1_win32-x86-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 18.1 ms                                                         | 19.9 ms: 1.10x slower                                                           |
| python_startup         | 22.9 ms                                                         | 25.9 ms: 1.13x slower                                                           |
| Geometric mean         | (ref)                                                           | 1.12x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241102-pythonperf1_win32-x86-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 9.10 ms                                                         | 7.33 ms: 1.24x faster                                                           |
| django_template | 36.0 ms                                                         | 37.2 ms: 1.03x slower                                                           |
| genshi_xml      | 46.6 ms                                                         | 60.0 ms: 1.29x slower                                                           |
| genshi_text     | 21.0 ms                                                         | 27.7 ms: 1.32x slower                                                           |
| Geometric mean  | (ref)                                                           | 1.09x slower                                                                    |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241102-pythonperf1_win32-x86-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d |
|--------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pidigits                 | 502 ms                                                          | 202 ms: 2.49x faster                                                            |
| typing_runtime_protocols | 396 us                                                          | 169 us: 2.34x faster                                                            |
| sqlglot_normalize        | 230 ms                                                          | 115 ms: 2.00x faster                                                            |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 500 ms: 1.84x faster                                                            |
| async_tree_io            | 940 ms                                                          | 573 ms: 1.64x faster                                                            |
| async_tree_none          | 394 ms                                                          | 245 ms: 1.61x faster                                                            |
| async_tree_memoization   | 467 ms                                                          | 299 ms: 1.56x faster                                                            |
| pylint                   | 384 ms                                                          | 279 ms: 1.37x faster                                                            |
| logging_silent           | 97.9 ns                                                         | 77.2 ns: 1.27x faster                                                           |
| mako                     | 9.10 ms                                                         | 7.33 ms: 1.24x faster                                                           |
| deepcopy_memo            | 29.6 us                                                         | 24.0 us: 1.23x faster                                                           |
| float                    | 69.6 ms                                                         | 56.6 ms: 1.23x faster                                                           |
| crypto_pyaes             | 81.3 ms                                                         | 67.0 ms: 1.21x faster                                                           |
| scimark_lu               | 89.8 ms                                                         | 74.4 ms: 1.21x faster                                                           |
| deltablue                | 4.04 ms                                                         | 3.36 ms: 1.20x faster                                                           |
| sqlite_synth             | 2.29 us                                                         | 1.96 us: 1.17x faster                                                           |
| regex_dna                | 131 ms                                                          | 112 ms: 1.17x faster                                                            |
| dulwich_log              | 58.5 ms                                                         | 50.8 ms: 1.15x faster                                                           |
| thrift                   | 902 us                                                          | 792 us: 1.14x faster                                                            |
| deepcopy                 | 310 us                                                          | 274 us: 1.13x faster                                                            |
| chaos                    | 74.4 ms                                                         | 65.9 ms: 1.13x faster                                                           |
| sqlglot_parse            | 1.33 ms                                                         | 1.18 ms: 1.13x faster                                                           |
| json_dumps               | 9.82 ms                                                         | 8.86 ms: 1.11x faster                                                           |
| go                       | 146 ms                                                          | 131 ms: 1.11x faster                                                            |
| pycparser                | 1.04 sec                                                        | 942 ms: 1.11x faster                                                            |
| bench_thread_pool        | 1.12 ms                                                         | 1.03 ms: 1.09x faster                                                           |
| coroutines               | 17.9 ms                                                         | 16.6 ms: 1.08x faster                                                           |
| xml_etree_parse          | 120 ms                                                          | 112 ms: 1.07x faster                                                            |
| tornado_http             | 118 ms                                                          | 110 ms: 1.07x faster                                                            |
| scimark_sor              | 115 ms                                                          | 108 ms: 1.06x faster                                                            |
| pyflate                  | 422 ms                                                          | 397 ms: 1.06x faster                                                            |
| html5lib                 | 52.1 ms                                                         | 49.7 ms: 1.05x faster                                                           |
| sqlglot_transpile        | 1.58 ms                                                         | 1.53 ms: 1.04x faster                                                           |
| tomli_loads              | 1.91 sec                                                        | 1.84 sec: 1.04x faster                                                          |
| json_loads               | 22.4 us                                                         | 21.7 us: 1.03x faster                                                           |
| xml_etree_iterparse      | 70.8 ms                                                         | 69.6 ms: 1.02x faster                                                           |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 3.21 ms: 1.01x faster                                                           |
| spectral_norm            | 80.2 ms                                                         | 79.9 ms: 1.00x faster                                                           |
| richards_super           | 49.9 ms                                                         | 50.2 ms: 1.01x slower                                                           |
| deepcopy_reduce          | 2.68 us                                                         | 2.73 us: 1.02x slower                                                           |
| regex_v8                 | 15.8 ms                                                         | 16.1 ms: 1.02x slower                                                           |
| unpickle_pure_python     | 189 us                                                          | 194 us: 1.02x slower                                                            |
| sympy_sum                | 122 ms                                                          | 126 ms: 1.03x slower                                                            |
| scimark_monte_carlo      | 61.9 ms                                                         | 63.9 ms: 1.03x slower                                                           |
| django_template          | 36.0 ms                                                         | 37.2 ms: 1.03x slower                                                           |
| mdp                      | 1.83 sec                                                        | 1.89 sec: 1.04x slower                                                          |
| comprehensions           | 17.7 us                                                         | 18.6 us: 1.05x slower                                                           |
| fannkuch                 | 317 ms                                                          | 333 ms: 1.05x slower                                                            |
| regex_compile            | 117 ms                                                          | 124 ms: 1.06x slower                                                            |
| raytrace                 | 303 ms                                                          | 323 ms: 1.07x slower                                                            |
| pathlib                  | 81.2 ms                                                         | 86.9 ms: 1.07x slower                                                           |
| pickle_pure_python       | 280 us                                                          | 301 us: 1.07x slower                                                            |
| coverage                 | 46.6 ms                                                         | 50.7 ms: 1.09x slower                                                           |
| sympy_expand             | 391 ms                                                          | 427 ms: 1.09x slower                                                            |
| regex_effbot             | 1.66 ms                                                         | 1.82 ms: 1.09x slower                                                           |
| sympy_str                | 229 ms                                                          | 251 ms: 1.09x slower                                                            |
| pprint_pformat           | 1.37 sec                                                        | 1.50 sec: 1.10x slower                                                          |
| meteor_contest           | 80.0 ms                                                         | 87.9 ms: 1.10x slower                                                           |
| docutils                 | 1.95 sec                                                        | 2.15 sec: 1.10x slower                                                          |
| 2to3                     | 265 ms                                                          | 293 ms: 1.10x slower                                                            |
| python_startup_no_site   | 18.1 ms                                                         | 19.9 ms: 1.10x slower                                                           |
| pprint_safe_repr         | 658 ms                                                          | 729 ms: 1.11x slower                                                            |
| python_startup           | 22.9 ms                                                         | 25.9 ms: 1.13x slower                                                           |
| richards                 | 40.3 ms                                                         | 45.6 ms: 1.13x slower                                                           |
| logging_format           | 7.91 us                                                         | 9.02 us: 1.14x slower                                                           |
| logging_simple           | 7.29 us                                                         | 8.40 us: 1.15x slower                                                           |
| nqueens                  | 87.1 ms                                                         | 100 ms: 1.15x slower                                                            |
| scimark_fft              | 216 ms                                                          | 251 ms: 1.16x slower                                                            |
| xml_etree_process        | 48.1 ms                                                         | 56.0 ms: 1.16x slower                                                           |
| generators               | 31.6 ms                                                         | 36.9 ms: 1.17x slower                                                           |
| sympy_integrate          | 16.6 ms                                                         | 19.8 ms: 1.19x slower                                                           |
| hexiom                   | 6.13 ms                                                         | 7.33 ms: 1.20x slower                                                           |
| xml_etree_generate       | 61.6 ms                                                         | 74.2 ms: 1.20x slower                                                           |
| nbody                    | 79.1 ms                                                         | 95.8 ms: 1.21x slower                                                           |
| sqlglot_optimize         | 44.7 ms                                                         | 56.9 ms: 1.27x slower                                                           |
| genshi_xml               | 46.6 ms                                                         | 60.0 ms: 1.29x slower                                                           |
| genshi_text              | 21.0 ms                                                         | 27.7 ms: 1.32x slower                                                           |
| async_generators         | 241 ms                                                          | 332 ms: 1.38x slower                                                            |
| gc_traversal             | 1.28 ms                                                         | 1.79 ms: 1.39x slower                                                           |
| bench_mp_pool            | 66.4 ms                                                         | 93.9 ms: 1.42x slower                                                           |
| telco                    | 4.83 ms                                                         | 7.45 ms: 1.54x slower                                                           |
| create_gc_cycles         | 694 us                                                          | 1.17 ms: 1.69x slower                                                           |
| Geometric mean           | (ref)                                                           | 1.02x faster                                                                    |

Benchmark hidden because not significant (1): json
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (10) of results/bm-20241102-3.14.0a1+-7d7d56d-JIT/bm-20241102-pythonperf1_win32-x86-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, shortest_path, sphinx

- Geometric mean (including insignificant results): 1.027x faster
# HPT report

- Reliability score: 67.35% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown
# Results vs. 3.10.4

- fork: python
- ref: v3.13.0
- machine: windows-x86
- commit hash: 60403a5
- commit date: 2024-10-07
- overall geometric mean: 1.102x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.07x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 255 ms: 1.04x faster                                            |
| chameleon      | 6.42 ms                                                         | 6.24 ms: 1.03x faster                                           |
| docutils       | 1.95 sec                                                        | 1.80 sec: 1.08x faster                                          |
| html5lib       | 52.1 ms                                                         | 47.1 ms: 1.11x faster                                           |
| tornado_http   | 118 ms                                                          | 105 ms: 1.12x faster                                            |
| Geometric mean | (ref)                                                           | 1.08x faster                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 |
|-------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 922 ms                                                          | 490 ms: 1.88x faster                                            |
| async_tree_io           | 940 ms                                                          | 530 ms: 1.77x faster                                            |
| async_tree_none         | 394 ms                                                          | 245 ms: 1.61x faster                                            |
| async_tree_memoization  | 467 ms                                                          | 302 ms: 1.55x faster                                            |
| Geometric mean          | (ref)                                                           | 1.70x faster                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 204 ms: 2.47x faster                                            |
| float          | 69.6 ms                                                         | 56.4 ms: 1.23x faster                                           |
| nbody          | 79.1 ms                                                         | 81.4 ms: 1.03x slower                                           |
| Geometric mean | (ref)                                                           | 1.44x faster                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| regex_dna      | 131 ms                                                          | 112 ms: 1.16x faster                                            |
| regex_compile  | 117 ms                                                          | 101 ms: 1.15x faster                                            |
| regex_v8       | 15.8 ms                                                         | 15.5 ms: 1.02x faster                                           |
| regex_effbot   | 1.66 ms                                                         | 1.82 ms: 1.09x slower                                           |
| Geometric mean | (ref)                                                           | 1.06x faster                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 |
|----------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| json_dumps           | 9.82 ms                                                         | 7.53 ms: 1.30x faster                                           |
| xml_etree_parse      | 120 ms                                                          | 102 ms: 1.17x faster                                            |
| pickle_pure_python   | 280 us                                                          | 239 us: 1.17x faster                                            |
| unpickle_pure_python | 189 us                                                          | 162 us: 1.17x faster                                            |
| xml_etree_iterparse  | 70.8 ms                                                         | 61.3 ms: 1.16x faster                                           |
| tomli_loads          | 1.91 sec                                                        | 1.74 sec: 1.10x faster                                          |
| xml_etree_process    | 48.1 ms                                                         | 44.6 ms: 1.08x faster                                           |
| json_loads           | 22.4 us                                                         | 21.7 us: 1.03x faster                                           |
| Geometric mean       | (ref)                                                           | 1.13x faster                                                    |

Benchmark hidden because not significant (1): xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 |
|------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| python_startup_no_site | 18.1 ms                                                         | 20.2 ms: 1.12x slower                                           |
| python_startup         | 22.9 ms                                                         | 28.3 ms: 1.23x slower                                           |
| Geometric mean         | (ref)                                                           | 1.17x slower                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 |
|-----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| mako            | 9.10 ms                                                         | 7.02 ms: 1.30x faster                                           |
| django_template | 36.0 ms                                                         | 32.0 ms: 1.12x faster                                           |
| genshi_text     | 21.0 ms                                                         | 21.7 ms: 1.04x slower                                           |
| genshi_xml      | 46.6 ms                                                         | 49.0 ms: 1.05x slower                                           |
| Geometric mean  | (ref)                                                           | 1.08x faster                                                    |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 |
|--------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| typing_runtime_protocols | 396 us                                                          | 141 us: 2.81x faster                                            |
| pidigits                 | 502 ms                                                          | 204 ms: 2.47x faster                                            |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 490 ms: 1.88x faster                                            |
| async_tree_io            | 940 ms                                                          | 530 ms: 1.77x faster                                            |
| deltablue                | 4.04 ms                                                         | 2.35 ms: 1.72x faster                                           |
| pylint                   | 384 ms                                                          | 225 ms: 1.71x faster                                            |
| async_tree_none          | 394 ms                                                          | 245 ms: 1.61x faster                                            |
| logging_silent           | 97.9 ns                                                         | 62.4 ns: 1.57x faster                                           |
| async_tree_memoization   | 467 ms                                                          | 302 ms: 1.55x faster                                            |
| chaos                    | 74.4 ms                                                         | 49.4 ms: 1.51x faster                                           |
| raytrace                 | 303 ms                                                          | 203 ms: 1.49x faster                                            |
| scimark_lu               | 89.8 ms                                                         | 60.7 ms: 1.48x faster                                           |
| generators               | 31.6 ms                                                         | 21.5 ms: 1.47x faster                                           |
| crypto_pyaes             | 81.3 ms                                                         | 56.6 ms: 1.44x faster                                           |
| comprehensions           | 17.7 us                                                         | 13.1 us: 1.35x faster                                           |
| richards_super           | 49.9 ms                                                         | 37.0 ms: 1.35x faster                                           |
| scimark_sor              | 115 ms                                                          | 85.8 ms: 1.34x faster                                           |
| hexiom                   | 6.13 ms                                                         | 4.60 ms: 1.33x faster                                           |
| go                       | 146 ms                                                          | 111 ms: 1.31x faster                                            |
| pyflate                  | 422 ms                                                          | 322 ms: 1.31x faster                                            |
| json_dumps               | 9.82 ms                                                         | 7.53 ms: 1.30x faster                                           |
| sqlglot_parse            | 1.33 ms                                                         | 1.02 ms: 1.30x faster                                           |
| mako                     | 9.10 ms                                                         | 7.02 ms: 1.30x faster                                           |
| scimark_monte_carlo      | 61.9 ms                                                         | 48.7 ms: 1.27x faster                                           |
| sqlglot_transpile        | 1.58 ms                                                         | 1.26 ms: 1.25x faster                                           |
| float                    | 69.6 ms                                                         | 56.4 ms: 1.23x faster                                           |
| richards                 | 40.3 ms                                                         | 33.4 ms: 1.21x faster                                           |
| pycparser                | 1.04 sec                                                        | 869 ms: 1.20x faster                                            |
| xml_etree_parse          | 120 ms                                                          | 102 ms: 1.17x faster                                            |
| pickle_pure_python       | 280 us                                                          | 239 us: 1.17x faster                                            |
| unpickle_pure_python     | 189 us                                                          | 162 us: 1.17x faster                                            |
| dulwich_log              | 58.5 ms                                                         | 50.2 ms: 1.17x faster                                           |
| regex_dna                | 131 ms                                                          | 112 ms: 1.16x faster                                            |
| sqlalchemy_imperative    | 13.2 ms                                                         | 11.3 ms: 1.16x faster                                           |
| nqueens                  | 87.1 ms                                                         | 75.1 ms: 1.16x faster                                           |
| xml_etree_iterparse      | 70.8 ms                                                         | 61.3 ms: 1.16x faster                                           |
| regex_compile            | 117 ms                                                          | 101 ms: 1.15x faster                                            |
| spectral_norm            | 80.2 ms                                                         | 70.0 ms: 1.15x faster                                           |
| sympy_sum                | 122 ms                                                          | 108 ms: 1.13x faster                                            |
| deepcopy_memo            | 29.6 us                                                         | 26.2 us: 1.13x faster                                           |
| tornado_http             | 118 ms                                                          | 105 ms: 1.12x faster                                            |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 2.88 ms: 1.12x faster                                           |
| django_template          | 36.0 ms                                                         | 32.0 ms: 1.12x faster                                           |
| coroutines               | 17.9 ms                                                         | 16.1 ms: 1.11x faster                                           |
| html5lib                 | 52.1 ms                                                         | 47.1 ms: 1.11x faster                                           |
| fannkuch                 | 317 ms                                                          | 288 ms: 1.10x faster                                            |
| sqlalchemy_declarative   | 104 ms                                                          | 94.8 ms: 1.10x faster                                           |
| tomli_loads              | 1.91 sec                                                        | 1.74 sec: 1.10x faster                                          |
| sympy_integrate          | 16.6 ms                                                         | 15.2 ms: 1.09x faster                                           |
| json                     | 4.76 ms                                                         | 4.40 ms: 1.08x faster                                           |
| docutils                 | 1.95 sec                                                        | 1.80 sec: 1.08x faster                                          |
| xml_etree_process        | 48.1 ms                                                         | 44.6 ms: 1.08x faster                                           |
| bench_thread_pool        | 1.12 ms                                                         | 1.04 ms: 1.08x faster                                           |
| mdp                      | 1.83 sec                                                        | 1.70 sec: 1.08x faster                                          |
| sympy_str                | 229 ms                                                          | 214 ms: 1.07x faster                                            |
| scimark_fft              | 216 ms                                                          | 204 ms: 1.06x faster                                            |
| sqlglot_optimize         | 44.7 ms                                                         | 42.4 ms: 1.05x faster                                           |
| 2to3                     | 265 ms                                                          | 255 ms: 1.04x faster                                            |
| pprint_pformat           | 1.37 sec                                                        | 1.32 sec: 1.04x faster                                          |
| sympy_expand             | 391 ms                                                          | 377 ms: 1.04x faster                                            |
| sqlglot_normalize        | 230 ms                                                          | 223 ms: 1.03x faster                                            |
| json_loads               | 22.4 us                                                         | 21.7 us: 1.03x faster                                           |
| chameleon                | 6.42 ms                                                         | 6.24 ms: 1.03x faster                                           |
| meteor_contest           | 80.0 ms                                                         | 78.1 ms: 1.02x faster                                           |
| regex_v8                 | 15.8 ms                                                         | 15.5 ms: 1.02x faster                                           |
| nbody                    | 79.1 ms                                                         | 81.4 ms: 1.03x slower                                           |
| genshi_text              | 21.0 ms                                                         | 21.7 ms: 1.04x slower                                           |
| genshi_xml               | 46.6 ms                                                         | 49.0 ms: 1.05x slower                                           |
| logging_simple           | 7.29 us                                                         | 7.89 us: 1.08x slower                                           |
| logging_format           | 7.91 us                                                         | 8.59 us: 1.09x slower                                           |
| regex_effbot             | 1.66 ms                                                         | 1.82 ms: 1.09x slower                                           |
| deepcopy_reduce          | 2.68 us                                                         | 2.94 us: 1.10x slower                                           |
| pathlib                  | 81.2 ms                                                         | 89.1 ms: 1.10x slower                                           |
| async_generators         | 241 ms                                                          | 267 ms: 1.11x slower                                            |
| python_startup_no_site   | 18.1 ms                                                         | 20.2 ms: 1.12x slower                                           |
| python_startup           | 22.9 ms                                                         | 28.3 ms: 1.23x slower                                           |
| telco                    | 4.83 ms                                                         | 6.27 ms: 1.30x slower                                           |
| gc_traversal             | 1.28 ms                                                         | 1.76 ms: 1.38x slower                                           |
| bench_mp_pool            | 66.4 ms                                                         | 93.6 ms: 1.41x slower                                           |
| create_gc_cycles         | 694 us                                                          | 1.08 ms: 1.56x slower                                           |
| coverage                 | 46.6 ms                                                         | 326 ms: 7.01x slower                                            |
| thrift                   | 902 us                                                          | 10.3 ms: 11.37x slower                                          |
| Geometric mean           | (ref)                                                           | 1.10x faster                                                    |

Benchmark hidden because not significant (3): pprint_safe_repr, deepcopy, xml_etree_generate
Ignored benchmarks (13) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, gevent_hub, k_core, shortest_path, sphinx

- Geometric mean (including insignificant results): 1.102x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.09x
- 95% likely to have a speedup of 1.09x
- 99% likely to have a speedup of 1.07x

# Memory
- memory change: unknown
# Results vs. 3.13.0

- fork: python
- ref: v3.10.4
- machine: windows-x86
- commit hash: 9d38120
- commit date: 2022-03-23
- overall geometric mean: 1.091x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.07x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| 2to3           | 255 ms                                                          | 265 ms: 1.04x slower                                            |
| chameleon      | 6.24 ms                                                         | 6.42 ms: 1.03x slower                                           |
| docutils       | 1.80 sec                                                        | 1.95 sec: 1.08x slower                                          |
| html5lib       | 47.1 ms                                                         | 52.1 ms: 1.11x slower                                           |
| tornado_http   | 105 ms                                                          | 118 ms: 1.12x slower                                            |
| Geometric mean | (ref)                                                           | 1.08x slower                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 |
|-------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| async_generators        | 267 ms                                                          | 241 ms: 1.11x faster                                            |
| coroutines              | 16.1 ms                                                         | 17.9 ms: 1.11x slower                                           |
| async_tree_memoization  | 302 ms                                                          | 467 ms: 1.55x slower                                            |
| async_tree_none         | 245 ms                                                          | 394 ms: 1.61x slower                                            |
| async_tree_io           | 530 ms                                                          | 940 ms: 1.77x slower                                            |
| async_tree_cpu_io_mixed | 490 ms                                                          | 922 ms: 1.88x slower                                            |
| Geometric mean          | (ref)                                                           | 1.42x slower                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| nbody          | 81.4 ms                                                         | 79.1 ms: 1.03x faster                                           |
| float          | 56.4 ms                                                         | 69.6 ms: 1.23x slower                                           |
| pidigits       | 204 ms                                                          | 502 ms: 2.47x slower                                            |
| Geometric mean | (ref)                                                           | 1.44x slower                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| regex_effbot   | 1.82 ms                                                         | 1.66 ms: 1.09x faster                                           |
| regex_v8       | 15.5 ms                                                         | 15.8 ms: 1.02x slower                                           |
| regex_compile  | 101 ms                                                          | 117 ms: 1.15x slower                                            |
| regex_dna      | 112 ms                                                          | 131 ms: 1.16x slower                                            |
| Geometric mean | (ref)                                                           | 1.06x slower                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 |
|----------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| json_loads           | 21.7 us                                                         | 22.4 us: 1.03x slower                                           |
| xml_etree_process    | 44.6 ms                                                         | 48.1 ms: 1.08x slower                                           |
| tomli_loads          | 1.74 sec                                                        | 1.91 sec: 1.10x slower                                          |
| xml_etree_iterparse  | 61.3 ms                                                         | 70.8 ms: 1.16x slower                                           |
| unpickle_pure_python | 162 us                                                          | 189 us: 1.17x slower                                            |
| pickle_pure_python   | 239 us                                                          | 280 us: 1.17x slower                                            |
| xml_etree_parse      | 102 ms                                                          | 120 ms: 1.17x slower                                            |
| json_dumps           | 7.53 ms                                                         | 9.82 ms: 1.30x slower                                           |
| Geometric mean       | (ref)                                                           | 1.13x slower                                                    |

Benchmark hidden because not significant (1): xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 |
|------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| python_startup         | 28.3 ms                                                         | 22.9 ms: 1.23x faster                                           |
| python_startup_no_site | 20.2 ms                                                         | 18.1 ms: 1.12x faster                                           |
| Geometric mean         | (ref)                                                           | 1.17x faster                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 |
|-----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| genshi_xml      | 49.0 ms                                                         | 46.6 ms: 1.05x faster                                           |
| genshi_text     | 21.7 ms                                                         | 21.0 ms: 1.04x faster                                           |
| django_template | 32.0 ms                                                         | 36.0 ms: 1.12x slower                                           |
| mako            | 7.02 ms                                                         | 9.10 ms: 1.30x slower                                           |
| Geometric mean  | (ref)                                                           | 1.08x slower                                                    |

All benchmarks:
===============

| Benchmark                | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 |
|--------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| thrift                   | 10.3 ms                                                         | 902 us: 11.37x faster                                           |
| coverage                 | 326 ms                                                          | 46.6 ms: 7.01x faster                                           |
| create_gc_cycles         | 1.08 ms                                                         | 694 us: 1.56x faster                                            |
| bench_mp_pool            | 93.6 ms                                                         | 66.4 ms: 1.41x faster                                           |
| gc_traversal             | 1.76 ms                                                         | 1.28 ms: 1.38x faster                                           |
| telco                    | 6.27 ms                                                         | 4.83 ms: 1.30x faster                                           |
| python_startup           | 28.3 ms                                                         | 22.9 ms: 1.23x faster                                           |
| python_startup_no_site   | 20.2 ms                                                         | 18.1 ms: 1.12x faster                                           |
| async_generators         | 267 ms                                                          | 241 ms: 1.11x faster                                            |
| pathlib                  | 89.1 ms                                                         | 81.2 ms: 1.10x faster                                           |
| deepcopy_reduce          | 2.94 us                                                         | 2.68 us: 1.10x faster                                           |
| regex_effbot             | 1.82 ms                                                         | 1.66 ms: 1.09x faster                                           |
| logging_format           | 8.59 us                                                         | 7.91 us: 1.09x faster                                           |
| logging_simple           | 7.89 us                                                         | 7.29 us: 1.08x faster                                           |
| genshi_xml               | 49.0 ms                                                         | 46.6 ms: 1.05x faster                                           |
| genshi_text              | 21.7 ms                                                         | 21.0 ms: 1.04x faster                                           |
| nbody                    | 81.4 ms                                                         | 79.1 ms: 1.03x faster                                           |
| regex_v8                 | 15.5 ms                                                         | 15.8 ms: 1.02x slower                                           |
| meteor_contest           | 78.1 ms                                                         | 80.0 ms: 1.02x slower                                           |
| chameleon                | 6.24 ms                                                         | 6.42 ms: 1.03x slower                                           |
| json_loads               | 21.7 us                                                         | 22.4 us: 1.03x slower                                           |
| sqlglot_normalize        | 223 ms                                                          | 230 ms: 1.03x slower                                            |
| sympy_expand             | 377 ms                                                          | 391 ms: 1.04x slower                                            |
| pprint_pformat           | 1.32 sec                                                        | 1.37 sec: 1.04x slower                                          |
| 2to3                     | 255 ms                                                          | 265 ms: 1.04x slower                                            |
| sqlglot_optimize         | 42.4 ms                                                         | 44.7 ms: 1.05x slower                                           |
| scimark_fft              | 204 ms                                                          | 216 ms: 1.06x slower                                            |
| sympy_str                | 214 ms                                                          | 229 ms: 1.07x slower                                            |
| mdp                      | 1.70 sec                                                        | 1.83 sec: 1.08x slower                                          |
| bench_thread_pool        | 1.04 ms                                                         | 1.12 ms: 1.08x slower                                           |
| xml_etree_process        | 44.6 ms                                                         | 48.1 ms: 1.08x slower                                           |
| docutils                 | 1.80 sec                                                        | 1.95 sec: 1.08x slower                                          |
| json                     | 4.40 ms                                                         | 4.76 ms: 1.08x slower                                           |
| sympy_integrate          | 15.2 ms                                                         | 16.6 ms: 1.09x slower                                           |
| tomli_loads              | 1.74 sec                                                        | 1.91 sec: 1.10x slower                                          |
| sqlalchemy_declarative   | 94.8 ms                                                         | 104 ms: 1.10x slower                                            |
| fannkuch                 | 288 ms                                                          | 317 ms: 1.10x slower                                            |
| html5lib                 | 47.1 ms                                                         | 52.1 ms: 1.11x slower                                           |
| coroutines               | 16.1 ms                                                         | 17.9 ms: 1.11x slower                                           |
| django_template          | 32.0 ms                                                         | 36.0 ms: 1.12x slower                                           |
| scimark_sparse_mat_mult  | 2.88 ms                                                         | 3.24 ms: 1.12x slower                                           |
| tornado_http             | 105 ms                                                          | 118 ms: 1.12x slower                                            |
| deepcopy_memo            | 26.2 us                                                         | 29.6 us: 1.13x slower                                           |
| sympy_sum                | 108 ms                                                          | 122 ms: 1.13x slower                                            |
| spectral_norm            | 70.0 ms                                                         | 80.2 ms: 1.15x slower                                           |
| regex_compile            | 101 ms                                                          | 117 ms: 1.15x slower                                            |
| xml_etree_iterparse      | 61.3 ms                                                         | 70.8 ms: 1.16x slower                                           |
| nqueens                  | 75.1 ms                                                         | 87.1 ms: 1.16x slower                                           |
| sqlalchemy_imperative    | 11.3 ms                                                         | 13.2 ms: 1.16x slower                                           |
| regex_dna                | 112 ms                                                          | 131 ms: 1.16x slower                                            |
| dulwich_log              | 50.2 ms                                                         | 58.5 ms: 1.17x slower                                           |
| unpickle_pure_python     | 162 us                                                          | 189 us: 1.17x slower                                            |
| pickle_pure_python       | 239 us                                                          | 280 us: 1.17x slower                                            |
| xml_etree_parse          | 102 ms                                                          | 120 ms: 1.17x slower                                            |
| pycparser                | 869 ms                                                          | 1.04 sec: 1.20x slower                                          |
| richards                 | 33.4 ms                                                         | 40.3 ms: 1.21x slower                                           |
| float                    | 56.4 ms                                                         | 69.6 ms: 1.23x slower                                           |
| sqlglot_transpile        | 1.26 ms                                                         | 1.58 ms: 1.25x slower                                           |
| scimark_monte_carlo      | 48.7 ms                                                         | 61.9 ms: 1.27x slower                                           |
| mako                     | 7.02 ms                                                         | 9.10 ms: 1.30x slower                                           |
| sqlglot_parse            | 1.02 ms                                                         | 1.33 ms: 1.30x slower                                           |
| json_dumps               | 7.53 ms                                                         | 9.82 ms: 1.30x slower                                           |
| pyflate                  | 322 ms                                                          | 422 ms: 1.31x slower                                            |
| go                       | 111 ms                                                          | 146 ms: 1.31x slower                                            |
| hexiom                   | 4.60 ms                                                         | 6.13 ms: 1.33x slower                                           |
| scimark_sor              | 85.8 ms                                                         | 115 ms: 1.34x slower                                            |
| richards_super           | 37.0 ms                                                         | 49.9 ms: 1.35x slower                                           |
| comprehensions           | 13.1 us                                                         | 17.7 us: 1.35x slower                                           |
| crypto_pyaes             | 56.6 ms                                                         | 81.3 ms: 1.44x slower                                           |
| generators               | 21.5 ms                                                         | 31.6 ms: 1.47x slower                                           |
| scimark_lu               | 60.7 ms                                                         | 89.8 ms: 1.48x slower                                           |
| raytrace                 | 203 ms                                                          | 303 ms: 1.49x slower                                            |
| chaos                    | 49.4 ms                                                         | 74.4 ms: 1.51x slower                                           |
| async_tree_memoization   | 302 ms                                                          | 467 ms: 1.55x slower                                            |
| logging_silent           | 62.4 ns                                                         | 97.9 ns: 1.57x slower                                           |
| async_tree_none          | 245 ms                                                          | 394 ms: 1.61x slower                                            |
| pylint                   | 225 ms                                                          | 384 ms: 1.71x slower                                            |
| deltablue                | 2.35 ms                                                         | 4.04 ms: 1.72x slower                                           |
| async_tree_io            | 530 ms                                                          | 940 ms: 1.77x slower                                            |
| async_tree_cpu_io_mixed  | 490 ms                                                          | 922 ms: 1.88x slower                                            |
| pidigits                 | 204 ms                                                          | 502 ms: 2.47x slower                                            |
| typing_runtime_protocols | 141 us                                                          | 396 us: 2.81x slower                                            |
| Geometric mean           | (ref)                                                           | 1.10x slower                                                    |

Benchmark hidden because not significant (3): xml_etree_generate, deepcopy, pprint_safe_repr
Ignored benchmarks (11) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, gevent_hub, k_core, shortest_path, sphinx
Ignored benchmarks (13) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.091x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.09x
- 95% likely to have a slowdown of 1.09x
- 99% likely to have a slowdown of 1.07x

# Memory
- memory change: unknown
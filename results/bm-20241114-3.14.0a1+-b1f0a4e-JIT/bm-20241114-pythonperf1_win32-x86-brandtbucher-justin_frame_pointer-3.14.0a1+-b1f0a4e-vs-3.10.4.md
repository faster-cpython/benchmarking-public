# Results vs. 3.10.4

- fork: brandtbucher
- ref: justin_frame_pointer
- machine: windows-x86
- commit hash: b1f0a4e
- commit date: 2024-11-14
- overall geometric mean: 1.003x slower
- HPT reliability: 91.42%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241114-pythonperf1_win32-x86-brandtbucher-justin_frame_pointer-3.14.0a1+-b1f0a4e |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 298 ms: 1.12x slower                                                                  |
| docutils       | 1.95 sec                                                        | 2.17 sec: 1.11x slower                                                                |
| html5lib       | 52.1 ms                                                         | 47.6 ms: 1.09x faster                                                                 |
| Geometric mean | (ref)                                                           | 1.05x slower                                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241114-pythonperf1_win32-x86-brandtbucher-justin_frame_pointer-3.14.0a1+-b1f0a4e |
|-------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 922 ms                                                          | 518 ms: 1.78x faster                                                                  |
| async_tree_io           | 940 ms                                                          | 554 ms: 1.70x faster                                                                  |
| async_tree_none         | 394 ms                                                          | 250 ms: 1.58x faster                                                                  |
| async_tree_memoization  | 467 ms                                                          | 306 ms: 1.52x faster                                                                  |
| Geometric mean          | (ref)                                                           | 1.64x faster                                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241114-pythonperf1_win32-x86-brandtbucher-justin_frame_pointer-3.14.0a1+-b1f0a4e |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 202 ms: 2.49x faster                                                                  |
| float          | 69.6 ms                                                         | 59.5 ms: 1.17x faster                                                                 |
| nbody          | 79.1 ms                                                         | 124 ms: 1.56x slower                                                                  |
| Geometric mean | (ref)                                                           | 1.23x faster                                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241114-pythonperf1_win32-x86-brandtbucher-justin_frame_pointer-3.14.0a1+-b1f0a4e |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| regex_dna      | 131 ms                                                          | 115 ms: 1.13x faster                                                                  |
| regex_v8       | 15.8 ms                                                         | 15.9 ms: 1.01x slower                                                                 |
| regex_compile  | 117 ms                                                          | 126 ms: 1.08x slower                                                                  |
| regex_effbot   | 1.66 ms                                                         | 1.83 ms: 1.10x slower                                                                 |
| Geometric mean | (ref)                                                           | 1.01x slower                                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241114-pythonperf1_win32-x86-brandtbucher-justin_frame_pointer-3.14.0a1+-b1f0a4e |
|--------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| json_dumps         | 9.82 ms                                                         | 9.18 ms: 1.07x faster                                                                 |
| xml_etree_parse    | 120 ms                                                          | 114 ms: 1.05x faster                                                                  |
| json_loads         | 22.4 us                                                         | 21.9 us: 1.02x faster                                                                 |
| tomli_loads        | 1.91 sec                                                        | 1.98 sec: 1.04x slower                                                                |
| pickle_pure_python | 280 us                                                          | 315 us: 1.12x slower                                                                  |
| xml_etree_process  | 48.1 ms                                                         | 58.0 ms: 1.20x slower                                                                 |
| xml_etree_generate | 61.6 ms                                                         | 76.0 ms: 1.23x slower                                                                 |
| Geometric mean     | (ref)                                                           | 1.05x slower                                                                          |

Benchmark hidden because not significant (2): xml_etree_iterparse, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241114-pythonperf1_win32-x86-brandtbucher-justin_frame_pointer-3.14.0a1+-b1f0a4e |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| python_startup_no_site | 18.1 ms                                                         | 19.6 ms: 1.09x slower                                                                 |
| python_startup         | 22.9 ms                                                         | 25.7 ms: 1.12x slower                                                                 |
| Geometric mean         | (ref)                                                           | 1.10x slower                                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241114-pythonperf1_win32-x86-brandtbucher-justin_frame_pointer-3.14.0a1+-b1f0a4e |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| mako            | 9.10 ms                                                         | 7.83 ms: 1.16x faster                                                                 |
| django_template | 36.0 ms                                                         | 37.1 ms: 1.03x slower                                                                 |
| genshi_text     | 21.0 ms                                                         | 27.3 ms: 1.30x slower                                                                 |
| genshi_xml      | 46.6 ms                                                         | 61.2 ms: 1.31x slower                                                                 |
| Geometric mean  | (ref)                                                           | 1.11x slower                                                                          |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241114-pythonperf1_win32-x86-brandtbucher-justin_frame_pointer-3.14.0a1+-b1f0a4e |
|--------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| pidigits                 | 502 ms                                                          | 202 ms: 2.49x faster                                                                  |
| typing_runtime_protocols | 396 us                                                          | 176 us: 2.25x faster                                                                  |
| sqlglot_normalize        | 230 ms                                                          | 118 ms: 1.95x faster                                                                  |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 518 ms: 1.78x faster                                                                  |
| async_tree_io            | 940 ms                                                          | 554 ms: 1.70x faster                                                                  |
| async_tree_none          | 394 ms                                                          | 250 ms: 1.58x faster                                                                  |
| async_tree_memoization   | 467 ms                                                          | 306 ms: 1.52x faster                                                                  |
| pylint                   | 384 ms                                                          | 294 ms: 1.31x faster                                                                  |
| scimark_lu               | 89.8 ms                                                         | 74.5 ms: 1.20x faster                                                                 |
| deltablue                | 4.04 ms                                                         | 3.42 ms: 1.18x faster                                                                 |
| logging_silent           | 97.9 ns                                                         | 83.2 ns: 1.18x faster                                                                 |
| float                    | 69.6 ms                                                         | 59.5 ms: 1.17x faster                                                                 |
| sqlite_synth             | 2.29 us                                                         | 1.96 us: 1.17x faster                                                                 |
| mako                     | 9.10 ms                                                         | 7.83 ms: 1.16x faster                                                                 |
| deepcopy_memo            | 29.6 us                                                         | 25.9 us: 1.14x faster                                                                 |
| dulwich_log              | 58.5 ms                                                         | 51.3 ms: 1.14x faster                                                                 |
| thrift                   | 902 us                                                          | 791 us: 1.14x faster                                                                  |
| regex_dna                | 131 ms                                                          | 115 ms: 1.13x faster                                                                  |
| go                       | 146 ms                                                          | 130 ms: 1.12x faster                                                                  |
| crypto_pyaes             | 81.3 ms                                                         | 73.4 ms: 1.11x faster                                                                 |
| pycparser                | 1.04 sec                                                        | 951 ms: 1.10x faster                                                                  |
| html5lib                 | 52.1 ms                                                         | 47.6 ms: 1.09x faster                                                                 |
| sqlglot_parse            | 1.33 ms                                                         | 1.23 ms: 1.08x faster                                                                 |
| coroutines               | 17.9 ms                                                         | 16.7 ms: 1.07x faster                                                                 |
| json_dumps               | 9.82 ms                                                         | 9.18 ms: 1.07x faster                                                                 |
| bench_thread_pool        | 1.12 ms                                                         | 1.05 ms: 1.07x faster                                                                 |
| deepcopy                 | 310 us                                                          | 292 us: 1.06x faster                                                                  |
| xml_etree_parse          | 120 ms                                                          | 114 ms: 1.05x faster                                                                  |
| chaos                    | 74.4 ms                                                         | 71.7 ms: 1.04x faster                                                                 |
| scimark_sor              | 115 ms                                                          | 112 ms: 1.03x faster                                                                  |
| json_loads               | 22.4 us                                                         | 21.9 us: 1.02x faster                                                                 |
| richards_super           | 49.9 ms                                                         | 48.8 ms: 1.02x faster                                                                 |
| pyflate                  | 422 ms                                                          | 419 ms: 1.01x faster                                                                  |
| regex_v8                 | 15.8 ms                                                         | 15.9 ms: 1.01x slower                                                                 |
| pathlib                  | 81.2 ms                                                         | 83.1 ms: 1.02x slower                                                                 |
| django_template          | 36.0 ms                                                         | 37.1 ms: 1.03x slower                                                                 |
| tomli_loads              | 1.91 sec                                                        | 1.98 sec: 1.04x slower                                                                |
| raytrace                 | 303 ms                                                          | 315 ms: 1.04x slower                                                                  |
| sympy_sum                | 122 ms                                                          | 128 ms: 1.05x slower                                                                  |
| mdp                      | 1.83 sec                                                        | 1.93 sec: 1.06x slower                                                                |
| regex_compile            | 117 ms                                                          | 126 ms: 1.08x slower                                                                  |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 3.51 ms: 1.08x slower                                                                 |
| deepcopy_reduce          | 2.68 us                                                         | 2.91 us: 1.09x slower                                                                 |
| python_startup_no_site   | 18.1 ms                                                         | 19.6 ms: 1.09x slower                                                                 |
| scimark_monte_carlo      | 61.9 ms                                                         | 67.5 ms: 1.09x slower                                                                 |
| regex_effbot             | 1.66 ms                                                         | 1.83 ms: 1.10x slower                                                                 |
| sympy_expand             | 391 ms                                                          | 430 ms: 1.10x slower                                                                  |
| comprehensions           | 17.7 us                                                         | 19.7 us: 1.11x slower                                                                 |
| docutils                 | 1.95 sec                                                        | 2.17 sec: 1.11x slower                                                                |
| sympy_str                | 229 ms                                                          | 256 ms: 1.12x slower                                                                  |
| richards                 | 40.3 ms                                                         | 45.0 ms: 1.12x slower                                                                 |
| python_startup           | 22.9 ms                                                         | 25.7 ms: 1.12x slower                                                                 |
| pickle_pure_python       | 280 us                                                          | 315 us: 1.12x slower                                                                  |
| 2to3                     | 265 ms                                                          | 298 ms: 1.12x slower                                                                  |
| coverage                 | 46.6 ms                                                         | 52.3 ms: 1.12x slower                                                                 |
| logging_simple           | 7.29 us                                                         | 8.25 us: 1.13x slower                                                                 |
| logging_format           | 7.91 us                                                         | 8.95 us: 1.13x slower                                                                 |
| spectral_norm            | 80.2 ms                                                         | 91.1 ms: 1.14x slower                                                                 |
| meteor_contest           | 80.0 ms                                                         | 93.1 ms: 1.16x slower                                                                 |
| fannkuch                 | 317 ms                                                          | 372 ms: 1.17x slower                                                                  |
| pprint_pformat           | 1.37 sec                                                        | 1.61 sec: 1.18x slower                                                                |
| sympy_integrate          | 16.6 ms                                                         | 19.7 ms: 1.19x slower                                                                 |
| nqueens                  | 87.1 ms                                                         | 104 ms: 1.19x slower                                                                  |
| pprint_safe_repr         | 658 ms                                                          | 787 ms: 1.20x slower                                                                  |
| xml_etree_process        | 48.1 ms                                                         | 58.0 ms: 1.20x slower                                                                 |
| generators               | 31.6 ms                                                         | 38.2 ms: 1.21x slower                                                                 |
| xml_etree_generate       | 61.6 ms                                                         | 76.0 ms: 1.23x slower                                                                 |
| hexiom                   | 6.13 ms                                                         | 7.80 ms: 1.27x slower                                                                 |
| genshi_text              | 21.0 ms                                                         | 27.3 ms: 1.30x slower                                                                 |
| genshi_xml               | 46.6 ms                                                         | 61.2 ms: 1.31x slower                                                                 |
| sqlglot_optimize         | 44.7 ms                                                         | 59.3 ms: 1.33x slower                                                                 |
| scimark_fft              | 216 ms                                                          | 288 ms: 1.33x slower                                                                  |
| gc_traversal             | 1.28 ms                                                         | 1.77 ms: 1.38x slower                                                                 |
| bench_mp_pool            | 66.4 ms                                                         | 92.6 ms: 1.40x slower                                                                 |
| async_generators         | 241 ms                                                          | 342 ms: 1.42x slower                                                                  |
| nbody                    | 79.1 ms                                                         | 124 ms: 1.56x slower                                                                  |
| telco                    | 4.83 ms                                                         | 7.71 ms: 1.60x slower                                                                 |
| create_gc_cycles         | 694 us                                                          | 1.16 ms: 1.67x slower                                                                 |
| Geometric mean           | (ref)                                                           | 1.00x slower                                                                          |

Benchmark hidden because not significant (4): json, sqlglot_transpile, xml_etree_iterparse, unpickle_pure_python
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20241114-3.14.0a1+-b1f0a4e-JIT/bm-20241114-pythonperf1_win32-x86-brandtbucher-justin_frame_pointer-3.14.0a1+-b1f0a4e.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.003x slower
# HPT report

- Reliability score: 91.42% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown
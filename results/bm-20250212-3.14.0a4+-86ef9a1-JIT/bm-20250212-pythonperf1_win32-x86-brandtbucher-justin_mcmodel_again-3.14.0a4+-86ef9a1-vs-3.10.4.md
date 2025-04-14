# Results vs. 3.10.4

- fork: brandtbucher
- ref: justin_mcmodel_again
- machine: windows-x86
- commit hash: 86ef9a1
- commit date: 2025-02-12
- overall geometric mean: 1.083x faster
- HPT reliability: 93.90%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250212-pythonperf1_win32-x86-brandtbucher-justin_mcmodel_again-3.14.0a4+-86ef9a1 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 273 ms: 1.03x slower                                                                  |
| docutils       | 1.95 sec                                                        | 1.97 sec: 1.01x slower                                                                |
| html5lib       | 52.1 ms                                                         | 47.6 ms: 1.09x faster                                                                 |
| Geometric mean | (ref)                                                           | 1.02x faster                                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250212-pythonperf1_win32-x86-brandtbucher-justin_mcmodel_again-3.14.0a4+-86ef9a1 |
|-------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| async_tree_io           | 940 ms                                                          | 479 ms: 1.96x faster                                                                  |
| async_tree_cpu_io_mixed | 922 ms                                                          | 490 ms: 1.88x faster                                                                  |
| async_tree_none         | 394 ms                                                          | 230 ms: 1.71x faster                                                                  |
| async_tree_memoization  | 467 ms                                                          | 278 ms: 1.68x faster                                                                  |
| Geometric mean          | (ref)                                                           | 1.80x faster                                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250212-pythonperf1_win32-x86-brandtbucher-justin_mcmodel_again-3.14.0a4+-86ef9a1 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 203 ms: 2.48x faster                                                                  |
| float          | 69.6 ms                                                         | 52.5 ms: 1.33x faster                                                                 |
| nbody          | 79.1 ms                                                         | 111 ms: 1.40x slower                                                                  |
| Geometric mean | (ref)                                                           | 1.33x faster                                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250212-pythonperf1_win32-x86-brandtbucher-justin_mcmodel_again-3.14.0a4+-86ef9a1 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| regex_dna      | 131 ms                                                          | 117 ms: 1.12x faster                                                                  |
| regex_effbot   | 1.66 ms                                                         | 1.53 ms: 1.09x faster                                                                 |
| regex_v8       | 15.8 ms                                                         | 15.7 ms: 1.01x faster                                                                 |
| regex_compile  | 117 ms                                                          | 118 ms: 1.01x slower                                                                  |
| Geometric mean | (ref)                                                           | 1.05x faster                                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250212-pythonperf1_win32-x86-brandtbucher-justin_mcmodel_again-3.14.0a4+-86ef9a1 |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| xml_etree_parse      | 120 ms                                                          | 107 ms: 1.12x faster                                                                  |
| tomli_loads          | 1.91 sec                                                        | 1.80 sec: 1.06x faster                                                                |
| xml_etree_iterparse  | 70.8 ms                                                         | 67.0 ms: 1.06x faster                                                                 |
| json_dumps           | 9.82 ms                                                         | 9.38 ms: 1.05x faster                                                                 |
| json_loads           | 22.4 us                                                         | 22.2 us: 1.01x faster                                                                 |
| pickle_pure_python   | 280 us                                                          | 325 us: 1.16x slower                                                                  |
| xml_etree_process    | 48.1 ms                                                         | 56.2 ms: 1.17x slower                                                                 |
| unpickle_pure_python | 189 us                                                          | 227 us: 1.20x slower                                                                  |
| xml_etree_generate   | 61.6 ms                                                         | 75.8 ms: 1.23x slower                                                                 |
| Geometric mean       | (ref)                                                           | 1.05x slower                                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250212-pythonperf1_win32-x86-brandtbucher-justin_mcmodel_again-3.14.0a4+-86ef9a1 |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| python_startup_no_site | 18.1 ms                                                         | 21.7 ms: 1.20x slower                                                                 |
| python_startup         | 22.9 ms                                                         | 28.4 ms: 1.24x slower                                                                 |
| Geometric mean         | (ref)                                                           | 1.22x slower                                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250212-pythonperf1_win32-x86-brandtbucher-justin_mcmodel_again-3.14.0a4+-86ef9a1 |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| mako            | 9.10 ms                                                         | 7.47 ms: 1.22x faster                                                                 |
| django_template | 36.0 ms                                                         | 36.4 ms: 1.01x slower                                                                 |
| genshi_xml      | 46.6 ms                                                         | 50.9 ms: 1.09x slower                                                                 |
| genshi_text     | 21.0 ms                                                         | 24.5 ms: 1.17x slower                                                                 |
| Geometric mean  | (ref)                                                           | 1.01x slower                                                                          |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250212-pythonperf1_win32-x86-brandtbucher-justin_mcmodel_again-3.14.0a4+-86ef9a1 |
|--------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| pidigits                 | 502 ms                                                          | 203 ms: 2.48x faster                                                                  |
| typing_runtime_protocols | 396 us                                                          | 168 us: 2.36x faster                                                                  |
| sqlglot_normalize        | 230 ms                                                          | 106 ms: 2.17x faster                                                                  |
| async_tree_io            | 940 ms                                                          | 479 ms: 1.96x faster                                                                  |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 490 ms: 1.88x faster                                                                  |
| async_tree_none          | 394 ms                                                          | 230 ms: 1.71x faster                                                                  |
| async_tree_memoization   | 467 ms                                                          | 278 ms: 1.68x faster                                                                  |
| pylint                   | 384 ms                                                          | 229 ms: 1.68x faster                                                                  |
| logging_silent           | 97.9 ns                                                         | 71.1 ns: 1.38x faster                                                                 |
| generators               | 31.6 ms                                                         | 23.3 ms: 1.35x faster                                                                 |
| deltablue                | 4.04 ms                                                         | 2.99 ms: 1.35x faster                                                                 |
| scimark_lu               | 89.8 ms                                                         | 67.2 ms: 1.34x faster                                                                 |
| go                       | 146 ms                                                          | 109 ms: 1.33x faster                                                                  |
| deepcopy_memo            | 29.6 us                                                         | 22.3 us: 1.33x faster                                                                 |
| float                    | 69.6 ms                                                         | 52.5 ms: 1.33x faster                                                                 |
| chaos                    | 74.4 ms                                                         | 57.1 ms: 1.30x faster                                                                 |
| pathlib                  | 81.2 ms                                                         | 63.3 ms: 1.28x faster                                                                 |
| scimark_monte_carlo      | 61.9 ms                                                         | 49.4 ms: 1.25x faster                                                                 |
| pyflate                  | 422 ms                                                          | 339 ms: 1.24x faster                                                                  |
| sqlite_synth             | 2.29 us                                                         | 1.86 us: 1.23x faster                                                                 |
| spectral_norm            | 80.2 ms                                                         | 65.7 ms: 1.22x faster                                                                 |
| mako                     | 9.10 ms                                                         | 7.47 ms: 1.22x faster                                                                 |
| deepcopy                 | 310 us                                                          | 259 us: 1.20x faster                                                                  |
| scimark_sor              | 115 ms                                                          | 96.4 ms: 1.19x faster                                                                 |
| raytrace                 | 303 ms                                                          | 254 ms: 1.19x faster                                                                  |
| thrift                   | 902 us                                                          | 775 us: 1.16x faster                                                                  |
| richards_super           | 49.9 ms                                                         | 43.5 ms: 1.15x faster                                                                 |
| coroutines               | 17.9 ms                                                         | 15.9 ms: 1.13x faster                                                                 |
| xml_etree_parse          | 120 ms                                                          | 107 ms: 1.12x faster                                                                  |
| regex_dna                | 131 ms                                                          | 117 ms: 1.12x faster                                                                  |
| dulwich_log              | 58.5 ms                                                         | 52.5 ms: 1.11x faster                                                                 |
| sqlglot_parse            | 1.33 ms                                                         | 1.20 ms: 1.11x faster                                                                 |
| crypto_pyaes             | 81.3 ms                                                         | 73.2 ms: 1.11x faster                                                                 |
| html5lib                 | 52.1 ms                                                         | 47.6 ms: 1.09x faster                                                                 |
| richards                 | 40.3 ms                                                         | 36.9 ms: 1.09x faster                                                                 |
| regex_effbot             | 1.66 ms                                                         | 1.53 ms: 1.09x faster                                                                 |
| comprehensions           | 17.7 us                                                         | 16.5 us: 1.08x faster                                                                 |
| sqlglot_transpile        | 1.58 ms                                                         | 1.47 ms: 1.07x faster                                                                 |
| sympy_sum                | 122 ms                                                          | 115 ms: 1.07x faster                                                                  |
| tomli_loads              | 1.91 sec                                                        | 1.80 sec: 1.06x faster                                                                |
| pycparser                | 1.04 sec                                                        | 983 ms: 1.06x faster                                                                  |
| xml_etree_iterparse      | 70.8 ms                                                         | 67.0 ms: 1.06x faster                                                                 |
| json                     | 4.76 ms                                                         | 4.51 ms: 1.06x faster                                                                 |
| json_dumps               | 9.82 ms                                                         | 9.38 ms: 1.05x faster                                                                 |
| hexiom                   | 6.13 ms                                                         | 5.98 ms: 1.03x faster                                                                 |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 3.18 ms: 1.02x faster                                                                 |
| json_loads               | 22.4 us                                                         | 22.2 us: 1.01x faster                                                                 |
| regex_v8                 | 15.8 ms                                                         | 15.7 ms: 1.01x faster                                                                 |
| regex_compile            | 117 ms                                                          | 118 ms: 1.01x slower                                                                  |
| django_template          | 36.0 ms                                                         | 36.4 ms: 1.01x slower                                                                 |
| docutils                 | 1.95 sec                                                        | 1.97 sec: 1.01x slower                                                                |
| mdp                      | 1.83 sec                                                        | 1.86 sec: 1.02x slower                                                                |
| deepcopy_reduce          | 2.68 us                                                         | 2.75 us: 1.02x slower                                                                 |
| sympy_integrate          | 16.6 ms                                                         | 17.0 ms: 1.02x slower                                                                 |
| sympy_str                | 229 ms                                                          | 235 ms: 1.02x slower                                                                  |
| 2to3                     | 265 ms                                                          | 273 ms: 1.03x slower                                                                  |
| sympy_expand             | 391 ms                                                          | 412 ms: 1.05x slower                                                                  |
| genshi_xml               | 46.6 ms                                                         | 50.9 ms: 1.09x slower                                                                 |
| coverage                 | 46.6 ms                                                         | 51.6 ms: 1.11x slower                                                                 |
| meteor_contest           | 80.0 ms                                                         | 90.3 ms: 1.13x slower                                                                 |
| sqlglot_optimize         | 44.7 ms                                                         | 50.5 ms: 1.13x slower                                                                 |
| logging_simple           | 7.29 us                                                         | 8.30 us: 1.14x slower                                                                 |
| logging_format           | 7.91 us                                                         | 9.03 us: 1.14x slower                                                                 |
| pprint_pformat           | 1.37 sec                                                        | 1.56 sec: 1.14x slower                                                                |
| pprint_safe_repr         | 658 ms                                                          | 756 ms: 1.15x slower                                                                  |
| pickle_pure_python       | 280 us                                                          | 325 us: 1.16x slower                                                                  |
| xml_etree_process        | 48.1 ms                                                         | 56.2 ms: 1.17x slower                                                                 |
| genshi_text              | 21.0 ms                                                         | 24.5 ms: 1.17x slower                                                                 |
| scimark_fft              | 216 ms                                                          | 255 ms: 1.18x slower                                                                  |
| fannkuch                 | 317 ms                                                          | 375 ms: 1.18x slower                                                                  |
| bench_thread_pool        | 1.12 ms                                                         | 1.34 ms: 1.20x slower                                                                 |
| unpickle_pure_python     | 189 us                                                          | 227 us: 1.20x slower                                                                  |
| python_startup_no_site   | 18.1 ms                                                         | 21.7 ms: 1.20x slower                                                                 |
| nqueens                  | 87.1 ms                                                         | 106 ms: 1.22x slower                                                                  |
| xml_etree_generate       | 61.6 ms                                                         | 75.8 ms: 1.23x slower                                                                 |
| python_startup           | 22.9 ms                                                         | 28.4 ms: 1.24x slower                                                                 |
| async_generators         | 241 ms                                                          | 326 ms: 1.35x slower                                                                  |
| nbody                    | 79.1 ms                                                         | 111 ms: 1.40x slower                                                                  |
| bench_mp_pool            | 66.4 ms                                                         | 93.6 ms: 1.41x slower                                                                 |
| gc_traversal             | 1.28 ms                                                         | 1.81 ms: 1.42x slower                                                                 |
| create_gc_cycles         | 694 us                                                          | 1.05 ms: 1.51x slower                                                                 |
| telco                    | 4.83 ms                                                         | 7.80 ms: 1.62x slower                                                                 |
| Geometric mean           | (ref)                                                           | 1.08x faster                                                                          |
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20250212-3.14.0a4+-86ef9a1-JIT/bm-20250212-pythonperf1_win32-x86-brandtbucher-justin_mcmodel_again-3.14.0a4+-86ef9a1.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.083x faster

# HPT report

- Reliability score: 93.90% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown
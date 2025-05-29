# Results vs. 3.12.0

- fork: Fidget-Spinner
- ref: grand_unified_tailca
- machine: linux-x86_64
- commit hash: d07479b
- commit date: 2025-02-13
- overall geometric mean: 1.138x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.07x faster
- Memory change: 1.11x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250213-linux-x86_64-Fidget%2dSpinner-grand_unified_tailca-3.14.0a5+-d07479b |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 254 ms: 1.08x faster                                                             |
| docutils       | 2.77 sec                                               | 2.64 sec: 1.05x faster                                                           |
| Geometric mean | (ref)                                                  | 1.07x faster                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250213-linux-x86_64-Fidget%2dSpinner-grand_unified_tailca-3.14.0a5+-d07479b |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_io              | 1.16 sec                                               | 611 ms: 1.89x faster                                                             |
| async_tree_io_tg           | 1.18 sec                                               | 625 ms: 1.89x faster                                                             |
| async_tree_none            | 472 ms                                                 | 256 ms: 1.84x faster                                                             |
| async_tree_memoization     | 578 ms                                                 | 314 ms: 1.84x faster                                                             |
| async_tree_memoization_tg  | 575 ms                                                 | 314 ms: 1.83x faster                                                             |
| async_tree_none_tg         | 450 ms                                                 | 248 ms: 1.81x faster                                                             |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 514 ms: 1.41x faster                                                             |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 526 ms: 1.38x faster                                                             |
| Geometric mean             | (ref)                                                  | 1.72x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250213-linux-x86_64-Fidget%2dSpinner-grand_unified_tailca-3.14.0a5+-d07479b |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 66.2 ms: 1.28x faster                                                            |
| nbody          | 97.0 ms                                                | 86.9 ms: 1.12x faster                                                            |
| pidigits       | 187 ms                                                 | 222 ms: 1.18x slower                                                             |
| Geometric mean | (ref)                                                  | 1.06x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250213-linux-x86_64-Fidget%2dSpinner-grand_unified_tailca-3.14.0a5+-d07479b |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 124 ms: 1.19x faster                                                             |
| regex_effbot   | 3.61 ms                                                | 3.15 ms: 1.14x faster                                                            |
| regex_dna      | 212 ms                                                 | 196 ms: 1.08x faster                                                             |
| regex_v8       | 23.1 ms                                                | 24.3 ms: 1.05x slower                                                            |
| Geometric mean | (ref)                                                  | 1.09x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250213-linux-x86_64-Fidget%2dSpinner-grand_unified_tailca-3.14.0a5+-d07479b |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.81 sec: 1.29x faster                                                           |
| xml_etree_generate   | 89.2 ms                                                | 80.4 ms: 1.11x faster                                                            |
| xml_etree_process    | 61.7 ms                                                | 55.7 ms: 1.11x faster                                                            |
| unpickle_pure_python | 230 us                                                 | 211 us: 1.09x faster                                                             |
| xml_etree_iterparse  | 107 ms                                                 | 102 ms: 1.04x faster                                                             |
| pickle_pure_python   | 324 us                                                 | 312 us: 1.04x faster                                                             |
| xml_etree_parse      | 159 ms                                                 | 158 ms: 1.01x faster                                                             |
| json_loads           | 28.5 us                                                | 30.6 us: 1.07x slower                                                            |
| json_dumps           | 10.4 ms                                                | 12.2 ms: 1.17x slower                                                            |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250213-linux-x86_64-Fidget%2dSpinner-grand_unified_tailca-3.14.0a5+-d07479b |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.01 ms: 1.01x slower                                                            |
| python_startup         | 9.55 ms                                                | 12.7 ms: 1.33x slower                                                            |
| Geometric mean         | (ref)                                                  | 1.16x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250213-linux-x86_64-Fidget%2dSpinner-grand_unified_tailca-3.14.0a5+-d07479b |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| django_template | 34.6 ms                                                | 30.4 ms: 1.14x faster                                                            |
| mako            | 11.9 ms                                                | 11.0 ms: 1.08x faster                                                            |
| Geometric mean  | (ref)                                                  | 1.11x faster                                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250213-linux-x86_64-Fidget%2dSpinner-grand_unified_tailca-3.14.0a5+-d07479b |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_io              | 1.16 sec                                               | 611 ms: 1.89x faster                                                             |
| async_tree_io_tg           | 1.18 sec                                               | 625 ms: 1.89x faster                                                             |
| async_tree_none            | 472 ms                                                 | 256 ms: 1.84x faster                                                             |
| async_tree_memoization     | 578 ms                                                 | 314 ms: 1.84x faster                                                             |
| async_tree_memoization_tg  | 575 ms                                                 | 314 ms: 1.83x faster                                                             |
| async_tree_none_tg         | 450 ms                                                 | 248 ms: 1.81x faster                                                             |
| deepcopy                   | 371 us                                                 | 242 us: 1.53x faster                                                             |
| spectral_norm              | 115 ms                                                 | 81.4 ms: 1.41x faster                                                            |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 514 ms: 1.41x faster                                                             |
| deepcopy_memo              | 40.7 us                                                | 28.9 us: 1.41x faster                                                            |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 526 ms: 1.38x faster                                                             |
| deepcopy_reduce            | 3.35 us                                                | 2.47 us: 1.35x faster                                                            |
| scimark_fft                | 382 ms                                                 | 286 ms: 1.34x faster                                                             |
| pathlib                    | 19.3 ms                                                | 14.5 ms: 1.33x faster                                                            |
| comprehensions             | 21.8 us                                                | 16.8 us: 1.30x faster                                                            |
| tomli_loads                | 2.33 sec                                               | 1.81 sec: 1.29x faster                                                           |
| float                      | 84.7 ms                                                | 66.2 ms: 1.28x faster                                                            |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.00 ms: 1.26x faster                                                            |
| scimark_monte_carlo        | 75.1 ms                                                | 60.2 ms: 1.25x faster                                                            |
| chaos                      | 67.0 ms                                                | 53.9 ms: 1.24x faster                                                            |
| logging_format             | 7.23 us                                                | 5.87 us: 1.23x faster                                                            |
| logging_simple             | 6.46 us                                                | 5.29 us: 1.22x faster                                                            |
| raytrace                   | 312 ms                                                 | 258 ms: 1.21x faster                                                             |
| scimark_sor                | 129 ms                                                 | 107 ms: 1.21x faster                                                             |
| logging_silent             | 104 ns                                                 | 86.5 ns: 1.21x faster                                                            |
| regex_compile              | 148 ms                                                 | 124 ms: 1.19x faster                                                             |
| pyflate                    | 482 ms                                                 | 407 ms: 1.18x faster                                                             |
| deltablue                  | 3.72 ms                                                | 3.14 ms: 1.18x faster                                                            |
| async_generators           | 463 ms                                                 | 395 ms: 1.17x faster                                                             |
| go                         | 139 ms                                                 | 120 ms: 1.16x faster                                                             |
| sqlalchemy_declarative     | 147 ms                                                 | 127 ms: 1.16x faster                                                             |
| sympy_sum                  | 169 ms                                                 | 147 ms: 1.15x faster                                                             |
| generators                 | 31.2 ms                                                | 27.2 ms: 1.15x faster                                                            |
| richards                   | 45.8 ms                                                | 40.0 ms: 1.15x faster                                                            |
| sqlalchemy_imperative      | 18.7 ms                                                | 16.3 ms: 1.14x faster                                                            |
| regex_effbot               | 3.61 ms                                                | 3.15 ms: 1.14x faster                                                            |
| django_template            | 34.6 ms                                                | 30.4 ms: 1.14x faster                                                            |
| crypto_pyaes               | 81.9 ms                                                | 72.6 ms: 1.13x faster                                                            |
| sympy_str                  | 300 ms                                                 | 266 ms: 1.12x faster                                                             |
| scimark_lu                 | 118 ms                                                 | 105 ms: 1.12x faster                                                             |
| nbody                      | 97.0 ms                                                | 86.9 ms: 1.12x faster                                                            |
| xml_etree_generate         | 89.2 ms                                                | 80.4 ms: 1.11x faster                                                            |
| xml_etree_process          | 61.7 ms                                                | 55.7 ms: 1.11x faster                                                            |
| sympy_integrate            | 21.4 ms                                                | 19.3 ms: 1.11x faster                                                            |
| richards_super             | 51.5 ms                                                | 46.8 ms: 1.10x faster                                                            |
| unpickle_pure_python       | 230 us                                                 | 211 us: 1.09x faster                                                             |
| mako                       | 11.9 ms                                                | 11.0 ms: 1.08x faster                                                            |
| regex_dna                  | 212 ms                                                 | 196 ms: 1.08x faster                                                             |
| 2to3                       | 274 ms                                                 | 254 ms: 1.08x faster                                                             |
| nqueens                    | 83.3 ms                                                | 77.2 ms: 1.08x faster                                                            |
| sqlglot_parse              | 1.36 ms                                                | 1.26 ms: 1.08x faster                                                            |
| dulwich_log                | 68.5 ms                                                | 63.9 ms: 1.07x faster                                                            |
| sqlite_synth               | 2.83 us                                                | 2.65 us: 1.07x faster                                                            |
| sqlglot_transpile          | 1.68 ms                                                | 1.58 ms: 1.07x faster                                                            |
| sqlglot_normalize          | 110 ms                                                 | 103 ms: 1.07x faster                                                             |
| pycparser                  | 1.18 sec                                               | 1.11 sec: 1.06x faster                                                           |
| docutils                   | 2.77 sec                                               | 2.64 sec: 1.05x faster                                                           |
| sympy_expand               | 478 ms                                                 | 456 ms: 1.05x faster                                                             |
| xml_etree_iterparse        | 107 ms                                                 | 102 ms: 1.04x faster                                                             |
| pprint_safe_repr           | 776 ms                                                 | 743 ms: 1.04x faster                                                             |
| fannkuch                   | 417 ms                                                 | 400 ms: 1.04x faster                                                             |
| pickle_pure_python         | 324 us                                                 | 312 us: 1.04x faster                                                             |
| coroutines                 | 23.2 ms                                                | 22.4 ms: 1.04x faster                                                            |
| sqlglot_optimize           | 54.8 ms                                                | 52.9 ms: 1.04x faster                                                            |
| typing_runtime_protocols   | 158 us                                                 | 155 us: 1.02x faster                                                             |
| xml_etree_parse            | 159 ms                                                 | 158 ms: 1.01x faster                                                             |
| bench_thread_pool          | 842 us                                                 | 837 us: 1.01x faster                                                             |
| python_startup_no_site     | 6.94 ms                                                | 7.01 ms: 1.01x slower                                                            |
| json                       | 5.26 ms                                                | 5.49 ms: 1.04x slower                                                            |
| regex_v8                   | 23.1 ms                                                | 24.3 ms: 1.05x slower                                                            |
| json_loads                 | 28.5 us                                                | 30.6 us: 1.07x slower                                                            |
| coverage                   | 72.7 ms                                                | 79.6 ms: 1.10x slower                                                            |
| mdp                        | 2.63 sec                                               | 2.90 sec: 1.10x slower                                                           |
| json_dumps                 | 10.4 ms                                                | 12.2 ms: 1.17x slower                                                            |
| pidigits                   | 187 ms                                                 | 222 ms: 1.18x slower                                                             |
| gc_traversal               | 3.79 ms                                                | 4.98 ms: 1.31x slower                                                            |
| python_startup             | 9.55 ms                                                | 12.7 ms: 1.33x slower                                                            |
| create_gc_cycles           | 1.48 ms                                                | 2.54 ms: 1.72x slower                                                            |
| bench_mp_pool              | 24.0 ms                                                | 79.6 ms: 3.32x slower                                                            |
| Geometric mean             | (ref)                                                  | 1.12x faster                                                                     |

Benchmark hidden because not significant (5): pprint_pformat, asyncio_websockets, hexiom, meteor_contest, telco
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20250213-3.14.0a5+-d07479b-CLANG,JIT/bm-20250213-linux-x86_64-Fidget%2dSpinner-grand_unified_tailca-3.14.0a5+-d07479b.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.138x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.09x
- 95% likely to have a speedup of 1.08x
- 99% likely to have a speedup of 1.07x

# Memory
- memory change: 1.11x
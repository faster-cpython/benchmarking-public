# Results vs. 3.12.0

- fork: faster-cpython
- ref: no_conditional_stack
- machine: linux-x86_64
- commit hash: d85c001
- commit date: 2025-01-15
- overall geometric mean: 1.103x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x faster
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250115-linux-x86_64-faster%2dcpython-no_conditional_stack-3.14.0a4+-d85c001 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 255 ms: 1.07x faster                                                             |
| docutils       | 2.77 sec                                               | 2.61 sec: 1.06x faster                                                           |
| Geometric mean | (ref)                                                  | 1.07x faster                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250115-linux-x86_64-faster%2dcpython-no_conditional_stack-3.14.0a4+-d85c001 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 592 ms: 2.00x faster                                                             |
| async_tree_io              | 1.16 sec                                               | 607 ms: 1.90x faster                                                             |
| async_tree_memoization_tg  | 575 ms                                                 | 308 ms: 1.87x faster                                                             |
| async_tree_none_tg         | 450 ms                                                 | 247 ms: 1.82x faster                                                             |
| async_tree_none            | 472 ms                                                 | 261 ms: 1.81x faster                                                             |
| async_tree_memoization     | 578 ms                                                 | 326 ms: 1.77x faster                                                             |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 464 ms: 1.57x faster                                                             |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 488 ms: 1.49x faster                                                             |
| Geometric mean             | (ref)                                                  | 1.77x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250115-linux-x86_64-faster%2dcpython-no_conditional_stack-3.14.0a4+-d85c001 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 72.9 ms: 1.16x faster                                                            |
| pidigits       | 187 ms                                                 | 187 ms: 1.00x faster                                                             |
| nbody          | 97.0 ms                                                | 98.0 ms: 1.01x slower                                                            |
| Geometric mean | (ref)                                                  | 1.05x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250115-linux-x86_64-faster%2dcpython-no_conditional_stack-3.14.0a4+-d85c001 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 130 ms: 1.14x faster                                                             |
| regex_effbot   | 3.61 ms                                                | 3.41 ms: 1.06x faster                                                            |
| regex_dna      | 212 ms                                                 | 215 ms: 1.01x slower                                                             |
| regex_v8       | 23.1 ms                                                | 25.3 ms: 1.09x slower                                                            |
| Geometric mean | (ref)                                                  | 1.02x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250115-linux-x86_64-faster%2dcpython-no_conditional_stack-3.14.0a4+-d85c001 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| xml_etree_parse      | 159 ms                                                 | 138 ms: 1.16x faster                                                             |
| tomli_loads          | 2.33 sec                                               | 2.03 sec: 1.15x faster                                                           |
| xml_etree_iterparse  | 107 ms                                                 | 97.8 ms: 1.09x faster                                                            |
| xml_etree_generate   | 89.2 ms                                                | 84.1 ms: 1.06x faster                                                            |
| unpickle_pure_python | 230 us                                                 | 228 us: 1.01x faster                                                             |
| pickle_pure_python   | 324 us                                                 | 328 us: 1.01x slower                                                             |
| json_loads           | 28.5 us                                                | 29.2 us: 1.02x slower                                                            |
| json_dumps           | 10.4 ms                                                | 11.9 ms: 1.14x slower                                                            |
| Geometric mean       | (ref)                                                  | 1.03x faster                                                                     |

Benchmark hidden because not significant (1): xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250115-linux-x86_64-faster%2dcpython-no_conditional_stack-3.14.0a4+-d85c001 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.03 ms: 1.01x slower                                                            |
| python_startup         | 9.55 ms                                                | 12.8 ms: 1.34x slower                                                            |
| Geometric mean         | (ref)                                                  | 1.17x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250115-linux-x86_64-faster%2dcpython-no_conditional_stack-3.14.0a4+-d85c001 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 11.2 ms: 1.06x faster                                                            |
| django_template | 34.6 ms                                                | 32.8 ms: 1.05x faster                                                            |
| Geometric mean  | (ref)                                                  | 1.06x faster                                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250115-linux-x86_64-faster%2dcpython-no_conditional_stack-3.14.0a4+-d85c001 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 592 ms: 2.00x faster                                                             |
| async_tree_io              | 1.16 sec                                               | 607 ms: 1.90x faster                                                             |
| async_tree_memoization_tg  | 575 ms                                                 | 308 ms: 1.87x faster                                                             |
| async_tree_none_tg         | 450 ms                                                 | 247 ms: 1.82x faster                                                             |
| async_tree_none            | 472 ms                                                 | 261 ms: 1.81x faster                                                             |
| async_tree_memoization     | 578 ms                                                 | 326 ms: 1.77x faster                                                             |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 464 ms: 1.57x faster                                                             |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 488 ms: 1.49x faster                                                             |
| deepcopy                   | 371 us                                                 | 262 us: 1.42x faster                                                             |
| deepcopy_memo              | 40.7 us                                                | 31.6 us: 1.29x faster                                                            |
| comprehensions             | 21.8 us                                                | 16.9 us: 1.29x faster                                                            |
| deepcopy_reduce            | 3.35 us                                                | 2.70 us: 1.24x faster                                                            |
| pathlib                    | 19.3 ms                                                | 15.8 ms: 1.22x faster                                                            |
| async_generators           | 463 ms                                                 | 387 ms: 1.20x faster                                                             |
| go                         | 139 ms                                                 | 119 ms: 1.18x faster                                                             |
| deltablue                  | 3.72 ms                                                | 3.17 ms: 1.17x faster                                                            |
| float                      | 84.7 ms                                                | 72.9 ms: 1.16x faster                                                            |
| xml_etree_parse            | 159 ms                                                 | 138 ms: 1.16x faster                                                             |
| raytrace                   | 312 ms                                                 | 271 ms: 1.15x faster                                                             |
| sympy_sum                  | 169 ms                                                 | 147 ms: 1.15x faster                                                             |
| tomli_loads                | 2.33 sec                                               | 2.03 sec: 1.15x faster                                                           |
| regex_compile              | 148 ms                                                 | 130 ms: 1.14x faster                                                             |
| generators                 | 31.2 ms                                                | 27.4 ms: 1.14x faster                                                            |
| crypto_pyaes               | 81.9 ms                                                | 72.1 ms: 1.14x faster                                                            |
| logging_format             | 7.23 us                                                | 6.41 us: 1.13x faster                                                            |
| sqlalchemy_declarative     | 147 ms                                                 | 131 ms: 1.12x faster                                                             |
| sqlalchemy_imperative      | 18.7 ms                                                | 16.8 ms: 1.11x faster                                                            |
| sympy_str                  | 300 ms                                                 | 270 ms: 1.11x faster                                                             |
| logging_simple             | 6.46 us                                                | 5.82 us: 1.11x faster                                                            |
| spectral_norm              | 115 ms                                                 | 104 ms: 1.10x faster                                                             |
| chaos                      | 67.0 ms                                                | 60.8 ms: 1.10x faster                                                            |
| scimark_monte_carlo        | 75.1 ms                                                | 68.6 ms: 1.09x faster                                                            |
| xml_etree_iterparse        | 107 ms                                                 | 97.8 ms: 1.09x faster                                                            |
| scimark_fft                | 382 ms                                                 | 350 ms: 1.09x faster                                                             |
| sqlglot_parse              | 1.36 ms                                                | 1.26 ms: 1.08x faster                                                            |
| sympy_integrate            | 21.4 ms                                                | 19.9 ms: 1.08x faster                                                            |
| 2to3                       | 274 ms                                                 | 255 ms: 1.07x faster                                                             |
| sqlglot_transpile          | 1.68 ms                                                | 1.57 ms: 1.07x faster                                                            |
| mdp                        | 2.63 sec                                               | 2.48 sec: 1.06x faster                                                           |
| scimark_sor                | 129 ms                                                 | 122 ms: 1.06x faster                                                             |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.76 ms: 1.06x faster                                                            |
| docutils                   | 2.77 sec                                               | 2.61 sec: 1.06x faster                                                           |
| mako                       | 11.9 ms                                                | 11.2 ms: 1.06x faster                                                            |
| regex_effbot               | 3.61 ms                                                | 3.41 ms: 1.06x faster                                                            |
| xml_etree_generate         | 89.2 ms                                                | 84.1 ms: 1.06x faster                                                            |
| meteor_contest             | 112 ms                                                 | 106 ms: 1.06x faster                                                             |
| django_template            | 34.6 ms                                                | 32.8 ms: 1.05x faster                                                            |
| pprint_safe_repr           | 776 ms                                                 | 736 ms: 1.05x faster                                                             |
| dulwich_log                | 68.5 ms                                                | 65.0 ms: 1.05x faster                                                            |
| sqlglot_normalize          | 110 ms                                                 | 105 ms: 1.05x faster                                                             |
| sympy_expand               | 478 ms                                                 | 457 ms: 1.05x faster                                                             |
| fannkuch                   | 417 ms                                                 | 402 ms: 1.04x faster                                                             |
| pprint_pformat             | 1.57 sec                                               | 1.51 sec: 1.04x faster                                                           |
| nqueens                    | 83.3 ms                                                | 80.5 ms: 1.03x faster                                                            |
| sqlglot_optimize           | 54.8 ms                                                | 53.2 ms: 1.03x faster                                                            |
| pyflate                    | 482 ms                                                 | 471 ms: 1.02x faster                                                             |
| scimark_lu                 | 118 ms                                                 | 115 ms: 1.02x faster                                                             |
| richards                   | 45.8 ms                                                | 44.8 ms: 1.02x faster                                                            |
| hexiom                     | 6.41 ms                                                | 6.28 ms: 1.02x faster                                                            |
| richards_super             | 51.5 ms                                                | 50.7 ms: 1.02x faster                                                            |
| sqlite_synth               | 2.83 us                                                | 2.80 us: 1.01x faster                                                            |
| unpickle_pure_python       | 230 us                                                 | 228 us: 1.01x faster                                                             |
| pidigits                   | 187 ms                                                 | 187 ms: 1.00x faster                                                             |
| coroutines                 | 23.2 ms                                                | 23.4 ms: 1.01x slower                                                            |
| nbody                      | 97.0 ms                                                | 98.0 ms: 1.01x slower                                                            |
| pickle_pure_python         | 324 us                                                 | 328 us: 1.01x slower                                                             |
| regex_dna                  | 212 ms                                                 | 215 ms: 1.01x slower                                                             |
| python_startup_no_site     | 6.94 ms                                                | 7.03 ms: 1.01x slower                                                            |
| json_loads                 | 28.5 us                                                | 29.2 us: 1.02x slower                                                            |
| logging_silent             | 104 ns                                                 | 108 ns: 1.03x slower                                                             |
| bench_thread_pool          | 842 us                                                 | 870 us: 1.03x slower                                                             |
| typing_runtime_protocols   | 158 us                                                 | 165 us: 1.04x slower                                                             |
| regex_v8                   | 23.1 ms                                                | 25.3 ms: 1.09x slower                                                            |
| telco                      | 7.10 ms                                                | 7.91 ms: 1.11x slower                                                            |
| json_dumps                 | 10.4 ms                                                | 11.9 ms: 1.14x slower                                                            |
| coverage                   | 72.7 ms                                                | 90.3 ms: 1.24x slower                                                            |
| gc_traversal               | 3.79 ms                                                | 4.78 ms: 1.26x slower                                                            |
| python_startup             | 9.55 ms                                                | 12.8 ms: 1.34x slower                                                            |
| create_gc_cycles           | 1.48 ms                                                | 2.46 ms: 1.67x slower                                                            |
| bench_mp_pool              | 24.0 ms                                                | 81.2 ms: 3.38x slower                                                            |
| Geometric mean             | (ref)                                                  | 1.08x faster                                                                     |

Benchmark hidden because not significant (4): pycparser, xml_etree_process, json, asyncio_websockets
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20250115-3.14.0a4+-d85c001/bm-20250115-linux-x86_64-faster%2dcpython-no_conditional_stack-3.14.0a4+-d85c001.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.103x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.05x

# Memory
- memory change: 1.09x
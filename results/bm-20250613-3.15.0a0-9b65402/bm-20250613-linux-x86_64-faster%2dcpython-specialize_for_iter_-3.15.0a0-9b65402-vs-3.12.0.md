# Results vs. 3.12.0

- fork: faster-cpython
- ref: specialize_for_iter_
- machine: linux-x86_64
- commit hash: 9b65402
- commit date: 2025-06-13
- overall geometric mean: 1.093x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x faster
- Memory change: 1.13x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250613-linux-x86_64-faster%2dcpython-specialize_for_iter_-3.15.0a0-9b65402 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 254 ms: 1.08x faster                                                            |
| docutils       | 2.77 sec                                               | 2.56 sec: 1.08x faster                                                          |
| Geometric mean | (ref)                                                  | 1.08x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250613-linux-x86_64-faster%2dcpython-specialize_for_iter_-3.15.0a0-9b65402 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 611 ms: 1.93x faster                                                            |
| async_tree_io              | 1.16 sec                                               | 598 ms: 1.93x faster                                                            |
| async_tree_memoization     | 578 ms                                                 | 313 ms: 1.84x faster                                                            |
| async_tree_memoization_tg  | 575 ms                                                 | 314 ms: 1.83x faster                                                            |
| async_tree_none            | 472 ms                                                 | 259 ms: 1.82x faster                                                            |
| async_tree_none_tg         | 450 ms                                                 | 249 ms: 1.80x faster                                                            |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 488 ms: 1.49x faster                                                            |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 496 ms: 1.46x faster                                                            |
| Geometric mean             | (ref)                                                  | 1.76x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250613-linux-x86_64-faster%2dcpython-specialize_for_iter_-3.15.0a0-9b65402 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 73.9 ms: 1.15x faster                                                           |
| pidigits       | 187 ms                                                 | 188 ms: 1.01x slower                                                            |
| nbody          | 97.0 ms                                                | 100 ms: 1.03x slower                                                            |
| Geometric mean | (ref)                                                  | 1.03x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250613-linux-x86_64-faster%2dcpython-specialize_for_iter_-3.15.0a0-9b65402 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 127 ms: 1.16x faster                                                            |
| regex_effbot   | 3.61 ms                                                | 3.11 ms: 1.16x faster                                                           |
| regex_dna      | 212 ms                                                 | 184 ms: 1.15x faster                                                            |
| regex_v8       | 23.1 ms                                                | 22.1 ms: 1.05x faster                                                           |
| Geometric mean | (ref)                                                  | 1.13x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250613-linux-x86_64-faster%2dcpython-specialize_for_iter_-3.15.0a0-9b65402 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.99 sec: 1.17x faster                                                          |
| xml_etree_parse      | 159 ms                                                 | 141 ms: 1.13x faster                                                            |
| xml_etree_iterparse  | 107 ms                                                 | 99.3 ms: 1.08x faster                                                           |
| unpickle_pure_python | 230 us                                                 | 220 us: 1.05x faster                                                            |
| xml_etree_generate   | 89.2 ms                                                | 85.4 ms: 1.04x faster                                                           |
| json_loads           | 28.5 us                                                | 27.7 us: 1.03x faster                                                           |
| xml_etree_process    | 61.7 ms                                                | 60.2 ms: 1.03x faster                                                           |
| pickle_pure_python   | 324 us                                                 | 317 us: 1.02x faster                                                            |
| json_dumps           | 10.4 ms                                                | 10.9 ms: 1.05x slower                                                           |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250613-linux-x86_64-faster%2dcpython-specialize_for_iter_-3.15.0a0-9b65402 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 6.91 ms: 1.00x faster                                                           |
| python_startup         | 9.55 ms                                                | 12.2 ms: 1.27x slower                                                           |
| Geometric mean         | (ref)                                                  | 1.13x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250613-linux-x86_64-faster%2dcpython-specialize_for_iter_-3.15.0a0-9b65402 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| django_template | 34.6 ms                                                | 32.2 ms: 1.07x faster                                                           |
| mako            | 11.9 ms                                                | 11.3 ms: 1.05x faster                                                           |
| Geometric mean  | (ref)                                                  | 1.06x faster                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250613-linux-x86_64-faster%2dcpython-specialize_for_iter_-3.15.0a0-9b65402 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mdp                        | 2.63 sec                                               | 1.23 sec: 2.14x faster                                                          |
| async_tree_io_tg           | 1.18 sec                                               | 611 ms: 1.93x faster                                                            |
| async_tree_io              | 1.16 sec                                               | 598 ms: 1.93x faster                                                            |
| async_tree_memoization     | 578 ms                                                 | 313 ms: 1.84x faster                                                            |
| async_tree_memoization_tg  | 575 ms                                                 | 314 ms: 1.83x faster                                                            |
| async_tree_none            | 472 ms                                                 | 259 ms: 1.82x faster                                                            |
| async_tree_none_tg         | 450 ms                                                 | 249 ms: 1.80x faster                                                            |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 488 ms: 1.49x faster                                                            |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 496 ms: 1.46x faster                                                            |
| deepcopy                   | 371 us                                                 | 261 us: 1.42x faster                                                            |
| deepcopy_memo              | 40.7 us                                                | 29.2 us: 1.40x faster                                                           |
| comprehensions             | 21.8 us                                                | 16.0 us: 1.36x faster                                                           |
| go                         | 139 ms                                                 | 112 ms: 1.24x faster                                                            |
| deepcopy_reduce            | 3.35 us                                                | 2.72 us: 1.23x faster                                                           |
| tomli_loads                | 2.33 sec                                               | 1.99 sec: 1.17x faster                                                          |
| regex_compile              | 148 ms                                                 | 127 ms: 1.16x faster                                                            |
| regex_effbot               | 3.61 ms                                                | 3.11 ms: 1.16x faster                                                           |
| raytrace                   | 312 ms                                                 | 270 ms: 1.15x faster                                                            |
| dulwich_log                | 68.5 ms                                                | 59.5 ms: 1.15x faster                                                           |
| regex_dna                  | 212 ms                                                 | 184 ms: 1.15x faster                                                            |
| float                      | 84.7 ms                                                | 73.9 ms: 1.15x faster                                                           |
| async_generators           | 463 ms                                                 | 407 ms: 1.14x faster                                                            |
| sympy_sum                  | 169 ms                                                 | 149 ms: 1.14x faster                                                            |
| pathlib                    | 19.3 ms                                                | 17.0 ms: 1.14x faster                                                           |
| xml_etree_parse            | 159 ms                                                 | 141 ms: 1.13x faster                                                            |
| sympy_integrate            | 21.4 ms                                                | 19.0 ms: 1.13x faster                                                           |
| chaos                      | 67.0 ms                                                | 59.5 ms: 1.13x faster                                                           |
| pyflate                    | 482 ms                                                 | 430 ms: 1.12x faster                                                            |
| sympy_str                  | 300 ms                                                 | 268 ms: 1.12x faster                                                            |
| scimark_monte_carlo        | 75.1 ms                                                | 68.4 ms: 1.10x faster                                                           |
| crypto_pyaes               | 81.9 ms                                                | 75.1 ms: 1.09x faster                                                           |
| docutils                   | 2.77 sec                                               | 2.56 sec: 1.08x faster                                                          |
| 2to3                       | 274 ms                                                 | 254 ms: 1.08x faster                                                            |
| scimark_sor                | 129 ms                                                 | 120 ms: 1.08x faster                                                            |
| xml_etree_iterparse        | 107 ms                                                 | 99.3 ms: 1.08x faster                                                           |
| django_template            | 34.6 ms                                                | 32.2 ms: 1.07x faster                                                           |
| meteor_contest             | 112 ms                                                 | 105 ms: 1.07x faster                                                            |
| hexiom                     | 6.41 ms                                                | 6.03 ms: 1.06x faster                                                           |
| pycparser                  | 1.18 sec                                               | 1.11 sec: 1.06x faster                                                          |
| richards                   | 45.8 ms                                                | 43.4 ms: 1.06x faster                                                           |
| spectral_norm              | 115 ms                                                 | 109 ms: 1.05x faster                                                            |
| mako                       | 11.9 ms                                                | 11.3 ms: 1.05x faster                                                           |
| logging_format             | 7.23 us                                                | 6.89 us: 1.05x faster                                                           |
| sympy_expand               | 478 ms                                                 | 455 ms: 1.05x faster                                                            |
| deltablue                  | 3.72 ms                                                | 3.54 ms: 1.05x faster                                                           |
| logging_simple             | 6.46 us                                                | 6.17 us: 1.05x faster                                                           |
| unpickle_pure_python       | 230 us                                                 | 220 us: 1.05x faster                                                            |
| regex_v8                   | 23.1 ms                                                | 22.1 ms: 1.05x faster                                                           |
| xml_etree_generate         | 89.2 ms                                                | 85.4 ms: 1.04x faster                                                           |
| generators                 | 31.2 ms                                                | 30.0 ms: 1.04x faster                                                           |
| richards_super             | 51.5 ms                                                | 49.5 ms: 1.04x faster                                                           |
| json_loads                 | 28.5 us                                                | 27.7 us: 1.03x faster                                                           |
| xml_etree_process          | 61.7 ms                                                | 60.2 ms: 1.03x faster                                                           |
| nqueens                    | 83.3 ms                                                | 81.3 ms: 1.02x faster                                                           |
| pickle_pure_python         | 324 us                                                 | 317 us: 1.02x faster                                                            |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.97 ms: 1.02x faster                                                           |
| json                       | 5.26 ms                                                | 5.22 ms: 1.01x faster                                                           |
| fannkuch                   | 417 ms                                                 | 414 ms: 1.01x faster                                                            |
| python_startup_no_site     | 6.94 ms                                                | 6.91 ms: 1.00x faster                                                           |
| pidigits                   | 187 ms                                                 | 188 ms: 1.01x slower                                                            |
| scimark_fft                | 382 ms                                                 | 384 ms: 1.01x slower                                                            |
| sqlite_synth               | 2.83 us                                                | 2.86 us: 1.01x slower                                                           |
| nbody                      | 97.0 ms                                                | 100 ms: 1.03x slower                                                            |
| json_dumps                 | 10.4 ms                                                | 10.9 ms: 1.05x slower                                                           |
| pprint_safe_repr           | 776 ms                                                 | 818 ms: 1.05x slower                                                            |
| pprint_pformat             | 1.57 sec                                               | 1.67 sec: 1.06x slower                                                          |
| typing_runtime_protocols   | 158 us                                                 | 170 us: 1.08x slower                                                            |
| coroutines                 | 23.2 ms                                                | 25.0 ms: 1.08x slower                                                           |
| telco                      | 7.10 ms                                                | 8.02 ms: 1.13x slower                                                           |
| python_startup             | 9.55 ms                                                | 12.2 ms: 1.27x slower                                                           |
| gc_traversal               | 3.79 ms                                                | 5.17 ms: 1.36x slower                                                           |
| create_gc_cycles           | 1.48 ms                                                | 2.58 ms: 1.75x slower                                                           |
| logging_silent             | 104 ns                                                 | 473 ns: 4.53x slower                                                            |
| coverage                   | 72.7 ms                                                | 419 ms: 5.76x slower                                                            |
| Geometric mean             | (ref)                                                  | 1.07x faster                                                                    |

Benchmark hidden because not significant (2): scimark_lu, asyncio_websockets
Ignored benchmarks (22) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250613-3.15.0a0-9b65402/bm-20250613-linux-x86_64-faster%2dcpython-specialize_for_iter_-3.15.0a0-9b65402.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.093x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.06x
- 99% likely to have a speedup of 1.05x

# Memory
- memory change: 1.13x
# Results vs. 3.12.0

- fork: faster-cpython
- ref: specialize_for_compa
- machine: linux-x86_64
- commit hash: e27d994
- commit date: 2025-06-18
- overall geometric mean: 1.122x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x faster
- Memory change: 1.13x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250618-linux-x86_64-faster%2dcpython-specialize_for_compa-3.15.0a0-e27d994 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 254 ms: 1.08x faster                                                            |
| docutils       | 2.77 sec                                               | 2.56 sec: 1.08x faster                                                          |
| Geometric mean | (ref)                                                  | 1.08x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250618-linux-x86_64-faster%2dcpython-specialize_for_compa-3.15.0a0-e27d994 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_io              | 1.16 sec                                               | 595 ms: 1.94x faster                                                            |
| async_tree_io_tg           | 1.18 sec                                               | 628 ms: 1.88x faster                                                            |
| async_tree_memoization_tg  | 575 ms                                                 | 306 ms: 1.88x faster                                                            |
| async_tree_memoization     | 578 ms                                                 | 309 ms: 1.87x faster                                                            |
| async_tree_none            | 472 ms                                                 | 258 ms: 1.83x faster                                                            |
| async_tree_none_tg         | 450 ms                                                 | 247 ms: 1.82x faster                                                            |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 479 ms: 1.52x faster                                                            |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 488 ms: 1.49x faster                                                            |
| Geometric mean             | (ref)                                                  | 1.77x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250618-linux-x86_64-faster%2dcpython-specialize_for_compa-3.15.0a0-e27d994 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 72.5 ms: 1.17x faster                                                           |
| pidigits       | 187 ms                                                 | 188 ms: 1.01x slower                                                            |
| nbody          | 97.0 ms                                                | 98.5 ms: 1.02x slower                                                           |
| Geometric mean | (ref)                                                  | 1.05x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250618-linux-x86_64-faster%2dcpython-specialize_for_compa-3.15.0a0-e27d994 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 126 ms: 1.18x faster                                                            |
| regex_effbot   | 3.61 ms                                                | 3.27 ms: 1.10x faster                                                           |
| regex_dna      | 212 ms                                                 | 203 ms: 1.05x faster                                                            |
| regex_v8       | 23.1 ms                                                | 22.2 ms: 1.04x faster                                                           |
| Geometric mean | (ref)                                                  | 1.09x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250618-linux-x86_64-faster%2dcpython-specialize_for_compa-3.15.0a0-e27d994 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.96 sec: 1.19x faster                                                          |
| xml_etree_parse      | 159 ms                                                 | 141 ms: 1.13x faster                                                            |
| xml_etree_iterparse  | 107 ms                                                 | 98.0 ms: 1.09x faster                                                           |
| unpickle_pure_python | 230 us                                                 | 217 us: 1.06x faster                                                            |
| xml_etree_generate   | 89.2 ms                                                | 85.1 ms: 1.05x faster                                                           |
| xml_etree_process    | 61.7 ms                                                | 59.9 ms: 1.03x faster                                                           |
| json_loads           | 28.5 us                                                | 28.0 us: 1.02x faster                                                           |
| pickle_pure_python   | 324 us                                                 | 319 us: 1.01x faster                                                            |
| json_dumps           | 10.4 ms                                                | 11.1 ms: 1.07x slower                                                           |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250618-linux-x86_64-faster%2dcpython-specialize_for_compa-3.15.0a0-e27d994 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 6.91 ms: 1.00x faster                                                           |
| python_startup         | 9.55 ms                                                | 12.2 ms: 1.27x slower                                                           |
| Geometric mean         | (ref)                                                  | 1.13x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250618-linux-x86_64-faster%2dcpython-specialize_for_compa-3.15.0a0-e27d994 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| django_template | 34.6 ms                                                | 32.9 ms: 1.05x faster                                                           |
| mako            | 11.9 ms                                                | 11.7 ms: 1.01x faster                                                           |
| Geometric mean  | (ref)                                                  | 1.03x faster                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250618-linux-x86_64-faster%2dcpython-specialize_for_compa-3.15.0a0-e27d994 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mdp                        | 2.63 sec                                               | 1.22 sec: 2.15x faster                                                          |
| async_tree_io              | 1.16 sec                                               | 595 ms: 1.94x faster                                                            |
| async_tree_io_tg           | 1.18 sec                                               | 628 ms: 1.88x faster                                                            |
| async_tree_memoization_tg  | 575 ms                                                 | 306 ms: 1.88x faster                                                            |
| async_tree_memoization     | 578 ms                                                 | 309 ms: 1.87x faster                                                            |
| async_tree_none            | 472 ms                                                 | 258 ms: 1.83x faster                                                            |
| async_tree_none_tg         | 450 ms                                                 | 247 ms: 1.82x faster                                                            |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 479 ms: 1.52x faster                                                            |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 488 ms: 1.49x faster                                                            |
| deepcopy                   | 371 us                                                 | 255 us: 1.46x faster                                                            |
| deepcopy_memo              | 40.7 us                                                | 29.1 us: 1.40x faster                                                           |
| comprehensions             | 21.8 us                                                | 16.1 us: 1.35x faster                                                           |
| go                         | 139 ms                                                 | 111 ms: 1.26x faster                                                            |
| deepcopy_reduce            | 3.35 us                                                | 2.68 us: 1.25x faster                                                           |
| tomli_loads                | 2.33 sec                                               | 1.96 sec: 1.19x faster                                                          |
| regex_compile              | 148 ms                                                 | 126 ms: 1.18x faster                                                            |
| float                      | 84.7 ms                                                | 72.5 ms: 1.17x faster                                                           |
| dulwich_log                | 68.5 ms                                                | 58.8 ms: 1.17x faster                                                           |
| raytrace                   | 312 ms                                                 | 270 ms: 1.16x faster                                                            |
| spectral_norm              | 115 ms                                                 | 99.3 ms: 1.16x faster                                                           |
| pyflate                    | 482 ms                                                 | 419 ms: 1.15x faster                                                            |
| sympy_sum                  | 169 ms                                                 | 147 ms: 1.15x faster                                                            |
| pathlib                    | 19.3 ms                                                | 17.0 ms: 1.14x faster                                                           |
| scimark_monte_carlo        | 75.1 ms                                                | 65.9 ms: 1.14x faster                                                           |
| sympy_integrate            | 21.4 ms                                                | 18.9 ms: 1.13x faster                                                           |
| sympy_str                  | 300 ms                                                 | 265 ms: 1.13x faster                                                            |
| xml_etree_parse            | 159 ms                                                 | 141 ms: 1.13x faster                                                            |
| async_generators           | 463 ms                                                 | 410 ms: 1.13x faster                                                            |
| chaos                      | 67.0 ms                                                | 59.4 ms: 1.13x faster                                                           |
| regex_effbot               | 3.61 ms                                                | 3.27 ms: 1.10x faster                                                           |
| scimark_sor                | 129 ms                                                 | 118 ms: 1.09x faster                                                            |
| xml_etree_iterparse        | 107 ms                                                 | 98.0 ms: 1.09x faster                                                           |
| logging_format             | 7.23 us                                                | 6.65 us: 1.09x faster                                                           |
| docutils                   | 2.77 sec                                               | 2.56 sec: 1.08x faster                                                          |
| 2to3                       | 274 ms                                                 | 254 ms: 1.08x faster                                                            |
| crypto_pyaes               | 81.9 ms                                                | 76.4 ms: 1.07x faster                                                           |
| hexiom                     | 6.41 ms                                                | 6.00 ms: 1.07x faster                                                           |
| logging_simple             | 6.46 us                                                | 6.05 us: 1.07x faster                                                           |
| deltablue                  | 3.72 ms                                                | 3.49 ms: 1.06x faster                                                           |
| sympy_expand               | 478 ms                                                 | 449 ms: 1.06x faster                                                            |
| unpickle_pure_python       | 230 us                                                 | 217 us: 1.06x faster                                                            |
| meteor_contest             | 112 ms                                                 | 106 ms: 1.06x faster                                                            |
| richards                   | 45.8 ms                                                | 43.3 ms: 1.06x faster                                                           |
| scimark_fft                | 382 ms                                                 | 362 ms: 1.06x faster                                                            |
| django_template            | 34.6 ms                                                | 32.9 ms: 1.05x faster                                                           |
| generators                 | 31.2 ms                                                | 29.7 ms: 1.05x faster                                                           |
| pycparser                  | 1.18 sec                                               | 1.12 sec: 1.05x faster                                                          |
| xml_etree_generate         | 89.2 ms                                                | 85.1 ms: 1.05x faster                                                           |
| regex_dna                  | 212 ms                                                 | 203 ms: 1.05x faster                                                            |
| regex_v8                   | 23.1 ms                                                | 22.2 ms: 1.04x faster                                                           |
| richards_super             | 51.5 ms                                                | 49.6 ms: 1.04x faster                                                           |
| nqueens                    | 83.3 ms                                                | 80.3 ms: 1.04x faster                                                           |
| xml_etree_process          | 61.7 ms                                                | 59.9 ms: 1.03x faster                                                           |
| fannkuch                   | 417 ms                                                 | 407 ms: 1.02x faster                                                            |
| json_loads                 | 28.5 us                                                | 28.0 us: 1.02x faster                                                           |
| pickle_pure_python         | 324 us                                                 | 319 us: 1.01x faster                                                            |
| mako                       | 11.9 ms                                                | 11.7 ms: 1.01x faster                                                           |
| python_startup_no_site     | 6.94 ms                                                | 6.91 ms: 1.00x faster                                                           |
| pidigits                   | 187 ms                                                 | 188 ms: 1.01x slower                                                            |
| sqlite_synth               | 2.83 us                                                | 2.86 us: 1.01x slower                                                           |
| nbody                      | 97.0 ms                                                | 98.5 ms: 1.02x slower                                                           |
| pprint_safe_repr           | 776 ms                                                 | 797 ms: 1.03x slower                                                            |
| typing_runtime_protocols   | 158 us                                                 | 164 us: 1.04x slower                                                            |
| pprint_pformat             | 1.57 sec                                               | 1.63 sec: 1.04x slower                                                          |
| coroutines                 | 23.2 ms                                                | 24.5 ms: 1.06x slower                                                           |
| json_dumps                 | 10.4 ms                                                | 11.1 ms: 1.07x slower                                                           |
| telco                      | 7.10 ms                                                | 8.04 ms: 1.13x slower                                                           |
| coverage                   | 72.7 ms                                                | 87.8 ms: 1.21x slower                                                           |
| python_startup             | 9.55 ms                                                | 12.2 ms: 1.27x slower                                                           |
| gc_traversal               | 3.79 ms                                                | 5.11 ms: 1.35x slower                                                           |
| create_gc_cycles           | 1.48 ms                                                | 2.57 ms: 1.74x slower                                                           |
| logging_silent             | 104 ns                                                 | 469 ns: 4.49x slower                                                            |
| Geometric mean             | (ref)                                                  | 1.10x faster                                                                    |

Benchmark hidden because not significant (4): json, asyncio_websockets, scimark_sparse_mat_mult, scimark_lu
Ignored benchmarks (22) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (17) of results/bm-20250618-3.15.0a0-e27d994/bm-20250618-linux-x86_64-faster%2dcpython-specialize_for_compa-3.15.0a0-e27d994.json: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.122x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.06x
- 99% likely to have a speedup of 1.05x

# Memory
- memory change: 1.13x
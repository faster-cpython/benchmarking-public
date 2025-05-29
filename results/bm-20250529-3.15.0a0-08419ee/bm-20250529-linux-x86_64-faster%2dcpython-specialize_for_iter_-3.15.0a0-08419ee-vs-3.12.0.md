# Results vs. 3.12.0

- fork: faster-cpython
- ref: specialize_for_iter_
- machine: linux-x86_64
- commit hash: 08419ee
- commit date: 2025-05-29
- overall geometric mean: 1.073x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: 1.13x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250529-linux-x86_64-faster%2dcpython-specialize_for_iter_-3.15.0a0-08419ee |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 256 ms: 1.07x faster                                                            |
| docutils       | 2.77 sec                                               | 2.57 sec: 1.08x faster                                                          |
| Geometric mean | (ref)                                                  | 1.07x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250529-linux-x86_64-faster%2dcpython-specialize_for_iter_-3.15.0a0-08419ee |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_io              | 1.16 sec                                               | 602 ms: 1.92x faster                                                            |
| async_tree_io_tg           | 1.18 sec                                               | 626 ms: 1.89x faster                                                            |
| async_tree_memoization     | 578 ms                                                 | 314 ms: 1.84x faster                                                            |
| async_tree_memoization_tg  | 575 ms                                                 | 317 ms: 1.81x faster                                                            |
| async_tree_none            | 472 ms                                                 | 262 ms: 1.80x faster                                                            |
| async_tree_none_tg         | 450 ms                                                 | 253 ms: 1.78x faster                                                            |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 489 ms: 1.48x faster                                                            |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 495 ms: 1.47x faster                                                            |
| Geometric mean             | (ref)                                                  | 1.74x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250529-linux-x86_64-faster%2dcpython-specialize_for_iter_-3.15.0a0-08419ee |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 73.0 ms: 1.16x faster                                                           |
| pidigits       | 187 ms                                                 | 188 ms: 1.00x slower                                                            |
| nbody          | 97.0 ms                                                | 100 ms: 1.03x slower                                                            |
| Geometric mean | (ref)                                                  | 1.04x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250529-linux-x86_64-faster%2dcpython-specialize_for_iter_-3.15.0a0-08419ee |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 128 ms: 1.16x faster                                                            |
| regex_effbot   | 3.61 ms                                                | 3.23 ms: 1.12x faster                                                           |
| regex_dna      | 212 ms                                                 | 209 ms: 1.02x faster                                                            |
| Geometric mean | (ref)                                                  | 1.07x faster                                                                    |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250529-linux-x86_64-faster%2dcpython-specialize_for_iter_-3.15.0a0-08419ee |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 2.01 sec: 1.16x faster                                                          |
| xml_etree_parse      | 159 ms                                                 | 143 ms: 1.11x faster                                                            |
| xml_etree_iterparse  | 107 ms                                                 | 99.2 ms: 1.08x faster                                                           |
| xml_etree_generate   | 89.2 ms                                                | 84.8 ms: 1.05x faster                                                           |
| unpickle_pure_python | 230 us                                                 | 219 us: 1.05x faster                                                            |
| xml_etree_process    | 61.7 ms                                                | 59.5 ms: 1.04x faster                                                           |
| pickle_pure_python   | 324 us                                                 | 319 us: 1.02x faster                                                            |
| json_loads           | 28.5 us                                                | 29.8 us: 1.05x slower                                                           |
| json_dumps           | 10.4 ms                                                | 11.2 ms: 1.08x slower                                                           |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250529-linux-x86_64-faster%2dcpython-specialize_for_iter_-3.15.0a0-08419ee |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 6.92 ms: 1.00x faster                                                           |
| python_startup         | 9.55 ms                                                | 12.2 ms: 1.28x slower                                                           |
| Geometric mean         | (ref)                                                  | 1.13x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250529-linux-x86_64-faster%2dcpython-specialize_for_iter_-3.15.0a0-08419ee |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| django_template | 34.6 ms                                                | 32.3 ms: 1.07x faster                                                           |
| mako            | 11.9 ms                                                | 11.3 ms: 1.05x faster                                                           |
| Geometric mean  | (ref)                                                  | 1.06x faster                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250529-linux-x86_64-faster%2dcpython-specialize_for_iter_-3.15.0a0-08419ee |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mdp                        | 2.63 sec                                               | 1.23 sec: 2.14x faster                                                          |
| async_tree_io              | 1.16 sec                                               | 602 ms: 1.92x faster                                                            |
| async_tree_io_tg           | 1.18 sec                                               | 626 ms: 1.89x faster                                                            |
| async_tree_memoization     | 578 ms                                                 | 314 ms: 1.84x faster                                                            |
| async_tree_memoization_tg  | 575 ms                                                 | 317 ms: 1.81x faster                                                            |
| async_tree_none            | 472 ms                                                 | 262 ms: 1.80x faster                                                            |
| async_tree_none_tg         | 450 ms                                                 | 253 ms: 1.78x faster                                                            |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 489 ms: 1.48x faster                                                            |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 495 ms: 1.47x faster                                                            |
| deepcopy                   | 371 us                                                 | 257 us: 1.45x faster                                                            |
| deepcopy_memo              | 40.7 us                                                | 29.6 us: 1.38x faster                                                           |
| comprehensions             | 21.8 us                                                | 16.2 us: 1.34x faster                                                           |
| go                         | 139 ms                                                 | 114 ms: 1.22x faster                                                            |
| deepcopy_reduce            | 3.35 us                                                | 2.74 us: 1.22x faster                                                           |
| regex_compile              | 148 ms                                                 | 128 ms: 1.16x faster                                                            |
| float                      | 84.7 ms                                                | 73.0 ms: 1.16x faster                                                           |
| tomli_loads                | 2.33 sec                                               | 2.01 sec: 1.16x faster                                                          |
| pathlib                    | 19.3 ms                                                | 16.7 ms: 1.16x faster                                                           |
| raytrace                   | 312 ms                                                 | 272 ms: 1.15x faster                                                            |
| dulwich_log                | 68.5 ms                                                | 59.9 ms: 1.14x faster                                                           |
| sympy_sum                  | 169 ms                                                 | 149 ms: 1.14x faster                                                            |
| sympy_integrate            | 21.4 ms                                                | 19.0 ms: 1.13x faster                                                           |
| async_generators           | 463 ms                                                 | 411 ms: 1.13x faster                                                            |
| sympy_str                  | 300 ms                                                 | 266 ms: 1.13x faster                                                            |
| pyflate                    | 482 ms                                                 | 429 ms: 1.13x faster                                                            |
| chaos                      | 67.0 ms                                                | 59.6 ms: 1.12x faster                                                           |
| regex_effbot               | 3.61 ms                                                | 3.23 ms: 1.12x faster                                                           |
| xml_etree_parse            | 159 ms                                                 | 143 ms: 1.11x faster                                                            |
| scimark_monte_carlo        | 75.1 ms                                                | 67.8 ms: 1.11x faster                                                           |
| crypto_pyaes               | 81.9 ms                                                | 73.9 ms: 1.11x faster                                                           |
| docutils                   | 2.77 sec                                               | 2.57 sec: 1.08x faster                                                          |
| xml_etree_iterparse        | 107 ms                                                 | 99.2 ms: 1.08x faster                                                           |
| 2to3                       | 274 ms                                                 | 256 ms: 1.07x faster                                                            |
| logging_format             | 7.23 us                                                | 6.74 us: 1.07x faster                                                           |
| django_template            | 34.6 ms                                                | 32.3 ms: 1.07x faster                                                           |
| meteor_contest             | 112 ms                                                 | 105 ms: 1.07x faster                                                            |
| scimark_sor                | 129 ms                                                 | 121 ms: 1.07x faster                                                            |
| logging_simple             | 6.46 us                                                | 6.06 us: 1.07x faster                                                           |
| sympy_expand               | 478 ms                                                 | 450 ms: 1.06x faster                                                            |
| mako                       | 11.9 ms                                                | 11.3 ms: 1.05x faster                                                           |
| hexiom                     | 6.41 ms                                                | 6.09 ms: 1.05x faster                                                           |
| xml_etree_generate         | 89.2 ms                                                | 84.8 ms: 1.05x faster                                                           |
| richards                   | 45.8 ms                                                | 43.6 ms: 1.05x faster                                                           |
| unpickle_pure_python       | 230 us                                                 | 219 us: 1.05x faster                                                            |
| generators                 | 31.2 ms                                                | 29.8 ms: 1.05x faster                                                           |
| deltablue                  | 3.72 ms                                                | 3.55 ms: 1.05x faster                                                           |
| spectral_norm              | 115 ms                                                 | 110 ms: 1.04x faster                                                            |
| xml_etree_process          | 61.7 ms                                                | 59.5 ms: 1.04x faster                                                           |
| richards_super             | 51.5 ms                                                | 49.8 ms: 1.04x faster                                                           |
| nqueens                    | 83.3 ms                                                | 81.0 ms: 1.03x faster                                                           |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.93 ms: 1.03x faster                                                           |
| fannkuch                   | 417 ms                                                 | 408 ms: 1.02x faster                                                            |
| pickle_pure_python         | 324 us                                                 | 319 us: 1.02x faster                                                            |
| regex_dna                  | 212 ms                                                 | 209 ms: 1.02x faster                                                            |
| pycparser                  | 1.18 sec                                               | 1.16 sec: 1.02x faster                                                          |
| python_startup_no_site     | 6.94 ms                                                | 6.92 ms: 1.00x faster                                                           |
| pidigits                   | 187 ms                                                 | 188 ms: 1.00x slower                                                            |
| scimark_lu                 | 118 ms                                                 | 119 ms: 1.01x slower                                                            |
| sqlite_synth               | 2.83 us                                                | 2.88 us: 1.02x slower                                                           |
| pprint_safe_repr           | 776 ms                                                 | 800 ms: 1.03x slower                                                            |
| nbody                      | 97.0 ms                                                | 100 ms: 1.03x slower                                                            |
| json                       | 5.26 ms                                                | 5.44 ms: 1.03x slower                                                           |
| pprint_pformat             | 1.57 sec                                               | 1.64 sec: 1.05x slower                                                          |
| json_loads                 | 28.5 us                                                | 29.8 us: 1.05x slower                                                           |
| bench_thread_pool          | 842 us                                                 | 887 us: 1.05x slower                                                            |
| typing_runtime_protocols   | 158 us                                                 | 168 us: 1.06x slower                                                            |
| json_dumps                 | 10.4 ms                                                | 11.2 ms: 1.08x slower                                                           |
| coroutines                 | 23.2 ms                                                | 25.7 ms: 1.11x slower                                                           |
| telco                      | 7.10 ms                                                | 7.97 ms: 1.12x slower                                                           |
| python_startup             | 9.55 ms                                                | 12.2 ms: 1.28x slower                                                           |
| gc_traversal               | 3.79 ms                                                | 5.08 ms: 1.34x slower                                                           |
| create_gc_cycles           | 1.48 ms                                                | 2.57 ms: 1.74x slower                                                           |
| dask                       | 372 ms                                                 | 912 ms: 2.45x slower                                                            |
| bench_mp_pool              | 24.0 ms                                                | 93.1 ms: 3.88x slower                                                           |
| logging_silent             | 104 ns                                                 | 477 ns: 4.56x slower                                                            |
| coverage                   | 72.7 ms                                                | 428 ms: 5.89x slower                                                            |
| Geometric mean             | (ref)                                                  | 1.03x faster                                                                    |

Benchmark hidden because not significant (3): scimark_fft, asyncio_websockets, regex_v8
Ignored benchmarks (19) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (24) of results/bm-20250529-3.15.0a0-08419ee/bm-20250529-linux-x86_64-faster%2dcpython-specialize_for_iter_-3.15.0a0-08419ee.json: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.073x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 1.13x
# Results vs. 3.12.0

- fork: mdboom
- ref: tuple_hash_cache2
- machine: linux-x86_64
- commit hash: 54e07d1
- commit date: 2025-03-20
- overall geometric mean: 1.116x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x faster
- Memory change: 1.11x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250320-linux-x86_64-mdboom-tuple_hash_cache2-3.14.0a6+-54e07d1 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 258 ms: 1.06x faster                                                |
| docutils       | 2.77 sec                                               | 2.61 sec: 1.06x faster                                              |
| Geometric mean | (ref)                                                  | 1.06x faster                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250320-linux-x86_64-mdboom-tuple_hash_cache2-3.14.0a6+-54e07d1 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 613 ms: 1.93x faster                                                |
| async_tree_io              | 1.16 sec                                               | 616 ms: 1.88x faster                                                |
| async_tree_none            | 472 ms                                                 | 261 ms: 1.81x faster                                                |
| async_tree_memoization     | 578 ms                                                 | 319 ms: 1.81x faster                                                |
| async_tree_memoization_tg  | 575 ms                                                 | 321 ms: 1.79x faster                                                |
| async_tree_none_tg         | 450 ms                                                 | 252 ms: 1.78x faster                                                |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 484 ms: 1.50x faster                                                |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 495 ms: 1.47x faster                                                |
| Geometric mean             | (ref)                                                  | 1.74x faster                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250320-linux-x86_64-mdboom-tuple_hash_cache2-3.14.0a6+-54e07d1 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 71.4 ms: 1.19x faster                                               |
| pidigits       | 187 ms                                                 | 186 ms: 1.01x faster                                                |
| nbody          | 97.0 ms                                                | 101 ms: 1.04x slower                                                |
| Geometric mean | (ref)                                                  | 1.05x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250320-linux-x86_64-mdboom-tuple_hash_cache2-3.14.0a6+-54e07d1 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 127 ms: 1.17x faster                                                |
| regex_effbot   | 3.61 ms                                                | 3.21 ms: 1.13x faster                                               |
| regex_dna      | 212 ms                                                 | 216 ms: 1.02x slower                                                |
| regex_v8       | 23.1 ms                                                | 24.0 ms: 1.04x slower                                               |
| Geometric mean | (ref)                                                  | 1.06x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250320-linux-x86_64-mdboom-tuple_hash_cache2-3.14.0a6+-54e07d1 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.99 sec: 1.17x faster                                              |
| xml_etree_parse      | 159 ms                                                 | 140 ms: 1.14x faster                                                |
| xml_etree_iterparse  | 107 ms                                                 | 98.7 ms: 1.08x faster                                               |
| xml_etree_generate   | 89.2 ms                                                | 84.7 ms: 1.05x faster                                               |
| xml_etree_process    | 61.7 ms                                                | 59.2 ms: 1.04x faster                                               |
| unpickle_pure_python | 230 us                                                 | 221 us: 1.04x faster                                                |
| pickle_pure_python   | 324 us                                                 | 318 us: 1.02x faster                                                |
| json_loads           | 28.5 us                                                | 29.7 us: 1.04x slower                                               |
| json_dumps           | 10.4 ms                                                | 11.5 ms: 1.11x slower                                               |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                        |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250320-linux-x86_64-mdboom-tuple_hash_cache2-3.14.0a6+-54e07d1 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 8.19 ms: 1.18x slower                                               |
| python_startup         | 9.55 ms                                                | 13.1 ms: 1.38x slower                                               |
| Geometric mean         | (ref)                                                  | 1.27x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250320-linux-x86_64-mdboom-tuple_hash_cache2-3.14.0a6+-54e07d1 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| django_template | 34.6 ms                                                | 31.6 ms: 1.10x faster                                               |
| mako            | 11.9 ms                                                | 11.5 ms: 1.04x faster                                               |
| Geometric mean  | (ref)                                                  | 1.07x faster                                                        |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250320-linux-x86_64-mdboom-tuple_hash_cache2-3.14.0a6+-54e07d1 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| mdp                        | 2.63 sec                                               | 1.25 sec: 2.11x faster                                              |
| async_tree_io_tg           | 1.18 sec                                               | 613 ms: 1.93x faster                                                |
| async_tree_io              | 1.16 sec                                               | 616 ms: 1.88x faster                                                |
| async_tree_none            | 472 ms                                                 | 261 ms: 1.81x faster                                                |
| async_tree_memoization     | 578 ms                                                 | 319 ms: 1.81x faster                                                |
| async_tree_memoization_tg  | 575 ms                                                 | 321 ms: 1.79x faster                                                |
| async_tree_none_tg         | 450 ms                                                 | 252 ms: 1.78x faster                                                |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 484 ms: 1.50x faster                                                |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 495 ms: 1.47x faster                                                |
| deepcopy                   | 371 us                                                 | 256 us: 1.45x faster                                                |
| deepcopy_memo              | 40.7 us                                                | 30.2 us: 1.35x faster                                               |
| comprehensions             | 21.8 us                                                | 17.0 us: 1.28x faster                                               |
| deepcopy_reduce            | 3.35 us                                                | 2.67 us: 1.25x faster                                               |
| go                         | 139 ms                                                 | 116 ms: 1.20x faster                                                |
| float                      | 84.7 ms                                                | 71.4 ms: 1.19x faster                                               |
| tomli_loads                | 2.33 sec                                               | 1.99 sec: 1.17x faster                                              |
| pathlib                    | 19.3 ms                                                | 16.5 ms: 1.17x faster                                               |
| regex_compile              | 148 ms                                                 | 127 ms: 1.17x faster                                                |
| deltablue                  | 3.72 ms                                                | 3.18 ms: 1.17x faster                                               |
| dulwich_log                | 68.5 ms                                                | 58.7 ms: 1.17x faster                                               |
| logging_format             | 7.23 us                                                | 6.24 us: 1.16x faster                                               |
| logging_simple             | 6.46 us                                                | 5.58 us: 1.16x faster                                               |
| raytrace                   | 312 ms                                                 | 271 ms: 1.15x faster                                                |
| async_generators           | 463 ms                                                 | 403 ms: 1.15x faster                                                |
| xml_etree_parse            | 159 ms                                                 | 140 ms: 1.14x faster                                                |
| sqlalchemy_declarative     | 147 ms                                                 | 130 ms: 1.13x faster                                                |
| sqlalchemy_imperative      | 18.7 ms                                                | 16.6 ms: 1.13x faster                                               |
| chaos                      | 67.0 ms                                                | 59.4 ms: 1.13x faster                                               |
| regex_effbot               | 3.61 ms                                                | 3.21 ms: 1.13x faster                                               |
| sympy_sum                  | 169 ms                                                 | 151 ms: 1.12x faster                                                |
| spectral_norm              | 115 ms                                                 | 103 ms: 1.11x faster                                                |
| sympy_str                  | 300 ms                                                 | 269 ms: 1.11x faster                                                |
| generators                 | 31.2 ms                                                | 28.1 ms: 1.11x faster                                               |
| django_template            | 34.6 ms                                                | 31.6 ms: 1.10x faster                                               |
| scimark_monte_carlo        | 75.1 ms                                                | 69.2 ms: 1.08x faster                                               |
| xml_etree_iterparse        | 107 ms                                                 | 98.7 ms: 1.08x faster                                               |
| scimark_sor                | 129 ms                                                 | 119 ms: 1.08x faster                                                |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.69 ms: 1.08x faster                                               |
| crypto_pyaes               | 81.9 ms                                                | 75.9 ms: 1.08x faster                                               |
| scimark_fft                | 382 ms                                                 | 355 ms: 1.08x faster                                                |
| sympy_integrate            | 21.4 ms                                                | 20.0 ms: 1.07x faster                                               |
| logging_silent             | 104 ns                                                 | 97.5 ns: 1.07x faster                                               |
| 2to3                       | 274 ms                                                 | 258 ms: 1.06x faster                                                |
| docutils                   | 2.77 sec                                               | 2.61 sec: 1.06x faster                                              |
| pyflate                    | 482 ms                                                 | 455 ms: 1.06x faster                                                |
| xml_etree_generate         | 89.2 ms                                                | 84.7 ms: 1.05x faster                                               |
| pprint_safe_repr           | 776 ms                                                 | 741 ms: 1.05x faster                                                |
| richards                   | 45.8 ms                                                | 43.9 ms: 1.04x faster                                               |
| xml_etree_process          | 61.7 ms                                                | 59.2 ms: 1.04x faster                                               |
| unpickle_pure_python       | 230 us                                                 | 221 us: 1.04x faster                                                |
| sympy_expand               | 478 ms                                                 | 460 ms: 1.04x faster                                                |
| pprint_pformat             | 1.57 sec                                               | 1.51 sec: 1.04x faster                                              |
| mako                       | 11.9 ms                                                | 11.5 ms: 1.04x faster                                               |
| meteor_contest             | 112 ms                                                 | 109 ms: 1.03x faster                                                |
| pycparser                  | 1.18 sec                                               | 1.14 sec: 1.03x faster                                              |
| richards_super             | 51.5 ms                                                | 50.2 ms: 1.03x faster                                               |
| sqlite_synth               | 2.83 us                                                | 2.77 us: 1.02x faster                                               |
| pickle_pure_python         | 324 us                                                 | 318 us: 1.02x faster                                                |
| hexiom                     | 6.41 ms                                                | 6.33 ms: 1.01x faster                                               |
| pidigits                   | 187 ms                                                 | 186 ms: 1.01x faster                                                |
| nqueens                    | 83.3 ms                                                | 83.6 ms: 1.00x slower                                               |
| regex_dna                  | 212 ms                                                 | 216 ms: 1.02x slower                                                |
| coroutines                 | 23.2 ms                                                | 23.6 ms: 1.02x slower                                               |
| typing_runtime_protocols   | 158 us                                                 | 163 us: 1.03x slower                                                |
| nbody                      | 97.0 ms                                                | 101 ms: 1.04x slower                                                |
| regex_v8                   | 23.1 ms                                                | 24.0 ms: 1.04x slower                                               |
| bench_thread_pool          | 842 us                                                 | 875 us: 1.04x slower                                                |
| json_loads                 | 28.5 us                                                | 29.7 us: 1.04x slower                                               |
| fannkuch                   | 417 ms                                                 | 436 ms: 1.04x slower                                                |
| telco                      | 7.10 ms                                                | 7.82 ms: 1.10x slower                                               |
| json_dumps                 | 10.4 ms                                                | 11.5 ms: 1.11x slower                                               |
| coverage                   | 72.7 ms                                                | 84.7 ms: 1.17x slower                                               |
| python_startup_no_site     | 6.94 ms                                                | 8.19 ms: 1.18x slower                                               |
| gc_traversal               | 3.79 ms                                                | 4.82 ms: 1.27x slower                                               |
| python_startup             | 9.55 ms                                                | 13.1 ms: 1.38x slower                                               |
| create_gc_cycles           | 1.48 ms                                                | 2.49 ms: 1.68x slower                                               |
| bench_mp_pool              | 24.0 ms                                                | 83.2 ms: 3.47x slower                                               |
| Geometric mean             | (ref)                                                  | 1.10x faster                                                        |

Benchmark hidden because not significant (3): json, scimark_lu, asyncio_websockets
Ignored benchmarks (18) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250320-3.14.0a6+-54e07d1/bm-20250320-linux-x86_64-mdboom-tuple_hash_cache2-3.14.0a6+-54e07d1.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.116x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.06x
- 99% likely to have a speedup of 1.05x

# Memory
- memory change: 1.11x
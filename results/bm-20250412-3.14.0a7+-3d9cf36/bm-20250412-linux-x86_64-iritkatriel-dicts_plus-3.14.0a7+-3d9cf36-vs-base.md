# Results vs. base

- fork: iritkatriel
- ref: dicts_plus
- machine: linux-x86_64
- commit hash: 3d9cf36
- commit date: 2025-04-12
- overall geometric mean: 1.009x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250410-linux-x86_64-python-07b8d3117fdbc4e5be55-3.14.0a7+-07b8d31 | bm-20250412-linux-x86_64-iritkatriel-dicts_plus-3.14.0a7+-3d9cf36 |
|----------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| 2to3           | 251 ms                                                                 | 250 ms: 1.01x faster                                              |
| docutils       | 2.61 sec                                                               | 2.58 sec: 1.01x faster                                            |
| html5lib       | 61.4 ms                                                                | 60.4 ms: 1.02x faster                                             |
| sphinx         | 1.02 sec                                                               | 1.01 sec: 1.01x faster                                            |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                      |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250410-linux-x86_64-python-07b8d3117fdbc4e5be55-3.14.0a7+-07b8d31 | bm-20250412-linux-x86_64-iritkatriel-dicts_plus-3.14.0a7+-3d9cf36 |
|----------------------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| async_tree_cpu_io_mixed    | 487 ms                                                                 | 476 ms: 1.02x faster                                              |
| coroutines                 | 24.3 ms                                                                | 23.8 ms: 1.02x faster                                             |
| async_tree_cpu_io_mixed_tg | 483 ms                                                                 | 473 ms: 1.02x faster                                              |
| async_tree_none_tg         | 250 ms                                                                 | 246 ms: 1.01x faster                                              |
| async_tree_none            | 257 ms                                                                 | 254 ms: 1.01x faster                                              |
| Geometric mean             | (ref)                                                                  | 1.01x faster                                                      |

Benchmark hidden because not significant (6): async_tree_io_tg, async_tree_io, async_tree_memoization_tg, async_tree_memoization, asyncio_websockets, async_generators

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250410-linux-x86_64-python-07b8d3117fdbc4e5be55-3.14.0a7+-07b8d31 | bm-20250412-linux-x86_64-iritkatriel-dicts_plus-3.14.0a7+-3d9cf36 |
|----------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| nbody          | 93.8 ms                                                                | 90.0 ms: 1.04x faster                                             |
| float          | 68.9 ms                                                                | 68.1 ms: 1.01x faster                                             |
| pidigits       | 186 ms                                                                 | 186 ms: 1.00x faster                                              |
| Geometric mean | (ref)                                                                  | 1.02x faster                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250410-linux-x86_64-python-07b8d3117fdbc4e5be55-3.14.0a7+-07b8d31 | bm-20250412-linux-x86_64-iritkatriel-dicts_plus-3.14.0a7+-3d9cf36 |
|----------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| regex_effbot   | 3.33 ms                                                                | 3.16 ms: 1.06x faster                                             |
| regex_v8       | 24.0 ms                                                                | 23.1 ms: 1.04x faster                                             |
| regex_dna      | 215 ms                                                                 | 208 ms: 1.03x faster                                              |
| regex_compile  | 125 ms                                                                 | 124 ms: 1.00x faster                                              |
| Geometric mean | (ref)                                                                  | 1.03x faster                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250410-linux-x86_64-python-07b8d3117fdbc4e5be55-3.14.0a7+-07b8d31 | bm-20250412-linux-x86_64-iritkatriel-dicts_plus-3.14.0a7+-3d9cf36 |
|----------------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| xml_etree_generate   | 84.7 ms                                                                | 83.2 ms: 1.02x faster                                             |
| unpickle_pure_python | 220 us                                                                 | 216 us: 1.02x faster                                              |
| tomli_loads          | 1.95 sec                                                               | 1.93 sec: 1.01x faster                                            |
| xml_etree_process    | 58.8 ms                                                                | 58.1 ms: 1.01x faster                                             |
| pickle_pure_python   | 316 us                                                                 | 314 us: 1.01x faster                                              |
| json_loads           | 29.2 us                                                                | 29.3 us: 1.00x slower                                             |
| Geometric mean       | (ref)                                                                  | 1.01x faster                                                      |

Benchmark hidden because not significant (3): xml_etree_iterparse, json_dumps, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250410-linux-x86_64-python-07b8d3117fdbc4e5be55-3.14.0a7+-07b8d31 | bm-20250412-linux-x86_64-iritkatriel-dicts_plus-3.14.0a7+-3d9cf36 |
|------------------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| python_startup         | 13.3 ms                                                                | 13.2 ms: 1.01x faster                                             |
| python_startup_no_site | 8.25 ms                                                                | 8.20 ms: 1.01x faster                                             |
| Geometric mean         | (ref)                                                                  | 1.01x faster                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250410-linux-x86_64-python-07b8d3117fdbc4e5be55-3.14.0a7+-07b8d31 | bm-20250412-linux-x86_64-iritkatriel-dicts_plus-3.14.0a7+-3d9cf36 |
|-----------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| genshi_text     | 21.2 ms                                                                | 20.8 ms: 1.02x faster                                             |
| mako            | 11.6 ms                                                                | 11.4 ms: 1.02x faster                                             |
| django_template | 31.6 ms                                                                | 31.1 ms: 1.01x faster                                             |
| genshi_xml      | 48.4 ms                                                                | 48.7 ms: 1.01x slower                                             |
| Geometric mean  | (ref)                                                                  | 1.01x faster                                                      |

All benchmarks:
===============

| Benchmark                  | bm-20250410-linux-x86_64-python-07b8d3117fdbc4e5be55-3.14.0a7+-07b8d31 | bm-20250412-linux-x86_64-iritkatriel-dicts_plus-3.14.0a7+-3d9cf36 |
|----------------------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| generators                 | 31.6 ms                                                                | 29.2 ms: 1.08x faster                                             |
| regex_effbot               | 3.33 ms                                                                | 3.16 ms: 1.06x faster                                             |
| nbody                      | 93.8 ms                                                                | 90.0 ms: 1.04x faster                                             |
| regex_v8                   | 24.0 ms                                                                | 23.1 ms: 1.04x faster                                             |
| logging_silent             | 98.5 ns                                                                | 95.0 ns: 1.04x faster                                             |
| regex_dna                  | 215 ms                                                                 | 208 ms: 1.03x faster                                              |
| bpe_tokeniser              | 4.55 sec                                                               | 4.43 sec: 1.03x faster                                            |
| dulwich_log                | 60.7 ms                                                                | 59.2 ms: 1.03x faster                                             |
| scimark_monte_carlo        | 66.9 ms                                                                | 65.2 ms: 1.03x faster                                             |
| spectral_norm              | 103 ms                                                                 | 100 ms: 1.02x faster                                              |
| typing_runtime_protocols   | 168 us                                                                 | 164 us: 1.02x faster                                              |
| scimark_lu                 | 118 ms                                                                 | 115 ms: 1.02x faster                                              |
| async_tree_cpu_io_mixed    | 487 ms                                                                 | 476 ms: 1.02x faster                                              |
| genshi_text                | 21.2 ms                                                                | 20.8 ms: 1.02x faster                                             |
| coroutines                 | 24.3 ms                                                                | 23.8 ms: 1.02x faster                                             |
| gc_traversal               | 4.82 ms                                                                | 4.72 ms: 1.02x faster                                             |
| deepcopy_reduce            | 2.64 us                                                                | 2.58 us: 1.02x faster                                             |
| async_tree_cpu_io_mixed_tg | 483 ms                                                                 | 473 ms: 1.02x faster                                              |
| chaos                      | 57.0 ms                                                                | 55.9 ms: 1.02x faster                                             |
| sympy_sum                  | 150 ms                                                                 | 148 ms: 1.02x faster                                              |
| mdp                        | 1.22 sec                                                               | 1.20 sec: 1.02x faster                                            |
| shortest_path              | 496 ms                                                                 | 487 ms: 1.02x faster                                              |
| xml_etree_generate         | 84.7 ms                                                                | 83.2 ms: 1.02x faster                                             |
| go                         | 112 ms                                                                 | 110 ms: 1.02x faster                                              |
| mako                       | 11.6 ms                                                                | 11.4 ms: 1.02x faster                                             |
| many_optionals             | 946 us                                                                 | 930 us: 1.02x faster                                              |
| unpickle_pure_python       | 220 us                                                                 | 216 us: 1.02x faster                                              |
| bench_mp_pool              | 83.3 ms                                                                | 81.9 ms: 1.02x faster                                             |
| html5lib                   | 61.4 ms                                                                | 60.4 ms: 1.02x faster                                             |
| scimark_fft                | 350 ms                                                                 | 345 ms: 1.01x faster                                              |
| richards_super             | 49.9 ms                                                                | 49.2 ms: 1.01x faster                                             |
| django_template            | 31.6 ms                                                                | 31.1 ms: 1.01x faster                                             |
| async_tree_none_tg         | 250 ms                                                                 | 246 ms: 1.01x faster                                              |
| tomli_loads                | 1.95 sec                                                               | 1.93 sec: 1.01x faster                                            |
| async_tree_none            | 257 ms                                                                 | 254 ms: 1.01x faster                                              |
| sphinx                     | 1.02 sec                                                               | 1.01 sec: 1.01x faster                                            |
| sqlalchemy_imperative      | 17.1 ms                                                                | 16.9 ms: 1.01x faster                                             |
| float                      | 68.9 ms                                                                | 68.1 ms: 1.01x faster                                             |
| xml_etree_process          | 58.8 ms                                                                | 58.1 ms: 1.01x faster                                             |
| scimark_sparse_mat_mult    | 4.78 ms                                                                | 4.73 ms: 1.01x faster                                             |
| sympy_str                  | 267 ms                                                                 | 264 ms: 1.01x faster                                              |
| sqlglot_v2_transpile       | 1.55 ms                                                                | 1.53 ms: 1.01x faster                                             |
| sympy_integrate            | 19.1 ms                                                                | 18.9 ms: 1.01x faster                                             |
| sqlglot_v2_parse           | 1.24 ms                                                                | 1.23 ms: 1.01x faster                                             |
| telco                      | 7.85 ms                                                                | 7.77 ms: 1.01x faster                                             |
| create_gc_cycles           | 2.47 ms                                                                | 2.45 ms: 1.01x faster                                             |
| docutils                   | 2.61 sec                                                               | 2.58 sec: 1.01x faster                                            |
| logging_format             | 6.18 us                                                                | 6.13 us: 1.01x faster                                             |
| richards                   | 43.2 ms                                                                | 42.8 ms: 1.01x faster                                             |
| fannkuch                   | 415 ms                                                                 | 412 ms: 1.01x faster                                              |
| pickle_pure_python         | 316 us                                                                 | 314 us: 1.01x faster                                              |
| subparsers                 | 20.9 ms                                                                | 20.7 ms: 1.01x faster                                             |
| 2to3                       | 251 ms                                                                 | 250 ms: 1.01x faster                                              |
| python_startup             | 13.3 ms                                                                | 13.2 ms: 1.01x faster                                             |
| raytrace                   | 261 ms                                                                 | 259 ms: 1.01x faster                                              |
| bench_thread_pool          | 893 us                                                                 | 887 us: 1.01x faster                                              |
| python_startup_no_site     | 8.25 ms                                                                | 8.20 ms: 1.01x faster                                             |
| nqueens                    | 80.6 ms                                                                | 80.2 ms: 1.00x faster                                             |
| sympy_expand               | 454 ms                                                                 | 452 ms: 1.00x faster                                              |
| pprint_pformat             | 1.46 sec                                                               | 1.45 sec: 1.00x faster                                            |
| regex_compile              | 125 ms                                                                 | 124 ms: 1.00x faster                                              |
| pidigits                   | 186 ms                                                                 | 186 ms: 1.00x faster                                              |
| sqlglot_v2_optimize        | 51.9 ms                                                                | 52.0 ms: 1.00x slower                                             |
| comprehensions             | 16.7 us                                                                | 16.7 us: 1.00x slower                                             |
| json_loads                 | 29.2 us                                                                | 29.3 us: 1.00x slower                                             |
| sqlglot_v2_normalize       | 105 ms                                                                 | 105 ms: 1.01x slower                                              |
| hexiom                     | 6.14 ms                                                                | 6.19 ms: 1.01x slower                                             |
| genshi_xml                 | 48.4 ms                                                                | 48.7 ms: 1.01x slower                                             |
| deepcopy_memo              | 28.4 us                                                                | 28.6 us: 1.01x slower                                             |
| meteor_contest             | 104 ms                                                                 | 105 ms: 1.01x slower                                              |
| pyflate                    | 451 ms                                                                 | 456 ms: 1.01x slower                                              |
| pathlib                    | 16.5 ms                                                                | 16.7 ms: 1.01x slower                                             |
| scimark_sor                | 116 ms                                                                 | 118 ms: 1.02x slower                                              |
| coverage                   | 85.5 ms                                                                | 87.6 ms: 1.02x slower                                             |
| Geometric mean             | (ref)                                                                  | 1.01x faster                                                      |

Benchmark hidden because not significant (21): async_tree_io_tg, pylint, async_tree_io, async_tree_memoization_tg, xml_etree_iterparse, async_tree_memoization, pycparser, deltablue, asyncio_websockets, sqlalchemy_declarative, json_dumps, logging_simple, xml_etree_parse, connected_components, pprint_safe_repr, crypto_pyaes, deepcopy, async_generators, sqlite_synth, json, k_core

- Geometric mean (including insignificant results): 1.009x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x
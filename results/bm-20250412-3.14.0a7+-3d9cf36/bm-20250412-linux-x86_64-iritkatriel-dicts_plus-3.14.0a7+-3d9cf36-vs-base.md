# Results vs. base

- fork: iritkatriel
- ref: dicts_plus
- machine: linux-x86_64
- commit hash: 3d9cf36
- commit date: 2025-04-12
- overall geometric mean: 1.005x faster
- HPT reliability: 99.99%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250410-linux-x86_64-python-07b8d3117fdbc4e5be55-3.14.0a7+-07b8d31 | bm-20250412-linux-x86_64-iritkatriel-dicts_plus-3.14.0a7+-3d9cf36 |
|----------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| 2to3           | 251 ms                                                                 | 250 ms: 1.01x faster                                              |
| docutils       | 2.61 sec                                                               | 2.59 sec: 1.01x faster                                            |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                      |

Benchmark hidden because not significant (2): html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250410-linux-x86_64-python-07b8d3117fdbc4e5be55-3.14.0a7+-07b8d31 | bm-20250412-linux-x86_64-iritkatriel-dicts_plus-3.14.0a7+-3d9cf36 |
|----------------------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| async_tree_cpu_io_mixed    | 487 ms                                                                 | 476 ms: 1.02x faster                                              |
| async_tree_cpu_io_mixed_tg | 483 ms                                                                 | 474 ms: 1.02x faster                                              |
| coroutines                 | 24.3 ms                                                                | 24.1 ms: 1.01x faster                                             |
| async_generators           | 389 ms                                                                 | 393 ms: 1.01x slower                                              |
| Geometric mean             | (ref)                                                                  | 1.01x faster                                                      |

Benchmark hidden because not significant (7): async_tree_none_tg, async_tree_io, async_tree_io_tg, async_tree_none, async_tree_memoization_tg, asyncio_websockets, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250410-linux-x86_64-python-07b8d3117fdbc4e5be55-3.14.0a7+-07b8d31 | bm-20250412-linux-x86_64-iritkatriel-dicts_plus-3.14.0a7+-3d9cf36 |
|----------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| float          | 68.9 ms                                                                | 67.1 ms: 1.03x faster                                             |
| pidigits       | 186 ms                                                                 | 186 ms: 1.00x faster                                              |
| nbody          | 93.8 ms                                                                | 95.2 ms: 1.01x slower                                             |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250410-linux-x86_64-python-07b8d3117fdbc4e5be55-3.14.0a7+-07b8d31 | bm-20250412-linux-x86_64-iritkatriel-dicts_plus-3.14.0a7+-3d9cf36 |
|----------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| regex_v8       | 24.0 ms                                                                | 23.3 ms: 1.03x faster                                             |
| regex_effbot   | 3.33 ms                                                                | 3.26 ms: 1.02x faster                                             |
| regex_dna      | 215 ms                                                                 | 215 ms: 1.00x slower                                              |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                      |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250410-linux-x86_64-python-07b8d3117fdbc4e5be55-3.14.0a7+-07b8d31 | bm-20250412-linux-x86_64-iritkatriel-dicts_plus-3.14.0a7+-3d9cf36 |
|----------------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| json_dumps           | 11.7 ms                                                                | 11.5 ms: 1.02x faster                                             |
| xml_etree_generate   | 84.7 ms                                                                | 83.4 ms: 1.02x faster                                             |
| xml_etree_process    | 58.8 ms                                                                | 58.2 ms: 1.01x faster                                             |
| unpickle_pure_python | 220 us                                                                 | 219 us: 1.00x faster                                              |
| xml_etree_iterparse  | 98.8 ms                                                                | 99.3 ms: 1.01x slower                                             |
| xml_etree_parse      | 140 ms                                                                 | 141 ms: 1.01x slower                                              |
| Geometric mean       | (ref)                                                                  | 1.00x faster                                                      |

Benchmark hidden because not significant (3): tomli_loads, pickle_pure_python, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250410-linux-x86_64-python-07b8d3117fdbc4e5be55-3.14.0a7+-07b8d31 | bm-20250412-linux-x86_64-iritkatriel-dicts_plus-3.14.0a7+-3d9cf36 |
|------------------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| python_startup         | 13.3 ms                                                                | 13.2 ms: 1.01x faster                                             |
| python_startup_no_site | 8.25 ms                                                                | 8.21 ms: 1.00x faster                                             |
| Geometric mean         | (ref)                                                                  | 1.01x faster                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250410-linux-x86_64-python-07b8d3117fdbc4e5be55-3.14.0a7+-07b8d31 | bm-20250412-linux-x86_64-iritkatriel-dicts_plus-3.14.0a7+-3d9cf36 |
|-----------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| mako            | 11.6 ms                                                                | 11.2 ms: 1.04x faster                                             |
| genshi_text     | 21.2 ms                                                                | 20.9 ms: 1.02x faster                                             |
| django_template | 31.6 ms                                                                | 31.3 ms: 1.01x faster                                             |
| genshi_xml      | 48.4 ms                                                                | 48.1 ms: 1.01x faster                                             |
| Geometric mean  | (ref)                                                                  | 1.02x faster                                                      |

All benchmarks:
===============

| Benchmark                  | bm-20250410-linux-x86_64-python-07b8d3117fdbc4e5be55-3.14.0a7+-07b8d31 | bm-20250412-linux-x86_64-iritkatriel-dicts_plus-3.14.0a7+-3d9cf36 |
|----------------------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| generators                 | 31.6 ms                                                                | 29.9 ms: 1.06x faster                                             |
| spectral_norm              | 103 ms                                                                 | 98.1 ms: 1.05x faster                                             |
| logging_silent             | 98.5 ns                                                                | 94.8 ns: 1.04x faster                                             |
| mako                       | 11.6 ms                                                                | 11.2 ms: 1.04x faster                                             |
| bpe_tokeniser              | 4.55 sec                                                               | 4.40 sec: 1.03x faster                                            |
| regex_v8                   | 24.0 ms                                                                | 23.3 ms: 1.03x faster                                             |
| typing_runtime_protocols   | 168 us                                                                 | 163 us: 1.03x faster                                              |
| logging_format             | 6.18 us                                                                | 6.01 us: 1.03x faster                                             |
| float                      | 68.9 ms                                                                | 67.1 ms: 1.03x faster                                             |
| async_tree_cpu_io_mixed    | 487 ms                                                                 | 476 ms: 1.02x faster                                              |
| regex_effbot               | 3.33 ms                                                                | 3.26 ms: 1.02x faster                                             |
| sympy_sum                  | 150 ms                                                                 | 147 ms: 1.02x faster                                              |
| genshi_text                | 21.2 ms                                                                | 20.9 ms: 1.02x faster                                             |
| dulwich_log                | 60.7 ms                                                                | 59.7 ms: 1.02x faster                                             |
| async_tree_cpu_io_mixed_tg | 483 ms                                                                 | 474 ms: 1.02x faster                                              |
| chaos                      | 57.0 ms                                                                | 56.0 ms: 1.02x faster                                             |
| bench_mp_pool              | 83.3 ms                                                                | 81.9 ms: 1.02x faster                                             |
| json_dumps                 | 11.7 ms                                                                | 11.5 ms: 1.02x faster                                             |
| logging_simple             | 5.53 us                                                                | 5.44 us: 1.02x faster                                             |
| go                         | 112 ms                                                                 | 110 ms: 1.02x faster                                              |
| xml_etree_generate         | 84.7 ms                                                                | 83.4 ms: 1.02x faster                                             |
| sqlalchemy_imperative      | 17.1 ms                                                                | 16.9 ms: 1.02x faster                                             |
| mdp                        | 1.22 sec                                                               | 1.20 sec: 1.02x faster                                            |
| many_optionals             | 946 us                                                                 | 932 us: 1.01x faster                                              |
| fannkuch                   | 415 ms                                                                 | 409 ms: 1.01x faster                                              |
| scimark_fft                | 350 ms                                                                 | 345 ms: 1.01x faster                                              |
| scimark_monte_carlo        | 66.9 ms                                                                | 65.9 ms: 1.01x faster                                             |
| pyflate                    | 451 ms                                                                 | 445 ms: 1.01x faster                                              |
| sqlglot_v2_parse           | 1.24 ms                                                                | 1.22 ms: 1.01x faster                                             |
| sqlglot_v2_transpile       | 1.55 ms                                                                | 1.53 ms: 1.01x faster                                             |
| comprehensions             | 16.7 us                                                                | 16.5 us: 1.01x faster                                             |
| sympy_str                  | 267 ms                                                                 | 264 ms: 1.01x faster                                              |
| bench_thread_pool          | 893 us                                                                 | 884 us: 1.01x faster                                              |
| xml_etree_process          | 58.8 ms                                                                | 58.2 ms: 1.01x faster                                             |
| sqlalchemy_declarative     | 132 ms                                                                 | 131 ms: 1.01x faster                                              |
| sympy_integrate            | 19.1 ms                                                                | 18.9 ms: 1.01x faster                                             |
| crypto_pyaes               | 72.8 ms                                                                | 72.3 ms: 1.01x faster                                             |
| python_startup             | 13.3 ms                                                                | 13.2 ms: 1.01x faster                                             |
| django_template            | 31.6 ms                                                                | 31.3 ms: 1.01x faster                                             |
| docutils                   | 2.61 sec                                                               | 2.59 sec: 1.01x faster                                            |
| coroutines                 | 24.3 ms                                                                | 24.1 ms: 1.01x faster                                             |
| 2to3                       | 251 ms                                                                 | 250 ms: 1.01x faster                                              |
| scimark_lu                 | 118 ms                                                                 | 117 ms: 1.01x faster                                              |
| genshi_xml                 | 48.4 ms                                                                | 48.1 ms: 1.01x faster                                             |
| python_startup_no_site     | 8.25 ms                                                                | 8.21 ms: 1.00x faster                                             |
| unpickle_pure_python       | 220 us                                                                 | 219 us: 1.00x faster                                              |
| raytrace                   | 261 ms                                                                 | 260 ms: 1.00x faster                                              |
| hexiom                     | 6.14 ms                                                                | 6.13 ms: 1.00x faster                                             |
| pidigits                   | 186 ms                                                                 | 186 ms: 1.00x faster                                              |
| regex_dna                  | 215 ms                                                                 | 215 ms: 1.00x slower                                              |
| sqlglot_v2_optimize        | 51.9 ms                                                                | 52.0 ms: 1.00x slower                                             |
| nqueens                    | 80.6 ms                                                                | 80.8 ms: 1.00x slower                                             |
| create_gc_cycles           | 2.47 ms                                                                | 2.48 ms: 1.00x slower                                             |
| xml_etree_iterparse        | 98.8 ms                                                                | 99.3 ms: 1.01x slower                                             |
| deepcopy                   | 247 us                                                                 | 249 us: 1.01x slower                                              |
| xml_etree_parse            | 140 ms                                                                 | 141 ms: 1.01x slower                                              |
| deepcopy_memo              | 28.4 us                                                                | 28.6 us: 1.01x slower                                             |
| async_generators           | 389 ms                                                                 | 393 ms: 1.01x slower                                              |
| scimark_sparse_mat_mult    | 4.78 ms                                                                | 4.83 ms: 1.01x slower                                             |
| scimark_sor                | 116 ms                                                                 | 117 ms: 1.01x slower                                              |
| shortest_path              | 496 ms                                                                 | 502 ms: 1.01x slower                                              |
| sqlite_synth               | 2.75 us                                                                | 2.78 us: 1.01x slower                                             |
| sqlglot_v2_normalize       | 105 ms                                                                 | 106 ms: 1.01x slower                                              |
| nbody                      | 93.8 ms                                                                | 95.2 ms: 1.01x slower                                             |
| coverage                   | 85.5 ms                                                                | 87.0 ms: 1.02x slower                                             |
| pathlib                    | 16.5 ms                                                                | 16.8 ms: 1.02x slower                                             |
| meteor_contest             | 104 ms                                                                 | 107 ms: 1.02x slower                                              |
| gc_traversal               | 4.82 ms                                                                | 4.97 ms: 1.03x slower                                             |
| pycparser                  | 1.12 sec                                                               | 1.16 sec: 1.04x slower                                            |
| Geometric mean             | (ref)                                                                  | 1.01x faster                                                      |

Benchmark hidden because not significant (26): pylint, async_tree_none_tg, async_tree_io, sphinx, async_tree_io_tg, connected_components, async_tree_none, tomli_loads, pprint_safe_repr, deepcopy_reduce, pickle_pure_python, async_tree_memoization_tg, richards_super, sympy_expand, asyncio_websockets, subparsers, regex_compile, json_loads, deltablue, richards, async_tree_memoization, pprint_pformat, k_core, json, telco, html5lib

- Geometric mean (including insignificant results): 1.005x faster

# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x
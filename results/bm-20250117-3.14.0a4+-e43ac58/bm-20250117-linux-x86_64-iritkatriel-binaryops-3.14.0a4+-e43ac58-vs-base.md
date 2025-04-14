# Results vs. base

- fork: iritkatriel
- ref: binaryops
- machine: linux-x86_64
- commit hash: e43ac58
- commit date: 2025-01-17
- overall geometric mean: 1.002x faster
- HPT reliability: 60.59%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250116-linux-x86_64-python-27494dd9ad6032c29e27-3.14.0a4+-27494dd | bm-20250117-linux-x86_64-iritkatriel-binaryops-3.14.0a4+-e43ac58 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------:|
| 2to3           | 253 ms                                                                 | 254 ms: 1.00x slower                                             |
| docutils       | 2.58 sec                                                               | 2.59 sec: 1.00x slower                                           |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                     |

Benchmark hidden because not significant (2): html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250116-linux-x86_64-python-27494dd9ad6032c29e27-3.14.0a4+-27494dd | bm-20250117-linux-x86_64-iritkatriel-binaryops-3.14.0a4+-e43ac58 |
|----------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------:|
| async_tree_cpu_io_mixed    | 494 ms                                                                 | 482 ms: 1.02x faster                                             |
| async_tree_cpu_io_mixed_tg | 469 ms                                                                 | 458 ms: 1.02x faster                                             |
| async_tree_io_tg           | 587 ms                                                                 | 582 ms: 1.01x faster                                             |
| async_generators           | 389 ms                                                                 | 388 ms: 1.00x faster                                             |
| coroutines                 | 23.3 ms                                                                | 23.6 ms: 1.01x slower                                            |
| Geometric mean             | (ref)                                                                  | 1.01x faster                                                     |

Benchmark hidden because not significant (6): async_tree_none, async_tree_io, async_tree_none_tg, async_tree_memoization_tg, async_tree_memoization, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250116-linux-x86_64-python-27494dd9ad6032c29e27-3.14.0a4+-27494dd | bm-20250117-linux-x86_64-iritkatriel-binaryops-3.14.0a4+-e43ac58 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------:|
| pidigits       | 186 ms                                                                 | 186 ms: 1.00x slower                                             |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                     |

Benchmark hidden because not significant (2): nbody, float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250116-linux-x86_64-python-27494dd9ad6032c29e27-3.14.0a4+-27494dd | bm-20250117-linux-x86_64-iritkatriel-binaryops-3.14.0a4+-e43ac58 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------:|
| regex_dna      | 216 ms                                                                 | 205 ms: 1.06x faster                                             |
| regex_compile  | 125 ms                                                                 | 126 ms: 1.00x slower                                             |
| regex_effbot   | 3.25 ms                                                                | 3.29 ms: 1.01x slower                                            |
| regex_v8       | 25.2 ms                                                                | 25.8 ms: 1.02x slower                                            |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250116-linux-x86_64-python-27494dd9ad6032c29e27-3.14.0a4+-27494dd | bm-20250117-linux-x86_64-iritkatriel-binaryops-3.14.0a4+-e43ac58 |
|----------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------:|
| unpickle_pure_python | 221 us                                                                 | 216 us: 1.03x faster                                             |
| pickle_pure_python   | 323 us                                                                 | 321 us: 1.01x faster                                             |
| xml_etree_process    | 59.6 ms                                                                | 60.0 ms: 1.01x slower                                            |
| tomli_loads          | 1.96 sec                                                               | 1.97 sec: 1.01x slower                                           |
| Geometric mean       | (ref)                                                                  | 1.00x faster                                                     |

Benchmark hidden because not significant (5): xml_etree_iterparse, xml_etree_parse, xml_etree_generate, json_dumps, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250116-linux-x86_64-python-27494dd9ad6032c29e27-3.14.0a4+-27494dd | bm-20250117-linux-x86_64-iritkatriel-binaryops-3.14.0a4+-e43ac58 |
|------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------:|
| python_startup_no_site | 7.05 ms                                                                | 7.04 ms: 1.00x faster                                            |
| python_startup         | 12.8 ms                                                                | 12.8 ms: 1.00x faster                                            |
| Geometric mean         | (ref)                                                                  | 1.00x faster                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250116-linux-x86_64-python-27494dd9ad6032c29e27-3.14.0a4+-27494dd | bm-20250117-linux-x86_64-iritkatriel-binaryops-3.14.0a4+-e43ac58 |
|-----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------:|
| genshi_xml      | 47.6 ms                                                                | 48.0 ms: 1.01x slower                                            |
| genshi_text     | 21.1 ms                                                                | 21.3 ms: 1.01x slower                                            |
| django_template | 31.8 ms                                                                | 32.3 ms: 1.02x slower                                            |
| mako            | 11.2 ms                                                                | 11.5 ms: 1.03x slower                                            |
| Geometric mean  | (ref)                                                                  | 1.02x slower                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20250116-linux-x86_64-python-27494dd9ad6032c29e27-3.14.0a4+-27494dd | bm-20250117-linux-x86_64-iritkatriel-binaryops-3.14.0a4+-e43ac58 |
|----------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------:|
| pyflate                    | 475 ms                                                                 | 449 ms: 1.06x faster                                             |
| regex_dna                  | 216 ms                                                                 | 205 ms: 1.06x faster                                             |
| gc_traversal               | 4.78 ms                                                                | 4.59 ms: 1.04x faster                                            |
| telco                      | 8.04 ms                                                                | 7.77 ms: 1.03x faster                                            |
| unpickle_pure_python       | 221 us                                                                 | 216 us: 1.03x faster                                             |
| scimark_sor                | 124 ms                                                                 | 121 ms: 1.03x faster                                             |
| async_tree_cpu_io_mixed    | 494 ms                                                                 | 482 ms: 1.02x faster                                             |
| async_tree_cpu_io_mixed_tg | 469 ms                                                                 | 458 ms: 1.02x faster                                             |
| scimark_monte_carlo        | 68.6 ms                                                                | 67.3 ms: 1.02x faster                                            |
| richards_super             | 50.7 ms                                                                | 49.8 ms: 1.02x faster                                            |
| pprint_safe_repr           | 725 ms                                                                 | 712 ms: 1.02x faster                                             |
| pathlib                    | 16.1 ms                                                                | 15.9 ms: 1.02x faster                                            |
| fannkuch                   | 407 ms                                                                 | 401 ms: 1.02x faster                                             |
| pprint_pformat             | 1.49 sec                                                               | 1.47 sec: 1.01x faster                                           |
| scimark_lu                 | 119 ms                                                                 | 117 ms: 1.01x faster                                             |
| richards                   | 44.3 ms                                                                | 43.8 ms: 1.01x faster                                            |
| sqlite_synth               | 2.81 us                                                                | 2.78 us: 1.01x faster                                            |
| coverage                   | 90.4 ms                                                                | 89.6 ms: 1.01x faster                                            |
| comprehensions             | 17.0 us                                                                | 16.8 us: 1.01x faster                                            |
| async_tree_io_tg           | 587 ms                                                                 | 582 ms: 1.01x faster                                             |
| go                         | 118 ms                                                                 | 117 ms: 1.01x faster                                             |
| sqlglot_transpile          | 1.57 ms                                                                | 1.56 ms: 1.01x faster                                            |
| pickle_pure_python         | 323 us                                                                 | 321 us: 1.01x faster                                             |
| sqlglot_parse              | 1.26 ms                                                                | 1.26 ms: 1.01x faster                                            |
| meteor_contest             | 107 ms                                                                 | 107 ms: 1.01x faster                                             |
| nqueens                    | 81.0 ms                                                                | 80.5 ms: 1.01x faster                                            |
| scimark_fft                | 349 ms                                                                 | 347 ms: 1.01x faster                                             |
| generators                 | 27.5 ms                                                                | 27.3 ms: 1.00x faster                                            |
| create_gc_cycles           | 2.46 ms                                                                | 2.45 ms: 1.00x faster                                            |
| deltablue                  | 3.18 ms                                                                | 3.17 ms: 1.00x faster                                            |
| async_generators           | 389 ms                                                                 | 388 ms: 1.00x faster                                             |
| python_startup_no_site     | 7.05 ms                                                                | 7.04 ms: 1.00x faster                                            |
| python_startup             | 12.8 ms                                                                | 12.8 ms: 1.00x faster                                            |
| pidigits                   | 186 ms                                                                 | 186 ms: 1.00x slower                                             |
| bench_thread_pool          | 863 us                                                                 | 865 us: 1.00x slower                                             |
| regex_compile              | 125 ms                                                                 | 126 ms: 1.00x slower                                             |
| 2to3                       | 253 ms                                                                 | 254 ms: 1.00x slower                                             |
| bpe_tokeniser              | 4.51 sec                                                               | 4.53 sec: 1.00x slower                                           |
| crypto_pyaes               | 71.3 ms                                                                | 71.6 ms: 1.00x slower                                            |
| sympy_str                  | 265 ms                                                                 | 266 ms: 1.00x slower                                             |
| docutils                   | 2.58 sec                                                               | 2.59 sec: 1.00x slower                                           |
| sympy_integrate            | 19.7 ms                                                                | 19.8 ms: 1.00x slower                                            |
| sqlalchemy_imperative      | 16.3 ms                                                                | 16.4 ms: 1.00x slower                                            |
| raytrace                   | 270 ms                                                                 | 271 ms: 1.00x slower                                             |
| sqlalchemy_declarative     | 129 ms                                                                 | 129 ms: 1.01x slower                                             |
| xml_etree_process          | 59.6 ms                                                                | 60.0 ms: 1.01x slower                                            |
| tomli_loads                | 1.96 sec                                                               | 1.97 sec: 1.01x slower                                           |
| deepcopy_memo              | 30.7 us                                                                | 30.9 us: 1.01x slower                                            |
| genshi_xml                 | 47.6 ms                                                                | 48.0 ms: 1.01x slower                                            |
| thrift                     | 756 us                                                                 | 762 us: 1.01x slower                                             |
| genshi_text                | 21.1 ms                                                                | 21.3 ms: 1.01x slower                                            |
| many_optionals             | 933 us                                                                 | 942 us: 1.01x slower                                             |
| regex_effbot               | 3.25 ms                                                                | 3.29 ms: 1.01x slower                                            |
| coroutines                 | 23.3 ms                                                                | 23.6 ms: 1.01x slower                                            |
| deepcopy                   | 255 us                                                                 | 259 us: 1.01x slower                                             |
| scimark_sparse_mat_mult    | 4.69 ms                                                                | 4.76 ms: 1.02x slower                                            |
| django_template            | 31.8 ms                                                                | 32.3 ms: 1.02x slower                                            |
| spectral_norm              | 96.2 ms                                                                | 97.8 ms: 1.02x slower                                            |
| logging_silent             | 105 ns                                                                 | 107 ns: 1.02x slower                                             |
| deepcopy_reduce            | 2.60 us                                                                | 2.65 us: 1.02x slower                                            |
| regex_v8                   | 25.2 ms                                                                | 25.8 ms: 1.02x slower                                            |
| pycparser                  | 1.13 sec                                                               | 1.16 sec: 1.02x slower                                           |
| mdp                        | 2.46 sec                                                               | 2.52 sec: 1.02x slower                                           |
| logging_simple             | 5.36 us                                                                | 5.53 us: 1.03x slower                                            |
| mako                       | 11.2 ms                                                                | 11.5 ms: 1.03x slower                                            |
| logging_format             | 5.93 us                                                                | 6.16 us: 1.04x slower                                            |
| Geometric mean             | (ref)                                                                  | 1.00x faster                                                     |

Benchmark hidden because not significant (30): async_tree_none, async_tree_io, async_tree_none_tg, async_tree_memoization_tg, typing_runtime_protocols, json, nbody, html5lib, xml_etree_iterparse, sqlglot_optimize, async_tree_memoization, bench_mp_pool, asyncio_websockets, xml_etree_parse, sympy_sum, shortest_path, chaos, hexiom, sqlglot_normalize, dulwich_log, xml_etree_generate, json_dumps, sphinx, sympy_expand, subparsers, float, json_loads, k_core, connected_components, pylint

- Geometric mean (including insignificant results): 1.002x faster

# HPT report

- Reliability score: 60.59% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x
# Results vs. base

- fork: iritkatriel
- ref: binaryops
- machine: linux-x86_64
- commit hash: 6476205
- commit date: 2025-01-21
- overall geometric mean: 1.002x faster
- HPT reliability: 85.26%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250116-linux-x86_64-python-27494dd9ad6032c29e27-3.14.0a4+-27494dd | bm-20250121-linux-x86_64-iritkatriel-binaryops-3.14.0a4+-6476205 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------:|
| 2to3           | 253 ms                                                                 | 254 ms: 1.00x slower                                             |
| docutils       | 2.58 sec                                                               | 2.59 sec: 1.00x slower                                           |
| html5lib       | 61.1 ms                                                                | 59.7 ms: 1.02x faster                                            |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                     |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250116-linux-x86_64-python-27494dd9ad6032c29e27-3.14.0a4+-27494dd | bm-20250121-linux-x86_64-iritkatriel-binaryops-3.14.0a4+-6476205 |
|----------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------:|
| async_tree_cpu_io_mixed    | 494 ms                                                                 | 481 ms: 1.03x faster                                             |
| async_tree_cpu_io_mixed_tg | 469 ms                                                                 | 457 ms: 1.03x faster                                             |
| async_tree_none            | 261 ms                                                                 | 257 ms: 1.02x faster                                             |
| async_tree_io_tg           | 587 ms                                                                 | 581 ms: 1.01x faster                                             |
| coroutines                 | 23.3 ms                                                                | 23.8 ms: 1.02x slower                                            |
| Geometric mean             | (ref)                                                                  | 1.01x faster                                                     |

Benchmark hidden because not significant (6): async_tree_io, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, async_generators, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250116-linux-x86_64-python-27494dd9ad6032c29e27-3.14.0a4+-27494dd | bm-20250121-linux-x86_64-iritkatriel-binaryops-3.14.0a4+-6476205 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------:|
| nbody          | 95.8 ms                                                                | 94.1 ms: 1.02x faster                                            |
| pidigits       | 186 ms                                                                 | 186 ms: 1.00x slower                                             |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                     |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250116-linux-x86_64-python-27494dd9ad6032c29e27-3.14.0a4+-27494dd | bm-20250121-linux-x86_64-iritkatriel-binaryops-3.14.0a4+-6476205 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------:|
| regex_dna      | 216 ms                                                                 | 210 ms: 1.03x faster                                             |
| regex_effbot   | 3.25 ms                                                                | 3.15 ms: 1.03x faster                                            |
| regex_v8       | 25.2 ms                                                                | 25.1 ms: 1.01x faster                                            |
| regex_compile  | 125 ms                                                                 | 127 ms: 1.01x slower                                             |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250116-linux-x86_64-python-27494dd9ad6032c29e27-3.14.0a4+-27494dd | bm-20250121-linux-x86_64-iritkatriel-binaryops-3.14.0a4+-6476205 |
|----------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------:|
| unpickle_pure_python | 221 us                                                                 | 216 us: 1.02x faster                                             |
| pickle_pure_python   | 323 us                                                                 | 320 us: 1.01x faster                                             |
| xml_etree_parse      | 139 ms                                                                 | 138 ms: 1.01x faster                                             |
| xml_etree_iterparse  | 97.7 ms                                                                | 96.9 ms: 1.01x faster                                            |
| json_loads           | 29.4 us                                                                | 29.6 us: 1.01x slower                                            |
| tomli_loads          | 1.96 sec                                                               | 1.98 sec: 1.01x slower                                           |
| Geometric mean       | (ref)                                                                  | 1.00x faster                                                     |

Benchmark hidden because not significant (3): xml_etree_process, xml_etree_generate, json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250116-linux-x86_64-python-27494dd9ad6032c29e27-3.14.0a4+-27494dd | bm-20250121-linux-x86_64-iritkatriel-binaryops-3.14.0a4+-6476205 |
|------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------:|
| python_startup_no_site | 7.05 ms                                                                | 7.06 ms: 1.00x slower                                            |
| python_startup         | 12.8 ms                                                                | 12.9 ms: 1.00x slower                                            |
| Geometric mean         | (ref)                                                                  | 1.00x slower                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250116-linux-x86_64-python-27494dd9ad6032c29e27-3.14.0a4+-27494dd | bm-20250121-linux-x86_64-iritkatriel-binaryops-3.14.0a4+-6476205 |
|-----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------:|
| django_template | 31.8 ms                                                                | 32.1 ms: 1.01x slower                                            |
| genshi_xml      | 47.6 ms                                                                | 48.1 ms: 1.01x slower                                            |
| mako            | 11.2 ms                                                                | 11.3 ms: 1.01x slower                                            |
| genshi_text     | 21.1 ms                                                                | 21.4 ms: 1.02x slower                                            |
| Geometric mean  | (ref)                                                                  | 1.01x slower                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20250116-linux-x86_64-python-27494dd9ad6032c29e27-3.14.0a4+-27494dd | bm-20250121-linux-x86_64-iritkatriel-binaryops-3.14.0a4+-6476205 |
|----------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------:|
| gc_traversal               | 4.78 ms                                                                | 4.58 ms: 1.04x faster                                            |
| scimark_lu                 | 119 ms                                                                 | 115 ms: 1.03x faster                                             |
| regex_dna                  | 216 ms                                                                 | 210 ms: 1.03x faster                                             |
| regex_effbot               | 3.25 ms                                                                | 3.15 ms: 1.03x faster                                            |
| async_tree_cpu_io_mixed    | 494 ms                                                                 | 481 ms: 1.03x faster                                             |
| async_tree_cpu_io_mixed_tg | 469 ms                                                                 | 457 ms: 1.03x faster                                             |
| unpickle_pure_python       | 221 us                                                                 | 216 us: 1.02x faster                                             |
| html5lib                   | 61.1 ms                                                                | 59.7 ms: 1.02x faster                                            |
| scimark_monte_carlo        | 68.6 ms                                                                | 67.3 ms: 1.02x faster                                            |
| nbody                      | 95.8 ms                                                                | 94.1 ms: 1.02x faster                                            |
| async_tree_none            | 261 ms                                                                 | 257 ms: 1.02x faster                                             |
| scimark_sor                | 124 ms                                                                 | 122 ms: 1.02x faster                                             |
| sqlite_synth               | 2.81 us                                                                | 2.77 us: 1.01x faster                                            |
| typing_runtime_protocols   | 163 us                                                                 | 161 us: 1.01x faster                                             |
| nqueens                    | 81.0 ms                                                                | 80.2 ms: 1.01x faster                                            |
| scimark_fft                | 349 ms                                                                 | 346 ms: 1.01x faster                                             |
| pyflate                    | 475 ms                                                                 | 470 ms: 1.01x faster                                             |
| pickle_pure_python         | 323 us                                                                 | 320 us: 1.01x faster                                             |
| async_tree_io_tg           | 587 ms                                                                 | 581 ms: 1.01x faster                                             |
| sqlglot_parse              | 1.26 ms                                                                | 1.25 ms: 1.01x faster                                            |
| xml_etree_parse            | 139 ms                                                                 | 138 ms: 1.01x faster                                             |
| xml_etree_iterparse        | 97.7 ms                                                                | 96.9 ms: 1.01x faster                                            |
| generators                 | 27.5 ms                                                                | 27.3 ms: 1.01x faster                                            |
| sqlglot_transpile          | 1.57 ms                                                                | 1.56 ms: 1.01x faster                                            |
| subparsers                 | 20.5 ms                                                                | 20.4 ms: 1.01x faster                                            |
| comprehensions             | 17.0 us                                                                | 16.9 us: 1.01x faster                                            |
| regex_v8                   | 25.2 ms                                                                | 25.1 ms: 1.01x faster                                            |
| create_gc_cycles           | 2.46 ms                                                                | 2.44 ms: 1.01x faster                                            |
| richards                   | 44.3 ms                                                                | 44.1 ms: 1.00x faster                                            |
| meteor_contest             | 107 ms                                                                 | 107 ms: 1.00x faster                                             |
| pprint_safe_repr           | 725 ms                                                                 | 722 ms: 1.00x faster                                             |
| dulwich_log                | 64.2 ms                                                                | 64.0 ms: 1.00x faster                                            |
| go                         | 118 ms                                                                 | 117 ms: 1.00x faster                                             |
| pidigits                   | 186 ms                                                                 | 186 ms: 1.00x slower                                             |
| python_startup_no_site     | 7.05 ms                                                                | 7.06 ms: 1.00x slower                                            |
| python_startup             | 12.8 ms                                                                | 12.9 ms: 1.00x slower                                            |
| hexiom                     | 6.23 ms                                                                | 6.25 ms: 1.00x slower                                            |
| bench_thread_pool          | 863 us                                                                 | 866 us: 1.00x slower                                             |
| sqlalchemy_declarative     | 129 ms                                                                 | 129 ms: 1.00x slower                                             |
| docutils                   | 2.58 sec                                                               | 2.59 sec: 1.00x slower                                           |
| 2to3                       | 253 ms                                                                 | 254 ms: 1.00x slower                                             |
| deltablue                  | 3.18 ms                                                                | 3.20 ms: 1.00x slower                                            |
| many_optionals             | 933 us                                                                 | 938 us: 1.01x slower                                             |
| thrift                     | 756 us                                                                 | 761 us: 1.01x slower                                             |
| json_loads                 | 29.4 us                                                                | 29.6 us: 1.01x slower                                            |
| sympy_integrate            | 19.7 ms                                                                | 19.8 ms: 1.01x slower                                            |
| sympy_str                  | 265 ms                                                                 | 267 ms: 1.01x slower                                             |
| sqlalchemy_imperative      | 16.3 ms                                                                | 16.4 ms: 1.01x slower                                            |
| tomli_loads                | 1.96 sec                                                               | 1.98 sec: 1.01x slower                                           |
| spectral_norm              | 96.2 ms                                                                | 97.0 ms: 1.01x slower                                            |
| django_template            | 31.8 ms                                                                | 32.1 ms: 1.01x slower                                            |
| genshi_xml                 | 47.6 ms                                                                | 48.1 ms: 1.01x slower                                            |
| deepcopy                   | 255 us                                                                 | 258 us: 1.01x slower                                             |
| regex_compile              | 125 ms                                                                 | 127 ms: 1.01x slower                                             |
| mako                       | 11.2 ms                                                                | 11.3 ms: 1.01x slower                                            |
| mdp                        | 2.46 sec                                                               | 2.49 sec: 1.01x slower                                           |
| fannkuch                   | 407 ms                                                                 | 413 ms: 1.01x slower                                             |
| genshi_text                | 21.1 ms                                                                | 21.4 ms: 1.02x slower                                            |
| logging_silent             | 105 ns                                                                 | 107 ns: 1.02x slower                                             |
| deepcopy_memo              | 30.7 us                                                                | 31.2 us: 1.02x slower                                            |
| logging_format             | 5.93 us                                                                | 6.04 us: 1.02x slower                                            |
| coroutines                 | 23.3 ms                                                                | 23.8 ms: 1.02x slower                                            |
| logging_simple             | 5.36 us                                                                | 5.49 us: 1.02x slower                                            |
| Geometric mean             | (ref)                                                                  | 1.00x faster                                                     |

Benchmark hidden because not significant (33): async_tree_io, pycparser, telco, async_tree_memoization_tg, pathlib, async_tree_none_tg, xml_etree_process, xml_etree_generate, asyncio_websockets, richards_super, sqlglot_optimize, raytrace, sympy_sum, chaos, json, async_generators, bench_mp_pool, pprint_pformat, sqlglot_normalize, crypto_pyaes, bpe_tokeniser, scimark_sparse_mat_mult, sympy_expand, coverage, async_tree_memoization, pylint, sphinx, deepcopy_reduce, shortest_path, json_dumps, connected_components, float, k_core

- Geometric mean (including insignificant results): 1.002x faster

# HPT report

- Reliability score: 85.26% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x
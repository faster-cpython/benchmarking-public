# Results vs. base

- fork: mdboom
- ref: aa_test_2025_2
- machine: linux-x86_64
- commit hash: 8ffb2c1
- commit date: 2025-01-23
- overall geometric mean: 1.002x slower
- HPT reliability: 78.54%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250121-linux-x86_64-python-f18b2264929c56360c86-3.14.0a4+-f18b226 | bm-20250123-linux-x86_64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------:|
| 2to3           | 256 ms                                                                 | 257 ms: 1.00x slower                                             |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                     |

Benchmark hidden because not significant (3): docutils, html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250121-linux-x86_64-python-f18b2264929c56360c86-3.14.0a4+-f18b226 | bm-20250123-linux-x86_64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|----------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------:|
| async_tree_none            | 258 ms                                                                 | 254 ms: 1.02x faster                                             |
| async_tree_io_tg           | 591 ms                                                                 | 585 ms: 1.01x faster                                             |
| async_tree_memoization_tg  | 308 ms                                                                 | 306 ms: 1.01x faster                                             |
| async_tree_cpu_io_mixed_tg | 470 ms                                                                 | 473 ms: 1.01x slower                                             |
| async_generators           | 385 ms                                                                 | 391 ms: 1.02x slower                                             |
| coroutines                 | 23.3 ms                                                                | 23.8 ms: 1.02x slower                                            |
| Geometric mean             | (ref)                                                                  | 1.00x faster                                                     |

Benchmark hidden because not significant (5): async_tree_memoization, async_tree_io, async_tree_none_tg, async_tree_cpu_io_mixed, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250121-linux-x86_64-python-f18b2264929c56360c86-3.14.0a4+-f18b226 | bm-20250123-linux-x86_64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------:|
| pidigits       | 186 ms                                                                 | 186 ms: 1.00x faster                                             |
| nbody          | 93.6 ms                                                                | 96.2 ms: 1.03x slower                                            |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                     |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250121-linux-x86_64-python-f18b2264929c56360c86-3.14.0a4+-f18b226 | bm-20250123-linux-x86_64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------:|
| regex_v8       | 25.6 ms                                                                | 25.2 ms: 1.02x faster                                            |
| regex_effbot   | 3.29 ms                                                                | 3.24 ms: 1.02x faster                                            |
| regex_compile  | 128 ms                                                                 | 128 ms: 1.00x faster                                             |
| regex_dna      | 203 ms                                                                 | 216 ms: 1.06x slower                                             |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250121-linux-x86_64-python-f18b2264929c56360c86-3.14.0a4+-f18b226 | bm-20250123-linux-x86_64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|----------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------:|
| unpickle_pure_python | 227 us                                                                 | 226 us: 1.01x faster                                             |
| pickle_pure_python   | 326 us                                                                 | 325 us: 1.00x faster                                             |
| xml_etree_generate   | 84.2 ms                                                                | 84.5 ms: 1.00x slower                                            |
| xml_etree_process    | 61.0 ms                                                                | 61.4 ms: 1.01x slower                                            |
| Geometric mean       | (ref)                                                                  | 1.00x slower                                                     |

Benchmark hidden because not significant (5): xml_etree_iterparse, tomli_loads, xml_etree_parse, json_dumps, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250121-linux-x86_64-python-f18b2264929c56360c86-3.14.0a4+-f18b226 | bm-20250123-linux-x86_64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------:|
| python_startup         | 12.9 ms                                                                | 12.9 ms: 1.01x slower                                            |
| python_startup_no_site | 7.06 ms                                                                | 7.11 ms: 1.01x slower                                            |
| Geometric mean         | (ref)                                                                  | 1.01x slower                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250121-linux-x86_64-python-f18b2264929c56360c86-3.14.0a4+-f18b226 | bm-20250123-linux-x86_64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|-----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------:|
| django_template | 32.0 ms                                                                | 32.2 ms: 1.01x slower                                            |
| mako            | 11.1 ms                                                                | 11.1 ms: 1.01x slower                                            |
| genshi_text     | 21.8 ms                                                                | 21.9 ms: 1.01x slower                                            |
| Geometric mean  | (ref)                                                                  | 1.00x slower                                                     |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20250121-linux-x86_64-python-f18b2264929c56360c86-3.14.0a4+-f18b226 | bm-20250123-linux-x86_64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|----------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------:|
| pycparser                  | 1.17 sec                                                               | 1.14 sec: 1.03x faster                                           |
| logging_simple             | 5.88 us                                                                | 5.77 us: 1.02x faster                                            |
| thrift                     | 783 us                                                                 | 769 us: 1.02x faster                                             |
| regex_v8                   | 25.6 ms                                                                | 25.2 ms: 1.02x faster                                            |
| generators                 | 28.1 ms                                                                | 27.7 ms: 1.02x faster                                            |
| async_tree_none            | 258 ms                                                                 | 254 ms: 1.02x faster                                             |
| regex_effbot               | 3.29 ms                                                                | 3.24 ms: 1.02x faster                                            |
| logging_silent             | 104 ns                                                                 | 103 ns: 1.02x faster                                             |
| async_tree_io_tg           | 591 ms                                                                 | 585 ms: 1.01x faster                                             |
| scimark_lu                 | 117 ms                                                                 | 116 ms: 1.01x faster                                             |
| sympy_expand               | 458 ms                                                                 | 454 ms: 1.01x faster                                             |
| deepcopy                   | 260 us                                                                 | 257 us: 1.01x faster                                             |
| async_tree_memoization_tg  | 308 ms                                                                 | 306 ms: 1.01x faster                                             |
| sqlglot_transpile          | 1.57 ms                                                                | 1.55 ms: 1.01x faster                                            |
| sympy_sum                  | 148 ms                                                                 | 147 ms: 1.01x faster                                             |
| hexiom                     | 6.33 ms                                                                | 6.28 ms: 1.01x faster                                            |
| sqlalchemy_imperative      | 16.8 ms                                                                | 16.7 ms: 1.01x faster                                            |
| subparsers                 | 20.8 ms                                                                | 20.6 ms: 1.01x faster                                            |
| deepcopy_reduce            | 2.65 us                                                                | 2.63 us: 1.01x faster                                            |
| unpickle_pure_python       | 227 us                                                                 | 226 us: 1.01x faster                                             |
| sqlalchemy_declarative     | 132 ms                                                                 | 131 ms: 1.00x faster                                             |
| sqlglot_parse              | 1.26 ms                                                                | 1.25 ms: 1.00x faster                                            |
| pickle_pure_python         | 326 us                                                                 | 325 us: 1.00x faster                                             |
| many_optionals             | 955 us                                                                 | 952 us: 1.00x faster                                             |
| pidigits                   | 186 ms                                                                 | 186 ms: 1.00x faster                                             |
| sympy_integrate            | 19.8 ms                                                                | 19.8 ms: 1.00x faster                                            |
| regex_compile              | 128 ms                                                                 | 128 ms: 1.00x faster                                             |
| create_gc_cycles           | 2.47 ms                                                                | 2.47 ms: 1.00x slower                                            |
| go                         | 116 ms                                                                 | 116 ms: 1.00x slower                                             |
| 2to3                       | 256 ms                                                                 | 257 ms: 1.00x slower                                             |
| xml_etree_generate         | 84.2 ms                                                                | 84.5 ms: 1.00x slower                                            |
| deltablue                  | 3.15 ms                                                                | 3.16 ms: 1.00x slower                                            |
| dulwich_log                | 64.8 ms                                                                | 65.1 ms: 1.01x slower                                            |
| async_tree_cpu_io_mixed_tg | 470 ms                                                                 | 473 ms: 1.01x slower                                             |
| django_template            | 32.0 ms                                                                | 32.2 ms: 1.01x slower                                            |
| pprint_pformat             | 1.47 sec                                                               | 1.48 sec: 1.01x slower                                           |
| mako                       | 11.1 ms                                                                | 11.1 ms: 1.01x slower                                            |
| chaos                      | 57.7 ms                                                                | 58.0 ms: 1.01x slower                                            |
| genshi_text                | 21.8 ms                                                                | 21.9 ms: 1.01x slower                                            |
| python_startup             | 12.9 ms                                                                | 12.9 ms: 1.01x slower                                            |
| xml_etree_process          | 61.0 ms                                                                | 61.4 ms: 1.01x slower                                            |
| crypto_pyaes               | 72.9 ms                                                                | 73.4 ms: 1.01x slower                                            |
| bpe_tokeniser              | 4.48 sec                                                               | 4.51 sec: 1.01x slower                                           |
| python_startup_no_site     | 7.06 ms                                                                | 7.11 ms: 1.01x slower                                            |
| richards_super             | 49.7 ms                                                                | 50.1 ms: 1.01x slower                                            |
| meteor_contest             | 105 ms                                                                 | 106 ms: 1.01x slower                                             |
| richards                   | 43.5 ms                                                                | 43.8 ms: 1.01x slower                                            |
| pathlib                    | 16.4 ms                                                                | 16.6 ms: 1.01x slower                                            |
| fannkuch                   | 400 ms                                                                 | 404 ms: 1.01x slower                                             |
| scimark_sor                | 120 ms                                                                 | 122 ms: 1.01x slower                                             |
| logging_format             | 6.36 us                                                                | 6.44 us: 1.01x slower                                            |
| scimark_sparse_mat_mult    | 4.78 ms                                                                | 4.85 ms: 1.01x slower                                            |
| gc_traversal               | 4.96 ms                                                                | 5.03 ms: 1.01x slower                                            |
| mdp                        | 2.47 sec                                                               | 2.51 sec: 1.01x slower                                           |
| scimark_fft                | 344 ms                                                                 | 349 ms: 1.02x slower                                             |
| async_generators           | 385 ms                                                                 | 391 ms: 1.02x slower                                             |
| coroutines                 | 23.3 ms                                                                | 23.8 ms: 1.02x slower                                            |
| nbody                      | 93.6 ms                                                                | 96.2 ms: 1.03x slower                                            |
| spectral_norm              | 98.8 ms                                                                | 104 ms: 1.05x slower                                             |
| regex_dna                  | 203 ms                                                                 | 216 ms: 1.06x slower                                             |
| Geometric mean             | (ref)                                                                  | 1.00x slower                                                     |

Benchmark hidden because not significant (36): async_tree_memoization, async_tree_io, async_tree_none_tg, xml_etree_iterparse, sphinx, sympy_str, sqlite_synth, telco, deepcopy_memo, bench_mp_pool, pylint, docutils, async_tree_cpu_io_mixed, comprehensions, tomli_loads, genshi_xml, raytrace, sqlglot_optimize, nqueens, pprint_safe_repr, scimark_monte_carlo, connected_components, asyncio_websockets, bench_thread_pool, xml_etree_parse, sqlglot_normalize, html5lib, shortest_path, coverage, json_dumps, typing_runtime_protocols, pyflate, json_loads, json, k_core, float

- Geometric mean (including insignificant results): 1.002x slower

# HPT report

- Reliability score: 78.54% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x
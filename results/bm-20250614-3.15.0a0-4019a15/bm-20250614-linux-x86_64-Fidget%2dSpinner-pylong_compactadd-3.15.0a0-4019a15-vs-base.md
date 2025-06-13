# Results vs. base

- fork: Fidget-Spinner
- ref: pylong_compactadd
- machine: linux-x86_64
- commit hash: 4019a15
- commit date: 2025-06-14
- overall geometric mean: 1.008x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250613-linux-x86_64-python-afc5ab6cce9d7095b99c-3.15.0a0-afc5ab6 | bm-20250614-linux-x86_64-Fidget%2dSpinner-pylong_compactadd-3.15.0a0-4019a15 |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 255 ms                                                                | 254 ms: 1.00x faster                                                         |
| docutils       | 2.58 sec                                                              | 2.57 sec: 1.01x faster                                                       |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                                 |

Benchmark hidden because not significant (2): html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250613-linux-x86_64-python-afc5ab6cce9d7095b99c-3.15.0a0-afc5ab6 | bm-20250614-linux-x86_64-Fidget%2dSpinner-pylong_compactadd-3.15.0a0-4019a15 |
|----------------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| coroutines                 | 26.1 ms                                                               | 24.5 ms: 1.07x faster                                                        |
| async_tree_cpu_io_mixed    | 502 ms                                                                | 487 ms: 1.03x faster                                                         |
| async_tree_cpu_io_mixed_tg | 492 ms                                                                | 478 ms: 1.03x faster                                                         |
| async_generators           | 410 ms                                                                | 418 ms: 1.02x slower                                                         |
| Geometric mean             | (ref)                                                                 | 1.01x faster                                                                 |

Benchmark hidden because not significant (7): async_tree_io, asyncio_websockets, async_tree_io_tg, async_tree_none_tg, async_tree_memoization, async_tree_none, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250613-linux-x86_64-python-afc5ab6cce9d7095b99c-3.15.0a0-afc5ab6 | bm-20250614-linux-x86_64-Fidget%2dSpinner-pylong_compactadd-3.15.0a0-4019a15 |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| nbody          | 102 ms                                                                | 97.5 ms: 1.05x faster                                                        |
| pidigits       | 192 ms                                                                | 189 ms: 1.02x faster                                                         |
| float          | 73.6 ms                                                               | 72.4 ms: 1.02x faster                                                        |
| Geometric mean | (ref)                                                                 | 1.03x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250613-linux-x86_64-python-afc5ab6cce9d7095b99c-3.15.0a0-afc5ab6 | bm-20250614-linux-x86_64-Fidget%2dSpinner-pylong_compactadd-3.15.0a0-4019a15 |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_dna      | 194 ms                                                                | 183 ms: 1.06x faster                                                         |
| regex_v8       | 23.3 ms                                                               | 22.1 ms: 1.05x faster                                                        |
| regex_effbot   | 3.22 ms                                                               | 3.06 ms: 1.05x faster                                                        |
| regex_compile  | 128 ms                                                                | 127 ms: 1.01x faster                                                         |
| Geometric mean | (ref)                                                                 | 1.04x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250613-linux-x86_64-python-afc5ab6cce9d7095b99c-3.15.0a0-afc5ab6 | bm-20250614-linux-x86_64-Fidget%2dSpinner-pylong_compactadd-3.15.0a0-4019a15 |
|----------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| unpickle_pure_python | 222 us                                                                | 217 us: 1.02x faster                                                         |
| json_dumps           | 11.2 ms                                                               | 11.0 ms: 1.02x faster                                                        |
| pickle_pure_python   | 324 us                                                                | 320 us: 1.01x faster                                                         |
| tomli_loads          | 2.03 sec                                                              | 2.01 sec: 1.01x faster                                                       |
| xml_etree_iterparse  | 99.1 ms                                                               | 98.5 ms: 1.01x faster                                                        |
| json_loads           | 27.8 us                                                               | 28.2 us: 1.01x slower                                                        |
| Geometric mean       | (ref)                                                                 | 1.01x faster                                                                 |

Benchmark hidden because not significant (3): xml_etree_process, xml_etree_parse, xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250613-linux-x86_64-python-afc5ab6cce9d7095b99c-3.15.0a0-afc5ab6 | bm-20250614-linux-x86_64-Fidget%2dSpinner-pylong_compactadd-3.15.0a0-4019a15 |
|------------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 6.92 ms                                                               | 6.90 ms: 1.00x faster                                                        |
| python_startup         | 12.2 ms                                                               | 12.1 ms: 1.00x faster                                                        |
| Geometric mean         | (ref)                                                                 | 1.00x faster                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250613-linux-x86_64-python-afc5ab6cce9d7095b99c-3.15.0a0-afc5ab6 | bm-20250614-linux-x86_64-Fidget%2dSpinner-pylong_compactadd-3.15.0a0-4019a15 |
|-----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| genshi_text     | 21.6 ms                                                               | 21.1 ms: 1.02x faster                                                        |
| genshi_xml      | 49.9 ms                                                               | 49.2 ms: 1.01x faster                                                        |
| django_template | 32.3 ms                                                               | 32.6 ms: 1.01x slower                                                        |
| mako            | 11.4 ms                                                               | 11.8 ms: 1.03x slower                                                        |
| Geometric mean  | (ref)                                                                 | 1.00x slower                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20250613-linux-x86_64-python-afc5ab6cce9d7095b99c-3.15.0a0-afc5ab6 | bm-20250614-linux-x86_64-Fidget%2dSpinner-pylong_compactadd-3.15.0a0-4019a15 |
|----------------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| coroutines                 | 26.1 ms                                                               | 24.5 ms: 1.07x faster                                                        |
| spectral_norm              | 110 ms                                                                | 104 ms: 1.06x faster                                                         |
| regex_dna                  | 194 ms                                                                | 183 ms: 1.06x faster                                                         |
| regex_v8                   | 23.3 ms                                                               | 22.1 ms: 1.05x faster                                                        |
| scimark_fft                | 386 ms                                                                | 367 ms: 1.05x faster                                                         |
| regex_effbot               | 3.22 ms                                                               | 3.06 ms: 1.05x faster                                                        |
| nbody                      | 102 ms                                                                | 97.5 ms: 1.05x faster                                                        |
| scimark_sor                | 120 ms                                                                | 116 ms: 1.04x faster                                                         |
| scimark_monte_carlo        | 69.6 ms                                                               | 67.2 ms: 1.03x faster                                                        |
| scimark_sparse_mat_mult    | 5.18 ms                                                               | 5.02 ms: 1.03x faster                                                        |
| async_tree_cpu_io_mixed    | 502 ms                                                                | 487 ms: 1.03x faster                                                         |
| async_tree_cpu_io_mixed_tg | 492 ms                                                                | 478 ms: 1.03x faster                                                         |
| shortest_path              | 517 ms                                                                | 503 ms: 1.03x faster                                                         |
| deepcopy_reduce            | 2.76 us                                                               | 2.69 us: 1.03x faster                                                        |
| unpickle_pure_python       | 222 us                                                                | 217 us: 1.02x faster                                                         |
| genshi_text                | 21.6 ms                                                               | 21.1 ms: 1.02x faster                                                        |
| hexiom                     | 6.15 ms                                                               | 6.03 ms: 1.02x faster                                                        |
| json_dumps                 | 11.2 ms                                                               | 11.0 ms: 1.02x faster                                                        |
| pidigits                   | 192 ms                                                                | 189 ms: 1.02x faster                                                         |
| float                      | 73.6 ms                                                               | 72.4 ms: 1.02x faster                                                        |
| fannkuch                   | 418 ms                                                                | 412 ms: 1.01x faster                                                         |
| pycparser                  | 1.14 sec                                                              | 1.12 sec: 1.01x faster                                                       |
| genshi_xml                 | 49.9 ms                                                               | 49.2 ms: 1.01x faster                                                        |
| pickle_pure_python         | 324 us                                                                | 320 us: 1.01x faster                                                         |
| sqlglot_v2_transpile       | 1.57 ms                                                               | 1.54 ms: 1.01x faster                                                        |
| go                         | 112 ms                                                                | 111 ms: 1.01x faster                                                         |
| telco                      | 8.08 ms                                                               | 7.99 ms: 1.01x faster                                                        |
| pyflate                    | 432 ms                                                                | 427 ms: 1.01x faster                                                         |
| richards_super             | 49.8 ms                                                               | 49.3 ms: 1.01x faster                                                        |
| sqlglot_v2_parse           | 1.25 ms                                                               | 1.24 ms: 1.01x faster                                                        |
| comprehensions             | 16.1 us                                                               | 15.9 us: 1.01x faster                                                        |
| regex_compile              | 128 ms                                                                | 127 ms: 1.01x faster                                                         |
| crypto_pyaes               | 76.3 ms                                                               | 75.6 ms: 1.01x faster                                                        |
| deltablue                  | 3.54 ms                                                               | 3.50 ms: 1.01x faster                                                        |
| tomli_loads                | 2.03 sec                                                              | 2.01 sec: 1.01x faster                                                       |
| bpe_tokeniser              | 4.54 sec                                                              | 4.50 sec: 1.01x faster                                                       |
| gc_traversal               | 4.95 ms                                                               | 4.90 ms: 1.01x faster                                                        |
| deepcopy_memo              | 29.4 us                                                               | 29.2 us: 1.01x faster                                                        |
| chaos                      | 61.5 ms                                                               | 61.1 ms: 1.01x faster                                                        |
| sqlglot_v2_normalize       | 107 ms                                                                | 106 ms: 1.01x faster                                                         |
| create_gc_cycles           | 2.60 ms                                                               | 2.58 ms: 1.01x faster                                                        |
| xml_etree_iterparse        | 99.1 ms                                                               | 98.5 ms: 1.01x faster                                                        |
| deepcopy                   | 256 us                                                                | 254 us: 1.01x faster                                                         |
| logging_silent             | 476 ns                                                                | 473 ns: 1.01x faster                                                         |
| docutils                   | 2.58 sec                                                              | 2.57 sec: 1.01x faster                                                       |
| dulwich_log                | 59.5 ms                                                               | 59.2 ms: 1.00x faster                                                        |
| mdp                        | 1.22 sec                                                              | 1.22 sec: 1.00x faster                                                       |
| python_startup_no_site     | 6.92 ms                                                               | 6.90 ms: 1.00x faster                                                        |
| 2to3                       | 255 ms                                                                | 254 ms: 1.00x faster                                                         |
| python_startup             | 12.2 ms                                                               | 12.1 ms: 1.00x faster                                                        |
| nqueens                    | 81.5 ms                                                               | 81.3 ms: 1.00x faster                                                        |
| sympy_integrate            | 18.9 ms                                                               | 19.0 ms: 1.00x slower                                                        |
| sympy_expand               | 450 ms                                                                | 452 ms: 1.00x slower                                                         |
| sympy_str                  | 265 ms                                                                | 267 ms: 1.01x slower                                                         |
| django_template            | 32.3 ms                                                               | 32.6 ms: 1.01x slower                                                        |
| typing_runtime_protocols   | 167 us                                                                | 168 us: 1.01x slower                                                         |
| logging_simple             | 6.07 us                                                               | 6.13 us: 1.01x slower                                                        |
| pprint_pformat             | 1.65 sec                                                              | 1.66 sec: 1.01x slower                                                       |
| pprint_safe_repr           | 805 ms                                                                | 813 ms: 1.01x slower                                                         |
| sympy_sum                  | 147 ms                                                                | 149 ms: 1.01x slower                                                         |
| meteor_contest             | 105 ms                                                                | 107 ms: 1.01x slower                                                         |
| json_loads                 | 27.8 us                                                               | 28.2 us: 1.01x slower                                                        |
| async_generators           | 410 ms                                                                | 418 ms: 1.02x slower                                                         |
| json                       | 5.13 ms                                                               | 5.27 ms: 1.03x slower                                                        |
| generators                 | 29.5 ms                                                               | 30.3 ms: 1.03x slower                                                        |
| mako                       | 11.4 ms                                                               | 11.8 ms: 1.03x slower                                                        |
| logging_format             | 6.72 us                                                               | 6.94 us: 1.03x slower                                                        |
| Geometric mean             | (ref)                                                                 | 1.01x faster                                                                 |

Benchmark hidden because not significant (25): sphinx, xml_etree_process, many_optionals, richards, async_tree_io, scimark_lu, asyncio_websockets, subparsers, pylint, xml_etree_parse, raytrace, html5lib, connected_components, thrift, coverage, sqlite_synth, async_tree_io_tg, sqlglot_v2_optimize, pathlib, k_core, xml_etree_generate, async_tree_none_tg, async_tree_memoization, async_tree_none, async_tree_memoization_tg

- Geometric mean (including insignificant results): 1.008x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x
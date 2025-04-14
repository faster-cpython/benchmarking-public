# Results vs. base

- fork: faster-cpython
- ref: close_escapes_2
- machine: linux-x86_64
- commit hash: fa5c6fd
- commit date: 2025-01-28
- overall geometric mean: 1.000x faster
- HPT reliability: 79.66%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250127-linux-x86_64-python-75b49621578a45415bfe-3.14.0a4+-75b4962 | bm-20250128-linux-x86_64-faster%2dcpython-close_escapes_2-3.14.0a4+-fa5c6fd |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 253 ms                                                                 | 254 ms: 1.00x slower                                                        |
| docutils       | 2.58 sec                                                               | 2.59 sec: 1.00x slower                                                      |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                                |

Benchmark hidden because not significant (2): html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250127-linux-x86_64-python-75b49621578a45415bfe-3.14.0a4+-75b4962 | bm-20250128-linux-x86_64-faster%2dcpython-close_escapes_2-3.14.0a4+-fa5c6fd |
|----------------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| coroutines                 | 24.6 ms                                                                | 23.2 ms: 1.06x faster                                                       |
| async_generators           | 387 ms                                                                 | 381 ms: 1.01x faster                                                        |
| async_tree_cpu_io_mixed    | 486 ms                                                                 | 495 ms: 1.02x slower                                                        |
| async_tree_cpu_io_mixed_tg | 475 ms                                                                 | 484 ms: 1.02x slower                                                        |
| Geometric mean             | (ref)                                                                  | 1.00x faster                                                                |

Benchmark hidden because not significant (7): async_tree_none, async_tree_memoization, async_tree_io, async_tree_none_tg, async_tree_io_tg, asyncio_websockets, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250127-linux-x86_64-python-75b49621578a45415bfe-3.14.0a4+-75b4962 | bm-20250128-linux-x86_64-faster%2dcpython-close_escapes_2-3.14.0a4+-fa5c6fd |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 94.2 ms                                                                | 92.8 ms: 1.01x faster                                                       |
| pidigits       | 187 ms                                                                 | 186 ms: 1.00x faster                                                        |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                                |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250127-linux-x86_64-python-75b49621578a45415bfe-3.14.0a4+-75b4962 | bm-20250128-linux-x86_64-faster%2dcpython-close_escapes_2-3.14.0a4+-fa5c6fd |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_effbot   | 3.35 ms                                                                | 3.34 ms: 1.00x faster                                                       |
| regex_v8       | 25.4 ms                                                                | 25.5 ms: 1.00x slower                                                       |
| regex_compile  | 126 ms                                                                 | 126 ms: 1.00x slower                                                        |
| regex_dna      | 208 ms                                                                 | 211 ms: 1.01x slower                                                        |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250127-linux-x86_64-python-75b49621578a45415bfe-3.14.0a4+-75b4962 | bm-20250128-linux-x86_64-faster%2dcpython-close_escapes_2-3.14.0a4+-fa5c6fd |
|----------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 1.96 sec                                                               | 1.94 sec: 1.01x faster                                                      |
| json_loads           | 28.8 us                                                                | 29.0 us: 1.01x slower                                                       |
| xml_etree_iterparse  | 97.3 ms                                                                | 97.9 ms: 1.01x slower                                                       |
| json_dumps           | 11.6 ms                                                                | 11.7 ms: 1.01x slower                                                       |
| unpickle_pure_python | 216 us                                                                 | 218 us: 1.01x slower                                                        |
| xml_etree_generate   | 84.6 ms                                                                | 85.3 ms: 1.01x slower                                                       |
| xml_etree_process    | 59.2 ms                                                                | 60.1 ms: 1.01x slower                                                       |
| pickle_pure_python   | 316 us                                                                 | 321 us: 1.02x slower                                                        |
| Geometric mean       | (ref)                                                                  | 1.01x slower                                                                |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250127-linux-x86_64-python-75b49621578a45415bfe-3.14.0a4+-75b4962 | bm-20250128-linux-x86_64-faster%2dcpython-close_escapes_2-3.14.0a4+-fa5c6fd |
|------------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 12.9 ms                                                                | 12.8 ms: 1.00x faster                                                       |
| python_startup_no_site | 7.05 ms                                                                | 7.04 ms: 1.00x faster                                                       |
| Geometric mean         | (ref)                                                                  | 1.00x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250127-linux-x86_64-python-75b49621578a45415bfe-3.14.0a4+-75b4962 | bm-20250128-linux-x86_64-faster%2dcpython-close_escapes_2-3.14.0a4+-fa5c6fd |
|-----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| django_template | 32.1 ms                                                                | 31.7 ms: 1.01x faster                                                       |
| genshi_text     | 21.5 ms                                                                | 21.3 ms: 1.01x faster                                                       |
| genshi_xml      | 48.6 ms                                                                | 49.0 ms: 1.01x slower                                                       |
| Geometric mean  | (ref)                                                                  | 1.00x faster                                                                |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                  | bm-20250127-linux-x86_64-python-75b49621578a45415bfe-3.14.0a4+-75b4962 | bm-20250128-linux-x86_64-faster%2dcpython-close_escapes_2-3.14.0a4+-fa5c6fd |
|----------------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| coroutines                 | 24.6 ms                                                                | 23.2 ms: 1.06x faster                                                       |
| pathlib                    | 16.3 ms                                                                | 15.7 ms: 1.04x faster                                                       |
| spectral_norm              | 99.7 ms                                                                | 96.5 ms: 1.03x faster                                                       |
| fannkuch                   | 407 ms                                                                 | 398 ms: 1.02x faster                                                        |
| subparsers                 | 20.7 ms                                                                | 20.3 ms: 1.02x faster                                                       |
| thrift                     | 774 us                                                                 | 759 us: 1.02x faster                                                        |
| scimark_sor                | 122 ms                                                                 | 120 ms: 1.02x faster                                                        |
| nbody                      | 94.2 ms                                                                | 92.8 ms: 1.01x faster                                                       |
| scimark_monte_carlo        | 67.5 ms                                                                | 66.6 ms: 1.01x faster                                                       |
| async_generators           | 387 ms                                                                 | 381 ms: 1.01x faster                                                        |
| deepcopy                   | 257 us                                                                 | 254 us: 1.01x faster                                                        |
| pyflate                    | 473 ms                                                                 | 466 ms: 1.01x faster                                                        |
| django_template            | 32.1 ms                                                                | 31.7 ms: 1.01x faster                                                       |
| hexiom                     | 6.18 ms                                                                | 6.12 ms: 1.01x faster                                                       |
| genshi_text                | 21.5 ms                                                                | 21.3 ms: 1.01x faster                                                       |
| tomli_loads                | 1.96 sec                                                               | 1.94 sec: 1.01x faster                                                      |
| richards                   | 43.8 ms                                                                | 43.5 ms: 1.01x faster                                                       |
| generators                 | 27.8 ms                                                                | 27.6 ms: 1.01x faster                                                       |
| scimark_sparse_mat_mult    | 4.65 ms                                                                | 4.62 ms: 1.01x faster                                                       |
| logging_silent             | 104 ns                                                                 | 103 ns: 1.00x faster                                                        |
| comprehensions             | 16.7 us                                                                | 16.6 us: 1.00x faster                                                       |
| pidigits                   | 187 ms                                                                 | 186 ms: 1.00x faster                                                        |
| many_optionals             | 942 us                                                                 | 939 us: 1.00x faster                                                        |
| python_startup             | 12.9 ms                                                                | 12.8 ms: 1.00x faster                                                       |
| regex_effbot               | 3.35 ms                                                                | 3.34 ms: 1.00x faster                                                       |
| meteor_contest             | 107 ms                                                                 | 107 ms: 1.00x faster                                                        |
| python_startup_no_site     | 7.05 ms                                                                | 7.04 ms: 1.00x faster                                                       |
| 2to3                       | 253 ms                                                                 | 254 ms: 1.00x slower                                                        |
| crypto_pyaes               | 71.5 ms                                                                | 71.7 ms: 1.00x slower                                                       |
| sqlalchemy_imperative      | 16.3 ms                                                                | 16.4 ms: 1.00x slower                                                       |
| bench_thread_pool          | 859 us                                                                 | 861 us: 1.00x slower                                                        |
| regex_v8                   | 25.4 ms                                                                | 25.5 ms: 1.00x slower                                                       |
| docutils                   | 2.58 sec                                                               | 2.59 sec: 1.00x slower                                                      |
| regex_compile              | 126 ms                                                                 | 126 ms: 1.00x slower                                                        |
| sqlglot_optimize           | 52.3 ms                                                                | 52.6 ms: 1.00x slower                                                       |
| create_gc_cycles           | 2.45 ms                                                                | 2.46 ms: 1.00x slower                                                       |
| sympy_integrate            | 19.6 ms                                                                | 19.7 ms: 1.01x slower                                                       |
| json_loads                 | 28.8 us                                                                | 29.0 us: 1.01x slower                                                       |
| xml_etree_iterparse        | 97.3 ms                                                                | 97.9 ms: 1.01x slower                                                       |
| json_dumps                 | 11.6 ms                                                                | 11.7 ms: 1.01x slower                                                       |
| unpickle_pure_python       | 216 us                                                                 | 218 us: 1.01x slower                                                        |
| pprint_pformat             | 1.47 sec                                                               | 1.48 sec: 1.01x slower                                                      |
| genshi_xml                 | 48.6 ms                                                                | 49.0 ms: 1.01x slower                                                       |
| xml_etree_generate         | 84.6 ms                                                                | 85.3 ms: 1.01x slower                                                       |
| raytrace                   | 269 ms                                                                 | 271 ms: 1.01x slower                                                        |
| deepcopy_memo              | 30.2 us                                                                | 30.4 us: 1.01x slower                                                       |
| typing_runtime_protocols   | 159 us                                                                 | 160 us: 1.01x slower                                                        |
| sympy_str                  | 264 ms                                                                 | 267 ms: 1.01x slower                                                        |
| logging_simple             | 5.43 us                                                                | 5.50 us: 1.01x slower                                                       |
| coverage                   | 90.3 ms                                                                | 91.5 ms: 1.01x slower                                                       |
| sympy_expand               | 450 ms                                                                 | 456 ms: 1.01x slower                                                        |
| regex_dna                  | 208 ms                                                                 | 211 ms: 1.01x slower                                                        |
| deepcopy_reduce            | 2.67 us                                                                | 2.71 us: 1.01x slower                                                       |
| xml_etree_process          | 59.2 ms                                                                | 60.1 ms: 1.01x slower                                                       |
| pickle_pure_python         | 316 us                                                                 | 321 us: 1.02x slower                                                        |
| async_tree_cpu_io_mixed    | 486 ms                                                                 | 495 ms: 1.02x slower                                                        |
| pprint_safe_repr           | 713 ms                                                                 | 726 ms: 1.02x slower                                                        |
| async_tree_cpu_io_mixed_tg | 475 ms                                                                 | 484 ms: 1.02x slower                                                        |
| gc_traversal               | 4.56 ms                                                                | 4.88 ms: 1.07x slower                                                       |
| Geometric mean             | (ref)                                                                  | 1.00x slower                                                                |

Benchmark hidden because not significant (37): async_tree_none, telco, richards_super, bench_mp_pool, scimark_lu, chaos, async_tree_memoization, float, deltablue, go, nqueens, dulwich_log, mdp, async_tree_io, connected_components, sqlalchemy_declarative, html5lib, xml_etree_parse, mako, sphinx, logging_format, sqlglot_transpile, scimark_fft, pylint, async_tree_none_tg, sympy_sum, async_tree_io_tg, asyncio_websockets, sqlglot_parse, bpe_tokeniser, shortest_path, sqlite_synth, sqlglot_normalize, k_core, async_tree_memoization_tg, json, pycparser

- Geometric mean (including insignificant results): 1.000x faster

# HPT report

- Reliability score: 79.66% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x
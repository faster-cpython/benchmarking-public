# Results vs. base

- fork: brandtbucher
- ref: 60ea678db0dd602ab693
- machine: linux-x86_64
- commit hash: 60ea678
- commit date: 2025-01-14
- overall geometric mean: 1.005x slower
- HPT reliability: 69.50%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250114-linux-x86_64-python-f7ceb317aec498823555-3.14.0a4+-f7ceb31 | bm-20250114-linux-x86_64-brandtbucher-60ea678db0dd602ab693-3.14.0a4+-60ea678 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 260 ms                                                                 | 261 ms: 1.00x slower                                                         |
| docutils       | 2.69 sec                                                               | 2.70 sec: 1.00x slower                                                       |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                                 |

Benchmark hidden because not significant (2): html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250114-linux-x86_64-python-f7ceb317aec498823555-3.14.0a4+-f7ceb31 | bm-20250114-linux-x86_64-brandtbucher-60ea678db0dd602ab693-3.14.0a4+-60ea678 |
|----------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed    | 498 ms                                                                 | 492 ms: 1.01x faster                                                         |
| async_tree_cpu_io_mixed_tg | 471 ms                                                                 | 466 ms: 1.01x faster                                                         |
| Geometric mean             | (ref)                                                                  | 1.00x faster                                                                 |

Benchmark hidden because not significant (9): async_tree_none_tg, async_tree_io, async_tree_io_tg, async_tree_memoization_tg, asyncio_websockets, async_tree_memoization, async_generators, coroutines, async_tree_none

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250114-linux-x86_64-python-f7ceb317aec498823555-3.14.0a4+-f7ceb31 | bm-20250114-linux-x86_64-brandtbucher-60ea678db0dd602ab693-3.14.0a4+-60ea678 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| pidigits       | 188 ms                                                                 | 186 ms: 1.01x faster                                                         |
| float          | 68.8 ms                                                                | 70.2 ms: 1.02x slower                                                        |
| nbody          | 85.2 ms                                                                | 93.8 ms: 1.10x slower                                                        |
| Geometric mean | (ref)                                                                  | 1.04x slower                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250114-linux-x86_64-python-f7ceb317aec498823555-3.14.0a4+-f7ceb31 | bm-20250114-linux-x86_64-brandtbucher-60ea678db0dd602ab693-3.14.0a4+-60ea678 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_effbot   | 3.06 ms                                                                | 3.00 ms: 1.02x faster                                                        |
| regex_dna      | 204 ms                                                                 | 202 ms: 1.01x faster                                                         |
| regex_compile  | 129 ms                                                                 | 128 ms: 1.01x faster                                                         |
| regex_v8       | 23.8 ms                                                                | 23.9 ms: 1.00x slower                                                        |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20250114-linux-x86_64-python-f7ceb317aec498823555-3.14.0a4+-f7ceb31 | bm-20250114-linux-x86_64-brandtbucher-60ea678db0dd602ab693-3.14.0a4+-60ea678 |
|---------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| xml_etree_process   | 55.7 ms                                                                | 54.7 ms: 1.02x faster                                                        |
| tomli_loads         | 1.85 sec                                                               | 1.83 sec: 1.01x faster                                                       |
| json_dumps          | 11.8 ms                                                                | 11.6 ms: 1.01x faster                                                        |
| json_loads          | 29.6 us                                                                | 29.4 us: 1.00x faster                                                        |
| xml_etree_iterparse | 94.2 ms                                                                | 94.5 ms: 1.00x slower                                                        |
| pickle_pure_python  | 312 us                                                                 | 319 us: 1.02x slower                                                         |
| Geometric mean      | (ref)                                                                  | 1.00x faster                                                                 |

Benchmark hidden because not significant (3): unpickle_pure_python, xml_etree_parse, xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20250114-linux-x86_64-python-f7ceb317aec498823555-3.14.0a4+-f7ceb31 | bm-20250114-linux-x86_64-brandtbucher-60ea678db0dd602ab693-3.14.0a4+-60ea678 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup | 12.9 ms                                                                | 12.8 ms: 1.00x faster                                                        |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                                 |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250114-linux-x86_64-python-f7ceb317aec498823555-3.14.0a4+-f7ceb31 | bm-20250114-linux-x86_64-brandtbucher-60ea678db0dd602ab693-3.14.0a4+-60ea678 |
|-----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| django_template | 33.3 ms                                                                | 33.8 ms: 1.01x slower                                                        |
| genshi_text     | 23.7 ms                                                                | 24.1 ms: 1.02x slower                                                        |
| mako            | 9.91 ms                                                                | 10.1 ms: 1.02x slower                                                        |
| genshi_xml      | 57.6 ms                                                                | 60.5 ms: 1.05x slower                                                        |
| Geometric mean  | (ref)                                                                  | 1.03x slower                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20250114-linux-x86_64-python-f7ceb317aec498823555-3.14.0a4+-f7ceb31 | bm-20250114-linux-x86_64-brandtbucher-60ea678db0dd602ab693-3.14.0a4+-60ea678 |
|----------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| sqlglot_normalize          | 110 ms                                                                 | 108 ms: 1.02x faster                                                         |
| gc_traversal               | 4.93 ms                                                                | 4.84 ms: 1.02x faster                                                        |
| telco                      | 7.69 ms                                                                | 7.55 ms: 1.02x faster                                                        |
| xml_etree_process          | 55.7 ms                                                                | 54.7 ms: 1.02x faster                                                        |
| regex_effbot               | 3.06 ms                                                                | 3.00 ms: 1.02x faster                                                        |
| connected_components       | 441 ms                                                                 | 435 ms: 1.01x faster                                                         |
| async_tree_cpu_io_mixed    | 498 ms                                                                 | 492 ms: 1.01x faster                                                         |
| regex_dna                  | 204 ms                                                                 | 202 ms: 1.01x faster                                                         |
| sympy_sum                  | 157 ms                                                                 | 156 ms: 1.01x faster                                                         |
| tomli_loads                | 1.85 sec                                                               | 1.83 sec: 1.01x faster                                                       |
| sqlglot_optimize           | 55.2 ms                                                                | 54.6 ms: 1.01x faster                                                        |
| async_tree_cpu_io_mixed_tg | 471 ms                                                                 | 466 ms: 1.01x faster                                                         |
| json_dumps                 | 11.8 ms                                                                | 11.6 ms: 1.01x faster                                                        |
| typing_runtime_protocols   | 168 us                                                                 | 166 us: 1.01x faster                                                         |
| pidigits                   | 188 ms                                                                 | 186 ms: 1.01x faster                                                         |
| pyflate                    | 453 ms                                                                 | 449 ms: 1.01x faster                                                         |
| generators                 | 37.7 ms                                                                | 37.5 ms: 1.01x faster                                                        |
| sqlglot_transpile          | 1.60 ms                                                                | 1.59 ms: 1.01x faster                                                        |
| regex_compile              | 129 ms                                                                 | 128 ms: 1.01x faster                                                         |
| coverage                   | 90.7 ms                                                                | 90.2 ms: 1.01x faster                                                        |
| shortest_path              | 481 ms                                                                 | 478 ms: 1.01x faster                                                         |
| json_loads                 | 29.6 us                                                                | 29.4 us: 1.00x faster                                                        |
| sqlalchemy_declarative     | 132 ms                                                                 | 131 ms: 1.00x faster                                                         |
| create_gc_cycles           | 2.45 ms                                                                | 2.44 ms: 1.00x faster                                                        |
| python_startup             | 12.9 ms                                                                | 12.8 ms: 1.00x faster                                                        |
| docutils                   | 2.69 sec                                                               | 2.70 sec: 1.00x slower                                                       |
| xml_etree_iterparse        | 94.2 ms                                                                | 94.5 ms: 1.00x slower                                                        |
| 2to3                       | 260 ms                                                                 | 261 ms: 1.00x slower                                                         |
| regex_v8                   | 23.8 ms                                                                | 23.9 ms: 1.00x slower                                                        |
| raytrace                   | 289 ms                                                                 | 291 ms: 1.01x slower                                                         |
| logging_format             | 6.31 us                                                                | 6.35 us: 1.01x slower                                                        |
| deltablue                  | 3.25 ms                                                                | 3.27 ms: 1.01x slower                                                        |
| deepcopy_memo              | 29.7 us                                                                | 29.9 us: 1.01x slower                                                        |
| go                         | 134 ms                                                                 | 135 ms: 1.01x slower                                                         |
| meteor_contest             | 108 ms                                                                 | 109 ms: 1.01x slower                                                         |
| hexiom                     | 7.12 ms                                                                | 7.18 ms: 1.01x slower                                                        |
| richards                   | 43.8 ms                                                                | 44.2 ms: 1.01x slower                                                        |
| scimark_monte_carlo        | 62.2 ms                                                                | 63.0 ms: 1.01x slower                                                        |
| fannkuch                   | 383 ms                                                                 | 389 ms: 1.01x slower                                                         |
| django_template            | 33.3 ms                                                                | 33.8 ms: 1.01x slower                                                        |
| bpe_tokeniser              | 4.40 sec                                                               | 4.47 sec: 1.02x slower                                                       |
| logging_silent             | 109 ns                                                                 | 111 ns: 1.02x slower                                                         |
| genshi_text                | 23.7 ms                                                                | 24.1 ms: 1.02x slower                                                        |
| mako                       | 9.91 ms                                                                | 10.1 ms: 1.02x slower                                                        |
| richards_super             | 49.9 ms                                                                | 50.9 ms: 1.02x slower                                                        |
| float                      | 68.8 ms                                                                | 70.2 ms: 1.02x slower                                                        |
| pickle_pure_python         | 312 us                                                                 | 319 us: 1.02x slower                                                         |
| chaos                      | 61.1 ms                                                                | 62.7 ms: 1.03x slower                                                        |
| scimark_sparse_mat_mult    | 4.44 ms                                                                | 4.60 ms: 1.04x slower                                                        |
| scimark_sor                | 112 ms                                                                 | 117 ms: 1.04x slower                                                         |
| genshi_xml                 | 57.6 ms                                                                | 60.5 ms: 1.05x slower                                                        |
| scimark_fft                | 314 ms                                                                 | 331 ms: 1.05x slower                                                         |
| crypto_pyaes               | 67.6 ms                                                                | 72.2 ms: 1.07x slower                                                        |
| nbody                      | 85.2 ms                                                                | 93.8 ms: 1.10x slower                                                        |
| spectral_norm              | 102 ms                                                                 | 121 ms: 1.19x slower                                                         |
| Geometric mean             | (ref)                                                                  | 1.01x slower                                                                 |

Benchmark hidden because not significant (41): pprint_pformat, unpickle_pure_python, pprint_safe_repr, xml_etree_parse, json, comprehensions, nqueens, async_tree_none_tg, sqlalchemy_imperative, async_tree_io, mdp, thrift, deepcopy_reduce, sympy_str, bench_thread_pool, async_tree_io_tg, pylint, python_startup_no_site, sympy_integrate, sqlglot_parse, many_optionals, bench_mp_pool, async_tree_memoization_tg, dulwich_log, asyncio_websockets, subparsers, sqlite_synth, sympy_expand, k_core, scimark_lu, async_tree_memoization, pycparser, async_generators, coroutines, deepcopy, sphinx, html5lib, xml_etree_generate, pathlib, logging_simple, async_tree_none

- Geometric mean (including insignificant results): 1.005x slower

# HPT report

- Reliability score: 69.50% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x
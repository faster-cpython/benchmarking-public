# Results vs. base

- fork: brandtbucher
- ref: tier_two_refcounts
- machine: linux-x86_64
- commit hash: 5501f0a
- commit date: 2025-01-15
- overall geometric mean: 1.004x slower
- HPT reliability: 98.51%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250114-linux-x86_64-python-f7ceb317aec498823555-3.14.0a4+-f7ceb31 | bm-20250115-linux-x86_64-brandtbucher-tier_two_refcounts-3.14.0a4+-5501f0a |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 260 ms                                                                 | 261 ms: 1.00x slower                                                       |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                               |

Benchmark hidden because not significant (3): docutils, html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250114-linux-x86_64-python-f7ceb317aec498823555-3.14.0a4+-f7ceb31 | bm-20250115-linux-x86_64-brandtbucher-tier_two_refcounts-3.14.0a4+-5501f0a |
|----------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| coroutines                 | 23.8 ms                                                                | 23.3 ms: 1.02x faster                                                      |
| async_tree_cpu_io_mixed_tg | 471 ms                                                                 | 474 ms: 1.01x slower                                                       |
| async_tree_cpu_io_mixed    | 498 ms                                                                 | 503 ms: 1.01x slower                                                       |
| async_generators           | 407 ms                                                                 | 416 ms: 1.02x slower                                                       |
| Geometric mean             | (ref)                                                                  | 1.00x slower                                                               |

Benchmark hidden because not significant (7): async_tree_io, async_tree_memoization_tg, async_tree_memoization, asyncio_websockets, async_tree_io_tg, async_tree_none_tg, async_tree_none

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250114-linux-x86_64-python-f7ceb317aec498823555-3.14.0a4+-f7ceb31 | bm-20250115-linux-x86_64-brandtbucher-tier_two_refcounts-3.14.0a4+-5501f0a |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pidigits       | 188 ms                                                                 | 186 ms: 1.01x faster                                                       |
| float          | 68.8 ms                                                                | 70.4 ms: 1.02x slower                                                      |
| nbody          | 85.2 ms                                                                | 91.8 ms: 1.08x slower                                                      |
| Geometric mean | (ref)                                                                  | 1.03x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250114-linux-x86_64-python-f7ceb317aec498823555-3.14.0a4+-f7ceb31 | bm-20250115-linux-x86_64-brandtbucher-tier_two_refcounts-3.14.0a4+-5501f0a |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_dna      | 204 ms                                                                 | 203 ms: 1.00x faster                                                       |
| regex_effbot   | 3.06 ms                                                                | 3.05 ms: 1.00x faster                                                      |
| regex_compile  | 129 ms                                                                 | 130 ms: 1.00x slower                                                       |
| regex_v8       | 23.8 ms                                                                | 24.2 ms: 1.02x slower                                                      |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20250114-linux-x86_64-python-f7ceb317aec498823555-3.14.0a4+-f7ceb31 | bm-20250115-linux-x86_64-brandtbucher-tier_two_refcounts-3.14.0a4+-5501f0a |
|---------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| xml_etree_process   | 55.7 ms                                                                | 55.3 ms: 1.01x faster                                                      |
| tomli_loads         | 1.85 sec                                                               | 1.84 sec: 1.01x faster                                                     |
| xml_etree_iterparse | 94.2 ms                                                                | 95.0 ms: 1.01x slower                                                      |
| xml_etree_generate  | 77.7 ms                                                                | 79.1 ms: 1.02x slower                                                      |
| pickle_pure_python  | 312 us                                                                 | 320 us: 1.03x slower                                                       |
| Geometric mean      | (ref)                                                                  | 1.00x slower                                                               |

Benchmark hidden because not significant (4): xml_etree_parse, json_loads, json_dumps, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20250114-linux-x86_64-python-f7ceb317aec498823555-3.14.0a4+-f7ceb31 | bm-20250115-linux-x86_64-brandtbucher-tier_two_refcounts-3.14.0a4+-5501f0a |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup | 12.9 ms                                                                | 12.8 ms: 1.00x faster                                                      |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                               |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250114-linux-x86_64-python-f7ceb317aec498823555-3.14.0a4+-f7ceb31 | bm-20250115-linux-x86_64-brandtbucher-tier_two_refcounts-3.14.0a4+-5501f0a |
|-----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| django_template | 33.3 ms                                                                | 33.7 ms: 1.01x slower                                                      |
| genshi_text     | 23.7 ms                                                                | 24.0 ms: 1.01x slower                                                      |
| genshi_xml      | 57.6 ms                                                                | 59.2 ms: 1.03x slower                                                      |
| Geometric mean  | (ref)                                                                  | 1.01x slower                                                               |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                  | bm-20250114-linux-x86_64-python-f7ceb317aec498823555-3.14.0a4+-f7ceb31 | bm-20250115-linux-x86_64-brandtbucher-tier_two_refcounts-3.14.0a4+-5501f0a |
|----------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pprint_pformat             | 1.52 sec                                                               | 1.48 sec: 1.02x faster                                                     |
| coroutines                 | 23.8 ms                                                                | 23.3 ms: 1.02x faster                                                      |
| pyflate                    | 453 ms                                                                 | 445 ms: 1.02x faster                                                       |
| logging_silent             | 109 ns                                                                 | 107 ns: 1.01x faster                                                       |
| raytrace                   | 289 ms                                                                 | 286 ms: 1.01x faster                                                       |
| sqlglot_normalize          | 110 ms                                                                 | 109 ms: 1.01x faster                                                       |
| sqlglot_transpile          | 1.60 ms                                                                | 1.58 ms: 1.01x faster                                                      |
| xml_etree_process          | 55.7 ms                                                                | 55.3 ms: 1.01x faster                                                      |
| pidigits                   | 188 ms                                                                 | 186 ms: 1.01x faster                                                       |
| tomli_loads                | 1.85 sec                                                               | 1.84 sec: 1.01x faster                                                     |
| sympy_sum                  | 157 ms                                                                 | 156 ms: 1.01x faster                                                       |
| coverage                   | 90.7 ms                                                                | 90.3 ms: 1.00x faster                                                      |
| dulwich_log                | 67.4 ms                                                                | 67.1 ms: 1.00x faster                                                      |
| regex_dna                  | 204 ms                                                                 | 203 ms: 1.00x faster                                                       |
| connected_components       | 441 ms                                                                 | 439 ms: 1.00x faster                                                       |
| regex_effbot               | 3.06 ms                                                                | 3.05 ms: 1.00x faster                                                      |
| meteor_contest             | 108 ms                                                                 | 108 ms: 1.00x faster                                                       |
| python_startup             | 12.9 ms                                                                | 12.8 ms: 1.00x faster                                                      |
| 2to3                       | 260 ms                                                                 | 261 ms: 1.00x slower                                                       |
| sympy_str                  | 281 ms                                                                 | 282 ms: 1.00x slower                                                       |
| regex_compile              | 129 ms                                                                 | 130 ms: 1.00x slower                                                       |
| sympy_integrate            | 20.6 ms                                                                | 20.8 ms: 1.01x slower                                                      |
| sqlite_synth               | 2.73 us                                                                | 2.75 us: 1.01x slower                                                      |
| scimark_monte_carlo        | 62.2 ms                                                                | 62.6 ms: 1.01x slower                                                      |
| async_tree_cpu_io_mixed_tg | 471 ms                                                                 | 474 ms: 1.01x slower                                                       |
| create_gc_cycles           | 2.45 ms                                                                | 2.47 ms: 1.01x slower                                                      |
| fannkuch                   | 383 ms                                                                 | 386 ms: 1.01x slower                                                       |
| comprehensions             | 17.3 us                                                                | 17.5 us: 1.01x slower                                                      |
| xml_etree_iterparse        | 94.2 ms                                                                | 95.0 ms: 1.01x slower                                                      |
| richards_super             | 49.9 ms                                                                | 50.4 ms: 1.01x slower                                                      |
| async_tree_cpu_io_mixed    | 498 ms                                                                 | 503 ms: 1.01x slower                                                       |
| django_template            | 33.3 ms                                                                | 33.7 ms: 1.01x slower                                                      |
| logging_format             | 6.31 us                                                                | 6.38 us: 1.01x slower                                                      |
| genshi_text                | 23.7 ms                                                                | 24.0 ms: 1.01x slower                                                      |
| subparsers                 | 20.7 ms                                                                | 21.0 ms: 1.01x slower                                                      |
| scimark_sor                | 112 ms                                                                 | 114 ms: 1.01x slower                                                       |
| scimark_fft                | 314 ms                                                                 | 319 ms: 1.01x slower                                                       |
| logging_simple             | 5.74 us                                                                | 5.83 us: 1.02x slower                                                      |
| xml_etree_generate         | 77.7 ms                                                                | 79.1 ms: 1.02x slower                                                      |
| deepcopy_memo              | 29.7 us                                                                | 30.2 us: 1.02x slower                                                      |
| regex_v8                   | 23.8 ms                                                                | 24.2 ms: 1.02x slower                                                      |
| deepcopy                   | 267 us                                                                 | 272 us: 1.02x slower                                                       |
| gc_traversal               | 4.93 ms                                                                | 5.03 ms: 1.02x slower                                                      |
| crypto_pyaes               | 67.6 ms                                                                | 68.9 ms: 1.02x slower                                                      |
| float                      | 68.8 ms                                                                | 70.4 ms: 1.02x slower                                                      |
| async_generators           | 407 ms                                                                 | 416 ms: 1.02x slower                                                       |
| pickle_pure_python         | 312 us                                                                 | 320 us: 1.03x slower                                                       |
| spectral_norm              | 102 ms                                                                 | 104 ms: 1.03x slower                                                       |
| genshi_xml                 | 57.6 ms                                                                | 59.2 ms: 1.03x slower                                                      |
| scimark_sparse_mat_mult    | 4.44 ms                                                                | 4.58 ms: 1.03x slower                                                      |
| generators                 | 37.7 ms                                                                | 40.2 ms: 1.07x slower                                                      |
| nbody                      | 85.2 ms                                                                | 91.8 ms: 1.08x slower                                                      |
| Geometric mean             | (ref)                                                                  | 1.00x slower                                                               |

Benchmark hidden because not significant (44): k_core, async_tree_io, async_tree_memoization_tg, html5lib, telco, typing_runtime_protocols, xml_etree_parse, bpe_tokeniser, sqlalchemy_imperative, pathlib, sqlalchemy_declarative, async_tree_memoization, sqlglot_parse, bench_mp_pool, scimark_lu, docutils, python_startup_no_site, deltablue, pylint, mdp, asyncio_websockets, mako, chaos, thrift, json, sqlglot_optimize, json_loads, go, bench_thread_pool, shortest_path, async_tree_io_tg, nqueens, hexiom, sympy_expand, json_dumps, unpickle_pure_python, deepcopy_reduce, many_optionals, async_tree_none_tg, richards, sphinx, pprint_safe_repr, async_tree_none, pycparser

- Geometric mean (including insignificant results): 1.004x slower

# HPT report

- Reliability score: 98.51% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x
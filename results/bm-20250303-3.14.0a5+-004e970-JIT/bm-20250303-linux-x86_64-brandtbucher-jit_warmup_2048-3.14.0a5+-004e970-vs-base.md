# Results vs. base

- fork: brandtbucher
- ref: jit_warmup_2048
- machine: linux-x86_64
- commit hash: 004e970
- commit date: 2025-03-03
- overall geometric mean: 1.004x faster
- HPT reliability: 99.82%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250302-linux-x86_64-python-7afa476874b9a432ad6d-3.14.0a5+-7afa476 | bm-20250303-linux-x86_64-brandtbucher-jit_warmup_2048-3.14.0a5+-004e970 |
|----------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 261 ms                                                                 | 259 ms: 1.00x faster                                                    |
| docutils       | 2.66 sec                                                               | 2.68 sec: 1.01x slower                                                  |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                            |

Benchmark hidden because not significant (2): html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250302-linux-x86_64-python-7afa476874b9a432ad6d-3.14.0a5+-7afa476 | bm-20250303-linux-x86_64-brandtbucher-jit_warmup_2048-3.14.0a5+-004e970 |
|----------------------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_cpu_io_mixed    | 495 ms                                                                 | 486 ms: 1.02x faster                                                    |
| coroutines                 | 24.7 ms                                                                | 24.3 ms: 1.01x faster                                                   |
| async_tree_cpu_io_mixed_tg | 485 ms                                                                 | 479 ms: 1.01x faster                                                    |
| async_generators           | 410 ms                                                                 | 407 ms: 1.01x faster                                                    |
| Geometric mean             | (ref)                                                                  | 1.00x faster                                                            |

Benchmark hidden because not significant (7): async_tree_none_tg, asyncio_websockets, async_tree_memoization, async_tree_none, async_tree_io, async_tree_memoization_tg, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250302-linux-x86_64-python-7afa476874b9a432ad6d-3.14.0a5+-7afa476 | bm-20250303-linux-x86_64-brandtbucher-jit_warmup_2048-3.14.0a5+-004e970 |
|----------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| nbody          | 91.2 ms                                                                | 94.1 ms: 1.03x slower                                                   |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                            |

Benchmark hidden because not significant (2): float, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250302-linux-x86_64-python-7afa476874b9a432ad6d-3.14.0a5+-7afa476 | bm-20250303-linux-x86_64-brandtbucher-jit_warmup_2048-3.14.0a5+-004e970 |
|----------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 128 ms                                                                 | 127 ms: 1.01x faster                                                    |
| regex_effbot   | 3.36 ms                                                                | 3.35 ms: 1.00x faster                                                   |
| regex_dna      | 214 ms                                                                 | 219 ms: 1.03x slower                                                    |
| regex_v8       | 24.9 ms                                                                | 25.6 ms: 1.03x slower                                                   |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250302-linux-x86_64-python-7afa476874b9a432ad6d-3.14.0a5+-7afa476 | bm-20250303-linux-x86_64-brandtbucher-jit_warmup_2048-3.14.0a5+-004e970 |
|----------------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| unpickle_pure_python | 208 us                                                                 | 204 us: 1.02x faster                                                    |
| json_dumps           | 11.4 ms                                                                | 11.2 ms: 1.01x faster                                                   |
| xml_etree_generate   | 79.0 ms                                                                | 78.2 ms: 1.01x faster                                                   |
| xml_etree_process    | 56.0 ms                                                                | 55.5 ms: 1.01x faster                                                   |
| xml_etree_parse      | 148 ms                                                                 | 147 ms: 1.01x faster                                                    |
| xml_etree_iterparse  | 99.5 ms                                                                | 99.2 ms: 1.00x faster                                                   |
| json_loads           | 29.8 us                                                                | 29.9 us: 1.00x slower                                                   |
| pickle_pure_python   | 319 us                                                                 | 321 us: 1.01x slower                                                    |
| Geometric mean       | (ref)                                                                  | 1.01x faster                                                            |

Benchmark hidden because not significant (1): tomli_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250302-linux-x86_64-python-7afa476874b9a432ad6d-3.14.0a5+-7afa476 | bm-20250303-linux-x86_64-brandtbucher-jit_warmup_2048-3.14.0a5+-004e970 |
|------------------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 12.9 ms                                                                | 13.0 ms: 1.00x slower                                                   |
| python_startup_no_site | 7.12 ms                                                                | 7.16 ms: 1.01x slower                                                   |
| Geometric mean         | (ref)                                                                  | 1.00x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250302-linux-x86_64-python-7afa476874b9a432ad6d-3.14.0a5+-7afa476 | bm-20250303-linux-x86_64-brandtbucher-jit_warmup_2048-3.14.0a5+-004e970 |
|-----------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_text     | 22.0 ms                                                                | 21.1 ms: 1.04x faster                                                   |
| mako            | 10.5 ms                                                                | 10.2 ms: 1.02x faster                                                   |
| django_template | 31.9 ms                                                                | 31.5 ms: 1.01x faster                                                   |
| genshi_xml      | 49.6 ms                                                                | 49.3 ms: 1.01x faster                                                   |
| Geometric mean  | (ref)                                                                  | 1.02x faster                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20250302-linux-x86_64-python-7afa476874b9a432ad6d-3.14.0a5+-7afa476 | bm-20250303-linux-x86_64-brandtbucher-jit_warmup_2048-3.14.0a5+-004e970 |
|----------------------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pyflate                    | 443 ms                                                                 | 426 ms: 1.04x faster                                                    |
| genshi_text                | 22.0 ms                                                                | 21.1 ms: 1.04x faster                                                   |
| crypto_pyaes               | 74.3 ms                                                                | 71.9 ms: 1.03x faster                                                   |
| nqueens                    | 83.5 ms                                                                | 81.1 ms: 1.03x faster                                                   |
| scimark_sparse_mat_mult    | 4.61 ms                                                                | 4.48 ms: 1.03x faster                                                   |
| typing_runtime_protocols   | 164 us                                                                 | 160 us: 1.03x faster                                                    |
| scimark_sor                | 122 ms                                                                 | 119 ms: 1.02x faster                                                    |
| shortest_path              | 485 ms                                                                 | 475 ms: 1.02x faster                                                    |
| unpickle_pure_python       | 208 us                                                                 | 204 us: 1.02x faster                                                    |
| mako                       | 10.5 ms                                                                | 10.2 ms: 1.02x faster                                                   |
| coverage                   | 85.7 ms                                                                | 84.2 ms: 1.02x faster                                                   |
| async_tree_cpu_io_mixed    | 495 ms                                                                 | 486 ms: 1.02x faster                                                    |
| connected_components       | 448 ms                                                                 | 441 ms: 1.02x faster                                                    |
| thrift                     | 764 us                                                                 | 752 us: 1.02x faster                                                    |
| coroutines                 | 24.7 ms                                                                | 24.3 ms: 1.01x faster                                                   |
| scimark_fft                | 314 ms                                                                 | 310 ms: 1.01x faster                                                    |
| async_tree_cpu_io_mixed_tg | 485 ms                                                                 | 479 ms: 1.01x faster                                                    |
| json_dumps                 | 11.4 ms                                                                | 11.2 ms: 1.01x faster                                                   |
| deltablue                  | 3.32 ms                                                                | 3.29 ms: 1.01x faster                                                   |
| deepcopy_reduce            | 2.66 us                                                                | 2.63 us: 1.01x faster                                                   |
| xml_etree_generate         | 79.0 ms                                                                | 78.2 ms: 1.01x faster                                                   |
| sqlite_synth               | 2.74 us                                                                | 2.71 us: 1.01x faster                                                   |
| django_template            | 31.9 ms                                                                | 31.5 ms: 1.01x faster                                                   |
| xml_etree_process          | 56.0 ms                                                                | 55.5 ms: 1.01x faster                                                   |
| richards                   | 43.9 ms                                                                | 43.5 ms: 1.01x faster                                                   |
| chaos                      | 60.2 ms                                                                | 59.7 ms: 1.01x faster                                                   |
| regex_compile              | 128 ms                                                                 | 127 ms: 1.01x faster                                                    |
| async_generators           | 410 ms                                                                 | 407 ms: 1.01x faster                                                    |
| xml_etree_parse            | 148 ms                                                                 | 147 ms: 1.01x faster                                                    |
| hexiom                     | 6.40 ms                                                                | 6.36 ms: 1.01x faster                                                   |
| genshi_xml                 | 49.6 ms                                                                | 49.3 ms: 1.01x faster                                                   |
| scimark_lu                 | 117 ms                                                                 | 116 ms: 1.01x faster                                                    |
| bpe_tokeniser              | 4.46 sec                                                               | 4.44 sec: 1.01x faster                                                  |
| gc_traversal               | 4.80 ms                                                                | 4.77 ms: 1.01x faster                                                   |
| dulwich_log                | 67.6 ms                                                                | 67.2 ms: 1.01x faster                                                   |
| telco                      | 7.63 ms                                                                | 7.59 ms: 1.00x faster                                                   |
| create_gc_cycles           | 2.43 ms                                                                | 2.42 ms: 1.00x faster                                                   |
| 2to3                       | 261 ms                                                                 | 259 ms: 1.00x faster                                                    |
| sqlglot_normalize          | 106 ms                                                                 | 106 ms: 1.00x faster                                                    |
| regex_effbot               | 3.36 ms                                                                | 3.35 ms: 1.00x faster                                                   |
| xml_etree_iterparse        | 99.5 ms                                                                | 99.2 ms: 1.00x faster                                                   |
| json_loads                 | 29.8 us                                                                | 29.9 us: 1.00x slower                                                   |
| python_startup             | 12.9 ms                                                                | 13.0 ms: 1.00x slower                                                   |
| bench_thread_pool          | 874 us                                                                 | 879 us: 1.01x slower                                                    |
| sympy_expand               | 469 ms                                                                 | 471 ms: 1.01x slower                                                    |
| sympy_str                  | 273 ms                                                                 | 275 ms: 1.01x slower                                                    |
| python_startup_no_site     | 7.12 ms                                                                | 7.16 ms: 1.01x slower                                                   |
| bench_mp_pool              | 81.7 ms                                                                | 82.2 ms: 1.01x slower                                                   |
| many_optionals             | 965 us                                                                 | 971 us: 1.01x slower                                                    |
| docutils                   | 2.66 sec                                                               | 2.68 sec: 1.01x slower                                                  |
| sympy_sum                  | 150 ms                                                                 | 152 ms: 1.01x slower                                                    |
| pickle_pure_python         | 319 us                                                                 | 321 us: 1.01x slower                                                    |
| deepcopy_memo              | 28.7 us                                                                | 28.9 us: 1.01x slower                                                   |
| sympy_integrate            | 20.1 ms                                                                | 20.3 ms: 1.01x slower                                                   |
| go                         | 118 ms                                                                 | 119 ms: 1.01x slower                                                    |
| generators                 | 27.9 ms                                                                | 28.2 ms: 1.01x slower                                                   |
| mdp                        | 2.51 sec                                                               | 2.54 sec: 1.01x slower                                                  |
| pprint_pformat             | 1.50 sec                                                               | 1.52 sec: 1.01x slower                                                  |
| sqlalchemy_declarative     | 130 ms                                                                 | 132 ms: 1.01x slower                                                    |
| pprint_safe_repr           | 734 ms                                                                 | 744 ms: 1.01x slower                                                    |
| regex_dna                  | 214 ms                                                                 | 219 ms: 1.03x slower                                                    |
| regex_v8                   | 24.9 ms                                                                | 25.6 ms: 1.03x slower                                                   |
| nbody                      | 91.2 ms                                                                | 94.1 ms: 1.03x slower                                                   |
| Geometric mean             | (ref)                                                                  | 1.00x faster                                                            |

Benchmark hidden because not significant (33): k_core, pycparser, pylint, async_tree_none_tg, float, subparsers, spectral_norm, logging_format, sqlglot_transpile, asyncio_websockets, raytrace, sqlglot_parse, pathlib, logging_silent, async_tree_memoization, logging_simple, comprehensions, async_tree_none, sphinx, pidigits, sqlglot_optimize, scimark_monte_carlo, deepcopy, sqlalchemy_imperative, tomli_loads, richards_super, html5lib, meteor_contest, fannkuch, json, async_tree_io, async_tree_memoization_tg, async_tree_io_tg

- Geometric mean (including insignificant results): 1.004x faster

# HPT report

- Reliability score: 99.82% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x
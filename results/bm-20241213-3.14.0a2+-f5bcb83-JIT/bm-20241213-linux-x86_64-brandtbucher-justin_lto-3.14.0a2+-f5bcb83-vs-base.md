# Results vs. base

- fork: brandtbucher
- ref: justin_lto
- machine: linux-x86_64
- commit hash: f5bcb83
- commit date: 2024-12-13
- overall geometric mean: 1.015x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x slower
- Memory change: 0.99x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241204-linux-x86_64-python-94b8f8b40943bf38cf5c-3.14.0a2+-94b8f8b | bm-20241213-linux-x86_64-brandtbucher-justin_lto-3.14.0a2+-f5bcb83 |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------:|
| 2to3           | 258 ms                                                                 | 262 ms: 1.02x slower                                               |
| docutils       | 2.68 sec                                                               | 2.71 sec: 1.01x slower                                             |
| html5lib       | 64.7 ms                                                                | 65.6 ms: 1.01x slower                                              |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                       |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241204-linux-x86_64-python-94b8f8b40943bf38cf5c-3.14.0a2+-94b8f8b | bm-20241213-linux-x86_64-brandtbucher-justin_lto-3.14.0a2+-f5bcb83 |
|----------------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------:|
| async_tree_cpu_io_mixed_tg | 489 ms                                                                 | 479 ms: 1.02x faster                                               |
| async_tree_cpu_io_mixed    | 503 ms                                                                 | 495 ms: 1.02x faster                                               |
| async_tree_none_tg         | 254 ms                                                                 | 252 ms: 1.01x faster                                               |
| async_generators           | 449 ms                                                                 | 458 ms: 1.02x slower                                               |
| Geometric mean             | (ref)                                                                  | 1.00x faster                                                       |

Benchmark hidden because not significant (7): async_tree_none, async_tree_memoization_tg, coroutines, async_tree_memoization, asyncio_websockets, async_tree_io, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241204-linux-x86_64-python-94b8f8b40943bf38cf5c-3.14.0a2+-94b8f8b | bm-20241213-linux-x86_64-brandtbucher-justin_lto-3.14.0a2+-f5bcb83 |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------:|
| nbody          | 80.8 ms                                                                | 82.8 ms: 1.02x slower                                              |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                       |

Benchmark hidden because not significant (2): pidigits, float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241204-linux-x86_64-python-94b8f8b40943bf38cf5c-3.14.0a2+-94b8f8b | bm-20241213-linux-x86_64-brandtbucher-justin_lto-3.14.0a2+-f5bcb83 |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_effbot   | 3.51 ms                                                                | 3.38 ms: 1.04x faster                                              |
| regex_dna      | 220 ms                                                                 | 216 ms: 1.02x faster                                               |
| regex_v8       | 25.1 ms                                                                | 24.9 ms: 1.01x faster                                              |
| regex_compile  | 128 ms                                                                 | 132 ms: 1.03x slower                                               |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241204-linux-x86_64-python-94b8f8b40943bf38cf5c-3.14.0a2+-94b8f8b | bm-20241213-linux-x86_64-brandtbucher-justin_lto-3.14.0a2+-f5bcb83 |
|----------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------:|
| xml_etree_generate   | 78.2 ms                                                                | 77.6 ms: 1.01x faster                                              |
| tomli_loads          | 1.93 sec                                                               | 1.92 sec: 1.01x faster                                             |
| json_loads           | 26.3 us                                                                | 26.2 us: 1.00x faster                                              |
| unpickle_pure_python | 195 us                                                                 | 199 us: 1.02x slower                                               |
| pickle_pure_python   | 318 us                                                                 | 326 us: 1.03x slower                                               |
| Geometric mean       | (ref)                                                                  | 1.00x slower                                                       |

Benchmark hidden because not significant (4): xml_etree_parse, xml_etree_process, xml_etree_iterparse, json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241204-linux-x86_64-python-94b8f8b40943bf38cf5c-3.14.0a2+-94b8f8b | bm-20241213-linux-x86_64-brandtbucher-justin_lto-3.14.0a2+-f5bcb83 |
|------------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup_no_site | 7.04 ms                                                                | 7.03 ms: 1.00x faster                                              |
| python_startup         | 12.8 ms                                                                | 12.8 ms: 1.00x faster                                              |
| Geometric mean         | (ref)                                                                  | 1.00x faster                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241204-linux-x86_64-python-94b8f8b40943bf38cf5c-3.14.0a2+-94b8f8b | bm-20241213-linux-x86_64-brandtbucher-justin_lto-3.14.0a2+-f5bcb83 |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------:|
| mako           | 10.2 ms                                                                | 10.4 ms: 1.02x slower                                              |
| genshi_text    | 24.0 ms                                                                | 25.2 ms: 1.05x slower                                              |
| genshi_xml     | 57.0 ms                                                                | 60.3 ms: 1.06x slower                                              |
| Geometric mean | (ref)                                                                  | 1.03x slower                                                       |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                  | bm-20241204-linux-x86_64-python-94b8f8b40943bf38cf5c-3.14.0a2+-94b8f8b | bm-20241213-linux-x86_64-brandtbucher-justin_lto-3.14.0a2+-f5bcb83 |
|----------------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------:|
| mdp                        | 2.77 sec                                                               | 2.58 sec: 1.07x faster                                             |
| gc_traversal               | 4.75 ms                                                                | 4.57 ms: 1.04x faster                                              |
| regex_effbot               | 3.51 ms                                                                | 3.38 ms: 1.04x faster                                              |
| deepcopy_reduce            | 2.81 us                                                                | 2.74 us: 1.03x faster                                              |
| async_tree_cpu_io_mixed_tg | 489 ms                                                                 | 479 ms: 1.02x faster                                               |
| regex_dna                  | 220 ms                                                                 | 216 ms: 1.02x faster                                               |
| nqueens                    | 91.0 ms                                                                | 89.3 ms: 1.02x faster                                              |
| async_tree_cpu_io_mixed    | 503 ms                                                                 | 495 ms: 1.02x faster                                               |
| typing_runtime_protocols   | 169 us                                                                 | 167 us: 1.01x faster                                               |
| async_tree_none_tg         | 254 ms                                                                 | 252 ms: 1.01x faster                                               |
| regex_v8                   | 25.1 ms                                                                | 24.9 ms: 1.01x faster                                              |
| xml_etree_generate         | 78.2 ms                                                                | 77.6 ms: 1.01x faster                                              |
| tomli_loads                | 1.93 sec                                                               | 1.92 sec: 1.01x faster                                             |
| json_loads                 | 26.3 us                                                                | 26.2 us: 1.00x faster                                              |
| python_startup_no_site     | 7.04 ms                                                                | 7.03 ms: 1.00x faster                                              |
| python_startup             | 12.8 ms                                                                | 12.8 ms: 1.00x faster                                              |
| bench_thread_pool          | 877 us                                                                 | 881 us: 1.00x slower                                               |
| bpe_tokeniser              | 4.39 sec                                                               | 4.41 sec: 1.01x slower                                             |
| sqlalchemy_declarative     | 130 ms                                                                 | 131 ms: 1.01x slower                                               |
| docutils                   | 2.68 sec                                                               | 2.71 sec: 1.01x slower                                             |
| crypto_pyaes               | 68.6 ms                                                                | 69.3 ms: 1.01x slower                                              |
| subparsers                 | 20.9 ms                                                                | 21.1 ms: 1.01x slower                                              |
| sqlglot_normalize          | 110 ms                                                                 | 111 ms: 1.01x slower                                               |
| fannkuch                   | 385 ms                                                                 | 388 ms: 1.01x slower                                               |
| coverage                   | 82.6 ms                                                                | 83.6 ms: 1.01x slower                                              |
| shortest_path              | 478 ms                                                                 | 484 ms: 1.01x slower                                               |
| pathlib                    | 16.2 ms                                                                | 16.4 ms: 1.01x slower                                              |
| scimark_sparse_mat_mult    | 4.57 ms                                                                | 4.63 ms: 1.01x slower                                              |
| connected_components       | 434 ms                                                                 | 440 ms: 1.01x slower                                               |
| dulwich_log                | 67.6 ms                                                                | 68.6 ms: 1.01x slower                                              |
| html5lib                   | 64.7 ms                                                                | 65.6 ms: 1.01x slower                                              |
| 2to3                       | 258 ms                                                                 | 262 ms: 1.02x slower                                               |
| pyflate                    | 447 ms                                                                 | 455 ms: 1.02x slower                                               |
| unpickle_pure_python       | 195 us                                                                 | 199 us: 1.02x slower                                               |
| scimark_lu                 | 111 ms                                                                 | 113 ms: 1.02x slower                                               |
| scimark_monte_carlo        | 64.8 ms                                                                | 66.0 ms: 1.02x slower                                              |
| sqlalchemy_imperative      | 16.7 ms                                                                | 17.0 ms: 1.02x slower                                              |
| async_generators           | 449 ms                                                                 | 458 ms: 1.02x slower                                               |
| sqlglot_optimize           | 55.3 ms                                                                | 56.4 ms: 1.02x slower                                              |
| mako                       | 10.2 ms                                                                | 10.4 ms: 1.02x slower                                              |
| many_optionals             | 974 us                                                                 | 993 us: 1.02x slower                                               |
| deepcopy_memo              | 29.2 us                                                                | 29.8 us: 1.02x slower                                              |
| sympy_integrate            | 20.5 ms                                                                | 20.9 ms: 1.02x slower                                              |
| sqlglot_transpile          | 1.64 ms                                                                | 1.67 ms: 1.02x slower                                              |
| nbody                      | 80.8 ms                                                                | 82.8 ms: 1.02x slower                                              |
| pickle_pure_python         | 318 us                                                                 | 326 us: 1.03x slower                                               |
| scimark_fft                | 321 ms                                                                 | 329 ms: 1.03x slower                                               |
| sqlglot_parse              | 1.32 ms                                                                | 1.35 ms: 1.03x slower                                              |
| sympy_str                  | 280 ms                                                                 | 288 ms: 1.03x slower                                               |
| regex_compile              | 128 ms                                                                 | 132 ms: 1.03x slower                                               |
| logging_simple             | 5.75 us                                                                | 5.92 us: 1.03x slower                                              |
| pycparser                  | 1.15 sec                                                               | 1.19 sec: 1.03x slower                                             |
| deltablue                  | 3.17 ms                                                                | 3.27 ms: 1.03x slower                                              |
| sympy_sum                  | 153 ms                                                                 | 159 ms: 1.03x slower                                               |
| generators                 | 36.2 ms                                                                | 37.4 ms: 1.03x slower                                              |
| pprint_safe_repr           | 715 ms                                                                 | 740 ms: 1.03x slower                                               |
| sympy_expand               | 473 ms                                                                 | 490 ms: 1.04x slower                                               |
| logging_silent             | 101 ns                                                                 | 104 ns: 1.04x slower                                               |
| logging_format             | 6.30 us                                                                | 6.55 us: 1.04x slower                                              |
| genshi_text                | 24.0 ms                                                                | 25.2 ms: 1.05x slower                                              |
| comprehensions             | 17.2 us                                                                | 18.1 us: 1.05x slower                                              |
| genshi_xml                 | 57.0 ms                                                                | 60.3 ms: 1.06x slower                                              |
| pprint_pformat             | 1.46 sec                                                               | 1.55 sec: 1.06x slower                                             |
| chaos                      | 59.1 ms                                                                | 62.9 ms: 1.06x slower                                              |
| raytrace                   | 282 ms                                                                 | 305 ms: 1.08x slower                                               |
| hexiom                     | 6.98 ms                                                                | 7.77 ms: 1.11x slower                                              |
| richards                   | 37.3 ms                                                                | 42.3 ms: 1.13x slower                                              |
| richards_super             | 44.7 ms                                                                | 51.3 ms: 1.15x slower                                              |
| go                         | 135 ms                                                                 | 155 ms: 1.15x slower                                               |
| Geometric mean             | (ref)                                                                  | 1.02x slower                                                       |

Benchmark hidden because not significant (29): thrift, async_tree_none, async_tree_memoization_tg, scimark_sor, json, xml_etree_parse, spectral_norm, coroutines, pidigits, xml_etree_process, bench_mp_pool, create_gc_cycles, async_tree_memoization, meteor_contest, asyncio_websockets, django_template, deepcopy, sphinx, xml_etree_iterparse, async_tree_io, async_tree_io_tg, k_core, sqlite_synth, json_dumps, float, telco, djangocms, pylint, mypy2

- Geometric mean (including insignificant results): 1.015x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 0.99x
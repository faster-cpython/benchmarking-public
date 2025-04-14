# Results vs. 3.13.0

- fork: brandtbucher
- ref: unbox
- machine: linux-x86_64
- commit hash: 1baa231
- commit date: 2025-04-01
- overall geometric mean: 1.023x faster
- HPT reliability: 58.87%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.05x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250401-linux-x86_64-brandtbucher-unbox-3.14.0a6+-1baa231 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 270 ms: 1.02x slower                                          |
| docutils       | 2.58 sec                                               | 2.73 sec: 1.06x slower                                        |
| html5lib       | 63.4 ms                                                | 63.9 ms: 1.01x slower                                         |
| Geometric mean | (ref)                                                  | 1.02x slower                                                  |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250401-linux-x86_64-brandtbucher-unbox-3.14.0a6+-1baa231 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 328 ms: 1.41x faster                                          |
| async_tree_memoization     | 437 ms                                                 | 323 ms: 1.35x faster                                          |
| async_tree_io_tg           | 861 ms                                                 | 637 ms: 1.35x faster                                          |
| async_tree_io              | 838 ms                                                 | 634 ms: 1.32x faster                                          |
| async_tree_none            | 350 ms                                                 | 267 ms: 1.31x faster                                          |
| async_tree_none_tg         | 319 ms                                                 | 259 ms: 1.23x faster                                          |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 497 ms: 1.15x faster                                          |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 486 ms: 1.12x faster                                          |
| coroutines                 | 22.2 ms                                                | 20.7 ms: 1.07x faster                                         |
| async_generators           | 433 ms                                                 | 426 ms: 1.02x faster                                          |
| Geometric mean             | (ref)                                                  | 1.20x faster                                                  |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250401-linux-x86_64-brandtbucher-unbox-3.14.0a6+-1baa231 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| float          | 78.7 ms                                                | 69.7 ms: 1.13x faster                                         |
| pidigits       | 186 ms                                                 | 188 ms: 1.01x slower                                          |
| nbody          | 87.7 ms                                                | 91.3 ms: 1.04x slower                                         |
| Geometric mean | (ref)                                                  | 1.02x faster                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250401-linux-x86_64-brandtbucher-unbox-3.14.0a6+-1baa231 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| regex_v8       | 26.9 ms                                                | 22.5 ms: 1.19x faster                                         |
| regex_effbot   | 3.77 ms                                                | 3.19 ms: 1.18x faster                                         |
| regex_dna      | 220 ms                                                 | 215 ms: 1.02x faster                                          |
| regex_compile  | 132 ms                                                 | 133 ms: 1.01x slower                                          |
| Geometric mean | (ref)                                                  | 1.09x faster                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250401-linux-x86_64-brandtbucher-unbox-3.14.0a6+-1baa231 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| tomli_loads          | 2.12 sec                                               | 1.79 sec: 1.18x faster                                        |
| xml_etree_parse      | 154 ms                                                 | 142 ms: 1.09x faster                                          |
| xml_etree_generate   | 86.8 ms                                                | 83.5 ms: 1.04x faster                                         |
| xml_etree_process    | 60.5 ms                                                | 58.8 ms: 1.03x faster                                         |
| xml_etree_iterparse  | 101 ms                                                 | 100 ms: 1.01x faster                                          |
| unpickle_pure_python | 213 us                                                 | 231 us: 1.08x slower                                          |
| pickle_pure_python   | 302 us                                                 | 334 us: 1.11x slower                                          |
| json_dumps           | 10.1 ms                                                | 11.5 ms: 1.13x slower                                         |
| json_loads           | 27.2 us                                                | 31.9 us: 1.17x slower                                         |
| Geometric mean       | (ref)                                                  | 1.02x slower                                                  |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250401-linux-x86_64-brandtbucher-unbox-3.14.0a6+-1baa231 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| python_startup         | 12.7 ms                                                | 13.2 ms: 1.04x slower                                         |
| python_startup_no_site | 7.00 ms                                                | 8.21 ms: 1.17x slower                                         |
| Geometric mean         | (ref)                                                  | 1.10x slower                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250401-linux-x86_64-brandtbucher-unbox-3.14.0a6+-1baa231 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| genshi_text     | 22.6 ms                                                | 21.9 ms: 1.03x faster                                         |
| django_template | 31.7 ms                                                | 33.1 ms: 1.05x slower                                         |
| mako            | 10.7 ms                                                | 11.8 ms: 1.10x slower                                         |
| Geometric mean  | (ref)                                                  | 1.03x slower                                                  |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250401-linux-x86_64-brandtbucher-unbox-3.14.0a6+-1baa231 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| mdp                        | 2.54 sec                                               | 1.27 sec: 2.00x faster                                        |
| async_tree_memoization_tg  | 463 ms                                                 | 328 ms: 1.41x faster                                          |
| async_tree_memoization     | 437 ms                                                 | 323 ms: 1.35x faster                                          |
| async_tree_io_tg           | 861 ms                                                 | 637 ms: 1.35x faster                                          |
| deepcopy                   | 354 us                                                 | 266 us: 1.33x faster                                          |
| async_tree_io              | 838 ms                                                 | 634 ms: 1.32x faster                                          |
| async_tree_none            | 350 ms                                                 | 267 ms: 1.31x faster                                          |
| deepcopy_memo              | 38.4 us                                                | 29.9 us: 1.29x faster                                         |
| richards                   | 47.5 ms                                                | 38.0 ms: 1.25x faster                                         |
| async_tree_none_tg         | 319 ms                                                 | 259 ms: 1.23x faster                                          |
| richards_super             | 53.7 ms                                                | 44.1 ms: 1.22x faster                                         |
| regex_v8                   | 26.9 ms                                                | 22.5 ms: 1.19x faster                                         |
| tomli_loads                | 2.12 sec                                               | 1.79 sec: 1.18x faster                                        |
| regex_effbot               | 3.77 ms                                                | 3.19 ms: 1.18x faster                                         |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 497 ms: 1.15x faster                                          |
| deepcopy_reduce            | 3.24 us                                                | 2.82 us: 1.15x faster                                         |
| spectral_norm              | 113 ms                                                 | 99.5 ms: 1.14x faster                                         |
| float                      | 78.7 ms                                                | 69.7 ms: 1.13x faster                                         |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 486 ms: 1.12x faster                                          |
| scimark_fft                | 367 ms                                                 | 329 ms: 1.11x faster                                          |
| xml_etree_parse            | 154 ms                                                 | 142 ms: 1.09x faster                                          |
| pylint                     | 312 ms                                                 | 287 ms: 1.09x faster                                          |
| coroutines                 | 22.2 ms                                                | 20.7 ms: 1.07x faster                                         |
| dulwich_log                | 64.6 ms                                                | 61.9 ms: 1.04x faster                                         |
| telco                      | 8.40 ms                                                | 8.06 ms: 1.04x faster                                         |
| xml_etree_generate         | 86.8 ms                                                | 83.5 ms: 1.04x faster                                         |
| sqlite_synth               | 2.90 us                                                | 2.79 us: 1.04x faster                                         |
| pathlib                    | 17.4 ms                                                | 16.8 ms: 1.04x faster                                         |
| genshi_text                | 22.6 ms                                                | 21.9 ms: 1.03x faster                                         |
| xml_etree_process          | 60.5 ms                                                | 58.8 ms: 1.03x faster                                         |
| regex_dna                  | 220 ms                                                 | 215 ms: 1.02x faster                                          |
| go                         | 141 ms                                                 | 138 ms: 1.02x faster                                          |
| logging_format             | 6.23 us                                                | 6.12 us: 1.02x faster                                         |
| async_generators           | 433 ms                                                 | 426 ms: 1.02x faster                                          |
| bpe_tokeniser              | 4.69 sec                                               | 4.61 sec: 1.02x faster                                        |
| logging_simple             | 5.65 us                                                | 5.56 us: 1.02x faster                                         |
| xml_etree_iterparse        | 101 ms                                                 | 100 ms: 1.01x faster                                          |
| generators                 | 28.8 ms                                                | 28.5 ms: 1.01x faster                                         |
| pidigits                   | 186 ms                                                 | 188 ms: 1.01x slower                                          |
| html5lib                   | 63.4 ms                                                | 63.9 ms: 1.01x slower                                         |
| regex_compile              | 132 ms                                                 | 133 ms: 1.01x slower                                          |
| sqlalchemy_declarative     | 133 ms                                                 | 135 ms: 1.01x slower                                          |
| chaos                      | 58.0 ms                                                | 58.9 ms: 1.02x slower                                         |
| 2to3                       | 266 ms                                                 | 270 ms: 1.02x slower                                          |
| create_gc_cycles           | 2.45 ms                                                | 2.49 ms: 1.02x slower                                         |
| sympy_sum                  | 150 ms                                                 | 154 ms: 1.02x slower                                          |
| logging_silent             | 101 ns                                                 | 103 ns: 1.02x slower                                          |
| json                       | 5.32 ms                                                | 5.46 ms: 1.03x slower                                         |
| connected_components       | 447 ms                                                 | 459 ms: 1.03x slower                                          |
| sympy_integrate            | 19.8 ms                                                | 20.4 ms: 1.03x slower                                         |
| coverage                   | 82.8 ms                                                | 85.2 ms: 1.03x slower                                         |
| meteor_contest             | 108 ms                                                 | 112 ms: 1.03x slower                                          |
| sympy_str                  | 273 ms                                                 | 281 ms: 1.03x slower                                          |
| gc_traversal               | 4.90 ms                                                | 5.06 ms: 1.03x slower                                         |
| sqlalchemy_imperative      | 16.9 ms                                                | 17.5 ms: 1.03x slower                                         |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 5.21 ms: 1.04x slower                                         |
| python_startup             | 12.7 ms                                                | 13.2 ms: 1.04x slower                                         |
| shortest_path              | 487 ms                                                 | 507 ms: 1.04x slower                                          |
| pycparser                  | 1.20 sec                                               | 1.25 sec: 1.04x slower                                        |
| nbody                      | 87.7 ms                                                | 91.3 ms: 1.04x slower                                         |
| scimark_monte_carlo        | 66.8 ms                                                | 69.8 ms: 1.05x slower                                         |
| deltablue                  | 3.19 ms                                                | 3.34 ms: 1.05x slower                                         |
| django_template            | 31.7 ms                                                | 33.1 ms: 1.05x slower                                         |
| docutils                   | 2.58 sec                                               | 2.73 sec: 1.06x slower                                        |
| sympy_expand               | 456 ms                                                 | 487 ms: 1.07x slower                                          |
| nqueens                    | 80.9 ms                                                | 86.4 ms: 1.07x slower                                         |
| raytrace                   | 262 ms                                                 | 281 ms: 1.07x slower                                          |
| unpickle_pure_python       | 213 us                                                 | 231 us: 1.08x slower                                          |
| scimark_lu                 | 114 ms                                                 | 124 ms: 1.09x slower                                          |
| typing_runtime_protocols   | 160 us                                                 | 174 us: 1.09x slower                                          |
| fannkuch                   | 394 ms                                                 | 431 ms: 1.10x slower                                          |
| bench_thread_pool          | 818 us                                                 | 897 us: 1.10x slower                                          |
| mako                       | 10.7 ms                                                | 11.8 ms: 1.10x slower                                         |
| pprint_pformat             | 1.48 sec                                               | 1.63 sec: 1.10x slower                                        |
| pickle_pure_python         | 302 us                                                 | 334 us: 1.11x slower                                          |
| pprint_safe_repr           | 727 ms                                                 | 805 ms: 1.11x slower                                          |
| json_dumps                 | 10.1 ms                                                | 11.5 ms: 1.13x slower                                         |
| hexiom                     | 6.08 ms                                                | 6.96 ms: 1.15x slower                                         |
| scimark_sor                | 122 ms                                                 | 141 ms: 1.16x slower                                          |
| many_optionals             | 857 us                                                 | 997 us: 1.16x slower                                          |
| crypto_pyaes               | 74.7 ms                                                | 87.4 ms: 1.17x slower                                         |
| python_startup_no_site     | 7.00 ms                                                | 8.21 ms: 1.17x slower                                         |
| json_loads                 | 27.2 us                                                | 31.9 us: 1.17x slower                                         |
| comprehensions             | 16.5 us                                                | 19.6 us: 1.19x slower                                         |
| subparsers                 | 15.5 ms                                                | 21.4 ms: 1.38x slower                                         |
| bench_mp_pool              | 24.0 ms                                                | 83.7 ms: 3.49x slower                                         |
| Geometric mean             | (ref)                                                  | 1.01x faster                                                  |

Benchmark hidden because not significant (5): k_core, genshi_xml, pyflate, asyncio_websockets, sphinx
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
Ignored benchmarks (4) of results/bm-20250401-3.14.0a6+-1baa231-JIT/bm-20250401-linux-x86_64-brandtbucher-unbox-3.14.0a6+-1baa231.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.023x faster

# HPT report

- Reliability score: 58.87% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.05x
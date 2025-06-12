# Results vs. 3.13.0

- fork: brandtbucher
- ref: justin_hot
- machine: linux-aarch64
- commit hash: 858624a
- commit date: 2025-06-12
- overall geometric mean: 1.080x slower
- HPT reliability: 70.73%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250612-arminc-aarch64-brandtbucher-justin_hot-3.15.0a0-858624a |
|----------------|:--------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 313 ms                                                   | 320 ms: 1.02x slower                                                |
| docutils       | 2.96 sec                                                 | 3.15 sec: 1.06x slower                                              |
| html5lib       | 65.6 ms                                                  | 62.5 ms: 1.05x faster                                               |
| Geometric mean | (ref)                                                    | 1.00x slower                                                        |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250612-arminc-aarch64-brandtbucher-justin_hot-3.15.0a0-858624a |
|----------------------------|:--------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_memoization     | 664 ms                                                   | 481 ms: 1.38x faster                                                |
| async_tree_memoization_tg  | 663 ms                                                   | 482 ms: 1.37x faster                                                |
| async_tree_none            | 504 ms                                                   | 406 ms: 1.24x faster                                                |
| async_tree_io_tg           | 1.16 sec                                                 | 945 ms: 1.23x faster                                                |
| async_tree_none_tg         | 484 ms                                                   | 393 ms: 1.23x faster                                                |
| async_tree_io              | 1.14 sec                                                 | 929 ms: 1.23x faster                                                |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 670 ms: 1.20x faster                                                |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 672 ms: 1.17x faster                                                |
| async_generators           | 500 ms                                                   | 485 ms: 1.03x faster                                                |
| Geometric mean             | (ref)                                                    | 1.18x faster                                                        |

Benchmark hidden because not significant (2): asyncio_websockets, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250612-arminc-aarch64-brandtbucher-justin_hot-3.15.0a0-858624a |
|----------------|:--------------------------------------------------------:|:-------------------------------------------------------------------:|
| float          | 95.8 ms                                                  | 89.6 ms: 1.07x faster                                               |
| nbody          | 118 ms                                                   | 145 ms: 1.23x slower                                                |
| Geometric mean | (ref)                                                    | 1.04x slower                                                        |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250612-arminc-aarch64-brandtbucher-justin_hot-3.15.0a0-858624a |
|----------------|:--------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_effbot   | 5.10 ms                                                  | 3.85 ms: 1.33x faster                                               |
| regex_dna      | 263 ms                                                   | 224 ms: 1.17x faster                                                |
| regex_v8       | 32.5 ms                                                  | 28.1 ms: 1.16x faster                                               |
| regex_compile  | 134 ms                                                   | 125 ms: 1.07x faster                                                |
| Geometric mean | (ref)                                                    | 1.18x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250612-arminc-aarch64-brandtbucher-justin_hot-3.15.0a0-858624a |
|----------------------|:--------------------------------------------------------:|:-------------------------------------------------------------------:|
| xml_etree_parse      | 203 ms                                                   | 179 ms: 1.13x faster                                                |
| xml_etree_iterparse  | 159 ms                                                   | 143 ms: 1.11x faster                                                |
| json_dumps           | 14.2 ms                                                  | 13.3 ms: 1.07x faster                                               |
| tomli_loads          | 2.67 sec                                                 | 2.54 sec: 1.05x faster                                              |
| pickle_pure_python   | 374 us                                                   | 407 us: 1.09x slower                                                |
| unpickle_pure_python | 265 us                                                   | 289 us: 1.09x slower                                                |
| Geometric mean       | (ref)                                                    | 1.02x faster                                                        |

Benchmark hidden because not significant (3): xml_etree_generate, json_loads, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250612-arminc-aarch64-brandtbucher-justin_hot-3.15.0a0-858624a |
|----------------|:--------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup | 16.0 ms                                                  | 15.2 ms: 1.06x faster                                               |
| Geometric mean | (ref)                                                    | 1.04x faster                                                        |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250612-arminc-aarch64-brandtbucher-justin_hot-3.15.0a0-858624a |
|----------------|:--------------------------------------------------------:|:-------------------------------------------------------------------:|
| genshi_xml     | 61.6 ms                                                  | 63.0 ms: 1.02x slower                                               |
| mako           | 14.0 ms                                                  | 15.2 ms: 1.09x slower                                               |
| Geometric mean | (ref)                                                    | 1.02x slower                                                        |

Benchmark hidden because not significant (2): genshi_text, django_template

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250612-arminc-aarch64-brandtbucher-justin_hot-3.15.0a0-858624a |
|----------------------------|:--------------------------------------------------------:|:-------------------------------------------------------------------:|
| mdp                        | 3.45 sec                                                 | 1.71 sec: 2.01x faster                                              |
| deepcopy                   | 479 us                                                   | 333 us: 1.44x faster                                                |
| deepcopy_memo              | 53.0 us                                                  | 37.3 us: 1.42x faster                                               |
| async_tree_memoization     | 664 ms                                                   | 481 ms: 1.38x faster                                                |
| async_tree_memoization_tg  | 663 ms                                                   | 482 ms: 1.37x faster                                                |
| regex_effbot               | 5.10 ms                                                  | 3.85 ms: 1.33x faster                                               |
| async_tree_none            | 504 ms                                                   | 406 ms: 1.24x faster                                                |
| async_tree_io_tg           | 1.16 sec                                                 | 945 ms: 1.23x faster                                                |
| async_tree_none_tg         | 484 ms                                                   | 393 ms: 1.23x faster                                                |
| async_tree_io              | 1.14 sec                                                 | 929 ms: 1.23x faster                                                |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 670 ms: 1.20x faster                                                |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 672 ms: 1.17x faster                                                |
| regex_dna                  | 263 ms                                                   | 224 ms: 1.17x faster                                                |
| regex_v8                   | 32.5 ms                                                  | 28.1 ms: 1.16x faster                                               |
| deepcopy_reduce            | 4.24 us                                                  | 3.67 us: 1.16x faster                                               |
| xml_etree_parse            | 203 ms                                                   | 179 ms: 1.13x faster                                                |
| generators                 | 40.3 ms                                                  | 35.7 ms: 1.13x faster                                               |
| scimark_sor                | 164 ms                                                   | 146 ms: 1.13x faster                                                |
| xml_etree_iterparse        | 159 ms                                                   | 143 ms: 1.11x faster                                                |
| richards_super             | 60.8 ms                                                  | 56.2 ms: 1.08x faster                                               |
| regex_compile              | 134 ms                                                   | 125 ms: 1.07x faster                                                |
| float                      | 95.8 ms                                                  | 89.6 ms: 1.07x faster                                               |
| json_dumps                 | 14.2 ms                                                  | 13.3 ms: 1.07x faster                                               |
| python_startup             | 16.0 ms                                                  | 15.2 ms: 1.06x faster                                               |
| richards                   | 54.5 ms                                                  | 51.7 ms: 1.06x faster                                               |
| sqlite_synth               | 4.08 us                                                  | 3.87 us: 1.05x faster                                               |
| json                       | 5.94 ms                                                  | 5.64 ms: 1.05x faster                                               |
| html5lib                   | 65.6 ms                                                  | 62.5 ms: 1.05x faster                                               |
| tomli_loads                | 2.67 sec                                                 | 2.54 sec: 1.05x faster                                              |
| k_core                     | 2.99 sec                                                 | 2.88 sec: 1.04x faster                                              |
| async_generators           | 500 ms                                                   | 485 ms: 1.03x faster                                                |
| bpe_tokeniser              | 6.02 sec                                                 | 5.88 sec: 1.02x faster                                              |
| 2to3                       | 313 ms                                                   | 320 ms: 1.02x slower                                                |
| genshi_xml                 | 61.6 ms                                                  | 63.0 ms: 1.02x slower                                               |
| connected_components       | 547 ms                                                   | 565 ms: 1.03x slower                                                |
| logging_format             | 8.10 us                                                  | 8.41 us: 1.04x slower                                               |
| shortest_path              | 565 ms                                                   | 588 ms: 1.04x slower                                                |
| logging_simple             | 7.25 us                                                  | 7.66 us: 1.06x slower                                               |
| spectral_norm              | 143 ms                                                   | 152 ms: 1.06x slower                                                |
| sympy_str                  | 265 ms                                                   | 281 ms: 1.06x slower                                                |
| docutils                   | 2.96 sec                                                 | 3.15 sec: 1.06x slower                                              |
| scimark_sparse_mat_mult    | 6.66 ms                                                  | 7.08 ms: 1.06x slower                                               |
| sympy_expand               | 472 ms                                                   | 507 ms: 1.07x slower                                                |
| pycparser                  | 1.34 sec                                                 | 1.44 sec: 1.07x slower                                              |
| typing_runtime_protocols   | 197 us                                                   | 214 us: 1.08x slower                                                |
| mako                       | 14.0 ms                                                  | 15.2 ms: 1.09x slower                                               |
| pickle_pure_python         | 374 us                                                   | 407 us: 1.09x slower                                                |
| unpickle_pure_python       | 265 us                                                   | 289 us: 1.09x slower                                                |
| meteor_contest             | 117 ms                                                   | 129 ms: 1.10x slower                                                |
| create_gc_cycles           | 3.39 ms                                                  | 3.74 ms: 1.10x slower                                               |
| raytrace                   | 310 ms                                                   | 343 ms: 1.11x slower                                                |
| gc_traversal               | 5.92 ms                                                  | 6.75 ms: 1.14x slower                                               |
| deltablue                  | 3.97 ms                                                  | 4.59 ms: 1.16x slower                                               |
| go                         | 164 ms                                                   | 195 ms: 1.19x slower                                                |
| comprehensions             | 20.8 us                                                  | 25.1 us: 1.20x slower                                               |
| crypto_pyaes               | 84.9 ms                                                  | 103 ms: 1.21x slower                                                |
| fannkuch                   | 478 ms                                                   | 582 ms: 1.22x slower                                                |
| hexiom                     | 7.34 ms                                                  | 8.98 ms: 1.22x slower                                               |
| nbody                      | 118 ms                                                   | 145 ms: 1.23x slower                                                |
| many_optionals             | 626 us                                                   | 830 us: 1.32x slower                                                |
| subparsers                 | 20.3 ms                                                  | 29.2 ms: 1.43x slower                                               |
| pprint_safe_repr           | 962 ms                                                   | 1.55 sec: 1.62x slower                                              |
| pprint_pformat             | 1.99 sec                                                 | 3.30 sec: 1.66x slower                                              |
| logging_silent             | 135 ns                                                   | 614 ns: 4.56x slower                                                |
| coverage                   | 106 ms                                                   | 578 ms: 5.47x slower                                                |
| thrift                     | 1.01 ms                                                  | 193 ms: 190.75x slower                                              |
| Geometric mean             | (ref)                                                    | 1.09x slower                                                        |

Benchmark hidden because not significant (21): pylint, pathlib, genshi_text, telco, xml_etree_generate, python_startup_no_site, json_loads, scimark_monte_carlo, sphinx, pidigits, sympy_sum, asyncio_websockets, coroutines, sympy_integrate, scimark_fft, chaos, pyflate, xml_etree_process, django_template, nqueens, scimark_lu
Ignored benchmarks (13) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (5) of results/bm-20250612-3.15.0a0-858624a-JIT/bm-20250612-arminc-aarch64-brandtbucher-justin_hot-3.15.0a0-858624a.json: dulwich_log, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.080x slower

# HPT report

- Reliability score: 70.73% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.09x
# Results vs. 3.13.0

- fork: brandtbucher
- ref: jit_targets
- machine: linux-aarch64
- commit hash: aa2b0df
- commit date: 2025-07-07
- overall geometric mean: 1.030x slower
- HPT reliability: 60.77%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250707-arminc-aarch64-brandtbucher-jit_targets-3.15.0a0-aa2b0df |
|----------------|:--------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 313 ms                                                   | 319 ms: 1.02x slower                                                 |
| docutils       | 2.96 sec                                                 | 3.17 sec: 1.07x slower                                               |
| html5lib       | 65.6 ms                                                  | 63.2 ms: 1.04x faster                                                |
| Geometric mean | (ref)                                                    | 1.01x slower                                                         |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250707-arminc-aarch64-brandtbucher-jit_targets-3.15.0a0-aa2b0df |
|----------------------------|:--------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_memoization_tg  | 663 ms                                                   | 482 ms: 1.37x faster                                                 |
| async_tree_memoization     | 664 ms                                                   | 497 ms: 1.34x faster                                                 |
| async_tree_none            | 504 ms                                                   | 398 ms: 1.27x faster                                                 |
| async_tree_io_tg           | 1.16 sec                                                 | 926 ms: 1.26x faster                                                 |
| async_tree_none_tg         | 484 ms                                                   | 389 ms: 1.24x faster                                                 |
| async_tree_io              | 1.14 sec                                                 | 930 ms: 1.23x faster                                                 |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 672 ms: 1.19x faster                                                 |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 685 ms: 1.15x faster                                                 |
| Geometric mean             | (ref)                                                    | 1.18x faster                                                         |

Benchmark hidden because not significant (3): asyncio_websockets, async_generators, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250707-arminc-aarch64-brandtbucher-jit_targets-3.15.0a0-aa2b0df |
|----------------|:--------------------------------------------------------:|:--------------------------------------------------------------------:|
| float          | 95.8 ms                                                  | 89.0 ms: 1.08x faster                                                |
| nbody          | 118 ms                                                   | 143 ms: 1.21x slower                                                 |
| Geometric mean | (ref)                                                    | 1.04x slower                                                         |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250707-arminc-aarch64-brandtbucher-jit_targets-3.15.0a0-aa2b0df |
|----------------|:--------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_effbot   | 5.10 ms                                                  | 3.76 ms: 1.36x faster                                                |
| regex_v8       | 32.5 ms                                                  | 26.2 ms: 1.24x faster                                                |
| regex_dna      | 263 ms                                                   | 220 ms: 1.20x faster                                                 |
| regex_compile  | 134 ms                                                   | 126 ms: 1.06x faster                                                 |
| Geometric mean | (ref)                                                    | 1.21x faster                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250707-arminc-aarch64-brandtbucher-jit_targets-3.15.0a0-aa2b0df |
|----------------------|:--------------------------------------------------------:|:--------------------------------------------------------------------:|
| xml_etree_parse      | 203 ms                                                   | 178 ms: 1.14x faster                                                 |
| xml_etree_iterparse  | 159 ms                                                   | 146 ms: 1.09x faster                                                 |
| tomli_loads          | 2.67 sec                                                 | 2.57 sec: 1.04x faster                                               |
| unpickle_pure_python | 265 us                                                   | 299 us: 1.13x slower                                                 |
| pickle_pure_python   | 374 us                                                   | 427 us: 1.14x slower                                                 |
| Geometric mean       | (ref)                                                    | 1.01x faster                                                         |

Benchmark hidden because not significant (4): json_dumps, xml_etree_generate, xml_etree_process, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250707-arminc-aarch64-brandtbucher-jit_targets-3.15.0a0-aa2b0df |
|----------------|:--------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup | 16.0 ms                                                  | 15.2 ms: 1.05x faster                                                |
| Geometric mean | (ref)                                                    | 1.03x faster                                                         |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250707-arminc-aarch64-brandtbucher-jit_targets-3.15.0a0-aa2b0df |
|-----------------|:--------------------------------------------------------:|:--------------------------------------------------------------------:|
| django_template | 39.4 ms                                                  | 40.9 ms: 1.04x slower                                                |
| genshi_xml      | 61.6 ms                                                  | 65.8 ms: 1.07x slower                                                |
| mako            | 14.0 ms                                                  | 15.2 ms: 1.09x slower                                                |
| Geometric mean  | (ref)                                                    | 1.04x slower                                                         |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250707-arminc-aarch64-brandtbucher-jit_targets-3.15.0a0-aa2b0df |
|----------------------------|:--------------------------------------------------------:|:--------------------------------------------------------------------:|
| mdp                        | 3.45 sec                                                 | 1.66 sec: 2.08x faster                                               |
| deepcopy                   | 479 us                                                   | 337 us: 1.42x faster                                                 |
| deepcopy_memo              | 53.0 us                                                  | 37.8 us: 1.40x faster                                                |
| async_tree_memoization_tg  | 663 ms                                                   | 482 ms: 1.37x faster                                                 |
| regex_effbot               | 5.10 ms                                                  | 3.76 ms: 1.36x faster                                                |
| async_tree_memoization     | 664 ms                                                   | 497 ms: 1.34x faster                                                 |
| async_tree_none            | 504 ms                                                   | 398 ms: 1.27x faster                                                 |
| async_tree_io_tg           | 1.16 sec                                                 | 926 ms: 1.26x faster                                                 |
| async_tree_none_tg         | 484 ms                                                   | 389 ms: 1.24x faster                                                 |
| regex_v8                   | 32.5 ms                                                  | 26.2 ms: 1.24x faster                                                |
| async_tree_io              | 1.14 sec                                                 | 930 ms: 1.23x faster                                                 |
| regex_dna                  | 263 ms                                                   | 220 ms: 1.20x faster                                                 |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 672 ms: 1.19x faster                                                 |
| deepcopy_reduce            | 4.24 us                                                  | 3.59 us: 1.18x faster                                                |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 685 ms: 1.15x faster                                                 |
| xml_etree_parse            | 203 ms                                                   | 178 ms: 1.14x faster                                                 |
| scimark_sor                | 164 ms                                                   | 145 ms: 1.14x faster                                                 |
| generators                 | 40.3 ms                                                  | 35.5 ms: 1.14x faster                                                |
| xml_etree_iterparse        | 159 ms                                                   | 146 ms: 1.09x faster                                                 |
| float                      | 95.8 ms                                                  | 89.0 ms: 1.08x faster                                                |
| richards                   | 54.5 ms                                                  | 51.0 ms: 1.07x faster                                                |
| logging_format             | 8.10 us                                                  | 7.62 us: 1.06x faster                                                |
| sqlite_synth               | 4.08 us                                                  | 3.85 us: 1.06x faster                                                |
| regex_compile              | 134 ms                                                   | 126 ms: 1.06x faster                                                 |
| python_startup             | 16.0 ms                                                  | 15.2 ms: 1.05x faster                                                |
| richards_super             | 60.8 ms                                                  | 58.1 ms: 1.05x faster                                                |
| tomli_loads                | 2.67 sec                                                 | 2.57 sec: 1.04x faster                                               |
| html5lib                   | 65.6 ms                                                  | 63.2 ms: 1.04x faster                                                |
| scimark_fft                | 463 ms                                                   | 447 ms: 1.03x faster                                                 |
| logging_silent             | 135 ns                                                   | 130 ns: 1.03x faster                                                 |
| k_core                     | 2.99 sec                                                 | 2.90 sec: 1.03x faster                                               |
| bpe_tokeniser              | 6.02 sec                                                 | 5.89 sec: 1.02x faster                                               |
| djangocms                  | 66.2 us                                                  | 65.0 us: 1.02x faster                                                |
| 2to3                       | 313 ms                                                   | 319 ms: 1.02x slower                                                 |
| pyflate                    | 582 ms                                                   | 596 ms: 1.02x slower                                                 |
| django_template            | 39.4 ms                                                  | 40.9 ms: 1.04x slower                                                |
| connected_components       | 547 ms                                                   | 574 ms: 1.05x slower                                                 |
| genshi_xml                 | 61.6 ms                                                  | 65.8 ms: 1.07x slower                                                |
| docutils                   | 2.96 sec                                                 | 3.17 sec: 1.07x slower                                               |
| pycparser                  | 1.34 sec                                                 | 1.44 sec: 1.07x slower                                               |
| sympy_expand               | 472 ms                                                   | 507 ms: 1.07x slower                                                 |
| shortest_path              | 565 ms                                                   | 611 ms: 1.08x slower                                                 |
| sympy_str                  | 265 ms                                                   | 288 ms: 1.09x slower                                                 |
| mako                       | 14.0 ms                                                  | 15.2 ms: 1.09x slower                                                |
| meteor_contest             | 117 ms                                                   | 128 ms: 1.10x slower                                                 |
| raytrace                   | 310 ms                                                   | 343 ms: 1.11x slower                                                 |
| create_gc_cycles           | 3.39 ms                                                  | 3.79 ms: 1.12x slower                                                |
| typing_runtime_protocols   | 197 us                                                   | 221 us: 1.12x slower                                                 |
| scimark_sparse_mat_mult    | 6.66 ms                                                  | 7.52 ms: 1.13x slower                                                |
| unpickle_pure_python       | 265 us                                                   | 299 us: 1.13x slower                                                 |
| pickle_pure_python         | 374 us                                                   | 427 us: 1.14x slower                                                 |
| gc_traversal               | 5.92 ms                                                  | 6.79 ms: 1.15x slower                                                |
| deltablue                  | 3.97 ms                                                  | 4.55 ms: 1.15x slower                                                |
| fannkuch                   | 478 ms                                                   | 567 ms: 1.19x slower                                                 |
| go                         | 164 ms                                                   | 198 ms: 1.21x slower                                                 |
| nbody                      | 118 ms                                                   | 143 ms: 1.21x slower                                                 |
| comprehensions             | 20.8 us                                                  | 25.3 us: 1.21x slower                                                |
| hexiom                     | 7.34 ms                                                  | 9.22 ms: 1.26x slower                                                |
| crypto_pyaes               | 84.9 ms                                                  | 108 ms: 1.27x slower                                                 |
| many_optionals             | 626 us                                                   | 809 us: 1.29x slower                                                 |
| pprint_pformat             | 1.99 sec                                                 | 2.84 sec: 1.43x slower                                               |
| subparsers                 | 20.3 ms                                                  | 29.4 ms: 1.44x slower                                                |
| pprint_safe_repr           | 962 ms                                                   | 1.39 sec: 1.44x slower                                               |
| telco                      | 10.5 ms                                                  | 166 ms: 15.90x slower                                                |
| Geometric mean             | (ref)                                                    | 1.02x slower                                                         |

Benchmark hidden because not significant (24): pylint, pathlib, json_dumps, thrift, json, logging_simple, coverage, xml_etree_generate, genshi_text, sphinx, chaos, asyncio_websockets, async_generators, spectral_norm, xml_etree_process, python_startup_no_site, pidigits, sympy_sum, json_loads, sympy_integrate, scimark_monte_carlo, nqueens, scimark_lu, coroutines
Ignored benchmarks (12) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: bench_mp_pool, bench_thread_pool, chameleon, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (5) of results/bm-20250707-3.15.0a0-aa2b0df-JIT/bm-20250707-arminc-aarch64-brandtbucher-jit_targets-3.15.0a0-aa2b0df.json: dulwich_log, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.030x slower

# HPT report

- Reliability score: 60.77% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.10x
# Results vs. 3.13.0

- fork: Fidget-Spinner
- ref: disable_tailcall
- machine: linux-aarch64
- commit hash: da5ad58
- commit date: 2025-02-25
- overall geometric mean: 1.063x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x slower
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250225-arminc-aarch64-Fidget%2dSpinner-disable_tailcall-3.14.0a5+-da5ad58 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 313 ms                                                   | 337 ms: 1.08x slower                                                           |
| docutils       | 2.96 sec                                                 | 3.16 sec: 1.07x slower                                                         |
| html5lib       | 65.6 ms                                                  | 70.3 ms: 1.07x slower                                                          |
| Geometric mean | (ref)                                                    | 1.06x slower                                                                   |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250225-arminc-aarch64-Fidget%2dSpinner-disable_tailcall-3.14.0a5+-da5ad58 |
|----------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 663 ms                                                   | 529 ms: 1.25x faster                                                           |
| async_tree_memoization     | 664 ms                                                   | 534 ms: 1.24x faster                                                           |
| async_tree_io_tg           | 1.16 sec                                                 | 993 ms: 1.17x faster                                                           |
| async_tree_none            | 504 ms                                                   | 434 ms: 1.16x faster                                                           |
| async_tree_none_tg         | 484 ms                                                   | 422 ms: 1.15x faster                                                           |
| async_tree_io              | 1.14 sec                                                 | 999 ms: 1.14x faster                                                           |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 761 ms: 1.05x faster                                                           |
| async_generators           | 500 ms                                                   | 484 ms: 1.03x faster                                                           |
| coroutines                 | 29.4 ms                                                  | 32.4 ms: 1.10x slower                                                          |
| Geometric mean             | (ref)                                                    | 1.09x faster                                                                   |

Benchmark hidden because not significant (2): async_tree_cpu_io_mixed, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250225-arminc-aarch64-Fidget%2dSpinner-disable_tailcall-3.14.0a5+-da5ad58 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------------:|
| float          | 95.8 ms                                                  | 100 ms: 1.05x slower                                                           |
| nbody          | 118 ms                                                   | 145 ms: 1.23x slower                                                           |
| pidigits       | 238 ms                                                   | 310 ms: 1.30x slower                                                           |
| Geometric mean | (ref)                                                    | 1.19x slower                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250225-arminc-aarch64-Fidget%2dSpinner-disable_tailcall-3.14.0a5+-da5ad58 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_effbot   | 5.10 ms                                                  | 4.20 ms: 1.21x faster                                                          |
| regex_dna      | 263 ms                                                   | 244 ms: 1.08x faster                                                           |
| regex_v8       | 32.5 ms                                                  | 35.4 ms: 1.09x slower                                                          |
| regex_compile  | 134 ms                                                   | 156 ms: 1.17x slower                                                           |
| Geometric mean | (ref)                                                    | 1.01x faster                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250225-arminc-aarch64-Fidget%2dSpinner-disable_tailcall-3.14.0a5+-da5ad58 |
|----------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------------:|
| xml_etree_parse      | 203 ms                                                   | 216 ms: 1.07x slower                                                           |
| json_loads           | 32.8 us                                                  | 36.6 us: 1.12x slower                                                          |
| json_dumps           | 14.2 ms                                                  | 15.9 ms: 1.12x slower                                                          |
| xml_etree_process    | 82.1 ms                                                  | 92.9 ms: 1.13x slower                                                          |
| tomli_loads          | 2.67 sec                                                 | 3.26 sec: 1.22x slower                                                         |
| pickle_pure_python   | 374 us                                                   | 465 us: 1.24x slower                                                           |
| unpickle_pure_python | 265 us                                                   | 333 us: 1.26x slower                                                           |
| Geometric mean       | (ref)                                                    | 1.14x slower                                                                   |

Benchmark hidden because not significant (2): xml_etree_iterparse, xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250225-arminc-aarch64-Fidget%2dSpinner-disable_tailcall-3.14.0a5+-da5ad58 |
|------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup         | 16.0 ms                                                  | 16.9 ms: 1.05x slower                                                          |
| python_startup_no_site | 8.79 ms                                                  | 9.39 ms: 1.07x slower                                                          |
| Geometric mean         | (ref)                                                    | 1.06x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250225-arminc-aarch64-Fidget%2dSpinner-disable_tailcall-3.14.0a5+-da5ad58 |
|-----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako            | 14.0 ms                                                  | 16.0 ms: 1.15x slower                                                          |
| django_template | 39.4 ms                                                  | 45.5 ms: 1.15x slower                                                          |
| genshi_text     | 28.6 ms                                                  | 33.7 ms: 1.18x slower                                                          |
| genshi_xml      | 61.6 ms                                                  | 73.1 ms: 1.19x slower                                                          |
| Geometric mean  | (ref)                                                    | 1.17x slower                                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250225-arminc-aarch64-Fidget%2dSpinner-disable_tailcall-3.14.0a5+-da5ad58 |
|----------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------------:|
| deepcopy                   | 479 us                                                   | 379 us: 1.26x faster                                                           |
| async_tree_memoization_tg  | 663 ms                                                   | 529 ms: 1.25x faster                                                           |
| async_tree_memoization     | 664 ms                                                   | 534 ms: 1.24x faster                                                           |
| regex_effbot               | 5.10 ms                                                  | 4.20 ms: 1.21x faster                                                          |
| async_tree_io_tg           | 1.16 sec                                                 | 993 ms: 1.17x faster                                                           |
| async_tree_none            | 504 ms                                                   | 434 ms: 1.16x faster                                                           |
| async_tree_none_tg         | 484 ms                                                   | 422 ms: 1.15x faster                                                           |
| spectral_norm              | 143 ms                                                   | 125 ms: 1.15x faster                                                           |
| async_tree_io              | 1.14 sec                                                 | 999 ms: 1.14x faster                                                           |
| deepcopy_memo              | 53.0 us                                                  | 47.8 us: 1.11x faster                                                          |
| regex_dna                  | 263 ms                                                   | 244 ms: 1.08x faster                                                           |
| scimark_sparse_mat_mult    | 6.66 ms                                                  | 6.25 ms: 1.07x faster                                                          |
| pylint                     | 345 ms                                                   | 324 ms: 1.07x faster                                                           |
| deepcopy_reduce            | 4.24 us                                                  | 4.03 us: 1.05x faster                                                          |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 761 ms: 1.05x faster                                                           |
| async_generators           | 500 ms                                                   | 484 ms: 1.03x faster                                                           |
| bpe_tokeniser              | 6.02 sec                                                 | 6.13 sec: 1.02x slower                                                         |
| connected_components       | 547 ms                                                   | 561 ms: 1.03x slower                                                           |
| shortest_path              | 565 ms                                                   | 582 ms: 1.03x slower                                                           |
| sqlite_synth               | 4.08 us                                                  | 4.26 us: 1.04x slower                                                          |
| float                      | 95.8 ms                                                  | 100 ms: 1.05x slower                                                           |
| python_startup             | 16.0 ms                                                  | 16.9 ms: 1.05x slower                                                          |
| docutils                   | 2.96 sec                                                 | 3.16 sec: 1.07x slower                                                         |
| python_startup_no_site     | 8.79 ms                                                  | 9.39 ms: 1.07x slower                                                          |
| go                         | 164 ms                                                   | 175 ms: 1.07x slower                                                           |
| xml_etree_parse            | 203 ms                                                   | 216 ms: 1.07x slower                                                           |
| json                       | 5.94 ms                                                  | 6.34 ms: 1.07x slower                                                          |
| html5lib                   | 65.6 ms                                                  | 70.3 ms: 1.07x slower                                                          |
| pycparser                  | 1.34 sec                                                 | 1.44 sec: 1.07x slower                                                         |
| comprehensions             | 20.8 us                                                  | 22.4 us: 1.08x slower                                                          |
| 2to3                       | 313 ms                                                   | 337 ms: 1.08x slower                                                           |
| sqlalchemy_imperative      | 16.1 ms                                                  | 17.4 ms: 1.08x slower                                                          |
| sqlglot_optimize           | 65.2 ms                                                  | 70.4 ms: 1.08x slower                                                          |
| regex_v8                   | 32.5 ms                                                  | 35.4 ms: 1.09x slower                                                          |
| pyflate                    | 582 ms                                                   | 633 ms: 1.09x slower                                                           |
| logging_silent             | 135 ns                                                   | 147 ns: 1.09x slower                                                           |
| sympy_integrate            | 21.4 ms                                                  | 23.5 ms: 1.10x slower                                                          |
| typing_runtime_protocols   | 197 us                                                   | 217 us: 1.10x slower                                                           |
| coroutines                 | 29.4 ms                                                  | 32.4 ms: 1.10x slower                                                          |
| logging_format             | 8.10 us                                                  | 9.02 us: 1.11x slower                                                          |
| json_loads                 | 32.8 us                                                  | 36.6 us: 1.12x slower                                                          |
| create_gc_cycles           | 3.39 ms                                                  | 3.79 ms: 1.12x slower                                                          |
| json_dumps                 | 14.2 ms                                                  | 15.9 ms: 1.12x slower                                                          |
| meteor_contest             | 117 ms                                                   | 131 ms: 1.12x slower                                                           |
| sympy_expand               | 472 ms                                                   | 532 ms: 1.13x slower                                                           |
| scimark_sor                | 164 ms                                                   | 185 ms: 1.13x slower                                                           |
| richards                   | 54.5 ms                                                  | 61.6 ms: 1.13x slower                                                          |
| xml_etree_process          | 82.1 ms                                                  | 92.9 ms: 1.13x slower                                                          |
| sqlglot_transpile          | 1.84 ms                                                  | 2.09 ms: 1.14x slower                                                          |
| nqueens                    | 105 ms                                                   | 120 ms: 1.14x slower                                                           |
| sympy_str                  | 265 ms                                                   | 303 ms: 1.14x slower                                                           |
| gc_traversal               | 5.92 ms                                                  | 6.79 ms: 1.15x slower                                                          |
| mako                       | 14.0 ms                                                  | 16.0 ms: 1.15x slower                                                          |
| logging_simple             | 7.25 us                                                  | 8.33 us: 1.15x slower                                                          |
| sqlglot_normalize          | 131 ms                                                   | 151 ms: 1.15x slower                                                           |
| django_template            | 39.4 ms                                                  | 45.5 ms: 1.15x slower                                                          |
| scimark_monte_carlo        | 87.8 ms                                                  | 101 ms: 1.15x slower                                                           |
| chaos                      | 70.7 ms                                                  | 82.2 ms: 1.16x slower                                                          |
| pprint_pformat             | 1.99 sec                                                 | 2.32 sec: 1.17x slower                                                         |
| regex_compile              | 134 ms                                                   | 156 ms: 1.17x slower                                                           |
| scimark_lu                 | 146 ms                                                   | 172 ms: 1.17x slower                                                           |
| genshi_text                | 28.6 ms                                                  | 33.7 ms: 1.18x slower                                                          |
| pprint_safe_repr           | 962 ms                                                   | 1.14 sec: 1.18x slower                                                         |
| raytrace                   | 310 ms                                                   | 368 ms: 1.19x slower                                                           |
| genshi_xml                 | 61.6 ms                                                  | 73.1 ms: 1.19x slower                                                          |
| crypto_pyaes               | 84.9 ms                                                  | 101 ms: 1.19x slower                                                           |
| richards_super             | 60.8 ms                                                  | 73.0 ms: 1.20x slower                                                          |
| generators                 | 40.3 ms                                                  | 48.5 ms: 1.20x slower                                                          |
| deltablue                  | 3.97 ms                                                  | 4.82 ms: 1.22x slower                                                          |
| tomli_loads                | 2.67 sec                                                 | 3.26 sec: 1.22x slower                                                         |
| sqlglot_parse              | 1.43 ms                                                  | 1.76 ms: 1.23x slower                                                          |
| nbody                      | 118 ms                                                   | 145 ms: 1.23x slower                                                           |
| hexiom                     | 7.34 ms                                                  | 9.10 ms: 1.24x slower                                                          |
| pickle_pure_python         | 374 us                                                   | 465 us: 1.24x slower                                                           |
| unpickle_pure_python       | 265 us                                                   | 333 us: 1.26x slower                                                           |
| pidigits                   | 238 ms                                                   | 310 ms: 1.30x slower                                                           |
| fannkuch                   | 478 ms                                                   | 624 ms: 1.31x slower                                                           |
| subparsers                 | 20.3 ms                                                  | 30.6 ms: 1.51x slower                                                          |
| many_optionals             | 626 us                                                   | 963 us: 1.54x slower                                                           |
| bench_mp_pool              | 8.07 ms                                                  | 8.30 sec: 1028.74x slower                                                      |
| Geometric mean             | (ref)                                                    | 1.15x slower                                                                   |

Benchmark hidden because not significant (15): pathlib, telco, scimark_fft, coverage, k_core, async_tree_cpu_io_mixed, sqlalchemy_declarative, mdp, asyncio_websockets, sphinx, xml_etree_iterparse, bench_thread_pool, xml_etree_generate, sympy_sum, thrift
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
Ignored benchmarks (1) of results/bm-20250225-3.14.0a5+-da5ad58-CLANG/bm-20250225-arminc-aarch64-Fidget%2dSpinner-disable_tailcall-3.14.0a5+-da5ad58.json: dulwich_log

- Geometric mean (including insignificant results): 1.063x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.04x
- 95% likely to have a slowdown of 1.04x
- 99% likely to have a slowdown of 1.03x

# Memory
- memory change: 1.08x
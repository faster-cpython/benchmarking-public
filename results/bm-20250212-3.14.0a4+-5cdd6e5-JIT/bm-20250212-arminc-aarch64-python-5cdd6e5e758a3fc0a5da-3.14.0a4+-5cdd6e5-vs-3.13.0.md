# Results vs. 3.13.0

- fork: python
- ref: 5cdd6e5e758a3fc0a5da
- machine: linux-aarch64
- commit hash: 5cdd6e5
- commit date: 2025-02-12
- overall geometric mean: 1.005x faster
- HPT reliability: 87.03%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250212-arminc-aarch64-python-5cdd6e5e758a3fc0a5da-3.14.0a4+-5cdd6e5 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| docutils       | 2.96 sec                                                 | 3.26 sec: 1.10x slower                                                   |
| Geometric mean | (ref)                                                    | 1.02x slower                                                             |

Benchmark hidden because not significant (3): 2to3, html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250212-arminc-aarch64-python-5cdd6e5e758a3fc0a5da-3.14.0a4+-5cdd6e5 |
|----------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization     | 664 ms                                                   | 515 ms: 1.29x faster                                                     |
| async_tree_memoization_tg  | 663 ms                                                   | 517 ms: 1.28x faster                                                     |
| async_tree_none            | 504 ms                                                   | 401 ms: 1.26x faster                                                     |
| async_tree_none_tg         | 484 ms                                                   | 393 ms: 1.23x faster                                                     |
| async_tree_io_tg           | 1.16 sec                                                 | 946 ms: 1.23x faster                                                     |
| async_tree_io              | 1.14 sec                                                 | 939 ms: 1.21x faster                                                     |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 683 ms: 1.17x faster                                                     |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 701 ms: 1.13x faster                                                     |
| async_generators           | 500 ms                                                   | 482 ms: 1.04x faster                                                     |
| Geometric mean             | (ref)                                                    | 1.16x faster                                                             |

Benchmark hidden because not significant (2): coroutines, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250212-arminc-aarch64-python-5cdd6e5e758a3fc0a5da-3.14.0a4+-5cdd6e5 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 95.8 ms                                                  | 85.4 ms: 1.12x faster                                                    |
| nbody          | 118 ms                                                   | 129 ms: 1.09x slower                                                     |
| Geometric mean | (ref)                                                    | 1.01x faster                                                             |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250212-arminc-aarch64-python-5cdd6e5e758a3fc0a5da-3.14.0a4+-5cdd6e5 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_effbot   | 5.10 ms                                                  | 3.91 ms: 1.30x faster                                                    |
| regex_dna      | 263 ms                                                   | 244 ms: 1.08x faster                                                     |
| Geometric mean | (ref)                                                    | 1.10x faster                                                             |

Benchmark hidden because not significant (2): regex_compile, regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250212-arminc-aarch64-python-5cdd6e5e758a3fc0a5da-3.14.0a4+-5cdd6e5 |
|---------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| xml_etree_parse     | 203 ms                                                   | 179 ms: 1.13x faster                                                     |
| xml_etree_iterparse | 159 ms                                                   | 147 ms: 1.08x faster                                                     |
| tomli_loads         | 2.67 sec                                                 | 2.54 sec: 1.05x faster                                                   |
| json_loads          | 32.8 us                                                  | 35.1 us: 1.07x slower                                                    |
| pickle_pure_python  | 374 us                                                   | 416 us: 1.11x slower                                                     |
| Geometric mean      | (ref)                                                    | 1.01x faster                                                             |

Benchmark hidden because not significant (4): xml_etree_generate, xml_etree_process, json_dumps, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250212-arminc-aarch64-python-5cdd6e5e758a3fc0a5da-3.14.0a4+-5cdd6e5 |
|------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 8.79 ms                                                  | 9.05 ms: 1.03x slower                                                    |
| Geometric mean         | (ref)                                                    | 1.02x slower                                                             |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250212-arminc-aarch64-python-5cdd6e5e758a3fc0a5da-3.14.0a4+-5cdd6e5 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| genshi_xml     | 61.6 ms                                                  | 67.4 ms: 1.09x slower                                                    |
| Geometric mean | (ref)                                                    | 1.02x slower                                                             |

Benchmark hidden because not significant (3): mako, django_template, genshi_text

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250212-arminc-aarch64-python-5cdd6e5e758a3fc0a5da-3.14.0a4+-5cdd6e5 |
|----------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| deepcopy                   | 479 us                                                   | 342 us: 1.40x faster                                                     |
| deepcopy_memo              | 53.0 us                                                  | 39.4 us: 1.34x faster                                                    |
| regex_effbot               | 5.10 ms                                                  | 3.91 ms: 1.30x faster                                                    |
| async_tree_memoization     | 664 ms                                                   | 515 ms: 1.29x faster                                                     |
| async_tree_memoization_tg  | 663 ms                                                   | 517 ms: 1.28x faster                                                     |
| async_tree_none            | 504 ms                                                   | 401 ms: 1.26x faster                                                     |
| async_tree_none_tg         | 484 ms                                                   | 393 ms: 1.23x faster                                                     |
| async_tree_io_tg           | 1.16 sec                                                 | 946 ms: 1.23x faster                                                     |
| spectral_norm              | 143 ms                                                   | 118 ms: 1.21x faster                                                     |
| deepcopy_reduce            | 4.24 us                                                  | 3.50 us: 1.21x faster                                                    |
| async_tree_io              | 1.14 sec                                                 | 939 ms: 1.21x faster                                                     |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 683 ms: 1.17x faster                                                     |
| xml_etree_parse            | 203 ms                                                   | 179 ms: 1.13x faster                                                     |
| pathlib                    | 24.3 ms                                                  | 21.5 ms: 1.13x faster                                                    |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 701 ms: 1.13x faster                                                     |
| float                      | 95.8 ms                                                  | 85.4 ms: 1.12x faster                                                    |
| generators                 | 40.3 ms                                                  | 36.6 ms: 1.10x faster                                                    |
| scimark_fft                | 463 ms                                                   | 423 ms: 1.09x faster                                                     |
| xml_etree_iterparse        | 159 ms                                                   | 147 ms: 1.08x faster                                                     |
| regex_dna                  | 263 ms                                                   | 244 ms: 1.08x faster                                                     |
| pylint                     | 345 ms                                                   | 322 ms: 1.07x faster                                                     |
| scimark_sor                | 164 ms                                                   | 153 ms: 1.07x faster                                                     |
| coverage                   | 106 ms                                                   | 99.7 ms: 1.06x faster                                                    |
| bpe_tokeniser              | 6.02 sec                                                 | 5.70 sec: 1.05x faster                                                   |
| tomli_loads                | 2.67 sec                                                 | 2.54 sec: 1.05x faster                                                   |
| richards_super             | 60.8 ms                                                  | 58.2 ms: 1.04x faster                                                    |
| async_generators           | 500 ms                                                   | 482 ms: 1.04x faster                                                     |
| richards                   | 54.5 ms                                                  | 52.7 ms: 1.03x faster                                                    |
| sqlite_synth               | 4.08 us                                                  | 3.97 us: 1.03x faster                                                    |
| mdp                        | 3.45 sec                                                 | 3.54 sec: 1.03x slower                                                   |
| python_startup_no_site     | 8.79 ms                                                  | 9.05 ms: 1.03x slower                                                    |
| shortest_path              | 565 ms                                                   | 586 ms: 1.04x slower                                                     |
| deltablue                  | 3.97 ms                                                  | 4.22 ms: 1.06x slower                                                    |
| pycparser                  | 1.34 sec                                                 | 1.43 sec: 1.07x slower                                                   |
| sympy_expand               | 472 ms                                                   | 504 ms: 1.07x slower                                                     |
| sympy_integrate            | 21.4 ms                                                  | 22.9 ms: 1.07x slower                                                    |
| create_gc_cycles           | 3.39 ms                                                  | 3.63 ms: 1.07x slower                                                    |
| json_loads                 | 32.8 us                                                  | 35.1 us: 1.07x slower                                                    |
| meteor_contest             | 117 ms                                                   | 127 ms: 1.08x slower                                                     |
| sympy_str                  | 265 ms                                                   | 287 ms: 1.08x slower                                                     |
| raytrace                   | 310 ms                                                   | 336 ms: 1.08x slower                                                     |
| nbody                      | 118 ms                                                   | 129 ms: 1.09x slower                                                     |
| genshi_xml                 | 61.6 ms                                                  | 67.4 ms: 1.09x slower                                                    |
| docutils                   | 2.96 sec                                                 | 3.26 sec: 1.10x slower                                                   |
| pickle_pure_python         | 374 us                                                   | 416 us: 1.11x slower                                                     |
| sqlglot_parse              | 1.43 ms                                                  | 1.60 ms: 1.11x slower                                                    |
| typing_runtime_protocols   | 197 us                                                   | 221 us: 1.12x slower                                                     |
| fannkuch                   | 478 ms                                                   | 539 ms: 1.13x slower                                                     |
| crypto_pyaes               | 84.9 ms                                                  | 98.2 ms: 1.16x slower                                                    |
| comprehensions             | 20.8 us                                                  | 24.6 us: 1.18x slower                                                    |
| gc_traversal               | 5.92 ms                                                  | 7.12 ms: 1.20x slower                                                    |
| nqueens                    | 105 ms                                                   | 127 ms: 1.21x slower                                                     |
| hexiom                     | 7.34 ms                                                  | 9.00 ms: 1.23x slower                                                    |
| subparsers                 | 20.3 ms                                                  | 26.3 ms: 1.29x slower                                                    |
| pprint_pformat             | 1.99 sec                                                 | 2.78 sec: 1.40x slower                                                   |
| pprint_safe_repr           | 962 ms                                                   | 1.35 sec: 1.40x slower                                                   |
| many_optionals             | 626 us                                                   | 883 us: 1.41x slower                                                     |
| bench_mp_pool              | 8.07 ms                                                  | 2.59 sec: 321.34x slower                                                 |
| Geometric mean             | (ref)                                                    | 1.06x slower                                                             |

Benchmark hidden because not significant (37): xml_etree_generate, scimark_lu, regex_compile, telco, chaos, logging_format, mako, scimark_monte_carlo, regex_v8, sphinx, pyflate, sqlalchemy_declarative, sqlalchemy_imperative, html5lib, coroutines, xml_etree_process, k_core, asyncio_websockets, thrift, logging_simple, sympy_sum, django_template, bench_thread_pool, 2to3, pidigits, sqlglot_normalize, connected_components, python_startup, genshi_text, go, scimark_sparse_mat_mult, json_dumps, json, unpickle_pure_python, sqlglot_optimize, sqlglot_transpile, logging_silent
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
Ignored benchmarks (1) of results/bm-20250212-3.14.0a4+-5cdd6e5-JIT/bm-20250212-arminc-aarch64-python-5cdd6e5e758a3fc0a5da-3.14.0a4+-5cdd6e5.json: dulwich_log

- Geometric mean (including insignificant results): 1.005x faster

# HPT report

- Reliability score: 87.03% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.04x
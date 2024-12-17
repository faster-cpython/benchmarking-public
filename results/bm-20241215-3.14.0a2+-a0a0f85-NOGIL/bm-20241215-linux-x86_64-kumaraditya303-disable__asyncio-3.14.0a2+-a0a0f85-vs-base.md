# Results vs. base

- fork: kumaraditya303
- ref: disable__asyncio
- machine: linux-x86_64
- commit hash: a0a0f85
- commit date: 2024-12-15
- overall geometric mean: 1.050x slower
- HPT reliability: 77.77%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.12x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241213-linux-x86_64-python-11ff3286b7e821bf439b-3.14.0a2+-11ff328 | bm-20241215-linux-x86_64-kumaraditya303-disable__asyncio-3.14.0a2+-a0a0f85 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| html5lib       | 90.2 ms                                                                | 92.3 ms: 1.02x slower                                                      |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                               |

Benchmark hidden because not significant (3): 2to3, docutils, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241213-linux-x86_64-python-11ff3286b7e821bf439b-3.14.0a2+-11ff328 | bm-20241215-linux-x86_64-kumaraditya303-disable__asyncio-3.14.0a2+-a0a0f85 |
|----------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| coroutines                 | 26.5 ms                                                                | 26.5 ms: 1.00x slower                                                      |
| async_generators           | 498 ms                                                                 | 505 ms: 1.01x slower                                                       |
| async_tree_cpu_io_mixed_tg | 580 ms                                                                 | 951 ms: 1.64x slower                                                       |
| async_tree_cpu_io_mixed    | 627 ms                                                                 | 1.03 sec: 1.65x slower                                                     |
| async_tree_io_tg           | 765 ms                                                                 | 1.28 sec: 1.67x slower                                                     |
| async_tree_io              | 810 ms                                                                 | 1.37 sec: 1.69x slower                                                     |
| async_tree_memoization_tg  | 433 ms                                                                 | 805 ms: 1.86x slower                                                       |
| async_tree_memoization     | 472 ms                                                                 | 884 ms: 1.87x slower                                                       |
| async_tree_none            | 372 ms                                                                 | 733 ms: 1.97x slower                                                       |
| async_tree_none_tg         | 333 ms                                                                 | 679 ms: 2.04x slower                                                       |
| Geometric mean             | (ref)                                                                  | 1.53x slower                                                               |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241213-linux-x86_64-python-11ff3286b7e821bf439b-3.14.0a2+-11ff328 | bm-20241215-linux-x86_64-kumaraditya303-disable__asyncio-3.14.0a2+-a0a0f85 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 129 ms                                                                 | 131 ms: 1.01x slower                                                       |
| nbody          | 135 ms                                                                 | 139 ms: 1.03x slower                                                       |
| pidigits       | 183 ms                                                                 | 190 ms: 1.04x slower                                                       |
| Geometric mean | (ref)                                                                  | 1.03x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241213-linux-x86_64-python-11ff3286b7e821bf439b-3.14.0a2+-11ff328 | bm-20241215-linux-x86_64-kumaraditya303-disable__asyncio-3.14.0a2+-a0a0f85 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_v8       | 26.6 ms                                                                | 26.0 ms: 1.02x faster                                                      |
| regex_dna      | 228 ms                                                                 | 226 ms: 1.01x faster                                                       |
| regex_compile  | 170 ms                                                                 | 171 ms: 1.01x slower                                                       |
| regex_effbot   | 3.34 ms                                                                | 3.50 ms: 1.05x slower                                                      |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241213-linux-x86_64-python-11ff3286b7e821bf439b-3.14.0a2+-11ff328 | bm-20241215-linux-x86_64-kumaraditya303-disable__asyncio-3.14.0a2+-a0a0f85 |
|----------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pickle_pure_python   | 477 us                                                                 | 475 us: 1.01x faster                                                       |
| unpickle_pure_python | 318 us                                                                 | 320 us: 1.00x slower                                                       |
| xml_etree_process    | 74.6 ms                                                                | 75.4 ms: 1.01x slower                                                      |
| tomli_loads          | 2.72 sec                                                               | 2.78 sec: 1.02x slower                                                     |
| Geometric mean       | (ref)                                                                  | 1.00x slower                                                               |

Benchmark hidden because not significant (5): json_loads, json_dumps, xml_etree_iterparse, xml_etree_parse, xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241213-linux-x86_64-python-11ff3286b7e821bf439b-3.14.0a2+-11ff328 | bm-20241215-linux-x86_64-kumaraditya303-disable__asyncio-3.14.0a2+-a0a0f85 |
|------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 16.2 ms                                                                | 16.3 ms: 1.01x slower                                                      |
| python_startup_no_site | 9.70 ms                                                                | 9.76 ms: 1.01x slower                                                      |
| Geometric mean         | (ref)                                                                  | 1.01x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241213-linux-x86_64-python-11ff3286b7e821bf439b-3.14.0a2+-11ff328 | bm-20241215-linux-x86_64-kumaraditya303-disable__asyncio-3.14.0a2+-a0a0f85 |
|-----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| django_template | 48.4 ms                                                                | 47.3 ms: 1.02x faster                                                      |
| genshi_xml      | 64.9 ms                                                                | 63.7 ms: 1.02x faster                                                      |
| genshi_text     | 32.0 ms                                                                | 31.7 ms: 1.01x faster                                                      |
| mako            | 18.5 ms                                                                | 18.4 ms: 1.01x faster                                                      |
| Geometric mean  | (ref)                                                                  | 1.02x faster                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20241213-linux-x86_64-python-11ff3286b7e821bf439b-3.14.0a2+-11ff328 | bm-20241215-linux-x86_64-kumaraditya303-disable__asyncio-3.14.0a2+-a0a0f85 |
|----------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pathlib                    | 18.1 ms                                                                | 17.6 ms: 1.03x faster                                                      |
| django_template            | 48.4 ms                                                                | 47.3 ms: 1.02x faster                                                      |
| logging_silent             | 177 ns                                                                 | 173 ns: 1.02x faster                                                       |
| regex_v8                   | 26.6 ms                                                                | 26.0 ms: 1.02x faster                                                      |
| pprint_safe_repr           | 1.02 sec                                                               | 998 ms: 1.02x faster                                                       |
| pycparser                  | 1.48 sec                                                               | 1.45 sec: 1.02x faster                                                     |
| genshi_xml                 | 64.9 ms                                                                | 63.7 ms: 1.02x faster                                                      |
| crypto_pyaes               | 93.7 ms                                                                | 92.5 ms: 1.01x faster                                                      |
| richards                   | 71.1 ms                                                                | 70.2 ms: 1.01x faster                                                      |
| coverage                   | 108 ms                                                                 | 107 ms: 1.01x faster                                                       |
| connected_components       | 542 ms                                                                 | 536 ms: 1.01x faster                                                       |
| pprint_pformat             | 2.09 sec                                                               | 2.07 sec: 1.01x faster                                                     |
| sympy_expand               | 681 ms                                                                 | 673 ms: 1.01x faster                                                       |
| genshi_text                | 32.0 ms                                                                | 31.7 ms: 1.01x faster                                                      |
| mdp                        | 3.10 sec                                                               | 3.07 sec: 1.01x faster                                                     |
| dulwich_log                | 81.1 ms                                                                | 80.4 ms: 1.01x faster                                                      |
| mako                       | 18.5 ms                                                                | 18.4 ms: 1.01x faster                                                      |
| sympy_integrate            | 26.2 ms                                                                | 26.0 ms: 1.01x faster                                                      |
| scimark_lu                 | 177 ms                                                                 | 176 ms: 1.01x faster                                                       |
| regex_dna                  | 228 ms                                                                 | 226 ms: 1.01x faster                                                       |
| bpe_tokeniser              | 5.30 sec                                                               | 5.27 sec: 1.01x faster                                                     |
| sympy_str                  | 376 ms                                                                 | 373 ms: 1.01x faster                                                       |
| pickle_pure_python         | 477 us                                                                 | 475 us: 1.01x faster                                                       |
| chaos                      | 100 ms                                                                 | 99.7 ms: 1.01x faster                                                      |
| sqlalchemy_declarative     | 192 ms                                                                 | 191 ms: 1.00x faster                                                       |
| sqlglot_normalize          | 132 ms                                                                 | 131 ms: 1.00x faster                                                       |
| sympy_sum                  | 234 ms                                                                 | 233 ms: 1.00x faster                                                       |
| coroutines                 | 26.5 ms                                                                | 26.5 ms: 1.00x slower                                                      |
| go                         | 242 ms                                                                 | 243 ms: 1.00x slower                                                       |
| unpickle_pure_python       | 318 us                                                                 | 320 us: 1.00x slower                                                       |
| regex_compile              | 170 ms                                                                 | 171 ms: 1.01x slower                                                       |
| generators                 | 35.7 ms                                                                | 35.9 ms: 1.01x slower                                                      |
| python_startup             | 16.2 ms                                                                | 16.3 ms: 1.01x slower                                                      |
| python_startup_no_site     | 9.70 ms                                                                | 9.76 ms: 1.01x slower                                                      |
| many_optionals             | 1.16 ms                                                                | 1.17 ms: 1.01x slower                                                      |
| hexiom                     | 9.65 ms                                                                | 9.72 ms: 1.01x slower                                                      |
| sqlite_synth               | 2.92 us                                                                | 2.94 us: 1.01x slower                                                      |
| create_gc_cycles           | 2.31 ms                                                                | 2.32 ms: 1.01x slower                                                      |
| json                       | 5.41 ms                                                                | 5.46 ms: 1.01x slower                                                      |
| fannkuch                   | 528 ms                                                                 | 533 ms: 1.01x slower                                                       |
| scimark_fft                | 445 ms                                                                 | 449 ms: 1.01x slower                                                       |
| scimark_monte_carlo        | 112 ms                                                                 | 113 ms: 1.01x slower                                                       |
| sqlglot_parse              | 2.40 ms                                                                | 2.42 ms: 1.01x slower                                                      |
| k_core                     | 2.53 sec                                                               | 2.56 sec: 1.01x slower                                                     |
| xml_etree_process          | 74.6 ms                                                                | 75.4 ms: 1.01x slower                                                      |
| float                      | 129 ms                                                                 | 131 ms: 1.01x slower                                                       |
| raytrace                   | 499 ms                                                                 | 505 ms: 1.01x slower                                                       |
| comprehensions             | 25.4 us                                                                | 25.8 us: 1.01x slower                                                      |
| deepcopy_memo              | 40.0 us                                                                | 40.6 us: 1.01x slower                                                      |
| deltablue                  | 7.45 ms                                                                | 7.56 ms: 1.01x slower                                                      |
| async_generators           | 498 ms                                                                 | 505 ms: 1.01x slower                                                       |
| scimark_sparse_mat_mult    | 6.25 ms                                                                | 6.34 ms: 1.01x slower                                                      |
| tomli_loads                | 2.72 sec                                                               | 2.78 sec: 1.02x slower                                                     |
| html5lib                   | 90.2 ms                                                                | 92.3 ms: 1.02x slower                                                      |
| gc_traversal               | 3.70 ms                                                                | 3.80 ms: 1.03x slower                                                      |
| pyflate                    | 675 ms                                                                 | 693 ms: 1.03x slower                                                       |
| nbody                      | 135 ms                                                                 | 139 ms: 1.03x slower                                                       |
| scimark_sor                | 230 ms                                                                 | 237 ms: 1.03x slower                                                       |
| pidigits                   | 183 ms                                                                 | 190 ms: 1.04x slower                                                       |
| regex_effbot               | 3.34 ms                                                                | 3.50 ms: 1.05x slower                                                      |
| async_tree_cpu_io_mixed_tg | 580 ms                                                                 | 951 ms: 1.64x slower                                                       |
| async_tree_cpu_io_mixed    | 627 ms                                                                 | 1.03 sec: 1.65x slower                                                     |
| async_tree_io_tg           | 765 ms                                                                 | 1.28 sec: 1.67x slower                                                     |
| async_tree_io              | 810 ms                                                                 | 1.37 sec: 1.69x slower                                                     |
| async_tree_memoization_tg  | 433 ms                                                                 | 805 ms: 1.86x slower                                                       |
| async_tree_memoization     | 472 ms                                                                 | 884 ms: 1.87x slower                                                       |
| async_tree_none            | 372 ms                                                                 | 733 ms: 1.97x slower                                                       |
| async_tree_none_tg         | 333 ms                                                                 | 679 ms: 2.04x slower                                                       |
| Geometric mean             | (ref)                                                                  | 1.05x slower                                                               |

Benchmark hidden because not significant (29): typing_runtime_protocols, telco, logging_format, thrift, json_loads, sphinx, json_dumps, deepcopy, sqlglot_optimize, deepcopy_reduce, docutils, shortest_path, nqueens, logging_simple, xml_etree_iterparse, 2to3, pylint, richards_super, mypy2, bench_mp_pool, meteor_contest, xml_etree_parse, asyncio_websockets, bench_thread_pool, sqlalchemy_imperative, xml_etree_generate, spectral_norm, subparsers, sqlglot_transpile

- Geometric mean (including insignificant results): 1.050x slower

# HPT report

- Reliability score: 77.77% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.12x
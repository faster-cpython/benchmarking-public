# Results vs. base

- fork: kumaraditya303
- ref: per_thread_tasks
- machine: linux-x86_64
- commit hash: cca4057
- commit date: 2025-01-12
- overall geometric mean: 1.004x faster
- HPT reliability: 99.89%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

Benchmark hidden because not significant (4): 2to3, docutils, html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250111-linux-x86_64-python-3a570c6d58bd5ad7d7c1-3.14.0a3+-3a570c6 | bm-20250112-linux-x86_64-kumaraditya303-per_thread_tasks-3.14.0a3+-cca4057 |
|----------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed_tg | 556 ms                                                                 | 536 ms: 1.04x faster                                                       |
| async_tree_none_tg         | 303 ms                                                                 | 294 ms: 1.03x faster                                                       |
| coroutines                 | 26.2 ms                                                                | 25.5 ms: 1.03x faster                                                      |
| async_tree_memoization_tg  | 397 ms                                                                 | 387 ms: 1.03x faster                                                       |
| async_tree_cpu_io_mixed    | 598 ms                                                                 | 583 ms: 1.03x faster                                                       |
| async_generators           | 498 ms                                                                 | 486 ms: 1.02x faster                                                       |
| async_tree_io              | 748 ms                                                                 | 733 ms: 1.02x faster                                                       |
| async_tree_io_tg           | 696 ms                                                                 | 682 ms: 1.02x faster                                                       |
| async_tree_memoization     | 442 ms                                                                 | 436 ms: 1.02x faster                                                       |
| async_tree_none            | 349 ms                                                                 | 344 ms: 1.01x faster                                                       |
| Geometric mean             | (ref)                                                                  | 1.02x faster                                                               |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250111-linux-x86_64-python-3a570c6d58bd5ad7d7c1-3.14.0a3+-3a570c6 | bm-20250112-linux-x86_64-kumaraditya303-per_thread_tasks-3.14.0a3+-cca4057 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 103 ms                                                                 | 105 ms: 1.02x slower                                                       |
| pidigits       | 181 ms                                                                 | 189 ms: 1.04x slower                                                       |
| nbody          | 134 ms                                                                 | 140 ms: 1.04x slower                                                       |
| Geometric mean | (ref)                                                                  | 1.03x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250111-linux-x86_64-python-3a570c6d58bd5ad7d7c1-3.14.0a3+-3a570c6 | bm-20250112-linux-x86_64-kumaraditya303-per_thread_tasks-3.14.0a3+-cca4057 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_dna      | 225 ms                                                                 | 222 ms: 1.01x faster                                                       |
| regex_effbot   | 3.48 ms                                                                | 3.46 ms: 1.01x faster                                                      |
| regex_v8       | 25.0 ms                                                                | 25.3 ms: 1.01x slower                                                      |
| regex_compile  | 161 ms                                                                 | 162 ms: 1.01x slower                                                       |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20250111-linux-x86_64-python-3a570c6d58bd5ad7d7c1-3.14.0a3+-3a570c6 | bm-20250112-linux-x86_64-kumaraditya303-per_thread_tasks-3.14.0a3+-cca4057 |
|---------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| xml_etree_iterparse | 98.8 ms                                                                | 96.0 ms: 1.03x faster                                                      |
| xml_etree_parse     | 149 ms                                                                 | 148 ms: 1.01x faster                                                       |
| xml_etree_generate  | 96.7 ms                                                                | 96.9 ms: 1.00x slower                                                      |
| tomli_loads         | 2.34 sec                                                               | 2.36 sec: 1.01x slower                                                     |
| xml_etree_process   | 72.5 ms                                                                | 73.2 ms: 1.01x slower                                                      |
| Geometric mean      | (ref)                                                                  | 1.00x faster                                                               |

Benchmark hidden because not significant (4): json_loads, unpickle_pure_python, pickle_pure_python, json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250111-linux-x86_64-python-3a570c6d58bd5ad7d7c1-3.14.0a3+-3a570c6 | bm-20250112-linux-x86_64-kumaraditya303-per_thread_tasks-3.14.0a3+-cca4057 |
|------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 9.61 ms                                                                | 9.62 ms: 1.00x slower                                                      |
| Geometric mean         | (ref)                                                                  | 1.00x slower                                                               |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250111-linux-x86_64-python-3a570c6d58bd5ad7d7c1-3.14.0a3+-3a570c6 | bm-20250112-linux-x86_64-kumaraditya303-per_thread_tasks-3.14.0a3+-cca4057 |
|-----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| django_template | 46.3 ms                                                                | 45.9 ms: 1.01x faster                                                      |
| mako            | 17.9 ms                                                                | 18.2 ms: 1.02x slower                                                      |
| Geometric mean  | (ref)                                                                  | 1.00x slower                                                               |

Benchmark hidden because not significant (2): genshi_text, genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20250111-linux-x86_64-python-3a570c6d58bd5ad7d7c1-3.14.0a3+-3a570c6 | bm-20250112-linux-x86_64-kumaraditya303-per_thread_tasks-3.14.0a3+-cca4057 |
|----------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed_tg | 556 ms                                                                 | 536 ms: 1.04x faster                                                       |
| mdp                        | 3.03 sec                                                               | 2.93 sec: 1.03x faster                                                     |
| scimark_sparse_mat_mult    | 6.21 ms                                                                | 6.02 ms: 1.03x faster                                                      |
| async_tree_none_tg         | 303 ms                                                                 | 294 ms: 1.03x faster                                                       |
| xml_etree_iterparse        | 98.8 ms                                                                | 96.0 ms: 1.03x faster                                                      |
| coroutines                 | 26.2 ms                                                                | 25.5 ms: 1.03x faster                                                      |
| async_tree_memoization_tg  | 397 ms                                                                 | 387 ms: 1.03x faster                                                       |
| async_tree_cpu_io_mixed    | 598 ms                                                                 | 583 ms: 1.03x faster                                                       |
| async_generators           | 498 ms                                                                 | 486 ms: 1.02x faster                                                       |
| pyflate                    | 636 ms                                                                 | 621 ms: 1.02x faster                                                       |
| fannkuch                   | 518 ms                                                                 | 507 ms: 1.02x faster                                                       |
| async_tree_io              | 748 ms                                                                 | 733 ms: 1.02x faster                                                       |
| async_tree_io_tg           | 696 ms                                                                 | 682 ms: 1.02x faster                                                       |
| scimark_lu                 | 160 ms                                                                 | 157 ms: 1.02x faster                                                       |
| richards                   | 63.6 ms                                                                | 62.5 ms: 1.02x faster                                                      |
| nqueens                    | 99.9 ms                                                                | 98.3 ms: 1.02x faster                                                      |
| async_tree_memoization     | 442 ms                                                                 | 436 ms: 1.02x faster                                                       |
| spectral_norm              | 125 ms                                                                 | 123 ms: 1.02x faster                                                       |
| sqlite_synth               | 2.81 us                                                                | 2.77 us: 1.01x faster                                                      |
| async_tree_none            | 349 ms                                                                 | 344 ms: 1.01x faster                                                       |
| regex_dna                  | 225 ms                                                                 | 222 ms: 1.01x faster                                                       |
| hexiom                     | 9.17 ms                                                                | 9.07 ms: 1.01x faster                                                      |
| deepcopy_reduce            | 3.35 us                                                                | 3.32 us: 1.01x faster                                                      |
| connected_components       | 536 ms                                                                 | 531 ms: 1.01x faster                                                       |
| django_template            | 46.3 ms                                                                | 45.9 ms: 1.01x faster                                                      |
| regex_effbot               | 3.48 ms                                                                | 3.46 ms: 1.01x faster                                                      |
| shortest_path              | 578 ms                                                                 | 573 ms: 1.01x faster                                                       |
| crypto_pyaes               | 91.9 ms                                                                | 91.3 ms: 1.01x faster                                                      |
| pprint_safe_repr           | 962 ms                                                                 | 955 ms: 1.01x faster                                                       |
| sqlglot_normalize          | 131 ms                                                                 | 130 ms: 1.01x faster                                                       |
| meteor_contest             | 130 ms                                                                 | 130 ms: 1.01x faster                                                       |
| xml_etree_parse            | 149 ms                                                                 | 148 ms: 1.01x faster                                                       |
| pprint_pformat             | 1.99 sec                                                               | 1.98 sec: 1.01x faster                                                     |
| sqlalchemy_declarative     | 181 ms                                                                 | 180 ms: 1.01x faster                                                       |
| raytrace                   | 472 ms                                                                 | 470 ms: 1.00x faster                                                       |
| scimark_sor                | 183 ms                                                                 | 183 ms: 1.00x faster                                                       |
| bpe_tokeniser              | 5.22 sec                                                               | 5.21 sec: 1.00x faster                                                     |
| deepcopy                   | 316 us                                                                 | 315 us: 1.00x faster                                                       |
| k_core                     | 2.48 sec                                                               | 2.47 sec: 1.00x faster                                                     |
| python_startup_no_site     | 9.61 ms                                                                | 9.62 ms: 1.00x slower                                                      |
| comprehensions             | 25.2 us                                                                | 25.3 us: 1.00x slower                                                      |
| xml_etree_generate         | 96.7 ms                                                                | 96.9 ms: 1.00x slower                                                      |
| gc_traversal               | 3.76 ms                                                                | 3.77 ms: 1.00x slower                                                      |
| create_gc_cycles           | 2.34 ms                                                                | 2.35 ms: 1.00x slower                                                      |
| deltablue                  | 6.89 ms                                                                | 6.93 ms: 1.01x slower                                                      |
| subparsers                 | 26.1 ms                                                                | 26.3 ms: 1.01x slower                                                      |
| tomli_loads                | 2.34 sec                                                               | 2.36 sec: 1.01x slower                                                     |
| sqlglot_parse              | 2.17 ms                                                                | 2.19 ms: 1.01x slower                                                      |
| regex_v8                   | 25.0 ms                                                                | 25.3 ms: 1.01x slower                                                      |
| regex_compile              | 161 ms                                                                 | 162 ms: 1.01x slower                                                       |
| pycparser                  | 1.33 sec                                                               | 1.35 sec: 1.01x slower                                                     |
| xml_etree_process          | 72.5 ms                                                                | 73.2 ms: 1.01x slower                                                      |
| thrift                     | 1.01 ms                                                                | 1.02 ms: 1.01x slower                                                      |
| many_optionals             | 1.12 ms                                                                | 1.13 ms: 1.01x slower                                                      |
| coverage                   | 102 ms                                                                 | 103 ms: 1.01x slower                                                       |
| logging_silent             | 176 ns                                                                 | 179 ns: 1.01x slower                                                       |
| deepcopy_memo              | 39.8 us                                                                | 40.4 us: 1.02x slower                                                      |
| float                      | 103 ms                                                                 | 105 ms: 1.02x slower                                                       |
| mako                       | 17.9 ms                                                                | 18.2 ms: 1.02x slower                                                      |
| pidigits                   | 181 ms                                                                 | 189 ms: 1.04x slower                                                       |
| nbody                      | 134 ms                                                                 | 140 ms: 1.04x slower                                                       |
| Geometric mean             | (ref)                                                                  | 1.00x faster                                                               |

Benchmark hidden because not significant (35): sqlglot_optimize, typing_runtime_protocols, telco, bench_mp_pool, logging_simple, bench_thread_pool, json_loads, go, scimark_fft, logging_format, sphinx, asyncio_websockets, 2to3, generators, sympy_sum, python_startup, sympy_str, unpickle_pure_python, dulwich_log, genshi_text, html5lib, chaos, docutils, sympy_integrate, pylint, scimark_monte_carlo, sympy_expand, pickle_pure_python, json_dumps, genshi_xml, pathlib, json, sqlglot_transpile, sqlalchemy_imperative, richards_super

- Geometric mean (including insignificant results): 1.004x faster

# HPT report

- Reliability score: 99.89% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x
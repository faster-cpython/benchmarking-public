# Results vs. 3.13.0

- fork: Fidget-Spinner
- ref: clang_hot
- machine: windows-amd64
- commit hash: 37fb620
- commit date: 2025-03-06
- overall geometric mean: 1.018x slower
- HPT reliability: 99.99%
- HPT 99th percentile: 1.03x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250306-pythonperf1-amd64-Fidget%2dSpinner-clang_hot-3.14.0a5+-37fb620 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 229 ms: 1.06x slower                                                       |
| docutils       | 1.53 sec                                                    | 1.77 sec: 1.15x slower                                                     |
| html5lib       | 38.2 ms                                                     | 39.3 ms: 1.03x slower                                                      |
| sphinx         | 617 ms                                                      | 701 ms: 1.14x slower                                                       |
| Geometric mean | (ref)                                                       | 1.09x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250306-pythonperf1-amd64-Fidget%2dSpinner-clang_hot-3.14.0a5+-37fb620 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 281 ms                                                      | 208 ms: 1.35x faster                                                       |
| async_tree_memoization     | 265 ms                                                      | 210 ms: 1.26x faster                                                       |
| async_tree_io_tg           | 497 ms                                                      | 396 ms: 1.26x faster                                                       |
| async_tree_io              | 513 ms                                                      | 409 ms: 1.25x faster                                                       |
| async_tree_none            | 219 ms                                                      | 181 ms: 1.21x faster                                                       |
| async_tree_none_tg         | 200 ms                                                      | 173 ms: 1.16x faster                                                       |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 362 ms: 1.05x faster                                                       |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 369 ms: 1.04x faster                                                       |
| async_generators           | 223 ms                                                      | 227 ms: 1.02x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 13.5 ms: 1.08x slower                                                      |
| asyncio_websockets         | 300 ms                                                      | 332 ms: 1.11x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.12x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250306-pythonperf1-amd64-Fidget%2dSpinner-clang_hot-3.14.0a5+-37fb620 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 50.8 ms                                                     | 46.4 ms: 1.10x faster                                                      |
| nbody          | 66.3 ms                                                     | 69.2 ms: 1.04x slower                                                      |
| pidigits       | 146 ms                                                      | 156 ms: 1.07x slower                                                       |
| Geometric mean | (ref)                                                       | 1.01x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250306-pythonperf1-amd64-Fidget%2dSpinner-clang_hot-3.14.0a5+-37fb620 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 16.7 ms: 1.43x faster                                                      |
| regex_compile  | 80.7 ms                                                     | 86.3 ms: 1.07x slower                                                      |
| regex_effbot   | 1.69 ms                                                     | 1.87 ms: 1.11x slower                                                      |
| regex_dna      | 115 ms                                                      | 131 ms: 1.14x slower                                                       |
| Geometric mean | (ref)                                                       | 1.02x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250306-pythonperf1-amd64-Fidget%2dSpinner-clang_hot-3.14.0a5+-37fb620 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| tomli_loads          | 1.37 sec                                                    | 1.34 sec: 1.02x faster                                                     |
| xml_etree_parse      | 92.2 ms                                                     | 102 ms: 1.10x slower                                                       |
| unpickle_pure_python | 130 us                                                      | 149 us: 1.15x slower                                                       |
| xml_etree_iterparse  | 60.5 ms                                                     | 70.3 ms: 1.16x slower                                                      |
| pickle_pure_python   | 186 us                                                      | 219 us: 1.18x slower                                                       |
| xml_etree_generate   | 53.5 ms                                                     | 66.5 ms: 1.24x slower                                                      |
| xml_etree_process    | 36.5 ms                                                     | 46.1 ms: 1.26x slower                                                      |
| json_dumps           | 6.19 ms                                                     | 7.86 ms: 1.27x slower                                                      |
| json_loads           | 15.1 us                                                     | 20.3 us: 1.34x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.18x slower                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250306-pythonperf1-amd64-Fidget%2dSpinner-clang_hot-3.14.0a5+-37fb620 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 27.3 ms: 1.12x slower                                                      |
| python_startup_no_site | 16.9 ms                                                     | 20.4 ms: 1.21x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.16x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250306-pythonperf1-amd64-Fidget%2dSpinner-clang_hot-3.14.0a5+-37fb620 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 6.56 ms                                                     | 8.19 ms: 1.25x slower                                                      |
| django_template | 20.3 ms                                                     | 25.6 ms: 1.26x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.11x slower                                                               |

Benchmark hidden because not significant (2): genshi_xml, genshi_text

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250306-pythonperf1-amd64-Fidget%2dSpinner-clang_hot-3.14.0a5+-37fb620 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| thrift                     | 8.47 ms                                                     | 546 us: 15.50x faster                                                      |
| pathlib                    | 75.3 ms                                                     | 31.9 ms: 2.36x faster                                                      |
| regex_v8                   | 23.8 ms                                                     | 16.7 ms: 1.43x faster                                                      |
| async_tree_memoization_tg  | 281 ms                                                      | 208 ms: 1.35x faster                                                       |
| async_tree_memoization     | 265 ms                                                      | 210 ms: 1.26x faster                                                       |
| async_tree_io_tg           | 497 ms                                                      | 396 ms: 1.26x faster                                                       |
| async_tree_io              | 513 ms                                                      | 409 ms: 1.25x faster                                                       |
| deepcopy                   | 223 us                                                      | 181 us: 1.23x faster                                                       |
| async_tree_none            | 219 ms                                                      | 181 ms: 1.21x faster                                                       |
| deepcopy_memo              | 23.1 us                                                     | 19.8 us: 1.17x faster                                                      |
| async_tree_none_tg         | 200 ms                                                      | 173 ms: 1.16x faster                                                       |
| go                         | 84.7 ms                                                     | 76.6 ms: 1.11x faster                                                      |
| float                      | 50.8 ms                                                     | 46.4 ms: 1.10x faster                                                      |
| generators                 | 19.0 ms                                                     | 17.6 ms: 1.08x faster                                                      |
| spectral_norm              | 63.4 ms                                                     | 59.3 ms: 1.07x faster                                                      |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 362 ms: 1.05x faster                                                       |
| deepcopy_reduce            | 2.02 us                                                     | 1.94 us: 1.05x faster                                                      |
| scimark_sor                | 76.2 ms                                                     | 73.2 ms: 1.04x faster                                                      |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 369 ms: 1.04x faster                                                       |
| tomli_loads                | 1.37 sec                                                    | 1.34 sec: 1.02x faster                                                     |
| scimark_monte_carlo        | 40.7 ms                                                     | 40.9 ms: 1.00x slower                                                      |
| shortest_path              | 355 ms                                                      | 357 ms: 1.01x slower                                                       |
| async_generators           | 223 ms                                                      | 227 ms: 1.02x slower                                                       |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 2.67 ms: 1.03x slower                                                      |
| meteor_contest             | 72.0 ms                                                     | 74.1 ms: 1.03x slower                                                      |
| sqlite_synth               | 1.59 us                                                     | 1.63 us: 1.03x slower                                                      |
| connected_components       | 320 ms                                                      | 330 ms: 1.03x slower                                                       |
| html5lib                   | 38.2 ms                                                     | 39.3 ms: 1.03x slower                                                      |
| pycparser                  | 695 ms                                                      | 724 ms: 1.04x slower                                                       |
| nbody                      | 66.3 ms                                                     | 69.2 ms: 1.04x slower                                                      |
| dulwich_log                | 40.1 ms                                                     | 42.4 ms: 1.06x slower                                                      |
| 2to3                       | 215 ms                                                      | 229 ms: 1.06x slower                                                       |
| pidigits                   | 146 ms                                                      | 156 ms: 1.07x slower                                                       |
| telco                      | 4.85 ms                                                     | 5.18 ms: 1.07x slower                                                      |
| regex_compile              | 80.7 ms                                                     | 86.3 ms: 1.07x slower                                                      |
| pyflate                    | 283 ms                                                      | 304 ms: 1.07x slower                                                       |
| hexiom                     | 3.84 ms                                                     | 4.13 ms: 1.07x slower                                                      |
| coroutines                 | 12.5 ms                                                     | 13.5 ms: 1.08x slower                                                      |
| sympy_expand               | 286 ms                                                      | 308 ms: 1.08x slower                                                       |
| typing_runtime_protocols   | 103 us                                                      | 111 us: 1.08x slower                                                       |
| sympy_str                  | 167 ms                                                      | 181 ms: 1.08x slower                                                       |
| chaos                      | 37.9 ms                                                     | 41.1 ms: 1.08x slower                                                      |
| sympy_sum                  | 85.2 ms                                                     | 92.5 ms: 1.09x slower                                                      |
| scimark_fft                | 175 ms                                                      | 190 ms: 1.09x slower                                                       |
| bench_thread_pool          | 810 us                                                      | 881 us: 1.09x slower                                                       |
| bench_mp_pool              | 84.2 ms                                                     | 92.2 ms: 1.09x slower                                                      |
| logging_simple             | 5.77 us                                                     | 6.34 us: 1.10x slower                                                      |
| sympy_integrate            | 12.3 ms                                                     | 13.6 ms: 1.10x slower                                                      |
| pprint_pformat             | 977 ms                                                      | 1.07 sec: 1.10x slower                                                     |
| pprint_safe_repr           | 485 ms                                                      | 534 ms: 1.10x slower                                                       |
| logging_format             | 6.18 us                                                     | 6.81 us: 1.10x slower                                                      |
| sqlglot_parse              | 764 us                                                      | 843 us: 1.10x slower                                                       |
| xml_etree_parse            | 92.2 ms                                                     | 102 ms: 1.10x slower                                                       |
| asyncio_websockets         | 300 ms                                                      | 332 ms: 1.11x slower                                                       |
| regex_effbot               | 1.69 ms                                                     | 1.87 ms: 1.11x slower                                                      |
| sqlglot_transpile          | 953 us                                                      | 1.05 ms: 1.11x slower                                                      |
| sqlglot_optimize           | 32.5 ms                                                     | 36.1 ms: 1.11x slower                                                      |
| richards                   | 26.3 ms                                                     | 29.3 ms: 1.11x slower                                                      |
| bpe_tokeniser              | 2.87 sec                                                    | 3.21 sec: 1.12x slower                                                     |
| python_startup             | 24.4 ms                                                     | 27.3 ms: 1.12x slower                                                      |
| create_gc_cycles           | 1.22 ms                                                     | 1.37 ms: 1.12x slower                                                      |
| comprehensions             | 10.4 us                                                     | 11.6 us: 1.12x slower                                                      |
| richards_super             | 29.8 ms                                                     | 33.4 ms: 1.12x slower                                                      |
| logging_silent             | 54.6 ns                                                     | 61.6 ns: 1.13x slower                                                      |
| crypto_pyaes               | 45.6 ms                                                     | 51.7 ms: 1.13x slower                                                      |
| fannkuch                   | 252 ms                                                      | 286 ms: 1.14x slower                                                       |
| sphinx                     | 617 ms                                                      | 701 ms: 1.14x slower                                                       |
| regex_dna                  | 115 ms                                                      | 131 ms: 1.14x slower                                                       |
| sqlglot_normalize          | 172 ms                                                      | 195 ms: 1.14x slower                                                       |
| mdp                        | 1.43 sec                                                    | 1.63 sec: 1.14x slower                                                     |
| raytrace                   | 153 ms                                                      | 175 ms: 1.14x slower                                                       |
| unpickle_pure_python       | 130 us                                                      | 149 us: 1.15x slower                                                       |
| nqueens                    | 56.1 ms                                                     | 64.7 ms: 1.15x slower                                                      |
| docutils                   | 1.53 sec                                                    | 1.77 sec: 1.15x slower                                                     |
| json                       | 3.30 ms                                                     | 3.82 ms: 1.16x slower                                                      |
| xml_etree_iterparse        | 60.5 ms                                                     | 70.3 ms: 1.16x slower                                                      |
| scimark_lu                 | 56.7 ms                                                     | 65.9 ms: 1.16x slower                                                      |
| coverage                   | 45.3 ms                                                     | 53.2 ms: 1.17x slower                                                      |
| pickle_pure_python         | 186 us                                                      | 219 us: 1.18x slower                                                       |
| python_startup_no_site     | 16.9 ms                                                     | 20.4 ms: 1.21x slower                                                      |
| xml_etree_generate         | 53.5 ms                                                     | 66.5 ms: 1.24x slower                                                      |
| mako                       | 6.56 ms                                                     | 8.19 ms: 1.25x slower                                                      |
| xml_etree_process          | 36.5 ms                                                     | 46.1 ms: 1.26x slower                                                      |
| django_template            | 20.3 ms                                                     | 25.6 ms: 1.26x slower                                                      |
| many_optionals             | 361 us                                                      | 457 us: 1.26x slower                                                       |
| json_dumps                 | 6.19 ms                                                     | 7.86 ms: 1.27x slower                                                      |
| json_loads                 | 15.1 us                                                     | 20.3 us: 1.34x slower                                                      |
| gc_traversal               | 1.96 ms                                                     | 2.77 ms: 1.41x slower                                                      |
| subparsers                 | 10.9 ms                                                     | 16.6 ms: 1.53x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.02x slower                                                               |

Benchmark hidden because not significant (5): genshi_xml, deltablue, genshi_text, pylint, k_core
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http

- Geometric mean (including insignificant results): 1.018x slower

# HPT report

- Reliability score: 99.99% likely to be slow
- 90% likely to have a slowdown of 1.05x
- 95% likely to have a slowdown of 1.04x
- 99% likely to have a slowdown of 1.03x

# Memory
- memory change: unknown
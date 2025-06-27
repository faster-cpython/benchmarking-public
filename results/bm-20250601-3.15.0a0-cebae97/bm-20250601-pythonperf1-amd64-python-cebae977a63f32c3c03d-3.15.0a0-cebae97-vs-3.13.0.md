# Results vs. 3.13.0

- fork: python
- ref: cebae977a63f32c3c03d
- machine: windows-amd64
- commit hash: cebae97
- commit date: 2025-06-01
- overall geometric mean: 1.071x faster
- HPT reliability: 68.44%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250601-pythonperf1-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 220 ms: 1.02x slower                                                       |
| docutils       | 1.53 sec                                                    | 1.62 sec: 1.06x slower                                                     |
| sphinx         | 617 ms                                                      | 635 ms: 1.03x slower                                                       |
| Geometric mean | (ref)                                                       | 1.03x slower                                                               |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250601-pythonperf1-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| asyncio_websockets         | 300 ms                                                      | 161 ms: 1.87x faster                                                       |
| async_tree_memoization_tg  | 281 ms                                                      | 210 ms: 1.34x faster                                                       |
| async_tree_none            | 219 ms                                                      | 169 ms: 1.30x faster                                                       |
| async_tree_io              | 513 ms                                                      | 397 ms: 1.29x faster                                                       |
| async_tree_memoization     | 265 ms                                                      | 206 ms: 1.28x faster                                                       |
| async_tree_io_tg           | 497 ms                                                      | 395 ms: 1.26x faster                                                       |
| async_tree_none_tg         | 200 ms                                                      | 170 ms: 1.17x faster                                                       |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 328 ms: 1.16x faster                                                       |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 338 ms: 1.13x faster                                                       |
| async_generators           | 223 ms                                                      | 227 ms: 1.02x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 13.9 ms: 1.11x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.22x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250601-pythonperf1-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 50.8 ms                                                     | 43.9 ms: 1.16x faster                                                      |
| nbody          | 66.3 ms                                                     | 60.9 ms: 1.09x faster                                                      |
| pidigits       | 146 ms                                                      | 148 ms: 1.01x slower                                                       |
| Geometric mean | (ref)                                                       | 1.08x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250601-pythonperf1-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 13.1 ms: 1.82x faster                                                      |
| regex_effbot   | 1.69 ms                                                     | 1.45 ms: 1.17x faster                                                      |
| regex_compile  | 80.7 ms                                                     | 79.6 ms: 1.01x faster                                                      |
| regex_dna      | 115 ms                                                      | 116 ms: 1.01x slower                                                       |
| Geometric mean | (ref)                                                       | 1.21x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250601-pythonperf1-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_loads           | 15.1 us                                                     | 14.1 us: 1.07x faster                                                      |
| xml_etree_parse      | 92.2 ms                                                     | 88.1 ms: 1.05x faster                                                      |
| tomli_loads          | 1.37 sec                                                    | 1.35 sec: 1.02x faster                                                     |
| unpickle_pure_python | 130 us                                                      | 134 us: 1.03x slower                                                       |
| xml_etree_generate   | 53.5 ms                                                     | 55.9 ms: 1.04x slower                                                      |
| xml_etree_iterparse  | 60.5 ms                                                     | 63.4 ms: 1.05x slower                                                      |
| xml_etree_process    | 36.5 ms                                                     | 39.1 ms: 1.07x slower                                                      |
| pickle_pure_python   | 186 us                                                      | 212 us: 1.14x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.02x slower                                                               |

Benchmark hidden because not significant (1): json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250601-pythonperf1-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 25.5 ms: 1.05x slower                                                      |
| python_startup_no_site | 16.9 ms                                                     | 19.3 ms: 1.14x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.09x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250601-pythonperf1-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 6.56 ms                                                     | 6.38 ms: 1.03x faster                                                      |
| django_template | 20.3 ms                                                     | 24.6 ms: 1.21x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.04x slower                                                               |

Benchmark hidden because not significant (2): genshi_text, genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250601-pythonperf1-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| thrift                     | 8.47 ms                                                     | 498 us: 17.01x faster                                                      |
| pathlib                    | 75.3 ms                                                     | 31.9 ms: 2.36x faster                                                      |
| asyncio_websockets         | 300 ms                                                      | 161 ms: 1.87x faster                                                       |
| regex_v8                   | 23.8 ms                                                     | 13.1 ms: 1.82x faster                                                      |
| mdp                        | 1.43 sec                                                    | 795 ms: 1.80x faster                                                       |
| async_tree_memoization_tg  | 281 ms                                                      | 210 ms: 1.34x faster                                                       |
| deepcopy_memo              | 23.1 us                                                     | 17.3 us: 1.33x faster                                                      |
| deepcopy                   | 223 us                                                      | 170 us: 1.31x faster                                                       |
| async_tree_none            | 219 ms                                                      | 169 ms: 1.30x faster                                                       |
| async_tree_io              | 513 ms                                                      | 397 ms: 1.29x faster                                                       |
| async_tree_memoization     | 265 ms                                                      | 206 ms: 1.28x faster                                                       |
| async_tree_io_tg           | 497 ms                                                      | 395 ms: 1.26x faster                                                       |
| async_tree_none_tg         | 200 ms                                                      | 170 ms: 1.17x faster                                                       |
| regex_effbot               | 1.69 ms                                                     | 1.45 ms: 1.17x faster                                                      |
| float                      | 50.8 ms                                                     | 43.9 ms: 1.16x faster                                                      |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 328 ms: 1.16x faster                                                       |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 338 ms: 1.13x faster                                                       |
| go                         | 84.7 ms                                                     | 75.7 ms: 1.12x faster                                                      |
| spectral_norm              | 63.4 ms                                                     | 57.0 ms: 1.11x faster                                                      |
| json                       | 3.30 ms                                                     | 2.98 ms: 1.11x faster                                                      |
| deepcopy_reduce            | 2.02 us                                                     | 1.84 us: 1.10x faster                                                      |
| nbody                      | 66.3 ms                                                     | 60.9 ms: 1.09x faster                                                      |
| json_loads                 | 15.1 us                                                     | 14.1 us: 1.07x faster                                                      |
| xml_etree_parse            | 92.2 ms                                                     | 88.1 ms: 1.05x faster                                                      |
| scimark_sor                | 76.2 ms                                                     | 72.9 ms: 1.05x faster                                                      |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 2.49 ms: 1.05x faster                                                      |
| telco                      | 4.85 ms                                                     | 4.65 ms: 1.04x faster                                                      |
| scimark_monte_carlo        | 40.7 ms                                                     | 39.5 ms: 1.03x faster                                                      |
| mako                       | 6.56 ms                                                     | 6.38 ms: 1.03x faster                                                      |
| typing_runtime_protocols   | 103 us                                                      | 100 us: 1.03x faster                                                       |
| tomli_loads                | 1.37 sec                                                    | 1.35 sec: 1.02x faster                                                     |
| scimark_fft                | 175 ms                                                      | 172 ms: 1.02x faster                                                       |
| pyflate                    | 283 ms                                                      | 278 ms: 1.02x faster                                                       |
| regex_compile              | 80.7 ms                                                     | 79.6 ms: 1.01x faster                                                      |
| bpe_tokeniser              | 2.87 sec                                                    | 2.89 sec: 1.00x slower                                                     |
| sympy_integrate            | 12.3 ms                                                     | 12.4 ms: 1.01x slower                                                      |
| regex_dna                  | 115 ms                                                      | 116 ms: 1.01x slower                                                       |
| scimark_lu                 | 56.7 ms                                                     | 57.1 ms: 1.01x slower                                                      |
| sympy_str                  | 167 ms                                                      | 169 ms: 1.01x slower                                                       |
| sympy_expand               | 286 ms                                                      | 289 ms: 1.01x slower                                                       |
| pidigits                   | 146 ms                                                      | 148 ms: 1.01x slower                                                       |
| fannkuch                   | 252 ms                                                      | 255 ms: 1.01x slower                                                       |
| async_generators           | 223 ms                                                      | 227 ms: 1.02x slower                                                       |
| crypto_pyaes               | 45.6 ms                                                     | 46.6 ms: 1.02x slower                                                      |
| 2to3                       | 215 ms                                                      | 220 ms: 1.02x slower                                                       |
| comprehensions             | 10.4 us                                                     | 10.6 us: 1.02x slower                                                      |
| sympy_sum                  | 85.2 ms                                                     | 87.2 ms: 1.02x slower                                                      |
| dulwich_log                | 40.1 ms                                                     | 41.2 ms: 1.03x slower                                                      |
| shortest_path              | 355 ms                                                      | 365 ms: 1.03x slower                                                       |
| sphinx                     | 617 ms                                                      | 635 ms: 1.03x slower                                                       |
| unpickle_pure_python       | 130 us                                                      | 134 us: 1.03x slower                                                       |
| richards_super             | 29.8 ms                                                     | 30.9 ms: 1.04x slower                                                      |
| chaos                      | 37.9 ms                                                     | 39.3 ms: 1.04x slower                                                      |
| generators                 | 19.0 ms                                                     | 19.8 ms: 1.04x slower                                                      |
| hexiom                     | 3.84 ms                                                     | 4.00 ms: 1.04x slower                                                      |
| richards                   | 26.3 ms                                                     | 27.4 ms: 1.04x slower                                                      |
| xml_etree_generate         | 53.5 ms                                                     | 55.9 ms: 1.04x slower                                                      |
| connected_components       | 320 ms                                                      | 335 ms: 1.05x slower                                                       |
| python_startup             | 24.4 ms                                                     | 25.5 ms: 1.05x slower                                                      |
| xml_etree_iterparse        | 60.5 ms                                                     | 63.4 ms: 1.05x slower                                                      |
| docutils                   | 1.53 sec                                                    | 1.62 sec: 1.06x slower                                                     |
| xml_etree_process          | 36.5 ms                                                     | 39.1 ms: 1.07x slower                                                      |
| nqueens                    | 56.1 ms                                                     | 60.6 ms: 1.08x slower                                                      |
| create_gc_cycles           | 1.22 ms                                                     | 1.32 ms: 1.08x slower                                                      |
| logging_simple             | 5.77 us                                                     | 6.26 us: 1.08x slower                                                      |
| logging_format             | 6.18 us                                                     | 6.69 us: 1.08x slower                                                      |
| gc_traversal               | 1.96 ms                                                     | 2.14 ms: 1.09x slower                                                      |
| coverage                   | 45.3 ms                                                     | 49.4 ms: 1.09x slower                                                      |
| pprint_safe_repr           | 485 ms                                                      | 533 ms: 1.10x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 13.9 ms: 1.11x slower                                                      |
| pprint_pformat             | 977 ms                                                      | 1.09 sec: 1.11x slower                                                     |
| pickle_pure_python         | 186 us                                                      | 212 us: 1.14x slower                                                       |
| python_startup_no_site     | 16.9 ms                                                     | 19.3 ms: 1.14x slower                                                      |
| deltablue                  | 1.89 ms                                                     | 2.19 ms: 1.16x slower                                                      |
| raytrace                   | 153 ms                                                      | 180 ms: 1.18x slower                                                       |
| django_template            | 20.3 ms                                                     | 24.6 ms: 1.21x slower                                                      |
| many_optionals             | 361 us                                                      | 441 us: 1.22x slower                                                       |
| subparsers                 | 10.9 ms                                                     | 17.1 ms: 1.58x slower                                                      |
| logging_silent             | 54.6 ns                                                     | 320 ns: 5.87x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.05x faster                                                               |

Benchmark hidden because not significant (9): pylint, html5lib, genshi_text, meteor_contest, sqlite_synth, genshi_xml, k_core, json_dumps, pycparser
Ignored benchmarks (12) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250601-3.15.0a0-cebae97/bm-20250601-pythonperf1-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.071x faster

# HPT report

- Reliability score: 68.44% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown
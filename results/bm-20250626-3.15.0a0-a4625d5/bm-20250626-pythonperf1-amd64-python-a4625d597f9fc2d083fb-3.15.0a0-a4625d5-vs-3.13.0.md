# Results vs. 3.13.0

- fork: python
- ref: a4625d597f9fc2d083fb
- machine: windows-amd64
- commit hash: a4625d5
- commit date: 2025-06-26
- overall geometric mean: 1.056x faster
- HPT reliability: 98.74%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250626-pythonperf1-amd64-python-a4625d597f9fc2d083fb-3.15.0a0-a4625d5 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 221 ms: 1.03x slower                                                       |
| docutils       | 1.53 sec                                                    | 1.62 sec: 1.06x slower                                                     |
| sphinx         | 617 ms                                                      | 634 ms: 1.03x slower                                                       |
| Geometric mean | (ref)                                                       | 1.03x slower                                                               |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250626-pythonperf1-amd64-python-a4625d597f9fc2d083fb-3.15.0a0-a4625d5 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| asyncio_websockets         | 300 ms                                                      | 161 ms: 1.87x faster                                                       |
| async_tree_memoization_tg  | 281 ms                                                      | 213 ms: 1.32x faster                                                       |
| async_tree_io              | 513 ms                                                      | 401 ms: 1.28x faster                                                       |
| async_tree_none            | 219 ms                                                      | 173 ms: 1.27x faster                                                       |
| async_tree_memoization     | 265 ms                                                      | 210 ms: 1.26x faster                                                       |
| async_tree_io_tg           | 497 ms                                                      | 398 ms: 1.25x faster                                                       |
| async_tree_none_tg         | 200 ms                                                      | 170 ms: 1.17x faster                                                       |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 333 ms: 1.14x faster                                                       |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 345 ms: 1.11x faster                                                       |
| async_generators           | 223 ms                                                      | 236 ms: 1.06x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 14.8 ms: 1.18x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.20x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250626-pythonperf1-amd64-python-a4625d597f9fc2d083fb-3.15.0a0-a4625d5 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 50.8 ms                                                     | 44.0 ms: 1.16x faster                                                      |
| nbody          | 66.3 ms                                                     | 65.4 ms: 1.01x faster                                                      |
| Geometric mean | (ref)                                                       | 1.05x faster                                                               |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250626-pythonperf1-amd64-python-a4625d597f9fc2d083fb-3.15.0a0-a4625d5 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 14.3 ms: 1.67x faster                                                      |
| regex_effbot   | 1.69 ms                                                     | 1.51 ms: 1.12x faster                                                      |
| regex_dna      | 115 ms                                                      | 120 ms: 1.05x slower                                                       |
| Geometric mean | (ref)                                                       | 1.16x faster                                                               |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250626-pythonperf1-amd64-python-a4625d597f9fc2d083fb-3.15.0a0-a4625d5 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_loads           | 15.1 us                                                     | 14.4 us: 1.05x faster                                                      |
| xml_etree_parse      | 92.2 ms                                                     | 88.8 ms: 1.04x faster                                                      |
| json_dumps           | 6.19 ms                                                     | 6.35 ms: 1.03x slower                                                      |
| unpickle_pure_python | 130 us                                                      | 134 us: 1.03x slower                                                       |
| tomli_loads          | 1.37 sec                                                    | 1.42 sec: 1.04x slower                                                     |
| xml_etree_generate   | 53.5 ms                                                     | 56.4 ms: 1.06x slower                                                      |
| xml_etree_process    | 36.5 ms                                                     | 38.9 ms: 1.07x slower                                                      |
| xml_etree_iterparse  | 60.5 ms                                                     | 64.6 ms: 1.07x slower                                                      |
| pickle_pure_python   | 186 us                                                      | 213 us: 1.15x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.04x slower                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250626-pythonperf1-amd64-python-a4625d597f9fc2d083fb-3.15.0a0-a4625d5 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 25.9 ms: 1.06x slower                                                      |
| python_startup_no_site | 16.9 ms                                                     | 19.5 ms: 1.15x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.11x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250626-pythonperf1-amd64-python-a4625d597f9fc2d083fb-3.15.0a0-a4625d5 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 6.56 ms                                                     | 6.72 ms: 1.02x slower                                                      |
| genshi_text     | 15.2 ms                                                     | 15.7 ms: 1.03x slower                                                      |
| django_template | 20.3 ms                                                     | 24.5 ms: 1.21x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.07x slower                                                               |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250626-pythonperf1-amd64-python-a4625d597f9fc2d083fb-3.15.0a0-a4625d5 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| thrift                     | 8.47 ms                                                     | 499 us: 16.96x faster                                                      |
| pathlib                    | 75.3 ms                                                     | 31.8 ms: 2.37x faster                                                      |
| asyncio_websockets         | 300 ms                                                      | 161 ms: 1.87x faster                                                       |
| mdp                        | 1.43 sec                                                    | 800 ms: 1.79x faster                                                       |
| regex_v8                   | 23.8 ms                                                     | 14.3 ms: 1.67x faster                                                      |
| deepcopy                   | 223 us                                                      | 169 us: 1.32x faster                                                       |
| async_tree_memoization_tg  | 281 ms                                                      | 213 ms: 1.32x faster                                                       |
| async_tree_io              | 513 ms                                                      | 401 ms: 1.28x faster                                                       |
| async_tree_none            | 219 ms                                                      | 173 ms: 1.27x faster                                                       |
| async_tree_memoization     | 265 ms                                                      | 210 ms: 1.26x faster                                                       |
| async_tree_io_tg           | 497 ms                                                      | 398 ms: 1.25x faster                                                       |
| deepcopy_memo              | 23.1 us                                                     | 18.5 us: 1.25x faster                                                      |
| async_tree_none_tg         | 200 ms                                                      | 170 ms: 1.17x faster                                                       |
| float                      | 50.8 ms                                                     | 44.0 ms: 1.16x faster                                                      |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 333 ms: 1.14x faster                                                       |
| regex_effbot               | 1.69 ms                                                     | 1.51 ms: 1.12x faster                                                      |
| deepcopy_reduce            | 2.02 us                                                     | 1.80 us: 1.12x faster                                                      |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 345 ms: 1.11x faster                                                       |
| go                         | 84.7 ms                                                     | 77.6 ms: 1.09x faster                                                      |
| json                       | 3.30 ms                                                     | 3.03 ms: 1.09x faster                                                      |
| telco                      | 4.85 ms                                                     | 4.60 ms: 1.05x faster                                                      |
| json_loads                 | 15.1 us                                                     | 14.4 us: 1.05x faster                                                      |
| xml_etree_parse            | 92.2 ms                                                     | 88.8 ms: 1.04x faster                                                      |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 2.53 ms: 1.03x faster                                                      |
| nbody                      | 66.3 ms                                                     | 65.4 ms: 1.01x faster                                                      |
| typing_runtime_protocols   | 103 us                                                      | 102 us: 1.01x faster                                                       |
| sqlite_synth               | 1.59 us                                                     | 1.60 us: 1.01x slower                                                      |
| generators                 | 19.0 ms                                                     | 19.2 ms: 1.01x slower                                                      |
| pprint_safe_repr           | 485 ms                                                      | 492 ms: 1.02x slower                                                       |
| sympy_str                  | 167 ms                                                      | 170 ms: 1.02x slower                                                       |
| sympy_integrate            | 12.3 ms                                                     | 12.6 ms: 1.02x slower                                                      |
| spectral_norm              | 63.4 ms                                                     | 64.9 ms: 1.02x slower                                                      |
| mako                       | 6.56 ms                                                     | 6.72 ms: 1.02x slower                                                      |
| sympy_expand               | 286 ms                                                      | 292 ms: 1.02x slower                                                       |
| shortest_path              | 355 ms                                                      | 364 ms: 1.02x slower                                                       |
| sympy_sum                  | 85.2 ms                                                     | 87.3 ms: 1.02x slower                                                      |
| json_dumps                 | 6.19 ms                                                     | 6.35 ms: 1.03x slower                                                      |
| dulwich_log                | 40.1 ms                                                     | 41.2 ms: 1.03x slower                                                      |
| sphinx                     | 617 ms                                                      | 634 ms: 1.03x slower                                                       |
| bpe_tokeniser              | 2.87 sec                                                    | 2.95 sec: 1.03x slower                                                     |
| unpickle_pure_python       | 130 us                                                      | 134 us: 1.03x slower                                                       |
| 2to3                       | 215 ms                                                      | 221 ms: 1.03x slower                                                       |
| genshi_text                | 15.2 ms                                                     | 15.7 ms: 1.03x slower                                                      |
| pyflate                    | 283 ms                                                      | 292 ms: 1.03x slower                                                       |
| scimark_sor                | 76.2 ms                                                     | 78.7 ms: 1.03x slower                                                      |
| tomli_loads                | 1.37 sec                                                    | 1.42 sec: 1.04x slower                                                     |
| pprint_pformat             | 977 ms                                                      | 1.01 sec: 1.04x slower                                                     |
| comprehensions             | 10.4 us                                                     | 10.8 us: 1.04x slower                                                      |
| fannkuch                   | 252 ms                                                      | 261 ms: 1.04x slower                                                       |
| richards                   | 26.3 ms                                                     | 27.3 ms: 1.04x slower                                                      |
| connected_components       | 320 ms                                                      | 333 ms: 1.04x slower                                                       |
| crypto_pyaes               | 45.6 ms                                                     | 47.6 ms: 1.04x slower                                                      |
| regex_dna                  | 115 ms                                                      | 120 ms: 1.05x slower                                                       |
| richards_super             | 29.8 ms                                                     | 31.2 ms: 1.05x slower                                                      |
| logging_silent             | 54.6 ns                                                     | 57.6 ns: 1.05x slower                                                      |
| xml_etree_generate         | 53.5 ms                                                     | 56.4 ms: 1.06x slower                                                      |
| scimark_lu                 | 56.7 ms                                                     | 60.0 ms: 1.06x slower                                                      |
| docutils                   | 1.53 sec                                                    | 1.62 sec: 1.06x slower                                                     |
| async_generators           | 223 ms                                                      | 236 ms: 1.06x slower                                                       |
| logging_simple             | 5.77 us                                                     | 6.13 us: 1.06x slower                                                      |
| python_startup             | 24.4 ms                                                     | 25.9 ms: 1.06x slower                                                      |
| logging_format             | 6.18 us                                                     | 6.56 us: 1.06x slower                                                      |
| hexiom                     | 3.84 ms                                                     | 4.08 ms: 1.06x slower                                                      |
| xml_etree_process          | 36.5 ms                                                     | 38.9 ms: 1.07x slower                                                      |
| xml_etree_iterparse        | 60.5 ms                                                     | 64.6 ms: 1.07x slower                                                      |
| gc_traversal               | 1.96 ms                                                     | 2.11 ms: 1.07x slower                                                      |
| create_gc_cycles           | 1.22 ms                                                     | 1.31 ms: 1.07x slower                                                      |
| chaos                      | 37.9 ms                                                     | 41.1 ms: 1.08x slower                                                      |
| scimark_fft                | 175 ms                                                      | 190 ms: 1.09x slower                                                       |
| nqueens                    | 56.1 ms                                                     | 61.6 ms: 1.10x slower                                                      |
| coverage                   | 45.3 ms                                                     | 51.6 ms: 1.14x slower                                                      |
| pickle_pure_python         | 186 us                                                      | 213 us: 1.15x slower                                                       |
| python_startup_no_site     | 16.9 ms                                                     | 19.5 ms: 1.15x slower                                                      |
| deltablue                  | 1.89 ms                                                     | 2.19 ms: 1.16x slower                                                      |
| raytrace                   | 153 ms                                                      | 179 ms: 1.17x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 14.8 ms: 1.18x slower                                                      |
| django_template            | 20.3 ms                                                     | 24.5 ms: 1.21x slower                                                      |
| many_optionals             | 361 us                                                      | 439 us: 1.21x slower                                                       |
| subparsers                 | 10.9 ms                                                     | 17.0 ms: 1.57x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.05x faster                                                               |

Benchmark hidden because not significant (9): pylint, regex_compile, meteor_contest, scimark_monte_carlo, pidigits, pycparser, k_core, html5lib, genshi_xml
Ignored benchmarks (12) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250626-3.15.0a0-a4625d5/bm-20250626-pythonperf1-amd64-python-a4625d597f9fc2d083fb-3.15.0a0-a4625d5.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.056x faster

# HPT report

- Reliability score: 98.74% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown
# Results vs. 3.13.0

- fork: python
- ref: 8dd8b5c2f0785675b928
- machine: windows-amd64
- commit hash: 8dd8b5c
- commit date: 2025-06-17
- overall geometric mean: 1.062x faster
- HPT reliability: 90.22%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250617-pythonperf1-amd64-python-8dd8b5c2f0785675b928-3.15.0a0-8dd8b5c |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 222 ms: 1.03x slower                                                       |
| docutils       | 1.53 sec                                                    | 1.62 sec: 1.06x slower                                                     |
| html5lib       | 38.2 ms                                                     | 39.0 ms: 1.02x slower                                                      |
| sphinx         | 617 ms                                                      | 639 ms: 1.03x slower                                                       |
| Geometric mean | (ref)                                                       | 1.04x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250617-pythonperf1-amd64-python-8dd8b5c2f0785675b928-3.15.0a0-8dd8b5c |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| asyncio_websockets         | 300 ms                                                      | 157 ms: 1.91x faster                                                       |
| async_tree_memoization_tg  | 281 ms                                                      | 211 ms: 1.33x faster                                                       |
| async_tree_io              | 513 ms                                                      | 400 ms: 1.28x faster                                                       |
| async_tree_memoization     | 265 ms                                                      | 209 ms: 1.27x faster                                                       |
| async_tree_none            | 219 ms                                                      | 174 ms: 1.26x faster                                                       |
| async_tree_io_tg           | 497 ms                                                      | 395 ms: 1.26x faster                                                       |
| async_tree_none_tg         | 200 ms                                                      | 170 ms: 1.18x faster                                                       |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 330 ms: 1.15x faster                                                       |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 340 ms: 1.13x faster                                                       |
| async_generators           | 223 ms                                                      | 231 ms: 1.04x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 14.1 ms: 1.13x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.22x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250617-pythonperf1-amd64-python-8dd8b5c2f0785675b928-3.15.0a0-8dd8b5c |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 50.8 ms                                                     | 44.1 ms: 1.15x faster                                                      |
| nbody          | 66.3 ms                                                     | 61.8 ms: 1.07x faster                                                      |
| Geometric mean | (ref)                                                       | 1.07x faster                                                               |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250617-pythonperf1-amd64-python-8dd8b5c2f0785675b928-3.15.0a0-8dd8b5c |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 14.0 ms: 1.70x faster                                                      |
| regex_effbot   | 1.69 ms                                                     | 1.61 ms: 1.05x faster                                                      |
| regex_compile  | 80.7 ms                                                     | 78.9 ms: 1.02x faster                                                      |
| regex_dna      | 115 ms                                                      | 122 ms: 1.06x slower                                                       |
| Geometric mean | (ref)                                                       | 1.15x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250617-pythonperf1-amd64-python-8dd8b5c2f0785675b928-3.15.0a0-8dd8b5c |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_loads           | 15.1 us                                                     | 14.2 us: 1.07x faster                                                      |
| xml_etree_parse      | 92.2 ms                                                     | 88.5 ms: 1.04x faster                                                      |
| unpickle_pure_python | 130 us                                                      | 133 us: 1.03x slower                                                       |
| xml_etree_generate   | 53.5 ms                                                     | 56.2 ms: 1.05x slower                                                      |
| xml_etree_iterparse  | 60.5 ms                                                     | 64.4 ms: 1.06x slower                                                      |
| xml_etree_process    | 36.5 ms                                                     | 39.3 ms: 1.08x slower                                                      |
| pickle_pure_python   | 186 us                                                      | 207 us: 1.11x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.02x slower                                                               |

Benchmark hidden because not significant (2): tomli_loads, json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250617-pythonperf1-amd64-python-8dd8b5c2f0785675b928-3.15.0a0-8dd8b5c |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 25.8 ms: 1.06x slower                                                      |
| python_startup_no_site | 16.9 ms                                                     | 19.4 ms: 1.15x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.10x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250617-pythonperf1-amd64-python-8dd8b5c2f0785675b928-3.15.0a0-8dd8b5c |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_text     | 15.2 ms                                                     | 15.4 ms: 1.01x slower                                                      |
| mako            | 6.56 ms                                                     | 6.73 ms: 1.03x slower                                                      |
| django_template | 20.3 ms                                                     | 24.1 ms: 1.19x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.06x slower                                                               |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250617-pythonperf1-amd64-python-8dd8b5c2f0785675b928-3.15.0a0-8dd8b5c |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| thrift                     | 8.47 ms                                                     | 500 us: 16.94x faster                                                      |
| pathlib                    | 75.3 ms                                                     | 32.1 ms: 2.35x faster                                                      |
| asyncio_websockets         | 300 ms                                                      | 157 ms: 1.91x faster                                                       |
| mdp                        | 1.43 sec                                                    | 800 ms: 1.79x faster                                                       |
| regex_v8                   | 23.8 ms                                                     | 14.0 ms: 1.70x faster                                                      |
| async_tree_memoization_tg  | 281 ms                                                      | 211 ms: 1.33x faster                                                       |
| deepcopy                   | 223 us                                                      | 170 us: 1.32x faster                                                       |
| deepcopy_memo              | 23.1 us                                                     | 17.6 us: 1.31x faster                                                      |
| async_tree_io              | 513 ms                                                      | 400 ms: 1.28x faster                                                       |
| async_tree_memoization     | 265 ms                                                      | 209 ms: 1.27x faster                                                       |
| async_tree_none            | 219 ms                                                      | 174 ms: 1.26x faster                                                       |
| async_tree_io_tg           | 497 ms                                                      | 395 ms: 1.26x faster                                                       |
| async_tree_none_tg         | 200 ms                                                      | 170 ms: 1.18x faster                                                       |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 330 ms: 1.15x faster                                                       |
| float                      | 50.8 ms                                                     | 44.1 ms: 1.15x faster                                                      |
| go                         | 84.7 ms                                                     | 74.9 ms: 1.13x faster                                                      |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 340 ms: 1.13x faster                                                       |
| json                       | 3.30 ms                                                     | 2.97 ms: 1.11x faster                                                      |
| deepcopy_reduce            | 2.02 us                                                     | 1.86 us: 1.09x faster                                                      |
| nbody                      | 66.3 ms                                                     | 61.8 ms: 1.07x faster                                                      |
| json_loads                 | 15.1 us                                                     | 14.2 us: 1.07x faster                                                      |
| telco                      | 4.85 ms                                                     | 4.55 ms: 1.07x faster                                                      |
| regex_effbot               | 1.69 ms                                                     | 1.61 ms: 1.05x faster                                                      |
| xml_etree_parse            | 92.2 ms                                                     | 88.5 ms: 1.04x faster                                                      |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 2.52 ms: 1.03x faster                                                      |
| typing_runtime_protocols   | 103 us                                                      | 101 us: 1.03x faster                                                       |
| regex_compile              | 80.7 ms                                                     | 78.9 ms: 1.02x faster                                                      |
| spectral_norm              | 63.4 ms                                                     | 62.1 ms: 1.02x faster                                                      |
| scimark_sor                | 76.2 ms                                                     | 75.0 ms: 1.02x faster                                                      |
| scimark_fft                | 175 ms                                                      | 172 ms: 1.02x faster                                                       |
| sympy_integrate            | 12.3 ms                                                     | 12.4 ms: 1.00x slower                                                      |
| sympy_str                  | 167 ms                                                      | 168 ms: 1.01x slower                                                       |
| meteor_contest             | 72.0 ms                                                     | 72.5 ms: 1.01x slower                                                      |
| genshi_text                | 15.2 ms                                                     | 15.4 ms: 1.01x slower                                                      |
| pyflate                    | 283 ms                                                      | 289 ms: 1.02x slower                                                       |
| richards                   | 26.3 ms                                                     | 26.8 ms: 1.02x slower                                                      |
| fannkuch                   | 252 ms                                                      | 257 ms: 1.02x slower                                                       |
| html5lib                   | 38.2 ms                                                     | 39.0 ms: 1.02x slower                                                      |
| scimark_lu                 | 56.7 ms                                                     | 58.0 ms: 1.02x slower                                                      |
| sympy_sum                  | 85.2 ms                                                     | 87.2 ms: 1.02x slower                                                      |
| richards_super             | 29.8 ms                                                     | 30.5 ms: 1.02x slower                                                      |
| mako                       | 6.56 ms                                                     | 6.73 ms: 1.03x slower                                                      |
| unpickle_pure_python       | 130 us                                                      | 133 us: 1.03x slower                                                       |
| dulwich_log                | 40.1 ms                                                     | 41.3 ms: 1.03x slower                                                      |
| 2to3                       | 215 ms                                                      | 222 ms: 1.03x slower                                                       |
| bpe_tokeniser              | 2.87 sec                                                    | 2.97 sec: 1.03x slower                                                     |
| crypto_pyaes               | 45.6 ms                                                     | 47.1 ms: 1.03x slower                                                      |
| sphinx                     | 617 ms                                                      | 639 ms: 1.03x slower                                                       |
| async_generators           | 223 ms                                                      | 231 ms: 1.04x slower                                                       |
| comprehensions             | 10.4 us                                                     | 10.8 us: 1.04x slower                                                      |
| generators                 | 19.0 ms                                                     | 19.8 ms: 1.04x slower                                                      |
| hexiom                     | 3.84 ms                                                     | 4.02 ms: 1.05x slower                                                      |
| connected_components       | 320 ms                                                      | 336 ms: 1.05x slower                                                       |
| xml_etree_generate         | 53.5 ms                                                     | 56.2 ms: 1.05x slower                                                      |
| chaos                      | 37.9 ms                                                     | 39.9 ms: 1.05x slower                                                      |
| python_startup             | 24.4 ms                                                     | 25.8 ms: 1.06x slower                                                      |
| regex_dna                  | 115 ms                                                      | 122 ms: 1.06x slower                                                       |
| docutils                   | 1.53 sec                                                    | 1.62 sec: 1.06x slower                                                     |
| xml_etree_iterparse        | 60.5 ms                                                     | 64.4 ms: 1.06x slower                                                      |
| shortest_path              | 355 ms                                                      | 381 ms: 1.07x slower                                                       |
| xml_etree_process          | 36.5 ms                                                     | 39.3 ms: 1.08x slower                                                      |
| coverage                   | 45.3 ms                                                     | 49.0 ms: 1.08x slower                                                      |
| nqueens                    | 56.1 ms                                                     | 60.9 ms: 1.09x slower                                                      |
| logging_simple             | 5.77 us                                                     | 6.28 us: 1.09x slower                                                      |
| logging_format             | 6.18 us                                                     | 6.77 us: 1.10x slower                                                      |
| create_gc_cycles           | 1.22 ms                                                     | 1.34 ms: 1.10x slower                                                      |
| gc_traversal               | 1.96 ms                                                     | 2.17 ms: 1.10x slower                                                      |
| pprint_safe_repr           | 485 ms                                                      | 537 ms: 1.11x slower                                                       |
| pickle_pure_python         | 186 us                                                      | 207 us: 1.11x slower                                                       |
| pprint_pformat             | 977 ms                                                      | 1.09 sec: 1.12x slower                                                     |
| coroutines                 | 12.5 ms                                                     | 14.1 ms: 1.13x slower                                                      |
| deltablue                  | 1.89 ms                                                     | 2.17 ms: 1.15x slower                                                      |
| python_startup_no_site     | 16.9 ms                                                     | 19.4 ms: 1.15x slower                                                      |
| raytrace                   | 153 ms                                                      | 177 ms: 1.15x slower                                                       |
| django_template            | 20.3 ms                                                     | 24.1 ms: 1.19x slower                                                      |
| many_optionals             | 361 us                                                      | 434 us: 1.20x slower                                                       |
| subparsers                 | 10.9 ms                                                     | 17.0 ms: 1.56x slower                                                      |
| logging_silent             | 54.6 ns                                                     | 342 ns: 6.27x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.04x faster                                                               |

Benchmark hidden because not significant (10): pylint, scimark_monte_carlo, tomli_loads, pidigits, k_core, sqlite_synth, sympy_expand, json_dumps, genshi_xml, pycparser
Ignored benchmarks (12) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250617-3.15.0a0-8dd8b5c/bm-20250617-pythonperf1-amd64-python-8dd8b5c2f0785675b928-3.15.0a0-8dd8b5c.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.062x faster

# HPT report

- Reliability score: 90.22% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown
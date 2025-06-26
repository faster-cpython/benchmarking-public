# Results vs. 3.13.0

- fork: python
- ref: fba5dded6df3c2b19435
- machine: windows-amd64
- commit hash: fba5dde
- commit date: 2025-06-17
- overall geometric mean: 1.072x faster
- HPT reliability: 61.60%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250617-pythonperf1-amd64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 220 ms: 1.02x slower                                                       |
| docutils       | 1.53 sec                                                    | 1.61 sec: 1.05x slower                                                     |
| sphinx         | 617 ms                                                      | 635 ms: 1.03x slower                                                       |
| Geometric mean | (ref)                                                       | 1.03x slower                                                               |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250617-pythonperf1-amd64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| asyncio_websockets         | 300 ms                                                      | 158 ms: 1.90x faster                                                       |
| async_tree_memoization_tg  | 281 ms                                                      | 208 ms: 1.35x faster                                                       |
| async_tree_none            | 219 ms                                                      | 167 ms: 1.31x faster                                                       |
| async_tree_io              | 513 ms                                                      | 395 ms: 1.30x faster                                                       |
| async_tree_io_tg           | 497 ms                                                      | 385 ms: 1.29x faster                                                       |
| async_tree_memoization     | 265 ms                                                      | 206 ms: 1.29x faster                                                       |
| async_tree_none_tg         | 200 ms                                                      | 166 ms: 1.20x faster                                                       |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 328 ms: 1.16x faster                                                       |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 339 ms: 1.13x faster                                                       |
| async_generators           | 223 ms                                                      | 230 ms: 1.03x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 14.1 ms: 1.13x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.23x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250617-pythonperf1-amd64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 50.8 ms                                                     | 43.2 ms: 1.18x faster                                                      |
| nbody          | 66.3 ms                                                     | 60.5 ms: 1.09x faster                                                      |
| Geometric mean | (ref)                                                       | 1.09x faster                                                               |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250617-pythonperf1-amd64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 14.0 ms: 1.71x faster                                                      |
| regex_effbot   | 1.69 ms                                                     | 1.51 ms: 1.12x faster                                                      |
| regex_compile  | 80.7 ms                                                     | 78.7 ms: 1.03x faster                                                      |
| regex_dna      | 115 ms                                                      | 122 ms: 1.06x slower                                                       |
| Geometric mean | (ref)                                                       | 1.17x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250617-pythonperf1-amd64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_loads           | 15.1 us                                                     | 14.3 us: 1.06x faster                                                      |
| xml_etree_parse      | 92.2 ms                                                     | 88.3 ms: 1.04x faster                                                      |
| tomli_loads          | 1.37 sec                                                    | 1.35 sec: 1.01x faster                                                     |
| unpickle_pure_python | 130 us                                                      | 131 us: 1.01x slower                                                       |
| xml_etree_generate   | 53.5 ms                                                     | 55.4 ms: 1.04x slower                                                      |
| xml_etree_process    | 36.5 ms                                                     | 38.5 ms: 1.05x slower                                                      |
| xml_etree_iterparse  | 60.5 ms                                                     | 64.5 ms: 1.07x slower                                                      |
| pickle_pure_python   | 186 us                                                      | 206 us: 1.11x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.02x slower                                                               |

Benchmark hidden because not significant (1): json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250617-pythonperf1-amd64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 25.6 ms: 1.05x slower                                                      |
| python_startup_no_site | 16.9 ms                                                     | 19.3 ms: 1.14x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.09x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250617-pythonperf1-amd64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_text     | 15.2 ms                                                     | 15.1 ms: 1.01x faster                                                      |
| django_template | 20.3 ms                                                     | 23.6 ms: 1.16x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.04x slower                                                               |

Benchmark hidden because not significant (2): mako, genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250617-pythonperf1-amd64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| thrift                     | 8.47 ms                                                     | 493 us: 17.18x faster                                                      |
| pathlib                    | 75.3 ms                                                     | 31.8 ms: 2.37x faster                                                      |
| asyncio_websockets         | 300 ms                                                      | 158 ms: 1.90x faster                                                       |
| mdp                        | 1.43 sec                                                    | 794 ms: 1.80x faster                                                       |
| regex_v8                   | 23.8 ms                                                     | 14.0 ms: 1.71x faster                                                      |
| async_tree_memoization_tg  | 281 ms                                                      | 208 ms: 1.35x faster                                                       |
| deepcopy                   | 223 us                                                      | 168 us: 1.33x faster                                                       |
| async_tree_none            | 219 ms                                                      | 167 ms: 1.31x faster                                                       |
| async_tree_io              | 513 ms                                                      | 395 ms: 1.30x faster                                                       |
| deepcopy_memo              | 23.1 us                                                     | 17.8 us: 1.30x faster                                                      |
| async_tree_io_tg           | 497 ms                                                      | 385 ms: 1.29x faster                                                       |
| async_tree_memoization     | 265 ms                                                      | 206 ms: 1.29x faster                                                       |
| async_tree_none_tg         | 200 ms                                                      | 166 ms: 1.20x faster                                                       |
| float                      | 50.8 ms                                                     | 43.2 ms: 1.18x faster                                                      |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 328 ms: 1.16x faster                                                       |
| go                         | 84.7 ms                                                     | 74.0 ms: 1.14x faster                                                      |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 339 ms: 1.13x faster                                                       |
| regex_effbot               | 1.69 ms                                                     | 1.51 ms: 1.12x faster                                                      |
| deepcopy_reduce            | 2.02 us                                                     | 1.81 us: 1.11x faster                                                      |
| json                       | 3.30 ms                                                     | 3.01 ms: 1.10x faster                                                      |
| nbody                      | 66.3 ms                                                     | 60.5 ms: 1.09x faster                                                      |
| telco                      | 4.85 ms                                                     | 4.52 ms: 1.07x faster                                                      |
| spectral_norm              | 63.4 ms                                                     | 59.7 ms: 1.06x faster                                                      |
| json_loads                 | 15.1 us                                                     | 14.3 us: 1.06x faster                                                      |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 2.48 ms: 1.05x faster                                                      |
| xml_etree_parse            | 92.2 ms                                                     | 88.3 ms: 1.04x faster                                                      |
| regex_compile              | 80.7 ms                                                     | 78.7 ms: 1.03x faster                                                      |
| scimark_sor                | 76.2 ms                                                     | 74.3 ms: 1.03x faster                                                      |
| typing_runtime_protocols   | 103 us                                                      | 101 us: 1.02x faster                                                       |
| scimark_monte_carlo        | 40.7 ms                                                     | 40.0 ms: 1.02x faster                                                      |
| fannkuch                   | 252 ms                                                      | 247 ms: 1.02x faster                                                       |
| tomli_loads                | 1.37 sec                                                    | 1.35 sec: 1.01x faster                                                     |
| scimark_fft                | 175 ms                                                      | 173 ms: 1.01x faster                                                       |
| genshi_text                | 15.2 ms                                                     | 15.1 ms: 1.01x faster                                                      |
| sqlite_synth               | 1.59 us                                                     | 1.58 us: 1.00x faster                                                      |
| sympy_integrate            | 12.3 ms                                                     | 12.3 ms: 1.00x faster                                                      |
| sympy_expand               | 286 ms                                                      | 287 ms: 1.00x slower                                                       |
| sympy_str                  | 167 ms                                                      | 168 ms: 1.01x slower                                                       |
| unpickle_pure_python       | 130 us                                                      | 131 us: 1.01x slower                                                       |
| bpe_tokeniser              | 2.87 sec                                                    | 2.90 sec: 1.01x slower                                                     |
| richards                   | 26.3 ms                                                     | 26.6 ms: 1.01x slower                                                      |
| richards_super             | 29.8 ms                                                     | 30.2 ms: 1.02x slower                                                      |
| hexiom                     | 3.84 ms                                                     | 3.91 ms: 1.02x slower                                                      |
| scimark_lu                 | 56.7 ms                                                     | 57.7 ms: 1.02x slower                                                      |
| shortest_path              | 355 ms                                                      | 362 ms: 1.02x slower                                                       |
| comprehensions             | 10.4 us                                                     | 10.6 us: 1.02x slower                                                      |
| 2to3                       | 215 ms                                                      | 220 ms: 1.02x slower                                                       |
| generators                 | 19.0 ms                                                     | 19.4 ms: 1.02x slower                                                      |
| crypto_pyaes               | 45.6 ms                                                     | 46.7 ms: 1.02x slower                                                      |
| dulwich_log                | 40.1 ms                                                     | 41.2 ms: 1.03x slower                                                      |
| sympy_sum                  | 85.2 ms                                                     | 87.6 ms: 1.03x slower                                                      |
| sphinx                     | 617 ms                                                      | 635 ms: 1.03x slower                                                       |
| async_generators           | 223 ms                                                      | 230 ms: 1.03x slower                                                       |
| xml_etree_generate         | 53.5 ms                                                     | 55.4 ms: 1.04x slower                                                      |
| chaos                      | 37.9 ms                                                     | 39.3 ms: 1.04x slower                                                      |
| connected_components       | 320 ms                                                      | 334 ms: 1.04x slower                                                       |
| python_startup             | 24.4 ms                                                     | 25.6 ms: 1.05x slower                                                      |
| docutils                   | 1.53 sec                                                    | 1.61 sec: 1.05x slower                                                     |
| xml_etree_process          | 36.5 ms                                                     | 38.5 ms: 1.05x slower                                                      |
| regex_dna                  | 115 ms                                                      | 122 ms: 1.06x slower                                                       |
| xml_etree_iterparse        | 60.5 ms                                                     | 64.5 ms: 1.07x slower                                                      |
| create_gc_cycles           | 1.22 ms                                                     | 1.31 ms: 1.07x slower                                                      |
| nqueens                    | 56.1 ms                                                     | 60.5 ms: 1.08x slower                                                      |
| logging_format             | 6.18 us                                                     | 6.73 us: 1.09x slower                                                      |
| pprint_safe_repr           | 485 ms                                                      | 530 ms: 1.09x slower                                                       |
| pprint_pformat             | 977 ms                                                      | 1.07 sec: 1.09x slower                                                     |
| logging_simple             | 5.77 us                                                     | 6.32 us: 1.10x slower                                                      |
| gc_traversal               | 1.96 ms                                                     | 2.16 ms: 1.10x slower                                                      |
| pickle_pure_python         | 186 us                                                      | 206 us: 1.11x slower                                                       |
| coverage                   | 45.3 ms                                                     | 50.6 ms: 1.12x slower                                                      |
| coroutines                 | 12.5 ms                                                     | 14.1 ms: 1.13x slower                                                      |
| deltablue                  | 1.89 ms                                                     | 2.14 ms: 1.13x slower                                                      |
| python_startup_no_site     | 16.9 ms                                                     | 19.3 ms: 1.14x slower                                                      |
| django_template            | 20.3 ms                                                     | 23.6 ms: 1.16x slower                                                      |
| raytrace                   | 153 ms                                                      | 180 ms: 1.17x slower                                                       |
| many_optionals             | 361 us                                                      | 433 us: 1.20x slower                                                       |
| subparsers                 | 10.9 ms                                                     | 16.8 ms: 1.55x slower                                                      |
| logging_silent             | 54.6 ns                                                     | 318 ns: 5.83x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.05x faster                                                               |

Benchmark hidden because not significant (10): pylint, pyflate, json_dumps, pidigits, meteor_contest, html5lib, mako, pycparser, genshi_xml, k_core
Ignored benchmarks (12) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250617-3.15.0a0-fba5dde/bm-20250617-pythonperf1-amd64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.072x faster

# HPT report

- Reliability score: 61.60% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown
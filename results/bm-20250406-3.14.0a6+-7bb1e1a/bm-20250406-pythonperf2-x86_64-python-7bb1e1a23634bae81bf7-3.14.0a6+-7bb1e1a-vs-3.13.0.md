# Results vs. 3.13.0

- fork: python
- ref: 7bb1e1a23634bae81bf7
- machine: linux-x86_64
- commit hash: 7bb1e1a
- commit date: 2025-04-06
- overall geometric mean: 1.071x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: 1.03x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250406-pythonperf2-x86_64-python-7bb1e1a23634bae81bf7-3.14.0a6+-7bb1e1a |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 275 ms: 1.07x faster                                                         |
| docutils       | 2.83 sec                                                     | 2.86 sec: 1.01x slower                                                       |
| html5lib       | 73.5 ms                                                      | 66.4 ms: 1.11x faster                                                        |
| sphinx         | 1.12 sec                                                     | 1.10 sec: 1.02x faster                                                       |
| Geometric mean | (ref)                                                        | 1.05x faster                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250406-pythonperf2-x86_64-python-7bb1e1a23634bae81bf7-3.14.0a6+-7bb1e1a |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 466 ms                                                       | 335 ms: 1.39x faster                                                         |
| async_tree_memoization     | 453 ms                                                       | 328 ms: 1.38x faster                                                         |
| async_tree_io              | 843 ms                                                       | 629 ms: 1.34x faster                                                         |
| async_tree_none            | 376 ms                                                       | 284 ms: 1.32x faster                                                         |
| async_tree_io_tg           | 831 ms                                                       | 636 ms: 1.31x faster                                                         |
| async_tree_none_tg         | 346 ms                                                       | 275 ms: 1.26x faster                                                         |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 509 ms: 1.19x faster                                                         |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 507 ms: 1.15x faster                                                         |
| async_generators           | 457 ms                                                       | 411 ms: 1.11x faster                                                         |
| coroutines                 | 21.6 ms                                                      | 21.2 ms: 1.02x faster                                                        |
| Geometric mean             | (ref)                                                        | 1.22x faster                                                                 |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250406-pythonperf2-x86_64-python-7bb1e1a23634bae81bf7-3.14.0a6+-7bb1e1a |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 81.3 ms                                                      | 69.1 ms: 1.18x faster                                                        |
| pidigits       | 252 ms                                                       | 253 ms: 1.00x slower                                                         |
| nbody          | 89.3 ms                                                      | 93.9 ms: 1.05x slower                                                        |
| Geometric mean | (ref)                                                        | 1.04x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250406-pythonperf2-x86_64-python-7bb1e1a23634bae81bf7-3.14.0a6+-7bb1e1a |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_effbot   | 3.67 ms                                                      | 3.03 ms: 1.21x faster                                                        |
| regex_v8       | 26.1 ms                                                      | 24.4 ms: 1.07x faster                                                        |
| regex_compile  | 143 ms                                                       | 134 ms: 1.07x faster                                                         |
| regex_dna      | 247 ms                                                       | 232 ms: 1.06x faster                                                         |
| Geometric mean | (ref)                                                        | 1.10x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250406-pythonperf2-x86_64-python-7bb1e1a23634bae81bf7-3.14.0a6+-7bb1e1a |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| tomli_loads          | 2.46 sec                                                     | 2.05 sec: 1.20x faster                                                       |
| xml_etree_parse      | 150 ms                                                       | 135 ms: 1.11x faster                                                         |
| xml_etree_iterparse  | 103 ms                                                       | 95.5 ms: 1.08x faster                                                        |
| xml_etree_generate   | 86.5 ms                                                      | 84.3 ms: 1.03x faster                                                        |
| xml_etree_process    | 61.2 ms                                                      | 59.6 ms: 1.03x faster                                                        |
| unpickle_pure_python | 217 us                                                       | 215 us: 1.01x faster                                                         |
| json_dumps           | 11.1 ms                                                      | 11.3 ms: 1.02x slower                                                        |
| pickle_pure_python   | 323 us                                                       | 332 us: 1.03x slower                                                         |
| json_loads           | 24.7 us                                                      | 26.7 us: 1.08x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.03x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250406-pythonperf2-x86_64-python-7bb1e1a23634bae81bf7-3.14.0a6+-7bb1e1a |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 15.9 ms                                                      | 16.4 ms: 1.03x slower                                                        |
| python_startup_no_site | 8.96 ms                                                      | 10.5 ms: 1.17x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.10x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250406-pythonperf2-x86_64-python-7bb1e1a23634bae81bf7-3.14.0a6+-7bb1e1a |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| genshi_text     | 26.2 ms                                                      | 23.8 ms: 1.10x faster                                                        |
| genshi_xml      | 57.1 ms                                                      | 52.8 ms: 1.08x faster                                                        |
| django_template | 36.4 ms                                                      | 35.8 ms: 1.01x faster                                                        |
| mako            | 10.4 ms                                                      | 10.9 ms: 1.05x slower                                                        |
| Geometric mean  | (ref)                                                        | 1.04x faster                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250406-pythonperf2-x86_64-python-7bb1e1a23634bae81bf7-3.14.0a6+-7bb1e1a |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mdp                        | 2.54 sec                                                     | 1.29 sec: 1.97x faster                                                       |
| deepcopy                   | 392 us                                                       | 281 us: 1.40x faster                                                         |
| async_tree_memoization_tg  | 466 ms                                                       | 335 ms: 1.39x faster                                                         |
| deepcopy_memo              | 38.6 us                                                      | 28.0 us: 1.38x faster                                                        |
| async_tree_memoization     | 453 ms                                                       | 328 ms: 1.38x faster                                                         |
| async_tree_io              | 843 ms                                                       | 629 ms: 1.34x faster                                                         |
| async_tree_none            | 376 ms                                                       | 284 ms: 1.32x faster                                                         |
| go                         | 162 ms                                                       | 124 ms: 1.31x faster                                                         |
| async_tree_io_tg           | 831 ms                                                       | 636 ms: 1.31x faster                                                         |
| async_tree_none_tg         | 346 ms                                                       | 275 ms: 1.26x faster                                                         |
| deepcopy_reduce            | 3.54 us                                                      | 2.90 us: 1.22x faster                                                        |
| regex_effbot               | 3.67 ms                                                      | 3.03 ms: 1.21x faster                                                        |
| tomli_loads                | 2.46 sec                                                     | 2.05 sec: 1.20x faster                                                       |
| generators                 | 33.6 ms                                                      | 28.1 ms: 1.20x faster                                                        |
| pyflate                    | 503 ms                                                       | 422 ms: 1.19x faster                                                         |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 509 ms: 1.19x faster                                                         |
| float                      | 81.3 ms                                                      | 69.1 ms: 1.18x faster                                                        |
| scimark_sor                | 123 ms                                                       | 105 ms: 1.17x faster                                                         |
| richards                   | 52.9 ms                                                      | 46.1 ms: 1.15x faster                                                        |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 507 ms: 1.15x faster                                                         |
| richards_super             | 59.6 ms                                                      | 52.4 ms: 1.14x faster                                                        |
| telco                      | 8.79 ms                                                      | 7.85 ms: 1.12x faster                                                        |
| scimark_monte_carlo        | 66.1 ms                                                      | 59.4 ms: 1.11x faster                                                        |
| spectral_norm              | 97.0 ms                                                      | 87.3 ms: 1.11x faster                                                        |
| xml_etree_parse            | 150 ms                                                       | 135 ms: 1.11x faster                                                         |
| async_generators           | 457 ms                                                       | 411 ms: 1.11x faster                                                         |
| html5lib                   | 73.5 ms                                                      | 66.4 ms: 1.11x faster                                                        |
| genshi_text                | 26.2 ms                                                      | 23.8 ms: 1.10x faster                                                        |
| dulwich_log                | 68.2 ms                                                      | 62.4 ms: 1.09x faster                                                        |
| bpe_tokeniser              | 5.09 sec                                                     | 4.67 sec: 1.09x faster                                                       |
| scimark_fft                | 328 ms                                                       | 303 ms: 1.08x faster                                                         |
| pylint                     | 347 ms                                                       | 320 ms: 1.08x faster                                                         |
| pprint_safe_repr           | 843 ms                                                       | 779 ms: 1.08x faster                                                         |
| genshi_xml                 | 57.1 ms                                                      | 52.8 ms: 1.08x faster                                                        |
| pprint_pformat             | 1.72 sec                                                     | 1.59 sec: 1.08x faster                                                       |
| xml_etree_iterparse        | 103 ms                                                       | 95.5 ms: 1.08x faster                                                        |
| regex_v8                   | 26.1 ms                                                      | 24.4 ms: 1.07x faster                                                        |
| regex_compile              | 143 ms                                                       | 134 ms: 1.07x faster                                                         |
| 2to3                       | 293 ms                                                       | 275 ms: 1.07x faster                                                         |
| hexiom                     | 6.55 ms                                                      | 6.16 ms: 1.06x faster                                                        |
| regex_dna                  | 247 ms                                                       | 232 ms: 1.06x faster                                                         |
| sympy_integrate            | 23.6 ms                                                      | 22.2 ms: 1.06x faster                                                        |
| logging_silent             | 97.9 ns                                                      | 92.9 ns: 1.05x faster                                                        |
| deltablue                  | 3.42 ms                                                      | 3.25 ms: 1.05x faster                                                        |
| sympy_expand               | 509 ms                                                       | 488 ms: 1.04x faster                                                         |
| logging_simple             | 6.39 us                                                      | 6.13 us: 1.04x faster                                                        |
| connected_components       | 432 ms                                                       | 415 ms: 1.04x faster                                                         |
| sympy_str                  | 298 ms                                                       | 286 ms: 1.04x faster                                                         |
| shortest_path              | 460 ms                                                       | 444 ms: 1.04x faster                                                         |
| json                       | 5.69 ms                                                      | 5.50 ms: 1.03x faster                                                        |
| sqlite_synth               | 2.91 us                                                      | 2.82 us: 1.03x faster                                                        |
| chaos                      | 60.2 ms                                                      | 58.5 ms: 1.03x faster                                                        |
| xml_etree_generate         | 86.5 ms                                                      | 84.3 ms: 1.03x faster                                                        |
| meteor_contest             | 130 ms                                                       | 126 ms: 1.03x faster                                                         |
| xml_etree_process          | 61.2 ms                                                      | 59.6 ms: 1.03x faster                                                        |
| k_core                     | 2.17 sec                                                     | 2.11 sec: 1.03x faster                                                       |
| sphinx                     | 1.12 sec                                                     | 1.10 sec: 1.02x faster                                                       |
| logging_format             | 6.94 us                                                      | 6.81 us: 1.02x faster                                                        |
| coroutines                 | 21.6 ms                                                      | 21.2 ms: 1.02x faster                                                        |
| sqlalchemy_declarative     | 148 ms                                                       | 146 ms: 1.02x faster                                                         |
| pycparser                  | 1.24 sec                                                     | 1.22 sec: 1.02x faster                                                       |
| django_template            | 36.4 ms                                                      | 35.8 ms: 1.01x faster                                                        |
| sympy_sum                  | 155 ms                                                       | 153 ms: 1.01x faster                                                         |
| pathlib                    | 17.5 ms                                                      | 17.3 ms: 1.01x faster                                                        |
| unpickle_pure_python       | 217 us                                                       | 215 us: 1.01x faster                                                         |
| sqlalchemy_imperative      | 18.3 ms                                                      | 18.1 ms: 1.01x faster                                                        |
| pidigits                   | 252 ms                                                       | 253 ms: 1.00x slower                                                         |
| docutils                   | 2.83 sec                                                     | 2.86 sec: 1.01x slower                                                       |
| typing_runtime_protocols   | 169 us                                                       | 171 us: 1.01x slower                                                         |
| json_dumps                 | 11.1 ms                                                      | 11.3 ms: 1.02x slower                                                        |
| comprehensions             | 17.0 us                                                      | 17.4 us: 1.02x slower                                                        |
| fannkuch                   | 363 ms                                                       | 371 ms: 1.02x slower                                                         |
| pickle_pure_python         | 323 us                                                       | 332 us: 1.03x slower                                                         |
| bench_thread_pool          | 942 us                                                       | 968 us: 1.03x slower                                                         |
| nqueens                    | 90.7 ms                                                      | 93.7 ms: 1.03x slower                                                        |
| python_startup             | 15.9 ms                                                      | 16.4 ms: 1.03x slower                                                        |
| create_gc_cycles           | 2.68 ms                                                      | 2.79 ms: 1.04x slower                                                        |
| nbody                      | 89.3 ms                                                      | 93.9 ms: 1.05x slower                                                        |
| mako                       | 10.4 ms                                                      | 10.9 ms: 1.05x slower                                                        |
| crypto_pyaes               | 73.3 ms                                                      | 79.1 ms: 1.08x slower                                                        |
| json_loads                 | 24.7 us                                                      | 26.7 us: 1.08x slower                                                        |
| many_optionals             | 930 us                                                       | 1.01 ms: 1.09x slower                                                        |
| python_startup_no_site     | 8.96 ms                                                      | 10.5 ms: 1.17x slower                                                        |
| subparsers                 | 17.5 ms                                                      | 22.8 ms: 1.31x slower                                                        |
| gc_traversal               | 4.74 ms                                                      | 6.39 ms: 1.35x slower                                                        |
| bench_mp_pool              | 5.12 ms                                                      | 1.19 sec: 232.87x slower                                                     |
| Geometric mean             | (ref)                                                        | 1.01x faster                                                                 |

Benchmark hidden because not significant (5): scimark_lu, coverage, scimark_sparse_mat_mult, asyncio_websockets, raytrace
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
Ignored benchmarks (4) of results/bm-20250406-3.14.0a6+-7bb1e1a/bm-20250406-pythonperf2-x86_64-python-7bb1e1a23634bae81bf7-3.14.0a6+-7bb1e1a.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.071x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 1.03x
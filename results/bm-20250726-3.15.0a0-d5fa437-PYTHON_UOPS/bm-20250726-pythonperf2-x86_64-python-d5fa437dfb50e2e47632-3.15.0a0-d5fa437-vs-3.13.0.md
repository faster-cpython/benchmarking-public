# Results vs. 3.13.0

- fork: python
- ref: d5fa437dfb50e2e47632
- machine: linux-x86_64
- commit hash: d5fa437
- commit date: 2025-07-26
- overall geometric mean: 1.120x slower
- HPT reliability: 99.67%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.11x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250726-pythonperf2-x86_64-python-d5fa437dfb50e2e47632-3.15.0a0-d5fa437 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 324 ms: 1.11x slower                                                        |
| docutils       | 2.83 sec                                                     | 3.13 sec: 1.11x slower                                                      |
| html5lib       | 73.5 ms                                                      | 75.4 ms: 1.03x slower                                                       |
| Geometric mean | (ref)                                                        | 1.06x slower                                                                |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250726-pythonperf2-x86_64-python-d5fa437dfb50e2e47632-3.15.0a0-d5fa437 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 466 ms                                                       | 351 ms: 1.33x faster                                                        |
| async_tree_io              | 843 ms                                                       | 664 ms: 1.27x faster                                                        |
| async_tree_memoization     | 453 ms                                                       | 360 ms: 1.26x faster                                                        |
| async_tree_io_tg           | 831 ms                                                       | 668 ms: 1.25x faster                                                        |
| async_tree_none            | 376 ms                                                       | 304 ms: 1.24x faster                                                        |
| async_tree_none_tg         | 346 ms                                                       | 288 ms: 1.20x faster                                                        |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 530 ms: 1.14x faster                                                        |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 527 ms: 1.10x faster                                                        |
| asyncio_websockets         | 388 ms                                                       | 381 ms: 1.02x faster                                                        |
| coroutines                 | 21.6 ms                                                      | 22.2 ms: 1.03x slower                                                       |
| Geometric mean             | (ref)                                                        | 1.16x faster                                                                |

Benchmark hidden because not significant (1): async_generators

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250726-pythonperf2-x86_64-python-d5fa437dfb50e2e47632-3.15.0a0-d5fa437 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pidigits       | 252 ms                                                       | 256 ms: 1.01x slower                                                        |
| float          | 81.3 ms                                                      | 105 ms: 1.29x slower                                                        |
| nbody          | 89.3 ms                                                      | 184 ms: 2.06x slower                                                        |
| Geometric mean | (ref)                                                        | 1.39x slower                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250726-pythonperf2-x86_64-python-d5fa437dfb50e2e47632-3.15.0a0-d5fa437 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_dna      | 247 ms                                                       | 222 ms: 1.11x faster                                                        |
| regex_effbot   | 3.67 ms                                                      | 3.44 ms: 1.07x faster                                                       |
| regex_v8       | 26.1 ms                                                      | 24.7 ms: 1.06x faster                                                       |
| regex_compile  | 143 ms                                                       | 159 ms: 1.12x slower                                                        |
| Geometric mean | (ref)                                                        | 1.03x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250726-pythonperf2-x86_64-python-d5fa437dfb50e2e47632-3.15.0a0-d5fa437 |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_parse      | 150 ms                                                       | 142 ms: 1.06x faster                                                        |
| xml_etree_iterparse  | 103 ms                                                       | 109 ms: 1.06x slower                                                        |
| json_loads           | 24.7 us                                                      | 26.4 us: 1.07x slower                                                       |
| xml_etree_process    | 61.2 ms                                                      | 75.1 ms: 1.23x slower                                                       |
| xml_etree_generate   | 86.5 ms                                                      | 107 ms: 1.24x slower                                                        |
| tomli_loads          | 2.46 sec                                                     | 3.11 sec: 1.26x slower                                                      |
| pickle_pure_python   | 323 us                                                       | 410 us: 1.27x slower                                                        |
| unpickle_pure_python | 217 us                                                       | 387 us: 1.78x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.19x slower                                                                |

Benchmark hidden because not significant (1): json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250726-pythonperf2-x86_64-python-d5fa437dfb50e2e47632-3.15.0a0-d5fa437 |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 15.9 ms                                                      | 15.4 ms: 1.04x faster                                                       |
| python_startup_no_site | 8.96 ms                                                      | 8.81 ms: 1.02x faster                                                       |
| Geometric mean         | (ref)                                                        | 1.03x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250726-pythonperf2-x86_64-python-d5fa437dfb50e2e47632-3.15.0a0-d5fa437 |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_text     | 26.2 ms                                                      | 24.0 ms: 1.09x faster                                                       |
| django_template | 36.4 ms                                                      | 35.3 ms: 1.03x faster                                                       |
| genshi_xml      | 57.1 ms                                                      | 56.6 ms: 1.01x faster                                                       |
| mako            | 10.4 ms                                                      | 17.1 ms: 1.65x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.10x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250726-pythonperf2-x86_64-python-d5fa437dfb50e2e47632-3.15.0a0-d5fa437 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mdp                        | 2.54 sec                                                     | 1.47 sec: 1.73x faster                                                      |
| deepcopy                   | 392 us                                                       | 283 us: 1.39x faster                                                        |
| deepcopy_memo              | 38.6 us                                                      | 27.9 us: 1.39x faster                                                       |
| async_tree_memoization_tg  | 466 ms                                                       | 351 ms: 1.33x faster                                                        |
| async_tree_io              | 843 ms                                                       | 664 ms: 1.27x faster                                                        |
| async_tree_memoization     | 453 ms                                                       | 360 ms: 1.26x faster                                                        |
| async_tree_io_tg           | 831 ms                                                       | 668 ms: 1.25x faster                                                        |
| async_tree_none            | 376 ms                                                       | 304 ms: 1.24x faster                                                        |
| deepcopy_reduce            | 3.54 us                                                      | 2.92 us: 1.21x faster                                                       |
| async_tree_none_tg         | 346 ms                                                       | 288 ms: 1.20x faster                                                        |
| scimark_sor                | 123 ms                                                       | 103 ms: 1.20x faster                                                        |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 530 ms: 1.14x faster                                                        |
| regex_dna                  | 247 ms                                                       | 222 ms: 1.11x faster                                                        |
| generators                 | 33.6 ms                                                      | 30.4 ms: 1.11x faster                                                       |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 527 ms: 1.10x faster                                                        |
| dulwich_log                | 68.2 ms                                                      | 61.8 ms: 1.10x faster                                                       |
| genshi_text                | 26.2 ms                                                      | 24.0 ms: 1.09x faster                                                       |
| regex_effbot               | 3.67 ms                                                      | 3.44 ms: 1.07x faster                                                       |
| logging_silent             | 97.9 ns                                                      | 92.3 ns: 1.06x faster                                                       |
| thrift                     | 901 us                                                       | 849 us: 1.06x faster                                                        |
| regex_v8                   | 26.1 ms                                                      | 24.7 ms: 1.06x faster                                                       |
| xml_etree_parse            | 150 ms                                                       | 142 ms: 1.06x faster                                                        |
| scimark_lu                 | 98.7 ms                                                      | 93.9 ms: 1.05x faster                                                       |
| json                       | 5.69 ms                                                      | 5.42 ms: 1.05x faster                                                       |
| pathlib                    | 17.5 ms                                                      | 16.9 ms: 1.04x faster                                                       |
| logging_simple             | 6.39 us                                                      | 6.17 us: 1.04x faster                                                       |
| python_startup             | 15.9 ms                                                      | 15.4 ms: 1.04x faster                                                       |
| django_template            | 36.4 ms                                                      | 35.3 ms: 1.03x faster                                                       |
| logging_format             | 6.94 us                                                      | 6.77 us: 1.03x faster                                                       |
| asyncio_websockets         | 388 ms                                                       | 381 ms: 1.02x faster                                                        |
| python_startup_no_site     | 8.96 ms                                                      | 8.81 ms: 1.02x faster                                                       |
| genshi_xml                 | 57.1 ms                                                      | 56.6 ms: 1.01x faster                                                       |
| coverage                   | 80.0 ms                                                      | 79.5 ms: 1.01x faster                                                       |
| richards_super             | 59.6 ms                                                      | 60.2 ms: 1.01x slower                                                       |
| sympy_integrate            | 23.6 ms                                                      | 23.8 ms: 1.01x slower                                                       |
| pidigits                   | 252 ms                                                       | 256 ms: 1.01x slower                                                        |
| richards                   | 52.9 ms                                                      | 54.0 ms: 1.02x slower                                                       |
| sqlite_synth               | 2.91 us                                                      | 2.98 us: 1.03x slower                                                       |
| html5lib                   | 73.5 ms                                                      | 75.4 ms: 1.03x slower                                                       |
| coroutines                 | 21.6 ms                                                      | 22.2 ms: 1.03x slower                                                       |
| chaos                      | 60.2 ms                                                      | 62.3 ms: 1.04x slower                                                       |
| sympy_sum                  | 155 ms                                                       | 163 ms: 1.05x slower                                                        |
| k_core                     | 2.17 sec                                                     | 2.29 sec: 1.05x slower                                                      |
| sympy_str                  | 298 ms                                                       | 316 ms: 1.06x slower                                                        |
| xml_etree_iterparse        | 103 ms                                                       | 109 ms: 1.06x slower                                                        |
| json_loads                 | 24.7 us                                                      | 26.4 us: 1.07x slower                                                       |
| create_gc_cycles           | 2.68 ms                                                      | 2.88 ms: 1.07x slower                                                       |
| sympy_expand               | 509 ms                                                       | 549 ms: 1.08x slower                                                        |
| shortest_path              | 460 ms                                                       | 506 ms: 1.10x slower                                                        |
| docutils                   | 2.83 sec                                                     | 3.13 sec: 1.11x slower                                                      |
| 2to3                       | 293 ms                                                       | 324 ms: 1.11x slower                                                        |
| regex_compile              | 143 ms                                                       | 159 ms: 1.12x slower                                                        |
| nqueens                    | 90.7 ms                                                      | 101 ms: 1.12x slower                                                        |
| connected_components       | 432 ms                                                       | 491 ms: 1.14x slower                                                        |
| raytrace                   | 273 ms                                                       | 325 ms: 1.19x slower                                                        |
| typing_runtime_protocols   | 169 us                                                       | 202 us: 1.20x slower                                                        |
| pycparser                  | 1.24 sec                                                     | 1.49 sec: 1.20x slower                                                      |
| xml_etree_process          | 61.2 ms                                                      | 75.1 ms: 1.23x slower                                                       |
| meteor_contest             | 130 ms                                                       | 160 ms: 1.24x slower                                                        |
| xml_etree_generate         | 86.5 ms                                                      | 107 ms: 1.24x slower                                                        |
| pyflate                    | 503 ms                                                       | 628 ms: 1.25x slower                                                        |
| tomli_loads                | 2.46 sec                                                     | 3.11 sec: 1.26x slower                                                      |
| pickle_pure_python         | 323 us                                                       | 410 us: 1.27x slower                                                        |
| bpe_tokeniser              | 5.09 sec                                                     | 6.47 sec: 1.27x slower                                                      |
| float                      | 81.3 ms                                                      | 105 ms: 1.29x slower                                                        |
| pprint_pformat             | 1.72 sec                                                     | 2.26 sec: 1.32x slower                                                      |
| pprint_safe_repr           | 843 ms                                                       | 1.12 sec: 1.33x slower                                                      |
| go                         | 162 ms                                                       | 219 ms: 1.35x slower                                                        |
| scimark_monte_carlo        | 66.1 ms                                                      | 89.5 ms: 1.35x slower                                                       |
| gc_traversal               | 4.74 ms                                                      | 6.48 ms: 1.37x slower                                                       |
| many_optionals             | 930 us                                                       | 1.28 ms: 1.37x slower                                                       |
| scimark_fft                | 328 ms                                                       | 465 ms: 1.42x slower                                                        |
| crypto_pyaes               | 73.3 ms                                                      | 106 ms: 1.44x slower                                                        |
| hexiom                     | 6.55 ms                                                      | 10.7 ms: 1.63x slower                                                       |
| mako                       | 10.4 ms                                                      | 17.1 ms: 1.65x slower                                                       |
| fannkuch                   | 363 ms                                                       | 618 ms: 1.70x slower                                                        |
| spectral_norm              | 97.0 ms                                                      | 167 ms: 1.72x slower                                                        |
| deltablue                  | 3.42 ms                                                      | 5.96 ms: 1.75x slower                                                       |
| scimark_sparse_mat_mult    | 4.77 ms                                                      | 8.41 ms: 1.76x slower                                                       |
| comprehensions             | 17.0 us                                                      | 30.3 us: 1.78x slower                                                       |
| unpickle_pure_python       | 217 us                                                       | 387 us: 1.78x slower                                                        |
| nbody                      | 89.3 ms                                                      | 184 ms: 2.06x slower                                                        |
| subparsers                 | 17.5 ms                                                      | 43.5 ms: 2.49x slower                                                       |
| telco                      | 8.79 ms                                                      | 158 ms: 18.01x slower                                                       |
| Geometric mean             | (ref)                                                        | 1.13x slower                                                                |

Benchmark hidden because not significant (5): pylint, djangocms, async_generators, json_dumps, sphinx
Ignored benchmarks (12) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: bench_mp_pool, bench_thread_pool, chameleon, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250726-3.15.0a0-d5fa437-PYTHON_UOPS/bm-20250726-pythonperf2-x86_64-python-d5fa437dfb50e2e47632-3.15.0a0-d5fa437.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.120x slower

# HPT report

- Reliability score: 99.67% likely to be slow
- 90% likely to have a slowdown of 1.03x
- 95% likely to have a slowdown of 1.02x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.11x
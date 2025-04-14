# Results vs. 3.13.0

- fork: python
- ref: c3ae5c9e4ad121f8ba60
- machine: linux-x86_64
- commit hash: c3ae5c9
- commit date: 2025-01-31
- overall geometric mean: 1.070x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250131-pythonperf2-x86_64-python-c3ae5c9e4ad121f8ba60-3.14.0a4+-c3ae5c9 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 279 ms: 1.05x faster                                                         |
| docutils       | 2.83 sec                                                     | 2.85 sec: 1.01x slower                                                       |
| html5lib       | 73.5 ms                                                      | 66.3 ms: 1.11x faster                                                        |
| sphinx         | 1.12 sec                                                     | 1.10 sec: 1.03x faster                                                       |
| Geometric mean | (ref)                                                        | 1.04x faster                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250131-pythonperf2-x86_64-python-c3ae5c9e4ad121f8ba60-3.14.0a4+-c3ae5c9 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 466 ms                                                       | 338 ms: 1.38x faster                                                         |
| async_tree_none            | 376 ms                                                       | 286 ms: 1.31x faster                                                         |
| async_tree_memoization     | 453 ms                                                       | 349 ms: 1.30x faster                                                         |
| async_tree_io              | 843 ms                                                       | 651 ms: 1.29x faster                                                         |
| async_tree_io_tg           | 831 ms                                                       | 643 ms: 1.29x faster                                                         |
| async_tree_none_tg         | 346 ms                                                       | 279 ms: 1.24x faster                                                         |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 517 ms: 1.17x faster                                                         |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 510 ms: 1.14x faster                                                         |
| async_generators           | 457 ms                                                       | 404 ms: 1.13x faster                                                         |
| coroutines                 | 21.6 ms                                                      | 20.8 ms: 1.04x faster                                                        |
| Geometric mean             | (ref)                                                        | 1.20x faster                                                                 |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250131-pythonperf2-x86_64-python-c3ae5c9e4ad121f8ba60-3.14.0a4+-c3ae5c9 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 81.3 ms                                                      | 69.7 ms: 1.17x faster                                                        |
| nbody          | 89.3 ms                                                      | 87.2 ms: 1.02x faster                                                        |
| pidigits       | 252 ms                                                       | 254 ms: 1.01x slower                                                         |
| Geometric mean | (ref)                                                        | 1.06x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250131-pythonperf2-x86_64-python-c3ae5c9e4ad121f8ba60-3.14.0a4+-c3ae5c9 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_effbot   | 3.67 ms                                                      | 3.20 ms: 1.15x faster                                                        |
| regex_compile  | 143 ms                                                       | 134 ms: 1.07x faster                                                         |
| regex_dna      | 247 ms                                                       | 238 ms: 1.04x faster                                                         |
| Geometric mean | (ref)                                                        | 1.06x faster                                                                 |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250131-pythonperf2-x86_64-python-c3ae5c9e4ad121f8ba60-3.14.0a4+-c3ae5c9 |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| tomli_loads          | 2.46 sec                                                     | 1.99 sec: 1.24x faster                                                       |
| xml_etree_parse      | 150 ms                                                       | 136 ms: 1.10x faster                                                         |
| unpickle_pure_python | 217 us                                                       | 205 us: 1.06x faster                                                         |
| xml_etree_iterparse  | 103 ms                                                       | 97.2 ms: 1.06x faster                                                        |
| xml_etree_process    | 61.2 ms                                                      | 57.9 ms: 1.06x faster                                                        |
| xml_etree_generate   | 86.5 ms                                                      | 82.9 ms: 1.04x faster                                                        |
| pickle_pure_python   | 323 us                                                       | 327 us: 1.01x slower                                                         |
| json_dumps           | 11.1 ms                                                      | 11.6 ms: 1.04x slower                                                        |
| json_loads           | 24.7 us                                                      | 26.4 us: 1.07x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.05x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250131-pythonperf2-x86_64-python-c3ae5c9e4ad121f8ba60-3.14.0a4+-c3ae5c9 |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 8.96 ms                                                      | 9.00 ms: 1.01x slower                                                        |
| python_startup         | 15.9 ms                                                      | 16.0 ms: 1.01x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.01x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250131-pythonperf2-x86_64-python-c3ae5c9e4ad121f8ba60-3.14.0a4+-c3ae5c9 |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| genshi_text     | 26.2 ms                                                      | 22.6 ms: 1.16x faster                                                        |
| genshi_xml      | 57.1 ms                                                      | 53.0 ms: 1.08x faster                                                        |
| django_template | 36.4 ms                                                      | 34.9 ms: 1.04x faster                                                        |
| mako            | 10.4 ms                                                      | 10.7 ms: 1.03x slower                                                        |
| Geometric mean  | (ref)                                                        | 1.06x faster                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250131-pythonperf2-x86_64-python-c3ae5c9e4ad121f8ba60-3.14.0a4+-c3ae5c9 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| deepcopy                   | 392 us                                                       | 281 us: 1.39x faster                                                         |
| async_tree_memoization_tg  | 466 ms                                                       | 338 ms: 1.38x faster                                                         |
| go                         | 162 ms                                                       | 124 ms: 1.31x faster                                                         |
| async_tree_none            | 376 ms                                                       | 286 ms: 1.31x faster                                                         |
| deepcopy_memo              | 38.6 us                                                      | 29.7 us: 1.30x faster                                                        |
| async_tree_memoization     | 453 ms                                                       | 349 ms: 1.30x faster                                                         |
| async_tree_io              | 843 ms                                                       | 651 ms: 1.29x faster                                                         |
| async_tree_io_tg           | 831 ms                                                       | 643 ms: 1.29x faster                                                         |
| async_tree_none_tg         | 346 ms                                                       | 279 ms: 1.24x faster                                                         |
| tomli_loads                | 2.46 sec                                                     | 1.99 sec: 1.24x faster                                                       |
| deepcopy_reduce            | 3.54 us                                                      | 2.90 us: 1.22x faster                                                        |
| pyflate                    | 503 ms                                                       | 429 ms: 1.17x faster                                                         |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 517 ms: 1.17x faster                                                         |
| float                      | 81.3 ms                                                      | 69.7 ms: 1.17x faster                                                        |
| richards                   | 52.9 ms                                                      | 45.5 ms: 1.16x faster                                                        |
| genshi_text                | 26.2 ms                                                      | 22.6 ms: 1.16x faster                                                        |
| generators                 | 33.6 ms                                                      | 29.0 ms: 1.16x faster                                                        |
| richards_super             | 59.6 ms                                                      | 51.5 ms: 1.16x faster                                                        |
| regex_effbot               | 3.67 ms                                                      | 3.20 ms: 1.15x faster                                                        |
| spectral_norm              | 97.0 ms                                                      | 84.5 ms: 1.15x faster                                                        |
| scimark_sor                | 123 ms                                                       | 108 ms: 1.14x faster                                                         |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 510 ms: 1.14x faster                                                         |
| async_generators           | 457 ms                                                       | 404 ms: 1.13x faster                                                         |
| pathlib                    | 17.5 ms                                                      | 15.6 ms: 1.12x faster                                                        |
| bpe_tokeniser              | 5.09 sec                                                     | 4.55 sec: 1.12x faster                                                       |
| telco                      | 8.79 ms                                                      | 7.86 ms: 1.12x faster                                                        |
| html5lib                   | 73.5 ms                                                      | 66.3 ms: 1.11x faster                                                        |
| pylint                     | 347 ms                                                       | 313 ms: 1.11x faster                                                         |
| xml_etree_parse            | 150 ms                                                       | 136 ms: 1.10x faster                                                         |
| hexiom                     | 6.55 ms                                                      | 5.97 ms: 1.10x faster                                                        |
| scimark_fft                | 328 ms                                                       | 302 ms: 1.09x faster                                                         |
| genshi_xml                 | 57.1 ms                                                      | 53.0 ms: 1.08x faster                                                        |
| pprint_safe_repr           | 843 ms                                                       | 783 ms: 1.08x faster                                                         |
| pprint_pformat             | 1.72 sec                                                     | 1.60 sec: 1.07x faster                                                       |
| regex_compile              | 143 ms                                                       | 134 ms: 1.07x faster                                                         |
| scimark_monte_carlo        | 66.1 ms                                                      | 62.0 ms: 1.07x faster                                                        |
| unpickle_pure_python       | 217 us                                                       | 205 us: 1.06x faster                                                         |
| nqueens                    | 90.7 ms                                                      | 85.7 ms: 1.06x faster                                                        |
| xml_etree_iterparse        | 103 ms                                                       | 97.2 ms: 1.06x faster                                                        |
| xml_etree_process          | 61.2 ms                                                      | 57.9 ms: 1.06x faster                                                        |
| sqlglot_parse              | 1.40 ms                                                      | 1.32 ms: 1.06x faster                                                        |
| sqlglot_normalize          | 119 ms                                                       | 113 ms: 1.06x faster                                                         |
| sqlglot_optimize           | 59.3 ms                                                      | 56.2 ms: 1.06x faster                                                        |
| sqlalchemy_declarative     | 148 ms                                                       | 141 ms: 1.05x faster                                                         |
| 2to3                       | 293 ms                                                       | 279 ms: 1.05x faster                                                         |
| meteor_contest             | 130 ms                                                       | 124 ms: 1.05x faster                                                         |
| thrift                     | 901 us                                                       | 860 us: 1.05x faster                                                         |
| sqlglot_transpile          | 1.79 ms                                                      | 1.71 ms: 1.05x faster                                                        |
| deltablue                  | 3.42 ms                                                      | 3.27 ms: 1.05x faster                                                        |
| connected_components       | 432 ms                                                       | 414 ms: 1.04x faster                                                         |
| scimark_lu                 | 98.7 ms                                                      | 94.6 ms: 1.04x faster                                                        |
| xml_etree_generate         | 86.5 ms                                                      | 82.9 ms: 1.04x faster                                                        |
| sympy_str                  | 298 ms                                                       | 286 ms: 1.04x faster                                                         |
| django_template            | 36.4 ms                                                      | 34.9 ms: 1.04x faster                                                        |
| mdp                        | 2.54 sec                                                     | 2.44 sec: 1.04x faster                                                       |
| sympy_expand               | 509 ms                                                       | 489 ms: 1.04x faster                                                         |
| coverage                   | 80.0 ms                                                      | 76.7 ms: 1.04x faster                                                        |
| shortest_path              | 460 ms                                                       | 442 ms: 1.04x faster                                                         |
| k_core                     | 2.17 sec                                                     | 2.08 sec: 1.04x faster                                                       |
| bench_thread_pool          | 942 us                                                       | 907 us: 1.04x faster                                                         |
| regex_dna                  | 247 ms                                                       | 238 ms: 1.04x faster                                                         |
| coroutines                 | 21.6 ms                                                      | 20.8 ms: 1.04x faster                                                        |
| sympy_sum                  | 155 ms                                                       | 149 ms: 1.04x faster                                                         |
| sqlite_synth               | 2.91 us                                                      | 2.81 us: 1.04x faster                                                        |
| sympy_integrate            | 23.6 ms                                                      | 22.8 ms: 1.03x faster                                                        |
| sqlalchemy_imperative      | 18.3 ms                                                      | 17.7 ms: 1.03x faster                                                        |
| dulwich_log                | 68.2 ms                                                      | 66.3 ms: 1.03x faster                                                        |
| json                       | 5.69 ms                                                      | 5.53 ms: 1.03x faster                                                        |
| scimark_sparse_mat_mult    | 4.77 ms                                                      | 4.65 ms: 1.03x faster                                                        |
| comprehensions             | 17.0 us                                                      | 16.6 us: 1.03x faster                                                        |
| logging_simple             | 6.39 us                                                      | 6.23 us: 1.03x faster                                                        |
| sphinx                     | 1.12 sec                                                     | 1.10 sec: 1.03x faster                                                       |
| nbody                      | 89.3 ms                                                      | 87.2 ms: 1.02x faster                                                        |
| chaos                      | 60.2 ms                                                      | 59.0 ms: 1.02x faster                                                        |
| logging_format             | 6.94 us                                                      | 6.84 us: 1.01x faster                                                        |
| logging_silent             | 97.9 ns                                                      | 96.8 ns: 1.01x faster                                                        |
| typing_runtime_protocols   | 169 us                                                       | 167 us: 1.01x faster                                                         |
| raytrace                   | 273 ms                                                       | 271 ms: 1.01x faster                                                         |
| crypto_pyaes               | 73.3 ms                                                      | 73.6 ms: 1.00x slower                                                        |
| python_startup_no_site     | 8.96 ms                                                      | 9.00 ms: 1.01x slower                                                        |
| fannkuch                   | 363 ms                                                       | 365 ms: 1.01x slower                                                         |
| python_startup             | 15.9 ms                                                      | 16.0 ms: 1.01x slower                                                        |
| pidigits                   | 252 ms                                                       | 254 ms: 1.01x slower                                                         |
| docutils                   | 2.83 sec                                                     | 2.85 sec: 1.01x slower                                                       |
| pickle_pure_python         | 323 us                                                       | 327 us: 1.01x slower                                                         |
| mako                       | 10.4 ms                                                      | 10.7 ms: 1.03x slower                                                        |
| json_dumps                 | 11.1 ms                                                      | 11.6 ms: 1.04x slower                                                        |
| create_gc_cycles           | 2.68 ms                                                      | 2.82 ms: 1.05x slower                                                        |
| json_loads                 | 24.7 us                                                      | 26.4 us: 1.07x slower                                                        |
| many_optionals             | 930 us                                                       | 1000 us: 1.07x slower                                                        |
| subparsers                 | 17.5 ms                                                      | 22.4 ms: 1.28x slower                                                        |
| gc_traversal               | 4.74 ms                                                      | 6.55 ms: 1.38x slower                                                        |
| bench_mp_pool              | 5.12 ms                                                      | 993 ms: 193.83x slower                                                       |
| Geometric mean             | (ref)                                                        | 1.01x faster                                                                 |

Benchmark hidden because not significant (3): regex_v8, pycparser, asyncio_websockets
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http

- Geometric mean (including insignificant results): 1.070x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: 1.02x
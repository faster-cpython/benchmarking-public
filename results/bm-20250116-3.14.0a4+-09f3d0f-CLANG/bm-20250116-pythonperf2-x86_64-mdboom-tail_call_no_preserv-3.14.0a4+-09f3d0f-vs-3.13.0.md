# Results vs. 3.13.0

- fork: mdboom
- ref: tail_call_no_preserv
- machine: linux-x86_64
- commit hash: 09f3d0f
- commit date: 2025-01-16
- overall geometric mean: 1.059x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250116-pythonperf2-x86_64-mdboom-tail_call_no_preserv-3.14.0a4+-09f3d0f |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 282 ms: 1.04x faster                                                         |
| docutils       | 2.83 sec                                                     | 2.89 sec: 1.02x slower                                                       |
| html5lib       | 73.5 ms                                                      | 67.0 ms: 1.10x faster                                                        |
| sphinx         | 1.12 sec                                                     | 1.10 sec: 1.02x faster                                                       |
| Geometric mean | (ref)                                                        | 1.03x faster                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250116-pythonperf2-x86_64-mdboom-tail_call_no_preserv-3.14.0a4+-09f3d0f |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 466 ms                                                       | 323 ms: 1.44x faster                                                         |
| async_tree_io              | 843 ms                                                       | 629 ms: 1.34x faster                                                         |
| async_tree_io_tg           | 831 ms                                                       | 621 ms: 1.34x faster                                                         |
| async_tree_none            | 376 ms                                                       | 283 ms: 1.33x faster                                                         |
| async_tree_memoization     | 453 ms                                                       | 347 ms: 1.31x faster                                                         |
| async_tree_none_tg         | 346 ms                                                       | 266 ms: 1.30x faster                                                         |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 522 ms: 1.11x faster                                                         |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 543 ms: 1.11x faster                                                         |
| async_generators           | 457 ms                                                       | 429 ms: 1.07x faster                                                         |
| asyncio_websockets         | 388 ms                                                       | 392 ms: 1.01x slower                                                         |
| coroutines                 | 21.6 ms                                                      | 22.3 ms: 1.03x slower                                                        |
| Geometric mean             | (ref)                                                        | 1.20x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250116-pythonperf2-x86_64-mdboom-tail_call_no_preserv-3.14.0a4+-09f3d0f |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 81.3 ms                                                      | 71.9 ms: 1.13x faster                                                        |
| pidigits       | 252 ms                                                       | 286 ms: 1.13x slower                                                         |
| Geometric mean | (ref)                                                        | 1.00x slower                                                                 |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250116-pythonperf2-x86_64-mdboom-tail_call_no_preserv-3.14.0a4+-09f3d0f |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_effbot   | 3.67 ms                                                      | 3.00 ms: 1.22x faster                                                        |
| regex_dna      | 247 ms                                                       | 223 ms: 1.11x faster                                                         |
| regex_compile  | 143 ms                                                       | 138 ms: 1.03x faster                                                         |
| regex_v8       | 26.1 ms                                                      | 27.2 ms: 1.04x slower                                                        |
| Geometric mean | (ref)                                                        | 1.08x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250116-pythonperf2-x86_64-mdboom-tail_call_no_preserv-3.14.0a4+-09f3d0f |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| tomli_loads          | 2.46 sec                                                     | 2.06 sec: 1.20x faster                                                       |
| xml_etree_generate   | 86.5 ms                                                      | 80.9 ms: 1.07x faster                                                        |
| xml_etree_process    | 61.2 ms                                                      | 57.6 ms: 1.06x faster                                                        |
| unpickle_pure_python | 217 us                                                       | 216 us: 1.01x faster                                                         |
| pickle_pure_python   | 323 us                                                       | 325 us: 1.01x slower                                                         |
| json_loads           | 24.7 us                                                      | 25.2 us: 1.02x slower                                                        |
| xml_etree_iterparse  | 103 ms                                                       | 105 ms: 1.02x slower                                                         |
| json_dumps           | 11.1 ms                                                      | 11.7 ms: 1.05x slower                                                        |
| xml_etree_parse      | 150 ms                                                       | 161 ms: 1.07x slower                                                         |
| Geometric mean       | (ref)                                                        | 1.02x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250116-pythonperf2-x86_64-mdboom-tail_call_no_preserv-3.14.0a4+-09f3d0f |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 15.9 ms                                                      | 16.0 ms: 1.01x slower                                                        |
| python_startup_no_site | 8.96 ms                                                      | 9.06 ms: 1.01x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.01x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250116-pythonperf2-x86_64-mdboom-tail_call_no_preserv-3.14.0a4+-09f3d0f |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| genshi_text     | 26.2 ms                                                      | 23.5 ms: 1.12x faster                                                        |
| genshi_xml      | 57.1 ms                                                      | 53.7 ms: 1.06x faster                                                        |
| django_template | 36.4 ms                                                      | 37.2 ms: 1.02x slower                                                        |
| mako            | 10.4 ms                                                      | 11.3 ms: 1.09x slower                                                        |
| Geometric mean  | (ref)                                                        | 1.02x faster                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250116-pythonperf2-x86_64-mdboom-tail_call_no_preserv-3.14.0a4+-09f3d0f |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 466 ms                                                       | 323 ms: 1.44x faster                                                         |
| deepcopy                   | 392 us                                                       | 279 us: 1.40x faster                                                         |
| async_tree_io              | 843 ms                                                       | 629 ms: 1.34x faster                                                         |
| async_tree_io_tg           | 831 ms                                                       | 621 ms: 1.34x faster                                                         |
| deepcopy_memo              | 38.6 us                                                      | 28.9 us: 1.34x faster                                                        |
| async_tree_none            | 376 ms                                                       | 283 ms: 1.33x faster                                                         |
| async_tree_memoization     | 453 ms                                                       | 347 ms: 1.31x faster                                                         |
| async_tree_none_tg         | 346 ms                                                       | 266 ms: 1.30x faster                                                         |
| go                         | 162 ms                                                       | 128 ms: 1.27x faster                                                         |
| deepcopy_reduce            | 3.54 us                                                      | 2.82 us: 1.26x faster                                                        |
| regex_effbot               | 3.67 ms                                                      | 3.00 ms: 1.22x faster                                                        |
| richards                   | 52.9 ms                                                      | 43.3 ms: 1.22x faster                                                        |
| scimark_fft                | 328 ms                                                       | 272 ms: 1.20x faster                                                         |
| tomli_loads                | 2.46 sec                                                     | 2.06 sec: 1.20x faster                                                       |
| richards_super             | 59.6 ms                                                      | 49.9 ms: 1.19x faster                                                        |
| scimark_sor                | 123 ms                                                       | 104 ms: 1.18x faster                                                         |
| pyflate                    | 503 ms                                                       | 431 ms: 1.17x faster                                                         |
| scimark_sparse_mat_mult    | 4.77 ms                                                      | 4.10 ms: 1.16x faster                                                        |
| scimark_monte_carlo        | 66.1 ms                                                      | 57.5 ms: 1.15x faster                                                        |
| float                      | 81.3 ms                                                      | 71.9 ms: 1.13x faster                                                        |
| genshi_text                | 26.2 ms                                                      | 23.5 ms: 1.12x faster                                                        |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 522 ms: 1.11x faster                                                         |
| pathlib                    | 17.5 ms                                                      | 15.8 ms: 1.11x faster                                                        |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 543 ms: 1.11x faster                                                         |
| scimark_lu                 | 98.7 ms                                                      | 89.2 ms: 1.11x faster                                                        |
| regex_dna                  | 247 ms                                                       | 223 ms: 1.11x faster                                                         |
| generators                 | 33.6 ms                                                      | 30.6 ms: 1.10x faster                                                        |
| html5lib                   | 73.5 ms                                                      | 67.0 ms: 1.10x faster                                                        |
| telco                      | 8.79 ms                                                      | 8.03 ms: 1.09x faster                                                        |
| thrift                     | 901 us                                                       | 827 us: 1.09x faster                                                         |
| json                       | 5.69 ms                                                      | 5.22 ms: 1.09x faster                                                        |
| logging_silent             | 97.9 ns                                                      | 89.9 ns: 1.09x faster                                                        |
| pylint                     | 347 ms                                                       | 319 ms: 1.09x faster                                                         |
| spectral_norm              | 97.0 ms                                                      | 90.0 ms: 1.08x faster                                                        |
| hexiom                     | 6.55 ms                                                      | 6.12 ms: 1.07x faster                                                        |
| xml_etree_generate         | 86.5 ms                                                      | 80.9 ms: 1.07x faster                                                        |
| async_generators           | 457 ms                                                       | 429 ms: 1.07x faster                                                         |
| genshi_xml                 | 57.1 ms                                                      | 53.7 ms: 1.06x faster                                                        |
| bpe_tokeniser              | 5.09 sec                                                     | 4.79 sec: 1.06x faster                                                       |
| xml_etree_process          | 61.2 ms                                                      | 57.6 ms: 1.06x faster                                                        |
| k_core                     | 2.17 sec                                                     | 2.05 sec: 1.05x faster                                                       |
| coverage                   | 80.0 ms                                                      | 75.9 ms: 1.05x faster                                                        |
| logging_simple             | 6.39 us                                                      | 6.10 us: 1.05x faster                                                        |
| dulwich_log                | 68.2 ms                                                      | 65.4 ms: 1.04x faster                                                        |
| sqlglot_parse              | 1.40 ms                                                      | 1.35 ms: 1.04x faster                                                        |
| pprint_pformat             | 1.72 sec                                                     | 1.65 sec: 1.04x faster                                                       |
| 2to3                       | 293 ms                                                       | 282 ms: 1.04x faster                                                         |
| regex_compile              | 143 ms                                                       | 138 ms: 1.03x faster                                                         |
| sqlalchemy_imperative      | 18.3 ms                                                      | 17.7 ms: 1.03x faster                                                        |
| pprint_safe_repr           | 843 ms                                                       | 817 ms: 1.03x faster                                                         |
| sqlglot_transpile          | 1.79 ms                                                      | 1.74 ms: 1.03x faster                                                        |
| sympy_sum                  | 155 ms                                                       | 150 ms: 1.03x faster                                                         |
| deltablue                  | 3.42 ms                                                      | 3.33 ms: 1.03x faster                                                        |
| sqlalchemy_declarative     | 148 ms                                                       | 145 ms: 1.02x faster                                                         |
| sqlite_synth               | 2.91 us                                                      | 2.84 us: 1.02x faster                                                        |
| sympy_integrate            | 23.6 ms                                                      | 23.0 ms: 1.02x faster                                                        |
| sympy_str                  | 298 ms                                                       | 292 ms: 1.02x faster                                                         |
| raytrace                   | 273 ms                                                       | 267 ms: 1.02x faster                                                         |
| sympy_expand               | 509 ms                                                       | 500 ms: 1.02x faster                                                         |
| sphinx                     | 1.12 sec                                                     | 1.10 sec: 1.02x faster                                                       |
| shortest_path              | 460 ms                                                       | 452 ms: 1.02x faster                                                         |
| logging_format             | 6.94 us                                                      | 6.83 us: 1.02x faster                                                        |
| unpickle_pure_python       | 217 us                                                       | 216 us: 1.01x faster                                                         |
| connected_components       | 432 ms                                                       | 430 ms: 1.01x faster                                                         |
| pickle_pure_python         | 323 us                                                       | 325 us: 1.01x slower                                                         |
| sqlglot_optimize           | 59.3 ms                                                      | 59.6 ms: 1.01x slower                                                        |
| fannkuch                   | 363 ms                                                       | 366 ms: 1.01x slower                                                         |
| python_startup             | 15.9 ms                                                      | 16.0 ms: 1.01x slower                                                        |
| asyncio_websockets         | 388 ms                                                       | 392 ms: 1.01x slower                                                         |
| python_startup_no_site     | 8.96 ms                                                      | 9.06 ms: 1.01x slower                                                        |
| pycparser                  | 1.24 sec                                                     | 1.26 sec: 1.02x slower                                                       |
| chaos                      | 60.2 ms                                                      | 61.4 ms: 1.02x slower                                                        |
| typing_runtime_protocols   | 169 us                                                       | 172 us: 1.02x slower                                                         |
| json_loads                 | 24.7 us                                                      | 25.2 us: 1.02x slower                                                        |
| django_template            | 36.4 ms                                                      | 37.2 ms: 1.02x slower                                                        |
| comprehensions             | 17.0 us                                                      | 17.4 us: 1.02x slower                                                        |
| docutils                   | 2.83 sec                                                     | 2.89 sec: 1.02x slower                                                       |
| xml_etree_iterparse        | 103 ms                                                       | 105 ms: 1.02x slower                                                         |
| meteor_contest             | 130 ms                                                       | 133 ms: 1.03x slower                                                         |
| coroutines                 | 21.6 ms                                                      | 22.3 ms: 1.03x slower                                                        |
| nqueens                    | 90.7 ms                                                      | 94.1 ms: 1.04x slower                                                        |
| regex_v8                   | 26.1 ms                                                      | 27.2 ms: 1.04x slower                                                        |
| mdp                        | 2.54 sec                                                     | 2.65 sec: 1.04x slower                                                       |
| json_dumps                 | 11.1 ms                                                      | 11.7 ms: 1.05x slower                                                        |
| crypto_pyaes               | 73.3 ms                                                      | 78.1 ms: 1.07x slower                                                        |
| xml_etree_parse            | 150 ms                                                       | 161 ms: 1.07x slower                                                         |
| create_gc_cycles           | 2.68 ms                                                      | 2.89 ms: 1.08x slower                                                        |
| mako                       | 10.4 ms                                                      | 11.3 ms: 1.09x slower                                                        |
| many_optionals             | 930 us                                                       | 1.03 ms: 1.10x slower                                                        |
| gc_traversal               | 4.74 ms                                                      | 5.34 ms: 1.13x slower                                                        |
| pidigits                   | 252 ms                                                       | 286 ms: 1.13x slower                                                         |
| subparsers                 | 17.5 ms                                                      | 22.6 ms: 1.29x slower                                                        |
| bench_mp_pool              | 5.12 ms                                                      | 1.36 sec: 265.95x slower                                                     |
| Geometric mean             | (ref)                                                        | 1.00x faster                                                                 |

Benchmark hidden because not significant (3): bench_thread_pool, nbody, sqlglot_normalize
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http

- Geometric mean (including insignificant results): 1.059x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.07x
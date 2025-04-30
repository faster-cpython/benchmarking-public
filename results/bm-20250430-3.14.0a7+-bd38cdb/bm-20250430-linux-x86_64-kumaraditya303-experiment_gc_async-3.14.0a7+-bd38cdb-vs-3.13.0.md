# Results vs. 3.13.0

- fork: kumaraditya303
- ref: experiment_gc_async
- machine: linux-x86_64
- commit hash: bd38cdb
- commit date: 2025-04-30
- overall geometric mean: 1.019x faster
- HPT reliability: 87.17%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250430-linux-x86_64-kumaraditya303-experiment_gc_async-3.14.0a7+-bd38cdb |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 254 ms: 1.04x faster                                                          |
| docutils       | 2.58 sec                                               | 2.63 sec: 1.02x slower                                                        |
| html5lib       | 63.4 ms                                                | 60.2 ms: 1.05x faster                                                         |
| Geometric mean | (ref)                                                  | 1.02x faster                                                                  |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250430-linux-x86_64-kumaraditya303-experiment_gc_async-3.14.0a7+-bd38cdb |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 391 ms: 1.18x faster                                                          |
| async_tree_memoization     | 437 ms                                                 | 384 ms: 1.14x faster                                                          |
| async_tree_none            | 350 ms                                                 | 320 ms: 1.09x faster                                                          |
| async_generators           | 433 ms                                                 | 411 ms: 1.05x faster                                                          |
| async_tree_io              | 838 ms                                                 | 804 ms: 1.04x faster                                                          |
| async_tree_io_tg           | 861 ms                                                 | 832 ms: 1.03x faster                                                          |
| async_tree_none_tg         | 319 ms                                                 | 324 ms: 1.02x slower                                                          |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 580 ms: 1.07x slower                                                          |
| coroutines                 | 22.2 ms                                                | 26.3 ms: 1.18x slower                                                         |
| Geometric mean             | (ref)                                                  | 1.02x faster                                                                  |

Benchmark hidden because not significant (2): asyncio_websockets, async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250430-linux-x86_64-kumaraditya303-experiment_gc_async-3.14.0a7+-bd38cdb |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 71.2 ms: 1.10x faster                                                         |
| pidigits       | 186 ms                                                 | 191 ms: 1.03x slower                                                          |
| nbody          | 87.7 ms                                                | 99.2 ms: 1.13x slower                                                         |
| Geometric mean | (ref)                                                  | 1.02x slower                                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250430-linux-x86_64-kumaraditya303-experiment_gc_async-3.14.0a7+-bd38cdb |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                | 3.11 ms: 1.21x faster                                                         |
| regex_v8       | 26.9 ms                                                | 22.5 ms: 1.19x faster                                                         |
| regex_dna      | 220 ms                                                 | 207 ms: 1.06x faster                                                          |
| regex_compile  | 132 ms                                                 | 127 ms: 1.04x faster                                                          |
| Geometric mean | (ref)                                                  | 1.12x faster                                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250430-linux-x86_64-kumaraditya303-experiment_gc_async-3.14.0a7+-bd38cdb |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| xml_etree_parse      | 154 ms                                                 | 142 ms: 1.09x faster                                                          |
| tomli_loads          | 2.12 sec                                               | 2.05 sec: 1.03x faster                                                        |
| xml_etree_generate   | 86.8 ms                                                | 84.9 ms: 1.02x faster                                                         |
| xml_etree_process    | 60.5 ms                                                | 59.2 ms: 1.02x faster                                                         |
| xml_etree_iterparse  | 101 ms                                                 | 99.2 ms: 1.02x faster                                                         |
| unpickle_pure_python | 213 us                                                 | 219 us: 1.03x slower                                                          |
| pickle_pure_python   | 302 us                                                 | 318 us: 1.05x slower                                                          |
| json_loads           | 27.2 us                                                | 30.5 us: 1.12x slower                                                         |
| json_dumps           | 10.1 ms                                                | 12.2 ms: 1.21x slower                                                         |
| Geometric mean       | (ref)                                                  | 1.02x slower                                                                  |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250430-linux-x86_64-kumaraditya303-experiment_gc_async-3.14.0a7+-bd38cdb |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| python_startup_no_site | 7.00 ms                                                | 6.93 ms: 1.01x faster                                                         |
| python_startup         | 12.7 ms                                                | 13.1 ms: 1.04x slower                                                         |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250430-linux-x86_64-kumaraditya303-experiment_gc_async-3.14.0a7+-bd38cdb |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| genshi_text     | 22.6 ms                                                | 21.1 ms: 1.07x faster                                                         |
| django_template | 31.7 ms                                                | 33.1 ms: 1.05x slower                                                         |
| mako            | 10.7 ms                                                | 11.6 ms: 1.09x slower                                                         |
| Geometric mean  | (ref)                                                  | 1.02x slower                                                                  |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250430-linux-x86_64-kumaraditya303-experiment_gc_async-3.14.0a7+-bd38cdb |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| mdp                        | 2.54 sec                                               | 1.22 sec: 2.08x faster                                                        |
| deepcopy                   | 354 us                                                 | 260 us: 1.36x faster                                                          |
| deepcopy_memo              | 38.4 us                                                | 29.0 us: 1.32x faster                                                         |
| go                         | 141 ms                                                 | 113 ms: 1.25x faster                                                          |
| regex_effbot               | 3.77 ms                                                | 3.11 ms: 1.21x faster                                                         |
| regex_v8                   | 26.9 ms                                                | 22.5 ms: 1.19x faster                                                         |
| deepcopy_reduce            | 3.24 us                                                | 2.73 us: 1.19x faster                                                         |
| async_tree_memoization_tg  | 463 ms                                                 | 391 ms: 1.18x faster                                                          |
| async_tree_memoization     | 437 ms                                                 | 384 ms: 1.14x faster                                                          |
| pylint                     | 312 ms                                                 | 281 ms: 1.11x faster                                                          |
| float                      | 78.7 ms                                                | 71.2 ms: 1.10x faster                                                         |
| richards                   | 47.5 ms                                                | 43.4 ms: 1.10x faster                                                         |
| async_tree_none            | 350 ms                                                 | 320 ms: 1.09x faster                                                          |
| xml_etree_parse            | 154 ms                                                 | 142 ms: 1.09x faster                                                          |
| richards_super             | 53.7 ms                                                | 49.9 ms: 1.08x faster                                                         |
| dulwich_log                | 64.6 ms                                                | 60.4 ms: 1.07x faster                                                         |
| genshi_text                | 22.6 ms                                                | 21.1 ms: 1.07x faster                                                         |
| regex_dna                  | 220 ms                                                 | 207 ms: 1.06x faster                                                          |
| telco                      | 8.40 ms                                                | 7.95 ms: 1.06x faster                                                         |
| async_generators           | 433 ms                                                 | 411 ms: 1.05x faster                                                          |
| html5lib                   | 63.4 ms                                                | 60.2 ms: 1.05x faster                                                         |
| spectral_norm              | 113 ms                                                 | 108 ms: 1.05x faster                                                          |
| 2to3                       | 266 ms                                                 | 254 ms: 1.04x faster                                                          |
| k_core                     | 2.37 sec                                               | 2.27 sec: 1.04x faster                                                        |
| async_tree_io              | 838 ms                                                 | 804 ms: 1.04x faster                                                          |
| regex_compile              | 132 ms                                                 | 127 ms: 1.04x faster                                                          |
| async_tree_io_tg           | 861 ms                                                 | 832 ms: 1.03x faster                                                          |
| tomli_loads                | 2.12 sec                                               | 2.05 sec: 1.03x faster                                                        |
| sympy_integrate            | 19.8 ms                                                | 19.2 ms: 1.03x faster                                                         |
| pyflate                    | 470 ms                                                 | 456 ms: 1.03x faster                                                          |
| bpe_tokeniser              | 4.69 sec                                               | 4.57 sec: 1.03x faster                                                        |
| gc_traversal               | 4.90 ms                                                | 4.78 ms: 1.03x faster                                                         |
| xml_etree_generate         | 86.8 ms                                                | 84.9 ms: 1.02x faster                                                         |
| xml_etree_process          | 60.5 ms                                                | 59.2 ms: 1.02x faster                                                         |
| sqlite_synth               | 2.90 us                                                | 2.84 us: 1.02x faster                                                         |
| xml_etree_iterparse        | 101 ms                                                 | 99.2 ms: 1.02x faster                                                         |
| pycparser                  | 1.20 sec                                               | 1.18 sec: 1.02x faster                                                        |
| meteor_contest             | 108 ms                                                 | 107 ms: 1.01x faster                                                          |
| sympy_str                  | 273 ms                                                 | 270 ms: 1.01x faster                                                          |
| sympy_sum                  | 150 ms                                                 | 149 ms: 1.01x faster                                                          |
| python_startup_no_site     | 7.00 ms                                                | 6.93 ms: 1.01x faster                                                         |
| scimark_sor                | 122 ms                                                 | 121 ms: 1.01x faster                                                          |
| sqlalchemy_declarative     | 133 ms                                                 | 133 ms: 1.00x slower                                                          |
| scimark_fft                | 367 ms                                                 | 369 ms: 1.01x slower                                                          |
| create_gc_cycles           | 2.45 ms                                                | 2.47 ms: 1.01x slower                                                         |
| connected_components       | 447 ms                                                 | 453 ms: 1.01x slower                                                          |
| pprint_pformat             | 1.48 sec                                               | 1.50 sec: 1.01x slower                                                        |
| sympy_expand               | 456 ms                                                 | 463 ms: 1.01x slower                                                          |
| async_tree_none_tg         | 319 ms                                                 | 324 ms: 1.02x slower                                                          |
| scimark_lu                 | 114 ms                                                 | 116 ms: 1.02x slower                                                          |
| docutils                   | 2.58 sec                                               | 2.63 sec: 1.02x slower                                                        |
| pprint_safe_repr           | 727 ms                                                 | 741 ms: 1.02x slower                                                          |
| scimark_monte_carlo        | 66.8 ms                                                | 68.1 ms: 1.02x slower                                                         |
| generators                 | 28.8 ms                                                | 29.4 ms: 1.02x slower                                                         |
| crypto_pyaes               | 74.7 ms                                                | 76.3 ms: 1.02x slower                                                         |
| sqlalchemy_imperative      | 16.9 ms                                                | 17.3 ms: 1.02x slower                                                         |
| shortest_path              | 487 ms                                                 | 499 ms: 1.02x slower                                                          |
| pidigits                   | 186 ms                                                 | 191 ms: 1.03x slower                                                          |
| unpickle_pure_python       | 213 us                                                 | 219 us: 1.03x slower                                                          |
| nqueens                    | 80.9 ms                                                | 83.1 ms: 1.03x slower                                                         |
| chaos                      | 58.0 ms                                                | 59.6 ms: 1.03x slower                                                         |
| hexiom                     | 6.08 ms                                                | 6.25 ms: 1.03x slower                                                         |
| raytrace                   | 262 ms                                                 | 269 ms: 1.03x slower                                                          |
| json                       | 5.32 ms                                                | 5.49 ms: 1.03x slower                                                         |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 5.19 ms: 1.03x slower                                                         |
| comprehensions             | 16.5 us                                                | 17.0 us: 1.03x slower                                                         |
| python_startup             | 12.7 ms                                                | 13.1 ms: 1.04x slower                                                         |
| deltablue                  | 3.19 ms                                                | 3.33 ms: 1.04x slower                                                         |
| django_template            | 31.7 ms                                                | 33.1 ms: 1.05x slower                                                         |
| pickle_pure_python         | 302 us                                                 | 318 us: 1.05x slower                                                          |
| typing_runtime_protocols   | 160 us                                                 | 169 us: 1.06x slower                                                          |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 580 ms: 1.07x slower                                                          |
| fannkuch                   | 394 ms                                                 | 421 ms: 1.07x slower                                                          |
| mako                       | 10.7 ms                                                | 11.6 ms: 1.09x slower                                                         |
| many_optionals             | 857 us                                                 | 935 us: 1.09x slower                                                          |
| bench_thread_pool          | 818 us                                                 | 893 us: 1.09x slower                                                          |
| coverage                   | 82.8 ms                                                | 91.5 ms: 1.10x slower                                                         |
| json_loads                 | 27.2 us                                                | 30.5 us: 1.12x slower                                                         |
| nbody                      | 87.7 ms                                                | 99.2 ms: 1.13x slower                                                         |
| coroutines                 | 22.2 ms                                                | 26.3 ms: 1.18x slower                                                         |
| json_dumps                 | 10.1 ms                                                | 12.2 ms: 1.21x slower                                                         |
| subparsers                 | 15.5 ms                                                | 21.3 ms: 1.38x slower                                                         |
| bench_mp_pool              | 24.0 ms                                                | 82.9 ms: 3.46x slower                                                         |
| Geometric mean             | (ref)                                                  | 1.01x faster                                                                  |

Benchmark hidden because not significant (8): sphinx, logging_silent, logging_simple, genshi_xml, pathlib, asyncio_websockets, async_tree_cpu_io_mixed, logging_format
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
Ignored benchmarks (12) of results/bm-20250430-3.14.0a7+-bd38cdb/bm-20250430-linux-x86_64-kumaraditya303-experiment_gc_async-3.14.0a7+-bd38cdb.json: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.019x faster

# HPT report

- Reliability score: 87.17% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.04x
# Results vs. 3.13.0

- fork: faster-cpython
- ref: specialize_for_iter_
- machine: linux-x86_64
- commit hash: 08419ee
- commit date: 2025-05-29
- overall geometric mean: 1.039x slower
- HPT reliability: 99.80%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.06x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250529-linux-x86_64-faster%2dcpython-specialize_for_iter_-3.15.0a0-08419ee |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 256 ms: 1.04x faster                                                            |
| docutils       | 2.58 sec                                               | 2.57 sec: 1.00x faster                                                          |
| html5lib       | 63.4 ms                                                | 61.7 ms: 1.03x faster                                                           |
| sphinx         | 1.03 sec                                               | 1.01 sec: 1.03x faster                                                          |
| Geometric mean | (ref)                                                  | 1.02x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250529-linux-x86_64-faster%2dcpython-specialize_for_iter_-3.15.0a0-08419ee |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 317 ms: 1.46x faster                                                            |
| async_tree_io              | 838 ms                                                 | 602 ms: 1.39x faster                                                            |
| async_tree_memoization     | 437 ms                                                 | 314 ms: 1.39x faster                                                            |
| async_tree_io_tg           | 861 ms                                                 | 626 ms: 1.38x faster                                                            |
| async_tree_none            | 350 ms                                                 | 262 ms: 1.34x faster                                                            |
| async_tree_none_tg         | 319 ms                                                 | 253 ms: 1.26x faster                                                            |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 495 ms: 1.16x faster                                                            |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 489 ms: 1.11x faster                                                            |
| async_generators           | 433 ms                                                 | 411 ms: 1.06x faster                                                            |
| coroutines                 | 22.2 ms                                                | 25.7 ms: 1.16x slower                                                           |
| Geometric mean             | (ref)                                                  | 1.20x faster                                                                    |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250529-linux-x86_64-faster%2dcpython-specialize_for_iter_-3.15.0a0-08419ee |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 73.0 ms: 1.08x faster                                                           |
| pidigits       | 186 ms                                                 | 188 ms: 1.01x slower                                                            |
| nbody          | 87.7 ms                                                | 100 ms: 1.14x slower                                                            |
| Geometric mean | (ref)                                                  | 1.02x slower                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250529-linux-x86_64-faster%2dcpython-specialize_for_iter_-3.15.0a0-08419ee |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                | 3.23 ms: 1.17x faster                                                           |
| regex_v8       | 26.9 ms                                                | 23.2 ms: 1.16x faster                                                           |
| regex_dna      | 220 ms                                                 | 209 ms: 1.05x faster                                                            |
| regex_compile  | 132 ms                                                 | 128 ms: 1.03x faster                                                            |
| Geometric mean | (ref)                                                  | 1.10x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250529-linux-x86_64-faster%2dcpython-specialize_for_iter_-3.15.0a0-08419ee |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| xml_etree_parse      | 154 ms                                                 | 143 ms: 1.08x faster                                                            |
| tomli_loads          | 2.12 sec                                               | 2.01 sec: 1.05x faster                                                          |
| xml_etree_generate   | 86.8 ms                                                | 84.8 ms: 1.02x faster                                                           |
| xml_etree_iterparse  | 101 ms                                                 | 99.2 ms: 1.02x faster                                                           |
| xml_etree_process    | 60.5 ms                                                | 59.5 ms: 1.02x faster                                                           |
| unpickle_pure_python | 213 us                                                 | 219 us: 1.03x slower                                                            |
| pickle_pure_python   | 302 us                                                 | 319 us: 1.05x slower                                                            |
| json_loads           | 27.2 us                                                | 29.8 us: 1.10x slower                                                           |
| json_dumps           | 10.1 ms                                                | 11.2 ms: 1.11x slower                                                           |
| Geometric mean       | (ref)                                                  | 1.01x slower                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250529-linux-x86_64-faster%2dcpython-specialize_for_iter_-3.15.0a0-08419ee |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 12.7 ms                                                | 12.2 ms: 1.04x faster                                                           |
| python_startup_no_site | 7.00 ms                                                | 6.92 ms: 1.01x faster                                                           |
| Geometric mean         | (ref)                                                  | 1.03x faster                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250529-linux-x86_64-faster%2dcpython-specialize_for_iter_-3.15.0a0-08419ee |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| genshi_text     | 22.6 ms                                                | 21.3 ms: 1.06x faster                                                           |
| genshi_xml      | 50.5 ms                                                | 49.0 ms: 1.03x faster                                                           |
| django_template | 31.7 ms                                                | 32.3 ms: 1.02x slower                                                           |
| mako            | 10.7 ms                                                | 11.3 ms: 1.06x slower                                                           |
| Geometric mean  | (ref)                                                  | 1.00x faster                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250529-linux-x86_64-faster%2dcpython-specialize_for_iter_-3.15.0a0-08419ee |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mdp                        | 2.54 sec                                               | 1.23 sec: 2.07x faster                                                          |
| async_tree_memoization_tg  | 463 ms                                                 | 317 ms: 1.46x faster                                                            |
| async_tree_io              | 838 ms                                                 | 602 ms: 1.39x faster                                                            |
| async_tree_memoization     | 437 ms                                                 | 314 ms: 1.39x faster                                                            |
| deepcopy                   | 354 us                                                 | 257 us: 1.38x faster                                                            |
| async_tree_io_tg           | 861 ms                                                 | 626 ms: 1.38x faster                                                            |
| async_tree_none            | 350 ms                                                 | 262 ms: 1.34x faster                                                            |
| deepcopy_memo              | 38.4 us                                                | 29.6 us: 1.30x faster                                                           |
| async_tree_none_tg         | 319 ms                                                 | 253 ms: 1.26x faster                                                            |
| go                         | 141 ms                                                 | 114 ms: 1.23x faster                                                            |
| deepcopy_reduce            | 3.24 us                                                | 2.74 us: 1.18x faster                                                           |
| regex_effbot               | 3.77 ms                                                | 3.23 ms: 1.17x faster                                                           |
| regex_v8                   | 26.9 ms                                                | 23.2 ms: 1.16x faster                                                           |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 495 ms: 1.16x faster                                                            |
| pylint                     | 312 ms                                                 | 278 ms: 1.12x faster                                                            |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 489 ms: 1.11x faster                                                            |
| pyflate                    | 470 ms                                                 | 429 ms: 1.10x faster                                                            |
| richards                   | 47.5 ms                                                | 43.6 ms: 1.09x faster                                                           |
| richards_super             | 53.7 ms                                                | 49.8 ms: 1.08x faster                                                           |
| dulwich_log                | 64.6 ms                                                | 59.9 ms: 1.08x faster                                                           |
| float                      | 78.7 ms                                                | 73.0 ms: 1.08x faster                                                           |
| xml_etree_parse            | 154 ms                                                 | 143 ms: 1.08x faster                                                            |
| genshi_text                | 22.6 ms                                                | 21.3 ms: 1.06x faster                                                           |
| async_generators           | 433 ms                                                 | 411 ms: 1.06x faster                                                            |
| tomli_loads                | 2.12 sec                                               | 2.01 sec: 1.05x faster                                                          |
| telco                      | 8.40 ms                                                | 7.97 ms: 1.05x faster                                                           |
| regex_dna                  | 220 ms                                                 | 209 ms: 1.05x faster                                                            |
| bpe_tokeniser              | 4.69 sec                                               | 4.46 sec: 1.05x faster                                                          |
| sympy_integrate            | 19.8 ms                                                | 19.0 ms: 1.04x faster                                                           |
| 2to3                       | 266 ms                                                 | 256 ms: 1.04x faster                                                            |
| pathlib                    | 17.4 ms                                                | 16.7 ms: 1.04x faster                                                           |
| python_startup             | 12.7 ms                                                | 12.2 ms: 1.04x faster                                                           |
| k_core                     | 2.37 sec                                               | 2.28 sec: 1.04x faster                                                          |
| regex_compile              | 132 ms                                                 | 128 ms: 1.03x faster                                                            |
| pycparser                  | 1.20 sec                                               | 1.16 sec: 1.03x faster                                                          |
| meteor_contest             | 108 ms                                                 | 105 ms: 1.03x faster                                                            |
| genshi_xml                 | 50.5 ms                                                | 49.0 ms: 1.03x faster                                                           |
| spectral_norm              | 113 ms                                                 | 110 ms: 1.03x faster                                                            |
| html5lib                   | 63.4 ms                                                | 61.7 ms: 1.03x faster                                                           |
| sphinx                     | 1.03 sec                                               | 1.01 sec: 1.03x faster                                                          |
| sympy_str                  | 273 ms                                                 | 266 ms: 1.03x faster                                                            |
| xml_etree_generate         | 86.8 ms                                                | 84.8 ms: 1.02x faster                                                           |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.93 ms: 1.02x faster                                                           |
| xml_etree_iterparse        | 101 ms                                                 | 99.2 ms: 1.02x faster                                                           |
| xml_etree_process          | 60.5 ms                                                | 59.5 ms: 1.02x faster                                                           |
| comprehensions             | 16.5 us                                                | 16.2 us: 1.02x faster                                                           |
| sympy_expand               | 456 ms                                                 | 450 ms: 1.01x faster                                                            |
| sympy_sum                  | 150 ms                                                 | 149 ms: 1.01x faster                                                            |
| python_startup_no_site     | 7.00 ms                                                | 6.92 ms: 1.01x faster                                                           |
| crypto_pyaes               | 74.7 ms                                                | 73.9 ms: 1.01x faster                                                           |
| scimark_sor                | 122 ms                                                 | 121 ms: 1.01x faster                                                            |
| sqlite_synth               | 2.90 us                                                | 2.88 us: 1.01x faster                                                           |
| docutils                   | 2.58 sec                                               | 2.57 sec: 1.00x faster                                                          |
| hexiom                     | 6.08 ms                                                | 6.09 ms: 1.00x slower                                                           |
| pidigits                   | 186 ms                                                 | 188 ms: 1.01x slower                                                            |
| shortest_path              | 487 ms                                                 | 493 ms: 1.01x slower                                                            |
| scimark_monte_carlo        | 66.8 ms                                                | 67.8 ms: 1.02x slower                                                           |
| django_template            | 31.7 ms                                                | 32.3 ms: 1.02x slower                                                           |
| json                       | 5.32 ms                                                | 5.44 ms: 1.02x slower                                                           |
| chaos                      | 58.0 ms                                                | 59.6 ms: 1.03x slower                                                           |
| unpickle_pure_python       | 213 us                                                 | 219 us: 1.03x slower                                                            |
| generators                 | 28.8 ms                                                | 29.8 ms: 1.03x slower                                                           |
| fannkuch                   | 394 ms                                                 | 408 ms: 1.04x slower                                                            |
| gc_traversal               | 4.90 ms                                                | 5.08 ms: 1.04x slower                                                           |
| connected_components       | 447 ms                                                 | 463 ms: 1.04x slower                                                            |
| scimark_fft                | 367 ms                                                 | 381 ms: 1.04x slower                                                            |
| scimark_lu                 | 114 ms                                                 | 119 ms: 1.04x slower                                                            |
| raytrace                   | 262 ms                                                 | 272 ms: 1.04x slower                                                            |
| typing_runtime_protocols   | 160 us                                                 | 168 us: 1.05x slower                                                            |
| create_gc_cycles           | 2.45 ms                                                | 2.57 ms: 1.05x slower                                                           |
| pickle_pure_python         | 302 us                                                 | 319 us: 1.05x slower                                                            |
| mako                       | 10.7 ms                                                | 11.3 ms: 1.06x slower                                                           |
| logging_simple             | 5.65 us                                                | 6.06 us: 1.07x slower                                                           |
| logging_format             | 6.23 us                                                | 6.74 us: 1.08x slower                                                           |
| bench_thread_pool          | 818 us                                                 | 887 us: 1.08x slower                                                            |
| json_loads                 | 27.2 us                                                | 29.8 us: 1.10x slower                                                           |
| pprint_safe_repr           | 727 ms                                                 | 800 ms: 1.10x slower                                                            |
| pprint_pformat             | 1.48 sec                                               | 1.64 sec: 1.11x slower                                                          |
| json_dumps                 | 10.1 ms                                                | 11.2 ms: 1.11x slower                                                           |
| deltablue                  | 3.19 ms                                                | 3.55 ms: 1.11x slower                                                           |
| many_optionals             | 857 us                                                 | 959 us: 1.12x slower                                                            |
| nbody                      | 87.7 ms                                                | 100 ms: 1.14x slower                                                            |
| coroutines                 | 22.2 ms                                                | 25.7 ms: 1.16x slower                                                           |
| subparsers                 | 15.5 ms                                                | 23.6 ms: 1.53x slower                                                           |
| bench_mp_pool              | 24.0 ms                                                | 93.1 ms: 3.88x slower                                                           |
| logging_silent             | 101 ns                                                 | 477 ns: 4.72x slower                                                            |
| coverage                   | 82.8 ms                                                | 428 ms: 5.17x slower                                                            |
| thrift                     | 800 us                                                 | 148 ms: 185.62x slower                                                          |
| Geometric mean             | (ref)                                                  | 1.07x slower                                                                    |

Benchmark hidden because not significant (2): asyncio_websockets, nqueens
Ignored benchmarks (11) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (13) of results/bm-20250529-3.15.0a0-08419ee/bm-20250529-linux-x86_64-faster%2dcpython-specialize_for_iter_-3.15.0a0-08419ee.json: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, dask, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.039x slower

# HPT report

- Reliability score: 99.80% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.06x
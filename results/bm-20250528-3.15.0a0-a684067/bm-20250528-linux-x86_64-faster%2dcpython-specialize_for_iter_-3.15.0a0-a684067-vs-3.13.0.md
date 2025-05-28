# Results vs. 3.13.0

- fork: faster-cpython
- ref: specialize_for_iter_
- machine: linux-x86_64
- commit hash: a684067
- commit date: 2025-05-28
- overall geometric mean: 1.035x slower
- HPT reliability: 99.90%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.06x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250528-linux-x86_64-faster%2dcpython-specialize_for_iter_-3.15.0a0-a684067 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 254 ms: 1.04x faster                                                            |
| docutils       | 2.58 sec                                               | 2.57 sec: 1.01x faster                                                          |
| html5lib       | 63.4 ms                                                | 61.3 ms: 1.03x faster                                                           |
| sphinx         | 1.03 sec                                               | 1.00 sec: 1.03x faster                                                          |
| Geometric mean | (ref)                                                  | 1.03x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250528-linux-x86_64-faster%2dcpython-specialize_for_iter_-3.15.0a0-a684067 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 318 ms: 1.46x faster                                                            |
| async_tree_io              | 838 ms                                                 | 600 ms: 1.40x faster                                                            |
| async_tree_io_tg           | 861 ms                                                 | 620 ms: 1.39x faster                                                            |
| async_tree_memoization     | 437 ms                                                 | 315 ms: 1.39x faster                                                            |
| async_tree_none            | 350 ms                                                 | 263 ms: 1.33x faster                                                            |
| async_tree_none_tg         | 319 ms                                                 | 251 ms: 1.27x faster                                                            |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 493 ms: 1.16x faster                                                            |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 483 ms: 1.12x faster                                                            |
| async_generators           | 433 ms                                                 | 403 ms: 1.08x faster                                                            |
| coroutines                 | 22.2 ms                                                | 25.6 ms: 1.15x slower                                                           |
| Geometric mean             | (ref)                                                  | 1.21x faster                                                                    |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250528-linux-x86_64-faster%2dcpython-specialize_for_iter_-3.15.0a0-a684067 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 71.4 ms: 1.10x faster                                                           |
| pidigits       | 186 ms                                                 | 188 ms: 1.01x slower                                                            |
| nbody          | 87.7 ms                                                | 100 ms: 1.14x slower                                                            |
| Geometric mean | (ref)                                                  | 1.01x slower                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250528-linux-x86_64-faster%2dcpython-specialize_for_iter_-3.15.0a0-a684067 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                | 3.22 ms: 1.17x faster                                                           |
| regex_v8       | 26.9 ms                                                | 23.5 ms: 1.14x faster                                                           |
| regex_dna      | 220 ms                                                 | 210 ms: 1.05x faster                                                            |
| regex_compile  | 132 ms                                                 | 127 ms: 1.04x faster                                                            |
| Geometric mean | (ref)                                                  | 1.10x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250528-linux-x86_64-faster%2dcpython-specialize_for_iter_-3.15.0a0-a684067 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| xml_etree_parse      | 154 ms                                                 | 141 ms: 1.10x faster                                                            |
| tomli_loads          | 2.12 sec                                               | 1.98 sec: 1.07x faster                                                          |
| xml_etree_generate   | 86.8 ms                                                | 84.4 ms: 1.03x faster                                                           |
| xml_etree_iterparse  | 101 ms                                                 | 99.0 ms: 1.02x faster                                                           |
| xml_etree_process    | 60.5 ms                                                | 59.9 ms: 1.01x faster                                                           |
| unpickle_pure_python | 213 us                                                 | 217 us: 1.02x slower                                                            |
| pickle_pure_python   | 302 us                                                 | 316 us: 1.05x slower                                                            |
| json_loads           | 27.2 us                                                | 29.0 us: 1.07x slower                                                           |
| json_dumps           | 10.1 ms                                                | 11.0 ms: 1.09x slower                                                           |
| Geometric mean       | (ref)                                                  | 1.00x faster                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250528-linux-x86_64-faster%2dcpython-specialize_for_iter_-3.15.0a0-a684067 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 12.7 ms                                                | 12.2 ms: 1.04x faster                                                           |
| python_startup_no_site | 7.00 ms                                                | 6.92 ms: 1.01x faster                                                           |
| Geometric mean         | (ref)                                                  | 1.03x faster                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250528-linux-x86_64-faster%2dcpython-specialize_for_iter_-3.15.0a0-a684067 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| genshi_text     | 22.6 ms                                                | 21.5 ms: 1.05x faster                                                           |
| genshi_xml      | 50.5 ms                                                | 49.2 ms: 1.03x faster                                                           |
| django_template | 31.7 ms                                                | 32.8 ms: 1.04x slower                                                           |
| mako            | 10.7 ms                                                | 11.3 ms: 1.05x slower                                                           |
| Geometric mean  | (ref)                                                  | 1.00x slower                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250528-linux-x86_64-faster%2dcpython-specialize_for_iter_-3.15.0a0-a684067 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mdp                        | 2.54 sec                                               | 1.22 sec: 2.09x faster                                                          |
| async_tree_memoization_tg  | 463 ms                                                 | 318 ms: 1.46x faster                                                            |
| async_tree_io              | 838 ms                                                 | 600 ms: 1.40x faster                                                            |
| deepcopy                   | 354 us                                                 | 254 us: 1.39x faster                                                            |
| async_tree_io_tg           | 861 ms                                                 | 620 ms: 1.39x faster                                                            |
| async_tree_memoization     | 437 ms                                                 | 315 ms: 1.39x faster                                                            |
| async_tree_none            | 350 ms                                                 | 263 ms: 1.33x faster                                                            |
| deepcopy_memo              | 38.4 us                                                | 29.5 us: 1.30x faster                                                           |
| async_tree_none_tg         | 319 ms                                                 | 251 ms: 1.27x faster                                                            |
| go                         | 141 ms                                                 | 111 ms: 1.26x faster                                                            |
| deepcopy_reduce            | 3.24 us                                                | 2.68 us: 1.21x faster                                                           |
| regex_effbot               | 3.77 ms                                                | 3.22 ms: 1.17x faster                                                           |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 493 ms: 1.16x faster                                                            |
| regex_v8                   | 26.9 ms                                                | 23.5 ms: 1.14x faster                                                           |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 483 ms: 1.12x faster                                                            |
| pylint                     | 312 ms                                                 | 277 ms: 1.12x faster                                                            |
| richards                   | 47.5 ms                                                | 42.8 ms: 1.11x faster                                                           |
| pyflate                    | 470 ms                                                 | 423 ms: 1.11x faster                                                            |
| float                      | 78.7 ms                                                | 71.4 ms: 1.10x faster                                                           |
| xml_etree_parse            | 154 ms                                                 | 141 ms: 1.10x faster                                                            |
| richards_super             | 53.7 ms                                                | 49.2 ms: 1.09x faster                                                           |
| pycparser                  | 1.20 sec                                               | 1.11 sec: 1.08x faster                                                          |
| dulwich_log                | 64.6 ms                                                | 60.0 ms: 1.08x faster                                                           |
| async_generators           | 433 ms                                                 | 403 ms: 1.08x faster                                                            |
| tomli_loads                | 2.12 sec                                               | 1.98 sec: 1.07x faster                                                          |
| bpe_tokeniser              | 4.69 sec                                               | 4.45 sec: 1.05x faster                                                          |
| genshi_text                | 22.6 ms                                                | 21.5 ms: 1.05x faster                                                           |
| telco                      | 8.40 ms                                                | 7.99 ms: 1.05x faster                                                           |
| sympy_integrate            | 19.8 ms                                                | 18.9 ms: 1.05x faster                                                           |
| regex_dna                  | 220 ms                                                 | 210 ms: 1.05x faster                                                            |
| 2to3                       | 266 ms                                                 | 254 ms: 1.04x faster                                                            |
| meteor_contest             | 108 ms                                                 | 104 ms: 1.04x faster                                                            |
| python_startup             | 12.7 ms                                                | 12.2 ms: 1.04x faster                                                           |
| spectral_norm              | 113 ms                                                 | 109 ms: 1.04x faster                                                            |
| regex_compile              | 132 ms                                                 | 127 ms: 1.04x faster                                                            |
| k_core                     | 2.37 sec                                               | 2.29 sec: 1.04x faster                                                          |
| json                       | 5.32 ms                                                | 5.14 ms: 1.04x faster                                                           |
| html5lib                   | 63.4 ms                                                | 61.3 ms: 1.03x faster                                                           |
| sympy_str                  | 273 ms                                                 | 265 ms: 1.03x faster                                                            |
| sphinx                     | 1.03 sec                                               | 1.00 sec: 1.03x faster                                                          |
| xml_etree_generate         | 86.8 ms                                                | 84.4 ms: 1.03x faster                                                           |
| genshi_xml                 | 50.5 ms                                                | 49.2 ms: 1.03x faster                                                           |
| sympy_sum                  | 150 ms                                                 | 147 ms: 1.02x faster                                                            |
| xml_etree_iterparse        | 101 ms                                                 | 99.0 ms: 1.02x faster                                                           |
| comprehensions             | 16.5 us                                                | 16.1 us: 1.02x faster                                                           |
| sympy_expand               | 456 ms                                                 | 448 ms: 1.02x faster                                                            |
| pathlib                    | 17.4 ms                                                | 17.1 ms: 1.02x faster                                                           |
| hexiom                     | 6.08 ms                                                | 5.99 ms: 1.01x faster                                                           |
| scimark_sor                | 122 ms                                                 | 120 ms: 1.01x faster                                                            |
| python_startup_no_site     | 7.00 ms                                                | 6.92 ms: 1.01x faster                                                           |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.98 ms: 1.01x faster                                                           |
| xml_etree_process          | 60.5 ms                                                | 59.9 ms: 1.01x faster                                                           |
| nqueens                    | 80.9 ms                                                | 80.2 ms: 1.01x faster                                                           |
| crypto_pyaes               | 74.7 ms                                                | 74.0 ms: 1.01x faster                                                           |
| sqlite_synth               | 2.90 us                                                | 2.88 us: 1.01x faster                                                           |
| docutils                   | 2.58 sec                                               | 2.57 sec: 1.01x faster                                                          |
| pidigits                   | 186 ms                                                 | 188 ms: 1.01x slower                                                            |
| scimark_fft                | 367 ms                                                 | 372 ms: 1.01x slower                                                            |
| unpickle_pure_python       | 213 us                                                 | 217 us: 1.02x slower                                                            |
| scimark_monte_carlo        | 66.8 ms                                                | 68.1 ms: 1.02x slower                                                           |
| generators                 | 28.8 ms                                                | 29.6 ms: 1.03x slower                                                           |
| raytrace                   | 262 ms                                                 | 269 ms: 1.03x slower                                                            |
| chaos                      | 58.0 ms                                                | 60.1 ms: 1.04x slower                                                           |
| django_template            | 31.7 ms                                                | 32.8 ms: 1.04x slower                                                           |
| connected_components       | 447 ms                                                 | 465 ms: 1.04x slower                                                            |
| pickle_pure_python         | 302 us                                                 | 316 us: 1.05x slower                                                            |
| fannkuch                   | 394 ms                                                 | 413 ms: 1.05x slower                                                            |
| scimark_lu                 | 114 ms                                                 | 120 ms: 1.05x slower                                                            |
| typing_runtime_protocols   | 160 us                                                 | 169 us: 1.05x slower                                                            |
| mako                       | 10.7 ms                                                | 11.3 ms: 1.05x slower                                                           |
| gc_traversal               | 4.90 ms                                                | 5.18 ms: 1.06x slower                                                           |
| create_gc_cycles           | 2.45 ms                                                | 2.59 ms: 1.06x slower                                                           |
| json_loads                 | 27.2 us                                                | 29.0 us: 1.07x slower                                                           |
| shortest_path              | 487 ms                                                 | 521 ms: 1.07x slower                                                            |
| deltablue                  | 3.19 ms                                                | 3.43 ms: 1.07x slower                                                           |
| logging_format             | 6.23 us                                                | 6.71 us: 1.08x slower                                                           |
| logging_simple             | 5.65 us                                                | 6.11 us: 1.08x slower                                                           |
| pprint_safe_repr           | 727 ms                                                 | 787 ms: 1.08x slower                                                            |
| bench_thread_pool          | 818 us                                                 | 886 us: 1.08x slower                                                            |
| json_dumps                 | 10.1 ms                                                | 11.0 ms: 1.09x slower                                                           |
| pprint_pformat             | 1.48 sec                                               | 1.61 sec: 1.09x slower                                                          |
| many_optionals             | 857 us                                                 | 961 us: 1.12x slower                                                            |
| nbody                      | 87.7 ms                                                | 100 ms: 1.14x slower                                                            |
| coroutines                 | 22.2 ms                                                | 25.6 ms: 1.15x slower                                                           |
| subparsers                 | 15.5 ms                                                | 23.6 ms: 1.52x slower                                                           |
| bench_mp_pool              | 24.0 ms                                                | 92.9 ms: 3.88x slower                                                           |
| logging_silent             | 101 ns                                                 | 471 ns: 4.67x slower                                                            |
| coverage                   | 82.8 ms                                                | 423 ms: 5.10x slower                                                            |
| thrift                     | 800 us                                                 | 149 ms: 185.76x slower                                                          |
| Geometric mean             | (ref)                                                  | 1.07x slower                                                                    |

Benchmark hidden because not significant (1): asyncio_websockets
Ignored benchmarks (11) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (13) of results/bm-20250528-3.15.0a0-a684067/bm-20250528-linux-x86_64-faster%2dcpython-specialize_for_iter_-3.15.0a0-a684067.json: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, dask, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.035x slower

# HPT report

- Reliability score: 99.90% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.06x
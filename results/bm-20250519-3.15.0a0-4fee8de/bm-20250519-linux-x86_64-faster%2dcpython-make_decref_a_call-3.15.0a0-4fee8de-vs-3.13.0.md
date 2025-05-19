# Results vs. 3.13.0

- fork: faster-cpython
- ref: make_decref_a_call
- machine: linux-x86_64
- commit hash: 4fee8de
- commit date: 2025-05-19
- overall geometric mean: 1.008x faster
- HPT reliability: 85.31%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.05x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250519-linux-x86_64-faster%2dcpython-make_decref_a_call-3.15.0a0-4fee8de |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 264 ms: 1.01x faster                                                          |
| docutils       | 2.58 sec                                               | 2.67 sec: 1.03x slower                                                        |
| sphinx         | 1.03 sec                                               | 1.05 sec: 1.02x slower                                                        |
| Geometric mean | (ref)                                                  | 1.01x slower                                                                  |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250519-linux-x86_64-faster%2dcpython-make_decref_a_call-3.15.0a0-4fee8de |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 324 ms: 1.43x faster                                                          |
| async_tree_io              | 838 ms                                                 | 615 ms: 1.36x faster                                                          |
| async_tree_io_tg           | 861 ms                                                 | 632 ms: 1.36x faster                                                          |
| async_tree_memoization     | 437 ms                                                 | 322 ms: 1.36x faster                                                          |
| async_tree_none            | 350 ms                                                 | 269 ms: 1.30x faster                                                          |
| async_tree_none_tg         | 319 ms                                                 | 256 ms: 1.25x faster                                                          |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 505 ms: 1.13x faster                                                          |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 497 ms: 1.09x faster                                                          |
| async_generators           | 433 ms                                                 | 424 ms: 1.02x faster                                                          |
| coroutines                 | 22.2 ms                                                | 25.3 ms: 1.14x slower                                                         |
| Geometric mean             | (ref)                                                  | 1.19x faster                                                                  |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250519-linux-x86_64-faster%2dcpython-make_decref_a_call-3.15.0a0-4fee8de |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 72.3 ms: 1.09x faster                                                         |
| pidigits       | 186 ms                                                 | 188 ms: 1.01x slower                                                          |
| nbody          | 87.7 ms                                                | 100 ms: 1.15x slower                                                          |
| Geometric mean | (ref)                                                  | 1.02x slower                                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250519-linux-x86_64-faster%2dcpython-make_decref_a_call-3.15.0a0-4fee8de |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| regex_v8       | 26.9 ms                                                | 24.2 ms: 1.11x faster                                                         |
| regex_effbot   | 3.77 ms                                                | 3.42 ms: 1.10x faster                                                         |
| regex_dna      | 220 ms                                                 | 217 ms: 1.01x faster                                                          |
| regex_compile  | 132 ms                                                 | 132 ms: 1.00x faster                                                          |
| Geometric mean | (ref)                                                  | 1.05x faster                                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250519-linux-x86_64-faster%2dcpython-make_decref_a_call-3.15.0a0-4fee8de |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| xml_etree_parse      | 154 ms                                                 | 148 ms: 1.04x faster                                                          |
| tomli_loads          | 2.12 sec                                               | 2.05 sec: 1.03x faster                                                        |
| xml_etree_iterparse  | 101 ms                                                 | 102 ms: 1.01x slower                                                          |
| xml_etree_generate   | 86.8 ms                                                | 91.2 ms: 1.05x slower                                                         |
| unpickle_pure_python | 213 us                                                 | 225 us: 1.06x slower                                                          |
| xml_etree_process    | 60.5 ms                                                | 64.1 ms: 1.06x slower                                                         |
| pickle_pure_python   | 302 us                                                 | 337 us: 1.12x slower                                                          |
| json_dumps           | 10.1 ms                                                | 11.3 ms: 1.12x slower                                                         |
| json_loads           | 27.2 us                                                | 31.5 us: 1.16x slower                                                         |
| Geometric mean       | (ref)                                                  | 1.05x slower                                                                  |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250519-linux-x86_64-faster%2dcpython-make_decref_a_call-3.15.0a0-4fee8de |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| python_startup         | 12.7 ms                                                | 12.4 ms: 1.02x faster                                                         |
| python_startup_no_site | 7.00 ms                                                | 7.01 ms: 1.00x slower                                                         |
| Geometric mean         | (ref)                                                  | 1.01x faster                                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250519-linux-x86_64-faster%2dcpython-make_decref_a_call-3.15.0a0-4fee8de |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| genshi_text     | 22.6 ms                                                | 23.1 ms: 1.02x slower                                                         |
| genshi_xml      | 50.5 ms                                                | 52.1 ms: 1.03x slower                                                         |
| django_template | 31.7 ms                                                | 33.7 ms: 1.07x slower                                                         |
| mako            | 10.7 ms                                                | 12.0 ms: 1.13x slower                                                         |
| Geometric mean  | (ref)                                                  | 1.06x slower                                                                  |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250519-linux-x86_64-faster%2dcpython-make_decref_a_call-3.15.0a0-4fee8de |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| mdp                        | 2.54 sec                                               | 1.29 sec: 1.98x faster                                                        |
| async_tree_memoization_tg  | 463 ms                                                 | 324 ms: 1.43x faster                                                          |
| async_tree_io              | 838 ms                                                 | 615 ms: 1.36x faster                                                          |
| async_tree_io_tg           | 861 ms                                                 | 632 ms: 1.36x faster                                                          |
| async_tree_memoization     | 437 ms                                                 | 322 ms: 1.36x faster                                                          |
| deepcopy                   | 354 us                                                 | 270 us: 1.31x faster                                                          |
| async_tree_none            | 350 ms                                                 | 269 ms: 1.30x faster                                                          |
| deepcopy_memo              | 38.4 us                                                | 30.4 us: 1.26x faster                                                         |
| async_tree_none_tg         | 319 ms                                                 | 256 ms: 1.25x faster                                                          |
| go                         | 141 ms                                                 | 115 ms: 1.22x faster                                                          |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 505 ms: 1.13x faster                                                          |
| deepcopy_reduce            | 3.24 us                                                | 2.89 us: 1.12x faster                                                         |
| regex_v8                   | 26.9 ms                                                | 24.2 ms: 1.11x faster                                                         |
| regex_effbot               | 3.77 ms                                                | 3.42 ms: 1.10x faster                                                         |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 497 ms: 1.09x faster                                                          |
| float                      | 78.7 ms                                                | 72.3 ms: 1.09x faster                                                         |
| pylint                     | 312 ms                                                 | 287 ms: 1.09x faster                                                          |
| dulwich_log                | 64.6 ms                                                | 59.8 ms: 1.08x faster                                                         |
| richards                   | 47.5 ms                                                | 44.4 ms: 1.07x faster                                                         |
| richards_super             | 53.7 ms                                                | 51.1 ms: 1.05x faster                                                         |
| spectral_norm              | 113 ms                                                 | 108 ms: 1.05x faster                                                          |
| xml_etree_parse            | 154 ms                                                 | 148 ms: 1.04x faster                                                          |
| tomli_loads                | 2.12 sec                                               | 2.05 sec: 1.03x faster                                                        |
| pycparser                  | 1.20 sec                                               | 1.17 sec: 1.03x faster                                                        |
| k_core                     | 2.37 sec                                               | 2.31 sec: 1.03x faster                                                        |
| python_startup             | 12.7 ms                                                | 12.4 ms: 1.02x faster                                                         |
| async_generators           | 433 ms                                                 | 424 ms: 1.02x faster                                                          |
| sympy_integrate            | 19.8 ms                                                | 19.4 ms: 1.02x faster                                                         |
| regex_dna                  | 220 ms                                                 | 217 ms: 1.01x faster                                                          |
| 2to3                       | 266 ms                                                 | 264 ms: 1.01x faster                                                          |
| regex_compile              | 132 ms                                                 | 132 ms: 1.00x faster                                                          |
| python_startup_no_site     | 7.00 ms                                                | 7.01 ms: 1.00x slower                                                         |
| pidigits                   | 186 ms                                                 | 188 ms: 1.01x slower                                                          |
| pathlib                    | 17.4 ms                                                | 17.5 ms: 1.01x slower                                                         |
| pyflate                    | 470 ms                                                 | 474 ms: 1.01x slower                                                          |
| connected_components       | 447 ms                                                 | 451 ms: 1.01x slower                                                          |
| xml_etree_iterparse        | 101 ms                                                 | 102 ms: 1.01x slower                                                          |
| sympy_sum                  | 150 ms                                                 | 152 ms: 1.01x slower                                                          |
| thrift                     | 800 us                                                 | 811 us: 1.01x slower                                                          |
| sympy_str                  | 273 ms                                                 | 277 ms: 1.01x slower                                                          |
| scimark_sor                | 122 ms                                                 | 124 ms: 1.02x slower                                                          |
| sphinx                     | 1.03 sec                                               | 1.05 sec: 1.02x slower                                                        |
| shortest_path              | 487 ms                                                 | 495 ms: 1.02x slower                                                          |
| genshi_text                | 22.6 ms                                                | 23.1 ms: 1.02x slower                                                         |
| docutils                   | 2.58 sec                                               | 2.67 sec: 1.03x slower                                                        |
| genshi_xml                 | 50.5 ms                                                | 52.1 ms: 1.03x slower                                                         |
| meteor_contest             | 108 ms                                                 | 112 ms: 1.03x slower                                                          |
| djangocms                  | 22.3 us                                                | 23.0 us: 1.03x slower                                                         |
| crypto_pyaes               | 74.7 ms                                                | 77.3 ms: 1.04x slower                                                         |
| sympy_expand               | 456 ms                                                 | 473 ms: 1.04x slower                                                          |
| gc_traversal               | 4.90 ms                                                | 5.08 ms: 1.04x slower                                                         |
| json                       | 5.32 ms                                                | 5.56 ms: 1.04x slower                                                         |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 5.27 ms: 1.05x slower                                                         |
| scimark_fft                | 367 ms                                                 | 385 ms: 1.05x slower                                                          |
| scimark_monte_carlo        | 66.8 ms                                                | 70.0 ms: 1.05x slower                                                         |
| xml_etree_generate         | 86.8 ms                                                | 91.2 ms: 1.05x slower                                                         |
| pprint_pformat             | 1.48 sec                                               | 1.56 sec: 1.05x slower                                                        |
| create_gc_cycles           | 2.45 ms                                                | 2.58 ms: 1.05x slower                                                         |
| raytrace                   | 262 ms                                                 | 275 ms: 1.05x slower                                                          |
| scimark_lu                 | 114 ms                                                 | 121 ms: 1.05x slower                                                          |
| chaos                      | 58.0 ms                                                | 61.2 ms: 1.06x slower                                                         |
| unpickle_pure_python       | 213 us                                                 | 225 us: 1.06x slower                                                          |
| hexiom                     | 6.08 ms                                                | 6.42 ms: 1.06x slower                                                         |
| pprint_safe_repr           | 727 ms                                                 | 769 ms: 1.06x slower                                                          |
| xml_etree_process          | 60.5 ms                                                | 64.1 ms: 1.06x slower                                                         |
| django_template            | 31.7 ms                                                | 33.7 ms: 1.07x slower                                                         |
| comprehensions             | 16.5 us                                                | 17.7 us: 1.07x slower                                                         |
| nqueens                    | 80.9 ms                                                | 87.0 ms: 1.08x slower                                                         |
| typing_runtime_protocols   | 160 us                                                 | 175 us: 1.09x slower                                                          |
| deltablue                  | 3.19 ms                                                | 3.53 ms: 1.10x slower                                                         |
| generators                 | 28.8 ms                                                | 31.8 ms: 1.10x slower                                                         |
| pickle_pure_python         | 302 us                                                 | 337 us: 1.12x slower                                                          |
| json_dumps                 | 10.1 ms                                                | 11.3 ms: 1.12x slower                                                         |
| bench_thread_pool          | 818 us                                                 | 913 us: 1.12x slower                                                          |
| fannkuch                   | 394 ms                                                 | 440 ms: 1.12x slower                                                          |
| mako                       | 10.7 ms                                                | 12.0 ms: 1.13x slower                                                         |
| coverage                   | 82.8 ms                                                | 93.3 ms: 1.13x slower                                                         |
| coroutines                 | 22.2 ms                                                | 25.3 ms: 1.14x slower                                                         |
| logging_simple             | 5.65 us                                                | 6.47 us: 1.14x slower                                                         |
| nbody                      | 87.7 ms                                                | 100 ms: 1.15x slower                                                          |
| logging_format             | 6.23 us                                                | 7.19 us: 1.15x slower                                                         |
| json_loads                 | 27.2 us                                                | 31.5 us: 1.16x slower                                                         |
| many_optionals             | 857 us                                                 | 995 us: 1.16x slower                                                          |
| subparsers                 | 15.5 ms                                                | 24.8 ms: 1.60x slower                                                         |
| bench_mp_pool              | 24.0 ms                                                | 94.8 ms: 3.95x slower                                                         |
| logging_silent             | 101 ns                                                 | 495 ns: 4.90x slower                                                          |
| Geometric mean             | (ref)                                                  | 1.03x slower                                                                  |

Benchmark hidden because not significant (5): html5lib, asyncio_websockets, bpe_tokeniser, sqlite_synth, telco
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (13) of results/bm-20250519-3.15.0a0-4fee8de/bm-20250519-linux-x86_64-faster%2dcpython-make_decref_a_call-3.15.0a0-4fee8de.json: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, dask, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.008x faster

# HPT report

- Reliability score: 85.31% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.05x
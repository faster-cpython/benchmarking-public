# Results vs. 3.13.0

- fork: faster-cpython
- ref: make_decref_a_call
- machine: linux-x86_64
- commit hash: bdf907f
- commit date: 2025-05-08
- overall geometric mean: 1.005x faster
- HPT reliability: 91.94%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.05x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250508-linux-x86_64-faster%2dcpython-make_decref_a_call-3.15.0a0-bdf907f |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 266 ms: 1.00x slower                                                          |
| docutils       | 2.58 sec                                               | 2.69 sec: 1.04x slower                                                        |
| html5lib       | 63.4 ms                                                | 63.8 ms: 1.01x slower                                                         |
| sphinx         | 1.03 sec                                               | 1.05 sec: 1.02x slower                                                        |
| Geometric mean | (ref)                                                  | 1.02x slower                                                                  |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250508-linux-x86_64-faster%2dcpython-make_decref_a_call-3.15.0a0-bdf907f |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 322 ms: 1.44x faster                                                          |
| async_tree_io_tg           | 861 ms                                                 | 644 ms: 1.34x faster                                                          |
| async_tree_io              | 838 ms                                                 | 631 ms: 1.33x faster                                                          |
| async_tree_memoization     | 437 ms                                                 | 331 ms: 1.32x faster                                                          |
| async_tree_none            | 350 ms                                                 | 275 ms: 1.27x faster                                                          |
| async_tree_none_tg         | 319 ms                                                 | 257 ms: 1.24x faster                                                          |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 520 ms: 1.10x faster                                                          |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 505 ms: 1.08x faster                                                          |
| async_generators           | 433 ms                                                 | 421 ms: 1.03x faster                                                          |
| coroutines                 | 22.2 ms                                                | 25.1 ms: 1.13x slower                                                         |
| Geometric mean             | (ref)                                                  | 1.17x faster                                                                  |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250508-linux-x86_64-faster%2dcpython-make_decref_a_call-3.15.0a0-bdf907f |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 72.5 ms: 1.09x faster                                                         |
| pidigits       | 186 ms                                                 | 200 ms: 1.07x slower                                                          |
| nbody          | 87.7 ms                                                | 104 ms: 1.18x slower                                                          |
| Geometric mean | (ref)                                                  | 1.05x slower                                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250508-linux-x86_64-faster%2dcpython-make_decref_a_call-3.15.0a0-bdf907f |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                | 3.26 ms: 1.15x faster                                                         |
| regex_v8       | 26.9 ms                                                | 23.8 ms: 1.13x faster                                                         |
| regex_dna      | 220 ms                                                 | 208 ms: 1.06x faster                                                          |
| regex_compile  | 132 ms                                                 | 133 ms: 1.01x slower                                                          |
| Geometric mean | (ref)                                                  | 1.08x faster                                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250508-linux-x86_64-faster%2dcpython-make_decref_a_call-3.15.0a0-bdf907f |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| xml_etree_parse      | 154 ms                                                 | 147 ms: 1.05x faster                                                          |
| tomli_loads          | 2.12 sec                                               | 2.08 sec: 1.02x faster                                                        |
| xml_etree_iterparse  | 101 ms                                                 | 103 ms: 1.01x slower                                                          |
| xml_etree_generate   | 86.8 ms                                                | 90.1 ms: 1.04x slower                                                         |
| xml_etree_process    | 60.5 ms                                                | 63.7 ms: 1.05x slower                                                         |
| unpickle_pure_python | 213 us                                                 | 230 us: 1.08x slower                                                          |
| pickle_pure_python   | 302 us                                                 | 341 us: 1.13x slower                                                          |
| json_loads           | 27.2 us                                                | 31.4 us: 1.16x slower                                                         |
| json_dumps           | 10.1 ms                                                | 12.5 ms: 1.23x slower                                                         |
| Geometric mean       | (ref)                                                  | 1.07x slower                                                                  |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250508-linux-x86_64-faster%2dcpython-make_decref_a_call-3.15.0a0-bdf907f |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| python_startup         | 12.7 ms                                                | 12.4 ms: 1.02x faster                                                         |
| python_startup_no_site | 7.00 ms                                                | 7.01 ms: 1.00x slower                                                         |
| Geometric mean         | (ref)                                                  | 1.01x faster                                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250508-linux-x86_64-faster%2dcpython-make_decref_a_call-3.15.0a0-bdf907f |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| genshi_text     | 22.6 ms                                                | 23.4 ms: 1.04x slower                                                         |
| genshi_xml      | 50.5 ms                                                | 53.0 ms: 1.05x slower                                                         |
| django_template | 31.7 ms                                                | 34.9 ms: 1.10x slower                                                         |
| mako            | 10.7 ms                                                | 12.4 ms: 1.16x slower                                                         |
| Geometric mean  | (ref)                                                  | 1.09x slower                                                                  |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250508-linux-x86_64-faster%2dcpython-make_decref_a_call-3.15.0a0-bdf907f |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| mdp                        | 2.54 sec                                               | 1.29 sec: 1.98x faster                                                        |
| async_tree_memoization_tg  | 463 ms                                                 | 322 ms: 1.44x faster                                                          |
| async_tree_io_tg           | 861 ms                                                 | 644 ms: 1.34x faster                                                          |
| async_tree_io              | 838 ms                                                 | 631 ms: 1.33x faster                                                          |
| async_tree_memoization     | 437 ms                                                 | 331 ms: 1.32x faster                                                          |
| deepcopy                   | 354 us                                                 | 276 us: 1.28x faster                                                          |
| async_tree_none            | 350 ms                                                 | 275 ms: 1.27x faster                                                          |
| async_tree_none_tg         | 319 ms                                                 | 257 ms: 1.24x faster                                                          |
| deepcopy_memo              | 38.4 us                                                | 30.9 us: 1.24x faster                                                         |
| go                         | 141 ms                                                 | 117 ms: 1.20x faster                                                          |
| regex_effbot               | 3.77 ms                                                | 3.26 ms: 1.15x faster                                                         |
| regex_v8                   | 26.9 ms                                                | 23.8 ms: 1.13x faster                                                         |
| deepcopy_reduce            | 3.24 us                                                | 2.92 us: 1.11x faster                                                         |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 520 ms: 1.10x faster                                                          |
| float                      | 78.7 ms                                                | 72.5 ms: 1.09x faster                                                         |
| pylint                     | 312 ms                                                 | 288 ms: 1.08x faster                                                          |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 505 ms: 1.08x faster                                                          |
| dulwich_log                | 64.6 ms                                                | 60.7 ms: 1.06x faster                                                         |
| regex_dna                  | 220 ms                                                 | 208 ms: 1.06x faster                                                          |
| richards                   | 47.5 ms                                                | 45.0 ms: 1.06x faster                                                         |
| spectral_norm              | 113 ms                                                 | 107 ms: 1.05x faster                                                          |
| xml_etree_parse            | 154 ms                                                 | 147 ms: 1.05x faster                                                          |
| richards_super             | 53.7 ms                                                | 51.4 ms: 1.04x faster                                                         |
| k_core                     | 2.37 sec                                               | 2.30 sec: 1.03x faster                                                        |
| async_generators           | 433 ms                                                 | 421 ms: 1.03x faster                                                          |
| python_startup             | 12.7 ms                                                | 12.4 ms: 1.02x faster                                                         |
| tomli_loads                | 2.12 sec                                               | 2.08 sec: 1.02x faster                                                        |
| sympy_integrate            | 19.8 ms                                                | 19.5 ms: 1.02x faster                                                         |
| python_startup_no_site     | 7.00 ms                                                | 7.01 ms: 1.00x slower                                                         |
| 2to3                       | 266 ms                                                 | 266 ms: 1.00x slower                                                          |
| pyflate                    | 470 ms                                                 | 471 ms: 1.00x slower                                                          |
| scimark_sor                | 122 ms                                                 | 123 ms: 1.00x slower                                                          |
| telco                      | 8.40 ms                                                | 8.45 ms: 1.01x slower                                                         |
| html5lib                   | 63.4 ms                                                | 63.8 ms: 1.01x slower                                                         |
| regex_compile              | 132 ms                                                 | 133 ms: 1.01x slower                                                          |
| xml_etree_iterparse        | 101 ms                                                 | 103 ms: 1.01x slower                                                          |
| shortest_path              | 487 ms                                                 | 494 ms: 1.01x slower                                                          |
| sphinx                     | 1.03 sec                                               | 1.05 sec: 1.02x slower                                                        |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 5.12 ms: 1.02x slower                                                         |
| sympy_str                  | 273 ms                                                 | 279 ms: 1.02x slower                                                          |
| sympy_sum                  | 150 ms                                                 | 154 ms: 1.02x slower                                                          |
| logging_simple             | 5.65 us                                                | 5.79 us: 1.02x slower                                                         |
| connected_components       | 447 ms                                                 | 459 ms: 1.03x slower                                                          |
| logging_format             | 6.23 us                                                | 6.40 us: 1.03x slower                                                         |
| logging_silent             | 101 ns                                                 | 104 ns: 1.03x slower                                                          |
| meteor_contest             | 108 ms                                                 | 112 ms: 1.03x slower                                                          |
| crypto_pyaes               | 74.7 ms                                                | 77.2 ms: 1.03x slower                                                         |
| generators                 | 28.8 ms                                                | 29.8 ms: 1.03x slower                                                         |
| genshi_text                | 22.6 ms                                                | 23.4 ms: 1.04x slower                                                         |
| gc_traversal               | 4.90 ms                                                | 5.08 ms: 1.04x slower                                                         |
| xml_etree_generate         | 86.8 ms                                                | 90.1 ms: 1.04x slower                                                         |
| json                       | 5.32 ms                                                | 5.53 ms: 1.04x slower                                                         |
| thrift                     | 800 us                                                 | 832 us: 1.04x slower                                                          |
| docutils                   | 2.58 sec                                               | 2.69 sec: 1.04x slower                                                        |
| sympy_expand               | 456 ms                                                 | 475 ms: 1.04x slower                                                          |
| scimark_monte_carlo        | 66.8 ms                                                | 69.8 ms: 1.05x slower                                                         |
| chaos                      | 58.0 ms                                                | 60.8 ms: 1.05x slower                                                         |
| genshi_xml                 | 50.5 ms                                                | 53.0 ms: 1.05x slower                                                         |
| djangocms                  | 22.3 us                                                | 23.4 us: 1.05x slower                                                         |
| xml_etree_process          | 60.5 ms                                                | 63.7 ms: 1.05x slower                                                         |
| create_gc_cycles           | 2.45 ms                                                | 2.59 ms: 1.06x slower                                                         |
| scimark_fft                | 367 ms                                                 | 388 ms: 1.06x slower                                                          |
| pprint_safe_repr           | 727 ms                                                 | 770 ms: 1.06x slower                                                          |
| pprint_pformat             | 1.48 sec                                               | 1.57 sec: 1.06x slower                                                        |
| nqueens                    | 80.9 ms                                                | 86.6 ms: 1.07x slower                                                         |
| pidigits                   | 186 ms                                                 | 200 ms: 1.07x slower                                                          |
| raytrace                   | 262 ms                                                 | 281 ms: 1.08x slower                                                          |
| unpickle_pure_python       | 213 us                                                 | 230 us: 1.08x slower                                                          |
| hexiom                     | 6.08 ms                                                | 6.58 ms: 1.08x slower                                                         |
| comprehensions             | 16.5 us                                                | 17.9 us: 1.08x slower                                                         |
| django_template            | 31.7 ms                                                | 34.9 ms: 1.10x slower                                                         |
| scimark_lu                 | 114 ms                                                 | 126 ms: 1.10x slower                                                          |
| typing_runtime_protocols   | 160 us                                                 | 177 us: 1.10x slower                                                          |
| bench_thread_pool          | 818 us                                                 | 909 us: 1.11x slower                                                          |
| fannkuch                   | 394 ms                                                 | 441 ms: 1.12x slower                                                          |
| coverage                   | 82.8 ms                                                | 93.1 ms: 1.12x slower                                                         |
| deltablue                  | 3.19 ms                                                | 3.59 ms: 1.13x slower                                                         |
| pickle_pure_python         | 302 us                                                 | 341 us: 1.13x slower                                                          |
| coroutines                 | 22.2 ms                                                | 25.1 ms: 1.13x slower                                                         |
| json_loads                 | 27.2 us                                                | 31.4 us: 1.16x slower                                                         |
| mako                       | 10.7 ms                                                | 12.4 ms: 1.16x slower                                                         |
| many_optionals             | 857 us                                                 | 998 us: 1.16x slower                                                          |
| nbody                      | 87.7 ms                                                | 104 ms: 1.18x slower                                                          |
| json_dumps                 | 10.1 ms                                                | 12.5 ms: 1.23x slower                                                         |
| subparsers                 | 15.5 ms                                                | 24.1 ms: 1.56x slower                                                         |
| bench_mp_pool              | 24.0 ms                                                | 95.1 ms: 3.97x slower                                                         |
| Geometric mean             | (ref)                                                  | 1.01x slower                                                                  |

Benchmark hidden because not significant (5): pathlib, sqlite_synth, bpe_tokeniser, asyncio_websockets, pycparser
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (13) of results/bm-20250508-3.15.0a0-bdf907f/bm-20250508-linux-x86_64-faster%2dcpython-make_decref_a_call-3.15.0a0-bdf907f.json: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, dask, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.005x faster

# HPT report

- Reliability score: 91.94% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.05x
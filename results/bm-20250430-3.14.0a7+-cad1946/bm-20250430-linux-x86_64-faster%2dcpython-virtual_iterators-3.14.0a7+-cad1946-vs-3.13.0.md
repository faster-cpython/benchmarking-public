# Results vs. 3.13.0

- fork: faster-cpython
- ref: virtual_iterators
- machine: linux-x86_64
- commit hash: cad1946
- commit date: 2025-04-30
- overall geometric mean: 1.048x faster
- HPT reliability: 99.90%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250430-linux-x86_64-faster%2dcpython-virtual_iterators-3.14.0a7+-cad1946 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 252 ms: 1.06x faster                                                          |
| docutils       | 2.58 sec                                               | 2.60 sec: 1.01x slower                                                        |
| html5lib       | 63.4 ms                                                | 60.9 ms: 1.04x faster                                                         |
| sphinx         | 1.03 sec                                               | 1.00 sec: 1.03x faster                                                        |
| Geometric mean | (ref)                                                  | 1.03x faster                                                                  |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250430-linux-x86_64-faster%2dcpython-virtual_iterators-3.14.0a7+-cad1946 |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 311 ms: 1.49x faster                                                          |
| async_tree_io              | 838 ms                                                 | 598 ms: 1.40x faster                                                          |
| async_tree_io_tg           | 861 ms                                                 | 614 ms: 1.40x faster                                                          |
| async_tree_memoization     | 437 ms                                                 | 316 ms: 1.38x faster                                                          |
| async_tree_none            | 350 ms                                                 | 262 ms: 1.34x faster                                                          |
| async_tree_none_tg         | 319 ms                                                 | 253 ms: 1.26x faster                                                          |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 495 ms: 1.16x faster                                                          |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 488 ms: 1.11x faster                                                          |
| async_generators           | 433 ms                                                 | 410 ms: 1.06x faster                                                          |
| coroutines                 | 22.2 ms                                                | 24.8 ms: 1.12x slower                                                         |
| Geometric mean             | (ref)                                                  | 1.21x faster                                                                  |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250430-linux-x86_64-faster%2dcpython-virtual_iterators-3.14.0a7+-cad1946 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 70.4 ms: 1.12x faster                                                         |
| pidigits       | 186 ms                                                 | 190 ms: 1.02x slower                                                          |
| nbody          | 87.7 ms                                                | 98.8 ms: 1.13x slower                                                         |
| Geometric mean | (ref)                                                  | 1.01x slower                                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250430-linux-x86_64-faster%2dcpython-virtual_iterators-3.14.0a7+-cad1946 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                | 3.10 ms: 1.21x faster                                                         |
| regex_v8       | 26.9 ms                                                | 22.3 ms: 1.20x faster                                                         |
| regex_dna      | 220 ms                                                 | 205 ms: 1.07x faster                                                          |
| regex_compile  | 132 ms                                                 | 127 ms: 1.04x faster                                                          |
| Geometric mean | (ref)                                                  | 1.13x faster                                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250430-linux-x86_64-faster%2dcpython-virtual_iterators-3.14.0a7+-cad1946 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| xml_etree_parse      | 154 ms                                                 | 141 ms: 1.09x faster                                                          |
| tomli_loads          | 2.12 sec                                               | 2.01 sec: 1.05x faster                                                        |
| xml_etree_iterparse  | 101 ms                                                 | 99.3 ms: 1.02x faster                                                         |
| xml_etree_generate   | 86.8 ms                                                | 85.5 ms: 1.02x faster                                                         |
| xml_etree_process    | 60.5 ms                                                | 59.7 ms: 1.01x faster                                                         |
| unpickle_pure_python | 213 us                                                 | 219 us: 1.03x slower                                                          |
| pickle_pure_python   | 302 us                                                 | 319 us: 1.05x slower                                                          |
| json_loads           | 27.2 us                                                | 30.4 us: 1.12x slower                                                         |
| json_dumps           | 10.1 ms                                                | 12.1 ms: 1.20x slower                                                         |
| Geometric mean       | (ref)                                                  | 1.02x slower                                                                  |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250430-linux-x86_64-faster%2dcpython-virtual_iterators-3.14.0a7+-cad1946 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| python_startup_no_site | 7.00 ms                                                | 6.92 ms: 1.01x faster                                                         |
| python_startup         | 12.7 ms                                                | 13.1 ms: 1.04x slower                                                         |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250430-linux-x86_64-faster%2dcpython-virtual_iterators-3.14.0a7+-cad1946 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| genshi_text     | 22.6 ms                                                | 21.0 ms: 1.08x faster                                                         |
| genshi_xml      | 50.5 ms                                                | 49.2 ms: 1.03x faster                                                         |
| django_template | 31.7 ms                                                | 32.0 ms: 1.01x slower                                                         |
| mako            | 10.7 ms                                                | 11.7 ms: 1.09x slower                                                         |
| Geometric mean  | (ref)                                                  | 1.00x slower                                                                  |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250430-linux-x86_64-faster%2dcpython-virtual_iterators-3.14.0a7+-cad1946 |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| mdp                        | 2.54 sec                                               | 1.22 sec: 2.09x faster                                                        |
| async_tree_memoization_tg  | 463 ms                                                 | 311 ms: 1.49x faster                                                          |
| async_tree_io              | 838 ms                                                 | 598 ms: 1.40x faster                                                          |
| async_tree_io_tg           | 861 ms                                                 | 614 ms: 1.40x faster                                                          |
| deepcopy                   | 354 us                                                 | 256 us: 1.38x faster                                                          |
| async_tree_memoization     | 437 ms                                                 | 316 ms: 1.38x faster                                                          |
| async_tree_none            | 350 ms                                                 | 262 ms: 1.34x faster                                                          |
| deepcopy_memo              | 38.4 us                                                | 28.9 us: 1.33x faster                                                         |
| go                         | 141 ms                                                 | 110 ms: 1.28x faster                                                          |
| async_tree_none_tg         | 319 ms                                                 | 253 ms: 1.26x faster                                                          |
| regex_effbot               | 3.77 ms                                                | 3.10 ms: 1.21x faster                                                         |
| regex_v8                   | 26.9 ms                                                | 22.3 ms: 1.20x faster                                                         |
| deepcopy_reduce            | 3.24 us                                                | 2.78 us: 1.17x faster                                                         |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 495 ms: 1.16x faster                                                          |
| float                      | 78.7 ms                                                | 70.4 ms: 1.12x faster                                                         |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 488 ms: 1.11x faster                                                          |
| richards                   | 47.5 ms                                                | 43.1 ms: 1.10x faster                                                         |
| xml_etree_parse            | 154 ms                                                 | 141 ms: 1.09x faster                                                          |
| dulwich_log                | 64.6 ms                                                | 59.7 ms: 1.08x faster                                                         |
| richards_super             | 53.7 ms                                                | 49.9 ms: 1.08x faster                                                         |
| genshi_text                | 22.6 ms                                                | 21.0 ms: 1.08x faster                                                         |
| regex_dna                  | 220 ms                                                 | 205 ms: 1.07x faster                                                          |
| telco                      | 8.40 ms                                                | 7.93 ms: 1.06x faster                                                         |
| async_generators           | 433 ms                                                 | 410 ms: 1.06x faster                                                          |
| 2to3                       | 266 ms                                                 | 252 ms: 1.06x faster                                                          |
| tomli_loads                | 2.12 sec                                               | 2.01 sec: 1.05x faster                                                        |
| bpe_tokeniser              | 4.69 sec                                               | 4.50 sec: 1.04x faster                                                        |
| spectral_norm              | 113 ms                                                 | 109 ms: 1.04x faster                                                          |
| html5lib                   | 63.4 ms                                                | 60.9 ms: 1.04x faster                                                         |
| regex_compile              | 132 ms                                                 | 127 ms: 1.04x faster                                                          |
| k_core                     | 2.37 sec                                               | 2.29 sec: 1.03x faster                                                        |
| sphinx                     | 1.03 sec                                               | 1.00 sec: 1.03x faster                                                        |
| pyflate                    | 470 ms                                                 | 457 ms: 1.03x faster                                                          |
| meteor_contest             | 108 ms                                                 | 105 ms: 1.03x faster                                                          |
| logging_silent             | 101 ns                                                 | 98.3 ns: 1.03x faster                                                         |
| pycparser                  | 1.20 sec                                               | 1.17 sec: 1.03x faster                                                        |
| genshi_xml                 | 50.5 ms                                                | 49.2 ms: 1.03x faster                                                         |
| scimark_sor                | 122 ms                                                 | 119 ms: 1.02x faster                                                          |
| xml_etree_iterparse        | 101 ms                                                 | 99.3 ms: 1.02x faster                                                         |
| comprehensions             | 16.5 us                                                | 16.2 us: 1.02x faster                                                         |
| sqlalchemy_declarative     | 133 ms                                                 | 131 ms: 1.02x faster                                                          |
| gc_traversal               | 4.90 ms                                                | 4.82 ms: 1.02x faster                                                         |
| logging_format             | 6.23 us                                                | 6.13 us: 1.02x faster                                                         |
| xml_etree_generate         | 86.8 ms                                                | 85.5 ms: 1.02x faster                                                         |
| pprint_safe_repr           | 727 ms                                                 | 715 ms: 1.02x faster                                                          |
| logging_simple             | 5.65 us                                                | 5.57 us: 1.02x faster                                                         |
| pprint_pformat             | 1.48 sec                                               | 1.46 sec: 1.02x faster                                                        |
| pathlib                    | 17.4 ms                                                | 17.1 ms: 1.01x faster                                                         |
| xml_etree_process          | 60.5 ms                                                | 59.7 ms: 1.01x faster                                                         |
| python_startup_no_site     | 7.00 ms                                                | 6.92 ms: 1.01x faster                                                         |
| sqlite_synth               | 2.90 us                                                | 2.87 us: 1.01x faster                                                         |
| crypto_pyaes               | 74.7 ms                                                | 75.1 ms: 1.01x slower                                                         |
| docutils                   | 2.58 sec                                               | 2.60 sec: 1.01x slower                                                        |
| typing_runtime_protocols   | 160 us                                                 | 161 us: 1.01x slower                                                          |
| nqueens                    | 80.9 ms                                                | 81.7 ms: 1.01x slower                                                         |
| hexiom                     | 6.08 ms                                                | 6.14 ms: 1.01x slower                                                         |
| create_gc_cycles           | 2.45 ms                                                | 2.48 ms: 1.01x slower                                                         |
| django_template            | 31.7 ms                                                | 32.0 ms: 1.01x slower                                                         |
| sqlalchemy_imperative      | 16.9 ms                                                | 17.1 ms: 1.01x slower                                                         |
| scimark_fft                | 367 ms                                                 | 372 ms: 1.01x slower                                                          |
| scimark_monte_carlo        | 66.8 ms                                                | 68.0 ms: 1.02x slower                                                         |
| pidigits                   | 186 ms                                                 | 190 ms: 1.02x slower                                                          |
| scimark_lu                 | 114 ms                                                 | 117 ms: 1.02x slower                                                          |
| generators                 | 28.8 ms                                                | 29.4 ms: 1.02x slower                                                         |
| raytrace                   | 262 ms                                                 | 268 ms: 1.02x slower                                                          |
| chaos                      | 58.0 ms                                                | 59.6 ms: 1.03x slower                                                         |
| unpickle_pure_python       | 213 us                                                 | 219 us: 1.03x slower                                                          |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 5.18 ms: 1.03x slower                                                         |
| json                       | 5.32 ms                                                | 5.49 ms: 1.03x slower                                                         |
| connected_components       | 447 ms                                                 | 464 ms: 1.04x slower                                                          |
| python_startup             | 12.7 ms                                                | 13.1 ms: 1.04x slower                                                         |
| shortest_path              | 487 ms                                                 | 510 ms: 1.05x slower                                                          |
| deltablue                  | 3.19 ms                                                | 3.36 ms: 1.05x slower                                                         |
| pickle_pure_python         | 302 us                                                 | 319 us: 1.05x slower                                                          |
| fannkuch                   | 394 ms                                                 | 418 ms: 1.06x slower                                                          |
| bench_thread_pool          | 818 us                                                 | 885 us: 1.08x slower                                                          |
| many_optionals             | 857 us                                                 | 934 us: 1.09x slower                                                          |
| mako                       | 10.7 ms                                                | 11.7 ms: 1.09x slower                                                         |
| coroutines                 | 22.2 ms                                                | 24.8 ms: 1.12x slower                                                         |
| json_loads                 | 27.2 us                                                | 30.4 us: 1.12x slower                                                         |
| coverage                   | 82.8 ms                                                | 93.2 ms: 1.12x slower                                                         |
| nbody                      | 87.7 ms                                                | 98.8 ms: 1.13x slower                                                         |
| json_dumps                 | 10.1 ms                                                | 12.1 ms: 1.20x slower                                                         |
| subparsers                 | 15.5 ms                                                | 21.1 ms: 1.36x slower                                                         |
| bench_mp_pool              | 24.0 ms                                                | 82.5 ms: 3.44x slower                                                         |
| Geometric mean             | (ref)                                                  | 1.03x faster                                                                  |

Benchmark hidden because not significant (1): asyncio_websockets
Ignored benchmarks (15) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, pylint, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift, tornado_http
Ignored benchmarks (12) of results/bm-20250430-3.14.0a7+-cad1946/bm-20250430-linux-x86_64-faster%2dcpython-virtual_iterators-3.14.0a7+-cad1946.json: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.048x faster

# HPT report

- Reliability score: 99.90% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.04x
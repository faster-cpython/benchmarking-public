# Results vs. 3.13.0

- fork: kumaraditya303
- ref: gc
- machine: linux-x86_64
- commit hash: e537b8b
- commit date: 2025-01-17
- overall geometric mean: 1.096x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.07x slower
- Memory change: 1.22x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250117-linux-x86_64-kumaraditya303-gc-3.14.0a4+-e537b8b |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 309 ms: 1.16x slower                                         |
| docutils       | 2.58 sec                                               | 2.83 sec: 1.09x slower                                       |
| html5lib       | 63.4 ms                                                | 69.5 ms: 1.10x slower                                        |
| sphinx         | 1.03 sec                                               | 1.13 sec: 1.10x slower                                       |
| Geometric mean | (ref)                                                  | 1.11x slower                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250117-linux-x86_64-kumaraditya303-gc-3.14.0a4+-e537b8b |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| async_tree_io_tg           | 861 ms                                                 | 542 ms: 1.59x faster                                         |
| async_tree_memoization_tg  | 463 ms                                                 | 315 ms: 1.47x faster                                         |
| async_tree_io              | 838 ms                                                 | 597 ms: 1.40x faster                                         |
| async_tree_none_tg         | 319 ms                                                 | 235 ms: 1.36x faster                                         |
| async_tree_none            | 350 ms                                                 | 290 ms: 1.21x faster                                         |
| async_tree_memoization     | 437 ms                                                 | 367 ms: 1.19x faster                                         |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 466 ms: 1.17x faster                                         |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 522 ms: 1.10x faster                                         |
| async_generators           | 433 ms                                                 | 445 ms: 1.03x slower                                         |
| coroutines                 | 22.2 ms                                                | 25.5 ms: 1.15x slower                                        |
| Geometric mean             | (ref)                                                  | 1.19x faster                                                 |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250117-linux-x86_64-kumaraditya303-gc-3.14.0a4+-e537b8b |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| float          | 78.7 ms                                                | 78.2 ms: 1.01x faster                                        |
| pidigits       | 186 ms                                                 | 190 ms: 1.02x slower                                         |
| nbody          | 87.7 ms                                                | 141 ms: 1.61x slower                                         |
| Geometric mean | (ref)                                                  | 1.18x slower                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250117-linux-x86_64-kumaraditya303-gc-3.14.0a4+-e537b8b |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                | 3.36 ms: 1.12x faster                                        |
| regex_v8       | 26.9 ms                                                | 24.8 ms: 1.08x faster                                        |
| regex_dna      | 220 ms                                                 | 222 ms: 1.01x slower                                         |
| regex_compile  | 132 ms                                                 | 149 ms: 1.13x slower                                         |
| Geometric mean | (ref)                                                  | 1.02x faster                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250117-linux-x86_64-kumaraditya303-gc-3.14.0a4+-e537b8b |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| xml_etree_iterparse  | 101 ms                                                 | 96.2 ms: 1.05x faster                                        |
| xml_etree_parse      | 154 ms                                                 | 149 ms: 1.04x faster                                         |
| xml_etree_generate   | 86.8 ms                                                | 96.1 ms: 1.11x slower                                        |
| xml_etree_process    | 60.5 ms                                                | 68.0 ms: 1.12x slower                                        |
| tomli_loads          | 2.12 sec                                               | 2.41 sec: 1.14x slower                                       |
| json_loads           | 27.2 us                                                | 31.8 us: 1.17x slower                                        |
| unpickle_pure_python | 213 us                                                 | 256 us: 1.20x slower                                         |
| pickle_pure_python   | 302 us                                                 | 368 us: 1.22x slower                                         |
| json_dumps           | 10.1 ms                                                | 12.7 ms: 1.26x slower                                        |
| Geometric mean       | (ref)                                                  | 1.12x slower                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250117-linux-x86_64-kumaraditya303-gc-3.14.0a4+-e537b8b |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup         | 12.7 ms                                                | 15.0 ms: 1.19x slower                                        |
| python_startup_no_site | 7.00 ms                                                | 9.35 ms: 1.34x slower                                        |
| Geometric mean         | (ref)                                                  | 1.26x slower                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250117-linux-x86_64-kumaraditya303-gc-3.14.0a4+-e537b8b |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| genshi_xml      | 50.5 ms                                                | 60.1 ms: 1.19x slower                                        |
| genshi_text     | 22.6 ms                                                | 28.4 ms: 1.25x slower                                        |
| django_template | 31.7 ms                                                | 41.7 ms: 1.32x slower                                        |
| mako            | 10.7 ms                                                | 16.2 ms: 1.52x slower                                        |
| Geometric mean  | (ref)                                                  | 1.31x slower                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250117-linux-x86_64-kumaraditya303-gc-3.14.0a4+-e537b8b |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| async_tree_io_tg           | 861 ms                                                 | 542 ms: 1.59x faster                                         |
| async_tree_memoization_tg  | 463 ms                                                 | 315 ms: 1.47x faster                                         |
| create_gc_cycles           | 2.45 ms                                                | 1.71 ms: 1.43x faster                                        |
| async_tree_io              | 838 ms                                                 | 597 ms: 1.40x faster                                         |
| async_tree_none_tg         | 319 ms                                                 | 235 ms: 1.36x faster                                         |
| async_tree_none            | 350 ms                                                 | 290 ms: 1.21x faster                                         |
| async_tree_memoization     | 437 ms                                                 | 367 ms: 1.19x faster                                         |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 466 ms: 1.17x faster                                         |
| deepcopy                   | 354 us                                                 | 311 us: 1.14x faster                                         |
| regex_effbot               | 3.77 ms                                                | 3.36 ms: 1.12x faster                                        |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 522 ms: 1.10x faster                                         |
| regex_v8                   | 26.9 ms                                                | 24.8 ms: 1.08x faster                                        |
| gc_traversal               | 4.90 ms                                                | 4.56 ms: 1.07x faster                                        |
| sqlite_synth               | 2.90 us                                                | 2.73 us: 1.06x faster                                        |
| pathlib                    | 17.4 ms                                                | 16.4 ms: 1.06x faster                                        |
| xml_etree_iterparse        | 101 ms                                                 | 96.2 ms: 1.05x faster                                        |
| xml_etree_parse            | 154 ms                                                 | 149 ms: 1.04x faster                                         |
| pycparser                  | 1.20 sec                                               | 1.18 sec: 1.01x faster                                       |
| float                      | 78.7 ms                                                | 78.2 ms: 1.01x faster                                        |
| deepcopy_reduce            | 3.24 us                                                | 3.26 us: 1.00x slower                                        |
| regex_dna                  | 220 ms                                                 | 222 ms: 1.01x slower                                         |
| pidigits                   | 186 ms                                                 | 190 ms: 1.02x slower                                         |
| async_generators           | 433 ms                                                 | 445 ms: 1.03x slower                                         |
| deepcopy_memo              | 38.4 us                                                | 39.7 us: 1.04x slower                                        |
| k_core                     | 2.37 sec                                               | 2.46 sec: 1.04x slower                                       |
| spectral_norm              | 113 ms                                                 | 119 ms: 1.05x slower                                         |
| json                       | 5.32 ms                                                | 5.60 ms: 1.05x slower                                        |
| dulwich_log                | 64.6 ms                                                | 68.7 ms: 1.06x slower                                        |
| bpe_tokeniser              | 4.69 sec                                               | 5.04 sec: 1.07x slower                                       |
| mdp                        | 2.54 sec                                               | 2.74 sec: 1.08x slower                                       |
| generators                 | 28.8 ms                                                | 31.1 ms: 1.08x slower                                        |
| telco                      | 8.40 ms                                                | 9.09 ms: 1.08x slower                                        |
| docutils                   | 2.58 sec                                               | 2.83 sec: 1.09x slower                                       |
| html5lib                   | 63.4 ms                                                | 69.5 ms: 1.10x slower                                        |
| sphinx                     | 1.03 sec                                               | 1.13 sec: 1.10x slower                                       |
| xml_etree_generate         | 86.8 ms                                                | 96.1 ms: 1.11x slower                                        |
| sqlglot_normalize          | 108 ms                                                 | 120 ms: 1.11x slower                                         |
| xml_etree_process          | 60.5 ms                                                | 68.0 ms: 1.12x slower                                        |
| regex_compile              | 132 ms                                                 | 149 ms: 1.13x slower                                         |
| pyflate                    | 470 ms                                                 | 532 ms: 1.13x slower                                         |
| richards                   | 47.5 ms                                                | 54.0 ms: 1.14x slower                                        |
| tomli_loads                | 2.12 sec                                               | 2.41 sec: 1.14x slower                                       |
| scimark_sor                | 122 ms                                                 | 139 ms: 1.14x slower                                         |
| sqlglot_optimize           | 53.4 ms                                                | 61.1 ms: 1.14x slower                                        |
| coroutines                 | 22.2 ms                                                | 25.5 ms: 1.15x slower                                        |
| sympy_expand               | 456 ms                                                 | 527 ms: 1.16x slower                                         |
| scimark_fft                | 367 ms                                                 | 426 ms: 1.16x slower                                         |
| 2to3                       | 266 ms                                                 | 309 ms: 1.16x slower                                         |
| sympy_str                  | 273 ms                                                 | 319 ms: 1.17x slower                                         |
| json_loads                 | 27.2 us                                                | 31.8 us: 1.17x slower                                        |
| pprint_safe_repr           | 727 ms                                                 | 852 ms: 1.17x slower                                         |
| shortest_path              | 487 ms                                                 | 572 ms: 1.18x slower                                         |
| sympy_sum                  | 150 ms                                                 | 177 ms: 1.18x slower                                         |
| thrift                     | 800 us                                                 | 948 us: 1.19x slower                                         |
| pprint_pformat             | 1.48 sec                                               | 1.75 sec: 1.19x slower                                       |
| logging_silent             | 101 ns                                                 | 120 ns: 1.19x slower                                         |
| python_startup             | 12.7 ms                                                | 15.0 ms: 1.19x slower                                        |
| connected_components       | 447 ms                                                 | 531 ms: 1.19x slower                                         |
| genshi_xml                 | 50.5 ms                                                | 60.1 ms: 1.19x slower                                        |
| logging_simple             | 5.65 us                                                | 6.73 us: 1.19x slower                                        |
| sympy_integrate            | 19.8 ms                                                | 23.7 ms: 1.20x slower                                        |
| richards_super             | 53.7 ms                                                | 64.3 ms: 1.20x slower                                        |
| unpickle_pure_python       | 213 us                                                 | 256 us: 1.20x slower                                         |
| crypto_pyaes               | 74.7 ms                                                | 90.4 ms: 1.21x slower                                        |
| pickle_pure_python         | 302 us                                                 | 368 us: 1.22x slower                                         |
| logging_format             | 6.23 us                                                | 7.58 us: 1.22x slower                                        |
| sqlalchemy_imperative      | 16.9 ms                                                | 20.6 ms: 1.22x slower                                        |
| sqlalchemy_declarative     | 133 ms                                                 | 162 ms: 1.22x slower                                         |
| meteor_contest             | 108 ms                                                 | 133 ms: 1.23x slower                                         |
| sqlglot_transpile          | 1.57 ms                                                | 1.93 ms: 1.23x slower                                        |
| nqueens                    | 80.9 ms                                                | 100 ms: 1.24x slower                                         |
| scimark_lu                 | 114 ms                                                 | 142 ms: 1.25x slower                                         |
| sqlglot_parse              | 1.26 ms                                                | 1.59 ms: 1.25x slower                                        |
| genshi_text                | 22.6 ms                                                | 28.4 ms: 1.25x slower                                        |
| json_dumps                 | 10.1 ms                                                | 12.7 ms: 1.26x slower                                        |
| comprehensions             | 16.5 us                                                | 20.8 us: 1.26x slower                                        |
| many_optionals             | 857 us                                                 | 1.09 ms: 1.27x slower                                        |
| hexiom                     | 6.08 ms                                                | 7.76 ms: 1.28x slower                                        |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 6.45 ms: 1.28x slower                                        |
| chaos                      | 58.0 ms                                                | 74.5 ms: 1.28x slower                                        |
| coverage                   | 82.8 ms                                                | 108 ms: 1.30x slower                                         |
| scimark_monte_carlo        | 66.8 ms                                                | 87.2 ms: 1.31x slower                                        |
| fannkuch                   | 394 ms                                                 | 516 ms: 1.31x slower                                         |
| typing_runtime_protocols   | 160 us                                                 | 211 us: 1.32x slower                                         |
| django_template            | 31.7 ms                                                | 41.7 ms: 1.32x slower                                        |
| python_startup_no_site     | 7.00 ms                                                | 9.35 ms: 1.34x slower                                        |
| raytrace                   | 262 ms                                                 | 356 ms: 1.36x slower                                         |
| deltablue                  | 3.19 ms                                                | 4.72 ms: 1.48x slower                                        |
| mako                       | 10.7 ms                                                | 16.2 ms: 1.52x slower                                        |
| subparsers                 | 15.5 ms                                                | 24.7 ms: 1.60x slower                                        |
| nbody                      | 87.7 ms                                                | 141 ms: 1.61x slower                                         |
| bench_mp_pool              | 24.0 ms                                                | 89.3 ms: 3.72x slower                                        |
| bench_thread_pool          | 818 us                                                 | 3.49 ms: 4.27x slower                                        |
| Geometric mean             | (ref)                                                  | 1.14x slower                                                 |

Benchmark hidden because not significant (3): asyncio_websockets, go, pylint
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http

- Geometric mean (including insignificant results): 1.096x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.09x
- 95% likely to have a slowdown of 1.08x
- 99% likely to have a slowdown of 1.07x

# Memory
- memory change: 1.22x
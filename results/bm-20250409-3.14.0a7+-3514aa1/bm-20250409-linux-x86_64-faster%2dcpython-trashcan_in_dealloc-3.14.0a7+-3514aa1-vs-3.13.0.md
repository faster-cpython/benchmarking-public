# Results vs. 3.13.0

- fork: faster-cpython
- ref: trashcan_in_dealloc
- machine: linux-x86_64
- commit hash: 3514aa1
- commit date: 2025-04-09
- overall geometric mean: 1.051x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.03x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250409-linux-x86_64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-3514aa1 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 252 ms: 1.05x faster                                                            |
| docutils       | 2.58 sec                                               | 2.60 sec: 1.01x slower                                                          |
| html5lib       | 63.4 ms                                                | 61.1 ms: 1.04x faster                                                           |
| sphinx         | 1.03 sec                                               | 1.01 sec: 1.02x faster                                                          |
| Geometric mean | (ref)                                                  | 1.02x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250409-linux-x86_64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-3514aa1 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 317 ms: 1.46x faster                                                            |
| async_tree_memoization     | 437 ms                                                 | 313 ms: 1.39x faster                                                            |
| async_tree_io_tg           | 861 ms                                                 | 618 ms: 1.39x faster                                                            |
| async_tree_io              | 838 ms                                                 | 615 ms: 1.36x faster                                                            |
| async_tree_none            | 350 ms                                                 | 261 ms: 1.34x faster                                                            |
| async_tree_none_tg         | 319 ms                                                 | 251 ms: 1.27x faster                                                            |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 486 ms: 1.18x faster                                                            |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 482 ms: 1.13x faster                                                            |
| async_generators           | 433 ms                                                 | 407 ms: 1.06x faster                                                            |
| coroutines                 | 22.2 ms                                                | 23.4 ms: 1.05x slower                                                           |
| Geometric mean             | (ref)                                                  | 1.22x faster                                                                    |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250409-linux-x86_64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-3514aa1 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 70.6 ms: 1.11x faster                                                           |
| pidigits       | 186 ms                                                 | 186 ms: 1.00x faster                                                            |
| nbody          | 87.7 ms                                                | 94.6 ms: 1.08x slower                                                           |
| Geometric mean | (ref)                                                  | 1.01x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250409-linux-x86_64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-3514aa1 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                | 3.26 ms: 1.16x faster                                                           |
| regex_v8       | 26.9 ms                                                | 23.8 ms: 1.13x faster                                                           |
| regex_compile  | 132 ms                                                 | 125 ms: 1.06x faster                                                            |
| regex_dna      | 220 ms                                                 | 212 ms: 1.04x faster                                                            |
| Geometric mean | (ref)                                                  | 1.09x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250409-linux-x86_64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-3514aa1 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| xml_etree_parse      | 154 ms                                                 | 142 ms: 1.09x faster                                                            |
| tomli_loads          | 2.12 sec                                               | 2.00 sec: 1.06x faster                                                          |
| xml_etree_process    | 60.5 ms                                                | 58.9 ms: 1.03x faster                                                           |
| xml_etree_iterparse  | 101 ms                                                 | 98.8 ms: 1.03x faster                                                           |
| xml_etree_generate   | 86.8 ms                                                | 84.8 ms: 1.02x faster                                                           |
| unpickle_pure_python | 213 us                                                 | 218 us: 1.02x slower                                                            |
| pickle_pure_python   | 302 us                                                 | 316 us: 1.04x slower                                                            |
| json_loads           | 27.2 us                                                | 30.5 us: 1.12x slower                                                           |
| json_dumps           | 10.1 ms                                                | 11.6 ms: 1.14x slower                                                           |
| Geometric mean       | (ref)                                                  | 1.01x slower                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250409-linux-x86_64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-3514aa1 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 12.7 ms                                                | 13.2 ms: 1.04x slower                                                           |
| python_startup_no_site | 7.00 ms                                                | 8.23 ms: 1.18x slower                                                           |
| Geometric mean         | (ref)                                                  | 1.11x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250409-linux-x86_64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-3514aa1 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| genshi_text     | 22.6 ms                                                | 21.1 ms: 1.07x faster                                                           |
| genshi_xml      | 50.5 ms                                                | 49.0 ms: 1.03x faster                                                           |
| django_template | 31.7 ms                                                | 31.5 ms: 1.00x faster                                                           |
| mako            | 10.7 ms                                                | 11.5 ms: 1.07x slower                                                           |
| Geometric mean  | (ref)                                                  | 1.01x faster                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250409-linux-x86_64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-3514aa1 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mdp                        | 2.54 sec                                               | 1.23 sec: 2.06x faster                                                          |
| async_tree_memoization_tg  | 463 ms                                                 | 317 ms: 1.46x faster                                                            |
| deepcopy                   | 354 us                                                 | 253 us: 1.40x faster                                                            |
| async_tree_memoization     | 437 ms                                                 | 313 ms: 1.39x faster                                                            |
| async_tree_io_tg           | 861 ms                                                 | 618 ms: 1.39x faster                                                            |
| async_tree_io              | 838 ms                                                 | 615 ms: 1.36x faster                                                            |
| async_tree_none            | 350 ms                                                 | 261 ms: 1.34x faster                                                            |
| deepcopy_memo              | 38.4 us                                                | 29.4 us: 1.31x faster                                                           |
| go                         | 141 ms                                                 | 110 ms: 1.28x faster                                                            |
| async_tree_none_tg         | 319 ms                                                 | 251 ms: 1.27x faster                                                            |
| deepcopy_reduce            | 3.24 us                                                | 2.65 us: 1.22x faster                                                           |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 486 ms: 1.18x faster                                                            |
| regex_effbot               | 3.77 ms                                                | 3.26 ms: 1.16x faster                                                           |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 482 ms: 1.13x faster                                                            |
| regex_v8                   | 26.9 ms                                                | 23.8 ms: 1.13x faster                                                           |
| pylint                     | 312 ms                                                 | 278 ms: 1.12x faster                                                            |
| richards                   | 47.5 ms                                                | 42.5 ms: 1.12x faster                                                           |
| float                      | 78.7 ms                                                | 70.6 ms: 1.11x faster                                                           |
| richards_super             | 53.7 ms                                                | 48.5 ms: 1.11x faster                                                           |
| xml_etree_parse            | 154 ms                                                 | 142 ms: 1.09x faster                                                            |
| spectral_norm              | 113 ms                                                 | 104 ms: 1.08x faster                                                            |
| dulwich_log                | 64.6 ms                                                | 59.7 ms: 1.08x faster                                                           |
| pycparser                  | 1.20 sec                                               | 1.11 sec: 1.08x faster                                                          |
| genshi_text                | 22.6 ms                                                | 21.1 ms: 1.07x faster                                                           |
| telco                      | 8.40 ms                                                | 7.85 ms: 1.07x faster                                                           |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.71 ms: 1.07x faster                                                           |
| async_generators           | 433 ms                                                 | 407 ms: 1.06x faster                                                            |
| tomli_loads                | 2.12 sec                                               | 2.00 sec: 1.06x faster                                                          |
| regex_compile              | 132 ms                                                 | 125 ms: 1.06x faster                                                            |
| 2to3                       | 266 ms                                                 | 252 ms: 1.05x faster                                                            |
| regex_dna                  | 220 ms                                                 | 212 ms: 1.04x faster                                                            |
| html5lib                   | 63.4 ms                                                | 61.1 ms: 1.04x faster                                                           |
| k_core                     | 2.37 sec                                               | 2.29 sec: 1.04x faster                                                          |
| sqlite_synth               | 2.90 us                                                | 2.81 us: 1.03x faster                                                           |
| pyflate                    | 470 ms                                                 | 454 ms: 1.03x faster                                                            |
| logging_silent             | 101 ns                                                 | 97.8 ns: 1.03x faster                                                           |
| sympy_integrate            | 19.8 ms                                                | 19.2 ms: 1.03x faster                                                           |
| genshi_xml                 | 50.5 ms                                                | 49.0 ms: 1.03x faster                                                           |
| logging_simple             | 5.65 us                                                | 5.49 us: 1.03x faster                                                           |
| logging_format             | 6.23 us                                                | 6.06 us: 1.03x faster                                                           |
| scimark_fft                | 367 ms                                                 | 357 ms: 1.03x faster                                                            |
| xml_etree_process          | 60.5 ms                                                | 58.9 ms: 1.03x faster                                                           |
| bpe_tokeniser              | 4.69 sec                                               | 4.57 sec: 1.03x faster                                                          |
| meteor_contest             | 108 ms                                                 | 106 ms: 1.03x faster                                                            |
| xml_etree_iterparse        | 101 ms                                                 | 98.8 ms: 1.03x faster                                                           |
| pathlib                    | 17.4 ms                                                | 17.0 ms: 1.02x faster                                                           |
| xml_etree_generate         | 86.8 ms                                                | 84.8 ms: 1.02x faster                                                           |
| scimark_sor                | 122 ms                                                 | 120 ms: 1.02x faster                                                            |
| chaos                      | 58.0 ms                                                | 57.0 ms: 1.02x faster                                                           |
| pprint_safe_repr           | 727 ms                                                 | 714 ms: 1.02x faster                                                            |
| sphinx                     | 1.03 sec                                               | 1.01 sec: 1.02x faster                                                          |
| sympy_str                  | 273 ms                                                 | 269 ms: 1.02x faster                                                            |
| scimark_monte_carlo        | 66.8 ms                                                | 65.9 ms: 1.01x faster                                                           |
| pprint_pformat             | 1.48 sec                                               | 1.47 sec: 1.01x faster                                                          |
| sympy_sum                  | 150 ms                                                 | 150 ms: 1.01x faster                                                            |
| django_template            | 31.7 ms                                                | 31.5 ms: 1.00x faster                                                           |
| crypto_pyaes               | 74.7 ms                                                | 74.4 ms: 1.00x faster                                                           |
| pidigits                   | 186 ms                                                 | 186 ms: 1.00x faster                                                            |
| sqlalchemy_declarative     | 133 ms                                                 | 133 ms: 1.00x faster                                                            |
| sqlalchemy_imperative      | 16.9 ms                                                | 17.0 ms: 1.01x slower                                                           |
| sympy_expand               | 456 ms                                                 | 459 ms: 1.01x slower                                                            |
| shortest_path              | 487 ms                                                 | 490 ms: 1.01x slower                                                            |
| docutils                   | 2.58 sec                                               | 2.60 sec: 1.01x slower                                                          |
| hexiom                     | 6.08 ms                                                | 6.12 ms: 1.01x slower                                                           |
| nqueens                    | 80.9 ms                                                | 81.5 ms: 1.01x slower                                                           |
| create_gc_cycles           | 2.45 ms                                                | 2.47 ms: 1.01x slower                                                           |
| raytrace                   | 262 ms                                                 | 264 ms: 1.01x slower                                                            |
| generators                 | 28.8 ms                                                | 29.1 ms: 1.01x slower                                                           |
| connected_components       | 447 ms                                                 | 452 ms: 1.01x slower                                                            |
| scimark_lu                 | 114 ms                                                 | 117 ms: 1.02x slower                                                            |
| unpickle_pure_python       | 213 us                                                 | 218 us: 1.02x slower                                                            |
| gc_traversal               | 4.90 ms                                                | 5.03 ms: 1.03x slower                                                           |
| comprehensions             | 16.5 us                                                | 17.0 us: 1.03x slower                                                           |
| coverage                   | 82.8 ms                                                | 85.7 ms: 1.03x slower                                                           |
| typing_runtime_protocols   | 160 us                                                 | 166 us: 1.03x slower                                                            |
| json                       | 5.32 ms                                                | 5.51 ms: 1.04x slower                                                           |
| deltablue                  | 3.19 ms                                                | 3.33 ms: 1.04x slower                                                           |
| pickle_pure_python         | 302 us                                                 | 316 us: 1.04x slower                                                            |
| python_startup             | 12.7 ms                                                | 13.2 ms: 1.04x slower                                                           |
| coroutines                 | 22.2 ms                                                | 23.4 ms: 1.05x slower                                                           |
| fannkuch                   | 394 ms                                                 | 415 ms: 1.05x slower                                                            |
| mako                       | 10.7 ms                                                | 11.5 ms: 1.07x slower                                                           |
| nbody                      | 87.7 ms                                                | 94.6 ms: 1.08x slower                                                           |
| bench_thread_pool          | 818 us                                                 | 884 us: 1.08x slower                                                            |
| many_optionals             | 857 us                                                 | 935 us: 1.09x slower                                                            |
| json_loads                 | 27.2 us                                                | 30.5 us: 1.12x slower                                                           |
| json_dumps                 | 10.1 ms                                                | 11.6 ms: 1.14x slower                                                           |
| python_startup_no_site     | 7.00 ms                                                | 8.23 ms: 1.18x slower                                                           |
| subparsers                 | 15.5 ms                                                | 20.9 ms: 1.35x slower                                                           |
| bench_mp_pool              | 24.0 ms                                                | 82.4 ms: 3.44x slower                                                           |
| Geometric mean             | (ref)                                                  | 1.04x faster                                                                    |

Benchmark hidden because not significant (1): asyncio_websockets
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
Ignored benchmarks (4) of results/bm-20250409-3.14.0a7+-3514aa1/bm-20250409-linux-x86_64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-3514aa1.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.051x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.03x
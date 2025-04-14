# Results vs. 3.13.0

- fork: iritkatriel
- ref: dicts_plus
- machine: linux-x86_64
- commit hash: 3d9cf36
- commit date: 2025-04-12
- overall geometric mean: 1.060x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250412-linux-x86_64-iritkatriel-dicts_plus-3.14.0a7+-3d9cf36 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 250 ms: 1.06x faster                                              |
| html5lib       | 63.4 ms                                                | 61.6 ms: 1.03x faster                                             |
| sphinx         | 1.03 sec                                               | 1.01 sec: 1.02x faster                                            |
| Geometric mean | (ref)                                                  | 1.03x faster                                                      |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250412-linux-x86_64-iritkatriel-dicts_plus-3.14.0a7+-3d9cf36 |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 316 ms: 1.47x faster                                              |
| async_tree_memoization     | 437 ms                                                 | 311 ms: 1.40x faster                                              |
| async_tree_io_tg           | 861 ms                                                 | 614 ms: 1.40x faster                                              |
| async_tree_io              | 838 ms                                                 | 610 ms: 1.37x faster                                              |
| async_tree_none            | 350 ms                                                 | 256 ms: 1.37x faster                                              |
| async_tree_none_tg         | 319 ms                                                 | 248 ms: 1.29x faster                                              |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 476 ms: 1.20x faster                                              |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 474 ms: 1.15x faster                                              |
| async_generators           | 433 ms                                                 | 393 ms: 1.10x faster                                              |
| coroutines                 | 22.2 ms                                                | 24.1 ms: 1.09x slower                                             |
| Geometric mean             | (ref)                                                  | 1.23x faster                                                      |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250412-linux-x86_64-iritkatriel-dicts_plus-3.14.0a7+-3d9cf36 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| float          | 78.7 ms                                                | 67.1 ms: 1.17x faster                                             |
| pidigits       | 186 ms                                                 | 186 ms: 1.00x faster                                              |
| nbody          | 87.7 ms                                                | 95.2 ms: 1.09x slower                                             |
| Geometric mean | (ref)                                                  | 1.03x faster                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250412-linux-x86_64-iritkatriel-dicts_plus-3.14.0a7+-3d9cf36 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                | 3.26 ms: 1.15x faster                                             |
| regex_v8       | 26.9 ms                                                | 23.3 ms: 1.15x faster                                             |
| regex_compile  | 132 ms                                                 | 125 ms: 1.06x faster                                              |
| regex_dna      | 220 ms                                                 | 215 ms: 1.02x faster                                              |
| Geometric mean | (ref)                                                  | 1.09x faster                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250412-linux-x86_64-iritkatriel-dicts_plus-3.14.0a7+-3d9cf36 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| xml_etree_parse      | 154 ms                                                 | 141 ms: 1.09x faster                                              |
| tomli_loads          | 2.12 sec                                               | 1.95 sec: 1.09x faster                                            |
| xml_etree_generate   | 86.8 ms                                                | 83.4 ms: 1.04x faster                                             |
| xml_etree_process    | 60.5 ms                                                | 58.2 ms: 1.04x faster                                             |
| xml_etree_iterparse  | 101 ms                                                 | 99.3 ms: 1.02x faster                                             |
| unpickle_pure_python | 213 us                                                 | 219 us: 1.03x slower                                              |
| pickle_pure_python   | 302 us                                                 | 315 us: 1.04x slower                                              |
| json_loads           | 27.2 us                                                | 29.2 us: 1.07x slower                                             |
| json_dumps           | 10.1 ms                                                | 11.5 ms: 1.14x slower                                             |
| Geometric mean       | (ref)                                                  | 1.00x faster                                                      |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250412-linux-x86_64-iritkatriel-dicts_plus-3.14.0a7+-3d9cf36 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| python_startup         | 12.7 ms                                                | 13.2 ms: 1.04x slower                                             |
| python_startup_no_site | 7.00 ms                                                | 8.21 ms: 1.17x slower                                             |
| Geometric mean         | (ref)                                                  | 1.11x slower                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250412-linux-x86_64-iritkatriel-dicts_plus-3.14.0a7+-3d9cf36 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| genshi_text     | 22.6 ms                                                | 20.9 ms: 1.08x faster                                             |
| genshi_xml      | 50.5 ms                                                | 48.1 ms: 1.05x faster                                             |
| django_template | 31.7 ms                                                | 31.3 ms: 1.01x faster                                             |
| mako            | 10.7 ms                                                | 11.2 ms: 1.05x slower                                             |
| Geometric mean  | (ref)                                                  | 1.02x faster                                                      |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250412-linux-x86_64-iritkatriel-dicts_plus-3.14.0a7+-3d9cf36 |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| mdp                        | 2.54 sec                                               | 1.20 sec: 2.11x faster                                            |
| async_tree_memoization_tg  | 463 ms                                                 | 316 ms: 1.47x faster                                              |
| deepcopy                   | 354 us                                                 | 249 us: 1.42x faster                                              |
| async_tree_memoization     | 437 ms                                                 | 311 ms: 1.40x faster                                              |
| async_tree_io_tg           | 861 ms                                                 | 614 ms: 1.40x faster                                              |
| async_tree_io              | 838 ms                                                 | 610 ms: 1.37x faster                                              |
| async_tree_none            | 350 ms                                                 | 256 ms: 1.37x faster                                              |
| deepcopy_memo              | 38.4 us                                                | 28.6 us: 1.34x faster                                             |
| async_tree_none_tg         | 319 ms                                                 | 248 ms: 1.29x faster                                              |
| go                         | 141 ms                                                 | 110 ms: 1.27x faster                                              |
| deepcopy_reduce            | 3.24 us                                                | 2.63 us: 1.23x faster                                             |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 476 ms: 1.20x faster                                              |
| float                      | 78.7 ms                                                | 67.1 ms: 1.17x faster                                             |
| regex_effbot               | 3.77 ms                                                | 3.26 ms: 1.15x faster                                             |
| spectral_norm              | 113 ms                                                 | 98.1 ms: 1.15x faster                                             |
| regex_v8                   | 26.9 ms                                                | 23.3 ms: 1.15x faster                                             |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 474 ms: 1.15x faster                                              |
| pylint                     | 312 ms                                                 | 278 ms: 1.12x faster                                              |
| async_generators           | 433 ms                                                 | 393 ms: 1.10x faster                                              |
| richards                   | 47.5 ms                                                | 43.2 ms: 1.10x faster                                             |
| xml_etree_parse            | 154 ms                                                 | 141 ms: 1.09x faster                                              |
| tomli_loads                | 2.12 sec                                               | 1.95 sec: 1.09x faster                                            |
| genshi_text                | 22.6 ms                                                | 20.9 ms: 1.08x faster                                             |
| dulwich_log                | 64.6 ms                                                | 59.7 ms: 1.08x faster                                             |
| richards_super             | 53.7 ms                                                | 49.7 ms: 1.08x faster                                             |
| telco                      | 8.40 ms                                                | 7.88 ms: 1.07x faster                                             |
| logging_silent             | 101 ns                                                 | 94.8 ns: 1.07x faster                                             |
| bpe_tokeniser              | 4.69 sec                                               | 4.40 sec: 1.06x faster                                            |
| scimark_fft                | 367 ms                                                 | 345 ms: 1.06x faster                                              |
| 2to3                       | 266 ms                                                 | 250 ms: 1.06x faster                                              |
| regex_compile              | 132 ms                                                 | 125 ms: 1.06x faster                                              |
| pyflate                    | 470 ms                                                 | 445 ms: 1.06x faster                                              |
| genshi_xml                 | 50.5 ms                                                | 48.1 ms: 1.05x faster                                             |
| sympy_integrate            | 19.8 ms                                                | 18.9 ms: 1.05x faster                                             |
| scimark_sor                | 122 ms                                                 | 117 ms: 1.04x faster                                              |
| sqlite_synth               | 2.90 us                                                | 2.78 us: 1.04x faster                                             |
| k_core                     | 2.37 sec                                               | 2.27 sec: 1.04x faster                                            |
| xml_etree_generate         | 86.8 ms                                                | 83.4 ms: 1.04x faster                                             |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.83 ms: 1.04x faster                                             |
| xml_etree_process          | 60.5 ms                                                | 58.2 ms: 1.04x faster                                             |
| logging_simple             | 5.65 us                                                | 5.44 us: 1.04x faster                                             |
| logging_format             | 6.23 us                                                | 6.01 us: 1.04x faster                                             |
| chaos                      | 58.0 ms                                                | 56.0 ms: 1.04x faster                                             |
| sympy_str                  | 273 ms                                                 | 264 ms: 1.03x faster                                              |
| crypto_pyaes               | 74.7 ms                                                | 72.3 ms: 1.03x faster                                             |
| pathlib                    | 17.4 ms                                                | 16.8 ms: 1.03x faster                                             |
| pycparser                  | 1.20 sec                                               | 1.16 sec: 1.03x faster                                            |
| html5lib                   | 63.4 ms                                                | 61.6 ms: 1.03x faster                                             |
| regex_dna                  | 220 ms                                                 | 215 ms: 1.02x faster                                              |
| sympy_sum                  | 150 ms                                                 | 147 ms: 1.02x faster                                              |
| pprint_safe_repr           | 727 ms                                                 | 712 ms: 1.02x faster                                              |
| xml_etree_iterparse        | 101 ms                                                 | 99.3 ms: 1.02x faster                                             |
| sphinx                     | 1.03 sec                                               | 1.01 sec: 1.02x faster                                            |
| sqlalchemy_declarative     | 133 ms                                                 | 131 ms: 1.02x faster                                              |
| meteor_contest             | 108 ms                                                 | 107 ms: 1.02x faster                                              |
| scimark_monte_carlo        | 66.8 ms                                                | 65.9 ms: 1.01x faster                                             |
| pprint_pformat             | 1.48 sec                                               | 1.46 sec: 1.01x faster                                            |
| json                       | 5.32 ms                                                | 5.26 ms: 1.01x faster                                             |
| django_template            | 31.7 ms                                                | 31.3 ms: 1.01x faster                                             |
| sympy_expand               | 456 ms                                                 | 453 ms: 1.01x faster                                              |
| raytrace                   | 262 ms                                                 | 260 ms: 1.01x faster                                              |
| pidigits                   | 186 ms                                                 | 186 ms: 1.00x faster                                              |
| hexiom                     | 6.08 ms                                                | 6.13 ms: 1.01x slower                                             |
| create_gc_cycles           | 2.45 ms                                                | 2.48 ms: 1.01x slower                                             |
| gc_traversal               | 4.90 ms                                                | 4.97 ms: 1.01x slower                                             |
| typing_runtime_protocols   | 160 us                                                 | 163 us: 1.02x slower                                              |
| scimark_lu                 | 114 ms                                                 | 117 ms: 1.03x slower                                              |
| unpickle_pure_python       | 213 us                                                 | 219 us: 1.03x slower                                              |
| shortest_path              | 487 ms                                                 | 502 ms: 1.03x slower                                              |
| generators                 | 28.8 ms                                                | 29.9 ms: 1.04x slower                                             |
| fannkuch                   | 394 ms                                                 | 409 ms: 1.04x slower                                              |
| pickle_pure_python         | 302 us                                                 | 315 us: 1.04x slower                                              |
| python_startup             | 12.7 ms                                                | 13.2 ms: 1.04x slower                                             |
| mako                       | 10.7 ms                                                | 11.2 ms: 1.05x slower                                             |
| coverage                   | 82.8 ms                                                | 87.0 ms: 1.05x slower                                             |
| deltablue                  | 3.19 ms                                                | 3.39 ms: 1.06x slower                                             |
| json_loads                 | 27.2 us                                                | 29.2 us: 1.07x slower                                             |
| bench_thread_pool          | 818 us                                                 | 884 us: 1.08x slower                                              |
| coroutines                 | 22.2 ms                                                | 24.1 ms: 1.09x slower                                             |
| nbody                      | 87.7 ms                                                | 95.2 ms: 1.09x slower                                             |
| many_optionals             | 857 us                                                 | 932 us: 1.09x slower                                              |
| json_dumps                 | 10.1 ms                                                | 11.5 ms: 1.14x slower                                             |
| python_startup_no_site     | 7.00 ms                                                | 8.21 ms: 1.17x slower                                             |
| subparsers                 | 15.5 ms                                                | 20.8 ms: 1.35x slower                                             |
| bench_mp_pool              | 24.0 ms                                                | 81.9 ms: 3.42x slower                                             |
| Geometric mean             | (ref)                                                  | 1.04x faster                                                      |

Benchmark hidden because not significant (6): sqlalchemy_imperative, nqueens, comprehensions, asyncio_websockets, docutils, connected_components
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
Ignored benchmarks (4) of results/bm-20250412-3.14.0a7+-3d9cf36/bm-20250412-linux-x86_64-iritkatriel-dicts_plus-3.14.0a7+-3d9cf36.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.060x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.04x
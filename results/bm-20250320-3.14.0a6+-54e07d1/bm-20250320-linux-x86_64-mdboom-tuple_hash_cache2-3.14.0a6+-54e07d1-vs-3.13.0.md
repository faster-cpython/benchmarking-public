# Results vs. 3.13.0

- fork: mdboom
- ref: tuple_hash_cache2
- machine: linux-x86_64
- commit hash: 54e07d1
- commit date: 2025-03-20
- overall geometric mean: 1.045x faster
- HPT reliability: 99.94%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250320-linux-x86_64-mdboom-tuple_hash_cache2-3.14.0a6+-54e07d1 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 258 ms: 1.03x faster                                                |
| docutils       | 2.58 sec                                               | 2.61 sec: 1.01x slower                                              |
| html5lib       | 63.4 ms                                                | 62.8 ms: 1.01x faster                                               |
| sphinx         | 1.03 sec                                               | 1.02 sec: 1.02x faster                                              |
| Geometric mean | (ref)                                                  | 1.01x faster                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250320-linux-x86_64-mdboom-tuple_hash_cache2-3.14.0a6+-54e07d1 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 321 ms: 1.44x faster                                                |
| async_tree_io_tg           | 861 ms                                                 | 613 ms: 1.40x faster                                                |
| async_tree_memoization     | 437 ms                                                 | 319 ms: 1.37x faster                                                |
| async_tree_io              | 838 ms                                                 | 616 ms: 1.36x faster                                                |
| async_tree_none            | 350 ms                                                 | 261 ms: 1.34x faster                                                |
| async_tree_none_tg         | 319 ms                                                 | 252 ms: 1.27x faster                                                |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 495 ms: 1.16x faster                                                |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 484 ms: 1.12x faster                                                |
| async_generators           | 433 ms                                                 | 403 ms: 1.07x faster                                                |
| coroutines                 | 22.2 ms                                                | 23.6 ms: 1.06x slower                                               |
| Geometric mean             | (ref)                                                  | 1.21x faster                                                        |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250320-linux-x86_64-mdboom-tuple_hash_cache2-3.14.0a6+-54e07d1 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 71.4 ms: 1.10x faster                                               |
| pidigits       | 186 ms                                                 | 186 ms: 1.00x faster                                                |
| nbody          | 87.7 ms                                                | 101 ms: 1.15x slower                                                |
| Geometric mean | (ref)                                                  | 1.01x slower                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250320-linux-x86_64-mdboom-tuple_hash_cache2-3.14.0a6+-54e07d1 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                | 3.21 ms: 1.17x faster                                               |
| regex_v8       | 26.9 ms                                                | 24.0 ms: 1.12x faster                                               |
| regex_compile  | 132 ms                                                 | 127 ms: 1.04x faster                                                |
| regex_dna      | 220 ms                                                 | 216 ms: 1.02x faster                                                |
| Geometric mean | (ref)                                                  | 1.09x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250320-linux-x86_64-mdboom-tuple_hash_cache2-3.14.0a6+-54e07d1 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| xml_etree_parse      | 154 ms                                                 | 140 ms: 1.10x faster                                                |
| tomli_loads          | 2.12 sec                                               | 1.99 sec: 1.07x faster                                              |
| xml_etree_iterparse  | 101 ms                                                 | 98.7 ms: 1.03x faster                                               |
| xml_etree_generate   | 86.8 ms                                                | 84.7 ms: 1.03x faster                                               |
| xml_etree_process    | 60.5 ms                                                | 59.2 ms: 1.02x faster                                               |
| unpickle_pure_python | 213 us                                                 | 221 us: 1.04x slower                                                |
| pickle_pure_python   | 302 us                                                 | 318 us: 1.05x slower                                                |
| json_loads           | 27.2 us                                                | 29.7 us: 1.09x slower                                               |
| json_dumps           | 10.1 ms                                                | 11.5 ms: 1.14x slower                                               |
| Geometric mean       | (ref)                                                  | 1.01x slower                                                        |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250320-linux-x86_64-mdboom-tuple_hash_cache2-3.14.0a6+-54e07d1 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 12.7 ms                                                | 13.1 ms: 1.04x slower                                               |
| python_startup_no_site | 7.00 ms                                                | 8.19 ms: 1.17x slower                                               |
| Geometric mean         | (ref)                                                  | 1.10x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250320-linux-x86_64-mdboom-tuple_hash_cache2-3.14.0a6+-54e07d1 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| genshi_text    | 22.6 ms                                                | 21.6 ms: 1.05x faster                                               |
| genshi_xml     | 50.5 ms                                                | 49.1 ms: 1.03x faster                                               |
| mako           | 10.7 ms                                                | 11.5 ms: 1.08x slower                                               |
| Geometric mean | (ref)                                                  | 1.00x faster                                                        |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250320-linux-x86_64-mdboom-tuple_hash_cache2-3.14.0a6+-54e07d1 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| mdp                        | 2.54 sec                                               | 1.25 sec: 2.04x faster                                              |
| async_tree_memoization_tg  | 463 ms                                                 | 321 ms: 1.44x faster                                                |
| async_tree_io_tg           | 861 ms                                                 | 613 ms: 1.40x faster                                                |
| deepcopy                   | 354 us                                                 | 256 us: 1.39x faster                                                |
| async_tree_memoization     | 437 ms                                                 | 319 ms: 1.37x faster                                                |
| async_tree_io              | 838 ms                                                 | 616 ms: 1.36x faster                                                |
| async_tree_none            | 350 ms                                                 | 261 ms: 1.34x faster                                                |
| deepcopy_memo              | 38.4 us                                                | 30.2 us: 1.27x faster                                               |
| async_tree_none_tg         | 319 ms                                                 | 252 ms: 1.27x faster                                                |
| deepcopy_reduce            | 3.24 us                                                | 2.67 us: 1.21x faster                                               |
| go                         | 141 ms                                                 | 116 ms: 1.21x faster                                                |
| regex_effbot               | 3.77 ms                                                | 3.21 ms: 1.17x faster                                               |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 495 ms: 1.16x faster                                                |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 484 ms: 1.12x faster                                                |
| pylint                     | 312 ms                                                 | 278 ms: 1.12x faster                                                |
| regex_v8                   | 26.9 ms                                                | 24.0 ms: 1.12x faster                                               |
| float                      | 78.7 ms                                                | 71.4 ms: 1.10x faster                                               |
| dulwich_log                | 64.6 ms                                                | 58.7 ms: 1.10x faster                                               |
| xml_etree_parse            | 154 ms                                                 | 140 ms: 1.10x faster                                                |
| spectral_norm              | 113 ms                                                 | 103 ms: 1.10x faster                                                |
| richards                   | 47.5 ms                                                | 43.9 ms: 1.08x faster                                               |
| async_generators           | 433 ms                                                 | 403 ms: 1.07x faster                                                |
| telco                      | 8.40 ms                                                | 7.82 ms: 1.07x faster                                               |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.69 ms: 1.07x faster                                               |
| richards_super             | 53.7 ms                                                | 50.2 ms: 1.07x faster                                               |
| tomli_loads                | 2.12 sec                                               | 1.99 sec: 1.07x faster                                              |
| pathlib                    | 17.4 ms                                                | 16.5 ms: 1.05x faster                                               |
| pycparser                  | 1.20 sec                                               | 1.14 sec: 1.05x faster                                              |
| genshi_text                | 22.6 ms                                                | 21.6 ms: 1.05x faster                                               |
| sqlite_synth               | 2.90 us                                                | 2.77 us: 1.05x faster                                               |
| k_core                     | 2.37 sec                                               | 2.27 sec: 1.04x faster                                              |
| regex_compile              | 132 ms                                                 | 127 ms: 1.04x faster                                                |
| logging_silent             | 101 ns                                                 | 97.5 ns: 1.04x faster                                               |
| scimark_fft                | 367 ms                                                 | 355 ms: 1.03x faster                                                |
| pyflate                    | 470 ms                                                 | 455 ms: 1.03x faster                                                |
| 2to3                       | 266 ms                                                 | 258 ms: 1.03x faster                                                |
| genshi_xml                 | 50.5 ms                                                | 49.1 ms: 1.03x faster                                               |
| xml_etree_iterparse        | 101 ms                                                 | 98.7 ms: 1.03x faster                                               |
| xml_etree_generate         | 86.8 ms                                                | 84.7 ms: 1.03x faster                                               |
| generators                 | 28.8 ms                                                | 28.1 ms: 1.02x faster                                               |
| scimark_sor                | 122 ms                                                 | 119 ms: 1.02x faster                                                |
| sqlalchemy_declarative     | 133 ms                                                 | 130 ms: 1.02x faster                                                |
| xml_etree_process          | 60.5 ms                                                | 59.2 ms: 1.02x faster                                               |
| sqlalchemy_imperative      | 16.9 ms                                                | 16.6 ms: 1.02x faster                                               |
| regex_dna                  | 220 ms                                                 | 216 ms: 1.02x faster                                                |
| json                       | 5.32 ms                                                | 5.24 ms: 1.02x faster                                               |
| sphinx                     | 1.03 sec                                               | 1.02 sec: 1.02x faster                                              |
| gc_traversal               | 4.90 ms                                                | 4.82 ms: 1.02x faster                                               |
| bpe_tokeniser              | 4.69 sec                                               | 4.62 sec: 1.01x faster                                              |
| sympy_str                  | 273 ms                                                 | 269 ms: 1.01x faster                                                |
| logging_simple             | 5.65 us                                                | 5.58 us: 1.01x faster                                               |
| html5lib                   | 63.4 ms                                                | 62.8 ms: 1.01x faster                                               |
| deltablue                  | 3.19 ms                                                | 3.18 ms: 1.00x faster                                               |
| pidigits                   | 186 ms                                                 | 186 ms: 1.00x faster                                                |
| sympy_integrate            | 19.8 ms                                                | 20.0 ms: 1.01x slower                                               |
| sympy_expand               | 456 ms                                                 | 460 ms: 1.01x slower                                                |
| docutils                   | 2.58 sec                                               | 2.61 sec: 1.01x slower                                              |
| shortest_path              | 487 ms                                                 | 492 ms: 1.01x slower                                                |
| create_gc_cycles           | 2.45 ms                                                | 2.49 ms: 1.02x slower                                               |
| typing_runtime_protocols   | 160 us                                                 | 163 us: 1.02x slower                                                |
| crypto_pyaes               | 74.7 ms                                                | 75.9 ms: 1.02x slower                                               |
| connected_components       | 447 ms                                                 | 454 ms: 1.02x slower                                                |
| pprint_safe_repr           | 727 ms                                                 | 741 ms: 1.02x slower                                                |
| pprint_pformat             | 1.48 sec                                               | 1.51 sec: 1.02x slower                                              |
| coverage                   | 82.8 ms                                                | 84.7 ms: 1.02x slower                                               |
| chaos                      | 58.0 ms                                                | 59.4 ms: 1.02x slower                                               |
| scimark_lu                 | 114 ms                                                 | 118 ms: 1.03x slower                                                |
| comprehensions             | 16.5 us                                                | 17.0 us: 1.03x slower                                               |
| nqueens                    | 80.9 ms                                                | 83.6 ms: 1.03x slower                                               |
| raytrace                   | 262 ms                                                 | 271 ms: 1.04x slower                                                |
| unpickle_pure_python       | 213 us                                                 | 221 us: 1.04x slower                                                |
| scimark_monte_carlo        | 66.8 ms                                                | 69.2 ms: 1.04x slower                                               |
| python_startup             | 12.7 ms                                                | 13.1 ms: 1.04x slower                                               |
| hexiom                     | 6.08 ms                                                | 6.33 ms: 1.04x slower                                               |
| pickle_pure_python         | 302 us                                                 | 318 us: 1.05x slower                                                |
| coroutines                 | 22.2 ms                                                | 23.6 ms: 1.06x slower                                               |
| bench_thread_pool          | 818 us                                                 | 875 us: 1.07x slower                                                |
| mako                       | 10.7 ms                                                | 11.5 ms: 1.08x slower                                               |
| json_loads                 | 27.2 us                                                | 29.7 us: 1.09x slower                                               |
| many_optionals             | 857 us                                                 | 944 us: 1.10x slower                                                |
| fannkuch                   | 394 ms                                                 | 436 ms: 1.11x slower                                                |
| json_dumps                 | 10.1 ms                                                | 11.5 ms: 1.14x slower                                               |
| nbody                      | 87.7 ms                                                | 101 ms: 1.15x slower                                                |
| python_startup_no_site     | 7.00 ms                                                | 8.19 ms: 1.17x slower                                               |
| subparsers                 | 15.5 ms                                                | 20.9 ms: 1.35x slower                                               |
| bench_mp_pool              | 24.0 ms                                                | 83.2 ms: 3.47x slower                                               |
| Geometric mean             | (ref)                                                  | 1.03x faster                                                        |

Benchmark hidden because not significant (5): django_template, asyncio_websockets, sympy_sum, logging_format, meteor_contest
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
Ignored benchmarks (4) of results/bm-20250320-3.14.0a6+-54e07d1/bm-20250320-linux-x86_64-mdboom-tuple_hash_cache2-3.14.0a6+-54e07d1.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.045x faster

# HPT report

- Reliability score: 99.94% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.04x
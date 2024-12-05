# Results vs. 3.13.0

- fork: iritkatriel
- ref: cmq_mdboom
- machine: linux-x86_64
- commit hash: 6cacd2b
- commit date: 2024-12-04
- overall geometric mean: 1.014x faster
- HPT reliability: 97.90%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241204-linux-x86_64-iritkatriel-cmq_mdboom-3.14.0a0-6cacd2b |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 255 ms: 1.04x faster                                             |
| docutils       | 2.58 sec                                               | 2.65 sec: 1.03x slower                                           |
| html5lib       | 63.4 ms                                                | 62.0 ms: 1.02x faster                                            |
| tornado_http   | 91.2 ms                                                | 90.7 ms: 1.01x faster                                            |
| Geometric mean | (ref)                                                  | 1.01x faster                                                     |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241204-linux-x86_64-iritkatriel-cmq_mdboom-3.14.0a0-6cacd2b |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 388 ms: 1.19x faster                                             |
| async_tree_none            | 350 ms                                                 | 328 ms: 1.07x faster                                             |
| async_tree_none_tg         | 319 ms                                                 | 307 ms: 1.04x faster                                             |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 554 ms: 1.03x faster                                             |
| asyncio_websockets         | 551 ms                                                 | 557 ms: 1.01x slower                                             |
| async_generators           | 433 ms                                                 | 439 ms: 1.01x slower                                             |
| async_tree_io_tg           | 861 ms                                                 | 885 ms: 1.03x slower                                             |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 562 ms: 1.03x slower                                             |
| coroutines                 | 22.2 ms                                                | 23.4 ms: 1.05x slower                                            |
| async_tree_io              | 838 ms                                                 | 891 ms: 1.06x slower                                             |
| Geometric mean             | (ref)                                                  | 1.01x faster                                                     |

Benchmark hidden because not significant (1): async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241204-linux-x86_64-iritkatriel-cmq_mdboom-3.14.0a0-6cacd2b |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| float          | 78.7 ms                                                | 75.3 ms: 1.04x faster                                            |
| pidigits       | 186 ms                                                 | 187 ms: 1.00x slower                                             |
| nbody          | 87.7 ms                                                | 89.4 ms: 1.02x slower                                            |
| Geometric mean | (ref)                                                  | 1.01x faster                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241204-linux-x86_64-iritkatriel-cmq_mdboom-3.14.0a0-6cacd2b |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| regex_v8       | 26.9 ms                                                | 24.7 ms: 1.09x faster                                            |
| regex_effbot   | 3.77 ms                                                | 3.62 ms: 1.04x faster                                            |
| regex_compile  | 132 ms                                                 | 128 ms: 1.03x faster                                             |
| Geometric mean | (ref)                                                  | 1.04x faster                                                     |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241204-linux-x86_64-iritkatriel-cmq_mdboom-3.14.0a0-6cacd2b |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| xml_etree_process    | 60.5 ms                                                | 59.0 ms: 1.02x faster                                            |
| tomli_loads          | 2.12 sec                                               | 2.08 sec: 1.02x faster                                           |
| xml_etree_generate   | 86.8 ms                                                | 85.7 ms: 1.01x faster                                            |
| json_loads           | 27.2 us                                                | 27.3 us: 1.00x slower                                            |
| unpickle_pure_python | 213 us                                                 | 214 us: 1.01x slower                                             |
| pickle_pure_python   | 302 us                                                 | 305 us: 1.01x slower                                             |
| json_dumps           | 10.1 ms                                                | 10.3 ms: 1.01x slower                                            |
| xml_etree_parse      | 154 ms                                                 | 159 ms: 1.03x slower                                             |
| xml_etree_iterparse  | 101 ms                                                 | 105 ms: 1.03x slower                                             |
| Geometric mean       | (ref)                                                  | 1.00x slower                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241204-linux-x86_64-iritkatriel-cmq_mdboom-3.14.0a0-6cacd2b |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| python_startup_no_site | 7.00 ms                                                | 6.97 ms: 1.00x faster                                            |
| python_startup         | 12.7 ms                                                | 12.6 ms: 1.00x faster                                            |
| Geometric mean         | (ref)                                                  | 1.00x faster                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241204-linux-x86_64-iritkatriel-cmq_mdboom-3.14.0a0-6cacd2b |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| genshi_xml     | 50.5 ms                                                | 49.3 ms: 1.02x faster                                            |
| genshi_text    | 22.6 ms                                                | 22.4 ms: 1.01x faster                                            |
| mako           | 10.7 ms                                                | 11.1 ms: 1.04x slower                                            |
| Geometric mean | (ref)                                                  | 1.00x slower                                                     |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241204-linux-x86_64-iritkatriel-cmq_mdboom-3.14.0a0-6cacd2b |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| deepcopy                   | 354 us                                                 | 261 us: 1.36x faster                                             |
| deepcopy_memo              | 38.4 us                                                | 29.4 us: 1.31x faster                                            |
| go                         | 141 ms                                                 | 117 ms: 1.20x faster                                             |
| async_tree_memoization_tg  | 463 ms                                                 | 388 ms: 1.19x faster                                             |
| deepcopy_reduce            | 3.24 us                                                | 2.74 us: 1.18x faster                                            |
| gc_traversal               | 4.90 ms                                                | 4.45 ms: 1.10x faster                                            |
| regex_v8                   | 26.9 ms                                                | 24.7 ms: 1.09x faster                                            |
| pathlib                    | 17.4 ms                                                | 16.0 ms: 1.08x faster                                            |
| json                       | 5.32 ms                                                | 4.96 ms: 1.07x faster                                            |
| async_tree_none            | 350 ms                                                 | 328 ms: 1.07x faster                                             |
| pycparser                  | 1.20 sec                                               | 1.12 sec: 1.07x faster                                           |
| thrift                     | 800 us                                                 | 765 us: 1.05x faster                                             |
| float                      | 78.7 ms                                                | 75.3 ms: 1.04x faster                                            |
| 2to3                       | 266 ms                                                 | 255 ms: 1.04x faster                                             |
| regex_effbot               | 3.77 ms                                                | 3.62 ms: 1.04x faster                                            |
| telco                      | 8.40 ms                                                | 8.06 ms: 1.04x faster                                            |
| async_tree_none_tg         | 319 ms                                                 | 307 ms: 1.04x faster                                             |
| sqlalchemy_declarative     | 133 ms                                                 | 128 ms: 1.04x faster                                             |
| richards                   | 47.5 ms                                                | 45.8 ms: 1.04x faster                                            |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.85 ms: 1.04x faster                                            |
| richards_super             | 53.7 ms                                                | 51.8 ms: 1.04x faster                                            |
| crypto_pyaes               | 74.7 ms                                                | 72.0 ms: 1.04x faster                                            |
| connected_components       | 447 ms                                                 | 432 ms: 1.04x faster                                             |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 554 ms: 1.03x faster                                             |
| sqlite_synth               | 2.90 us                                                | 2.81 us: 1.03x faster                                            |
| shortest_path              | 487 ms                                                 | 471 ms: 1.03x faster                                             |
| sympy_str                  | 273 ms                                                 | 265 ms: 1.03x faster                                             |
| sympy_sum                  | 150 ms                                                 | 146 ms: 1.03x faster                                             |
| regex_compile              | 132 ms                                                 | 128 ms: 1.03x faster                                             |
| xml_etree_process          | 60.5 ms                                                | 59.0 ms: 1.02x faster                                            |
| scimark_fft                | 367 ms                                                 | 358 ms: 1.02x faster                                             |
| genshi_xml                 | 50.5 ms                                                | 49.3 ms: 1.02x faster                                            |
| html5lib                   | 63.4 ms                                                | 62.0 ms: 1.02x faster                                            |
| scimark_lu                 | 114 ms                                                 | 112 ms: 1.02x faster                                             |
| meteor_contest             | 108 ms                                                 | 106 ms: 1.02x faster                                             |
| tomli_loads                | 2.12 sec                                               | 2.08 sec: 1.02x faster                                           |
| chaos                      | 58.0 ms                                                | 57.0 ms: 1.02x faster                                            |
| nqueens                    | 80.9 ms                                                | 79.7 ms: 1.02x faster                                            |
| sqlglot_normalize          | 108 ms                                                 | 106 ms: 1.01x faster                                             |
| xml_etree_generate         | 86.8 ms                                                | 85.7 ms: 1.01x faster                                            |
| generators                 | 28.8 ms                                                | 28.4 ms: 1.01x faster                                            |
| subparsers                 | 15.5 ms                                                | 15.3 ms: 1.01x faster                                            |
| typing_runtime_protocols   | 160 us                                                 | 159 us: 1.01x faster                                             |
| pprint_safe_repr           | 727 ms                                                 | 720 ms: 1.01x faster                                             |
| genshi_text                | 22.6 ms                                                | 22.4 ms: 1.01x faster                                            |
| sympy_expand               | 456 ms                                                 | 453 ms: 1.01x faster                                             |
| pprint_pformat             | 1.48 sec                                               | 1.47 sec: 1.01x faster                                           |
| tornado_http               | 91.2 ms                                                | 90.7 ms: 1.01x faster                                            |
| python_startup_no_site     | 7.00 ms                                                | 6.97 ms: 1.00x faster                                            |
| sympy_integrate            | 19.8 ms                                                | 19.8 ms: 1.00x faster                                            |
| python_startup             | 12.7 ms                                                | 12.6 ms: 1.00x faster                                            |
| sqlglot_optimize           | 53.4 ms                                                | 53.5 ms: 1.00x slower                                            |
| json_loads                 | 27.2 us                                                | 27.3 us: 1.00x slower                                            |
| pidigits                   | 186 ms                                                 | 187 ms: 1.00x slower                                             |
| unpickle_pure_python       | 213 us                                                 | 214 us: 1.01x slower                                             |
| many_optionals             | 857 us                                                 | 863 us: 1.01x slower                                             |
| pickle_pure_python         | 302 us                                                 | 305 us: 1.01x slower                                             |
| pyflate                    | 470 ms                                                 | 474 ms: 1.01x slower                                             |
| asyncio_websockets         | 551 ms                                                 | 557 ms: 1.01x slower                                             |
| sqlglot_parse              | 1.26 ms                                                | 1.28 ms: 1.01x slower                                            |
| scimark_monte_carlo        | 66.8 ms                                                | 67.7 ms: 1.01x slower                                            |
| json_dumps                 | 10.1 ms                                                | 10.3 ms: 1.01x slower                                            |
| async_generators           | 433 ms                                                 | 439 ms: 1.01x slower                                             |
| coverage                   | 82.8 ms                                                | 84.1 ms: 1.02x slower                                            |
| hexiom                     | 6.08 ms                                                | 6.18 ms: 1.02x slower                                            |
| nbody                      | 87.7 ms                                                | 89.4 ms: 1.02x slower                                            |
| docutils                   | 2.58 sec                                               | 2.65 sec: 1.03x slower                                           |
| scimark_sor                | 122 ms                                                 | 126 ms: 1.03x slower                                             |
| async_tree_io_tg           | 861 ms                                                 | 885 ms: 1.03x slower                                             |
| xml_etree_parse            | 154 ms                                                 | 159 ms: 1.03x slower                                             |
| xml_etree_iterparse        | 101 ms                                                 | 105 ms: 1.03x slower                                             |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 562 ms: 1.03x slower                                             |
| mako                       | 10.7 ms                                                | 11.1 ms: 1.04x slower                                            |
| fannkuch                   | 394 ms                                                 | 410 ms: 1.04x slower                                             |
| bpe_tokeniser              | 4.69 sec                                               | 4.91 sec: 1.05x slower                                           |
| bench_thread_pool          | 818 us                                                 | 860 us: 1.05x slower                                             |
| coroutines                 | 22.2 ms                                                | 23.4 ms: 1.05x slower                                            |
| mdp                        | 2.54 sec                                               | 2.70 sec: 1.06x slower                                           |
| async_tree_io              | 838 ms                                                 | 891 ms: 1.06x slower                                             |
| create_gc_cycles           | 2.45 ms                                                | 2.61 ms: 1.06x slower                                            |
| k_core                     | 2.37 sec                                               | 3.48 sec: 1.47x slower                                           |
| bench_mp_pool              | 24.0 ms                                                | 77.9 ms: 3.25x slower                                            |
| Geometric mean             | (ref)                                                  | 1.00x faster                                                     |

Benchmark hidden because not significant (15): async_tree_memoization, djangocms, spectral_norm, deltablue, regex_dna, dulwich_log, comprehensions, django_template, sqlglot_transpile, sqlalchemy_imperative, logging_simple, logging_format, logging_silent, sphinx, pylint
Ignored benchmarks (4) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, gevent_hub, gunicorn, raytrace

- Geometric mean (including insignificant results): 1.014x faster

# HPT report

- Reliability score: 97.90% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.02x
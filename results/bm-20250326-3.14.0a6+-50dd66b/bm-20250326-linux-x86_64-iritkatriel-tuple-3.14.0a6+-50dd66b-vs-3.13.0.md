# Results vs. 3.13.0

- fork: iritkatriel
- ref: tuple
- machine: linux-x86_64
- commit hash: 50dd66b
- commit date: 2025-03-26
- overall geometric mean: 1.049x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.03x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250326-linux-x86_64-iritkatriel-tuple-3.14.0a6+-50dd66b |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 256 ms: 1.04x faster                                         |
| html5lib       | 63.4 ms                                                | 62.3 ms: 1.02x faster                                        |
| sphinx         | 1.03 sec                                               | 1.01 sec: 1.03x faster                                       |
| Geometric mean | (ref)                                                  | 1.02x faster                                                 |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250326-linux-x86_64-iritkatriel-tuple-3.14.0a6+-50dd66b |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 306 ms: 1.51x faster                                         |
| async_tree_memoization     | 437 ms                                                 | 310 ms: 1.41x faster                                         |
| async_tree_io_tg           | 861 ms                                                 | 614 ms: 1.40x faster                                         |
| async_tree_io              | 838 ms                                                 | 607 ms: 1.38x faster                                         |
| async_tree_none            | 350 ms                                                 | 256 ms: 1.37x faster                                         |
| async_tree_none_tg         | 319 ms                                                 | 247 ms: 1.30x faster                                         |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 489 ms: 1.17x faster                                         |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 469 ms: 1.16x faster                                         |
| async_generators           | 433 ms                                                 | 391 ms: 1.11x faster                                         |
| coroutines                 | 22.2 ms                                                | 23.7 ms: 1.07x slower                                        |
| Geometric mean             | (ref)                                                  | 1.24x faster                                                 |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250326-linux-x86_64-iritkatriel-tuple-3.14.0a6+-50dd66b |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| float          | 78.7 ms                                                | 69.5 ms: 1.13x faster                                        |
| pidigits       | 186 ms                                                 | 186 ms: 1.00x faster                                         |
| nbody          | 87.7 ms                                                | 93.8 ms: 1.07x slower                                        |
| Geometric mean | (ref)                                                  | 1.02x faster                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250326-linux-x86_64-iritkatriel-tuple-3.14.0a6+-50dd66b |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                | 3.09 ms: 1.22x faster                                        |
| regex_v8       | 26.9 ms                                                | 23.0 ms: 1.17x faster                                        |
| regex_compile  | 132 ms                                                 | 126 ms: 1.05x faster                                         |
| regex_dna      | 220 ms                                                 | 211 ms: 1.04x faster                                         |
| Geometric mean | (ref)                                                  | 1.12x faster                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250326-linux-x86_64-iritkatriel-tuple-3.14.0a6+-50dd66b |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| tomli_loads          | 2.12 sec                                               | 1.94 sec: 1.09x faster                                       |
| xml_etree_parse      | 154 ms                                                 | 142 ms: 1.09x faster                                         |
| xml_etree_iterparse  | 101 ms                                                 | 98.5 ms: 1.03x faster                                        |
| xml_etree_generate   | 86.8 ms                                                | 84.5 ms: 1.03x faster                                        |
| xml_etree_process    | 60.5 ms                                                | 58.9 ms: 1.03x faster                                        |
| unpickle_pure_python | 213 us                                                 | 219 us: 1.03x slower                                         |
| pickle_pure_python   | 302 us                                                 | 319 us: 1.05x slower                                         |
| json_loads           | 27.2 us                                                | 30.5 us: 1.12x slower                                        |
| json_dumps           | 10.1 ms                                                | 11.6 ms: 1.15x slower                                        |
| Geometric mean       | (ref)                                                  | 1.01x slower                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250326-linux-x86_64-iritkatriel-tuple-3.14.0a6+-50dd66b |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup         | 12.7 ms                                                | 13.0 ms: 1.03x slower                                        |
| python_startup_no_site | 7.00 ms                                                | 8.17 ms: 1.17x slower                                        |
| Geometric mean         | (ref)                                                  | 1.10x slower                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250326-linux-x86_64-iritkatriel-tuple-3.14.0a6+-50dd66b |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| genshi_text     | 22.6 ms                                                | 21.7 ms: 1.04x faster                                        |
| genshi_xml      | 50.5 ms                                                | 49.1 ms: 1.03x faster                                        |
| django_template | 31.7 ms                                                | 32.0 ms: 1.01x slower                                        |
| mako            | 10.7 ms                                                | 11.3 ms: 1.06x slower                                        |
| Geometric mean  | (ref)                                                  | 1.00x faster                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250326-linux-x86_64-iritkatriel-tuple-3.14.0a6+-50dd66b |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 306 ms: 1.51x faster                                         |
| async_tree_memoization     | 437 ms                                                 | 310 ms: 1.41x faster                                         |
| async_tree_io_tg           | 861 ms                                                 | 614 ms: 1.40x faster                                         |
| deepcopy                   | 354 us                                                 | 257 us: 1.38x faster                                         |
| async_tree_io              | 838 ms                                                 | 607 ms: 1.38x faster                                         |
| async_tree_none            | 350 ms                                                 | 256 ms: 1.37x faster                                         |
| deepcopy_memo              | 38.4 us                                                | 29.4 us: 1.30x faster                                        |
| async_tree_none_tg         | 319 ms                                                 | 247 ms: 1.30x faster                                         |
| go                         | 141 ms                                                 | 114 ms: 1.23x faster                                         |
| regex_effbot               | 3.77 ms                                                | 3.09 ms: 1.22x faster                                        |
| deepcopy_reduce            | 3.24 us                                                | 2.72 us: 1.19x faster                                        |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 489 ms: 1.17x faster                                         |
| regex_v8                   | 26.9 ms                                                | 23.0 ms: 1.17x faster                                        |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 469 ms: 1.16x faster                                         |
| spectral_norm              | 113 ms                                                 | 97.8 ms: 1.16x faster                                        |
| pylint                     | 312 ms                                                 | 275 ms: 1.13x faster                                         |
| float                      | 78.7 ms                                                | 69.5 ms: 1.13x faster                                        |
| dulwich_log                | 64.6 ms                                                | 57.9 ms: 1.12x faster                                        |
| async_generators           | 433 ms                                                 | 391 ms: 1.11x faster                                         |
| richards                   | 47.5 ms                                                | 43.3 ms: 1.10x faster                                        |
| tomli_loads                | 2.12 sec                                               | 1.94 sec: 1.09x faster                                       |
| xml_etree_parse            | 154 ms                                                 | 142 ms: 1.09x faster                                         |
| richards_super             | 53.7 ms                                                | 49.4 ms: 1.09x faster                                        |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.65 ms: 1.08x faster                                        |
| logging_silent             | 101 ns                                                 | 94.2 ns: 1.07x faster                                        |
| pycparser                  | 1.20 sec                                               | 1.12 sec: 1.07x faster                                       |
| scimark_fft                | 367 ms                                                 | 348 ms: 1.05x faster                                         |
| pathlib                    | 17.4 ms                                                | 16.5 ms: 1.05x faster                                        |
| pyflate                    | 470 ms                                                 | 445 ms: 1.05x faster                                         |
| telco                      | 8.40 ms                                                | 7.98 ms: 1.05x faster                                        |
| gc_traversal               | 4.90 ms                                                | 4.65 ms: 1.05x faster                                        |
| sqlite_synth               | 2.90 us                                                | 2.76 us: 1.05x faster                                        |
| regex_compile              | 132 ms                                                 | 126 ms: 1.05x faster                                         |
| regex_dna                  | 220 ms                                                 | 211 ms: 1.04x faster                                         |
| genshi_text                | 22.6 ms                                                | 21.7 ms: 1.04x faster                                        |
| thrift                     | 800 us                                                 | 768 us: 1.04x faster                                         |
| 2to3                       | 266 ms                                                 | 256 ms: 1.04x faster                                         |
| scimark_sor                | 122 ms                                                 | 118 ms: 1.04x faster                                         |
| k_core                     | 2.37 sec                                               | 2.28 sec: 1.04x faster                                       |
| logging_format             | 6.23 us                                                | 6.05 us: 1.03x faster                                        |
| genshi_xml                 | 50.5 ms                                                | 49.1 ms: 1.03x faster                                        |
| xml_etree_iterparse        | 101 ms                                                 | 98.5 ms: 1.03x faster                                        |
| xml_etree_generate         | 86.8 ms                                                | 84.5 ms: 1.03x faster                                        |
| xml_etree_process          | 60.5 ms                                                | 58.9 ms: 1.03x faster                                        |
| sphinx                     | 1.03 sec                                               | 1.01 sec: 1.03x faster                                       |
| sympy_str                  | 273 ms                                                 | 266 ms: 1.03x faster                                         |
| sympy_integrate            | 19.8 ms                                                | 19.3 ms: 1.03x faster                                        |
| sqlalchemy_declarative     | 133 ms                                                 | 130 ms: 1.02x faster                                         |
| sympy_sum                  | 150 ms                                                 | 147 ms: 1.02x faster                                         |
| logging_simple             | 5.65 us                                                | 5.53 us: 1.02x faster                                        |
| generators                 | 28.8 ms                                                | 28.2 ms: 1.02x faster                                        |
| deltablue                  | 3.19 ms                                                | 3.13 ms: 1.02x faster                                        |
| bpe_tokeniser              | 4.69 sec                                               | 4.60 sec: 1.02x faster                                       |
| sqlalchemy_imperative      | 16.9 ms                                                | 16.6 ms: 1.02x faster                                        |
| mdp                        | 2.54 sec                                               | 2.50 sec: 1.02x faster                                       |
| html5lib                   | 63.4 ms                                                | 62.3 ms: 1.02x faster                                        |
| meteor_contest             | 108 ms                                                 | 107 ms: 1.02x faster                                         |
| crypto_pyaes               | 74.7 ms                                                | 73.9 ms: 1.01x faster                                        |
| pidigits                   | 186 ms                                                 | 186 ms: 1.00x faster                                         |
| pprint_safe_repr           | 727 ms                                                 | 730 ms: 1.00x slower                                         |
| raytrace                   | 262 ms                                                 | 263 ms: 1.00x slower                                         |
| nqueens                    | 80.9 ms                                                | 81.3 ms: 1.01x slower                                        |
| comprehensions             | 16.5 us                                                | 16.6 us: 1.01x slower                                        |
| create_gc_cycles           | 2.45 ms                                                | 2.47 ms: 1.01x slower                                        |
| scimark_monte_carlo        | 66.8 ms                                                | 67.5 ms: 1.01x slower                                        |
| django_template            | 31.7 ms                                                | 32.0 ms: 1.01x slower                                        |
| connected_components       | 447 ms                                                 | 452 ms: 1.01x slower                                         |
| scimark_lu                 | 114 ms                                                 | 116 ms: 1.01x slower                                         |
| shortest_path              | 487 ms                                                 | 494 ms: 1.01x slower                                         |
| hexiom                     | 6.08 ms                                                | 6.19 ms: 1.02x slower                                        |
| unpickle_pure_python       | 213 us                                                 | 219 us: 1.03x slower                                         |
| python_startup             | 12.7 ms                                                | 13.0 ms: 1.03x slower                                        |
| pickle_pure_python         | 302 us                                                 | 319 us: 1.05x slower                                         |
| mako                       | 10.7 ms                                                | 11.3 ms: 1.06x slower                                        |
| bench_thread_pool          | 818 us                                                 | 871 us: 1.06x slower                                         |
| fannkuch                   | 394 ms                                                 | 420 ms: 1.07x slower                                         |
| coroutines                 | 22.2 ms                                                | 23.7 ms: 1.07x slower                                        |
| nbody                      | 87.7 ms                                                | 93.8 ms: 1.07x slower                                        |
| coverage                   | 82.8 ms                                                | 91.7 ms: 1.11x slower                                        |
| many_optionals             | 857 us                                                 | 951 us: 1.11x slower                                         |
| json_loads                 | 27.2 us                                                | 30.5 us: 1.12x slower                                        |
| json_dumps                 | 10.1 ms                                                | 11.6 ms: 1.15x slower                                        |
| python_startup_no_site     | 7.00 ms                                                | 8.17 ms: 1.17x slower                                        |
| subparsers                 | 15.5 ms                                                | 20.9 ms: 1.35x slower                                        |
| bench_mp_pool              | 24.0 ms                                                | 82.8 ms: 3.45x slower                                        |
| Geometric mean             | (ref)                                                  | 1.03x faster                                                 |

Benchmark hidden because not significant (7): json, typing_runtime_protocols, docutils, asyncio_websockets, pprint_pformat, chaos, sympy_expand
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250326-3.14.0a6+-50dd66b/bm-20250326-linux-x86_64-iritkatriel-tuple-3.14.0a6+-50dd66b.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.049x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.03x
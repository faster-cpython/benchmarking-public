# Results vs. 3.13.0

- fork: iritkatriel
- ref: tuple
- machine: linux-x86_64
- commit hash: 2d69c9f
- commit date: 2025-03-25
- overall geometric mean: 1.044x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.03x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250325-linux-x86_64-iritkatriel-tuple-3.14.0a6+-2d69c9f |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 256 ms: 1.04x faster                                         |
| docutils       | 2.58 sec                                               | 2.59 sec: 1.00x slower                                       |
| html5lib       | 63.4 ms                                                | 62.5 ms: 1.01x faster                                        |
| sphinx         | 1.03 sec                                               | 1.00 sec: 1.03x faster                                       |
| Geometric mean | (ref)                                                  | 1.02x faster                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250325-linux-x86_64-iritkatriel-tuple-3.14.0a6+-2d69c9f |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 316 ms: 1.46x faster                                         |
| async_tree_io_tg           | 861 ms                                                 | 620 ms: 1.39x faster                                         |
| async_tree_memoization     | 437 ms                                                 | 318 ms: 1.37x faster                                         |
| async_tree_io              | 838 ms                                                 | 619 ms: 1.35x faster                                         |
| async_tree_none            | 350 ms                                                 | 259 ms: 1.35x faster                                         |
| async_tree_none_tg         | 319 ms                                                 | 250 ms: 1.28x faster                                         |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 493 ms: 1.16x faster                                         |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 473 ms: 1.15x faster                                         |
| async_generators           | 433 ms                                                 | 396 ms: 1.09x faster                                         |
| coroutines                 | 22.2 ms                                                | 23.3 ms: 1.05x slower                                        |
| Geometric mean             | (ref)                                                  | 1.22x faster                                                 |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250325-linux-x86_64-iritkatriel-tuple-3.14.0a6+-2d69c9f |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| float          | 78.7 ms                                                | 69.9 ms: 1.13x faster                                        |
| pidigits       | 186 ms                                                 | 186 ms: 1.00x faster                                         |
| nbody          | 87.7 ms                                                | 96.4 ms: 1.10x slower                                        |
| Geometric mean | (ref)                                                  | 1.01x faster                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250325-linux-x86_64-iritkatriel-tuple-3.14.0a6+-2d69c9f |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                | 3.19 ms: 1.18x faster                                        |
| regex_v8       | 26.9 ms                                                | 22.9 ms: 1.17x faster                                        |
| regex_compile  | 132 ms                                                 | 126 ms: 1.05x faster                                         |
| regex_dna      | 220 ms                                                 | 217 ms: 1.01x faster                                         |
| Geometric mean | (ref)                                                  | 1.10x faster                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250325-linux-x86_64-iritkatriel-tuple-3.14.0a6+-2d69c9f |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| xml_etree_parse      | 154 ms                                                 | 141 ms: 1.09x faster                                         |
| tomli_loads          | 2.12 sec                                               | 1.97 sec: 1.07x faster                                       |
| xml_etree_generate   | 86.8 ms                                                | 83.6 ms: 1.04x faster                                        |
| xml_etree_process    | 60.5 ms                                                | 58.4 ms: 1.04x faster                                        |
| xml_etree_iterparse  | 101 ms                                                 | 98.3 ms: 1.03x faster                                        |
| unpickle_pure_python | 213 us                                                 | 220 us: 1.03x slower                                         |
| pickle_pure_python   | 302 us                                                 | 316 us: 1.05x slower                                         |
| json_loads           | 27.2 us                                                | 29.8 us: 1.10x slower                                        |
| json_dumps           | 10.1 ms                                                | 11.4 ms: 1.13x slower                                        |
| Geometric mean       | (ref)                                                  | 1.00x slower                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250325-linux-x86_64-iritkatriel-tuple-3.14.0a6+-2d69c9f |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup         | 12.7 ms                                                | 13.1 ms: 1.03x slower                                        |
| python_startup_no_site | 7.00 ms                                                | 8.17 ms: 1.17x slower                                        |
| Geometric mean         | (ref)                                                  | 1.10x slower                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250325-linux-x86_64-iritkatriel-tuple-3.14.0a6+-2d69c9f |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| genshi_text    | 22.6 ms                                                | 21.4 ms: 1.06x faster                                        |
| genshi_xml     | 50.5 ms                                                | 49.3 ms: 1.02x faster                                        |
| mako           | 10.7 ms                                                | 11.1 ms: 1.04x slower                                        |
| Geometric mean | (ref)                                                  | 1.01x faster                                                 |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250325-linux-x86_64-iritkatriel-tuple-3.14.0a6+-2d69c9f |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 316 ms: 1.46x faster                                         |
| async_tree_io_tg           | 861 ms                                                 | 620 ms: 1.39x faster                                         |
| deepcopy                   | 354 us                                                 | 257 us: 1.38x faster                                         |
| async_tree_memoization     | 437 ms                                                 | 318 ms: 1.37x faster                                         |
| async_tree_io              | 838 ms                                                 | 619 ms: 1.35x faster                                         |
| async_tree_none            | 350 ms                                                 | 259 ms: 1.35x faster                                         |
| deepcopy_memo              | 38.4 us                                                | 29.0 us: 1.33x faster                                        |
| async_tree_none_tg         | 319 ms                                                 | 250 ms: 1.28x faster                                         |
| go                         | 141 ms                                                 | 115 ms: 1.22x faster                                         |
| deepcopy_reduce            | 3.24 us                                                | 2.70 us: 1.20x faster                                        |
| regex_effbot               | 3.77 ms                                                | 3.19 ms: 1.18x faster                                        |
| regex_v8                   | 26.9 ms                                                | 22.9 ms: 1.17x faster                                        |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 493 ms: 1.16x faster                                         |
| spectral_norm              | 113 ms                                                 | 98.4 ms: 1.15x faster                                        |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 473 ms: 1.15x faster                                         |
| pylint                     | 312 ms                                                 | 277 ms: 1.13x faster                                         |
| float                      | 78.7 ms                                                | 69.9 ms: 1.13x faster                                        |
| dulwich_log                | 64.6 ms                                                | 58.4 ms: 1.11x faster                                        |
| richards                   | 47.5 ms                                                | 43.2 ms: 1.10x faster                                        |
| async_generators           | 433 ms                                                 | 396 ms: 1.09x faster                                         |
| xml_etree_parse            | 154 ms                                                 | 141 ms: 1.09x faster                                         |
| richards_super             | 53.7 ms                                                | 49.5 ms: 1.08x faster                                        |
| tomli_loads                | 2.12 sec                                               | 1.97 sec: 1.07x faster                                       |
| pycparser                  | 1.20 sec                                               | 1.12 sec: 1.07x faster                                       |
| scimark_fft                | 367 ms                                                 | 344 ms: 1.06x faster                                         |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.74 ms: 1.06x faster                                        |
| genshi_text                | 22.6 ms                                                | 21.4 ms: 1.06x faster                                        |
| scimark_sor                | 122 ms                                                 | 116 ms: 1.05x faster                                         |
| telco                      | 8.40 ms                                                | 8.01 ms: 1.05x faster                                        |
| regex_compile              | 132 ms                                                 | 126 ms: 1.05x faster                                         |
| sqlite_synth               | 2.90 us                                                | 2.78 us: 1.04x faster                                        |
| pyflate                    | 470 ms                                                 | 450 ms: 1.04x faster                                         |
| xml_etree_generate         | 86.8 ms                                                | 83.6 ms: 1.04x faster                                        |
| 2to3                       | 266 ms                                                 | 256 ms: 1.04x faster                                         |
| k_core                     | 2.37 sec                                               | 2.28 sec: 1.04x faster                                       |
| xml_etree_process          | 60.5 ms                                                | 58.4 ms: 1.04x faster                                        |
| deltablue                  | 3.19 ms                                                | 3.09 ms: 1.03x faster                                        |
| thrift                     | 800 us                                                 | 775 us: 1.03x faster                                         |
| xml_etree_iterparse        | 101 ms                                                 | 98.3 ms: 1.03x faster                                        |
| sqlalchemy_imperative      | 16.9 ms                                                | 16.4 ms: 1.03x faster                                        |
| sphinx                     | 1.03 sec                                               | 1.00 sec: 1.03x faster                                       |
| logging_simple             | 5.65 us                                                | 5.52 us: 1.02x faster                                        |
| logging_silent             | 101 ns                                                 | 98.6 ns: 1.02x faster                                        |
| genshi_xml                 | 50.5 ms                                                | 49.3 ms: 1.02x faster                                        |
| mdp                        | 2.54 sec                                               | 2.49 sec: 1.02x faster                                       |
| sympy_str                  | 273 ms                                                 | 267 ms: 1.02x faster                                         |
| pathlib                    | 17.4 ms                                                | 17.0 ms: 1.02x faster                                        |
| sqlalchemy_declarative     | 133 ms                                                 | 130 ms: 1.02x faster                                         |
| sympy_sum                  | 150 ms                                                 | 148 ms: 1.02x faster                                         |
| meteor_contest             | 108 ms                                                 | 107 ms: 1.01x faster                                         |
| html5lib                   | 63.4 ms                                                | 62.5 ms: 1.01x faster                                        |
| regex_dna                  | 220 ms                                                 | 217 ms: 1.01x faster                                         |
| bpe_tokeniser              | 4.69 sec                                               | 4.64 sec: 1.01x faster                                       |
| logging_format             | 6.23 us                                                | 6.16 us: 1.01x faster                                        |
| json                       | 5.32 ms                                                | 5.27 ms: 1.01x faster                                        |
| pprint_safe_repr           | 727 ms                                                 | 724 ms: 1.00x faster                                         |
| sympy_expand               | 456 ms                                                 | 455 ms: 1.00x faster                                         |
| pidigits                   | 186 ms                                                 | 186 ms: 1.00x faster                                         |
| docutils                   | 2.58 sec                                               | 2.59 sec: 1.00x slower                                       |
| sympy_integrate            | 19.8 ms                                                | 19.9 ms: 1.00x slower                                        |
| scimark_lu                 | 114 ms                                                 | 115 ms: 1.01x slower                                         |
| create_gc_cycles           | 2.45 ms                                                | 2.47 ms: 1.01x slower                                        |
| raytrace                   | 262 ms                                                 | 264 ms: 1.01x slower                                         |
| shortest_path              | 487 ms                                                 | 492 ms: 1.01x slower                                         |
| connected_components       | 447 ms                                                 | 453 ms: 1.01x slower                                         |
| crypto_pyaes               | 74.7 ms                                                | 76.1 ms: 1.02x slower                                        |
| comprehensions             | 16.5 us                                                | 16.8 us: 1.02x slower                                        |
| chaos                      | 58.0 ms                                                | 59.3 ms: 1.02x slower                                        |
| typing_runtime_protocols   | 160 us                                                 | 164 us: 1.02x slower                                         |
| nqueens                    | 80.9 ms                                                | 82.7 ms: 1.02x slower                                        |
| gc_traversal               | 4.90 ms                                                | 5.02 ms: 1.03x slower                                        |
| unpickle_pure_python       | 213 us                                                 | 220 us: 1.03x slower                                         |
| scimark_monte_carlo        | 66.8 ms                                                | 68.9 ms: 1.03x slower                                        |
| hexiom                     | 6.08 ms                                                | 6.28 ms: 1.03x slower                                        |
| python_startup             | 12.7 ms                                                | 13.1 ms: 1.03x slower                                        |
| mako                       | 10.7 ms                                                | 11.1 ms: 1.04x slower                                        |
| pickle_pure_python         | 302 us                                                 | 316 us: 1.05x slower                                         |
| coroutines                 | 22.2 ms                                                | 23.3 ms: 1.05x slower                                        |
| bench_thread_pool          | 818 us                                                 | 872 us: 1.07x slower                                         |
| fannkuch                   | 394 ms                                                 | 431 ms: 1.09x slower                                         |
| json_loads                 | 27.2 us                                                | 29.8 us: 1.10x slower                                        |
| nbody                      | 87.7 ms                                                | 96.4 ms: 1.10x slower                                        |
| coverage                   | 82.8 ms                                                | 91.4 ms: 1.10x slower                                        |
| many_optionals             | 857 us                                                 | 946 us: 1.10x slower                                         |
| json_dumps                 | 10.1 ms                                                | 11.4 ms: 1.13x slower                                        |
| python_startup_no_site     | 7.00 ms                                                | 8.17 ms: 1.17x slower                                        |
| subparsers                 | 15.5 ms                                                | 20.6 ms: 1.33x slower                                        |
| bench_mp_pool              | 24.0 ms                                                | 82.9 ms: 3.46x slower                                        |
| Geometric mean             | (ref)                                                  | 1.03x faster                                                 |

Benchmark hidden because not significant (4): generators, pprint_pformat, asyncio_websockets, django_template
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250325-3.14.0a6+-2d69c9f/bm-20250325-linux-x86_64-iritkatriel-tuple-3.14.0a6+-2d69c9f.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.044x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.03x
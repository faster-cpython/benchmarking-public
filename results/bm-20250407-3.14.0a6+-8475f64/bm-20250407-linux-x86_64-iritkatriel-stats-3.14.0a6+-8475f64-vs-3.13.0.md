# Results vs. 3.13.0

- fork: iritkatriel
- ref: stats
- machine: linux-x86_64
- commit hash: 8475f64
- commit date: 2025-04-07
- overall geometric mean: 1.067x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.03x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250407-linux-x86_64-iritkatriel-stats-3.14.0a6+-8475f64 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 250 ms: 1.06x faster                                         |
| docutils       | 2.58 sec                                               | 2.57 sec: 1.00x faster                                       |
| html5lib       | 63.4 ms                                                | 60.4 ms: 1.05x faster                                        |
| sphinx         | 1.03 sec                                               | 1.01 sec: 1.02x faster                                       |
| Geometric mean | (ref)                                                  | 1.03x faster                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250407-linux-x86_64-iritkatriel-stats-3.14.0a6+-8475f64 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 312 ms: 1.49x faster                                         |
| async_tree_memoization     | 437 ms                                                 | 307 ms: 1.42x faster                                         |
| async_tree_io_tg           | 861 ms                                                 | 609 ms: 1.41x faster                                         |
| async_tree_io              | 838 ms                                                 | 608 ms: 1.38x faster                                         |
| async_tree_none            | 350 ms                                                 | 255 ms: 1.38x faster                                         |
| async_tree_none_tg         | 319 ms                                                 | 245 ms: 1.31x faster                                         |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 476 ms: 1.20x faster                                         |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 474 ms: 1.15x faster                                         |
| async_generators           | 433 ms                                                 | 390 ms: 1.11x faster                                         |
| coroutines                 | 22.2 ms                                                | 22.9 ms: 1.03x slower                                        |
| Geometric mean             | (ref)                                                  | 1.24x faster                                                 |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250407-linux-x86_64-iritkatriel-stats-3.14.0a6+-8475f64 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| float          | 78.7 ms                                                | 66.3 ms: 1.19x faster                                        |
| nbody          | 87.7 ms                                                | 86.4 ms: 1.01x faster                                        |
| pidigits       | 186 ms                                                 | 186 ms: 1.00x faster                                         |
| Geometric mean | (ref)                                                  | 1.06x faster                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250407-linux-x86_64-iritkatriel-stats-3.14.0a6+-8475f64 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| regex_v8       | 26.9 ms                                                | 22.5 ms: 1.19x faster                                        |
| regex_effbot   | 3.77 ms                                                | 3.45 ms: 1.09x faster                                        |
| regex_compile  | 132 ms                                                 | 124 ms: 1.06x faster                                         |
| regex_dna      | 220 ms                                                 | 217 ms: 1.01x faster                                         |
| Geometric mean | (ref)                                                  | 1.09x faster                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250407-linux-x86_64-iritkatriel-stats-3.14.0a6+-8475f64 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| tomli_loads          | 2.12 sec                                               | 1.92 sec: 1.10x faster                                       |
| xml_etree_parse      | 154 ms                                                 | 141 ms: 1.10x faster                                         |
| xml_etree_generate   | 86.8 ms                                                | 83.8 ms: 1.04x faster                                        |
| xml_etree_process    | 60.5 ms                                                | 58.6 ms: 1.03x faster                                        |
| xml_etree_iterparse  | 101 ms                                                 | 98.6 ms: 1.03x faster                                        |
| unpickle_pure_python | 213 us                                                 | 217 us: 1.02x slower                                         |
| pickle_pure_python   | 302 us                                                 | 313 us: 1.04x slower                                         |
| json_loads           | 27.2 us                                                | 29.9 us: 1.10x slower                                        |
| json_dumps           | 10.1 ms                                                | 11.8 ms: 1.17x slower                                        |
| Geometric mean       | (ref)                                                  | 1.00x slower                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250407-linux-x86_64-iritkatriel-stats-3.14.0a6+-8475f64 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup         | 12.7 ms                                                | 13.2 ms: 1.04x slower                                        |
| python_startup_no_site | 7.00 ms                                                | 8.21 ms: 1.17x slower                                        |
| Geometric mean         | (ref)                                                  | 1.11x slower                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250407-linux-x86_64-iritkatriel-stats-3.14.0a6+-8475f64 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| genshi_text     | 22.6 ms                                                | 20.7 ms: 1.09x faster                                        |
| genshi_xml      | 50.5 ms                                                | 48.6 ms: 1.04x faster                                        |
| django_template | 31.7 ms                                                | 31.3 ms: 1.01x faster                                        |
| mako            | 10.7 ms                                                | 11.0 ms: 1.03x slower                                        |
| Geometric mean  | (ref)                                                  | 1.03x faster                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250407-linux-x86_64-iritkatriel-stats-3.14.0a6+-8475f64 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| mdp                        | 2.54 sec                                               | 1.22 sec: 2.09x faster                                       |
| async_tree_memoization_tg  | 463 ms                                                 | 312 ms: 1.49x faster                                         |
| deepcopy                   | 354 us                                                 | 245 us: 1.45x faster                                         |
| async_tree_memoization     | 437 ms                                                 | 307 ms: 1.42x faster                                         |
| async_tree_io_tg           | 861 ms                                                 | 609 ms: 1.41x faster                                         |
| async_tree_io              | 838 ms                                                 | 608 ms: 1.38x faster                                         |
| async_tree_none            | 350 ms                                                 | 255 ms: 1.38x faster                                         |
| deepcopy_memo              | 38.4 us                                                | 28.6 us: 1.34x faster                                        |
| async_tree_none_tg         | 319 ms                                                 | 245 ms: 1.31x faster                                         |
| go                         | 141 ms                                                 | 110 ms: 1.28x faster                                         |
| deepcopy_reduce            | 3.24 us                                                | 2.57 us: 1.26x faster                                        |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 476 ms: 1.20x faster                                         |
| regex_v8                   | 26.9 ms                                                | 22.5 ms: 1.19x faster                                        |
| float                      | 78.7 ms                                                | 66.3 ms: 1.19x faster                                        |
| spectral_norm              | 113 ms                                                 | 97.0 ms: 1.17x faster                                        |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 474 ms: 1.15x faster                                         |
| pylint                     | 312 ms                                                 | 276 ms: 1.13x faster                                         |
| async_generators           | 433 ms                                                 | 390 ms: 1.11x faster                                         |
| richards                   | 47.5 ms                                                | 42.9 ms: 1.11x faster                                        |
| richards_super             | 53.7 ms                                                | 48.5 ms: 1.11x faster                                        |
| tomli_loads                | 2.12 sec                                               | 1.92 sec: 1.10x faster                                       |
| scimark_fft                | 367 ms                                                 | 332 ms: 1.10x faster                                         |
| xml_etree_parse            | 154 ms                                                 | 141 ms: 1.10x faster                                         |
| dulwich_log                | 64.6 ms                                                | 59.0 ms: 1.09x faster                                        |
| genshi_text                | 22.6 ms                                                | 20.7 ms: 1.09x faster                                        |
| regex_effbot               | 3.77 ms                                                | 3.45 ms: 1.09x faster                                        |
| telco                      | 8.40 ms                                                | 7.79 ms: 1.08x faster                                        |
| gc_traversal               | 4.90 ms                                                | 4.60 ms: 1.06x faster                                        |
| 2to3                       | 266 ms                                                 | 250 ms: 1.06x faster                                         |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.73 ms: 1.06x faster                                        |
| pathlib                    | 17.4 ms                                                | 16.3 ms: 1.06x faster                                        |
| regex_compile              | 132 ms                                                 | 124 ms: 1.06x faster                                         |
| pyflate                    | 470 ms                                                 | 446 ms: 1.05x faster                                         |
| html5lib                   | 63.4 ms                                                | 60.4 ms: 1.05x faster                                        |
| sqlite_synth               | 2.90 us                                                | 2.77 us: 1.05x faster                                        |
| pycparser                  | 1.20 sec                                               | 1.15 sec: 1.05x faster                                       |
| k_core                     | 2.37 sec                                               | 2.26 sec: 1.05x faster                                       |
| chaos                      | 58.0 ms                                                | 55.6 ms: 1.04x faster                                        |
| scimark_monte_carlo        | 66.8 ms                                                | 64.0 ms: 1.04x faster                                        |
| scimark_sor                | 122 ms                                                 | 117 ms: 1.04x faster                                         |
| sympy_integrate            | 19.8 ms                                                | 19.0 ms: 1.04x faster                                        |
| genshi_xml                 | 50.5 ms                                                | 48.6 ms: 1.04x faster                                        |
| logging_silent             | 101 ns                                                 | 97.2 ns: 1.04x faster                                        |
| crypto_pyaes               | 74.7 ms                                                | 72.0 ms: 1.04x faster                                        |
| xml_etree_generate         | 86.8 ms                                                | 83.8 ms: 1.04x faster                                        |
| bpe_tokeniser              | 4.69 sec                                               | 4.53 sec: 1.03x faster                                       |
| xml_etree_process          | 60.5 ms                                                | 58.6 ms: 1.03x faster                                        |
| raytrace                   | 262 ms                                                 | 254 ms: 1.03x faster                                         |
| logging_simple             | 5.65 us                                                | 5.48 us: 1.03x faster                                        |
| xml_etree_iterparse        | 101 ms                                                 | 98.6 ms: 1.03x faster                                        |
| logging_format             | 6.23 us                                                | 6.07 us: 1.03x faster                                        |
| meteor_contest             | 108 ms                                                 | 106 ms: 1.03x faster                                         |
| sympy_str                  | 273 ms                                                 | 267 ms: 1.02x faster                                         |
| sphinx                     | 1.03 sec                                               | 1.01 sec: 1.02x faster                                       |
| pprint_safe_repr           | 727 ms                                                 | 712 ms: 1.02x faster                                         |
| sqlalchemy_declarative     | 133 ms                                                 | 131 ms: 1.02x faster                                         |
| sqlalchemy_imperative      | 16.9 ms                                                | 16.6 ms: 1.02x faster                                        |
| pprint_pformat             | 1.48 sec                                               | 1.46 sec: 1.01x faster                                       |
| sympy_sum                  | 150 ms                                                 | 148 ms: 1.01x faster                                         |
| nbody                      | 87.7 ms                                                | 86.4 ms: 1.01x faster                                        |
| regex_dna                  | 220 ms                                                 | 217 ms: 1.01x faster                                         |
| django_template            | 31.7 ms                                                | 31.3 ms: 1.01x faster                                        |
| nqueens                    | 80.9 ms                                                | 80.4 ms: 1.01x faster                                        |
| docutils                   | 2.58 sec                                               | 2.57 sec: 1.00x faster                                       |
| pidigits                   | 186 ms                                                 | 186 ms: 1.00x faster                                         |
| create_gc_cycles           | 2.45 ms                                                | 2.47 ms: 1.01x slower                                        |
| connected_components       | 447 ms                                                 | 451 ms: 1.01x slower                                         |
| comprehensions             | 16.5 us                                                | 16.7 us: 1.01x slower                                        |
| shortest_path              | 487 ms                                                 | 494 ms: 1.02x slower                                         |
| unpickle_pure_python       | 213 us                                                 | 217 us: 1.02x slower                                         |
| scimark_lu                 | 114 ms                                                 | 116 ms: 1.02x slower                                         |
| hexiom                     | 6.08 ms                                                | 6.21 ms: 1.02x slower                                        |
| typing_runtime_protocols   | 160 us                                                 | 165 us: 1.03x slower                                         |
| coroutines                 | 22.2 ms                                                | 22.9 ms: 1.03x slower                                        |
| coverage                   | 82.8 ms                                                | 85.4 ms: 1.03x slower                                        |
| mako                       | 10.7 ms                                                | 11.0 ms: 1.03x slower                                        |
| generators                 | 28.8 ms                                                | 29.8 ms: 1.03x slower                                        |
| pickle_pure_python         | 302 us                                                 | 313 us: 1.04x slower                                         |
| fannkuch                   | 394 ms                                                 | 409 ms: 1.04x slower                                         |
| deltablue                  | 3.19 ms                                                | 3.32 ms: 1.04x slower                                        |
| python_startup             | 12.7 ms                                                | 13.2 ms: 1.04x slower                                        |
| bench_thread_pool          | 818 us                                                 | 875 us: 1.07x slower                                         |
| many_optionals             | 857 us                                                 | 925 us: 1.08x slower                                         |
| json_loads                 | 27.2 us                                                | 29.9 us: 1.10x slower                                        |
| json_dumps                 | 10.1 ms                                                | 11.8 ms: 1.17x slower                                        |
| python_startup_no_site     | 7.00 ms                                                | 8.21 ms: 1.17x slower                                        |
| subparsers                 | 15.5 ms                                                | 20.6 ms: 1.34x slower                                        |
| bench_mp_pool              | 24.0 ms                                                | 82.3 ms: 3.43x slower                                        |
| Geometric mean             | (ref)                                                  | 1.05x faster                                                 |

Benchmark hidden because not significant (3): sympy_expand, asyncio_websockets, json
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
Ignored benchmarks (4) of results/bm-20250407-3.14.0a6+-8475f64/bm-20250407-linux-x86_64-iritkatriel-stats-3.14.0a6+-8475f64.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.067x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.03x
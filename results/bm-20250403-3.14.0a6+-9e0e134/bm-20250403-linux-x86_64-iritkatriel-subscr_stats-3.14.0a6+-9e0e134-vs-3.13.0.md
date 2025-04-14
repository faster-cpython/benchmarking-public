# Results vs. 3.13.0

- fork: iritkatriel
- ref: subscr_stats
- machine: linux-x86_64
- commit hash: 9e0e134
- commit date: 2025-04-03
- overall geometric mean: 1.055x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250403-linux-x86_64-iritkatriel-subscr_stats-3.14.0a6+-9e0e134 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 254 ms: 1.05x faster                                                |
| html5lib       | 63.4 ms                                                | 62.5 ms: 1.01x faster                                               |
| Geometric mean | (ref)                                                  | 1.02x faster                                                        |

Benchmark hidden because not significant (2): docutils, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250403-linux-x86_64-iritkatriel-subscr_stats-3.14.0a6+-9e0e134 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 314 ms: 1.47x faster                                                |
| async_tree_io_tg           | 861 ms                                                 | 610 ms: 1.41x faster                                                |
| async_tree_memoization     | 437 ms                                                 | 312 ms: 1.40x faster                                                |
| async_tree_io              | 838 ms                                                 | 608 ms: 1.38x faster                                                |
| async_tree_none            | 350 ms                                                 | 260 ms: 1.35x faster                                                |
| async_tree_none_tg         | 319 ms                                                 | 249 ms: 1.28x faster                                                |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 488 ms: 1.17x faster                                                |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 476 ms: 1.14x faster                                                |
| async_generators           | 433 ms                                                 | 392 ms: 1.11x faster                                                |
| coroutines                 | 22.2 ms                                                | 23.8 ms: 1.07x slower                                               |
| Geometric mean             | (ref)                                                  | 1.23x faster                                                        |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250403-linux-x86_64-iritkatriel-subscr_stats-3.14.0a6+-9e0e134 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 69.0 ms: 1.14x faster                                               |
| pidigits       | 186 ms                                                 | 186 ms: 1.00x faster                                                |
| nbody          | 87.7 ms                                                | 97.7 ms: 1.11x slower                                               |
| Geometric mean | (ref)                                                  | 1.01x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250403-linux-x86_64-iritkatriel-subscr_stats-3.14.0a6+-9e0e134 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_v8       | 26.9 ms                                                | 22.9 ms: 1.17x faster                                               |
| regex_compile  | 132 ms                                                 | 126 ms: 1.05x faster                                                |
| regex_dna      | 220 ms                                                 | 216 ms: 1.02x faster                                                |
| regex_effbot   | 3.77 ms                                                | 3.81 ms: 1.01x slower                                               |
| Geometric mean | (ref)                                                  | 1.06x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250403-linux-x86_64-iritkatriel-subscr_stats-3.14.0a6+-9e0e134 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| xml_etree_parse      | 154 ms                                                 | 142 ms: 1.09x faster                                                |
| tomli_loads          | 2.12 sec                                               | 2.00 sec: 1.06x faster                                              |
| xml_etree_process    | 60.5 ms                                                | 58.5 ms: 1.03x faster                                               |
| xml_etree_generate   | 86.8 ms                                                | 84.2 ms: 1.03x faster                                               |
| xml_etree_iterparse  | 101 ms                                                 | 98.4 ms: 1.03x faster                                               |
| unpickle_pure_python | 213 us                                                 | 217 us: 1.02x slower                                                |
| pickle_pure_python   | 302 us                                                 | 317 us: 1.05x slower                                                |
| json_loads           | 27.2 us                                                | 29.5 us: 1.09x slower                                               |
| json_dumps           | 10.1 ms                                                | 11.6 ms: 1.14x slower                                               |
| Geometric mean       | (ref)                                                  | 1.01x slower                                                        |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250403-linux-x86_64-iritkatriel-subscr_stats-3.14.0a6+-9e0e134 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 12.7 ms                                                | 13.1 ms: 1.03x slower                                               |
| python_startup_no_site | 7.00 ms                                                | 8.19 ms: 1.17x slower                                               |
| Geometric mean         | (ref)                                                  | 1.10x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250403-linux-x86_64-iritkatriel-subscr_stats-3.14.0a6+-9e0e134 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| genshi_text     | 22.6 ms                                                | 21.5 ms: 1.05x faster                                               |
| genshi_xml      | 50.5 ms                                                | 48.8 ms: 1.03x faster                                               |
| django_template | 31.7 ms                                                | 31.4 ms: 1.01x faster                                               |
| mako            | 10.7 ms                                                | 11.3 ms: 1.06x slower                                               |
| Geometric mean  | (ref)                                                  | 1.01x faster                                                        |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250403-linux-x86_64-iritkatriel-subscr_stats-3.14.0a6+-9e0e134 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| mdp                        | 2.54 sec                                               | 1.23 sec: 2.07x faster                                              |
| async_tree_memoization_tg  | 463 ms                                                 | 314 ms: 1.47x faster                                                |
| async_tree_io_tg           | 861 ms                                                 | 610 ms: 1.41x faster                                                |
| async_tree_memoization     | 437 ms                                                 | 312 ms: 1.40x faster                                                |
| deepcopy                   | 354 us                                                 | 254 us: 1.39x faster                                                |
| async_tree_io              | 838 ms                                                 | 608 ms: 1.38x faster                                                |
| async_tree_none            | 350 ms                                                 | 260 ms: 1.35x faster                                                |
| deepcopy_memo              | 38.4 us                                                | 29.6 us: 1.30x faster                                               |
| async_tree_none_tg         | 319 ms                                                 | 249 ms: 1.28x faster                                                |
| go                         | 141 ms                                                 | 112 ms: 1.25x faster                                                |
| deepcopy_reduce            | 3.24 us                                                | 2.70 us: 1.20x faster                                               |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 488 ms: 1.17x faster                                                |
| regex_v8                   | 26.9 ms                                                | 22.9 ms: 1.17x faster                                               |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 476 ms: 1.14x faster                                                |
| float                      | 78.7 ms                                                | 69.0 ms: 1.14x faster                                               |
| spectral_norm              | 113 ms                                                 | 100.0 ms: 1.13x faster                                              |
| pylint                     | 312 ms                                                 | 276 ms: 1.13x faster                                                |
| async_generators           | 433 ms                                                 | 392 ms: 1.11x faster                                                |
| dulwich_log                | 64.6 ms                                                | 58.5 ms: 1.10x faster                                               |
| pyflate                    | 470 ms                                                 | 432 ms: 1.09x faster                                                |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.63 ms: 1.09x faster                                               |
| xml_etree_parse            | 154 ms                                                 | 142 ms: 1.09x faster                                                |
| richards                   | 47.5 ms                                                | 44.1 ms: 1.08x faster                                               |
| richards_super             | 53.7 ms                                                | 50.0 ms: 1.08x faster                                               |
| telco                      | 8.40 ms                                                | 7.89 ms: 1.06x faster                                               |
| pathlib                    | 17.4 ms                                                | 16.4 ms: 1.06x faster                                               |
| tomli_loads                | 2.12 sec                                               | 2.00 sec: 1.06x faster                                              |
| sqlite_synth               | 2.90 us                                                | 2.76 us: 1.05x faster                                               |
| logging_silent             | 101 ns                                                 | 96.1 ns: 1.05x faster                                               |
| genshi_text                | 22.6 ms                                                | 21.5 ms: 1.05x faster                                               |
| regex_compile              | 132 ms                                                 | 126 ms: 1.05x faster                                                |
| 2to3                       | 266 ms                                                 | 254 ms: 1.05x faster                                                |
| sympy_integrate            | 19.8 ms                                                | 19.0 ms: 1.04x faster                                               |
| k_core                     | 2.37 sec                                               | 2.28 sec: 1.04x faster                                              |
| scimark_fft                | 367 ms                                                 | 354 ms: 1.04x faster                                                |
| scimark_sor                | 122 ms                                                 | 118 ms: 1.04x faster                                                |
| xml_etree_process          | 60.5 ms                                                | 58.5 ms: 1.03x faster                                               |
| genshi_xml                 | 50.5 ms                                                | 48.8 ms: 1.03x faster                                               |
| logging_simple             | 5.65 us                                                | 5.48 us: 1.03x faster                                               |
| xml_etree_generate         | 86.8 ms                                                | 84.2 ms: 1.03x faster                                               |
| xml_etree_iterparse        | 101 ms                                                 | 98.4 ms: 1.03x faster                                               |
| pycparser                  | 1.20 sec                                               | 1.17 sec: 1.03x faster                                              |
| logging_format             | 6.23 us                                                | 6.07 us: 1.03x faster                                               |
| deltablue                  | 3.19 ms                                                | 3.11 ms: 1.03x faster                                               |
| sympy_str                  | 273 ms                                                 | 266 ms: 1.03x faster                                                |
| sympy_sum                  | 150 ms                                                 | 147 ms: 1.03x faster                                                |
| sqlalchemy_declarative     | 133 ms                                                 | 130 ms: 1.02x faster                                                |
| bpe_tokeniser              | 4.69 sec                                               | 4.58 sec: 1.02x faster                                              |
| crypto_pyaes               | 74.7 ms                                                | 73.0 ms: 1.02x faster                                               |
| regex_dna                  | 220 ms                                                 | 216 ms: 1.02x faster                                                |
| sqlalchemy_imperative      | 16.9 ms                                                | 16.6 ms: 1.02x faster                                               |
| html5lib                   | 63.4 ms                                                | 62.5 ms: 1.01x faster                                               |
| meteor_contest             | 108 ms                                                 | 107 ms: 1.01x faster                                                |
| gc_traversal               | 4.90 ms                                                | 4.85 ms: 1.01x faster                                               |
| django_template            | 31.7 ms                                                | 31.4 ms: 1.01x faster                                               |
| pprint_pformat             | 1.48 sec                                               | 1.47 sec: 1.01x faster                                              |
| pprint_safe_repr           | 727 ms                                                 | 722 ms: 1.01x faster                                                |
| generators                 | 28.8 ms                                                | 28.6 ms: 1.00x faster                                               |
| pidigits                   | 186 ms                                                 | 186 ms: 1.00x faster                                                |
| chaos                      | 58.0 ms                                                | 58.3 ms: 1.00x slower                                               |
| scimark_lu                 | 114 ms                                                 | 115 ms: 1.01x slower                                                |
| regex_effbot               | 3.77 ms                                                | 3.81 ms: 1.01x slower                                               |
| nqueens                    | 80.9 ms                                                | 81.8 ms: 1.01x slower                                               |
| scimark_monte_carlo        | 66.8 ms                                                | 67.7 ms: 1.01x slower                                               |
| create_gc_cycles           | 2.45 ms                                                | 2.48 ms: 1.01x slower                                               |
| raytrace                   | 262 ms                                                 | 266 ms: 1.02x slower                                                |
| connected_components       | 447 ms                                                 | 455 ms: 1.02x slower                                                |
| unpickle_pure_python       | 213 us                                                 | 217 us: 1.02x slower                                                |
| shortest_path              | 487 ms                                                 | 496 ms: 1.02x slower                                                |
| python_startup             | 12.7 ms                                                | 13.1 ms: 1.03x slower                                               |
| pickle_pure_python         | 302 us                                                 | 317 us: 1.05x slower                                                |
| mako                       | 10.7 ms                                                | 11.3 ms: 1.06x slower                                               |
| bench_thread_pool          | 818 us                                                 | 869 us: 1.06x slower                                                |
| fannkuch                   | 394 ms                                                 | 419 ms: 1.07x slower                                                |
| coroutines                 | 22.2 ms                                                | 23.8 ms: 1.07x slower                                               |
| json_loads                 | 27.2 us                                                | 29.5 us: 1.09x slower                                               |
| many_optionals             | 857 us                                                 | 944 us: 1.10x slower                                                |
| nbody                      | 87.7 ms                                                | 97.7 ms: 1.11x slower                                               |
| json_dumps                 | 10.1 ms                                                | 11.6 ms: 1.14x slower                                               |
| python_startup_no_site     | 7.00 ms                                                | 8.19 ms: 1.17x slower                                               |
| subparsers                 | 15.5 ms                                                | 20.6 ms: 1.33x slower                                               |
| bench_mp_pool              | 24.0 ms                                                | 82.9 ms: 3.46x slower                                               |
| Geometric mean             | (ref)                                                  | 1.04x faster                                                        |

Benchmark hidden because not significant (9): sphinx, json, coverage, hexiom, comprehensions, sympy_expand, asyncio_websockets, docutils, typing_runtime_protocols
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
Ignored benchmarks (4) of results/bm-20250403-3.14.0a6+-9e0e134/bm-20250403-linux-x86_64-iritkatriel-subscr_stats-3.14.0a6+-9e0e134.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.055x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.04x
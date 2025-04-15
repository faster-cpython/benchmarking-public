# Results vs. 3.13.0

- fork: mdboom
- ref: pyframe_clearexceptc
- machine: linux-x86_64
- commit hash: 89a680f
- commit date: 2025-04-15
- overall geometric mean: 1.056x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250415-linux-x86_64-mdboom-pyframe_clearexceptc-3.14.0a7+-89a680f |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 251 ms: 1.06x faster                                                   |
| html5lib       | 63.4 ms                                                | 61.3 ms: 1.03x faster                                                  |
| sphinx         | 1.03 sec                                               | 1.01 sec: 1.02x faster                                                 |
| Geometric mean | (ref)                                                  | 1.03x faster                                                           |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250415-linux-x86_64-mdboom-pyframe_clearexceptc-3.14.0a7+-89a680f |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 313 ms: 1.48x faster                                                   |
| async_tree_memoization     | 437 ms                                                 | 310 ms: 1.41x faster                                                   |
| async_tree_io_tg           | 861 ms                                                 | 617 ms: 1.39x faster                                                   |
| async_tree_io              | 838 ms                                                 | 613 ms: 1.37x faster                                                   |
| async_tree_none            | 350 ms                                                 | 258 ms: 1.36x faster                                                   |
| async_tree_none_tg         | 319 ms                                                 | 247 ms: 1.29x faster                                                   |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 484 ms: 1.18x faster                                                   |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 480 ms: 1.13x faster                                                   |
| async_generators           | 433 ms                                                 | 388 ms: 1.12x faster                                                   |
| coroutines                 | 22.2 ms                                                | 24.4 ms: 1.10x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.23x faster                                                           |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250415-linux-x86_64-mdboom-pyframe_clearexceptc-3.14.0a7+-89a680f |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 67.0 ms: 1.17x faster                                                  |
| pidigits       | 186 ms                                                 | 194 ms: 1.04x slower                                                   |
| nbody          | 87.7 ms                                                | 95.2 ms: 1.09x slower                                                  |
| Geometric mean | (ref)                                                  | 1.01x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250415-linux-x86_64-mdboom-pyframe_clearexceptc-3.14.0a7+-89a680f |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_v8       | 26.9 ms                                                | 23.2 ms: 1.16x faster                                                  |
| regex_effbot   | 3.77 ms                                                | 3.28 ms: 1.15x faster                                                  |
| regex_compile  | 132 ms                                                 | 125 ms: 1.05x faster                                                   |
| regex_dna      | 220 ms                                                 | 209 ms: 1.05x faster                                                   |
| Geometric mean | (ref)                                                  | 1.10x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250415-linux-x86_64-mdboom-pyframe_clearexceptc-3.14.0a7+-89a680f |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| xml_etree_parse      | 154 ms                                                 | 141 ms: 1.09x faster                                                   |
| tomli_loads          | 2.12 sec                                               | 1.98 sec: 1.07x faster                                                 |
| xml_etree_iterparse  | 101 ms                                                 | 98.2 ms: 1.03x faster                                                  |
| xml_etree_generate   | 86.8 ms                                                | 85.0 ms: 1.02x faster                                                  |
| xml_etree_process    | 60.5 ms                                                | 59.2 ms: 1.02x faster                                                  |
| unpickle_pure_python | 213 us                                                 | 218 us: 1.02x slower                                                   |
| pickle_pure_python   | 302 us                                                 | 319 us: 1.05x slower                                                   |
| json_loads           | 27.2 us                                                | 30.2 us: 1.11x slower                                                  |
| json_dumps           | 10.1 ms                                                | 11.5 ms: 1.14x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.01x slower                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250415-linux-x86_64-mdboom-pyframe_clearexceptc-3.14.0a7+-89a680f |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 12.7 ms                                                | 13.2 ms: 1.04x slower                                                  |
| python_startup_no_site | 7.00 ms                                                | 8.21 ms: 1.17x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.11x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250415-linux-x86_64-mdboom-pyframe_clearexceptc-3.14.0a7+-89a680f |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_text    | 22.6 ms                                                | 20.9 ms: 1.08x faster                                                  |
| genshi_xml     | 50.5 ms                                                | 48.8 ms: 1.03x faster                                                  |
| mako           | 10.7 ms                                                | 11.2 ms: 1.05x slower                                                  |
| Geometric mean | (ref)                                                  | 1.02x faster                                                           |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250415-linux-x86_64-mdboom-pyframe_clearexceptc-3.14.0a7+-89a680f |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mdp                        | 2.54 sec                                               | 1.21 sec: 2.10x faster                                                 |
| async_tree_memoization_tg  | 463 ms                                                 | 313 ms: 1.48x faster                                                   |
| async_tree_memoization     | 437 ms                                                 | 310 ms: 1.41x faster                                                   |
| deepcopy                   | 354 us                                                 | 254 us: 1.40x faster                                                   |
| async_tree_io_tg           | 861 ms                                                 | 617 ms: 1.39x faster                                                   |
| async_tree_io              | 838 ms                                                 | 613 ms: 1.37x faster                                                   |
| async_tree_none            | 350 ms                                                 | 258 ms: 1.36x faster                                                   |
| deepcopy_memo              | 38.4 us                                                | 28.6 us: 1.34x faster                                                  |
| async_tree_none_tg         | 319 ms                                                 | 247 ms: 1.29x faster                                                   |
| go                         | 141 ms                                                 | 112 ms: 1.25x faster                                                   |
| deepcopy_reduce            | 3.24 us                                                | 2.71 us: 1.20x faster                                                  |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 484 ms: 1.18x faster                                                   |
| float                      | 78.7 ms                                                | 67.0 ms: 1.17x faster                                                  |
| regex_v8                   | 26.9 ms                                                | 23.2 ms: 1.16x faster                                                  |
| regex_effbot               | 3.77 ms                                                | 3.28 ms: 1.15x faster                                                  |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 480 ms: 1.13x faster                                                   |
| pylint                     | 312 ms                                                 | 279 ms: 1.12x faster                                                   |
| async_generators           | 433 ms                                                 | 388 ms: 1.12x faster                                                   |
| richards                   | 47.5 ms                                                | 42.9 ms: 1.11x faster                                                  |
| spectral_norm              | 113 ms                                                 | 103 ms: 1.10x faster                                                   |
| pyflate                    | 470 ms                                                 | 428 ms: 1.10x faster                                                   |
| telco                      | 8.40 ms                                                | 7.67 ms: 1.09x faster                                                  |
| xml_etree_parse            | 154 ms                                                 | 141 ms: 1.09x faster                                                   |
| richards_super             | 53.7 ms                                                | 49.4 ms: 1.09x faster                                                  |
| genshi_text                | 22.6 ms                                                | 20.9 ms: 1.08x faster                                                  |
| dulwich_log                | 64.6 ms                                                | 59.8 ms: 1.08x faster                                                  |
| tomli_loads                | 2.12 sec                                               | 1.98 sec: 1.07x faster                                                 |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.71 ms: 1.07x faster                                                  |
| 2to3                       | 266 ms                                                 | 251 ms: 1.06x faster                                                   |
| regex_compile              | 132 ms                                                 | 125 ms: 1.05x faster                                                   |
| regex_dna                  | 220 ms                                                 | 209 ms: 1.05x faster                                                   |
| logging_silent             | 101 ns                                                 | 96.6 ns: 1.05x faster                                                  |
| k_core                     | 2.37 sec                                               | 2.27 sec: 1.04x faster                                                 |
| sqlite_synth               | 2.90 us                                                | 2.79 us: 1.04x faster                                                  |
| pycparser                  | 1.20 sec                                               | 1.16 sec: 1.04x faster                                                 |
| genshi_xml                 | 50.5 ms                                                | 48.8 ms: 1.03x faster                                                  |
| html5lib                   | 63.4 ms                                                | 61.3 ms: 1.03x faster                                                  |
| pathlib                    | 17.4 ms                                                | 16.8 ms: 1.03x faster                                                  |
| sympy_integrate            | 19.8 ms                                                | 19.2 ms: 1.03x faster                                                  |
| chaos                      | 58.0 ms                                                | 56.2 ms: 1.03x faster                                                  |
| xml_etree_iterparse        | 101 ms                                                 | 98.2 ms: 1.03x faster                                                  |
| crypto_pyaes               | 74.7 ms                                                | 72.4 ms: 1.03x faster                                                  |
| meteor_contest             | 108 ms                                                 | 105 ms: 1.03x faster                                                   |
| logging_simple             | 5.65 us                                                | 5.50 us: 1.03x faster                                                  |
| scimark_sor                | 122 ms                                                 | 119 ms: 1.03x faster                                                   |
| bpe_tokeniser              | 4.69 sec                                               | 4.59 sec: 1.02x faster                                                 |
| scimark_fft                | 367 ms                                                 | 359 ms: 1.02x faster                                                   |
| xml_etree_generate         | 86.8 ms                                                | 85.0 ms: 1.02x faster                                                  |
| xml_etree_process          | 60.5 ms                                                | 59.2 ms: 1.02x faster                                                  |
| sympy_str                  | 273 ms                                                 | 267 ms: 1.02x faster                                                   |
| sphinx                     | 1.03 sec                                               | 1.01 sec: 1.02x faster                                                 |
| logging_format             | 6.23 us                                                | 6.11 us: 1.02x faster                                                  |
| sympy_sum                  | 150 ms                                                 | 148 ms: 1.02x faster                                                   |
| pprint_safe_repr           | 727 ms                                                 | 715 ms: 1.02x faster                                                   |
| gc_traversal               | 4.90 ms                                                | 4.82 ms: 1.02x faster                                                  |
| pprint_pformat             | 1.48 sec                                               | 1.46 sec: 1.01x faster                                                 |
| nqueens                    | 80.9 ms                                                | 80.3 ms: 1.01x faster                                                  |
| scimark_monte_carlo        | 66.8 ms                                                | 66.3 ms: 1.01x faster                                                  |
| sqlalchemy_declarative     | 133 ms                                                 | 132 ms: 1.00x faster                                                   |
| create_gc_cycles           | 2.45 ms                                                | 2.46 ms: 1.00x slower                                                  |
| raytrace                   | 262 ms                                                 | 264 ms: 1.01x slower                                                   |
| comprehensions             | 16.5 us                                                | 16.7 us: 1.01x slower                                                  |
| shortest_path              | 487 ms                                                 | 494 ms: 1.01x slower                                                   |
| json                       | 5.32 ms                                                | 5.41 ms: 1.02x slower                                                  |
| scimark_lu                 | 114 ms                                                 | 117 ms: 1.02x slower                                                   |
| typing_runtime_protocols   | 160 us                                                 | 164 us: 1.02x slower                                                   |
| unpickle_pure_python       | 213 us                                                 | 218 us: 1.02x slower                                                   |
| hexiom                     | 6.08 ms                                                | 6.27 ms: 1.03x slower                                                  |
| generators                 | 28.8 ms                                                | 29.9 ms: 1.04x slower                                                  |
| pidigits                   | 186 ms                                                 | 194 ms: 1.04x slower                                                   |
| python_startup             | 12.7 ms                                                | 13.2 ms: 1.04x slower                                                  |
| fannkuch                   | 394 ms                                                 | 411 ms: 1.04x slower                                                   |
| mako                       | 10.7 ms                                                | 11.2 ms: 1.05x slower                                                  |
| pickle_pure_python         | 302 us                                                 | 319 us: 1.05x slower                                                   |
| deltablue                  | 3.19 ms                                                | 3.38 ms: 1.06x slower                                                  |
| coverage                   | 82.8 ms                                                | 89.2 ms: 1.08x slower                                                  |
| bench_thread_pool          | 818 us                                                 | 883 us: 1.08x slower                                                   |
| nbody                      | 87.7 ms                                                | 95.2 ms: 1.09x slower                                                  |
| many_optionals             | 857 us                                                 | 932 us: 1.09x slower                                                   |
| coroutines                 | 22.2 ms                                                | 24.4 ms: 1.10x slower                                                  |
| json_loads                 | 27.2 us                                                | 30.2 us: 1.11x slower                                                  |
| json_dumps                 | 10.1 ms                                                | 11.5 ms: 1.14x slower                                                  |
| python_startup_no_site     | 7.00 ms                                                | 8.21 ms: 1.17x slower                                                  |
| subparsers                 | 15.5 ms                                                | 20.7 ms: 1.34x slower                                                  |
| bench_mp_pool              | 24.0 ms                                                | 82.0 ms: 3.42x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.04x faster                                                           |

Benchmark hidden because not significant (6): sqlalchemy_imperative, django_template, asyncio_websockets, sympy_expand, docutils, connected_components
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
Ignored benchmarks (4) of results/bm-20250415-3.14.0a7+-89a680f/bm-20250415-linux-x86_64-mdboom-pyframe_clearexceptc-3.14.0a7+-89a680f.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.056x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.04x
# Results vs. 3.13.0

- fork: iritkatriel
- ref: list_subscr
- machine: linux-x86_64
- commit hash: 3074926
- commit date: 2025-04-17
- overall geometric mean: 1.054x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250417-linux-x86_64-iritkatriel-list_subscr-3.14.0a7+-3074926 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 252 ms: 1.05x faster                                               |
| docutils       | 2.58 sec                                               | 2.62 sec: 1.01x slower                                             |
| html5lib       | 63.4 ms                                                | 62.5 ms: 1.01x faster                                              |
| sphinx         | 1.03 sec                                               | 1.01 sec: 1.02x faster                                             |
| Geometric mean | (ref)                                                  | 1.02x faster                                                       |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250417-linux-x86_64-iritkatriel-list_subscr-3.14.0a7+-3074926 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 312 ms: 1.48x faster                                               |
| async_tree_memoization     | 437 ms                                                 | 310 ms: 1.41x faster                                               |
| async_tree_io_tg           | 861 ms                                                 | 614 ms: 1.40x faster                                               |
| async_tree_io              | 838 ms                                                 | 610 ms: 1.37x faster                                               |
| async_tree_none            | 350 ms                                                 | 257 ms: 1.36x faster                                               |
| async_tree_none_tg         | 319 ms                                                 | 246 ms: 1.30x faster                                               |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 480 ms: 1.19x faster                                               |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 477 ms: 1.14x faster                                               |
| async_generators           | 433 ms                                                 | 399 ms: 1.09x faster                                               |
| coroutines                 | 22.2 ms                                                | 24.4 ms: 1.10x slower                                              |
| Geometric mean             | (ref)                                                  | 1.23x faster                                                       |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250417-linux-x86_64-iritkatriel-list_subscr-3.14.0a7+-3074926 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 67.7 ms: 1.16x faster                                              |
| pidigits       | 186 ms                                                 | 187 ms: 1.00x slower                                               |
| nbody          | 87.7 ms                                                | 95.4 ms: 1.09x slower                                              |
| Geometric mean | (ref)                                                  | 1.02x faster                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250417-linux-x86_64-iritkatriel-list_subscr-3.14.0a7+-3074926 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_v8       | 26.9 ms                                                | 23.0 ms: 1.17x faster                                              |
| regex_effbot   | 3.77 ms                                                | 3.25 ms: 1.16x faster                                              |
| regex_compile  | 132 ms                                                 | 125 ms: 1.05x faster                                               |
| regex_dna      | 220 ms                                                 | 211 ms: 1.04x faster                                               |
| Geometric mean | (ref)                                                  | 1.10x faster                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250417-linux-x86_64-iritkatriel-list_subscr-3.14.0a7+-3074926 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| xml_etree_parse      | 154 ms                                                 | 141 ms: 1.10x faster                                               |
| tomli_loads          | 2.12 sec                                               | 1.98 sec: 1.07x faster                                             |
| xml_etree_process    | 60.5 ms                                                | 58.6 ms: 1.03x faster                                              |
| xml_etree_generate   | 86.8 ms                                                | 84.2 ms: 1.03x faster                                              |
| xml_etree_iterparse  | 101 ms                                                 | 98.8 ms: 1.03x faster                                              |
| unpickle_pure_python | 213 us                                                 | 218 us: 1.02x slower                                               |
| pickle_pure_python   | 302 us                                                 | 319 us: 1.05x slower                                               |
| json_loads           | 27.2 us                                                | 30.2 us: 1.11x slower                                              |
| json_dumps           | 10.1 ms                                                | 11.5 ms: 1.14x slower                                              |
| Geometric mean       | (ref)                                                  | 1.01x slower                                                       |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250417-linux-x86_64-iritkatriel-list_subscr-3.14.0a7+-3074926 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup         | 12.7 ms                                                | 13.3 ms: 1.05x slower                                              |
| python_startup_no_site | 7.00 ms                                                | 8.26 ms: 1.18x slower                                              |
| Geometric mean         | (ref)                                                  | 1.11x slower                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250417-linux-x86_64-iritkatriel-list_subscr-3.14.0a7+-3074926 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| genshi_text     | 22.6 ms                                                | 20.8 ms: 1.09x faster                                              |
| genshi_xml      | 50.5 ms                                                | 49.1 ms: 1.03x faster                                              |
| django_template | 31.7 ms                                                | 31.4 ms: 1.01x faster                                              |
| mako            | 10.7 ms                                                | 11.3 ms: 1.06x slower                                              |
| Geometric mean  | (ref)                                                  | 1.02x faster                                                       |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250417-linux-x86_64-iritkatriel-list_subscr-3.14.0a7+-3074926 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| mdp                        | 2.54 sec                                               | 1.22 sec: 2.08x faster                                             |
| async_tree_memoization_tg  | 463 ms                                                 | 312 ms: 1.48x faster                                               |
| deepcopy                   | 354 us                                                 | 250 us: 1.42x faster                                               |
| async_tree_memoization     | 437 ms                                                 | 310 ms: 1.41x faster                                               |
| async_tree_io_tg           | 861 ms                                                 | 614 ms: 1.40x faster                                               |
| async_tree_io              | 838 ms                                                 | 610 ms: 1.37x faster                                               |
| async_tree_none            | 350 ms                                                 | 257 ms: 1.36x faster                                               |
| deepcopy_memo              | 38.4 us                                                | 28.5 us: 1.35x faster                                              |
| async_tree_none_tg         | 319 ms                                                 | 246 ms: 1.30x faster                                               |
| go                         | 141 ms                                                 | 111 ms: 1.26x faster                                               |
| deepcopy_reduce            | 3.24 us                                                | 2.66 us: 1.22x faster                                              |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 480 ms: 1.19x faster                                               |
| regex_v8                   | 26.9 ms                                                | 23.0 ms: 1.17x faster                                              |
| float                      | 78.7 ms                                                | 67.7 ms: 1.16x faster                                              |
| regex_effbot               | 3.77 ms                                                | 3.25 ms: 1.16x faster                                              |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 477 ms: 1.14x faster                                               |
| pylint                     | 312 ms                                                 | 279 ms: 1.12x faster                                               |
| xml_etree_parse            | 154 ms                                                 | 141 ms: 1.10x faster                                               |
| spectral_norm              | 113 ms                                                 | 103 ms: 1.09x faster                                               |
| richards_super             | 53.7 ms                                                | 49.3 ms: 1.09x faster                                              |
| richards                   | 47.5 ms                                                | 43.6 ms: 1.09x faster                                              |
| genshi_text                | 22.6 ms                                                | 20.8 ms: 1.09x faster                                              |
| telco                      | 8.40 ms                                                | 7.71 ms: 1.09x faster                                              |
| async_generators           | 433 ms                                                 | 399 ms: 1.09x faster                                               |
| dulwich_log                | 64.6 ms                                                | 59.9 ms: 1.08x faster                                              |
| tomli_loads                | 2.12 sec                                               | 1.98 sec: 1.07x faster                                             |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.75 ms: 1.06x faster                                              |
| 2to3                       | 266 ms                                                 | 252 ms: 1.05x faster                                               |
| logging_silent             | 101 ns                                                 | 95.8 ns: 1.05x faster                                              |
| regex_compile              | 132 ms                                                 | 125 ms: 1.05x faster                                               |
| regex_dna                  | 220 ms                                                 | 211 ms: 1.04x faster                                               |
| sympy_integrate            | 19.8 ms                                                | 19.0 ms: 1.04x faster                                              |
| scimark_fft                | 367 ms                                                 | 352 ms: 1.04x faster                                               |
| k_core                     | 2.37 sec                                               | 2.28 sec: 1.04x faster                                             |
| sqlite_synth               | 2.90 us                                                | 2.79 us: 1.04x faster                                              |
| logging_simple             | 5.65 us                                                | 5.43 us: 1.04x faster                                              |
| pyflate                    | 470 ms                                                 | 452 ms: 1.04x faster                                               |
| chaos                      | 58.0 ms                                                | 56.0 ms: 1.04x faster                                              |
| logging_format             | 6.23 us                                                | 6.01 us: 1.04x faster                                              |
| xml_etree_process          | 60.5 ms                                                | 58.6 ms: 1.03x faster                                              |
| crypto_pyaes               | 74.7 ms                                                | 72.4 ms: 1.03x faster                                              |
| xml_etree_generate         | 86.8 ms                                                | 84.2 ms: 1.03x faster                                              |
| pycparser                  | 1.20 sec                                               | 1.16 sec: 1.03x faster                                             |
| genshi_xml                 | 50.5 ms                                                | 49.1 ms: 1.03x faster                                              |
| scimark_sor                | 122 ms                                                 | 119 ms: 1.03x faster                                               |
| pprint_pformat             | 1.48 sec                                               | 1.44 sec: 1.03x faster                                             |
| xml_etree_iterparse        | 101 ms                                                 | 98.8 ms: 1.03x faster                                              |
| sympy_str                  | 273 ms                                                 | 267 ms: 1.02x faster                                               |
| pprint_safe_repr           | 727 ms                                                 | 710 ms: 1.02x faster                                               |
| bpe_tokeniser              | 4.69 sec                                               | 4.60 sec: 1.02x faster                                             |
| sphinx                     | 1.03 sec                                               | 1.01 sec: 1.02x faster                                             |
| html5lib                   | 63.4 ms                                                | 62.5 ms: 1.01x faster                                              |
| pathlib                    | 17.4 ms                                                | 17.2 ms: 1.01x faster                                              |
| sympy_expand               | 456 ms                                                 | 452 ms: 1.01x faster                                               |
| scimark_monte_carlo        | 66.8 ms                                                | 66.2 ms: 1.01x faster                                              |
| django_template            | 31.7 ms                                                | 31.4 ms: 1.01x faster                                              |
| sympy_sum                  | 150 ms                                                 | 149 ms: 1.01x faster                                               |
| sqlalchemy_declarative     | 133 ms                                                 | 133 ms: 1.00x faster                                               |
| pidigits                   | 186 ms                                                 | 187 ms: 1.00x slower                                               |
| sqlalchemy_imperative      | 16.9 ms                                                | 17.0 ms: 1.00x slower                                              |
| raytrace                   | 262 ms                                                 | 263 ms: 1.01x slower                                               |
| create_gc_cycles           | 2.45 ms                                                | 2.48 ms: 1.01x slower                                              |
| connected_components       | 447 ms                                                 | 453 ms: 1.01x slower                                               |
| docutils                   | 2.58 sec                                               | 2.62 sec: 1.01x slower                                             |
| comprehensions             | 16.5 us                                                | 16.7 us: 1.01x slower                                              |
| json                       | 5.32 ms                                                | 5.41 ms: 1.02x slower                                              |
| shortest_path              | 487 ms                                                 | 496 ms: 1.02x slower                                               |
| hexiom                     | 6.08 ms                                                | 6.19 ms: 1.02x slower                                              |
| scimark_lu                 | 114 ms                                                 | 117 ms: 1.02x slower                                               |
| unpickle_pure_python       | 213 us                                                 | 218 us: 1.02x slower                                               |
| gc_traversal               | 4.90 ms                                                | 5.05 ms: 1.03x slower                                              |
| fannkuch                   | 394 ms                                                 | 406 ms: 1.03x slower                                               |
| typing_runtime_protocols   | 160 us                                                 | 166 us: 1.04x slower                                               |
| python_startup             | 12.7 ms                                                | 13.3 ms: 1.05x slower                                              |
| pickle_pure_python         | 302 us                                                 | 319 us: 1.05x slower                                               |
| deltablue                  | 3.19 ms                                                | 3.37 ms: 1.06x slower                                              |
| generators                 | 28.8 ms                                                | 30.4 ms: 1.06x slower                                              |
| coverage                   | 82.8 ms                                                | 87.7 ms: 1.06x slower                                              |
| mako                       | 10.7 ms                                                | 11.3 ms: 1.06x slower                                              |
| bench_thread_pool          | 818 us                                                 | 888 us: 1.09x slower                                               |
| nbody                      | 87.7 ms                                                | 95.4 ms: 1.09x slower                                              |
| many_optionals             | 857 us                                                 | 937 us: 1.09x slower                                               |
| coroutines                 | 22.2 ms                                                | 24.4 ms: 1.10x slower                                              |
| json_loads                 | 27.2 us                                                | 30.2 us: 1.11x slower                                              |
| json_dumps                 | 10.1 ms                                                | 11.5 ms: 1.14x slower                                              |
| python_startup_no_site     | 7.00 ms                                                | 8.26 ms: 1.18x slower                                              |
| subparsers                 | 15.5 ms                                                | 21.0 ms: 1.36x slower                                              |
| bench_mp_pool              | 24.0 ms                                                | 82.2 ms: 3.43x slower                                              |
| Geometric mean             | (ref)                                                  | 1.04x faster                                                       |

Benchmark hidden because not significant (3): meteor_contest, nqueens, asyncio_websockets
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
Ignored benchmarks (4) of results/bm-20250417-3.14.0a7+-3074926/bm-20250417-linux-x86_64-iritkatriel-list_subscr-3.14.0a7+-3074926.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.054x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.04x
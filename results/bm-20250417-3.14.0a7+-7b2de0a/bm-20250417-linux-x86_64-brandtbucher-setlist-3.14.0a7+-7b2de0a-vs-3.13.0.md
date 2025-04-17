# Results vs. 3.13.0

- fork: brandtbucher
- ref: setlist
- machine: linux-x86_64
- commit hash: 7b2de0a
- commit date: 2025-04-17
- overall geometric mean: 1.055x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250417-linux-x86_64-brandtbucher-setlist-3.14.0a7+-7b2de0a |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 249 ms: 1.07x faster                                            |
| docutils       | 2.58 sec                                               | 2.60 sec: 1.01x slower                                          |
| html5lib       | 63.4 ms                                                | 60.1 ms: 1.05x faster                                           |
| sphinx         | 1.03 sec                                               | 1.01 sec: 1.02x faster                                          |
| Geometric mean | (ref)                                                  | 1.03x faster                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250417-linux-x86_64-brandtbucher-setlist-3.14.0a7+-7b2de0a |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 311 ms: 1.49x faster                                            |
| async_tree_memoization     | 437 ms                                                 | 309 ms: 1.41x faster                                            |
| async_tree_io_tg           | 861 ms                                                 | 612 ms: 1.41x faster                                            |
| async_tree_io              | 838 ms                                                 | 613 ms: 1.37x faster                                            |
| async_tree_none            | 350 ms                                                 | 256 ms: 1.37x faster                                            |
| async_tree_none_tg         | 319 ms                                                 | 247 ms: 1.29x faster                                            |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 481 ms: 1.19x faster                                            |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 474 ms: 1.15x faster                                            |
| async_generators           | 433 ms                                                 | 398 ms: 1.09x faster                                            |
| coroutines                 | 22.2 ms                                                | 24.0 ms: 1.08x slower                                           |
| Geometric mean             | (ref)                                                  | 1.23x faster                                                    |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250417-linux-x86_64-brandtbucher-setlist-3.14.0a7+-7b2de0a |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| float          | 78.7 ms                                                | 68.7 ms: 1.15x faster                                           |
| pidigits       | 186 ms                                                 | 190 ms: 1.02x slower                                            |
| nbody          | 87.7 ms                                                | 97.2 ms: 1.11x slower                                           |
| Geometric mean | (ref)                                                  | 1.00x faster                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250417-linux-x86_64-brandtbucher-setlist-3.14.0a7+-7b2de0a |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| regex_v8       | 26.9 ms                                                | 22.6 ms: 1.19x faster                                           |
| regex_effbot   | 3.77 ms                                                | 3.27 ms: 1.15x faster                                           |
| regex_dna      | 220 ms                                                 | 206 ms: 1.07x faster                                            |
| regex_compile  | 132 ms                                                 | 125 ms: 1.06x faster                                            |
| Geometric mean | (ref)                                                  | 1.11x faster                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250417-linux-x86_64-brandtbucher-setlist-3.14.0a7+-7b2de0a |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| xml_etree_parse      | 154 ms                                                 | 141 ms: 1.09x faster                                            |
| tomli_loads          | 2.12 sec                                               | 1.96 sec: 1.08x faster                                          |
| xml_etree_generate   | 86.8 ms                                                | 84.3 ms: 1.03x faster                                           |
| xml_etree_process    | 60.5 ms                                                | 59.2 ms: 1.02x faster                                           |
| xml_etree_iterparse  | 101 ms                                                 | 99.7 ms: 1.02x faster                                           |
| unpickle_pure_python | 213 us                                                 | 215 us: 1.01x slower                                            |
| pickle_pure_python   | 302 us                                                 | 311 us: 1.03x slower                                            |
| json_loads           | 27.2 us                                                | 29.9 us: 1.10x slower                                           |
| json_dumps           | 10.1 ms                                                | 11.4 ms: 1.12x slower                                           |
| Geometric mean       | (ref)                                                  | 1.00x slower                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250417-linux-x86_64-brandtbucher-setlist-3.14.0a7+-7b2de0a |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| python_startup         | 12.7 ms                                                | 13.2 ms: 1.04x slower                                           |
| python_startup_no_site | 7.00 ms                                                | 8.20 ms: 1.17x slower                                           |
| Geometric mean         | (ref)                                                  | 1.10x slower                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250417-linux-x86_64-brandtbucher-setlist-3.14.0a7+-7b2de0a |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| genshi_text     | 22.6 ms                                                | 20.9 ms: 1.08x faster                                           |
| genshi_xml      | 50.5 ms                                                | 48.7 ms: 1.04x faster                                           |
| django_template | 31.7 ms                                                | 32.2 ms: 1.02x slower                                           |
| mako            | 10.7 ms                                                | 11.5 ms: 1.07x slower                                           |
| Geometric mean  | (ref)                                                  | 1.01x faster                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250417-linux-x86_64-brandtbucher-setlist-3.14.0a7+-7b2de0a |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| mdp                        | 2.54 sec                                               | 1.22 sec: 2.09x faster                                          |
| async_tree_memoization_tg  | 463 ms                                                 | 311 ms: 1.49x faster                                            |
| deepcopy                   | 354 us                                                 | 250 us: 1.42x faster                                            |
| async_tree_memoization     | 437 ms                                                 | 309 ms: 1.41x faster                                            |
| async_tree_io_tg           | 861 ms                                                 | 612 ms: 1.41x faster                                            |
| async_tree_io              | 838 ms                                                 | 613 ms: 1.37x faster                                            |
| async_tree_none            | 350 ms                                                 | 256 ms: 1.37x faster                                            |
| deepcopy_memo              | 38.4 us                                                | 28.4 us: 1.35x faster                                           |
| async_tree_none_tg         | 319 ms                                                 | 247 ms: 1.29x faster                                            |
| go                         | 141 ms                                                 | 110 ms: 1.27x faster                                            |
| deepcopy_reduce            | 3.24 us                                                | 2.71 us: 1.20x faster                                           |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 481 ms: 1.19x faster                                            |
| regex_v8                   | 26.9 ms                                                | 22.6 ms: 1.19x faster                                           |
| regex_effbot               | 3.77 ms                                                | 3.27 ms: 1.15x faster                                           |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 474 ms: 1.15x faster                                            |
| float                      | 78.7 ms                                                | 68.7 ms: 1.15x faster                                           |
| pylint                     | 312 ms                                                 | 278 ms: 1.12x faster                                            |
| richards                   | 47.5 ms                                                | 43.0 ms: 1.11x faster                                           |
| xml_etree_parse            | 154 ms                                                 | 141 ms: 1.09x faster                                            |
| richards_super             | 53.7 ms                                                | 49.2 ms: 1.09x faster                                           |
| async_generators           | 433 ms                                                 | 398 ms: 1.09x faster                                            |
| dulwich_log                | 64.6 ms                                                | 59.5 ms: 1.09x faster                                           |
| spectral_norm              | 113 ms                                                 | 104 ms: 1.09x faster                                            |
| genshi_text                | 22.6 ms                                                | 20.9 ms: 1.08x faster                                           |
| logging_silent             | 101 ns                                                 | 93.3 ns: 1.08x faster                                           |
| tomli_loads                | 2.12 sec                                               | 1.96 sec: 1.08x faster                                          |
| telco                      | 8.40 ms                                                | 7.85 ms: 1.07x faster                                           |
| regex_dna                  | 220 ms                                                 | 206 ms: 1.07x faster                                            |
| 2to3                       | 266 ms                                                 | 249 ms: 1.07x faster                                            |
| regex_compile              | 132 ms                                                 | 125 ms: 1.06x faster                                            |
| html5lib                   | 63.4 ms                                                | 60.1 ms: 1.05x faster                                           |
| sqlite_synth               | 2.90 us                                                | 2.78 us: 1.04x faster                                           |
| sympy_integrate            | 19.8 ms                                                | 19.0 ms: 1.04x faster                                           |
| pyflate                    | 470 ms                                                 | 451 ms: 1.04x faster                                            |
| pycparser                  | 1.20 sec                                               | 1.16 sec: 1.04x faster                                          |
| chaos                      | 58.0 ms                                                | 56.0 ms: 1.04x faster                                           |
| k_core                     | 2.37 sec                                               | 2.29 sec: 1.04x faster                                          |
| genshi_xml                 | 50.5 ms                                                | 48.7 ms: 1.04x faster                                           |
| pathlib                    | 17.4 ms                                                | 16.8 ms: 1.03x faster                                           |
| sympy_str                  | 273 ms                                                 | 265 ms: 1.03x faster                                            |
| xml_etree_generate         | 86.8 ms                                                | 84.3 ms: 1.03x faster                                           |
| scimark_fft                | 367 ms                                                 | 356 ms: 1.03x faster                                            |
| logging_simple             | 5.65 us                                                | 5.49 us: 1.03x faster                                           |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.89 ms: 1.03x faster                                           |
| scimark_sor                | 122 ms                                                 | 119 ms: 1.03x faster                                            |
| sphinx                     | 1.03 sec                                               | 1.01 sec: 1.02x faster                                          |
| meteor_contest             | 108 ms                                                 | 106 ms: 1.02x faster                                            |
| xml_etree_process          | 60.5 ms                                                | 59.2 ms: 1.02x faster                                           |
| bpe_tokeniser              | 4.69 sec                                               | 4.59 sec: 1.02x faster                                          |
| crypto_pyaes               | 74.7 ms                                                | 73.1 ms: 1.02x faster                                           |
| nqueens                    | 80.9 ms                                                | 79.3 ms: 1.02x faster                                           |
| pprint_safe_repr           | 727 ms                                                 | 714 ms: 1.02x faster                                            |
| sympy_sum                  | 150 ms                                                 | 148 ms: 1.02x faster                                            |
| logging_format             | 6.23 us                                                | 6.14 us: 1.02x faster                                           |
| xml_etree_iterparse        | 101 ms                                                 | 99.7 ms: 1.02x faster                                           |
| pprint_pformat             | 1.48 sec                                               | 1.46 sec: 1.01x faster                                          |
| sympy_expand               | 456 ms                                                 | 450 ms: 1.01x faster                                            |
| raytrace                   | 262 ms                                                 | 259 ms: 1.01x faster                                            |
| docutils                   | 2.58 sec                                               | 2.60 sec: 1.01x slower                                          |
| connected_components       | 447 ms                                                 | 450 ms: 1.01x slower                                            |
| unpickle_pure_python       | 213 us                                                 | 215 us: 1.01x slower                                            |
| shortest_path              | 487 ms                                                 | 492 ms: 1.01x slower                                            |
| create_gc_cycles           | 2.45 ms                                                | 2.49 ms: 1.01x slower                                           |
| django_template            | 31.7 ms                                                | 32.2 ms: 1.02x slower                                           |
| pidigits                   | 186 ms                                                 | 190 ms: 1.02x slower                                            |
| scimark_lu                 | 114 ms                                                 | 118 ms: 1.03x slower                                            |
| pickle_pure_python         | 302 us                                                 | 311 us: 1.03x slower                                            |
| gc_traversal               | 4.90 ms                                                | 5.04 ms: 1.03x slower                                           |
| hexiom                     | 6.08 ms                                                | 6.27 ms: 1.03x slower                                           |
| typing_runtime_protocols   | 160 us                                                 | 166 us: 1.04x slower                                            |
| python_startup             | 12.7 ms                                                | 13.2 ms: 1.04x slower                                           |
| fannkuch                   | 394 ms                                                 | 414 ms: 1.05x slower                                            |
| deltablue                  | 3.19 ms                                                | 3.37 ms: 1.06x slower                                           |
| coverage                   | 82.8 ms                                                | 88.2 ms: 1.07x slower                                           |
| generators                 | 28.8 ms                                                | 30.7 ms: 1.07x slower                                           |
| mako                       | 10.7 ms                                                | 11.5 ms: 1.07x slower                                           |
| coroutines                 | 22.2 ms                                                | 24.0 ms: 1.08x slower                                           |
| many_optionals             | 857 us                                                 | 929 us: 1.08x slower                                            |
| bench_thread_pool          | 818 us                                                 | 889 us: 1.09x slower                                            |
| json_loads                 | 27.2 us                                                | 29.9 us: 1.10x slower                                           |
| nbody                      | 87.7 ms                                                | 97.2 ms: 1.11x slower                                           |
| json_dumps                 | 10.1 ms                                                | 11.4 ms: 1.12x slower                                           |
| python_startup_no_site     | 7.00 ms                                                | 8.20 ms: 1.17x slower                                           |
| subparsers                 | 15.5 ms                                                | 20.7 ms: 1.34x slower                                           |
| bench_mp_pool              | 24.0 ms                                                | 81.8 ms: 3.41x slower                                           |
| Geometric mean             | (ref)                                                  | 1.04x faster                                                    |

Benchmark hidden because not significant (6): scimark_monte_carlo, sqlalchemy_imperative, sqlalchemy_declarative, asyncio_websockets, json, comprehensions
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
Ignored benchmarks (4) of results/bm-20250417-3.14.0a7+-7b2de0a/bm-20250417-linux-x86_64-brandtbucher-setlist-3.14.0a7+-7b2de0a.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.055x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.04x
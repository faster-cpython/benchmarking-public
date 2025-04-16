# Results vs. 3.13.0

- fork: brandtbucher
- ref: call_self_or_null
- machine: linux-x86_64
- commit hash: 1196dc5
- commit date: 2025-04-16
- overall geometric mean: 1.049x faster
- HPT reliability: 99.99%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250416-linux-x86_64-brandtbucher-call_self_or_null-3.14.0a7+-1196dc5 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 250 ms: 1.07x faster                                                      |
| docutils       | 2.58 sec                                               | 2.59 sec: 1.00x slower                                                    |
| html5lib       | 63.4 ms                                                | 62.6 ms: 1.01x faster                                                     |
| sphinx         | 1.03 sec                                               | 1.01 sec: 1.02x faster                                                    |
| Geometric mean | (ref)                                                  | 1.02x faster                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250416-linux-x86_64-brandtbucher-call_self_or_null-3.14.0a7+-1196dc5 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 320 ms: 1.45x faster                                                      |
| async_tree_io_tg           | 861 ms                                                 | 623 ms: 1.38x faster                                                      |
| async_tree_memoization     | 437 ms                                                 | 318 ms: 1.37x faster                                                      |
| async_tree_io              | 838 ms                                                 | 624 ms: 1.34x faster                                                      |
| async_tree_none            | 350 ms                                                 | 263 ms: 1.33x faster                                                      |
| async_tree_none_tg         | 319 ms                                                 | 253 ms: 1.26x faster                                                      |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 485 ms: 1.18x faster                                                      |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 480 ms: 1.13x faster                                                      |
| async_generators           | 433 ms                                                 | 400 ms: 1.08x faster                                                      |
| coroutines                 | 22.2 ms                                                | 24.2 ms: 1.09x slower                                                     |
| Geometric mean             | (ref)                                                  | 1.21x faster                                                              |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250416-linux-x86_64-brandtbucher-call_self_or_null-3.14.0a7+-1196dc5 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 73.0 ms: 1.08x faster                                                     |
| pidigits       | 186 ms                                                 | 194 ms: 1.04x slower                                                      |
| nbody          | 87.7 ms                                                | 96.6 ms: 1.10x slower                                                     |
| Geometric mean | (ref)                                                  | 1.02x slower                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250416-linux-x86_64-brandtbucher-call_self_or_null-3.14.0a7+-1196dc5 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_v8       | 26.9 ms                                                | 22.6 ms: 1.19x faster                                                     |
| regex_effbot   | 3.77 ms                                                | 3.25 ms: 1.16x faster                                                     |
| regex_compile  | 132 ms                                                 | 127 ms: 1.04x faster                                                      |
| regex_dna      | 220 ms                                                 | 212 ms: 1.04x faster                                                      |
| Geometric mean | (ref)                                                  | 1.10x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250416-linux-x86_64-brandtbucher-call_self_or_null-3.14.0a7+-1196dc5 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| xml_etree_parse      | 154 ms                                                 | 141 ms: 1.09x faster                                                      |
| tomli_loads          | 2.12 sec                                               | 1.96 sec: 1.08x faster                                                    |
| xml_etree_generate   | 86.8 ms                                                | 84.1 ms: 1.03x faster                                                     |
| xml_etree_process    | 60.5 ms                                                | 58.7 ms: 1.03x faster                                                     |
| xml_etree_iterparse  | 101 ms                                                 | 98.7 ms: 1.03x faster                                                     |
| pickle_pure_python   | 302 us                                                 | 318 us: 1.05x slower                                                      |
| json_loads           | 27.2 us                                                | 29.4 us: 1.08x slower                                                     |
| unpickle_pure_python | 213 us                                                 | 231 us: 1.09x slower                                                      |
| json_dumps           | 10.1 ms                                                | 11.4 ms: 1.13x slower                                                     |
| Geometric mean       | (ref)                                                  | 1.01x slower                                                              |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250416-linux-x86_64-brandtbucher-call_self_or_null-3.14.0a7+-1196dc5 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 12.7 ms                                                | 13.2 ms: 1.04x slower                                                     |
| python_startup_no_site | 7.00 ms                                                | 8.24 ms: 1.18x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.11x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250416-linux-x86_64-brandtbucher-call_self_or_null-3.14.0a7+-1196dc5 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| genshi_text    | 22.6 ms                                                | 21.8 ms: 1.04x faster                                                     |
| genshi_xml     | 50.5 ms                                                | 49.1 ms: 1.03x faster                                                     |
| mako           | 10.7 ms                                                | 11.0 ms: 1.03x slower                                                     |
| Geometric mean | (ref)                                                  | 1.01x faster                                                              |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250416-linux-x86_64-brandtbucher-call_self_or_null-3.14.0a7+-1196dc5 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mdp                        | 2.54 sec                                               | 1.20 sec: 2.12x faster                                                    |
| async_tree_memoization_tg  | 463 ms                                                 | 320 ms: 1.45x faster                                                      |
| deepcopy                   | 354 us                                                 | 249 us: 1.42x faster                                                      |
| async_tree_io_tg           | 861 ms                                                 | 623 ms: 1.38x faster                                                      |
| async_tree_memoization     | 437 ms                                                 | 318 ms: 1.37x faster                                                      |
| deepcopy_memo              | 38.4 us                                                | 28.4 us: 1.35x faster                                                     |
| async_tree_io              | 838 ms                                                 | 624 ms: 1.34x faster                                                      |
| async_tree_none            | 350 ms                                                 | 263 ms: 1.33x faster                                                      |
| async_tree_none_tg         | 319 ms                                                 | 253 ms: 1.26x faster                                                      |
| go                         | 141 ms                                                 | 113 ms: 1.25x faster                                                      |
| deepcopy_reduce            | 3.24 us                                                | 2.63 us: 1.23x faster                                                     |
| regex_v8                   | 26.9 ms                                                | 22.6 ms: 1.19x faster                                                     |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 485 ms: 1.18x faster                                                      |
| regex_effbot               | 3.77 ms                                                | 3.25 ms: 1.16x faster                                                     |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 480 ms: 1.13x faster                                                      |
| richards                   | 47.5 ms                                                | 42.2 ms: 1.13x faster                                                     |
| pylint                     | 312 ms                                                 | 278 ms: 1.12x faster                                                      |
| richards_super             | 53.7 ms                                                | 48.3 ms: 1.11x faster                                                     |
| spectral_norm              | 113 ms                                                 | 103 ms: 1.10x faster                                                      |
| xml_etree_parse            | 154 ms                                                 | 141 ms: 1.09x faster                                                      |
| async_generators           | 433 ms                                                 | 400 ms: 1.08x faster                                                      |
| tomli_loads                | 2.12 sec                                               | 1.96 sec: 1.08x faster                                                    |
| float                      | 78.7 ms                                                | 73.0 ms: 1.08x faster                                                     |
| dulwich_log                | 64.6 ms                                                | 60.0 ms: 1.08x faster                                                     |
| telco                      | 8.40 ms                                                | 7.79 ms: 1.08x faster                                                     |
| 2to3                       | 266 ms                                                 | 250 ms: 1.07x faster                                                      |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.74 ms: 1.06x faster                                                     |
| k_core                     | 2.37 sec                                               | 2.27 sec: 1.04x faster                                                    |
| regex_compile              | 132 ms                                                 | 127 ms: 1.04x faster                                                      |
| pyflate                    | 470 ms                                                 | 452 ms: 1.04x faster                                                      |
| regex_dna                  | 220 ms                                                 | 212 ms: 1.04x faster                                                      |
| genshi_text                | 22.6 ms                                                | 21.8 ms: 1.04x faster                                                     |
| sqlite_synth               | 2.90 us                                                | 2.80 us: 1.03x faster                                                     |
| scimark_fft                | 367 ms                                                 | 355 ms: 1.03x faster                                                      |
| scimark_sor                | 122 ms                                                 | 118 ms: 1.03x faster                                                      |
| xml_etree_generate         | 86.8 ms                                                | 84.1 ms: 1.03x faster                                                     |
| xml_etree_process          | 60.5 ms                                                | 58.7 ms: 1.03x faster                                                     |
| genshi_xml                 | 50.5 ms                                                | 49.1 ms: 1.03x faster                                                     |
| pycparser                  | 1.20 sec                                               | 1.17 sec: 1.03x faster                                                    |
| sympy_str                  | 273 ms                                                 | 265 ms: 1.03x faster                                                      |
| xml_etree_iterparse        | 101 ms                                                 | 98.7 ms: 1.03x faster                                                     |
| crypto_pyaes               | 74.7 ms                                                | 72.8 ms: 1.03x faster                                                     |
| logging_silent             | 101 ns                                                 | 98.5 ns: 1.03x faster                                                     |
| bpe_tokeniser              | 4.69 sec                                               | 4.57 sec: 1.03x faster                                                    |
| pathlib                    | 17.4 ms                                                | 16.9 ms: 1.03x faster                                                     |
| sympy_integrate            | 19.8 ms                                                | 19.4 ms: 1.02x faster                                                     |
| sphinx                     | 1.03 sec                                               | 1.01 sec: 1.02x faster                                                    |
| meteor_contest             | 108 ms                                                 | 106 ms: 1.02x faster                                                      |
| scimark_monte_carlo        | 66.8 ms                                                | 65.6 ms: 1.02x faster                                                     |
| logging_format             | 6.23 us                                                | 6.12 us: 1.02x faster                                                     |
| sympy_expand               | 456 ms                                                 | 448 ms: 1.02x faster                                                      |
| sympy_sum                  | 150 ms                                                 | 148 ms: 1.02x faster                                                      |
| json                       | 5.32 ms                                                | 5.25 ms: 1.01x faster                                                     |
| html5lib                   | 63.4 ms                                                | 62.6 ms: 1.01x faster                                                     |
| sqlalchemy_declarative     | 133 ms                                                 | 132 ms: 1.01x faster                                                      |
| logging_simple             | 5.65 us                                                | 5.62 us: 1.01x faster                                                     |
| pprint_pformat             | 1.48 sec                                               | 1.47 sec: 1.01x faster                                                    |
| sqlalchemy_imperative      | 16.9 ms                                                | 16.8 ms: 1.01x faster                                                     |
| docutils                   | 2.58 sec                                               | 2.59 sec: 1.00x slower                                                    |
| nqueens                    | 80.9 ms                                                | 81.3 ms: 1.00x slower                                                     |
| create_gc_cycles           | 2.45 ms                                                | 2.48 ms: 1.01x slower                                                     |
| comprehensions             | 16.5 us                                                | 16.7 us: 1.01x slower                                                     |
| generators                 | 28.8 ms                                                | 29.3 ms: 1.02x slower                                                     |
| connected_components       | 447 ms                                                 | 455 ms: 1.02x slower                                                      |
| shortest_path              | 487 ms                                                 | 499 ms: 1.03x slower                                                      |
| mako                       | 10.7 ms                                                | 11.0 ms: 1.03x slower                                                     |
| hexiom                     | 6.08 ms                                                | 6.24 ms: 1.03x slower                                                     |
| gc_traversal               | 4.90 ms                                                | 5.05 ms: 1.03x slower                                                     |
| scimark_lu                 | 114 ms                                                 | 118 ms: 1.03x slower                                                      |
| typing_runtime_protocols   | 160 us                                                 | 166 us: 1.04x slower                                                      |
| pidigits                   | 186 ms                                                 | 194 ms: 1.04x slower                                                      |
| coverage                   | 82.8 ms                                                | 86.3 ms: 1.04x slower                                                     |
| python_startup             | 12.7 ms                                                | 13.2 ms: 1.04x slower                                                     |
| chaos                      | 58.0 ms                                                | 60.7 ms: 1.05x slower                                                     |
| pickle_pure_python         | 302 us                                                 | 318 us: 1.05x slower                                                      |
| fannkuch                   | 394 ms                                                 | 415 ms: 1.05x slower                                                      |
| deltablue                  | 3.19 ms                                                | 3.40 ms: 1.07x slower                                                     |
| json_loads                 | 27.2 us                                                | 29.4 us: 1.08x slower                                                     |
| bench_thread_pool          | 818 us                                                 | 886 us: 1.08x slower                                                      |
| unpickle_pure_python       | 213 us                                                 | 231 us: 1.09x slower                                                      |
| many_optionals             | 857 us                                                 | 932 us: 1.09x slower                                                      |
| coroutines                 | 22.2 ms                                                | 24.2 ms: 1.09x slower                                                     |
| nbody                      | 87.7 ms                                                | 96.6 ms: 1.10x slower                                                     |
| raytrace                   | 262 ms                                                 | 293 ms: 1.12x slower                                                      |
| json_dumps                 | 10.1 ms                                                | 11.4 ms: 1.13x slower                                                     |
| python_startup_no_site     | 7.00 ms                                                | 8.24 ms: 1.18x slower                                                     |
| subparsers                 | 15.5 ms                                                | 20.4 ms: 1.32x slower                                                     |
| bench_mp_pool              | 24.0 ms                                                | 81.7 ms: 3.41x slower                                                     |
| Geometric mean             | (ref)                                                  | 1.03x faster                                                              |

Benchmark hidden because not significant (3): django_template, pprint_safe_repr, asyncio_websockets
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
Ignored benchmarks (4) of results/bm-20250416-3.14.0a7+-1196dc5/bm-20250416-linux-x86_64-brandtbucher-call_self_or_null-3.14.0a7+-1196dc5.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.049x faster

# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.04x
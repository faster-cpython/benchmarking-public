# Results vs. 3.13.0

- fork: brandtbucher
- ref: jit_up_10_6
- machine: linux-x86_64
- commit hash: 89bbf67
- commit date: 2025-03-29
- overall geometric mean: 1.040x faster
- HPT reliability: 96.91%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.05x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250329-linux-x86_64-brandtbucher-jit_up_10_6-3.14.0a6+-89bbf67 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 267 ms: 1.00x slower                                                |
| docutils       | 2.58 sec                                               | 2.70 sec: 1.05x slower                                              |
| Geometric mean | (ref)                                                  | 1.01x slower                                                        |

Benchmark hidden because not significant (2): html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250329-linux-x86_64-brandtbucher-jit_up_10_6-3.14.0a6+-89bbf67 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 314 ms: 1.48x faster                                                |
| async_tree_io_tg           | 861 ms                                                 | 621 ms: 1.39x faster                                                |
| async_tree_memoization     | 437 ms                                                 | 315 ms: 1.39x faster                                                |
| async_tree_io              | 838 ms                                                 | 616 ms: 1.36x faster                                                |
| async_tree_none            | 350 ms                                                 | 260 ms: 1.35x faster                                                |
| async_tree_none_tg         | 319 ms                                                 | 252 ms: 1.27x faster                                                |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 492 ms: 1.16x faster                                                |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 477 ms: 1.14x faster                                                |
| async_generators           | 433 ms                                                 | 415 ms: 1.04x faster                                                |
| coroutines                 | 22.2 ms                                                | 23.4 ms: 1.05x slower                                               |
| Geometric mean             | (ref)                                                  | 1.22x faster                                                        |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250329-linux-x86_64-brandtbucher-jit_up_10_6-3.14.0a6+-89bbf67 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 64.8 ms: 1.21x faster                                               |
| nbody          | 87.7 ms                                                | 86.6 ms: 1.01x faster                                               |
| pidigits       | 186 ms                                                 | 186 ms: 1.00x faster                                                |
| Geometric mean | (ref)                                                  | 1.07x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250329-linux-x86_64-brandtbucher-jit_up_10_6-3.14.0a6+-89bbf67 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                | 3.08 ms: 1.22x faster                                               |
| regex_v8       | 26.9 ms                                                | 22.7 ms: 1.18x faster                                               |
| regex_dna      | 220 ms                                                 | 211 ms: 1.04x faster                                                |
| regex_compile  | 132 ms                                                 | 129 ms: 1.02x faster                                                |
| Geometric mean | (ref)                                                  | 1.11x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250329-linux-x86_64-brandtbucher-jit_up_10_6-3.14.0a6+-89bbf67 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| tomli_loads          | 2.12 sec                                               | 1.89 sec: 1.12x faster                                              |
| xml_etree_parse      | 154 ms                                                 | 139 ms: 1.11x faster                                                |
| xml_etree_generate   | 86.8 ms                                                | 80.2 ms: 1.08x faster                                               |
| xml_etree_process    | 60.5 ms                                                | 56.7 ms: 1.07x faster                                               |
| xml_etree_iterparse  | 101 ms                                                 | 98.7 ms: 1.03x faster                                               |
| unpickle_pure_python | 213 us                                                 | 211 us: 1.01x faster                                                |
| pickle_pure_python   | 302 us                                                 | 328 us: 1.08x slower                                                |
| json_loads           | 27.2 us                                                | 30.1 us: 1.11x slower                                               |
| json_dumps           | 10.1 ms                                                | 11.5 ms: 1.14x slower                                               |
| Geometric mean       | (ref)                                                  | 1.01x faster                                                        |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250329-linux-x86_64-brandtbucher-jit_up_10_6-3.14.0a6+-89bbf67 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 12.7 ms                                                | 13.2 ms: 1.04x slower                                               |
| python_startup_no_site | 7.00 ms                                                | 8.23 ms: 1.17x slower                                               |
| Geometric mean         | (ref)                                                  | 1.10x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250329-linux-x86_64-brandtbucher-jit_up_10_6-3.14.0a6+-89bbf67 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| genshi_text    | 22.6 ms                                                | 21.2 ms: 1.07x faster                                               |
| genshi_xml     | 50.5 ms                                                | 49.8 ms: 1.01x faster                                               |
| mako           | 10.7 ms                                                | 11.1 ms: 1.04x slower                                               |
| Geometric mean | (ref)                                                  | 1.01x faster                                                        |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250329-linux-x86_64-brandtbucher-jit_up_10_6-3.14.0a6+-89bbf67 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 314 ms: 1.48x faster                                                |
| async_tree_io_tg           | 861 ms                                                 | 621 ms: 1.39x faster                                                |
| async_tree_memoization     | 437 ms                                                 | 315 ms: 1.39x faster                                                |
| async_tree_io              | 838 ms                                                 | 616 ms: 1.36x faster                                                |
| async_tree_none            | 350 ms                                                 | 260 ms: 1.35x faster                                                |
| deepcopy                   | 354 us                                                 | 265 us: 1.34x faster                                                |
| deepcopy_memo              | 38.4 us                                                | 29.1 us: 1.32x faster                                               |
| richards                   | 47.5 ms                                                | 37.2 ms: 1.28x faster                                               |
| async_tree_none_tg         | 319 ms                                                 | 252 ms: 1.27x faster                                                |
| richards_super             | 53.7 ms                                                | 42.8 ms: 1.26x faster                                               |
| regex_effbot               | 3.77 ms                                                | 3.08 ms: 1.22x faster                                               |
| float                      | 78.7 ms                                                | 64.8 ms: 1.21x faster                                               |
| deepcopy_reduce            | 3.24 us                                                | 2.74 us: 1.18x faster                                               |
| regex_v8                   | 26.9 ms                                                | 22.7 ms: 1.18x faster                                               |
| scimark_fft                | 367 ms                                                 | 313 ms: 1.17x faster                                                |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 492 ms: 1.16x faster                                                |
| spectral_norm              | 113 ms                                                 | 97.4 ms: 1.16x faster                                               |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 477 ms: 1.14x faster                                                |
| tomli_loads                | 2.12 sec                                               | 1.89 sec: 1.12x faster                                              |
| xml_etree_parse            | 154 ms                                                 | 139 ms: 1.11x faster                                                |
| pylint                     | 312 ms                                                 | 285 ms: 1.10x faster                                                |
| go                         | 141 ms                                                 | 129 ms: 1.09x faster                                                |
| xml_etree_generate         | 86.8 ms                                                | 80.2 ms: 1.08x faster                                               |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.65 ms: 1.08x faster                                               |
| xml_etree_process          | 60.5 ms                                                | 56.7 ms: 1.07x faster                                               |
| genshi_text                | 22.6 ms                                                | 21.2 ms: 1.07x faster                                               |
| pyflate                    | 470 ms                                                 | 443 ms: 1.06x faster                                                |
| dulwich_log                | 64.6 ms                                                | 61.0 ms: 1.06x faster                                               |
| pycparser                  | 1.20 sec                                               | 1.13 sec: 1.06x faster                                              |
| deltablue                  | 3.19 ms                                                | 3.03 ms: 1.05x faster                                               |
| sqlite_synth               | 2.90 us                                                | 2.76 us: 1.05x faster                                               |
| async_generators           | 433 ms                                                 | 415 ms: 1.04x faster                                                |
| regex_dna                  | 220 ms                                                 | 211 ms: 1.04x faster                                                |
| pathlib                    | 17.4 ms                                                | 16.7 ms: 1.04x faster                                               |
| thrift                     | 800 us                                                 | 776 us: 1.03x faster                                                |
| telco                      | 8.40 ms                                                | 8.16 ms: 1.03x faster                                               |
| scimark_sor                | 122 ms                                                 | 119 ms: 1.03x faster                                                |
| xml_etree_iterparse        | 101 ms                                                 | 98.7 ms: 1.03x faster                                               |
| k_core                     | 2.37 sec                                               | 2.31 sec: 1.02x faster                                              |
| regex_compile              | 132 ms                                                 | 129 ms: 1.02x faster                                                |
| logging_format             | 6.23 us                                                | 6.11 us: 1.02x faster                                               |
| logging_simple             | 5.65 us                                                | 5.55 us: 1.02x faster                                               |
| gc_traversal               | 4.90 ms                                                | 4.82 ms: 1.02x faster                                               |
| mdp                        | 2.54 sec                                               | 2.51 sec: 1.01x faster                                              |
| genshi_xml                 | 50.5 ms                                                | 49.8 ms: 1.01x faster                                               |
| nbody                      | 87.7 ms                                                | 86.6 ms: 1.01x faster                                               |
| unpickle_pure_python       | 213 us                                                 | 211 us: 1.01x faster                                                |
| bpe_tokeniser              | 4.69 sec                                               | 4.65 sec: 1.01x faster                                              |
| pidigits                   | 186 ms                                                 | 186 ms: 1.00x faster                                                |
| 2to3                       | 266 ms                                                 | 267 ms: 1.00x slower                                                |
| generators                 | 28.8 ms                                                | 29.0 ms: 1.01x slower                                               |
| connected_components       | 447 ms                                                 | 453 ms: 1.01x slower                                                |
| crypto_pyaes               | 74.7 ms                                                | 76.0 ms: 1.02x slower                                               |
| create_gc_cycles           | 2.45 ms                                                | 2.49 ms: 1.02x slower                                               |
| raytrace                   | 262 ms                                                 | 267 ms: 1.02x slower                                                |
| sympy_str                  | 273 ms                                                 | 279 ms: 1.02x slower                                                |
| scimark_monte_carlo        | 66.8 ms                                                | 68.5 ms: 1.02x slower                                               |
| sympy_integrate            | 19.8 ms                                                | 20.4 ms: 1.03x slower                                               |
| sympy_sum                  | 150 ms                                                 | 155 ms: 1.03x slower                                                |
| chaos                      | 58.0 ms                                                | 59.8 ms: 1.03x slower                                               |
| mako                       | 10.7 ms                                                | 11.1 ms: 1.04x slower                                               |
| sqlalchemy_declarative     | 133 ms                                                 | 138 ms: 1.04x slower                                                |
| sqlalchemy_imperative      | 16.9 ms                                                | 17.6 ms: 1.04x slower                                               |
| python_startup             | 12.7 ms                                                | 13.2 ms: 1.04x slower                                               |
| coverage                   | 82.8 ms                                                | 86.2 ms: 1.04x slower                                               |
| scimark_lu                 | 114 ms                                                 | 119 ms: 1.04x slower                                                |
| pprint_safe_repr           | 727 ms                                                 | 759 ms: 1.04x slower                                                |
| docutils                   | 2.58 sec                                               | 2.70 sec: 1.05x slower                                              |
| sympy_expand               | 456 ms                                                 | 478 ms: 1.05x slower                                                |
| typing_runtime_protocols   | 160 us                                                 | 168 us: 1.05x slower                                                |
| coroutines                 | 22.2 ms                                                | 23.4 ms: 1.05x slower                                               |
| pprint_pformat             | 1.48 sec                                               | 1.58 sec: 1.07x slower                                              |
| nqueens                    | 80.9 ms                                                | 86.3 ms: 1.07x slower                                               |
| fannkuch                   | 394 ms                                                 | 422 ms: 1.07x slower                                                |
| pickle_pure_python         | 302 us                                                 | 328 us: 1.08x slower                                                |
| bench_thread_pool          | 818 us                                                 | 889 us: 1.09x slower                                                |
| json_loads                 | 27.2 us                                                | 30.1 us: 1.11x slower                                               |
| comprehensions             | 16.5 us                                                | 18.4 us: 1.11x slower                                               |
| json_dumps                 | 10.1 ms                                                | 11.5 ms: 1.14x slower                                               |
| hexiom                     | 6.08 ms                                                | 7.04 ms: 1.16x slower                                               |
| many_optionals             | 857 us                                                 | 994 us: 1.16x slower                                                |
| python_startup_no_site     | 7.00 ms                                                | 8.23 ms: 1.17x slower                                               |
| subparsers                 | 15.5 ms                                                | 20.9 ms: 1.35x slower                                               |
| bench_mp_pool              | 24.0 ms                                                | 83.4 ms: 3.48x slower                                               |
| Geometric mean             | (ref)                                                  | 1.02x faster                                                        |

Benchmark hidden because not significant (8): logging_silent, json, html5lib, sphinx, asyncio_websockets, meteor_contest, shortest_path, django_template
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250329-3.14.0a6+-89bbf67-JIT/bm-20250329-linux-x86_64-brandtbucher-jit_up_10_6-3.14.0a6+-89bbf67.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.040x faster

# HPT report

- Reliability score: 96.91% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.05x
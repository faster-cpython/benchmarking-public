# Results vs. 3.13.0

- fork: brandtbucher
- ref: jit_up_10_9
- machine: linux-x86_64
- commit hash: 07ab4d7
- commit date: 2025-03-28
- overall geometric mean: 1.034x faster
- HPT reliability: 96.83%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.05x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250328-linux-x86_64-brandtbucher-jit_up_10_9-3.14.0a6+-07ab4d7 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| docutils       | 2.58 sec                                               | 2.70 sec: 1.05x slower                                              |
| Geometric mean | (ref)                                                  | 1.01x slower                                                        |

Benchmark hidden because not significant (3): 2to3, html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250328-linux-x86_64-brandtbucher-jit_up_10_9-3.14.0a6+-07ab4d7 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 316 ms: 1.46x faster                                                |
| async_tree_io_tg           | 861 ms                                                 | 628 ms: 1.37x faster                                                |
| async_tree_io              | 838 ms                                                 | 619 ms: 1.35x faster                                                |
| async_tree_memoization     | 437 ms                                                 | 323 ms: 1.35x faster                                                |
| async_tree_none            | 350 ms                                                 | 262 ms: 1.34x faster                                                |
| async_tree_none_tg         | 319 ms                                                 | 254 ms: 1.26x faster                                                |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 495 ms: 1.16x faster                                                |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 479 ms: 1.14x faster                                                |
| async_generators           | 433 ms                                                 | 414 ms: 1.05x faster                                                |
| coroutines                 | 22.2 ms                                                | 23.7 ms: 1.07x slower                                               |
| Geometric mean             | (ref)                                                  | 1.21x faster                                                        |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250328-linux-x86_64-brandtbucher-jit_up_10_9-3.14.0a6+-07ab4d7 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 66.1 ms: 1.19x faster                                               |
| pidigits       | 186 ms                                                 | 185 ms: 1.01x faster                                                |
| Geometric mean | (ref)                                                  | 1.06x faster                                                        |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250328-linux-x86_64-brandtbucher-jit_up_10_9-3.14.0a6+-07ab4d7 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_v8       | 26.9 ms                                                | 23.5 ms: 1.14x faster                                               |
| regex_effbot   | 3.77 ms                                                | 3.40 ms: 1.11x faster                                               |
| regex_dna      | 220 ms                                                 | 214 ms: 1.03x faster                                                |
| regex_compile  | 132 ms                                                 | 129 ms: 1.02x faster                                                |
| Geometric mean | (ref)                                                  | 1.07x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250328-linux-x86_64-brandtbucher-jit_up_10_9-3.14.0a6+-07ab4d7 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| tomli_loads          | 2.12 sec                                               | 1.86 sec: 1.14x faster                                              |
| xml_etree_parse      | 154 ms                                                 | 140 ms: 1.10x faster                                                |
| xml_etree_generate   | 86.8 ms                                                | 80.4 ms: 1.08x faster                                               |
| xml_etree_process    | 60.5 ms                                                | 56.8 ms: 1.07x faster                                               |
| xml_etree_iterparse  | 101 ms                                                 | 98.0 ms: 1.03x faster                                               |
| unpickle_pure_python | 213 us                                                 | 212 us: 1.00x faster                                                |
| pickle_pure_python   | 302 us                                                 | 325 us: 1.07x slower                                                |
| json_loads           | 27.2 us                                                | 29.6 us: 1.09x slower                                               |
| json_dumps           | 10.1 ms                                                | 11.7 ms: 1.15x slower                                               |
| Geometric mean       | (ref)                                                  | 1.01x faster                                                        |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250328-linux-x86_64-brandtbucher-jit_up_10_9-3.14.0a6+-07ab4d7 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 12.7 ms                                                | 13.1 ms: 1.04x slower                                               |
| python_startup_no_site | 7.00 ms                                                | 8.21 ms: 1.17x slower                                               |
| Geometric mean         | (ref)                                                  | 1.10x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250328-linux-x86_64-brandtbucher-jit_up_10_9-3.14.0a6+-07ab4d7 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| genshi_text    | 22.6 ms                                                | 21.3 ms: 1.06x faster                                               |
| mako           | 10.7 ms                                                | 11.0 ms: 1.03x slower                                               |
| Geometric mean | (ref)                                                  | 1.01x faster                                                        |

Benchmark hidden because not significant (2): django_template, genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250328-linux-x86_64-brandtbucher-jit_up_10_9-3.14.0a6+-07ab4d7 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 316 ms: 1.46x faster                                                |
| async_tree_io_tg           | 861 ms                                                 | 628 ms: 1.37x faster                                                |
| async_tree_io              | 838 ms                                                 | 619 ms: 1.35x faster                                                |
| async_tree_memoization     | 437 ms                                                 | 323 ms: 1.35x faster                                                |
| deepcopy                   | 354 us                                                 | 262 us: 1.35x faster                                                |
| async_tree_none            | 350 ms                                                 | 262 ms: 1.34x faster                                                |
| deepcopy_memo              | 38.4 us                                                | 28.8 us: 1.33x faster                                               |
| async_tree_none_tg         | 319 ms                                                 | 254 ms: 1.26x faster                                                |
| spectral_norm              | 113 ms                                                 | 91.9 ms: 1.23x faster                                               |
| float                      | 78.7 ms                                                | 66.1 ms: 1.19x faster                                               |
| deepcopy_reduce            | 3.24 us                                                | 2.73 us: 1.19x faster                                               |
| richards_super             | 53.7 ms                                                | 45.6 ms: 1.18x faster                                               |
| scimark_fft                | 367 ms                                                 | 313 ms: 1.17x faster                                                |
| richards                   | 47.5 ms                                                | 40.8 ms: 1.16x faster                                               |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 495 ms: 1.16x faster                                                |
| regex_v8                   | 26.9 ms                                                | 23.5 ms: 1.14x faster                                               |
| tomli_loads                | 2.12 sec                                               | 1.86 sec: 1.14x faster                                              |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 479 ms: 1.14x faster                                                |
| regex_effbot               | 3.77 ms                                                | 3.40 ms: 1.11x faster                                               |
| xml_etree_parse            | 154 ms                                                 | 140 ms: 1.10x faster                                                |
| go                         | 141 ms                                                 | 128 ms: 1.10x faster                                                |
| pylint                     | 312 ms                                                 | 284 ms: 1.10x faster                                                |
| xml_etree_generate         | 86.8 ms                                                | 80.4 ms: 1.08x faster                                               |
| telco                      | 8.40 ms                                                | 7.87 ms: 1.07x faster                                               |
| xml_etree_process          | 60.5 ms                                                | 56.8 ms: 1.07x faster                                               |
| dulwich_log                | 64.6 ms                                                | 60.7 ms: 1.06x faster                                               |
| sqlite_synth               | 2.90 us                                                | 2.73 us: 1.06x faster                                               |
| genshi_text                | 22.6 ms                                                | 21.3 ms: 1.06x faster                                               |
| async_generators           | 433 ms                                                 | 414 ms: 1.05x faster                                                |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.81 ms: 1.05x faster                                               |
| deltablue                  | 3.19 ms                                                | 3.05 ms: 1.05x faster                                               |
| xml_etree_iterparse        | 101 ms                                                 | 98.0 ms: 1.03x faster                                               |
| pathlib                    | 17.4 ms                                                | 16.8 ms: 1.03x faster                                               |
| regex_dna                  | 220 ms                                                 | 214 ms: 1.03x faster                                                |
| regex_compile              | 132 ms                                                 | 129 ms: 1.02x faster                                                |
| thrift                     | 800 us                                                 | 781 us: 1.02x faster                                                |
| pycparser                  | 1.20 sec                                               | 1.17 sec: 1.02x faster                                              |
| mdp                        | 2.54 sec                                               | 2.49 sec: 1.02x faster                                              |
| k_core                     | 2.37 sec                                               | 2.32 sec: 1.02x faster                                              |
| pyflate                    | 470 ms                                                 | 461 ms: 1.02x faster                                                |
| gc_traversal               | 4.90 ms                                                | 4.82 ms: 1.02x faster                                               |
| logging_format             | 6.23 us                                                | 6.17 us: 1.01x faster                                               |
| logging_simple             | 5.65 us                                                | 5.60 us: 1.01x faster                                               |
| bpe_tokeniser              | 4.69 sec                                               | 4.66 sec: 1.01x faster                                              |
| pidigits                   | 186 ms                                                 | 185 ms: 1.01x faster                                                |
| unpickle_pure_python       | 213 us                                                 | 212 us: 1.00x faster                                                |
| generators                 | 28.8 ms                                                | 28.9 ms: 1.00x slower                                               |
| shortest_path              | 487 ms                                                 | 490 ms: 1.01x slower                                                |
| crypto_pyaes               | 74.7 ms                                                | 75.5 ms: 1.01x slower                                               |
| meteor_contest             | 108 ms                                                 | 110 ms: 1.01x slower                                                |
| create_gc_cycles           | 2.45 ms                                                | 2.49 ms: 1.02x slower                                               |
| scimark_lu                 | 114 ms                                                 | 116 ms: 1.02x slower                                                |
| sqlalchemy_declarative     | 133 ms                                                 | 136 ms: 1.02x slower                                                |
| sympy_str                  | 273 ms                                                 | 279 ms: 1.02x slower                                                |
| scimark_monte_carlo        | 66.8 ms                                                | 68.3 ms: 1.02x slower                                               |
| sqlalchemy_imperative      | 16.9 ms                                                | 17.4 ms: 1.03x slower                                               |
| raytrace                   | 262 ms                                                 | 268 ms: 1.03x slower                                                |
| mako                       | 10.7 ms                                                | 11.0 ms: 1.03x slower                                               |
| sympy_integrate            | 19.8 ms                                                | 20.4 ms: 1.03x slower                                               |
| sympy_sum                  | 150 ms                                                 | 155 ms: 1.03x slower                                                |
| chaos                      | 58.0 ms                                                | 60.0 ms: 1.03x slower                                               |
| logging_silent             | 101 ns                                                 | 105 ns: 1.04x slower                                                |
| python_startup             | 12.7 ms                                                | 13.1 ms: 1.04x slower                                               |
| coverage                   | 82.8 ms                                                | 86.5 ms: 1.04x slower                                               |
| docutils                   | 2.58 sec                                               | 2.70 sec: 1.05x slower                                              |
| pprint_pformat             | 1.48 sec                                               | 1.55 sec: 1.05x slower                                              |
| sympy_expand               | 456 ms                                                 | 479 ms: 1.05x slower                                                |
| pprint_safe_repr           | 727 ms                                                 | 769 ms: 1.06x slower                                                |
| nqueens                    | 80.9 ms                                                | 85.8 ms: 1.06x slower                                               |
| coroutines                 | 22.2 ms                                                | 23.7 ms: 1.07x slower                                               |
| pickle_pure_python         | 302 us                                                 | 325 us: 1.07x slower                                                |
| typing_runtime_protocols   | 160 us                                                 | 173 us: 1.08x slower                                                |
| fannkuch                   | 394 ms                                                 | 427 ms: 1.08x slower                                                |
| bench_thread_pool          | 818 us                                                 | 888 us: 1.09x slower                                                |
| json_loads                 | 27.2 us                                                | 29.6 us: 1.09x slower                                               |
| connected_components       | 447 ms                                                 | 494 ms: 1.11x slower                                                |
| many_optionals             | 857 us                                                 | 985 us: 1.15x slower                                                |
| json_dumps                 | 10.1 ms                                                | 11.7 ms: 1.15x slower                                               |
| comprehensions             | 16.5 us                                                | 19.1 us: 1.16x slower                                               |
| hexiom                     | 6.08 ms                                                | 7.10 ms: 1.17x slower                                               |
| python_startup_no_site     | 7.00 ms                                                | 8.21 ms: 1.17x slower                                               |
| subparsers                 | 15.5 ms                                                | 20.9 ms: 1.35x slower                                               |
| bench_mp_pool              | 24.0 ms                                                | 83.1 ms: 3.47x slower                                               |
| Geometric mean             | (ref)                                                  | 1.02x faster                                                        |

Benchmark hidden because not significant (9): scimark_sor, json, sphinx, 2to3, django_template, asyncio_websockets, genshi_xml, html5lib, nbody
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250328-3.14.0a6+-07ab4d7-JIT/bm-20250328-linux-x86_64-brandtbucher-jit_up_10_9-3.14.0a6+-07ab4d7.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.034x faster

# HPT report

- Reliability score: 96.83% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.05x
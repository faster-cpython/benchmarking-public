# Results vs. 3.13.0

- fork: brandtbucher
- ref: jit_nops
- machine: linux-x86_64
- commit hash: 75922b6
- commit date: 2025-06-27
- overall geometric mean: 1.064x faster
- HPT reliability: 99.99%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250627-linux-x86_64-brandtbucher-jit_nops-3.15.0a0-75922b6 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 259 ms: 1.03x faster                                            |
| docutils       | 2.58 sec                                               | 2.63 sec: 1.02x slower                                          |
| html5lib       | 63.4 ms                                                | 61.4 ms: 1.03x faster                                           |
| sphinx         | 1.03 sec                                               | 1.02 sec: 1.02x faster                                          |
| Geometric mean | (ref)                                                  | 1.01x faster                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250627-linux-x86_64-brandtbucher-jit_nops-3.15.0a0-75922b6 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 310 ms: 1.49x faster                                            |
| async_tree_io              | 838 ms                                                 | 600 ms: 1.40x faster                                            |
| async_tree_memoization     | 437 ms                                                 | 314 ms: 1.39x faster                                            |
| async_tree_io_tg           | 861 ms                                                 | 636 ms: 1.35x faster                                            |
| async_tree_none            | 350 ms                                                 | 263 ms: 1.33x faster                                            |
| async_tree_none_tg         | 319 ms                                                 | 248 ms: 1.29x faster                                            |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 499 ms: 1.15x faster                                            |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 489 ms: 1.11x faster                                            |
| async_generators           | 433 ms                                                 | 427 ms: 1.01x faster                                            |
| asyncio_websockets         | 551 ms                                                 | 553 ms: 1.00x slower                                            |
| coroutines                 | 22.2 ms                                                | 25.0 ms: 1.13x slower                                           |
| Geometric mean             | (ref)                                                  | 1.20x faster                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250627-linux-x86_64-brandtbucher-jit_nops-3.15.0a0-75922b6 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| float          | 78.7 ms                                                | 65.7 ms: 1.20x faster                                           |
| pidigits       | 186 ms                                                 | 188 ms: 1.01x slower                                            |
| nbody          | 87.7 ms                                                | 98.8 ms: 1.13x slower                                           |
| Geometric mean | (ref)                                                  | 1.02x faster                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250627-linux-x86_64-brandtbucher-jit_nops-3.15.0a0-75922b6 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                | 3.25 ms: 1.16x faster                                           |
| regex_v8       | 26.9 ms                                                | 23.7 ms: 1.13x faster                                           |
| regex_compile  | 132 ms                                                 | 127 ms: 1.04x faster                                            |
| regex_dna      | 220 ms                                                 | 213 ms: 1.03x faster                                            |
| Geometric mean | (ref)                                                  | 1.09x faster                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250627-linux-x86_64-brandtbucher-jit_nops-3.15.0a0-75922b6 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| tomli_loads          | 2.12 sec                                               | 1.82 sec: 1.16x faster                                          |
| unpickle_pure_python | 213 us                                                 | 193 us: 1.10x faster                                            |
| xml_etree_process    | 60.5 ms                                                | 55.3 ms: 1.09x faster                                           |
| xml_etree_parse      | 154 ms                                                 | 142 ms: 1.09x faster                                            |
| xml_etree_generate   | 86.8 ms                                                | 79.8 ms: 1.09x faster                                           |
| xml_etree_iterparse  | 101 ms                                                 | 98.3 ms: 1.03x faster                                           |
| json_loads           | 27.2 us                                                | 28.2 us: 1.04x slower                                           |
| pickle_pure_python   | 302 us                                                 | 320 us: 1.06x slower                                            |
| json_dumps           | 10.1 ms                                                | 11.0 ms: 1.08x slower                                           |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250627-linux-x86_64-brandtbucher-jit_nops-3.15.0a0-75922b6 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| python_startup         | 12.7 ms                                                | 12.2 ms: 1.03x faster                                           |
| python_startup_no_site | 7.00 ms                                                | 6.98 ms: 1.00x faster                                           |
| Geometric mean         | (ref)                                                  | 1.02x faster                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250627-linux-x86_64-brandtbucher-jit_nops-3.15.0a0-75922b6 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| genshi_text     | 22.6 ms                                                | 21.6 ms: 1.05x faster                                           |
| mako            | 10.7 ms                                                | 10.6 ms: 1.00x faster                                           |
| genshi_xml      | 50.5 ms                                                | 50.7 ms: 1.00x slower                                           |
| django_template | 31.7 ms                                                | 32.1 ms: 1.01x slower                                           |
| Geometric mean  | (ref)                                                  | 1.01x faster                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250627-linux-x86_64-brandtbucher-jit_nops-3.15.0a0-75922b6 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| mdp                        | 2.54 sec                                               | 1.24 sec: 2.05x faster                                          |
| async_tree_memoization_tg  | 463 ms                                                 | 310 ms: 1.49x faster                                            |
| richards                   | 47.5 ms                                                | 32.2 ms: 1.48x faster                                           |
| richards_super             | 53.7 ms                                                | 37.8 ms: 1.42x faster                                           |
| async_tree_io              | 838 ms                                                 | 600 ms: 1.40x faster                                            |
| async_tree_memoization     | 437 ms                                                 | 314 ms: 1.39x faster                                            |
| deepcopy                   | 354 us                                                 | 257 us: 1.38x faster                                            |
| async_tree_io_tg           | 861 ms                                                 | 636 ms: 1.35x faster                                            |
| async_tree_none            | 350 ms                                                 | 263 ms: 1.33x faster                                            |
| deepcopy_memo              | 38.4 us                                                | 29.4 us: 1.31x faster                                           |
| async_tree_none_tg         | 319 ms                                                 | 248 ms: 1.29x faster                                            |
| spectral_norm              | 113 ms                                                 | 91.9 ms: 1.23x faster                                           |
| go                         | 141 ms                                                 | 115 ms: 1.22x faster                                            |
| deepcopy_reduce            | 3.24 us                                                | 2.70 us: 1.20x faster                                           |
| float                      | 78.7 ms                                                | 65.7 ms: 1.20x faster                                           |
| scimark_fft                | 367 ms                                                 | 313 ms: 1.17x faster                                            |
| tomli_loads                | 2.12 sec                                               | 1.82 sec: 1.16x faster                                          |
| regex_effbot               | 3.77 ms                                                | 3.25 ms: 1.16x faster                                           |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 499 ms: 1.15x faster                                            |
| pyflate                    | 470 ms                                                 | 410 ms: 1.15x faster                                            |
| regex_v8                   | 26.9 ms                                                | 23.7 ms: 1.13x faster                                           |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 489 ms: 1.11x faster                                            |
| unpickle_pure_python       | 213 us                                                 | 193 us: 1.10x faster                                            |
| pylint                     | 312 ms                                                 | 283 ms: 1.10x faster                                            |
| xml_etree_process          | 60.5 ms                                                | 55.3 ms: 1.09x faster                                           |
| telco                      | 8.40 ms                                                | 7.70 ms: 1.09x faster                                           |
| dulwich_log                | 64.6 ms                                                | 59.3 ms: 1.09x faster                                           |
| xml_etree_parse            | 154 ms                                                 | 142 ms: 1.09x faster                                            |
| xml_etree_generate         | 86.8 ms                                                | 79.8 ms: 1.09x faster                                           |
| pycparser                  | 1.20 sec                                               | 1.11 sec: 1.08x faster                                          |
| bpe_tokeniser              | 4.69 sec                                               | 4.33 sec: 1.08x faster                                          |
| deltablue                  | 3.19 ms                                                | 3.04 ms: 1.05x faster                                           |
| genshi_text                | 22.6 ms                                                | 21.6 ms: 1.05x faster                                           |
| regex_compile              | 132 ms                                                 | 127 ms: 1.04x faster                                            |
| sqlite_synth               | 2.90 us                                                | 2.79 us: 1.04x faster                                           |
| k_core                     | 2.37 sec                                               | 2.28 sec: 1.04x faster                                          |
| python_startup             | 12.7 ms                                                | 12.2 ms: 1.03x faster                                           |
| html5lib                   | 63.4 ms                                                | 61.4 ms: 1.03x faster                                           |
| regex_dna                  | 220 ms                                                 | 213 ms: 1.03x faster                                            |
| meteor_contest             | 108 ms                                                 | 105 ms: 1.03x faster                                            |
| xml_etree_iterparse        | 101 ms                                                 | 98.3 ms: 1.03x faster                                           |
| thrift                     | 800 us                                                 | 779 us: 1.03x faster                                            |
| sympy_integrate            | 19.8 ms                                                | 19.3 ms: 1.03x faster                                           |
| 2to3                       | 266 ms                                                 | 259 ms: 1.03x faster                                            |
| scimark_sor                | 122 ms                                                 | 119 ms: 1.03x faster                                            |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.92 ms: 1.02x faster                                           |
| sphinx                     | 1.03 sec                                               | 1.02 sec: 1.02x faster                                          |
| json                       | 5.32 ms                                                | 5.24 ms: 1.02x faster                                           |
| sympy_sum                  | 150 ms                                                 | 148 ms: 1.02x faster                                            |
| async_generators           | 433 ms                                                 | 427 ms: 1.01x faster                                            |
| scimark_monte_carlo        | 66.8 ms                                                | 65.9 ms: 1.01x faster                                           |
| pathlib                    | 17.4 ms                                                | 17.2 ms: 1.01x faster                                           |
| comprehensions             | 16.5 us                                                | 16.4 us: 1.01x faster                                           |
| mako                       | 10.7 ms                                                | 10.6 ms: 1.00x faster                                           |
| python_startup_no_site     | 7.00 ms                                                | 6.98 ms: 1.00x faster                                           |
| asyncio_websockets         | 551 ms                                                 | 553 ms: 1.00x slower                                            |
| genshi_xml                 | 50.5 ms                                                | 50.7 ms: 1.00x slower                                           |
| fannkuch                   | 394 ms                                                 | 397 ms: 1.01x slower                                            |
| pidigits                   | 186 ms                                                 | 188 ms: 1.01x slower                                            |
| logging_silent             | 101 ns                                                 | 102 ns: 1.01x slower                                            |
| django_template            | 31.7 ms                                                | 32.1 ms: 1.01x slower                                           |
| logging_simple             | 5.65 us                                                | 5.73 us: 1.01x slower                                           |
| nqueens                    | 80.9 ms                                                | 82.0 ms: 1.01x slower                                           |
| shortest_path              | 487 ms                                                 | 495 ms: 1.02x slower                                            |
| docutils                   | 2.58 sec                                               | 2.63 sec: 1.02x slower                                          |
| hexiom                     | 6.08 ms                                                | 6.19 ms: 1.02x slower                                           |
| gc_traversal               | 4.90 ms                                                | 5.02 ms: 1.03x slower                                           |
| connected_components       | 447 ms                                                 | 458 ms: 1.03x slower                                            |
| sympy_expand               | 456 ms                                                 | 469 ms: 1.03x slower                                            |
| logging_format             | 6.23 us                                                | 6.43 us: 1.03x slower                                           |
| scimark_lu                 | 114 ms                                                 | 118 ms: 1.03x slower                                            |
| json_loads                 | 27.2 us                                                | 28.2 us: 1.04x slower                                           |
| raytrace                   | 262 ms                                                 | 273 ms: 1.04x slower                                            |
| coverage                   | 82.8 ms                                                | 87.2 ms: 1.05x slower                                           |
| generators                 | 28.8 ms                                                | 30.3 ms: 1.05x slower                                           |
| chaos                      | 58.0 ms                                                | 61.3 ms: 1.06x slower                                           |
| typing_runtime_protocols   | 160 us                                                 | 169 us: 1.06x slower                                            |
| pickle_pure_python         | 302 us                                                 | 320 us: 1.06x slower                                            |
| create_gc_cycles           | 2.45 ms                                                | 2.61 ms: 1.07x slower                                           |
| json_dumps                 | 10.1 ms                                                | 11.0 ms: 1.08x slower                                           |
| coroutines                 | 22.2 ms                                                | 25.0 ms: 1.13x slower                                           |
| nbody                      | 87.7 ms                                                | 98.8 ms: 1.13x slower                                           |
| many_optionals             | 857 us                                                 | 972 us: 1.14x slower                                            |
| subparsers                 | 15.5 ms                                                | 23.8 ms: 1.54x slower                                           |
| Geometric mean             | (ref)                                                  | 1.06x faster                                                    |

Benchmark hidden because not significant (5): djangocms, pprint_safe_repr, sympy_str, crypto_pyaes, pprint_pformat
Ignored benchmarks (12) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: bench_mp_pool, bench_thread_pool, chameleon, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250627-3.15.0a0-75922b6-JIT/bm-20250627-linux-x86_64-brandtbucher-jit_nops-3.15.0a0-75922b6.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.064x faster

# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.07x
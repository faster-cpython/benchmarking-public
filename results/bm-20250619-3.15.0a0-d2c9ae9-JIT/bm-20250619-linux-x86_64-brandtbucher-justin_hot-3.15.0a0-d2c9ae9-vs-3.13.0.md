# Results vs. 3.13.0

- fork: brandtbucher
- ref: justin_hot
- machine: linux-x86_64
- commit hash: d2c9ae9
- commit date: 2025-06-19
- overall geometric mean: 1.046x faster
- HPT reliability: 98.17%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250619-linux-x86_64-brandtbucher-justin_hot-3.15.0a0-d2c9ae9 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 260 ms: 1.02x faster                                              |
| docutils       | 2.58 sec                                               | 2.65 sec: 1.03x slower                                            |
| html5lib       | 63.4 ms                                                | 62.3 ms: 1.02x faster                                             |
| Geometric mean | (ref)                                                  | 1.01x faster                                                      |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250619-linux-x86_64-brandtbucher-justin_hot-3.15.0a0-d2c9ae9 |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 316 ms: 1.47x faster                                              |
| async_tree_io_tg           | 861 ms                                                 | 614 ms: 1.40x faster                                              |
| async_tree_io              | 838 ms                                                 | 599 ms: 1.40x faster                                              |
| async_tree_memoization     | 437 ms                                                 | 314 ms: 1.39x faster                                              |
| async_tree_none            | 350 ms                                                 | 262 ms: 1.33x faster                                              |
| async_tree_none_tg         | 319 ms                                                 | 249 ms: 1.28x faster                                              |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 498 ms: 1.15x faster                                              |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 490 ms: 1.11x faster                                              |
| asyncio_websockets         | 551 ms                                                 | 554 ms: 1.00x slower                                              |
| coroutines                 | 22.2 ms                                                | 24.3 ms: 1.09x slower                                             |
| Geometric mean             | (ref)                                                  | 1.21x faster                                                      |

Benchmark hidden because not significant (1): async_generators

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250619-linux-x86_64-brandtbucher-justin_hot-3.15.0a0-d2c9ae9 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| float          | 78.7 ms                                                | 66.3 ms: 1.19x faster                                             |
| pidigits       | 186 ms                                                 | 187 ms: 1.00x slower                                              |
| nbody          | 87.7 ms                                                | 95.0 ms: 1.08x slower                                             |
| Geometric mean | (ref)                                                  | 1.03x faster                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250619-linux-x86_64-brandtbucher-justin_hot-3.15.0a0-d2c9ae9 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| regex_v8       | 26.9 ms                                                | 22.8 ms: 1.18x faster                                             |
| regex_effbot   | 3.77 ms                                                | 3.32 ms: 1.13x faster                                             |
| regex_compile  | 132 ms                                                 | 128 ms: 1.03x faster                                              |
| Geometric mean | (ref)                                                  | 1.09x faster                                                      |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250619-linux-x86_64-brandtbucher-justin_hot-3.15.0a0-d2c9ae9 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| tomli_loads          | 2.12 sec                                               | 1.92 sec: 1.10x faster                                            |
| xml_etree_parse      | 154 ms                                                 | 140 ms: 1.10x faster                                              |
| xml_etree_process    | 60.5 ms                                                | 56.2 ms: 1.08x faster                                             |
| xml_etree_generate   | 86.8 ms                                                | 80.8 ms: 1.07x faster                                             |
| unpickle_pure_python | 213 us                                                 | 205 us: 1.04x faster                                              |
| xml_etree_iterparse  | 101 ms                                                 | 98.3 ms: 1.03x faster                                             |
| json_loads           | 27.2 us                                                | 28.8 us: 1.06x slower                                             |
| pickle_pure_python   | 302 us                                                 | 325 us: 1.07x slower                                              |
| json_dumps           | 10.1 ms                                                | 11.0 ms: 1.09x slower                                             |
| Geometric mean       | (ref)                                                  | 1.02x faster                                                      |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250619-linux-x86_64-brandtbucher-justin_hot-3.15.0a0-d2c9ae9 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| python_startup         | 12.7 ms                                                | 12.2 ms: 1.04x faster                                             |
| python_startup_no_site | 7.00 ms                                                | 6.96 ms: 1.01x faster                                             |
| Geometric mean         | (ref)                                                  | 1.02x faster                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250619-linux-x86_64-brandtbucher-justin_hot-3.15.0a0-d2c9ae9 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| genshi_text     | 22.6 ms                                                | 21.1 ms: 1.07x faster                                             |
| mako            | 10.7 ms                                                | 10.8 ms: 1.01x slower                                             |
| django_template | 31.7 ms                                                | 32.7 ms: 1.03x slower                                             |
| Geometric mean  | (ref)                                                  | 1.01x faster                                                      |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250619-linux-x86_64-brandtbucher-justin_hot-3.15.0a0-d2c9ae9 |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| mdp                        | 2.54 sec                                               | 1.25 sec: 2.04x faster                                            |
| async_tree_memoization_tg  | 463 ms                                                 | 316 ms: 1.47x faster                                              |
| async_tree_io_tg           | 861 ms                                                 | 614 ms: 1.40x faster                                              |
| async_tree_io              | 838 ms                                                 | 599 ms: 1.40x faster                                              |
| async_tree_memoization     | 437 ms                                                 | 314 ms: 1.39x faster                                              |
| richards                   | 47.5 ms                                                | 34.2 ms: 1.39x faster                                             |
| richards_super             | 53.7 ms                                                | 39.3 ms: 1.37x faster                                             |
| deepcopy                   | 354 us                                                 | 260 us: 1.36x faster                                              |
| async_tree_none            | 350 ms                                                 | 262 ms: 1.33x faster                                              |
| deepcopy_memo              | 38.4 us                                                | 29.8 us: 1.29x faster                                             |
| async_tree_none_tg         | 319 ms                                                 | 249 ms: 1.28x faster                                              |
| deepcopy_reduce            | 3.24 us                                                | 2.72 us: 1.19x faster                                             |
| float                      | 78.7 ms                                                | 66.3 ms: 1.19x faster                                             |
| regex_v8                   | 26.9 ms                                                | 22.8 ms: 1.18x faster                                             |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 498 ms: 1.15x faster                                              |
| go                         | 141 ms                                                 | 123 ms: 1.14x faster                                              |
| regex_effbot               | 3.77 ms                                                | 3.32 ms: 1.13x faster                                             |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 490 ms: 1.11x faster                                              |
| tomli_loads                | 2.12 sec                                               | 1.92 sec: 1.10x faster                                            |
| pylint                     | 312 ms                                                 | 283 ms: 1.10x faster                                              |
| xml_etree_parse            | 154 ms                                                 | 140 ms: 1.10x faster                                              |
| scimark_fft                | 367 ms                                                 | 336 ms: 1.09x faster                                              |
| pyflate                    | 470 ms                                                 | 432 ms: 1.09x faster                                              |
| dulwich_log                | 64.6 ms                                                | 59.6 ms: 1.08x faster                                             |
| spectral_norm              | 113 ms                                                 | 105 ms: 1.08x faster                                              |
| telco                      | 8.40 ms                                                | 7.80 ms: 1.08x faster                                             |
| xml_etree_process          | 60.5 ms                                                | 56.2 ms: 1.08x faster                                             |
| xml_etree_generate         | 86.8 ms                                                | 80.8 ms: 1.07x faster                                             |
| pycparser                  | 1.20 sec                                               | 1.12 sec: 1.07x faster                                            |
| genshi_text                | 22.6 ms                                                | 21.1 ms: 1.07x faster                                             |
| bpe_tokeniser              | 4.69 sec                                               | 4.43 sec: 1.06x faster                                            |
| unpickle_pure_python       | 213 us                                                 | 205 us: 1.04x faster                                              |
| sqlite_synth               | 2.90 us                                                | 2.79 us: 1.04x faster                                             |
| python_startup             | 12.7 ms                                                | 12.2 ms: 1.04x faster                                             |
| k_core                     | 2.37 sec                                               | 2.29 sec: 1.03x faster                                            |
| regex_compile              | 132 ms                                                 | 128 ms: 1.03x faster                                              |
| xml_etree_iterparse        | 101 ms                                                 | 98.3 ms: 1.03x faster                                             |
| pathlib                    | 17.4 ms                                                | 16.9 ms: 1.03x faster                                             |
| thrift                     | 800 us                                                 | 780 us: 1.03x faster                                              |
| 2to3                       | 266 ms                                                 | 260 ms: 1.02x faster                                              |
| meteor_contest             | 108 ms                                                 | 106 ms: 1.02x faster                                              |
| html5lib                   | 63.4 ms                                                | 62.3 ms: 1.02x faster                                             |
| sympy_integrate            | 19.8 ms                                                | 19.5 ms: 1.02x faster                                             |
| scimark_sor                | 122 ms                                                 | 121 ms: 1.01x faster                                              |
| python_startup_no_site     | 7.00 ms                                                | 6.96 ms: 1.01x faster                                             |
| pidigits                   | 186 ms                                                 | 187 ms: 1.00x slower                                              |
| sympy_sum                  | 150 ms                                                 | 151 ms: 1.00x slower                                              |
| asyncio_websockets         | 551 ms                                                 | 554 ms: 1.00x slower                                              |
| gc_traversal               | 4.90 ms                                                | 4.93 ms: 1.01x slower                                             |
| deltablue                  | 3.19 ms                                                | 3.22 ms: 1.01x slower                                             |
| mako                       | 10.7 ms                                                | 10.8 ms: 1.01x slower                                             |
| crypto_pyaes               | 74.7 ms                                                | 76.0 ms: 1.02x slower                                             |
| shortest_path              | 487 ms                                                 | 498 ms: 1.02x slower                                              |
| docutils                   | 2.58 sec                                               | 2.65 sec: 1.03x slower                                            |
| sympy_expand               | 456 ms                                                 | 469 ms: 1.03x slower                                              |
| django_template            | 31.7 ms                                                | 32.7 ms: 1.03x slower                                             |
| connected_components       | 447 ms                                                 | 462 ms: 1.03x slower                                              |
| scimark_lu                 | 114 ms                                                 | 119 ms: 1.04x slower                                              |
| nqueens                    | 80.9 ms                                                | 84.0 ms: 1.04x slower                                             |
| comprehensions             | 16.5 us                                                | 17.4 us: 1.06x slower                                             |
| fannkuch                   | 394 ms                                                 | 416 ms: 1.06x slower                                              |
| create_gc_cycles           | 2.45 ms                                                | 2.59 ms: 1.06x slower                                             |
| json_loads                 | 27.2 us                                                | 28.8 us: 1.06x slower                                             |
| generators                 | 28.8 ms                                                | 30.5 ms: 1.06x slower                                             |
| coverage                   | 82.8 ms                                                | 88.1 ms: 1.06x slower                                             |
| raytrace                   | 262 ms                                                 | 278 ms: 1.06x slower                                              |
| typing_runtime_protocols   | 160 us                                                 | 171 us: 1.07x slower                                              |
| hexiom                     | 6.08 ms                                                | 6.53 ms: 1.07x slower                                             |
| pickle_pure_python         | 302 us                                                 | 325 us: 1.07x slower                                              |
| chaos                      | 58.0 ms                                                | 62.4 ms: 1.08x slower                                             |
| nbody                      | 87.7 ms                                                | 95.0 ms: 1.08x slower                                             |
| json_dumps                 | 10.1 ms                                                | 11.0 ms: 1.09x slower                                             |
| coroutines                 | 22.2 ms                                                | 24.3 ms: 1.09x slower                                             |
| logging_simple             | 5.65 us                                                | 6.21 us: 1.10x slower                                             |
| logging_format             | 6.23 us                                                | 6.89 us: 1.11x slower                                             |
| many_optionals             | 857 us                                                 | 983 us: 1.15x slower                                              |
| pprint_safe_repr           | 727 ms                                                 | 839 ms: 1.15x slower                                              |
| pprint_pformat             | 1.48 sec                                               | 1.73 sec: 1.17x slower                                            |
| subparsers                 | 15.5 ms                                                | 23.5 ms: 1.52x slower                                             |
| logging_silent             | 101 ns                                                 | 474 ns: 4.69x slower                                              |
| Geometric mean             | (ref)                                                  | 1.03x faster                                                      |

Benchmark hidden because not significant (9): sphinx, json, regex_dna, genshi_xml, async_generators, sympy_str, scimark_sparse_mat_mult, scimark_monte_carlo, djangocms
Ignored benchmarks (12) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: bench_mp_pool, bench_thread_pool, chameleon, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250619-3.15.0a0-d2c9ae9-JIT/bm-20250619-linux-x86_64-brandtbucher-justin_hot-3.15.0a0-d2c9ae9.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.046x faster

# HPT report

- Reliability score: 98.17% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.07x
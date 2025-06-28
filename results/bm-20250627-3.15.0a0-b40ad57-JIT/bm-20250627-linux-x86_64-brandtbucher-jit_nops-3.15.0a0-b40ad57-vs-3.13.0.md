# Results vs. 3.13.0

- fork: brandtbucher
- ref: jit_nops
- machine: linux-x86_64
- commit hash: b40ad57
- commit date: 2025-06-27
- overall geometric mean: 1.059x faster
- HPT reliability: 99.96%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250627-linux-x86_64-brandtbucher-jit_nops-3.15.0a0-b40ad57 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 259 ms: 1.03x faster                                            |
| docutils       | 2.58 sec                                               | 2.64 sec: 1.02x slower                                          |
| html5lib       | 63.4 ms                                                | 61.2 ms: 1.04x faster                                           |
| sphinx         | 1.03 sec                                               | 1.01 sec: 1.02x faster                                          |
| Geometric mean | (ref)                                                  | 1.01x faster                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250627-linux-x86_64-brandtbucher-jit_nops-3.15.0a0-b40ad57 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 312 ms: 1.48x faster                                            |
| async_tree_io              | 838 ms                                                 | 601 ms: 1.39x faster                                            |
| async_tree_memoization     | 437 ms                                                 | 314 ms: 1.39x faster                                            |
| async_tree_io_tg           | 861 ms                                                 | 639 ms: 1.35x faster                                            |
| async_tree_none            | 350 ms                                                 | 263 ms: 1.33x faster                                            |
| async_tree_none_tg         | 319 ms                                                 | 250 ms: 1.28x faster                                            |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 496 ms: 1.16x faster                                            |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 490 ms: 1.11x faster                                            |
| async_generators           | 433 ms                                                 | 429 ms: 1.01x faster                                            |
| coroutines                 | 22.2 ms                                                | 24.7 ms: 1.11x slower                                           |
| Geometric mean             | (ref)                                                  | 1.20x faster                                                    |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250627-linux-x86_64-brandtbucher-jit_nops-3.15.0a0-b40ad57 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| float          | 78.7 ms                                                | 66.1 ms: 1.19x faster                                           |
| pidigits       | 186 ms                                                 | 188 ms: 1.01x slower                                            |
| nbody          | 87.7 ms                                                | 96.9 ms: 1.11x slower                                           |
| Geometric mean | (ref)                                                  | 1.02x faster                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250627-linux-x86_64-brandtbucher-jit_nops-3.15.0a0-b40ad57 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                | 3.25 ms: 1.16x faster                                           |
| regex_v8       | 26.9 ms                                                | 23.2 ms: 1.16x faster                                           |
| regex_dna      | 220 ms                                                 | 211 ms: 1.04x faster                                            |
| regex_compile  | 132 ms                                                 | 127 ms: 1.04x faster                                            |
| Geometric mean | (ref)                                                  | 1.10x faster                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250627-linux-x86_64-brandtbucher-jit_nops-3.15.0a0-b40ad57 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| tomli_loads          | 2.12 sec                                               | 1.85 sec: 1.14x faster                                          |
| xml_etree_parse      | 154 ms                                                 | 141 ms: 1.10x faster                                            |
| xml_etree_generate   | 86.8 ms                                                | 80.5 ms: 1.08x faster                                           |
| xml_etree_process    | 60.5 ms                                                | 56.3 ms: 1.08x faster                                           |
| unpickle_pure_python | 213 us                                                 | 201 us: 1.06x faster                                            |
| xml_etree_iterparse  | 101 ms                                                 | 99.0 ms: 1.02x faster                                           |
| json_loads           | 27.2 us                                                | 28.2 us: 1.04x slower                                           |
| json_dumps           | 10.1 ms                                                | 11.0 ms: 1.08x slower                                           |
| pickle_pure_python   | 302 us                                                 | 328 us: 1.08x slower                                            |
| Geometric mean       | (ref)                                                  | 1.03x faster                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250627-linux-x86_64-brandtbucher-jit_nops-3.15.0a0-b40ad57 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| python_startup         | 12.7 ms                                                | 12.2 ms: 1.04x faster                                           |
| python_startup_no_site | 7.00 ms                                                | 6.93 ms: 1.01x faster                                           |
| Geometric mean         | (ref)                                                  | 1.03x faster                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250627-linux-x86_64-brandtbucher-jit_nops-3.15.0a0-b40ad57 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| genshi_text     | 22.6 ms                                                | 21.6 ms: 1.05x faster                                           |
| mako            | 10.7 ms                                                | 10.8 ms: 1.01x slower                                           |
| genshi_xml      | 50.5 ms                                                | 51.3 ms: 1.02x slower                                           |
| django_template | 31.7 ms                                                | 32.8 ms: 1.03x slower                                           |
| Geometric mean  | (ref)                                                  | 1.00x slower                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250627-linux-x86_64-brandtbucher-jit_nops-3.15.0a0-b40ad57 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| mdp                        | 2.54 sec                                               | 1.24 sec: 2.06x faster                                          |
| async_tree_memoization_tg  | 463 ms                                                 | 312 ms: 1.48x faster                                            |
| richards                   | 47.5 ms                                                | 33.3 ms: 1.43x faster                                           |
| richards_super             | 53.7 ms                                                | 38.5 ms: 1.40x faster                                           |
| async_tree_io              | 838 ms                                                 | 601 ms: 1.39x faster                                            |
| async_tree_memoization     | 437 ms                                                 | 314 ms: 1.39x faster                                            |
| deepcopy                   | 354 us                                                 | 256 us: 1.38x faster                                            |
| async_tree_io_tg           | 861 ms                                                 | 639 ms: 1.35x faster                                            |
| async_tree_none            | 350 ms                                                 | 263 ms: 1.33x faster                                            |
| deepcopy_memo              | 38.4 us                                                | 29.2 us: 1.31x faster                                           |
| async_tree_none_tg         | 319 ms                                                 | 250 ms: 1.28x faster                                            |
| spectral_norm              | 113 ms                                                 | 93.6 ms: 1.21x faster                                           |
| deepcopy_reduce            | 3.24 us                                                | 2.69 us: 1.21x faster                                           |
| go                         | 141 ms                                                 | 118 ms: 1.19x faster                                            |
| float                      | 78.7 ms                                                | 66.1 ms: 1.19x faster                                           |
| regex_effbot               | 3.77 ms                                                | 3.25 ms: 1.16x faster                                           |
| regex_v8                   | 26.9 ms                                                | 23.2 ms: 1.16x faster                                           |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 496 ms: 1.16x faster                                            |
| tomli_loads                | 2.12 sec                                               | 1.85 sec: 1.14x faster                                          |
| scimark_fft                | 367 ms                                                 | 324 ms: 1.13x faster                                            |
| pyflate                    | 470 ms                                                 | 416 ms: 1.13x faster                                            |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 490 ms: 1.11x faster                                            |
| pylint                     | 312 ms                                                 | 282 ms: 1.11x faster                                            |
| xml_etree_parse            | 154 ms                                                 | 141 ms: 1.10x faster                                            |
| dulwich_log                | 64.6 ms                                                | 59.3 ms: 1.09x faster                                           |
| pycparser                  | 1.20 sec                                               | 1.11 sec: 1.08x faster                                          |
| telco                      | 8.40 ms                                                | 7.77 ms: 1.08x faster                                           |
| xml_etree_generate         | 86.8 ms                                                | 80.5 ms: 1.08x faster                                           |
| xml_etree_process          | 60.5 ms                                                | 56.3 ms: 1.08x faster                                           |
| bpe_tokeniser              | 4.69 sec                                               | 4.40 sec: 1.06x faster                                          |
| unpickle_pure_python       | 213 us                                                 | 201 us: 1.06x faster                                            |
| genshi_text                | 22.6 ms                                                | 21.6 ms: 1.05x faster                                           |
| regex_dna                  | 220 ms                                                 | 211 ms: 1.04x faster                                            |
| python_startup             | 12.7 ms                                                | 12.2 ms: 1.04x faster                                           |
| regex_compile              | 132 ms                                                 | 127 ms: 1.04x faster                                            |
| html5lib                   | 63.4 ms                                                | 61.2 ms: 1.04x faster                                           |
| k_core                     | 2.37 sec                                               | 2.29 sec: 1.04x faster                                          |
| sqlite_synth               | 2.90 us                                                | 2.80 us: 1.03x faster                                           |
| scimark_sor                | 122 ms                                                 | 119 ms: 1.03x faster                                            |
| thrift                     | 800 us                                                 | 780 us: 1.03x faster                                            |
| 2to3                       | 266 ms                                                 | 259 ms: 1.03x faster                                            |
| deltablue                  | 3.19 ms                                                | 3.12 ms: 1.02x faster                                           |
| sympy_integrate            | 19.8 ms                                                | 19.3 ms: 1.02x faster                                           |
| xml_etree_iterparse        | 101 ms                                                 | 99.0 ms: 1.02x faster                                           |
| pathlib                    | 17.4 ms                                                | 17.0 ms: 1.02x faster                                           |
| json                       | 5.32 ms                                                | 5.23 ms: 1.02x faster                                           |
| meteor_contest             | 108 ms                                                 | 106 ms: 1.02x faster                                            |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.95 ms: 1.02x faster                                           |
| sphinx                     | 1.03 sec                                               | 1.01 sec: 1.02x faster                                          |
| scimark_monte_carlo        | 66.8 ms                                                | 65.8 ms: 1.02x faster                                           |
| python_startup_no_site     | 7.00 ms                                                | 6.93 ms: 1.01x faster                                           |
| async_generators           | 433 ms                                                 | 429 ms: 1.01x faster                                            |
| sympy_sum                  | 150 ms                                                 | 150 ms: 1.01x faster                                            |
| logging_format             | 6.23 us                                                | 6.28 us: 1.01x slower                                           |
| mako                       | 10.7 ms                                                | 10.8 ms: 1.01x slower                                           |
| pidigits                   | 186 ms                                                 | 188 ms: 1.01x slower                                            |
| gc_traversal               | 4.90 ms                                                | 4.96 ms: 1.01x slower                                           |
| crypto_pyaes               | 74.7 ms                                                | 75.7 ms: 1.01x slower                                           |
| genshi_xml                 | 50.5 ms                                                | 51.3 ms: 1.02x slower                                           |
| docutils                   | 2.58 sec                                               | 2.64 sec: 1.02x slower                                          |
| sympy_expand               | 456 ms                                                 | 467 ms: 1.02x slower                                            |
| comprehensions             | 16.5 us                                                | 17.0 us: 1.03x slower                                           |
| connected_components       | 447 ms                                                 | 460 ms: 1.03x slower                                            |
| django_template            | 31.7 ms                                                | 32.8 ms: 1.03x slower                                           |
| shortest_path              | 487 ms                                                 | 505 ms: 1.04x slower                                            |
| json_loads                 | 27.2 us                                                | 28.2 us: 1.04x slower                                           |
| nqueens                    | 80.9 ms                                                | 84.0 ms: 1.04x slower                                           |
| hexiom                     | 6.08 ms                                                | 6.32 ms: 1.04x slower                                           |
| typing_runtime_protocols   | 160 us                                                 | 167 us: 1.04x slower                                            |
| raytrace                   | 262 ms                                                 | 273 ms: 1.04x slower                                            |
| scimark_lu                 | 114 ms                                                 | 120 ms: 1.05x slower                                            |
| chaos                      | 58.0 ms                                                | 60.9 ms: 1.05x slower                                           |
| create_gc_cycles           | 2.45 ms                                                | 2.58 ms: 1.05x slower                                           |
| fannkuch                   | 394 ms                                                 | 414 ms: 1.05x slower                                            |
| coverage                   | 82.8 ms                                                | 87.8 ms: 1.06x slower                                           |
| json_dumps                 | 10.1 ms                                                | 11.0 ms: 1.08x slower                                           |
| pickle_pure_python         | 302 us                                                 | 328 us: 1.08x slower                                            |
| nbody                      | 87.7 ms                                                | 96.9 ms: 1.11x slower                                           |
| coroutines                 | 22.2 ms                                                | 24.7 ms: 1.11x slower                                           |
| generators                 | 28.8 ms                                                | 32.0 ms: 1.11x slower                                           |
| many_optionals             | 857 us                                                 | 973 us: 1.14x slower                                            |
| subparsers                 | 15.5 ms                                                | 23.8 ms: 1.54x slower                                           |
| Geometric mean             | (ref)                                                  | 1.06x faster                                                    |

Benchmark hidden because not significant (7): pprint_safe_repr, sympy_str, logging_simple, asyncio_websockets, logging_silent, pprint_pformat, djangocms
Ignored benchmarks (12) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: bench_mp_pool, bench_thread_pool, chameleon, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250627-3.15.0a0-b40ad57-JIT/bm-20250627-linux-x86_64-brandtbucher-jit_nops-3.15.0a0-b40ad57.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.059x faster

# HPT report

- Reliability score: 99.96% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.07x
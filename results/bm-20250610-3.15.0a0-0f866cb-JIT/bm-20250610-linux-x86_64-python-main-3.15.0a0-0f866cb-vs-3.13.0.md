# Results vs. 3.13.0

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: 0f866cb
- commit date: 2025-06-10
- overall geometric mean: 1.033x slower
- HPT reliability: 94.61%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250610-linux-x86_64-python-main-3.15.0a0-0f866cb |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| 2to3           | 266 ms                                                 | 262 ms: 1.02x faster                                  |
| docutils       | 2.58 sec                                               | 2.66 sec: 1.03x slower                                |
| html5lib       | 63.4 ms                                                | 62.2 ms: 1.02x faster                                 |
| Geometric mean | (ref)                                                  | 1.00x faster                                          |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250610-linux-x86_64-python-main-3.15.0a0-0f866cb |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 315 ms: 1.47x faster                                  |
| async_tree_io              | 838 ms                                                 | 599 ms: 1.40x faster                                  |
| async_tree_memoization     | 437 ms                                                 | 312 ms: 1.40x faster                                  |
| async_tree_io_tg           | 861 ms                                                 | 623 ms: 1.38x faster                                  |
| async_tree_none            | 350 ms                                                 | 261 ms: 1.34x faster                                  |
| async_tree_none_tg         | 319 ms                                                 | 249 ms: 1.28x faster                                  |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 499 ms: 1.15x faster                                  |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 492 ms: 1.10x faster                                  |
| asyncio_websockets         | 551 ms                                                 | 553 ms: 1.00x slower                                  |
| coroutines                 | 22.2 ms                                                | 25.3 ms: 1.14x slower                                 |
| Geometric mean             | (ref)                                                  | 1.20x faster                                          |

Benchmark hidden because not significant (1): async_generators

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250610-linux-x86_64-python-main-3.15.0a0-0f866cb |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| float          | 78.7 ms                                                | 65.9 ms: 1.19x faster                                 |
| pidigits       | 186 ms                                                 | 187 ms: 1.00x slower                                  |
| nbody          | 87.7 ms                                                | 94.6 ms: 1.08x slower                                 |
| Geometric mean | (ref)                                                  | 1.03x faster                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250610-linux-x86_64-python-main-3.15.0a0-0f866cb |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| regex_v8       | 26.9 ms                                                | 22.6 ms: 1.19x faster                                 |
| regex_effbot   | 3.77 ms                                                | 3.25 ms: 1.16x faster                                 |
| regex_dna      | 220 ms                                                 | 199 ms: 1.10x faster                                  |
| regex_compile  | 132 ms                                                 | 128 ms: 1.03x faster                                  |
| Geometric mean | (ref)                                                  | 1.12x faster                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250610-linux-x86_64-python-main-3.15.0a0-0f866cb |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| tomli_loads          | 2.12 sec                                               | 1.90 sec: 1.11x faster                                |
| xml_etree_parse      | 154 ms                                                 | 140 ms: 1.10x faster                                  |
| xml_etree_process    | 60.5 ms                                                | 56.3 ms: 1.07x faster                                 |
| xml_etree_generate   | 86.8 ms                                                | 81.0 ms: 1.07x faster                                 |
| unpickle_pure_python | 213 us                                                 | 201 us: 1.06x faster                                  |
| xml_etree_iterparse  | 101 ms                                                 | 98.2 ms: 1.03x faster                                 |
| json_loads           | 27.2 us                                                | 28.5 us: 1.05x slower                                 |
| pickle_pure_python   | 302 us                                                 | 326 us: 1.08x slower                                  |
| json_dumps           | 10.1 ms                                                | 11.2 ms: 1.11x slower                                 |
| Geometric mean       | (ref)                                                  | 1.02x faster                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250610-linux-x86_64-python-main-3.15.0a0-0f866cb |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| python_startup         | 12.7 ms                                                | 12.2 ms: 1.04x faster                                 |
| python_startup_no_site | 7.00 ms                                                | 6.96 ms: 1.01x faster                                 |
| Geometric mean         | (ref)                                                  | 1.02x faster                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250610-linux-x86_64-python-main-3.15.0a0-0f866cb |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| genshi_text     | 22.6 ms                                                | 21.5 ms: 1.05x faster                                 |
| django_template | 31.7 ms                                                | 33.1 ms: 1.05x slower                                 |
| Geometric mean  | (ref)                                                  | 1.00x faster                                          |

Benchmark hidden because not significant (2): mako, genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250610-linux-x86_64-python-main-3.15.0a0-0f866cb |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| mdp                        | 2.54 sec                                               | 1.25 sec: 2.04x faster                                |
| async_tree_memoization_tg  | 463 ms                                                 | 315 ms: 1.47x faster                                  |
| async_tree_io              | 838 ms                                                 | 599 ms: 1.40x faster                                  |
| async_tree_memoization     | 437 ms                                                 | 312 ms: 1.40x faster                                  |
| richards                   | 47.5 ms                                                | 34.3 ms: 1.39x faster                                 |
| async_tree_io_tg           | 861 ms                                                 | 623 ms: 1.38x faster                                  |
| deepcopy                   | 354 us                                                 | 258 us: 1.37x faster                                  |
| richards_super             | 53.7 ms                                                | 39.6 ms: 1.36x faster                                 |
| async_tree_none            | 350 ms                                                 | 261 ms: 1.34x faster                                  |
| deepcopy_memo              | 38.4 us                                                | 29.7 us: 1.29x faster                                 |
| async_tree_none_tg         | 319 ms                                                 | 249 ms: 1.28x faster                                  |
| float                      | 78.7 ms                                                | 65.9 ms: 1.19x faster                                 |
| regex_v8                   | 26.9 ms                                                | 22.6 ms: 1.19x faster                                 |
| deepcopy_reduce            | 3.24 us                                                | 2.80 us: 1.16x faster                                 |
| regex_effbot               | 3.77 ms                                                | 3.25 ms: 1.16x faster                                 |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 499 ms: 1.15x faster                                  |
| go                         | 141 ms                                                 | 124 ms: 1.13x faster                                  |
| tomli_loads                | 2.12 sec                                               | 1.90 sec: 1.11x faster                                |
| spectral_norm              | 113 ms                                                 | 102 ms: 1.11x faster                                  |
| pyflate                    | 470 ms                                                 | 424 ms: 1.11x faster                                  |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 492 ms: 1.10x faster                                  |
| scimark_fft                | 367 ms                                                 | 332 ms: 1.10x faster                                  |
| regex_dna                  | 220 ms                                                 | 199 ms: 1.10x faster                                  |
| xml_etree_parse            | 154 ms                                                 | 140 ms: 1.10x faster                                  |
| pylint                     | 312 ms                                                 | 284 ms: 1.10x faster                                  |
| xml_etree_process          | 60.5 ms                                                | 56.3 ms: 1.07x faster                                 |
| xml_etree_generate         | 86.8 ms                                                | 81.0 ms: 1.07x faster                                 |
| telco                      | 8.40 ms                                                | 7.89 ms: 1.06x faster                                 |
| unpickle_pure_python       | 213 us                                                 | 201 us: 1.06x faster                                  |
| bpe_tokeniser              | 4.69 sec                                               | 4.43 sec: 1.06x faster                                |
| pycparser                  | 1.20 sec                                               | 1.14 sec: 1.06x faster                                |
| genshi_text                | 22.6 ms                                                | 21.5 ms: 1.05x faster                                 |
| sqlite_synth               | 2.90 us                                                | 2.79 us: 1.04x faster                                 |
| dulwich_log                | 64.6 ms                                                | 62.1 ms: 1.04x faster                                 |
| python_startup             | 12.7 ms                                                | 12.2 ms: 1.04x faster                                 |
| regex_compile              | 132 ms                                                 | 128 ms: 1.03x faster                                  |
| xml_etree_iterparse        | 101 ms                                                 | 98.2 ms: 1.03x faster                                 |
| k_core                     | 2.37 sec                                               | 2.31 sec: 1.02x faster                                |
| deltablue                  | 3.19 ms                                                | 3.13 ms: 1.02x faster                                 |
| html5lib                   | 63.4 ms                                                | 62.2 ms: 1.02x faster                                 |
| sympy_integrate            | 19.8 ms                                                | 19.5 ms: 1.02x faster                                 |
| 2to3                       | 266 ms                                                 | 262 ms: 1.02x faster                                  |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.96 ms: 1.01x faster                                 |
| meteor_contest             | 108 ms                                                 | 107 ms: 1.01x faster                                  |
| pathlib                    | 17.4 ms                                                | 17.2 ms: 1.01x faster                                 |
| python_startup_no_site     | 7.00 ms                                                | 6.96 ms: 1.01x faster                                 |
| pidigits                   | 186 ms                                                 | 187 ms: 1.00x slower                                  |
| asyncio_websockets         | 551 ms                                                 | 553 ms: 1.00x slower                                  |
| scimark_monte_carlo        | 66.8 ms                                                | 67.3 ms: 1.01x slower                                 |
| scimark_sor                | 122 ms                                                 | 124 ms: 1.01x slower                                  |
| shortest_path              | 487 ms                                                 | 496 ms: 1.02x slower                                  |
| connected_components       | 447 ms                                                 | 456 ms: 1.02x slower                                  |
| gc_traversal               | 4.90 ms                                                | 5.01 ms: 1.02x slower                                 |
| sympy_expand               | 456 ms                                                 | 468 ms: 1.03x slower                                  |
| crypto_pyaes               | 74.7 ms                                                | 76.8 ms: 1.03x slower                                 |
| docutils                   | 2.58 sec                                               | 2.66 sec: 1.03x slower                                |
| nqueens                    | 80.9 ms                                                | 83.6 ms: 1.03x slower                                 |
| comprehensions             | 16.5 us                                                | 17.0 us: 1.03x slower                                 |
| scimark_lu                 | 114 ms                                                 | 120 ms: 1.04x slower                                  |
| django_template            | 31.7 ms                                                | 33.1 ms: 1.05x slower                                 |
| json_loads                 | 27.2 us                                                | 28.5 us: 1.05x slower                                 |
| hexiom                     | 6.08 ms                                                | 6.41 ms: 1.05x slower                                 |
| fannkuch                   | 394 ms                                                 | 418 ms: 1.06x slower                                  |
| create_gc_cycles           | 2.45 ms                                                | 2.60 ms: 1.06x slower                                 |
| generators                 | 28.8 ms                                                | 30.6 ms: 1.06x slower                                 |
| raytrace                   | 262 ms                                                 | 280 ms: 1.07x slower                                  |
| typing_runtime_protocols   | 160 us                                                 | 172 us: 1.07x slower                                  |
| pickle_pure_python         | 302 us                                                 | 326 us: 1.08x slower                                  |
| nbody                      | 87.7 ms                                                | 94.6 ms: 1.08x slower                                 |
| logging_simple             | 5.65 us                                                | 6.16 us: 1.09x slower                                 |
| chaos                      | 58.0 ms                                                | 63.7 ms: 1.10x slower                                 |
| logging_format             | 6.23 us                                                | 6.84 us: 1.10x slower                                 |
| json_dumps                 | 10.1 ms                                                | 11.2 ms: 1.11x slower                                 |
| pprint_safe_repr           | 727 ms                                                 | 815 ms: 1.12x slower                                  |
| coroutines                 | 22.2 ms                                                | 25.3 ms: 1.14x slower                                 |
| pprint_pformat             | 1.48 sec                                               | 1.69 sec: 1.15x slower                                |
| many_optionals             | 857 us                                                 | 986 us: 1.15x slower                                  |
| subparsers                 | 15.5 ms                                                | 23.8 ms: 1.54x slower                                 |
| logging_silent             | 101 ns                                                 | 475 ns: 4.71x slower                                  |
| coverage                   | 82.8 ms                                                | 424 ms: 5.12x slower                                  |
| thrift                     | 800 us                                                 | 148 ms: 184.97x slower                                |
| Geometric mean             | (ref)                                                  | 1.05x slower                                          |

Benchmark hidden because not significant (7): sphinx, json, mako, sympy_str, async_generators, sympy_sum, genshi_xml
Ignored benchmarks (13) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250610-3.15.0a0-0f866cb-JIT/bm-20250610-linux-x86_64-python-main-3.15.0a0-0f866cb.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.033x slower

# HPT report

- Reliability score: 94.61% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.07x
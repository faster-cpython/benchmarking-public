# Results vs. 3.13.0

- fork: brandtbucher
- ref: jit_o2
- machine: linux-x86_64
- commit hash: f528bf3
- commit date: 2025-06-28
- overall geometric mean: 1.063x faster
- HPT reliability: 99.99%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250628-linux-x86_64-brandtbucher-jit_o2-3.15.0a0-f528bf3 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 260 ms: 1.02x faster                                          |
| docutils       | 2.58 sec                                               | 2.63 sec: 1.02x slower                                        |
| html5lib       | 63.4 ms                                                | 61.7 ms: 1.03x faster                                         |
| sphinx         | 1.03 sec                                               | 1.02 sec: 1.01x faster                                        |
| Geometric mean | (ref)                                                  | 1.01x faster                                                  |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250628-linux-x86_64-brandtbucher-jit_o2-3.15.0a0-f528bf3 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 311 ms: 1.49x faster                                          |
| async_tree_io              | 838 ms                                                 | 597 ms: 1.40x faster                                          |
| async_tree_memoization     | 437 ms                                                 | 313 ms: 1.40x faster                                          |
| async_tree_io_tg           | 861 ms                                                 | 633 ms: 1.36x faster                                          |
| async_tree_none            | 350 ms                                                 | 261 ms: 1.34x faster                                          |
| async_tree_none_tg         | 319 ms                                                 | 248 ms: 1.29x faster                                          |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 492 ms: 1.16x faster                                          |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 486 ms: 1.12x faster                                          |
| async_generators           | 433 ms                                                 | 428 ms: 1.01x faster                                          |
| coroutines                 | 22.2 ms                                                | 25.3 ms: 1.14x slower                                         |
| Geometric mean             | (ref)                                                  | 1.21x faster                                                  |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250628-linux-x86_64-brandtbucher-jit_o2-3.15.0a0-f528bf3 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| float          | 78.7 ms                                                | 65.7 ms: 1.20x faster                                         |
| pidigits       | 186 ms                                                 | 188 ms: 1.01x slower                                          |
| nbody          | 87.7 ms                                                | 97.7 ms: 1.11x slower                                         |
| Geometric mean | (ref)                                                  | 1.02x faster                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250628-linux-x86_64-brandtbucher-jit_o2-3.15.0a0-f528bf3 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| regex_v8       | 26.9 ms                                                | 22.9 ms: 1.17x faster                                         |
| regex_effbot   | 3.77 ms                                                | 3.28 ms: 1.15x faster                                         |
| regex_dna      | 220 ms                                                 | 207 ms: 1.06x faster                                          |
| regex_compile  | 132 ms                                                 | 127 ms: 1.03x faster                                          |
| Geometric mean | (ref)                                                  | 1.10x faster                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250628-linux-x86_64-brandtbucher-jit_o2-3.15.0a0-f528bf3 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| tomli_loads          | 2.12 sec                                               | 1.82 sec: 1.16x faster                                        |
| xml_etree_parse      | 154 ms                                                 | 140 ms: 1.10x faster                                          |
| unpickle_pure_python | 213 us                                                 | 195 us: 1.09x faster                                          |
| xml_etree_process    | 60.5 ms                                                | 55.5 ms: 1.09x faster                                         |
| xml_etree_generate   | 86.8 ms                                                | 80.4 ms: 1.08x faster                                         |
| xml_etree_iterparse  | 101 ms                                                 | 99.0 ms: 1.02x faster                                         |
| json_loads           | 27.2 us                                                | 28.2 us: 1.04x slower                                         |
| pickle_pure_python   | 302 us                                                 | 324 us: 1.07x slower                                          |
| json_dumps           | 10.1 ms                                                | 11.1 ms: 1.09x slower                                         |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                  |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250628-linux-x86_64-brandtbucher-jit_o2-3.15.0a0-f528bf3 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| python_startup         | 12.7 ms                                                | 12.2 ms: 1.04x faster                                         |
| python_startup_no_site | 7.00 ms                                                | 6.96 ms: 1.01x faster                                         |
| Geometric mean         | (ref)                                                  | 1.02x faster                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250628-linux-x86_64-brandtbucher-jit_o2-3.15.0a0-f528bf3 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| genshi_text     | 22.6 ms                                                | 21.6 ms: 1.05x faster                                         |
| genshi_xml      | 50.5 ms                                                | 49.8 ms: 1.01x faster                                         |
| mako            | 10.7 ms                                                | 10.6 ms: 1.01x faster                                         |
| django_template | 31.7 ms                                                | 32.6 ms: 1.03x slower                                         |
| Geometric mean  | (ref)                                                  | 1.01x faster                                                  |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250628-linux-x86_64-brandtbucher-jit_o2-3.15.0a0-f528bf3 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| mdp                        | 2.54 sec                                               | 1.23 sec: 2.06x faster                                        |
| async_tree_memoization_tg  | 463 ms                                                 | 311 ms: 1.49x faster                                          |
| richards                   | 47.5 ms                                                | 32.8 ms: 1.45x faster                                         |
| async_tree_io              | 838 ms                                                 | 597 ms: 1.40x faster                                          |
| richards_super             | 53.7 ms                                                | 38.3 ms: 1.40x faster                                         |
| async_tree_memoization     | 437 ms                                                 | 313 ms: 1.40x faster                                          |
| deepcopy                   | 354 us                                                 | 258 us: 1.37x faster                                          |
| async_tree_io_tg           | 861 ms                                                 | 633 ms: 1.36x faster                                          |
| async_tree_none            | 350 ms                                                 | 261 ms: 1.34x faster                                          |
| deepcopy_memo              | 38.4 us                                                | 29.1 us: 1.32x faster                                         |
| async_tree_none_tg         | 319 ms                                                 | 248 ms: 1.29x faster                                          |
| spectral_norm              | 113 ms                                                 | 93.9 ms: 1.21x faster                                         |
| go                         | 141 ms                                                 | 117 ms: 1.20x faster                                          |
| float                      | 78.7 ms                                                | 65.7 ms: 1.20x faster                                         |
| deepcopy_reduce            | 3.24 us                                                | 2.73 us: 1.19x faster                                         |
| regex_v8                   | 26.9 ms                                                | 22.9 ms: 1.17x faster                                         |
| scimark_fft                | 367 ms                                                 | 313 ms: 1.17x faster                                          |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 492 ms: 1.16x faster                                          |
| tomli_loads                | 2.12 sec                                               | 1.82 sec: 1.16x faster                                        |
| regex_effbot               | 3.77 ms                                                | 3.28 ms: 1.15x faster                                         |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 486 ms: 1.12x faster                                          |
| pylint                     | 312 ms                                                 | 282 ms: 1.10x faster                                          |
| pyflate                    | 470 ms                                                 | 425 ms: 1.10x faster                                          |
| telco                      | 8.40 ms                                                | 7.63 ms: 1.10x faster                                         |
| xml_etree_parse            | 154 ms                                                 | 140 ms: 1.10x faster                                          |
| unpickle_pure_python       | 213 us                                                 | 195 us: 1.09x faster                                          |
| dulwich_log                | 64.6 ms                                                | 59.2 ms: 1.09x faster                                         |
| xml_etree_process          | 60.5 ms                                                | 55.5 ms: 1.09x faster                                         |
| bpe_tokeniser              | 4.69 sec                                               | 4.33 sec: 1.08x faster                                        |
| xml_etree_generate         | 86.8 ms                                                | 80.4 ms: 1.08x faster                                         |
| regex_dna                  | 220 ms                                                 | 207 ms: 1.06x faster                                          |
| deltablue                  | 3.19 ms                                                | 3.05 ms: 1.05x faster                                         |
| genshi_text                | 22.6 ms                                                | 21.6 ms: 1.05x faster                                         |
| sqlite_synth               | 2.90 us                                                | 2.78 us: 1.04x faster                                         |
| thrift                     | 800 us                                                 | 769 us: 1.04x faster                                          |
| k_core                     | 2.37 sec                                               | 2.28 sec: 1.04x faster                                        |
| python_startup             | 12.7 ms                                                | 12.2 ms: 1.04x faster                                         |
| regex_compile              | 132 ms                                                 | 127 ms: 1.03x faster                                          |
| pprint_pformat             | 1.48 sec                                               | 1.43 sec: 1.03x faster                                        |
| html5lib                   | 63.4 ms                                                | 61.7 ms: 1.03x faster                                         |
| sympy_integrate            | 19.8 ms                                                | 19.3 ms: 1.03x faster                                         |
| pycparser                  | 1.20 sec                                               | 1.17 sec: 1.03x faster                                        |
| pprint_safe_repr           | 727 ms                                                 | 709 ms: 1.02x faster                                          |
| xml_etree_iterparse        | 101 ms                                                 | 99.0 ms: 1.02x faster                                         |
| 2to3                       | 266 ms                                                 | 260 ms: 1.02x faster                                          |
| scimark_sor                | 122 ms                                                 | 120 ms: 1.02x faster                                          |
| pathlib                    | 17.4 ms                                                | 17.1 ms: 1.02x faster                                         |
| sphinx                     | 1.03 sec                                               | 1.02 sec: 1.01x faster                                        |
| genshi_xml                 | 50.5 ms                                                | 49.8 ms: 1.01x faster                                         |
| logging_simple             | 5.65 us                                                | 5.58 us: 1.01x faster                                         |
| async_generators           | 433 ms                                                 | 428 ms: 1.01x faster                                          |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.97 ms: 1.01x faster                                         |
| mako                       | 10.7 ms                                                | 10.6 ms: 1.01x faster                                         |
| crypto_pyaes               | 74.7 ms                                                | 74.0 ms: 1.01x faster                                         |
| meteor_contest             | 108 ms                                                 | 107 ms: 1.01x faster                                          |
| comprehensions             | 16.5 us                                                | 16.4 us: 1.01x faster                                         |
| python_startup_no_site     | 7.00 ms                                                | 6.96 ms: 1.01x faster                                         |
| sympy_sum                  | 150 ms                                                 | 150 ms: 1.00x faster                                          |
| pidigits                   | 186 ms                                                 | 188 ms: 1.01x slower                                          |
| nqueens                    | 80.9 ms                                                | 81.9 ms: 1.01x slower                                         |
| logging_format             | 6.23 us                                                | 6.33 us: 1.02x slower                                         |
| fannkuch                   | 394 ms                                                 | 400 ms: 1.02x slower                                          |
| sympy_expand               | 456 ms                                                 | 465 ms: 1.02x slower                                          |
| docutils                   | 2.58 sec                                               | 2.63 sec: 1.02x slower                                        |
| connected_components       | 447 ms                                                 | 456 ms: 1.02x slower                                          |
| scimark_lu                 | 114 ms                                                 | 117 ms: 1.02x slower                                          |
| django_template            | 31.7 ms                                                | 32.6 ms: 1.03x slower                                         |
| hexiom                     | 6.08 ms                                                | 6.27 ms: 1.03x slower                                         |
| logging_silent             | 101 ns                                                 | 104 ns: 1.03x slower                                          |
| shortest_path              | 487 ms                                                 | 504 ms: 1.04x slower                                          |
| json_loads                 | 27.2 us                                                | 28.2 us: 1.04x slower                                         |
| typing_runtime_protocols   | 160 us                                                 | 167 us: 1.04x slower                                          |
| raytrace                   | 262 ms                                                 | 275 ms: 1.05x slower                                          |
| gc_traversal               | 4.90 ms                                                | 5.16 ms: 1.05x slower                                         |
| chaos                      | 58.0 ms                                                | 61.2 ms: 1.06x slower                                         |
| create_gc_cycles           | 2.45 ms                                                | 2.59 ms: 1.06x slower                                         |
| generators                 | 28.8 ms                                                | 30.5 ms: 1.06x slower                                         |
| coverage                   | 82.8 ms                                                | 88.2 ms: 1.06x slower                                         |
| pickle_pure_python         | 302 us                                                 | 324 us: 1.07x slower                                          |
| json_dumps                 | 10.1 ms                                                | 11.1 ms: 1.09x slower                                         |
| nbody                      | 87.7 ms                                                | 97.7 ms: 1.11x slower                                         |
| many_optionals             | 857 us                                                 | 973 us: 1.14x slower                                          |
| coroutines                 | 22.2 ms                                                | 25.3 ms: 1.14x slower                                         |
| subparsers                 | 15.5 ms                                                | 23.6 ms: 1.53x slower                                         |
| Geometric mean             | (ref)                                                  | 1.06x faster                                                  |

Benchmark hidden because not significant (5): json, sympy_str, scimark_monte_carlo, asyncio_websockets, djangocms
Ignored benchmarks (12) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: bench_mp_pool, bench_thread_pool, chameleon, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250628-3.15.0a0-f528bf3-JIT/bm-20250628-linux-x86_64-brandtbucher-jit_o2-3.15.0a0-f528bf3.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.063x faster

# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.07x
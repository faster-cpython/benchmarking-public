# Results vs. 3.13.0

- fork: faster-cpython
- ref: tier_2_tos_caching
- machine: linux-x86_64
- commit hash: 2850d72
- commit date: 2025-06-19
- overall geometric mean: 1.055x faster
- HPT reliability: 99.80%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250619-linux-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-2850d72 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 260 ms: 1.02x faster                                                          |
| docutils       | 2.58 sec                                               | 2.64 sec: 1.02x slower                                                        |
| html5lib       | 63.4 ms                                                | 61.5 ms: 1.03x faster                                                         |
| sphinx         | 1.03 sec                                               | 1.02 sec: 1.02x faster                                                        |
| Geometric mean | (ref)                                                  | 1.01x faster                                                                  |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250619-linux-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-2850d72 |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 316 ms: 1.46x faster                                                          |
| async_tree_io_tg           | 861 ms                                                 | 616 ms: 1.40x faster                                                          |
| async_tree_io              | 838 ms                                                 | 607 ms: 1.38x faster                                                          |
| async_tree_memoization     | 437 ms                                                 | 317 ms: 1.38x faster                                                          |
| async_tree_none            | 350 ms                                                 | 265 ms: 1.32x faster                                                          |
| async_tree_none_tg         | 319 ms                                                 | 252 ms: 1.26x faster                                                          |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 506 ms: 1.13x faster                                                          |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 498 ms: 1.09x faster                                                          |
| async_generators           | 433 ms                                                 | 428 ms: 1.01x faster                                                          |
| coroutines                 | 22.2 ms                                                | 25.1 ms: 1.13x slower                                                         |
| Geometric mean             | (ref)                                                  | 1.20x faster                                                                  |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250619-linux-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-2850d72 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 65.0 ms: 1.21x faster                                                         |
| nbody          | 87.7 ms                                                | 82.8 ms: 1.06x faster                                                         |
| pidigits       | 186 ms                                                 | 193 ms: 1.03x slower                                                          |
| Geometric mean | (ref)                                                  | 1.07x faster                                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250619-linux-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-2850d72 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                | 3.10 ms: 1.21x faster                                                         |
| regex_v8       | 26.9 ms                                                | 22.3 ms: 1.21x faster                                                         |
| regex_dna      | 220 ms                                                 | 186 ms: 1.18x faster                                                          |
| regex_compile  | 132 ms                                                 | 127 ms: 1.04x faster                                                          |
| Geometric mean | (ref)                                                  | 1.16x faster                                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250619-linux-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-2850d72 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| tomli_loads          | 2.12 sec                                               | 1.86 sec: 1.14x faster                                                        |
| xml_etree_parse      | 154 ms                                                 | 139 ms: 1.11x faster                                                          |
| xml_etree_process    | 60.5 ms                                                | 56.0 ms: 1.08x faster                                                         |
| xml_etree_generate   | 86.8 ms                                                | 81.1 ms: 1.07x faster                                                         |
| unpickle_pure_python | 213 us                                                 | 205 us: 1.04x faster                                                          |
| xml_etree_iterparse  | 101 ms                                                 | 98.5 ms: 1.03x faster                                                         |
| json_loads           | 27.2 us                                                | 27.9 us: 1.03x slower                                                         |
| pickle_pure_python   | 302 us                                                 | 324 us: 1.07x slower                                                          |
| json_dumps           | 10.1 ms                                                | 11.0 ms: 1.09x slower                                                         |
| Geometric mean       | (ref)                                                  | 1.03x faster                                                                  |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250619-linux-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-2850d72 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| python_startup         | 12.7 ms                                                | 12.2 ms: 1.03x faster                                                         |
| python_startup_no_site | 7.00 ms                                                | 6.98 ms: 1.00x faster                                                         |
| Geometric mean         | (ref)                                                  | 1.02x faster                                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250619-linux-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-2850d72 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| genshi_text     | 22.6 ms                                                | 21.8 ms: 1.04x faster                                                         |
| genshi_xml      | 50.5 ms                                                | 51.0 ms: 1.01x slower                                                         |
| mako            | 10.7 ms                                                | 10.8 ms: 1.01x slower                                                         |
| django_template | 31.7 ms                                                | 32.3 ms: 1.02x slower                                                         |
| Geometric mean  | (ref)                                                  | 1.00x slower                                                                  |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250619-linux-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-2850d72 |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| mdp                        | 2.54 sec                                               | 1.24 sec: 2.06x faster                                                        |
| async_tree_memoization_tg  | 463 ms                                                 | 316 ms: 1.46x faster                                                          |
| richards                   | 47.5 ms                                                | 33.8 ms: 1.41x faster                                                         |
| async_tree_io_tg           | 861 ms                                                 | 616 ms: 1.40x faster                                                          |
| richards_super             | 53.7 ms                                                | 38.9 ms: 1.38x faster                                                         |
| async_tree_io              | 838 ms                                                 | 607 ms: 1.38x faster                                                          |
| async_tree_memoization     | 437 ms                                                 | 317 ms: 1.38x faster                                                          |
| deepcopy                   | 354 us                                                 | 262 us: 1.35x faster                                                          |
| async_tree_none            | 350 ms                                                 | 265 ms: 1.32x faster                                                          |
| deepcopy_memo              | 38.4 us                                                | 29.5 us: 1.30x faster                                                         |
| async_tree_none_tg         | 319 ms                                                 | 252 ms: 1.26x faster                                                          |
| regex_effbot               | 3.77 ms                                                | 3.10 ms: 1.21x faster                                                         |
| float                      | 78.7 ms                                                | 65.0 ms: 1.21x faster                                                         |
| regex_v8                   | 26.9 ms                                                | 22.3 ms: 1.21x faster                                                         |
| deepcopy_reduce            | 3.24 us                                                | 2.69 us: 1.20x faster                                                         |
| spectral_norm              | 113 ms                                                 | 94.7 ms: 1.20x faster                                                         |
| regex_dna                  | 220 ms                                                 | 186 ms: 1.18x faster                                                          |
| go                         | 141 ms                                                 | 121 ms: 1.16x faster                                                          |
| scimark_fft                | 367 ms                                                 | 318 ms: 1.15x faster                                                          |
| tomli_loads                | 2.12 sec                                               | 1.86 sec: 1.14x faster                                                        |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 506 ms: 1.13x faster                                                          |
| pyflate                    | 470 ms                                                 | 420 ms: 1.12x faster                                                          |
| xml_etree_parse            | 154 ms                                                 | 139 ms: 1.11x faster                                                          |
| pylint                     | 312 ms                                                 | 283 ms: 1.10x faster                                                          |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 498 ms: 1.09x faster                                                          |
| dulwich_log                | 64.6 ms                                                | 59.5 ms: 1.09x faster                                                         |
| pycparser                  | 1.20 sec                                               | 1.11 sec: 1.08x faster                                                        |
| xml_etree_process          | 60.5 ms                                                | 56.0 ms: 1.08x faster                                                         |
| bpe_tokeniser              | 4.69 sec                                               | 4.35 sec: 1.08x faster                                                        |
| xml_etree_generate         | 86.8 ms                                                | 81.1 ms: 1.07x faster                                                         |
| telco                      | 8.40 ms                                                | 7.91 ms: 1.06x faster                                                         |
| nbody                      | 87.7 ms                                                | 82.8 ms: 1.06x faster                                                         |
| regex_compile              | 132 ms                                                 | 127 ms: 1.04x faster                                                          |
| unpickle_pure_python       | 213 us                                                 | 205 us: 1.04x faster                                                          |
| genshi_text                | 22.6 ms                                                | 21.8 ms: 1.04x faster                                                         |
| scimark_sor                | 122 ms                                                 | 118 ms: 1.04x faster                                                          |
| python_startup             | 12.7 ms                                                | 12.2 ms: 1.03x faster                                                         |
| json                       | 5.32 ms                                                | 5.15 ms: 1.03x faster                                                         |
| k_core                     | 2.37 sec                                               | 2.30 sec: 1.03x faster                                                        |
| sqlite_synth               | 2.90 us                                                | 2.81 us: 1.03x faster                                                         |
| html5lib                   | 63.4 ms                                                | 61.5 ms: 1.03x faster                                                         |
| xml_etree_iterparse        | 101 ms                                                 | 98.5 ms: 1.03x faster                                                         |
| sympy_integrate            | 19.8 ms                                                | 19.3 ms: 1.02x faster                                                         |
| thrift                     | 800 us                                                 | 781 us: 1.02x faster                                                          |
| 2to3                       | 266 ms                                                 | 260 ms: 1.02x faster                                                          |
| pathlib                    | 17.4 ms                                                | 17.0 ms: 1.02x faster                                                         |
| deltablue                  | 3.19 ms                                                | 3.14 ms: 1.02x faster                                                         |
| sphinx                     | 1.03 sec                                               | 1.02 sec: 1.02x faster                                                        |
| async_generators           | 433 ms                                                 | 428 ms: 1.01x faster                                                          |
| scimark_monte_carlo        | 66.8 ms                                                | 66.0 ms: 1.01x faster                                                         |
| meteor_contest             | 108 ms                                                 | 107 ms: 1.01x faster                                                          |
| python_startup_no_site     | 7.00 ms                                                | 6.98 ms: 1.00x faster                                                         |
| genshi_xml                 | 50.5 ms                                                | 51.0 ms: 1.01x slower                                                         |
| mako                       | 10.7 ms                                                | 10.8 ms: 1.01x slower                                                         |
| nqueens                    | 80.9 ms                                                | 82.0 ms: 1.01x slower                                                         |
| fannkuch                   | 394 ms                                                 | 401 ms: 1.02x slower                                                          |
| docutils                   | 2.58 sec                                               | 2.64 sec: 1.02x slower                                                        |
| django_template            | 31.7 ms                                                | 32.3 ms: 1.02x slower                                                         |
| sympy_expand               | 456 ms                                                 | 468 ms: 1.03x slower                                                          |
| json_loads                 | 27.2 us                                                | 27.9 us: 1.03x slower                                                         |
| crypto_pyaes               | 74.7 ms                                                | 76.8 ms: 1.03x slower                                                         |
| scimark_lu                 | 114 ms                                                 | 118 ms: 1.03x slower                                                          |
| pidigits                   | 186 ms                                                 | 193 ms: 1.03x slower                                                          |
| gc_traversal               | 4.90 ms                                                | 5.07 ms: 1.04x slower                                                         |
| connected_components       | 447 ms                                                 | 464 ms: 1.04x slower                                                          |
| comprehensions             | 16.5 us                                                | 17.2 us: 1.04x slower                                                         |
| shortest_path              | 487 ms                                                 | 508 ms: 1.04x slower                                                          |
| raytrace                   | 262 ms                                                 | 274 ms: 1.05x slower                                                          |
| generators                 | 28.8 ms                                                | 30.3 ms: 1.05x slower                                                         |
| coverage                   | 82.8 ms                                                | 87.4 ms: 1.05x slower                                                         |
| hexiom                     | 6.08 ms                                                | 6.41 ms: 1.06x slower                                                         |
| create_gc_cycles           | 2.45 ms                                                | 2.59 ms: 1.06x slower                                                         |
| chaos                      | 58.0 ms                                                | 61.5 ms: 1.06x slower                                                         |
| typing_runtime_protocols   | 160 us                                                 | 171 us: 1.07x slower                                                          |
| pickle_pure_python         | 302 us                                                 | 324 us: 1.07x slower                                                          |
| json_dumps                 | 10.1 ms                                                | 11.0 ms: 1.09x slower                                                         |
| logging_simple             | 5.65 us                                                | 6.19 us: 1.09x slower                                                         |
| logging_format             | 6.23 us                                                | 6.85 us: 1.10x slower                                                         |
| coroutines                 | 22.2 ms                                                | 25.1 ms: 1.13x slower                                                         |
| many_optionals             | 857 us                                                 | 982 us: 1.15x slower                                                          |
| pprint_safe_repr           | 727 ms                                                 | 855 ms: 1.18x slower                                                          |
| pprint_pformat             | 1.48 sec                                               | 1.75 sec: 1.19x slower                                                        |
| subparsers                 | 15.5 ms                                                | 23.9 ms: 1.54x slower                                                         |
| logging_silent             | 101 ns                                                 | 477 ns: 4.72x slower                                                          |
| Geometric mean             | (ref)                                                  | 1.04x faster                                                                  |

Benchmark hidden because not significant (5): sympy_str, sympy_sum, scimark_sparse_mat_mult, asyncio_websockets, djangocms
Ignored benchmarks (12) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: bench_mp_pool, bench_thread_pool, chameleon, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250619-3.15.0a0-2850d72-JIT/bm-20250619-linux-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-2850d72.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.055x faster

# HPT report

- Reliability score: 99.80% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.08x
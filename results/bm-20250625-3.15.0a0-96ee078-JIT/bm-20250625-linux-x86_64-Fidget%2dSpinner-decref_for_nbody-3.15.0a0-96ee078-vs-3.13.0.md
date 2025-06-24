# Results vs. 3.13.0

- fork: Fidget-Spinner
- ref: decref_for_nbody
- machine: linux-x86_64
- commit hash: 96ee078
- commit date: 2025-06-25
- overall geometric mean: 1.056x faster
- HPT reliability: 99.82%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250625-linux-x86_64-Fidget%2dSpinner-decref_for_nbody-3.15.0a0-96ee078 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 260 ms: 1.02x faster                                                        |
| docutils       | 2.58 sec                                               | 2.65 sec: 1.03x slower                                                      |
| html5lib       | 63.4 ms                                                | 61.6 ms: 1.03x faster                                                       |
| Geometric mean | (ref)                                                  | 1.01x faster                                                                |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250625-linux-x86_64-Fidget%2dSpinner-decref_for_nbody-3.15.0a0-96ee078 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 314 ms: 1.47x faster                                                        |
| async_tree_io_tg           | 861 ms                                                 | 612 ms: 1.41x faster                                                        |
| async_tree_io              | 838 ms                                                 | 599 ms: 1.40x faster                                                        |
| async_tree_memoization     | 437 ms                                                 | 312 ms: 1.40x faster                                                        |
| async_tree_none            | 350 ms                                                 | 260 ms: 1.35x faster                                                        |
| async_tree_none_tg         | 319 ms                                                 | 248 ms: 1.29x faster                                                        |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 494 ms: 1.16x faster                                                        |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 488 ms: 1.11x faster                                                        |
| async_generators           | 433 ms                                                 | 430 ms: 1.01x faster                                                        |
| asyncio_websockets         | 551 ms                                                 | 554 ms: 1.00x slower                                                        |
| coroutines                 | 22.2 ms                                                | 25.5 ms: 1.15x slower                                                       |
| Geometric mean             | (ref)                                                  | 1.21x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250625-linux-x86_64-Fidget%2dSpinner-decref_for_nbody-3.15.0a0-96ee078 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 65.5 ms: 1.20x faster                                                       |
| pidigits       | 186 ms                                                 | 188 ms: 1.01x slower                                                        |
| nbody          | 87.7 ms                                                | 90.3 ms: 1.03x slower                                                       |
| Geometric mean | (ref)                                                  | 1.05x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250625-linux-x86_64-Fidget%2dSpinner-decref_for_nbody-3.15.0a0-96ee078 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_v8       | 26.9 ms                                                | 24.0 ms: 1.12x faster                                                       |
| regex_effbot   | 3.77 ms                                                | 3.38 ms: 1.11x faster                                                       |
| regex_dna      | 220 ms                                                 | 210 ms: 1.05x faster                                                        |
| regex_compile  | 132 ms                                                 | 127 ms: 1.04x faster                                                        |
| Geometric mean | (ref)                                                  | 1.08x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250625-linux-x86_64-Fidget%2dSpinner-decref_for_nbody-3.15.0a0-96ee078 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 2.12 sec                                               | 1.83 sec: 1.16x faster                                                      |
| xml_etree_parse      | 154 ms                                                 | 141 ms: 1.10x faster                                                        |
| xml_etree_process    | 60.5 ms                                                | 56.0 ms: 1.08x faster                                                       |
| xml_etree_generate   | 86.8 ms                                                | 80.6 ms: 1.08x faster                                                       |
| unpickle_pure_python | 213 us                                                 | 201 us: 1.06x faster                                                        |
| xml_etree_iterparse  | 101 ms                                                 | 98.0 ms: 1.03x faster                                                       |
| json_loads           | 27.2 us                                                | 28.8 us: 1.06x slower                                                       |
| pickle_pure_python   | 302 us                                                 | 323 us: 1.07x slower                                                        |
| json_dumps           | 10.1 ms                                                | 10.9 ms: 1.08x slower                                                       |
| Geometric mean       | (ref)                                                  | 1.03x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250625-linux-x86_64-Fidget%2dSpinner-decref_for_nbody-3.15.0a0-96ee078 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 12.7 ms                                                | 12.2 ms: 1.04x faster                                                       |
| python_startup_no_site | 7.00 ms                                                | 6.97 ms: 1.00x faster                                                       |
| Geometric mean         | (ref)                                                  | 1.02x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250625-linux-x86_64-Fidget%2dSpinner-decref_for_nbody-3.15.0a0-96ee078 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_text     | 22.6 ms                                                | 21.5 ms: 1.05x faster                                                       |
| mako            | 10.7 ms                                                | 10.8 ms: 1.01x slower                                                       |
| genshi_xml      | 50.5 ms                                                | 51.2 ms: 1.01x slower                                                       |
| django_template | 31.7 ms                                                | 32.7 ms: 1.03x slower                                                       |
| Geometric mean  | (ref)                                                  | 1.00x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250625-linux-x86_64-Fidget%2dSpinner-decref_for_nbody-3.15.0a0-96ee078 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mdp                        | 2.54 sec                                               | 1.24 sec: 2.05x faster                                                      |
| async_tree_memoization_tg  | 463 ms                                                 | 314 ms: 1.47x faster                                                        |
| richards                   | 47.5 ms                                                | 33.7 ms: 1.41x faster                                                       |
| async_tree_io_tg           | 861 ms                                                 | 612 ms: 1.41x faster                                                        |
| async_tree_io              | 838 ms                                                 | 599 ms: 1.40x faster                                                        |
| async_tree_memoization     | 437 ms                                                 | 312 ms: 1.40x faster                                                        |
| deepcopy                   | 354 us                                                 | 257 us: 1.38x faster                                                        |
| richards_super             | 53.7 ms                                                | 39.7 ms: 1.35x faster                                                       |
| async_tree_none            | 350 ms                                                 | 260 ms: 1.35x faster                                                        |
| deepcopy_memo              | 38.4 us                                                | 29.3 us: 1.31x faster                                                       |
| async_tree_none_tg         | 319 ms                                                 | 248 ms: 1.29x faster                                                        |
| deepcopy_reduce            | 3.24 us                                                | 2.66 us: 1.22x faster                                                       |
| spectral_norm              | 113 ms                                                 | 94.2 ms: 1.20x faster                                                       |
| float                      | 78.7 ms                                                | 65.5 ms: 1.20x faster                                                       |
| go                         | 141 ms                                                 | 120 ms: 1.17x faster                                                        |
| scimark_fft                | 367 ms                                                 | 314 ms: 1.17x faster                                                        |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 494 ms: 1.16x faster                                                        |
| tomli_loads                | 2.12 sec                                               | 1.83 sec: 1.16x faster                                                      |
| regex_v8                   | 26.9 ms                                                | 24.0 ms: 1.12x faster                                                       |
| regex_effbot               | 3.77 ms                                                | 3.38 ms: 1.11x faster                                                       |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 488 ms: 1.11x faster                                                        |
| pyflate                    | 470 ms                                                 | 423 ms: 1.11x faster                                                        |
| pylint                     | 312 ms                                                 | 283 ms: 1.10x faster                                                        |
| telco                      | 8.40 ms                                                | 7.65 ms: 1.10x faster                                                       |
| xml_etree_parse            | 154 ms                                                 | 141 ms: 1.10x faster                                                        |
| dulwich_log                | 64.6 ms                                                | 59.4 ms: 1.09x faster                                                       |
| xml_etree_process          | 60.5 ms                                                | 56.0 ms: 1.08x faster                                                       |
| xml_etree_generate         | 86.8 ms                                                | 80.6 ms: 1.08x faster                                                       |
| bpe_tokeniser              | 4.69 sec                                               | 4.37 sec: 1.07x faster                                                      |
| unpickle_pure_python       | 213 us                                                 | 201 us: 1.06x faster                                                        |
| genshi_text                | 22.6 ms                                                | 21.5 ms: 1.05x faster                                                       |
| thrift                     | 800 us                                                 | 762 us: 1.05x faster                                                        |
| regex_dna                  | 220 ms                                                 | 210 ms: 1.05x faster                                                        |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.82 ms: 1.04x faster                                                       |
| k_core                     | 2.37 sec                                               | 2.28 sec: 1.04x faster                                                      |
| sqlite_synth               | 2.90 us                                                | 2.80 us: 1.04x faster                                                       |
| regex_compile              | 132 ms                                                 | 127 ms: 1.04x faster                                                        |
| python_startup             | 12.7 ms                                                | 12.2 ms: 1.04x faster                                                       |
| scimark_sor                | 122 ms                                                 | 118 ms: 1.03x faster                                                        |
| xml_etree_iterparse        | 101 ms                                                 | 98.0 ms: 1.03x faster                                                       |
| gc_traversal               | 4.90 ms                                                | 4.75 ms: 1.03x faster                                                       |
| html5lib                   | 63.4 ms                                                | 61.6 ms: 1.03x faster                                                       |
| pycparser                  | 1.20 sec                                               | 1.17 sec: 1.03x faster                                                      |
| scimark_monte_carlo        | 66.8 ms                                                | 65.2 ms: 1.02x faster                                                       |
| 2to3                       | 266 ms                                                 | 260 ms: 1.02x faster                                                        |
| sympy_integrate            | 19.8 ms                                                | 19.4 ms: 1.02x faster                                                       |
| meteor_contest             | 108 ms                                                 | 106 ms: 1.02x faster                                                        |
| deltablue                  | 3.19 ms                                                | 3.13 ms: 1.02x faster                                                       |
| pathlib                    | 17.4 ms                                                | 17.1 ms: 1.02x faster                                                       |
| async_generators           | 433 ms                                                 | 430 ms: 1.01x faster                                                        |
| python_startup_no_site     | 7.00 ms                                                | 6.97 ms: 1.00x faster                                                       |
| asyncio_websockets         | 551 ms                                                 | 554 ms: 1.00x slower                                                        |
| fannkuch                   | 394 ms                                                 | 397 ms: 1.01x slower                                                        |
| mako                       | 10.7 ms                                                | 10.8 ms: 1.01x slower                                                       |
| pidigits                   | 186 ms                                                 | 188 ms: 1.01x slower                                                        |
| nqueens                    | 80.9 ms                                                | 81.7 ms: 1.01x slower                                                       |
| crypto_pyaes               | 74.7 ms                                                | 75.5 ms: 1.01x slower                                                       |
| genshi_xml                 | 50.5 ms                                                | 51.2 ms: 1.01x slower                                                       |
| shortest_path              | 487 ms                                                 | 495 ms: 1.02x slower                                                        |
| scimark_lu                 | 114 ms                                                 | 117 ms: 1.02x slower                                                        |
| docutils                   | 2.58 sec                                               | 2.65 sec: 1.03x slower                                                      |
| connected_components       | 447 ms                                                 | 459 ms: 1.03x slower                                                        |
| sympy_expand               | 456 ms                                                 | 469 ms: 1.03x slower                                                        |
| nbody                      | 87.7 ms                                                | 90.3 ms: 1.03x slower                                                       |
| comprehensions             | 16.5 us                                                | 17.0 us: 1.03x slower                                                       |
| django_template            | 31.7 ms                                                | 32.7 ms: 1.03x slower                                                       |
| generators                 | 28.8 ms                                                | 30.0 ms: 1.04x slower                                                       |
| typing_runtime_protocols   | 160 us                                                 | 167 us: 1.04x slower                                                        |
| chaos                      | 58.0 ms                                                | 60.6 ms: 1.04x slower                                                       |
| raytrace                   | 262 ms                                                 | 273 ms: 1.05x slower                                                        |
| coverage                   | 82.8 ms                                                | 87.6 ms: 1.06x slower                                                       |
| json_loads                 | 27.2 us                                                | 28.8 us: 1.06x slower                                                       |
| create_gc_cycles           | 2.45 ms                                                | 2.60 ms: 1.06x slower                                                       |
| hexiom                     | 6.08 ms                                                | 6.45 ms: 1.06x slower                                                       |
| pickle_pure_python         | 302 us                                                 | 323 us: 1.07x slower                                                        |
| json_dumps                 | 10.1 ms                                                | 10.9 ms: 1.08x slower                                                       |
| logging_format             | 6.23 us                                                | 6.77 us: 1.09x slower                                                       |
| logging_simple             | 5.65 us                                                | 6.15 us: 1.09x slower                                                       |
| pprint_safe_repr           | 727 ms                                                 | 803 ms: 1.11x slower                                                        |
| pprint_pformat             | 1.48 sec                                               | 1.66 sec: 1.12x slower                                                      |
| many_optionals             | 857 us                                                 | 981 us: 1.14x slower                                                        |
| coroutines                 | 22.2 ms                                                | 25.5 ms: 1.15x slower                                                       |
| subparsers                 | 15.5 ms                                                | 23.8 ms: 1.54x slower                                                       |
| logging_silent             | 101 ns                                                 | 473 ns: 4.68x slower                                                        |
| Geometric mean             | (ref)                                                  | 1.04x faster                                                                |

Benchmark hidden because not significant (5): sphinx, json, sympy_str, sympy_sum, djangocms
Ignored benchmarks (12) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: bench_mp_pool, bench_thread_pool, chameleon, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250625-3.15.0a0-96ee078-JIT/bm-20250625-linux-x86_64-Fidget%2dSpinner-decref_for_nbody-3.15.0a0-96ee078.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.056x faster

# HPT report

- Reliability score: 99.82% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.07x
# Results vs. 3.13.0

- fork: faster-cpython
- ref: specialize_for_compa
- machine: linux-x86_64
- commit hash: e27d994
- commit date: 2025-06-18
- overall geometric mean: 1.049x faster
- HPT reliability: 99.99%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.06x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250618-linux-x86_64-faster%2dcpython-specialize_for_compa-3.15.0a0-e27d994 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 254 ms: 1.05x faster                                                            |
| docutils       | 2.58 sec                                               | 2.56 sec: 1.01x faster                                                          |
| html5lib       | 63.4 ms                                                | 61.9 ms: 1.02x faster                                                           |
| sphinx         | 1.03 sec                                               | 1.01 sec: 1.03x faster                                                          |
| Geometric mean | (ref)                                                  | 1.03x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250618-linux-x86_64-faster%2dcpython-specialize_for_compa-3.15.0a0-e27d994 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 306 ms: 1.51x faster                                                            |
| async_tree_memoization     | 437 ms                                                 | 309 ms: 1.41x faster                                                            |
| async_tree_io              | 838 ms                                                 | 595 ms: 1.41x faster                                                            |
| async_tree_io_tg           | 861 ms                                                 | 628 ms: 1.37x faster                                                            |
| async_tree_none            | 350 ms                                                 | 258 ms: 1.36x faster                                                            |
| async_tree_none_tg         | 319 ms                                                 | 247 ms: 1.29x faster                                                            |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 488 ms: 1.17x faster                                                            |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 479 ms: 1.14x faster                                                            |
| async_generators           | 433 ms                                                 | 410 ms: 1.06x faster                                                            |
| coroutines                 | 22.2 ms                                                | 24.5 ms: 1.10x slower                                                           |
| Geometric mean             | (ref)                                                  | 1.22x faster                                                                    |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250618-linux-x86_64-faster%2dcpython-specialize_for_compa-3.15.0a0-e27d994 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 72.5 ms: 1.08x faster                                                           |
| pidigits       | 186 ms                                                 | 188 ms: 1.01x slower                                                            |
| nbody          | 87.7 ms                                                | 98.5 ms: 1.12x slower                                                           |
| Geometric mean | (ref)                                                  | 1.02x slower                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250618-linux-x86_64-faster%2dcpython-specialize_for_compa-3.15.0a0-e27d994 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_v8       | 26.9 ms                                                | 22.2 ms: 1.21x faster                                                           |
| regex_effbot   | 3.77 ms                                                | 3.27 ms: 1.15x faster                                                           |
| regex_dna      | 220 ms                                                 | 203 ms: 1.09x faster                                                            |
| regex_compile  | 132 ms                                                 | 126 ms: 1.05x faster                                                            |
| Geometric mean | (ref)                                                  | 1.12x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250618-linux-x86_64-faster%2dcpython-specialize_for_compa-3.15.0a0-e27d994 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| xml_etree_parse      | 154 ms                                                 | 141 ms: 1.09x faster                                                            |
| tomli_loads          | 2.12 sec                                               | 1.96 sec: 1.08x faster                                                          |
| xml_etree_iterparse  | 101 ms                                                 | 98.0 ms: 1.03x faster                                                           |
| xml_etree_generate   | 86.8 ms                                                | 85.1 ms: 1.02x faster                                                           |
| xml_etree_process    | 60.5 ms                                                | 59.9 ms: 1.01x faster                                                           |
| unpickle_pure_python | 213 us                                                 | 217 us: 1.02x slower                                                            |
| json_loads           | 27.2 us                                                | 28.0 us: 1.03x slower                                                           |
| pickle_pure_python   | 302 us                                                 | 319 us: 1.06x slower                                                            |
| json_dumps           | 10.1 ms                                                | 11.1 ms: 1.10x slower                                                           |
| Geometric mean       | (ref)                                                  | 1.00x faster                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250618-linux-x86_64-faster%2dcpython-specialize_for_compa-3.15.0a0-e27d994 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 12.7 ms                                                | 12.2 ms: 1.04x faster                                                           |
| python_startup_no_site | 7.00 ms                                                | 6.91 ms: 1.01x faster                                                           |
| Geometric mean         | (ref)                                                  | 1.03x faster                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250618-linux-x86_64-faster%2dcpython-specialize_for_compa-3.15.0a0-e27d994 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| genshi_text     | 22.6 ms                                                | 21.1 ms: 1.07x faster                                                           |
| genshi_xml      | 50.5 ms                                                | 49.3 ms: 1.02x faster                                                           |
| django_template | 31.7 ms                                                | 32.9 ms: 1.04x slower                                                           |
| mako            | 10.7 ms                                                | 11.7 ms: 1.10x slower                                                           |
| Geometric mean  | (ref)                                                  | 1.01x slower                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250618-linux-x86_64-faster%2dcpython-specialize_for_compa-3.15.0a0-e27d994 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mdp                        | 2.54 sec                                               | 1.22 sec: 2.08x faster                                                          |
| async_tree_memoization_tg  | 463 ms                                                 | 306 ms: 1.51x faster                                                            |
| async_tree_memoization     | 437 ms                                                 | 309 ms: 1.41x faster                                                            |
| async_tree_io              | 838 ms                                                 | 595 ms: 1.41x faster                                                            |
| deepcopy                   | 354 us                                                 | 255 us: 1.39x faster                                                            |
| async_tree_io_tg           | 861 ms                                                 | 628 ms: 1.37x faster                                                            |
| async_tree_none            | 350 ms                                                 | 258 ms: 1.36x faster                                                            |
| deepcopy_memo              | 38.4 us                                                | 29.1 us: 1.32x faster                                                           |
| async_tree_none_tg         | 319 ms                                                 | 247 ms: 1.29x faster                                                            |
| go                         | 141 ms                                                 | 111 ms: 1.27x faster                                                            |
| regex_v8                   | 26.9 ms                                                | 22.2 ms: 1.21x faster                                                           |
| deepcopy_reduce            | 3.24 us                                                | 2.68 us: 1.21x faster                                                           |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 488 ms: 1.17x faster                                                            |
| regex_effbot               | 3.77 ms                                                | 3.27 ms: 1.15x faster                                                           |
| spectral_norm              | 113 ms                                                 | 99.3 ms: 1.14x faster                                                           |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 479 ms: 1.14x faster                                                            |
| pylint                     | 312 ms                                                 | 277 ms: 1.12x faster                                                            |
| pyflate                    | 470 ms                                                 | 419 ms: 1.12x faster                                                            |
| dulwich_log                | 64.6 ms                                                | 58.8 ms: 1.10x faster                                                           |
| richards                   | 47.5 ms                                                | 43.3 ms: 1.10x faster                                                           |
| xml_etree_parse            | 154 ms                                                 | 141 ms: 1.09x faster                                                            |
| regex_dna                  | 220 ms                                                 | 203 ms: 1.09x faster                                                            |
| float                      | 78.7 ms                                                | 72.5 ms: 1.08x faster                                                           |
| richards_super             | 53.7 ms                                                | 49.6 ms: 1.08x faster                                                           |
| tomli_loads                | 2.12 sec                                               | 1.96 sec: 1.08x faster                                                          |
| genshi_text                | 22.6 ms                                                | 21.1 ms: 1.07x faster                                                           |
| pycparser                  | 1.20 sec                                               | 1.12 sec: 1.07x faster                                                          |
| async_generators           | 433 ms                                                 | 410 ms: 1.06x faster                                                            |
| sympy_integrate            | 19.8 ms                                                | 18.9 ms: 1.05x faster                                                           |
| bpe_tokeniser              | 4.69 sec                                               | 4.48 sec: 1.05x faster                                                          |
| thrift                     | 800 us                                                 | 764 us: 1.05x faster                                                            |
| 2to3                       | 266 ms                                                 | 254 ms: 1.05x faster                                                            |
| regex_compile              | 132 ms                                                 | 126 ms: 1.05x faster                                                            |
| telco                      | 8.40 ms                                                | 8.04 ms: 1.04x faster                                                           |
| python_startup             | 12.7 ms                                                | 12.2 ms: 1.04x faster                                                           |
| k_core                     | 2.37 sec                                               | 2.28 sec: 1.04x faster                                                          |
| xml_etree_iterparse        | 101 ms                                                 | 98.0 ms: 1.03x faster                                                           |
| scimark_sor                | 122 ms                                                 | 118 ms: 1.03x faster                                                            |
| sympy_str                  | 273 ms                                                 | 265 ms: 1.03x faster                                                            |
| sphinx                     | 1.03 sec                                               | 1.01 sec: 1.03x faster                                                          |
| pathlib                    | 17.4 ms                                                | 17.0 ms: 1.02x faster                                                           |
| comprehensions             | 16.5 us                                                | 16.1 us: 1.02x faster                                                           |
| html5lib                   | 63.4 ms                                                | 61.9 ms: 1.02x faster                                                           |
| genshi_xml                 | 50.5 ms                                                | 49.3 ms: 1.02x faster                                                           |
| sympy_sum                  | 150 ms                                                 | 147 ms: 1.02x faster                                                            |
| meteor_contest             | 108 ms                                                 | 106 ms: 1.02x faster                                                            |
| xml_etree_generate         | 86.8 ms                                                | 85.1 ms: 1.02x faster                                                           |
| sympy_expand               | 456 ms                                                 | 449 ms: 1.02x faster                                                            |
| sqlite_synth               | 2.90 us                                                | 2.86 us: 1.01x faster                                                           |
| scimark_fft                | 367 ms                                                 | 362 ms: 1.01x faster                                                            |
| scimark_monte_carlo        | 66.8 ms                                                | 65.9 ms: 1.01x faster                                                           |
| python_startup_no_site     | 7.00 ms                                                | 6.91 ms: 1.01x faster                                                           |
| hexiom                     | 6.08 ms                                                | 6.00 ms: 1.01x faster                                                           |
| json                       | 5.32 ms                                                | 5.26 ms: 1.01x faster                                                           |
| xml_etree_process          | 60.5 ms                                                | 59.9 ms: 1.01x faster                                                           |
| docutils                   | 2.58 sec                                               | 2.56 sec: 1.01x faster                                                          |
| nqueens                    | 80.9 ms                                                | 80.3 ms: 1.01x faster                                                           |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 5.06 ms: 1.01x slower                                                           |
| pidigits                   | 186 ms                                                 | 188 ms: 1.01x slower                                                            |
| unpickle_pure_python       | 213 us                                                 | 217 us: 1.02x slower                                                            |
| typing_runtime_protocols   | 160 us                                                 | 164 us: 1.02x slower                                                            |
| crypto_pyaes               | 74.7 ms                                                | 76.4 ms: 1.02x slower                                                           |
| chaos                      | 58.0 ms                                                | 59.4 ms: 1.02x slower                                                           |
| raytrace                   | 262 ms                                                 | 270 ms: 1.03x slower                                                            |
| json_loads                 | 27.2 us                                                | 28.0 us: 1.03x slower                                                           |
| generators                 | 28.8 ms                                                | 29.7 ms: 1.03x slower                                                           |
| scimark_lu                 | 114 ms                                                 | 118 ms: 1.03x slower                                                            |
| fannkuch                   | 394 ms                                                 | 407 ms: 1.03x slower                                                            |
| django_template            | 31.7 ms                                                | 32.9 ms: 1.04x slower                                                           |
| gc_traversal               | 4.90 ms                                                | 5.11 ms: 1.04x slower                                                           |
| create_gc_cycles           | 2.45 ms                                                | 2.57 ms: 1.05x slower                                                           |
| connected_components       | 447 ms                                                 | 471 ms: 1.05x slower                                                            |
| pickle_pure_python         | 302 us                                                 | 319 us: 1.06x slower                                                            |
| coverage                   | 82.8 ms                                                | 87.8 ms: 1.06x slower                                                           |
| shortest_path              | 487 ms                                                 | 516 ms: 1.06x slower                                                            |
| logging_format             | 6.23 us                                                | 6.65 us: 1.07x slower                                                           |
| logging_simple             | 5.65 us                                                | 6.05 us: 1.07x slower                                                           |
| deltablue                  | 3.19 ms                                                | 3.49 ms: 1.09x slower                                                           |
| pprint_safe_repr           | 727 ms                                                 | 797 ms: 1.10x slower                                                            |
| mako                       | 10.7 ms                                                | 11.7 ms: 1.10x slower                                                           |
| json_dumps                 | 10.1 ms                                                | 11.1 ms: 1.10x slower                                                           |
| coroutines                 | 22.2 ms                                                | 24.5 ms: 1.10x slower                                                           |
| pprint_pformat             | 1.48 sec                                               | 1.63 sec: 1.10x slower                                                          |
| many_optionals             | 857 us                                                 | 957 us: 1.12x slower                                                            |
| nbody                      | 87.7 ms                                                | 98.5 ms: 1.12x slower                                                           |
| subparsers                 | 15.5 ms                                                | 23.4 ms: 1.52x slower                                                           |
| logging_silent             | 101 ns                                                 | 469 ns: 4.64x slower                                                            |
| Geometric mean             | (ref)                                                  | 1.03x faster                                                                    |

Benchmark hidden because not significant (2): djangocms, asyncio_websockets
Ignored benchmarks (12) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: bench_mp_pool, bench_thread_pool, chameleon, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250618-3.15.0a0-e27d994/bm-20250618-linux-x86_64-faster%2dcpython-specialize_for_compa-3.15.0a0-e27d994.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.049x faster

# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.06x
# Results vs. 3.13.0

- fork: brandtbucher
- ref: justin_hot
- machine: linux-x86_64
- commit hash: a987be7
- commit date: 2025-06-23
- overall geometric mean: 1.059x faster
- HPT reliability: 99.92%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250623-linux-x86_64-brandtbucher-justin_hot-3.15.0a0-a987be7 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 259 ms: 1.03x faster                                              |
| docutils       | 2.58 sec                                               | 2.64 sec: 1.02x slower                                            |
| html5lib       | 63.4 ms                                                | 61.9 ms: 1.02x faster                                             |
| Geometric mean | (ref)                                                  | 1.01x faster                                                      |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250623-linux-x86_64-brandtbucher-justin_hot-3.15.0a0-a987be7 |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 317 ms: 1.46x faster                                              |
| async_tree_io              | 838 ms                                                 | 598 ms: 1.40x faster                                              |
| async_tree_memoization     | 437 ms                                                 | 312 ms: 1.40x faster                                              |
| async_tree_io_tg           | 861 ms                                                 | 616 ms: 1.40x faster                                              |
| async_tree_none            | 350 ms                                                 | 261 ms: 1.34x faster                                              |
| async_tree_none_tg         | 319 ms                                                 | 250 ms: 1.28x faster                                              |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 495 ms: 1.16x faster                                              |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 490 ms: 1.11x faster                                              |
| async_generators           | 433 ms                                                 | 431 ms: 1.00x faster                                              |
| coroutines                 | 22.2 ms                                                | 24.9 ms: 1.12x slower                                             |
| Geometric mean             | (ref)                                                  | 1.21x faster                                                      |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250623-linux-x86_64-brandtbucher-justin_hot-3.15.0a0-a987be7 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| float          | 78.7 ms                                                | 65.0 ms: 1.21x faster                                             |
| pidigits       | 186 ms                                                 | 187 ms: 1.00x slower                                              |
| nbody          | 87.7 ms                                                | 96.0 ms: 1.09x slower                                             |
| Geometric mean | (ref)                                                  | 1.03x faster                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250623-linux-x86_64-brandtbucher-justin_hot-3.15.0a0-a987be7 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| regex_v8       | 26.9 ms                                                | 22.5 ms: 1.19x faster                                             |
| regex_effbot   | 3.77 ms                                                | 3.25 ms: 1.16x faster                                             |
| regex_dna      | 220 ms                                                 | 199 ms: 1.11x faster                                              |
| regex_compile  | 132 ms                                                 | 127 ms: 1.04x faster                                              |
| Geometric mean | (ref)                                                  | 1.12x faster                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250623-linux-x86_64-brandtbucher-justin_hot-3.15.0a0-a987be7 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| tomli_loads          | 2.12 sec                                               | 1.86 sec: 1.14x faster                                            |
| unpickle_pure_python | 213 us                                                 | 195 us: 1.09x faster                                              |
| xml_etree_parse      | 154 ms                                                 | 141 ms: 1.09x faster                                              |
| xml_etree_process    | 60.5 ms                                                | 55.4 ms: 1.09x faster                                             |
| xml_etree_generate   | 86.8 ms                                                | 80.0 ms: 1.08x faster                                             |
| xml_etree_iterparse  | 101 ms                                                 | 98.3 ms: 1.03x faster                                             |
| json_loads           | 27.2 us                                                | 28.2 us: 1.04x slower                                             |
| pickle_pure_python   | 302 us                                                 | 320 us: 1.06x slower                                              |
| json_dumps           | 10.1 ms                                                | 10.9 ms: 1.07x slower                                             |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                      |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250623-linux-x86_64-brandtbucher-justin_hot-3.15.0a0-a987be7 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| python_startup         | 12.7 ms                                                | 12.2 ms: 1.04x faster                                             |
| python_startup_no_site | 7.00 ms                                                | 6.93 ms: 1.01x faster                                             |
| Geometric mean         | (ref)                                                  | 1.03x faster                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250623-linux-x86_64-brandtbucher-justin_hot-3.15.0a0-a987be7 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| genshi_text     | 22.6 ms                                                | 21.1 ms: 1.07x faster                                             |
| mako            | 10.7 ms                                                | 10.4 ms: 1.02x faster                                             |
| django_template | 31.7 ms                                                | 32.4 ms: 1.02x slower                                             |
| Geometric mean  | (ref)                                                  | 1.02x faster                                                      |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250623-linux-x86_64-brandtbucher-justin_hot-3.15.0a0-a987be7 |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| mdp                        | 2.54 sec                                               | 1.25 sec: 2.04x faster                                            |
| async_tree_memoization_tg  | 463 ms                                                 | 317 ms: 1.46x faster                                              |
| richards                   | 47.5 ms                                                | 32.9 ms: 1.44x faster                                             |
| async_tree_io              | 838 ms                                                 | 598 ms: 1.40x faster                                              |
| async_tree_memoization     | 437 ms                                                 | 312 ms: 1.40x faster                                              |
| async_tree_io_tg           | 861 ms                                                 | 616 ms: 1.40x faster                                              |
| richards_super             | 53.7 ms                                                | 38.6 ms: 1.39x faster                                             |
| deepcopy                   | 354 us                                                 | 259 us: 1.37x faster                                              |
| async_tree_none            | 350 ms                                                 | 261 ms: 1.34x faster                                              |
| deepcopy_memo              | 38.4 us                                                | 29.8 us: 1.29x faster                                             |
| async_tree_none_tg         | 319 ms                                                 | 250 ms: 1.28x faster                                              |
| float                      | 78.7 ms                                                | 65.0 ms: 1.21x faster                                             |
| go                         | 141 ms                                                 | 117 ms: 1.20x faster                                              |
| regex_v8                   | 26.9 ms                                                | 22.5 ms: 1.19x faster                                             |
| deepcopy_reduce            | 3.24 us                                                | 2.73 us: 1.19x faster                                             |
| regex_effbot               | 3.77 ms                                                | 3.25 ms: 1.16x faster                                             |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 495 ms: 1.16x faster                                              |
| pyflate                    | 470 ms                                                 | 406 ms: 1.16x faster                                              |
| tomli_loads                | 2.12 sec                                               | 1.86 sec: 1.14x faster                                            |
| scimark_fft                | 367 ms                                                 | 328 ms: 1.12x faster                                              |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 490 ms: 1.11x faster                                              |
| telco                      | 8.40 ms                                                | 7.59 ms: 1.11x faster                                             |
| regex_dna                  | 220 ms                                                 | 199 ms: 1.11x faster                                              |
| spectral_norm              | 113 ms                                                 | 103 ms: 1.10x faster                                              |
| pylint                     | 312 ms                                                 | 282 ms: 1.10x faster                                              |
| unpickle_pure_python       | 213 us                                                 | 195 us: 1.09x faster                                              |
| xml_etree_parse            | 154 ms                                                 | 141 ms: 1.09x faster                                              |
| xml_etree_process          | 60.5 ms                                                | 55.4 ms: 1.09x faster                                             |
| xml_etree_generate         | 86.8 ms                                                | 80.0 ms: 1.08x faster                                             |
| dulwich_log                | 64.6 ms                                                | 59.6 ms: 1.08x faster                                             |
| genshi_text                | 22.6 ms                                                | 21.1 ms: 1.07x faster                                             |
| bpe_tokeniser              | 4.69 sec                                               | 4.38 sec: 1.07x faster                                            |
| pycparser                  | 1.20 sec                                               | 1.12 sec: 1.07x faster                                            |
| deltablue                  | 3.19 ms                                                | 3.06 ms: 1.04x faster                                             |
| python_startup             | 12.7 ms                                                | 12.2 ms: 1.04x faster                                             |
| regex_compile              | 132 ms                                                 | 127 ms: 1.04x faster                                              |
| sqlite_synth               | 2.90 us                                                | 2.80 us: 1.03x faster                                             |
| k_core                     | 2.37 sec                                               | 2.29 sec: 1.03x faster                                            |
| xml_etree_iterparse        | 101 ms                                                 | 98.3 ms: 1.03x faster                                             |
| 2to3                       | 266 ms                                                 | 259 ms: 1.03x faster                                              |
| pathlib                    | 17.4 ms                                                | 17.0 ms: 1.03x faster                                             |
| sympy_integrate            | 19.8 ms                                                | 19.4 ms: 1.02x faster                                             |
| thrift                     | 800 us                                                 | 781 us: 1.02x faster                                              |
| mako                       | 10.7 ms                                                | 10.4 ms: 1.02x faster                                             |
| html5lib                   | 63.4 ms                                                | 61.9 ms: 1.02x faster                                             |
| json                       | 5.32 ms                                                | 5.23 ms: 1.02x faster                                             |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.94 ms: 1.02x faster                                             |
| meteor_contest             | 108 ms                                                 | 107 ms: 1.02x faster                                              |
| comprehensions             | 16.5 us                                                | 16.3 us: 1.01x faster                                             |
| python_startup_no_site     | 7.00 ms                                                | 6.93 ms: 1.01x faster                                             |
| async_generators           | 433 ms                                                 | 431 ms: 1.00x faster                                              |
| sympy_sum                  | 150 ms                                                 | 150 ms: 1.00x faster                                              |
| crypto_pyaes               | 74.7 ms                                                | 74.4 ms: 1.00x faster                                             |
| pidigits                   | 186 ms                                                 | 187 ms: 1.00x slower                                              |
| scimark_sor                | 122 ms                                                 | 123 ms: 1.00x slower                                              |
| connected_components       | 447 ms                                                 | 454 ms: 1.01x slower                                              |
| gc_traversal               | 4.90 ms                                                | 4.97 ms: 1.02x slower                                             |
| docutils                   | 2.58 sec                                               | 2.64 sec: 1.02x slower                                            |
| nqueens                    | 80.9 ms                                                | 82.6 ms: 1.02x slower                                             |
| sympy_expand               | 456 ms                                                 | 466 ms: 1.02x slower                                              |
| fannkuch                   | 394 ms                                                 | 403 ms: 1.02x slower                                              |
| django_template            | 31.7 ms                                                | 32.4 ms: 1.02x slower                                             |
| json_loads                 | 27.2 us                                                | 28.2 us: 1.04x slower                                             |
| hexiom                     | 6.08 ms                                                | 6.30 ms: 1.04x slower                                             |
| scimark_lu                 | 114 ms                                                 | 119 ms: 1.04x slower                                              |
| raytrace                   | 262 ms                                                 | 273 ms: 1.04x slower                                              |
| coverage                   | 82.8 ms                                                | 87.0 ms: 1.05x slower                                             |
| typing_runtime_protocols   | 160 us                                                 | 169 us: 1.05x slower                                              |
| generators                 | 28.8 ms                                                | 30.4 ms: 1.06x slower                                             |
| pickle_pure_python         | 302 us                                                 | 320 us: 1.06x slower                                              |
| create_gc_cycles           | 2.45 ms                                                | 2.60 ms: 1.06x slower                                             |
| chaos                      | 58.0 ms                                                | 62.3 ms: 1.07x slower                                             |
| json_dumps                 | 10.1 ms                                                | 10.9 ms: 1.07x slower                                             |
| logging_simple             | 5.65 us                                                | 6.11 us: 1.08x slower                                             |
| logging_format             | 6.23 us                                                | 6.74 us: 1.08x slower                                             |
| nbody                      | 87.7 ms                                                | 96.0 ms: 1.09x slower                                             |
| pprint_safe_repr           | 727 ms                                                 | 804 ms: 1.11x slower                                              |
| pprint_pformat             | 1.48 sec                                               | 1.64 sec: 1.11x slower                                            |
| coroutines                 | 22.2 ms                                                | 24.9 ms: 1.12x slower                                             |
| many_optionals             | 857 us                                                 | 982 us: 1.15x slower                                              |
| subparsers                 | 15.5 ms                                                | 23.5 ms: 1.52x slower                                             |
| logging_silent             | 101 ns                                                 | 472 ns: 4.67x slower                                              |
| Geometric mean             | (ref)                                                  | 1.04x faster                                                      |

Benchmark hidden because not significant (7): sphinx, djangocms, sympy_str, scimark_monte_carlo, genshi_xml, asyncio_websockets, shortest_path
Ignored benchmarks (12) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: bench_mp_pool, bench_thread_pool, chameleon, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250623-3.15.0a0-a987be7-JIT/bm-20250623-linux-x86_64-brandtbucher-justin_hot-3.15.0a0-a987be7.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.059x faster

# HPT report

- Reliability score: 99.92% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.07x
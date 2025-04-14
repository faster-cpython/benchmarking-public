# Results vs. 3.13.0

- fork: brandtbucher
- ref: jit_guard_dict_tuple
- machine: linux-x86_64
- commit hash: 99d6288
- commit date: 2025-04-01
- overall geometric mean: 1.061x faster
- HPT reliability: 99.99%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.05x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250401-linux-x86_64-brandtbucher-jit_guard_dict_tuple-3.14.0a6+-99d6288 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 258 ms: 1.03x faster                                                         |
| docutils       | 2.58 sec                                               | 2.68 sec: 1.04x slower                                                       |
| html5lib       | 63.4 ms                                                | 61.0 ms: 1.04x faster                                                        |
| Geometric mean | (ref)                                                  | 1.01x faster                                                                 |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250401-linux-x86_64-brandtbucher-jit_guard_dict_tuple-3.14.0a6+-99d6288 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 316 ms: 1.47x faster                                                         |
| async_tree_io_tg           | 861 ms                                                 | 611 ms: 1.41x faster                                                         |
| async_tree_memoization     | 437 ms                                                 | 311 ms: 1.41x faster                                                         |
| async_tree_io              | 838 ms                                                 | 613 ms: 1.37x faster                                                         |
| async_tree_none            | 350 ms                                                 | 259 ms: 1.35x faster                                                         |
| async_tree_none_tg         | 319 ms                                                 | 251 ms: 1.27x faster                                                         |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 490 ms: 1.17x faster                                                         |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 477 ms: 1.14x faster                                                         |
| async_generators           | 433 ms                                                 | 413 ms: 1.05x faster                                                         |
| coroutines                 | 22.2 ms                                                | 23.6 ms: 1.06x slower                                                        |
| Geometric mean             | (ref)                                                  | 1.22x faster                                                                 |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250401-linux-x86_64-brandtbucher-jit_guard_dict_tuple-3.14.0a6+-99d6288 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 61.6 ms: 1.28x faster                                                        |
| nbody          | 87.7 ms                                                | 84.0 ms: 1.04x faster                                                        |
| pidigits       | 186 ms                                                 | 186 ms: 1.00x faster                                                         |
| Geometric mean | (ref)                                                  | 1.10x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250401-linux-x86_64-brandtbucher-jit_guard_dict_tuple-3.14.0a6+-99d6288 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                | 3.15 ms: 1.20x faster                                                        |
| regex_v8       | 26.9 ms                                                | 23.1 ms: 1.16x faster                                                        |
| regex_dna      | 220 ms                                                 | 205 ms: 1.07x faster                                                         |
| regex_compile  | 132 ms                                                 | 127 ms: 1.04x faster                                                         |
| Geometric mean | (ref)                                                  | 1.11x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250401-linux-x86_64-brandtbucher-jit_guard_dict_tuple-3.14.0a6+-99d6288 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| tomli_loads          | 2.12 sec                                               | 1.83 sec: 1.16x faster                                                       |
| xml_etree_parse      | 154 ms                                                 | 141 ms: 1.10x faster                                                         |
| xml_etree_generate   | 86.8 ms                                                | 79.6 ms: 1.09x faster                                                        |
| xml_etree_process    | 60.5 ms                                                | 56.5 ms: 1.07x faster                                                        |
| xml_etree_iterparse  | 101 ms                                                 | 98.2 ms: 1.03x faster                                                        |
| unpickle_pure_python | 213 us                                                 | 209 us: 1.02x faster                                                         |
| pickle_pure_python   | 302 us                                                 | 320 us: 1.06x slower                                                         |
| json_loads           | 27.2 us                                                | 29.7 us: 1.09x slower                                                        |
| json_dumps           | 10.1 ms                                                | 11.5 ms: 1.14x slower                                                        |
| Geometric mean       | (ref)                                                  | 1.02x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250401-linux-x86_64-brandtbucher-jit_guard_dict_tuple-3.14.0a6+-99d6288 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 12.7 ms                                                | 13.2 ms: 1.04x slower                                                        |
| python_startup_no_site | 7.00 ms                                                | 8.21 ms: 1.17x slower                                                        |
| Geometric mean         | (ref)                                                  | 1.10x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250401-linux-x86_64-brandtbucher-jit_guard_dict_tuple-3.14.0a6+-99d6288 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| genshi_text     | 22.6 ms                                                | 21.4 ms: 1.06x faster                                                        |
| genshi_xml      | 50.5 ms                                                | 49.3 ms: 1.02x faster                                                        |
| django_template | 31.7 ms                                                | 31.8 ms: 1.00x slower                                                        |
| mako            | 10.7 ms                                                | 10.9 ms: 1.03x slower                                                        |
| Geometric mean  | (ref)                                                  | 1.01x faster                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250401-linux-x86_64-brandtbucher-jit_guard_dict_tuple-3.14.0a6+-99d6288 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mdp                        | 2.54 sec                                               | 1.22 sec: 2.08x faster                                                       |
| async_tree_memoization_tg  | 463 ms                                                 | 316 ms: 1.47x faster                                                         |
| async_tree_io_tg           | 861 ms                                                 | 611 ms: 1.41x faster                                                         |
| async_tree_memoization     | 437 ms                                                 | 311 ms: 1.41x faster                                                         |
| deepcopy                   | 354 us                                                 | 254 us: 1.40x faster                                                         |
| async_tree_io              | 838 ms                                                 | 613 ms: 1.37x faster                                                         |
| richards                   | 47.5 ms                                                | 34.9 ms: 1.36x faster                                                        |
| richards_super             | 53.7 ms                                                | 39.6 ms: 1.36x faster                                                        |
| async_tree_none            | 350 ms                                                 | 259 ms: 1.35x faster                                                         |
| deepcopy_memo              | 38.4 us                                                | 29.2 us: 1.31x faster                                                        |
| float                      | 78.7 ms                                                | 61.6 ms: 1.28x faster                                                        |
| async_tree_none_tg         | 319 ms                                                 | 251 ms: 1.27x faster                                                         |
| deepcopy_reduce            | 3.24 us                                                | 2.68 us: 1.21x faster                                                        |
| regex_effbot               | 3.77 ms                                                | 3.15 ms: 1.20x faster                                                        |
| scimark_fft                | 367 ms                                                 | 307 ms: 1.19x faster                                                         |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 490 ms: 1.17x faster                                                         |
| regex_v8                   | 26.9 ms                                                | 23.1 ms: 1.16x faster                                                        |
| tomli_loads                | 2.12 sec                                               | 1.83 sec: 1.16x faster                                                       |
| spectral_norm              | 113 ms                                                 | 99.1 ms: 1.14x faster                                                        |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 477 ms: 1.14x faster                                                         |
| go                         | 141 ms                                                 | 125 ms: 1.13x faster                                                         |
| pylint                     | 312 ms                                                 | 280 ms: 1.11x faster                                                         |
| xml_etree_parse            | 154 ms                                                 | 141 ms: 1.10x faster                                                         |
| xml_etree_generate         | 86.8 ms                                                | 79.6 ms: 1.09x faster                                                        |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.63 ms: 1.09x faster                                                        |
| pycparser                  | 1.20 sec                                               | 1.12 sec: 1.07x faster                                                       |
| regex_dna                  | 220 ms                                                 | 205 ms: 1.07x faster                                                         |
| xml_etree_process          | 60.5 ms                                                | 56.5 ms: 1.07x faster                                                        |
| telco                      | 8.40 ms                                                | 7.86 ms: 1.07x faster                                                        |
| dulwich_log                | 64.6 ms                                                | 60.6 ms: 1.07x faster                                                        |
| sqlite_synth               | 2.90 us                                                | 2.72 us: 1.07x faster                                                        |
| pyflate                    | 470 ms                                                 | 442 ms: 1.06x faster                                                         |
| genshi_text                | 22.6 ms                                                | 21.4 ms: 1.06x faster                                                        |
| async_generators           | 433 ms                                                 | 413 ms: 1.05x faster                                                         |
| pathlib                    | 17.4 ms                                                | 16.6 ms: 1.04x faster                                                        |
| nbody                      | 87.7 ms                                                | 84.0 ms: 1.04x faster                                                        |
| html5lib                   | 63.4 ms                                                | 61.0 ms: 1.04x faster                                                        |
| k_core                     | 2.37 sec                                               | 2.28 sec: 1.04x faster                                                       |
| regex_compile              | 132 ms                                                 | 127 ms: 1.04x faster                                                         |
| xml_etree_iterparse        | 101 ms                                                 | 98.2 ms: 1.03x faster                                                        |
| 2to3                       | 266 ms                                                 | 258 ms: 1.03x faster                                                         |
| bpe_tokeniser              | 4.69 sec                                               | 4.55 sec: 1.03x faster                                                       |
| deltablue                  | 3.19 ms                                                | 3.11 ms: 1.03x faster                                                        |
| scimark_sor                | 122 ms                                                 | 119 ms: 1.02x faster                                                         |
| genshi_xml                 | 50.5 ms                                                | 49.3 ms: 1.02x faster                                                        |
| chaos                      | 58.0 ms                                                | 57.0 ms: 1.02x faster                                                        |
| scimark_monte_carlo        | 66.8 ms                                                | 65.6 ms: 1.02x faster                                                        |
| unpickle_pure_python       | 213 us                                                 | 209 us: 1.02x faster                                                         |
| crypto_pyaes               | 74.7 ms                                                | 74.0 ms: 1.01x faster                                                        |
| sympy_integrate            | 19.8 ms                                                | 19.7 ms: 1.01x faster                                                        |
| raytrace                   | 262 ms                                                 | 260 ms: 1.00x faster                                                         |
| sqlalchemy_declarative     | 133 ms                                                 | 133 ms: 1.00x faster                                                         |
| pidigits                   | 186 ms                                                 | 186 ms: 1.00x faster                                                         |
| django_template            | 31.7 ms                                                | 31.8 ms: 1.00x slower                                                        |
| sqlalchemy_imperative      | 16.9 ms                                                | 17.0 ms: 1.01x slower                                                        |
| scimark_lu                 | 114 ms                                                 | 116 ms: 1.01x slower                                                         |
| logging_format             | 6.23 us                                                | 6.30 us: 1.01x slower                                                        |
| shortest_path              | 487 ms                                                 | 493 ms: 1.01x slower                                                         |
| connected_components       | 447 ms                                                 | 454 ms: 1.02x slower                                                         |
| create_gc_cycles           | 2.45 ms                                                | 2.49 ms: 1.02x slower                                                        |
| gc_traversal               | 4.90 ms                                                | 4.99 ms: 1.02x slower                                                        |
| nqueens                    | 80.9 ms                                                | 82.8 ms: 1.02x slower                                                        |
| mako                       | 10.7 ms                                                | 10.9 ms: 1.03x slower                                                        |
| generators                 | 28.8 ms                                                | 29.7 ms: 1.03x slower                                                        |
| sympy_expand               | 456 ms                                                 | 471 ms: 1.03x slower                                                         |
| pprint_safe_repr           | 727 ms                                                 | 751 ms: 1.03x slower                                                         |
| docutils                   | 2.58 sec                                               | 2.68 sec: 1.04x slower                                                       |
| coverage                   | 82.8 ms                                                | 86.0 ms: 1.04x slower                                                        |
| python_startup             | 12.7 ms                                                | 13.2 ms: 1.04x slower                                                        |
| pprint_pformat             | 1.48 sec                                               | 1.54 sec: 1.04x slower                                                       |
| fannkuch                   | 394 ms                                                 | 414 ms: 1.05x slower                                                         |
| typing_runtime_protocols   | 160 us                                                 | 169 us: 1.05x slower                                                         |
| pickle_pure_python         | 302 us                                                 | 320 us: 1.06x slower                                                         |
| coroutines                 | 22.2 ms                                                | 23.6 ms: 1.06x slower                                                        |
| bench_thread_pool          | 818 us                                                 | 887 us: 1.09x slower                                                         |
| json_loads                 | 27.2 us                                                | 29.7 us: 1.09x slower                                                        |
| many_optionals             | 857 us                                                 | 946 us: 1.10x slower                                                         |
| hexiom                     | 6.08 ms                                                | 6.72 ms: 1.11x slower                                                        |
| comprehensions             | 16.5 us                                                | 18.3 us: 1.11x slower                                                        |
| json_dumps                 | 10.1 ms                                                | 11.5 ms: 1.14x slower                                                        |
| python_startup_no_site     | 7.00 ms                                                | 8.21 ms: 1.17x slower                                                        |
| subparsers                 | 15.5 ms                                                | 20.8 ms: 1.35x slower                                                        |
| bench_mp_pool              | 24.0 ms                                                | 83.4 ms: 3.48x slower                                                        |
| Geometric mean             | (ref)                                                  | 1.04x faster                                                                 |

Benchmark hidden because not significant (8): sphinx, json, logging_silent, sympy_str, meteor_contest, asyncio_websockets, logging_simple, sympy_sum
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
Ignored benchmarks (4) of results/bm-20250401-3.14.0a6+-99d6288-JIT/bm-20250401-linux-x86_64-brandtbucher-jit_guard_dict_tuple-3.14.0a6+-99d6288.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.061x faster

# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.05x
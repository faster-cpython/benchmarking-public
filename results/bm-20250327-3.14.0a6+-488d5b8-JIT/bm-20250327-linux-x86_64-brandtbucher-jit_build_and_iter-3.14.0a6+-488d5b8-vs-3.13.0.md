# Results vs. 3.13.0

- fork: brandtbucher
- ref: jit_build_and_iter
- machine: linux-x86_64
- commit hash: 488d5b8
- commit date: 2025-03-27
- overall geometric mean: 1.038x faster
- HPT reliability: 97.08%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.05x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250327-linux-x86_64-brandtbucher-jit_build_and_iter-3.14.0a6+-488d5b8 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 264 ms: 1.01x faster                                                       |
| docutils       | 2.58 sec                                               | 2.69 sec: 1.04x slower                                                     |
| Geometric mean | (ref)                                                  | 1.01x slower                                                               |

Benchmark hidden because not significant (2): html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250327-linux-x86_64-brandtbucher-jit_build_and_iter-3.14.0a6+-488d5b8 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 315 ms: 1.47x faster                                                       |
| async_tree_io_tg           | 861 ms                                                 | 623 ms: 1.38x faster                                                       |
| async_tree_memoization     | 437 ms                                                 | 316 ms: 1.38x faster                                                       |
| async_tree_io              | 838 ms                                                 | 623 ms: 1.34x faster                                                       |
| async_tree_none            | 350 ms                                                 | 265 ms: 1.32x faster                                                       |
| async_tree_none_tg         | 319 ms                                                 | 254 ms: 1.26x faster                                                       |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 492 ms: 1.17x faster                                                       |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 477 ms: 1.14x faster                                                       |
| async_generators           | 433 ms                                                 | 412 ms: 1.05x faster                                                       |
| asyncio_websockets         | 551 ms                                                 | 553 ms: 1.00x slower                                                       |
| coroutines                 | 22.2 ms                                                | 23.3 ms: 1.05x slower                                                      |
| Geometric mean             | (ref)                                                  | 1.21x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250327-linux-x86_64-brandtbucher-jit_build_and_iter-3.14.0a6+-488d5b8 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 65.7 ms: 1.20x faster                                                      |
| pidigits       | 186 ms                                                 | 186 ms: 1.00x faster                                                       |
| nbody          | 87.7 ms                                                | 88.4 ms: 1.01x slower                                                      |
| Geometric mean | (ref)                                                  | 1.06x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250327-linux-x86_64-brandtbucher-jit_build_and_iter-3.14.0a6+-488d5b8 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                | 3.20 ms: 1.18x faster                                                      |
| regex_v8       | 26.9 ms                                                | 23.7 ms: 1.13x faster                                                      |
| regex_compile  | 132 ms                                                 | 129 ms: 1.03x faster                                                       |
| regex_dna      | 220 ms                                                 | 217 ms: 1.02x faster                                                       |
| Geometric mean | (ref)                                                  | 1.09x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250327-linux-x86_64-brandtbucher-jit_build_and_iter-3.14.0a6+-488d5b8 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| tomli_loads          | 2.12 sec                                               | 1.87 sec: 1.13x faster                                                     |
| xml_etree_parse      | 154 ms                                                 | 139 ms: 1.11x faster                                                       |
| xml_etree_generate   | 86.8 ms                                                | 80.7 ms: 1.08x faster                                                      |
| xml_etree_process    | 60.5 ms                                                | 56.6 ms: 1.07x faster                                                      |
| xml_etree_iterparse  | 101 ms                                                 | 97.9 ms: 1.03x faster                                                      |
| unpickle_pure_python | 213 us                                                 | 216 us: 1.01x slower                                                       |
| pickle_pure_python   | 302 us                                                 | 325 us: 1.08x slower                                                       |
| json_loads           | 27.2 us                                                | 29.7 us: 1.09x slower                                                      |
| json_dumps           | 10.1 ms                                                | 11.6 ms: 1.15x slower                                                      |
| Geometric mean       | (ref)                                                  | 1.01x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250327-linux-x86_64-brandtbucher-jit_build_and_iter-3.14.0a6+-488d5b8 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 12.7 ms                                                | 13.2 ms: 1.04x slower                                                      |
| python_startup_no_site | 7.00 ms                                                | 8.24 ms: 1.18x slower                                                      |
| Geometric mean         | (ref)                                                  | 1.11x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250327-linux-x86_64-brandtbucher-jit_build_and_iter-3.14.0a6+-488d5b8 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_text     | 22.6 ms                                                | 21.4 ms: 1.06x faster                                                      |
| genshi_xml      | 50.5 ms                                                | 49.7 ms: 1.02x faster                                                      |
| django_template | 31.7 ms                                                | 32.2 ms: 1.02x slower                                                      |
| mako            | 10.7 ms                                                | 11.0 ms: 1.03x slower                                                      |
| Geometric mean  | (ref)                                                  | 1.01x faster                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250327-linux-x86_64-brandtbucher-jit_build_and_iter-3.14.0a6+-488d5b8 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 315 ms: 1.47x faster                                                       |
| async_tree_io_tg           | 861 ms                                                 | 623 ms: 1.38x faster                                                       |
| async_tree_memoization     | 437 ms                                                 | 316 ms: 1.38x faster                                                       |
| deepcopy                   | 354 us                                                 | 263 us: 1.35x faster                                                       |
| async_tree_io              | 838 ms                                                 | 623 ms: 1.34x faster                                                       |
| async_tree_none            | 350 ms                                                 | 265 ms: 1.32x faster                                                       |
| richards                   | 47.5 ms                                                | 36.2 ms: 1.31x faster                                                      |
| deepcopy_memo              | 38.4 us                                                | 29.2 us: 1.31x faster                                                      |
| richards_super             | 53.7 ms                                                | 41.6 ms: 1.29x faster                                                      |
| async_tree_none_tg         | 319 ms                                                 | 254 ms: 1.26x faster                                                       |
| deepcopy_reduce            | 3.24 us                                                | 2.71 us: 1.20x faster                                                      |
| float                      | 78.7 ms                                                | 65.7 ms: 1.20x faster                                                      |
| spectral_norm              | 113 ms                                                 | 95.2 ms: 1.19x faster                                                      |
| regex_effbot               | 3.77 ms                                                | 3.20 ms: 1.18x faster                                                      |
| scimark_fft                | 367 ms                                                 | 314 ms: 1.17x faster                                                       |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 492 ms: 1.17x faster                                                       |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 477 ms: 1.14x faster                                                       |
| tomli_loads                | 2.12 sec                                               | 1.87 sec: 1.13x faster                                                     |
| regex_v8                   | 26.9 ms                                                | 23.7 ms: 1.13x faster                                                      |
| pylint                     | 312 ms                                                 | 282 ms: 1.11x faster                                                       |
| xml_etree_parse            | 154 ms                                                 | 139 ms: 1.11x faster                                                       |
| pyflate                    | 470 ms                                                 | 427 ms: 1.10x faster                                                       |
| go                         | 141 ms                                                 | 129 ms: 1.09x faster                                                       |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.67 ms: 1.08x faster                                                      |
| xml_etree_generate         | 86.8 ms                                                | 80.7 ms: 1.08x faster                                                      |
| telco                      | 8.40 ms                                                | 7.82 ms: 1.07x faster                                                      |
| xml_etree_process          | 60.5 ms                                                | 56.6 ms: 1.07x faster                                                      |
| sqlite_synth               | 2.90 us                                                | 2.73 us: 1.06x faster                                                      |
| dulwich_log                | 64.6 ms                                                | 60.9 ms: 1.06x faster                                                      |
| genshi_text                | 22.6 ms                                                | 21.4 ms: 1.06x faster                                                      |
| async_generators           | 433 ms                                                 | 412 ms: 1.05x faster                                                       |
| pycparser                  | 1.20 sec                                               | 1.15 sec: 1.05x faster                                                     |
| deltablue                  | 3.19 ms                                                | 3.07 ms: 1.04x faster                                                      |
| xml_etree_iterparse        | 101 ms                                                 | 97.9 ms: 1.03x faster                                                      |
| thrift                     | 800 us                                                 | 776 us: 1.03x faster                                                       |
| pathlib                    | 17.4 ms                                                | 16.9 ms: 1.03x faster                                                      |
| regex_compile              | 132 ms                                                 | 129 ms: 1.03x faster                                                       |
| k_core                     | 2.37 sec                                               | 2.32 sec: 1.02x faster                                                     |
| mdp                        | 2.54 sec                                               | 2.49 sec: 1.02x faster                                                     |
| regex_dna                  | 220 ms                                                 | 217 ms: 1.02x faster                                                       |
| genshi_xml                 | 50.5 ms                                                | 49.7 ms: 1.02x faster                                                      |
| bpe_tokeniser              | 4.69 sec                                               | 4.62 sec: 1.01x faster                                                     |
| gc_traversal               | 4.90 ms                                                | 4.83 ms: 1.01x faster                                                      |
| 2to3                       | 266 ms                                                 | 264 ms: 1.01x faster                                                       |
| scimark_sor                | 122 ms                                                 | 121 ms: 1.01x faster                                                       |
| generators                 | 28.8 ms                                                | 28.6 ms: 1.00x faster                                                      |
| pidigits                   | 186 ms                                                 | 186 ms: 1.00x faster                                                       |
| asyncio_websockets         | 551 ms                                                 | 553 ms: 1.00x slower                                                       |
| sqlalchemy_declarative     | 133 ms                                                 | 134 ms: 1.00x slower                                                       |
| logging_format             | 6.23 us                                                | 6.27 us: 1.01x slower                                                      |
| nbody                      | 87.7 ms                                                | 88.4 ms: 1.01x slower                                                      |
| sympy_str                  | 273 ms                                                 | 275 ms: 1.01x slower                                                       |
| meteor_contest             | 108 ms                                                 | 109 ms: 1.01x slower                                                       |
| unpickle_pure_python       | 213 us                                                 | 216 us: 1.01x slower                                                       |
| sympy_integrate            | 19.8 ms                                                | 20.1 ms: 1.01x slower                                                      |
| create_gc_cycles           | 2.45 ms                                                | 2.49 ms: 1.02x slower                                                      |
| sympy_sum                  | 150 ms                                                 | 153 ms: 1.02x slower                                                       |
| django_template            | 31.7 ms                                                | 32.2 ms: 1.02x slower                                                      |
| scimark_monte_carlo        | 66.8 ms                                                | 68.3 ms: 1.02x slower                                                      |
| sqlalchemy_imperative      | 16.9 ms                                                | 17.3 ms: 1.02x slower                                                      |
| mako                       | 10.7 ms                                                | 11.0 ms: 1.03x slower                                                      |
| scimark_lu                 | 114 ms                                                 | 118 ms: 1.03x slower                                                       |
| chaos                      | 58.0 ms                                                | 59.8 ms: 1.03x slower                                                      |
| connected_components       | 447 ms                                                 | 461 ms: 1.03x slower                                                       |
| shortest_path              | 487 ms                                                 | 503 ms: 1.03x slower                                                       |
| docutils                   | 2.58 sec                                               | 2.69 sec: 1.04x slower                                                     |
| typing_runtime_protocols   | 160 us                                                 | 167 us: 1.04x slower                                                       |
| python_startup             | 12.7 ms                                                | 13.2 ms: 1.04x slower                                                      |
| nqueens                    | 80.9 ms                                                | 84.4 ms: 1.04x slower                                                      |
| sympy_expand               | 456 ms                                                 | 476 ms: 1.04x slower                                                       |
| raytrace                   | 262 ms                                                 | 273 ms: 1.04x slower                                                       |
| coroutines                 | 22.2 ms                                                | 23.3 ms: 1.05x slower                                                      |
| crypto_pyaes               | 74.7 ms                                                | 79.3 ms: 1.06x slower                                                      |
| fannkuch                   | 394 ms                                                 | 420 ms: 1.07x slower                                                       |
| coverage                   | 82.8 ms                                                | 88.9 ms: 1.07x slower                                                      |
| pickle_pure_python         | 302 us                                                 | 325 us: 1.08x slower                                                       |
| bench_thread_pool          | 818 us                                                 | 882 us: 1.08x slower                                                       |
| json_loads                 | 27.2 us                                                | 29.7 us: 1.09x slower                                                      |
| pprint_pformat             | 1.48 sec                                               | 1.64 sec: 1.11x slower                                                     |
| pprint_safe_repr           | 727 ms                                                 | 804 ms: 1.11x slower                                                       |
| hexiom                     | 6.08 ms                                                | 6.88 ms: 1.13x slower                                                      |
| many_optionals             | 857 us                                                 | 971 us: 1.13x slower                                                       |
| comprehensions             | 16.5 us                                                | 18.8 us: 1.14x slower                                                      |
| json_dumps                 | 10.1 ms                                                | 11.6 ms: 1.15x slower                                                      |
| python_startup_no_site     | 7.00 ms                                                | 8.24 ms: 1.18x slower                                                      |
| subparsers                 | 15.5 ms                                                | 21.3 ms: 1.38x slower                                                      |
| bench_mp_pool              | 24.0 ms                                                | 83.5 ms: 3.48x slower                                                      |
| Geometric mean             | (ref)                                                  | 1.02x faster                                                               |

Benchmark hidden because not significant (5): logging_silent, json, sphinx, logging_simple, html5lib
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250327-3.14.0a6+-488d5b8-JIT/bm-20250327-linux-x86_64-brandtbucher-jit_build_and_iter-3.14.0a6+-488d5b8.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.038x faster

# HPT report

- Reliability score: 97.08% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.05x
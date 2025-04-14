# Results vs. 3.13.0

- fork: brandtbucher
- ref: jit_up_10_8
- machine: linux-x86_64
- commit hash: a00e400
- commit date: 2025-03-28
- overall geometric mean: 1.032x faster
- HPT reliability: 93.51%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.05x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250328-linux-x86_64-brandtbucher-jit_up_10_8-3.14.0a6+-a00e400 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| docutils       | 2.58 sec                                               | 2.70 sec: 1.05x slower                                              |
| html5lib       | 63.4 ms                                                | 62.5 ms: 1.01x faster                                               |
| Geometric mean | (ref)                                                  | 1.01x slower                                                        |

Benchmark hidden because not significant (2): 2to3, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250328-linux-x86_64-brandtbucher-jit_up_10_8-3.14.0a6+-a00e400 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 315 ms: 1.47x faster                                                |
| async_tree_io_tg           | 861 ms                                                 | 623 ms: 1.38x faster                                                |
| async_tree_memoization     | 437 ms                                                 | 317 ms: 1.38x faster                                                |
| async_tree_io              | 838 ms                                                 | 621 ms: 1.35x faster                                                |
| async_tree_none            | 350 ms                                                 | 262 ms: 1.34x faster                                                |
| async_tree_none_tg         | 319 ms                                                 | 255 ms: 1.25x faster                                                |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 493 ms: 1.16x faster                                                |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 475 ms: 1.15x faster                                                |
| async_generators           | 433 ms                                                 | 419 ms: 1.03x faster                                                |
| coroutines                 | 22.2 ms                                                | 23.6 ms: 1.06x slower                                               |
| Geometric mean             | (ref)                                                  | 1.21x faster                                                        |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250328-linux-x86_64-brandtbucher-jit_up_10_8-3.14.0a6+-a00e400 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 65.4 ms: 1.20x faster                                               |
| pidigits       | 186 ms                                                 | 185 ms: 1.01x faster                                                |
| Geometric mean | (ref)                                                  | 1.07x faster                                                        |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250328-linux-x86_64-brandtbucher-jit_up_10_8-3.14.0a6+-a00e400 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_v8       | 26.9 ms                                                | 24.0 ms: 1.12x faster                                               |
| regex_effbot   | 3.77 ms                                                | 3.54 ms: 1.06x faster                                               |
| regex_compile  | 132 ms                                                 | 129 ms: 1.03x faster                                                |
| regex_dna      | 220 ms                                                 | 226 ms: 1.03x slower                                                |
| Geometric mean | (ref)                                                  | 1.04x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250328-linux-x86_64-brandtbucher-jit_up_10_8-3.14.0a6+-a00e400 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| tomli_loads          | 2.12 sec                                               | 1.89 sec: 1.12x faster                                              |
| xml_etree_parse      | 154 ms                                                 | 139 ms: 1.11x faster                                                |
| xml_etree_generate   | 86.8 ms                                                | 80.2 ms: 1.08x faster                                               |
| xml_etree_process    | 60.5 ms                                                | 56.5 ms: 1.07x faster                                               |
| xml_etree_iterparse  | 101 ms                                                 | 98.0 ms: 1.03x faster                                               |
| unpickle_pure_python | 213 us                                                 | 212 us: 1.01x faster                                                |
| pickle_pure_python   | 302 us                                                 | 325 us: 1.07x slower                                                |
| json_loads           | 27.2 us                                                | 30.0 us: 1.10x slower                                               |
| json_dumps           | 10.1 ms                                                | 11.7 ms: 1.16x slower                                               |
| Geometric mean       | (ref)                                                  | 1.01x faster                                                        |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250328-linux-x86_64-brandtbucher-jit_up_10_8-3.14.0a6+-a00e400 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 12.7 ms                                                | 13.2 ms: 1.04x slower                                               |
| python_startup_no_site | 7.00 ms                                                | 8.23 ms: 1.18x slower                                               |
| Geometric mean         | (ref)                                                  | 1.10x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250328-linux-x86_64-brandtbucher-jit_up_10_8-3.14.0a6+-a00e400 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| genshi_text     | 22.6 ms                                                | 21.6 ms: 1.05x faster                                               |
| genshi_xml      | 50.5 ms                                                | 50.0 ms: 1.01x faster                                               |
| django_template | 31.7 ms                                                | 32.2 ms: 1.02x slower                                               |
| mako            | 10.7 ms                                                | 11.0 ms: 1.03x slower                                               |
| Geometric mean  | (ref)                                                  | 1.00x faster                                                        |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250328-linux-x86_64-brandtbucher-jit_up_10_8-3.14.0a6+-a00e400 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 315 ms: 1.47x faster                                                |
| async_tree_io_tg           | 861 ms                                                 | 623 ms: 1.38x faster                                                |
| async_tree_memoization     | 437 ms                                                 | 317 ms: 1.38x faster                                                |
| deepcopy                   | 354 us                                                 | 261 us: 1.36x faster                                                |
| async_tree_io              | 838 ms                                                 | 621 ms: 1.35x faster                                                |
| async_tree_none            | 350 ms                                                 | 262 ms: 1.34x faster                                                |
| deepcopy_memo              | 38.4 us                                                | 29.1 us: 1.32x faster                                               |
| richards                   | 47.5 ms                                                | 37.0 ms: 1.29x faster                                               |
| async_tree_none_tg         | 319 ms                                                 | 255 ms: 1.25x faster                                                |
| richards_super             | 53.7 ms                                                | 42.9 ms: 1.25x faster                                               |
| float                      | 78.7 ms                                                | 65.4 ms: 1.20x faster                                               |
| deepcopy_reduce            | 3.24 us                                                | 2.70 us: 1.20x faster                                               |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 493 ms: 1.16x faster                                                |
| scimark_fft                | 367 ms                                                 | 318 ms: 1.15x faster                                                |
| spectral_norm              | 113 ms                                                 | 98.8 ms: 1.15x faster                                               |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 475 ms: 1.15x faster                                                |
| tomli_loads                | 2.12 sec                                               | 1.89 sec: 1.12x faster                                              |
| regex_v8                   | 26.9 ms                                                | 24.0 ms: 1.12x faster                                               |
| xml_etree_parse            | 154 ms                                                 | 139 ms: 1.11x faster                                                |
| pylint                     | 312 ms                                                 | 284 ms: 1.10x faster                                                |
| go                         | 141 ms                                                 | 129 ms: 1.09x faster                                                |
| xml_etree_generate         | 86.8 ms                                                | 80.2 ms: 1.08x faster                                               |
| telco                      | 8.40 ms                                                | 7.78 ms: 1.08x faster                                               |
| xml_etree_process          | 60.5 ms                                                | 56.5 ms: 1.07x faster                                               |
| dulwich_log                | 64.6 ms                                                | 60.6 ms: 1.07x faster                                               |
| sqlite_synth               | 2.90 us                                                | 2.73 us: 1.06x faster                                               |
| regex_effbot               | 3.77 ms                                                | 3.54 ms: 1.06x faster                                               |
| pyflate                    | 470 ms                                                 | 447 ms: 1.05x faster                                                |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.79 ms: 1.05x faster                                               |
| deltablue                  | 3.19 ms                                                | 3.05 ms: 1.05x faster                                               |
| genshi_text                | 22.6 ms                                                | 21.6 ms: 1.05x faster                                               |
| pathlib                    | 17.4 ms                                                | 16.8 ms: 1.04x faster                                               |
| k_core                     | 2.37 sec                                               | 2.29 sec: 1.04x faster                                              |
| async_generators           | 433 ms                                                 | 419 ms: 1.03x faster                                                |
| xml_etree_iterparse        | 101 ms                                                 | 98.0 ms: 1.03x faster                                               |
| regex_compile              | 132 ms                                                 | 129 ms: 1.03x faster                                                |
| pycparser                  | 1.20 sec                                               | 1.18 sec: 1.02x faster                                              |
| bpe_tokeniser              | 4.69 sec                                               | 4.61 sec: 1.02x faster                                              |
| mdp                        | 2.54 sec                                               | 2.50 sec: 1.02x faster                                              |
| logging_silent             | 101 ns                                                 | 99.5 ns: 1.02x faster                                               |
| scimark_sor                | 122 ms                                                 | 120 ms: 1.02x faster                                                |
| html5lib                   | 63.4 ms                                                | 62.5 ms: 1.01x faster                                               |
| genshi_xml                 | 50.5 ms                                                | 50.0 ms: 1.01x faster                                               |
| unpickle_pure_python       | 213 us                                                 | 212 us: 1.01x faster                                                |
| pidigits                   | 186 ms                                                 | 185 ms: 1.01x faster                                                |
| gc_traversal               | 4.90 ms                                                | 4.91 ms: 1.00x slower                                               |
| crypto_pyaes               | 74.7 ms                                                | 75.2 ms: 1.01x slower                                               |
| django_template            | 31.7 ms                                                | 32.2 ms: 1.02x slower                                               |
| create_gc_cycles           | 2.45 ms                                                | 2.49 ms: 1.02x slower                                               |
| scimark_lu                 | 114 ms                                                 | 117 ms: 1.02x slower                                                |
| generators                 | 28.8 ms                                                | 29.4 ms: 1.02x slower                                               |
| sympy_str                  | 273 ms                                                 | 279 ms: 1.02x slower                                                |
| shortest_path              | 487 ms                                                 | 498 ms: 1.02x slower                                                |
| sqlalchemy_declarative     | 133 ms                                                 | 136 ms: 1.03x slower                                                |
| sympy_integrate            | 19.8 ms                                                | 20.3 ms: 1.03x slower                                               |
| raytrace                   | 262 ms                                                 | 268 ms: 1.03x slower                                                |
| mako                       | 10.7 ms                                                | 11.0 ms: 1.03x slower                                               |
| regex_dna                  | 220 ms                                                 | 226 ms: 1.03x slower                                                |
| scimark_monte_carlo        | 66.8 ms                                                | 68.8 ms: 1.03x slower                                               |
| sqlalchemy_imperative      | 16.9 ms                                                | 17.5 ms: 1.03x slower                                               |
| sympy_sum                  | 150 ms                                                 | 156 ms: 1.03x slower                                                |
| python_startup             | 12.7 ms                                                | 13.2 ms: 1.04x slower                                               |
| coverage                   | 82.8 ms                                                | 86.0 ms: 1.04x slower                                               |
| chaos                      | 58.0 ms                                                | 60.6 ms: 1.04x slower                                               |
| docutils                   | 2.58 sec                                               | 2.70 sec: 1.05x slower                                              |
| sympy_expand               | 456 ms                                                 | 478 ms: 1.05x slower                                                |
| typing_runtime_protocols   | 160 us                                                 | 169 us: 1.05x slower                                                |
| coroutines                 | 22.2 ms                                                | 23.6 ms: 1.06x slower                                               |
| pprint_safe_repr           | 727 ms                                                 | 774 ms: 1.06x slower                                                |
| pickle_pure_python         | 302 us                                                 | 325 us: 1.07x slower                                                |
| nqueens                    | 80.9 ms                                                | 87.5 ms: 1.08x slower                                               |
| fannkuch                   | 394 ms                                                 | 426 ms: 1.08x slower                                                |
| bench_thread_pool          | 818 us                                                 | 892 us: 1.09x slower                                                |
| pprint_pformat             | 1.48 sec                                               | 1.63 sec: 1.10x slower                                              |
| json_loads                 | 27.2 us                                                | 30.0 us: 1.10x slower                                               |
| connected_components       | 447 ms                                                 | 495 ms: 1.11x slower                                                |
| comprehensions             | 16.5 us                                                | 18.5 us: 1.12x slower                                               |
| json_dumps                 | 10.1 ms                                                | 11.7 ms: 1.16x slower                                               |
| many_optionals             | 857 us                                                 | 996 us: 1.16x slower                                                |
| hexiom                     | 6.08 ms                                                | 7.07 ms: 1.16x slower                                               |
| python_startup_no_site     | 7.00 ms                                                | 8.23 ms: 1.18x slower                                               |
| subparsers                 | 15.5 ms                                                | 21.2 ms: 1.37x slower                                               |
| bench_mp_pool              | 24.0 ms                                                | 83.5 ms: 3.48x slower                                               |
| Geometric mean             | (ref)                                                  | 1.02x faster                                                        |

Benchmark hidden because not significant (9): json, thrift, nbody, logging_simple, logging_format, 2to3, asyncio_websockets, sphinx, meteor_contest
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250328-3.14.0a6+-a00e400-JIT/bm-20250328-linux-x86_64-brandtbucher-jit_up_10_8-3.14.0a6+-a00e400.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.032x faster

# HPT report

- Reliability score: 93.51% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.05x
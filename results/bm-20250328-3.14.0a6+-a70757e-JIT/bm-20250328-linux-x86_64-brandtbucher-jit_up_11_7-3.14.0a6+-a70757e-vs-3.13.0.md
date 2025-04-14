# Results vs. 3.13.0

- fork: brandtbucher
- ref: jit_up_11_7
- machine: linux-x86_64
- commit hash: a70757e
- commit date: 2025-03-28
- overall geometric mean: 1.041x faster
- HPT reliability: 98.26%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.05x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250328-linux-x86_64-brandtbucher-jit_up_11_7-3.14.0a6+-a70757e |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 264 ms: 1.01x faster                                                |
| docutils       | 2.58 sec                                               | 2.68 sec: 1.04x slower                                              |
| Geometric mean | (ref)                                                  | 1.01x slower                                                        |

Benchmark hidden because not significant (2): html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250328-linux-x86_64-brandtbucher-jit_up_11_7-3.14.0a6+-a70757e |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 315 ms: 1.47x faster                                                |
| async_tree_io_tg           | 861 ms                                                 | 621 ms: 1.39x faster                                                |
| async_tree_memoization     | 437 ms                                                 | 317 ms: 1.38x faster                                                |
| async_tree_io              | 838 ms                                                 | 616 ms: 1.36x faster                                                |
| async_tree_none            | 350 ms                                                 | 260 ms: 1.35x faster                                                |
| async_tree_none_tg         | 319 ms                                                 | 254 ms: 1.26x faster                                                |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 489 ms: 1.17x faster                                                |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 472 ms: 1.15x faster                                                |
| async_generators           | 433 ms                                                 | 414 ms: 1.05x faster                                                |
| coroutines                 | 22.2 ms                                                | 24.2 ms: 1.09x slower                                               |
| Geometric mean             | (ref)                                                  | 1.21x faster                                                        |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250328-linux-x86_64-brandtbucher-jit_up_11_7-3.14.0a6+-a70757e |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 65.3 ms: 1.20x faster                                               |
| pidigits       | 186 ms                                                 | 185 ms: 1.01x faster                                                |
| Geometric mean | (ref)                                                  | 1.06x faster                                                        |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250328-linux-x86_64-brandtbucher-jit_up_11_7-3.14.0a6+-a70757e |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                | 3.10 ms: 1.21x faster                                               |
| regex_v8       | 26.9 ms                                                | 22.9 ms: 1.17x faster                                               |
| regex_dna      | 220 ms                                                 | 211 ms: 1.04x faster                                                |
| regex_compile  | 132 ms                                                 | 128 ms: 1.03x faster                                                |
| Geometric mean | (ref)                                                  | 1.11x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250328-linux-x86_64-brandtbucher-jit_up_11_7-3.14.0a6+-a70757e |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| tomli_loads          | 2.12 sec                                               | 1.87 sec: 1.13x faster                                              |
| xml_etree_parse      | 154 ms                                                 | 140 ms: 1.10x faster                                                |
| xml_etree_generate   | 86.8 ms                                                | 80.5 ms: 1.08x faster                                               |
| xml_etree_process    | 60.5 ms                                                | 56.6 ms: 1.07x faster                                               |
| xml_etree_iterparse  | 101 ms                                                 | 98.2 ms: 1.03x faster                                               |
| unpickle_pure_python | 213 us                                                 | 216 us: 1.01x slower                                                |
| pickle_pure_python   | 302 us                                                 | 325 us: 1.08x slower                                                |
| json_loads           | 27.2 us                                                | 30.0 us: 1.10x slower                                               |
| json_dumps           | 10.1 ms                                                | 11.6 ms: 1.14x slower                                               |
| Geometric mean       | (ref)                                                  | 1.01x faster                                                        |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250328-linux-x86_64-brandtbucher-jit_up_11_7-3.14.0a6+-a70757e |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 12.7 ms                                                | 13.1 ms: 1.04x slower                                               |
| python_startup_no_site | 7.00 ms                                                | 8.21 ms: 1.17x slower                                               |
| Geometric mean         | (ref)                                                  | 1.10x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250328-linux-x86_64-brandtbucher-jit_up_11_7-3.14.0a6+-a70757e |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| genshi_text     | 22.6 ms                                                | 21.5 ms: 1.05x faster                                               |
| genshi_xml      | 50.5 ms                                                | 49.8 ms: 1.01x faster                                               |
| mako            | 10.7 ms                                                | 10.9 ms: 1.02x slower                                               |
| django_template | 31.7 ms                                                | 32.9 ms: 1.04x slower                                               |
| Geometric mean  | (ref)                                                  | 1.00x faster                                                        |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250328-linux-x86_64-brandtbucher-jit_up_11_7-3.14.0a6+-a70757e |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 315 ms: 1.47x faster                                                |
| async_tree_io_tg           | 861 ms                                                 | 621 ms: 1.39x faster                                                |
| async_tree_memoization     | 437 ms                                                 | 317 ms: 1.38x faster                                                |
| async_tree_io              | 838 ms                                                 | 616 ms: 1.36x faster                                                |
| async_tree_none            | 350 ms                                                 | 260 ms: 1.35x faster                                                |
| deepcopy                   | 354 us                                                 | 264 us: 1.34x faster                                                |
| richards_super             | 53.7 ms                                                | 41.2 ms: 1.30x faster                                               |
| deepcopy_memo              | 38.4 us                                                | 29.5 us: 1.30x faster                                               |
| richards                   | 47.5 ms                                                | 36.8 ms: 1.29x faster                                               |
| async_tree_none_tg         | 319 ms                                                 | 254 ms: 1.26x faster                                                |
| regex_effbot               | 3.77 ms                                                | 3.10 ms: 1.21x faster                                               |
| float                      | 78.7 ms                                                | 65.3 ms: 1.20x faster                                               |
| deepcopy_reduce            | 3.24 us                                                | 2.74 us: 1.18x faster                                               |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 489 ms: 1.17x faster                                                |
| regex_v8                   | 26.9 ms                                                | 22.9 ms: 1.17x faster                                               |
| scimark_fft                | 367 ms                                                 | 314 ms: 1.17x faster                                                |
| spectral_norm              | 113 ms                                                 | 97.0 ms: 1.17x faster                                               |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 472 ms: 1.15x faster                                                |
| tomli_loads                | 2.12 sec                                               | 1.87 sec: 1.13x faster                                              |
| go                         | 141 ms                                                 | 127 ms: 1.11x faster                                                |
| pylint                     | 312 ms                                                 | 282 ms: 1.10x faster                                                |
| xml_etree_parse            | 154 ms                                                 | 140 ms: 1.10x faster                                                |
| pyflate                    | 470 ms                                                 | 429 ms: 1.10x faster                                                |
| telco                      | 8.40 ms                                                | 7.78 ms: 1.08x faster                                               |
| xml_etree_generate         | 86.8 ms                                                | 80.5 ms: 1.08x faster                                               |
| xml_etree_process          | 60.5 ms                                                | 56.6 ms: 1.07x faster                                               |
| sqlite_synth               | 2.90 us                                                | 2.72 us: 1.07x faster                                               |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.73 ms: 1.06x faster                                               |
| dulwich_log                | 64.6 ms                                                | 60.9 ms: 1.06x faster                                               |
| pycparser                  | 1.20 sec                                               | 1.14 sec: 1.05x faster                                              |
| genshi_text                | 22.6 ms                                                | 21.5 ms: 1.05x faster                                               |
| async_generators           | 433 ms                                                 | 414 ms: 1.05x faster                                                |
| pathlib                    | 17.4 ms                                                | 16.6 ms: 1.04x faster                                               |
| regex_dna                  | 220 ms                                                 | 211 ms: 1.04x faster                                                |
| deltablue                  | 3.19 ms                                                | 3.08 ms: 1.04x faster                                               |
| thrift                     | 800 us                                                 | 775 us: 1.03x faster                                                |
| xml_etree_iterparse        | 101 ms                                                 | 98.2 ms: 1.03x faster                                               |
| logging_silent             | 101 ns                                                 | 98.1 ns: 1.03x faster                                               |
| regex_compile              | 132 ms                                                 | 128 ms: 1.03x faster                                                |
| k_core                     | 2.37 sec                                               | 2.31 sec: 1.03x faster                                              |
| bpe_tokeniser              | 4.69 sec                                               | 4.59 sec: 1.02x faster                                              |
| mdp                        | 2.54 sec                                               | 2.49 sec: 1.02x faster                                              |
| scimark_sor                | 122 ms                                                 | 120 ms: 1.02x faster                                                |
| logging_format             | 6.23 us                                                | 6.14 us: 1.02x faster                                               |
| genshi_xml                 | 50.5 ms                                                | 49.8 ms: 1.01x faster                                               |
| gc_traversal               | 4.90 ms                                                | 4.85 ms: 1.01x faster                                               |
| logging_simple             | 5.65 us                                                | 5.60 us: 1.01x faster                                               |
| 2to3                       | 266 ms                                                 | 264 ms: 1.01x faster                                                |
| pidigits                   | 186 ms                                                 | 185 ms: 1.01x faster                                                |
| generators                 | 28.8 ms                                                | 29.1 ms: 1.01x slower                                               |
| crypto_pyaes               | 74.7 ms                                                | 75.5 ms: 1.01x slower                                               |
| shortest_path              | 487 ms                                                 | 493 ms: 1.01x slower                                                |
| unpickle_pure_python       | 213 us                                                 | 216 us: 1.01x slower                                                |
| create_gc_cycles           | 2.45 ms                                                | 2.48 ms: 1.01x slower                                               |
| sympy_str                  | 273 ms                                                 | 277 ms: 1.02x slower                                                |
| raytrace                   | 262 ms                                                 | 266 ms: 1.02x slower                                                |
| connected_components       | 447 ms                                                 | 454 ms: 1.02x slower                                                |
| sqlalchemy_declarative     | 133 ms                                                 | 136 ms: 1.02x slower                                                |
| mako                       | 10.7 ms                                                | 10.9 ms: 1.02x slower                                               |
| sympy_integrate            | 19.8 ms                                                | 20.3 ms: 1.02x slower                                               |
| sympy_sum                  | 150 ms                                                 | 155 ms: 1.03x slower                                                |
| chaos                      | 58.0 ms                                                | 59.8 ms: 1.03x slower                                               |
| sqlalchemy_imperative      | 16.9 ms                                                | 17.4 ms: 1.03x slower                                               |
| scimark_monte_carlo        | 66.8 ms                                                | 68.9 ms: 1.03x slower                                               |
| python_startup             | 12.7 ms                                                | 13.1 ms: 1.04x slower                                               |
| django_template            | 31.7 ms                                                | 32.9 ms: 1.04x slower                                               |
| docutils                   | 2.58 sec                                               | 2.68 sec: 1.04x slower                                              |
| coverage                   | 82.8 ms                                                | 86.0 ms: 1.04x slower                                               |
| scimark_lu                 | 114 ms                                                 | 119 ms: 1.04x slower                                                |
| sympy_expand               | 456 ms                                                 | 478 ms: 1.05x slower                                                |
| pprint_pformat             | 1.48 sec                                               | 1.55 sec: 1.05x slower                                              |
| fannkuch                   | 394 ms                                                 | 414 ms: 1.05x slower                                                |
| nqueens                    | 80.9 ms                                                | 85.5 ms: 1.06x slower                                               |
| typing_runtime_protocols   | 160 us                                                 | 170 us: 1.06x slower                                                |
| pprint_safe_repr           | 727 ms                                                 | 777 ms: 1.07x slower                                                |
| pickle_pure_python         | 302 us                                                 | 325 us: 1.08x slower                                                |
| bench_thread_pool          | 818 us                                                 | 886 us: 1.08x slower                                                |
| coroutines                 | 22.2 ms                                                | 24.2 ms: 1.09x slower                                               |
| json_loads                 | 27.2 us                                                | 30.0 us: 1.10x slower                                               |
| comprehensions             | 16.5 us                                                | 18.7 us: 1.13x slower                                               |
| many_optionals             | 857 us                                                 | 978 us: 1.14x slower                                                |
| json_dumps                 | 10.1 ms                                                | 11.6 ms: 1.14x slower                                               |
| hexiom                     | 6.08 ms                                                | 7.11 ms: 1.17x slower                                               |
| python_startup_no_site     | 7.00 ms                                                | 8.21 ms: 1.17x slower                                               |
| subparsers                 | 15.5 ms                                                | 20.7 ms: 1.34x slower                                               |
| bench_mp_pool              | 24.0 ms                                                | 83.3 ms: 3.47x slower                                               |
| Geometric mean             | (ref)                                                  | 1.03x faster                                                        |

Benchmark hidden because not significant (6): sphinx, html5lib, asyncio_websockets, meteor_contest, json, nbody
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250328-3.14.0a6+-a70757e-JIT/bm-20250328-linux-x86_64-brandtbucher-jit_up_11_7-3.14.0a6+-a70757e.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.041x faster

# HPT report

- Reliability score: 98.26% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.05x
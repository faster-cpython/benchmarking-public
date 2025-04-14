# Results vs. 3.13.0

- fork: brandtbucher
- ref: jit_up_11_6
- machine: linux-x86_64
- commit hash: a0aff13
- commit date: 2025-03-29
- overall geometric mean: 1.038x faster
- HPT reliability: 96.61%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.05x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250329-linux-x86_64-brandtbucher-jit_up_11_6-3.14.0a6+-a0aff13 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 265 ms: 1.00x faster                                                |
| docutils       | 2.58 sec                                               | 2.71 sec: 1.05x slower                                              |
| html5lib       | 63.4 ms                                                | 61.9 ms: 1.02x faster                                               |
| Geometric mean | (ref)                                                  | 1.01x slower                                                        |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250329-linux-x86_64-brandtbucher-jit_up_11_6-3.14.0a6+-a0aff13 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 314 ms: 1.48x faster                                                |
| async_tree_io_tg           | 861 ms                                                 | 622 ms: 1.38x faster                                                |
| async_tree_memoization     | 437 ms                                                 | 316 ms: 1.38x faster                                                |
| async_tree_io              | 838 ms                                                 | 617 ms: 1.36x faster                                                |
| async_tree_none            | 350 ms                                                 | 260 ms: 1.35x faster                                                |
| async_tree_none_tg         | 319 ms                                                 | 251 ms: 1.27x faster                                                |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 490 ms: 1.17x faster                                                |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 473 ms: 1.15x faster                                                |
| async_generators           | 433 ms                                                 | 415 ms: 1.04x faster                                                |
| coroutines                 | 22.2 ms                                                | 23.8 ms: 1.07x slower                                               |
| Geometric mean             | (ref)                                                  | 1.22x faster                                                        |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250329-linux-x86_64-brandtbucher-jit_up_11_6-3.14.0a6+-a0aff13 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 65.7 ms: 1.20x faster                                               |
| nbody          | 87.7 ms                                                | 86.8 ms: 1.01x faster                                               |
| pidigits       | 186 ms                                                 | 186 ms: 1.01x faster                                                |
| Geometric mean | (ref)                                                  | 1.07x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250329-linux-x86_64-brandtbucher-jit_up_11_6-3.14.0a6+-a0aff13 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_v8       | 26.9 ms                                                | 23.6 ms: 1.14x faster                                               |
| regex_effbot   | 3.77 ms                                                | 3.36 ms: 1.12x faster                                               |
| regex_compile  | 132 ms                                                 | 129 ms: 1.03x faster                                                |
| regex_dna      | 220 ms                                                 | 226 ms: 1.03x slower                                                |
| Geometric mean | (ref)                                                  | 1.06x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250329-linux-x86_64-brandtbucher-jit_up_11_6-3.14.0a6+-a0aff13 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| tomli_loads          | 2.12 sec                                               | 1.88 sec: 1.12x faster                                              |
| xml_etree_parse      | 154 ms                                                 | 139 ms: 1.11x faster                                                |
| xml_etree_generate   | 86.8 ms                                                | 80.6 ms: 1.08x faster                                               |
| xml_etree_process    | 60.5 ms                                                | 56.9 ms: 1.06x faster                                               |
| xml_etree_iterparse  | 101 ms                                                 | 98.0 ms: 1.03x faster                                               |
| unpickle_pure_python | 213 us                                                 | 211 us: 1.01x faster                                                |
| pickle_pure_python   | 302 us                                                 | 326 us: 1.08x slower                                                |
| json_loads           | 27.2 us                                                | 30.1 us: 1.11x slower                                               |
| json_dumps           | 10.1 ms                                                | 11.6 ms: 1.15x slower                                               |
| Geometric mean       | (ref)                                                  | 1.01x faster                                                        |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250329-linux-x86_64-brandtbucher-jit_up_11_6-3.14.0a6+-a0aff13 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 12.7 ms                                                | 13.1 ms: 1.04x slower                                               |
| python_startup_no_site | 7.00 ms                                                | 8.19 ms: 1.17x slower                                               |
| Geometric mean         | (ref)                                                  | 1.10x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250329-linux-x86_64-brandtbucher-jit_up_11_6-3.14.0a6+-a0aff13 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| genshi_text     | 22.6 ms                                                | 21.7 ms: 1.04x faster                                               |
| genshi_xml      | 50.5 ms                                                | 50.2 ms: 1.01x faster                                               |
| django_template | 31.7 ms                                                | 32.0 ms: 1.01x slower                                               |
| mako            | 10.7 ms                                                | 11.0 ms: 1.03x slower                                               |
| Geometric mean  | (ref)                                                  | 1.00x faster                                                        |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250329-linux-x86_64-brandtbucher-jit_up_11_6-3.14.0a6+-a0aff13 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 314 ms: 1.48x faster                                                |
| async_tree_io_tg           | 861 ms                                                 | 622 ms: 1.38x faster                                                |
| async_tree_memoization     | 437 ms                                                 | 316 ms: 1.38x faster                                                |
| async_tree_io              | 838 ms                                                 | 617 ms: 1.36x faster                                                |
| async_tree_none            | 350 ms                                                 | 260 ms: 1.35x faster                                                |
| deepcopy                   | 354 us                                                 | 264 us: 1.34x faster                                                |
| deepcopy_memo              | 38.4 us                                                | 29.1 us: 1.32x faster                                               |
| async_tree_none_tg         | 319 ms                                                 | 251 ms: 1.27x faster                                                |
| richards                   | 47.5 ms                                                | 37.7 ms: 1.26x faster                                               |
| richards_super             | 53.7 ms                                                | 42.8 ms: 1.25x faster                                               |
| float                      | 78.7 ms                                                | 65.7 ms: 1.20x faster                                               |
| deepcopy_reduce            | 3.24 us                                                | 2.73 us: 1.19x faster                                               |
| scimark_fft                | 367 ms                                                 | 311 ms: 1.18x faster                                                |
| spectral_norm              | 113 ms                                                 | 96.6 ms: 1.17x faster                                               |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 490 ms: 1.17x faster                                                |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 473 ms: 1.15x faster                                                |
| regex_v8                   | 26.9 ms                                                | 23.6 ms: 1.14x faster                                               |
| tomli_loads                | 2.12 sec                                               | 1.88 sec: 1.12x faster                                              |
| regex_effbot               | 3.77 ms                                                | 3.36 ms: 1.12x faster                                               |
| xml_etree_parse            | 154 ms                                                 | 139 ms: 1.11x faster                                                |
| pylint                     | 312 ms                                                 | 284 ms: 1.10x faster                                                |
| go                         | 141 ms                                                 | 130 ms: 1.08x faster                                                |
| xml_etree_generate         | 86.8 ms                                                | 80.6 ms: 1.08x faster                                               |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.68 ms: 1.08x faster                                               |
| sqlite_synth               | 2.90 us                                                | 2.71 us: 1.07x faster                                               |
| telco                      | 8.40 ms                                                | 7.86 ms: 1.07x faster                                               |
| dulwich_log                | 64.6 ms                                                | 60.7 ms: 1.06x faster                                               |
| xml_etree_process          | 60.5 ms                                                | 56.9 ms: 1.06x faster                                               |
| gc_traversal               | 4.90 ms                                                | 4.65 ms: 1.05x faster                                               |
| async_generators           | 433 ms                                                 | 415 ms: 1.04x faster                                                |
| genshi_text                | 22.6 ms                                                | 21.7 ms: 1.04x faster                                               |
| deltablue                  | 3.19 ms                                                | 3.07 ms: 1.04x faster                                               |
| pathlib                    | 17.4 ms                                                | 16.8 ms: 1.04x faster                                               |
| xml_etree_iterparse        | 101 ms                                                 | 98.0 ms: 1.03x faster                                               |
| pyflate                    | 470 ms                                                 | 458 ms: 1.03x faster                                                |
| thrift                     | 800 us                                                 | 780 us: 1.03x faster                                                |
| regex_compile              | 132 ms                                                 | 129 ms: 1.03x faster                                                |
| html5lib                   | 63.4 ms                                                | 61.9 ms: 1.02x faster                                               |
| k_core                     | 2.37 sec                                               | 2.31 sec: 1.02x faster                                              |
| mdp                        | 2.54 sec                                               | 2.51 sec: 1.01x faster                                              |
| logging_silent             | 101 ns                                                 | 99.6 ns: 1.01x faster                                               |
| scimark_sor                | 122 ms                                                 | 121 ms: 1.01x faster                                                |
| bpe_tokeniser              | 4.69 sec                                               | 4.64 sec: 1.01x faster                                              |
| nbody                      | 87.7 ms                                                | 86.8 ms: 1.01x faster                                               |
| unpickle_pure_python       | 213 us                                                 | 211 us: 1.01x faster                                                |
| genshi_xml                 | 50.5 ms                                                | 50.2 ms: 1.01x faster                                               |
| pidigits                   | 186 ms                                                 | 186 ms: 1.01x faster                                                |
| 2to3                       | 266 ms                                                 | 265 ms: 1.00x faster                                                |
| create_gc_cycles           | 2.45 ms                                                | 2.47 ms: 1.01x slower                                               |
| shortest_path              | 487 ms                                                 | 490 ms: 1.01x slower                                                |
| django_template            | 31.7 ms                                                | 32.0 ms: 1.01x slower                                               |
| json                       | 5.32 ms                                                | 5.40 ms: 1.01x slower                                               |
| crypto_pyaes               | 74.7 ms                                                | 75.8 ms: 1.01x slower                                               |
| sympy_str                  | 273 ms                                                 | 277 ms: 1.01x slower                                                |
| meteor_contest             | 108 ms                                                 | 110 ms: 1.01x slower                                                |
| pprint_safe_repr           | 727 ms                                                 | 738 ms: 1.02x slower                                                |
| sqlalchemy_imperative      | 16.9 ms                                                | 17.2 ms: 1.02x slower                                               |
| connected_components       | 447 ms                                                 | 455 ms: 1.02x slower                                                |
| scimark_lu                 | 114 ms                                                 | 117 ms: 1.02x slower                                                |
| sympy_integrate            | 19.8 ms                                                | 20.3 ms: 1.02x slower                                               |
| raytrace                   | 262 ms                                                 | 268 ms: 1.02x slower                                                |
| sympy_sum                  | 150 ms                                                 | 154 ms: 1.02x slower                                                |
| sqlalchemy_declarative     | 133 ms                                                 | 136 ms: 1.03x slower                                                |
| regex_dna                  | 220 ms                                                 | 226 ms: 1.03x slower                                                |
| scimark_monte_carlo        | 66.8 ms                                                | 68.6 ms: 1.03x slower                                               |
| mako                       | 10.7 ms                                                | 11.0 ms: 1.03x slower                                               |
| chaos                      | 58.0 ms                                                | 60.0 ms: 1.03x slower                                               |
| python_startup             | 12.7 ms                                                | 13.1 ms: 1.04x slower                                               |
| sympy_expand               | 456 ms                                                 | 474 ms: 1.04x slower                                                |
| coverage                   | 82.8 ms                                                | 86.2 ms: 1.04x slower                                               |
| pprint_pformat             | 1.48 sec                                               | 1.55 sec: 1.05x slower                                              |
| docutils                   | 2.58 sec                                               | 2.71 sec: 1.05x slower                                              |
| typing_runtime_protocols   | 160 us                                                 | 169 us: 1.05x slower                                                |
| coroutines                 | 22.2 ms                                                | 23.8 ms: 1.07x slower                                               |
| nqueens                    | 80.9 ms                                                | 86.7 ms: 1.07x slower                                               |
| fannkuch                   | 394 ms                                                 | 424 ms: 1.08x slower                                                |
| pickle_pure_python         | 302 us                                                 | 326 us: 1.08x slower                                                |
| bench_thread_pool          | 818 us                                                 | 887 us: 1.08x slower                                                |
| json_loads                 | 27.2 us                                                | 30.1 us: 1.11x slower                                               |
| hexiom                     | 6.08 ms                                                | 6.88 ms: 1.13x slower                                               |
| json_dumps                 | 10.1 ms                                                | 11.6 ms: 1.15x slower                                               |
| many_optionals             | 857 us                                                 | 982 us: 1.15x slower                                                |
| comprehensions             | 16.5 us                                                | 19.0 us: 1.15x slower                                               |
| python_startup_no_site     | 7.00 ms                                                | 8.19 ms: 1.17x slower                                               |
| subparsers                 | 15.5 ms                                                | 20.8 ms: 1.35x slower                                               |
| bench_mp_pool              | 24.0 ms                                                | 83.1 ms: 3.47x slower                                               |
| Geometric mean             | (ref)                                                  | 1.02x faster                                                        |

Benchmark hidden because not significant (6): pycparser, logging_simple, asyncio_websockets, generators, sphinx, logging_format
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250329-3.14.0a6+-a0aff13-JIT/bm-20250329-linux-x86_64-brandtbucher-jit_up_11_6-3.14.0a6+-a0aff13.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.038x faster

# HPT report

- Reliability score: 96.61% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.05x
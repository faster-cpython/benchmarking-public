# Results vs. 3.13.0

- fork: brandtbucher
- ref: jit_up_6_6
- machine: linux-x86_64
- commit hash: 6c99b17
- commit date: 2025-07-02
- overall geometric mean: 1.023x faster
- HPT reliability: 99.70%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.11x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250702-linux-x86_64-brandtbucher-jit_up_6_6-3.15.0a0-6c99b17 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 267 ms: 1.00x slower                                              |
| docutils       | 2.58 sec                                               | 2.69 sec: 1.04x slower                                            |
| html5lib       | 63.4 ms                                                | 61.7 ms: 1.03x faster                                             |
| Geometric mean | (ref)                                                  | 1.00x slower                                                      |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250702-linux-x86_64-brandtbucher-jit_up_6_6-3.15.0a0-6c99b17 |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 319 ms: 1.45x faster                                              |
| async_tree_io              | 838 ms                                                 | 602 ms: 1.39x faster                                              |
| async_tree_none            | 350 ms                                                 | 255 ms: 1.37x faster                                              |
| async_tree_memoization     | 437 ms                                                 | 321 ms: 1.36x faster                                              |
| async_tree_io_tg           | 861 ms                                                 | 639 ms: 1.35x faster                                              |
| async_tree_none_tg         | 319 ms                                                 | 249 ms: 1.28x faster                                              |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 502 ms: 1.14x faster                                              |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 500 ms: 1.09x faster                                              |
| async_generators           | 433 ms                                                 | 427 ms: 1.01x faster                                              |
| coroutines                 | 22.2 ms                                                | 25.4 ms: 1.14x slower                                             |
| Geometric mean             | (ref)                                                  | 1.20x faster                                                      |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250702-linux-x86_64-brandtbucher-jit_up_6_6-3.15.0a0-6c99b17 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| float          | 78.7 ms                                                | 65.7 ms: 1.20x faster                                             |
| pidigits       | 186 ms                                                 | 193 ms: 1.04x slower                                              |
| nbody          | 87.7 ms                                                | 92.9 ms: 1.06x slower                                             |
| Geometric mean | (ref)                                                  | 1.03x faster                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250702-linux-x86_64-brandtbucher-jit_up_6_6-3.15.0a0-6c99b17 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| regex_v8       | 26.9 ms                                                | 23.1 ms: 1.16x faster                                             |
| regex_effbot   | 3.77 ms                                                | 3.39 ms: 1.11x faster                                             |
| regex_dna      | 220 ms                                                 | 216 ms: 1.02x faster                                              |
| regex_compile  | 132 ms                                                 | 130 ms: 1.02x faster                                              |
| Geometric mean | (ref)                                                  | 1.08x faster                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250702-linux-x86_64-brandtbucher-jit_up_6_6-3.15.0a0-6c99b17 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| tomli_loads          | 2.12 sec                                               | 1.85 sec: 1.14x faster                                            |
| unpickle_pure_python | 213 us                                                 | 192 us: 1.11x faster                                              |
| xml_etree_parse      | 154 ms                                                 | 140 ms: 1.10x faster                                              |
| xml_etree_generate   | 86.8 ms                                                | 78.8 ms: 1.10x faster                                             |
| xml_etree_process    | 60.5 ms                                                | 54.9 ms: 1.10x faster                                             |
| xml_etree_iterparse  | 101 ms                                                 | 98.2 ms: 1.03x faster                                             |
| pickle_pure_python   | 302 us                                                 | 321 us: 1.06x slower                                              |
| json_loads           | 27.2 us                                                | 28.9 us: 1.07x slower                                             |
| json_dumps           | 10.1 ms                                                | 11.1 ms: 1.09x slower                                             |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                      |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250702-linux-x86_64-brandtbucher-jit_up_6_6-3.15.0a0-6c99b17 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| python_startup         | 12.7 ms                                                | 12.2 ms: 1.04x faster                                             |
| python_startup_no_site | 7.00 ms                                                | 6.95 ms: 1.01x faster                                             |
| Geometric mean         | (ref)                                                  | 1.02x faster                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250702-linux-x86_64-brandtbucher-jit_up_6_6-3.15.0a0-6c99b17 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| genshi_text     | 22.6 ms                                                | 21.5 ms: 1.05x faster                                             |
| mako            | 10.7 ms                                                | 10.5 ms: 1.02x faster                                             |
| genshi_xml      | 50.5 ms                                                | 50.9 ms: 1.01x slower                                             |
| django_template | 31.7 ms                                                | 32.6 ms: 1.03x slower                                             |
| Geometric mean  | (ref)                                                  | 1.01x faster                                                      |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250702-linux-x86_64-brandtbucher-jit_up_6_6-3.15.0a0-6c99b17 |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| mdp                        | 2.54 sec                                               | 1.24 sec: 2.05x faster                                            |
| async_tree_memoization_tg  | 463 ms                                                 | 319 ms: 1.45x faster                                              |
| async_tree_io              | 838 ms                                                 | 602 ms: 1.39x faster                                              |
| async_tree_none            | 350 ms                                                 | 255 ms: 1.37x faster                                              |
| richards_super             | 53.7 ms                                                | 39.3 ms: 1.37x faster                                             |
| richards                   | 47.5 ms                                                | 34.7 ms: 1.37x faster                                             |
| deepcopy                   | 354 us                                                 | 260 us: 1.36x faster                                              |
| async_tree_memoization     | 437 ms                                                 | 321 ms: 1.36x faster                                              |
| async_tree_io_tg           | 861 ms                                                 | 639 ms: 1.35x faster                                              |
| deepcopy_memo              | 38.4 us                                                | 29.8 us: 1.29x faster                                             |
| async_tree_none_tg         | 319 ms                                                 | 249 ms: 1.28x faster                                              |
| spectral_norm              | 113 ms                                                 | 90.1 ms: 1.26x faster                                             |
| go                         | 141 ms                                                 | 115 ms: 1.23x faster                                              |
| float                      | 78.7 ms                                                | 65.7 ms: 1.20x faster                                             |
| deepcopy_reduce            | 3.24 us                                                | 2.72 us: 1.19x faster                                             |
| scimark_fft                | 367 ms                                                 | 312 ms: 1.17x faster                                              |
| regex_v8                   | 26.9 ms                                                | 23.1 ms: 1.16x faster                                             |
| pyflate                    | 470 ms                                                 | 406 ms: 1.16x faster                                              |
| tomli_loads                | 2.12 sec                                               | 1.85 sec: 1.14x faster                                            |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 502 ms: 1.14x faster                                              |
| regex_effbot               | 3.77 ms                                                | 3.39 ms: 1.11x faster                                             |
| unpickle_pure_python       | 213 us                                                 | 192 us: 1.11x faster                                              |
| xml_etree_parse            | 154 ms                                                 | 140 ms: 1.10x faster                                              |
| xml_etree_generate         | 86.8 ms                                                | 78.8 ms: 1.10x faster                                             |
| xml_etree_process          | 60.5 ms                                                | 54.9 ms: 1.10x faster                                             |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 500 ms: 1.09x faster                                              |
| dulwich_log                | 64.6 ms                                                | 59.8 ms: 1.08x faster                                             |
| pylint                     | 312 ms                                                 | 289 ms: 1.08x faster                                              |
| bpe_tokeniser              | 4.69 sec                                               | 4.37 sec: 1.07x faster                                            |
| pprint_pformat             | 1.48 sec                                               | 1.39 sec: 1.06x faster                                            |
| genshi_text                | 22.6 ms                                                | 21.5 ms: 1.05x faster                                             |
| meteor_contest             | 108 ms                                                 | 103 ms: 1.05x faster                                              |
| deltablue                  | 3.19 ms                                                | 3.06 ms: 1.04x faster                                             |
| k_core                     | 2.37 sec                                               | 2.27 sec: 1.04x faster                                            |
| pprint_safe_repr           | 727 ms                                                 | 698 ms: 1.04x faster                                              |
| pycparser                  | 1.20 sec                                               | 1.15 sec: 1.04x faster                                            |
| python_startup             | 12.7 ms                                                | 12.2 ms: 1.04x faster                                             |
| sqlite_synth               | 2.90 us                                                | 2.80 us: 1.04x faster                                             |
| crypto_pyaes               | 74.7 ms                                                | 72.2 ms: 1.03x faster                                             |
| thrift                     | 800 us                                                 | 776 us: 1.03x faster                                              |
| xml_etree_iterparse        | 101 ms                                                 | 98.2 ms: 1.03x faster                                             |
| html5lib                   | 63.4 ms                                                | 61.7 ms: 1.03x faster                                             |
| regex_dna                  | 220 ms                                                 | 216 ms: 1.02x faster                                              |
| regex_compile              | 132 ms                                                 | 130 ms: 1.02x faster                                              |
| mako                       | 10.7 ms                                                | 10.5 ms: 1.02x faster                                             |
| scimark_sor                | 122 ms                                                 | 120 ms: 1.02x faster                                              |
| comprehensions             | 16.5 us                                                | 16.2 us: 1.02x faster                                             |
| async_generators           | 433 ms                                                 | 427 ms: 1.01x faster                                              |
| pathlib                    | 17.4 ms                                                | 17.2 ms: 1.01x faster                                             |
| python_startup_no_site     | 7.00 ms                                                | 6.95 ms: 1.01x faster                                             |
| 2to3                       | 266 ms                                                 | 267 ms: 1.00x slower                                              |
| logging_simple             | 5.65 us                                                | 5.68 us: 1.01x slower                                             |
| fannkuch                   | 394 ms                                                 | 396 ms: 1.01x slower                                              |
| genshi_xml                 | 50.5 ms                                                | 50.9 ms: 1.01x slower                                             |
| shortest_path              | 487 ms                                                 | 492 ms: 1.01x slower                                              |
| logging_silent             | 101 ns                                                 | 102 ns: 1.01x slower                                              |
| sympy_sum                  | 150 ms                                                 | 153 ms: 1.02x slower                                              |
| logging_format             | 6.23 us                                                | 6.35 us: 1.02x slower                                             |
| djangocms                  | 22.3 us                                                | 22.8 us: 1.02x slower                                             |
| gc_traversal               | 4.90 ms                                                | 5.03 ms: 1.03x slower                                             |
| connected_components       | 447 ms                                                 | 459 ms: 1.03x slower                                              |
| sympy_expand               | 456 ms                                                 | 470 ms: 1.03x slower                                              |
| django_template            | 31.7 ms                                                | 32.6 ms: 1.03x slower                                             |
| raytrace                   | 262 ms                                                 | 270 ms: 1.03x slower                                              |
| pidigits                   | 186 ms                                                 | 193 ms: 1.04x slower                                              |
| docutils                   | 2.58 sec                                               | 2.69 sec: 1.04x slower                                            |
| nqueens                    | 80.9 ms                                                | 84.1 ms: 1.04x slower                                             |
| scimark_lu                 | 114 ms                                                 | 119 ms: 1.04x slower                                              |
| chaos                      | 58.0 ms                                                | 60.5 ms: 1.04x slower                                             |
| coverage                   | 82.8 ms                                                | 87.4 ms: 1.06x slower                                             |
| generators                 | 28.8 ms                                                | 30.4 ms: 1.06x slower                                             |
| nbody                      | 87.7 ms                                                | 92.9 ms: 1.06x slower                                             |
| pickle_pure_python         | 302 us                                                 | 321 us: 1.06x slower                                              |
| typing_runtime_protocols   | 160 us                                                 | 170 us: 1.06x slower                                              |
| json_loads                 | 27.2 us                                                | 28.9 us: 1.07x slower                                             |
| create_gc_cycles           | 2.45 ms                                                | 2.64 ms: 1.08x slower                                             |
| json_dumps                 | 10.1 ms                                                | 11.1 ms: 1.09x slower                                             |
| coroutines                 | 22.2 ms                                                | 25.4 ms: 1.14x slower                                             |
| many_optionals             | 857 us                                                 | 999 us: 1.17x slower                                              |
| subparsers                 | 15.5 ms                                                | 23.9 ms: 1.55x slower                                             |
| telco                      | 8.40 ms                                                | 161 ms: 19.20x slower                                             |
| Geometric mean             | (ref)                                                  | 1.02x faster                                                      |

Benchmark hidden because not significant (8): sphinx, scimark_sparse_mat_mult, hexiom, sympy_integrate, json, asyncio_websockets, scimark_monte_carlo, sympy_str
Ignored benchmarks (12) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: bench_mp_pool, bench_thread_pool, chameleon, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250702-3.15.0a0-6c99b17-JIT/bm-20250702-linux-x86_64-brandtbucher-jit_up_6_6-3.15.0a0-6c99b17.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.023x faster

# HPT report

- Reliability score: 99.70% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.11x
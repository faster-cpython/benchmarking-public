# Results vs. 3.13.0

- fork: brandtbucher
- ref: jit_cached_consts
- machine: linux-x86_64
- commit hash: 4953e8a
- commit date: 2025-03-28
- overall geometric mean: 1.049x faster
- HPT reliability: 99.83%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250328-linux-x86_64-brandtbucher-jit_cached_consts-3.14.0a6+-4953e8a |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 261 ms: 1.02x faster                                                      |
| docutils       | 2.58 sec                                               | 2.66 sec: 1.03x slower                                                    |
| html5lib       | 63.4 ms                                                | 61.7 ms: 1.03x faster                                                     |
| sphinx         | 1.03 sec                                               | 1.02 sec: 1.01x faster                                                    |
| Geometric mean | (ref)                                                  | 1.01x faster                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250328-linux-x86_64-brandtbucher-jit_cached_consts-3.14.0a6+-4953e8a |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 314 ms: 1.47x faster                                                      |
| async_tree_io_tg           | 861 ms                                                 | 614 ms: 1.40x faster                                                      |
| async_tree_memoization     | 437 ms                                                 | 316 ms: 1.38x faster                                                      |
| async_tree_io              | 838 ms                                                 | 612 ms: 1.37x faster                                                      |
| async_tree_none            | 350 ms                                                 | 256 ms: 1.37x faster                                                      |
| async_tree_none_tg         | 319 ms                                                 | 249 ms: 1.28x faster                                                      |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 488 ms: 1.18x faster                                                      |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 473 ms: 1.15x faster                                                      |
| async_generators           | 433 ms                                                 | 419 ms: 1.03x faster                                                      |
| coroutines                 | 22.2 ms                                                | 23.3 ms: 1.05x slower                                                     |
| Geometric mean             | (ref)                                                  | 1.22x faster                                                              |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250328-linux-x86_64-brandtbucher-jit_cached_consts-3.14.0a6+-4953e8a |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 64.6 ms: 1.22x faster                                                     |
| pidigits       | 186 ms                                                 | 186 ms: 1.01x faster                                                      |
| nbody          | 87.7 ms                                                | 88.7 ms: 1.01x slower                                                     |
| Geometric mean | (ref)                                                  | 1.07x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250328-linux-x86_64-brandtbucher-jit_cached_consts-3.14.0a6+-4953e8a |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                | 3.16 ms: 1.19x faster                                                     |
| regex_v8       | 26.9 ms                                                | 23.1 ms: 1.16x faster                                                     |
| regex_compile  | 132 ms                                                 | 127 ms: 1.04x faster                                                      |
| regex_dna      | 220 ms                                                 | 217 ms: 1.02x faster                                                      |
| Geometric mean | (ref)                                                  | 1.10x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250328-linux-x86_64-brandtbucher-jit_cached_consts-3.14.0a6+-4953e8a |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| tomli_loads          | 2.12 sec                                               | 1.85 sec: 1.14x faster                                                    |
| xml_etree_parse      | 154 ms                                                 | 140 ms: 1.10x faster                                                      |
| xml_etree_generate   | 86.8 ms                                                | 79.2 ms: 1.10x faster                                                     |
| xml_etree_process    | 60.5 ms                                                | 55.4 ms: 1.09x faster                                                     |
| xml_etree_iterparse  | 101 ms                                                 | 97.4 ms: 1.04x faster                                                     |
| unpickle_pure_python | 213 us                                                 | 212 us: 1.00x faster                                                      |
| pickle_pure_python   | 302 us                                                 | 322 us: 1.07x slower                                                      |
| json_loads           | 27.2 us                                                | 29.7 us: 1.09x slower                                                     |
| json_dumps           | 10.1 ms                                                | 11.6 ms: 1.15x slower                                                     |
| Geometric mean       | (ref)                                                  | 1.02x faster                                                              |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250328-linux-x86_64-brandtbucher-jit_cached_consts-3.14.0a6+-4953e8a |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 12.7 ms                                                | 13.1 ms: 1.03x slower                                                     |
| python_startup_no_site | 7.00 ms                                                | 8.19 ms: 1.17x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.10x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250328-linux-x86_64-brandtbucher-jit_cached_consts-3.14.0a6+-4953e8a |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| genshi_text    | 22.6 ms                                                | 20.8 ms: 1.09x faster                                                     |
| genshi_xml     | 50.5 ms                                                | 49.7 ms: 1.02x faster                                                     |
| mako           | 10.7 ms                                                | 10.9 ms: 1.03x slower                                                     |
| Geometric mean | (ref)                                                  | 1.02x faster                                                              |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250328-linux-x86_64-brandtbucher-jit_cached_consts-3.14.0a6+-4953e8a |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 314 ms: 1.47x faster                                                      |
| async_tree_io_tg           | 861 ms                                                 | 614 ms: 1.40x faster                                                      |
| deepcopy                   | 354 us                                                 | 254 us: 1.39x faster                                                      |
| async_tree_memoization     | 437 ms                                                 | 316 ms: 1.38x faster                                                      |
| async_tree_io              | 838 ms                                                 | 612 ms: 1.37x faster                                                      |
| async_tree_none            | 350 ms                                                 | 256 ms: 1.37x faster                                                      |
| richards                   | 47.5 ms                                                | 34.9 ms: 1.36x faster                                                     |
| richards_super             | 53.7 ms                                                | 39.7 ms: 1.35x faster                                                     |
| deepcopy_memo              | 38.4 us                                                | 29.5 us: 1.30x faster                                                     |
| async_tree_none_tg         | 319 ms                                                 | 249 ms: 1.28x faster                                                      |
| float                      | 78.7 ms                                                | 64.6 ms: 1.22x faster                                                     |
| deepcopy_reduce            | 3.24 us                                                | 2.69 us: 1.21x faster                                                     |
| spectral_norm              | 113 ms                                                 | 93.9 ms: 1.21x faster                                                     |
| regex_effbot               | 3.77 ms                                                | 3.16 ms: 1.19x faster                                                     |
| scimark_fft                | 367 ms                                                 | 309 ms: 1.19x faster                                                      |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 488 ms: 1.18x faster                                                      |
| regex_v8                   | 26.9 ms                                                | 23.1 ms: 1.16x faster                                                     |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 473 ms: 1.15x faster                                                      |
| tomli_loads                | 2.12 sec                                               | 1.85 sec: 1.14x faster                                                    |
| pylint                     | 312 ms                                                 | 280 ms: 1.11x faster                                                      |
| go                         | 141 ms                                                 | 126 ms: 1.11x faster                                                      |
| xml_etree_parse            | 154 ms                                                 | 140 ms: 1.10x faster                                                      |
| xml_etree_generate         | 86.8 ms                                                | 79.2 ms: 1.10x faster                                                     |
| xml_etree_process          | 60.5 ms                                                | 55.4 ms: 1.09x faster                                                     |
| genshi_text                | 22.6 ms                                                | 20.8 ms: 1.09x faster                                                     |
| pyflate                    | 470 ms                                                 | 433 ms: 1.08x faster                                                      |
| sqlite_synth               | 2.90 us                                                | 2.69 us: 1.08x faster                                                     |
| pycparser                  | 1.20 sec                                               | 1.12 sec: 1.07x faster                                                    |
| telco                      | 8.40 ms                                                | 7.85 ms: 1.07x faster                                                     |
| dulwich_log                | 64.6 ms                                                | 60.4 ms: 1.07x faster                                                     |
| deltablue                  | 3.19 ms                                                | 2.99 ms: 1.07x faster                                                     |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.76 ms: 1.06x faster                                                     |
| thrift                     | 800 us                                                 | 764 us: 1.05x faster                                                      |
| pathlib                    | 17.4 ms                                                | 16.6 ms: 1.05x faster                                                     |
| scimark_sor                | 122 ms                                                 | 117 ms: 1.04x faster                                                      |
| xml_etree_iterparse        | 101 ms                                                 | 97.4 ms: 1.04x faster                                                     |
| regex_compile              | 132 ms                                                 | 127 ms: 1.04x faster                                                      |
| logging_silent             | 101 ns                                                 | 97.4 ns: 1.04x faster                                                     |
| async_generators           | 433 ms                                                 | 419 ms: 1.03x faster                                                      |
| html5lib                   | 63.4 ms                                                | 61.7 ms: 1.03x faster                                                     |
| bpe_tokeniser              | 4.69 sec                                               | 4.57 sec: 1.03x faster                                                    |
| mdp                        | 2.54 sec                                               | 2.48 sec: 1.03x faster                                                    |
| generators                 | 28.8 ms                                                | 28.1 ms: 1.03x faster                                                     |
| k_core                     | 2.37 sec                                               | 2.32 sec: 1.02x faster                                                    |
| 2to3                       | 266 ms                                                 | 261 ms: 1.02x faster                                                      |
| genshi_xml                 | 50.5 ms                                                | 49.7 ms: 1.02x faster                                                     |
| regex_dna                  | 220 ms                                                 | 217 ms: 1.02x faster                                                      |
| sphinx                     | 1.03 sec                                               | 1.02 sec: 1.01x faster                                                    |
| json                       | 5.32 ms                                                | 5.26 ms: 1.01x faster                                                     |
| logging_simple             | 5.65 us                                                | 5.62 us: 1.01x faster                                                     |
| pidigits                   | 186 ms                                                 | 186 ms: 1.01x faster                                                      |
| meteor_contest             | 108 ms                                                 | 108 ms: 1.00x faster                                                      |
| unpickle_pure_python       | 213 us                                                 | 212 us: 1.00x faster                                                      |
| sqlalchemy_declarative     | 133 ms                                                 | 133 ms: 1.00x faster                                                      |
| sympy_sum                  | 150 ms                                                 | 152 ms: 1.01x slower                                                      |
| nbody                      | 87.7 ms                                                | 88.7 ms: 1.01x slower                                                     |
| sympy_integrate            | 19.8 ms                                                | 20.1 ms: 1.02x slower                                                     |
| chaos                      | 58.0 ms                                                | 59.0 ms: 1.02x slower                                                     |
| raytrace                   | 262 ms                                                 | 266 ms: 1.02x slower                                                      |
| shortest_path              | 487 ms                                                 | 496 ms: 1.02x slower                                                      |
| gc_traversal               | 4.90 ms                                                | 4.99 ms: 1.02x slower                                                     |
| create_gc_cycles           | 2.45 ms                                                | 2.50 ms: 1.02x slower                                                     |
| connected_components       | 447 ms                                                 | 457 ms: 1.02x slower                                                      |
| coverage                   | 82.8 ms                                                | 84.8 ms: 1.02x slower                                                     |
| mako                       | 10.7 ms                                                | 10.9 ms: 1.03x slower                                                     |
| docutils                   | 2.58 sec                                               | 2.66 sec: 1.03x slower                                                    |
| sympy_expand               | 456 ms                                                 | 470 ms: 1.03x slower                                                      |
| python_startup             | 12.7 ms                                                | 13.1 ms: 1.03x slower                                                     |
| scimark_lu                 | 114 ms                                                 | 119 ms: 1.04x slower                                                      |
| pprint_pformat             | 1.48 sec                                               | 1.54 sec: 1.04x slower                                                    |
| nqueens                    | 80.9 ms                                                | 84.4 ms: 1.04x slower                                                     |
| pprint_safe_repr           | 727 ms                                                 | 758 ms: 1.04x slower                                                      |
| coroutines                 | 22.2 ms                                                | 23.3 ms: 1.05x slower                                                     |
| crypto_pyaes               | 74.7 ms                                                | 78.7 ms: 1.05x slower                                                     |
| pickle_pure_python         | 302 us                                                 | 322 us: 1.07x slower                                                      |
| typing_runtime_protocols   | 160 us                                                 | 172 us: 1.07x slower                                                      |
| fannkuch                   | 394 ms                                                 | 423 ms: 1.07x slower                                                      |
| bench_thread_pool          | 818 us                                                 | 879 us: 1.08x slower                                                      |
| hexiom                     | 6.08 ms                                                | 6.64 ms: 1.09x slower                                                     |
| json_loads                 | 27.2 us                                                | 29.7 us: 1.09x slower                                                     |
| many_optionals             | 857 us                                                 | 964 us: 1.13x slower                                                      |
| json_dumps                 | 10.1 ms                                                | 11.6 ms: 1.15x slower                                                     |
| comprehensions             | 16.5 us                                                | 19.0 us: 1.15x slower                                                     |
| python_startup_no_site     | 7.00 ms                                                | 8.19 ms: 1.17x slower                                                     |
| subparsers                 | 15.5 ms                                                | 21.0 ms: 1.36x slower                                                     |
| bench_mp_pool              | 24.0 ms                                                | 82.5 ms: 3.44x slower                                                     |
| Geometric mean             | (ref)                                                  | 1.03x faster                                                              |

Benchmark hidden because not significant (6): logging_format, django_template, sqlalchemy_imperative, scimark_monte_carlo, sympy_str, asyncio_websockets
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250328-3.14.0a6+-4953e8a-JIT/bm-20250328-linux-x86_64-brandtbucher-jit_cached_consts-3.14.0a6+-4953e8a.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.049x faster

# HPT report

- Reliability score: 99.83% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.04x
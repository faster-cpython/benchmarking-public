# Results vs. 3.13.0

- fork: brandtbucher
- ref: jit_cached_consts
- machine: linux-x86_64
- commit hash: 6510018
- commit date: 2025-03-17
- overall geometric mean: 1.049x faster
- HPT reliability: 99.68%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250317-linux-x86_64-brandtbucher-jit_cached_consts-3.14.0a6+-6510018 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 261 ms: 1.02x faster                                                      |
| docutils       | 2.58 sec                                               | 2.68 sec: 1.04x slower                                                    |
| html5lib       | 63.4 ms                                                | 62.6 ms: 1.01x faster                                                     |
| Geometric mean | (ref)                                                  | 1.00x faster                                                              |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250317-linux-x86_64-brandtbucher-jit_cached_consts-3.14.0a6+-6510018 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 314 ms: 1.47x faster                                                      |
| async_tree_io_tg           | 861 ms                                                 | 614 ms: 1.40x faster                                                      |
| async_tree_memoization     | 437 ms                                                 | 314 ms: 1.39x faster                                                      |
| async_tree_io              | 838 ms                                                 | 609 ms: 1.38x faster                                                      |
| async_tree_none            | 350 ms                                                 | 255 ms: 1.37x faster                                                      |
| async_tree_none_tg         | 319 ms                                                 | 248 ms: 1.28x faster                                                      |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 490 ms: 1.17x faster                                                      |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 475 ms: 1.15x faster                                                      |
| async_generators           | 433 ms                                                 | 415 ms: 1.04x faster                                                      |
| coroutines                 | 22.2 ms                                                | 24.0 ms: 1.08x slower                                                     |
| Geometric mean             | (ref)                                                  | 1.22x faster                                                              |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250317-linux-x86_64-brandtbucher-jit_cached_consts-3.14.0a6+-6510018 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 64.8 ms: 1.21x faster                                                     |
| pidigits       | 186 ms                                                 | 186 ms: 1.00x faster                                                      |
| Geometric mean | (ref)                                                  | 1.07x faster                                                              |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250317-linux-x86_64-brandtbucher-jit_cached_consts-3.14.0a6+-6510018 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_v8       | 26.9 ms                                                | 23.2 ms: 1.16x faster                                                     |
| regex_effbot   | 3.77 ms                                                | 3.47 ms: 1.08x faster                                                     |
| regex_compile  | 132 ms                                                 | 126 ms: 1.04x faster                                                      |
| Geometric mean | (ref)                                                  | 1.07x faster                                                              |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250317-linux-x86_64-brandtbucher-jit_cached_consts-3.14.0a6+-6510018 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| tomli_loads          | 2.12 sec                                               | 1.86 sec: 1.14x faster                                                    |
| xml_etree_parse      | 154 ms                                                 | 139 ms: 1.11x faster                                                      |
| xml_etree_generate   | 86.8 ms                                                | 79.2 ms: 1.10x faster                                                     |
| xml_etree_process    | 60.5 ms                                                | 55.5 ms: 1.09x faster                                                     |
| xml_etree_iterparse  | 101 ms                                                 | 97.6 ms: 1.04x faster                                                     |
| unpickle_pure_python | 213 us                                                 | 212 us: 1.00x faster                                                      |
| pickle_pure_python   | 302 us                                                 | 320 us: 1.06x slower                                                      |
| json_loads           | 27.2 us                                                | 29.8 us: 1.10x slower                                                     |
| json_dumps           | 10.1 ms                                                | 11.6 ms: 1.15x slower                                                     |
| Geometric mean       | (ref)                                                  | 1.02x faster                                                              |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250317-linux-x86_64-brandtbucher-jit_cached_consts-3.14.0a6+-6510018 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 12.7 ms                                                | 13.1 ms: 1.04x slower                                                     |
| python_startup_no_site | 7.00 ms                                                | 8.20 ms: 1.17x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.10x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250317-linux-x86_64-brandtbucher-jit_cached_consts-3.14.0a6+-6510018 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| genshi_text    | 22.6 ms                                                | 21.2 ms: 1.07x faster                                                     |
| mako           | 10.7 ms                                                | 11.1 ms: 1.04x slower                                                     |
| Geometric mean | (ref)                                                  | 1.01x faster                                                              |

Benchmark hidden because not significant (2): genshi_xml, django_template

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250317-linux-x86_64-brandtbucher-jit_cached_consts-3.14.0a6+-6510018 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 314 ms: 1.47x faster                                                      |
| async_tree_io_tg           | 861 ms                                                 | 614 ms: 1.40x faster                                                      |
| deepcopy                   | 354 us                                                 | 254 us: 1.40x faster                                                      |
| async_tree_memoization     | 437 ms                                                 | 314 ms: 1.39x faster                                                      |
| async_tree_io              | 838 ms                                                 | 609 ms: 1.38x faster                                                      |
| async_tree_none            | 350 ms                                                 | 255 ms: 1.37x faster                                                      |
| richards                   | 47.5 ms                                                | 34.6 ms: 1.37x faster                                                     |
| richards_super             | 53.7 ms                                                | 39.7 ms: 1.35x faster                                                     |
| deepcopy_memo              | 38.4 us                                                | 28.5 us: 1.35x faster                                                     |
| async_tree_none_tg         | 319 ms                                                 | 248 ms: 1.28x faster                                                      |
| deepcopy_reduce            | 3.24 us                                                | 2.67 us: 1.22x faster                                                     |
| float                      | 78.7 ms                                                | 64.8 ms: 1.21x faster                                                     |
| spectral_norm              | 113 ms                                                 | 94.3 ms: 1.20x faster                                                     |
| scimark_fft                | 367 ms                                                 | 310 ms: 1.18x faster                                                      |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 490 ms: 1.17x faster                                                      |
| regex_v8                   | 26.9 ms                                                | 23.2 ms: 1.16x faster                                                     |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 475 ms: 1.15x faster                                                      |
| tomli_loads                | 2.12 sec                                               | 1.86 sec: 1.14x faster                                                    |
| pylint                     | 312 ms                                                 | 281 ms: 1.11x faster                                                      |
| xml_etree_parse            | 154 ms                                                 | 139 ms: 1.11x faster                                                      |
| xml_etree_generate         | 86.8 ms                                                | 79.2 ms: 1.10x faster                                                     |
| go                         | 141 ms                                                 | 129 ms: 1.09x faster                                                      |
| xml_etree_process          | 60.5 ms                                                | 55.5 ms: 1.09x faster                                                     |
| regex_effbot               | 3.77 ms                                                | 3.47 ms: 1.08x faster                                                     |
| telco                      | 8.40 ms                                                | 7.80 ms: 1.08x faster                                                     |
| dulwich_log                | 64.6 ms                                                | 60.0 ms: 1.08x faster                                                     |
| sqlite_synth               | 2.90 us                                                | 2.70 us: 1.08x faster                                                     |
| deltablue                  | 3.19 ms                                                | 2.97 ms: 1.07x faster                                                     |
| genshi_text                | 22.6 ms                                                | 21.2 ms: 1.07x faster                                                     |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.71 ms: 1.07x faster                                                     |
| pathlib                    | 17.4 ms                                                | 16.4 ms: 1.06x faster                                                     |
| scimark_sor                | 122 ms                                                 | 116 ms: 1.05x faster                                                      |
| pyflate                    | 470 ms                                                 | 449 ms: 1.05x faster                                                      |
| thrift                     | 800 us                                                 | 765 us: 1.05x faster                                                      |
| regex_compile              | 132 ms                                                 | 126 ms: 1.04x faster                                                      |
| logging_silent             | 101 ns                                                 | 96.7 ns: 1.04x faster                                                     |
| async_generators           | 433 ms                                                 | 415 ms: 1.04x faster                                                      |
| xml_etree_iterparse        | 101 ms                                                 | 97.6 ms: 1.04x faster                                                     |
| mdp                        | 2.54 sec                                               | 2.46 sec: 1.04x faster                                                    |
| generators                 | 28.8 ms                                                | 27.9 ms: 1.03x faster                                                     |
| logging_simple             | 5.65 us                                                | 5.48 us: 1.03x faster                                                     |
| logging_format             | 6.23 us                                                | 6.05 us: 1.03x faster                                                     |
| pycparser                  | 1.20 sec                                               | 1.17 sec: 1.03x faster                                                    |
| k_core                     | 2.37 sec                                               | 2.31 sec: 1.02x faster                                                    |
| bpe_tokeniser              | 4.69 sec                                               | 4.59 sec: 1.02x faster                                                    |
| 2to3                       | 266 ms                                                 | 261 ms: 1.02x faster                                                      |
| html5lib                   | 63.4 ms                                                | 62.6 ms: 1.01x faster                                                     |
| pidigits                   | 186 ms                                                 | 186 ms: 1.00x faster                                                      |
| unpickle_pure_python       | 213 us                                                 | 212 us: 1.00x faster                                                      |
| sqlalchemy_declarative     | 133 ms                                                 | 132 ms: 1.00x faster                                                      |
| gc_traversal               | 4.90 ms                                                | 4.91 ms: 1.00x slower                                                     |
| sympy_sum                  | 150 ms                                                 | 151 ms: 1.00x slower                                                      |
| meteor_contest             | 108 ms                                                 | 109 ms: 1.01x slower                                                      |
| raytrace                   | 262 ms                                                 | 265 ms: 1.01x slower                                                      |
| create_gc_cycles           | 2.45 ms                                                | 2.49 ms: 1.02x slower                                                     |
| sympy_integrate            | 19.8 ms                                                | 20.1 ms: 1.02x slower                                                     |
| chaos                      | 58.0 ms                                                | 59.0 ms: 1.02x slower                                                     |
| connected_components       | 447 ms                                                 | 456 ms: 1.02x slower                                                      |
| coverage                   | 82.8 ms                                                | 84.5 ms: 1.02x slower                                                     |
| scimark_lu                 | 114 ms                                                 | 117 ms: 1.02x slower                                                      |
| pprint_safe_repr           | 727 ms                                                 | 745 ms: 1.03x slower                                                      |
| sympy_expand               | 456 ms                                                 | 471 ms: 1.03x slower                                                      |
| python_startup             | 12.7 ms                                                | 13.1 ms: 1.04x slower                                                     |
| docutils                   | 2.58 sec                                               | 2.68 sec: 1.04x slower                                                    |
| mako                       | 10.7 ms                                                | 11.1 ms: 1.04x slower                                                     |
| nqueens                    | 80.9 ms                                                | 84.4 ms: 1.04x slower                                                     |
| crypto_pyaes               | 74.7 ms                                                | 78.1 ms: 1.05x slower                                                     |
| typing_runtime_protocols   | 160 us                                                 | 168 us: 1.05x slower                                                      |
| pickle_pure_python         | 302 us                                                 | 320 us: 1.06x slower                                                      |
| pprint_pformat             | 1.48 sec                                               | 1.57 sec: 1.06x slower                                                    |
| bench_thread_pool          | 818 us                                                 | 874 us: 1.07x slower                                                      |
| coroutines                 | 22.2 ms                                                | 24.0 ms: 1.08x slower                                                     |
| fannkuch                   | 394 ms                                                 | 430 ms: 1.09x slower                                                      |
| json_loads                 | 27.2 us                                                | 29.8 us: 1.10x slower                                                     |
| hexiom                     | 6.08 ms                                                | 6.77 ms: 1.11x slower                                                     |
| many_optionals             | 857 us                                                 | 959 us: 1.12x slower                                                      |
| comprehensions             | 16.5 us                                                | 18.8 us: 1.14x slower                                                     |
| json_dumps                 | 10.1 ms                                                | 11.6 ms: 1.15x slower                                                     |
| python_startup_no_site     | 7.00 ms                                                | 8.20 ms: 1.17x slower                                                     |
| subparsers                 | 15.5 ms                                                | 20.6 ms: 1.34x slower                                                     |
| bench_mp_pool              | 24.0 ms                                                | 82.9 ms: 3.46x slower                                                     |
| Geometric mean             | (ref)                                                  | 1.03x faster                                                              |

Benchmark hidden because not significant (11): sphinx, genshi_xml, json, django_template, sqlalchemy_imperative, asyncio_websockets, regex_dna, scimark_monte_carlo, shortest_path, sympy_str, nbody
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250317-3.14.0a6+-6510018-JIT/bm-20250317-linux-x86_64-brandtbucher-jit_cached_consts-3.14.0a6+-6510018.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.049x faster

# HPT report

- Reliability score: 99.68% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.04x
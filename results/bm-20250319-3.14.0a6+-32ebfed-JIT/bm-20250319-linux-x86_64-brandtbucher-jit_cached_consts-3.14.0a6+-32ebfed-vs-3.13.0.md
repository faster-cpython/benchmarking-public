# Results vs. 3.13.0

- fork: brandtbucher
- ref: jit_cached_consts
- machine: linux-x86_64
- commit hash: 32ebfed
- commit date: 2025-03-19
- overall geometric mean: 1.045x faster
- HPT reliability: 99.52%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250319-linux-x86_64-brandtbucher-jit_cached_consts-3.14.0a6+-32ebfed |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 262 ms: 1.01x faster                                                      |
| docutils       | 2.58 sec                                               | 2.69 sec: 1.04x slower                                                    |
| Geometric mean | (ref)                                                  | 1.00x slower                                                              |

Benchmark hidden because not significant (2): html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250319-linux-x86_64-brandtbucher-jit_cached_consts-3.14.0a6+-32ebfed |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 317 ms: 1.46x faster                                                      |
| async_tree_io_tg           | 861 ms                                                 | 620 ms: 1.39x faster                                                      |
| async_tree_memoization     | 437 ms                                                 | 319 ms: 1.37x faster                                                      |
| async_tree_io              | 838 ms                                                 | 620 ms: 1.35x faster                                                      |
| async_tree_none            | 350 ms                                                 | 259 ms: 1.35x faster                                                      |
| async_tree_none_tg         | 319 ms                                                 | 251 ms: 1.27x faster                                                      |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 496 ms: 1.16x faster                                                      |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 478 ms: 1.14x faster                                                      |
| async_generators           | 433 ms                                                 | 421 ms: 1.03x faster                                                      |
| coroutines                 | 22.2 ms                                                | 23.8 ms: 1.07x slower                                                     |
| Geometric mean             | (ref)                                                  | 1.21x faster                                                              |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250319-linux-x86_64-brandtbucher-jit_cached_consts-3.14.0a6+-32ebfed |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 65.2 ms: 1.21x faster                                                     |
| nbody          | 87.7 ms                                                | 86.9 ms: 1.01x faster                                                     |
| pidigits       | 186 ms                                                 | 186 ms: 1.00x faster                                                      |
| Geometric mean | (ref)                                                  | 1.07x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250319-linux-x86_64-brandtbucher-jit_cached_consts-3.14.0a6+-32ebfed |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_v8       | 26.9 ms                                                | 23.2 ms: 1.16x faster                                                     |
| regex_effbot   | 3.77 ms                                                | 3.45 ms: 1.09x faster                                                     |
| regex_compile  | 132 ms                                                 | 128 ms: 1.03x faster                                                      |
| Geometric mean | (ref)                                                  | 1.07x faster                                                              |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250319-linux-x86_64-brandtbucher-jit_cached_consts-3.14.0a6+-32ebfed |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| tomli_loads          | 2.12 sec                                               | 1.86 sec: 1.14x faster                                                    |
| xml_etree_parse      | 154 ms                                                 | 140 ms: 1.10x faster                                                      |
| xml_etree_generate   | 86.8 ms                                                | 79.3 ms: 1.10x faster                                                     |
| xml_etree_process    | 60.5 ms                                                | 55.5 ms: 1.09x faster                                                     |
| xml_etree_iterparse  | 101 ms                                                 | 97.7 ms: 1.04x faster                                                     |
| unpickle_pure_python | 213 us                                                 | 213 us: 1.00x faster                                                      |
| pickle_pure_python   | 302 us                                                 | 321 us: 1.06x slower                                                      |
| json_loads           | 27.2 us                                                | 29.8 us: 1.10x slower                                                     |
| json_dumps           | 10.1 ms                                                | 11.5 ms: 1.14x slower                                                     |
| Geometric mean       | (ref)                                                  | 1.02x faster                                                              |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250319-linux-x86_64-brandtbucher-jit_cached_consts-3.14.0a6+-32ebfed |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 12.7 ms                                                | 13.1 ms: 1.04x slower                                                     |
| python_startup_no_site | 7.00 ms                                                | 8.20 ms: 1.17x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.10x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250319-linux-x86_64-brandtbucher-jit_cached_consts-3.14.0a6+-32ebfed |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| genshi_text    | 22.6 ms                                                | 21.0 ms: 1.08x faster                                                     |
| genshi_xml     | 50.5 ms                                                | 49.9 ms: 1.01x faster                                                     |
| mako           | 10.7 ms                                                | 10.9 ms: 1.02x slower                                                     |
| Geometric mean | (ref)                                                  | 1.02x faster                                                              |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250319-linux-x86_64-brandtbucher-jit_cached_consts-3.14.0a6+-32ebfed |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 317 ms: 1.46x faster                                                      |
| async_tree_io_tg           | 861 ms                                                 | 620 ms: 1.39x faster                                                      |
| deepcopy                   | 354 us                                                 | 256 us: 1.38x faster                                                      |
| async_tree_memoization     | 437 ms                                                 | 319 ms: 1.37x faster                                                      |
| richards                   | 47.5 ms                                                | 34.9 ms: 1.36x faster                                                     |
| async_tree_io              | 838 ms                                                 | 620 ms: 1.35x faster                                                      |
| async_tree_none            | 350 ms                                                 | 259 ms: 1.35x faster                                                      |
| richards_super             | 53.7 ms                                                | 40.3 ms: 1.33x faster                                                     |
| deepcopy_memo              | 38.4 us                                                | 29.4 us: 1.30x faster                                                     |
| async_tree_none_tg         | 319 ms                                                 | 251 ms: 1.27x faster                                                      |
| float                      | 78.7 ms                                                | 65.2 ms: 1.21x faster                                                     |
| spectral_norm              | 113 ms                                                 | 95.8 ms: 1.18x faster                                                     |
| scimark_fft                | 367 ms                                                 | 311 ms: 1.18x faster                                                      |
| deepcopy_reduce            | 3.24 us                                                | 2.75 us: 1.18x faster                                                     |
| regex_v8                   | 26.9 ms                                                | 23.2 ms: 1.16x faster                                                     |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 496 ms: 1.16x faster                                                      |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 478 ms: 1.14x faster                                                      |
| tomli_loads                | 2.12 sec                                               | 1.86 sec: 1.14x faster                                                    |
| pylint                     | 312 ms                                                 | 281 ms: 1.11x faster                                                      |
| xml_etree_parse            | 154 ms                                                 | 140 ms: 1.10x faster                                                      |
| xml_etree_generate         | 86.8 ms                                                | 79.3 ms: 1.10x faster                                                     |
| go                         | 141 ms                                                 | 129 ms: 1.09x faster                                                      |
| regex_effbot               | 3.77 ms                                                | 3.45 ms: 1.09x faster                                                     |
| xml_etree_process          | 60.5 ms                                                | 55.5 ms: 1.09x faster                                                     |
| sqlite_synth               | 2.90 us                                                | 2.69 us: 1.08x faster                                                     |
| genshi_text                | 22.6 ms                                                | 21.0 ms: 1.08x faster                                                     |
| deltablue                  | 3.19 ms                                                | 3.01 ms: 1.06x faster                                                     |
| telco                      | 8.40 ms                                                | 7.92 ms: 1.06x faster                                                     |
| dulwich_log                | 64.6 ms                                                | 60.9 ms: 1.06x faster                                                     |
| pyflate                    | 470 ms                                                 | 444 ms: 1.06x faster                                                      |
| pathlib                    | 17.4 ms                                                | 16.7 ms: 1.04x faster                                                     |
| scimark_sor                | 122 ms                                                 | 117 ms: 1.04x faster                                                      |
| xml_etree_iterparse        | 101 ms                                                 | 97.7 ms: 1.04x faster                                                     |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.86 ms: 1.04x faster                                                     |
| generators                 | 28.8 ms                                                | 27.8 ms: 1.04x faster                                                     |
| regex_compile              | 132 ms                                                 | 128 ms: 1.03x faster                                                      |
| logging_silent             | 101 ns                                                 | 98.1 ns: 1.03x faster                                                     |
| async_generators           | 433 ms                                                 | 421 ms: 1.03x faster                                                      |
| mdp                        | 2.54 sec                                               | 2.48 sec: 1.03x faster                                                    |
| logging_simple             | 5.65 us                                                | 5.53 us: 1.02x faster                                                     |
| pycparser                  | 1.20 sec                                               | 1.17 sec: 1.02x faster                                                    |
| thrift                     | 800 us                                                 | 786 us: 1.02x faster                                                      |
| gc_traversal               | 4.90 ms                                                | 4.83 ms: 1.01x faster                                                     |
| bpe_tokeniser              | 4.69 sec                                               | 4.62 sec: 1.01x faster                                                    |
| 2to3                       | 266 ms                                                 | 262 ms: 1.01x faster                                                      |
| logging_format             | 6.23 us                                                | 6.16 us: 1.01x faster                                                     |
| genshi_xml                 | 50.5 ms                                                | 49.9 ms: 1.01x faster                                                     |
| nbody                      | 87.7 ms                                                | 86.9 ms: 1.01x faster                                                     |
| pidigits                   | 186 ms                                                 | 186 ms: 1.00x faster                                                      |
| unpickle_pure_python       | 213 us                                                 | 213 us: 1.00x faster                                                      |
| sqlalchemy_declarative     | 133 ms                                                 | 133 ms: 1.00x slower                                                      |
| meteor_contest             | 108 ms                                                 | 109 ms: 1.01x slower                                                      |
| scimark_monte_carlo        | 66.8 ms                                                | 67.6 ms: 1.01x slower                                                     |
| raytrace                   | 262 ms                                                 | 266 ms: 1.02x slower                                                      |
| create_gc_cycles           | 2.45 ms                                                | 2.50 ms: 1.02x slower                                                     |
| mako                       | 10.7 ms                                                | 10.9 ms: 1.02x slower                                                     |
| chaos                      | 58.0 ms                                                | 59.4 ms: 1.02x slower                                                     |
| coverage                   | 82.8 ms                                                | 84.8 ms: 1.02x slower                                                     |
| shortest_path              | 487 ms                                                 | 499 ms: 1.02x slower                                                      |
| connected_components       | 447 ms                                                 | 460 ms: 1.03x slower                                                      |
| scimark_lu                 | 114 ms                                                 | 118 ms: 1.03x slower                                                      |
| python_startup             | 12.7 ms                                                | 13.1 ms: 1.04x slower                                                     |
| nqueens                    | 80.9 ms                                                | 84.1 ms: 1.04x slower                                                     |
| docutils                   | 2.58 sec                                               | 2.69 sec: 1.04x slower                                                    |
| crypto_pyaes               | 74.7 ms                                                | 78.2 ms: 1.05x slower                                                     |
| pprint_safe_repr           | 727 ms                                                 | 767 ms: 1.06x slower                                                      |
| pprint_pformat             | 1.48 sec                                               | 1.57 sec: 1.06x slower                                                    |
| pickle_pure_python         | 302 us                                                 | 321 us: 1.06x slower                                                      |
| typing_runtime_protocols   | 160 us                                                 | 171 us: 1.07x slower                                                      |
| coroutines                 | 22.2 ms                                                | 23.8 ms: 1.07x slower                                                     |
| fannkuch                   | 394 ms                                                 | 424 ms: 1.08x slower                                                      |
| bench_thread_pool          | 818 us                                                 | 882 us: 1.08x slower                                                      |
| json_loads                 | 27.2 us                                                | 29.8 us: 1.10x slower                                                     |
| hexiom                     | 6.08 ms                                                | 6.79 ms: 1.12x slower                                                     |
| many_optionals             | 857 us                                                 | 968 us: 1.13x slower                                                      |
| comprehensions             | 16.5 us                                                | 18.8 us: 1.14x slower                                                     |
| json_dumps                 | 10.1 ms                                                | 11.5 ms: 1.14x slower                                                     |
| python_startup_no_site     | 7.00 ms                                                | 8.20 ms: 1.17x slower                                                     |
| subparsers                 | 15.5 ms                                                | 21.2 ms: 1.37x slower                                                     |
| bench_mp_pool              | 24.0 ms                                                | 82.8 ms: 3.45x slower                                                     |
| Geometric mean             | (ref)                                                  | 1.03x faster                                                              |

Benchmark hidden because not significant (8): k_core, json, sphinx, django_template, html5lib, sqlalchemy_imperative, asyncio_websockets, regex_dna
Ignored benchmarks (13) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, sympy_expand, sympy_integrate, sympy_str, sympy_sum, tornado_http
Ignored benchmarks (4) of results/bm-20250319-3.14.0a6+-32ebfed-JIT/bm-20250319-linux-x86_64-brandtbucher-jit_cached_consts-3.14.0a6+-32ebfed.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.045x faster

# HPT report

- Reliability score: 99.52% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.04x
# Results vs. 3.13.0

- fork: brandtbucher
- ref: jit_unknown_syms
- machine: linux-x86_64
- commit hash: 88219fd
- commit date: 2025-03-19
- overall geometric mean: 1.045x faster
- HPT reliability: 99.52%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250319-linux-x86_64-brandtbucher-jit_unknown_syms-3.14.0a6+-88219fd |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 262 ms: 1.01x faster                                                     |
| docutils       | 2.58 sec                                               | 2.69 sec: 1.04x slower                                                   |
| Geometric mean | (ref)                                                  | 1.01x slower                                                             |

Benchmark hidden because not significant (2): html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250319-linux-x86_64-brandtbucher-jit_unknown_syms-3.14.0a6+-88219fd |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 315 ms: 1.47x faster                                                     |
| async_tree_io_tg           | 861 ms                                                 | 614 ms: 1.40x faster                                                     |
| async_tree_memoization     | 437 ms                                                 | 315 ms: 1.39x faster                                                     |
| async_tree_io              | 838 ms                                                 | 612 ms: 1.37x faster                                                     |
| async_tree_none            | 350 ms                                                 | 258 ms: 1.36x faster                                                     |
| async_tree_none_tg         | 319 ms                                                 | 249 ms: 1.28x faster                                                     |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 494 ms: 1.16x faster                                                     |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 478 ms: 1.14x faster                                                     |
| async_generators           | 433 ms                                                 | 415 ms: 1.05x faster                                                     |
| coroutines                 | 22.2 ms                                                | 23.4 ms: 1.05x slower                                                    |
| Geometric mean             | (ref)                                                  | 1.22x faster                                                             |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250319-linux-x86_64-brandtbucher-jit_unknown_syms-3.14.0a6+-88219fd |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 65.0 ms: 1.21x faster                                                    |
| nbody          | 87.7 ms                                                | 87.0 ms: 1.01x faster                                                    |
| pidigits       | 186 ms                                                 | 185 ms: 1.01x faster                                                     |
| Geometric mean | (ref)                                                  | 1.07x faster                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250319-linux-x86_64-brandtbucher-jit_unknown_syms-3.14.0a6+-88219fd |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_v8       | 26.9 ms                                                | 23.3 ms: 1.15x faster                                                    |
| regex_effbot   | 3.77 ms                                                | 3.53 ms: 1.07x faster                                                    |
| regex_compile  | 132 ms                                                 | 128 ms: 1.03x faster                                                     |
| Geometric mean | (ref)                                                  | 1.06x faster                                                             |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250319-linux-x86_64-brandtbucher-jit_unknown_syms-3.14.0a6+-88219fd |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| tomli_loads          | 2.12 sec                                               | 1.88 sec: 1.13x faster                                                   |
| xml_etree_parse      | 154 ms                                                 | 140 ms: 1.10x faster                                                     |
| xml_etree_generate   | 86.8 ms                                                | 80.1 ms: 1.08x faster                                                    |
| xml_etree_process    | 60.5 ms                                                | 55.8 ms: 1.08x faster                                                    |
| xml_etree_iterparse  | 101 ms                                                 | 97.8 ms: 1.04x faster                                                    |
| unpickle_pure_python | 213 us                                                 | 215 us: 1.01x slower                                                     |
| pickle_pure_python   | 302 us                                                 | 320 us: 1.06x slower                                                     |
| json_loads           | 27.2 us                                                | 29.6 us: 1.09x slower                                                    |
| json_dumps           | 10.1 ms                                                | 11.4 ms: 1.13x slower                                                    |
| Geometric mean       | (ref)                                                  | 1.02x faster                                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250319-linux-x86_64-brandtbucher-jit_unknown_syms-3.14.0a6+-88219fd |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 12.7 ms                                                | 13.1 ms: 1.03x slower                                                    |
| python_startup_no_site | 7.00 ms                                                | 8.16 ms: 1.17x slower                                                    |
| Geometric mean         | (ref)                                                  | 1.10x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250319-linux-x86_64-brandtbucher-jit_unknown_syms-3.14.0a6+-88219fd |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| genshi_text     | 22.6 ms                                                | 21.3 ms: 1.06x faster                                                    |
| django_template | 31.7 ms                                                | 31.4 ms: 1.01x faster                                                    |
| genshi_xml      | 50.5 ms                                                | 50.2 ms: 1.01x faster                                                    |
| mako            | 10.7 ms                                                | 11.0 ms: 1.03x slower                                                    |
| Geometric mean  | (ref)                                                  | 1.01x faster                                                             |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250319-linux-x86_64-brandtbucher-jit_unknown_syms-3.14.0a6+-88219fd |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 315 ms: 1.47x faster                                                     |
| async_tree_io_tg           | 861 ms                                                 | 614 ms: 1.40x faster                                                     |
| async_tree_memoization     | 437 ms                                                 | 315 ms: 1.39x faster                                                     |
| deepcopy                   | 354 us                                                 | 256 us: 1.39x faster                                                     |
| async_tree_io              | 838 ms                                                 | 612 ms: 1.37x faster                                                     |
| async_tree_none            | 350 ms                                                 | 258 ms: 1.36x faster                                                     |
| richards                   | 47.5 ms                                                | 35.3 ms: 1.35x faster                                                    |
| richards_super             | 53.7 ms                                                | 40.6 ms: 1.32x faster                                                    |
| deepcopy_memo              | 38.4 us                                                | 29.2 us: 1.32x faster                                                    |
| async_tree_none_tg         | 319 ms                                                 | 249 ms: 1.28x faster                                                     |
| float                      | 78.7 ms                                                | 65.0 ms: 1.21x faster                                                    |
| deepcopy_reduce            | 3.24 us                                                | 2.70 us: 1.20x faster                                                    |
| spectral_norm              | 113 ms                                                 | 96.3 ms: 1.18x faster                                                    |
| scimark_fft                | 367 ms                                                 | 313 ms: 1.17x faster                                                     |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 494 ms: 1.16x faster                                                     |
| regex_v8                   | 26.9 ms                                                | 23.3 ms: 1.15x faster                                                    |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 478 ms: 1.14x faster                                                     |
| tomli_loads                | 2.12 sec                                               | 1.88 sec: 1.13x faster                                                   |
| pylint                     | 312 ms                                                 | 282 ms: 1.11x faster                                                     |
| xml_etree_parse            | 154 ms                                                 | 140 ms: 1.10x faster                                                     |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.62 ms: 1.09x faster                                                    |
| go                         | 141 ms                                                 | 129 ms: 1.09x faster                                                     |
| xml_etree_generate         | 86.8 ms                                                | 80.1 ms: 1.08x faster                                                    |
| xml_etree_process          | 60.5 ms                                                | 55.8 ms: 1.08x faster                                                    |
| dulwich_log                | 64.6 ms                                                | 60.4 ms: 1.07x faster                                                    |
| regex_effbot               | 3.77 ms                                                | 3.53 ms: 1.07x faster                                                    |
| telco                      | 8.40 ms                                                | 7.87 ms: 1.07x faster                                                    |
| sqlite_synth               | 2.90 us                                                | 2.72 us: 1.07x faster                                                    |
| genshi_text                | 22.6 ms                                                | 21.3 ms: 1.06x faster                                                    |
| logging_silent             | 101 ns                                                 | 95.4 ns: 1.06x faster                                                    |
| async_generators           | 433 ms                                                 | 415 ms: 1.05x faster                                                     |
| pathlib                    | 17.4 ms                                                | 16.7 ms: 1.04x faster                                                    |
| pyflate                    | 470 ms                                                 | 451 ms: 1.04x faster                                                     |
| deltablue                  | 3.19 ms                                                | 3.07 ms: 1.04x faster                                                    |
| thrift                     | 800 us                                                 | 773 us: 1.04x faster                                                     |
| xml_etree_iterparse        | 101 ms                                                 | 97.8 ms: 1.04x faster                                                    |
| k_core                     | 2.37 sec                                               | 2.30 sec: 1.03x faster                                                   |
| scimark_sor                | 122 ms                                                 | 119 ms: 1.03x faster                                                     |
| regex_compile              | 132 ms                                                 | 128 ms: 1.03x faster                                                     |
| mdp                        | 2.54 sec                                               | 2.48 sec: 1.03x faster                                                   |
| logging_simple             | 5.65 us                                                | 5.57 us: 1.02x faster                                                    |
| bpe_tokeniser              | 4.69 sec                                               | 4.62 sec: 1.01x faster                                                   |
| pycparser                  | 1.20 sec                                               | 1.18 sec: 1.01x faster                                                   |
| 2to3                       | 266 ms                                                 | 262 ms: 1.01x faster                                                     |
| django_template            | 31.7 ms                                                | 31.4 ms: 1.01x faster                                                    |
| nbody                      | 87.7 ms                                                | 87.0 ms: 1.01x faster                                                    |
| genshi_xml                 | 50.5 ms                                                | 50.2 ms: 1.01x faster                                                    |
| pidigits                   | 186 ms                                                 | 185 ms: 1.01x faster                                                     |
| sqlalchemy_imperative      | 16.9 ms                                                | 17.0 ms: 1.00x slower                                                    |
| unpickle_pure_python       | 213 us                                                 | 215 us: 1.01x slower                                                     |
| meteor_contest             | 108 ms                                                 | 109 ms: 1.01x slower                                                     |
| shortest_path              | 487 ms                                                 | 492 ms: 1.01x slower                                                     |
| connected_components       | 447 ms                                                 | 453 ms: 1.01x slower                                                     |
| gc_traversal               | 4.90 ms                                                | 4.98 ms: 1.02x slower                                                    |
| scimark_monte_carlo        | 66.8 ms                                                | 67.9 ms: 1.02x slower                                                    |
| create_gc_cycles           | 2.45 ms                                                | 2.49 ms: 1.02x slower                                                    |
| coverage                   | 82.8 ms                                                | 84.4 ms: 1.02x slower                                                    |
| raytrace                   | 262 ms                                                 | 268 ms: 1.02x slower                                                     |
| mako                       | 10.7 ms                                                | 11.0 ms: 1.03x slower                                                    |
| chaos                      | 58.0 ms                                                | 59.8 ms: 1.03x slower                                                    |
| python_startup             | 12.7 ms                                                | 13.1 ms: 1.03x slower                                                    |
| scimark_lu                 | 114 ms                                                 | 118 ms: 1.03x slower                                                     |
| typing_runtime_protocols   | 160 us                                                 | 166 us: 1.04x slower                                                     |
| docutils                   | 2.58 sec                                               | 2.69 sec: 1.04x slower                                                   |
| crypto_pyaes               | 74.7 ms                                                | 78.1 ms: 1.05x slower                                                    |
| coroutines                 | 22.2 ms                                                | 23.4 ms: 1.05x slower                                                    |
| pprint_pformat             | 1.48 sec                                               | 1.56 sec: 1.06x slower                                                   |
| pickle_pure_python         | 302 us                                                 | 320 us: 1.06x slower                                                     |
| pprint_safe_repr           | 727 ms                                                 | 769 ms: 1.06x slower                                                     |
| nqueens                    | 80.9 ms                                                | 85.9 ms: 1.06x slower                                                    |
| bench_thread_pool          | 818 us                                                 | 881 us: 1.08x slower                                                     |
| fannkuch                   | 394 ms                                                 | 424 ms: 1.08x slower                                                     |
| json_loads                 | 27.2 us                                                | 29.6 us: 1.09x slower                                                    |
| hexiom                     | 6.08 ms                                                | 6.79 ms: 1.12x slower                                                    |
| json_dumps                 | 10.1 ms                                                | 11.4 ms: 1.13x slower                                                    |
| many_optionals             | 857 us                                                 | 966 us: 1.13x slower                                                     |
| comprehensions             | 16.5 us                                                | 18.8 us: 1.14x slower                                                    |
| python_startup_no_site     | 7.00 ms                                                | 8.16 ms: 1.17x slower                                                    |
| subparsers                 | 15.5 ms                                                | 21.0 ms: 1.36x slower                                                    |
| bench_mp_pool              | 24.0 ms                                                | 82.6 ms: 3.44x slower                                                    |
| Geometric mean             | (ref)                                                  | 1.03x faster                                                             |

Benchmark hidden because not significant (8): json, sphinx, generators, sqlalchemy_declarative, asyncio_websockets, logging_format, html5lib, regex_dna
Ignored benchmarks (13) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, sympy_expand, sympy_integrate, sympy_str, sympy_sum, tornado_http
Ignored benchmarks (4) of results/bm-20250319-3.14.0a6+-88219fd-JIT/bm-20250319-linux-x86_64-brandtbucher-jit_unknown_syms-3.14.0a6+-88219fd.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.045x faster

# HPT report

- Reliability score: 99.52% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.04x
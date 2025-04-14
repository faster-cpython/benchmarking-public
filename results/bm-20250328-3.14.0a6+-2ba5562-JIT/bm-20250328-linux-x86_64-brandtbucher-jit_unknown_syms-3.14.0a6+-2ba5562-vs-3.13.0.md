# Results vs. 3.13.0

- fork: brandtbucher
- ref: jit_unknown_syms
- machine: linux-x86_64
- commit hash: 2ba5562
- commit date: 2025-03-28
- overall geometric mean: 1.044x faster
- HPT reliability: 98.71%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250328-linux-x86_64-brandtbucher-jit_unknown_syms-3.14.0a6+-2ba5562 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 261 ms: 1.02x faster                                                     |
| docutils       | 2.58 sec                                               | 2.68 sec: 1.04x slower                                                   |
| Geometric mean | (ref)                                                  | 1.00x slower                                                             |

Benchmark hidden because not significant (2): html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250328-linux-x86_64-brandtbucher-jit_unknown_syms-3.14.0a6+-2ba5562 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 316 ms: 1.46x faster                                                     |
| async_tree_io_tg           | 861 ms                                                 | 617 ms: 1.39x faster                                                     |
| async_tree_memoization     | 437 ms                                                 | 316 ms: 1.38x faster                                                     |
| async_tree_io              | 838 ms                                                 | 611 ms: 1.37x faster                                                     |
| async_tree_none            | 350 ms                                                 | 261 ms: 1.34x faster                                                     |
| async_tree_none_tg         | 319 ms                                                 | 250 ms: 1.28x faster                                                     |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 489 ms: 1.17x faster                                                     |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 473 ms: 1.15x faster                                                     |
| async_generators           | 433 ms                                                 | 412 ms: 1.05x faster                                                     |
| coroutines                 | 22.2 ms                                                | 23.5 ms: 1.06x slower                                                    |
| Geometric mean             | (ref)                                                  | 1.22x faster                                                             |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250328-linux-x86_64-brandtbucher-jit_unknown_syms-3.14.0a6+-2ba5562 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 64.8 ms: 1.21x faster                                                    |
| pidigits       | 186 ms                                                 | 186 ms: 1.00x faster                                                     |
| Geometric mean | (ref)                                                  | 1.07x faster                                                             |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250328-linux-x86_64-brandtbucher-jit_unknown_syms-3.14.0a6+-2ba5562 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_v8       | 26.9 ms                                                | 23.4 ms: 1.15x faster                                                    |
| regex_effbot   | 3.77 ms                                                | 3.47 ms: 1.08x faster                                                    |
| regex_compile  | 132 ms                                                 | 127 ms: 1.04x faster                                                     |
| regex_dna      | 220 ms                                                 | 225 ms: 1.02x slower                                                     |
| Geometric mean | (ref)                                                  | 1.06x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250328-linux-x86_64-brandtbucher-jit_unknown_syms-3.14.0a6+-2ba5562 |
|---------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| tomli_loads         | 2.12 sec                                               | 1.86 sec: 1.14x faster                                                   |
| xml_etree_generate  | 86.8 ms                                                | 79.1 ms: 1.10x faster                                                    |
| xml_etree_parse     | 154 ms                                                 | 141 ms: 1.10x faster                                                     |
| xml_etree_process   | 60.5 ms                                                | 55.2 ms: 1.10x faster                                                    |
| xml_etree_iterparse | 101 ms                                                 | 98.5 ms: 1.03x faster                                                    |
| pickle_pure_python  | 302 us                                                 | 322 us: 1.07x slower                                                     |
| json_loads          | 27.2 us                                                | 29.7 us: 1.10x slower                                                    |
| json_dumps          | 10.1 ms                                                | 11.4 ms: 1.12x slower                                                    |
| Geometric mean      | (ref)                                                  | 1.02x faster                                                             |

Benchmark hidden because not significant (1): unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250328-linux-x86_64-brandtbucher-jit_unknown_syms-3.14.0a6+-2ba5562 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 12.7 ms                                                | 13.1 ms: 1.03x slower                                                    |
| python_startup_no_site | 7.00 ms                                                | 8.19 ms: 1.17x slower                                                    |
| Geometric mean         | (ref)                                                  | 1.10x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250328-linux-x86_64-brandtbucher-jit_unknown_syms-3.14.0a6+-2ba5562 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| genshi_text     | 22.6 ms                                                | 21.1 ms: 1.07x faster                                                    |
| django_template | 31.7 ms                                                | 31.5 ms: 1.01x faster                                                    |
| mako            | 10.7 ms                                                | 11.0 ms: 1.03x slower                                                    |
| Geometric mean  | (ref)                                                  | 1.01x faster                                                             |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250328-linux-x86_64-brandtbucher-jit_unknown_syms-3.14.0a6+-2ba5562 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 316 ms: 1.46x faster                                                     |
| async_tree_io_tg           | 861 ms                                                 | 617 ms: 1.39x faster                                                     |
| async_tree_memoization     | 437 ms                                                 | 316 ms: 1.38x faster                                                     |
| deepcopy                   | 354 us                                                 | 257 us: 1.38x faster                                                     |
| async_tree_io              | 838 ms                                                 | 611 ms: 1.37x faster                                                     |
| richards                   | 47.5 ms                                                | 35.2 ms: 1.35x faster                                                    |
| richards_super             | 53.7 ms                                                | 40.0 ms: 1.34x faster                                                    |
| async_tree_none            | 350 ms                                                 | 261 ms: 1.34x faster                                                     |
| deepcopy_memo              | 38.4 us                                                | 29.3 us: 1.31x faster                                                    |
| async_tree_none_tg         | 319 ms                                                 | 250 ms: 1.28x faster                                                     |
| float                      | 78.7 ms                                                | 64.8 ms: 1.21x faster                                                    |
| deepcopy_reduce            | 3.24 us                                                | 2.70 us: 1.20x faster                                                    |
| spectral_norm              | 113 ms                                                 | 94.2 ms: 1.20x faster                                                    |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 489 ms: 1.17x faster                                                     |
| scimark_fft                | 367 ms                                                 | 314 ms: 1.17x faster                                                     |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 473 ms: 1.15x faster                                                     |
| regex_v8                   | 26.9 ms                                                | 23.4 ms: 1.15x faster                                                    |
| tomli_loads                | 2.12 sec                                               | 1.86 sec: 1.14x faster                                                   |
| pylint                     | 312 ms                                                 | 279 ms: 1.12x faster                                                     |
| go                         | 141 ms                                                 | 127 ms: 1.11x faster                                                     |
| xml_etree_generate         | 86.8 ms                                                | 79.1 ms: 1.10x faster                                                    |
| xml_etree_parse            | 154 ms                                                 | 141 ms: 1.10x faster                                                     |
| xml_etree_process          | 60.5 ms                                                | 55.2 ms: 1.10x faster                                                    |
| regex_effbot               | 3.77 ms                                                | 3.47 ms: 1.08x faster                                                    |
| pyflate                    | 470 ms                                                 | 436 ms: 1.08x faster                                                     |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.68 ms: 1.07x faster                                                    |
| telco                      | 8.40 ms                                                | 7.82 ms: 1.07x faster                                                    |
| genshi_text                | 22.6 ms                                                | 21.1 ms: 1.07x faster                                                    |
| dulwich_log                | 64.6 ms                                                | 60.5 ms: 1.07x faster                                                    |
| sqlite_synth               | 2.90 us                                                | 2.73 us: 1.06x faster                                                    |
| pathlib                    | 17.4 ms                                                | 16.5 ms: 1.05x faster                                                    |
| async_generators           | 433 ms                                                 | 412 ms: 1.05x faster                                                     |
| deltablue                  | 3.19 ms                                                | 3.06 ms: 1.04x faster                                                    |
| regex_compile              | 132 ms                                                 | 127 ms: 1.04x faster                                                     |
| thrift                     | 800 us                                                 | 770 us: 1.04x faster                                                     |
| mdp                        | 2.54 sec                                               | 2.46 sec: 1.03x faster                                                   |
| scimark_sor                | 122 ms                                                 | 118 ms: 1.03x faster                                                     |
| logging_silent             | 101 ns                                                 | 98.1 ns: 1.03x faster                                                    |
| xml_etree_iterparse        | 101 ms                                                 | 98.5 ms: 1.03x faster                                                    |
| generators                 | 28.8 ms                                                | 28.1 ms: 1.03x faster                                                    |
| pycparser                  | 1.20 sec                                               | 1.17 sec: 1.02x faster                                                   |
| bpe_tokeniser              | 4.69 sec                                               | 4.60 sec: 1.02x faster                                                   |
| 2to3                       | 266 ms                                                 | 261 ms: 1.02x faster                                                     |
| sympy_sum                  | 150 ms                                                 | 149 ms: 1.01x faster                                                     |
| django_template            | 31.7 ms                                                | 31.5 ms: 1.01x faster                                                    |
| pidigits                   | 186 ms                                                 | 186 ms: 1.00x faster                                                     |
| sqlalchemy_declarative     | 133 ms                                                 | 132 ms: 1.00x faster                                                     |
| scimark_monte_carlo        | 66.8 ms                                                | 67.1 ms: 1.01x slower                                                    |
| coverage                   | 82.8 ms                                                | 84.2 ms: 1.02x slower                                                    |
| shortest_path              | 487 ms                                                 | 495 ms: 1.02x slower                                                     |
| sympy_integrate            | 19.8 ms                                                | 20.2 ms: 1.02x slower                                                    |
| gc_traversal               | 4.90 ms                                                | 4.99 ms: 1.02x slower                                                    |
| create_gc_cycles           | 2.45 ms                                                | 2.50 ms: 1.02x slower                                                    |
| regex_dna                  | 220 ms                                                 | 225 ms: 1.02x slower                                                     |
| raytrace                   | 262 ms                                                 | 267 ms: 1.02x slower                                                     |
| connected_components       | 447 ms                                                 | 457 ms: 1.02x slower                                                     |
| chaos                      | 58.0 ms                                                | 59.5 ms: 1.02x slower                                                    |
| sympy_expand               | 456 ms                                                 | 469 ms: 1.03x slower                                                     |
| mako                       | 10.7 ms                                                | 11.0 ms: 1.03x slower                                                    |
| scimark_lu                 | 114 ms                                                 | 118 ms: 1.03x slower                                                     |
| python_startup             | 12.7 ms                                                | 13.1 ms: 1.03x slower                                                    |
| docutils                   | 2.58 sec                                               | 2.68 sec: 1.04x slower                                                   |
| crypto_pyaes               | 74.7 ms                                                | 77.7 ms: 1.04x slower                                                    |
| typing_runtime_protocols   | 160 us                                                 | 169 us: 1.05x slower                                                     |
| coroutines                 | 22.2 ms                                                | 23.5 ms: 1.06x slower                                                    |
| pprint_safe_repr           | 727 ms                                                 | 770 ms: 1.06x slower                                                     |
| pprint_pformat             | 1.48 sec                                               | 1.57 sec: 1.06x slower                                                   |
| pickle_pure_python         | 302 us                                                 | 322 us: 1.07x slower                                                     |
| nqueens                    | 80.9 ms                                                | 86.4 ms: 1.07x slower                                                    |
| fannkuch                   | 394 ms                                                 | 423 ms: 1.07x slower                                                     |
| bench_thread_pool          | 818 us                                                 | 882 us: 1.08x slower                                                     |
| json_loads                 | 27.2 us                                                | 29.7 us: 1.10x slower                                                    |
| hexiom                     | 6.08 ms                                                | 6.69 ms: 1.10x slower                                                    |
| json_dumps                 | 10.1 ms                                                | 11.4 ms: 1.12x slower                                                    |
| many_optionals             | 857 us                                                 | 965 us: 1.13x slower                                                     |
| comprehensions             | 16.5 us                                                | 18.7 us: 1.14x slower                                                    |
| python_startup_no_site     | 7.00 ms                                                | 8.19 ms: 1.17x slower                                                    |
| subparsers                 | 15.5 ms                                                | 20.9 ms: 1.36x slower                                                    |
| bench_mp_pool              | 24.0 ms                                                | 82.8 ms: 3.45x slower                                                    |
| Geometric mean             | (ref)                                                  | 1.03x faster                                                             |

Benchmark hidden because not significant (13): k_core, sympy_str, logging_simple, html5lib, sphinx, json, sqlalchemy_imperative, genshi_xml, asyncio_websockets, unpickle_pure_python, nbody, logging_format, meteor_contest
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250328-3.14.0a6+-2ba5562-JIT/bm-20250328-linux-x86_64-brandtbucher-jit_unknown_syms-3.14.0a6+-2ba5562.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.044x faster

# HPT report

- Reliability score: 98.71% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.04x
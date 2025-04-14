# Results vs. 3.13.0

- fork: python
- ref: 0cd4befb02df07c0b320
- machine: linux-x86_64
- commit hash: 0cd4bef
- commit date: 2025-03-31
- overall geometric mean: 1.054x faster
- HPT reliability: 99.31%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.05x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250331-linux-x86_64-python-0cd4befb02df07c0b320-3.14.0a6+-0cd4bef |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 262 ms: 1.01x faster                                                   |
| docutils       | 2.58 sec                                               | 2.69 sec: 1.04x slower                                                 |
| Geometric mean | (ref)                                                  | 1.01x slower                                                           |

Benchmark hidden because not significant (2): html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250331-linux-x86_64-python-0cd4befb02df07c0b320-3.14.0a6+-0cd4bef |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 317 ms: 1.46x faster                                                   |
| async_tree_io_tg           | 861 ms                                                 | 613 ms: 1.40x faster                                                   |
| async_tree_memoization     | 437 ms                                                 | 312 ms: 1.40x faster                                                   |
| async_tree_io              | 838 ms                                                 | 613 ms: 1.37x faster                                                   |
| async_tree_none            | 350 ms                                                 | 260 ms: 1.35x faster                                                   |
| async_tree_none_tg         | 319 ms                                                 | 253 ms: 1.26x faster                                                   |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 495 ms: 1.16x faster                                                   |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 483 ms: 1.13x faster                                                   |
| async_generators           | 433 ms                                                 | 416 ms: 1.04x faster                                                   |
| coroutines                 | 22.2 ms                                                | 23.4 ms: 1.05x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.22x faster                                                           |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250331-linux-x86_64-python-0cd4befb02df07c0b320-3.14.0a6+-0cd4bef |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 63.9 ms: 1.23x faster                                                  |
| nbody          | 87.7 ms                                                | 85.6 ms: 1.02x faster                                                  |
| pidigits       | 186 ms                                                 | 186 ms: 1.00x faster                                                   |
| Geometric mean | (ref)                                                  | 1.08x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250331-linux-x86_64-python-0cd4befb02df07c0b320-3.14.0a6+-0cd4bef |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_v8       | 26.9 ms                                                | 23.0 ms: 1.17x faster                                                  |
| regex_effbot   | 3.77 ms                                                | 3.37 ms: 1.12x faster                                                  |
| regex_compile  | 132 ms                                                 | 127 ms: 1.04x faster                                                   |
| regex_dna      | 220 ms                                                 | 218 ms: 1.01x faster                                                   |
| Geometric mean | (ref)                                                  | 1.08x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250331-linux-x86_64-python-0cd4befb02df07c0b320-3.14.0a6+-0cd4bef |
|---------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| tomli_loads         | 2.12 sec                                               | 1.85 sec: 1.15x faster                                                 |
| xml_etree_parse     | 154 ms                                                 | 141 ms: 1.10x faster                                                   |
| xml_etree_generate  | 86.8 ms                                                | 79.8 ms: 1.09x faster                                                  |
| xml_etree_process   | 60.5 ms                                                | 56.2 ms: 1.08x faster                                                  |
| xml_etree_iterparse | 101 ms                                                 | 97.4 ms: 1.04x faster                                                  |
| pickle_pure_python  | 302 us                                                 | 323 us: 1.07x slower                                                   |
| json_loads          | 27.2 us                                                | 29.7 us: 1.09x slower                                                  |
| json_dumps          | 10.1 ms                                                | 11.5 ms: 1.14x slower                                                  |
| Geometric mean      | (ref)                                                  | 1.02x faster                                                           |

Benchmark hidden because not significant (1): unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250331-linux-x86_64-python-0cd4befb02df07c0b320-3.14.0a6+-0cd4bef |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 12.7 ms                                                | 13.2 ms: 1.04x slower                                                  |
| python_startup_no_site | 7.00 ms                                                | 8.22 ms: 1.17x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.10x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250331-linux-x86_64-python-0cd4befb02df07c0b320-3.14.0a6+-0cd4bef |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_text     | 22.6 ms                                                | 21.1 ms: 1.07x faster                                                  |
| genshi_xml      | 50.5 ms                                                | 50.1 ms: 1.01x faster                                                  |
| django_template | 31.7 ms                                                | 32.3 ms: 1.02x slower                                                  |
| mako            | 10.7 ms                                                | 11.0 ms: 1.03x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.01x faster                                                           |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250331-linux-x86_64-python-0cd4befb02df07c0b320-3.14.0a6+-0cd4bef |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mdp                        | 2.54 sec                                               | 1.25 sec: 2.03x faster                                                 |
| async_tree_memoization_tg  | 463 ms                                                 | 317 ms: 1.46x faster                                                   |
| async_tree_io_tg           | 861 ms                                                 | 613 ms: 1.40x faster                                                   |
| async_tree_memoization     | 437 ms                                                 | 312 ms: 1.40x faster                                                   |
| deepcopy                   | 354 us                                                 | 255 us: 1.39x faster                                                   |
| async_tree_io              | 838 ms                                                 | 613 ms: 1.37x faster                                                   |
| async_tree_none            | 350 ms                                                 | 260 ms: 1.35x faster                                                   |
| richards                   | 47.5 ms                                                | 35.5 ms: 1.34x faster                                                  |
| richards_super             | 53.7 ms                                                | 40.6 ms: 1.32x faster                                                  |
| deepcopy_memo              | 38.4 us                                                | 29.8 us: 1.29x faster                                                  |
| async_tree_none_tg         | 319 ms                                                 | 253 ms: 1.26x faster                                                   |
| float                      | 78.7 ms                                                | 63.9 ms: 1.23x faster                                                  |
| deepcopy_reduce            | 3.24 us                                                | 2.67 us: 1.22x faster                                                  |
| spectral_norm              | 113 ms                                                 | 94.0 ms: 1.20x faster                                                  |
| scimark_fft                | 367 ms                                                 | 307 ms: 1.19x faster                                                   |
| regex_v8                   | 26.9 ms                                                | 23.0 ms: 1.17x faster                                                  |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 495 ms: 1.16x faster                                                   |
| tomli_loads                | 2.12 sec                                               | 1.85 sec: 1.15x faster                                                 |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 483 ms: 1.13x faster                                                   |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.49 ms: 1.12x faster                                                  |
| regex_effbot               | 3.77 ms                                                | 3.37 ms: 1.12x faster                                                  |
| go                         | 141 ms                                                 | 126 ms: 1.11x faster                                                   |
| pylint                     | 312 ms                                                 | 281 ms: 1.11x faster                                                   |
| xml_etree_parse            | 154 ms                                                 | 141 ms: 1.10x faster                                                   |
| pyflate                    | 470 ms                                                 | 429 ms: 1.09x faster                                                   |
| xml_etree_generate         | 86.8 ms                                                | 79.8 ms: 1.09x faster                                                  |
| xml_etree_process          | 60.5 ms                                                | 56.2 ms: 1.08x faster                                                  |
| genshi_text                | 22.6 ms                                                | 21.1 ms: 1.07x faster                                                  |
| dulwich_log                | 64.6 ms                                                | 60.5 ms: 1.07x faster                                                  |
| sqlite_synth               | 2.90 us                                                | 2.72 us: 1.07x faster                                                  |
| telco                      | 8.40 ms                                                | 7.89 ms: 1.06x faster                                                  |
| deltablue                  | 3.19 ms                                                | 3.03 ms: 1.05x faster                                                  |
| async_generators           | 433 ms                                                 | 416 ms: 1.04x faster                                                   |
| pathlib                    | 17.4 ms                                                | 16.7 ms: 1.04x faster                                                  |
| xml_etree_iterparse        | 101 ms                                                 | 97.4 ms: 1.04x faster                                                  |
| regex_compile              | 132 ms                                                 | 127 ms: 1.04x faster                                                   |
| logging_silent             | 101 ns                                                 | 97.8 ns: 1.03x faster                                                  |
| bpe_tokeniser              | 4.69 sec                                               | 4.54 sec: 1.03x faster                                                 |
| generators                 | 28.8 ms                                                | 28.1 ms: 1.02x faster                                                  |
| nbody                      | 87.7 ms                                                | 85.6 ms: 1.02x faster                                                  |
| k_core                     | 2.37 sec                                               | 2.32 sec: 1.02x faster                                                 |
| 2to3                       | 266 ms                                                 | 262 ms: 1.01x faster                                                   |
| sympy_integrate            | 19.8 ms                                                | 19.6 ms: 1.01x faster                                                  |
| scimark_sor                | 122 ms                                                 | 121 ms: 1.01x faster                                                   |
| pycparser                  | 1.20 sec                                               | 1.19 sec: 1.01x faster                                                 |
| meteor_contest             | 108 ms                                                 | 107 ms: 1.01x faster                                                   |
| regex_dna                  | 220 ms                                                 | 218 ms: 1.01x faster                                                   |
| genshi_xml                 | 50.5 ms                                                | 50.1 ms: 1.01x faster                                                  |
| pidigits                   | 186 ms                                                 | 186 ms: 1.00x faster                                                   |
| crypto_pyaes               | 74.7 ms                                                | 74.5 ms: 1.00x faster                                                  |
| logging_format             | 6.23 us                                                | 6.28 us: 1.01x slower                                                  |
| connected_components       | 447 ms                                                 | 453 ms: 1.01x slower                                                   |
| shortest_path              | 487 ms                                                 | 493 ms: 1.01x slower                                                   |
| scimark_monte_carlo        | 66.8 ms                                                | 67.8 ms: 1.02x slower                                                  |
| sqlalchemy_imperative      | 16.9 ms                                                | 17.2 ms: 1.02x slower                                                  |
| scimark_lu                 | 114 ms                                                 | 116 ms: 1.02x slower                                                   |
| create_gc_cycles           | 2.45 ms                                                | 2.49 ms: 1.02x slower                                                  |
| raytrace                   | 262 ms                                                 | 267 ms: 1.02x slower                                                   |
| django_template            | 31.7 ms                                                | 32.3 ms: 1.02x slower                                                  |
| chaos                      | 58.0 ms                                                | 59.5 ms: 1.03x slower                                                  |
| nqueens                    | 80.9 ms                                                | 83.1 ms: 1.03x slower                                                  |
| coverage                   | 82.8 ms                                                | 85.4 ms: 1.03x slower                                                  |
| mako                       | 10.7 ms                                                | 11.0 ms: 1.03x slower                                                  |
| gc_traversal               | 4.90 ms                                                | 5.06 ms: 1.03x slower                                                  |
| fannkuch                   | 394 ms                                                 | 408 ms: 1.04x slower                                                   |
| docutils                   | 2.58 sec                                               | 2.69 sec: 1.04x slower                                                 |
| python_startup             | 12.7 ms                                                | 13.2 ms: 1.04x slower                                                  |
| sympy_expand               | 456 ms                                                 | 475 ms: 1.04x slower                                                   |
| coroutines                 | 22.2 ms                                                | 23.4 ms: 1.05x slower                                                  |
| typing_runtime_protocols   | 160 us                                                 | 170 us: 1.06x slower                                                   |
| pprint_pformat             | 1.48 sec                                               | 1.57 sec: 1.06x slower                                                 |
| pprint_safe_repr           | 727 ms                                                 | 773 ms: 1.06x slower                                                   |
| pickle_pure_python         | 302 us                                                 | 323 us: 1.07x slower                                                   |
| bench_thread_pool          | 818 us                                                 | 885 us: 1.08x slower                                                   |
| json_loads                 | 27.2 us                                                | 29.7 us: 1.09x slower                                                  |
| hexiom                     | 6.08 ms                                                | 6.81 ms: 1.12x slower                                                  |
| comprehensions             | 16.5 us                                                | 18.5 us: 1.12x slower                                                  |
| many_optionals             | 857 us                                                 | 971 us: 1.13x slower                                                   |
| json_dumps                 | 10.1 ms                                                | 11.5 ms: 1.14x slower                                                  |
| python_startup_no_site     | 7.00 ms                                                | 8.22 ms: 1.17x slower                                                  |
| subparsers                 | 15.5 ms                                                | 21.1 ms: 1.37x slower                                                  |
| bench_mp_pool              | 24.0 ms                                                | 83.1 ms: 3.47x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.04x faster                                                           |

Benchmark hidden because not significant (9): json, unpickle_pure_python, sqlalchemy_declarative, logging_simple, html5lib, asyncio_websockets, sphinx, sympy_sum, sympy_str
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
Ignored benchmarks (4) of results/bm-20250331-3.14.0a6+-0cd4bef-JIT/bm-20250331-linux-x86_64-python-0cd4befb02df07c0b320-3.14.0a6+-0cd4bef.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.054x faster

# HPT report

- Reliability score: 99.31% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.05x
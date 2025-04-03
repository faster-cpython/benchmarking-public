# Results vs. 3.13.0

- fork: python
- ref: 0cd4befb02df07c0b320
- machine: linux-x86_64
- commit hash: 0cd4bef
- commit date: 2025-03-31
- overall geometric mean: 1.050x faster
- HPT reliability: 99.99%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250331-linux-x86_64-python-0cd4befb02df07c0b320-3.14.0a6+-0cd4bef |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 254 ms: 1.05x faster                                                   |
| docutils       | 2.58 sec                                               | 2.60 sec: 1.01x slower                                                 |
| html5lib       | 63.4 ms                                                | 63.0 ms: 1.01x faster                                                  |
| sphinx         | 1.03 sec                                               | 1.01 sec: 1.02x faster                                                 |
| Geometric mean | (ref)                                                  | 1.02x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250331-linux-x86_64-python-0cd4befb02df07c0b320-3.14.0a6+-0cd4bef |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 316 ms: 1.47x faster                                                   |
| async_tree_io_tg           | 861 ms                                                 | 612 ms: 1.41x faster                                                   |
| async_tree_memoization     | 437 ms                                                 | 312 ms: 1.40x faster                                                   |
| async_tree_io              | 838 ms                                                 | 610 ms: 1.37x faster                                                   |
| async_tree_none            | 350 ms                                                 | 259 ms: 1.35x faster                                                   |
| async_tree_none_tg         | 319 ms                                                 | 249 ms: 1.28x faster                                                   |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 483 ms: 1.19x faster                                                   |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 474 ms: 1.15x faster                                                   |
| async_generators           | 433 ms                                                 | 389 ms: 1.12x faster                                                   |
| coroutines                 | 22.2 ms                                                | 23.4 ms: 1.05x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.23x faster                                                           |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250331-linux-x86_64-python-0cd4befb02df07c0b320-3.14.0a6+-0cd4bef |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 69.3 ms: 1.14x faster                                                  |
| pidigits       | 186 ms                                                 | 187 ms: 1.00x slower                                                   |
| nbody          | 87.7 ms                                                | 96.4 ms: 1.10x slower                                                  |
| Geometric mean | (ref)                                                  | 1.01x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250331-linux-x86_64-python-0cd4befb02df07c0b320-3.14.0a6+-0cd4bef |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_v8       | 26.9 ms                                                | 22.9 ms: 1.17x faster                                                  |
| regex_compile  | 132 ms                                                 | 127 ms: 1.04x faster                                                   |
| regex_dna      | 220 ms                                                 | 215 ms: 1.02x faster                                                   |
| Geometric mean | (ref)                                                  | 1.05x faster                                                           |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250331-linux-x86_64-python-0cd4befb02df07c0b320-3.14.0a6+-0cd4bef |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| xml_etree_parse      | 154 ms                                                 | 141 ms: 1.10x faster                                                   |
| tomli_loads          | 2.12 sec                                               | 1.95 sec: 1.08x faster                                                 |
| xml_etree_process    | 60.5 ms                                                | 58.9 ms: 1.03x faster                                                  |
| xml_etree_iterparse  | 101 ms                                                 | 99.1 ms: 1.02x faster                                                  |
| xml_etree_generate   | 86.8 ms                                                | 85.0 ms: 1.02x faster                                                  |
| unpickle_pure_python | 213 us                                                 | 219 us: 1.03x slower                                                   |
| pickle_pure_python   | 302 us                                                 | 321 us: 1.06x slower                                                   |
| json_loads           | 27.2 us                                                | 29.9 us: 1.10x slower                                                  |
| json_dumps           | 10.1 ms                                                | 11.5 ms: 1.13x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.01x slower                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250331-linux-x86_64-python-0cd4befb02df07c0b320-3.14.0a6+-0cd4bef |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 12.7 ms                                                | 13.1 ms: 1.03x slower                                                  |
| python_startup_no_site | 7.00 ms                                                | 8.16 ms: 1.17x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.10x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250331-linux-x86_64-python-0cd4befb02df07c0b320-3.14.0a6+-0cd4bef |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_text     | 22.6 ms                                                | 21.5 ms: 1.05x faster                                                  |
| genshi_xml      | 50.5 ms                                                | 49.6 ms: 1.02x faster                                                  |
| django_template | 31.7 ms                                                | 31.9 ms: 1.01x slower                                                  |
| mako            | 10.7 ms                                                | 11.4 ms: 1.07x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.00x slower                                                           |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250331-linux-x86_64-python-0cd4befb02df07c0b320-3.14.0a6+-0cd4bef |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mdp                        | 2.54 sec                                               | 1.24 sec: 2.06x faster                                                 |
| async_tree_memoization_tg  | 463 ms                                                 | 316 ms: 1.47x faster                                                   |
| async_tree_io_tg           | 861 ms                                                 | 612 ms: 1.41x faster                                                   |
| async_tree_memoization     | 437 ms                                                 | 312 ms: 1.40x faster                                                   |
| async_tree_io              | 838 ms                                                 | 610 ms: 1.37x faster                                                   |
| deepcopy                   | 354 us                                                 | 258 us: 1.37x faster                                                   |
| async_tree_none            | 350 ms                                                 | 259 ms: 1.35x faster                                                   |
| async_tree_none_tg         | 319 ms                                                 | 249 ms: 1.28x faster                                                   |
| deepcopy_memo              | 38.4 us                                                | 30.0 us: 1.28x faster                                                  |
| go                         | 141 ms                                                 | 115 ms: 1.23x faster                                                   |
| deepcopy_reduce            | 3.24 us                                                | 2.70 us: 1.20x faster                                                  |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 483 ms: 1.19x faster                                                   |
| spectral_norm              | 113 ms                                                 | 96.3 ms: 1.18x faster                                                  |
| regex_v8                   | 26.9 ms                                                | 22.9 ms: 1.17x faster                                                  |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 474 ms: 1.15x faster                                                   |
| float                      | 78.7 ms                                                | 69.3 ms: 1.14x faster                                                  |
| pylint                     | 312 ms                                                 | 276 ms: 1.13x faster                                                   |
| async_generators           | 433 ms                                                 | 389 ms: 1.12x faster                                                   |
| dulwich_log                | 64.6 ms                                                | 58.4 ms: 1.11x faster                                                  |
| xml_etree_parse            | 154 ms                                                 | 141 ms: 1.10x faster                                                   |
| tomli_loads                | 2.12 sec                                               | 1.95 sec: 1.08x faster                                                 |
| telco                      | 8.40 ms                                                | 7.86 ms: 1.07x faster                                                  |
| pathlib                    | 17.4 ms                                                | 16.3 ms: 1.07x faster                                                  |
| richards_super             | 53.7 ms                                                | 50.6 ms: 1.06x faster                                                  |
| richards                   | 47.5 ms                                                | 44.9 ms: 1.06x faster                                                  |
| genshi_text                | 22.6 ms                                                | 21.5 ms: 1.05x faster                                                  |
| 2to3                       | 266 ms                                                 | 254 ms: 1.05x faster                                                   |
| pyflate                    | 470 ms                                                 | 449 ms: 1.05x faster                                                   |
| k_core                     | 2.37 sec                                               | 2.27 sec: 1.04x faster                                                 |
| regex_compile              | 132 ms                                                 | 127 ms: 1.04x faster                                                   |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.86 ms: 1.03x faster                                                  |
| sqlite_synth               | 2.90 us                                                | 2.81 us: 1.03x faster                                                  |
| sympy_integrate            | 19.8 ms                                                | 19.2 ms: 1.03x faster                                                  |
| scimark_fft                | 367 ms                                                 | 355 ms: 1.03x faster                                                   |
| scimark_sor                | 122 ms                                                 | 119 ms: 1.03x faster                                                   |
| meteor_contest             | 108 ms                                                 | 105 ms: 1.03x faster                                                   |
| xml_etree_process          | 60.5 ms                                                | 58.9 ms: 1.03x faster                                                  |
| pycparser                  | 1.20 sec                                               | 1.17 sec: 1.03x faster                                                 |
| bpe_tokeniser              | 4.69 sec                                               | 4.58 sec: 1.02x faster                                                 |
| xml_etree_iterparse        | 101 ms                                                 | 99.1 ms: 1.02x faster                                                  |
| xml_etree_generate         | 86.8 ms                                                | 85.0 ms: 1.02x faster                                                  |
| logging_silent             | 101 ns                                                 | 98.9 ns: 1.02x faster                                                  |
| regex_dna                  | 220 ms                                                 | 215 ms: 1.02x faster                                                   |
| sqlalchemy_declarative     | 133 ms                                                 | 130 ms: 1.02x faster                                                   |
| sympy_sum                  | 150 ms                                                 | 148 ms: 1.02x faster                                                   |
| genshi_xml                 | 50.5 ms                                                | 49.6 ms: 1.02x faster                                                  |
| sphinx                     | 1.03 sec                                               | 1.01 sec: 1.02x faster                                                 |
| sympy_str                  | 273 ms                                                 | 268 ms: 1.02x faster                                                   |
| sqlalchemy_imperative      | 16.9 ms                                                | 16.6 ms: 1.02x faster                                                  |
| deltablue                  | 3.19 ms                                                | 3.15 ms: 1.01x faster                                                  |
| crypto_pyaes               | 74.7 ms                                                | 73.8 ms: 1.01x faster                                                  |
| generators                 | 28.8 ms                                                | 28.6 ms: 1.01x faster                                                  |
| html5lib                   | 63.4 ms                                                | 63.0 ms: 1.01x faster                                                  |
| pidigits                   | 186 ms                                                 | 187 ms: 1.00x slower                                                   |
| scimark_lu                 | 114 ms                                                 | 115 ms: 1.01x slower                                                   |
| docutils                   | 2.58 sec                                               | 2.60 sec: 1.01x slower                                                 |
| django_template            | 31.7 ms                                                | 31.9 ms: 1.01x slower                                                  |
| comprehensions             | 16.5 us                                                | 16.7 us: 1.01x slower                                                  |
| sympy_expand               | 456 ms                                                 | 461 ms: 1.01x slower                                                   |
| shortest_path              | 487 ms                                                 | 493 ms: 1.01x slower                                                   |
| raytrace                   | 262 ms                                                 | 266 ms: 1.02x slower                                                   |
| scimark_monte_carlo        | 66.8 ms                                                | 67.9 ms: 1.02x slower                                                  |
| coverage                   | 82.8 ms                                                | 84.3 ms: 1.02x slower                                                  |
| nqueens                    | 80.9 ms                                                | 82.6 ms: 1.02x slower                                                  |
| create_gc_cycles           | 2.45 ms                                                | 2.50 ms: 1.02x slower                                                  |
| gc_traversal               | 4.90 ms                                                | 5.02 ms: 1.02x slower                                                  |
| unpickle_pure_python       | 213 us                                                 | 219 us: 1.03x slower                                                   |
| hexiom                     | 6.08 ms                                                | 6.25 ms: 1.03x slower                                                  |
| python_startup             | 12.7 ms                                                | 13.1 ms: 1.03x slower                                                  |
| coroutines                 | 22.2 ms                                                | 23.4 ms: 1.05x slower                                                  |
| pickle_pure_python         | 302 us                                                 | 321 us: 1.06x slower                                                   |
| bench_thread_pool          | 818 us                                                 | 872 us: 1.07x slower                                                   |
| mako                       | 10.7 ms                                                | 11.4 ms: 1.07x slower                                                  |
| fannkuch                   | 394 ms                                                 | 426 ms: 1.08x slower                                                   |
| nbody                      | 87.7 ms                                                | 96.4 ms: 1.10x slower                                                  |
| json_loads                 | 27.2 us                                                | 29.9 us: 1.10x slower                                                  |
| many_optionals             | 857 us                                                 | 947 us: 1.11x slower                                                   |
| json_dumps                 | 10.1 ms                                                | 11.5 ms: 1.13x slower                                                  |
| python_startup_no_site     | 7.00 ms                                                | 8.16 ms: 1.17x slower                                                  |
| subparsers                 | 15.5 ms                                                | 20.8 ms: 1.35x slower                                                  |
| bench_mp_pool              | 24.0 ms                                                | 82.5 ms: 3.44x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.03x faster                                                           |

Benchmark hidden because not significant (10): logging_format, pprint_pformat, pprint_safe_repr, asyncio_websockets, connected_components, chaos, logging_simple, json, typing_runtime_protocols, regex_effbot
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
Ignored benchmarks (4) of results/bm-20250331-3.14.0a6+-0cd4bef/bm-20250331-linux-x86_64-python-0cd4befb02df07c0b320-3.14.0a6+-0cd4bef.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.050x faster

# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.04x
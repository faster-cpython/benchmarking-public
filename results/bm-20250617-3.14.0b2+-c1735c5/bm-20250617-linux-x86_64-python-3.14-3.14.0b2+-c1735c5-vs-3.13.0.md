# Results vs. 3.13.0

- fork: python
- ref: 3.14
- machine: linux-x86_64
- commit hash: c1735c5
- commit date: 2025-06-17
- overall geometric mean: 1.044x faster
- HPT reliability: 99.73%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.06x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250617-linux-x86_64-python-3.14-3.14.0b2+-c1735c5 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 257 ms: 1.03x faster                                   |
| docutils       | 2.58 sec                                               | 2.60 sec: 1.00x slower                                 |
| html5lib       | 63.4 ms                                                | 61.6 ms: 1.03x faster                                  |
| sphinx         | 1.03 sec                                               | 1.01 sec: 1.02x faster                                 |
| Geometric mean | (ref)                                                  | 1.02x faster                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250617-linux-x86_64-python-3.14-3.14.0b2+-c1735c5 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 310 ms: 1.49x faster                                   |
| async_tree_memoization     | 437 ms                                                 | 308 ms: 1.42x faster                                   |
| async_tree_io              | 838 ms                                                 | 592 ms: 1.42x faster                                   |
| async_tree_io_tg           | 861 ms                                                 | 608 ms: 1.42x faster                                   |
| async_tree_none            | 350 ms                                                 | 261 ms: 1.34x faster                                   |
| async_tree_none_tg         | 319 ms                                                 | 245 ms: 1.30x faster                                   |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 487 ms: 1.18x faster                                   |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 481 ms: 1.13x faster                                   |
| async_generators           | 433 ms                                                 | 408 ms: 1.06x faster                                   |
| asyncio_websockets         | 551 ms                                                 | 553 ms: 1.00x slower                                   |
| coroutines                 | 22.2 ms                                                | 24.8 ms: 1.11x slower                                  |
| Geometric mean             | (ref)                                                  | 1.23x faster                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250617-linux-x86_64-python-3.14-3.14.0b2+-c1735c5 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| float          | 78.7 ms                                                | 70.1 ms: 1.12x faster                                  |
| pidigits       | 186 ms                                                 | 187 ms: 1.00x slower                                   |
| nbody          | 87.7 ms                                                | 100 ms: 1.14x slower                                   |
| Geometric mean | (ref)                                                  | 1.01x slower                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250617-linux-x86_64-python-3.14-3.14.0b2+-c1735c5 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                | 3.21 ms: 1.17x faster                                  |
| regex_v8       | 26.9 ms                                                | 23.3 ms: 1.15x faster                                  |
| regex_dna      | 220 ms                                                 | 207 ms: 1.06x faster                                   |
| regex_compile  | 132 ms                                                 | 127 ms: 1.04x faster                                   |
| Geometric mean | (ref)                                                  | 1.11x faster                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250617-linux-x86_64-python-3.14-3.14.0b2+-c1735c5 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| xml_etree_parse      | 154 ms                                                 | 144 ms: 1.07x faster                                   |
| tomli_loads          | 2.12 sec                                               | 2.01 sec: 1.05x faster                                 |
| xml_etree_iterparse  | 101 ms                                                 | 99.0 ms: 1.02x faster                                  |
| xml_etree_generate   | 86.8 ms                                                | 85.4 ms: 1.02x faster                                  |
| xml_etree_process    | 60.5 ms                                                | 60.2 ms: 1.00x faster                                  |
| unpickle_pure_python | 213 us                                                 | 219 us: 1.03x slower                                   |
| pickle_pure_python   | 302 us                                                 | 316 us: 1.05x slower                                   |
| json_loads           | 27.2 us                                                | 28.6 us: 1.05x slower                                  |
| json_dumps           | 10.1 ms                                                | 10.9 ms: 1.08x slower                                  |
| Geometric mean       | (ref)                                                  | 1.00x slower                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250617-linux-x86_64-python-3.14-3.14.0b2+-c1735c5 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup_no_site | 7.00 ms                                                | 6.92 ms: 1.01x faster                                  |
| python_startup         | 12.7 ms                                                | 13.1 ms: 1.04x slower                                  |
| Geometric mean         | (ref)                                                  | 1.01x slower                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250617-linux-x86_64-python-3.14-3.14.0b2+-c1735c5 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| genshi_text     | 22.6 ms                                                | 21.7 ms: 1.04x faster                                  |
| genshi_xml      | 50.5 ms                                                | 49.1 ms: 1.03x faster                                  |
| django_template | 31.7 ms                                                | 32.1 ms: 1.01x slower                                  |
| mako            | 10.7 ms                                                | 11.5 ms: 1.08x slower                                  |
| Geometric mean  | (ref)                                                  | 1.00x slower                                           |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250617-linux-x86_64-python-3.14-3.14.0b2+-c1735c5 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| mdp                        | 2.54 sec                                               | 1.23 sec: 2.06x faster                                 |
| async_tree_memoization_tg  | 463 ms                                                 | 310 ms: 1.49x faster                                   |
| async_tree_memoization     | 437 ms                                                 | 308 ms: 1.42x faster                                   |
| async_tree_io              | 838 ms                                                 | 592 ms: 1.42x faster                                   |
| async_tree_io_tg           | 861 ms                                                 | 608 ms: 1.42x faster                                   |
| deepcopy                   | 354 us                                                 | 259 us: 1.37x faster                                   |
| async_tree_none            | 350 ms                                                 | 261 ms: 1.34x faster                                   |
| deepcopy_memo              | 38.4 us                                                | 29.5 us: 1.30x faster                                  |
| async_tree_none_tg         | 319 ms                                                 | 245 ms: 1.30x faster                                   |
| go                         | 141 ms                                                 | 112 ms: 1.25x faster                                   |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 487 ms: 1.18x faster                                   |
| regex_effbot               | 3.77 ms                                                | 3.21 ms: 1.17x faster                                  |
| deepcopy_reduce            | 3.24 us                                                | 2.78 us: 1.17x faster                                  |
| regex_v8                   | 26.9 ms                                                | 23.3 ms: 1.15x faster                                  |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 481 ms: 1.13x faster                                   |
| pylint                     | 312 ms                                                 | 278 ms: 1.12x faster                                   |
| float                      | 78.7 ms                                                | 70.1 ms: 1.12x faster                                  |
| richards                   | 47.5 ms                                                | 42.6 ms: 1.12x faster                                  |
| pyflate                    | 470 ms                                                 | 426 ms: 1.10x faster                                   |
| richards_super             | 53.7 ms                                                | 48.8 ms: 1.10x faster                                  |
| dulwich_log                | 64.6 ms                                                | 59.5 ms: 1.09x faster                                  |
| xml_etree_parse            | 154 ms                                                 | 144 ms: 1.07x faster                                   |
| async_generators           | 433 ms                                                 | 408 ms: 1.06x faster                                   |
| regex_dna                  | 220 ms                                                 | 207 ms: 1.06x faster                                   |
| tomli_loads                | 2.12 sec                                               | 2.01 sec: 1.05x faster                                 |
| telco                      | 8.40 ms                                                | 8.02 ms: 1.05x faster                                  |
| sympy_integrate            | 19.8 ms                                                | 18.9 ms: 1.05x faster                                  |
| bpe_tokeniser              | 4.69 sec                                               | 4.50 sec: 1.04x faster                                 |
| genshi_text                | 22.6 ms                                                | 21.7 ms: 1.04x faster                                  |
| regex_compile              | 132 ms                                                 | 127 ms: 1.04x faster                                   |
| pycparser                  | 1.20 sec                                               | 1.16 sec: 1.04x faster                                 |
| k_core                     | 2.37 sec                                               | 2.29 sec: 1.03x faster                                 |
| 2to3                       | 266 ms                                                 | 257 ms: 1.03x faster                                   |
| gc_traversal               | 4.90 ms                                                | 4.74 ms: 1.03x faster                                  |
| genshi_xml                 | 50.5 ms                                                | 49.1 ms: 1.03x faster                                  |
| html5lib                   | 63.4 ms                                                | 61.6 ms: 1.03x faster                                  |
| spectral_norm              | 113 ms                                                 | 110 ms: 1.03x faster                                   |
| meteor_contest             | 108 ms                                                 | 106 ms: 1.03x faster                                   |
| sympy_sum                  | 150 ms                                                 | 147 ms: 1.02x faster                                   |
| json                       | 5.32 ms                                                | 5.20 ms: 1.02x faster                                  |
| xml_etree_iterparse        | 101 ms                                                 | 99.0 ms: 1.02x faster                                  |
| sympy_str                  | 273 ms                                                 | 267 ms: 1.02x faster                                   |
| sphinx                     | 1.03 sec                                               | 1.01 sec: 1.02x faster                                 |
| xml_etree_generate         | 86.8 ms                                                | 85.4 ms: 1.02x faster                                  |
| python_startup_no_site     | 7.00 ms                                                | 6.92 ms: 1.01x faster                                  |
| sqlite_synth               | 2.90 us                                                | 2.87 us: 1.01x faster                                  |
| scimark_sor                | 122 ms                                                 | 121 ms: 1.01x faster                                   |
| xml_etree_process          | 60.5 ms                                                | 60.2 ms: 1.00x faster                                  |
| docutils                   | 2.58 sec                                               | 2.60 sec: 1.00x slower                                 |
| asyncio_websockets         | 551 ms                                                 | 553 ms: 1.00x slower                                   |
| pidigits                   | 186 ms                                                 | 187 ms: 1.00x slower                                   |
| sqlalchemy_declarative     | 133 ms                                                 | 134 ms: 1.01x slower                                   |
| hexiom                     | 6.08 ms                                                | 6.12 ms: 1.01x slower                                  |
| shortest_path              | 487 ms                                                 | 492 ms: 1.01x slower                                   |
| django_template            | 31.7 ms                                                | 32.1 ms: 1.01x slower                                  |
| scimark_monte_carlo        | 66.8 ms                                                | 67.7 ms: 1.01x slower                                  |
| scimark_fft                | 367 ms                                                 | 373 ms: 1.02x slower                                   |
| scimark_lu                 | 114 ms                                                 | 117 ms: 1.02x slower                                   |
| pprint_safe_repr           | 727 ms                                                 | 743 ms: 1.02x slower                                   |
| pprint_pformat             | 1.48 sec                                               | 1.52 sec: 1.03x slower                                 |
| unpickle_pure_python       | 213 us                                                 | 219 us: 1.03x slower                                   |
| raytrace                   | 262 ms                                                 | 270 ms: 1.03x slower                                   |
| connected_components       | 447 ms                                                 | 462 ms: 1.03x slower                                   |
| python_startup             | 12.7 ms                                                | 13.1 ms: 1.04x slower                                  |
| chaos                      | 58.0 ms                                                | 60.1 ms: 1.04x slower                                  |
| sqlalchemy_imperative      | 16.9 ms                                                | 17.6 ms: 1.04x slower                                  |
| typing_runtime_protocols   | 160 us                                                 | 167 us: 1.05x slower                                   |
| pickle_pure_python         | 302 us                                                 | 316 us: 1.05x slower                                   |
| deltablue                  | 3.19 ms                                                | 3.35 ms: 1.05x slower                                  |
| create_gc_cycles           | 2.45 ms                                                | 2.58 ms: 1.05x slower                                  |
| json_loads                 | 27.2 us                                                | 28.6 us: 1.05x slower                                  |
| coverage                   | 82.8 ms                                                | 87.1 ms: 1.05x slower                                  |
| fannkuch                   | 394 ms                                                 | 416 ms: 1.06x slower                                   |
| json_dumps                 | 10.1 ms                                                | 10.9 ms: 1.08x slower                                  |
| mako                       | 10.7 ms                                                | 11.5 ms: 1.08x slower                                  |
| logging_simple             | 5.65 us                                                | 6.13 us: 1.08x slower                                  |
| logging_format             | 6.23 us                                                | 6.77 us: 1.09x slower                                  |
| generators                 | 28.8 ms                                                | 31.4 ms: 1.09x slower                                  |
| coroutines                 | 22.2 ms                                                | 24.8 ms: 1.11x slower                                  |
| many_optionals             | 857 us                                                 | 961 us: 1.12x slower                                   |
| nbody                      | 87.7 ms                                                | 100 ms: 1.14x slower                                   |
| subparsers                 | 15.5 ms                                                | 23.5 ms: 1.52x slower                                  |
| logging_silent             | 101 ns                                                 | 471 ns: 4.66x slower                                   |
| Geometric mean             | (ref)                                                  | 1.03x faster                                           |

Benchmark hidden because not significant (6): pathlib, crypto_pyaes, scimark_sparse_mat_mult, sympy_expand, nqueens, comprehensions
Ignored benchmarks (12) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
Ignored benchmarks (4) of results/bm-20250617-3.14.0b2+-c1735c5/bm-20250617-linux-x86_64-python-3.14-3.14.0b2+-c1735c5.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.044x faster

# HPT report

- Reliability score: 99.73% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.06x
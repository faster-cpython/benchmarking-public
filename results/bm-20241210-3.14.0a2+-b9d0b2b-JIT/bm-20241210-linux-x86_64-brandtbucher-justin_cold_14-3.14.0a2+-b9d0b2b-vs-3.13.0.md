# Results vs. 3.13.0

- fork: brandtbucher
- ref: justin_cold_14
- machine: linux-x86_64
- commit hash: b9d0b2b
- commit date: 2024-12-10
- overall geometric mean: 1.029x faster
- HPT reliability: 98.77%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241210-linux-x86_64-brandtbucher-justin_cold_14-3.14.0a2+-b9d0b2b |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 259 ms: 1.03x faster                                                   |
| docutils       | 2.58 sec                                               | 2.65 sec: 1.02x slower                                                 |
| html5lib       | 63.4 ms                                                | 64.9 ms: 1.02x slower                                                  |
| Geometric mean | (ref)                                                  | 1.01x slower                                                           |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241210-linux-x86_64-brandtbucher-justin_cold_14-3.14.0a2+-b9d0b2b |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 317 ms: 1.46x faster                                                   |
| async_tree_io_tg           | 861 ms                                                 | 629 ms: 1.37x faster                                                   |
| async_tree_io              | 838 ms                                                 | 625 ms: 1.34x faster                                                   |
| async_tree_none            | 350 ms                                                 | 271 ms: 1.29x faster                                                   |
| async_tree_memoization     | 437 ms                                                 | 342 ms: 1.28x faster                                                   |
| async_tree_none_tg         | 319 ms                                                 | 254 ms: 1.25x faster                                                   |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 497 ms: 1.15x faster                                                   |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 483 ms: 1.13x faster                                                   |
| asyncio_websockets         | 551 ms                                                 | 553 ms: 1.00x slower                                                   |
| coroutines                 | 22.2 ms                                                | 23.2 ms: 1.05x slower                                                  |
| async_generators           | 433 ms                                                 | 454 ms: 1.05x slower                                                   |
| Geometric mean             | (ref)                                                  | 1.19x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241210-linux-x86_64-brandtbucher-justin_cold_14-3.14.0a2+-b9d0b2b |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 87.7 ms                                                | 81.0 ms: 1.08x faster                                                  |
| float          | 78.7 ms                                                | 76.1 ms: 1.03x faster                                                  |
| pidigits       | 186 ms                                                 | 187 ms: 1.00x slower                                                   |
| Geometric mean | (ref)                                                  | 1.04x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241210-linux-x86_64-brandtbucher-justin_cold_14-3.14.0a2+-b9d0b2b |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                | 3.26 ms: 1.16x faster                                                  |
| regex_v8       | 26.9 ms                                                | 25.1 ms: 1.07x faster                                                  |
| regex_dna      | 220 ms                                                 | 215 ms: 1.02x faster                                                   |
| regex_compile  | 132 ms                                                 | 130 ms: 1.01x faster                                                   |
| Geometric mean | (ref)                                                  | 1.06x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241210-linux-x86_64-brandtbucher-justin_cold_14-3.14.0a2+-b9d0b2b |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| xml_etree_parse      | 154 ms                                                 | 137 ms: 1.12x faster                                                   |
| tomli_loads          | 2.12 sec                                               | 1.93 sec: 1.09x faster                                                 |
| unpickle_pure_python | 213 us                                                 | 196 us: 1.09x faster                                                   |
| xml_etree_generate   | 86.8 ms                                                | 80.2 ms: 1.08x faster                                                  |
| xml_etree_iterparse  | 101 ms                                                 | 95.4 ms: 1.06x faster                                                  |
| xml_etree_process    | 60.5 ms                                                | 57.1 ms: 1.06x faster                                                  |
| json_loads           | 27.2 us                                                | 26.1 us: 1.04x faster                                                  |
| pickle_pure_python   | 302 us                                                 | 322 us: 1.06x slower                                                   |
| json_dumps           | 10.1 ms                                                | 11.0 ms: 1.09x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241210-linux-x86_64-brandtbucher-justin_cold_14-3.14.0a2+-b9d0b2b |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 7.00 ms                                                | 7.06 ms: 1.01x slower                                                  |
| python_startup         | 12.7 ms                                                | 12.8 ms: 1.01x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241210-linux-x86_64-brandtbucher-justin_cold_14-3.14.0a2+-b9d0b2b |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 10.7 ms                                                | 10.2 ms: 1.05x faster                                                  |
| django_template | 31.7 ms                                                | 34.4 ms: 1.09x slower                                                  |
| genshi_text     | 22.6 ms                                                | 25.0 ms: 1.11x slower                                                  |
| genshi_xml      | 50.5 ms                                                | 58.8 ms: 1.17x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.08x slower                                                           |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241210-linux-x86_64-brandtbucher-justin_cold_14-3.14.0a2+-b9d0b2b |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 317 ms: 1.46x faster                                                   |
| async_tree_io_tg           | 861 ms                                                 | 629 ms: 1.37x faster                                                   |
| async_tree_io              | 838 ms                                                 | 625 ms: 1.34x faster                                                   |
| deepcopy_memo              | 38.4 us                                                | 29.3 us: 1.31x faster                                                  |
| deepcopy                   | 354 us                                                 | 274 us: 1.29x faster                                                   |
| async_tree_none            | 350 ms                                                 | 271 ms: 1.29x faster                                                   |
| async_tree_memoization     | 437 ms                                                 | 342 ms: 1.28x faster                                                   |
| async_tree_none_tg         | 319 ms                                                 | 254 ms: 1.25x faster                                                   |
| richards                   | 47.5 ms                                                | 38.2 ms: 1.24x faster                                                  |
| richards_super             | 53.7 ms                                                | 45.0 ms: 1.20x faster                                                  |
| deepcopy_reduce            | 3.24 us                                                | 2.74 us: 1.18x faster                                                  |
| regex_effbot               | 3.77 ms                                                | 3.26 ms: 1.16x faster                                                  |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 497 ms: 1.15x faster                                                   |
| scimark_fft                | 367 ms                                                 | 322 ms: 1.14x faster                                                   |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 483 ms: 1.13x faster                                                   |
| xml_etree_parse            | 154 ms                                                 | 137 ms: 1.12x faster                                                   |
| json                       | 5.32 ms                                                | 4.74 ms: 1.12x faster                                                  |
| telco                      | 8.40 ms                                                | 7.56 ms: 1.11x faster                                                  |
| pylint                     | 312 ms                                                 | 284 ms: 1.10x faster                                                   |
| tomli_loads                | 2.12 sec                                               | 1.93 sec: 1.09x faster                                                 |
| unpickle_pure_python       | 213 us                                                 | 196 us: 1.09x faster                                                   |
| nbody                      | 87.7 ms                                                | 81.0 ms: 1.08x faster                                                  |
| xml_etree_generate         | 86.8 ms                                                | 80.2 ms: 1.08x faster                                                  |
| crypto_pyaes               | 74.7 ms                                                | 69.0 ms: 1.08x faster                                                  |
| pathlib                    | 17.4 ms                                                | 16.1 ms: 1.08x faster                                                  |
| regex_v8                   | 26.9 ms                                                | 25.1 ms: 1.07x faster                                                  |
| xml_etree_iterparse        | 101 ms                                                 | 95.4 ms: 1.06x faster                                                  |
| xml_etree_process          | 60.5 ms                                                | 57.1 ms: 1.06x faster                                                  |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.76 ms: 1.06x faster                                                  |
| go                         | 141 ms                                                 | 134 ms: 1.05x faster                                                   |
| mako                       | 10.7 ms                                                | 10.2 ms: 1.05x faster                                                  |
| scimark_monte_carlo        | 66.8 ms                                                | 64.1 ms: 1.04x faster                                                  |
| json_loads                 | 27.2 us                                                | 26.1 us: 1.04x faster                                                  |
| sqlite_synth               | 2.90 us                                                | 2.80 us: 1.04x faster                                                  |
| pyflate                    | 470 ms                                                 | 453 ms: 1.04x faster                                                   |
| float                      | 78.7 ms                                                | 76.1 ms: 1.03x faster                                                  |
| k_core                     | 2.37 sec                                               | 2.30 sec: 1.03x faster                                                 |
| 2to3                       | 266 ms                                                 | 259 ms: 1.03x faster                                                   |
| connected_components       | 447 ms                                                 | 436 ms: 1.02x faster                                                   |
| regex_dna                  | 220 ms                                                 | 215 ms: 1.02x faster                                                   |
| scimark_lu                 | 114 ms                                                 | 112 ms: 1.02x faster                                                   |
| scimark_sor                | 122 ms                                                 | 119 ms: 1.02x faster                                                   |
| bpe_tokeniser              | 4.69 sec                                               | 4.59 sec: 1.02x faster                                                 |
| sqlalchemy_declarative     | 133 ms                                                 | 130 ms: 1.02x faster                                                   |
| regex_compile              | 132 ms                                                 | 130 ms: 1.01x faster                                                   |
| pycparser                  | 1.20 sec                                               | 1.19 sec: 1.01x faster                                                 |
| shortest_path              | 487 ms                                                 | 482 ms: 1.01x faster                                                   |
| sqlalchemy_imperative      | 16.9 ms                                                | 16.8 ms: 1.01x faster                                                  |
| gc_traversal               | 4.90 ms                                                | 4.87 ms: 1.00x faster                                                  |
| deltablue                  | 3.19 ms                                                | 3.18 ms: 1.00x faster                                                  |
| pidigits                   | 186 ms                                                 | 187 ms: 1.00x slower                                                   |
| create_gc_cycles           | 2.45 ms                                                | 2.45 ms: 1.00x slower                                                  |
| asyncio_websockets         | 551 ms                                                 | 553 ms: 1.00x slower                                                   |
| python_startup_no_site     | 7.00 ms                                                | 7.06 ms: 1.01x slower                                                  |
| coverage                   | 82.8 ms                                                | 83.8 ms: 1.01x slower                                                  |
| python_startup             | 12.7 ms                                                | 12.8 ms: 1.01x slower                                                  |
| sympy_str                  | 273 ms                                                 | 277 ms: 1.01x slower                                                   |
| logging_format             | 6.23 us                                                | 6.33 us: 1.02x slower                                                  |
| spectral_norm              | 113 ms                                                 | 115 ms: 1.02x slower                                                   |
| sympy_expand               | 456 ms                                                 | 465 ms: 1.02x slower                                                   |
| sqlglot_normalize          | 108 ms                                                 | 110 ms: 1.02x slower                                                   |
| fannkuch                   | 394 ms                                                 | 402 ms: 1.02x slower                                                   |
| sympy_sum                  | 150 ms                                                 | 154 ms: 1.02x slower                                                   |
| chaos                      | 58.0 ms                                                | 59.4 ms: 1.02x slower                                                  |
| html5lib                   | 63.4 ms                                                | 64.9 ms: 1.02x slower                                                  |
| docutils                   | 2.58 sec                                               | 2.65 sec: 1.02x slower                                                 |
| logging_simple             | 5.65 us                                                | 5.83 us: 1.03x slower                                                  |
| sympy_integrate            | 19.8 ms                                                | 20.5 ms: 1.03x slower                                                  |
| sqlglot_optimize           | 53.4 ms                                                | 55.2 ms: 1.03x slower                                                  |
| sqlglot_transpile          | 1.57 ms                                                | 1.64 ms: 1.04x slower                                                  |
| coroutines                 | 22.2 ms                                                | 23.2 ms: 1.05x slower                                                  |
| async_generators           | 433 ms                                                 | 454 ms: 1.05x slower                                                   |
| sqlglot_parse              | 1.26 ms                                                | 1.33 ms: 1.05x slower                                                  |
| comprehensions             | 16.5 us                                                | 17.4 us: 1.06x slower                                                  |
| dulwich_log                | 64.6 ms                                                | 68.3 ms: 1.06x slower                                                  |
| pickle_pure_python         | 302 us                                                 | 322 us: 1.06x slower                                                   |
| typing_runtime_protocols   | 160 us                                                 | 172 us: 1.08x slower                                                   |
| bench_thread_pool          | 818 us                                                 | 880 us: 1.08x slower                                                   |
| django_template            | 31.7 ms                                                | 34.4 ms: 1.09x slower                                                  |
| json_dumps                 | 10.1 ms                                                | 11.0 ms: 1.09x slower                                                  |
| mdp                        | 2.54 sec                                               | 2.78 sec: 1.09x slower                                                 |
| raytrace                   | 262 ms                                                 | 287 ms: 1.10x slower                                                   |
| genshi_text                | 22.6 ms                                                | 25.0 ms: 1.11x slower                                                  |
| nqueens                    | 80.9 ms                                                | 91.5 ms: 1.13x slower                                                  |
| many_optionals             | 857 us                                                 | 977 us: 1.14x slower                                                   |
| genshi_xml                 | 50.5 ms                                                | 58.8 ms: 1.17x slower                                                  |
| hexiom                     | 6.08 ms                                                | 7.10 ms: 1.17x slower                                                  |
| generators                 | 28.8 ms                                                | 36.5 ms: 1.27x slower                                                  |
| subparsers                 | 15.5 ms                                                | 21.0 ms: 1.36x slower                                                  |
| bench_mp_pool              | 24.0 ms                                                | 82.0 ms: 3.42x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.01x faster                                                           |

Benchmark hidden because not significant (7): pprint_safe_repr, thrift, djangocms, meteor_contest, logging_silent, pprint_pformat, sphinx
Ignored benchmarks (4) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, gevent_hub, gunicorn, tornado_http
Ignored benchmarks (1) of results/bm-20241210-3.14.0a2+-b9d0b2b-JIT/bm-20241210-linux-x86_64-brandtbucher-justin_cold_14-3.14.0a2+-b9d0b2b.json: mypy2

- Geometric mean (including insignificant results): 1.029x faster

# HPT report

- Reliability score: 98.77% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.04x
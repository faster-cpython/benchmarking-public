# Results vs. 3.13.0

- fork: brandtbucher
- ref: justin_compact_exits
- machine: linux-x86_64
- commit hash: aa6e11c
- commit date: 2025-02-06
- overall geometric mean: 1.043x faster
- HPT reliability: 99.72%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250206-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a4+-aa6e11c |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 262 ms: 1.01x faster                                                         |
| docutils       | 2.58 sec                                               | 2.69 sec: 1.04x slower                                                       |
| Geometric mean | (ref)                                                  | 1.01x slower                                                                 |

Benchmark hidden because not significant (2): html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250206-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a4+-aa6e11c |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 317 ms: 1.46x faster                                                         |
| async_tree_io_tg           | 861 ms                                                 | 617 ms: 1.39x faster                                                         |
| async_tree_io              | 838 ms                                                 | 620 ms: 1.35x faster                                                         |
| async_tree_memoization     | 437 ms                                                 | 325 ms: 1.34x faster                                                         |
| async_tree_none            | 350 ms                                                 | 268 ms: 1.31x faster                                                         |
| async_tree_none_tg         | 319 ms                                                 | 253 ms: 1.26x faster                                                         |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 494 ms: 1.16x faster                                                         |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 481 ms: 1.13x faster                                                         |
| async_generators           | 433 ms                                                 | 408 ms: 1.06x faster                                                         |
| coroutines                 | 22.2 ms                                                | 23.0 ms: 1.03x slower                                                        |
| Geometric mean             | (ref)                                                  | 1.21x faster                                                                 |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250206-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a4+-aa6e11c |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 66.9 ms: 1.18x faster                                                        |
| pidigits       | 186 ms                                                 | 186 ms: 1.00x faster                                                         |
| nbody          | 87.7 ms                                                | 94.6 ms: 1.08x slower                                                        |
| Geometric mean | (ref)                                                  | 1.03x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250206-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a4+-aa6e11c |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                | 3.31 ms: 1.14x faster                                                        |
| regex_v8       | 26.9 ms                                                | 24.0 ms: 1.12x faster                                                        |
| regex_dna      | 220 ms                                                 | 212 ms: 1.04x faster                                                         |
| regex_compile  | 132 ms                                                 | 128 ms: 1.03x faster                                                         |
| Geometric mean | (ref)                                                  | 1.08x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250206-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a4+-aa6e11c |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| tomli_loads          | 2.12 sec                                               | 1.79 sec: 1.18x faster                                                       |
| xml_etree_parse      | 154 ms                                                 | 137 ms: 1.13x faster                                                         |
| xml_etree_generate   | 86.8 ms                                                | 77.5 ms: 1.12x faster                                                        |
| xml_etree_process    | 60.5 ms                                                | 54.7 ms: 1.10x faster                                                        |
| unpickle_pure_python | 213 us                                                 | 194 us: 1.10x faster                                                         |
| xml_etree_iterparse  | 101 ms                                                 | 95.2 ms: 1.06x faster                                                        |
| pickle_pure_python   | 302 us                                                 | 318 us: 1.05x slower                                                         |
| json_loads           | 27.2 us                                                | 29.0 us: 1.07x slower                                                        |
| json_dumps           | 10.1 ms                                                | 11.3 ms: 1.12x slower                                                        |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250206-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a4+-aa6e11c |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 7.00 ms                                                | 7.01 ms: 1.00x slower                                                        |
| python_startup         | 12.7 ms                                                | 12.7 ms: 1.01x slower                                                        |
| Geometric mean         | (ref)                                                  | 1.00x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250206-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a4+-aa6e11c |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 10.7 ms                                                | 10.0 ms: 1.07x faster                                                        |
| genshi_text     | 22.6 ms                                                | 23.0 ms: 1.02x slower                                                        |
| django_template | 31.7 ms                                                | 32.3 ms: 1.02x slower                                                        |
| genshi_xml      | 50.5 ms                                                | 55.1 ms: 1.09x slower                                                        |
| Geometric mean  | (ref)                                                  | 1.01x slower                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250206-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a4+-aa6e11c |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 317 ms: 1.46x faster                                                         |
| async_tree_io_tg           | 861 ms                                                 | 617 ms: 1.39x faster                                                         |
| async_tree_io              | 838 ms                                                 | 620 ms: 1.35x faster                                                         |
| async_tree_memoization     | 437 ms                                                 | 325 ms: 1.34x faster                                                         |
| deepcopy                   | 354 us                                                 | 265 us: 1.34x faster                                                         |
| async_tree_none            | 350 ms                                                 | 268 ms: 1.31x faster                                                         |
| deepcopy_memo              | 38.4 us                                                | 30.3 us: 1.27x faster                                                        |
| async_tree_none_tg         | 319 ms                                                 | 253 ms: 1.26x faster                                                         |
| deepcopy_reduce            | 3.24 us                                                | 2.69 us: 1.21x faster                                                        |
| spectral_norm              | 113 ms                                                 | 95.4 ms: 1.19x faster                                                        |
| scimark_fft                | 367 ms                                                 | 310 ms: 1.18x faster                                                         |
| tomli_loads                | 2.12 sec                                               | 1.79 sec: 1.18x faster                                                       |
| float                      | 78.7 ms                                                | 66.9 ms: 1.18x faster                                                        |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 494 ms: 1.16x faster                                                         |
| richards                   | 47.5 ms                                                | 41.2 ms: 1.15x faster                                                        |
| richards_super             | 53.7 ms                                                | 47.2 ms: 1.14x faster                                                        |
| regex_effbot               | 3.77 ms                                                | 3.31 ms: 1.14x faster                                                        |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 481 ms: 1.13x faster                                                         |
| xml_etree_parse            | 154 ms                                                 | 137 ms: 1.13x faster                                                         |
| xml_etree_generate         | 86.8 ms                                                | 77.5 ms: 1.12x faster                                                        |
| regex_v8                   | 26.9 ms                                                | 24.0 ms: 1.12x faster                                                        |
| go                         | 141 ms                                                 | 126 ms: 1.12x faster                                                         |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.54 ms: 1.11x faster                                                        |
| xml_etree_process          | 60.5 ms                                                | 54.7 ms: 1.10x faster                                                        |
| bpe_tokeniser              | 4.69 sec                                               | 4.26 sec: 1.10x faster                                                       |
| telco                      | 8.40 ms                                                | 7.65 ms: 1.10x faster                                                        |
| unpickle_pure_python       | 213 us                                                 | 194 us: 1.10x faster                                                         |
| pylint                     | 312 ms                                                 | 286 ms: 1.09x faster                                                         |
| pathlib                    | 17.4 ms                                                | 16.0 ms: 1.09x faster                                                        |
| pyflate                    | 470 ms                                                 | 438 ms: 1.07x faster                                                         |
| sqlite_synth               | 2.90 us                                                | 2.72 us: 1.07x faster                                                        |
| scimark_sor                | 122 ms                                                 | 114 ms: 1.07x faster                                                         |
| mako                       | 10.7 ms                                                | 10.0 ms: 1.07x faster                                                        |
| xml_etree_iterparse        | 101 ms                                                 | 95.2 ms: 1.06x faster                                                        |
| gc_traversal               | 4.90 ms                                                | 4.61 ms: 1.06x faster                                                        |
| async_generators           | 433 ms                                                 | 408 ms: 1.06x faster                                                         |
| thrift                     | 800 us                                                 | 758 us: 1.05x faster                                                         |
| scimark_monte_carlo        | 66.8 ms                                                | 63.5 ms: 1.05x faster                                                        |
| connected_components       | 447 ms                                                 | 425 ms: 1.05x faster                                                         |
| crypto_pyaes               | 74.7 ms                                                | 71.3 ms: 1.05x faster                                                        |
| json                       | 5.32 ms                                                | 5.12 ms: 1.04x faster                                                        |
| pycparser                  | 1.20 sec                                               | 1.16 sec: 1.04x faster                                                       |
| regex_dna                  | 220 ms                                                 | 212 ms: 1.04x faster                                                         |
| regex_compile              | 132 ms                                                 | 128 ms: 1.03x faster                                                         |
| fannkuch                   | 394 ms                                                 | 382 ms: 1.03x faster                                                         |
| k_core                     | 2.37 sec                                               | 2.30 sec: 1.03x faster                                                       |
| shortest_path              | 487 ms                                                 | 476 ms: 1.02x faster                                                         |
| sqlalchemy_declarative     | 133 ms                                                 | 131 ms: 1.02x faster                                                         |
| 2to3                       | 266 ms                                                 | 262 ms: 1.01x faster                                                         |
| sqlglot_normalize          | 108 ms                                                 | 107 ms: 1.01x faster                                                         |
| sqlalchemy_imperative      | 16.9 ms                                                | 16.8 ms: 1.01x faster                                                        |
| pidigits                   | 186 ms                                                 | 186 ms: 1.00x faster                                                         |
| create_gc_cycles           | 2.45 ms                                                | 2.45 ms: 1.00x faster                                                        |
| python_startup_no_site     | 7.00 ms                                                | 7.01 ms: 1.00x slower                                                        |
| sqlglot_optimize           | 53.4 ms                                                | 53.5 ms: 1.00x slower                                                        |
| python_startup             | 12.7 ms                                                | 12.7 ms: 1.01x slower                                                        |
| pprint_pformat             | 1.48 sec                                               | 1.49 sec: 1.01x slower                                                       |
| comprehensions             | 16.5 us                                                | 16.7 us: 1.01x slower                                                        |
| logging_simple             | 5.65 us                                                | 5.71 us: 1.01x slower                                                        |
| sqlglot_transpile          | 1.57 ms                                                | 1.59 ms: 1.01x slower                                                        |
| pprint_safe_repr           | 727 ms                                                 | 737 ms: 1.01x slower                                                         |
| genshi_text                | 22.6 ms                                                | 23.0 ms: 1.02x slower                                                        |
| scimark_lu                 | 114 ms                                                 | 116 ms: 1.02x slower                                                         |
| django_template            | 31.7 ms                                                | 32.3 ms: 1.02x slower                                                        |
| sympy_sum                  | 150 ms                                                 | 154 ms: 1.02x slower                                                         |
| chaos                      | 58.0 ms                                                | 59.4 ms: 1.02x slower                                                        |
| typing_runtime_protocols   | 160 us                                                 | 164 us: 1.03x slower                                                         |
| sympy_str                  | 273 ms                                                 | 280 ms: 1.03x slower                                                         |
| dulwich_log                | 64.6 ms                                                | 66.7 ms: 1.03x slower                                                        |
| sympy_integrate            | 19.8 ms                                                | 20.5 ms: 1.03x slower                                                        |
| coroutines                 | 22.2 ms                                                | 23.0 ms: 1.03x slower                                                        |
| meteor_contest             | 108 ms                                                 | 113 ms: 1.04x slower                                                         |
| docutils                   | 2.58 sec                                               | 2.69 sec: 1.04x slower                                                       |
| sympy_expand               | 456 ms                                                 | 476 ms: 1.04x slower                                                         |
| pickle_pure_python         | 302 us                                                 | 318 us: 1.05x slower                                                         |
| json_loads                 | 27.2 us                                                | 29.0 us: 1.07x slower                                                        |
| nqueens                    | 80.9 ms                                                | 87.1 ms: 1.08x slower                                                        |
| coverage                   | 82.8 ms                                                | 89.3 ms: 1.08x slower                                                        |
| nbody                      | 87.7 ms                                                | 94.6 ms: 1.08x slower                                                        |
| logging_silent             | 101 ns                                                 | 109 ns: 1.08x slower                                                         |
| genshi_xml                 | 50.5 ms                                                | 55.1 ms: 1.09x slower                                                        |
| bench_thread_pool          | 818 us                                                 | 893 us: 1.09x slower                                                         |
| deltablue                  | 3.19 ms                                                | 3.49 ms: 1.09x slower                                                        |
| raytrace                   | 262 ms                                                 | 287 ms: 1.10x slower                                                         |
| many_optionals             | 857 us                                                 | 956 us: 1.12x slower                                                         |
| json_dumps                 | 10.1 ms                                                | 11.3 ms: 1.12x slower                                                        |
| hexiom                     | 6.08 ms                                                | 7.22 ms: 1.19x slower                                                        |
| generators                 | 28.8 ms                                                | 36.4 ms: 1.27x slower                                                        |
| subparsers                 | 15.5 ms                                                | 20.5 ms: 1.33x slower                                                        |
| bench_mp_pool              | 24.0 ms                                                | 80.3 ms: 3.35x slower                                                        |
| Geometric mean             | (ref)                                                  | 1.03x faster                                                                 |

Benchmark hidden because not significant (6): logging_format, mdp, asyncio_websockets, sqlglot_parse, html5lib, sphinx
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http

- Geometric mean (including insignificant results): 1.043x faster

# HPT report

- Reliability score: 99.72% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.04x
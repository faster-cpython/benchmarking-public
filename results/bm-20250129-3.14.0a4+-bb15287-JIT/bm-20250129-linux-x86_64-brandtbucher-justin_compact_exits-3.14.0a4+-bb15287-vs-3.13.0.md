# Results vs. 3.13.0

- fork: brandtbucher
- ref: justin_compact_exits
- machine: linux-x86_64
- commit hash: bb15287
- commit date: 2025-01-29
- overall geometric mean: 1.047x faster
- HPT reliability: 99.98%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250129-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a4+-bb15287 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 259 ms: 1.03x faster                                                         |
| docutils       | 2.58 sec                                               | 2.65 sec: 1.03x slower                                                       |
| html5lib       | 63.4 ms                                                | 66.1 ms: 1.04x slower                                                        |
| Geometric mean | (ref)                                                  | 1.01x slower                                                                 |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250129-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a4+-bb15287 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 317 ms: 1.46x faster                                                         |
| async_tree_io_tg           | 861 ms                                                 | 611 ms: 1.41x faster                                                         |
| async_tree_io              | 838 ms                                                 | 628 ms: 1.34x faster                                                         |
| async_tree_memoization     | 437 ms                                                 | 329 ms: 1.33x faster                                                         |
| async_tree_none            | 350 ms                                                 | 269 ms: 1.30x faster                                                         |
| async_tree_none_tg         | 319 ms                                                 | 257 ms: 1.24x faster                                                         |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 494 ms: 1.16x faster                                                         |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 483 ms: 1.13x faster                                                         |
| async_generators           | 433 ms                                                 | 407 ms: 1.06x faster                                                         |
| coroutines                 | 22.2 ms                                                | 24.0 ms: 1.08x slower                                                        |
| Geometric mean             | (ref)                                                  | 1.20x faster                                                                 |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250129-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a4+-bb15287 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 66.5 ms: 1.18x faster                                                        |
| nbody          | 87.7 ms                                                | 86.7 ms: 1.01x faster                                                        |
| pidigits       | 186 ms                                                 | 186 ms: 1.00x faster                                                         |
| Geometric mean | (ref)                                                  | 1.06x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250129-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a4+-bb15287 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                | 3.23 ms: 1.17x faster                                                        |
| regex_v8       | 26.9 ms                                                | 23.9 ms: 1.13x faster                                                        |
| regex_dna      | 220 ms                                                 | 213 ms: 1.03x faster                                                         |
| regex_compile  | 132 ms                                                 | 128 ms: 1.03x faster                                                         |
| Geometric mean | (ref)                                                  | 1.09x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250129-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a4+-bb15287 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| tomli_loads          | 2.12 sec                                               | 1.79 sec: 1.18x faster                                                       |
| unpickle_pure_python | 213 us                                                 | 188 us: 1.13x faster                                                         |
| xml_etree_parse      | 154 ms                                                 | 138 ms: 1.12x faster                                                         |
| xml_etree_generate   | 86.8 ms                                                | 78.0 ms: 1.11x faster                                                        |
| xml_etree_process    | 60.5 ms                                                | 54.9 ms: 1.10x faster                                                        |
| xml_etree_iterparse  | 101 ms                                                 | 94.9 ms: 1.07x faster                                                        |
| pickle_pure_python   | 302 us                                                 | 313 us: 1.03x slower                                                         |
| json_loads           | 27.2 us                                                | 28.8 us: 1.06x slower                                                        |
| json_dumps           | 10.1 ms                                                | 11.5 ms: 1.14x slower                                                        |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250129-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a4+-bb15287 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 7.00 ms                                                | 7.11 ms: 1.02x slower                                                        |
| python_startup         | 12.7 ms                                                | 12.9 ms: 1.02x slower                                                        |
| Geometric mean         | (ref)                                                  | 1.02x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250129-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a4+-bb15287 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 10.7 ms                                                | 9.95 ms: 1.07x faster                                                        |
| django_template | 31.7 ms                                                | 31.9 ms: 1.01x slower                                                        |
| genshi_text     | 22.6 ms                                                | 23.5 ms: 1.04x slower                                                        |
| genshi_xml      | 50.5 ms                                                | 57.7 ms: 1.14x slower                                                        |
| Geometric mean  | (ref)                                                  | 1.03x slower                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250129-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a4+-bb15287 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 317 ms: 1.46x faster                                                         |
| async_tree_io_tg           | 861 ms                                                 | 611 ms: 1.41x faster                                                         |
| async_tree_io              | 838 ms                                                 | 628 ms: 1.34x faster                                                         |
| deepcopy                   | 354 us                                                 | 266 us: 1.33x faster                                                         |
| async_tree_memoization     | 437 ms                                                 | 329 ms: 1.33x faster                                                         |
| async_tree_none            | 350 ms                                                 | 269 ms: 1.30x faster                                                         |
| deepcopy_memo              | 38.4 us                                                | 29.6 us: 1.30x faster                                                        |
| async_tree_none_tg         | 319 ms                                                 | 257 ms: 1.24x faster                                                         |
| deepcopy_reduce            | 3.24 us                                                | 2.69 us: 1.21x faster                                                        |
| spectral_norm              | 113 ms                                                 | 94.4 ms: 1.20x faster                                                        |
| scimark_fft                | 367 ms                                                 | 307 ms: 1.19x faster                                                         |
| richards                   | 47.5 ms                                                | 40.0 ms: 1.19x faster                                                        |
| tomli_loads                | 2.12 sec                                               | 1.79 sec: 1.18x faster                                                       |
| float                      | 78.7 ms                                                | 66.5 ms: 1.18x faster                                                        |
| regex_effbot               | 3.77 ms                                                | 3.23 ms: 1.17x faster                                                        |
| richards_super             | 53.7 ms                                                | 46.3 ms: 1.16x faster                                                        |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 494 ms: 1.16x faster                                                         |
| go                         | 141 ms                                                 | 121 ms: 1.16x faster                                                         |
| unpickle_pure_python       | 213 us                                                 | 188 us: 1.13x faster                                                         |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 483 ms: 1.13x faster                                                         |
| regex_v8                   | 26.9 ms                                                | 23.9 ms: 1.13x faster                                                        |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.47 ms: 1.12x faster                                                        |
| xml_etree_parse            | 154 ms                                                 | 138 ms: 1.12x faster                                                         |
| pyflate                    | 470 ms                                                 | 420 ms: 1.12x faster                                                         |
| xml_etree_generate         | 86.8 ms                                                | 78.0 ms: 1.11x faster                                                        |
| pylint                     | 312 ms                                                 | 281 ms: 1.11x faster                                                         |
| bpe_tokeniser              | 4.69 sec                                               | 4.24 sec: 1.11x faster                                                       |
| xml_etree_process          | 60.5 ms                                                | 54.9 ms: 1.10x faster                                                        |
| telco                      | 8.40 ms                                                | 7.64 ms: 1.10x faster                                                        |
| pathlib                    | 17.4 ms                                                | 15.9 ms: 1.09x faster                                                        |
| crypto_pyaes               | 74.7 ms                                                | 69.1 ms: 1.08x faster                                                        |
| sqlite_synth               | 2.90 us                                                | 2.69 us: 1.08x faster                                                        |
| scimark_monte_carlo        | 66.8 ms                                                | 62.0 ms: 1.08x faster                                                        |
| scimark_sor                | 122 ms                                                 | 114 ms: 1.07x faster                                                         |
| mako                       | 10.7 ms                                                | 9.95 ms: 1.07x faster                                                        |
| pycparser                  | 1.20 sec                                               | 1.12 sec: 1.07x faster                                                       |
| xml_etree_iterparse        | 101 ms                                                 | 94.9 ms: 1.07x faster                                                        |
| async_generators           | 433 ms                                                 | 407 ms: 1.06x faster                                                         |
| thrift                     | 800 us                                                 | 762 us: 1.05x faster                                                         |
| k_core                     | 2.37 sec                                               | 2.29 sec: 1.03x faster                                                       |
| fannkuch                   | 394 ms                                                 | 382 ms: 1.03x faster                                                         |
| regex_dna                  | 220 ms                                                 | 213 ms: 1.03x faster                                                         |
| shortest_path              | 487 ms                                                 | 472 ms: 1.03x faster                                                         |
| regex_compile              | 132 ms                                                 | 128 ms: 1.03x faster                                                         |
| pprint_safe_repr           | 727 ms                                                 | 707 ms: 1.03x faster                                                         |
| json                       | 5.32 ms                                                | 5.18 ms: 1.03x faster                                                        |
| connected_components       | 447 ms                                                 | 435 ms: 1.03x faster                                                         |
| 2to3                       | 266 ms                                                 | 259 ms: 1.03x faster                                                         |
| pprint_pformat             | 1.48 sec                                               | 1.45 sec: 1.02x faster                                                       |
| logging_format             | 6.23 us                                                | 6.11 us: 1.02x faster                                                        |
| sqlalchemy_declarative     | 133 ms                                                 | 130 ms: 1.02x faster                                                         |
| sqlalchemy_imperative      | 16.9 ms                                                | 16.7 ms: 1.01x faster                                                        |
| nbody                      | 87.7 ms                                                | 86.7 ms: 1.01x faster                                                        |
| sqlglot_normalize          | 108 ms                                                 | 107 ms: 1.01x faster                                                         |
| logging_simple             | 5.65 us                                                | 5.61 us: 1.01x faster                                                        |
| sqlglot_parse              | 1.26 ms                                                | 1.26 ms: 1.00x faster                                                        |
| gc_traversal               | 4.90 ms                                                | 4.88 ms: 1.00x faster                                                        |
| pidigits                   | 186 ms                                                 | 186 ms: 1.00x faster                                                         |
| sqlglot_transpile          | 1.57 ms                                                | 1.58 ms: 1.00x slower                                                        |
| sqlglot_optimize           | 53.4 ms                                                | 53.6 ms: 1.00x slower                                                        |
| meteor_contest             | 108 ms                                                 | 109 ms: 1.01x slower                                                         |
| scimark_lu                 | 114 ms                                                 | 115 ms: 1.01x slower                                                         |
| django_template            | 31.7 ms                                                | 31.9 ms: 1.01x slower                                                        |
| create_gc_cycles           | 2.45 ms                                                | 2.47 ms: 1.01x slower                                                        |
| typing_runtime_protocols   | 160 us                                                 | 162 us: 1.01x slower                                                         |
| python_startup_no_site     | 7.00 ms                                                | 7.11 ms: 1.02x slower                                                        |
| python_startup             | 12.7 ms                                                | 12.9 ms: 1.02x slower                                                        |
| sympy_str                  | 273 ms                                                 | 279 ms: 1.02x slower                                                         |
| sympy_expand               | 456 ms                                                 | 467 ms: 1.02x slower                                                         |
| sympy_sum                  | 150 ms                                                 | 154 ms: 1.02x slower                                                         |
| docutils                   | 2.58 sec                                               | 2.65 sec: 1.03x slower                                                       |
| sympy_integrate            | 19.8 ms                                                | 20.4 ms: 1.03x slower                                                        |
| pickle_pure_python         | 302 us                                                 | 313 us: 1.03x slower                                                         |
| genshi_text                | 22.6 ms                                                | 23.5 ms: 1.04x slower                                                        |
| dulwich_log                | 64.6 ms                                                | 67.3 ms: 1.04x slower                                                        |
| html5lib                   | 63.4 ms                                                | 66.1 ms: 1.04x slower                                                        |
| json_loads                 | 27.2 us                                                | 28.8 us: 1.06x slower                                                        |
| logging_silent             | 101 ns                                                 | 107 ns: 1.06x slower                                                         |
| deltablue                  | 3.19 ms                                                | 3.43 ms: 1.07x slower                                                        |
| coroutines                 | 22.2 ms                                                | 24.0 ms: 1.08x slower                                                        |
| bench_thread_pool          | 818 us                                                 | 892 us: 1.09x slower                                                         |
| raytrace                   | 262 ms                                                 | 286 ms: 1.09x slower                                                         |
| coverage                   | 82.8 ms                                                | 90.8 ms: 1.10x slower                                                        |
| nqueens                    | 80.9 ms                                                | 89.2 ms: 1.10x slower                                                        |
| many_optionals             | 857 us                                                 | 961 us: 1.12x slower                                                         |
| json_dumps                 | 10.1 ms                                                | 11.5 ms: 1.14x slower                                                        |
| genshi_xml                 | 50.5 ms                                                | 57.7 ms: 1.14x slower                                                        |
| hexiom                     | 6.08 ms                                                | 7.10 ms: 1.17x slower                                                        |
| generators                 | 28.8 ms                                                | 36.5 ms: 1.27x slower                                                        |
| subparsers                 | 15.5 ms                                                | 20.8 ms: 1.35x slower                                                        |
| bench_mp_pool              | 24.0 ms                                                | 81.7 ms: 3.41x slower                                                        |
| Geometric mean             | (ref)                                                  | 1.03x faster                                                                 |

Benchmark hidden because not significant (5): comprehensions, chaos, asyncio_websockets, mdp, sphinx
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http

- Geometric mean (including insignificant results): 1.047x faster

# HPT report

- Reliability score: 99.98% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.04x
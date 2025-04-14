# Results vs. 3.13.0

- fork: brandtbucher
- ref: justin_compact_exits
- machine: linux-x86_64
- commit hash: 31b1d53
- commit date: 2025-02-05
- overall geometric mean: 1.043x faster
- HPT reliability: 99.97%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250205-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a4+-31b1d53 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 258 ms: 1.03x faster                                                         |
| docutils       | 2.58 sec                                               | 2.61 sec: 1.01x slower                                                       |
| html5lib       | 63.4 ms                                                | 61.4 ms: 1.03x faster                                                        |
| sphinx         | 1.03 sec                                               | 1.01 sec: 1.02x faster                                                       |
| Geometric mean | (ref)                                                  | 1.02x faster                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250205-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a4+-31b1d53 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 318 ms: 1.46x faster                                                         |
| async_tree_io_tg           | 861 ms                                                 | 620 ms: 1.39x faster                                                         |
| async_tree_io              | 838 ms                                                 | 626 ms: 1.34x faster                                                         |
| async_tree_memoization     | 437 ms                                                 | 331 ms: 1.32x faster                                                         |
| async_tree_none            | 350 ms                                                 | 269 ms: 1.30x faster                                                         |
| async_tree_none_tg         | 319 ms                                                 | 257 ms: 1.24x faster                                                         |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 501 ms: 1.14x faster                                                         |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 488 ms: 1.11x faster                                                         |
| async_generators           | 433 ms                                                 | 406 ms: 1.07x faster                                                         |
| coroutines                 | 22.2 ms                                                | 23.4 ms: 1.05x slower                                                        |
| Geometric mean             | (ref)                                                  | 1.20x faster                                                                 |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250205-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a4+-31b1d53 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 67.6 ms: 1.16x faster                                                        |
| pidigits       | 186 ms                                                 | 188 ms: 1.01x slower                                                         |
| nbody          | 87.7 ms                                                | 94.8 ms: 1.08x slower                                                        |
| Geometric mean | (ref)                                                  | 1.02x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250205-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a4+-31b1d53 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                | 3.12 ms: 1.21x faster                                                        |
| regex_v8       | 26.9 ms                                                | 24.3 ms: 1.11x faster                                                        |
| regex_dna      | 220 ms                                                 | 210 ms: 1.05x faster                                                         |
| regex_compile  | 132 ms                                                 | 130 ms: 1.02x faster                                                         |
| Geometric mean | (ref)                                                  | 1.09x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250205-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a4+-31b1d53 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| tomli_loads          | 2.12 sec                                               | 1.81 sec: 1.17x faster                                                       |
| xml_etree_parse      | 154 ms                                                 | 137 ms: 1.12x faster                                                         |
| unpickle_pure_python | 213 us                                                 | 194 us: 1.10x faster                                                         |
| xml_etree_generate   | 86.8 ms                                                | 79.6 ms: 1.09x faster                                                        |
| xml_etree_process    | 60.5 ms                                                | 57.0 ms: 1.06x faster                                                        |
| xml_etree_iterparse  | 101 ms                                                 | 95.7 ms: 1.06x faster                                                        |
| pickle_pure_python   | 302 us                                                 | 318 us: 1.05x slower                                                         |
| json_loads           | 27.2 us                                                | 29.0 us: 1.07x slower                                                        |
| json_dumps           | 10.1 ms                                                | 11.7 ms: 1.16x slower                                                        |
| Geometric mean       | (ref)                                                  | 1.03x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250205-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a4+-31b1d53 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 7.00 ms                                                | 7.02 ms: 1.00x slower                                                        |
| python_startup         | 12.7 ms                                                | 12.8 ms: 1.01x slower                                                        |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250205-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a4+-31b1d53 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 10.7 ms                                                | 10.1 ms: 1.06x faster                                                        |
| genshi_text     | 22.6 ms                                                | 23.2 ms: 1.02x slower                                                        |
| django_template | 31.7 ms                                                | 32.8 ms: 1.04x slower                                                        |
| genshi_xml      | 50.5 ms                                                | 56.7 ms: 1.12x slower                                                        |
| Geometric mean  | (ref)                                                  | 1.03x slower                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250205-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a4+-31b1d53 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 318 ms: 1.46x faster                                                         |
| async_tree_io_tg           | 861 ms                                                 | 620 ms: 1.39x faster                                                         |
| async_tree_io              | 838 ms                                                 | 626 ms: 1.34x faster                                                         |
| async_tree_memoization     | 437 ms                                                 | 331 ms: 1.32x faster                                                         |
| deepcopy                   | 354 us                                                 | 269 us: 1.32x faster                                                         |
| async_tree_none            | 350 ms                                                 | 269 ms: 1.30x faster                                                         |
| deepcopy_memo              | 38.4 us                                                | 29.9 us: 1.28x faster                                                        |
| async_tree_none_tg         | 319 ms                                                 | 257 ms: 1.24x faster                                                         |
| regex_effbot               | 3.77 ms                                                | 3.12 ms: 1.21x faster                                                        |
| deepcopy_reduce            | 3.24 us                                                | 2.69 us: 1.20x faster                                                        |
| richards                   | 47.5 ms                                                | 39.9 ms: 1.19x faster                                                        |
| tomli_loads                | 2.12 sec                                               | 1.81 sec: 1.17x faster                                                       |
| richards_super             | 53.7 ms                                                | 46.1 ms: 1.17x faster                                                        |
| float                      | 78.7 ms                                                | 67.6 ms: 1.16x faster                                                        |
| spectral_norm              | 113 ms                                                 | 98.0 ms: 1.16x faster                                                        |
| scimark_fft                | 367 ms                                                 | 318 ms: 1.15x faster                                                         |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 501 ms: 1.14x faster                                                         |
| go                         | 141 ms                                                 | 125 ms: 1.13x faster                                                         |
| pylint                     | 312 ms                                                 | 277 ms: 1.12x faster                                                         |
| xml_etree_parse            | 154 ms                                                 | 137 ms: 1.12x faster                                                         |
| telco                      | 8.40 ms                                                | 7.49 ms: 1.12x faster                                                        |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 488 ms: 1.11x faster                                                         |
| regex_v8                   | 26.9 ms                                                | 24.3 ms: 1.11x faster                                                        |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.56 ms: 1.10x faster                                                        |
| unpickle_pure_python       | 213 us                                                 | 194 us: 1.10x faster                                                         |
| pathlib                    | 17.4 ms                                                | 15.9 ms: 1.09x faster                                                        |
| xml_etree_generate         | 86.8 ms                                                | 79.6 ms: 1.09x faster                                                        |
| scimark_sor                | 122 ms                                                 | 113 ms: 1.08x faster                                                         |
| crypto_pyaes               | 74.7 ms                                                | 70.0 ms: 1.07x faster                                                        |
| async_generators           | 433 ms                                                 | 406 ms: 1.07x faster                                                         |
| scimark_monte_carlo        | 66.8 ms                                                | 63.0 ms: 1.06x faster                                                        |
| xml_etree_process          | 60.5 ms                                                | 57.0 ms: 1.06x faster                                                        |
| xml_etree_iterparse        | 101 ms                                                 | 95.7 ms: 1.06x faster                                                        |
| sqlite_synth               | 2.90 us                                                | 2.74 us: 1.06x faster                                                        |
| mako                       | 10.7 ms                                                | 10.1 ms: 1.06x faster                                                        |
| pycparser                  | 1.20 sec                                               | 1.14 sec: 1.05x faster                                                       |
| bpe_tokeniser              | 4.69 sec                                               | 4.45 sec: 1.05x faster                                                       |
| pyflate                    | 470 ms                                                 | 448 ms: 1.05x faster                                                         |
| regex_dna                  | 220 ms                                                 | 210 ms: 1.05x faster                                                         |
| thrift                     | 800 us                                                 | 765 us: 1.05x faster                                                         |
| k_core                     | 2.37 sec                                               | 2.29 sec: 1.03x faster                                                       |
| 2to3                       | 266 ms                                                 | 258 ms: 1.03x faster                                                         |
| html5lib                   | 63.4 ms                                                | 61.4 ms: 1.03x faster                                                        |
| connected_components       | 447 ms                                                 | 434 ms: 1.03x faster                                                         |
| shortest_path              | 487 ms                                                 | 473 ms: 1.03x faster                                                         |
| json                       | 5.32 ms                                                | 5.18 ms: 1.03x faster                                                        |
| logging_simple             | 5.65 us                                                | 5.52 us: 1.02x faster                                                        |
| gc_traversal               | 4.90 ms                                                | 4.79 ms: 1.02x faster                                                        |
| sphinx                     | 1.03 sec                                               | 1.01 sec: 1.02x faster                                                       |
| fannkuch                   | 394 ms                                                 | 386 ms: 1.02x faster                                                         |
| logging_format             | 6.23 us                                                | 6.12 us: 1.02x faster                                                        |
| sqlalchemy_declarative     | 133 ms                                                 | 130 ms: 1.02x faster                                                         |
| regex_compile              | 132 ms                                                 | 130 ms: 1.02x faster                                                         |
| scimark_lu                 | 114 ms                                                 | 113 ms: 1.02x faster                                                         |
| sqlalchemy_imperative      | 16.9 ms                                                | 16.6 ms: 1.02x faster                                                        |
| sympy_str                  | 273 ms                                                 | 271 ms: 1.01x faster                                                         |
| sqlglot_optimize           | 53.4 ms                                                | 53.1 ms: 1.01x faster                                                        |
| sqlglot_parse              | 1.26 ms                                                | 1.26 ms: 1.01x faster                                                        |
| python_startup_no_site     | 7.00 ms                                                | 7.02 ms: 1.00x slower                                                        |
| pidigits                   | 186 ms                                                 | 188 ms: 1.01x slower                                                         |
| python_startup             | 12.7 ms                                                | 12.8 ms: 1.01x slower                                                        |
| comprehensions             | 16.5 us                                                | 16.7 us: 1.01x slower                                                        |
| docutils                   | 2.58 sec                                               | 2.61 sec: 1.01x slower                                                       |
| sympy_integrate            | 19.8 ms                                                | 20.1 ms: 1.02x slower                                                        |
| chaos                      | 58.0 ms                                                | 59.4 ms: 1.02x slower                                                        |
| genshi_text                | 22.6 ms                                                | 23.2 ms: 1.02x slower                                                        |
| pprint_safe_repr           | 727 ms                                                 | 746 ms: 1.03x slower                                                         |
| meteor_contest             | 108 ms                                                 | 112 ms: 1.03x slower                                                         |
| dulwich_log                | 64.6 ms                                                | 66.8 ms: 1.03x slower                                                        |
| django_template            | 31.7 ms                                                | 32.8 ms: 1.04x slower                                                        |
| pprint_pformat             | 1.48 sec                                               | 1.54 sec: 1.04x slower                                                       |
| coroutines                 | 22.2 ms                                                | 23.4 ms: 1.05x slower                                                        |
| pickle_pure_python         | 302 us                                                 | 318 us: 1.05x slower                                                         |
| deltablue                  | 3.19 ms                                                | 3.40 ms: 1.06x slower                                                        |
| json_loads                 | 27.2 us                                                | 29.0 us: 1.07x slower                                                        |
| nbody                      | 87.7 ms                                                | 94.8 ms: 1.08x slower                                                        |
| coverage                   | 82.8 ms                                                | 89.8 ms: 1.08x slower                                                        |
| logging_silent             | 101 ns                                                 | 110 ns: 1.09x slower                                                         |
| bench_thread_pool          | 818 us                                                 | 891 us: 1.09x slower                                                         |
| raytrace                   | 262 ms                                                 | 286 ms: 1.09x slower                                                         |
| many_optionals             | 857 us                                                 | 960 us: 1.12x slower                                                         |
| nqueens                    | 80.9 ms                                                | 90.7 ms: 1.12x slower                                                        |
| genshi_xml                 | 50.5 ms                                                | 56.7 ms: 1.12x slower                                                        |
| json_dumps                 | 10.1 ms                                                | 11.7 ms: 1.16x slower                                                        |
| hexiom                     | 6.08 ms                                                | 7.28 ms: 1.20x slower                                                        |
| generators                 | 28.8 ms                                                | 36.2 ms: 1.26x slower                                                        |
| subparsers                 | 15.5 ms                                                | 20.4 ms: 1.32x slower                                                        |
| bench_mp_pool              | 24.0 ms                                                | 80.5 ms: 3.36x slower                                                        |
| Geometric mean             | (ref)                                                  | 1.03x faster                                                                 |

Benchmark hidden because not significant (8): sqlglot_normalize, sqlglot_transpile, mdp, sympy_expand, create_gc_cycles, typing_runtime_protocols, sympy_sum, asyncio_websockets
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http

- Geometric mean (including insignificant results): 1.043x faster

# HPT report

- Reliability score: 99.97% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.04x
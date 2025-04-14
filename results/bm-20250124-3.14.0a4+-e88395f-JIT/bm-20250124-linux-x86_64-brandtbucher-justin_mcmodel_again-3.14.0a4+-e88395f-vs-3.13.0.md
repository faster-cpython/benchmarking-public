# Results vs. 3.13.0

- fork: brandtbucher
- ref: justin_mcmodel_again
- machine: linux-x86_64
- commit hash: e88395f
- commit date: 2025-01-24
- overall geometric mean: 1.039x faster
- HPT reliability: 99.86%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.32x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250124-linux-x86_64-brandtbucher-justin_mcmodel_again-3.14.0a4+-e88395f |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 259 ms: 1.03x faster                                                         |
| docutils       | 2.58 sec                                               | 2.67 sec: 1.03x slower                                                       |
| Geometric mean | (ref)                                                  | 1.00x slower                                                                 |

Benchmark hidden because not significant (2): html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250124-linux-x86_64-brandtbucher-justin_mcmodel_again-3.14.0a4+-e88395f |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 318 ms: 1.46x faster                                                         |
| async_tree_io_tg           | 861 ms                                                 | 621 ms: 1.39x faster                                                         |
| async_tree_io              | 838 ms                                                 | 614 ms: 1.37x faster                                                         |
| async_tree_memoization     | 437 ms                                                 | 340 ms: 1.29x faster                                                         |
| async_tree_none            | 350 ms                                                 | 274 ms: 1.28x faster                                                         |
| async_tree_none_tg         | 319 ms                                                 | 256 ms: 1.25x faster                                                         |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 505 ms: 1.13x faster                                                         |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 489 ms: 1.11x faster                                                         |
| async_generators           | 433 ms                                                 | 413 ms: 1.05x faster                                                         |
| coroutines                 | 22.2 ms                                                | 23.8 ms: 1.07x slower                                                        |
| Geometric mean             | (ref)                                                  | 1.19x faster                                                                 |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250124-linux-x86_64-brandtbucher-justin_mcmodel_again-3.14.0a4+-e88395f |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 63.2 ms: 1.24x faster                                                        |
| nbody          | 87.7 ms                                                | 80.4 ms: 1.09x faster                                                        |
| pidigits       | 186 ms                                                 | 186 ms: 1.00x faster                                                         |
| Geometric mean | (ref)                                                  | 1.11x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250124-linux-x86_64-brandtbucher-justin_mcmodel_again-3.14.0a4+-e88395f |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                | 3.32 ms: 1.14x faster                                                        |
| regex_v8       | 26.9 ms                                                | 24.0 ms: 1.12x faster                                                        |
| regex_dna      | 220 ms                                                 | 212 ms: 1.04x faster                                                         |
| regex_compile  | 132 ms                                                 | 129 ms: 1.02x faster                                                         |
| Geometric mean | (ref)                                                  | 1.08x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250124-linux-x86_64-brandtbucher-justin_mcmodel_again-3.14.0a4+-e88395f |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| tomli_loads          | 2.12 sec                                               | 1.85 sec: 1.15x faster                                                       |
| xml_etree_parse      | 154 ms                                                 | 139 ms: 1.11x faster                                                         |
| xml_etree_generate   | 86.8 ms                                                | 78.8 ms: 1.10x faster                                                        |
| unpickle_pure_python | 213 us                                                 | 195 us: 1.09x faster                                                         |
| xml_etree_process    | 60.5 ms                                                | 56.2 ms: 1.08x faster                                                        |
| xml_etree_iterparse  | 101 ms                                                 | 96.0 ms: 1.05x faster                                                        |
| pickle_pure_python   | 302 us                                                 | 309 us: 1.02x slower                                                         |
| json_dumps           | 10.1 ms                                                | 11.2 ms: 1.11x slower                                                        |
| json_loads           | 27.2 us                                                | 35.0 us: 1.29x slower                                                        |
| Geometric mean       | (ref)                                                  | 1.02x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250124-linux-x86_64-brandtbucher-justin_mcmodel_again-3.14.0a4+-e88395f |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 7.00 ms                                                | 7.09 ms: 1.01x slower                                                        |
| python_startup         | 12.7 ms                                                | 12.9 ms: 1.02x slower                                                        |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250124-linux-x86_64-brandtbucher-justin_mcmodel_again-3.14.0a4+-e88395f |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 10.7 ms                                                | 10.0 ms: 1.06x faster                                                        |
| genshi_text     | 22.6 ms                                                | 22.9 ms: 1.01x slower                                                        |
| django_template | 31.7 ms                                                | 33.7 ms: 1.06x slower                                                        |
| genshi_xml      | 50.5 ms                                                | 57.0 ms: 1.13x slower                                                        |
| Geometric mean  | (ref)                                                  | 1.03x slower                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250124-linux-x86_64-brandtbucher-justin_mcmodel_again-3.14.0a4+-e88395f |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 318 ms: 1.46x faster                                                         |
| async_tree_io_tg           | 861 ms                                                 | 621 ms: 1.39x faster                                                         |
| async_tree_io              | 838 ms                                                 | 614 ms: 1.37x faster                                                         |
| deepcopy                   | 354 us                                                 | 264 us: 1.34x faster                                                         |
| async_tree_memoization     | 437 ms                                                 | 340 ms: 1.29x faster                                                         |
| async_tree_none            | 350 ms                                                 | 274 ms: 1.28x faster                                                         |
| deepcopy_memo              | 38.4 us                                                | 30.2 us: 1.27x faster                                                        |
| async_tree_none_tg         | 319 ms                                                 | 256 ms: 1.25x faster                                                         |
| float                      | 78.7 ms                                                | 63.2 ms: 1.24x faster                                                        |
| deepcopy_reduce            | 3.24 us                                                | 2.67 us: 1.21x faster                                                        |
| scimark_fft                | 367 ms                                                 | 309 ms: 1.19x faster                                                         |
| spectral_norm              | 113 ms                                                 | 96.1 ms: 1.18x faster                                                        |
| richards                   | 47.5 ms                                                | 41.3 ms: 1.15x faster                                                        |
| richards_super             | 53.7 ms                                                | 46.8 ms: 1.15x faster                                                        |
| tomli_loads                | 2.12 sec                                               | 1.85 sec: 1.15x faster                                                       |
| regex_effbot               | 3.77 ms                                                | 3.32 ms: 1.14x faster                                                        |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 505 ms: 1.13x faster                                                         |
| regex_v8                   | 26.9 ms                                                | 24.0 ms: 1.12x faster                                                        |
| crypto_pyaes               | 74.7 ms                                                | 67.0 ms: 1.11x faster                                                        |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 489 ms: 1.11x faster                                                         |
| xml_etree_parse            | 154 ms                                                 | 139 ms: 1.11x faster                                                         |
| xml_etree_generate         | 86.8 ms                                                | 78.8 ms: 1.10x faster                                                        |
| telco                      | 8.40 ms                                                | 7.69 ms: 1.09x faster                                                        |
| unpickle_pure_python       | 213 us                                                 | 195 us: 1.09x faster                                                         |
| nbody                      | 87.7 ms                                                | 80.4 ms: 1.09x faster                                                        |
| go                         | 141 ms                                                 | 129 ms: 1.09x faster                                                         |
| pylint                     | 312 ms                                                 | 288 ms: 1.08x faster                                                         |
| pyflate                    | 470 ms                                                 | 433 ms: 1.08x faster                                                         |
| scimark_monte_carlo        | 66.8 ms                                                | 61.8 ms: 1.08x faster                                                        |
| pathlib                    | 17.4 ms                                                | 16.1 ms: 1.08x faster                                                        |
| scimark_sor                | 122 ms                                                 | 113 ms: 1.08x faster                                                         |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.66 ms: 1.08x faster                                                        |
| xml_etree_process          | 60.5 ms                                                | 56.2 ms: 1.08x faster                                                        |
| sqlite_synth               | 2.90 us                                                | 2.70 us: 1.08x faster                                                        |
| pycparser                  | 1.20 sec                                               | 1.12 sec: 1.07x faster                                                       |
| bpe_tokeniser              | 4.69 sec                                               | 4.38 sec: 1.07x faster                                                       |
| mako                       | 10.7 ms                                                | 10.0 ms: 1.06x faster                                                        |
| xml_etree_iterparse        | 101 ms                                                 | 96.0 ms: 1.05x faster                                                        |
| async_generators           | 433 ms                                                 | 413 ms: 1.05x faster                                                         |
| thrift                     | 800 us                                                 | 769 us: 1.04x faster                                                         |
| k_core                     | 2.37 sec                                               | 2.28 sec: 1.04x faster                                                       |
| regex_dna                  | 220 ms                                                 | 212 ms: 1.04x faster                                                         |
| 2to3                       | 266 ms                                                 | 259 ms: 1.03x faster                                                         |
| fannkuch                   | 394 ms                                                 | 384 ms: 1.03x faster                                                         |
| regex_compile              | 132 ms                                                 | 129 ms: 1.02x faster                                                         |
| pprint_safe_repr           | 727 ms                                                 | 711 ms: 1.02x faster                                                         |
| chaos                      | 58.0 ms                                                | 56.9 ms: 1.02x faster                                                        |
| sqlalchemy_declarative     | 133 ms                                                 | 131 ms: 1.02x faster                                                         |
| pprint_pformat             | 1.48 sec                                               | 1.46 sec: 1.01x faster                                                       |
| logging_format             | 6.23 us                                                | 6.16 us: 1.01x faster                                                        |
| sqlglot_parse              | 1.26 ms                                                | 1.25 ms: 1.01x faster                                                        |
| sqlalchemy_imperative      | 16.9 ms                                                | 16.8 ms: 1.01x faster                                                        |
| shortest_path              | 487 ms                                                 | 484 ms: 1.01x faster                                                         |
| pidigits                   | 186 ms                                                 | 186 ms: 1.00x faster                                                         |
| mdp                        | 2.54 sec                                               | 2.56 sec: 1.01x slower                                                       |
| sqlglot_transpile          | 1.57 ms                                                | 1.58 ms: 1.01x slower                                                        |
| create_gc_cycles           | 2.45 ms                                                | 2.47 ms: 1.01x slower                                                        |
| logging_simple             | 5.65 us                                                | 5.72 us: 1.01x slower                                                        |
| python_startup_no_site     | 7.00 ms                                                | 7.09 ms: 1.01x slower                                                        |
| genshi_text                | 22.6 ms                                                | 22.9 ms: 1.01x slower                                                        |
| python_startup             | 12.7 ms                                                | 12.9 ms: 1.02x slower                                                        |
| scimark_lu                 | 114 ms                                                 | 117 ms: 1.02x slower                                                         |
| sympy_str                  | 273 ms                                                 | 279 ms: 1.02x slower                                                         |
| pickle_pure_python         | 302 us                                                 | 309 us: 1.02x slower                                                         |
| sqlglot_optimize           | 53.4 ms                                                | 54.7 ms: 1.02x slower                                                        |
| comprehensions             | 16.5 us                                                | 16.9 us: 1.03x slower                                                        |
| sympy_sum                  | 150 ms                                                 | 155 ms: 1.03x slower                                                         |
| gc_traversal               | 4.90 ms                                                | 5.04 ms: 1.03x slower                                                        |
| sympy_integrate            | 19.8 ms                                                | 20.5 ms: 1.03x slower                                                        |
| docutils                   | 2.58 sec                                               | 2.67 sec: 1.03x slower                                                       |
| dulwich_log                | 64.6 ms                                                | 66.7 ms: 1.03x slower                                                        |
| sympy_expand               | 456 ms                                                 | 472 ms: 1.03x slower                                                         |
| typing_runtime_protocols   | 160 us                                                 | 166 us: 1.03x slower                                                         |
| raytrace                   | 262 ms                                                 | 278 ms: 1.06x slower                                                         |
| django_template            | 31.7 ms                                                | 33.7 ms: 1.06x slower                                                        |
| logging_silent             | 101 ns                                                 | 108 ns: 1.07x slower                                                         |
| coroutines                 | 22.2 ms                                                | 23.8 ms: 1.07x slower                                                        |
| bench_thread_pool          | 818 us                                                 | 889 us: 1.09x slower                                                         |
| coverage                   | 82.8 ms                                                | 90.3 ms: 1.09x slower                                                        |
| nqueens                    | 80.9 ms                                                | 89.6 ms: 1.11x slower                                                        |
| json_dumps                 | 10.1 ms                                                | 11.2 ms: 1.11x slower                                                        |
| json                       | 5.32 ms                                                | 5.95 ms: 1.12x slower                                                        |
| genshi_xml                 | 50.5 ms                                                | 57.0 ms: 1.13x slower                                                        |
| many_optionals             | 857 us                                                 | 973 us: 1.14x slower                                                         |
| hexiom                     | 6.08 ms                                                | 7.12 ms: 1.17x slower                                                        |
| generators                 | 28.8 ms                                                | 35.8 ms: 1.24x slower                                                        |
| json_loads                 | 27.2 us                                                | 35.0 us: 1.29x slower                                                        |
| subparsers                 | 15.5 ms                                                | 20.8 ms: 1.35x slower                                                        |
| bench_mp_pool              | 24.0 ms                                                | 81.1 ms: 3.38x slower                                                        |
| Geometric mean             | (ref)                                                  | 1.02x faster                                                                 |

Benchmark hidden because not significant (7): connected_components, meteor_contest, html5lib, deltablue, asyncio_websockets, sqlglot_normalize, sphinx
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http

- Geometric mean (including insignificant results): 1.039x faster

# HPT report

- Reliability score: 99.86% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.32x
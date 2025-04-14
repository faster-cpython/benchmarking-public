# Results vs. 3.13.0

- fork: brandtbucher
- ref: remove_optimizer_api
- machine: linux-x86_64
- commit hash: 085e172
- commit date: 2025-01-21
- overall geometric mean: 1.033x faster
- HPT reliability: 97.49%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250121-linux-x86_64-brandtbucher-remove_optimizer_api-3.14.0a4+-085e172 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 262 ms: 1.02x faster                                                         |
| docutils       | 2.58 sec                                               | 2.70 sec: 1.04x slower                                                       |
| html5lib       | 63.4 ms                                                | 64.6 ms: 1.02x slower                                                        |
| sphinx         | 1.03 sec                                               | 1.05 sec: 1.02x slower                                                       |
| Geometric mean | (ref)                                                  | 1.02x slower                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250121-linux-x86_64-brandtbucher-remove_optimizer_api-3.14.0a4+-085e172 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 311 ms: 1.49x faster                                                         |
| async_tree_io_tg           | 861 ms                                                 | 589 ms: 1.46x faster                                                         |
| async_tree_io              | 838 ms                                                 | 598 ms: 1.40x faster                                                         |
| async_tree_none            | 350 ms                                                 | 257 ms: 1.36x faster                                                         |
| async_tree_memoization     | 437 ms                                                 | 322 ms: 1.36x faster                                                         |
| async_tree_none_tg         | 319 ms                                                 | 249 ms: 1.28x faster                                                         |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 485 ms: 1.18x faster                                                         |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 466 ms: 1.17x faster                                                         |
| async_generators           | 433 ms                                                 | 415 ms: 1.04x faster                                                         |
| coroutines                 | 22.2 ms                                                | 23.8 ms: 1.07x slower                                                        |
| Geometric mean             | (ref)                                                  | 1.23x faster                                                                 |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250121-linux-x86_64-brandtbucher-remove_optimizer_api-3.14.0a4+-085e172 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 65.1 ms: 1.21x faster                                                        |
| nbody          | 87.7 ms                                                | 86.7 ms: 1.01x faster                                                        |
| pidigits       | 186 ms                                                 | 186 ms: 1.00x faster                                                         |
| Geometric mean | (ref)                                                  | 1.07x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250121-linux-x86_64-brandtbucher-remove_optimizer_api-3.14.0a4+-085e172 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                | 3.30 ms: 1.14x faster                                                        |
| regex_v8       | 26.9 ms                                                | 23.6 ms: 1.14x faster                                                        |
| regex_dna      | 220 ms                                                 | 212 ms: 1.04x faster                                                         |
| regex_compile  | 132 ms                                                 | 130 ms: 1.01x faster                                                         |
| Geometric mean | (ref)                                                  | 1.08x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250121-linux-x86_64-brandtbucher-remove_optimizer_api-3.14.0a4+-085e172 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| tomli_loads          | 2.12 sec                                               | 1.85 sec: 1.15x faster                                                       |
| xml_etree_parse      | 154 ms                                                 | 138 ms: 1.12x faster                                                         |
| xml_etree_generate   | 86.8 ms                                                | 80.3 ms: 1.08x faster                                                        |
| xml_etree_iterparse  | 101 ms                                                 | 94.0 ms: 1.08x faster                                                        |
| unpickle_pure_python | 213 us                                                 | 206 us: 1.03x faster                                                         |
| xml_etree_process    | 60.5 ms                                                | 59.6 ms: 1.02x faster                                                        |
| json_loads           | 27.2 us                                                | 29.4 us: 1.08x slower                                                        |
| pickle_pure_python   | 302 us                                                 | 328 us: 1.08x slower                                                         |
| json_dumps           | 10.1 ms                                                | 11.7 ms: 1.16x slower                                                        |
| Geometric mean       | (ref)                                                  | 1.02x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250121-linux-x86_64-brandtbucher-remove_optimizer_api-3.14.0a4+-085e172 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 7.00 ms                                                | 7.07 ms: 1.01x slower                                                        |
| python_startup         | 12.7 ms                                                | 12.9 ms: 1.02x slower                                                        |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250121-linux-x86_64-brandtbucher-remove_optimizer_api-3.14.0a4+-085e172 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 10.7 ms                                                | 9.83 ms: 1.09x faster                                                        |
| django_template | 31.7 ms                                                | 33.5 ms: 1.06x slower                                                        |
| genshi_text     | 22.6 ms                                                | 24.2 ms: 1.07x slower                                                        |
| genshi_xml      | 50.5 ms                                                | 59.1 ms: 1.17x slower                                                        |
| Geometric mean  | (ref)                                                  | 1.05x slower                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250121-linux-x86_64-brandtbucher-remove_optimizer_api-3.14.0a4+-085e172 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 311 ms: 1.49x faster                                                         |
| async_tree_io_tg           | 861 ms                                                 | 589 ms: 1.46x faster                                                         |
| async_tree_io              | 838 ms                                                 | 598 ms: 1.40x faster                                                         |
| async_tree_none            | 350 ms                                                 | 257 ms: 1.36x faster                                                         |
| async_tree_memoization     | 437 ms                                                 | 322 ms: 1.36x faster                                                         |
| deepcopy                   | 354 us                                                 | 271 us: 1.31x faster                                                         |
| async_tree_none_tg         | 319 ms                                                 | 249 ms: 1.28x faster                                                         |
| deepcopy_memo              | 38.4 us                                                | 30.0 us: 1.28x faster                                                        |
| float                      | 78.7 ms                                                | 65.1 ms: 1.21x faster                                                        |
| deepcopy_reduce            | 3.24 us                                                | 2.69 us: 1.21x faster                                                        |
| spectral_norm              | 113 ms                                                 | 95.1 ms: 1.19x faster                                                        |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 485 ms: 1.18x faster                                                         |
| scimark_fft                | 367 ms                                                 | 313 ms: 1.17x faster                                                         |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 466 ms: 1.17x faster                                                         |
| tomli_loads                | 2.12 sec                                               | 1.85 sec: 1.15x faster                                                       |
| regex_effbot               | 3.77 ms                                                | 3.30 ms: 1.14x faster                                                        |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.42 ms: 1.14x faster                                                        |
| regex_v8                   | 26.9 ms                                                | 23.6 ms: 1.14x faster                                                        |
| xml_etree_parse            | 154 ms                                                 | 138 ms: 1.12x faster                                                         |
| telco                      | 8.40 ms                                                | 7.58 ms: 1.11x faster                                                        |
| crypto_pyaes               | 74.7 ms                                                | 68.4 ms: 1.09x faster                                                        |
| richards_super             | 53.7 ms                                                | 49.3 ms: 1.09x faster                                                        |
| pylint                     | 312 ms                                                 | 287 ms: 1.09x faster                                                         |
| mako                       | 10.7 ms                                                | 9.83 ms: 1.09x faster                                                        |
| xml_etree_generate         | 86.8 ms                                                | 80.3 ms: 1.08x faster                                                        |
| xml_etree_iterparse        | 101 ms                                                 | 94.0 ms: 1.08x faster                                                        |
| bpe_tokeniser              | 4.69 sec                                               | 4.36 sec: 1.08x faster                                                       |
| scimark_monte_carlo        | 66.8 ms                                                | 62.2 ms: 1.07x faster                                                        |
| pathlib                    | 17.4 ms                                                | 16.3 ms: 1.07x faster                                                        |
| gc_traversal               | 4.90 ms                                                | 4.60 ms: 1.07x faster                                                        |
| scimark_sor                | 122 ms                                                 | 115 ms: 1.06x faster                                                         |
| pyflate                    | 470 ms                                                 | 443 ms: 1.06x faster                                                         |
| sqlite_synth               | 2.90 us                                                | 2.74 us: 1.06x faster                                                        |
| go                         | 141 ms                                                 | 133 ms: 1.06x faster                                                         |
| async_generators           | 433 ms                                                 | 415 ms: 1.04x faster                                                         |
| regex_dna                  | 220 ms                                                 | 212 ms: 1.04x faster                                                         |
| pycparser                  | 1.20 sec                                               | 1.16 sec: 1.04x faster                                                       |
| unpickle_pure_python       | 213 us                                                 | 206 us: 1.03x faster                                                         |
| k_core                     | 2.37 sec                                               | 2.30 sec: 1.03x faster                                                       |
| connected_components       | 447 ms                                                 | 436 ms: 1.03x faster                                                         |
| thrift                     | 800 us                                                 | 783 us: 1.02x faster                                                         |
| shortest_path              | 487 ms                                                 | 478 ms: 1.02x faster                                                         |
| 2to3                       | 266 ms                                                 | 262 ms: 1.02x faster                                                         |
| xml_etree_process          | 60.5 ms                                                | 59.6 ms: 1.02x faster                                                        |
| regex_compile              | 132 ms                                                 | 130 ms: 1.01x faster                                                         |
| nbody                      | 87.7 ms                                                | 86.7 ms: 1.01x faster                                                        |
| richards                   | 47.5 ms                                                | 47.1 ms: 1.01x faster                                                        |
| scimark_lu                 | 114 ms                                                 | 113 ms: 1.01x faster                                                         |
| pidigits                   | 186 ms                                                 | 186 ms: 1.00x faster                                                         |
| sqlglot_parse              | 1.26 ms                                                | 1.27 ms: 1.01x slower                                                        |
| sqlglot_normalize          | 108 ms                                                 | 109 ms: 1.01x slower                                                         |
| sqlglot_transpile          | 1.57 ms                                                | 1.58 ms: 1.01x slower                                                        |
| python_startup_no_site     | 7.00 ms                                                | 7.07 ms: 1.01x slower                                                        |
| pprint_safe_repr           | 727 ms                                                 | 737 ms: 1.01x slower                                                         |
| python_startup             | 12.7 ms                                                | 12.9 ms: 1.02x slower                                                        |
| chaos                      | 58.0 ms                                                | 59.0 ms: 1.02x slower                                                        |
| sqlalchemy_imperative      | 16.9 ms                                                | 17.2 ms: 1.02x slower                                                        |
| sphinx                     | 1.03 sec                                               | 1.05 sec: 1.02x slower                                                       |
| html5lib                   | 63.4 ms                                                | 64.6 ms: 1.02x slower                                                        |
| sqlglot_optimize           | 53.4 ms                                                | 54.9 ms: 1.03x slower                                                        |
| sympy_str                  | 273 ms                                                 | 281 ms: 1.03x slower                                                         |
| sympy_sum                  | 150 ms                                                 | 155 ms: 1.03x slower                                                         |
| sympy_expand               | 456 ms                                                 | 475 ms: 1.04x slower                                                         |
| sympy_integrate            | 19.8 ms                                                | 20.7 ms: 1.04x slower                                                        |
| pprint_pformat             | 1.48 sec                                               | 1.54 sec: 1.04x slower                                                       |
| typing_runtime_protocols   | 160 us                                                 | 167 us: 1.04x slower                                                         |
| docutils                   | 2.58 sec                                               | 2.70 sec: 1.04x slower                                                       |
| dulwich_log                | 64.6 ms                                                | 67.9 ms: 1.05x slower                                                        |
| comprehensions             | 16.5 us                                                | 17.4 us: 1.06x slower                                                        |
| django_template            | 31.7 ms                                                | 33.5 ms: 1.06x slower                                                        |
| genshi_text                | 22.6 ms                                                | 24.2 ms: 1.07x slower                                                        |
| coroutines                 | 22.2 ms                                                | 23.8 ms: 1.07x slower                                                        |
| logging_format             | 6.23 us                                                | 6.71 us: 1.08x slower                                                        |
| json_loads                 | 27.2 us                                                | 29.4 us: 1.08x slower                                                        |
| pickle_pure_python         | 302 us                                                 | 328 us: 1.08x slower                                                         |
| logging_simple             | 5.65 us                                                | 6.15 us: 1.09x slower                                                        |
| bench_thread_pool          | 818 us                                                 | 890 us: 1.09x slower                                                         |
| raytrace                   | 262 ms                                                 | 286 ms: 1.09x slower                                                         |
| logging_silent             | 101 ns                                                 | 111 ns: 1.10x slower                                                         |
| coverage                   | 82.8 ms                                                | 91.8 ms: 1.11x slower                                                        |
| nqueens                    | 80.9 ms                                                | 90.9 ms: 1.12x slower                                                        |
| many_optionals             | 857 us                                                 | 987 us: 1.15x slower                                                         |
| json_dumps                 | 10.1 ms                                                | 11.7 ms: 1.16x slower                                                        |
| genshi_xml                 | 50.5 ms                                                | 59.1 ms: 1.17x slower                                                        |
| hexiom                     | 6.08 ms                                                | 7.11 ms: 1.17x slower                                                        |
| generators                 | 28.8 ms                                                | 37.2 ms: 1.29x slower                                                        |
| subparsers                 | 15.5 ms                                                | 21.0 ms: 1.36x slower                                                        |
| bench_mp_pool              | 24.0 ms                                                | 81.7 ms: 3.41x slower                                                        |
| Geometric mean             | (ref)                                                  | 1.02x faster                                                                 |

Benchmark hidden because not significant (8): fannkuch, json, create_gc_cycles, deltablue, sqlalchemy_declarative, asyncio_websockets, meteor_contest, mdp
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http

- Geometric mean (including insignificant results): 1.033x faster

# HPT report

- Reliability score: 97.49% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.04x
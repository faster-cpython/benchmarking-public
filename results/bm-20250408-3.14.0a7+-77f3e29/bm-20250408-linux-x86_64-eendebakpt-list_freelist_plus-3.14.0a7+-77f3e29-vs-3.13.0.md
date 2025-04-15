# Results vs. 3.13.0

- fork: eendebakpt
- ref: list_freelist_plus
- machine: linux-x86_64
- commit hash: 77f3e29
- commit date: 2025-04-08
- overall geometric mean: 1.064x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.03x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250408-linux-x86_64-eendebakpt-list_freelist_plus-3.14.0a7+-77f3e29 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 252 ms: 1.05x faster                                                     |
| html5lib       | 63.4 ms                                                | 62.0 ms: 1.02x faster                                                    |
| sphinx         | 1.03 sec                                               | 1.01 sec: 1.03x faster                                                   |
| Geometric mean | (ref)                                                  | 1.02x faster                                                             |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250408-linux-x86_64-eendebakpt-list_freelist_plus-3.14.0a7+-77f3e29 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 312 ms: 1.48x faster                                                     |
| async_tree_memoization     | 437 ms                                                 | 310 ms: 1.41x faster                                                     |
| async_tree_io_tg           | 861 ms                                                 | 617 ms: 1.39x faster                                                     |
| async_tree_io              | 838 ms                                                 | 608 ms: 1.38x faster                                                     |
| async_tree_none            | 350 ms                                                 | 255 ms: 1.37x faster                                                     |
| async_tree_none_tg         | 319 ms                                                 | 247 ms: 1.29x faster                                                     |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 481 ms: 1.19x faster                                                     |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 469 ms: 1.16x faster                                                     |
| async_generators           | 433 ms                                                 | 388 ms: 1.12x faster                                                     |
| coroutines                 | 22.2 ms                                                | 23.3 ms: 1.05x slower                                                    |
| Geometric mean             | (ref)                                                  | 1.24x faster                                                             |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250408-linux-x86_64-eendebakpt-list_freelist_plus-3.14.0a7+-77f3e29 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 68.3 ms: 1.15x faster                                                    |
| pidigits       | 186 ms                                                 | 186 ms: 1.00x faster                                                     |
| nbody          | 87.7 ms                                                | 95.5 ms: 1.09x slower                                                    |
| Geometric mean | (ref)                                                  | 1.02x faster                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250408-linux-x86_64-eendebakpt-list_freelist_plus-3.14.0a7+-77f3e29 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                | 3.10 ms: 1.22x faster                                                    |
| regex_v8       | 26.9 ms                                                | 22.8 ms: 1.18x faster                                                    |
| regex_dna      | 220 ms                                                 | 204 ms: 1.08x faster                                                     |
| regex_compile  | 132 ms                                                 | 125 ms: 1.06x faster                                                     |
| Geometric mean | (ref)                                                  | 1.13x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250408-linux-x86_64-eendebakpt-list_freelist_plus-3.14.0a7+-77f3e29 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| tomli_loads          | 2.12 sec                                               | 1.94 sec: 1.09x faster                                                   |
| xml_etree_parse      | 154 ms                                                 | 143 ms: 1.08x faster                                                     |
| xml_etree_generate   | 86.8 ms                                                | 85.1 ms: 1.02x faster                                                    |
| xml_etree_iterparse  | 101 ms                                                 | 99.3 ms: 1.02x faster                                                    |
| xml_etree_process    | 60.5 ms                                                | 59.9 ms: 1.01x faster                                                    |
| unpickle_pure_python | 213 us                                                 | 217 us: 1.02x slower                                                     |
| pickle_pure_python   | 302 us                                                 | 312 us: 1.03x slower                                                     |
| json_loads           | 27.2 us                                                | 29.2 us: 1.08x slower                                                    |
| json_dumps           | 10.1 ms                                                | 11.6 ms: 1.14x slower                                                    |
| Geometric mean       | (ref)                                                  | 1.01x slower                                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250408-linux-x86_64-eendebakpt-list_freelist_plus-3.14.0a7+-77f3e29 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 12.7 ms                                                | 13.2 ms: 1.04x slower                                                    |
| python_startup_no_site | 7.00 ms                                                | 8.21 ms: 1.17x slower                                                    |
| Geometric mean         | (ref)                                                  | 1.11x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250408-linux-x86_64-eendebakpt-list_freelist_plus-3.14.0a7+-77f3e29 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| genshi_text     | 22.6 ms                                                | 20.9 ms: 1.08x faster                                                    |
| genshi_xml      | 50.5 ms                                                | 49.0 ms: 1.03x faster                                                    |
| django_template | 31.7 ms                                                | 31.4 ms: 1.01x faster                                                    |
| mako            | 10.7 ms                                                | 11.2 ms: 1.05x slower                                                    |
| Geometric mean  | (ref)                                                  | 1.02x faster                                                             |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250408-linux-x86_64-eendebakpt-list_freelist_plus-3.14.0a7+-77f3e29 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| mdp                        | 2.54 sec                                               | 1.21 sec: 2.10x faster                                                   |
| async_tree_memoization_tg  | 463 ms                                                 | 312 ms: 1.48x faster                                                     |
| deepcopy                   | 354 us                                                 | 251 us: 1.41x faster                                                     |
| async_tree_memoization     | 437 ms                                                 | 310 ms: 1.41x faster                                                     |
| async_tree_io_tg           | 861 ms                                                 | 617 ms: 1.39x faster                                                     |
| async_tree_io              | 838 ms                                                 | 608 ms: 1.38x faster                                                     |
| async_tree_none            | 350 ms                                                 | 255 ms: 1.37x faster                                                     |
| deepcopy_memo              | 38.4 us                                                | 28.8 us: 1.33x faster                                                    |
| async_tree_none_tg         | 319 ms                                                 | 247 ms: 1.29x faster                                                     |
| go                         | 141 ms                                                 | 112 ms: 1.26x faster                                                     |
| deepcopy_reduce            | 3.24 us                                                | 2.60 us: 1.25x faster                                                    |
| regex_effbot               | 3.77 ms                                                | 3.10 ms: 1.22x faster                                                    |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 481 ms: 1.19x faster                                                     |
| regex_v8                   | 26.9 ms                                                | 22.8 ms: 1.18x faster                                                    |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 469 ms: 1.16x faster                                                     |
| float                      | 78.7 ms                                                | 68.3 ms: 1.15x faster                                                    |
| spectral_norm              | 113 ms                                                 | 100.0 ms: 1.13x faster                                                   |
| pylint                     | 312 ms                                                 | 277 ms: 1.13x faster                                                     |
| async_generators           | 433 ms                                                 | 388 ms: 1.12x faster                                                     |
| richards                   | 47.5 ms                                                | 43.1 ms: 1.10x faster                                                    |
| telco                      | 8.40 ms                                                | 7.70 ms: 1.09x faster                                                    |
| tomli_loads                | 2.12 sec                                               | 1.94 sec: 1.09x faster                                                   |
| pycparser                  | 1.20 sec                                               | 1.10 sec: 1.09x faster                                                   |
| dulwich_log                | 64.6 ms                                                | 59.3 ms: 1.09x faster                                                    |
| richards_super             | 53.7 ms                                                | 49.4 ms: 1.09x faster                                                    |
| genshi_text                | 22.6 ms                                                | 20.9 ms: 1.08x faster                                                    |
| xml_etree_parse            | 154 ms                                                 | 143 ms: 1.08x faster                                                     |
| regex_dna                  | 220 ms                                                 | 204 ms: 1.08x faster                                                     |
| crypto_pyaes               | 74.7 ms                                                | 69.9 ms: 1.07x faster                                                    |
| scimark_fft                | 367 ms                                                 | 344 ms: 1.07x faster                                                     |
| chaos                      | 58.0 ms                                                | 54.6 ms: 1.06x faster                                                    |
| regex_compile              | 132 ms                                                 | 125 ms: 1.06x faster                                                     |
| gc_traversal               | 4.90 ms                                                | 4.64 ms: 1.06x faster                                                    |
| 2to3                       | 266 ms                                                 | 252 ms: 1.05x faster                                                     |
| pyflate                    | 470 ms                                                 | 446 ms: 1.05x faster                                                     |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.80 ms: 1.05x faster                                                    |
| pathlib                    | 17.4 ms                                                | 16.6 ms: 1.05x faster                                                    |
| sqlite_synth               | 2.90 us                                                | 2.79 us: 1.04x faster                                                    |
| nqueens                    | 80.9 ms                                                | 77.7 ms: 1.04x faster                                                    |
| bpe_tokeniser              | 4.69 sec                                               | 4.52 sec: 1.04x faster                                                   |
| k_core                     | 2.37 sec                                               | 2.29 sec: 1.04x faster                                                   |
| sympy_integrate            | 19.8 ms                                                | 19.2 ms: 1.03x faster                                                    |
| fannkuch                   | 394 ms                                                 | 381 ms: 1.03x faster                                                     |
| genshi_xml                 | 50.5 ms                                                | 49.0 ms: 1.03x faster                                                    |
| logging_format             | 6.23 us                                                | 6.04 us: 1.03x faster                                                    |
| logging_silent             | 101 ns                                                 | 98.2 ns: 1.03x faster                                                    |
| scimark_sor                | 122 ms                                                 | 119 ms: 1.03x faster                                                     |
| sphinx                     | 1.03 sec                                               | 1.01 sec: 1.03x faster                                                   |
| scimark_monte_carlo        | 66.8 ms                                                | 65.3 ms: 1.02x faster                                                    |
| html5lib                   | 63.4 ms                                                | 62.0 ms: 1.02x faster                                                    |
| json                       | 5.32 ms                                                | 5.21 ms: 1.02x faster                                                    |
| meteor_contest             | 108 ms                                                 | 106 ms: 1.02x faster                                                     |
| xml_etree_generate         | 86.8 ms                                                | 85.1 ms: 1.02x faster                                                    |
| xml_etree_iterparse        | 101 ms                                                 | 99.3 ms: 1.02x faster                                                    |
| raytrace                   | 262 ms                                                 | 257 ms: 1.02x faster                                                     |
| logging_simple             | 5.65 us                                                | 5.55 us: 1.02x faster                                                    |
| sympy_str                  | 273 ms                                                 | 268 ms: 1.02x faster                                                     |
| hexiom                     | 6.08 ms                                                | 5.99 ms: 1.01x faster                                                    |
| sympy_sum                  | 150 ms                                                 | 148 ms: 1.01x faster                                                     |
| xml_etree_process          | 60.5 ms                                                | 59.9 ms: 1.01x faster                                                    |
| django_template            | 31.7 ms                                                | 31.4 ms: 1.01x faster                                                    |
| sqlalchemy_declarative     | 133 ms                                                 | 132 ms: 1.00x faster                                                     |
| pidigits                   | 186 ms                                                 | 186 ms: 1.00x faster                                                     |
| pprint_pformat             | 1.48 sec                                               | 1.49 sec: 1.01x slower                                                   |
| scimark_lu                 | 114 ms                                                 | 115 ms: 1.01x slower                                                     |
| shortest_path              | 487 ms                                                 | 493 ms: 1.01x slower                                                     |
| unpickle_pure_python       | 213 us                                                 | 217 us: 1.02x slower                                                     |
| comprehensions             | 16.5 us                                                | 16.8 us: 1.02x slower                                                    |
| generators                 | 28.8 ms                                                | 29.5 ms: 1.02x slower                                                    |
| pickle_pure_python         | 302 us                                                 | 312 us: 1.03x slower                                                     |
| typing_runtime_protocols   | 160 us                                                 | 166 us: 1.03x slower                                                     |
| coverage                   | 82.8 ms                                                | 86.3 ms: 1.04x slower                                                    |
| python_startup             | 12.7 ms                                                | 13.2 ms: 1.04x slower                                                    |
| mako                       | 10.7 ms                                                | 11.2 ms: 1.05x slower                                                    |
| coroutines                 | 22.2 ms                                                | 23.3 ms: 1.05x slower                                                    |
| deltablue                  | 3.19 ms                                                | 3.36 ms: 1.05x slower                                                    |
| bench_thread_pool          | 818 us                                                 | 878 us: 1.07x slower                                                     |
| json_loads                 | 27.2 us                                                | 29.2 us: 1.08x slower                                                    |
| nbody                      | 87.7 ms                                                | 95.5 ms: 1.09x slower                                                    |
| many_optionals             | 857 us                                                 | 935 us: 1.09x slower                                                     |
| json_dumps                 | 10.1 ms                                                | 11.6 ms: 1.14x slower                                                    |
| python_startup_no_site     | 7.00 ms                                                | 8.21 ms: 1.17x slower                                                    |
| subparsers                 | 15.5 ms                                                | 20.7 ms: 1.34x slower                                                    |
| bench_mp_pool              | 24.0 ms                                                | 82.2 ms: 3.43x slower                                                    |
| Geometric mean             | (ref)                                                  | 1.05x faster                                                             |

Benchmark hidden because not significant (7): sqlalchemy_imperative, pprint_safe_repr, sympy_expand, create_gc_cycles, docutils, asyncio_websockets, connected_components
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
Ignored benchmarks (4) of results/bm-20250408-3.14.0a7+-77f3e29/bm-20250408-linux-x86_64-eendebakpt-list_freelist_plus-3.14.0a7+-77f3e29.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.064x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.03x
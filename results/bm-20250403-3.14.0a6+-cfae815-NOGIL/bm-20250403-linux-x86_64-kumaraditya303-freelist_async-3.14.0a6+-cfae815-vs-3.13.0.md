# Results vs. 3.13.0

- fork: kumaraditya303
- ref: freelist_async
- machine: linux-x86_64
- commit hash: cfae815
- commit date: 2025-04-03
- overall geometric mean: 1.025x slower
- HPT reliability: 99.39%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.23x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250403-linux-x86_64-kumaraditya303-freelist_async-3.14.0a6+-cfae815 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 287 ms: 1.08x slower                                                     |
| docutils       | 2.58 sec                                               | 2.77 sec: 1.07x slower                                                   |
| html5lib       | 63.4 ms                                                | 66.5 ms: 1.05x slower                                                    |
| sphinx         | 1.03 sec                                               | 1.10 sec: 1.07x slower                                                   |
| Geometric mean | (ref)                                                  | 1.07x slower                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250403-linux-x86_64-kumaraditya303-freelist_async-3.14.0a6+-cfae815 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_io_tg           | 861 ms                                                 | 504 ms: 1.71x faster                                                     |
| async_tree_memoization_tg  | 463 ms                                                 | 292 ms: 1.59x faster                                                     |
| async_tree_io              | 838 ms                                                 | 542 ms: 1.55x faster                                                     |
| async_tree_none_tg         | 319 ms                                                 | 223 ms: 1.43x faster                                                     |
| async_tree_none            | 350 ms                                                 | 262 ms: 1.34x faster                                                     |
| async_tree_memoization     | 437 ms                                                 | 328 ms: 1.33x faster                                                     |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 449 ms: 1.21x faster                                                     |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 487 ms: 1.18x faster                                                     |
| async_generators           | 433 ms                                                 | 419 ms: 1.04x faster                                                     |
| coroutines                 | 22.2 ms                                                | 24.2 ms: 1.09x slower                                                    |
| Geometric mean             | (ref)                                                  | 1.27x faster                                                             |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250403-linux-x86_64-kumaraditya303-freelist_async-3.14.0a6+-cfae815 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 68.5 ms: 1.15x faster                                                    |
| pidigits       | 186 ms                                                 | 189 ms: 1.02x slower                                                     |
| nbody          | 87.7 ms                                                | 119 ms: 1.35x slower                                                     |
| Geometric mean | (ref)                                                  | 1.06x slower                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250403-linux-x86_64-kumaraditya303-freelist_async-3.14.0a6+-cfae815 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_v8       | 26.9 ms                                                | 22.0 ms: 1.22x faster                                                    |
| regex_effbot   | 3.77 ms                                                | 3.32 ms: 1.13x faster                                                    |
| regex_dna      | 220 ms                                                 | 211 ms: 1.04x faster                                                     |
| regex_compile  | 132 ms                                                 | 143 ms: 1.09x slower                                                     |
| Geometric mean | (ref)                                                  | 1.07x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250403-linux-x86_64-kumaraditya303-freelist_async-3.14.0a6+-cfae815 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| xml_etree_iterparse  | 101 ms                                                 | 93.9 ms: 1.08x faster                                                    |
| xml_etree_parse      | 154 ms                                                 | 148 ms: 1.04x faster                                                     |
| tomli_loads          | 2.12 sec                                               | 2.15 sec: 1.01x slower                                                   |
| xml_etree_generate   | 86.8 ms                                                | 93.4 ms: 1.08x slower                                                    |
| xml_etree_process    | 60.5 ms                                                | 65.5 ms: 1.08x slower                                                    |
| unpickle_pure_python | 213 us                                                 | 236 us: 1.11x slower                                                     |
| pickle_pure_python   | 302 us                                                 | 336 us: 1.11x slower                                                     |
| json_loads           | 27.2 us                                                | 32.1 us: 1.18x slower                                                    |
| json_dumps           | 10.1 ms                                                | 12.8 ms: 1.26x slower                                                    |
| Geometric mean       | (ref)                                                  | 1.08x slower                                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250403-linux-x86_64-kumaraditya303-freelist_async-3.14.0a6+-cfae815 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 12.7 ms                                                | 15.6 ms: 1.23x slower                                                    |
| python_startup_no_site | 7.00 ms                                                | 10.9 ms: 1.56x slower                                                    |
| Geometric mean         | (ref)                                                  | 1.39x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250403-linux-x86_64-kumaraditya303-freelist_async-3.14.0a6+-cfae815 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| genshi_xml      | 50.5 ms                                                | 58.0 ms: 1.15x slower                                                    |
| genshi_text     | 22.6 ms                                                | 27.1 ms: 1.20x slower                                                    |
| django_template | 31.7 ms                                                | 38.2 ms: 1.21x slower                                                    |
| mako            | 10.7 ms                                                | 15.7 ms: 1.47x slower                                                    |
| Geometric mean  | (ref)                                                  | 1.25x slower                                                             |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250403-linux-x86_64-kumaraditya303-freelist_async-3.14.0a6+-cfae815 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| gc_traversal               | 4.90 ms                                                | 2.03 ms: 2.41x faster                                                    |
| mdp                        | 2.54 sec                                               | 1.37 sec: 1.86x faster                                                   |
| async_tree_io_tg           | 861 ms                                                 | 504 ms: 1.71x faster                                                     |
| async_tree_memoization_tg  | 463 ms                                                 | 292 ms: 1.59x faster                                                     |
| async_tree_io              | 838 ms                                                 | 542 ms: 1.55x faster                                                     |
| create_gc_cycles           | 2.45 ms                                                | 1.69 ms: 1.45x faster                                                    |
| async_tree_none_tg         | 319 ms                                                 | 223 ms: 1.43x faster                                                     |
| async_tree_none            | 350 ms                                                 | 262 ms: 1.34x faster                                                     |
| async_tree_memoization     | 437 ms                                                 | 328 ms: 1.33x faster                                                     |
| regex_v8                   | 26.9 ms                                                | 22.0 ms: 1.22x faster                                                    |
| deepcopy                   | 354 us                                                 | 292 us: 1.21x faster                                                     |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 449 ms: 1.21x faster                                                     |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 487 ms: 1.18x faster                                                     |
| float                      | 78.7 ms                                                | 68.5 ms: 1.15x faster                                                    |
| regex_effbot               | 3.77 ms                                                | 3.32 ms: 1.13x faster                                                    |
| go                         | 141 ms                                                 | 129 ms: 1.09x faster                                                     |
| deepcopy_memo              | 38.4 us                                                | 35.2 us: 1.09x faster                                                    |
| xml_etree_iterparse        | 101 ms                                                 | 93.9 ms: 1.08x faster                                                    |
| deepcopy_reduce            | 3.24 us                                                | 3.10 us: 1.05x faster                                                    |
| sqlite_synth               | 2.90 us                                                | 2.78 us: 1.05x faster                                                    |
| regex_dna                  | 220 ms                                                 | 211 ms: 1.04x faster                                                     |
| pathlib                    | 17.4 ms                                                | 16.7 ms: 1.04x faster                                                    |
| xml_etree_parse            | 154 ms                                                 | 148 ms: 1.04x faster                                                     |
| spectral_norm              | 113 ms                                                 | 109 ms: 1.04x faster                                                     |
| async_generators           | 433 ms                                                 | 419 ms: 1.04x faster                                                     |
| pycparser                  | 1.20 sec                                               | 1.16 sec: 1.03x faster                                                   |
| dulwich_log                | 64.6 ms                                                | 62.7 ms: 1.03x faster                                                    |
| scimark_fft                | 367 ms                                                 | 371 ms: 1.01x slower                                                     |
| tomli_loads                | 2.12 sec                                               | 2.15 sec: 1.01x slower                                                   |
| pidigits                   | 186 ms                                                 | 189 ms: 1.02x slower                                                     |
| k_core                     | 2.37 sec                                               | 2.41 sec: 1.02x slower                                                   |
| logging_silent             | 101 ns                                                 | 103 ns: 1.02x slower                                                     |
| bpe_tokeniser              | 4.69 sec                                               | 4.79 sec: 1.02x slower                                                   |
| generators                 | 28.8 ms                                                | 29.6 ms: 1.03x slower                                                    |
| scimark_sor                | 122 ms                                                 | 127 ms: 1.04x slower                                                     |
| json                       | 5.32 ms                                                | 5.56 ms: 1.04x slower                                                    |
| html5lib                   | 63.4 ms                                                | 66.5 ms: 1.05x slower                                                    |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 5.28 ms: 1.05x slower                                                    |
| sphinx                     | 1.03 sec                                               | 1.10 sec: 1.07x slower                                                   |
| docutils                   | 2.58 sec                                               | 2.77 sec: 1.07x slower                                                   |
| xml_etree_generate         | 86.8 ms                                                | 93.4 ms: 1.08x slower                                                    |
| 2to3                       | 266 ms                                                 | 287 ms: 1.08x slower                                                     |
| xml_etree_process          | 60.5 ms                                                | 65.5 ms: 1.08x slower                                                    |
| richards                   | 47.5 ms                                                | 51.5 ms: 1.08x slower                                                    |
| regex_compile              | 132 ms                                                 | 143 ms: 1.09x slower                                                     |
| coroutines                 | 22.2 ms                                                | 24.2 ms: 1.09x slower                                                    |
| telco                      | 8.40 ms                                                | 9.18 ms: 1.09x slower                                                    |
| richards_super             | 53.7 ms                                                | 59.0 ms: 1.10x slower                                                    |
| pprint_safe_repr           | 727 ms                                                 | 801 ms: 1.10x slower                                                     |
| nqueens                    | 80.9 ms                                                | 89.3 ms: 1.10x slower                                                    |
| unpickle_pure_python       | 213 us                                                 | 236 us: 1.11x slower                                                     |
| pickle_pure_python         | 302 us                                                 | 336 us: 1.11x slower                                                     |
| chaos                      | 58.0 ms                                                | 65.0 ms: 1.12x slower                                                    |
| pprint_pformat             | 1.48 sec                                               | 1.66 sec: 1.12x slower                                                   |
| deltablue                  | 3.19 ms                                                | 3.60 ms: 1.13x slower                                                    |
| sympy_integrate            | 19.8 ms                                                | 22.4 ms: 1.13x slower                                                    |
| sympy_str                  | 273 ms                                                 | 309 ms: 1.13x slower                                                     |
| logging_simple             | 5.65 us                                                | 6.41 us: 1.13x slower                                                    |
| sympy_expand               | 456 ms                                                 | 520 ms: 1.14x slower                                                     |
| genshi_xml                 | 50.5 ms                                                | 58.0 ms: 1.15x slower                                                    |
| crypto_pyaes               | 74.7 ms                                                | 86.1 ms: 1.15x slower                                                    |
| sympy_sum                  | 150 ms                                                 | 173 ms: 1.15x slower                                                     |
| shortest_path              | 487 ms                                                 | 563 ms: 1.16x slower                                                     |
| scimark_lu                 | 114 ms                                                 | 132 ms: 1.16x slower                                                     |
| comprehensions             | 16.5 us                                                | 19.2 us: 1.16x slower                                                    |
| logging_format             | 6.23 us                                                | 7.26 us: 1.16x slower                                                    |
| connected_components       | 447 ms                                                 | 525 ms: 1.17x slower                                                     |
| scimark_monte_carlo        | 66.8 ms                                                | 78.7 ms: 1.18x slower                                                    |
| raytrace                   | 262 ms                                                 | 308 ms: 1.18x slower                                                     |
| hexiom                     | 6.08 ms                                                | 7.17 ms: 1.18x slower                                                    |
| json_loads                 | 27.2 us                                                | 32.1 us: 1.18x slower                                                    |
| sqlalchemy_declarative     | 133 ms                                                 | 158 ms: 1.19x slower                                                     |
| genshi_text                | 22.6 ms                                                | 27.1 ms: 1.20x slower                                                    |
| django_template            | 31.7 ms                                                | 38.2 ms: 1.21x slower                                                    |
| many_optionals             | 857 us                                                 | 1.04 ms: 1.21x slower                                                    |
| sqlalchemy_imperative      | 16.9 ms                                                | 20.5 ms: 1.21x slower                                                    |
| typing_runtime_protocols   | 160 us                                                 | 195 us: 1.22x slower                                                     |
| meteor_contest             | 108 ms                                                 | 133 ms: 1.22x slower                                                     |
| fannkuch                   | 394 ms                                                 | 482 ms: 1.22x slower                                                     |
| python_startup             | 12.7 ms                                                | 15.6 ms: 1.23x slower                                                    |
| json_dumps                 | 10.1 ms                                                | 12.8 ms: 1.26x slower                                                    |
| nbody                      | 87.7 ms                                                | 119 ms: 1.35x slower                                                     |
| coverage                   | 82.8 ms                                                | 119 ms: 1.43x slower                                                     |
| mako                       | 10.7 ms                                                | 15.7 ms: 1.47x slower                                                    |
| subparsers                 | 15.5 ms                                                | 23.4 ms: 1.52x slower                                                    |
| python_startup_no_site     | 7.00 ms                                                | 10.9 ms: 1.56x slower                                                    |
| bench_mp_pool              | 24.0 ms                                                | 90.1 ms: 3.76x slower                                                    |
| bench_thread_pool          | 818 us                                                 | 3.25 ms: 3.98x slower                                                    |
| Geometric mean             | (ref)                                                  | 1.06x slower                                                             |

Benchmark hidden because not significant (3): pylint, asyncio_websockets, pyflate
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
Ignored benchmarks (4) of results/bm-20250403-3.14.0a6+-cfae815-NOGIL/bm-20250403-linux-x86_64-kumaraditya303-freelist_async-3.14.0a6+-cfae815.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.025x slower

# HPT report

- Reliability score: 99.39% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.23x
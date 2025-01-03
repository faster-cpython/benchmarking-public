# Results vs. 3.13.0

- fork: python
- ref: e1baa778f602ede66831
- machine: linux-x86_64
- commit hash: e1baa77
- commit date: 2025-01-02
- overall geometric mean: 1.057x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250102-pythonperf2-x86_64-python-e1baa778f602ede66831-3.14.0a3+-e1baa77 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 281 ms: 1.04x faster                                                         |
| docutils       | 2.83 sec                                                     | 2.90 sec: 1.03x slower                                                       |
| html5lib       | 73.5 ms                                                      | 68.2 ms: 1.08x faster                                                        |
| sphinx         | 1.12 sec                                                     | 1.11 sec: 1.01x faster                                                       |
| Geometric mean | (ref)                                                        | 1.03x faster                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250102-pythonperf2-x86_64-python-e1baa778f602ede66831-3.14.0a3+-e1baa77 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 466 ms                                                       | 326 ms: 1.43x faster                                                         |
| async_tree_io              | 843 ms                                                       | 635 ms: 1.33x faster                                                         |
| async_tree_io_tg           | 831 ms                                                       | 627 ms: 1.33x faster                                                         |
| async_tree_none            | 376 ms                                                       | 289 ms: 1.30x faster                                                         |
| async_tree_none_tg         | 346 ms                                                       | 268 ms: 1.29x faster                                                         |
| async_tree_memoization     | 453 ms                                                       | 352 ms: 1.29x faster                                                         |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 513 ms: 1.18x faster                                                         |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 495 ms: 1.17x faster                                                         |
| async_generators           | 457 ms                                                       | 437 ms: 1.05x faster                                                         |
| coroutines                 | 21.6 ms                                                      | 21.0 ms: 1.03x faster                                                        |
| Geometric mean             | (ref)                                                        | 1.21x faster                                                                 |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250102-pythonperf2-x86_64-python-e1baa778f602ede66831-3.14.0a3+-e1baa77 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 81.3 ms                                                      | 72.1 ms: 1.13x faster                                                        |
| pidigits       | 252 ms                                                       | 255 ms: 1.01x slower                                                         |
| Geometric mean | (ref)                                                        | 1.04x faster                                                                 |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250102-pythonperf2-x86_64-python-e1baa778f602ede66831-3.14.0a3+-e1baa77 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_effbot   | 3.67 ms                                                      | 3.19 ms: 1.15x faster                                                        |
| regex_compile  | 143 ms                                                       | 135 ms: 1.06x faster                                                         |
| regex_dna      | 247 ms                                                       | 235 ms: 1.05x faster                                                         |
| Geometric mean | (ref)                                                        | 1.06x faster                                                                 |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250102-pythonperf2-x86_64-python-e1baa778f602ede66831-3.14.0a3+-e1baa77 |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| tomli_loads          | 2.46 sec                                                     | 2.07 sec: 1.19x faster                                                       |
| xml_etree_parse      | 150 ms                                                       | 135 ms: 1.11x faster                                                         |
| xml_etree_iterparse  | 103 ms                                                       | 94.5 ms: 1.09x faster                                                        |
| xml_etree_generate   | 86.5 ms                                                      | 82.4 ms: 1.05x faster                                                        |
| unpickle_pure_python | 217 us                                                       | 208 us: 1.05x faster                                                         |
| xml_etree_process    | 61.2 ms                                                      | 58.5 ms: 1.04x faster                                                        |
| json_loads           | 24.7 us                                                      | 23.8 us: 1.04x faster                                                        |
| pickle_pure_python   | 323 us                                                       | 326 us: 1.01x slower                                                         |
| json_dumps           | 11.1 ms                                                      | 11.5 ms: 1.03x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.06x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250102-pythonperf2-x86_64-python-e1baa778f602ede66831-3.14.0a3+-e1baa77 |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 8.96 ms                                                      | 9.02 ms: 1.01x slower                                                        |
| python_startup         | 15.9 ms                                                      | 16.1 ms: 1.01x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.01x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250102-pythonperf2-x86_64-python-e1baa778f602ede66831-3.14.0a3+-e1baa77 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| genshi_text    | 26.2 ms                                                      | 24.7 ms: 1.06x faster                                                        |
| genshi_xml     | 57.1 ms                                                      | 54.6 ms: 1.05x faster                                                        |
| mako           | 10.4 ms                                                      | 10.9 ms: 1.05x slower                                                        |
| Geometric mean | (ref)                                                        | 1.02x faster                                                                 |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250102-pythonperf2-x86_64-python-e1baa778f602ede66831-3.14.0a3+-e1baa77 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 466 ms                                                       | 326 ms: 1.43x faster                                                         |
| deepcopy                   | 392 us                                                       | 285 us: 1.38x faster                                                         |
| async_tree_io              | 843 ms                                                       | 635 ms: 1.33x faster                                                         |
| async_tree_io_tg           | 831 ms                                                       | 627 ms: 1.33x faster                                                         |
| async_tree_none            | 376 ms                                                       | 289 ms: 1.30x faster                                                         |
| async_tree_none_tg         | 346 ms                                                       | 268 ms: 1.29x faster                                                         |
| async_tree_memoization     | 453 ms                                                       | 352 ms: 1.29x faster                                                         |
| go                         | 162 ms                                                       | 127 ms: 1.27x faster                                                         |
| deepcopy_memo              | 38.6 us                                                      | 30.4 us: 1.27x faster                                                        |
| deepcopy_reduce            | 3.54 us                                                      | 2.88 us: 1.23x faster                                                        |
| tomli_loads                | 2.46 sec                                                     | 2.07 sec: 1.19x faster                                                       |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 513 ms: 1.18x faster                                                         |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 495 ms: 1.17x faster                                                         |
| regex_effbot               | 3.67 ms                                                      | 3.19 ms: 1.15x faster                                                        |
| richards_super             | 59.6 ms                                                      | 51.7 ms: 1.15x faster                                                        |
| richards                   | 52.9 ms                                                      | 46.0 ms: 1.15x faster                                                        |
| generators                 | 33.6 ms                                                      | 29.5 ms: 1.14x faster                                                        |
| float                      | 81.3 ms                                                      | 72.1 ms: 1.13x faster                                                        |
| json                       | 5.69 ms                                                      | 5.09 ms: 1.12x faster                                                        |
| xml_etree_parse            | 150 ms                                                       | 135 ms: 1.11x faster                                                         |
| telco                      | 8.79 ms                                                      | 7.90 ms: 1.11x faster                                                        |
| pyflate                    | 503 ms                                                       | 453 ms: 1.11x faster                                                         |
| spectral_norm              | 97.0 ms                                                      | 87.7 ms: 1.11x faster                                                        |
| scimark_fft                | 328 ms                                                       | 297 ms: 1.10x faster                                                         |
| pathlib                    | 17.5 ms                                                      | 15.9 ms: 1.10x faster                                                        |
| pylint                     | 347 ms                                                       | 319 ms: 1.09x faster                                                         |
| xml_etree_iterparse        | 103 ms                                                       | 94.5 ms: 1.09x faster                                                        |
| html5lib                   | 73.5 ms                                                      | 68.2 ms: 1.08x faster                                                        |
| bpe_tokeniser              | 5.09 sec                                                     | 4.73 sec: 1.08x faster                                                       |
| scimark_sor                | 123 ms                                                       | 115 ms: 1.07x faster                                                         |
| pprint_pformat             | 1.72 sec                                                     | 1.61 sec: 1.07x faster                                                       |
| hexiom                     | 6.55 ms                                                      | 6.15 ms: 1.07x faster                                                        |
| genshi_text                | 26.2 ms                                                      | 24.7 ms: 1.06x faster                                                        |
| pprint_safe_repr           | 843 ms                                                       | 796 ms: 1.06x faster                                                         |
| scimark_monte_carlo        | 66.1 ms                                                      | 62.6 ms: 1.06x faster                                                        |
| sqlglot_parse              | 1.40 ms                                                      | 1.33 ms: 1.06x faster                                                        |
| regex_compile              | 143 ms                                                       | 135 ms: 1.06x faster                                                         |
| regex_dna                  | 247 ms                                                       | 235 ms: 1.05x faster                                                         |
| xml_etree_generate         | 86.5 ms                                                      | 82.4 ms: 1.05x faster                                                        |
| thrift                     | 901 us                                                       | 859 us: 1.05x faster                                                         |
| unpickle_pure_python       | 217 us                                                       | 208 us: 1.05x faster                                                         |
| async_generators           | 457 ms                                                       | 437 ms: 1.05x faster                                                         |
| genshi_xml                 | 57.1 ms                                                      | 54.6 ms: 1.05x faster                                                        |
| xml_etree_process          | 61.2 ms                                                      | 58.5 ms: 1.04x faster                                                        |
| 2to3                       | 293 ms                                                       | 281 ms: 1.04x faster                                                         |
| scimark_sparse_mat_mult    | 4.77 ms                                                      | 4.59 ms: 1.04x faster                                                        |
| json_loads                 | 24.7 us                                                      | 23.8 us: 1.04x faster                                                        |
| shortest_path              | 460 ms                                                       | 443 ms: 1.04x faster                                                         |
| sqlalchemy_declarative     | 148 ms                                                       | 143 ms: 1.04x faster                                                         |
| sqlglot_transpile          | 1.79 ms                                                      | 1.73 ms: 1.04x faster                                                        |
| sqlglot_normalize          | 119 ms                                                       | 115 ms: 1.04x faster                                                         |
| connected_components       | 432 ms                                                       | 418 ms: 1.03x faster                                                         |
| k_core                     | 2.17 sec                                                     | 2.10 sec: 1.03x faster                                                       |
| scimark_lu                 | 98.7 ms                                                      | 95.8 ms: 1.03x faster                                                        |
| coroutines                 | 21.6 ms                                                      | 21.0 ms: 1.03x faster                                                        |
| sqlglot_optimize           | 59.3 ms                                                      | 57.7 ms: 1.03x faster                                                        |
| meteor_contest             | 130 ms                                                       | 127 ms: 1.02x faster                                                         |
| sqlite_synth               | 2.91 us                                                      | 2.84 us: 1.02x faster                                                        |
| sqlalchemy_imperative      | 18.3 ms                                                      | 17.9 ms: 1.02x faster                                                        |
| sympy_expand               | 509 ms                                                       | 498 ms: 1.02x faster                                                         |
| sympy_str                  | 298 ms                                                       | 292 ms: 1.02x faster                                                         |
| sympy_sum                  | 155 ms                                                       | 152 ms: 1.02x faster                                                         |
| fannkuch                   | 363 ms                                                       | 358 ms: 1.02x faster                                                         |
| sympy_integrate            | 23.6 ms                                                      | 23.2 ms: 1.01x faster                                                        |
| logging_simple             | 6.39 us                                                      | 6.31 us: 1.01x faster                                                        |
| dulwich_log                | 68.2 ms                                                      | 67.3 ms: 1.01x faster                                                        |
| sphinx                     | 1.12 sec                                                     | 1.11 sec: 1.01x faster                                                       |
| nqueens                    | 90.7 ms                                                      | 89.7 ms: 1.01x faster                                                        |
| deltablue                  | 3.42 ms                                                      | 3.39 ms: 1.01x faster                                                        |
| mdp                        | 2.54 sec                                                     | 2.55 sec: 1.00x slower                                                       |
| logging_silent             | 97.9 ns                                                      | 98.4 ns: 1.01x slower                                                        |
| crypto_pyaes               | 73.3 ms                                                      | 73.7 ms: 1.01x slower                                                        |
| python_startup_no_site     | 8.96 ms                                                      | 9.02 ms: 1.01x slower                                                        |
| logging_format             | 6.94 us                                                      | 7.00 us: 1.01x slower                                                        |
| pidigits                   | 252 ms                                                       | 255 ms: 1.01x slower                                                         |
| pickle_pure_python         | 323 us                                                       | 326 us: 1.01x slower                                                         |
| python_startup             | 15.9 ms                                                      | 16.1 ms: 1.01x slower                                                        |
| docutils                   | 2.83 sec                                                     | 2.90 sec: 1.03x slower                                                       |
| json_dumps                 | 11.1 ms                                                      | 11.5 ms: 1.03x slower                                                        |
| typing_runtime_protocols   | 169 us                                                       | 174 us: 1.03x slower                                                         |
| chaos                      | 60.2 ms                                                      | 62.4 ms: 1.04x slower                                                        |
| comprehensions             | 17.0 us                                                      | 17.8 us: 1.05x slower                                                        |
| mako                       | 10.4 ms                                                      | 10.9 ms: 1.05x slower                                                        |
| create_gc_cycles           | 2.68 ms                                                      | 2.85 ms: 1.06x slower                                                        |
| many_optionals             | 930 us                                                       | 1.02 ms: 1.10x slower                                                        |
| subparsers                 | 17.5 ms                                                      | 23.0 ms: 1.32x slower                                                        |
| gc_traversal               | 4.74 ms                                                      | 6.41 ms: 1.35x slower                                                        |
| bench_mp_pool              | 5.12 ms                                                      | 1.59 sec: 310.91x slower                                                     |
| Geometric mean             | (ref)                                                        | 1.00x slower                                                                 |

Benchmark hidden because not significant (9): nbody, bench_thread_pool, djangocms, pycparser, django_template, asyncio_websockets, coverage, raytrace, regex_v8
Ignored benchmarks (4) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, gevent_hub, gunicorn, tornado_http
Ignored benchmarks (1) of results/bm-20250102-3.14.0a3+-e1baa77/bm-20250102-pythonperf2-x86_64-python-e1baa778f602ede66831-3.14.0a3+-e1baa77.json: mypy2

- Geometric mean (including insignificant results): 1.057x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.02x
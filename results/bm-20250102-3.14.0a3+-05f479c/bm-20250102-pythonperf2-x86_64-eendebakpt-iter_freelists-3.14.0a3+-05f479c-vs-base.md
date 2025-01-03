# Results vs. base

- fork: eendebakpt
- ref: iter_freelists
- machine: linux-x86_64
- commit hash: 05f479c
- commit date: 2025-01-02
- overall geometric mean: 1.013x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250102-pythonperf2-x86_64-python-e1baa778f602ede66831-3.14.0a3+-e1baa77 | bm-20250102-pythonperf2-x86_64-eendebakpt-iter_freelists-3.14.0a3+-05f479c |
|----------------|:----------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 281 ms                                                                       | 279 ms: 1.01x faster                                                       |
| docutils       | 2.90 sec                                                                     | 2.84 sec: 1.02x faster                                                     |
| sphinx         | 1.11 sec                                                                     | 1.09 sec: 1.02x faster                                                     |
| Geometric mean | (ref)                                                                        | 1.01x faster                                                               |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250102-pythonperf2-x86_64-python-e1baa778f602ede66831-3.14.0a3+-e1baa77 | bm-20250102-pythonperf2-x86_64-eendebakpt-iter_freelists-3.14.0a3+-05f479c |
|----------------------------|:----------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_none            | 289 ms                                                                       | 280 ms: 1.03x faster                                                       |
| async_tree_memoization     | 352 ms                                                                       | 342 ms: 1.03x faster                                                       |
| async_tree_cpu_io_mixed    | 513 ms                                                                       | 501 ms: 1.02x faster                                                       |
| async_tree_io              | 635 ms                                                                       | 621 ms: 1.02x faster                                                       |
| async_tree_cpu_io_mixed_tg | 495 ms                                                                       | 488 ms: 1.02x faster                                                       |
| async_tree_none_tg         | 268 ms                                                                       | 264 ms: 1.01x faster                                                       |
| asyncio_websockets         | 387 ms                                                                       | 382 ms: 1.01x faster                                                       |
| async_tree_io_tg           | 627 ms                                                                       | 619 ms: 1.01x faster                                                       |
| async_tree_memoization_tg  | 326 ms                                                                       | 323 ms: 1.01x faster                                                       |
| async_generators           | 437 ms                                                                       | 433 ms: 1.01x faster                                                       |
| coroutines                 | 21.0 ms                                                                      | 20.9 ms: 1.01x faster                                                      |
| Geometric mean             | (ref)                                                                        | 1.02x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250102-pythonperf2-x86_64-python-e1baa778f602ede66831-3.14.0a3+-e1baa77 | bm-20250102-pythonperf2-x86_64-eendebakpt-iter_freelists-3.14.0a3+-05f479c |
|----------------|:----------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 72.1 ms                                                                      | 70.8 ms: 1.02x faster                                                      |
| pidigits       | 255 ms                                                                       | 256 ms: 1.01x slower                                                       |
| Geometric mean | (ref)                                                                        | 1.00x faster                                                               |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250102-pythonperf2-x86_64-python-e1baa778f602ede66831-3.14.0a3+-e1baa77 | bm-20250102-pythonperf2-x86_64-eendebakpt-iter_freelists-3.14.0a3+-05f479c |
|----------------|:----------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 135 ms                                                                       | 132 ms: 1.02x faster                                                       |
| regex_v8       | 26.4 ms                                                                      | 26.2 ms: 1.01x faster                                                      |
| regex_dna      | 235 ms                                                                       | 240 ms: 1.02x slower                                                       |
| regex_effbot   | 3.19 ms                                                                      | 3.26 ms: 1.02x slower                                                      |
| Geometric mean | (ref)                                                                        | 1.00x slower                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250102-pythonperf2-x86_64-python-e1baa778f602ede66831-3.14.0a3+-e1baa77 | bm-20250102-pythonperf2-x86_64-eendebakpt-iter_freelists-3.14.0a3+-05f479c |
|----------------------|:----------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| unpickle_pure_python | 208 us                                                                       | 205 us: 1.02x faster                                                       |
| xml_etree_process    | 58.5 ms                                                                      | 57.7 ms: 1.01x faster                                                      |
| xml_etree_generate   | 82.4 ms                                                                      | 81.3 ms: 1.01x faster                                                      |
| json_loads           | 23.8 us                                                                      | 23.5 us: 1.01x faster                                                      |
| tomli_loads          | 2.07 sec                                                                     | 2.06 sec: 1.01x faster                                                     |
| json_dumps           | 11.5 ms                                                                      | 11.4 ms: 1.01x faster                                                      |
| xml_etree_parse      | 135 ms                                                                       | 136 ms: 1.01x slower                                                       |
| xml_etree_iterparse  | 94.5 ms                                                                      | 96.2 ms: 1.02x slower                                                      |
| pickle_pure_python   | 326 us                                                                       | 335 us: 1.03x slower                                                       |
| Geometric mean       | (ref)                                                                        | 1.00x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250102-pythonperf2-x86_64-python-e1baa778f602ede66831-3.14.0a3+-e1baa77 | bm-20250102-pythonperf2-x86_64-eendebakpt-iter_freelists-3.14.0a3+-05f479c |
|------------------------|:----------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 9.02 ms                                                                      | 9.05 ms: 1.00x slower                                                      |
| python_startup         | 16.1 ms                                                                      | 16.1 ms: 1.00x slower                                                      |
| Geometric mean         | (ref)                                                                        | 1.00x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250102-pythonperf2-x86_64-python-e1baa778f602ede66831-3.14.0a3+-e1baa77 | bm-20250102-pythonperf2-x86_64-eendebakpt-iter_freelists-3.14.0a3+-05f479c |
|-----------------|:----------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_text     | 24.7 ms                                                                      | 23.6 ms: 1.05x faster                                                      |
| django_template | 36.2 ms                                                                      | 35.0 ms: 1.03x faster                                                      |
| genshi_xml      | 54.6 ms                                                                      | 54.3 ms: 1.00x faster                                                      |
| mako            | 10.9 ms                                                                      | 11.0 ms: 1.01x slower                                                      |
| Geometric mean  | (ref)                                                                        | 1.02x faster                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20250102-pythonperf2-x86_64-python-e1baa778f602ede66831-3.14.0a3+-e1baa77 | bm-20250102-pythonperf2-x86_64-eendebakpt-iter_freelists-3.14.0a3+-05f479c |
|----------------------------|:----------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| typing_runtime_protocols   | 174 us                                                                       | 165 us: 1.06x faster                                                       |
| sqlglot_optimize           | 57.7 ms                                                                      | 54.8 ms: 1.05x faster                                                      |
| scimark_sor                | 115 ms                                                                       | 109 ms: 1.05x faster                                                       |
| sqlglot_normalize          | 115 ms                                                                       | 110 ms: 1.05x faster                                                       |
| genshi_text                | 24.7 ms                                                                      | 23.6 ms: 1.05x faster                                                      |
| pprint_safe_repr           | 796 ms                                                                       | 763 ms: 1.04x faster                                                       |
| pyflate                    | 453 ms                                                                       | 435 ms: 1.04x faster                                                       |
| nqueens                    | 89.7 ms                                                                      | 86.2 ms: 1.04x faster                                                      |
| comprehensions             | 17.8 us                                                                      | 17.1 us: 1.04x faster                                                      |
| mdp                        | 2.55 sec                                                                     | 2.45 sec: 1.04x faster                                                     |
| pprint_pformat             | 1.61 sec                                                                     | 1.55 sec: 1.04x faster                                                     |
| django_template            | 36.2 ms                                                                      | 35.0 ms: 1.03x faster                                                      |
| async_tree_none            | 289 ms                                                                       | 280 ms: 1.03x faster                                                       |
| deltablue                  | 3.39 ms                                                                      | 3.28 ms: 1.03x faster                                                      |
| bpe_tokeniser              | 4.73 sec                                                                     | 4.59 sec: 1.03x faster                                                     |
| telco                      | 7.90 ms                                                                      | 7.66 ms: 1.03x faster                                                      |
| sympy_expand               | 498 ms                                                                       | 484 ms: 1.03x faster                                                       |
| logging_format             | 7.00 us                                                                      | 6.80 us: 1.03x faster                                                      |
| deepcopy                   | 285 us                                                                       | 277 us: 1.03x faster                                                       |
| async_tree_memoization     | 352 ms                                                                       | 342 ms: 1.03x faster                                                       |
| pycparser                  | 1.24 sec                                                                     | 1.21 sec: 1.03x faster                                                     |
| async_tree_cpu_io_mixed    | 513 ms                                                                       | 501 ms: 1.02x faster                                                       |
| chaos                      | 62.4 ms                                                                      | 60.9 ms: 1.02x faster                                                      |
| sympy_integrate            | 23.2 ms                                                                      | 22.7 ms: 1.02x faster                                                      |
| async_tree_io              | 635 ms                                                                       | 621 ms: 1.02x faster                                                       |
| docutils                   | 2.90 sec                                                                     | 2.84 sec: 1.02x faster                                                     |
| sympy_str                  | 292 ms                                                                       | 286 ms: 1.02x faster                                                       |
| hexiom                     | 6.15 ms                                                                      | 6.01 ms: 1.02x faster                                                      |
| regex_compile              | 135 ms                                                                       | 132 ms: 1.02x faster                                                       |
| thrift                     | 859 us                                                                       | 840 us: 1.02x faster                                                       |
| create_gc_cycles           | 2.85 ms                                                                      | 2.79 ms: 1.02x faster                                                      |
| sphinx                     | 1.11 sec                                                                     | 1.09 sec: 1.02x faster                                                     |
| go                         | 127 ms                                                                       | 125 ms: 1.02x faster                                                       |
| sympy_sum                  | 152 ms                                                                       | 149 ms: 1.02x faster                                                       |
| float                      | 72.1 ms                                                                      | 70.8 ms: 1.02x faster                                                      |
| sqlglot_transpile          | 1.73 ms                                                                      | 1.70 ms: 1.02x faster                                                      |
| many_optionals             | 1.02 ms                                                                      | 1.00 ms: 1.02x faster                                                      |
| unpickle_pure_python       | 208 us                                                                       | 205 us: 1.02x faster                                                       |
| async_tree_cpu_io_mixed_tg | 495 ms                                                                       | 488 ms: 1.02x faster                                                       |
| async_tree_none_tg         | 268 ms                                                                       | 264 ms: 1.01x faster                                                       |
| xml_etree_process          | 58.5 ms                                                                      | 57.7 ms: 1.01x faster                                                      |
| logging_simple             | 6.31 us                                                                      | 6.22 us: 1.01x faster                                                      |
| mypy2                      | 1.03 sec                                                                     | 1.01 sec: 1.01x faster                                                     |
| deepcopy_memo              | 30.4 us                                                                      | 29.9 us: 1.01x faster                                                      |
| crypto_pyaes               | 73.7 ms                                                                      | 72.7 ms: 1.01x faster                                                      |
| xml_etree_generate         | 82.4 ms                                                                      | 81.3 ms: 1.01x faster                                                      |
| asyncio_websockets         | 387 ms                                                                       | 382 ms: 1.01x faster                                                       |
| raytrace                   | 274 ms                                                                       | 270 ms: 1.01x faster                                                       |
| async_tree_io_tg           | 627 ms                                                                       | 619 ms: 1.01x faster                                                       |
| dulwich_log                | 67.3 ms                                                                      | 66.5 ms: 1.01x faster                                                      |
| scimark_lu                 | 95.8 ms                                                                      | 94.7 ms: 1.01x faster                                                      |
| json_loads                 | 23.8 us                                                                      | 23.5 us: 1.01x faster                                                      |
| sqlalchemy_declarative     | 143 ms                                                                       | 142 ms: 1.01x faster                                                       |
| generators                 | 29.5 ms                                                                      | 29.2 ms: 1.01x faster                                                      |
| sqlalchemy_imperative      | 17.9 ms                                                                      | 17.7 ms: 1.01x faster                                                      |
| async_tree_memoization_tg  | 326 ms                                                                       | 323 ms: 1.01x faster                                                       |
| async_generators           | 437 ms                                                                       | 433 ms: 1.01x faster                                                       |
| sqlite_synth               | 2.84 us                                                                      | 2.82 us: 1.01x faster                                                      |
| meteor_contest             | 127 ms                                                                       | 125 ms: 1.01x faster                                                       |
| tomli_loads                | 2.07 sec                                                                     | 2.06 sec: 1.01x faster                                                     |
| regex_v8                   | 26.4 ms                                                                      | 26.2 ms: 1.01x faster                                                      |
| json_dumps                 | 11.5 ms                                                                      | 11.4 ms: 1.01x faster                                                      |
| gc_traversal               | 6.41 ms                                                                      | 6.37 ms: 1.01x faster                                                      |
| 2to3                       | 281 ms                                                                       | 279 ms: 1.01x faster                                                       |
| coroutines                 | 21.0 ms                                                                      | 20.9 ms: 1.01x faster                                                      |
| shortest_path              | 443 ms                                                                       | 441 ms: 1.01x faster                                                       |
| genshi_xml                 | 54.6 ms                                                                      | 54.3 ms: 1.00x faster                                                      |
| logging_silent             | 98.4 ns                                                                      | 97.9 ns: 1.00x faster                                                      |
| pathlib                    | 15.9 ms                                                                      | 15.9 ms: 1.00x faster                                                      |
| python_startup_no_site     | 9.02 ms                                                                      | 9.05 ms: 1.00x slower                                                      |
| python_startup             | 16.1 ms                                                                      | 16.1 ms: 1.00x slower                                                      |
| pidigits                   | 255 ms                                                                       | 256 ms: 1.01x slower                                                       |
| fannkuch                   | 358 ms                                                                       | 360 ms: 1.01x slower                                                       |
| xml_etree_parse            | 135 ms                                                                       | 136 ms: 1.01x slower                                                       |
| richards_super             | 51.7 ms                                                                      | 52.3 ms: 1.01x slower                                                      |
| coverage                   | 80.1 ms                                                                      | 81.2 ms: 1.01x slower                                                      |
| mako                       | 10.9 ms                                                                      | 11.0 ms: 1.01x slower                                                      |
| scimark_fft                | 297 ms                                                                       | 302 ms: 1.02x slower                                                       |
| spectral_norm              | 87.7 ms                                                                      | 89.2 ms: 1.02x slower                                                      |
| xml_etree_iterparse        | 94.5 ms                                                                      | 96.2 ms: 1.02x slower                                                      |
| regex_dna                  | 235 ms                                                                       | 240 ms: 1.02x slower                                                       |
| regex_effbot               | 3.19 ms                                                                      | 3.26 ms: 1.02x slower                                                      |
| pickle_pure_python         | 326 us                                                                       | 335 us: 1.03x slower                                                       |
| scimark_sparse_mat_mult    | 4.59 ms                                                                      | 4.73 ms: 1.03x slower                                                      |
| Geometric mean             | (ref)                                                                        | 1.01x faster                                                               |

Benchmark hidden because not significant (14): bench_mp_pool, pylint, bench_thread_pool, html5lib, k_core, deepcopy_reduce, subparsers, sqlglot_parse, richards, json, nbody, connected_components, djangocms, scimark_monte_carlo

- Geometric mean (including insignificant results): 1.013x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x
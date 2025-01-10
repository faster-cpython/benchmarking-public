# Results vs. base

- fork: kumaraditya303
- ref: fast_coro
- machine: linux-x86_64
- commit hash: e4984ea
- commit date: 2025-01-09
- overall geometric mean: 1.006x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250109-linux-x86_64-python-7dc41ad6a7826ffc675f-3.14.0a3+-7dc41ad | bm-20250109-linux-x86_64-kumaraditya303-fast_coro-3.14.0a3+-e4984ea |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 339 ms                                                                 | 342 ms: 1.01x slower                                                |
| docutils       | 2.97 sec                                                               | 3.01 sec: 1.01x slower                                              |
| html5lib       | 84.3 ms                                                                | 84.9 ms: 1.01x slower                                               |
| sphinx         | 1.16 sec                                                               | 1.17 sec: 1.01x slower                                              |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250109-linux-x86_64-python-7dc41ad6a7826ffc675f-3.14.0a3+-7dc41ad | bm-20250109-linux-x86_64-kumaraditya303-fast_coro-3.14.0a3+-e4984ea |
|----------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_generators           | 499 ms                                                                 | 496 ms: 1.00x faster                                                |
| asyncio_websockets         | 553 ms                                                                 | 550 ms: 1.00x faster                                                |
| coroutines                 | 25.3 ms                                                                | 25.4 ms: 1.00x slower                                               |
| async_tree_cpu_io_mixed    | 580 ms                                                                 | 587 ms: 1.01x slower                                                |
| async_tree_cpu_io_mixed_tg | 535 ms                                                                 | 544 ms: 1.02x slower                                                |
| Geometric mean             | (ref)                                                                  | 1.00x slower                                                        |

Benchmark hidden because not significant (6): async_tree_io, async_tree_none, async_tree_io_tg, async_tree_memoization, async_tree_memoization_tg, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250109-linux-x86_64-python-7dc41ad6a7826ffc675f-3.14.0a3+-7dc41ad | bm-20250109-linux-x86_64-kumaraditya303-fast_coro-3.14.0a3+-e4984ea |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| pidigits       | 181 ms                                                                 | 181 ms: 1.00x slower                                                |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                        |

Benchmark hidden because not significant (2): float, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250109-linux-x86_64-python-7dc41ad6a7826ffc675f-3.14.0a3+-7dc41ad | bm-20250109-linux-x86_64-kumaraditya303-fast_coro-3.14.0a3+-e4984ea |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_v8       | 26.2 ms                                                                | 25.3 ms: 1.03x faster                                               |
| regex_compile  | 160 ms                                                                 | 161 ms: 1.01x slower                                                |
| regex_dna      | 228 ms                                                                 | 233 ms: 1.02x slower                                                |
| regex_effbot   | 3.38 ms                                                                | 3.60 ms: 1.06x slower                                               |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250109-linux-x86_64-python-7dc41ad6a7826ffc675f-3.14.0a3+-7dc41ad | bm-20250109-linux-x86_64-kumaraditya303-fast_coro-3.14.0a3+-e4984ea |
|----------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| xml_etree_iterparse  | 97.2 ms                                                                | 96.3 ms: 1.01x faster                                               |
| tomli_loads          | 2.35 sec                                                               | 2.35 sec: 1.00x slower                                              |
| unpickle_pure_python | 308 us                                                                 | 309 us: 1.01x slower                                                |
| xml_etree_parse      | 147 ms                                                                 | 148 ms: 1.01x slower                                                |
| json_loads           | 29.5 us                                                                | 29.7 us: 1.01x slower                                               |
| xml_etree_process    | 73.3 ms                                                                | 74.2 ms: 1.01x slower                                               |
| json_dumps           | 13.2 ms                                                                | 13.4 ms: 1.01x slower                                               |
| xml_etree_generate   | 98.0 ms                                                                | 100.0 ms: 1.02x slower                                              |
| Geometric mean       | (ref)                                                                  | 1.01x slower                                                        |

Benchmark hidden because not significant (1): pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250109-linux-x86_64-python-7dc41ad6a7826ffc675f-3.14.0a3+-7dc41ad | bm-20250109-linux-x86_64-kumaraditya303-fast_coro-3.14.0a3+-e4984ea |
|------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup_no_site | 9.61 ms                                                                | 9.65 ms: 1.00x slower                                               |
| python_startup         | 15.5 ms                                                                | 15.6 ms: 1.01x slower                                               |
| Geometric mean         | (ref)                                                                  | 1.00x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250109-linux-x86_64-python-7dc41ad6a7826ffc675f-3.14.0a3+-7dc41ad | bm-20250109-linux-x86_64-kumaraditya303-fast_coro-3.14.0a3+-e4984ea |
|-----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| genshi_text     | 30.5 ms                                                                | 30.2 ms: 1.01x faster                                               |
| django_template | 45.7 ms                                                                | 46.6 ms: 1.02x slower                                               |
| Geometric mean  | (ref)                                                                  | 1.00x slower                                                        |

Benchmark hidden because not significant (2): genshi_xml, mako

All benchmarks:
===============

| Benchmark                  | bm-20250109-linux-x86_64-python-7dc41ad6a7826ffc675f-3.14.0a3+-7dc41ad | bm-20250109-linux-x86_64-kumaraditya303-fast_coro-3.14.0a3+-e4984ea |
|----------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| scimark_monte_carlo        | 106 ms                                                                 | 102 ms: 1.04x faster                                                |
| regex_v8                   | 26.2 ms                                                                | 25.3 ms: 1.03x faster                                               |
| logging_silent             | 175 ns                                                                 | 171 ns: 1.02x faster                                                |
| logging_format             | 8.76 us                                                                | 8.57 us: 1.02x faster                                               |
| richards                   | 63.2 ms                                                                | 62.3 ms: 1.01x faster                                               |
| pprint_safe_repr           | 961 ms                                                                 | 949 ms: 1.01x faster                                                |
| pprint_pformat             | 1.99 sec                                                               | 1.97 sec: 1.01x faster                                              |
| logging_simple             | 7.82 us                                                                | 7.74 us: 1.01x faster                                               |
| k_core                     | 2.48 sec                                                               | 2.46 sec: 1.01x faster                                              |
| xml_etree_iterparse        | 97.2 ms                                                                | 96.3 ms: 1.01x faster                                               |
| genshi_text                | 30.5 ms                                                                | 30.2 ms: 1.01x faster                                               |
| sqlite_synth               | 2.77 us                                                                | 2.75 us: 1.01x faster                                               |
| connected_components       | 534 ms                                                                 | 530 ms: 1.01x faster                                                |
| sqlglot_normalize          | 131 ms                                                                 | 130 ms: 1.01x faster                                                |
| scimark_sparse_mat_mult    | 6.17 ms                                                                | 6.13 ms: 1.01x faster                                               |
| async_generators           | 499 ms                                                                 | 496 ms: 1.00x faster                                                |
| asyncio_websockets         | 553 ms                                                                 | 550 ms: 1.00x faster                                                |
| hexiom                     | 9.09 ms                                                                | 9.06 ms: 1.00x faster                                               |
| pidigits                   | 181 ms                                                                 | 181 ms: 1.00x slower                                                |
| scimark_sor                | 182 ms                                                                 | 183 ms: 1.00x slower                                                |
| tomli_loads                | 2.35 sec                                                               | 2.35 sec: 1.00x slower                                              |
| python_startup_no_site     | 9.61 ms                                                                | 9.65 ms: 1.00x slower                                               |
| coroutines                 | 25.3 ms                                                                | 25.4 ms: 1.00x slower                                               |
| shortest_path              | 573 ms                                                                 | 575 ms: 1.00x slower                                                |
| crypto_pyaes               | 91.4 ms                                                                | 91.8 ms: 1.00x slower                                               |
| bench_mp_pool              | 94.9 ms                                                                | 95.3 ms: 1.00x slower                                               |
| sympy_sum                  | 183 ms                                                                 | 184 ms: 1.00x slower                                                |
| unpickle_pure_python       | 308 us                                                                 | 309 us: 1.01x slower                                                |
| python_startup             | 15.5 ms                                                                | 15.6 ms: 1.01x slower                                               |
| sympy_str                  | 331 ms                                                                 | 333 ms: 1.01x slower                                                |
| coverage                   | 101 ms                                                                 | 102 ms: 1.01x slower                                                |
| sqlalchemy_declarative     | 181 ms                                                                 | 182 ms: 1.01x slower                                                |
| deltablue                  | 6.81 ms                                                                | 6.85 ms: 1.01x slower                                               |
| raytrace                   | 466 ms                                                                 | 469 ms: 1.01x slower                                                |
| bpe_tokeniser              | 5.19 sec                                                               | 5.22 sec: 1.01x slower                                              |
| sphinx                     | 1.16 sec                                                               | 1.17 sec: 1.01x slower                                              |
| xml_etree_parse            | 147 ms                                                                 | 148 ms: 1.01x slower                                                |
| html5lib                   | 84.3 ms                                                                | 84.9 ms: 1.01x slower                                               |
| 2to3                       | 339 ms                                                                 | 342 ms: 1.01x slower                                                |
| gc_traversal               | 4.05 ms                                                                | 4.08 ms: 1.01x slower                                               |
| json_loads                 | 29.5 us                                                                | 29.7 us: 1.01x slower                                               |
| chaos                      | 91.3 ms                                                                | 92.1 ms: 1.01x slower                                               |
| deepcopy                   | 314 us                                                                 | 317 us: 1.01x slower                                                |
| scimark_lu                 | 156 ms                                                                 | 158 ms: 1.01x slower                                                |
| regex_compile              | 160 ms                                                                 | 161 ms: 1.01x slower                                                |
| pathlib                    | 16.9 ms                                                                | 17.0 ms: 1.01x slower                                               |
| many_optionals             | 1.12 ms                                                                | 1.13 ms: 1.01x slower                                               |
| create_gc_cycles           | 2.35 ms                                                                | 2.38 ms: 1.01x slower                                               |
| dulwich_log                | 74.0 ms                                                                | 74.9 ms: 1.01x slower                                               |
| xml_etree_process          | 73.3 ms                                                                | 74.2 ms: 1.01x slower                                               |
| async_tree_cpu_io_mixed    | 580 ms                                                                 | 587 ms: 1.01x slower                                                |
| sympy_expand               | 548 ms                                                                 | 555 ms: 1.01x slower                                                |
| meteor_contest             | 131 ms                                                                 | 133 ms: 1.01x slower                                                |
| go                         | 209 ms                                                                 | 212 ms: 1.01x slower                                                |
| docutils                   | 2.97 sec                                                               | 3.01 sec: 1.01x slower                                              |
| json_dumps                 | 13.2 ms                                                                | 13.4 ms: 1.01x slower                                               |
| fannkuch                   | 507 ms                                                                 | 514 ms: 1.01x slower                                                |
| comprehensions             | 25.3 us                                                                | 25.6 us: 1.01x slower                                               |
| async_tree_cpu_io_mixed_tg | 535 ms                                                                 | 544 ms: 1.02x slower                                                |
| json                       | 5.31 ms                                                                | 5.40 ms: 1.02x slower                                               |
| richards_super             | 69.7 ms                                                                | 70.9 ms: 1.02x slower                                               |
| typing_runtime_protocols   | 205 us                                                                 | 208 us: 1.02x slower                                                |
| subparsers                 | 25.9 ms                                                                | 26.3 ms: 1.02x slower                                               |
| django_template            | 45.7 ms                                                                | 46.6 ms: 1.02x slower                                               |
| regex_dna                  | 228 ms                                                                 | 233 ms: 1.02x slower                                                |
| xml_etree_generate         | 98.0 ms                                                                | 100.0 ms: 1.02x slower                                              |
| generators                 | 35.8 ms                                                                | 36.9 ms: 1.03x slower                                               |
| pyflate                    | 616 ms                                                                 | 636 ms: 1.03x slower                                                |
| pycparser                  | 1.29 sec                                                               | 1.34 sec: 1.04x slower                                              |
| mdp                        | 2.88 sec                                                               | 3.01 sec: 1.04x slower                                              |
| spectral_norm              | 119 ms                                                                 | 125 ms: 1.05x slower                                                |
| regex_effbot               | 3.38 ms                                                                | 3.60 ms: 1.06x slower                                               |
| Geometric mean             | (ref)                                                                  | 1.01x slower                                                        |

Benchmark hidden because not significant (24): telco, sqlglot_transpile, async_tree_io, pickle_pure_python, deepcopy_reduce, genshi_xml, sympy_integrate, bench_thread_pool, sqlglot_optimize, mako, scimark_fft, float, async_tree_none, async_tree_io_tg, nqueens, async_tree_memoization, deepcopy_memo, nbody, thrift, sqlglot_parse, async_tree_memoization_tg, pylint, async_tree_none_tg, sqlalchemy_imperative

- Geometric mean (including insignificant results): 1.006x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.01x
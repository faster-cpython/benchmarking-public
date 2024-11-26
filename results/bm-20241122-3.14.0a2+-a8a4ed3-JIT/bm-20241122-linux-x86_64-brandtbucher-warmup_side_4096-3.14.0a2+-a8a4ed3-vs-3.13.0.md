# Results vs. 3.13.0

- fork: brandtbucher
- ref: warmup_side_4096
- machine: linux-x86_64
- commit hash: a8a4ed3
- commit date: 2024-11-22
- overall geometric mean: 1.018x faster
- HPT reliability: 94.40%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.03x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241122-linux-x86_64-brandtbucher-warmup_side_4096-3.14.0a2+-a8a4ed3 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 267 ms                                                 | 260 ms: 1.03x faster                                                     |
| docutils       | 2.59 sec                                               | 2.77 sec: 1.07x slower                                                   |
| html5lib       | 64.2 ms                                                | 67.1 ms: 1.04x slower                                                    |
| sphinx         | 1.03 sec                                               | 1.09 sec: 1.05x slower                                                   |
| Geometric mean | (ref)                                                  | 1.03x slower                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241122-linux-x86_64-brandtbucher-warmup_side_4096-3.14.0a2+-a8a4ed3 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 464 ms                                                 | 400 ms: 1.16x faster                                                     |
| async_tree_none            | 351 ms                                                 | 325 ms: 1.08x faster                                                     |
| async_tree_memoization     | 442 ms                                                 | 411 ms: 1.08x faster                                                     |
| async_tree_cpu_io_mixed    | 577 ms                                                 | 563 ms: 1.03x faster                                                     |
| asyncio_websockets         | 552 ms                                                 | 554 ms: 1.00x slower                                                     |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 567 ms: 1.04x slower                                                     |
| async_generators           | 436 ms                                                 | 461 ms: 1.06x slower                                                     |
| async_tree_io_tg           | 857 ms                                                 | 917 ms: 1.07x slower                                                     |
| async_tree_io              | 842 ms                                                 | 914 ms: 1.09x slower                                                     |
| Geometric mean             | (ref)                                                  | 1.01x faster                                                             |

Benchmark hidden because not significant (2): async_tree_none_tg, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241122-linux-x86_64-brandtbucher-warmup_side_4096-3.14.0a2+-a8a4ed3 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| nbody          | 87.0 ms                                                | 82.9 ms: 1.05x faster                                                    |
| float          | 79.2 ms                                                | 78.0 ms: 1.02x faster                                                    |
| pidigits       | 186 ms                                                 | 188 ms: 1.01x slower                                                     |
| Geometric mean | (ref)                                                  | 1.02x faster                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241122-linux-x86_64-brandtbucher-warmup_side_4096-3.14.0a2+-a8a4ed3 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_effbot   | 3.73 ms                                                | 3.36 ms: 1.11x faster                                                    |
| regex_compile  | 132 ms                                                 | 129 ms: 1.03x faster                                                     |
| regex_v8       | 26.2 ms                                                | 25.9 ms: 1.01x faster                                                    |
| Geometric mean | (ref)                                                  | 1.04x faster                                                             |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241122-linux-x86_64-brandtbucher-warmup_side_4096-3.14.0a2+-a8a4ed3 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| unpickle_pure_python | 216 us                                                 | 195 us: 1.11x faster                                                     |
| xml_etree_generate   | 86.7 ms                                                | 78.5 ms: 1.10x faster                                                    |
| xml_etree_process    | 60.6 ms                                                | 55.4 ms: 1.10x faster                                                    |
| tomli_loads          | 2.14 sec                                               | 1.96 sec: 1.09x faster                                                   |
| xml_etree_parse      | 156 ms                                                 | 148 ms: 1.05x faster                                                     |
| json_loads           | 27.2 us                                                | 26.2 us: 1.04x faster                                                    |
| pickle_pure_python   | 310 us                                                 | 320 us: 1.03x slower                                                     |
| json_dumps           | 10.6 ms                                                | 11.2 ms: 1.06x slower                                                    |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                             |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241122-linux-x86_64-brandtbucher-warmup_side_4096-3.14.0a2+-a8a4ed3 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 6.96 ms                                                | 7.09 ms: 1.02x slower                                                    |
| python_startup         | 12.5 ms                                                | 12.9 ms: 1.03x slower                                                    |
| Geometric mean         | (ref)                                                  | 1.03x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241122-linux-x86_64-brandtbucher-warmup_side_4096-3.14.0a2+-a8a4ed3 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| mako            | 11.1 ms                                                | 9.96 ms: 1.11x faster                                                    |
| django_template | 35.2 ms                                                | 33.5 ms: 1.05x faster                                                    |
| genshi_text     | 23.5 ms                                                | 25.4 ms: 1.08x slower                                                    |
| genshi_xml      | 50.9 ms                                                | 59.6 ms: 1.17x slower                                                    |
| Geometric mean  | (ref)                                                  | 1.02x slower                                                             |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241122-linux-x86_64-brandtbucher-warmup_side_4096-3.14.0a2+-a8a4ed3 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| deepcopy                   | 358 us                                                 | 267 us: 1.34x faster                                                     |
| deepcopy_memo              | 39.1 us                                                | 29.2 us: 1.34x faster                                                    |
| richards                   | 48.7 ms                                                | 38.5 ms: 1.26x faster                                                    |
| richards_super             | 54.9 ms                                                | 44.5 ms: 1.23x faster                                                    |
| deepcopy_reduce            | 3.20 us                                                | 2.71 us: 1.18x faster                                                    |
| async_tree_memoization_tg  | 464 ms                                                 | 400 ms: 1.16x faster                                                     |
| pylint                     | 313 ms                                                 | 272 ms: 1.15x faster                                                     |
| scimark_fft                | 364 ms                                                 | 318 ms: 1.14x faster                                                     |
| telco                      | 8.54 ms                                                | 7.57 ms: 1.13x faster                                                    |
| json                       | 5.36 ms                                                | 4.78 ms: 1.12x faster                                                    |
| mako                       | 11.1 ms                                                | 9.96 ms: 1.11x faster                                                    |
| regex_effbot               | 3.73 ms                                                | 3.36 ms: 1.11x faster                                                    |
| unpickle_pure_python       | 216 us                                                 | 195 us: 1.11x faster                                                     |
| xml_etree_generate         | 86.7 ms                                                | 78.5 ms: 1.10x faster                                                    |
| scimark_sparse_mat_mult    | 5.04 ms                                                | 4.57 ms: 1.10x faster                                                    |
| crypto_pyaes               | 75.3 ms                                                | 68.5 ms: 1.10x faster                                                    |
| xml_etree_process          | 60.6 ms                                                | 55.4 ms: 1.10x faster                                                    |
| tomli_loads                | 2.14 sec                                               | 1.96 sec: 1.09x faster                                                   |
| async_tree_none            | 351 ms                                                 | 325 ms: 1.08x faster                                                     |
| go                         | 144 ms                                                 | 133 ms: 1.08x faster                                                     |
| async_tree_memoization     | 442 ms                                                 | 411 ms: 1.08x faster                                                     |
| pathlib                    | 17.5 ms                                                | 16.4 ms: 1.07x faster                                                    |
| pyflate                    | 471 ms                                                 | 442 ms: 1.07x faster                                                     |
| pycparser                  | 1.20 sec                                               | 1.14 sec: 1.05x faster                                                   |
| bpe_tokeniser              | 4.75 sec                                               | 4.51 sec: 1.05x faster                                                   |
| mdp                        | 2.72 sec                                               | 2.59 sec: 1.05x faster                                                   |
| django_template            | 35.2 ms                                                | 33.5 ms: 1.05x faster                                                    |
| nbody                      | 87.0 ms                                                | 82.9 ms: 1.05x faster                                                    |
| thrift                     | 809 us                                                 | 772 us: 1.05x faster                                                     |
| xml_etree_parse            | 156 ms                                                 | 148 ms: 1.05x faster                                                     |
| fannkuch                   | 404 ms                                                 | 386 ms: 1.05x faster                                                     |
| scimark_monte_carlo        | 67.4 ms                                                | 64.6 ms: 1.04x faster                                                    |
| json_loads                 | 27.2 us                                                | 26.2 us: 1.04x faster                                                    |
| scimark_sor                | 124 ms                                                 | 120 ms: 1.03x faster                                                     |
| sqlalchemy_declarative     | 133 ms                                                 | 129 ms: 1.03x faster                                                     |
| 2to3                       | 267 ms                                                 | 260 ms: 1.03x faster                                                     |
| regex_compile              | 132 ms                                                 | 129 ms: 1.03x faster                                                     |
| async_tree_cpu_io_mixed    | 577 ms                                                 | 563 ms: 1.03x faster                                                     |
| connected_components       | 444 ms                                                 | 435 ms: 1.02x faster                                                     |
| pprint_safe_repr           | 728 ms                                                 | 715 ms: 1.02x faster                                                     |
| logging_format             | 6.40 us                                                | 6.28 us: 1.02x faster                                                    |
| float                      | 79.2 ms                                                | 78.0 ms: 1.02x faster                                                    |
| deltablue                  | 3.23 ms                                                | 3.19 ms: 1.01x faster                                                    |
| regex_v8                   | 26.2 ms                                                | 25.9 ms: 1.01x faster                                                    |
| scimark_lu                 | 113 ms                                                 | 112 ms: 1.01x faster                                                     |
| meteor_contest             | 109 ms                                                 | 108 ms: 1.01x faster                                                     |
| spectral_norm              | 115 ms                                                 | 114 ms: 1.01x faster                                                     |
| logging_silent             | 102 ns                                                 | 101 ns: 1.00x faster                                                     |
| asyncio_websockets         | 552 ms                                                 | 554 ms: 1.00x slower                                                     |
| pidigits                   | 186 ms                                                 | 188 ms: 1.01x slower                                                     |
| python_startup_no_site     | 6.96 ms                                                | 7.09 ms: 1.02x slower                                                    |
| typing_runtime_protocols   | 165 us                                                 | 168 us: 1.02x slower                                                     |
| sympy_str                  | 275 ms                                                 | 281 ms: 1.02x slower                                                     |
| sqlglot_transpile          | 1.58 ms                                                | 1.62 ms: 1.02x slower                                                    |
| chaos                      | 58.1 ms                                                | 59.6 ms: 1.03x slower                                                    |
| sympy_expand               | 463 ms                                                 | 477 ms: 1.03x slower                                                     |
| pickle_pure_python         | 310 us                                                 | 320 us: 1.03x slower                                                     |
| sqlglot_normalize          | 108 ms                                                 | 111 ms: 1.03x slower                                                     |
| python_startup             | 12.5 ms                                                | 12.9 ms: 1.03x slower                                                    |
| sympy_sum                  | 150 ms                                                 | 156 ms: 1.03x slower                                                     |
| sqlglot_optimize           | 53.7 ms                                                | 55.7 ms: 1.04x slower                                                    |
| sqlglot_parse              | 1.27 ms                                                | 1.32 ms: 1.04x slower                                                    |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 567 ms: 1.04x slower                                                     |
| sympy_integrate            | 19.9 ms                                                | 20.7 ms: 1.04x slower                                                    |
| comprehensions             | 16.5 us                                                | 17.2 us: 1.04x slower                                                    |
| html5lib                   | 64.2 ms                                                | 67.1 ms: 1.04x slower                                                    |
| dulwich_log                | 64.3 ms                                                | 67.4 ms: 1.05x slower                                                    |
| sphinx                     | 1.03 sec                                               | 1.09 sec: 1.05x slower                                                   |
| json_dumps                 | 10.6 ms                                                | 11.2 ms: 1.06x slower                                                    |
| async_generators           | 436 ms                                                 | 461 ms: 1.06x slower                                                     |
| bench_thread_pool          | 822 us                                                 | 874 us: 1.06x slower                                                     |
| raytrace                   | 267 ms                                                 | 284 ms: 1.07x slower                                                     |
| docutils                   | 2.59 sec                                               | 2.77 sec: 1.07x slower                                                   |
| async_tree_io_tg           | 857 ms                                                 | 917 ms: 1.07x slower                                                     |
| gc_traversal               | 4.37 ms                                                | 4.68 ms: 1.07x slower                                                    |
| genshi_text                | 23.5 ms                                                | 25.4 ms: 1.08x slower                                                    |
| async_tree_io              | 842 ms                                                 | 914 ms: 1.09x slower                                                     |
| create_gc_cycles           | 2.41 ms                                                | 2.67 ms: 1.11x slower                                                    |
| nqueens                    | 78.4 ms                                                | 88.1 ms: 1.12x slower                                                    |
| hexiom                     | 6.16 ms                                                | 7.04 ms: 1.14x slower                                                    |
| genshi_xml                 | 50.9 ms                                                | 59.6 ms: 1.17x slower                                                    |
| k_core                     | 2.35 sec                                               | 2.91 sec: 1.24x slower                                                   |
| generators                 | 29.0 ms                                                | 36.5 ms: 1.26x slower                                                    |
| bench_mp_pool              | 24.0 ms                                                | 79.3 ms: 3.31x slower                                                    |
| Geometric mean             | (ref)                                                  | 1.00x faster                                                             |

Benchmark hidden because not significant (9): async_tree_none_tg, pprint_pformat, logging_simple, xml_etree_iterparse, shortest_path, regex_dna, coverage, coroutines, sqlalchemy_imperative
Ignored benchmarks (4) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, gevent_hub, mypy2, tornado_http
Ignored benchmarks (4) of results/bm-20241122-3.14.0a2+-a8a4ed3-JIT/bm-20241122-linux-x86_64-brandtbucher-warmup_side_4096-3.14.0a2+-a8a4ed3.json: djangocms, many_optionals, sqlite_synth, subparsers

- Geometric mean (including insignificant results): 1.018x faster
# HPT report

- Reliability score: 94.40% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.03x
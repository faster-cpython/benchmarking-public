# Results vs. 3.13.0

- fork: brandtbucher
- ref: justin_no_externs
- machine: linux-x86_64
- commit hash: 64b198a
- commit date: 2024-10-25
- overall geometric mean: 1.027x slower
- HPT reliability: 99.98%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241025-linux-x86_64-brandtbucher-justin_no_externs-3.14.0a1+-64b198a |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 267 ms                                                 | 286 ms: 1.07x slower                                                      |
| docutils       | 2.59 sec                                               | 2.97 sec: 1.14x slower                                                    |
| html5lib       | 64.2 ms                                                | 67.5 ms: 1.05x slower                                                     |
| sphinx         | 1.03 sec                                               | 1.19 sec: 1.15x slower                                                    |
| tornado_http   | 92.4 ms                                                | 96.4 ms: 1.04x slower                                                     |
| Geometric mean | (ref)                                                  | 1.09x slower                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241025-linux-x86_64-brandtbucher-justin_no_externs-3.14.0a1+-64b198a |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 464 ms                                                 | 381 ms: 1.22x faster                                                      |
| async_tree_memoization     | 442 ms                                                 | 419 ms: 1.05x faster                                                      |
| async_tree_none            | 351 ms                                                 | 339 ms: 1.03x faster                                                      |
| asyncio_websockets         | 552 ms                                                 | 554 ms: 1.00x slower                                                      |
| coroutines                 | 22.7 ms                                                | 23.2 ms: 1.02x slower                                                     |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 566 ms: 1.04x slower                                                      |
| async_generators           | 436 ms                                                 | 458 ms: 1.05x slower                                                      |
| async_tree_io_tg           | 857 ms                                                 | 974 ms: 1.14x slower                                                      |
| Geometric mean             | (ref)                                                  | 1.00x faster                                                              |

Benchmark hidden because not significant (3): async_tree_cpu_io_mixed, async_tree_none_tg, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241025-linux-x86_64-brandtbucher-justin_no_externs-3.14.0a1+-64b198a |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| float          | 79.2 ms                                                | 78.6 ms: 1.01x faster                                                     |
| pidigits       | 186 ms                                                 | 187 ms: 1.00x slower                                                      |
| nbody          | 87.0 ms                                                | 87.6 ms: 1.01x slower                                                     |
| Geometric mean | (ref)                                                  | 1.00x slower                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241025-linux-x86_64-brandtbucher-justin_no_externs-3.14.0a1+-64b198a |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_v8       | 26.2 ms                                                | 24.7 ms: 1.06x faster                                                     |
| regex_effbot   | 3.73 ms                                                | 3.77 ms: 1.01x slower                                                     |
| regex_dna      | 218 ms                                                 | 222 ms: 1.02x slower                                                      |
| regex_compile  | 132 ms                                                 | 142 ms: 1.07x slower                                                      |
| Geometric mean | (ref)                                                  | 1.01x slower                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241025-linux-x86_64-brandtbucher-justin_no_externs-3.14.0a1+-64b198a |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| tomli_loads          | 2.14 sec                                               | 2.01 sec: 1.06x faster                                                    |
| xml_etree_generate   | 86.7 ms                                                | 82.4 ms: 1.05x faster                                                     |
| xml_etree_parse      | 156 ms                                                 | 148 ms: 1.05x faster                                                      |
| xml_etree_process    | 60.6 ms                                                | 58.0 ms: 1.05x faster                                                     |
| json_loads           | 27.2 us                                                | 27.1 us: 1.01x faster                                                     |
| xml_etree_iterparse  | 101 ms                                                 | 102 ms: 1.00x slower                                                      |
| pickle_pure_python   | 310 us                                                 | 326 us: 1.05x slower                                                      |
| unpickle_pure_python | 216 us                                                 | 226 us: 1.05x slower                                                      |
| json_dumps           | 10.6 ms                                                | 11.5 ms: 1.09x slower                                                     |
| Geometric mean       | (ref)                                                  | 1.00x faster                                                              |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241025-linux-x86_64-brandtbucher-justin_no_externs-3.14.0a1+-64b198a |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 12.5 ms                                                | 11.8 ms: 1.05x faster                                                     |
| python_startup_no_site | 6.96 ms                                                | 7.08 ms: 1.02x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.02x faster                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241025-linux-x86_64-brandtbucher-justin_no_externs-3.14.0a1+-64b198a |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako            | 11.1 ms                                                | 10.8 ms: 1.03x faster                                                     |
| django_template | 35.2 ms                                                | 36.6 ms: 1.04x slower                                                     |
| genshi_text     | 23.5 ms                                                | 26.5 ms: 1.13x slower                                                     |
| genshi_xml      | 50.9 ms                                                | 62.9 ms: 1.23x slower                                                     |
| Geometric mean  | (ref)                                                  | 1.09x slower                                                              |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241025-linux-x86_64-brandtbucher-justin_no_externs-3.14.0a1+-64b198a |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| deepcopy                   | 358 us                                                 | 283 us: 1.27x faster                                                      |
| deepcopy_memo              | 39.1 us                                                | 31.3 us: 1.25x faster                                                     |
| async_tree_memoization_tg  | 464 ms                                                 | 381 ms: 1.22x faster                                                      |
| deepcopy_reduce            | 3.20 us                                                | 2.88 us: 1.11x faster                                                     |
| richards_super             | 54.9 ms                                                | 49.7 ms: 1.10x faster                                                     |
| pathlib                    | 17.5 ms                                                | 16.1 ms: 1.09x faster                                                     |
| scimark_fft                | 364 ms                                                 | 336 ms: 1.08x faster                                                      |
| richards                   | 48.7 ms                                                | 45.3 ms: 1.07x faster                                                     |
| tomli_loads                | 2.14 sec                                               | 2.01 sec: 1.06x faster                                                    |
| regex_v8                   | 26.2 ms                                                | 24.7 ms: 1.06x faster                                                     |
| telco                      | 8.54 ms                                                | 8.04 ms: 1.06x faster                                                     |
| async_tree_memoization     | 442 ms                                                 | 419 ms: 1.05x faster                                                      |
| python_startup             | 12.5 ms                                                | 11.8 ms: 1.05x faster                                                     |
| xml_etree_generate         | 86.7 ms                                                | 82.4 ms: 1.05x faster                                                     |
| json                       | 5.36 ms                                                | 5.11 ms: 1.05x faster                                                     |
| xml_etree_parse            | 156 ms                                                 | 148 ms: 1.05x faster                                                      |
| xml_etree_process          | 60.6 ms                                                | 58.0 ms: 1.05x faster                                                     |
| logging_format             | 6.40 us                                                | 6.13 us: 1.04x faster                                                     |
| async_tree_none            | 351 ms                                                 | 339 ms: 1.03x faster                                                      |
| crypto_pyaes               | 75.3 ms                                                | 73.0 ms: 1.03x faster                                                     |
| go                         | 144 ms                                                 | 140 ms: 1.03x faster                                                      |
| mako                       | 11.1 ms                                                | 10.8 ms: 1.03x faster                                                     |
| logging_simple             | 5.72 us                                                | 5.60 us: 1.02x faster                                                     |
| pycparser                  | 1.20 sec                                               | 1.18 sec: 1.02x faster                                                    |
| thrift                     | 809 us                                                 | 796 us: 1.02x faster                                                      |
| bpe_tokeniser              | 4.75 sec                                               | 4.67 sec: 1.02x faster                                                    |
| float                      | 79.2 ms                                                | 78.6 ms: 1.01x faster                                                     |
| json_loads                 | 27.2 us                                                | 27.1 us: 1.01x faster                                                     |
| pidigits                   | 186 ms                                                 | 187 ms: 1.00x slower                                                      |
| xml_etree_iterparse        | 101 ms                                                 | 102 ms: 1.00x slower                                                      |
| asyncio_websockets         | 552 ms                                                 | 554 ms: 1.00x slower                                                      |
| nbody                      | 87.0 ms                                                | 87.6 ms: 1.01x slower                                                     |
| regex_effbot               | 3.73 ms                                                | 3.77 ms: 1.01x slower                                                     |
| mdp                        | 2.72 sec                                               | 2.75 sec: 1.01x slower                                                    |
| python_startup_no_site     | 6.96 ms                                                | 7.08 ms: 1.02x slower                                                     |
| regex_dna                  | 218 ms                                                 | 222 ms: 1.02x slower                                                      |
| pyflate                    | 471 ms                                                 | 480 ms: 1.02x slower                                                      |
| coroutines                 | 22.7 ms                                                | 23.2 ms: 1.02x slower                                                     |
| scimark_lu                 | 113 ms                                                 | 116 ms: 1.03x slower                                                      |
| scimark_sor                | 124 ms                                                 | 127 ms: 1.03x slower                                                      |
| scimark_monte_carlo        | 67.4 ms                                                | 69.6 ms: 1.03x slower                                                     |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 566 ms: 1.04x slower                                                      |
| meteor_contest             | 109 ms                                                 | 113 ms: 1.04x slower                                                      |
| django_template            | 35.2 ms                                                | 36.6 ms: 1.04x slower                                                     |
| pprint_pformat             | 1.49 sec                                               | 1.56 sec: 1.04x slower                                                    |
| tornado_http               | 92.4 ms                                                | 96.4 ms: 1.04x slower                                                     |
| pickle_pure_python         | 310 us                                                 | 326 us: 1.05x slower                                                      |
| unpickle_pure_python       | 216 us                                                 | 226 us: 1.05x slower                                                      |
| async_generators           | 436 ms                                                 | 458 ms: 1.05x slower                                                      |
| pylint                     | 313 ms                                                 | 329 ms: 1.05x slower                                                      |
| html5lib                   | 64.2 ms                                                | 67.5 ms: 1.05x slower                                                     |
| pprint_safe_repr           | 728 ms                                                 | 766 ms: 1.05x slower                                                      |
| typing_runtime_protocols   | 165 us                                                 | 173 us: 1.05x slower                                                      |
| dulwich_log                | 64.3 ms                                                | 68.5 ms: 1.06x slower                                                     |
| sqlalchemy_imperative      | 17.1 ms                                                | 18.2 ms: 1.06x slower                                                     |
| spectral_norm              | 115 ms                                                 | 123 ms: 1.07x slower                                                      |
| deltablue                  | 3.23 ms                                                | 3.44 ms: 1.07x slower                                                     |
| sqlglot_parse              | 1.27 ms                                                | 1.36 ms: 1.07x slower                                                     |
| 2to3                       | 267 ms                                                 | 286 ms: 1.07x slower                                                      |
| regex_compile              | 132 ms                                                 | 142 ms: 1.07x slower                                                      |
| json_dumps                 | 10.6 ms                                                | 11.5 ms: 1.09x slower                                                     |
| sqlglot_transpile          | 1.58 ms                                                | 1.72 ms: 1.09x slower                                                     |
| gc_traversal               | 4.37 ms                                                | 4.75 ms: 1.09x slower                                                     |
| bench_thread_pool          | 822 us                                                 | 893 us: 1.09x slower                                                      |
| chaos                      | 58.1 ms                                                | 63.2 ms: 1.09x slower                                                     |
| logging_silent             | 102 ns                                                 | 111 ns: 1.09x slower                                                      |
| sqlglot_normalize          | 108 ms                                                 | 118 ms: 1.10x slower                                                      |
| create_gc_cycles           | 2.41 ms                                                | 2.68 ms: 1.11x slower                                                     |
| sqlalchemy_declarative     | 133 ms                                                 | 148 ms: 1.11x slower                                                      |
| raytrace                   | 267 ms                                                 | 297 ms: 1.11x slower                                                      |
| sympy_expand               | 463 ms                                                 | 516 ms: 1.11x slower                                                      |
| genshi_text                | 23.5 ms                                                | 26.5 ms: 1.13x slower                                                     |
| sympy_str                  | 275 ms                                                 | 312 ms: 1.14x slower                                                      |
| async_tree_io_tg           | 857 ms                                                 | 974 ms: 1.14x slower                                                      |
| comprehensions             | 16.5 us                                                | 18.8 us: 1.14x slower                                                     |
| docutils                   | 2.59 sec                                               | 2.97 sec: 1.14x slower                                                    |
| sqlglot_optimize           | 53.7 ms                                                | 61.6 ms: 1.15x slower                                                     |
| sphinx                     | 1.03 sec                                               | 1.19 sec: 1.15x slower                                                    |
| nqueens                    | 78.4 ms                                                | 93.2 ms: 1.19x slower                                                     |
| sympy_sum                  | 150 ms                                                 | 180 ms: 1.20x slower                                                      |
| sympy_integrate            | 19.9 ms                                                | 24.0 ms: 1.20x slower                                                     |
| hexiom                     | 6.16 ms                                                | 7.60 ms: 1.23x slower                                                     |
| genshi_xml                 | 50.9 ms                                                | 62.9 ms: 1.23x slower                                                     |
| generators                 | 29.0 ms                                                | 37.6 ms: 1.30x slower                                                     |
| bench_mp_pool              | 24.0 ms                                                | 84.7 ms: 3.53x slower                                                     |
| Geometric mean             | (ref)                                                  | 1.04x slower                                                              |

Benchmark hidden because not significant (6): scimark_sparse_mat_mult, coverage, async_tree_cpu_io_mixed, async_tree_none_tg, fannkuch, async_tree_io
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path

- Geometric mean (including insignificant results): 1.027x slower
# HPT report

- Reliability score: 99.98% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.07x
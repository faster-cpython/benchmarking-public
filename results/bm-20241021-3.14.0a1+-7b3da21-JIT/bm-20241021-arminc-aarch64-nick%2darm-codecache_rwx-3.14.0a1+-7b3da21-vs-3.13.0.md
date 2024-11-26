# Results vs. 3.13.0

- fork: nick-arm
- ref: codecache_rwx
- machine: linux-aarch64
- commit hash: 7b3da21
- commit date: 2024-10-21
- overall geometric mean: 1.081x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x slower
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241021-arminc-aarch64-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|----------------|:--------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 304 ms                                                   | 363 ms: 1.20x slower                                                  |
| docutils       | 2.89 sec                                                 | 3.48 sec: 1.20x slower                                                |
| html5lib       | 66.4 ms                                                  | 71.7 ms: 1.08x slower                                                 |
| sphinx         | 1.17 sec                                                 | 1.38 sec: 1.18x slower                                                |
| tornado_http   | 128 ms                                                   | 143 ms: 1.12x slower                                                  |
| Geometric mean | (ref)                                                    | 1.16x slower                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241021-arminc-aarch64-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|----------------------------|:--------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_memoization_tg  | 649 ms                                                   | 539 ms: 1.20x faster                                                  |
| async_tree_memoization     | 651 ms                                                   | 604 ms: 1.08x faster                                                  |
| async_tree_none            | 497 ms                                                   | 473 ms: 1.05x faster                                                  |
| async_tree_none_tg         | 470 ms                                                   | 448 ms: 1.05x faster                                                  |
| async_tree_cpu_io_mixed_tg | 769 ms                                                   | 744 ms: 1.03x faster                                                  |
| coroutines                 | 28.5 ms                                                  | 28.7 ms: 1.01x slower                                                 |
| async_generators           | 489 ms                                                   | 506 ms: 1.03x slower                                                  |
| async_tree_io              | 1.11 sec                                                 | 1.20 sec: 1.08x slower                                                |
| async_tree_io_tg           | 1.13 sec                                                 | 1.26 sec: 1.12x slower                                                |
| Geometric mean             | (ref)                                                    | 1.02x faster                                                          |

Benchmark hidden because not significant (2): async_tree_cpu_io_mixed, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241021-arminc-aarch64-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|----------------|:--------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 93.3 ms                                                  | 97.0 ms: 1.04x slower                                                 |
| Geometric mean | (ref)                                                    | 1.01x slower                                                          |

Benchmark hidden because not significant (2): nbody, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241021-arminc-aarch64-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|----------------|:--------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_v8       | 31.8 ms                                                  | 31.0 ms: 1.03x faster                                                 |
| regex_compile  | 127 ms                                                   | 162 ms: 1.28x slower                                                  |
| Geometric mean | (ref)                                                    | 1.06x slower                                                          |

Benchmark hidden because not significant (2): regex_dna, regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241021-arminc-aarch64-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|----------------------|:--------------------------------------------------------:|:---------------------------------------------------------------------:|
| xml_etree_parse      | 197 ms                                                   | 188 ms: 1.04x faster                                                  |
| json_loads           | 31.7 us                                                  | 31.3 us: 1.01x faster                                                 |
| xml_etree_iterparse  | 149 ms                                                   | 153 ms: 1.02x slower                                                  |
| tomli_loads          | 2.54 sec                                                 | 2.61 sec: 1.03x slower                                                |
| json_dumps           | 13.6 ms                                                  | 14.3 ms: 1.06x slower                                                 |
| unpickle_pure_python | 251 us                                                   | 267 us: 1.06x slower                                                  |
| pickle_pure_python   | 357 us                                                   | 392 us: 1.10x slower                                                  |
| Geometric mean       | (ref)                                                    | 1.02x slower                                                          |

Benchmark hidden because not significant (2): xml_etree_generate, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241021-arminc-aarch64-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|----------------|:--------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup | 15.4 ms                                                  | 14.5 ms: 1.06x faster                                                 |
| Geometric mean | (ref)                                                    | 1.03x faster                                                          |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241021-arminc-aarch64-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|-----------------|:--------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 13.4 ms                                                  | 13.2 ms: 1.02x faster                                                 |
| genshi_text     | 27.7 ms                                                  | 32.6 ms: 1.17x slower                                                 |
| django_template | 41.6 ms                                                  | 50.6 ms: 1.22x slower                                                 |
| genshi_xml      | 60.3 ms                                                  | 78.6 ms: 1.30x slower                                                 |
| Geometric mean  | (ref)                                                    | 1.16x slower                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241021-arminc-aarch64-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|----------------------------|:--------------------------------------------------------:|:---------------------------------------------------------------------:|
| deepcopy_memo              | 50.4 us                                                  | 38.9 us: 1.29x faster                                                 |
| async_tree_memoization_tg  | 649 ms                                                   | 539 ms: 1.20x faster                                                  |
| deepcopy                   | 447 us                                                   | 379 us: 1.18x faster                                                  |
| async_tree_memoization     | 651 ms                                                   | 604 ms: 1.08x faster                                                  |
| python_startup             | 15.4 ms                                                  | 14.5 ms: 1.06x faster                                                 |
| deepcopy_reduce            | 4.07 us                                                  | 3.87 us: 1.05x faster                                                 |
| async_tree_none            | 497 ms                                                   | 473 ms: 1.05x faster                                                  |
| async_tree_none_tg         | 470 ms                                                   | 448 ms: 1.05x faster                                                  |
| scimark_sor                | 160 ms                                                   | 153 ms: 1.04x faster                                                  |
| xml_etree_parse            | 197 ms                                                   | 188 ms: 1.04x faster                                                  |
| pathlib                    | 22.7 ms                                                  | 21.8 ms: 1.04x faster                                                 |
| async_tree_cpu_io_mixed_tg | 769 ms                                                   | 744 ms: 1.03x faster                                                  |
| thrift                     | 968 us                                                   | 941 us: 1.03x faster                                                  |
| regex_v8                   | 31.8 ms                                                  | 31.0 ms: 1.03x faster                                                 |
| telco                      | 9.74 ms                                                  | 9.49 ms: 1.03x faster                                                 |
| mako                       | 13.4 ms                                                  | 13.2 ms: 1.02x faster                                                 |
| json_loads                 | 31.7 us                                                  | 31.3 us: 1.01x faster                                                 |
| coroutines                 | 28.5 ms                                                  | 28.7 ms: 1.01x slower                                                 |
| scimark_fft                | 447 ms                                                   | 454 ms: 1.02x slower                                                  |
| logging_format             | 7.82 us                                                  | 7.99 us: 1.02x slower                                                 |
| bpe_tokeniser              | 5.87 sec                                                 | 6.00 sec: 1.02x slower                                                |
| xml_etree_iterparse        | 149 ms                                                   | 153 ms: 1.02x slower                                                  |
| tomli_loads                | 2.54 sec                                                 | 2.61 sec: 1.03x slower                                                |
| async_generators           | 489 ms                                                   | 506 ms: 1.03x slower                                                  |
| mdp                        | 3.34 sec                                                 | 3.47 sec: 1.04x slower                                                |
| float                      | 93.3 ms                                                  | 97.0 ms: 1.04x slower                                                 |
| logging_simple             | 7.07 us                                                  | 7.38 us: 1.04x slower                                                 |
| json_dumps                 | 13.6 ms                                                  | 14.3 ms: 1.06x slower                                                 |
| unpickle_pure_python       | 251 us                                                   | 267 us: 1.06x slower                                                  |
| richards_super             | 60.1 ms                                                  | 63.9 ms: 1.06x slower                                                 |
| bench_thread_pool          | 1.27 ms                                                  | 1.36 ms: 1.07x slower                                                 |
| scimark_monte_carlo        | 83.6 ms                                                  | 90.0 ms: 1.08x slower                                                 |
| async_tree_io              | 1.11 sec                                                 | 1.20 sec: 1.08x slower                                                |
| html5lib                   | 66.4 ms                                                  | 71.7 ms: 1.08x slower                                                 |
| crypto_pyaes               | 83.7 ms                                                  | 90.5 ms: 1.08x slower                                                 |
| typing_runtime_protocols   | 193 us                                                   | 210 us: 1.09x slower                                                  |
| create_gc_cycles           | 3.35 ms                                                  | 3.64 ms: 1.09x slower                                                 |
| gc_traversal               | 5.77 ms                                                  | 6.29 ms: 1.09x slower                                                 |
| meteor_contest             | 114 ms                                                   | 124 ms: 1.09x slower                                                  |
| scimark_lu                 | 139 ms                                                   | 152 ms: 1.09x slower                                                  |
| pickle_pure_python         | 357 us                                                   | 392 us: 1.10x slower                                                  |
| go                         | 160 ms                                                   | 177 ms: 1.11x slower                                                  |
| spectral_norm              | 143 ms                                                   | 159 ms: 1.11x slower                                                  |
| richards                   | 53.6 ms                                                  | 59.7 ms: 1.11x slower                                                 |
| fannkuch                   | 461 ms                                                   | 513 ms: 1.11x slower                                                  |
| async_tree_io_tg           | 1.13 sec                                                 | 1.26 sec: 1.12x slower                                                |
| scimark_sparse_mat_mult    | 6.51 ms                                                  | 7.27 ms: 1.12x slower                                                 |
| tornado_http               | 128 ms                                                   | 143 ms: 1.12x slower                                                  |
| pyflate                    | 556 ms                                                   | 636 ms: 1.14x slower                                                  |
| pycparser                  | 1.27 sec                                                 | 1.48 sec: 1.16x slower                                                |
| raytrace                   | 300 ms                                                   | 351 ms: 1.17x slower                                                  |
| deltablue                  | 3.82 ms                                                  | 4.49 ms: 1.17x slower                                                 |
| genshi_text                | 27.7 ms                                                  | 32.6 ms: 1.17x slower                                                 |
| sqlglot_normalize          | 127 ms                                                   | 150 ms: 1.18x slower                                                  |
| sphinx                     | 1.17 sec                                                 | 1.38 sec: 1.18x slower                                                |
| 2to3                       | 304 ms                                                   | 363 ms: 1.20x slower                                                  |
| docutils                   | 2.89 sec                                                 | 3.48 sec: 1.20x slower                                                |
| comprehensions             | 20.4 us                                                  | 24.6 us: 1.21x slower                                                 |
| django_template            | 41.6 ms                                                  | 50.6 ms: 1.22x slower                                                 |
| sqlglot_parse              | 1.38 ms                                                  | 1.68 ms: 1.22x slower                                                 |
| sympy_expand               | 457 ms                                                   | 563 ms: 1.23x slower                                                  |
| sqlglot_optimize           | 62.2 ms                                                  | 77.0 ms: 1.24x slower                                                 |
| sqlglot_transpile          | 1.73 ms                                                  | 2.15 ms: 1.24x slower                                                 |
| chaos                      | 68.0 ms                                                  | 85.4 ms: 1.26x slower                                                 |
| nqueens                    | 100 ms                                                   | 126 ms: 1.26x slower                                                  |
| regex_compile              | 127 ms                                                   | 162 ms: 1.28x slower                                                  |
| pylint                     | 342 ms                                                   | 442 ms: 1.29x slower                                                  |
| sympy_str                  | 264 ms                                                   | 343 ms: 1.30x slower                                                  |
| genshi_xml                 | 60.3 ms                                                  | 78.6 ms: 1.30x slower                                                 |
| pprint_safe_repr           | 926 ms                                                   | 1.22 sec: 1.32x slower                                                |
| pprint_pformat             | 1.90 sec                                                 | 2.58 sec: 1.36x slower                                                |
| hexiom                     | 7.11 ms                                                  | 9.81 ms: 1.38x slower                                                 |
| sympy_integrate            | 20.8 ms                                                  | 28.9 ms: 1.39x slower                                                 |
| sympy_sum                  | 144 ms                                                   | 205 ms: 1.43x slower                                                  |
| generators                 | 37.6 ms                                                  | 58.8 ms: 1.56x slower                                                 |
| bench_mp_pool              | 7.68 ms                                                  | 4.29 sec: 558.27x slower                                              |
| Geometric mean             | (ref)                                                    | 1.17x slower                                                          |

Benchmark hidden because not significant (12): json, regex_dna, nbody, async_tree_cpu_io_mixed, asyncio_websockets, logging_silent, python_startup_no_site, xml_etree_generate, pidigits, regex_effbot, coverage, xml_etree_process
Ignored benchmarks (8) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (1) of results/bm-20241021-3.14.0a1+-7b3da21-JIT/bm-20241021-arminc-aarch64-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21.json: dulwich_log

- Geometric mean (including insignificant results): 1.081x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.05x
- 95% likely to have a slowdown of 1.04x
- 99% likely to have a slowdown of 1.03x

# Memory
- memory change: 1.09x
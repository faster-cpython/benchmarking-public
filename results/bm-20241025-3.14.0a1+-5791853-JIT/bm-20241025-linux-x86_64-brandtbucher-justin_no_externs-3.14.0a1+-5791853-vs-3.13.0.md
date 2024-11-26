# Results vs. 3.13.0

- fork: brandtbucher
- ref: justin_no_externs
- machine: linux-x86_64
- commit hash: 5791853
- commit date: 2024-10-25
- overall geometric mean: 1.017x slower
- HPT reliability: 99.51%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241025-linux-x86_64-brandtbucher-justin_no_externs-3.14.0a1+-5791853 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 267 ms                                                 | 283 ms: 1.06x slower                                                      |
| docutils       | 2.59 sec                                               | 2.94 sec: 1.13x slower                                                    |
| html5lib       | 64.2 ms                                                | 66.0 ms: 1.03x slower                                                     |
| sphinx         | 1.03 sec                                               | 1.18 sec: 1.14x slower                                                    |
| tornado_http   | 92.4 ms                                                | 95.0 ms: 1.03x slower                                                     |
| Geometric mean | (ref)                                                  | 1.08x slower                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241025-linux-x86_64-brandtbucher-justin_no_externs-3.14.0a1+-5791853 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 464 ms                                                 | 381 ms: 1.22x faster                                                      |
| async_tree_memoization     | 442 ms                                                 | 418 ms: 1.06x faster                                                      |
| async_tree_none            | 351 ms                                                 | 341 ms: 1.03x faster                                                      |
| coroutines                 | 22.7 ms                                                | 22.9 ms: 1.01x slower                                                     |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 565 ms: 1.03x slower                                                      |
| async_generators           | 436 ms                                                 | 454 ms: 1.04x slower                                                      |
| async_tree_io_tg           | 857 ms                                                 | 975 ms: 1.14x slower                                                      |
| Geometric mean             | (ref)                                                  | 1.00x faster                                                              |

Benchmark hidden because not significant (4): asyncio_websockets, async_tree_none_tg, async_tree_cpu_io_mixed, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241025-linux-x86_64-brandtbucher-justin_no_externs-3.14.0a1+-5791853 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| float          | 79.2 ms                                                | 77.8 ms: 1.02x faster                                                     |
| pidigits       | 186 ms                                                 | 187 ms: 1.01x slower                                                      |
| nbody          | 87.0 ms                                                | 89.2 ms: 1.03x slower                                                     |
| Geometric mean | (ref)                                                  | 1.00x slower                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241025-linux-x86_64-brandtbucher-justin_no_externs-3.14.0a1+-5791853 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_v8       | 26.2 ms                                                | 24.9 ms: 1.05x faster                                                     |
| regex_effbot   | 3.73 ms                                                | 3.86 ms: 1.03x slower                                                     |
| regex_compile  | 132 ms                                                 | 141 ms: 1.07x slower                                                      |
| Geometric mean | (ref)                                                  | 1.01x slower                                                              |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241025-linux-x86_64-brandtbucher-justin_no_externs-3.14.0a1+-5791853 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| tomli_loads          | 2.14 sec                                               | 1.97 sec: 1.09x faster                                                    |
| xml_etree_generate   | 86.7 ms                                                | 80.7 ms: 1.07x faster                                                     |
| xml_etree_process    | 60.6 ms                                                | 57.4 ms: 1.06x faster                                                     |
| xml_etree_parse      | 156 ms                                                 | 148 ms: 1.05x faster                                                      |
| json_loads           | 27.2 us                                                | 26.7 us: 1.02x faster                                                     |
| pickle_pure_python   | 310 us                                                 | 321 us: 1.03x slower                                                      |
| unpickle_pure_python | 216 us                                                 | 223 us: 1.04x slower                                                      |
| json_dumps           | 10.6 ms                                                | 11.1 ms: 1.05x slower                                                     |
| Geometric mean       | (ref)                                                  | 1.02x faster                                                              |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241025-linux-x86_64-brandtbucher-justin_no_externs-3.14.0a1+-5791853 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 12.5 ms                                                | 11.8 ms: 1.05x faster                                                     |
| python_startup_no_site | 6.96 ms                                                | 7.09 ms: 1.02x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.02x faster                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241025-linux-x86_64-brandtbucher-justin_no_externs-3.14.0a1+-5791853 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako            | 11.1 ms                                                | 10.5 ms: 1.05x faster                                                     |
| django_template | 35.2 ms                                                | 36.7 ms: 1.04x slower                                                     |
| genshi_text     | 23.5 ms                                                | 25.7 ms: 1.09x slower                                                     |
| genshi_xml      | 50.9 ms                                                | 60.5 ms: 1.19x slower                                                     |
| Geometric mean  | (ref)                                                  | 1.06x slower                                                              |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241025-linux-x86_64-brandtbucher-justin_no_externs-3.14.0a1+-5791853 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| deepcopy                   | 358 us                                                 | 278 us: 1.29x faster                                                      |
| deepcopy_memo              | 39.1 us                                                | 31.8 us: 1.23x faster                                                     |
| async_tree_memoization_tg  | 464 ms                                                 | 381 ms: 1.22x faster                                                      |
| richards_super             | 54.9 ms                                                | 48.5 ms: 1.13x faster                                                     |
| deepcopy_reduce            | 3.20 us                                                | 2.84 us: 1.13x faster                                                     |
| scimark_fft                | 364 ms                                                 | 333 ms: 1.09x faster                                                      |
| pathlib                    | 17.5 ms                                                | 16.1 ms: 1.09x faster                                                     |
| richards                   | 48.7 ms                                                | 44.8 ms: 1.09x faster                                                     |
| tomli_loads                | 2.14 sec                                               | 1.97 sec: 1.09x faster                                                    |
| xml_etree_generate         | 86.7 ms                                                | 80.7 ms: 1.07x faster                                                     |
| json                       | 5.36 ms                                                | 5.00 ms: 1.07x faster                                                     |
| telco                      | 8.54 ms                                                | 7.99 ms: 1.07x faster                                                     |
| scimark_sparse_mat_mult    | 5.04 ms                                                | 4.76 ms: 1.06x faster                                                     |
| async_tree_memoization     | 442 ms                                                 | 418 ms: 1.06x faster                                                      |
| xml_etree_process          | 60.6 ms                                                | 57.4 ms: 1.06x faster                                                     |
| python_startup             | 12.5 ms                                                | 11.8 ms: 1.05x faster                                                     |
| mako                       | 11.1 ms                                                | 10.5 ms: 1.05x faster                                                     |
| xml_etree_parse            | 156 ms                                                 | 148 ms: 1.05x faster                                                      |
| regex_v8                   | 26.2 ms                                                | 24.9 ms: 1.05x faster                                                     |
| crypto_pyaes               | 75.3 ms                                                | 72.6 ms: 1.04x faster                                                     |
| logging_format             | 6.40 us                                                | 6.18 us: 1.03x faster                                                     |
| go                         | 144 ms                                                 | 139 ms: 1.03x faster                                                      |
| mdp                        | 2.72 sec                                               | 2.64 sec: 1.03x faster                                                    |
| pyflate                    | 471 ms                                                 | 457 ms: 1.03x faster                                                      |
| async_tree_none            | 351 ms                                                 | 341 ms: 1.03x faster                                                      |
| bpe_tokeniser              | 4.75 sec                                               | 4.63 sec: 1.02x faster                                                    |
| json_loads                 | 27.2 us                                                | 26.7 us: 1.02x faster                                                     |
| float                      | 79.2 ms                                                | 77.8 ms: 1.02x faster                                                     |
| logging_simple             | 5.72 us                                                | 5.62 us: 1.02x faster                                                     |
| pycparser                  | 1.20 sec                                               | 1.18 sec: 1.01x faster                                                    |
| thrift                     | 809 us                                                 | 801 us: 1.01x faster                                                      |
| pidigits                   | 186 ms                                                 | 187 ms: 1.01x slower                                                      |
| scimark_monte_carlo        | 67.4 ms                                                | 67.9 ms: 1.01x slower                                                     |
| coroutines                 | 22.7 ms                                                | 22.9 ms: 1.01x slower                                                     |
| pprint_safe_repr           | 728 ms                                                 | 738 ms: 1.01x slower                                                      |
| fannkuch                   | 404 ms                                                 | 411 ms: 1.02x slower                                                      |
| python_startup_no_site     | 6.96 ms                                                | 7.09 ms: 1.02x slower                                                     |
| scimark_sor                | 124 ms                                                 | 126 ms: 1.02x slower                                                      |
| scimark_lu                 | 113 ms                                                 | 115 ms: 1.02x slower                                                      |
| nbody                      | 87.0 ms                                                | 89.2 ms: 1.03x slower                                                     |
| meteor_contest             | 109 ms                                                 | 112 ms: 1.03x slower                                                      |
| html5lib                   | 64.2 ms                                                | 66.0 ms: 1.03x slower                                                     |
| tornado_http               | 92.4 ms                                                | 95.0 ms: 1.03x slower                                                     |
| pprint_pformat             | 1.49 sec                                               | 1.54 sec: 1.03x slower                                                    |
| pickle_pure_python         | 310 us                                                 | 321 us: 1.03x slower                                                      |
| regex_effbot               | 3.73 ms                                                | 3.86 ms: 1.03x slower                                                     |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 565 ms: 1.03x slower                                                      |
| unpickle_pure_python       | 216 us                                                 | 223 us: 1.04x slower                                                      |
| async_generators           | 436 ms                                                 | 454 ms: 1.04x slower                                                      |
| django_template            | 35.2 ms                                                | 36.7 ms: 1.04x slower                                                     |
| sqlalchemy_imperative      | 17.1 ms                                                | 17.9 ms: 1.05x slower                                                     |
| spectral_norm              | 115 ms                                                 | 121 ms: 1.05x slower                                                      |
| json_dumps                 | 10.6 ms                                                | 11.1 ms: 1.05x slower                                                     |
| typing_runtime_protocols   | 165 us                                                 | 173 us: 1.05x slower                                                      |
| dulwich_log                | 64.3 ms                                                | 67.7 ms: 1.05x slower                                                     |
| 2to3                       | 267 ms                                                 | 283 ms: 1.06x slower                                                      |
| deltablue                  | 3.23 ms                                                | 3.44 ms: 1.07x slower                                                     |
| chaos                      | 58.1 ms                                                | 61.9 ms: 1.07x slower                                                     |
| sqlglot_parse              | 1.27 ms                                                | 1.36 ms: 1.07x slower                                                     |
| regex_compile              | 132 ms                                                 | 141 ms: 1.07x slower                                                      |
| sqlglot_transpile          | 1.58 ms                                                | 1.71 ms: 1.08x slower                                                     |
| gc_traversal               | 4.37 ms                                                | 4.74 ms: 1.09x slower                                                     |
| bench_thread_pool          | 822 us                                                 | 893 us: 1.09x slower                                                      |
| genshi_text                | 23.5 ms                                                | 25.7 ms: 1.09x slower                                                     |
| sqlglot_normalize          | 108 ms                                                 | 118 ms: 1.09x slower                                                      |
| sympy_expand               | 463 ms                                                 | 507 ms: 1.09x slower                                                      |
| comprehensions             | 16.5 us                                                | 18.0 us: 1.10x slower                                                     |
| logging_silent             | 102 ns                                                 | 112 ns: 1.10x slower                                                      |
| sqlalchemy_declarative     | 133 ms                                                 | 147 ms: 1.10x slower                                                      |
| raytrace                   | 267 ms                                                 | 295 ms: 1.11x slower                                                      |
| create_gc_cycles           | 2.41 ms                                                | 2.67 ms: 1.11x slower                                                     |
| sympy_str                  | 275 ms                                                 | 306 ms: 1.11x slower                                                      |
| sqlglot_optimize           | 53.7 ms                                                | 60.8 ms: 1.13x slower                                                     |
| docutils                   | 2.59 sec                                               | 2.94 sec: 1.13x slower                                                    |
| async_tree_io_tg           | 857 ms                                                 | 975 ms: 1.14x slower                                                      |
| sphinx                     | 1.03 sec                                               | 1.18 sec: 1.14x slower                                                    |
| sympy_sum                  | 150 ms                                                 | 178 ms: 1.18x slower                                                      |
| genshi_xml                 | 50.9 ms                                                | 60.5 ms: 1.19x slower                                                     |
| sympy_integrate            | 19.9 ms                                                | 23.8 ms: 1.19x slower                                                     |
| nqueens                    | 78.4 ms                                                | 93.8 ms: 1.20x slower                                                     |
| hexiom                     | 6.16 ms                                                | 7.45 ms: 1.21x slower                                                     |
| generators                 | 29.0 ms                                                | 36.4 ms: 1.26x slower                                                     |
| bench_mp_pool              | 24.0 ms                                                | 84.3 ms: 3.51x slower                                                     |
| Geometric mean             | (ref)                                                  | 1.03x slower                                                              |

Benchmark hidden because not significant (8): coverage, regex_dna, asyncio_websockets, xml_etree_iterparse, async_tree_none_tg, async_tree_cpu_io_mixed, async_tree_io, pylint
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path

- Geometric mean (including insignificant results): 1.017x slower
# HPT report

- Reliability score: 99.51% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.07x
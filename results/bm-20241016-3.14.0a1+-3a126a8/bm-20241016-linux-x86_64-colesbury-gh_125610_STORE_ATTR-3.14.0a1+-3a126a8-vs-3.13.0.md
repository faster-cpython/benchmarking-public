# Results vs. 3.13.0

- fork: colesbury
- ref: gh_125610_STORE_ATTR
- machine: linux-x86_64
- commit hash: 3a126a8
- commit date: 2024-10-16
- overall geometric mean: 1.018x faster
- HPT reliability: 96.60%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241016-linux-x86_64-colesbury-gh_125610_STORE_ATTR-3.14.0a1+-3a126a8 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 267 ms                                                 | 254 ms: 1.05x faster                                                      |
| docutils       | 2.59 sec                                               | 2.64 sec: 1.02x slower                                                    |
| html5lib       | 64.2 ms                                                | 63.0 ms: 1.02x faster                                                     |
| tornado_http   | 92.4 ms                                                | 90.2 ms: 1.02x faster                                                     |
| Geometric mean | (ref)                                                  | 1.01x faster                                                              |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241016-linux-x86_64-colesbury-gh_125610_STORE_ATTR-3.14.0a1+-3a126a8 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 464 ms                                                 | 381 ms: 1.22x faster                                                      |
| async_tree_none            | 351 ms                                                 | 328 ms: 1.07x faster                                                      |
| async_tree_memoization     | 442 ms                                                 | 415 ms: 1.06x faster                                                      |
| async_generators           | 436 ms                                                 | 434 ms: 1.00x faster                                                      |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 564 ms: 1.03x slower                                                      |
| coroutines                 | 22.7 ms                                                | 23.6 ms: 1.04x slower                                                     |
| async_tree_io_tg           | 857 ms                                                 | 975 ms: 1.14x slower                                                      |
| Geometric mean             | (ref)                                                  | 1.01x faster                                                              |

Benchmark hidden because not significant (4): async_tree_cpu_io_mixed, async_tree_none_tg, asyncio_websockets, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241016-linux-x86_64-colesbury-gh_125610_STORE_ATTR-3.14.0a1+-3a126a8 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| float          | 79.2 ms                                                | 78.7 ms: 1.01x faster                                                     |
| pidigits       | 186 ms                                                 | 187 ms: 1.01x slower                                                      |
| nbody          | 87.0 ms                                                | 89.3 ms: 1.03x slower                                                     |
| Geometric mean | (ref)                                                  | 1.01x slower                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241016-linux-x86_64-colesbury-gh_125610_STORE_ATTR-3.14.0a1+-3a126a8 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_v8       | 26.2 ms                                                | 24.6 ms: 1.06x faster                                                     |
| regex_dna      | 218 ms                                                 | 210 ms: 1.04x faster                                                      |
| regex_effbot   | 3.73 ms                                                | 3.61 ms: 1.03x faster                                                     |
| regex_compile  | 132 ms                                                 | 129 ms: 1.03x faster                                                      |
| Geometric mean | (ref)                                                  | 1.04x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241016-linux-x86_64-colesbury-gh_125610_STORE_ATTR-3.14.0a1+-3a126a8 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| tomli_loads          | 2.14 sec                                               | 2.09 sec: 1.03x faster                                                    |
| xml_etree_process    | 60.6 ms                                                | 59.6 ms: 1.02x faster                                                     |
| json_loads           | 27.2 us                                                | 27.0 us: 1.01x faster                                                     |
| xml_etree_generate   | 86.7 ms                                                | 86.1 ms: 1.01x faster                                                     |
| pickle_pure_python   | 310 us                                                 | 309 us: 1.01x faster                                                      |
| unpickle_pure_python | 216 us                                                 | 217 us: 1.01x slower                                                      |
| xml_etree_parse      | 156 ms                                                 | 160 ms: 1.03x slower                                                      |
| xml_etree_iterparse  | 101 ms                                                 | 106 ms: 1.05x slower                                                      |
| json_dumps           | 10.6 ms                                                | 11.5 ms: 1.09x slower                                                     |
| Geometric mean       | (ref)                                                  | 1.01x slower                                                              |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241016-linux-x86_64-colesbury-gh_125610_STORE_ATTR-3.14.0a1+-3a126a8 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 12.5 ms                                                | 11.8 ms: 1.06x faster                                                     |
| python_startup_no_site | 6.96 ms                                                | 7.04 ms: 1.01x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.02x faster                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241016-linux-x86_64-colesbury-gh_125610_STORE_ATTR-3.14.0a1+-3a126a8 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| genshi_text     | 23.5 ms                                                | 22.9 ms: 1.03x faster                                                     |
| django_template | 35.2 ms                                                | 34.2 ms: 1.03x faster                                                     |
| genshi_xml      | 50.9 ms                                                | 51.3 ms: 1.01x slower                                                     |
| mako            | 11.1 ms                                                | 11.5 ms: 1.04x slower                                                     |
| Geometric mean  | (ref)                                                  | 1.00x faster                                                              |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241016-linux-x86_64-colesbury-gh_125610_STORE_ATTR-3.14.0a1+-3a126a8 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| deepcopy                   | 358 us                                                 | 262 us: 1.37x faster                                                      |
| deepcopy_memo              | 39.1 us                                                | 30.7 us: 1.27x faster                                                     |
| async_tree_memoization_tg  | 464 ms                                                 | 381 ms: 1.22x faster                                                      |
| go                         | 144 ms                                                 | 120 ms: 1.20x faster                                                      |
| deepcopy_reduce            | 3.20 us                                                | 2.71 us: 1.18x faster                                                     |
| pathlib                    | 17.5 ms                                                | 16.1 ms: 1.09x faster                                                     |
| telco                      | 8.54 ms                                                | 7.86 ms: 1.09x faster                                                     |
| async_tree_none            | 351 ms                                                 | 328 ms: 1.07x faster                                                      |
| regex_v8                   | 26.2 ms                                                | 24.6 ms: 1.06x faster                                                     |
| async_tree_memoization     | 442 ms                                                 | 415 ms: 1.06x faster                                                      |
| logging_format             | 6.40 us                                                | 6.05 us: 1.06x faster                                                     |
| python_startup             | 12.5 ms                                                | 11.8 ms: 1.06x faster                                                     |
| richards                   | 48.7 ms                                                | 46.1 ms: 1.06x faster                                                     |
| richards_super             | 54.9 ms                                                | 52.2 ms: 1.05x faster                                                     |
| json                       | 5.36 ms                                                | 5.10 ms: 1.05x faster                                                     |
| 2to3                       | 267 ms                                                 | 254 ms: 1.05x faster                                                      |
| scimark_sparse_mat_mult    | 5.04 ms                                                | 4.80 ms: 1.05x faster                                                     |
| logging_simple             | 5.72 us                                                | 5.47 us: 1.05x faster                                                     |
| generators                 | 29.0 ms                                                | 27.7 ms: 1.04x faster                                                     |
| crypto_pyaes               | 75.3 ms                                                | 72.4 ms: 1.04x faster                                                     |
| regex_dna                  | 218 ms                                                 | 210 ms: 1.04x faster                                                      |
| thrift                     | 809 us                                                 | 782 us: 1.04x faster                                                      |
| regex_effbot               | 3.73 ms                                                | 3.61 ms: 1.03x faster                                                     |
| typing_runtime_protocols   | 165 us                                                 | 160 us: 1.03x faster                                                      |
| genshi_text                | 23.5 ms                                                | 22.9 ms: 1.03x faster                                                     |
| django_template            | 35.2 ms                                                | 34.2 ms: 1.03x faster                                                     |
| pycparser                  | 1.20 sec                                               | 1.17 sec: 1.03x faster                                                    |
| sympy_str                  | 275 ms                                                 | 268 ms: 1.03x faster                                                      |
| regex_compile              | 132 ms                                                 | 129 ms: 1.03x faster                                                      |
| tomli_loads                | 2.14 sec                                               | 2.09 sec: 1.03x faster                                                    |
| sympy_sum                  | 150 ms                                                 | 147 ms: 1.02x faster                                                      |
| tornado_http               | 92.4 ms                                                | 90.2 ms: 1.02x faster                                                     |
| sympy_expand               | 463 ms                                                 | 455 ms: 1.02x faster                                                      |
| html5lib                   | 64.2 ms                                                | 63.0 ms: 1.02x faster                                                     |
| meteor_contest             | 109 ms                                                 | 107 ms: 1.02x faster                                                      |
| xml_etree_process          | 60.6 ms                                                | 59.6 ms: 1.02x faster                                                     |
| sqlglot_normalize          | 108 ms                                                 | 106 ms: 1.02x faster                                                      |
| dulwich_log                | 64.3 ms                                                | 63.6 ms: 1.01x faster                                                     |
| sqlglot_optimize           | 53.7 ms                                                | 53.1 ms: 1.01x faster                                                     |
| json_loads                 | 27.2 us                                                | 27.0 us: 1.01x faster                                                     |
| xml_etree_generate         | 86.7 ms                                                | 86.1 ms: 1.01x faster                                                     |
| float                      | 79.2 ms                                                | 78.7 ms: 1.01x faster                                                     |
| pickle_pure_python         | 310 us                                                 | 309 us: 1.01x faster                                                      |
| mdp                        | 2.72 sec                                               | 2.71 sec: 1.00x faster                                                    |
| async_generators           | 436 ms                                                 | 434 ms: 1.00x faster                                                      |
| sympy_integrate            | 19.9 ms                                                | 19.8 ms: 1.00x faster                                                     |
| scimark_fft                | 364 ms                                                 | 363 ms: 1.00x faster                                                      |
| gc_traversal               | 4.37 ms                                                | 4.37 ms: 1.00x faster                                                     |
| sqlglot_transpile          | 1.58 ms                                                | 1.59 ms: 1.00x slower                                                     |
| pidigits                   | 186 ms                                                 | 187 ms: 1.01x slower                                                      |
| unpickle_pure_python       | 216 us                                                 | 217 us: 1.01x slower                                                      |
| genshi_xml                 | 50.9 ms                                                | 51.3 ms: 1.01x slower                                                     |
| bpe_tokeniser              | 4.75 sec                                               | 4.78 sec: 1.01x slower                                                    |
| comprehensions             | 16.5 us                                                | 16.6 us: 1.01x slower                                                     |
| deltablue                  | 3.23 ms                                                | 3.25 ms: 1.01x slower                                                     |
| hexiom                     | 6.16 ms                                                | 6.23 ms: 1.01x slower                                                     |
| python_startup_no_site     | 6.96 ms                                                | 7.04 ms: 1.01x slower                                                     |
| scimark_lu                 | 113 ms                                                 | 114 ms: 1.02x slower                                                      |
| scimark_monte_carlo        | 67.4 ms                                                | 68.5 ms: 1.02x slower                                                     |
| sqlglot_parse              | 1.27 ms                                                | 1.29 ms: 1.02x slower                                                     |
| docutils                   | 2.59 sec                                               | 2.64 sec: 1.02x slower                                                    |
| pyflate                    | 471 ms                                                 | 480 ms: 1.02x slower                                                      |
| bench_thread_pool          | 822 us                                                 | 838 us: 1.02x slower                                                      |
| logging_silent             | 102 ns                                                 | 104 ns: 1.02x slower                                                      |
| scimark_sor                | 124 ms                                                 | 126 ms: 1.02x slower                                                      |
| xml_etree_parse            | 156 ms                                                 | 160 ms: 1.03x slower                                                      |
| nbody                      | 87.0 ms                                                | 89.3 ms: 1.03x slower                                                     |
| chaos                      | 58.1 ms                                                | 59.9 ms: 1.03x slower                                                     |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 564 ms: 1.03x slower                                                      |
| mako                       | 11.1 ms                                                | 11.5 ms: 1.04x slower                                                     |
| coroutines                 | 22.7 ms                                                | 23.6 ms: 1.04x slower                                                     |
| xml_etree_iterparse        | 101 ms                                                 | 106 ms: 1.05x slower                                                      |
| nqueens                    | 78.4 ms                                                | 82.7 ms: 1.06x slower                                                     |
| json_dumps                 | 10.6 ms                                                | 11.5 ms: 1.09x slower                                                     |
| create_gc_cycles           | 2.41 ms                                                | 2.66 ms: 1.10x slower                                                     |
| async_tree_io_tg           | 857 ms                                                 | 975 ms: 1.14x slower                                                      |
| bench_mp_pool              | 24.0 ms                                                | 78.5 ms: 3.27x slower                                                     |
| Geometric mean             | (ref)                                                  | 1.00x faster                                                              |

Benchmark hidden because not significant (12): pprint_pformat, raytrace, async_tree_cpu_io_mixed, coverage, async_tree_none_tg, spectral_norm, asyncio_websockets, pprint_safe_repr, fannkuch, sphinx, pylint, async_tree_io
Ignored benchmarks (8) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sqlalchemy_declarative, sqlalchemy_imperative

- Geometric mean (including insignificant results): 1.018x faster
# HPT report

- Reliability score: 96.60% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x
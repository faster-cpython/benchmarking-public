# Results vs. 3.13.0

- fork: bdraco
- ref: speed_up_async_sched
- machine: darwin-arm64
- commit hash: f78838c
- commit date: 2024-08-24
- overall geometric mean: 1.091x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: 0.63x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240824-darwin-arm64-bdraco-speed_up_async_sched-3.14.0a0-f78838c |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 187 ms                                                 | 160 ms: 1.17x faster                                                  |
| docutils       | 1.44 sec                                               | 1.47 sec: 1.02x slower                                                |
| html5lib       | 36.6 ms                                                | 31.2 ms: 1.17x faster                                                 |
| Geometric mean | (ref)                                                  | 1.05x faster                                                          |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240824-darwin-arm64-bdraco-speed_up_async_sched-3.14.0a0-f78838c |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| coroutines                       | 19.8 ms                                                | 16.1 ms: 1.23x faster                                                 |
| async_tree_memoization_tg        | 288 ms                                                 | 237 ms: 1.21x faster                                                  |
| async_tree_eager                 | 70.1 ms                                                | 60.8 ms: 1.15x faster                                                 |
| async_tree_eager_tg              | 47.8 ms                                                | 42.2 ms: 1.13x faster                                                 |
| async_tree_none                  | 215 ms                                                 | 192 ms: 1.12x faster                                                  |
| async_tree_eager_memoization     | 168 ms                                                 | 151 ms: 1.11x faster                                                  |
| async_tree_memoization           | 268 ms                                                 | 243 ms: 1.10x faster                                                  |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 129 ms: 1.07x faster                                                  |
| async_generators                 | 295 ms                                                 | 281 ms: 1.05x faster                                                  |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 360 ms: 1.04x faster                                                  |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 337 ms: 1.03x faster                                                  |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 465 ms: 1.04x slower                                                  |
| async_tree_io                    | 507 ms                                                 | 598 ms: 1.18x slower                                                  |
| async_tree_io_tg                 | 497 ms                                                 | 606 ms: 1.22x slower                                                  |
| async_tree_eager_io              | 514 ms                                                 | 699 ms: 1.36x slower                                                  |
| async_tree_eager_io_tg           | 477 ms                                                 | 742 ms: 1.56x slower                                                  |
| asyncio_websockets               | 242 ms                                                 | 409 ms: 1.69x slower                                                  |
| Geometric mean                   | (ref)                                                  | 1.03x slower                                                          |

Benchmark hidden because not significant (2): async_tree_cpu_io_mixed, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240824-darwin-arm64-bdraco-speed_up_async_sched-3.14.0a0-f78838c |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 74.0 ms                                                | 59.4 ms: 1.25x faster                                                 |
| float          | 56.0 ms                                                | 48.9 ms: 1.15x faster                                                 |
| pidigits       | 284 ms                                                 | 282 ms: 1.01x faster                                                  |
| Geometric mean | (ref)                                                  | 1.13x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240824-darwin-arm64-bdraco-speed_up_async_sched-3.14.0a0-f78838c |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 78.6 ms                                                | 66.9 ms: 1.17x faster                                                 |
| regex_effbot   | 2.63 ms                                                | 2.46 ms: 1.07x faster                                                 |
| regex_v8       | 17.0 ms                                                | 16.5 ms: 1.03x faster                                                 |
| regex_dna      | 149 ms                                                 | 145 ms: 1.03x faster                                                  |
| Geometric mean | (ref)                                                  | 1.07x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240824-darwin-arm64-bdraco-speed_up_async_sched-3.14.0a0-f78838c |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle_pure_python   | 214 us                                                 | 181 us: 1.18x faster                                                  |
| unpickle_pure_python | 164 us                                                 | 143 us: 1.14x faster                                                  |
| xml_etree_process    | 41.0 ms                                                | 37.7 ms: 1.09x faster                                                 |
| xml_etree_generate   | 57.0 ms                                                | 53.2 ms: 1.07x faster                                                 |
| tomli_loads          | 1.57 sec                                               | 1.48 sec: 1.06x faster                                                |
| json_dumps           | 6.52 ms                                                | 6.30 ms: 1.04x faster                                                 |
| json_loads           | 17.0 us                                                | 17.2 us: 1.02x slower                                                 |
| xml_etree_parse      | 107 ms                                                 | 110 ms: 1.03x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.06x faster                                                          |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240824-darwin-arm64-bdraco-speed_up_async_sched-3.14.0a0-f78838c |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 18.9 ms                                                | 16.5 ms: 1.15x faster                                                 |
| python_startup_no_site | 14.5 ms                                                | 13.5 ms: 1.07x faster                                                 |
| Geometric mean         | (ref)                                                  | 1.11x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240824-darwin-arm64-bdraco-speed_up_async_sched-3.14.0a0-f78838c |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_text     | 16.9 ms                                                | 13.8 ms: 1.22x faster                                                 |
| genshi_xml      | 34.4 ms                                                | 30.1 ms: 1.14x faster                                                 |
| django_template | 22.2 ms                                                | 19.7 ms: 1.13x faster                                                 |
| mako            | 7.68 ms                                                | 6.94 ms: 1.11x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.15x faster                                                          |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240824-darwin-arm64-bdraco-speed_up_async_sched-3.14.0a0-f78838c |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| deepcopy                         | 237 us                                                 | 144 us: 1.65x faster                                                  |
| deepcopy_memo                    | 27.4 us                                                | 16.9 us: 1.62x faster                                                 |
| generators                       | 31.5 ms                                                | 20.4 ms: 1.54x faster                                                 |
| deepcopy_reduce                  | 2.07 us                                                | 1.51 us: 1.37x faster                                                 |
| create_gc_cycles                 | 1.17 ms                                                | 906 us: 1.29x faster                                                  |
| bench_mp_pool                    | 62.5 ms                                                | 48.7 ms: 1.28x faster                                                 |
| deltablue                        | 2.68 ms                                                | 2.13 ms: 1.25x faster                                                 |
| nbody                            | 74.0 ms                                                | 59.4 ms: 1.25x faster                                                 |
| comprehensions                   | 12.3 us                                                | 9.93 us: 1.24x faster                                                 |
| coroutines                       | 19.8 ms                                                | 16.1 ms: 1.23x faster                                                 |
| genshi_text                      | 16.9 ms                                                | 13.8 ms: 1.22x faster                                                 |
| raytrace                         | 181 ms                                                 | 149 ms: 1.21x faster                                                  |
| async_tree_memoization_tg        | 288 ms                                                 | 237 ms: 1.21x faster                                                  |
| hexiom                           | 4.86 ms                                                | 4.06 ms: 1.20x faster                                                 |
| pickle_pure_python               | 214 us                                                 | 181 us: 1.18x faster                                                  |
| gc_traversal                     | 2.91 ms                                                | 2.47 ms: 1.18x faster                                                 |
| 2to3                             | 187 ms                                                 | 160 ms: 1.17x faster                                                  |
| regex_compile                    | 78.6 ms                                                | 66.9 ms: 1.17x faster                                                 |
| nqueens                          | 62.5 ms                                                | 53.3 ms: 1.17x faster                                                 |
| logging_simple                   | 3.60 us                                                | 3.07 us: 1.17x faster                                                 |
| html5lib                         | 36.6 ms                                                | 31.2 ms: 1.17x faster                                                 |
| richards_super                   | 39.1 ms                                                | 33.4 ms: 1.17x faster                                                 |
| pprint_safe_repr                 | 533 ms                                                 | 457 ms: 1.17x faster                                                  |
| pprint_pformat                   | 1.08 sec                                               | 930 ms: 1.17x faster                                                  |
| scimark_monte_carlo              | 50.4 ms                                                | 43.3 ms: 1.16x faster                                                 |
| richards                         | 35.2 ms                                                | 30.4 ms: 1.16x faster                                                 |
| sqlglot_parse                    | 856 us                                                 | 739 us: 1.16x faster                                                  |
| chaos                            | 41.2 ms                                                | 35.7 ms: 1.15x faster                                                 |
| async_tree_eager                 | 70.1 ms                                                | 60.8 ms: 1.15x faster                                                 |
| scimark_lu                       | 76.7 ms                                                | 66.7 ms: 1.15x faster                                                 |
| python_startup                   | 18.9 ms                                                | 16.5 ms: 1.15x faster                                                 |
| float                            | 56.0 ms                                                | 48.9 ms: 1.15x faster                                                 |
| logging_format                   | 3.89 us                                                | 3.40 us: 1.15x faster                                                 |
| logging_silent                   | 70.1 ns                                                | 61.2 ns: 1.15x faster                                                 |
| unpickle_pure_python             | 164 us                                                 | 143 us: 1.14x faster                                                  |
| genshi_xml                       | 34.4 ms                                                | 30.1 ms: 1.14x faster                                                 |
| sqlglot_transpile                | 1.02 ms                                                | 897 us: 1.14x faster                                                  |
| async_tree_eager_tg              | 47.8 ms                                                | 42.2 ms: 1.13x faster                                                 |
| scimark_sor                      | 105 ms                                                 | 93.3 ms: 1.13x faster                                                 |
| sqlglot_normalize                | 189 ms                                                 | 168 ms: 1.13x faster                                                  |
| django_template                  | 22.2 ms                                                | 19.7 ms: 1.13x faster                                                 |
| spectral_norm                    | 76.3 ms                                                | 67.7 ms: 1.13x faster                                                 |
| bench_thread_pool                | 505 us                                                 | 449 us: 1.12x faster                                                  |
| async_tree_none                  | 215 ms                                                 | 192 ms: 1.12x faster                                                  |
| sqlglot_optimize                 | 34.9 ms                                                | 31.2 ms: 1.12x faster                                                 |
| typing_runtime_protocols         | 101 us                                                 | 90.9 us: 1.11x faster                                                 |
| async_tree_eager_memoization     | 168 ms                                                 | 151 ms: 1.11x faster                                                  |
| sympy_str                        | 145 ms                                                 | 131 ms: 1.11x faster                                                  |
| mako                             | 7.68 ms                                                | 6.94 ms: 1.11x faster                                                 |
| thrift                           | 466 us                                                 | 423 us: 1.10x faster                                                  |
| async_tree_memoization           | 268 ms                                                 | 243 ms: 1.10x faster                                                  |
| pycparser                        | 705 ms                                                 | 643 ms: 1.10x faster                                                  |
| sympy_integrate                  | 11.3 ms                                                | 10.3 ms: 1.10x faster                                                 |
| pyflate                          | 351 ms                                                 | 321 ms: 1.09x faster                                                  |
| sympy_sum                        | 75.4 ms                                                | 69.1 ms: 1.09x faster                                                 |
| fannkuch                         | 284 ms                                                 | 260 ms: 1.09x faster                                                  |
| sympy_expand                     | 246 ms                                                 | 226 ms: 1.09x faster                                                  |
| go                               | 115 ms                                                 | 106 ms: 1.09x faster                                                  |
| xml_etree_process                | 41.0 ms                                                | 37.7 ms: 1.09x faster                                                 |
| scimark_fft                      | 201 ms                                                 | 185 ms: 1.09x faster                                                  |
| scimark_sparse_mat_mult          | 2.99 ms                                                | 2.78 ms: 1.07x faster                                                 |
| python_startup_no_site           | 14.5 ms                                                | 13.5 ms: 1.07x faster                                                 |
| xml_etree_generate               | 57.0 ms                                                | 53.2 ms: 1.07x faster                                                 |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 129 ms: 1.07x faster                                                  |
| regex_effbot                     | 2.63 ms                                                | 2.46 ms: 1.07x faster                                                 |
| crypto_pyaes                     | 54.2 ms                                                | 50.9 ms: 1.07x faster                                                 |
| tomli_loads                      | 1.57 sec                                               | 1.48 sec: 1.06x faster                                                |
| dulwich_log                      | 28.5 ms                                                | 27.1 ms: 1.05x faster                                                 |
| async_generators                 | 295 ms                                                 | 281 ms: 1.05x faster                                                  |
| mdp                              | 1.49 sec                                               | 1.43 sec: 1.05x faster                                                |
| bpe_tokeniser                    | 3.25 sec                                               | 3.13 sec: 1.04x faster                                                |
| coverage                         | 46.0 ms                                                | 44.3 ms: 1.04x faster                                                 |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 360 ms: 1.04x faster                                                  |
| json_dumps                       | 6.52 ms                                                | 6.30 ms: 1.04x faster                                                 |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 337 ms: 1.03x faster                                                  |
| regex_v8                         | 17.0 ms                                                | 16.5 ms: 1.03x faster                                                 |
| regex_dna                        | 149 ms                                                 | 145 ms: 1.03x faster                                                  |
| meteor_contest                   | 74.0 ms                                                | 72.5 ms: 1.02x faster                                                 |
| pidigits                         | 284 ms                                                 | 282 ms: 1.01x faster                                                  |
| telco                            | 4.76 ms                                                | 4.78 ms: 1.00x slower                                                 |
| json_loads                       | 17.0 us                                                | 17.2 us: 1.02x slower                                                 |
| docutils                         | 1.44 sec                                               | 1.47 sec: 1.02x slower                                                |
| xml_etree_parse                  | 107 ms                                                 | 110 ms: 1.03x slower                                                  |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 465 ms: 1.04x slower                                                  |
| async_tree_io                    | 507 ms                                                 | 598 ms: 1.18x slower                                                  |
| async_tree_io_tg                 | 497 ms                                                 | 606 ms: 1.22x slower                                                  |
| async_tree_eager_io              | 514 ms                                                 | 699 ms: 1.36x slower                                                  |
| async_tree_eager_io_tg           | 477 ms                                                 | 742 ms: 1.56x slower                                                  |
| asyncio_websockets               | 242 ms                                                 | 409 ms: 1.69x slower                                                  |
| Geometric mean                   | (ref)                                                  | 1.09x faster                                                          |

Benchmark hidden because not significant (7): json, async_tree_cpu_io_mixed, async_tree_none_tg, xml_etree_iterparse, pathlib, pylint, tornado_http
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, dask, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (2) of results/bm-20240824-3.14.0a0-f78838c/bm-20240824-darwin-arm64-bdraco-speed_up_async_sched-3.14.0a0-f78838c.json: asyncio_tcp, asyncio_tcp_ssl

- Geometric mean (including insignificant results): 1.091x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: 0.63x
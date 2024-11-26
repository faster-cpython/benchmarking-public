# Results vs. 3.13.0

- fork: mdboom
- ref: simplify_richcompare
- machine: darwin-arm64
- commit hash: c9a5962
- commit date: 2024-08-29
- overall geometric mean: 1.094x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: 0.58x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-darwin-arm64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 187 ms                                                 | 162 ms: 1.15x faster                                                  |
| docutils       | 1.44 sec                                               | 1.45 sec: 1.01x slower                                                |
| html5lib       | 36.6 ms                                                | 30.1 ms: 1.22x faster                                                 |
| Geometric mean | (ref)                                                  | 1.06x faster                                                          |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-darwin-arm64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_memoization_tg        | 288 ms                                                 | 243 ms: 1.18x faster                                                  |
| coroutines                       | 19.8 ms                                                | 16.8 ms: 1.18x faster                                                 |
| async_tree_eager                 | 70.1 ms                                                | 60.3 ms: 1.16x faster                                                 |
| async_tree_eager_tg              | 47.8 ms                                                | 41.9 ms: 1.14x faster                                                 |
| async_tree_none                  | 215 ms                                                 | 193 ms: 1.12x faster                                                  |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 125 ms: 1.11x faster                                                  |
| async_tree_eager_memoization     | 168 ms                                                 | 155 ms: 1.08x faster                                                  |
| async_tree_memoization           | 268 ms                                                 | 250 ms: 1.07x faster                                                  |
| async_generators                 | 295 ms                                                 | 281 ms: 1.05x faster                                                  |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 336 ms: 1.03x faster                                                  |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 361 ms: 1.03x faster                                                  |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 458 ms: 1.02x slower                                                  |
| async_tree_io_tg                 | 497 ms                                                 | 574 ms: 1.15x slower                                                  |
| async_tree_io                    | 507 ms                                                 | 595 ms: 1.17x slower                                                  |
| async_tree_eager_io              | 514 ms                                                 | 681 ms: 1.33x slower                                                  |
| async_tree_eager_io_tg           | 477 ms                                                 | 717 ms: 1.50x slower                                                  |
| asyncio_websockets               | 242 ms                                                 | 409 ms: 1.69x slower                                                  |
| Geometric mean                   | (ref)                                                  | 1.02x slower                                                          |

Benchmark hidden because not significant (2): async_tree_cpu_io_mixed, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-darwin-arm64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 74.0 ms                                                | 59.5 ms: 1.24x faster                                                 |
| float          | 56.0 ms                                                | 48.7 ms: 1.15x faster                                                 |
| pidigits       | 284 ms                                                 | 281 ms: 1.01x faster                                                  |
| Geometric mean | (ref)                                                  | 1.13x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-darwin-arm64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 78.6 ms                                                | 67.8 ms: 1.16x faster                                                 |
| regex_effbot   | 2.63 ms                                                | 2.47 ms: 1.06x faster                                                 |
| regex_v8       | 17.0 ms                                                | 16.5 ms: 1.03x faster                                                 |
| regex_dna      | 149 ms                                                 | 147 ms: 1.02x faster                                                  |
| Geometric mean | (ref)                                                  | 1.06x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-darwin-arm64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle_pure_python   | 214 us                                                 | 183 us: 1.17x faster                                                  |
| unpickle_pure_python | 164 us                                                 | 142 us: 1.15x faster                                                  |
| xml_etree_process    | 41.0 ms                                                | 37.8 ms: 1.09x faster                                                 |
| tomli_loads          | 1.57 sec                                               | 1.47 sec: 1.07x faster                                                |
| xml_etree_generate   | 57.0 ms                                                | 53.4 ms: 1.07x faster                                                 |
| json_dumps           | 6.52 ms                                                | 6.43 ms: 1.01x faster                                                 |
| xml_etree_iterparse  | 73.6 ms                                                | 74.1 ms: 1.01x slower                                                 |
| json_loads           | 17.0 us                                                | 17.3 us: 1.02x slower                                                 |
| xml_etree_parse      | 107 ms                                                 | 109 ms: 1.02x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-darwin-arm64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 18.9 ms                                                | 16.6 ms: 1.14x faster                                                 |
| python_startup_no_site | 14.5 ms                                                | 13.7 ms: 1.06x faster                                                 |
| Geometric mean         | (ref)                                                  | 1.10x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-darwin-arm64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_text     | 16.9 ms                                                | 13.9 ms: 1.22x faster                                                 |
| genshi_xml      | 34.4 ms                                                | 30.3 ms: 1.13x faster                                                 |
| django_template | 22.2 ms                                                | 19.6 ms: 1.13x faster                                                 |
| mako            | 7.68 ms                                                | 6.94 ms: 1.11x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.15x faster                                                          |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-darwin-arm64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| deepcopy_memo                    | 27.4 us                                                | 16.5 us: 1.66x faster                                                 |
| deepcopy                         | 237 us                                                 | 144 us: 1.64x faster                                                  |
| generators                       | 31.5 ms                                                | 20.4 ms: 1.54x faster                                                 |
| go                               | 115 ms                                                 | 79.2 ms: 1.45x faster                                                 |
| deepcopy_reduce                  | 2.07 us                                                | 1.50 us: 1.38x faster                                                 |
| create_gc_cycles                 | 1.17 ms                                                | 905 us: 1.29x faster                                                  |
| bench_mp_pool                    | 62.5 ms                                                | 48.9 ms: 1.28x faster                                                 |
| deltablue                        | 2.68 ms                                                | 2.15 ms: 1.25x faster                                                 |
| nbody                            | 74.0 ms                                                | 59.5 ms: 1.24x faster                                                 |
| comprehensions                   | 12.3 us                                                | 9.96 us: 1.23x faster                                                 |
| raytrace                         | 181 ms                                                 | 149 ms: 1.22x faster                                                  |
| genshi_text                      | 16.9 ms                                                | 13.9 ms: 1.22x faster                                                 |
| html5lib                         | 36.6 ms                                                | 30.1 ms: 1.22x faster                                                 |
| hexiom                           | 4.86 ms                                                | 4.07 ms: 1.20x faster                                                 |
| pprint_safe_repr                 | 533 ms                                                 | 450 ms: 1.18x faster                                                  |
| async_tree_memoization_tg        | 288 ms                                                 | 243 ms: 1.18x faster                                                  |
| gc_traversal                     | 2.91 ms                                                | 2.46 ms: 1.18x faster                                                 |
| coroutines                       | 19.8 ms                                                | 16.8 ms: 1.18x faster                                                 |
| pprint_pformat                   | 1.08 sec                                               | 922 ms: 1.18x faster                                                  |
| pickle_pure_python               | 214 us                                                 | 183 us: 1.17x faster                                                  |
| nqueens                          | 62.5 ms                                                | 53.6 ms: 1.17x faster                                                 |
| logging_simple                   | 3.60 us                                                | 3.09 us: 1.17x faster                                                 |
| scimark_monte_carlo              | 50.4 ms                                                | 43.2 ms: 1.17x faster                                                 |
| async_tree_eager                 | 70.1 ms                                                | 60.3 ms: 1.16x faster                                                 |
| regex_compile                    | 78.6 ms                                                | 67.8 ms: 1.16x faster                                                 |
| chaos                            | 41.2 ms                                                | 35.7 ms: 1.16x faster                                                 |
| sqlglot_parse                    | 856 us                                                 | 741 us: 1.15x faster                                                  |
| unpickle_pure_python             | 164 us                                                 | 142 us: 1.15x faster                                                  |
| 2to3                             | 187 ms                                                 | 162 ms: 1.15x faster                                                  |
| float                            | 56.0 ms                                                | 48.7 ms: 1.15x faster                                                 |
| scimark_lu                       | 76.7 ms                                                | 66.7 ms: 1.15x faster                                                 |
| logging_silent                   | 70.1 ns                                                | 61.3 ns: 1.14x faster                                                 |
| logging_format                   | 3.89 us                                                | 3.41 us: 1.14x faster                                                 |
| async_tree_eager_tg              | 47.8 ms                                                | 41.9 ms: 1.14x faster                                                 |
| python_startup                   | 18.9 ms                                                | 16.6 ms: 1.14x faster                                                 |
| genshi_xml                       | 34.4 ms                                                | 30.3 ms: 1.13x faster                                                 |
| sqlglot_transpile                | 1.02 ms                                                | 902 us: 1.13x faster                                                  |
| django_template                  | 22.2 ms                                                | 19.6 ms: 1.13x faster                                                 |
| scimark_sor                      | 105 ms                                                 | 93.1 ms: 1.13x faster                                                 |
| spectral_norm                    | 76.3 ms                                                | 67.5 ms: 1.13x faster                                                 |
| sqlglot_normalize                | 189 ms                                                 | 167 ms: 1.13x faster                                                  |
| bench_thread_pool                | 505 us                                                 | 451 us: 1.12x faster                                                  |
| sqlglot_optimize                 | 34.9 ms                                                | 31.2 ms: 1.12x faster                                                 |
| richards                         | 35.2 ms                                                | 31.4 ms: 1.12x faster                                                 |
| async_tree_none                  | 215 ms                                                 | 193 ms: 1.12x faster                                                  |
| richards_super                   | 39.1 ms                                                | 35.1 ms: 1.11x faster                                                 |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 125 ms: 1.11x faster                                                  |
| mako                             | 7.68 ms                                                | 6.94 ms: 1.11x faster                                                 |
| sympy_str                        | 145 ms                                                 | 131 ms: 1.11x faster                                                  |
| typing_runtime_protocols         | 101 us                                                 | 91.6 us: 1.10x faster                                                 |
| thrift                           | 466 us                                                 | 422 us: 1.10x faster                                                  |
| pycparser                        | 705 ms                                                 | 641 ms: 1.10x faster                                                  |
| pyflate                          | 351 ms                                                 | 321 ms: 1.10x faster                                                  |
| sympy_integrate                  | 11.3 ms                                                | 10.3 ms: 1.09x faster                                                 |
| sympy_sum                        | 75.4 ms                                                | 69.1 ms: 1.09x faster                                                 |
| sympy_expand                     | 246 ms                                                 | 227 ms: 1.09x faster                                                  |
| xml_etree_process                | 41.0 ms                                                | 37.8 ms: 1.09x faster                                                 |
| scimark_fft                      | 201 ms                                                 | 185 ms: 1.08x faster                                                  |
| async_tree_eager_memoization     | 168 ms                                                 | 155 ms: 1.08x faster                                                  |
| fannkuch                         | 284 ms                                                 | 263 ms: 1.08x faster                                                  |
| async_tree_memoization           | 268 ms                                                 | 250 ms: 1.07x faster                                                  |
| crypto_pyaes                     | 54.2 ms                                                | 50.6 ms: 1.07x faster                                                 |
| scimark_sparse_mat_mult          | 2.99 ms                                                | 2.79 ms: 1.07x faster                                                 |
| tomli_loads                      | 1.57 sec                                               | 1.47 sec: 1.07x faster                                                |
| xml_etree_generate               | 57.0 ms                                                | 53.4 ms: 1.07x faster                                                 |
| regex_effbot                     | 2.63 ms                                                | 2.47 ms: 1.06x faster                                                 |
| dulwich_log                      | 28.5 ms                                                | 27.0 ms: 1.06x faster                                                 |
| python_startup_no_site           | 14.5 ms                                                | 13.7 ms: 1.06x faster                                                 |
| async_generators                 | 295 ms                                                 | 281 ms: 1.05x faster                                                  |
| mdp                              | 1.49 sec                                               | 1.43 sec: 1.05x faster                                                |
| bpe_tokeniser                    | 3.25 sec                                               | 3.14 sec: 1.03x faster                                                |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 336 ms: 1.03x faster                                                  |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 361 ms: 1.03x faster                                                  |
| regex_v8                         | 17.0 ms                                                | 16.5 ms: 1.03x faster                                                 |
| json                             | 3.03 ms                                                | 2.96 ms: 1.02x faster                                                 |
| meteor_contest                   | 74.0 ms                                                | 72.4 ms: 1.02x faster                                                 |
| coverage                         | 46.0 ms                                                | 45.0 ms: 1.02x faster                                                 |
| regex_dna                        | 149 ms                                                 | 147 ms: 1.02x faster                                                  |
| json_dumps                       | 6.52 ms                                                | 6.43 ms: 1.01x faster                                                 |
| pidigits                         | 284 ms                                                 | 281 ms: 1.01x faster                                                  |
| xml_etree_iterparse              | 73.6 ms                                                | 74.1 ms: 1.01x slower                                                 |
| docutils                         | 1.44 sec                                               | 1.45 sec: 1.01x slower                                                |
| telco                            | 4.76 ms                                                | 4.84 ms: 1.02x slower                                                 |
| json_loads                       | 17.0 us                                                | 17.3 us: 1.02x slower                                                 |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 458 ms: 1.02x slower                                                  |
| xml_etree_parse                  | 107 ms                                                 | 109 ms: 1.02x slower                                                  |
| pathlib                          | 23.4 ms                                                | 24.0 ms: 1.03x slower                                                 |
| async_tree_io_tg                 | 497 ms                                                 | 574 ms: 1.15x slower                                                  |
| async_tree_io                    | 507 ms                                                 | 595 ms: 1.17x slower                                                  |
| async_tree_eager_io              | 514 ms                                                 | 681 ms: 1.33x slower                                                  |
| async_tree_eager_io_tg           | 477 ms                                                 | 717 ms: 1.50x slower                                                  |
| asyncio_websockets               | 242 ms                                                 | 409 ms: 1.69x slower                                                  |
| Geometric mean                   | (ref)                                                  | 1.10x faster                                                          |

Benchmark hidden because not significant (4): async_tree_cpu_io_mixed, async_tree_none_tg, pylint, tornado_http
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, dask, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (2) of results/bm-20240829-3.14.0a0-c9a5962/bm-20240829-darwin-arm64-mdboom-simplify_richcompare-3.14.0a0-c9a5962.json: asyncio_tcp, asyncio_tcp_ssl

- Geometric mean (including insignificant results): 1.094x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: 0.58x
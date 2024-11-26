# Results vs. 3.13.0

- fork: python
- ref: v3.13.0b4
- machine: darwin-arm64
- commit hash: 567c38b
- commit date: 2024-07-18
- overall geometric mean: 1.107x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x faster
- Memory change: 0.93x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240718-darwin-arm64-python-v3.13.0b4-3.13.0b4-567c38b |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| 2to3           | 187 ms                                                 | 162 ms: 1.15x faster                                       |
| chameleon      | 5.08 ms                                                | 4.31 ms: 1.18x faster                                      |
| docutils       | 1.44 sec                                               | 1.45 sec: 1.01x slower                                     |
| html5lib       | 36.6 ms                                                | 31.5 ms: 1.16x faster                                      |
| Geometric mean | (ref)                                                  | 1.12x faster                                               |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240718-darwin-arm64-python-v3.13.0b4-3.13.0b4-567c38b |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| coroutines                       | 19.8 ms                                                | 15.9 ms: 1.24x faster                                      |
| async_tree_memoization_tg        | 288 ms                                                 | 240 ms: 1.20x faster                                       |
| async_tree_eager_tg              | 47.8 ms                                                | 41.6 ms: 1.15x faster                                      |
| async_tree_eager                 | 70.1 ms                                                | 61.1 ms: 1.15x faster                                      |
| async_tree_eager_memoization     | 168 ms                                                 | 150 ms: 1.13x faster                                       |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 126 ms: 1.09x faster                                       |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 331 ms: 1.05x faster                                       |
| async_generators                 | 295 ms                                                 | 282 ms: 1.04x faster                                       |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 359 ms: 1.04x faster                                       |
| async_tree_none                  | 215 ms                                                 | 210 ms: 1.03x faster                                       |
| async_tree_cpu_io_mixed          | 460 ms                                                 | 469 ms: 1.02x slower                                       |
| async_tree_io                    | 507 ms                                                 | 557 ms: 1.10x slower                                       |
| async_tree_io_tg                 | 497 ms                                                 | 562 ms: 1.13x slower                                       |
| async_tree_eager_io              | 514 ms                                                 | 768 ms: 1.49x slower                                       |
| async_tree_eager_io_tg           | 477 ms                                                 | 766 ms: 1.60x slower                                       |
| asyncio_websockets               | 242 ms                                                 | 408 ms: 1.69x slower                                       |
| Geometric mean                   | (ref)                                                  | 1.03x slower                                               |

Benchmark hidden because not significant (3): async_tree_memoization, async_tree_none_tg, async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240718-darwin-arm64-python-v3.13.0b4-3.13.0b4-567c38b |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| nbody          | 74.0 ms                                                | 59.8 ms: 1.24x faster                                      |
| float          | 56.0 ms                                                | 48.7 ms: 1.15x faster                                      |
| pidigits       | 284 ms                                                 | 281 ms: 1.01x faster                                       |
| Geometric mean | (ref)                                                  | 1.13x faster                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240718-darwin-arm64-python-v3.13.0b4-3.13.0b4-567c38b |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| regex_compile  | 78.6 ms                                                | 68.4 ms: 1.15x faster                                      |
| regex_effbot   | 2.63 ms                                                | 2.57 ms: 1.02x faster                                      |
| regex_v8       | 17.0 ms                                                | 17.2 ms: 1.01x slower                                      |
| Geometric mean | (ref)                                                  | 1.04x faster                                               |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240718-darwin-arm64-python-v3.13.0b4-3.13.0b4-567c38b |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| pickle_pure_python   | 214 us                                                 | 180 us: 1.19x faster                                       |
| unpickle_pure_python | 164 us                                                 | 142 us: 1.15x faster                                       |
| xml_etree_process    | 41.0 ms                                                | 37.3 ms: 1.10x faster                                      |
| xml_etree_generate   | 57.0 ms                                                | 53.0 ms: 1.07x faster                                      |
| tomli_loads          | 1.57 sec                                               | 1.48 sec: 1.06x faster                                     |
| json_dumps           | 6.52 ms                                                | 6.25 ms: 1.04x faster                                      |
| xml_etree_iterparse  | 73.6 ms                                                | 71.3 ms: 1.03x faster                                      |
| xml_etree_parse      | 107 ms                                                 | 105 ms: 1.02x faster                                       |
| Geometric mean       | (ref)                                                  | 1.07x faster                                               |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240718-darwin-arm64-python-v3.13.0b4-3.13.0b4-567c38b |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| python_startup         | 18.9 ms                                                | 14.1 ms: 1.34x faster                                      |
| python_startup_no_site | 14.5 ms                                                | 11.3 ms: 1.28x faster                                      |
| Geometric mean         | (ref)                                                  | 1.31x faster                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240718-darwin-arm64-python-v3.13.0b4-3.13.0b4-567c38b |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| genshi_text     | 16.9 ms                                                | 13.8 ms: 1.23x faster                                      |
| genshi_xml      | 34.4 ms                                                | 29.8 ms: 1.16x faster                                      |
| django_template | 22.2 ms                                                | 19.5 ms: 1.14x faster                                      |
| mako            | 7.68 ms                                                | 7.00 ms: 1.10x faster                                      |
| Geometric mean  | (ref)                                                  | 1.15x faster                                               |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240718-darwin-arm64-python-v3.13.0b4-3.13.0b4-567c38b |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| dask                             | 790 ms                                                 | 220 ms: 3.59x faster                                       |
| mypy2                            | 701 ms                                                 | 447 ms: 1.57x faster                                       |
| generators                       | 31.5 ms                                                | 23.0 ms: 1.37x faster                                      |
| create_gc_cycles                 | 1.17 ms                                                | 867 us: 1.35x faster                                       |
| bench_mp_pool                    | 62.5 ms                                                | 46.5 ms: 1.34x faster                                      |
| python_startup                   | 18.9 ms                                                | 14.1 ms: 1.34x faster                                      |
| python_startup_no_site           | 14.5 ms                                                | 11.3 ms: 1.28x faster                                      |
| deltablue                        | 2.68 ms                                                | 2.15 ms: 1.24x faster                                      |
| coroutines                       | 19.8 ms                                                | 15.9 ms: 1.24x faster                                      |
| nbody                            | 74.0 ms                                                | 59.8 ms: 1.24x faster                                      |
| genshi_text                      | 16.9 ms                                                | 13.8 ms: 1.23x faster                                      |
| raytrace                         | 181 ms                                                 | 148 ms: 1.22x faster                                       |
| deepcopy_memo                    | 27.4 us                                                | 22.7 us: 1.21x faster                                      |
| comprehensions                   | 12.3 us                                                | 10.2 us: 1.20x faster                                      |
| async_tree_memoization_tg        | 288 ms                                                 | 240 ms: 1.20x faster                                       |
| hexiom                           | 4.86 ms                                                | 4.07 ms: 1.20x faster                                      |
| pickle_pure_python               | 214 us                                                 | 180 us: 1.19x faster                                       |
| chaos                            | 41.2 ms                                                | 34.7 ms: 1.19x faster                                      |
| gc_traversal                     | 2.91 ms                                                | 2.45 ms: 1.19x faster                                      |
| scimark_monte_carlo              | 50.4 ms                                                | 42.6 ms: 1.18x faster                                      |
| nqueens                          | 62.5 ms                                                | 52.9 ms: 1.18x faster                                      |
| chameleon                        | 5.08 ms                                                | 4.31 ms: 1.18x faster                                      |
| sqlglot_parse                    | 856 us                                                 | 730 us: 1.17x faster                                       |
| logging_silent                   | 70.1 ns                                                | 60.1 ns: 1.17x faster                                      |
| html5lib                         | 36.6 ms                                                | 31.5 ms: 1.16x faster                                      |
| pprint_safe_repr                 | 533 ms                                                 | 459 ms: 1.16x faster                                       |
| deepcopy                         | 237 us                                                 | 204 us: 1.16x faster                                       |
| logging_simple                   | 3.60 us                                                | 3.11 us: 1.16x faster                                      |
| pprint_pformat                   | 1.08 sec                                               | 936 ms: 1.16x faster                                       |
| genshi_xml                       | 34.4 ms                                                | 29.8 ms: 1.16x faster                                      |
| unpickle_pure_python             | 164 us                                                 | 142 us: 1.15x faster                                       |
| 2to3                             | 187 ms                                                 | 162 ms: 1.15x faster                                       |
| async_tree_eager_tg              | 47.8 ms                                                | 41.6 ms: 1.15x faster                                      |
| float                            | 56.0 ms                                                | 48.7 ms: 1.15x faster                                      |
| regex_compile                    | 78.6 ms                                                | 68.4 ms: 1.15x faster                                      |
| scimark_lu                       | 76.7 ms                                                | 66.7 ms: 1.15x faster                                      |
| go                               | 115 ms                                                 | 100 ms: 1.15x faster                                       |
| async_tree_eager                 | 70.1 ms                                                | 61.1 ms: 1.15x faster                                      |
| sqlglot_transpile                | 1.02 ms                                                | 892 us: 1.15x faster                                       |
| logging_format                   | 3.89 us                                                | 3.40 us: 1.15x faster                                      |
| spectral_norm                    | 76.3 ms                                                | 66.8 ms: 1.14x faster                                      |
| typing_runtime_protocols         | 101 us                                                 | 88.7 us: 1.14x faster                                      |
| richards_super                   | 39.1 ms                                                | 34.3 ms: 1.14x faster                                      |
| sqlglot_normalize                | 189 ms                                                 | 166 ms: 1.14x faster                                       |
| django_template                  | 22.2 ms                                                | 19.5 ms: 1.14x faster                                      |
| deepcopy_reduce                  | 2.07 us                                                | 1.82 us: 1.14x faster                                      |
| sqlglot_optimize                 | 34.9 ms                                                | 30.8 ms: 1.13x faster                                      |
| richards                         | 35.2 ms                                                | 31.2 ms: 1.13x faster                                      |
| async_tree_eager_memoization     | 168 ms                                                 | 150 ms: 1.13x faster                                       |
| pycparser                        | 705 ms                                                 | 630 ms: 1.12x faster                                       |
| fannkuch                         | 284 ms                                                 | 254 ms: 1.12x faster                                       |
| scimark_fft                      | 201 ms                                                 | 181 ms: 1.11x faster                                       |
| scimark_sor                      | 105 ms                                                 | 95.0 ms: 1.11x faster                                      |
| sympy_str                        | 145 ms                                                 | 132 ms: 1.10x faster                                       |
| xml_etree_process                | 41.0 ms                                                | 37.3 ms: 1.10x faster                                      |
| bench_thread_pool                | 505 us                                                 | 460 us: 1.10x faster                                       |
| mako                             | 7.68 ms                                                | 7.00 ms: 1.10x faster                                      |
| pyflate                          | 351 ms                                                 | 321 ms: 1.10x faster                                       |
| sympy_expand                     | 246 ms                                                 | 225 ms: 1.10x faster                                       |
| sympy_integrate                  | 11.3 ms                                                | 10.3 ms: 1.09x faster                                      |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 126 ms: 1.09x faster                                       |
| crypto_pyaes                     | 54.2 ms                                                | 50.0 ms: 1.09x faster                                      |
| sympy_sum                        | 75.4 ms                                                | 69.5 ms: 1.09x faster                                      |
| thrift                           | 466 us                                                 | 433 us: 1.08x faster                                       |
| xml_etree_generate               | 57.0 ms                                                | 53.0 ms: 1.07x faster                                      |
| scimark_sparse_mat_mult          | 2.99 ms                                                | 2.80 ms: 1.07x faster                                      |
| bpe_tokeniser                    | 3.25 sec                                               | 3.05 sec: 1.06x faster                                     |
| tomli_loads                      | 1.57 sec                                               | 1.48 sec: 1.06x faster                                     |
| mdp                              | 1.49 sec                                               | 1.41 sec: 1.06x faster                                     |
| meteor_contest                   | 74.0 ms                                                | 70.5 ms: 1.05x faster                                      |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 331 ms: 1.05x faster                                       |
| async_generators                 | 295 ms                                                 | 282 ms: 1.04x faster                                       |
| json_dumps                       | 6.52 ms                                                | 6.25 ms: 1.04x faster                                      |
| dulwich_log                      | 28.5 ms                                                | 27.4 ms: 1.04x faster                                      |
| json                             | 3.03 ms                                                | 2.92 ms: 1.04x faster                                      |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 359 ms: 1.04x faster                                       |
| xml_etree_iterparse              | 73.6 ms                                                | 71.3 ms: 1.03x faster                                      |
| telco                            | 4.76 ms                                                | 4.63 ms: 1.03x faster                                      |
| async_tree_none                  | 215 ms                                                 | 210 ms: 1.03x faster                                       |
| xml_etree_parse                  | 107 ms                                                 | 105 ms: 1.02x faster                                       |
| regex_effbot                     | 2.63 ms                                                | 2.57 ms: 1.02x faster                                      |
| coverage                         | 46.0 ms                                                | 45.0 ms: 1.02x faster                                      |
| pidigits                         | 284 ms                                                 | 281 ms: 1.01x faster                                       |
| docutils                         | 1.44 sec                                               | 1.45 sec: 1.01x slower                                     |
| pathlib                          | 23.4 ms                                                | 23.7 ms: 1.01x slower                                      |
| regex_v8                         | 17.0 ms                                                | 17.2 ms: 1.01x slower                                      |
| async_tree_cpu_io_mixed          | 460 ms                                                 | 469 ms: 1.02x slower                                       |
| async_tree_io                    | 507 ms                                                 | 557 ms: 1.10x slower                                       |
| async_tree_io_tg                 | 497 ms                                                 | 562 ms: 1.13x slower                                       |
| async_tree_eager_io              | 514 ms                                                 | 768 ms: 1.49x slower                                       |
| async_tree_eager_io_tg           | 477 ms                                                 | 766 ms: 1.60x slower                                       |
| asyncio_websockets               | 242 ms                                                 | 408 ms: 1.69x slower                                       |
| Geometric mean                   | (ref)                                                  | 1.11x faster                                               |

Benchmark hidden because not significant (7): tornado_http, pylint, async_tree_memoization, regex_dna, json_loads, async_tree_none_tg, async_tree_cpu_io_mixed_tg
Ignored benchmarks (7) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: connected_components, gevent_hub, k_core, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (2) of results/bm-20240718-3.13.0b4-567c38b/bm-20240718-darwin-arm64-python-v3.13.0b4-3.13.0b4-567c38b.json: asyncio_tcp, asyncio_tcp_ssl

- Geometric mean (including insignificant results): 1.107x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.06x
- 99% likely to have a speedup of 1.05x

# Memory
- memory change: 0.93x
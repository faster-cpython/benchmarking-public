# Results vs. 3.13.0

- fork: python
- ref: v3.13.0rc1
- machine: darwin-arm64
- commit hash: e4a3e78
- commit date: 2024-07-31
- overall geometric mean: 1.098x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x faster
- Memory change: 0.38x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240731-darwin-arm64-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| 2to3           | 187 ms                                                 | 160 ms: 1.17x faster                                         |
| chameleon      | 5.08 ms                                                | 4.36 ms: 1.16x faster                                        |
| docutils       | 1.44 sec                                               | 1.45 sec: 1.01x slower                                       |
| html5lib       | 36.6 ms                                                | 31.7 ms: 1.15x faster                                        |
| Geometric mean | (ref)                                                  | 1.12x faster                                                 |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240731-darwin-arm64-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|----------------------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| coroutines                       | 19.8 ms                                                | 16.0 ms: 1.24x faster                                        |
| async_tree_memoization_tg        | 288 ms                                                 | 240 ms: 1.20x faster                                         |
| async_tree_eager_tg              | 47.8 ms                                                | 41.7 ms: 1.15x faster                                        |
| async_tree_eager                 | 70.1 ms                                                | 61.5 ms: 1.14x faster                                        |
| async_tree_eager_memoization     | 168 ms                                                 | 153 ms: 1.10x faster                                         |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 126 ms: 1.09x faster                                         |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 332 ms: 1.04x faster                                         |
| async_generators                 | 295 ms                                                 | 283 ms: 1.04x faster                                         |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 360 ms: 1.03x faster                                         |
| async_tree_none                  | 215 ms                                                 | 210 ms: 1.03x faster                                         |
| async_tree_cpu_io_mixed          | 460 ms                                                 | 468 ms: 1.02x slower                                         |
| async_tree_io                    | 507 ms                                                 | 555 ms: 1.10x slower                                         |
| async_tree_io_tg                 | 497 ms                                                 | 564 ms: 1.13x slower                                         |
| async_tree_eager_io              | 514 ms                                                 | 763 ms: 1.48x slower                                         |
| async_tree_eager_io_tg           | 477 ms                                                 | 762 ms: 1.60x slower                                         |
| asyncio_websockets               | 242 ms                                                 | 409 ms: 1.69x slower                                         |
| Geometric mean                   | (ref)                                                  | 1.03x slower                                                 |

Benchmark hidden because not significant (3): async_tree_memoization, async_tree_none_tg, async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240731-darwin-arm64-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| nbody          | 74.0 ms                                                | 60.6 ms: 1.22x faster                                        |
| float          | 56.0 ms                                                | 48.5 ms: 1.16x faster                                        |
| pidigits       | 284 ms                                                 | 283 ms: 1.00x faster                                         |
| Geometric mean | (ref)                                                  | 1.12x faster                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240731-darwin-arm64-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| regex_compile  | 78.6 ms                                                | 69.3 ms: 1.13x faster                                        |
| regex_effbot   | 2.63 ms                                                | 2.59 ms: 1.01x faster                                        |
| regex_dna      | 149 ms                                                 | 151 ms: 1.01x slower                                         |
| regex_v8       | 17.0 ms                                                | 17.3 ms: 1.02x slower                                        |
| Geometric mean | (ref)                                                  | 1.03x faster                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240731-darwin-arm64-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| pickle_pure_python   | 214 us                                                 | 182 us: 1.18x faster                                         |
| unpickle_pure_python | 164 us                                                 | 143 us: 1.15x faster                                         |
| xml_etree_process    | 41.0 ms                                                | 38.0 ms: 1.08x faster                                        |
| tomli_loads          | 1.57 sec                                               | 1.46 sec: 1.07x faster                                       |
| xml_etree_generate   | 57.0 ms                                                | 53.2 ms: 1.07x faster                                        |
| json_dumps           | 6.52 ms                                                | 6.22 ms: 1.05x faster                                        |
| xml_etree_iterparse  | 73.6 ms                                                | 72.0 ms: 1.02x faster                                        |
| xml_etree_parse      | 107 ms                                                 | 106 ms: 1.01x faster                                         |
| json_loads           | 17.0 us                                                | 16.9 us: 1.01x faster                                        |
| Geometric mean       | (ref)                                                  | 1.07x faster                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240731-darwin-arm64-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup         | 18.9 ms                                                | 15.4 ms: 1.23x faster                                        |
| python_startup_no_site | 14.5 ms                                                | 12.7 ms: 1.14x faster                                        |
| Geometric mean         | (ref)                                                  | 1.19x faster                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240731-darwin-arm64-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| genshi_text     | 16.9 ms                                                | 14.0 ms: 1.21x faster                                        |
| genshi_xml      | 34.4 ms                                                | 30.1 ms: 1.14x faster                                        |
| django_template | 22.2 ms                                                | 20.0 ms: 1.11x faster                                        |
| mako            | 7.68 ms                                                | 7.23 ms: 1.06x faster                                        |
| Geometric mean  | (ref)                                                  | 1.13x faster                                                 |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240731-darwin-arm64-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|----------------------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| dask                             | 790 ms                                                 | 220 ms: 3.58x faster                                         |
| mypy2                            | 701 ms                                                 | 455 ms: 1.54x faster                                         |
| generators                       | 31.5 ms                                                | 22.9 ms: 1.38x faster                                        |
| create_gc_cycles                 | 1.17 ms                                                | 880 us: 1.33x faster                                         |
| bench_mp_pool                    | 62.5 ms                                                | 47.9 ms: 1.31x faster                                        |
| deltablue                        | 2.68 ms                                                | 2.15 ms: 1.24x faster                                        |
| coroutines                       | 19.8 ms                                                | 16.0 ms: 1.24x faster                                        |
| python_startup                   | 18.9 ms                                                | 15.4 ms: 1.23x faster                                        |
| nbody                            | 74.0 ms                                                | 60.6 ms: 1.22x faster                                        |
| raytrace                         | 181 ms                                                 | 148 ms: 1.22x faster                                         |
| genshi_text                      | 16.9 ms                                                | 14.0 ms: 1.21x faster                                        |
| async_tree_memoization_tg        | 288 ms                                                 | 240 ms: 1.20x faster                                         |
| chaos                            | 41.2 ms                                                | 34.5 ms: 1.19x faster                                        |
| hexiom                           | 4.86 ms                                                | 4.10 ms: 1.19x faster                                        |
| gc_traversal                     | 2.91 ms                                                | 2.46 ms: 1.18x faster                                        |
| pickle_pure_python               | 214 us                                                 | 182 us: 1.18x faster                                         |
| deepcopy_memo                    | 27.4 us                                                | 23.2 us: 1.18x faster                                        |
| scimark_monte_carlo              | 50.4 ms                                                | 42.9 ms: 1.18x faster                                        |
| nqueens                          | 62.5 ms                                                | 53.3 ms: 1.17x faster                                        |
| 2to3                             | 187 ms                                                 | 160 ms: 1.17x faster                                         |
| chameleon                        | 5.08 ms                                                | 4.36 ms: 1.16x faster                                        |
| logging_format                   | 3.89 us                                                | 3.35 us: 1.16x faster                                        |
| logging_simple                   | 3.60 us                                                | 3.10 us: 1.16x faster                                        |
| float                            | 56.0 ms                                                | 48.5 ms: 1.16x faster                                        |
| comprehensions                   | 12.3 us                                                | 10.6 us: 1.16x faster                                        |
| sqlglot_parse                    | 856 us                                                 | 741 us: 1.16x faster                                         |
| html5lib                         | 36.6 ms                                                | 31.7 ms: 1.15x faster                                        |
| deepcopy                         | 237 us                                                 | 205 us: 1.15x faster                                         |
| logging_silent                   | 70.1 ns                                                | 60.9 ns: 1.15x faster                                        |
| unpickle_pure_python             | 164 us                                                 | 143 us: 1.15x faster                                         |
| async_tree_eager_tg              | 47.8 ms                                                | 41.7 ms: 1.15x faster                                        |
| typing_runtime_protocols         | 101 us                                                 | 88.5 us: 1.14x faster                                        |
| python_startup_no_site           | 14.5 ms                                                | 12.7 ms: 1.14x faster                                        |
| genshi_xml                       | 34.4 ms                                                | 30.1 ms: 1.14x faster                                        |
| go                               | 115 ms                                                 | 101 ms: 1.14x faster                                         |
| async_tree_eager                 | 70.1 ms                                                | 61.5 ms: 1.14x faster                                        |
| pprint_pformat                   | 1.08 sec                                               | 953 ms: 1.14x faster                                         |
| pprint_safe_repr                 | 533 ms                                                 | 469 ms: 1.14x faster                                         |
| regex_compile                    | 78.6 ms                                                | 69.3 ms: 1.13x faster                                        |
| spectral_norm                    | 76.3 ms                                                | 67.4 ms: 1.13x faster                                        |
| sqlglot_transpile                | 1.02 ms                                                | 904 us: 1.13x faster                                         |
| deepcopy_reduce                  | 2.07 us                                                | 1.83 us: 1.13x faster                                        |
| sqlglot_normalize                | 189 ms                                                 | 167 ms: 1.13x faster                                         |
| scimark_lu                       | 76.7 ms                                                | 67.9 ms: 1.13x faster                                        |
| richards_super                   | 39.1 ms                                                | 34.7 ms: 1.13x faster                                        |
| fannkuch                         | 284 ms                                                 | 254 ms: 1.12x faster                                         |
| sqlglot_optimize                 | 34.9 ms                                                | 31.3 ms: 1.12x faster                                        |
| richards                         | 35.2 ms                                                | 31.6 ms: 1.11x faster                                        |
| django_template                  | 22.2 ms                                                | 20.0 ms: 1.11x faster                                        |
| scimark_sor                      | 105 ms                                                 | 95.2 ms: 1.11x faster                                        |
| pycparser                        | 705 ms                                                 | 638 ms: 1.11x faster                                         |
| async_tree_eager_memoization     | 168 ms                                                 | 153 ms: 1.10x faster                                         |
| sympy_str                        | 145 ms                                                 | 133 ms: 1.10x faster                                         |
| pyflate                          | 351 ms                                                 | 321 ms: 1.10x faster                                         |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 126 ms: 1.09x faster                                         |
| scimark_fft                      | 201 ms                                                 | 184 ms: 1.09x faster                                         |
| bench_thread_pool                | 505 us                                                 | 463 us: 1.09x faster                                         |
| crypto_pyaes                     | 54.2 ms                                                | 50.0 ms: 1.08x faster                                        |
| sympy_integrate                  | 11.3 ms                                                | 10.4 ms: 1.08x faster                                        |
| sympy_expand                     | 246 ms                                                 | 228 ms: 1.08x faster                                         |
| xml_etree_process                | 41.0 ms                                                | 38.0 ms: 1.08x faster                                        |
| tomli_loads                      | 1.57 sec                                               | 1.46 sec: 1.07x faster                                       |
| sympy_sum                        | 75.4 ms                                                | 70.2 ms: 1.07x faster                                        |
| thrift                           | 466 us                                                 | 435 us: 1.07x faster                                         |
| xml_etree_generate               | 57.0 ms                                                | 53.2 ms: 1.07x faster                                        |
| mako                             | 7.68 ms                                                | 7.23 ms: 1.06x faster                                        |
| bpe_tokeniser                    | 3.25 sec                                               | 3.06 sec: 1.06x faster                                       |
| scimark_sparse_mat_mult          | 2.99 ms                                                | 2.84 ms: 1.05x faster                                        |
| meteor_contest                   | 74.0 ms                                                | 70.4 ms: 1.05x faster                                        |
| json_dumps                       | 6.52 ms                                                | 6.22 ms: 1.05x faster                                        |
| mdp                              | 1.49 sec                                               | 1.43 sec: 1.05x faster                                       |
| json                             | 3.03 ms                                                | 2.90 ms: 1.05x faster                                        |
| dulwich_log                      | 28.5 ms                                                | 27.3 ms: 1.04x faster                                        |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 332 ms: 1.04x faster                                         |
| async_generators                 | 295 ms                                                 | 283 ms: 1.04x faster                                         |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 360 ms: 1.03x faster                                         |
| telco                            | 4.76 ms                                                | 4.64 ms: 1.03x faster                                        |
| async_tree_none                  | 215 ms                                                 | 210 ms: 1.03x faster                                         |
| xml_etree_iterparse              | 73.6 ms                                                | 72.0 ms: 1.02x faster                                        |
| coverage                         | 46.0 ms                                                | 45.0 ms: 1.02x faster                                        |
| xml_etree_parse                  | 107 ms                                                 | 106 ms: 1.01x faster                                         |
| regex_effbot                     | 2.63 ms                                                | 2.59 ms: 1.01x faster                                        |
| json_loads                       | 17.0 us                                                | 16.9 us: 1.01x faster                                        |
| pidigits                         | 284 ms                                                 | 283 ms: 1.00x faster                                         |
| docutils                         | 1.44 sec                                               | 1.45 sec: 1.01x slower                                       |
| regex_dna                        | 149 ms                                                 | 151 ms: 1.01x slower                                         |
| pathlib                          | 23.4 ms                                                | 23.8 ms: 1.02x slower                                        |
| async_tree_cpu_io_mixed          | 460 ms                                                 | 468 ms: 1.02x slower                                         |
| regex_v8                         | 17.0 ms                                                | 17.3 ms: 1.02x slower                                        |
| async_tree_io                    | 507 ms                                                 | 555 ms: 1.10x slower                                         |
| async_tree_io_tg                 | 497 ms                                                 | 564 ms: 1.13x slower                                         |
| async_tree_eager_io              | 514 ms                                                 | 763 ms: 1.48x slower                                         |
| async_tree_eager_io_tg           | 477 ms                                                 | 762 ms: 1.60x slower                                         |
| asyncio_websockets               | 242 ms                                                 | 409 ms: 1.69x slower                                         |
| Geometric mean                   | (ref)                                                  | 1.10x faster                                                 |

Benchmark hidden because not significant (5): tornado_http, async_tree_memoization, pylint, async_tree_none_tg, async_tree_cpu_io_mixed_tg
Ignored benchmarks (7) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: connected_components, gevent_hub, k_core, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (2) of results/bm-20240731-3.13.0rc1-e4a3e78/bm-20240731-darwin-arm64-python-v3.13.0rc1-3.13.0rc1-e4a3e78.json: asyncio_tcp, asyncio_tcp_ssl

- Geometric mean (including insignificant results): 1.098x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.06x
- 99% likely to have a speedup of 1.05x

# Memory
- memory change: 0.38x
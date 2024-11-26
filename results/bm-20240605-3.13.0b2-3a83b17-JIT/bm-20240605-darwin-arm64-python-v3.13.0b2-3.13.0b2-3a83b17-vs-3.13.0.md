# Results vs. 3.13.0

- fork: python
- ref: v3.13.0b2
- machine: darwin-arm64
- commit hash: 3a83b17
- commit date: 2024-06-05
- overall geometric mean: 1.077x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: 1.13x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| 2to3           | 187 ms                                                 | 173 ms: 1.08x faster                                       |
| chameleon      | 5.08 ms                                                | 4.41 ms: 1.15x faster                                      |
| docutils       | 1.44 sec                                               | 1.51 sec: 1.05x slower                                     |
| html5lib       | 36.6 ms                                                | 31.1 ms: 1.17x faster                                      |
| Geometric mean | (ref)                                                  | 1.09x faster                                               |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| coroutines                       | 19.8 ms                                                | 16.0 ms: 1.23x faster                                      |
| async_tree_memoization_tg        | 288 ms                                                 | 242 ms: 1.19x faster                                       |
| async_tree_eager_tg              | 47.8 ms                                                | 42.7 ms: 1.12x faster                                      |
| async_tree_eager                 | 70.1 ms                                                | 63.3 ms: 1.11x faster                                      |
| async_tree_eager_memoization     | 168 ms                                                 | 155 ms: 1.09x faster                                       |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 128 ms: 1.08x faster                                       |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 334 ms: 1.04x faster                                       |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 364 ms: 1.02x faster                                       |
| async_generators                 | 295 ms                                                 | 296 ms: 1.00x slower                                       |
| async_tree_cpu_io_mixed          | 460 ms                                                 | 472 ms: 1.03x slower                                       |
| async_tree_io                    | 507 ms                                                 | 571 ms: 1.13x slower                                       |
| async_tree_io_tg                 | 497 ms                                                 | 570 ms: 1.15x slower                                       |
| async_tree_eager_io              | 514 ms                                                 | 761 ms: 1.48x slower                                       |
| async_tree_eager_io_tg           | 477 ms                                                 | 769 ms: 1.61x slower                                       |
| asyncio_websockets               | 242 ms                                                 | 409 ms: 1.69x slower                                       |
| Geometric mean                   | (ref)                                                  | 1.05x slower                                               |

Benchmark hidden because not significant (4): async_tree_memoization, async_tree_none, async_tree_none_tg, async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| float          | 56.0 ms                                                | 47.4 ms: 1.18x faster                                      |
| nbody          | 74.0 ms                                                | 63.5 ms: 1.17x faster                                      |
| pidigits       | 284 ms                                                 | 282 ms: 1.00x faster                                       |
| Geometric mean | (ref)                                                  | 1.12x faster                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| regex_compile  | 78.6 ms                                                | 71.9 ms: 1.09x faster                                      |
| regex_effbot   | 2.63 ms                                                | 2.58 ms: 1.02x faster                                      |
| regex_v8       | 17.0 ms                                                | 17.3 ms: 1.02x slower                                      |
| Geometric mean | (ref)                                                  | 1.02x faster                                               |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| tomli_loads          | 1.57 sec                                               | 1.24 sec: 1.26x faster                                     |
| unpickle_pure_python | 164 us                                                 | 132 us: 1.24x faster                                       |
| pickle_pure_python   | 214 us                                                 | 173 us: 1.24x faster                                       |
| xml_etree_process    | 41.0 ms                                                | 35.8 ms: 1.14x faster                                      |
| xml_etree_generate   | 57.0 ms                                                | 51.6 ms: 1.10x faster                                      |
| json_dumps           | 6.52 ms                                                | 6.17 ms: 1.06x faster                                      |
| xml_etree_iterparse  | 73.6 ms                                                | 70.5 ms: 1.04x faster                                      |
| xml_etree_parse      | 107 ms                                                 | 105 ms: 1.02x faster                                       |
| json_loads           | 17.0 us                                                | 16.9 us: 1.00x faster                                      |
| Geometric mean       | (ref)                                                  | 1.12x faster                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| python_startup         | 18.9 ms                                                | 16.4 ms: 1.16x faster                                      |
| python_startup_no_site | 14.5 ms                                                | 13.4 ms: 1.08x faster                                      |
| Geometric mean         | (ref)                                                  | 1.12x faster                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| mako            | 7.68 ms                                                | 6.40 ms: 1.20x faster                                      |
| django_template | 22.2 ms                                                | 21.3 ms: 1.04x faster                                      |
| genshi_text     | 16.9 ms                                                | 16.4 ms: 1.03x faster                                      |
| genshi_xml      | 34.4 ms                                                | 39.3 ms: 1.14x slower                                      |
| Geometric mean  | (ref)                                                  | 1.03x faster                                               |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| dask                             | 790 ms                                                 | 223 ms: 3.54x faster                                       |
| mypy2                            | 701 ms                                                 | 408 ms: 1.72x faster                                       |
| generators                       | 31.5 ms                                                | 23.6 ms: 1.34x faster                                      |
| create_gc_cycles                 | 1.17 ms                                                | 903 us: 1.29x faster                                       |
| deepcopy_memo                    | 27.4 us                                                | 21.5 us: 1.27x faster                                      |
| tomli_loads                      | 1.57 sec                                               | 1.24 sec: 1.26x faster                                     |
| unpickle_pure_python             | 164 us                                                 | 132 us: 1.24x faster                                       |
| pickle_pure_python               | 214 us                                                 | 173 us: 1.24x faster                                       |
| coroutines                       | 19.8 ms                                                | 16.0 ms: 1.23x faster                                      |
| fannkuch                         | 284 ms                                                 | 233 ms: 1.22x faster                                       |
| bench_mp_pool                    | 62.5 ms                                                | 51.4 ms: 1.22x faster                                      |
| mako                             | 7.68 ms                                                | 6.40 ms: 1.20x faster                                      |
| logging_simple                   | 3.60 us                                                | 3.02 us: 1.19x faster                                      |
| async_tree_memoization_tg        | 288 ms                                                 | 242 ms: 1.19x faster                                       |
| float                            | 56.0 ms                                                | 47.4 ms: 1.18x faster                                      |
| gc_traversal                     | 2.91 ms                                                | 2.46 ms: 1.18x faster                                      |
| html5lib                         | 36.6 ms                                                | 31.1 ms: 1.17x faster                                      |
| logging_format                   | 3.89 us                                                | 3.33 us: 1.17x faster                                      |
| nbody                            | 74.0 ms                                                | 63.5 ms: 1.17x faster                                      |
| python_startup                   | 18.9 ms                                                | 16.4 ms: 1.16x faster                                      |
| chameleon                        | 5.08 ms                                                | 4.41 ms: 1.15x faster                                      |
| pprint_safe_repr                 | 533 ms                                                 | 464 ms: 1.15x faster                                       |
| scimark_monte_carlo              | 50.4 ms                                                | 44.0 ms: 1.14x faster                                      |
| xml_etree_process                | 41.0 ms                                                | 35.8 ms: 1.14x faster                                      |
| deepcopy                         | 237 us                                                 | 208 us: 1.14x faster                                       |
| deepcopy_reduce                  | 2.07 us                                                | 1.82 us: 1.14x faster                                      |
| pprint_pformat                   | 1.08 sec                                               | 958 ms: 1.13x faster                                       |
| spectral_norm                    | 76.3 ms                                                | 67.5 ms: 1.13x faster                                      |
| go                               | 115 ms                                                 | 102 ms: 1.13x faster                                       |
| async_tree_eager_tg              | 47.8 ms                                                | 42.7 ms: 1.12x faster                                      |
| hexiom                           | 4.86 ms                                                | 4.36 ms: 1.12x faster                                      |
| pyflate                          | 351 ms                                                 | 315 ms: 1.11x faster                                       |
| raytrace                         | 181 ms                                                 | 163 ms: 1.11x faster                                       |
| logging_silent                   | 70.1 ns                                                | 63.1 ns: 1.11x faster                                      |
| richards                         | 35.2 ms                                                | 31.7 ms: 1.11x faster                                      |
| async_tree_eager                 | 70.1 ms                                                | 63.3 ms: 1.11x faster                                      |
| xml_etree_generate               | 57.0 ms                                                | 51.6 ms: 1.10x faster                                      |
| nqueens                          | 62.5 ms                                                | 56.8 ms: 1.10x faster                                      |
| richards_super                   | 39.1 ms                                                | 35.7 ms: 1.10x faster                                      |
| regex_compile                    | 78.6 ms                                                | 71.9 ms: 1.09x faster                                      |
| async_tree_eager_memoization     | 168 ms                                                 | 155 ms: 1.09x faster                                       |
| deltablue                        | 2.68 ms                                                | 2.47 ms: 1.09x faster                                      |
| 2to3                             | 187 ms                                                 | 173 ms: 1.08x faster                                       |
| scimark_fft                      | 201 ms                                                 | 185 ms: 1.08x faster                                       |
| typing_runtime_protocols         | 101 us                                                 | 93.5 us: 1.08x faster                                      |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 128 ms: 1.08x faster                                       |
| python_startup_no_site           | 14.5 ms                                                | 13.4 ms: 1.08x faster                                      |
| sqlglot_optimize                 | 34.9 ms                                                | 32.6 ms: 1.07x faster                                      |
| thrift                           | 466 us                                                 | 438 us: 1.06x faster                                       |
| sympy_str                        | 145 ms                                                 | 137 ms: 1.06x faster                                       |
| chaos                            | 41.2 ms                                                | 38.9 ms: 1.06x faster                                      |
| json_dumps                       | 6.52 ms                                                | 6.17 ms: 1.06x faster                                      |
| bpe_tokeniser                    | 3.25 sec                                               | 3.09 sec: 1.05x faster                                     |
| bench_thread_pool                | 505 us                                                 | 481 us: 1.05x faster                                       |
| pycparser                        | 705 ms                                                 | 672 ms: 1.05x faster                                       |
| scimark_sor                      | 105 ms                                                 | 100 ms: 1.05x faster                                       |
| crypto_pyaes                     | 54.2 ms                                                | 51.8 ms: 1.05x faster                                      |
| mdp                              | 1.49 sec                                               | 1.43 sec: 1.05x faster                                     |
| sympy_expand                     | 246 ms                                                 | 236 ms: 1.04x faster                                       |
| xml_etree_iterparse              | 73.6 ms                                                | 70.5 ms: 1.04x faster                                      |
| django_template                  | 22.2 ms                                                | 21.3 ms: 1.04x faster                                      |
| sympy_sum                        | 75.4 ms                                                | 72.4 ms: 1.04x faster                                      |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 334 ms: 1.04x faster                                       |
| sympy_integrate                  | 11.3 ms                                                | 10.9 ms: 1.04x faster                                      |
| sqlglot_parse                    | 856 us                                                 | 826 us: 1.04x faster                                       |
| meteor_contest                   | 74.0 ms                                                | 71.4 ms: 1.04x faster                                      |
| json                             | 3.03 ms                                                | 2.93 ms: 1.03x faster                                      |
| genshi_text                      | 16.9 ms                                                | 16.4 ms: 1.03x faster                                      |
| telco                            | 4.76 ms                                                | 4.64 ms: 1.03x faster                                      |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 364 ms: 1.02x faster                                       |
| coverage                         | 46.0 ms                                                | 44.9 ms: 1.02x faster                                      |
| scimark_sparse_mat_mult          | 2.99 ms                                                | 2.92 ms: 1.02x faster                                      |
| sqlglot_transpile                | 1.02 ms                                                | 1.00 ms: 1.02x faster                                      |
| xml_etree_parse                  | 107 ms                                                 | 105 ms: 1.02x faster                                       |
| regex_effbot                     | 2.63 ms                                                | 2.58 ms: 1.02x faster                                      |
| pidigits                         | 284 ms                                                 | 282 ms: 1.00x faster                                       |
| json_loads                       | 17.0 us                                                | 16.9 us: 1.00x faster                                      |
| async_generators                 | 295 ms                                                 | 296 ms: 1.00x slower                                       |
| dulwich_log                      | 28.5 ms                                                | 28.8 ms: 1.01x slower                                      |
| regex_v8                         | 17.0 ms                                                | 17.3 ms: 1.02x slower                                      |
| scimark_lu                       | 76.7 ms                                                | 78.6 ms: 1.03x slower                                      |
| async_tree_cpu_io_mixed          | 460 ms                                                 | 472 ms: 1.03x slower                                       |
| docutils                         | 1.44 sec                                               | 1.51 sec: 1.05x slower                                     |
| async_tree_io                    | 507 ms                                                 | 571 ms: 1.13x slower                                       |
| genshi_xml                       | 34.4 ms                                                | 39.3 ms: 1.14x slower                                      |
| async_tree_io_tg                 | 497 ms                                                 | 570 ms: 1.15x slower                                       |
| async_tree_eager_io              | 514 ms                                                 | 761 ms: 1.48x slower                                       |
| async_tree_eager_io_tg           | 477 ms                                                 | 769 ms: 1.61x slower                                       |
| asyncio_websockets               | 242 ms                                                 | 409 ms: 1.69x slower                                       |
| Geometric mean                   | (ref)                                                  | 1.08x faster                                               |

Benchmark hidden because not significant (9): tornado_http, async_tree_memoization, async_tree_none, comprehensions, regex_dna, pathlib, async_tree_none_tg, pylint, async_tree_cpu_io_mixed_tg
Ignored benchmarks (8) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: connected_components, gevent_hub, k_core, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize
Ignored benchmarks (11) of results/bm-20240605-3.13.0b2-3a83b17-JIT/bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.077x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 1.13x
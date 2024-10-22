# Results vs. 3.13.0

- fork: python
- ref: v3.13.0b1
- machine: darwin-arm64
- commit hash: 2268289
- commit date: 2024-05-08
- overall geometric mean: 1.06x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: 6.62x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240508-darwin-arm64-python-v3.13.0b1-3.13.0b1-2268289 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| 2to3           | 178 ms                                                 | 179 ms: 1.01x slower                                       |
| chameleon      | 5.08 ms                                                | 4.35 ms: 1.17x faster                                      |
| docutils       | 1.44 sec                                               | 1.46 sec: 1.01x slower                                     |
| html5lib       | 36.6 ms                                                | 31.2 ms: 1.18x faster                                      |
| Geometric mean | (ref)                                                  | 1.08x faster                                               |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240508-darwin-arm64-python-v3.13.0b1-3.13.0b1-2268289 |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| coroutines                       | 19.8 ms                                                | 16.2 ms: 1.22x faster                                      |
| async_tree_memoization_tg        | 291 ms                                                 | 245 ms: 1.19x faster                                       |
| async_tree_eager_tg              | 48.4 ms                                                | 41.4 ms: 1.17x faster                                      |
| async_tree_eager                 | 70.5 ms                                                | 61.0 ms: 1.16x faster                                      |
| async_tree_eager_memoization     | 169 ms                                                 | 149 ms: 1.14x faster                                       |
| async_tree_eager_memoization_tg  | 139 ms                                                 | 128 ms: 1.09x faster                                       |
| asyncio_tcp                      | 457 ms                                                 | 424 ms: 1.08x faster                                       |
| async_generators                 | 294 ms                                                 | 278 ms: 1.06x faster                                       |
| async_tree_eager_cpu_io_mixed_tg | 348 ms                                                 | 333 ms: 1.05x faster                                       |
| async_tree_memoization           | 270 ms                                                 | 258 ms: 1.05x faster                                       |
| async_tree_eager_cpu_io_mixed    | 375 ms                                                 | 361 ms: 1.04x faster                                       |
| async_tree_cpu_io_mixed          | 460 ms                                                 | 469 ms: 1.02x slower                                       |
| asyncio_tcp_ssl                  | 1.26 sec                                               | 1.29 sec: 1.02x slower                                     |
| async_tree_io                    | 507 ms                                                 | 570 ms: 1.12x slower                                       |
| async_tree_io_tg                 | 500 ms                                                 | 564 ms: 1.13x slower                                       |
| async_tree_eager_io              | 513 ms                                                 | 772 ms: 1.51x slower                                       |
| async_tree_eager_io_tg           | 477 ms                                                 | 755 ms: 1.58x slower                                       |
| asyncio_websockets               | 241 ms                                                 | 408 ms: 1.69x slower                                       |
| Geometric mean                   | (ref)                                                  | 1.03x slower                                               |

Benchmark hidden because not significant (3): async_tree_none, async_tree_none_tg, async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240508-darwin-arm64-python-v3.13.0b1-3.13.0b1-2268289 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| float          | 56.2 ms                                                | 49.0 ms: 1.15x faster                                      |
| nbody          | 73.9 ms                                                | 65.7 ms: 1.12x faster                                      |
| pidigits       | 284 ms                                                 | 282 ms: 1.01x faster                                       |
| Geometric mean | (ref)                                                  | 1.09x faster                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240508-darwin-arm64-python-v3.13.0b1-3.13.0b1-2268289 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| regex_compile  | 78.5 ms                                                | 68.2 ms: 1.15x faster                                      |
| regex_dna      | 148 ms                                                 | 139 ms: 1.06x faster                                       |
| regex_effbot   | 2.63 ms                                                | 2.55 ms: 1.03x faster                                      |
| regex_v8       | 16.9 ms                                                | 16.8 ms: 1.01x faster                                      |
| Geometric mean | (ref)                                                  | 1.06x faster                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240508-darwin-arm64-python-v3.13.0b1-3.13.0b1-2268289 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| pickle_pure_python   | 213 us                                                 | 181 us: 1.17x faster                                       |
| unpickle_pure_python | 163 us                                                 | 141 us: 1.16x faster                                       |
| xml_etree_parse      | 109 ms                                                 | 97.6 ms: 1.11x faster                                      |
| xml_etree_process    | 40.9 ms                                                | 37.1 ms: 1.10x faster                                      |
| xml_etree_iterparse  | 74.2 ms                                                | 67.5 ms: 1.10x faster                                      |
| xml_etree_generate   | 56.6 ms                                                | 51.8 ms: 1.09x faster                                      |
| tomli_loads          | 1.56 sec                                               | 1.45 sec: 1.07x faster                                     |
| json_dumps           | 6.56 ms                                                | 6.35 ms: 1.03x faster                                      |
| pickle_list          | 2.99 us                                                | 2.98 us: 1.00x faster                                      |
| pickle               | 7.36 us                                                | 7.47 us: 1.01x slower                                      |
| json_loads           | 16.9 us                                                | 17.3 us: 1.03x slower                                      |
| unpickle             | 9.15 us                                                | 9.70 us: 1.06x slower                                      |
| unpickle_list        | 2.93 us                                                | 3.31 us: 1.13x slower                                      |
| Geometric mean       | (ref)                                                  | 1.04x faster                                               |

Benchmark hidden because not significant (1): pickle_dict

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240508-darwin-arm64-python-v3.13.0b1-3.13.0b1-2268289 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| python_startup         | 17.0 ms                                                | 14.3 ms: 1.19x faster                                      |
| python_startup_no_site | 13.7 ms                                                | 11.6 ms: 1.18x faster                                      |
| Geometric mean         | (ref)                                                  | 1.18x faster                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240508-darwin-arm64-python-v3.13.0b1-3.13.0b1-2268289 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| genshi_text     | 16.9 ms                                                | 13.8 ms: 1.22x faster                                      |
| genshi_xml      | 34.4 ms                                                | 30.0 ms: 1.15x faster                                      |
| django_template | 22.2 ms                                                | 19.4 ms: 1.15x faster                                      |
| mako            | 7.68 ms                                                | 6.88 ms: 1.12x faster                                      |
| Geometric mean  | (ref)                                                  | 1.16x faster                                               |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240508-darwin-arm64-python-v3.13.0b1-3.13.0b1-2268289 |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| generators                       | 31.5 ms                                                | 22.7 ms: 1.39x faster                                      |
| deltablue                        | 2.68 ms                                                | 2.15 ms: 1.25x faster                                      |
| coroutines                       | 19.8 ms                                                | 16.2 ms: 1.22x faster                                      |
| genshi_text                      | 16.9 ms                                                | 13.8 ms: 1.22x faster                                      |
| deepcopy_memo                    | 27.2 us                                                | 22.4 us: 1.22x faster                                      |
| raytrace                         | 182 ms                                                 | 150 ms: 1.21x faster                                       |
| nqueens                          | 62.9 ms                                                | 52.8 ms: 1.19x faster                                      |
| async_tree_memoization_tg        | 291 ms                                                 | 245 ms: 1.19x faster                                       |
| hexiom                           | 4.85 ms                                                | 4.09 ms: 1.19x faster                                      |
| python_startup                   | 17.0 ms                                                | 14.3 ms: 1.19x faster                                      |
| gunicorn                         | 1.31 ms                                                | 1.11 ms: 1.18x faster                                      |
| python_startup_no_site           | 13.7 ms                                                | 11.6 ms: 1.18x faster                                      |
| html5lib                         | 36.6 ms                                                | 31.2 ms: 1.18x faster                                      |
| pickle_pure_python               | 213 us                                                 | 181 us: 1.17x faster                                       |
| scimark_monte_carlo              | 50.4 ms                                                | 43.0 ms: 1.17x faster                                      |
| chameleon                        | 5.08 ms                                                | 4.35 ms: 1.17x faster                                      |
| async_tree_eager_tg              | 48.4 ms                                                | 41.4 ms: 1.17x faster                                      |
| logging_simple                   | 3.57 us                                                | 3.06 us: 1.17x faster                                      |
| dask                             | 255 ms                                                 | 219 ms: 1.17x faster                                       |
| logging_silent                   | 69.9 ns                                                | 60.1 ns: 1.16x faster                                      |
| sqlglot_parse                    | 856 us                                                 | 739 us: 1.16x faster                                       |
| unpickle_pure_python             | 163 us                                                 | 141 us: 1.16x faster                                       |
| async_tree_eager                 | 70.5 ms                                                | 61.0 ms: 1.16x faster                                      |
| regex_compile                    | 78.5 ms                                                | 68.2 ms: 1.15x faster                                      |
| chaos                            | 41.3 ms                                                | 35.9 ms: 1.15x faster                                      |
| go                               | 115 ms                                                 | 100 ms: 1.15x faster                                       |
| float                            | 56.2 ms                                                | 49.0 ms: 1.15x faster                                      |
| deepcopy_reduce                  | 2.06 us                                                | 1.79 us: 1.15x faster                                      |
| aiohttp                          | 1.26 ms                                                | 1.10 ms: 1.15x faster                                      |
| logging_format                   | 3.85 us                                                | 3.36 us: 1.15x faster                                      |
| genshi_xml                       | 34.4 ms                                                | 30.0 ms: 1.15x faster                                      |
| django_template                  | 22.2 ms                                                | 19.4 ms: 1.15x faster                                      |
| deepcopy                         | 232 us                                                 | 203 us: 1.14x faster                                       |
| sqlglot_transpile                | 1.02 ms                                                | 897 us: 1.14x faster                                       |
| pprint_pformat                   | 1.08 sec                                               | 947 ms: 1.14x faster                                       |
| async_tree_eager_memoization     | 169 ms                                                 | 149 ms: 1.14x faster                                       |
| pprint_safe_repr                 | 531 ms                                                 | 468 ms: 1.13x faster                                       |
| sqlglot_normalize                | 189 ms                                                 | 166 ms: 1.13x faster                                       |
| spectral_norm                    | 77.3 ms                                                | 68.2 ms: 1.13x faster                                      |
| bench_mp_pool                    | 50.9 ms                                                | 45.2 ms: 1.13x faster                                      |
| nbody                            | 73.9 ms                                                | 65.7 ms: 1.12x faster                                      |
| sqlglot_optimize                 | 34.9 ms                                                | 31.1 ms: 1.12x faster                                      |
| comprehensions                   | 12.2 us                                                | 10.9 us: 1.12x faster                                      |
| scimark_lu                       | 76.5 ms                                                | 68.3 ms: 1.12x faster                                      |
| pycparser                        | 706 ms                                                 | 630 ms: 1.12x faster                                       |
| fannkuch                         | 282 ms                                                 | 252 ms: 1.12x faster                                       |
| mako                             | 7.68 ms                                                | 6.88 ms: 1.12x faster                                      |
| xml_etree_parse                  | 109 ms                                                 | 97.6 ms: 1.11x faster                                      |
| richards_super                   | 39.1 ms                                                | 35.2 ms: 1.11x faster                                      |
| richards                         | 35.4 ms                                                | 31.9 ms: 1.11x faster                                      |
| xml_etree_process                | 40.9 ms                                                | 37.1 ms: 1.10x faster                                      |
| pyflate                          | 351 ms                                                 | 319 ms: 1.10x faster                                       |
| xml_etree_iterparse              | 74.2 ms                                                | 67.5 ms: 1.10x faster                                      |
| sympy_str                        | 145 ms                                                 | 133 ms: 1.10x faster                                       |
| scimark_sor                      | 106 ms                                                 | 96.3 ms: 1.10x faster                                      |
| sympy_integrate                  | 11.3 ms                                                | 10.3 ms: 1.10x faster                                      |
| xml_etree_generate               | 56.6 ms                                                | 51.8 ms: 1.09x faster                                      |
| typing_runtime_protocols         | 101 us                                                 | 92.5 us: 1.09x faster                                      |
| bench_thread_pool                | 506 us                                                 | 464 us: 1.09x faster                                       |
| async_tree_eager_memoization_tg  | 139 ms                                                 | 128 ms: 1.09x faster                                       |
| sympy_expand                     | 246 ms                                                 | 228 ms: 1.08x faster                                       |
| asyncio_tcp                      | 457 ms                                                 | 424 ms: 1.08x faster                                       |
| sympy_sum                        | 75.6 ms                                                | 70.2 ms: 1.08x faster                                      |
| crypto_pyaes                     | 54.0 ms                                                | 50.3 ms: 1.07x faster                                      |
| thrift                           | 466 us                                                 | 434 us: 1.07x faster                                       |
| pylint                           | 181 ms                                                 | 169 ms: 1.07x faster                                       |
| tomli_loads                      | 1.56 sec                                               | 1.45 sec: 1.07x faster                                     |
| scimark_sparse_mat_mult          | 2.99 ms                                                | 2.80 ms: 1.07x faster                                      |
| regex_dna                        | 148 ms                                                 | 139 ms: 1.06x faster                                       |
| async_generators                 | 294 ms                                                 | 278 ms: 1.06x faster                                       |
| scimark_fft                      | 201 ms                                                 | 190 ms: 1.06x faster                                       |
| telco                            | 4.80 ms                                                | 4.56 ms: 1.05x faster                                      |
| dulwich_log                      | 28.7 ms                                                | 27.3 ms: 1.05x faster                                      |
| async_tree_eager_cpu_io_mixed_tg | 348 ms                                                 | 333 ms: 1.05x faster                                       |
| async_tree_memoization           | 270 ms                                                 | 258 ms: 1.05x faster                                       |
| meteor_contest                   | 73.8 ms                                                | 70.6 ms: 1.05x faster                                      |
| async_tree_eager_cpu_io_mixed    | 375 ms                                                 | 361 ms: 1.04x faster                                       |
| json_dumps                       | 6.56 ms                                                | 6.35 ms: 1.03x faster                                      |
| regex_effbot                     | 2.63 ms                                                | 2.55 ms: 1.03x faster                                      |
| regex_v8                         | 16.9 ms                                                | 16.8 ms: 1.01x faster                                      |
| gc_traversal                     | 2.48 ms                                                | 2.46 ms: 1.01x faster                                      |
| pidigits                         | 284 ms                                                 | 282 ms: 1.01x faster                                       |
| pathlib                          | 22.8 ms                                                | 22.7 ms: 1.01x faster                                      |
| sqlite_synth                     | 1.54 us                                                | 1.54 us: 1.00x faster                                      |
| pickle_list                      | 2.99 us                                                | 2.98 us: 1.00x faster                                      |
| coverage                         | 46.1 ms                                                | 46.5 ms: 1.01x slower                                      |
| docutils                         | 1.44 sec                                               | 1.46 sec: 1.01x slower                                     |
| 2to3                             | 178 ms                                                 | 179 ms: 1.01x slower                                       |
| pickle                           | 7.36 us                                                | 7.47 us: 1.01x slower                                      |
| json                             | 2.94 ms                                                | 2.99 ms: 1.02x slower                                      |
| async_tree_cpu_io_mixed          | 460 ms                                                 | 469 ms: 1.02x slower                                       |
| asyncio_tcp_ssl                  | 1.26 sec                                               | 1.29 sec: 1.02x slower                                     |
| json_loads                       | 16.9 us                                                | 17.3 us: 1.03x slower                                      |
| unpickle                         | 9.15 us                                                | 9.70 us: 1.06x slower                                      |
| create_gc_cycles                 | 803 us                                                 | 884 us: 1.10x slower                                       |
| async_tree_io                    | 507 ms                                                 | 570 ms: 1.12x slower                                       |
| async_tree_io_tg                 | 500 ms                                                 | 564 ms: 1.13x slower                                       |
| unpickle_list                    | 2.93 us                                                | 3.31 us: 1.13x slower                                      |
| mypy2                            | 396 ms                                                 | 461 ms: 1.17x slower                                       |
| async_tree_eager_io              | 513 ms                                                 | 772 ms: 1.51x slower                                       |
| async_tree_eager_io_tg           | 477 ms                                                 | 755 ms: 1.58x slower                                       |
| asyncio_websockets               | 241 ms                                                 | 408 ms: 1.69x slower                                       |
| flaskblogging                    | 2.89 ms                                                | 5.10 ms: 1.77x slower                                      |
| Geometric mean                   | (ref)                                                  | 1.06x faster                                               |

Benchmark hidden because not significant (6): tornado_http, async_tree_none, async_tree_none_tg, mdp, pickle_dict, async_tree_cpu_io_mixed_tg
Ignored benchmarks (2) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: bpe_tokeniser, unpack_sequence

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.06x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: 6.62x
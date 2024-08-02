# Results vs. 3.13.0b2

- fork: brandtbucher
- ref: no_cold_exits
- machine: darwin-arm64
- commit hash: a1bdb94
- commit date: 2024-06-18
- overall geometric mean: 1.02x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x slower
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240618-darwin-arm64-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94 |
|----------------|:----------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 161 ms                                                     | 170 ms: 1.05x slower                                                 |
| docutils       | 1.44 sec                                                   | 1.50 sec: 1.04x slower                                               |
| html5lib       | 31.2 ms                                                    | 30.7 ms: 1.01x faster                                                |
| Geometric mean | (ref)                                                      | 1.02x slower                                                         |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240618-darwin-arm64-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94 |
|----------------------------------|:----------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_eager_cpu_io_mixed_tg | 331 ms                                                     | 332 ms: 1.01x slower                                                 |
| async_tree_eager_cpu_io_mixed    | 358 ms                                                     | 362 ms: 1.01x slower                                                 |
| async_tree_eager_tg              | 41.4 ms                                                    | 42.3 ms: 1.02x slower                                                |
| async_tree_none                  | 209 ms                                                     | 217 ms: 1.03x slower                                                 |
| async_tree_eager                 | 60.3 ms                                                    | 63.4 ms: 1.05x slower                                                |
| async_tree_memoization_tg        | 240 ms                                                     | 253 ms: 1.06x slower                                                 |
| Geometric mean                   | (ref)                                                      | 1.02x slower                                                         |

Benchmark hidden because not significant (10): async_tree_io_tg, async_tree_eager_io, async_tree_none_tg, async_tree_eager_memoization_tg, async_tree_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_cpu_io_mixed, async_tree_eager_memoization, async_tree_io, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240618-darwin-arm64-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94 |
|----------------|:----------------------------------------------------------:|:--------------------------------------------------------------------:|
| float          | 48.6 ms                                                    | 46.4 ms: 1.05x faster                                                |
| pidigits       | 282 ms                                                     | 286 ms: 1.01x slower                                                 |
| nbody          | 59.6 ms                                                    | 63.6 ms: 1.07x slower                                                |
| Geometric mean | (ref)                                                      | 1.01x slower                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240618-darwin-arm64-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94 |
|----------------|:----------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_effbot   | 2.58 ms                                                    | 2.56 ms: 1.01x faster                                                |
| regex_v8       | 17.3 ms                                                    | 17.4 ms: 1.01x slower                                                |
| regex_compile  | 68.5 ms                                                    | 72.1 ms: 1.05x slower                                                |
| Geometric mean | (ref)                                                      | 1.01x slower                                                         |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240618-darwin-arm64-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94 |
|----------------------|:----------------------------------------------------------:|:--------------------------------------------------------------------:|
| tomli_loads          | 1.47 sec                                                   | 1.27 sec: 1.16x faster                                               |
| unpickle_pure_python | 141 us                                                     | 132 us: 1.07x faster                                                 |
| xml_etree_process    | 37.1 ms                                                    | 36.1 ms: 1.03x faster                                                |
| pickle_pure_python   | 179 us                                                     | 176 us: 1.02x faster                                                 |
| xml_etree_generate   | 52.7 ms                                                    | 52.2 ms: 1.01x faster                                                |
| json_dumps           | 6.23 ms                                                    | 6.26 ms: 1.01x slower                                                |
| json_loads           | 16.8 us                                                    | 17.0 us: 1.01x slower                                                |
| pickle_dict          | 18.3 us                                                    | 18.6 us: 1.01x slower                                                |
| unpickle_list        | 2.88 us                                                    | 2.93 us: 1.02x slower                                                |
| pickle_list          | 2.96 us                                                    | 3.02 us: 1.02x slower                                                |
| unpickle             | 9.12 us                                                    | 9.32 us: 1.02x slower                                                |
| Geometric mean       | (ref)                                                      | 1.01x faster                                                         |

Benchmark hidden because not significant (3): xml_etree_iterparse, pickle, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240618-darwin-arm64-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94 |
|----------------|:----------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup | 15.2 ms                                                    | 14.9 ms: 1.01x faster                                                |
| Geometric mean | (ref)                                                      | 1.01x faster                                                         |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240618-darwin-arm64-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94 |
|-----------------|:----------------------------------------------------------:|:--------------------------------------------------------------------:|
| mako            | 6.99 ms                                                    | 6.46 ms: 1.08x faster                                                |
| django_template | 19.4 ms                                                    | 21.9 ms: 1.13x slower                                                |
| genshi_text     | 13.9 ms                                                    | 15.9 ms: 1.15x slower                                                |
| genshi_xml      | 29.9 ms                                                    | 40.3 ms: 1.35x slower                                                |
| Geometric mean  | (ref)                                                      | 1.13x slower                                                         |

All benchmarks:
===============

| Benchmark                        | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240618-darwin-arm64-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94 |
|----------------------------------|:----------------------------------------------------------:|:--------------------------------------------------------------------:|
| deepcopy_memo                    | 22.6 us                                                    | 16.8 us: 1.34x faster                                                |
| deepcopy                         | 204 us                                                     | 155 us: 1.32x faster                                                 |
| deepcopy_reduce                  | 1.82 us                                                    | 1.55 us: 1.18x faster                                                |
| tomli_loads                      | 1.47 sec                                                   | 1.27 sec: 1.16x faster                                               |
| mako                             | 6.99 ms                                                    | 6.46 ms: 1.08x faster                                                |
| mdp                              | 1.53 sec                                                   | 1.44 sec: 1.07x faster                                               |
| unpickle_pure_python             | 141 us                                                     | 132 us: 1.07x faster                                                 |
| richards                         | 31.8 ms                                                    | 30.4 ms: 1.05x faster                                                |
| float                            | 48.6 ms                                                    | 46.4 ms: 1.05x faster                                                |
| richards_super                   | 35.2 ms                                                    | 34.3 ms: 1.03x faster                                                |
| xml_etree_process                | 37.1 ms                                                    | 36.1 ms: 1.03x faster                                                |
| pickle_pure_python               | 179 us                                                     | 176 us: 1.02x faster                                                 |
| pyflate                          | 321 ms                                                     | 316 ms: 1.02x faster                                                 |
| fannkuch                         | 248 ms                                                     | 244 ms: 1.02x faster                                                 |
| html5lib                         | 31.2 ms                                                    | 30.7 ms: 1.01x faster                                                |
| python_startup                   | 15.2 ms                                                    | 14.9 ms: 1.01x faster                                                |
| logging_simple                   | 3.04 us                                                    | 3.01 us: 1.01x faster                                                |
| telco                            | 4.60 ms                                                    | 4.55 ms: 1.01x faster                                                |
| xml_etree_generate               | 52.7 ms                                                    | 52.2 ms: 1.01x faster                                                |
| regex_effbot                     | 2.58 ms                                                    | 2.56 ms: 1.01x faster                                                |
| create_gc_cycles                 | 897 us                                                     | 894 us: 1.00x faster                                                 |
| gc_traversal                     | 2.45 ms                                                    | 2.46 ms: 1.00x slower                                                |
| async_tree_eager_cpu_io_mixed_tg | 331 ms                                                     | 332 ms: 1.01x slower                                                 |
| json_dumps                       | 6.23 ms                                                    | 6.26 ms: 1.01x slower                                                |
| go                               | 101 ms                                                     | 101 ms: 1.01x slower                                                 |
| regex_v8                         | 17.3 ms                                                    | 17.4 ms: 1.01x slower                                                |
| thrift                           | 435 us                                                     | 438 us: 1.01x slower                                                 |
| json_loads                       | 16.8 us                                                    | 17.0 us: 1.01x slower                                                |
| coroutines                       | 15.8 ms                                                    | 16.0 ms: 1.01x slower                                                |
| async_tree_eager_cpu_io_mixed    | 358 ms                                                     | 362 ms: 1.01x slower                                                 |
| generators                       | 22.9 ms                                                    | 23.2 ms: 1.01x slower                                                |
| sqlite_synth                     | 1.55 us                                                    | 1.57 us: 1.01x slower                                                |
| pidigits                         | 282 ms                                                     | 286 ms: 1.01x slower                                                 |
| spectral_norm                    | 66.4 ms                                                    | 67.3 ms: 1.01x slower                                                |
| pickle_dict                      | 18.3 us                                                    | 18.6 us: 1.01x slower                                                |
| unpickle_list                    | 2.88 us                                                    | 2.93 us: 1.02x slower                                                |
| bpe_tokeniser                    | 3.05 sec                                                   | 3.12 sec: 1.02x slower                                               |
| pickle_list                      | 2.96 us                                                    | 3.02 us: 1.02x slower                                                |
| unpickle                         | 9.12 us                                                    | 9.32 us: 1.02x slower                                                |
| async_tree_eager_tg              | 41.4 ms                                                    | 42.3 ms: 1.02x slower                                                |
| pprint_safe_repr                 | 465 ms                                                     | 475 ms: 1.02x slower                                                 |
| meteor_contest                   | 70.3 ms                                                    | 72.1 ms: 1.02x slower                                                |
| scimark_monte_carlo              | 42.5 ms                                                    | 43.6 ms: 1.03x slower                                                |
| coverage                         | 45.0 ms                                                    | 46.3 ms: 1.03x slower                                                |
| pprint_pformat                   | 947 ms                                                     | 976 ms: 1.03x slower                                                 |
| bench_mp_pool                    | 47.2 ms                                                    | 48.7 ms: 1.03x slower                                                |
| scimark_fft                      | 181 ms                                                     | 187 ms: 1.03x slower                                                 |
| async_tree_none                  | 209 ms                                                     | 217 ms: 1.03x slower                                                 |
| logging_silent                   | 60.1 ns                                                    | 62.5 ns: 1.04x slower                                                |
| crypto_pyaes                     | 49.5 ms                                                    | 51.5 ms: 1.04x slower                                                |
| docutils                         | 1.44 sec                                                   | 1.50 sec: 1.04x slower                                               |
| async_generators                 | 281 ms                                                     | 294 ms: 1.05x slower                                                 |
| async_tree_eager                 | 60.3 ms                                                    | 63.4 ms: 1.05x slower                                                |
| regex_compile                    | 68.5 ms                                                    | 72.1 ms: 1.05x slower                                                |
| scimark_sparse_mat_mult          | 2.77 ms                                                    | 2.92 ms: 1.05x slower                                                |
| 2to3                             | 161 ms                                                     | 170 ms: 1.05x slower                                                 |
| sympy_str                        | 131 ms                                                     | 139 ms: 1.05x slower                                                 |
| async_tree_memoization_tg        | 240 ms                                                     | 253 ms: 1.06x slower                                                 |
| sympy_expand                     | 226 ms                                                     | 239 ms: 1.06x slower                                                 |
| bench_thread_pool                | 447 us                                                     | 472 us: 1.06x slower                                                 |
| sympy_integrate                  | 10.3 ms                                                    | 10.9 ms: 1.06x slower                                                |
| sympy_sum                        | 69.2 ms                                                    | 73.4 ms: 1.06x slower                                                |
| pycparser                        | 632 ms                                                     | 672 ms: 1.06x slower                                                 |
| sqlglot_normalize                | 166 ms                                                     | 177 ms: 1.07x slower                                                 |
| nbody                            | 59.6 ms                                                    | 63.6 ms: 1.07x slower                                                |
| sqlglot_optimize                 | 30.9 ms                                                    | 33.1 ms: 1.07x slower                                                |
| typing_runtime_protocols         | 87.6 us                                                    | 94.1 us: 1.08x slower                                                |
| scimark_sor                      | 94.9 ms                                                    | 102 ms: 1.08x slower                                                 |
| pylint                           | 170 ms                                                     | 183 ms: 1.08x slower                                                 |
| hexiom                           | 4.06 ms                                                    | 4.44 ms: 1.10x slower                                                |
| nqueens                          | 52.2 ms                                                    | 57.3 ms: 1.10x slower                                                |
| raytrace                         | 147 ms                                                     | 162 ms: 1.10x slower                                                 |
| deltablue                        | 2.14 ms                                                    | 2.36 ms: 1.10x slower                                                |
| sqlglot_transpile                | 891 us                                                     | 994 us: 1.12x slower                                                 |
| django_template                  | 19.4 ms                                                    | 21.9 ms: 1.13x slower                                                |
| sqlglot_parse                    | 732 us                                                     | 827 us: 1.13x slower                                                 |
| chaos                            | 34.0 ms                                                    | 39.0 ms: 1.15x slower                                                |
| genshi_text                      | 13.9 ms                                                    | 15.9 ms: 1.15x slower                                                |
| scimark_lu                       | 66.9 ms                                                    | 80.8 ms: 1.21x slower                                                |
| comprehensions                   | 10.2 us                                                    | 12.3 us: 1.21x slower                                                |
| genshi_xml                       | 29.9 ms                                                    | 40.3 ms: 1.35x slower                                                |
| Geometric mean                   | (ref)                                                      | 1.02x slower                                                         |

Benchmark hidden because not significant (23): async_tree_io_tg, async_tree_eager_io, async_tree_none_tg, xml_etree_iterparse, asyncio_tcp_ssl, logging_format, regex_dna, asyncio_websockets, python_startup_no_site, pickle, json, xml_etree_parse, tornado_http, pathlib, async_tree_eager_memoization_tg, async_tree_cpu_io_mixed_tg, async_tree_eager_io_tg, dask, async_tree_cpu_io_mixed, async_tree_eager_memoization, async_tree_io, async_tree_memoization, asyncio_tcp
Ignored benchmarks (6) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dulwich_log, flaskblogging, gunicorn, mypy2

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: 1.10x
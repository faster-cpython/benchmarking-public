# Results vs. 3.13.0b2

- fork: python
- ref: v3.14.0a1
- machine: darwin-arm64
- commit hash: 8cdaca8
- commit date: 2024-10-15
- overall geometric mean: 1.00x slower
- HPT reliability: 94.79%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.11x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241015-darwin-arm64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| 2to3           | 161 ms                                                     | 160 ms: 1.01x faster                                       |
| docutils       | 1.44 sec                                                   | 1.41 sec: 1.02x faster                                     |
| html5lib       | 31.2 ms                                                    | 31.8 ms: 1.02x slower                                      |
| Geometric mean | (ref)                                                      | 1.03x slower                                               |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241015-darwin-arm64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------------------------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| async_tree_eager_io              | 766 ms                                                     | 654 ms: 1.17x faster                                       |
| async_tree_eager_io_tg           | 768 ms                                                     | 704 ms: 1.09x faster                                       |
| async_tree_memoization           | 260 ms                                                     | 243 ms: 1.07x faster                                       |
| async_tree_none                  | 209 ms                                                     | 196 ms: 1.07x faster                                       |
| async_tree_memoization_tg        | 240 ms                                                     | 233 ms: 1.03x faster                                       |
| async_tree_cpu_io_mixed          | 467 ms                                                     | 455 ms: 1.03x faster                                       |
| async_tree_eager                 | 60.3 ms                                                    | 59.0 ms: 1.02x faster                                      |
| async_tree_eager_cpu_io_mixed_tg | 331 ms                                                     | 333 ms: 1.01x slower                                       |
| async_tree_eager_memoization_tg  | 126 ms                                                     | 129 ms: 1.03x slower                                       |
| async_tree_cpu_io_mixed_tg       | 451 ms                                                     | 468 ms: 1.04x slower                                       |
| async_tree_none_tg               | 198 ms                                                     | 213 ms: 1.08x slower                                       |
| async_tree_io_tg                 | 565 ms                                                     | 611 ms: 1.08x slower                                       |
| Geometric mean                   | (ref)                                                      | 1.01x faster                                               |

Benchmark hidden because not significant (4): async_tree_eager_memoization, async_tree_eager_cpu_io_mixed, async_tree_eager_tg, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241015-darwin-arm64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| pidigits       | 282 ms                                                     | 283 ms: 1.00x slower                                       |
| float          | 48.6 ms                                                    | 49.7 ms: 1.02x slower                                      |
| nbody          | 59.6 ms                                                    | 65.5 ms: 1.10x slower                                      |
| Geometric mean | (ref)                                                      | 1.04x slower                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241015-darwin-arm64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| regex_v8       | 17.3 ms                                                    | 16.5 ms: 1.05x faster                                      |
| regex_dna      | 149 ms                                                     | 146 ms: 1.02x faster                                       |
| regex_compile  | 68.5 ms                                                    | 68.4 ms: 1.00x faster                                      |
| regex_effbot   | 2.58 ms                                                    | 2.59 ms: 1.00x slower                                      |
| Geometric mean | (ref)                                                      | 1.02x faster                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241015-darwin-arm64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| json_loads           | 16.8 us                                                    | 16.4 us: 1.03x faster                                      |
| pickle               | 7.48 us                                                    | 7.33 us: 1.02x faster                                      |
| pickle_dict          | 18.3 us                                                    | 18.1 us: 1.01x faster                                      |
| unpickle             | 9.12 us                                                    | 9.03 us: 1.01x faster                                      |
| xml_etree_generate   | 52.7 ms                                                    | 52.5 ms: 1.00x faster                                      |
| pickle_list          | 2.96 us                                                    | 2.98 us: 1.01x slower                                      |
| xml_etree_process    | 37.1 ms                                                    | 37.5 ms: 1.01x slower                                      |
| unpickle_pure_python | 141 us                                                     | 143 us: 1.02x slower                                       |
| tomli_loads          | 1.47 sec                                                   | 1.50 sec: 1.02x slower                                     |
| xml_etree_parse      | 106 ms                                                     | 109 ms: 1.03x slower                                       |
| pickle_pure_python   | 179 us                                                     | 186 us: 1.04x slower                                       |
| unpickle_list        | 2.88 us                                                    | 3.01 us: 1.05x slower                                      |
| xml_etree_iterparse  | 71.5 ms                                                    | 75.1 ms: 1.05x slower                                      |
| json_dumps           | 6.23 ms                                                    | 7.18 ms: 1.15x slower                                      |
| Geometric mean       | (ref)                                                      | 1.02x slower                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241015-darwin-arm64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|------------------------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| python_startup_no_site | 12.3 ms                                                    | 14.7 ms: 1.20x slower                                      |
| python_startup         | 15.2 ms                                                    | 19.0 ms: 1.25x slower                                      |
| Geometric mean         | (ref)                                                      | 1.23x slower                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241015-darwin-arm64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|-----------------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| genshi_text     | 13.9 ms                                                    | 13.7 ms: 1.02x faster                                      |
| genshi_xml      | 29.9 ms                                                    | 29.8 ms: 1.00x faster                                      |
| mako            | 6.99 ms                                                    | 7.01 ms: 1.00x slower                                      |
| django_template | 19.4 ms                                                    | 19.8 ms: 1.02x slower                                      |
| Geometric mean  | (ref)                                                      | 1.00x slower                                               |

All benchmarks:
===============

| Benchmark                        | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241015-darwin-arm64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------------------------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| asyncio_websockets               | 409 ms                                                     | 241 ms: 1.70x faster                                       |
| deepcopy                         | 204 us                                                     | 146 us: 1.40x faster                                       |
| deepcopy_memo                    | 22.6 us                                                    | 17.4 us: 1.30x faster                                      |
| go                               | 101 ms                                                     | 82.1 ms: 1.22x faster                                      |
| deepcopy_reduce                  | 1.82 us                                                    | 1.52 us: 1.20x faster                                      |
| async_tree_eager_io              | 766 ms                                                     | 654 ms: 1.17x faster                                       |
| generators                       | 22.9 ms                                                    | 20.1 ms: 1.14x faster                                      |
| async_tree_eager_io_tg           | 768 ms                                                     | 704 ms: 1.09x faster                                       |
| async_tree_memoization           | 260 ms                                                     | 243 ms: 1.07x faster                                       |
| async_tree_none                  | 209 ms                                                     | 196 ms: 1.07x faster                                       |
| pathlib                          | 23.3 ms                                                    | 22.0 ms: 1.06x faster                                      |
| mdp                              | 1.53 sec                                                   | 1.46 sec: 1.05x faster                                     |
| regex_v8                         | 17.3 ms                                                    | 16.5 ms: 1.05x faster                                      |
| thrift                           | 435 us                                                     | 416 us: 1.05x faster                                       |
| bench_thread_pool                | 447 us                                                     | 433 us: 1.03x faster                                       |
| async_tree_memoization_tg        | 240 ms                                                     | 233 ms: 1.03x faster                                       |
| async_tree_cpu_io_mixed          | 467 ms                                                     | 455 ms: 1.03x faster                                       |
| json_loads                       | 16.8 us                                                    | 16.4 us: 1.03x faster                                      |
| richards                         | 31.8 ms                                                    | 31.0 ms: 1.03x faster                                      |
| richards_super                   | 35.2 ms                                                    | 34.3 ms: 1.03x faster                                      |
| docutils                         | 1.44 sec                                                   | 1.41 sec: 1.02x faster                                     |
| regex_dna                        | 149 ms                                                     | 146 ms: 1.02x faster                                       |
| async_tree_eager                 | 60.3 ms                                                    | 59.0 ms: 1.02x faster                                      |
| pickle                           | 7.48 us                                                    | 7.33 us: 1.02x faster                                      |
| json                             | 2.93 ms                                                    | 2.87 ms: 1.02x faster                                      |
| sqlite_synth                     | 1.55 us                                                    | 1.52 us: 1.02x faster                                      |
| async_generators                 | 281 ms                                                     | 276 ms: 1.02x faster                                       |
| telco                            | 4.60 ms                                                    | 4.53 ms: 1.02x faster                                      |
| genshi_text                      | 13.9 ms                                                    | 13.7 ms: 1.02x faster                                      |
| pickle_dict                      | 18.3 us                                                    | 18.1 us: 1.01x faster                                      |
| pprint_pformat                   | 947 ms                                                     | 936 ms: 1.01x faster                                       |
| unpickle                         | 9.12 us                                                    | 9.03 us: 1.01x faster                                      |
| dulwich_log                      | 27.6 ms                                                    | 27.3 ms: 1.01x faster                                      |
| 2to3                             | 161 ms                                                     | 160 ms: 1.01x faster                                       |
| pprint_safe_repr                 | 465 ms                                                     | 462 ms: 1.01x faster                                       |
| coverage                         | 45.0 ms                                                    | 44.8 ms: 1.01x faster                                      |
| xml_etree_generate               | 52.7 ms                                                    | 52.5 ms: 1.00x faster                                      |
| genshi_xml                       | 29.9 ms                                                    | 29.8 ms: 1.00x faster                                      |
| regex_compile                    | 68.5 ms                                                    | 68.4 ms: 1.00x faster                                      |
| meteor_contest                   | 70.3 ms                                                    | 70.5 ms: 1.00x slower                                      |
| regex_effbot                     | 2.58 ms                                                    | 2.59 ms: 1.00x slower                                      |
| mako                             | 6.99 ms                                                    | 7.01 ms: 1.00x slower                                      |
| pidigits                         | 282 ms                                                     | 283 ms: 1.00x slower                                       |
| sqlglot_normalize                | 166 ms                                                     | 166 ms: 1.00x slower                                       |
| sympy_expand                     | 226 ms                                                     | 227 ms: 1.01x slower                                       |
| sqlglot_optimize                 | 30.9 ms                                                    | 31.1 ms: 1.01x slower                                      |
| sympy_sum                        | 69.2 ms                                                    | 69.6 ms: 1.01x slower                                      |
| async_tree_eager_cpu_io_mixed_tg | 331 ms                                                     | 333 ms: 1.01x slower                                       |
| pickle_list                      | 2.96 us                                                    | 2.98 us: 1.01x slower                                      |
| xml_etree_process                | 37.1 ms                                                    | 37.5 ms: 1.01x slower                                      |
| scimark_sor                      | 94.9 ms                                                    | 95.9 ms: 1.01x slower                                      |
| sqlglot_transpile                | 891 us                                                     | 901 us: 1.01x slower                                       |
| logging_simple                   | 3.04 us                                                    | 3.08 us: 1.01x slower                                      |
| logging_silent                   | 60.1 ns                                                    | 60.9 ns: 1.01x slower                                      |
| logging_format                   | 3.31 us                                                    | 3.35 us: 1.01x slower                                      |
| sympy_str                        | 131 ms                                                     | 133 ms: 1.01x slower                                       |
| bpe_tokeniser                    | 3.05 sec                                                   | 3.10 sec: 1.01x slower                                     |
| sqlglot_parse                    | 732 us                                                     | 743 us: 1.02x slower                                       |
| unpickle_pure_python             | 141 us                                                     | 143 us: 1.02x slower                                       |
| hexiom                           | 4.06 ms                                                    | 4.13 ms: 1.02x slower                                      |
| django_template                  | 19.4 ms                                                    | 19.8 ms: 1.02x slower                                      |
| pyflate                          | 321 ms                                                     | 327 ms: 1.02x slower                                       |
| scimark_sparse_mat_mult          | 2.77 ms                                                    | 2.83 ms: 1.02x slower                                      |
| html5lib                         | 31.2 ms                                                    | 31.8 ms: 1.02x slower                                      |
| scimark_lu                       | 66.9 ms                                                    | 68.2 ms: 1.02x slower                                      |
| float                            | 48.6 ms                                                    | 49.7 ms: 1.02x slower                                      |
| tomli_loads                      | 1.47 sec                                                   | 1.50 sec: 1.02x slower                                     |
| nqueens                          | 52.2 ms                                                    | 53.6 ms: 1.03x slower                                      |
| scimark_monte_carlo              | 42.5 ms                                                    | 43.6 ms: 1.03x slower                                      |
| xml_etree_parse                  | 106 ms                                                     | 109 ms: 1.03x slower                                       |
| async_tree_eager_memoization_tg  | 126 ms                                                     | 129 ms: 1.03x slower                                       |
| async_tree_cpu_io_mixed_tg       | 451 ms                                                     | 468 ms: 1.04x slower                                       |
| pickle_pure_python               | 179 us                                                     | 186 us: 1.04x slower                                       |
| deltablue                        | 2.14 ms                                                    | 2.23 ms: 1.04x slower                                      |
| coroutines                       | 15.8 ms                                                    | 16.5 ms: 1.04x slower                                      |
| crypto_pyaes                     | 49.5 ms                                                    | 51.7 ms: 1.04x slower                                      |
| unpickle_list                    | 2.88 us                                                    | 3.01 us: 1.05x slower                                      |
| raytrace                         | 147 ms                                                     | 154 ms: 1.05x slower                                       |
| xml_etree_iterparse              | 71.5 ms                                                    | 75.1 ms: 1.05x slower                                      |
| scimark_fft                      | 181 ms                                                     | 190 ms: 1.05x slower                                       |
| typing_runtime_protocols         | 87.6 us                                                    | 92.3 us: 1.05x slower                                      |
| spectral_norm                    | 66.4 ms                                                    | 70.2 ms: 1.06x slower                                      |
| sympy_integrate                  | 10.3 ms                                                    | 11.0 ms: 1.06x slower                                      |
| fannkuch                         | 248 ms                                                     | 268 ms: 1.08x slower                                       |
| async_tree_none_tg               | 198 ms                                                     | 213 ms: 1.08x slower                                       |
| async_tree_io_tg                 | 565 ms                                                     | 611 ms: 1.08x slower                                       |
| asyncio_tcp                      | 402 ms                                                     | 437 ms: 1.09x slower                                       |
| comprehensions                   | 10.2 us                                                    | 11.1 us: 1.10x slower                                      |
| chaos                            | 34.0 ms                                                    | 37.3 ms: 1.10x slower                                      |
| nbody                            | 59.6 ms                                                    | 65.5 ms: 1.10x slower                                      |
| json_dumps                       | 6.23 ms                                                    | 7.18 ms: 1.15x slower                                      |
| python_startup_no_site           | 12.3 ms                                                    | 14.7 ms: 1.20x slower                                      |
| gc_traversal                     | 2.45 ms                                                    | 2.94 ms: 1.20x slower                                      |
| bench_mp_pool                    | 47.2 ms                                                    | 58.9 ms: 1.25x slower                                      |
| python_startup                   | 15.2 ms                                                    | 19.0 ms: 1.25x slower                                      |
| create_gc_cycles                 | 897 us                                                     | 1.30 ms: 1.45x slower                                      |
| Geometric mean                   | (ref)                                                      | 1.00x slower                                               |

Benchmark hidden because not significant (8): async_tree_eager_memoization, async_tree_eager_cpu_io_mixed, async_tree_eager_tg, asyncio_tcp_ssl, pycparser, async_tree_io, pylint, tornado_http
Ignored benchmarks (6) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2
Ignored benchmarks (2) of results/bm-20241015-3.14.0a1-8cdaca8/bm-20241015-darwin-arm64-python-v3.14.0a1-3.14.0a1-8cdaca8.json: sphinx, unpack_sequence

# HPT report

- Reliability score: 94.79% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.11x
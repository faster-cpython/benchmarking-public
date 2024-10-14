# Results vs. 3.13.0b2

- fork: Fidget-Spinner
- ref: fix_unsafe_refcounti
- machine: darwin-arm64
- commit hash: 8278d07
- commit date: 2024-10-12
- overall geometric mean: 1.00x slower
- HPT reliability: 99.07%
- HPT 99th percentile: 1.00x slower
- Memory change: 0.57x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241012-darwin-arm64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 161 ms                                                     | 196 ms: 1.22x slower                                                            |
| docutils       | 1.44 sec                                                   | 1.41 sec: 1.02x faster                                                          |
| html5lib       | 31.2 ms                                                    | 32.0 ms: 1.03x slower                                                           |
| Geometric mean | (ref)                                                      | 1.08x slower                                                                    |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241012-darwin-arm64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|----------------------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_eager_io              | 766 ms                                                     | 677 ms: 1.13x faster                                                            |
| async_tree_none                  | 209 ms                                                     | 192 ms: 1.09x faster                                                            |
| async_tree_eager_io_tg           | 768 ms                                                     | 711 ms: 1.08x faster                                                            |
| async_tree_eager                 | 60.3 ms                                                    | 59.7 ms: 1.01x faster                                                           |
| async_tree_eager_cpu_io_mixed    | 358 ms                                                     | 362 ms: 1.01x slower                                                            |
| async_tree_eager_tg              | 41.4 ms                                                    | 41.9 ms: 1.01x slower                                                           |
| async_tree_eager_cpu_io_mixed_tg | 331 ms                                                     | 337 ms: 1.02x slower                                                            |
| async_tree_io                    | 563 ms                                                     | 593 ms: 1.05x slower                                                            |
| Geometric mean                   | (ref)                                                      | 1.01x faster                                                                    |

Benchmark hidden because not significant (8): async_tree_memoization, async_tree_cpu_io_mixed, async_tree_io_tg, async_tree_none_tg, async_tree_eager_memoization_tg, async_tree_cpu_io_mixed_tg, async_tree_memoization_tg, async_tree_eager_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241012-darwin-arm64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pidigits       | 282 ms                                                     | 283 ms: 1.00x slower                                                            |
| float          | 48.6 ms                                                    | 49.0 ms: 1.01x slower                                                           |
| nbody          | 59.6 ms                                                    | 65.6 ms: 1.10x slower                                                           |
| Geometric mean | (ref)                                                      | 1.04x slower                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241012-darwin-arm64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_v8       | 17.3 ms                                                    | 16.5 ms: 1.05x faster                                                           |
| regex_dna      | 149 ms                                                     | 146 ms: 1.02x faster                                                            |
| regex_compile  | 68.5 ms                                                    | 68.3 ms: 1.00x faster                                                           |
| regex_effbot   | 2.58 ms                                                    | 2.60 ms: 1.00x slower                                                           |
| Geometric mean | (ref)                                                      | 1.02x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241012-darwin-arm64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|----------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| json_loads           | 16.8 us                                                    | 16.4 us: 1.03x faster                                                           |
| pickle               | 7.48 us                                                    | 7.34 us: 1.02x faster                                                           |
| pickle_list          | 2.96 us                                                    | 2.91 us: 1.02x faster                                                           |
| xml_etree_generate   | 52.7 ms                                                    | 52.4 ms: 1.01x faster                                                           |
| pickle_dict          | 18.3 us                                                    | 18.2 us: 1.01x faster                                                           |
| xml_etree_process    | 37.1 ms                                                    | 37.4 ms: 1.01x slower                                                           |
| unpickle_pure_python | 141 us                                                     | 142 us: 1.01x slower                                                            |
| tomli_loads          | 1.47 sec                                                   | 1.49 sec: 1.02x slower                                                          |
| xml_etree_iterparse  | 71.5 ms                                                    | 73.1 ms: 1.02x slower                                                           |
| xml_etree_parse      | 106 ms                                                     | 108 ms: 1.02x slower                                                            |
| pickle_pure_python   | 179 us                                                     | 183 us: 1.03x slower                                                            |
| unpickle_list        | 2.88 us                                                    | 2.99 us: 1.04x slower                                                           |
| json_dumps           | 6.23 ms                                                    | 7.25 ms: 1.16x slower                                                           |
| Geometric mean       | (ref)                                                      | 1.02x slower                                                                    |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241012-darwin-arm64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|------------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 15.2 ms                                                    | 19.0 ms: 1.25x slower                                                           |
| python_startup_no_site | 12.3 ms                                                    | 15.9 ms: 1.29x slower                                                           |
| Geometric mean         | (ref)                                                      | 1.27x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241012-darwin-arm64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|-----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| genshi_text     | 13.9 ms                                                    | 13.7 ms: 1.02x faster                                                           |
| django_template | 19.4 ms                                                    | 20.0 ms: 1.03x slower                                                           |
| Geometric mean  | (ref)                                                      | 1.00x slower                                                                    |

Benchmark hidden because not significant (2): genshi_xml, mako

All benchmarks:
===============

| Benchmark                        | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241012-darwin-arm64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|----------------------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| asyncio_websockets               | 409 ms                                                     | 242 ms: 1.69x faster                                                            |
| deepcopy                         | 204 us                                                     | 147 us: 1.39x faster                                                            |
| deepcopy_memo                    | 22.6 us                                                    | 17.3 us: 1.31x faster                                                           |
| go                               | 101 ms                                                     | 81.8 ms: 1.23x faster                                                           |
| deepcopy_reduce                  | 1.82 us                                                    | 1.53 us: 1.19x faster                                                           |
| async_tree_eager_io              | 766 ms                                                     | 677 ms: 1.13x faster                                                            |
| generators                       | 22.9 ms                                                    | 20.3 ms: 1.13x faster                                                           |
| async_tree_none                  | 209 ms                                                     | 192 ms: 1.09x faster                                                            |
| async_tree_eager_io_tg           | 768 ms                                                     | 711 ms: 1.08x faster                                                            |
| pathlib                          | 23.3 ms                                                    | 22.0 ms: 1.06x faster                                                           |
| regex_v8                         | 17.3 ms                                                    | 16.5 ms: 1.05x faster                                                           |
| mdp                              | 1.53 sec                                                   | 1.47 sec: 1.05x faster                                                          |
| thrift                           | 435 us                                                     | 419 us: 1.04x faster                                                            |
| json                             | 2.93 ms                                                    | 2.82 ms: 1.04x faster                                                           |
| coverage                         | 45.0 ms                                                    | 43.6 ms: 1.03x faster                                                           |
| json_loads                       | 16.8 us                                                    | 16.4 us: 1.03x faster                                                           |
| sqlite_synth                     | 1.55 us                                                    | 1.52 us: 1.02x faster                                                           |
| richards                         | 31.8 ms                                                    | 31.2 ms: 1.02x faster                                                           |
| pickle                           | 7.48 us                                                    | 7.34 us: 1.02x faster                                                           |
| docutils                         | 1.44 sec                                                   | 1.41 sec: 1.02x faster                                                          |
| regex_dna                        | 149 ms                                                     | 146 ms: 1.02x faster                                                            |
| genshi_text                      | 13.9 ms                                                    | 13.7 ms: 1.02x faster                                                           |
| pickle_list                      | 2.96 us                                                    | 2.91 us: 1.02x faster                                                           |
| richards_super                   | 35.2 ms                                                    | 34.8 ms: 1.01x faster                                                           |
| async_tree_eager                 | 60.3 ms                                                    | 59.7 ms: 1.01x faster                                                           |
| pprint_safe_repr                 | 465 ms                                                     | 461 ms: 1.01x faster                                                            |
| async_generators                 | 281 ms                                                     | 279 ms: 1.01x faster                                                            |
| telco                            | 4.60 ms                                                    | 4.57 ms: 1.01x faster                                                           |
| dulwich_log                      | 27.6 ms                                                    | 27.4 ms: 1.01x faster                                                           |
| xml_etree_generate               | 52.7 ms                                                    | 52.4 ms: 1.01x faster                                                           |
| pickle_dict                      | 18.3 us                                                    | 18.2 us: 1.01x faster                                                           |
| pprint_pformat                   | 947 ms                                                     | 943 ms: 1.00x faster                                                            |
| regex_compile                    | 68.5 ms                                                    | 68.3 ms: 1.00x faster                                                           |
| sympy_expand                     | 226 ms                                                     | 225 ms: 1.00x faster                                                            |
| sqlglot_optimize                 | 30.9 ms                                                    | 31.0 ms: 1.00x slower                                                           |
| logging_simple                   | 3.04 us                                                    | 3.05 us: 1.00x slower                                                           |
| sqlglot_normalize                | 166 ms                                                     | 166 ms: 1.00x slower                                                            |
| pidigits                         | 282 ms                                                     | 283 ms: 1.00x slower                                                            |
| regex_effbot                     | 2.58 ms                                                    | 2.60 ms: 1.00x slower                                                           |
| logging_silent                   | 60.1 ns                                                    | 60.6 ns: 1.01x slower                                                           |
| float                            | 48.6 ms                                                    | 49.0 ms: 1.01x slower                                                           |
| sqlglot_transpile                | 891 us                                                     | 898 us: 1.01x slower                                                            |
| pycparser                        | 632 ms                                                     | 638 ms: 1.01x slower                                                            |
| bpe_tokeniser                    | 3.05 sec                                                   | 3.08 sec: 1.01x slower                                                          |
| logging_format                   | 3.31 us                                                    | 3.34 us: 1.01x slower                                                           |
| xml_etree_process                | 37.1 ms                                                    | 37.4 ms: 1.01x slower                                                           |
| scimark_sor                      | 94.9 ms                                                    | 95.9 ms: 1.01x slower                                                           |
| async_tree_eager_cpu_io_mixed    | 358 ms                                                     | 362 ms: 1.01x slower                                                            |
| unpickle_pure_python             | 141 us                                                     | 142 us: 1.01x slower                                                            |
| async_tree_eager_tg              | 41.4 ms                                                    | 41.9 ms: 1.01x slower                                                           |
| sympy_str                        | 131 ms                                                     | 133 ms: 1.01x slower                                                            |
| sqlglot_parse                    | 732 us                                                     | 743 us: 1.02x slower                                                            |
| scimark_sparse_mat_mult          | 2.77 ms                                                    | 2.82 ms: 1.02x slower                                                           |
| meteor_contest                   | 70.3 ms                                                    | 71.5 ms: 1.02x slower                                                           |
| bench_thread_pool                | 447 us                                                     | 455 us: 1.02x slower                                                            |
| tomli_loads                      | 1.47 sec                                                   | 1.49 sec: 1.02x slower                                                          |
| async_tree_eager_cpu_io_mixed_tg | 331 ms                                                     | 337 ms: 1.02x slower                                                            |
| pyflate                          | 321 ms                                                     | 327 ms: 1.02x slower                                                            |
| hexiom                           | 4.06 ms                                                    | 4.14 ms: 1.02x slower                                                           |
| gc_traversal                     | 2.45 ms                                                    | 2.50 ms: 1.02x slower                                                           |
| xml_etree_iterparse              | 71.5 ms                                                    | 73.1 ms: 1.02x slower                                                           |
| xml_etree_parse                  | 106 ms                                                     | 108 ms: 1.02x slower                                                            |
| pickle_pure_python               | 179 us                                                     | 183 us: 1.03x slower                                                            |
| html5lib                         | 31.2 ms                                                    | 32.0 ms: 1.03x slower                                                           |
| scimark_monte_carlo              | 42.5 ms                                                    | 43.7 ms: 1.03x slower                                                           |
| django_template                  | 19.4 ms                                                    | 20.0 ms: 1.03x slower                                                           |
| crypto_pyaes                     | 49.5 ms                                                    | 51.2 ms: 1.04x slower                                                           |
| create_gc_cycles                 | 897 us                                                     | 929 us: 1.04x slower                                                            |
| unpickle_list                    | 2.88 us                                                    | 2.99 us: 1.04x slower                                                           |
| nqueens                          | 52.2 ms                                                    | 54.2 ms: 1.04x slower                                                           |
| deltablue                        | 2.14 ms                                                    | 2.22 ms: 1.04x slower                                                           |
| raytrace                         | 147 ms                                                     | 154 ms: 1.05x slower                                                            |
| async_tree_io                    | 563 ms                                                     | 593 ms: 1.05x slower                                                            |
| coroutines                       | 15.8 ms                                                    | 16.7 ms: 1.05x slower                                                           |
| scimark_fft                      | 181 ms                                                     | 190 ms: 1.05x slower                                                            |
| typing_runtime_protocols         | 87.6 us                                                    | 92.9 us: 1.06x slower                                                           |
| sympy_integrate                  | 10.3 ms                                                    | 11.0 ms: 1.06x slower                                                           |
| spectral_norm                    | 66.4 ms                                                    | 70.8 ms: 1.07x slower                                                           |
| bench_mp_pool                    | 47.2 ms                                                    | 50.5 ms: 1.07x slower                                                           |
| fannkuch                         | 248 ms                                                     | 266 ms: 1.07x slower                                                            |
| comprehensions                   | 10.2 us                                                    | 11.0 us: 1.09x slower                                                           |
| asyncio_tcp                      | 402 ms                                                     | 439 ms: 1.09x slower                                                            |
| chaos                            | 34.0 ms                                                    | 37.4 ms: 1.10x slower                                                           |
| nbody                            | 59.6 ms                                                    | 65.6 ms: 1.10x slower                                                           |
| json_dumps                       | 6.23 ms                                                    | 7.25 ms: 1.16x slower                                                           |
| 2to3                             | 161 ms                                                     | 196 ms: 1.22x slower                                                            |
| python_startup                   | 15.2 ms                                                    | 19.0 ms: 1.25x slower                                                           |
| python_startup_no_site           | 12.3 ms                                                    | 15.9 ms: 1.29x slower                                                           |
| Geometric mean                   | (ref)                                                      | 1.00x slower                                                                    |

Benchmark hidden because not significant (16): async_tree_memoization, async_tree_cpu_io_mixed, async_tree_io_tg, async_tree_none_tg, asyncio_tcp_ssl, unpickle, genshi_xml, mako, sympy_sum, scimark_lu, async_tree_eager_memoization_tg, async_tree_cpu_io_mixed_tg, async_tree_memoization_tg, async_tree_eager_memoization, pylint, tornado_http
Ignored benchmarks (6) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2
Ignored benchmarks (1) of results/bm-20241012-3.14.0a0-8278d07/bm-20241012-darwin-arm64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07.json: unpack_sequence

# HPT report

- Reliability score: 99.07% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 0.57x
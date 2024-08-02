# Results vs. 3.13.0b2

- fork: brandtbucher
- ref: justin_align
- machine: darwin-arm64
- commit hash: 0081bcd
- commit date: 2024-05-23
- overall geometric mean: 1.02x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x slower
- Memory change: 0.66x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240523-darwin-arm64-brandtbucher-justin_align-3.14.0a0-0081bcd |
|----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 161 ms                                                     | 171 ms: 1.06x slower                                                |
| chameleon      | 4.27 ms                                                    | 4.44 ms: 1.04x slower                                               |
| docutils       | 1.44 sec                                                   | 1.52 sec: 1.05x slower                                              |
| html5lib       | 31.2 ms                                                    | 30.8 ms: 1.01x faster                                               |
| Geometric mean | (ref)                                                      | 1.03x slower                                                        |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240523-darwin-arm64-brandtbucher-justin_align-3.14.0a0-0081bcd |
|----------------------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_eager_cpu_io_mixed_tg | 331 ms                                                     | 332 ms: 1.01x slower                                                |
| async_tree_eager_cpu_io_mixed    | 358 ms                                                     | 363 ms: 1.01x slower                                                |
| async_tree_eager_tg              | 41.4 ms                                                    | 41.9 ms: 1.01x slower                                               |
| async_tree_none                  | 209 ms                                                     | 216 ms: 1.03x slower                                                |
| async_tree_eager                 | 60.3 ms                                                    | 62.8 ms: 1.04x slower                                               |
| Geometric mean                   | (ref)                                                      | 1.01x slower                                                        |

Benchmark hidden because not significant (11): async_tree_eager_io_tg, async_tree_cpu_io_mixed_tg, async_tree_memoization_tg, async_tree_none_tg, async_tree_io_tg, async_tree_eager_memoization_tg, async_tree_eager_memoization, async_tree_eager_io, async_tree_cpu_io_mixed, async_tree_memoization, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240523-darwin-arm64-brandtbucher-justin_align-3.14.0a0-0081bcd |
|----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------:|
| float          | 48.6 ms                                                    | 47.2 ms: 1.03x faster                                               |
| nbody          | 59.6 ms                                                    | 63.5 ms: 1.07x slower                                               |
| Geometric mean | (ref)                                                      | 1.01x slower                                                        |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240523-darwin-arm64-brandtbucher-justin_align-3.14.0a0-0081bcd |
|----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_effbot   | 2.58 ms                                                    | 2.57 ms: 1.01x faster                                               |
| regex_v8       | 17.3 ms                                                    | 17.4 ms: 1.01x slower                                               |
| regex_compile  | 68.5 ms                                                    | 71.7 ms: 1.05x slower                                               |
| Geometric mean | (ref)                                                      | 1.01x slower                                                        |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240523-darwin-arm64-brandtbucher-justin_align-3.14.0a0-0081bcd |
|----------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------:|
| tomli_loads          | 1.47 sec                                                   | 1.24 sec: 1.18x faster                                              |
| unpickle_pure_python | 141 us                                                     | 131 us: 1.07x faster                                                |
| xml_etree_process    | 37.1 ms                                                    | 35.4 ms: 1.05x faster                                               |
| pickle_pure_python   | 179 us                                                     | 172 us: 1.04x faster                                                |
| xml_etree_generate   | 52.7 ms                                                    | 51.1 ms: 1.03x faster                                               |
| json_dumps           | 6.23 ms                                                    | 6.07 ms: 1.03x faster                                               |
| xml_etree_parse      | 106 ms                                                     | 103 ms: 1.02x faster                                                |
| xml_etree_iterparse  | 71.5 ms                                                    | 70.1 ms: 1.02x faster                                               |
| unpickle_list        | 2.88 us                                                    | 2.83 us: 1.02x faster                                               |
| pickle_dict          | 18.3 us                                                    | 18.1 us: 1.01x faster                                               |
| pickle               | 7.48 us                                                    | 7.46 us: 1.00x faster                                               |
| json_loads           | 16.8 us                                                    | 17.0 us: 1.01x slower                                               |
| pickle_list          | 2.96 us                                                    | 2.98 us: 1.01x slower                                               |
| unpickle             | 9.12 us                                                    | 9.32 us: 1.02x slower                                               |
| Geometric mean       | (ref)                                                      | 1.03x faster                                                        |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240523-darwin-arm64-brandtbucher-justin_align-3.14.0a0-0081bcd |
|------------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 15.2 ms                                                    | 15.7 ms: 1.03x slower                                               |
| python_startup_no_site | 12.3 ms                                                    | 13.2 ms: 1.07x slower                                               |
| Geometric mean         | (ref)                                                      | 1.05x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240523-darwin-arm64-brandtbucher-justin_align-3.14.0a0-0081bcd |
|-----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------:|
| mako            | 6.99 ms                                                    | 6.40 ms: 1.09x faster                                               |
| django_template | 19.4 ms                                                    | 21.0 ms: 1.08x slower                                               |
| genshi_text     | 13.9 ms                                                    | 16.1 ms: 1.16x slower                                               |
| genshi_xml      | 29.9 ms                                                    | 39.5 ms: 1.32x slower                                               |
| Geometric mean  | (ref)                                                      | 1.11x slower                                                        |

All benchmarks:
===============

| Benchmark                        | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240523-darwin-arm64-brandtbucher-justin_align-3.14.0a0-0081bcd |
|----------------------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------:|
| tomli_loads                      | 1.47 sec                                                   | 1.24 sec: 1.18x faster                                              |
| mako                             | 6.99 ms                                                    | 6.40 ms: 1.09x faster                                               |
| unpickle_pure_python             | 141 us                                                     | 131 us: 1.07x faster                                                |
| fannkuch                         | 248 ms                                                     | 234 ms: 1.06x faster                                                |
| deepcopy_memo                    | 22.6 us                                                    | 21.4 us: 1.06x faster                                               |
| pathlib                          | 23.3 ms                                                    | 22.2 ms: 1.05x faster                                               |
| xml_etree_process                | 37.1 ms                                                    | 35.4 ms: 1.05x faster                                               |
| pickle_pure_python               | 179 us                                                     | 172 us: 1.04x faster                                                |
| xml_etree_generate               | 52.7 ms                                                    | 51.1 ms: 1.03x faster                                               |
| float                            | 48.6 ms                                                    | 47.2 ms: 1.03x faster                                               |
| pyflate                          | 321 ms                                                     | 312 ms: 1.03x faster                                                |
| json_dumps                       | 6.23 ms                                                    | 6.07 ms: 1.03x faster                                               |
| xml_etree_parse                  | 106 ms                                                     | 103 ms: 1.02x faster                                                |
| flaskblogging                    | 3.61 ms                                                    | 3.53 ms: 1.02x faster                                               |
| xml_etree_iterparse              | 71.5 ms                                                    | 70.1 ms: 1.02x faster                                               |
| richards                         | 31.8 ms                                                    | 31.2 ms: 1.02x faster                                               |
| unpickle_list                    | 2.88 us                                                    | 2.83 us: 1.02x faster                                               |
| pprint_safe_repr                 | 465 ms                                                     | 457 ms: 1.02x faster                                                |
| mdp                              | 1.53 sec                                                   | 1.51 sec: 1.02x faster                                              |
| html5lib                         | 31.2 ms                                                    | 30.8 ms: 1.01x faster                                               |
| deepcopy_reduce                  | 1.82 us                                                    | 1.80 us: 1.01x faster                                               |
| telco                            | 4.60 ms                                                    | 4.55 ms: 1.01x faster                                               |
| pickle_dict                      | 18.3 us                                                    | 18.1 us: 1.01x faster                                               |
| richards_super                   | 35.2 ms                                                    | 34.9 ms: 1.01x faster                                               |
| regex_effbot                     | 2.58 ms                                                    | 2.57 ms: 1.01x faster                                               |
| logging_format                   | 3.31 us                                                    | 3.29 us: 1.00x faster                                               |
| logging_simple                   | 3.04 us                                                    | 3.03 us: 1.00x faster                                               |
| pickle                           | 7.48 us                                                    | 7.46 us: 1.00x faster                                               |
| thrift                           | 435 us                                                     | 434 us: 1.00x faster                                                |
| async_tree_eager_cpu_io_mixed_tg | 331 ms                                                     | 332 ms: 1.01x slower                                                |
| sqlite_synth                     | 1.55 us                                                    | 1.56 us: 1.01x slower                                               |
| coroutines                       | 15.8 ms                                                    | 15.9 ms: 1.01x slower                                               |
| coverage                         | 45.0 ms                                                    | 45.3 ms: 1.01x slower                                               |
| gc_traversal                     | 2.45 ms                                                    | 2.47 ms: 1.01x slower                                               |
| json_loads                       | 16.8 us                                                    | 17.0 us: 1.01x slower                                               |
| regex_v8                         | 17.3 ms                                                    | 17.4 ms: 1.01x slower                                               |
| pickle_list                      | 2.96 us                                                    | 2.98 us: 1.01x slower                                               |
| spectral_norm                    | 66.4 ms                                                    | 67.1 ms: 1.01x slower                                               |
| generators                       | 22.9 ms                                                    | 23.2 ms: 1.01x slower                                               |
| async_tree_eager_cpu_io_mixed    | 358 ms                                                     | 363 ms: 1.01x slower                                                |
| async_tree_eager_tg              | 41.4 ms                                                    | 41.9 ms: 1.01x slower                                               |
| meteor_contest                   | 70.3 ms                                                    | 71.5 ms: 1.02x slower                                               |
| scimark_fft                      | 181 ms                                                     | 184 ms: 1.02x slower                                                |
| unpickle                         | 9.12 us                                                    | 9.32 us: 1.02x slower                                               |
| create_gc_cycles                 | 897 us                                                     | 919 us: 1.03x slower                                                |
| logging_silent                   | 60.1 ns                                                    | 61.8 ns: 1.03x slower                                               |
| go                               | 101 ms                                                     | 103 ms: 1.03x slower                                                |
| async_tree_none                  | 209 ms                                                     | 216 ms: 1.03x slower                                                |
| python_startup                   | 15.2 ms                                                    | 15.7 ms: 1.03x slower                                               |
| scimark_monte_carlo              | 42.5 ms                                                    | 43.9 ms: 1.03x slower                                               |
| sympy_str                        | 131 ms                                                     | 136 ms: 1.04x slower                                                |
| sympy_sum                        | 69.2 ms                                                    | 71.9 ms: 1.04x slower                                               |
| chameleon                        | 4.27 ms                                                    | 4.44 ms: 1.04x slower                                               |
| async_tree_eager                 | 60.3 ms                                                    | 62.8 ms: 1.04x slower                                               |
| sympy_expand                     | 226 ms                                                     | 235 ms: 1.04x slower                                                |
| regex_compile                    | 68.5 ms                                                    | 71.7 ms: 1.05x slower                                               |
| sympy_integrate                  | 10.3 ms                                                    | 10.8 ms: 1.05x slower                                               |
| async_generators                 | 281 ms                                                     | 295 ms: 1.05x slower                                                |
| crypto_pyaes                     | 49.5 ms                                                    | 51.9 ms: 1.05x slower                                               |
| scimark_sparse_mat_mult          | 2.77 ms                                                    | 2.91 ms: 1.05x slower                                               |
| bench_mp_pool                    | 47.2 ms                                                    | 49.6 ms: 1.05x slower                                               |
| docutils                         | 1.44 sec                                                   | 1.52 sec: 1.05x slower                                              |
| pycparser                        | 632 ms                                                     | 667 ms: 1.06x slower                                                |
| scimark_sor                      | 94.9 ms                                                    | 100 ms: 1.06x slower                                                |
| sqlglot_optimize                 | 30.9 ms                                                    | 32.7 ms: 1.06x slower                                               |
| 2to3                             | 161 ms                                                     | 171 ms: 1.06x slower                                                |
| nbody                            | 59.6 ms                                                    | 63.5 ms: 1.07x slower                                               |
| typing_runtime_protocols         | 87.6 us                                                    | 93.5 us: 1.07x slower                                               |
| python_startup_no_site           | 12.3 ms                                                    | 13.2 ms: 1.07x slower                                               |
| hexiom                           | 4.06 ms                                                    | 4.36 ms: 1.07x slower                                               |
| bench_thread_pool                | 447 us                                                     | 483 us: 1.08x slower                                                |
| pylint                           | 170 ms                                                     | 184 ms: 1.08x slower                                                |
| django_template                  | 19.4 ms                                                    | 21.0 ms: 1.08x slower                                               |
| nqueens                          | 52.2 ms                                                    | 57.2 ms: 1.10x slower                                               |
| raytrace                         | 147 ms                                                     | 162 ms: 1.10x slower                                                |
| sqlglot_transpile                | 891 us                                                     | 1.00 ms: 1.13x slower                                               |
| sqlglot_parse                    | 732 us                                                     | 830 us: 1.13x slower                                                |
| chaos                            | 34.0 ms                                                    | 38.8 ms: 1.14x slower                                               |
| deltablue                        | 2.14 ms                                                    | 2.46 ms: 1.15x slower                                               |
| genshi_text                      | 13.9 ms                                                    | 16.1 ms: 1.16x slower                                               |
| scimark_lu                       | 66.9 ms                                                    | 78.2 ms: 1.17x slower                                               |
| comprehensions                   | 10.2 us                                                    | 12.2 us: 1.20x slower                                               |
| genshi_xml                       | 29.9 ms                                                    | 39.5 ms: 1.32x slower                                               |
| Geometric mean                   | (ref)                                                      | 1.02x slower                                                        |

Benchmark hidden because not significant (21): asyncio_tcp_ssl, asyncio_websockets, pidigits, pprint_pformat, deepcopy, regex_dna, dask, async_tree_eager_io_tg, json, async_tree_cpu_io_mixed_tg, async_tree_memoization_tg, async_tree_none_tg, async_tree_io_tg, async_tree_eager_memoization_tg, async_tree_eager_memoization, async_tree_eager_io, async_tree_cpu_io_mixed, tornado_http, async_tree_memoization, async_tree_io, asyncio_tcp
Ignored benchmarks (6) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, bpe_tokeniser, dulwich_log, gunicorn, mypy2, sqlglot_normalize

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 0.66x
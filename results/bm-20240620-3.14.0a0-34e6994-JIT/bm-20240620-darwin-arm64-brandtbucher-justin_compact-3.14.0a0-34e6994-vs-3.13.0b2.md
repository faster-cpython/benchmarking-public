# Results vs. 3.13.0b2

- fork: brandtbucher
- ref: justin_compact
- machine: darwin-arm64
- commit hash: 34e6994
- commit date: 2024-06-20
- overall geometric mean: 1.02x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x slower
- Memory change: 1.19x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240620-darwin-arm64-brandtbucher-justin_compact-3.14.0a0-34e6994 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 161 ms                                                     | 172 ms: 1.07x slower                                                  |
| docutils       | 1.44 sec                                                   | 1.50 sec: 1.05x slower                                                |
| html5lib       | 31.2 ms                                                    | 30.9 ms: 1.01x faster                                                 |
| Geometric mean | (ref)                                                      | 1.03x slower                                                          |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240620-darwin-arm64-brandtbucher-justin_compact-3.14.0a0-34e6994 |
|----------------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_eager_cpu_io_mixed_tg | 331 ms                                                     | 333 ms: 1.01x slower                                                  |
| async_tree_eager_cpu_io_mixed    | 358 ms                                                     | 362 ms: 1.01x slower                                                  |
| async_tree_eager_tg              | 41.4 ms                                                    | 42.4 ms: 1.02x slower                                                 |
| async_tree_cpu_io_mixed          | 467 ms                                                     | 480 ms: 1.03x slower                                                  |
| async_tree_none                  | 209 ms                                                     | 219 ms: 1.04x slower                                                  |
| async_tree_memoization           | 260 ms                                                     | 271 ms: 1.04x slower                                                  |
| async_tree_eager                 | 60.3 ms                                                    | 63.7 ms: 1.06x slower                                                 |
| async_tree_memoization_tg        | 240 ms                                                     | 256 ms: 1.07x slower                                                  |
| Geometric mean                   | (ref)                                                      | 1.02x slower                                                          |

Benchmark hidden because not significant (8): async_tree_io_tg, async_tree_eager_io, async_tree_none_tg, async_tree_eager_memoization_tg, async_tree_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_io, async_tree_eager_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240620-darwin-arm64-brandtbucher-justin_compact-3.14.0a0-34e6994 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 48.6 ms                                                    | 46.5 ms: 1.05x faster                                                 |
| pidigits       | 282 ms                                                     | 282 ms: 1.00x slower                                                  |
| nbody          | 59.6 ms                                                    | 63.5 ms: 1.07x slower                                                 |
| Geometric mean | (ref)                                                      | 1.01x slower                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240620-darwin-arm64-brandtbucher-justin_compact-3.14.0a0-34e6994 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 2.58 ms                                                    | 2.58 ms: 1.00x faster                                                 |
| regex_v8       | 17.3 ms                                                    | 17.4 ms: 1.01x slower                                                 |
| regex_compile  | 68.5 ms                                                    | 71.5 ms: 1.04x slower                                                 |
| Geometric mean | (ref)                                                      | 1.01x slower                                                          |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240620-darwin-arm64-brandtbucher-justin_compact-3.14.0a0-34e6994 |
|----------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 1.47 sec                                                   | 1.24 sec: 1.18x faster                                                |
| unpickle_pure_python | 141 us                                                     | 132 us: 1.06x faster                                                  |
| pickle_pure_python   | 179 us                                                     | 173 us: 1.03x faster                                                  |
| xml_etree_process    | 37.1 ms                                                    | 36.1 ms: 1.03x faster                                                 |
| xml_etree_iterparse  | 71.5 ms                                                    | 70.6 ms: 1.01x faster                                                 |
| xml_etree_generate   | 52.7 ms                                                    | 52.1 ms: 1.01x faster                                                 |
| pickle_list          | 2.96 us                                                    | 2.97 us: 1.01x slower                                                 |
| unpickle_list        | 2.88 us                                                    | 2.90 us: 1.01x slower                                                 |
| json_loads           | 16.8 us                                                    | 17.1 us: 1.01x slower                                                 |
| unpickle             | 9.12 us                                                    | 9.28 us: 1.02x slower                                                 |
| json_dumps           | 6.23 ms                                                    | 6.40 ms: 1.03x slower                                                 |
| Geometric mean       | (ref)                                                      | 1.02x faster                                                          |

Benchmark hidden because not significant (3): xml_etree_parse, pickle_dict, pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240620-darwin-arm64-brandtbucher-justin_compact-3.14.0a0-34e6994 |
|------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 12.3 ms                                                    | 11.3 ms: 1.09x faster                                                 |
| python_startup         | 15.2 ms                                                    | 14.2 ms: 1.07x faster                                                 |
| Geometric mean         | (ref)                                                      | 1.08x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240620-darwin-arm64-brandtbucher-justin_compact-3.14.0a0-34e6994 |
|-----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 6.99 ms                                                    | 6.46 ms: 1.08x faster                                                 |
| django_template | 19.4 ms                                                    | 21.6 ms: 1.11x slower                                                 |
| genshi_text     | 13.9 ms                                                    | 15.9 ms: 1.14x slower                                                 |
| genshi_xml      | 29.9 ms                                                    | 35.2 ms: 1.18x slower                                                 |
| Geometric mean  | (ref)                                                      | 1.08x slower                                                          |

All benchmarks:
===============

| Benchmark                        | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240620-darwin-arm64-brandtbucher-justin_compact-3.14.0a0-34e6994 |
|----------------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| deepcopy                         | 204 us                                                     | 151 us: 1.35x faster                                                  |
| deepcopy_memo                    | 22.6 us                                                    | 16.9 us: 1.34x faster                                                 |
| deepcopy_reduce                  | 1.82 us                                                    | 1.54 us: 1.18x faster                                                 |
| tomli_loads                      | 1.47 sec                                                   | 1.24 sec: 1.18x faster                                                |
| python_startup_no_site           | 12.3 ms                                                    | 11.3 ms: 1.09x faster                                                 |
| mako                             | 6.99 ms                                                    | 6.46 ms: 1.08x faster                                                 |
| python_startup                   | 15.2 ms                                                    | 14.2 ms: 1.07x faster                                                 |
| unpickle_pure_python             | 141 us                                                     | 132 us: 1.06x faster                                                  |
| mdp                              | 1.53 sec                                                   | 1.45 sec: 1.06x faster                                                |
| float                            | 48.6 ms                                                    | 46.5 ms: 1.05x faster                                                 |
| pickle_pure_python               | 179 us                                                     | 173 us: 1.03x faster                                                  |
| xml_etree_process                | 37.1 ms                                                    | 36.1 ms: 1.03x faster                                                 |
| pyflate                          | 321 ms                                                     | 314 ms: 1.02x faster                                                  |
| xml_etree_iterparse              | 71.5 ms                                                    | 70.6 ms: 1.01x faster                                                 |
| xml_etree_generate               | 52.7 ms                                                    | 52.1 ms: 1.01x faster                                                 |
| logging_simple                   | 3.04 us                                                    | 3.01 us: 1.01x faster                                                 |
| fannkuch                         | 248 ms                                                     | 246 ms: 1.01x faster                                                  |
| html5lib                         | 31.2 ms                                                    | 30.9 ms: 1.01x faster                                                 |
| richards                         | 31.8 ms                                                    | 31.6 ms: 1.01x faster                                                 |
| telco                            | 4.60 ms                                                    | 4.58 ms: 1.00x faster                                                 |
| go                               | 101 ms                                                     | 100 ms: 1.00x faster                                                  |
| regex_effbot                     | 2.58 ms                                                    | 2.58 ms: 1.00x faster                                                 |
| pidigits                         | 282 ms                                                     | 282 ms: 1.00x slower                                                  |
| pprint_safe_repr                 | 465 ms                                                     | 467 ms: 1.01x slower                                                  |
| pickle_list                      | 2.96 us                                                    | 2.97 us: 1.01x slower                                                 |
| unpickle_list                    | 2.88 us                                                    | 2.90 us: 1.01x slower                                                 |
| async_tree_eager_cpu_io_mixed_tg | 331 ms                                                     | 333 ms: 1.01x slower                                                  |
| regex_v8                         | 17.3 ms                                                    | 17.4 ms: 1.01x slower                                                 |
| richards_super                   | 35.2 ms                                                    | 35.5 ms: 1.01x slower                                                 |
| coverage                         | 45.0 ms                                                    | 45.3 ms: 1.01x slower                                                 |
| spectral_norm                    | 66.4 ms                                                    | 67.0 ms: 1.01x slower                                                 |
| create_gc_cycles                 | 897 us                                                     | 906 us: 1.01x slower                                                  |
| gc_traversal                     | 2.45 ms                                                    | 2.48 ms: 1.01x slower                                                 |
| async_tree_eager_cpu_io_mixed    | 358 ms                                                     | 362 ms: 1.01x slower                                                  |
| sqlite_synth                     | 1.55 us                                                    | 1.57 us: 1.01x slower                                                 |
| json_loads                       | 16.8 us                                                    | 17.1 us: 1.01x slower                                                 |
| thrift                           | 435 us                                                     | 441 us: 1.01x slower                                                  |
| coroutines                       | 15.8 ms                                                    | 16.1 ms: 1.01x slower                                                 |
| generators                       | 22.9 ms                                                    | 23.3 ms: 1.02x slower                                                 |
| pprint_pformat                   | 947 ms                                                     | 962 ms: 1.02x slower                                                  |
| unpickle                         | 9.12 us                                                    | 9.28 us: 1.02x slower                                                 |
| meteor_contest                   | 70.3 ms                                                    | 71.7 ms: 1.02x slower                                                 |
| bpe_tokeniser                    | 3.05 sec                                                   | 3.11 sec: 1.02x slower                                                |
| async_tree_eager_tg              | 41.4 ms                                                    | 42.4 ms: 1.02x slower                                                 |
| async_tree_cpu_io_mixed          | 467 ms                                                     | 480 ms: 1.03x slower                                                  |
| json_dumps                       | 6.23 ms                                                    | 6.40 ms: 1.03x slower                                                 |
| scimark_fft                      | 181 ms                                                     | 186 ms: 1.03x slower                                                  |
| scimark_monte_carlo              | 42.5 ms                                                    | 43.9 ms: 1.03x slower                                                 |
| logging_silent                   | 60.1 ns                                                    | 62.6 ns: 1.04x slower                                                 |
| bench_mp_pool                    | 47.2 ms                                                    | 49.2 ms: 1.04x slower                                                 |
| regex_compile                    | 68.5 ms                                                    | 71.5 ms: 1.04x slower                                                 |
| async_tree_none                  | 209 ms                                                     | 219 ms: 1.04x slower                                                  |
| async_tree_memoization           | 260 ms                                                     | 271 ms: 1.04x slower                                                  |
| docutils                         | 1.44 sec                                                   | 1.50 sec: 1.05x slower                                                |
| async_generators                 | 281 ms                                                     | 294 ms: 1.05x slower                                                  |
| crypto_pyaes                     | 49.5 ms                                                    | 52.2 ms: 1.05x slower                                                 |
| scimark_sparse_mat_mult          | 2.77 ms                                                    | 2.93 ms: 1.06x slower                                                 |
| async_tree_eager                 | 60.3 ms                                                    | 63.7 ms: 1.06x slower                                                 |
| pycparser                        | 632 ms                                                     | 671 ms: 1.06x slower                                                  |
| bench_thread_pool                | 447 us                                                     | 475 us: 1.06x slower                                                  |
| sympy_str                        | 131 ms                                                     | 140 ms: 1.07x slower                                                  |
| nbody                            | 59.6 ms                                                    | 63.5 ms: 1.07x slower                                                 |
| async_tree_memoization_tg        | 240 ms                                                     | 256 ms: 1.07x slower                                                  |
| 2to3                             | 161 ms                                                     | 172 ms: 1.07x slower                                                  |
| sympy_integrate                  | 10.3 ms                                                    | 11.1 ms: 1.07x slower                                                 |
| sympy_expand                     | 226 ms                                                     | 241 ms: 1.07x slower                                                  |
| sqlglot_normalize                | 166 ms                                                     | 177 ms: 1.07x slower                                                  |
| sympy_sum                        | 69.2 ms                                                    | 74.0 ms: 1.07x slower                                                 |
| sqlglot_optimize                 | 30.9 ms                                                    | 33.0 ms: 1.07x slower                                                 |
| hexiom                           | 4.06 ms                                                    | 4.34 ms: 1.07x slower                                                 |
| typing_runtime_protocols         | 87.6 us                                                    | 95.0 us: 1.08x slower                                                 |
| scimark_sor                      | 94.9 ms                                                    | 103 ms: 1.09x slower                                                  |
| deltablue                        | 2.14 ms                                                    | 2.35 ms: 1.10x slower                                                 |
| raytrace                         | 147 ms                                                     | 162 ms: 1.10x slower                                                  |
| django_template                  | 19.4 ms                                                    | 21.6 ms: 1.11x slower                                                 |
| nqueens                          | 52.2 ms                                                    | 58.5 ms: 1.12x slower                                                 |
| asyncio_tcp                      | 402 ms                                                     | 453 ms: 1.13x slower                                                  |
| sqlglot_transpile                | 891 us                                                     | 1.01 ms: 1.13x slower                                                 |
| sqlglot_parse                    | 732 us                                                     | 827 us: 1.13x slower                                                  |
| genshi_text                      | 13.9 ms                                                    | 15.9 ms: 1.14x slower                                                 |
| chaos                            | 34.0 ms                                                    | 39.4 ms: 1.16x slower                                                 |
| genshi_xml                       | 29.9 ms                                                    | 35.2 ms: 1.18x slower                                                 |
| scimark_lu                       | 66.9 ms                                                    | 80.5 ms: 1.20x slower                                                 |
| comprehensions                   | 10.2 us                                                    | 12.4 us: 1.22x slower                                                 |
| Geometric mean                   | (ref)                                                      | 1.02x slower                                                          |

Benchmark hidden because not significant (20): async_tree_io_tg, xml_etree_parse, pathlib, async_tree_eager_io, regex_dna, pickle_dict, logging_format, asyncio_websockets, json, pickle, asyncio_tcp_ssl, async_tree_none_tg, dask, async_tree_eager_memoization_tg, async_tree_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_io, tornado_http, async_tree_eager_memoization, pylint
Ignored benchmarks (6) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dulwich_log, flaskblogging, gunicorn, mypy2

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: 1.19x
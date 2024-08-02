# Results vs. 3.13.0b2

- fork: brandtbucher
- ref: justin_compact
- machine: darwin-arm64
- commit hash: e04d5ab
- commit date: 2024-06-19
- overall geometric mean: 1.05x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x slower
- Memory change: 1.19x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240619-darwin-arm64-brandtbucher-justin_compact-3.14.0a0-e04d5ab |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 161 ms                                                     | 176 ms: 1.10x slower                                                  |
| docutils       | 1.44 sec                                                   | 1.55 sec: 1.08x slower                                                |
| html5lib       | 31.2 ms                                                    | 32.1 ms: 1.03x slower                                                 |
| tornado_http   | 66.7 ms                                                    | 69.5 ms: 1.04x slower                                                 |
| Geometric mean | (ref)                                                      | 1.06x slower                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240619-darwin-arm64-brandtbucher-justin_compact-3.14.0a0-e04d5ab |
|----------------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_eager_cpu_io_mixed_tg | 331 ms                                                     | 337 ms: 1.02x slower                                                  |
| async_tree_eager_cpu_io_mixed    | 358 ms                                                     | 369 ms: 1.03x slower                                                  |
| async_tree_cpu_io_mixed_tg       | 451 ms                                                     | 466 ms: 1.03x slower                                                  |
| async_tree_none_tg               | 198 ms                                                     | 207 ms: 1.05x slower                                                  |
| async_tree_cpu_io_mixed          | 467 ms                                                     | 489 ms: 1.05x slower                                                  |
| async_tree_eager_memoization_tg  | 126 ms                                                     | 132 ms: 1.05x slower                                                  |
| async_tree_eager_io_tg           | 768 ms                                                     | 807 ms: 1.05x slower                                                  |
| async_tree_io                    | 563 ms                                                     | 597 ms: 1.06x slower                                                  |
| async_tree_eager_memoization     | 152 ms                                                     | 162 ms: 1.06x slower                                                  |
| async_tree_eager_tg              | 41.4 ms                                                    | 44.8 ms: 1.08x slower                                                 |
| async_tree_memoization           | 260 ms                                                     | 282 ms: 1.09x slower                                                  |
| async_tree_none                  | 209 ms                                                     | 228 ms: 1.09x slower                                                  |
| async_tree_memoization_tg        | 240 ms                                                     | 266 ms: 1.11x slower                                                  |
| async_tree_eager                 | 60.3 ms                                                    | 67.4 ms: 1.12x slower                                                 |
| Geometric mean                   | (ref)                                                      | 1.06x slower                                                          |

Benchmark hidden because not significant (2): async_tree_io_tg, async_tree_eager_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240619-darwin-arm64-brandtbucher-justin_compact-3.14.0a0-e04d5ab |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 48.6 ms                                                    | 47.4 ms: 1.03x faster                                                 |
| nbody          | 59.6 ms                                                    | 63.3 ms: 1.06x slower                                                 |
| Geometric mean | (ref)                                                      | 1.01x slower                                                          |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240619-darwin-arm64-brandtbucher-justin_compact-3.14.0a0-e04d5ab |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 2.58 ms                                                    | 2.58 ms: 1.00x faster                                                 |
| regex_v8       | 17.3 ms                                                    | 17.4 ms: 1.01x slower                                                 |
| regex_compile  | 68.5 ms                                                    | 74.1 ms: 1.08x slower                                                 |
| Geometric mean | (ref)                                                      | 1.02x slower                                                          |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240619-darwin-arm64-brandtbucher-justin_compact-3.14.0a0-e04d5ab |
|----------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 1.47 sec                                                   | 1.29 sec: 1.14x faster                                                |
| unpickle_pure_python | 141 us                                                     | 140 us: 1.01x faster                                                  |
| pickle_list          | 2.96 us                                                    | 2.98 us: 1.01x slower                                                 |
| unpickle_list        | 2.88 us                                                    | 2.91 us: 1.01x slower                                                 |
| pickle               | 7.48 us                                                    | 7.55 us: 1.01x slower                                                 |
| xml_etree_parse      | 106 ms                                                     | 107 ms: 1.01x slower                                                  |
| xml_etree_iterparse  | 71.5 ms                                                    | 72.4 ms: 1.01x slower                                                 |
| pickle_pure_python   | 179 us                                                     | 181 us: 1.01x slower                                                  |
| xml_etree_generate   | 52.7 ms                                                    | 53.4 ms: 1.01x slower                                                 |
| json_dumps           | 6.23 ms                                                    | 6.32 ms: 1.01x slower                                                 |
| xml_etree_process    | 37.1 ms                                                    | 37.7 ms: 1.02x slower                                                 |
| json_loads           | 16.8 us                                                    | 17.2 us: 1.02x slower                                                 |
| unpickle             | 9.12 us                                                    | 9.51 us: 1.04x slower                                                 |
| Geometric mean       | (ref)                                                      | 1.00x slower                                                          |

Benchmark hidden because not significant (1): pickle_dict

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240619-darwin-arm64-brandtbucher-justin_compact-3.14.0a0-e04d5ab |
|------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 15.2 ms                                                    | 16.4 ms: 1.08x slower                                                 |
| python_startup_no_site | 12.3 ms                                                    | 13.6 ms: 1.11x slower                                                 |
| Geometric mean         | (ref)                                                      | 1.10x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240619-darwin-arm64-brandtbucher-justin_compact-3.14.0a0-e04d5ab |
|-----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 6.99 ms                                                    | 6.51 ms: 1.07x faster                                                 |
| genshi_text     | 13.9 ms                                                    | 16.5 ms: 1.19x slower                                                 |
| django_template | 19.4 ms                                                    | 23.1 ms: 1.19x slower                                                 |
| genshi_xml      | 29.9 ms                                                    | 36.8 ms: 1.23x slower                                                 |
| Geometric mean  | (ref)                                                      | 1.13x slower                                                          |

All benchmarks:
===============

| Benchmark                        | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240619-darwin-arm64-brandtbucher-justin_compact-3.14.0a0-e04d5ab |
|----------------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| deepcopy_memo                    | 22.6 us                                                    | 17.0 us: 1.33x faster                                                 |
| deepcopy                         | 204 us                                                     | 158 us: 1.29x faster                                                  |
| tomli_loads                      | 1.47 sec                                                   | 1.29 sec: 1.14x faster                                                |
| deepcopy_reduce                  | 1.82 us                                                    | 1.62 us: 1.12x faster                                                 |
| mako                             | 6.99 ms                                                    | 6.51 ms: 1.07x faster                                                 |
| mdp                              | 1.53 sec                                                   | 1.49 sec: 1.03x faster                                                |
| float                            | 48.6 ms                                                    | 47.4 ms: 1.03x faster                                                 |
| fannkuch                         | 248 ms                                                     | 243 ms: 1.02x faster                                                  |
| pyflate                          | 321 ms                                                     | 318 ms: 1.01x faster                                                  |
| unpickle_pure_python             | 141 us                                                     | 140 us: 1.01x faster                                                  |
| regex_effbot                     | 2.58 ms                                                    | 2.58 ms: 1.00x faster                                                 |
| asyncio_websockets               | 409 ms                                                     | 408 ms: 1.00x faster                                                  |
| telco                            | 4.60 ms                                                    | 4.63 ms: 1.01x slower                                                 |
| pickle_list                      | 2.96 us                                                    | 2.98 us: 1.01x slower                                                 |
| unpickle_list                    | 2.88 us                                                    | 2.91 us: 1.01x slower                                                 |
| regex_v8                         | 17.3 ms                                                    | 17.4 ms: 1.01x slower                                                 |
| pickle                           | 7.48 us                                                    | 7.55 us: 1.01x slower                                                 |
| spectral_norm                    | 66.4 ms                                                    | 67.1 ms: 1.01x slower                                                 |
| xml_etree_parse                  | 106 ms                                                     | 107 ms: 1.01x slower                                                  |
| xml_etree_iterparse              | 71.5 ms                                                    | 72.4 ms: 1.01x slower                                                 |
| pickle_pure_python               | 179 us                                                     | 181 us: 1.01x slower                                                  |
| xml_etree_generate               | 52.7 ms                                                    | 53.4 ms: 1.01x slower                                                 |
| json_dumps                       | 6.23 ms                                                    | 6.32 ms: 1.01x slower                                                 |
| create_gc_cycles                 | 897 us                                                     | 912 us: 1.02x slower                                                  |
| xml_etree_process                | 37.1 ms                                                    | 37.7 ms: 1.02x slower                                                 |
| async_tree_eager_cpu_io_mixed_tg | 331 ms                                                     | 337 ms: 1.02x slower                                                  |
| sqlite_synth                     | 1.55 us                                                    | 1.58 us: 1.02x slower                                                 |
| json_loads                       | 16.8 us                                                    | 17.2 us: 1.02x slower                                                 |
| async_tree_eager_cpu_io_mixed    | 358 ms                                                     | 369 ms: 1.03x slower                                                  |
| html5lib                         | 31.2 ms                                                    | 32.1 ms: 1.03x slower                                                 |
| async_tree_cpu_io_mixed_tg       | 451 ms                                                     | 466 ms: 1.03x slower                                                  |
| meteor_contest                   | 70.3 ms                                                    | 72.7 ms: 1.03x slower                                                 |
| scimark_fft                      | 181 ms                                                     | 187 ms: 1.03x slower                                                  |
| bpe_tokeniser                    | 3.05 sec                                                   | 3.18 sec: 1.04x slower                                                |
| unpickle                         | 9.12 us                                                    | 9.51 us: 1.04x slower                                                 |
| tornado_http                     | 66.7 ms                                                    | 69.5 ms: 1.04x slower                                                 |
| dask                             | 221 ms                                                     | 231 ms: 1.04x slower                                                  |
| pprint_safe_repr                 | 465 ms                                                     | 485 ms: 1.04x slower                                                  |
| pprint_pformat                   | 947 ms                                                     | 988 ms: 1.04x slower                                                  |
| async_tree_none_tg               | 198 ms                                                     | 207 ms: 1.05x slower                                                  |
| async_tree_cpu_io_mixed          | 467 ms                                                     | 489 ms: 1.05x slower                                                  |
| scimark_monte_carlo              | 42.5 ms                                                    | 44.5 ms: 1.05x slower                                                 |
| go                               | 101 ms                                                     | 106 ms: 1.05x slower                                                  |
| async_tree_eager_memoization_tg  | 126 ms                                                     | 132 ms: 1.05x slower                                                  |
| async_tree_eager_io_tg           | 768 ms                                                     | 807 ms: 1.05x slower                                                  |
| async_tree_io                    | 563 ms                                                     | 597 ms: 1.06x slower                                                  |
| thrift                           | 435 us                                                     | 462 us: 1.06x slower                                                  |
| crypto_pyaes                     | 49.5 ms                                                    | 52.5 ms: 1.06x slower                                                 |
| async_tree_eager_memoization     | 152 ms                                                     | 162 ms: 1.06x slower                                                  |
| nbody                            | 59.6 ms                                                    | 63.3 ms: 1.06x slower                                                 |
| richards                         | 31.8 ms                                                    | 33.9 ms: 1.07x slower                                                 |
| coverage                         | 45.0 ms                                                    | 48.0 ms: 1.07x slower                                                 |
| gc_traversal                     | 2.45 ms                                                    | 2.61 ms: 1.07x slower                                                 |
| logging_simple                   | 3.04 us                                                    | 3.26 us: 1.07x slower                                                 |
| logging_format                   | 3.31 us                                                    | 3.55 us: 1.07x slower                                                 |
| docutils                         | 1.44 sec                                                   | 1.55 sec: 1.08x slower                                                |
| regex_compile                    | 68.5 ms                                                    | 74.1 ms: 1.08x slower                                                 |
| async_tree_eager_tg              | 41.4 ms                                                    | 44.8 ms: 1.08x slower                                                 |
| scimark_sparse_mat_mult          | 2.77 ms                                                    | 3.00 ms: 1.08x slower                                                 |
| python_startup                   | 15.2 ms                                                    | 16.4 ms: 1.08x slower                                                 |
| async_tree_memoization           | 260 ms                                                     | 282 ms: 1.09x slower                                                  |
| pycparser                        | 632 ms                                                     | 687 ms: 1.09x slower                                                  |
| hexiom                           | 4.06 ms                                                    | 4.41 ms: 1.09x slower                                                 |
| logging_silent                   | 60.1 ns                                                    | 65.4 ns: 1.09x slower                                                 |
| async_tree_none                  | 209 ms                                                     | 228 ms: 1.09x slower                                                  |
| sympy_sum                        | 69.2 ms                                                    | 75.4 ms: 1.09x slower                                                 |
| async_generators                 | 281 ms                                                     | 306 ms: 1.09x slower                                                  |
| bench_mp_pool                    | 47.2 ms                                                    | 51.5 ms: 1.09x slower                                                 |
| richards_super                   | 35.2 ms                                                    | 38.5 ms: 1.09x slower                                                 |
| bench_thread_pool                | 447 us                                                     | 489 us: 1.09x slower                                                  |
| 2to3                             | 161 ms                                                     | 176 ms: 1.10x slower                                                  |
| sympy_integrate                  | 10.3 ms                                                    | 11.4 ms: 1.10x slower                                                 |
| sympy_str                        | 131 ms                                                     | 145 ms: 1.10x slower                                                  |
| asyncio_tcp                      | 402 ms                                                     | 443 ms: 1.10x slower                                                  |
| pylint                           | 170 ms                                                     | 188 ms: 1.11x slower                                                  |
| python_startup_no_site           | 12.3 ms                                                    | 13.6 ms: 1.11x slower                                                 |
| async_tree_memoization_tg        | 240 ms                                                     | 266 ms: 1.11x slower                                                  |
| sympy_expand                     | 226 ms                                                     | 252 ms: 1.12x slower                                                  |
| async_tree_eager                 | 60.3 ms                                                    | 67.4 ms: 1.12x slower                                                 |
| sqlglot_optimize                 | 30.9 ms                                                    | 34.5 ms: 1.12x slower                                                 |
| typing_runtime_protocols         | 87.6 us                                                    | 98.8 us: 1.13x slower                                                 |
| scimark_sor                      | 94.9 ms                                                    | 107 ms: 1.13x slower                                                  |
| generators                       | 22.9 ms                                                    | 26.3 ms: 1.15x slower                                                 |
| nqueens                          | 52.2 ms                                                    | 60.0 ms: 1.15x slower                                                 |
| coroutines                       | 15.8 ms                                                    | 18.3 ms: 1.16x slower                                                 |
| sqlglot_transpile                | 891 us                                                     | 1.05 ms: 1.18x slower                                                 |
| genshi_text                      | 13.9 ms                                                    | 16.5 ms: 1.19x slower                                                 |
| django_template                  | 19.4 ms                                                    | 23.1 ms: 1.19x slower                                                 |
| sqlglot_parse                    | 732 us                                                     | 871 us: 1.19x slower                                                  |
| deltablue                        | 2.14 ms                                                    | 2.57 ms: 1.20x slower                                                 |
| chaos                            | 34.0 ms                                                    | 41.5 ms: 1.22x slower                                                 |
| comprehensions                   | 10.2 us                                                    | 12.5 us: 1.23x slower                                                 |
| genshi_xml                       | 29.9 ms                                                    | 36.8 ms: 1.23x slower                                                 |
| raytrace                         | 147 ms                                                     | 182 ms: 1.24x slower                                                  |
| scimark_lu                       | 66.9 ms                                                    | 86.3 ms: 1.29x slower                                                 |
| Geometric mean                   | (ref)                                                      | 1.05x slower                                                          |

Benchmark hidden because not significant (8): pathlib, async_tree_io_tg, pickle_dict, pidigits, regex_dna, asyncio_tcp_ssl, json, async_tree_eager_io
Ignored benchmarks (7) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dulwich_log, flaskblogging, gunicorn, mypy2, sqlglot_normalize

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.04x
- 95% likely to have a slowdown of 1.04x
- 99% likely to have a slowdown of 1.04x

# Memory
- memory change: 1.19x
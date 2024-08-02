# Results vs. 3.13.0b2

- fork: python
- ref: e418fc3a6e7bade68ab5
- machine: darwin-arm64
- commit hash: e418fc3
- commit date: 2024-05-25
- overall geometric mean: 1.14x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x slower
- Memory change: 0.65x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240525-darwin-arm64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 161 ms                                                     | 182 ms: 1.13x slower                                                  |
| chameleon      | 4.27 ms                                                    | 4.99 ms: 1.17x slower                                                 |
| docutils       | 1.44 sec                                                   | 1.68 sec: 1.17x slower                                                |
| html5lib       | 31.2 ms                                                    | 33.3 ms: 1.07x slower                                                 |
| tornado_http   | 66.7 ms                                                    | 70.6 ms: 1.06x slower                                                 |
| Geometric mean | (ref)                                                      | 1.12x slower                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240525-darwin-arm64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_eager_cpu_io_mixed_tg | 331 ms                                                     | 336 ms: 1.02x slower                                                  |
| async_tree_eager_cpu_io_mixed    | 358 ms                                                     | 368 ms: 1.03x slower                                                  |
| async_tree_eager_memoization_tg  | 126 ms                                                     | 130 ms: 1.03x slower                                                  |
| async_tree_eager_io              | 766 ms                                                     | 795 ms: 1.04x slower                                                  |
| async_tree_io                    | 563 ms                                                     | 587 ms: 1.04x slower                                                  |
| async_tree_cpu_io_mixed          | 467 ms                                                     | 488 ms: 1.05x slower                                                  |
| async_tree_none_tg               | 198 ms                                                     | 207 ms: 1.05x slower                                                  |
| async_tree_eager_memoization     | 152 ms                                                     | 160 ms: 1.05x slower                                                  |
| async_tree_eager_tg              | 41.4 ms                                                    | 44.4 ms: 1.07x slower                                                 |
| async_tree_memoization           | 260 ms                                                     | 279 ms: 1.08x slower                                                  |
| async_tree_none                  | 209 ms                                                     | 226 ms: 1.08x slower                                                  |
| async_tree_memoization_tg        | 240 ms                                                     | 261 ms: 1.09x slower                                                  |
| async_tree_eager                 | 60.3 ms                                                    | 69.1 ms: 1.15x slower                                                 |
| Geometric mean                   | (ref)                                                      | 1.05x slower                                                          |

Benchmark hidden because not significant (3): async_tree_io_tg, async_tree_cpu_io_mixed_tg, async_tree_eager_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240525-darwin-arm64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| pidigits       | 282 ms                                                     | 283 ms: 1.00x slower                                                  |
| float          | 48.6 ms                                                    | 61.3 ms: 1.26x slower                                                 |
| nbody          | 59.6 ms                                                    | 76.1 ms: 1.28x slower                                                 |
| Geometric mean | (ref)                                                      | 1.17x slower                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240525-darwin-arm64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 2.58 ms                                                    | 2.59 ms: 1.00x slower                                                 |
| regex_v8       | 17.3 ms                                                    | 17.6 ms: 1.02x slower                                                 |
| regex_compile  | 68.5 ms                                                    | 96.5 ms: 1.41x slower                                                 |
| Geometric mean | (ref)                                                      | 1.10x slower                                                          |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240525-darwin-arm64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle               | 7.48 us                                                    | 7.41 us: 1.01x faster                                                 |
| pickle_dict          | 18.3 us                                                    | 18.2 us: 1.00x faster                                                 |
| unpickle_list        | 2.88 us                                                    | 2.90 us: 1.01x slower                                                 |
| json_loads           | 16.8 us                                                    | 17.0 us: 1.01x slower                                                 |
| xml_etree_parse      | 106 ms                                                     | 106 ms: 1.01x slower                                                  |
| unpickle             | 9.12 us                                                    | 9.28 us: 1.02x slower                                                 |
| json_dumps           | 6.23 ms                                                    | 6.62 ms: 1.06x slower                                                 |
| xml_etree_iterparse  | 71.5 ms                                                    | 76.6 ms: 1.07x slower                                                 |
| xml_etree_process    | 37.1 ms                                                    | 41.4 ms: 1.12x slower                                                 |
| xml_etree_generate   | 52.7 ms                                                    | 59.0 ms: 1.12x slower                                                 |
| tomli_loads          | 1.47 sec                                                   | 1.65 sec: 1.13x slower                                                |
| unpickle_pure_python | 141 us                                                     | 179 us: 1.27x slower                                                  |
| pickle_pure_python   | 179 us                                                     | 228 us: 1.28x slower                                                  |
| Geometric mean       | (ref)                                                      | 1.07x slower                                                          |

Benchmark hidden because not significant (1): pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240525-darwin-arm64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 15.2 ms                                                    | 14.6 ms: 1.04x faster                                                 |
| python_startup_no_site | 12.3 ms                                                    | 12.0 ms: 1.03x faster                                                 |
| Geometric mean         | (ref)                                                      | 1.03x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240525-darwin-arm64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|-----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_xml      | 29.9 ms                                                    | 36.4 ms: 1.22x slower                                                 |
| django_template | 19.4 ms                                                    | 24.1 ms: 1.24x slower                                                 |
| genshi_text     | 13.9 ms                                                    | 17.5 ms: 1.26x slower                                                 |
| mako            | 6.99 ms                                                    | 9.12 ms: 1.31x slower                                                 |
| Geometric mean  | (ref)                                                      | 1.25x slower                                                          |

All benchmarks:
===============

| Benchmark                        | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240525-darwin-arm64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup                   | 15.2 ms                                                    | 14.6 ms: 1.04x faster                                                 |
| python_startup_no_site           | 12.3 ms                                                    | 12.0 ms: 1.03x faster                                                 |
| pathlib                          | 23.3 ms                                                    | 23.0 ms: 1.02x faster                                                 |
| pickle                           | 7.48 us                                                    | 7.41 us: 1.01x faster                                                 |
| pickle_dict                      | 18.3 us                                                    | 18.2 us: 1.00x faster                                                 |
| pidigits                         | 282 ms                                                     | 283 ms: 1.00x slower                                                  |
| regex_effbot                     | 2.58 ms                                                    | 2.59 ms: 1.00x slower                                                 |
| unpickle_list                    | 2.88 us                                                    | 2.90 us: 1.01x slower                                                 |
| json_loads                       | 16.8 us                                                    | 17.0 us: 1.01x slower                                                 |
| xml_etree_parse                  | 106 ms                                                     | 106 ms: 1.01x slower                                                  |
| create_gc_cycles                 | 897 us                                                     | 905 us: 1.01x slower                                                  |
| gc_traversal                     | 2.45 ms                                                    | 2.47 ms: 1.01x slower                                                 |
| json                             | 2.93 ms                                                    | 2.98 ms: 1.02x slower                                                 |
| async_tree_eager_cpu_io_mixed_tg | 331 ms                                                     | 336 ms: 1.02x slower                                                  |
| unpickle                         | 9.12 us                                                    | 9.28 us: 1.02x slower                                                 |
| thrift                           | 435 us                                                     | 443 us: 1.02x slower                                                  |
| regex_v8                         | 17.3 ms                                                    | 17.6 ms: 1.02x slower                                                 |
| generators                       | 22.9 ms                                                    | 23.4 ms: 1.02x slower                                                 |
| coverage                         | 45.0 ms                                                    | 46.2 ms: 1.03x slower                                                 |
| async_tree_eager_cpu_io_mixed    | 358 ms                                                     | 368 ms: 1.03x slower                                                  |
| dask                             | 221 ms                                                     | 228 ms: 1.03x slower                                                  |
| async_tree_eager_memoization_tg  | 126 ms                                                     | 130 ms: 1.03x slower                                                  |
| async_tree_eager_io              | 766 ms                                                     | 795 ms: 1.04x slower                                                  |
| sqlite_synth                     | 1.55 us                                                    | 1.61 us: 1.04x slower                                                 |
| async_tree_io                    | 563 ms                                                     | 587 ms: 1.04x slower                                                  |
| coroutines                       | 15.8 ms                                                    | 16.6 ms: 1.04x slower                                                 |
| async_tree_cpu_io_mixed          | 467 ms                                                     | 488 ms: 1.05x slower                                                  |
| async_tree_none_tg               | 198 ms                                                     | 207 ms: 1.05x slower                                                  |
| async_tree_eager_memoization     | 152 ms                                                     | 160 ms: 1.05x slower                                                  |
| async_generators                 | 281 ms                                                     | 295 ms: 1.05x slower                                                  |
| tornado_http                     | 66.7 ms                                                    | 70.6 ms: 1.06x slower                                                 |
| json_dumps                       | 6.23 ms                                                    | 6.62 ms: 1.06x slower                                                 |
| logging_simple                   | 3.04 us                                                    | 3.25 us: 1.07x slower                                                 |
| html5lib                         | 31.2 ms                                                    | 33.3 ms: 1.07x slower                                                 |
| xml_etree_iterparse              | 71.5 ms                                                    | 76.6 ms: 1.07x slower                                                 |
| async_tree_eager_tg              | 41.4 ms                                                    | 44.4 ms: 1.07x slower                                                 |
| mdp                              | 1.53 sec                                                   | 1.65 sec: 1.07x slower                                                |
| logging_format                   | 3.31 us                                                    | 3.56 us: 1.07x slower                                                 |
| async_tree_memoization           | 260 ms                                                     | 279 ms: 1.08x slower                                                  |
| async_tree_none                  | 209 ms                                                     | 226 ms: 1.08x slower                                                  |
| async_tree_memoization_tg        | 240 ms                                                     | 261 ms: 1.09x slower                                                  |
| telco                            | 4.60 ms                                                    | 5.05 ms: 1.10x slower                                                 |
| xml_etree_process                | 37.1 ms                                                    | 41.4 ms: 1.12x slower                                                 |
| xml_etree_generate               | 52.7 ms                                                    | 59.0 ms: 1.12x slower                                                 |
| scimark_sor                      | 94.9 ms                                                    | 107 ms: 1.13x slower                                                  |
| tomli_loads                      | 1.47 sec                                                   | 1.65 sec: 1.13x slower                                                |
| 2to3                             | 161 ms                                                     | 182 ms: 1.13x slower                                                  |
| meteor_contest                   | 70.3 ms                                                    | 80.1 ms: 1.14x slower                                                 |
| pylint                           | 170 ms                                                     | 194 ms: 1.14x slower                                                  |
| async_tree_eager                 | 60.3 ms                                                    | 69.1 ms: 1.15x slower                                                 |
| pycparser                        | 632 ms                                                     | 731 ms: 1.16x slower                                                  |
| richards_super                   | 35.2 ms                                                    | 40.9 ms: 1.16x slower                                                 |
| go                               | 101 ms                                                     | 117 ms: 1.17x slower                                                  |
| docutils                         | 1.44 sec                                                   | 1.68 sec: 1.17x slower                                                |
| chameleon                        | 4.27 ms                                                    | 4.99 ms: 1.17x slower                                                 |
| richards                         | 31.8 ms                                                    | 37.3 ms: 1.17x slower                                                 |
| deepcopy_reduce                  | 1.82 us                                                    | 2.15 us: 1.18x slower                                                 |
| sympy_expand                     | 226 ms                                                     | 266 ms: 1.18x slower                                                  |
| bench_thread_pool                | 447 us                                                     | 533 us: 1.19x slower                                                  |
| raytrace                         | 147 ms                                                     | 178 ms: 1.21x slower                                                  |
| sqlglot_optimize                 | 30.9 ms                                                    | 37.6 ms: 1.22x slower                                                 |
| genshi_xml                       | 29.9 ms                                                    | 36.4 ms: 1.22x slower                                                 |
| sympy_integrate                  | 10.3 ms                                                    | 12.7 ms: 1.23x slower                                                 |
| scimark_fft                      | 181 ms                                                     | 223 ms: 1.23x slower                                                  |
| deepcopy                         | 204 us                                                     | 253 us: 1.24x slower                                                  |
| crypto_pyaes                     | 49.5 ms                                                    | 61.3 ms: 1.24x slower                                                 |
| django_template                  | 19.4 ms                                                    | 24.1 ms: 1.24x slower                                                 |
| pprint_safe_repr                 | 465 ms                                                     | 576 ms: 1.24x slower                                                  |
| pprint_pformat                   | 947 ms                                                     | 1.18 sec: 1.24x slower                                                |
| pyflate                          | 321 ms                                                     | 399 ms: 1.24x slower                                                  |
| typing_runtime_protocols         | 87.6 us                                                    | 109 us: 1.25x slower                                                  |
| genshi_text                      | 13.9 ms                                                    | 17.5 ms: 1.26x slower                                                 |
| sympy_sum                        | 69.2 ms                                                    | 87.2 ms: 1.26x slower                                                 |
| sympy_str                        | 131 ms                                                     | 166 ms: 1.26x slower                                                  |
| float                            | 48.6 ms                                                    | 61.3 ms: 1.26x slower                                                 |
| unpickle_pure_python             | 141 us                                                     | 179 us: 1.27x slower                                                  |
| pickle_pure_python               | 179 us                                                     | 228 us: 1.28x slower                                                  |
| nbody                            | 59.6 ms                                                    | 76.1 ms: 1.28x slower                                                 |
| fannkuch                         | 248 ms                                                     | 319 ms: 1.29x slower                                                  |
| sqlglot_transpile                | 891 us                                                     | 1.16 ms: 1.30x slower                                                 |
| mako                             | 6.99 ms                                                    | 9.12 ms: 1.31x slower                                                 |
| sqlglot_parse                    | 732 us                                                     | 958 us: 1.31x slower                                                  |
| nqueens                          | 52.2 ms                                                    | 69.1 ms: 1.32x slower                                                 |
| deltablue                        | 2.14 ms                                                    | 2.93 ms: 1.37x slower                                                 |
| chaos                            | 34.0 ms                                                    | 46.8 ms: 1.38x slower                                                 |
| scimark_sparse_mat_mult          | 2.77 ms                                                    | 3.82 ms: 1.38x slower                                                 |
| regex_compile                    | 68.5 ms                                                    | 96.5 ms: 1.41x slower                                                 |
| spectral_norm                    | 66.4 ms                                                    | 94.6 ms: 1.42x slower                                                 |
| deepcopy_memo                    | 22.6 us                                                    | 32.6 us: 1.44x slower                                                 |
| scimark_monte_carlo              | 42.5 ms                                                    | 61.4 ms: 1.45x slower                                                 |
| hexiom                           | 4.06 ms                                                    | 5.98 ms: 1.47x slower                                                 |
| scimark_lu                       | 66.9 ms                                                    | 100.0 ms: 1.49x slower                                                |
| logging_silent                   | 60.1 ns                                                    | 95.9 ns: 1.59x slower                                                 |
| comprehensions                   | 10.2 us                                                    | 17.5 us: 1.72x slower                                                 |
| Geometric mean                   | (ref)                                                      | 1.14x slower                                                          |

Benchmark hidden because not significant (10): flaskblogging, asyncio_tcp_ssl, pickle_list, asyncio_websockets, async_tree_io_tg, regex_dna, bench_mp_pool, asyncio_tcp, async_tree_cpu_io_mixed_tg, async_tree_eager_io_tg
Ignored benchmarks (6) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, bpe_tokeniser, dulwich_log, gunicorn, mypy2, sqlglot_normalize

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.07x
- 95% likely to have a slowdown of 1.07x
- 99% likely to have a slowdown of 1.06x

# Memory
- memory change: 0.65x
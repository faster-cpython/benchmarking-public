# Results vs. 3.13.0b2

- fork: python
- ref: v3.13.0a5
- machine: darwin-arm64
- commit hash: 076d169
- commit date: 2024-03-12
- overall geometric mean: 1.08x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.07x slower
- Memory change: 0.43x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240312-darwin-arm64-python-v3.13.0a5-3.13.0a5-076d169 |
|----------------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| 2to3           | 161 ms                                                     | 173 ms: 1.07x slower                                       |
| chameleon      | 4.27 ms                                                    | 5.13 ms: 1.20x slower                                      |
| docutils       | 1.44 sec                                                   | 1.47 sec: 1.02x slower                                     |
| html5lib       | 31.2 ms                                                    | 35.5 ms: 1.14x slower                                      |
| Geometric mean | (ref)                                                      | 1.09x slower                                               |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240312-darwin-arm64-python-v3.13.0a5-3.13.0a5-076d169 |
|----------------------------------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| async_tree_eager_io_tg           | 768 ms                                                     | 649 ms: 1.18x faster                                       |
| async_tree_eager_io              | 766 ms                                                     | 676 ms: 1.13x faster                                       |
| async_tree_eager_cpu_io_mixed_tg | 331 ms                                                     | 344 ms: 1.04x slower                                       |
| async_tree_eager_cpu_io_mixed    | 358 ms                                                     | 374 ms: 1.04x slower                                       |
| async_tree_cpu_io_mixed          | 467 ms                                                     | 525 ms: 1.12x slower                                       |
| async_tree_eager_memoization_tg  | 126 ms                                                     | 141 ms: 1.13x slower                                       |
| async_tree_eager_memoization     | 152 ms                                                     | 175 ms: 1.15x slower                                       |
| async_tree_eager_tg              | 41.4 ms                                                    | 48.3 ms: 1.17x slower                                      |
| async_tree_cpu_io_mixed_tg       | 451 ms                                                     | 531 ms: 1.18x slower                                       |
| async_tree_io_tg                 | 565 ms                                                     | 672 ms: 1.19x slower                                       |
| async_tree_eager                 | 60.3 ms                                                    | 72.2 ms: 1.20x slower                                      |
| async_tree_none                  | 209 ms                                                     | 257 ms: 1.23x slower                                       |
| async_tree_io                    | 563 ms                                                     | 710 ms: 1.26x slower                                       |
| async_tree_memoization           | 260 ms                                                     | 335 ms: 1.29x slower                                       |
| async_tree_none_tg               | 198 ms                                                     | 259 ms: 1.31x slower                                       |
| async_tree_memoization_tg        | 240 ms                                                     | 323 ms: 1.35x slower                                       |
| Geometric mean                   | (ref)                                                      | 1.14x slower                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240312-darwin-arm64-python-v3.13.0a5-3.13.0a5-076d169 |
|----------------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| pidigits       | 282 ms                                                     | 282 ms: 1.00x slower                                       |
| float          | 48.6 ms                                                    | 57.0 ms: 1.17x slower                                      |
| nbody          | 59.6 ms                                                    | 73.7 ms: 1.24x slower                                      |
| Geometric mean | (ref)                                                      | 1.13x slower                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240312-darwin-arm64-python-v3.13.0a5-3.13.0a5-076d169 |
|----------------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| regex_v8       | 17.3 ms                                                    | 17.1 ms: 1.01x faster                                      |
| regex_effbot   | 2.58 ms                                                    | 2.56 ms: 1.01x faster                                      |
| regex_dna      | 149 ms                                                     | 152 ms: 1.02x slower                                       |
| regex_compile  | 68.5 ms                                                    | 75.1 ms: 1.10x slower                                      |
| Geometric mean | (ref)                                                      | 1.02x slower                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240312-darwin-arm64-python-v3.13.0a5-3.13.0a5-076d169 |
|----------------------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| pickle               | 7.48 us                                                    | 7.31 us: 1.02x faster                                      |
| pickle_dict          | 18.3 us                                                    | 18.2 us: 1.00x faster                                      |
| xml_etree_parse      | 106 ms                                                     | 106 ms: 1.01x slower                                       |
| json_loads           | 16.8 us                                                    | 17.1 us: 1.02x slower                                      |
| unpickle             | 9.12 us                                                    | 9.30 us: 1.02x slower                                      |
| json_dumps           | 6.23 ms                                                    | 6.52 ms: 1.05x slower                                      |
| unpickle_list        | 2.88 us                                                    | 3.05 us: 1.06x slower                                      |
| tomli_loads          | 1.47 sec                                                   | 1.55 sec: 1.06x slower                                     |
| xml_etree_iterparse  | 71.5 ms                                                    | 75.9 ms: 1.06x slower                                      |
| xml_etree_process    | 37.1 ms                                                    | 40.4 ms: 1.09x slower                                      |
| xml_etree_generate   | 52.7 ms                                                    | 58.1 ms: 1.10x slower                                      |
| unpickle_pure_python | 141 us                                                     | 157 us: 1.11x slower                                       |
| pickle_pure_python   | 179 us                                                     | 201 us: 1.13x slower                                       |
| Geometric mean       | (ref)                                                      | 1.05x slower                                               |

Benchmark hidden because not significant (1): pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240312-darwin-arm64-python-v3.13.0a5-3.13.0a5-076d169 |
|------------------------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| python_startup         | 15.2 ms                                                    | 12.9 ms: 1.18x faster                                      |
| python_startup_no_site | 12.3 ms                                                    | 11.3 ms: 1.09x faster                                      |
| Geometric mean         | (ref)                                                      | 1.13x faster                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240312-darwin-arm64-python-v3.13.0a5-3.13.0a5-076d169 |
|-----------------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| mako            | 6.99 ms                                                    | 7.57 ms: 1.08x slower                                      |
| genshi_xml      | 29.9 ms                                                    | 33.8 ms: 1.13x slower                                      |
| django_template | 19.4 ms                                                    | 22.2 ms: 1.14x slower                                      |
| genshi_text     | 13.9 ms                                                    | 15.9 ms: 1.14x slower                                      |
| Geometric mean  | (ref)                                                      | 1.12x slower                                               |

All benchmarks:
===============

| Benchmark                        | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240312-darwin-arm64-python-v3.13.0a5-3.13.0a5-076d169 |
|----------------------------------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| create_gc_cycles                 | 897 us                                                     | 710 us: 1.26x faster                                       |
| typing_runtime_protocols         | 87.6 us                                                    | 72.9 us: 1.20x faster                                      |
| async_tree_eager_io_tg           | 768 ms                                                     | 649 ms: 1.18x faster                                       |
| python_startup                   | 15.2 ms                                                    | 12.9 ms: 1.18x faster                                      |
| async_tree_eager_io              | 766 ms                                                     | 676 ms: 1.13x faster                                       |
| python_startup_no_site           | 12.3 ms                                                    | 11.3 ms: 1.09x faster                                      |
| flaskblogging                    | 3.61 ms                                                    | 3.40 ms: 1.06x faster                                      |
| bench_mp_pool                    | 47.2 ms                                                    | 45.4 ms: 1.04x faster                                      |
| pickle                           | 7.48 us                                                    | 7.31 us: 1.02x faster                                      |
| crypto_pyaes                     | 49.5 ms                                                    | 48.7 ms: 1.02x faster                                      |
| gc_traversal                     | 2.45 ms                                                    | 2.42 ms: 1.01x faster                                      |
| regex_v8                         | 17.3 ms                                                    | 17.1 ms: 1.01x faster                                      |
| regex_effbot                     | 2.58 ms                                                    | 2.56 ms: 1.01x faster                                      |
| pickle_dict                      | 18.3 us                                                    | 18.2 us: 1.00x faster                                      |
| asyncio_websockets               | 409 ms                                                     | 408 ms: 1.00x faster                                       |
| pidigits                         | 282 ms                                                     | 282 ms: 1.00x slower                                       |
| telco                            | 4.60 ms                                                    | 4.63 ms: 1.01x slower                                      |
| xml_etree_parse                  | 106 ms                                                     | 106 ms: 1.01x slower                                       |
| json                             | 2.93 ms                                                    | 2.95 ms: 1.01x slower                                      |
| sqlite_synth                     | 1.55 us                                                    | 1.57 us: 1.02x slower                                      |
| json_loads                       | 16.8 us                                                    | 17.1 us: 1.02x slower                                      |
| regex_dna                        | 149 ms                                                     | 152 ms: 1.02x slower                                       |
| dask                             | 221 ms                                                     | 225 ms: 1.02x slower                                       |
| unpickle                         | 9.12 us                                                    | 9.30 us: 1.02x slower                                      |
| docutils                         | 1.44 sec                                                   | 1.47 sec: 1.02x slower                                     |
| asyncio_tcp_ssl                  | 1.29 sec                                                   | 1.32 sec: 1.03x slower                                     |
| thrift                           | 435 us                                                     | 452 us: 1.04x slower                                       |
| async_tree_eager_cpu_io_mixed_tg | 331 ms                                                     | 344 ms: 1.04x slower                                       |
| async_tree_eager_cpu_io_mixed    | 358 ms                                                     | 374 ms: 1.04x slower                                       |
| gunicorn                         | 1.04 ms                                                    | 1.08 ms: 1.04x slower                                      |
| meteor_contest                   | 70.3 ms                                                    | 73.6 ms: 1.05x slower                                      |
| json_dumps                       | 6.23 ms                                                    | 6.52 ms: 1.05x slower                                      |
| go                               | 101 ms                                                     | 105 ms: 1.05x slower                                       |
| sympy_integrate                  | 10.3 ms                                                    | 10.9 ms: 1.05x slower                                      |
| unpickle_list                    | 2.88 us                                                    | 3.05 us: 1.06x slower                                      |
| tomli_loads                      | 1.47 sec                                                   | 1.55 sec: 1.06x slower                                     |
| aiohttp                          | 997 us                                                     | 1.06 ms: 1.06x slower                                      |
| xml_etree_iterparse              | 71.5 ms                                                    | 75.9 ms: 1.06x slower                                      |
| pathlib                          | 23.3 ms                                                    | 24.8 ms: 1.06x slower                                      |
| pyflate                          | 321 ms                                                     | 342 ms: 1.07x slower                                       |
| mdp                              | 1.53 sec                                                   | 1.64 sec: 1.07x slower                                     |
| dulwich_log                      | 27.6 ms                                                    | 29.6 ms: 1.07x slower                                      |
| 2to3                             | 161 ms                                                     | 173 ms: 1.07x slower                                       |
| coverage                         | 45.0 ms                                                    | 48.4 ms: 1.08x slower                                      |
| async_generators                 | 281 ms                                                     | 302 ms: 1.08x slower                                       |
| sympy_expand                     | 226 ms                                                     | 243 ms: 1.08x slower                                       |
| richards_super                   | 35.2 ms                                                    | 38.0 ms: 1.08x slower                                      |
| sympy_sum                        | 69.2 ms                                                    | 75.0 ms: 1.08x slower                                      |
| richards                         | 31.8 ms                                                    | 34.5 ms: 1.08x slower                                      |
| mako                             | 6.99 ms                                                    | 7.57 ms: 1.08x slower                                      |
| sqlglot_parse                    | 732 us                                                     | 795 us: 1.09x slower                                       |
| asyncio_tcp                      | 402 ms                                                     | 438 ms: 1.09x slower                                       |
| sympy_str                        | 131 ms                                                     | 143 ms: 1.09x slower                                       |
| xml_etree_process                | 37.1 ms                                                    | 40.4 ms: 1.09x slower                                      |
| sqlglot_transpile                | 891 us                                                     | 972 us: 1.09x slower                                       |
| regex_compile                    | 68.5 ms                                                    | 75.1 ms: 1.10x slower                                      |
| xml_etree_generate               | 52.7 ms                                                    | 58.1 ms: 1.10x slower                                      |
| fannkuch                         | 248 ms                                                     | 274 ms: 1.10x slower                                       |
| pycparser                        | 632 ms                                                     | 700 ms: 1.11x slower                                       |
| sqlglot_optimize                 | 30.9 ms                                                    | 34.2 ms: 1.11x slower                                      |
| bench_thread_pool                | 447 us                                                     | 495 us: 1.11x slower                                       |
| scimark_sor                      | 94.9 ms                                                    | 105 ms: 1.11x slower                                       |
| scimark_lu                       | 66.9 ms                                                    | 74.3 ms: 1.11x slower                                      |
| unpickle_pure_python             | 141 us                                                     | 157 us: 1.11x slower                                       |
| sqlglot_normalize                | 166 ms                                                     | 185 ms: 1.11x slower                                       |
| pprint_pformat                   | 947 ms                                                     | 1.06 sec: 1.12x slower                                     |
| pprint_safe_repr                 | 465 ms                                                     | 522 ms: 1.12x slower                                       |
| async_tree_cpu_io_mixed          | 467 ms                                                     | 525 ms: 1.12x slower                                       |
| deepcopy                         | 204 us                                                     | 230 us: 1.13x slower                                       |
| async_tree_eager_memoization_tg  | 126 ms                                                     | 141 ms: 1.13x slower                                       |
| pickle_pure_python               | 179 us                                                     | 201 us: 1.13x slower                                       |
| genshi_xml                       | 29.9 ms                                                    | 33.8 ms: 1.13x slower                                      |
| scimark_sparse_mat_mult          | 2.77 ms                                                    | 3.13 ms: 1.13x slower                                      |
| deepcopy_reduce                  | 1.82 us                                                    | 2.06 us: 1.13x slower                                      |
| scimark_monte_carlo              | 42.5 ms                                                    | 48.3 ms: 1.14x slower                                      |
| html5lib                         | 31.2 ms                                                    | 35.5 ms: 1.14x slower                                      |
| django_template                  | 19.4 ms                                                    | 22.2 ms: 1.14x slower                                      |
| spectral_norm                    | 66.4 ms                                                    | 75.8 ms: 1.14x slower                                      |
| genshi_text                      | 13.9 ms                                                    | 15.9 ms: 1.14x slower                                      |
| scimark_fft                      | 181 ms                                                     | 207 ms: 1.14x slower                                       |
| deltablue                        | 2.14 ms                                                    | 2.45 ms: 1.15x slower                                      |
| logging_format                   | 3.31 us                                                    | 3.80 us: 1.15x slower                                      |
| deepcopy_memo                    | 22.6 us                                                    | 25.9 us: 1.15x slower                                      |
| logging_simple                   | 3.04 us                                                    | 3.50 us: 1.15x slower                                      |
| async_tree_eager_memoization     | 152 ms                                                     | 175 ms: 1.15x slower                                       |
| logging_silent                   | 60.1 ns                                                    | 70.0 ns: 1.16x slower                                      |
| raytrace                         | 147 ms                                                     | 171 ms: 1.16x slower                                       |
| async_tree_eager_tg              | 41.4 ms                                                    | 48.3 ms: 1.17x slower                                      |
| float                            | 48.6 ms                                                    | 57.0 ms: 1.17x slower                                      |
| chaos                            | 34.0 ms                                                    | 39.9 ms: 1.17x slower                                      |
| async_tree_cpu_io_mixed_tg       | 451 ms                                                     | 531 ms: 1.18x slower                                       |
| comprehensions                   | 10.2 us                                                    | 12.1 us: 1.19x slower                                      |
| hexiom                           | 4.06 ms                                                    | 4.83 ms: 1.19x slower                                      |
| async_tree_io_tg                 | 565 ms                                                     | 672 ms: 1.19x slower                                       |
| async_tree_eager                 | 60.3 ms                                                    | 72.2 ms: 1.20x slower                                      |
| chameleon                        | 4.27 ms                                                    | 5.13 ms: 1.20x slower                                      |
| mypy2                            | 379 ms                                                     | 457 ms: 1.20x slower                                       |
| coroutines                       | 15.8 ms                                                    | 19.2 ms: 1.21x slower                                      |
| async_tree_none                  | 209 ms                                                     | 257 ms: 1.23x slower                                       |
| nbody                            | 59.6 ms                                                    | 73.7 ms: 1.24x slower                                      |
| generators                       | 22.9 ms                                                    | 28.6 ms: 1.25x slower                                      |
| nqueens                          | 52.2 ms                                                    | 65.2 ms: 1.25x slower                                      |
| async_tree_io                    | 563 ms                                                     | 710 ms: 1.26x slower                                       |
| async_tree_memoization           | 260 ms                                                     | 335 ms: 1.29x slower                                       |
| async_tree_none_tg               | 198 ms                                                     | 259 ms: 1.31x slower                                       |
| async_tree_memoization_tg        | 240 ms                                                     | 323 ms: 1.35x slower                                       |
| Geometric mean                   | (ref)                                                      | 1.08x slower                                               |

Benchmark hidden because not significant (3): pickle_list, pylint, tornado_http
Ignored benchmarks (1) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17.json: bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.07x
- 95% likely to have a slowdown of 1.07x
- 99% likely to have a slowdown of 1.07x

# Memory
- memory change: 0.43x
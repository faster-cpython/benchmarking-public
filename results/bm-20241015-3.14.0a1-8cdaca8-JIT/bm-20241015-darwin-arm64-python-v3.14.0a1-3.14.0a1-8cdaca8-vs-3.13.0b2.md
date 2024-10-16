# Results vs. 3.13.0b2

- fork: python
- ref: v3.14.0a1
- machine: darwin-arm64
- commit hash: 8cdaca8
- commit date: 2024-10-15
- overall geometric mean: 1.05x slower
- HPT reliability: 99.99%
- HPT 99th percentile: 1.01x slower
- Memory change: 1.20x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241015-darwin-arm64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| 2to3           | 161 ms                                                     | 183 ms: 1.14x slower                                       |
| docutils       | 1.44 sec                                                   | 1.57 sec: 1.09x slower                                     |
| html5lib       | 31.2 ms                                                    | 34.2 ms: 1.10x slower                                      |
| Geometric mean | (ref)                                                      | 1.11x slower                                               |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241015-darwin-arm64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------------------------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| async_tree_eager_io              | 766 ms                                                     | 667 ms: 1.15x faster                                       |
| async_tree_eager_io_tg           | 768 ms                                                     | 714 ms: 1.08x faster                                       |
| async_tree_memoization           | 260 ms                                                     | 246 ms: 1.06x faster                                       |
| async_tree_none                  | 209 ms                                                     | 199 ms: 1.05x faster                                       |
| async_tree_cpu_io_mixed          | 467 ms                                                     | 459 ms: 1.02x faster                                       |
| async_tree_eager_cpu_io_mixed    | 358 ms                                                     | 363 ms: 1.01x slower                                       |
| async_tree_eager_cpu_io_mixed_tg | 331 ms                                                     | 336 ms: 1.02x slower                                       |
| async_tree_eager_tg              | 41.4 ms                                                    | 42.6 ms: 1.03x slower                                      |
| async_tree_io                    | 563 ms                                                     | 584 ms: 1.04x slower                                       |
| async_tree_eager_memoization_tg  | 126 ms                                                     | 130 ms: 1.04x slower                                       |
| async_tree_cpu_io_mixed_tg       | 451 ms                                                     | 470 ms: 1.04x slower                                       |
| async_tree_eager                 | 60.3 ms                                                    | 63.5 ms: 1.05x slower                                      |
| async_tree_none_tg               | 198 ms                                                     | 213 ms: 1.08x slower                                       |
| async_tree_io_tg                 | 565 ms                                                     | 611 ms: 1.08x slower                                       |
| Geometric mean                   | (ref)                                                      | 1.00x slower                                               |

Benchmark hidden because not significant (2): async_tree_memoization_tg, async_tree_eager_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241015-darwin-arm64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| float          | 48.6 ms                                                    | 48.2 ms: 1.01x faster                                      |
| pidigits       | 282 ms                                                     | 283 ms: 1.00x slower                                       |
| nbody          | 59.6 ms                                                    | 65.3 ms: 1.10x slower                                      |
| Geometric mean | (ref)                                                      | 1.03x slower                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241015-darwin-arm64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| regex_v8       | 17.3 ms                                                    | 16.8 ms: 1.03x faster                                      |
| regex_dna      | 149 ms                                                     | 148 ms: 1.01x faster                                       |
| regex_effbot   | 2.58 ms                                                    | 2.61 ms: 1.01x slower                                      |
| regex_compile  | 68.5 ms                                                    | 74.8 ms: 1.09x slower                                      |
| Geometric mean | (ref)                                                      | 1.01x slower                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241015-darwin-arm64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| tomli_loads          | 1.47 sec                                                   | 1.25 sec: 1.18x faster                                     |
| unpickle_pure_python | 141 us                                                     | 132 us: 1.07x faster                                       |
| xml_etree_process    | 37.1 ms                                                    | 34.8 ms: 1.07x faster                                      |
| xml_etree_generate   | 52.7 ms                                                    | 50.4 ms: 1.05x faster                                      |
| pickle               | 7.48 us                                                    | 7.33 us: 1.02x faster                                      |
| json_loads           | 16.8 us                                                    | 16.5 us: 1.02x faster                                      |
| unpickle             | 9.12 us                                                    | 9.02 us: 1.01x faster                                      |
| pickle_dict          | 18.3 us                                                    | 18.2 us: 1.01x faster                                      |
| xml_etree_parse      | 106 ms                                                     | 107 ms: 1.02x slower                                       |
| xml_etree_iterparse  | 71.5 ms                                                    | 73.1 ms: 1.02x slower                                      |
| unpickle_list        | 2.88 us                                                    | 2.97 us: 1.03x slower                                      |
| json_dumps           | 6.23 ms                                                    | 7.13 ms: 1.14x slower                                      |
| Geometric mean       | (ref)                                                      | 1.01x faster                                               |

Benchmark hidden because not significant (2): pickle_pure_python, pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241015-darwin-arm64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|------------------------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| python_startup_no_site | 12.3 ms                                                    | 14.6 ms: 1.19x slower                                      |
| python_startup         | 15.2 ms                                                    | 19.0 ms: 1.25x slower                                      |
| Geometric mean         | (ref)                                                      | 1.22x slower                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241015-darwin-arm64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|-----------------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| mako            | 6.99 ms                                                    | 6.46 ms: 1.08x faster                                      |
| django_template | 19.4 ms                                                    | 23.0 ms: 1.18x slower                                      |
| genshi_text     | 13.9 ms                                                    | 16.6 ms: 1.20x slower                                      |
| genshi_xml      | 29.9 ms                                                    | 42.3 ms: 1.41x slower                                      |
| Geometric mean  | (ref)                                                      | 1.17x slower                                               |

All benchmarks:
===============

| Benchmark                        | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241015-darwin-arm64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------------------------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| asyncio_websockets               | 409 ms                                                     | 242 ms: 1.69x faster                                       |
| deepcopy_memo                    | 22.6 us                                                    | 16.8 us: 1.35x faster                                      |
| deepcopy                         | 204 us                                                     | 154 us: 1.32x faster                                       |
| deepcopy_reduce                  | 1.82 us                                                    | 1.53 us: 1.19x faster                                      |
| tomli_loads                      | 1.47 sec                                                   | 1.25 sec: 1.18x faster                                     |
| async_tree_eager_io              | 766 ms                                                     | 667 ms: 1.15x faster                                       |
| scimark_sor                      | 94.9 ms                                                    | 86.0 ms: 1.10x faster                                      |
| mako                             | 6.99 ms                                                    | 6.46 ms: 1.08x faster                                      |
| async_tree_eager_io_tg           | 768 ms                                                     | 714 ms: 1.08x faster                                       |
| unpickle_pure_python             | 141 us                                                     | 132 us: 1.07x faster                                       |
| xml_etree_process                | 37.1 ms                                                    | 34.8 ms: 1.07x faster                                      |
| async_tree_memoization           | 260 ms                                                     | 246 ms: 1.06x faster                                       |
| async_tree_none                  | 209 ms                                                     | 199 ms: 1.05x faster                                       |
| xml_etree_generate               | 52.7 ms                                                    | 50.4 ms: 1.05x faster                                      |
| pathlib                          | 23.3 ms                                                    | 22.4 ms: 1.04x faster                                      |
| scimark_lu                       | 66.9 ms                                                    | 64.6 ms: 1.04x faster                                      |
| go                               | 101 ms                                                     | 97.6 ms: 1.03x faster                                      |
| coverage                         | 45.0 ms                                                    | 43.8 ms: 1.03x faster                                      |
| regex_v8                         | 17.3 ms                                                    | 16.8 ms: 1.03x faster                                      |
| thrift                           | 435 us                                                     | 426 us: 1.02x faster                                       |
| pickle                           | 7.48 us                                                    | 7.33 us: 1.02x faster                                      |
| json_loads                       | 16.8 us                                                    | 16.5 us: 1.02x faster                                      |
| async_tree_cpu_io_mixed          | 467 ms                                                     | 459 ms: 1.02x faster                                       |
| unpickle                         | 9.12 us                                                    | 9.02 us: 1.01x faster                                      |
| regex_dna                        | 149 ms                                                     | 148 ms: 1.01x faster                                       |
| sqlite_synth                     | 1.55 us                                                    | 1.54 us: 1.01x faster                                      |
| float                            | 48.6 ms                                                    | 48.2 ms: 1.01x faster                                      |
| telco                            | 4.60 ms                                                    | 4.57 ms: 1.01x faster                                      |
| pickle_dict                      | 18.3 us                                                    | 18.2 us: 1.01x faster                                      |
| bpe_tokeniser                    | 3.05 sec                                                   | 3.05 sec: 1.00x faster                                     |
| pidigits                         | 282 ms                                                     | 283 ms: 1.00x slower                                       |
| regex_effbot                     | 2.58 ms                                                    | 2.61 ms: 1.01x slower                                      |
| pyflate                          | 321 ms                                                     | 325 ms: 1.01x slower                                       |
| async_tree_eager_cpu_io_mixed    | 358 ms                                                     | 363 ms: 1.01x slower                                       |
| xml_etree_parse                  | 106 ms                                                     | 107 ms: 1.02x slower                                       |
| async_tree_eager_cpu_io_mixed_tg | 331 ms                                                     | 336 ms: 1.02x slower                                       |
| mdp                              | 1.53 sec                                                   | 1.56 sec: 1.02x slower                                     |
| logging_simple                   | 3.04 us                                                    | 3.10 us: 1.02x slower                                      |
| xml_etree_iterparse              | 71.5 ms                                                    | 73.1 ms: 1.02x slower                                      |
| unpickle_list                    | 2.88 us                                                    | 2.97 us: 1.03x slower                                      |
| async_tree_eager_tg              | 41.4 ms                                                    | 42.6 ms: 1.03x slower                                      |
| logging_format                   | 3.31 us                                                    | 3.42 us: 1.03x slower                                      |
| async_tree_io                    | 563 ms                                                     | 584 ms: 1.04x slower                                       |
| pprint_safe_repr                 | 465 ms                                                     | 483 ms: 1.04x slower                                       |
| async_tree_eager_memoization_tg  | 126 ms                                                     | 130 ms: 1.04x slower                                       |
| async_generators                 | 281 ms                                                     | 292 ms: 1.04x slower                                       |
| async_tree_cpu_io_mixed_tg       | 451 ms                                                     | 470 ms: 1.04x slower                                       |
| spectral_norm                    | 66.4 ms                                                    | 69.3 ms: 1.04x slower                                      |
| pprint_pformat                   | 947 ms                                                     | 990 ms: 1.05x slower                                       |
| dulwich_log                      | 27.6 ms                                                    | 28.9 ms: 1.05x slower                                      |
| scimark_fft                      | 181 ms                                                     | 190 ms: 1.05x slower                                       |
| coroutines                       | 15.8 ms                                                    | 16.7 ms: 1.05x slower                                      |
| async_tree_eager                 | 60.3 ms                                                    | 63.5 ms: 1.05x slower                                      |
| meteor_contest                   | 70.3 ms                                                    | 74.4 ms: 1.06x slower                                      |
| bench_thread_pool                | 447 us                                                     | 474 us: 1.06x slower                                       |
| pycparser                        | 632 ms                                                     | 678 ms: 1.07x slower                                       |
| scimark_monte_carlo              | 42.5 ms                                                    | 45.5 ms: 1.07x slower                                      |
| async_tree_none_tg               | 198 ms                                                     | 213 ms: 1.08x slower                                       |
| fannkuch                         | 248 ms                                                     | 269 ms: 1.08x slower                                       |
| async_tree_io_tg                 | 565 ms                                                     | 611 ms: 1.08x slower                                       |
| sympy_expand                     | 226 ms                                                     | 246 ms: 1.09x slower                                       |
| regex_compile                    | 68.5 ms                                                    | 74.8 ms: 1.09x slower                                      |
| crypto_pyaes                     | 49.5 ms                                                    | 54.0 ms: 1.09x slower                                      |
| docutils                         | 1.44 sec                                                   | 1.57 sec: 1.09x slower                                     |
| nbody                            | 59.6 ms                                                    | 65.3 ms: 1.10x slower                                      |
| html5lib                         | 31.2 ms                                                    | 34.2 ms: 1.10x slower                                      |
| richards_super                   | 35.2 ms                                                    | 38.7 ms: 1.10x slower                                      |
| richards                         | 31.8 ms                                                    | 35.0 ms: 1.10x slower                                      |
| generators                       | 22.9 ms                                                    | 25.4 ms: 1.11x slower                                      |
| deltablue                        | 2.14 ms                                                    | 2.38 ms: 1.11x slower                                      |
| typing_runtime_protocols         | 87.6 us                                                    | 97.8 us: 1.12x slower                                      |
| sqlglot_normalize                | 166 ms                                                     | 186 ms: 1.12x slower                                       |
| nqueens                          | 52.2 ms                                                    | 58.8 ms: 1.13x slower                                      |
| asyncio_tcp                      | 402 ms                                                     | 456 ms: 1.13x slower                                       |
| scimark_sparse_mat_mult          | 2.77 ms                                                    | 3.14 ms: 1.13x slower                                      |
| 2to3                             | 161 ms                                                     | 183 ms: 1.14x slower                                       |
| json_dumps                       | 6.23 ms                                                    | 7.13 ms: 1.14x slower                                      |
| sympy_str                        | 131 ms                                                     | 151 ms: 1.15x slower                                       |
| sympy_sum                        | 69.2 ms                                                    | 79.4 ms: 1.15x slower                                      |
| logging_silent                   | 60.1 ns                                                    | 69.8 ns: 1.16x slower                                      |
| raytrace                         | 147 ms                                                     | 171 ms: 1.16x slower                                       |
| django_template                  | 19.4 ms                                                    | 23.0 ms: 1.18x slower                                      |
| sqlglot_transpile                | 891 us                                                     | 1.06 ms: 1.19x slower                                      |
| python_startup_no_site           | 12.3 ms                                                    | 14.6 ms: 1.19x slower                                      |
| sqlglot_parse                    | 732 us                                                     | 875 us: 1.20x slower                                       |
| genshi_text                      | 13.9 ms                                                    | 16.6 ms: 1.20x slower                                      |
| gc_traversal                     | 2.45 ms                                                    | 2.94 ms: 1.20x slower                                      |
| sqlglot_optimize                 | 30.9 ms                                                    | 37.1 ms: 1.20x slower                                      |
| sympy_integrate                  | 10.3 ms                                                    | 12.5 ms: 1.21x slower                                      |
| chaos                            | 34.0 ms                                                    | 41.5 ms: 1.22x slower                                      |
| hexiom                           | 4.06 ms                                                    | 4.96 ms: 1.22x slower                                      |
| pylint                           | 170 ms                                                     | 212 ms: 1.24x slower                                       |
| python_startup                   | 15.2 ms                                                    | 19.0 ms: 1.25x slower                                      |
| comprehensions                   | 10.2 us                                                    | 13.1 us: 1.29x slower                                      |
| bench_mp_pool                    | 47.2 ms                                                    | 61.8 ms: 1.31x slower                                      |
| genshi_xml                       | 29.9 ms                                                    | 42.3 ms: 1.41x slower                                      |
| create_gc_cycles                 | 897 us                                                     | 1.30 ms: 1.45x slower                                      |
| Geometric mean                   | (ref)                                                      | 1.05x slower                                               |

Benchmark hidden because not significant (7): async_tree_memoization_tg, pickle_pure_python, pickle_list, json, async_tree_eager_memoization, asyncio_tcp_ssl, tornado_http
Ignored benchmarks (6) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2
Ignored benchmarks (2) of results/bm-20241015-3.14.0a1-8cdaca8-JIT/bm-20241015-darwin-arm64-python-v3.14.0a1-3.14.0a1-8cdaca8.json: sphinx, unpack_sequence

# HPT report

- Reliability score: 99.99% likely to be slow
- 90% likely to have a slowdown of 1.03x
- 95% likely to have a slowdown of 1.02x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: 1.20x
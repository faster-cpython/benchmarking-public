# Results vs. 3.13.0b2

- fork: nick-arm
- ref: codecache
- machine: darwin-arm64
- commit hash: c2fad93
- commit date: 2024-10-17
- overall geometric mean: 1.01x slower
- HPT reliability: 99.01%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.17x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241017-darwin-arm64-nick%2darm-codecache-3.14.0a0-c2fad93 |
|----------------|:----------------------------------------------------------:|:--------------------------------------------------------------:|
| 2to3           | 161 ms                                                     | 170 ms: 1.06x slower                                           |
| docutils       | 1.44 sec                                                   | 1.50 sec: 1.04x slower                                         |
| html5lib       | 31.2 ms                                                    | 32.7 ms: 1.05x slower                                          |
| Geometric mean | (ref)                                                      | 1.07x slower                                                   |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241017-darwin-arm64-nick%2darm-codecache-3.14.0a0-c2fad93 |
|----------------------------------|:----------------------------------------------------------:|:--------------------------------------------------------------:|
| async_tree_eager_io              | 766 ms                                                     | 681 ms: 1.13x faster                                           |
| async_tree_eager_io_tg           | 768 ms                                                     | 703 ms: 1.09x faster                                           |
| async_tree_none                  | 209 ms                                                     | 198 ms: 1.06x faster                                           |
| async_tree_io_tg                 | 565 ms                                                     | 539 ms: 1.05x faster                                           |
| async_tree_cpu_io_mixed          | 467 ms                                                     | 454 ms: 1.03x faster                                           |
| async_tree_eager_cpu_io_mixed    | 358 ms                                                     | 360 ms: 1.01x slower                                           |
| async_tree_eager_tg              | 41.4 ms                                                    | 41.7 ms: 1.01x slower                                          |
| async_tree_eager_cpu_io_mixed_tg | 331 ms                                                     | 335 ms: 1.01x slower                                           |
| async_tree_eager                 | 60.3 ms                                                    | 61.9 ms: 1.03x slower                                          |
| async_tree_eager_memoization_tg  | 126 ms                                                     | 129 ms: 1.03x slower                                           |
| Geometric mean                   | (ref)                                                      | 1.01x faster                                                   |

Benchmark hidden because not significant (6): async_tree_none_tg, async_tree_eager_memoization, async_tree_memoization, async_tree_cpu_io_mixed_tg, async_tree_memoization_tg, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241017-darwin-arm64-nick%2darm-codecache-3.14.0a0-c2fad93 |
|----------------|:----------------------------------------------------------:|:--------------------------------------------------------------:|
| float          | 48.6 ms                                                    | 46.2 ms: 1.05x faster                                          |
| pidigits       | 282 ms                                                     | 283 ms: 1.00x slower                                           |
| nbody          | 59.6 ms                                                    | 63.7 ms: 1.07x slower                                          |
| Geometric mean | (ref)                                                      | 1.01x slower                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241017-darwin-arm64-nick%2darm-codecache-3.14.0a0-c2fad93 |
|----------------|:----------------------------------------------------------:|:--------------------------------------------------------------:|
| regex_v8       | 17.3 ms                                                    | 17.0 ms: 1.02x faster                                          |
| regex_effbot   | 2.58 ms                                                    | 2.63 ms: 1.02x slower                                          |
| regex_compile  | 68.5 ms                                                    | 72.0 ms: 1.05x slower                                          |
| Geometric mean | (ref)                                                      | 1.01x slower                                                   |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241017-darwin-arm64-nick%2darm-codecache-3.14.0a0-c2fad93 |
|----------------------|:----------------------------------------------------------:|:--------------------------------------------------------------:|
| tomli_loads          | 1.47 sec                                                   | 1.25 sec: 1.17x faster                                         |
| xml_etree_process    | 37.1 ms                                                    | 33.9 ms: 1.09x faster                                          |
| unpickle_pure_python | 141 us                                                     | 131 us: 1.07x faster                                           |
| xml_etree_generate   | 52.7 ms                                                    | 49.5 ms: 1.06x faster                                          |
| pickle               | 7.48 us                                                    | 7.29 us: 1.03x faster                                          |
| json_loads           | 16.8 us                                                    | 16.4 us: 1.02x faster                                          |
| pickle_pure_python   | 179 us                                                     | 176 us: 1.01x faster                                           |
| json_dumps           | 6.23 ms                                                    | 6.16 ms: 1.01x faster                                          |
| xml_etree_iterparse  | 71.5 ms                                                    | 72.4 ms: 1.01x slower                                          |
| pickle_dict          | 18.3 us                                                    | 18.6 us: 1.02x slower                                          |
| unpickle_list        | 2.88 us                                                    | 3.00 us: 1.04x slower                                          |
| pickle_list          | 2.96 us                                                    | 3.11 us: 1.05x slower                                          |
| Geometric mean       | (ref)                                                      | 1.02x faster                                                   |

Benchmark hidden because not significant (2): unpickle, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241017-darwin-arm64-nick%2darm-codecache-3.14.0a0-c2fad93 |
|------------------------|:----------------------------------------------------------:|:--------------------------------------------------------------:|
| python_startup_no_site | 12.3 ms                                                    | 14.9 ms: 1.21x slower                                          |
| python_startup         | 15.2 ms                                                    | 19.2 ms: 1.27x slower                                          |
| Geometric mean         | (ref)                                                      | 1.24x slower                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241017-darwin-arm64-nick%2darm-codecache-3.14.0a0-c2fad93 |
|-----------------|:----------------------------------------------------------:|:--------------------------------------------------------------:|
| mako            | 6.99 ms                                                    | 6.43 ms: 1.09x faster                                          |
| genshi_text     | 13.9 ms                                                    | 14.4 ms: 1.04x slower                                          |
| django_template | 19.4 ms                                                    | 20.2 ms: 1.04x slower                                          |
| genshi_xml      | 29.9 ms                                                    | 32.1 ms: 1.07x slower                                          |
| Geometric mean  | (ref)                                                      | 1.02x slower                                                   |

All benchmarks:
===============

| Benchmark                        | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241017-darwin-arm64-nick%2darm-codecache-3.14.0a0-c2fad93 |
|----------------------------------|:----------------------------------------------------------:|:--------------------------------------------------------------:|
| asyncio_websockets               | 409 ms                                                     | 242 ms: 1.69x faster                                           |
| deepcopy                         | 204 us                                                     | 149 us: 1.37x faster                                           |
| deepcopy_memo                    | 22.6 us                                                    | 16.6 us: 1.36x faster                                          |
| deepcopy_reduce                  | 1.82 us                                                    | 1.49 us: 1.22x faster                                          |
| tomli_loads                      | 1.47 sec                                                   | 1.25 sec: 1.17x faster                                         |
| async_tree_eager_io              | 766 ms                                                     | 681 ms: 1.13x faster                                           |
| scimark_sor                      | 94.9 ms                                                    | 85.8 ms: 1.11x faster                                          |
| xml_etree_process                | 37.1 ms                                                    | 33.9 ms: 1.09x faster                                          |
| async_tree_eager_io_tg           | 768 ms                                                     | 703 ms: 1.09x faster                                           |
| mako                             | 6.99 ms                                                    | 6.43 ms: 1.09x faster                                          |
| unpickle_pure_python             | 141 us                                                     | 131 us: 1.07x faster                                           |
| logging_silent                   | 60.1 ns                                                    | 56.4 ns: 1.07x faster                                          |
| xml_etree_generate               | 52.7 ms                                                    | 49.5 ms: 1.06x faster                                          |
| richards                         | 31.8 ms                                                    | 29.9 ms: 1.06x faster                                          |
| async_tree_none                  | 209 ms                                                     | 198 ms: 1.06x faster                                           |
| richards_super                   | 35.2 ms                                                    | 33.4 ms: 1.05x faster                                          |
| float                            | 48.6 ms                                                    | 46.2 ms: 1.05x faster                                          |
| pathlib                          | 23.3 ms                                                    | 22.2 ms: 1.05x faster                                          |
| async_tree_io_tg                 | 565 ms                                                     | 539 ms: 1.05x faster                                           |
| go                               | 101 ms                                                     | 96.1 ms: 1.05x faster                                          |
| scimark_lu                       | 66.9 ms                                                    | 64.0 ms: 1.05x faster                                          |
| mdp                              | 1.53 sec                                                   | 1.48 sec: 1.03x faster                                         |
| coverage                         | 45.0 ms                                                    | 43.5 ms: 1.03x faster                                          |
| thrift                           | 435 us                                                     | 423 us: 1.03x faster                                           |
| async_tree_cpu_io_mixed          | 467 ms                                                     | 454 ms: 1.03x faster                                           |
| pickle                           | 7.48 us                                                    | 7.29 us: 1.03x faster                                          |
| json_loads                       | 16.8 us                                                    | 16.4 us: 1.02x faster                                          |
| pyflate                          | 321 ms                                                     | 314 ms: 1.02x faster                                           |
| pprint_safe_repr                 | 465 ms                                                     | 456 ms: 1.02x faster                                           |
| regex_v8                         | 17.3 ms                                                    | 17.0 ms: 1.02x faster                                          |
| json                             | 2.93 ms                                                    | 2.89 ms: 1.01x faster                                          |
| pickle_pure_python               | 179 us                                                     | 176 us: 1.01x faster                                           |
| sqlite_synth                     | 1.55 us                                                    | 1.53 us: 1.01x faster                                          |
| json_dumps                       | 6.23 ms                                                    | 6.16 ms: 1.01x faster                                          |
| telco                            | 4.60 ms                                                    | 4.56 ms: 1.01x faster                                          |
| logging_simple                   | 3.04 us                                                    | 3.02 us: 1.01x faster                                          |
| pidigits                         | 282 ms                                                     | 283 ms: 1.00x slower                                           |
| async_tree_eager_cpu_io_mixed    | 358 ms                                                     | 360 ms: 1.01x slower                                           |
| async_tree_eager_tg              | 41.4 ms                                                    | 41.7 ms: 1.01x slower                                          |
| logging_format                   | 3.31 us                                                    | 3.33 us: 1.01x slower                                          |
| bpe_tokeniser                    | 3.05 sec                                                   | 3.08 sec: 1.01x slower                                         |
| xml_etree_iterparse              | 71.5 ms                                                    | 72.4 ms: 1.01x slower                                          |
| async_tree_eager_cpu_io_mixed_tg | 331 ms                                                     | 335 ms: 1.01x slower                                           |
| regex_effbot                     | 2.58 ms                                                    | 2.63 ms: 1.02x slower                                          |
| pickle_dict                      | 18.3 us                                                    | 18.6 us: 1.02x slower                                          |
| scimark_fft                      | 181 ms                                                     | 184 ms: 1.02x slower                                           |
| async_generators                 | 281 ms                                                     | 288 ms: 1.03x slower                                           |
| async_tree_eager                 | 60.3 ms                                                    | 61.9 ms: 1.03x slower                                          |
| async_tree_eager_memoization_tg  | 126 ms                                                     | 129 ms: 1.03x slower                                           |
| pycparser                        | 632 ms                                                     | 650 ms: 1.03x slower                                           |
| coroutines                       | 15.8 ms                                                    | 16.3 ms: 1.03x slower                                          |
| fannkuch                         | 248 ms                                                     | 257 ms: 1.03x slower                                           |
| spectral_norm                    | 66.4 ms                                                    | 68.6 ms: 1.03x slower                                          |
| genshi_text                      | 13.9 ms                                                    | 14.4 ms: 1.04x slower                                          |
| dulwich_log                      | 27.6 ms                                                    | 28.6 ms: 1.04x slower                                          |
| unpickle_list                    | 2.88 us                                                    | 3.00 us: 1.04x slower                                          |
| docutils                         | 1.44 sec                                                   | 1.50 sec: 1.04x slower                                         |
| django_template                  | 19.4 ms                                                    | 20.2 ms: 1.04x slower                                          |
| sympy_expand                     | 226 ms                                                     | 236 ms: 1.05x slower                                           |
| html5lib                         | 31.2 ms                                                    | 32.7 ms: 1.05x slower                                          |
| scimark_monte_carlo              | 42.5 ms                                                    | 44.6 ms: 1.05x slower                                          |
| regex_compile                    | 68.5 ms                                                    | 72.0 ms: 1.05x slower                                          |
| sqlglot_normalize                | 166 ms                                                     | 174 ms: 1.05x slower                                           |
| pickle_list                      | 2.96 us                                                    | 3.11 us: 1.05x slower                                          |
| crypto_pyaes                     | 49.5 ms                                                    | 52.2 ms: 1.05x slower                                          |
| generators                       | 22.9 ms                                                    | 24.2 ms: 1.06x slower                                          |
| 2to3                             | 161 ms                                                     | 170 ms: 1.06x slower                                           |
| meteor_contest                   | 70.3 ms                                                    | 74.5 ms: 1.06x slower                                          |
| bench_thread_pool                | 447 us                                                     | 475 us: 1.06x slower                                           |
| nbody                            | 59.6 ms                                                    | 63.7 ms: 1.07x slower                                          |
| scimark_sparse_mat_mult          | 2.77 ms                                                    | 2.97 ms: 1.07x slower                                          |
| genshi_xml                       | 29.9 ms                                                    | 32.1 ms: 1.07x slower                                          |
| sympy_sum                        | 69.2 ms                                                    | 74.5 ms: 1.08x slower                                          |
| deltablue                        | 2.14 ms                                                    | 2.31 ms: 1.08x slower                                          |
| sympy_str                        | 131 ms                                                     | 142 ms: 1.08x slower                                           |
| nqueens                          | 52.2 ms                                                    | 56.6 ms: 1.08x slower                                          |
| typing_runtime_protocols         | 87.6 us                                                    | 95.0 us: 1.09x slower                                          |
| sqlglot_optimize                 | 30.9 ms                                                    | 33.8 ms: 1.09x slower                                          |
| asyncio_tcp                      | 402 ms                                                     | 442 ms: 1.10x slower                                           |
| hexiom                           | 4.06 ms                                                    | 4.47 ms: 1.10x slower                                          |
| sqlglot_parse                    | 732 us                                                     | 808 us: 1.10x slower                                           |
| sqlglot_transpile                | 891 us                                                     | 984 us: 1.10x slower                                           |
| sympy_integrate                  | 10.3 ms                                                    | 11.8 ms: 1.14x slower                                          |
| pylint                           | 170 ms                                                     | 195 ms: 1.15x slower                                           |
| chaos                            | 34.0 ms                                                    | 39.8 ms: 1.17x slower                                          |
| gc_traversal                     | 2.45 ms                                                    | 2.91 ms: 1.19x slower                                          |
| python_startup_no_site           | 12.3 ms                                                    | 14.9 ms: 1.21x slower                                          |
| raytrace                         | 147 ms                                                     | 180 ms: 1.22x slower                                           |
| comprehensions                   | 10.2 us                                                    | 12.5 us: 1.23x slower                                          |
| python_startup                   | 15.2 ms                                                    | 19.2 ms: 1.27x slower                                          |
| bench_mp_pool                    | 47.2 ms                                                    | 61.0 ms: 1.29x slower                                          |
| create_gc_cycles                 | 897 us                                                     | 1.29 ms: 1.44x slower                                          |
| Geometric mean                   | (ref)                                                      | 1.01x slower                                                   |

Benchmark hidden because not significant (12): async_tree_none_tg, async_tree_eager_memoization, unpickle, regex_dna, pprint_pformat, xml_etree_parse, async_tree_memoization, asyncio_tcp_ssl, async_tree_cpu_io_mixed_tg, async_tree_memoization_tg, async_tree_io, tornado_http
Ignored benchmarks (6) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2
Ignored benchmarks (2) of results/bm-20241017-3.14.0a0-c2fad93-JIT/bm-20241017-darwin-arm64-nick%2darm-codecache-3.14.0a0-c2fad93.json: sphinx, unpack_sequence

# HPT report

- Reliability score: 99.01% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.17x
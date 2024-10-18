# Results vs. 3.13.0b2

- fork: nick-arm
- ref: codecache
- machine: linux-aarch64
- commit hash: c2fad93
- commit date: 2024-10-17
- overall geometric mean: 1.16x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x slower
- Memory change: 1.22x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241017-arminc-aarch64-nick%2darm-codecache-3.14.0a0-c2fad93 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| 2to3           | 305 ms                                                       | 375 ms: 1.23x slower                                             |
| docutils       | 3.10 sec                                                     | 3.67 sec: 1.18x slower                                           |
| html5lib       | 66.1 ms                                                      | 71.1 ms: 1.08x slower                                            |
| tornado_http   | 128 ms                                                       | 146 ms: 1.14x slower                                             |
| Geometric mean | (ref)                                                        | 1.16x slower                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241017-arminc-aarch64-nick%2darm-codecache-3.14.0a0-c2fad93 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| async_tree_none_tg         | 476 ms                                                       | 422 ms: 1.13x faster                                             |
| async_tree_memoization_tg  | 604 ms                                                       | 544 ms: 1.11x faster                                             |
| async_tree_memoization     | 645 ms                                                       | 582 ms: 1.11x faster                                             |
| async_tree_none            | 492 ms                                                       | 455 ms: 1.08x faster                                             |
| async_tree_io_tg           | 1.27 sec                                                     | 1.19 sec: 1.07x faster                                           |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 718 ms: 1.06x faster                                             |
| async_tree_cpu_io_mixed    | 791 ms                                                       | 757 ms: 1.05x faster                                             |
| Geometric mean             | (ref)                                                        | 1.08x faster                                                     |

Benchmark hidden because not significant (1): async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241017-arminc-aarch64-nick%2darm-codecache-3.14.0a0-c2fad93 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| nbody          | 114 ms                                                       | 110 ms: 1.04x faster                                             |
| float          | 91.4 ms                                                      | 93.8 ms: 1.03x slower                                            |
| Geometric mean | (ref)                                                        | 1.00x faster                                                     |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241017-arminc-aarch64-nick%2darm-codecache-3.14.0a0-c2fad93 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| regex_dna      | 259 ms                                                       | 247 ms: 1.05x faster                                             |
| regex_effbot   | 4.98 ms                                                      | 4.90 ms: 1.02x faster                                            |
| regex_v8       | 31.1 ms                                                      | 31.5 ms: 1.01x slower                                            |
| regex_compile  | 128 ms                                                       | 176 ms: 1.38x slower                                             |
| Geometric mean | (ref)                                                        | 1.07x slower                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241017-arminc-aarch64-nick%2darm-codecache-3.14.0a0-c2fad93 |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| json_loads           | 32.1 us                                                      | 31.2 us: 1.03x faster                                            |
| unpickle             | 19.8 us                                                      | 19.2 us: 1.03x faster                                            |
| xml_etree_generate   | 114 ms                                                       | 112 ms: 1.01x faster                                             |
| pickle_list          | 5.27 us                                                      | 5.21 us: 1.01x faster                                            |
| unpickle_list        | 6.52 us                                                      | 6.60 us: 1.01x slower                                            |
| pickle_dict          | 37.6 us                                                      | 38.2 us: 1.01x slower                                            |
| json_dumps           | 13.1 ms                                                      | 13.4 ms: 1.02x slower                                            |
| xml_etree_iterparse  | 147 ms                                                       | 151 ms: 1.03x slower                                             |
| tomli_loads          | 2.57 sec                                                     | 2.64 sec: 1.03x slower                                           |
| pickle               | 13.4 us                                                      | 13.8 us: 1.03x slower                                            |
| unpickle_pure_python | 251 us                                                       | 267 us: 1.06x slower                                             |
| pickle_pure_python   | 359 us                                                       | 388 us: 1.08x slower                                             |
| Geometric mean       | (ref)                                                        | 1.01x slower                                                     |

Benchmark hidden because not significant (2): xml_etree_parse, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241017-arminc-aarch64-nick%2darm-codecache-3.14.0a0-c2fad93 |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| python_startup_no_site | 8.60 ms                                                      | 8.76 ms: 1.02x slower                                            |
| python_startup         | 13.0 ms                                                      | 14.7 ms: 1.13x slower                                            |
| Geometric mean         | (ref)                                                        | 1.08x slower                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241017-arminc-aarch64-nick%2darm-codecache-3.14.0a0-c2fad93 |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| mako            | 13.2 ms                                                      | 12.9 ms: 1.02x faster                                            |
| django_template | 42.3 ms                                                      | 52.3 ms: 1.24x slower                                            |
| genshi_text     | 27.4 ms                                                      | 35.0 ms: 1.28x slower                                            |
| genshi_xml      | 60.4 ms                                                      | 85.1 ms: 1.41x slower                                            |
| Geometric mean  | (ref)                                                        | 1.22x slower                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241017-arminc-aarch64-nick%2darm-codecache-3.14.0a0-c2fad93 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| deepcopy_memo              | 50.8 us                                                      | 37.7 us: 1.35x faster                                            |
| async_tree_none_tg         | 476 ms                                                       | 422 ms: 1.13x faster                                             |
| deepcopy                   | 448 us                                                       | 397 us: 1.13x faster                                             |
| async_tree_memoization_tg  | 604 ms                                                       | 544 ms: 1.11x faster                                             |
| async_tree_memoization     | 645 ms                                                       | 582 ms: 1.11x faster                                             |
| async_tree_none            | 492 ms                                                       | 455 ms: 1.08x faster                                             |
| async_tree_io_tg           | 1.27 sec                                                     | 1.19 sec: 1.07x faster                                           |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 718 ms: 1.06x faster                                             |
| deepcopy_reduce            | 4.04 us                                                      | 3.83 us: 1.06x faster                                            |
| pathlib                    | 22.8 ms                                                      | 21.6 ms: 1.05x faster                                            |
| telco                      | 10.0 ms                                                      | 9.53 ms: 1.05x faster                                            |
| regex_dna                  | 259 ms                                                       | 247 ms: 1.05x faster                                             |
| scimark_sor                | 159 ms                                                       | 152 ms: 1.05x faster                                             |
| async_tree_cpu_io_mixed    | 791 ms                                                       | 757 ms: 1.05x faster                                             |
| nbody                      | 114 ms                                                       | 110 ms: 1.04x faster                                             |
| json_loads                 | 32.1 us                                                      | 31.2 us: 1.03x faster                                            |
| unpickle                   | 19.8 us                                                      | 19.2 us: 1.03x faster                                            |
| json                       | 5.64 ms                                                      | 5.53 ms: 1.02x faster                                            |
| coroutines                 | 29.0 ms                                                      | 28.5 ms: 1.02x faster                                            |
| sqlite_synth               | 3.90 us                                                      | 3.83 us: 1.02x faster                                            |
| regex_effbot               | 4.98 ms                                                      | 4.90 ms: 1.02x faster                                            |
| mako                       | 13.2 ms                                                      | 12.9 ms: 1.02x faster                                            |
| xml_etree_generate         | 114 ms                                                       | 112 ms: 1.01x faster                                             |
| pickle_list                | 5.27 us                                                      | 5.21 us: 1.01x faster                                            |
| asyncio_websockets         | 657 ms                                                       | 663 ms: 1.01x slower                                             |
| unpickle_list              | 6.52 us                                                      | 6.60 us: 1.01x slower                                            |
| pickle_dict                | 37.6 us                                                      | 38.2 us: 1.01x slower                                            |
| logging_silent             | 133 ns                                                       | 135 ns: 1.01x slower                                             |
| regex_v8                   | 31.1 ms                                                      | 31.5 ms: 1.01x slower                                            |
| python_startup_no_site     | 8.60 ms                                                      | 8.76 ms: 1.02x slower                                            |
| json_dumps                 | 13.1 ms                                                      | 13.4 ms: 1.02x slower                                            |
| float                      | 91.4 ms                                                      | 93.8 ms: 1.03x slower                                            |
| xml_etree_iterparse        | 147 ms                                                       | 151 ms: 1.03x slower                                             |
| tomli_loads                | 2.57 sec                                                     | 2.64 sec: 1.03x slower                                           |
| asyncio_tcp_ssl            | 2.21 sec                                                     | 2.28 sec: 1.03x slower                                           |
| pickle                     | 13.4 us                                                      | 13.8 us: 1.03x slower                                            |
| scimark_sparse_mat_mult    | 6.55 ms                                                      | 6.80 ms: 1.04x slower                                            |
| async_generators           | 488 ms                                                       | 510 ms: 1.05x slower                                             |
| coverage                   | 98.4 ms                                                      | 103 ms: 1.05x slower                                             |
| mdp                        | 3.33 sec                                                     | 3.49 sec: 1.05x slower                                           |
| logging_format             | 7.82 us                                                      | 8.22 us: 1.05x slower                                            |
| bpe_tokeniser              | 5.83 sec                                                     | 6.13 sec: 1.05x slower                                           |
| scimark_lu                 | 141 ms                                                       | 149 ms: 1.05x slower                                             |
| logging_simple             | 7.21 us                                                      | 7.62 us: 1.06x slower                                            |
| unpickle_pure_python       | 251 us                                                       | 267 us: 1.06x slower                                             |
| asyncio_tcp                | 584 ms                                                       | 623 ms: 1.07x slower                                             |
| typing_runtime_protocols   | 193 us                                                       | 207 us: 1.07x slower                                             |
| spectral_norm              | 141 ms                                                       | 152 ms: 1.07x slower                                             |
| html5lib                   | 66.1 ms                                                      | 71.1 ms: 1.08x slower                                            |
| crypto_pyaes               | 82.0 ms                                                      | 88.5 ms: 1.08x slower                                            |
| pickle_pure_python         | 359 us                                                       | 388 us: 1.08x slower                                             |
| meteor_contest             | 113 ms                                                       | 125 ms: 1.10x slower                                             |
| scimark_monte_carlo        | 82.3 ms                                                      | 90.9 ms: 1.10x slower                                            |
| pyflate                    | 557 ms                                                       | 621 ms: 1.12x slower                                             |
| bench_thread_pool          | 1.26 ms                                                      | 1.40 ms: 1.12x slower                                            |
| python_startup             | 13.0 ms                                                      | 14.7 ms: 1.13x slower                                            |
| tornado_http               | 128 ms                                                       | 146 ms: 1.14x slower                                             |
| fannkuch                   | 451 ms                                                       | 519 ms: 1.15x slower                                             |
| deltablue                  | 3.88 ms                                                      | 4.47 ms: 1.15x slower                                            |
| raytrace                   | 297 ms                                                       | 347 ms: 1.17x slower                                             |
| go                         | 161 ms                                                       | 189 ms: 1.17x slower                                             |
| docutils                   | 3.10 sec                                                     | 3.67 sec: 1.18x slower                                           |
| sqlglot_parse              | 1.42 ms                                                      | 1.69 ms: 1.18x slower                                            |
| gc_traversal               | 5.17 ms                                                      | 6.17 ms: 1.19x slower                                            |
| sqlglot_normalize          | 129 ms                                                       | 154 ms: 1.19x slower                                             |
| pycparser                  | 1.22 sec                                                     | 1.48 sec: 1.21x slower                                           |
| comprehensions             | 20.5 us                                                      | 24.9 us: 1.22x slower                                            |
| nqueens                    | 98.9 ms                                                      | 121 ms: 1.22x slower                                             |
| richards_super             | 62.3 ms                                                      | 76.3 ms: 1.23x slower                                            |
| 2to3                       | 305 ms                                                       | 375 ms: 1.23x slower                                             |
| richards                   | 55.9 ms                                                      | 68.8 ms: 1.23x slower                                            |
| django_template            | 42.3 ms                                                      | 52.3 ms: 1.24x slower                                            |
| chaos                      | 68.3 ms                                                      | 86.0 ms: 1.26x slower                                            |
| sqlglot_optimize           | 62.6 ms                                                      | 79.2 ms: 1.27x slower                                            |
| genshi_text                | 27.4 ms                                                      | 35.0 ms: 1.28x slower                                            |
| sqlglot_transpile          | 1.71 ms                                                      | 2.20 ms: 1.28x slower                                            |
| sympy_expand               | 457 ms                                                       | 593 ms: 1.30x slower                                             |
| pprint_safe_repr           | 933 ms                                                       | 1.22 sec: 1.31x slower                                           |
| dulwich_log                | 58.5 ms                                                      | 77.3 ms: 1.32x slower                                            |
| sympy_str                  | 265 ms                                                       | 355 ms: 1.34x slower                                             |
| pprint_pformat             | 1.93 sec                                                     | 2.60 sec: 1.35x slower                                           |
| regex_compile              | 128 ms                                                       | 176 ms: 1.38x slower                                             |
| sympy_integrate            | 20.9 ms                                                      | 28.9 ms: 1.39x slower                                            |
| genshi_xml                 | 60.4 ms                                                      | 85.1 ms: 1.41x slower                                            |
| pylint                     | 337 ms                                                       | 483 ms: 1.43x slower                                             |
| sympy_sum                  | 144 ms                                                       | 210 ms: 1.46x slower                                             |
| hexiom                     | 7.08 ms                                                      | 10.4 ms: 1.46x slower                                            |
| create_gc_cycles           | 2.33 ms                                                      | 3.58 ms: 1.53x slower                                            |
| generators                 | 37.1 ms                                                      | 59.3 ms: 1.60x slower                                            |
| bench_mp_pool              | 7.03 ms                                                      | 3.29 sec: 467.50x slower                                         |
| Geometric mean             | (ref)                                                        | 1.16x slower                                                     |

Benchmark hidden because not significant (6): async_tree_io, xml_etree_parse, scimark_fft, thrift, xml_etree_process, pidigits
Ignored benchmarks (6) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2
Ignored benchmarks (2) of results/bm-20241017-3.14.0a0-c2fad93-JIT/bm-20241017-arminc-aarch64-nick%2darm-codecache-3.14.0a0-c2fad93.json: sphinx, unpack_sequence

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.05x
- 95% likely to have a slowdown of 1.04x
- 99% likely to have a slowdown of 1.03x

# Memory
- memory change: 1.22x
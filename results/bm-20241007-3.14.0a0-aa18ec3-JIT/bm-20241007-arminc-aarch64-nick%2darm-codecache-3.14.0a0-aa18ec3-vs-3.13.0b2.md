# Results vs. 3.13.0b2

- fork: nick-arm
- ref: codecache
- machine: linux-aarch64
- commit hash: aa18ec3
- commit date: 2024-10-07
- overall geometric mean: 1.14x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x slower
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241007-arminc-aarch64-nick%2darm-codecache-3.14.0a0-aa18ec3 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| 2to3           | 305 ms                                                       | 374 ms: 1.23x slower                                             |
| docutils       | 3.10 sec                                                     | 3.63 sec: 1.17x slower                                           |
| html5lib       | 66.1 ms                                                      | 71.3 ms: 1.08x slower                                            |
| tornado_http   | 128 ms                                                       | 142 ms: 1.11x slower                                             |
| Geometric mean | (ref)                                                        | 1.15x slower                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241007-arminc-aarch64-nick%2darm-codecache-3.14.0a0-aa18ec3 |
|---------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| async_tree_none_tg        | 476 ms                                                       | 426 ms: 1.12x faster                                             |
| async_tree_none           | 492 ms                                                       | 448 ms: 1.10x faster                                             |
| async_tree_memoization    | 645 ms                                                       | 591 ms: 1.09x faster                                             |
| async_tree_io_tg          | 1.27 sec                                                     | 1.18 sec: 1.08x faster                                           |
| async_tree_memoization_tg | 604 ms                                                       | 561 ms: 1.08x faster                                             |
| async_tree_io             | 1.22 sec                                                     | 1.15 sec: 1.07x faster                                           |
| async_tree_cpu_io_mixed   | 791 ms                                                       | 752 ms: 1.05x faster                                             |
| Geometric mean            | (ref)                                                        | 1.08x faster                                                     |

Benchmark hidden because not significant (1): async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241007-arminc-aarch64-nick%2darm-codecache-3.14.0a0-aa18ec3 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| float          | 91.4 ms                                                      | 90.0 ms: 1.02x faster                                            |
| Geometric mean | (ref)                                                        | 1.01x faster                                                     |

Benchmark hidden because not significant (2): nbody, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241007-arminc-aarch64-nick%2darm-codecache-3.14.0a0-aa18ec3 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| regex_dna      | 259 ms                                                       | 247 ms: 1.05x faster                                             |
| regex_effbot   | 4.98 ms                                                      | 4.90 ms: 1.02x faster                                            |
| regex_v8       | 31.1 ms                                                      | 31.4 ms: 1.01x slower                                            |
| regex_compile  | 128 ms                                                       | 181 ms: 1.41x slower                                             |
| Geometric mean | (ref)                                                        | 1.08x slower                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241007-arminc-aarch64-nick%2darm-codecache-3.14.0a0-aa18ec3 |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| json_loads           | 32.1 us                                                      | 31.0 us: 1.03x faster                                            |
| unpickle             | 19.8 us                                                      | 19.2 us: 1.03x faster                                            |
| xml_etree_generate   | 114 ms                                                       | 110 ms: 1.03x faster                                             |
| unpickle_list        | 6.52 us                                                      | 6.40 us: 1.02x faster                                            |
| pickle_list          | 5.27 us                                                      | 5.21 us: 1.01x faster                                            |
| json_dumps           | 13.1 ms                                                      | 13.2 ms: 1.01x slower                                            |
| pickle_dict          | 37.6 us                                                      | 38.1 us: 1.01x slower                                            |
| tomli_loads          | 2.57 sec                                                     | 2.61 sec: 1.02x slower                                           |
| pickle               | 13.4 us                                                      | 13.6 us: 1.02x slower                                            |
| xml_etree_iterparse  | 147 ms                                                       | 152 ms: 1.03x slower                                             |
| unpickle_pure_python | 251 us                                                       | 267 us: 1.06x slower                                             |
| pickle_pure_python   | 359 us                                                       | 384 us: 1.07x slower                                             |
| Geometric mean       | (ref)                                                        | 1.01x slower                                                     |

Benchmark hidden because not significant (2): xml_etree_process, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241007-arminc-aarch64-nick%2darm-codecache-3.14.0a0-aa18ec3 |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| python_startup         | 13.0 ms                                                      | 13.1 ms: 1.01x slower                                            |
| python_startup_no_site | 8.60 ms                                                      | 8.81 ms: 1.02x slower                                            |
| Geometric mean         | (ref)                                                        | 1.02x slower                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241007-arminc-aarch64-nick%2darm-codecache-3.14.0a0-aa18ec3 |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| django_template | 42.3 ms                                                      | 51.9 ms: 1.23x slower                                            |
| genshi_text     | 27.4 ms                                                      | 34.8 ms: 1.27x slower                                            |
| genshi_xml      | 60.4 ms                                                      | 83.0 ms: 1.38x slower                                            |
| Geometric mean  | (ref)                                                        | 1.21x slower                                                     |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                 | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241007-arminc-aarch64-nick%2darm-codecache-3.14.0a0-aa18ec3 |
|---------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| deepcopy_memo             | 50.8 us                                                      | 37.4 us: 1.36x faster                                            |
| async_tree_none_tg        | 476 ms                                                       | 426 ms: 1.12x faster                                             |
| deepcopy                  | 448 us                                                       | 405 us: 1.11x faster                                             |
| async_tree_none           | 492 ms                                                       | 448 ms: 1.10x faster                                             |
| async_tree_memoization    | 645 ms                                                       | 591 ms: 1.09x faster                                             |
| async_tree_io_tg          | 1.27 sec                                                     | 1.18 sec: 1.08x faster                                           |
| async_tree_memoization_tg | 604 ms                                                       | 561 ms: 1.08x faster                                             |
| async_tree_io             | 1.22 sec                                                     | 1.15 sec: 1.07x faster                                           |
| pathlib                   | 22.8 ms                                                      | 21.5 ms: 1.06x faster                                            |
| async_tree_cpu_io_mixed   | 791 ms                                                       | 752 ms: 1.05x faster                                             |
| deepcopy_reduce           | 4.04 us                                                      | 3.85 us: 1.05x faster                                            |
| regex_dna                 | 259 ms                                                       | 247 ms: 1.05x faster                                             |
| json_loads                | 32.1 us                                                      | 31.0 us: 1.03x faster                                            |
| unpickle                  | 19.8 us                                                      | 19.2 us: 1.03x faster                                            |
| xml_etree_generate        | 114 ms                                                       | 110 ms: 1.03x faster                                             |
| sqlite_synth              | 3.90 us                                                      | 3.81 us: 1.03x faster                                            |
| unpickle_list             | 6.52 us                                                      | 6.40 us: 1.02x faster                                            |
| regex_effbot              | 4.98 ms                                                      | 4.90 ms: 1.02x faster                                            |
| float                     | 91.4 ms                                                      | 90.0 ms: 1.02x faster                                            |
| telco                     | 10.0 ms                                                      | 9.86 ms: 1.02x faster                                            |
| pickle_list               | 5.27 us                                                      | 5.21 us: 1.01x faster                                            |
| python_startup            | 13.0 ms                                                      | 13.1 ms: 1.01x slower                                            |
| json_dumps                | 13.1 ms                                                      | 13.2 ms: 1.01x slower                                            |
| asyncio_websockets        | 657 ms                                                       | 663 ms: 1.01x slower                                             |
| regex_v8                  | 31.1 ms                                                      | 31.4 ms: 1.01x slower                                            |
| pickle_dict               | 37.6 us                                                      | 38.1 us: 1.01x slower                                            |
| tomli_loads               | 2.57 sec                                                     | 2.61 sec: 1.02x slower                                           |
| pickle                    | 13.4 us                                                      | 13.6 us: 1.02x slower                                            |
| python_startup_no_site    | 8.60 ms                                                      | 8.81 ms: 1.02x slower                                            |
| logging_format            | 7.82 us                                                      | 8.02 us: 1.03x slower                                            |
| logging_simple            | 7.21 us                                                      | 7.40 us: 1.03x slower                                            |
| bpe_tokeniser             | 5.83 sec                                                     | 5.99 sec: 1.03x slower                                           |
| spectral_norm             | 141 ms                                                       | 145 ms: 1.03x slower                                             |
| asyncio_tcp_ssl           | 2.21 sec                                                     | 2.29 sec: 1.03x slower                                           |
| xml_etree_iterparse       | 147 ms                                                       | 152 ms: 1.03x slower                                             |
| scimark_sparse_mat_mult   | 6.55 ms                                                      | 6.79 ms: 1.04x slower                                            |
| async_generators          | 488 ms                                                       | 507 ms: 1.04x slower                                             |
| scimark_sor               | 159 ms                                                       | 167 ms: 1.05x slower                                             |
| mdp                       | 3.33 sec                                                     | 3.50 sec: 1.05x slower                                           |
| unpickle_pure_python      | 251 us                                                       | 267 us: 1.06x slower                                             |
| scimark_lu                | 141 ms                                                       | 150 ms: 1.06x slower                                             |
| scimark_monte_carlo       | 82.3 ms                                                      | 87.5 ms: 1.06x slower                                            |
| asyncio_tcp               | 584 ms                                                       | 622 ms: 1.06x slower                                             |
| pickle_pure_python        | 359 us                                                       | 384 us: 1.07x slower                                             |
| crypto_pyaes              | 82.0 ms                                                      | 88.1 ms: 1.08x slower                                            |
| html5lib                  | 66.1 ms                                                      | 71.3 ms: 1.08x slower                                            |
| richards                  | 55.9 ms                                                      | 60.3 ms: 1.08x slower                                            |
| bench_thread_pool         | 1.26 ms                                                      | 1.37 ms: 1.09x slower                                            |
| typing_runtime_protocols  | 193 us                                                       | 211 us: 1.09x slower                                             |
| meteor_contest            | 113 ms                                                       | 125 ms: 1.10x slower                                             |
| tornado_http              | 128 ms                                                       | 142 ms: 1.11x slower                                             |
| pyflate                   | 557 ms                                                       | 617 ms: 1.11x slower                                             |
| fannkuch                  | 451 ms                                                       | 503 ms: 1.12x slower                                             |
| deltablue                 | 3.88 ms                                                      | 4.38 ms: 1.13x slower                                            |
| richards_super            | 62.3 ms                                                      | 70.7 ms: 1.14x slower                                            |
| raytrace                  | 297 ms                                                       | 347 ms: 1.17x slower                                             |
| docutils                  | 3.10 sec                                                     | 3.63 sec: 1.17x slower                                           |
| go                        | 161 ms                                                       | 189 ms: 1.17x slower                                             |
| sqlglot_parse             | 1.42 ms                                                      | 1.68 ms: 1.18x slower                                            |
| comprehensions            | 20.5 us                                                      | 24.5 us: 1.19x slower                                            |
| sqlglot_normalize         | 129 ms                                                       | 155 ms: 1.20x slower                                             |
| pycparser                 | 1.22 sec                                                     | 1.47 sec: 1.20x slower                                           |
| django_template           | 42.3 ms                                                      | 51.9 ms: 1.23x slower                                            |
| 2to3                      | 305 ms                                                       | 374 ms: 1.23x slower                                             |
| nqueens                   | 98.9 ms                                                      | 122 ms: 1.23x slower                                             |
| genshi_text               | 27.4 ms                                                      | 34.8 ms: 1.27x slower                                            |
| sqlglot_optimize          | 62.6 ms                                                      | 80.2 ms: 1.28x slower                                            |
| pprint_safe_repr          | 933 ms                                                       | 1.20 sec: 1.29x slower                                           |
| sympy_expand              | 457 ms                                                       | 591 ms: 1.29x slower                                             |
| chaos                     | 68.3 ms                                                      | 88.3 ms: 1.29x slower                                            |
| pprint_pformat            | 1.93 sec                                                     | 2.50 sec: 1.29x slower                                           |
| dulwich_log               | 58.5 ms                                                      | 76.0 ms: 1.30x slower                                            |
| sqlglot_transpile         | 1.71 ms                                                      | 2.22 ms: 1.30x slower                                            |
| sympy_str                 | 265 ms                                                       | 358 ms: 1.35x slower                                             |
| genshi_xml                | 60.4 ms                                                      | 83.0 ms: 1.38x slower                                            |
| sympy_integrate           | 20.9 ms                                                      | 28.8 ms: 1.38x slower                                            |
| pylint                    | 337 ms                                                       | 472 ms: 1.40x slower                                             |
| regex_compile             | 128 ms                                                       | 181 ms: 1.41x slower                                             |
| hexiom                    | 7.08 ms                                                      | 10.1 ms: 1.43x slower                                            |
| sympy_sum                 | 144 ms                                                       | 214 ms: 1.49x slower                                             |
| generators                | 37.1 ms                                                      | 59.3 ms: 1.60x slower                                            |
| bench_mp_pool             | 7.03 ms                                                      | 1.89 sec: 269.41x slower                                         |
| Geometric mean            | (ref)                                                        | 1.14x slower                                                     |

Benchmark hidden because not significant (14): async_tree_cpu_io_mixed_tg, json, coroutines, xml_etree_process, nbody, create_gc_cycles, logging_silent, scimark_fft, thrift, mako, pidigits, xml_etree_parse, gc_traversal, coverage
Ignored benchmarks (6) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2
Ignored benchmarks (1) of results/bm-20241007-3.14.0a0-aa18ec3-JIT/bm-20241007-arminc-aarch64-nick%2darm-codecache-3.14.0a0-aa18ec3.json: unpack_sequence

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.03x
- 95% likely to have a slowdown of 1.03x
- 99% likely to have a slowdown of 1.02x

# Memory
- memory change: 1.09x
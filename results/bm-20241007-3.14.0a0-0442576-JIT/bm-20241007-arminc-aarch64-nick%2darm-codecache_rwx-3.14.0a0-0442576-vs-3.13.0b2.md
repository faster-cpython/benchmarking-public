# Results vs. 3.13.0b2

- fork: nick-arm
- ref: codecache_rwx
- machine: linux-aarch64
- commit hash: 0442576
- commit date: 2024-10-07
- overall geometric mean: 1.14x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x slower
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241007-arminc-aarch64-nick%2darm-codecache_rwx-3.14.0a0-0442576 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 305 ms                                                       | 365 ms: 1.20x slower                                                 |
| docutils       | 3.10 sec                                                     | 3.56 sec: 1.15x slower                                               |
| html5lib       | 66.1 ms                                                      | 70.6 ms: 1.07x slower                                                |
| tornado_http   | 128 ms                                                       | 149 ms: 1.16x slower                                                 |
| Geometric mean | (ref)                                                        | 1.14x slower                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241007-arminc-aarch64-nick%2darm-codecache_rwx-3.14.0a0-0442576 |
|----------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_none_tg         | 476 ms                                                       | 427 ms: 1.11x faster                                                 |
| async_tree_none            | 492 ms                                                       | 442 ms: 1.11x faster                                                 |
| async_tree_memoization     | 645 ms                                                       | 585 ms: 1.10x faster                                                 |
| async_tree_io_tg           | 1.27 sec                                                     | 1.17 sec: 1.09x faster                                               |
| async_tree_memoization_tg  | 604 ms                                                       | 561 ms: 1.08x faster                                                 |
| async_tree_io              | 1.22 sec                                                     | 1.15 sec: 1.07x faster                                               |
| async_tree_cpu_io_mixed    | 791 ms                                                       | 754 ms: 1.05x faster                                                 |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 732 ms: 1.04x faster                                                 |
| Geometric mean             | (ref)                                                        | 1.08x faster                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241007-arminc-aarch64-nick%2darm-codecache_rwx-3.14.0a0-0442576 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------:|
| nbody          | 114 ms                                                       | 111 ms: 1.03x faster                                                 |
| float          | 91.4 ms                                                      | 90.2 ms: 1.01x faster                                                |
| Geometric mean | (ref)                                                        | 1.01x faster                                                         |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241007-arminc-aarch64-nick%2darm-codecache_rwx-3.14.0a0-0442576 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_dna      | 259 ms                                                       | 263 ms: 1.02x slower                                                 |
| regex_compile  | 128 ms                                                       | 174 ms: 1.36x slower                                                 |
| Geometric mean | (ref)                                                        | 1.09x slower                                                         |

Benchmark hidden because not significant (2): regex_effbot, regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241007-arminc-aarch64-nick%2darm-codecache_rwx-3.14.0a0-0442576 |
|----------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------:|
| xml_etree_generate   | 114 ms                                                       | 109 ms: 1.04x faster                                                 |
| json_loads           | 32.1 us                                                      | 31.1 us: 1.03x faster                                                |
| unpickle             | 19.8 us                                                      | 19.1 us: 1.03x faster                                                |
| unpickle_list        | 6.52 us                                                      | 6.37 us: 1.02x faster                                                |
| xml_etree_process    | 80.8 ms                                                      | 79.4 ms: 1.02x faster                                                |
| pickle_list          | 5.27 us                                                      | 5.19 us: 1.02x faster                                                |
| tomli_loads          | 2.57 sec                                                     | 2.64 sec: 1.03x slower                                               |
| pickle               | 13.4 us                                                      | 13.8 us: 1.03x slower                                                |
| xml_etree_iterparse  | 147 ms                                                       | 151 ms: 1.03x slower                                                 |
| unpickle_pure_python | 251 us                                                       | 265 us: 1.06x slower                                                 |
| pickle_pure_python   | 359 us                                                       | 395 us: 1.10x slower                                                 |
| Geometric mean       | (ref)                                                        | 1.01x slower                                                         |

Benchmark hidden because not significant (3): xml_etree_parse, json_dumps, pickle_dict

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241007-arminc-aarch64-nick%2darm-codecache_rwx-3.14.0a0-0442576 |
|------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup         | 13.0 ms                                                      | 13.1 ms: 1.01x slower                                                |
| python_startup_no_site | 8.60 ms                                                      | 8.75 ms: 1.02x slower                                                |
| Geometric mean         | (ref)                                                        | 1.02x slower                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241007-arminc-aarch64-nick%2darm-codecache_rwx-3.14.0a0-0442576 |
|-----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------:|
| genshi_text     | 27.4 ms                                                      | 33.1 ms: 1.21x slower                                                |
| django_template | 42.3 ms                                                      | 51.2 ms: 1.21x slower                                                |
| genshi_xml      | 60.4 ms                                                      | 78.1 ms: 1.29x slower                                                |
| Geometric mean  | (ref)                                                        | 1.17x slower                                                         |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241007-arminc-aarch64-nick%2darm-codecache_rwx-3.14.0a0-0442576 |
|----------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------:|
| deepcopy_memo              | 50.8 us                                                      | 37.4 us: 1.36x faster                                                |
| async_tree_none_tg         | 476 ms                                                       | 427 ms: 1.11x faster                                                 |
| deepcopy                   | 448 us                                                       | 402 us: 1.11x faster                                                 |
| async_tree_none            | 492 ms                                                       | 442 ms: 1.11x faster                                                 |
| async_tree_memoization     | 645 ms                                                       | 585 ms: 1.10x faster                                                 |
| async_tree_io_tg           | 1.27 sec                                                     | 1.17 sec: 1.09x faster                                               |
| async_tree_memoization_tg  | 604 ms                                                       | 561 ms: 1.08x faster                                                 |
| telco                      | 10.0 ms                                                      | 9.37 ms: 1.07x faster                                                |
| async_tree_io              | 1.22 sec                                                     | 1.15 sec: 1.07x faster                                               |
| scimark_sor                | 159 ms                                                       | 151 ms: 1.06x faster                                                 |
| async_tree_cpu_io_mixed    | 791 ms                                                       | 754 ms: 1.05x faster                                                 |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 732 ms: 1.04x faster                                                 |
| pathlib                    | 22.8 ms                                                      | 21.9 ms: 1.04x faster                                                |
| xml_etree_generate         | 114 ms                                                       | 109 ms: 1.04x faster                                                 |
| json_loads                 | 32.1 us                                                      | 31.1 us: 1.03x faster                                                |
| unpickle                   | 19.8 us                                                      | 19.1 us: 1.03x faster                                                |
| nbody                      | 114 ms                                                       | 111 ms: 1.03x faster                                                 |
| deepcopy_reduce            | 4.04 us                                                      | 3.94 us: 1.03x faster                                                |
| unpickle_list              | 6.52 us                                                      | 6.37 us: 1.02x faster                                                |
| create_gc_cycles           | 2.33 ms                                                      | 2.28 ms: 1.02x faster                                                |
| json                       | 5.64 ms                                                      | 5.54 ms: 1.02x faster                                                |
| xml_etree_process          | 80.8 ms                                                      | 79.4 ms: 1.02x faster                                                |
| pickle_list                | 5.27 us                                                      | 5.19 us: 1.02x faster                                                |
| coroutines                 | 29.0 ms                                                      | 28.6 ms: 1.02x faster                                                |
| float                      | 91.4 ms                                                      | 90.2 ms: 1.01x faster                                                |
| logging_silent             | 133 ns                                                       | 132 ns: 1.01x faster                                                 |
| asyncio_websockets         | 657 ms                                                       | 665 ms: 1.01x slower                                                 |
| python_startup             | 13.0 ms                                                      | 13.1 ms: 1.01x slower                                                |
| regex_dna                  | 259 ms                                                       | 263 ms: 1.02x slower                                                 |
| python_startup_no_site     | 8.60 ms                                                      | 8.75 ms: 1.02x slower                                                |
| richards                   | 55.9 ms                                                      | 56.9 ms: 1.02x slower                                                |
| bpe_tokeniser              | 5.83 sec                                                     | 5.96 sec: 1.02x slower                                               |
| tomli_loads                | 2.57 sec                                                     | 2.64 sec: 1.03x slower                                               |
| pickle                     | 13.4 us                                                      | 13.8 us: 1.03x slower                                                |
| xml_etree_iterparse        | 147 ms                                                       | 151 ms: 1.03x slower                                                 |
| asyncio_tcp_ssl            | 2.21 sec                                                     | 2.28 sec: 1.03x slower                                               |
| mdp                        | 3.33 sec                                                     | 3.45 sec: 1.04x slower                                               |
| logging_format             | 7.82 us                                                      | 8.10 us: 1.04x slower                                                |
| logging_simple             | 7.21 us                                                      | 7.49 us: 1.04x slower                                                |
| scimark_sparse_mat_mult    | 6.55 ms                                                      | 6.83 ms: 1.04x slower                                                |
| spectral_norm              | 141 ms                                                       | 147 ms: 1.04x slower                                                 |
| unpickle_pure_python       | 251 us                                                       | 265 us: 1.06x slower                                                 |
| async_generators           | 488 ms                                                       | 517 ms: 1.06x slower                                                 |
| typing_runtime_protocols   | 193 us                                                       | 205 us: 1.06x slower                                                 |
| asyncio_tcp                | 584 ms                                                       | 622 ms: 1.06x slower                                                 |
| html5lib                   | 66.1 ms                                                      | 70.6 ms: 1.07x slower                                                |
| scimark_lu                 | 141 ms                                                       | 151 ms: 1.07x slower                                                 |
| scimark_monte_carlo        | 82.3 ms                                                      | 88.2 ms: 1.07x slower                                                |
| richards_super             | 62.3 ms                                                      | 67.3 ms: 1.08x slower                                                |
| crypto_pyaes               | 82.0 ms                                                      | 88.6 ms: 1.08x slower                                                |
| meteor_contest             | 113 ms                                                       | 123 ms: 1.08x slower                                                 |
| bench_thread_pool          | 1.26 ms                                                      | 1.37 ms: 1.09x slower                                                |
| pickle_pure_python         | 359 us                                                       | 395 us: 1.10x slower                                                 |
| pyflate                    | 557 ms                                                       | 620 ms: 1.11x slower                                                 |
| fannkuch                   | 451 ms                                                       | 504 ms: 1.12x slower                                                 |
| deltablue                  | 3.88 ms                                                      | 4.34 ms: 1.12x slower                                                |
| go                         | 161 ms                                                       | 182 ms: 1.13x slower                                                 |
| docutils                   | 3.10 sec                                                     | 3.56 sec: 1.15x slower                                               |
| sqlglot_normalize          | 129 ms                                                       | 149 ms: 1.15x slower                                                 |
| tornado_http               | 128 ms                                                       | 149 ms: 1.16x slower                                                 |
| raytrace                   | 297 ms                                                       | 345 ms: 1.16x slower                                                 |
| sqlglot_parse              | 1.42 ms                                                      | 1.68 ms: 1.18x slower                                                |
| comprehensions             | 20.5 us                                                      | 24.6 us: 1.20x slower                                                |
| 2to3                       | 305 ms                                                       | 365 ms: 1.20x slower                                                 |
| pycparser                  | 1.22 sec                                                     | 1.47 sec: 1.21x slower                                               |
| genshi_text                | 27.4 ms                                                      | 33.1 ms: 1.21x slower                                                |
| django_template            | 42.3 ms                                                      | 51.2 ms: 1.21x slower                                                |
| sqlglot_optimize           | 62.6 ms                                                      | 76.1 ms: 1.22x slower                                                |
| nqueens                    | 98.9 ms                                                      | 123 ms: 1.24x slower                                                 |
| sympy_expand               | 457 ms                                                       | 573 ms: 1.25x slower                                                 |
| chaos                      | 68.3 ms                                                      | 86.4 ms: 1.27x slower                                                |
| sqlglot_transpile          | 1.71 ms                                                      | 2.21 ms: 1.29x slower                                                |
| genshi_xml                 | 60.4 ms                                                      | 78.1 ms: 1.29x slower                                                |
| sympy_str                  | 265 ms                                                       | 346 ms: 1.30x slower                                                 |
| pprint_safe_repr           | 933 ms                                                       | 1.22 sec: 1.31x slower                                               |
| pprint_pformat             | 1.93 sec                                                     | 2.54 sec: 1.32x slower                                               |
| regex_compile              | 128 ms                                                       | 174 ms: 1.36x slower                                                 |
| pylint                     | 337 ms                                                       | 459 ms: 1.36x slower                                                 |
| sympy_integrate            | 20.9 ms                                                      | 28.5 ms: 1.37x slower                                                |
| dulwich_log                | 58.5 ms                                                      | 81.3 ms: 1.39x slower                                                |
| hexiom                     | 7.08 ms                                                      | 9.90 ms: 1.40x slower                                                |
| sympy_sum                  | 144 ms                                                       | 210 ms: 1.46x slower                                                 |
| generators                 | 37.1 ms                                                      | 58.8 ms: 1.58x slower                                                |
| bench_mp_pool              | 7.03 ms                                                      | 2.94 sec: 418.72x slower                                             |
| Geometric mean             | (ref)                                                        | 1.14x slower                                                         |

Benchmark hidden because not significant (12): sqlite_synth, xml_etree_parse, thrift, coverage, mako, pidigits, scimark_fft, json_dumps, regex_effbot, pickle_dict, regex_v8, gc_traversal
Ignored benchmarks (6) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2
Ignored benchmarks (1) of results/bm-20241007-3.14.0a0-0442576-JIT/bm-20241007-arminc-aarch64-nick%2darm-codecache_rwx-3.14.0a0-0442576.json: unpack_sequence

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.03x
- 95% likely to have a slowdown of 1.02x
- 99% likely to have a slowdown of 1.02x

# Memory
- memory change: 1.07x
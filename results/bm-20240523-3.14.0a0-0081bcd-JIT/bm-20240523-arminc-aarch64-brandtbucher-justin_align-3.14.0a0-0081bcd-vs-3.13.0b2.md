# Results vs. 3.13.0b2

- fork: brandtbucher
- ref: justin_align
- machine: linux-aarch64
- commit hash: 0081bcd
- commit date: 2024-05-23
- overall geometric mean: 1.07x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x slower
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240523-arminc-aarch64-brandtbucher-justin_align-3.14.0a0-0081bcd |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 305 ms                                                       | 353 ms: 1.16x slower                                                  |
| chameleon      | 8.95 ms                                                      | 9.09 ms: 1.02x slower                                                 |
| docutils       | 3.10 sec                                                     | 3.54 sec: 1.14x slower                                                |
| html5lib       | 66.1 ms                                                      | 70.4 ms: 1.06x slower                                                 |
| tornado_http   | 128 ms                                                       | 138 ms: 1.08x slower                                                  |
| Geometric mean | (ref)                                                        | 1.09x slower                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240523-arminc-aarch64-brandtbucher-justin_align-3.14.0a0-0081bcd |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_io_tg           | 1.27 sec                                                     | 1.22 sec: 1.04x faster                                                |
| async_tree_io              | 1.22 sec                                                     | 1.26 sec: 1.03x slower                                                |
| async_tree_none            | 492 ms                                                       | 509 ms: 1.03x slower                                                  |
| async_tree_memoization_tg  | 604 ms                                                       | 628 ms: 1.04x slower                                                  |
| async_tree_memoization     | 645 ms                                                       | 676 ms: 1.05x slower                                                  |
| async_tree_cpu_io_mixed    | 791 ms                                                       | 831 ms: 1.05x slower                                                  |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 807 ms: 1.06x slower                                                  |
| Geometric mean             | (ref)                                                        | 1.03x slower                                                          |

Benchmark hidden because not significant (1): async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240523-arminc-aarch64-brandtbucher-justin_align-3.14.0a0-0081bcd |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 91.4 ms                                                      | 91.0 ms: 1.00x faster                                                 |
| Geometric mean | (ref)                                                        | 1.01x faster                                                          |

Benchmark hidden because not significant (2): nbody, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240523-arminc-aarch64-brandtbucher-justin_align-3.14.0a0-0081bcd |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_v8       | 31.1 ms                                                      | 30.1 ms: 1.03x faster                                                 |
| regex_dna      | 259 ms                                                       | 251 ms: 1.03x faster                                                  |
| regex_effbot   | 4.98 ms                                                      | 4.90 ms: 1.02x faster                                                 |
| regex_compile  | 128 ms                                                       | 165 ms: 1.29x slower                                                  |
| Geometric mean | (ref)                                                        | 1.04x slower                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240523-arminc-aarch64-brandtbucher-justin_align-3.14.0a0-0081bcd |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------:|
| xml_etree_generate   | 114 ms                                                       | 110 ms: 1.03x faster                                                  |
| unpickle_list        | 6.52 us                                                      | 6.35 us: 1.03x faster                                                 |
| unpickle             | 19.8 us                                                      | 19.5 us: 1.01x faster                                                 |
| pickle_list          | 5.27 us                                                      | 5.24 us: 1.01x faster                                                 |
| tomli_loads          | 2.57 sec                                                     | 2.62 sec: 1.02x slower                                                |
| pickle               | 13.4 us                                                      | 13.6 us: 1.02x slower                                                 |
| xml_etree_iterparse  | 147 ms                                                       | 150 ms: 1.02x slower                                                  |
| unpickle_pure_python | 251 us                                                       | 272 us: 1.08x slower                                                  |
| pickle_pure_python   | 359 us                                                       | 403 us: 1.12x slower                                                  |
| Geometric mean       | (ref)                                                        | 1.01x slower                                                          |

Benchmark hidden because not significant (5): xml_etree_process, pickle_dict, json_dumps, xml_etree_parse, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240523-arminc-aarch64-brandtbucher-justin_align-3.14.0a0-0081bcd |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 13.0 ms                                                      | 14.9 ms: 1.14x slower                                                 |
| python_startup_no_site | 8.60 ms                                                      | 10.9 ms: 1.26x slower                                                 |
| Geometric mean         | (ref)                                                        | 1.20x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240523-arminc-aarch64-brandtbucher-justin_align-3.14.0a0-0081bcd |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 13.2 ms                                                      | 12.6 ms: 1.04x faster                                                 |
| django_template | 42.3 ms                                                      | 49.3 ms: 1.17x slower                                                 |
| genshi_text     | 27.4 ms                                                      | 33.2 ms: 1.21x slower                                                 |
| genshi_xml      | 60.4 ms                                                      | 80.0 ms: 1.33x slower                                                 |
| Geometric mean  | (ref)                                                        | 1.16x slower                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240523-arminc-aarch64-brandtbucher-justin_align-3.14.0a0-0081bcd |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------:|
| richards                   | 55.9 ms                                                      | 52.7 ms: 1.06x faster                                                 |
| pathlib                    | 22.8 ms                                                      | 21.7 ms: 1.05x faster                                                 |
| async_tree_io_tg           | 1.27 sec                                                     | 1.22 sec: 1.04x faster                                                |
| deepcopy_memo              | 50.8 us                                                      | 48.7 us: 1.04x faster                                                 |
| mako                       | 13.2 ms                                                      | 12.6 ms: 1.04x faster                                                 |
| richards_super             | 62.3 ms                                                      | 60.2 ms: 1.03x faster                                                 |
| regex_v8                   | 31.1 ms                                                      | 30.1 ms: 1.03x faster                                                 |
| xml_etree_generate         | 114 ms                                                       | 110 ms: 1.03x faster                                                  |
| fannkuch                   | 451 ms                                                       | 437 ms: 1.03x faster                                                  |
| regex_dna                  | 259 ms                                                       | 251 ms: 1.03x faster                                                  |
| unpickle_list              | 6.52 us                                                      | 6.35 us: 1.03x faster                                                 |
| sqlite_synth               | 3.90 us                                                      | 3.84 us: 1.02x faster                                                 |
| regex_effbot               | 4.98 ms                                                      | 4.90 ms: 1.02x faster                                                 |
| telco                      | 10.0 ms                                                      | 9.90 ms: 1.01x faster                                                 |
| unpickle                   | 19.8 us                                                      | 19.5 us: 1.01x faster                                                 |
| pickle_list                | 5.27 us                                                      | 5.24 us: 1.01x faster                                                 |
| float                      | 91.4 ms                                                      | 91.0 ms: 1.00x faster                                                 |
| scimark_fft                | 445 ms                                                       | 451 ms: 1.01x slower                                                  |
| asyncio_websockets         | 657 ms                                                       | 666 ms: 1.01x slower                                                  |
| spectral_norm              | 141 ms                                                       | 143 ms: 1.02x slower                                                  |
| chameleon                  | 8.95 ms                                                      | 9.09 ms: 1.02x slower                                                 |
| tomli_loads                | 2.57 sec                                                     | 2.62 sec: 1.02x slower                                                |
| gc_traversal               | 5.17 ms                                                      | 5.27 ms: 1.02x slower                                                 |
| pickle                     | 13.4 us                                                      | 13.6 us: 1.02x slower                                                 |
| logging_silent             | 133 ns                                                       | 136 ns: 1.02x slower                                                  |
| xml_etree_iterparse        | 147 ms                                                       | 150 ms: 1.02x slower                                                  |
| meteor_contest             | 113 ms                                                       | 116 ms: 1.03x slower                                                  |
| async_tree_io              | 1.22 sec                                                     | 1.26 sec: 1.03x slower                                                |
| asyncio_tcp_ssl            | 2.21 sec                                                     | 2.29 sec: 1.03x slower                                                |
| async_tree_none            | 492 ms                                                       | 509 ms: 1.03x slower                                                  |
| generators                 | 37.1 ms                                                      | 38.5 ms: 1.04x slower                                                 |
| mdp                        | 3.33 sec                                                     | 3.46 sec: 1.04x slower                                                |
| async_tree_memoization_tg  | 604 ms                                                       | 628 ms: 1.04x slower                                                  |
| async_generators           | 488 ms                                                       | 510 ms: 1.05x slower                                                  |
| scimark_sparse_mat_mult    | 6.55 ms                                                      | 6.87 ms: 1.05x slower                                                 |
| async_tree_memoization     | 645 ms                                                       | 676 ms: 1.05x slower                                                  |
| async_tree_cpu_io_mixed    | 791 ms                                                       | 831 ms: 1.05x slower                                                  |
| bench_thread_pool          | 1.26 ms                                                      | 1.32 ms: 1.05x slower                                                 |
| typing_runtime_protocols   | 193 us                                                       | 204 us: 1.05x slower                                                  |
| crypto_pyaes               | 82.0 ms                                                      | 86.7 ms: 1.06x slower                                                 |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 807 ms: 1.06x slower                                                  |
| dask                       | 370 ms                                                       | 393 ms: 1.06x slower                                                  |
| html5lib                   | 66.1 ms                                                      | 70.4 ms: 1.06x slower                                                 |
| asyncio_tcp                | 584 ms                                                       | 629 ms: 1.08x slower                                                  |
| unpickle_pure_python       | 251 us                                                       | 272 us: 1.08x slower                                                  |
| raytrace                   | 297 ms                                                       | 321 ms: 1.08x slower                                                  |
| tornado_http               | 128 ms                                                       | 138 ms: 1.08x slower                                                  |
| go                         | 161 ms                                                       | 176 ms: 1.09x slower                                                  |
| scimark_monte_carlo        | 82.3 ms                                                      | 90.0 ms: 1.09x slower                                                 |
| deepcopy                   | 448 us                                                       | 492 us: 1.10x slower                                                  |
| pycparser                  | 1.22 sec                                                     | 1.34 sec: 1.10x slower                                                |
| scimark_sor                | 159 ms                                                       | 175 ms: 1.10x slower                                                  |
| sqlglot_optimize           | 62.6 ms                                                      | 68.9 ms: 1.10x slower                                                 |
| pyflate                    | 557 ms                                                       | 613 ms: 1.10x slower                                                  |
| sqlglot_normalize          | 129 ms                                                       | 142 ms: 1.10x slower                                                  |
| sqlglot_parse              | 1.42 ms                                                      | 1.58 ms: 1.11x slower                                                 |
| flaskblogging              | 4.70 ms                                                      | 5.23 ms: 1.11x slower                                                 |
| comprehensions             | 20.5 us                                                      | 23.0 us: 1.12x slower                                                 |
| pickle_pure_python         | 359 us                                                       | 403 us: 1.12x slower                                                  |
| deepcopy_reduce            | 4.04 us                                                      | 4.61 us: 1.14x slower                                                 |
| docutils                   | 3.10 sec                                                     | 3.54 sec: 1.14x slower                                                |
| python_startup             | 13.0 ms                                                      | 14.9 ms: 1.14x slower                                                 |
| pprint_safe_repr           | 933 ms                                                       | 1.07 sec: 1.15x slower                                                |
| pprint_pformat             | 1.93 sec                                                     | 2.22 sec: 1.15x slower                                                |
| nqueens                    | 98.9 ms                                                      | 114 ms: 1.16x slower                                                  |
| 2to3                       | 305 ms                                                       | 353 ms: 1.16x slower                                                  |
| sympy_expand               | 457 ms                                                       | 532 ms: 1.16x slower                                                  |
| django_template            | 42.3 ms                                                      | 49.3 ms: 1.17x slower                                                 |
| sqlglot_transpile          | 1.71 ms                                                      | 2.01 ms: 1.17x slower                                                 |
| deltablue                  | 3.88 ms                                                      | 4.57 ms: 1.18x slower                                                 |
| bench_mp_pool              | 7.03 ms                                                      | 8.28 ms: 1.18x slower                                                 |
| sympy_str                  | 265 ms                                                       | 313 ms: 1.18x slower                                                  |
| dulwich_log                | 58.5 ms                                                      | 69.5 ms: 1.19x slower                                                 |
| genshi_text                | 27.4 ms                                                      | 33.2 ms: 1.21x slower                                                 |
| hexiom                     | 7.08 ms                                                      | 8.67 ms: 1.22x slower                                                 |
| sympy_integrate            | 20.9 ms                                                      | 25.6 ms: 1.23x slower                                                 |
| pylint                     | 337 ms                                                       | 415 ms: 1.23x slower                                                  |
| chaos                      | 68.3 ms                                                      | 85.6 ms: 1.25x slower                                                 |
| sympy_sum                  | 144 ms                                                       | 181 ms: 1.26x slower                                                  |
| python_startup_no_site     | 8.60 ms                                                      | 10.9 ms: 1.26x slower                                                 |
| scimark_lu                 | 141 ms                                                       | 179 ms: 1.27x slower                                                  |
| regex_compile              | 128 ms                                                       | 165 ms: 1.29x slower                                                  |
| genshi_xml                 | 60.4 ms                                                      | 80.0 ms: 1.33x slower                                                 |
| Geometric mean             | (ref)                                                        | 1.07x slower                                                          |

Benchmark hidden because not significant (15): nbody, xml_etree_process, pickle_dict, json, pidigits, json_dumps, logging_simple, xml_etree_parse, json_loads, logging_format, coroutines, thrift, create_gc_cycles, async_tree_none_tg, coverage
Ignored benchmarks (4) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, bpe_tokeniser, gunicorn, mypy2

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.03x
- 95% likely to have a slowdown of 1.03x
- 99% likely to have a slowdown of 1.03x

# Memory
- memory change: 1.09x
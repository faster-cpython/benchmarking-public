# Results vs. base

- fork: brandtbucher
- ref: faster_pprint
- machine: linux-x86_64
- commit hash: ccfdf31
- commit date: 2025-06-17
- overall geometric mean: 1.127x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.10x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250617-linux-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde | bm-20250617-linux-x86_64-brandtbucher-faster_pprint-3.15.0a0-ccfdf31 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 292 ms                                                                | 257 ms: 1.14x faster                                                 |
| docutils       | 2.85 sec                                                              | 2.58 sec: 1.11x faster                                               |
| html5lib       | 64.8 ms                                                               | 62.8 ms: 1.03x faster                                                |
| sphinx         | 1.13 sec                                                              | 1.01 sec: 1.12x faster                                               |
| Geometric mean | (ref)                                                                 | 1.10x faster                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250617-linux-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde | bm-20250617-linux-x86_64-brandtbucher-faster_pprint-3.15.0a0-ccfdf31 |
|----------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_cpu_io_mixed_tg | 593 ms                                                                | 497 ms: 1.19x faster                                                 |
| async_tree_cpu_io_mixed    | 602 ms                                                                | 505 ms: 1.19x faster                                                 |
| async_tree_memoization_tg  | 346 ms                                                                | 311 ms: 1.11x faster                                                 |
| async_tree_none_tg         | 276 ms                                                                | 249 ms: 1.11x faster                                                 |
| async_tree_memoization     | 347 ms                                                                | 314 ms: 1.10x faster                                                 |
| async_tree_io              | 663 ms                                                                | 601 ms: 1.10x faster                                                 |
| async_tree_none            | 289 ms                                                                | 264 ms: 1.09x faster                                                 |
| async_tree_io_tg           | 676 ms                                                                | 633 ms: 1.07x faster                                                 |
| coroutines                 | 26.8 ms                                                               | 25.9 ms: 1.04x faster                                                |
| async_generators           | 413 ms                                                                | 415 ms: 1.01x slower                                                 |
| Geometric mean             | (ref)                                                                 | 1.09x faster                                                         |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250617-linux-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde | bm-20250617-linux-x86_64-brandtbucher-faster_pprint-3.15.0a0-ccfdf31 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| pidigits       | 205 ms                                                                | 193 ms: 1.06x faster                                                 |
| nbody          | 106 ms                                                                | 99.9 ms: 1.06x faster                                                |
| float          | 75.3 ms                                                               | 73.9 ms: 1.02x faster                                                |
| Geometric mean | (ref)                                                                 | 1.05x faster                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250617-linux-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde | bm-20250617-linux-x86_64-brandtbucher-faster_pprint-3.15.0a0-ccfdf31 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_compile  | 144 ms                                                                | 127 ms: 1.13x faster                                                 |
| regex_v8       | 24.2 ms                                                               | 22.0 ms: 1.10x faster                                                |
| regex_dna      | 197 ms                                                                | 201 ms: 1.02x slower                                                 |
| regex_effbot   | 2.93 ms                                                               | 3.26 ms: 1.11x slower                                                |
| Geometric mean | (ref)                                                                 | 1.02x faster                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250617-linux-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde | bm-20250617-linux-x86_64-brandtbucher-faster_pprint-3.15.0a0-ccfdf31 |
|----------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| xml_etree_generate   | 108 ms                                                                | 85.9 ms: 1.26x faster                                                |
| xml_etree_process    | 74.4 ms                                                               | 60.5 ms: 1.23x faster                                                |
| json_dumps           | 13.4 ms                                                               | 11.1 ms: 1.21x faster                                                |
| json_loads           | 34.0 us                                                               | 28.5 us: 1.19x faster                                                |
| unpickle_pure_python | 259 us                                                                | 222 us: 1.16x faster                                                 |
| pickle_pure_python   | 374 us                                                                | 323 us: 1.16x faster                                                 |
| xml_etree_parse      | 162 ms                                                                | 144 ms: 1.13x faster                                                 |
| xml_etree_iterparse  | 112 ms                                                                | 99.0 ms: 1.13x faster                                                |
| tomli_loads          | 2.22 sec                                                              | 1.99 sec: 1.12x faster                                               |
| Geometric mean       | (ref)                                                                 | 1.18x faster                                                         |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250617-linux-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde | bm-20250617-linux-x86_64-brandtbucher-faster_pprint-3.15.0a0-ccfdf31 |
|------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup         | 13.2 ms                                                               | 12.2 ms: 1.08x faster                                                |
| python_startup_no_site | 7.40 ms                                                               | 6.90 ms: 1.07x faster                                                |
| Geometric mean         | (ref)                                                                 | 1.08x faster                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250617-linux-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde | bm-20250617-linux-x86_64-brandtbucher-faster_pprint-3.15.0a0-ccfdf31 |
|-----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| django_template | 40.8 ms                                                               | 32.3 ms: 1.26x faster                                                |
| mako            | 13.6 ms                                                               | 11.2 ms: 1.21x faster                                                |
| genshi_text     | 25.7 ms                                                               | 21.6 ms: 1.19x faster                                                |
| genshi_xml      | 57.2 ms                                                               | 49.5 ms: 1.15x faster                                                |
| Geometric mean  | (ref)                                                                 | 1.20x faster                                                         |

All benchmarks:
===============

| Benchmark                  | bm-20250617-linux-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde | bm-20250617-linux-x86_64-brandtbucher-faster_pprint-3.15.0a0-ccfdf31 |
|----------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| pprint_safe_repr           | 993 ms                                                                | 731 ms: 1.36x faster                                                 |
| pprint_pformat             | 2.01 sec                                                              | 1.49 sec: 1.35x faster                                               |
| logging_silent             | 623 ns                                                                | 474 ns: 1.31x faster                                                 |
| django_template            | 40.8 ms                                                               | 32.3 ms: 1.26x faster                                                |
| xml_etree_generate         | 108 ms                                                                | 85.9 ms: 1.26x faster                                                |
| thrift                     | 956 us                                                                | 764 us: 1.25x faster                                                 |
| richards                   | 54.3 ms                                                               | 43.6 ms: 1.24x faster                                                |
| richards_super             | 62.2 ms                                                               | 50.1 ms: 1.24x faster                                                |
| logging_format             | 8.43 us                                                               | 6.83 us: 1.23x faster                                                |
| deepcopy                   | 315 us                                                                | 256 us: 1.23x faster                                                 |
| xml_etree_process          | 74.4 ms                                                               | 60.5 ms: 1.23x faster                                                |
| json_dumps                 | 13.4 ms                                                               | 11.1 ms: 1.21x faster                                                |
| sqlglot_v2_normalize       | 128 ms                                                                | 106 ms: 1.21x faster                                                 |
| mako                       | 13.6 ms                                                               | 11.2 ms: 1.21x faster                                                |
| logging_simple             | 7.47 us                                                               | 6.16 us: 1.21x faster                                                |
| nqueens                    | 98.2 ms                                                               | 81.4 ms: 1.21x faster                                                |
| deepcopy_reduce            | 3.32 us                                                               | 2.76 us: 1.20x faster                                                |
| mdp                        | 1.47 sec                                                              | 1.23 sec: 1.20x faster                                               |
| telco                      | 9.52 ms                                                               | 7.96 ms: 1.20x faster                                                |
| sqlglot_v2_optimize        | 63.1 ms                                                               | 52.7 ms: 1.20x faster                                                |
| json_loads                 | 34.0 us                                                               | 28.5 us: 1.19x faster                                                |
| sympy_expand               | 541 ms                                                                | 453 ms: 1.19x faster                                                 |
| comprehensions             | 19.3 us                                                               | 16.1 us: 1.19x faster                                                |
| async_tree_cpu_io_mixed_tg | 593 ms                                                                | 497 ms: 1.19x faster                                                 |
| async_tree_cpu_io_mixed    | 602 ms                                                                | 505 ms: 1.19x faster                                                 |
| subparsers                 | 28.1 ms                                                               | 23.5 ms: 1.19x faster                                                |
| genshi_text                | 25.7 ms                                                               | 21.6 ms: 1.19x faster                                                |
| typing_runtime_protocols   | 198 us                                                                | 168 us: 1.18x faster                                                 |
| raytrace                   | 320 ms                                                                | 274 ms: 1.17x faster                                                 |
| bpe_tokeniser              | 5.32 sec                                                              | 4.55 sec: 1.17x faster                                               |
| coverage                   | 102 ms                                                                | 87.4 ms: 1.17x faster                                                |
| unpickle_pure_python       | 259 us                                                                | 222 us: 1.16x faster                                                 |
| deepcopy_memo              | 34.1 us                                                               | 29.5 us: 1.16x faster                                                |
| pickle_pure_python         | 374 us                                                                | 323 us: 1.16x faster                                                 |
| sympy_str                  | 308 ms                                                                | 266 ms: 1.16x faster                                                 |
| fannkuch                   | 479 ms                                                                | 415 ms: 1.16x faster                                                 |
| genshi_xml                 | 57.2 ms                                                               | 49.5 ms: 1.15x faster                                                |
| json                       | 6.08 ms                                                               | 5.34 ms: 1.14x faster                                                |
| 2to3                       | 292 ms                                                                | 257 ms: 1.14x faster                                                 |
| crypto_pyaes               | 85.6 ms                                                               | 75.7 ms: 1.13x faster                                                |
| xml_etree_parse            | 162 ms                                                                | 144 ms: 1.13x faster                                                 |
| xml_etree_iterparse        | 112 ms                                                                | 99.0 ms: 1.13x faster                                                |
| regex_compile              | 144 ms                                                                | 127 ms: 1.13x faster                                                 |
| scimark_sparse_mat_mult    | 5.61 ms                                                               | 4.98 ms: 1.12x faster                                                |
| sqlglot_v2_transpile       | 1.76 ms                                                               | 1.57 ms: 1.12x faster                                                |
| sphinx                     | 1.13 sec                                                              | 1.01 sec: 1.12x faster                                               |
| many_optionals             | 1.08 ms                                                               | 961 us: 1.12x faster                                                 |
| tomli_loads                | 2.22 sec                                                              | 1.99 sec: 1.12x faster                                               |
| sympy_sum                  | 166 ms                                                                | 149 ms: 1.12x faster                                                 |
| sqlglot_v2_parse           | 1.41 ms                                                               | 1.26 ms: 1.12x faster                                                |
| pycparser                  | 1.26 sec                                                              | 1.13 sec: 1.12x faster                                               |
| scimark_sor                | 134 ms                                                                | 120 ms: 1.11x faster                                                 |
| chaos                      | 68.8 ms                                                               | 61.9 ms: 1.11x faster                                                |
| pylint                     | 311 ms                                                                | 280 ms: 1.11x faster                                                 |
| async_tree_memoization_tg  | 346 ms                                                                | 311 ms: 1.11x faster                                                 |
| async_tree_none_tg         | 276 ms                                                                | 249 ms: 1.11x faster                                                 |
| scimark_monte_carlo        | 76.4 ms                                                               | 68.9 ms: 1.11x faster                                                |
| docutils                   | 2.85 sec                                                              | 2.58 sec: 1.11x faster                                               |
| async_tree_memoization     | 347 ms                                                                | 314 ms: 1.10x faster                                                 |
| sympy_integrate            | 20.9 ms                                                               | 19.0 ms: 1.10x faster                                                |
| async_tree_io              | 663 ms                                                                | 601 ms: 1.10x faster                                                 |
| hexiom                     | 6.65 ms                                                               | 6.03 ms: 1.10x faster                                                |
| sqlite_synth               | 3.18 us                                                               | 2.90 us: 1.10x faster                                                |
| regex_v8                   | 24.2 ms                                                               | 22.0 ms: 1.10x faster                                                |
| generators                 | 33.0 ms                                                               | 30.1 ms: 1.10x faster                                                |
| async_tree_none            | 289 ms                                                                | 264 ms: 1.09x faster                                                 |
| djangocms                  | 24.4 us                                                               | 22.3 us: 1.09x faster                                                |
| scimark_lu                 | 133 ms                                                                | 122 ms: 1.09x faster                                                 |
| meteor_contest             | 116 ms                                                                | 107 ms: 1.09x faster                                                 |
| python_startup             | 13.2 ms                                                               | 12.2 ms: 1.08x faster                                                |
| spectral_norm              | 113 ms                                                                | 105 ms: 1.08x faster                                                 |
| deltablue                  | 3.86 ms                                                               | 3.58 ms: 1.08x faster                                                |
| scimark_fft                | 403 ms                                                                | 374 ms: 1.08x faster                                                 |
| pathlib                    | 18.4 ms                                                               | 17.1 ms: 1.08x faster                                                |
| dulwich_log                | 63.8 ms                                                               | 59.4 ms: 1.07x faster                                                |
| python_startup_no_site     | 7.40 ms                                                               | 6.90 ms: 1.07x faster                                                |
| async_tree_io_tg           | 676 ms                                                                | 633 ms: 1.07x faster                                                 |
| pidigits                   | 205 ms                                                                | 193 ms: 1.06x faster                                                 |
| nbody                      | 106 ms                                                                | 99.9 ms: 1.06x faster                                                |
| pyflate                    | 465 ms                                                                | 440 ms: 1.06x faster                                                 |
| go                         | 119 ms                                                                | 114 ms: 1.04x faster                                                 |
| coroutines                 | 26.8 ms                                                               | 25.9 ms: 1.04x faster                                                |
| k_core                     | 2.40 sec                                                              | 2.31 sec: 1.04x faster                                               |
| html5lib                   | 64.8 ms                                                               | 62.8 ms: 1.03x faster                                                |
| create_gc_cycles           | 2.63 ms                                                               | 2.58 ms: 1.02x faster                                                |
| float                      | 75.3 ms                                                               | 73.9 ms: 1.02x faster                                                |
| gc_traversal               | 5.14 ms                                                               | 5.06 ms: 1.02x faster                                                |
| shortest_path              | 532 ms                                                                | 525 ms: 1.01x faster                                                 |
| async_generators           | 413 ms                                                                | 415 ms: 1.01x slower                                                 |
| regex_dna                  | 197 ms                                                                | 201 ms: 1.02x slower                                                 |
| regex_effbot               | 2.93 ms                                                               | 3.26 ms: 1.11x slower                                                |
| Geometric mean             | (ref)                                                                 | 1.13x faster                                                         |

Benchmark hidden because not significant (2): connected_components, asyncio_websockets
Ignored benchmarks (10) of results/bm-20250617-3.15.0a0-fba5dde/bm-20250617-linux-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde.json: asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.127x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.10x
- 95% likely to have a speedup of 1.10x
- 99% likely to have a speedup of 1.10x

# Memory
- memory change: 1.00x
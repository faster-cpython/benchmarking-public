# Results vs. base

- fork: python
- ref: 2f60b8f02fe7cb83dd58
- machine: linux-x86_64
- commit hash: 2f60b8f
- commit date: 2025-11-01
- overall geometric mean: 1.003x slower
- HPT reliability: 98.33%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20251101-3.15.0a1+-2f60b8f/bm-20251101-pythonperf2-x86_64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f.json | results/bm-20251101-3.15.0a1+-2f60b8f-JIT/bm-20251101-pythonperf2-x86_64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 276 ms                                                                                                                  | 280 ms: 1.02x slower                                                                                                        |
| docutils       | 2.84 sec                                                                                                                | 2.88 sec: 1.02x slower                                                                                                      |
| sphinx         | 1.06 sec                                                                                                                | 1.07 sec: 1.01x slower                                                                                                      |
| Geometric mean | (ref)                                                                                                                   | 1.01x slower                                                                                                                |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | results/bm-20251101-3.15.0a1+-2f60b8f/bm-20251101-pythonperf2-x86_64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f.json | results/bm-20251101-3.15.0a1+-2f60b8f-JIT/bm-20251101-pythonperf2-x86_64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f.json |
|---------------------------|:-----------------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------------:|
| asyncio_tcp_ssl           | 1.58 sec                                                                                                                | 1.59 sec: 1.00x slower                                                                                                      |
| asyncio_websockets        | 409 ms                                                                                                                  | 411 ms: 1.00x slower                                                                                                        |
| asyncio_tcp               | 370 ms                                                                                                                  | 372 ms: 1.01x slower                                                                                                        |
| async_tree_none           | 243 ms                                                                                                                  | 248 ms: 1.02x slower                                                                                                        |
| coroutines                | 22.4 ms                                                                                                                 | 22.9 ms: 1.02x slower                                                                                                       |
| async_tree_io_tg          | 558 ms                                                                                                                  | 576 ms: 1.03x slower                                                                                                        |
| async_generators          | 426 ms                                                                                                                  | 444 ms: 1.04x slower                                                                                                        |
| async_tree_memoization_tg | 296 ms                                                                                                                  | 315 ms: 1.07x slower                                                                                                        |
| Geometric mean            | (ref)                                                                                                                   | 1.02x slower                                                                                                                |

Benchmark hidden because not significant (5): async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, async_tree_memoization, async_tree_io, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20251101-3.15.0a1+-2f60b8f/bm-20251101-pythonperf2-x86_64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f.json | results/bm-20251101-3.15.0a1+-2f60b8f-JIT/bm-20251101-pythonperf2-x86_64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------------:|
| pidigits       | 254 ms                                                                                                                  | 255 ms: 1.00x slower                                                                                                        |
| nbody          | 89.7 ms                                                                                                                 | 92.7 ms: 1.03x slower                                                                                                       |
| Geometric mean | (ref)                                                                                                                   | 1.01x slower                                                                                                                |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20251101-3.15.0a1+-2f60b8f/bm-20251101-pythonperf2-x86_64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f.json | results/bm-20251101-3.15.0a1+-2f60b8f-JIT/bm-20251101-pythonperf2-x86_64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                                                                                 | 23.5 ms: 1.01x faster                                                                                                       |
| regex_compile  | 132 ms                                                                                                                  | 132 ms: 1.00x slower                                                                                                        |
| regex_effbot   | 3.48 ms                                                                                                                 | 3.51 ms: 1.01x slower                                                                                                       |
| regex_dna      | 222 ms                                                                                                                  | 228 ms: 1.03x slower                                                                                                        |
| Geometric mean | (ref)                                                                                                                   | 1.01x slower                                                                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20251101-3.15.0a1+-2f60b8f/bm-20251101-pythonperf2-x86_64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f.json | results/bm-20251101-3.15.0a1+-2f60b8f-JIT/bm-20251101-pythonperf2-x86_64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f.json |
|----------------------|:-----------------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------------:|
| unpickle_pure_python | 206 us                                                                                                                  | 194 us: 1.06x faster                                                                                                        |
| tomli_loads          | 1.97 sec                                                                                                                | 1.90 sec: 1.04x faster                                                                                                      |
| xml_etree_process    | 57.4 ms                                                                                                                 | 55.4 ms: 1.04x faster                                                                                                       |
| xml_etree_generate   | 81.1 ms                                                                                                                 | 78.7 ms: 1.03x faster                                                                                                       |
| xml_etree_parse      | 136 ms                                                                                                                  | 133 ms: 1.02x faster                                                                                                        |
| json_loads           | 25.2 us                                                                                                                 | 25.0 us: 1.01x faster                                                                                                       |
| xml_etree_iterparse  | 86.2 ms                                                                                                                 | 85.4 ms: 1.01x faster                                                                                                       |
| json_dumps           | 10.1 ms                                                                                                                 | 10.2 ms: 1.00x slower                                                                                                       |
| pickle               | 12.3 us                                                                                                                 | 12.5 us: 1.02x slower                                                                                                       |
| pickle_list          | 4.88 us                                                                                                                 | 4.98 us: 1.02x slower                                                                                                       |
| pickle_pure_python   | 322 us                                                                                                                  | 329 us: 1.02x slower                                                                                                        |
| pickle_dict          | 31.8 us                                                                                                                 | 33.6 us: 1.06x slower                                                                                                       |
| Geometric mean       | (ref)                                                                                                                   | 1.01x faster                                                                                                                |

Benchmark hidden because not significant (2): unpickle, unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | results/bm-20251101-3.15.0a1+-2f60b8f/bm-20251101-pythonperf2-x86_64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f.json | results/bm-20251101-3.15.0a1+-2f60b8f-JIT/bm-20251101-pythonperf2-x86_64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f.json |
|------------------------|:-----------------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------------:|
| python_startup         | 15.0 ms                                                                                                                 | 15.0 ms: 1.00x slower                                                                                                       |
| python_startup_no_site | 8.67 ms                                                                                                                 | 8.74 ms: 1.01x slower                                                                                                       |
| Geometric mean         | (ref)                                                                                                                   | 1.01x slower                                                                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark      | results/bm-20251101-3.15.0a1+-2f60b8f/bm-20251101-pythonperf2-x86_64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f.json | results/bm-20251101-3.15.0a1+-2f60b8f-JIT/bm-20251101-pythonperf2-x86_64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------------:|
| mako           | 10.7 ms                                                                                                                 | 9.74 ms: 1.10x faster                                                                                                       |
| genshi_text    | 22.8 ms                                                                                                                 | 23.9 ms: 1.05x slower                                                                                                       |
| genshi_xml     | 53.2 ms                                                                                                                 | 56.1 ms: 1.05x slower                                                                                                       |
| Geometric mean | (ref)                                                                                                                   | 1.00x faster                                                                                                                |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                 | results/bm-20251101-3.15.0a1+-2f60b8f/bm-20251101-pythonperf2-x86_64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f.json | results/bm-20251101-3.15.0a1+-2f60b8f-JIT/bm-20251101-pythonperf2-x86_64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f.json |
|---------------------------|:-----------------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------------:|
| bench_mp_pool             | 2.57 sec                                                                                                                | 1.33 sec: 1.92x faster                                                                                                      |
| richards                  | 44.2 ms                                                                                                                 | 37.9 ms: 1.17x faster                                                                                                       |
| richards_super            | 50.1 ms                                                                                                                 | 43.8 ms: 1.14x faster                                                                                                       |
| mako                      | 10.7 ms                                                                                                                 | 9.74 ms: 1.10x faster                                                                                                       |
| pprint_pformat            | 1.57 sec                                                                                                                | 1.46 sec: 1.07x faster                                                                                                      |
| unpickle_pure_python      | 206 us                                                                                                                  | 194 us: 1.06x faster                                                                                                        |
| pprint_safe_repr          | 771 ms                                                                                                                  | 730 ms: 1.06x faster                                                                                                        |
| k_core                    | 1.95 sec                                                                                                                | 1.87 sec: 1.04x faster                                                                                                      |
| tomli_loads               | 1.97 sec                                                                                                                | 1.90 sec: 1.04x faster                                                                                                      |
| deepcopy_memo             | 24.9 us                                                                                                                 | 24.0 us: 1.04x faster                                                                                                       |
| connected_components      | 422 ms                                                                                                                  | 408 ms: 1.04x faster                                                                                                        |
| xml_etree_process         | 57.4 ms                                                                                                                 | 55.4 ms: 1.04x faster                                                                                                       |
| xml_etree_generate        | 81.1 ms                                                                                                                 | 78.7 ms: 1.03x faster                                                                                                       |
| pyflate                   | 405 ms                                                                                                                  | 394 ms: 1.03x faster                                                                                                        |
| shortest_path             | 454 ms                                                                                                                  | 443 ms: 1.03x faster                                                                                                        |
| xml_etree_parse           | 136 ms                                                                                                                  | 133 ms: 1.02x faster                                                                                                        |
| scimark_fft               | 281 ms                                                                                                                  | 276 ms: 1.02x faster                                                                                                        |
| coverage                  | 79.9 ms                                                                                                                 | 78.5 ms: 1.02x faster                                                                                                       |
| bpe_tokeniser             | 4.68 sec                                                                                                                | 4.62 sec: 1.01x faster                                                                                                      |
| generators                | 29.8 ms                                                                                                                 | 29.4 ms: 1.01x faster                                                                                                       |
| regex_v8                  | 23.8 ms                                                                                                                 | 23.5 ms: 1.01x faster                                                                                                       |
| pycparser                 | 1.22 sec                                                                                                                | 1.21 sec: 1.01x faster                                                                                                      |
| json_loads                | 25.2 us                                                                                                                 | 25.0 us: 1.01x faster                                                                                                       |
| xml_etree_iterparse       | 86.2 ms                                                                                                                 | 85.4 ms: 1.01x faster                                                                                                       |
| logging_format            | 6.49 us                                                                                                                 | 6.44 us: 1.01x faster                                                                                                       |
| subparsers                | 44.4 ms                                                                                                                 | 44.1 ms: 1.01x faster                                                                                                       |
| logging_simple            | 5.90 us                                                                                                                 | 5.86 us: 1.01x faster                                                                                                       |
| asyncio_tcp_ssl           | 1.58 sec                                                                                                                | 1.59 sec: 1.00x slower                                                                                                      |
| regex_compile             | 132 ms                                                                                                                  | 132 ms: 1.00x slower                                                                                                        |
| pidigits                  | 254 ms                                                                                                                  | 255 ms: 1.00x slower                                                                                                        |
| json_dumps                | 10.1 ms                                                                                                                 | 10.2 ms: 1.00x slower                                                                                                       |
| many_optionals            | 1.19 ms                                                                                                                 | 1.19 ms: 1.00x slower                                                                                                       |
| dulwich_log               | 59.0 ms                                                                                                                 | 59.3 ms: 1.00x slower                                                                                                       |
| asyncio_websockets        | 409 ms                                                                                                                  | 411 ms: 1.00x slower                                                                                                        |
| python_startup            | 15.0 ms                                                                                                                 | 15.0 ms: 1.00x slower                                                                                                       |
| asyncio_tcp               | 370 ms                                                                                                                  | 372 ms: 1.01x slower                                                                                                        |
| sphinx                    | 1.06 sec                                                                                                                | 1.07 sec: 1.01x slower                                                                                                      |
| python_startup_no_site    | 8.67 ms                                                                                                                 | 8.74 ms: 1.01x slower                                                                                                       |
| spectral_norm             | 82.9 ms                                                                                                                 | 83.7 ms: 1.01x slower                                                                                                       |
| regex_effbot              | 3.48 ms                                                                                                                 | 3.51 ms: 1.01x slower                                                                                                       |
| deepcopy                  | 264 us                                                                                                                  | 267 us: 1.01x slower                                                                                                        |
| go                        | 118 ms                                                                                                                  | 119 ms: 1.01x slower                                                                                                        |
| mdp                       | 1.25 sec                                                                                                                | 1.27 sec: 1.01x slower                                                                                                      |
| sympy_integrate           | 21.9 ms                                                                                                                 | 22.3 ms: 1.02x slower                                                                                                       |
| raytrace                  | 268 ms                                                                                                                  | 272 ms: 1.02x slower                                                                                                        |
| docutils                  | 2.84 sec                                                                                                                | 2.88 sec: 1.02x slower                                                                                                      |
| pickle                    | 12.3 us                                                                                                                 | 12.5 us: 1.02x slower                                                                                                       |
| sympy_sum                 | 149 ms                                                                                                                  | 151 ms: 1.02x slower                                                                                                        |
| bench_thread_pool         | 929 us                                                                                                                  | 946 us: 1.02x slower                                                                                                        |
| 2to3                      | 276 ms                                                                                                                  | 280 ms: 1.02x slower                                                                                                        |
| async_tree_none           | 243 ms                                                                                                                  | 248 ms: 1.02x slower                                                                                                        |
| scimark_sor               | 98.6 ms                                                                                                                 | 100 ms: 1.02x slower                                                                                                        |
| json                      | 5.34 ms                                                                                                                 | 5.44 ms: 1.02x slower                                                                                                       |
| pickle_list               | 4.88 us                                                                                                                 | 4.98 us: 1.02x slower                                                                                                       |
| sympy_str                 | 287 ms                                                                                                                  | 292 ms: 1.02x slower                                                                                                        |
| sympy_expand              | 490 ms                                                                                                                  | 500 ms: 1.02x slower                                                                                                        |
| pathlib                   | 14.8 ms                                                                                                                 | 15.1 ms: 1.02x slower                                                                                                       |
| pickle_pure_python        | 322 us                                                                                                                  | 329 us: 1.02x slower                                                                                                        |
| coroutines                | 22.4 ms                                                                                                                 | 22.9 ms: 1.02x slower                                                                                                       |
| deltablue                 | 3.12 ms                                                                                                                 | 3.20 ms: 1.02x slower                                                                                                       |
| telco                     | 152 ms                                                                                                                  | 156 ms: 1.02x slower                                                                                                        |
| sqlglot_v2_transpile      | 1.64 ms                                                                                                                 | 1.68 ms: 1.02x slower                                                                                                       |
| create_gc_cycles          | 2.86 ms                                                                                                                 | 2.94 ms: 1.03x slower                                                                                                       |
| crypto_pyaes              | 74.9 ms                                                                                                                 | 76.8 ms: 1.03x slower                                                                                                       |
| deepcopy_reduce           | 2.90 us                                                                                                                 | 2.97 us: 1.03x slower                                                                                                       |
| meteor_contest            | 119 ms                                                                                                                  | 122 ms: 1.03x slower                                                                                                        |
| regex_dna                 | 222 ms                                                                                                                  | 228 ms: 1.03x slower                                                                                                        |
| chaos                     | 55.7 ms                                                                                                                 | 57.4 ms: 1.03x slower                                                                                                       |
| async_tree_io_tg          | 558 ms                                                                                                                  | 576 ms: 1.03x slower                                                                                                        |
| nbody                     | 89.7 ms                                                                                                                 | 92.7 ms: 1.03x slower                                                                                                       |
| sqlglot_v2_normalize      | 112 ms                                                                                                                  | 116 ms: 1.03x slower                                                                                                        |
| typing_runtime_protocols  | 167 us                                                                                                                  | 173 us: 1.04x slower                                                                                                        |
| hexiom                    | 5.67 ms                                                                                                                 | 5.88 ms: 1.04x slower                                                                                                       |
| sqlglot_v2_optimize       | 56.2 ms                                                                                                                 | 58.3 ms: 1.04x slower                                                                                                       |
| scimark_monte_carlo       | 59.1 ms                                                                                                                 | 61.6 ms: 1.04x slower                                                                                                       |
| async_generators          | 426 ms                                                                                                                  | 444 ms: 1.04x slower                                                                                                        |
| fannkuch                  | 358 ms                                                                                                                  | 375 ms: 1.05x slower                                                                                                        |
| genshi_text               | 22.8 ms                                                                                                                 | 23.9 ms: 1.05x slower                                                                                                       |
| scimark_lu                | 91.6 ms                                                                                                                 | 96.2 ms: 1.05x slower                                                                                                       |
| genshi_xml                | 53.2 ms                                                                                                                 | 56.1 ms: 1.05x slower                                                                                                       |
| comprehensions            | 16.2 us                                                                                                                 | 17.0 us: 1.05x slower                                                                                                       |
| scimark_sparse_mat_mult   | 4.49 ms                                                                                                                 | 4.74 ms: 1.05x slower                                                                                                       |
| pickle_dict               | 31.8 us                                                                                                                 | 33.6 us: 1.06x slower                                                                                                       |
| async_tree_memoization_tg | 296 ms                                                                                                                  | 315 ms: 1.07x slower                                                                                                        |
| gc_traversal              | 6.14 ms                                                                                                                 | 6.88 ms: 1.12x slower                                                                                                       |
| unpack_sequence           | 45.3 ns                                                                                                                 | 52.4 ns: 1.16x slower                                                                                                       |
| Geometric mean            | (ref)                                                                                                                   | 1.00x slower                                                                                                                |

Benchmark hidden because not significant (17): html5lib, unpickle, django_template, sqlite_synth, logging_silent, djangocms, unpickle_list, nqueens, async_tree_cpu_io_mixed, sqlglot_v2_parse, async_tree_cpu_io_mixed_tg, pylint, thrift, float, async_tree_memoization, async_tree_io, async_tree_none_tg

- Geometric mean (including insignificant results): 1.003x slower

# HPT report

- Reliability score: 98.33% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.01x
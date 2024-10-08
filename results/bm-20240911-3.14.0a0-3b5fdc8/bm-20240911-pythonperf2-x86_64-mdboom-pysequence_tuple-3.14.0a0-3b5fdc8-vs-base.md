# Results vs. base

- fork: mdboom
- ref: pysequence_tuple
- machine: linux-x86_64
- commit hash: 3b5fdc8
- commit date: 2024-09-11
- overall geometric mean: 1.01x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240911-pythonperf2-x86_64-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b | bm-20240911-pythonperf2-x86_64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|----------------|:---------------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 281 ms                                                                      | 287 ms: 1.02x slower                                                    |
| html5lib       | 71.5 ms                                                                     | 72.9 ms: 1.02x slower                                                   |
| tornado_http   | 116 ms                                                                      | 118 ms: 1.02x slower                                                    |
| Geometric mean | (ref)                                                                       | 1.01x slower                                                            |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240911-pythonperf2-x86_64-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b | bm-20240911-pythonperf2-x86_64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|----------------------------|:---------------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| asyncio_tcp_ssl            | 1.57 sec                                                                    | 1.58 sec: 1.00x slower                                                  |
| async_tree_io_tg           | 778 ms                                                                      | 784 ms: 1.01x slower                                                    |
| async_tree_memoization_tg  | 387 ms                                                                      | 392 ms: 1.01x slower                                                    |
| async_tree_memoization     | 396 ms                                                                      | 403 ms: 1.02x slower                                                    |
| async_tree_cpu_io_mixed_tg | 559 ms                                                                      | 570 ms: 1.02x slower                                                    |
| asyncio_websockets         | 384 ms                                                                      | 392 ms: 1.02x slower                                                    |
| async_tree_cpu_io_mixed    | 567 ms                                                                      | 580 ms: 1.02x slower                                                    |
| async_tree_none            | 317 ms                                                                      | 326 ms: 1.03x slower                                                    |
| async_generators           | 350 ms                                                                      | 360 ms: 1.03x slower                                                    |
| coroutines                 | 21.3 ms                                                                     | 22.3 ms: 1.04x slower                                                   |
| Geometric mean             | (ref)                                                                       | 1.02x slower                                                            |

Benchmark hidden because not significant (3): async_tree_io, asyncio_tcp, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240911-pythonperf2-x86_64-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b | bm-20240911-pythonperf2-x86_64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|----------------|:---------------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| nbody          | 87.6 ms                                                                     | 85.3 ms: 1.03x faster                                                   |
| float          | 79.7 ms                                                                     | 80.4 ms: 1.01x slower                                                   |
| pidigits       | 251 ms                                                                      | 254 ms: 1.01x slower                                                    |
| Geometric mean | (ref)                                                                       | 1.00x faster                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240911-pythonperf2-x86_64-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b | bm-20240911-pythonperf2-x86_64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|----------------|:---------------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_effbot   | 3.57 ms                                                                     | 3.46 ms: 1.03x faster                                                   |
| regex_dna      | 243 ms                                                                      | 240 ms: 1.01x faster                                                    |
| regex_v8       | 26.1 ms                                                                     | 25.8 ms: 1.01x faster                                                   |
| regex_compile  | 141 ms                                                                      | 140 ms: 1.01x faster                                                    |
| Geometric mean | (ref)                                                                       | 1.01x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240911-pythonperf2-x86_64-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b | bm-20240911-pythonperf2-x86_64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|----------------------|:---------------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| unpickle_list        | 4.75 us                                                                     | 4.66 us: 1.02x faster                                                   |
| pickle_list          | 4.16 us                                                                     | 4.13 us: 1.01x faster                                                   |
| pickle_dict          | 29.9 us                                                                     | 29.8 us: 1.00x faster                                                   |
| json_loads           | 24.8 us                                                                     | 24.9 us: 1.01x slower                                                   |
| unpickle             | 15.2 us                                                                     | 15.5 us: 1.02x slower                                                   |
| xml_etree_generate   | 83.7 ms                                                                     | 85.3 ms: 1.02x slower                                                   |
| json_dumps           | 10.7 ms                                                                     | 11.1 ms: 1.04x slower                                                   |
| unpickle_pure_python | 214 us                                                                      | 226 us: 1.05x slower                                                    |
| Geometric mean       | (ref)                                                                       | 1.01x slower                                                            |

Benchmark hidden because not significant (6): xml_etree_parse, xml_etree_iterparse, pickle, xml_etree_process, tomli_loads, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240911-pythonperf2-x86_64-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b | bm-20240911-pythonperf2-x86_64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|------------------------|:---------------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 13.4 ms                                                                     | 13.4 ms: 1.00x faster                                                   |
| python_startup_no_site | 8.96 ms                                                                     | 8.95 ms: 1.00x faster                                                   |
| Geometric mean         | (ref)                                                                       | 1.00x faster                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240911-pythonperf2-x86_64-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b | bm-20240911-pythonperf2-x86_64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|-----------------|:---------------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_xml      | 53.8 ms                                                                     | 54.2 ms: 1.01x slower                                                   |
| mako            | 10.2 ms                                                                     | 10.4 ms: 1.01x slower                                                   |
| genshi_text     | 24.8 ms                                                                     | 25.2 ms: 1.02x slower                                                   |
| django_template | 39.6 ms                                                                     | 41.3 ms: 1.04x slower                                                   |
| Geometric mean  | (ref)                                                                       | 1.02x slower                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20240911-pythonperf2-x86_64-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b | bm-20240911-pythonperf2-x86_64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|----------------------------|:---------------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| gc_traversal               | 4.88 ms                                                                     | 4.42 ms: 1.10x faster                                                   |
| coverage                   | 79.7 ms                                                                     | 77.4 ms: 1.03x faster                                                   |
| regex_effbot               | 3.57 ms                                                                     | 3.46 ms: 1.03x faster                                                   |
| nbody                      | 87.6 ms                                                                     | 85.3 ms: 1.03x faster                                                   |
| telco                      | 8.54 ms                                                                     | 8.35 ms: 1.02x faster                                                   |
| unpickle_list              | 4.75 us                                                                     | 4.66 us: 1.02x faster                                                   |
| deepcopy_memo              | 30.1 us                                                                     | 29.7 us: 1.01x faster                                                   |
| regex_dna                  | 243 ms                                                                      | 240 ms: 1.01x faster                                                    |
| regex_v8                   | 26.1 ms                                                                     | 25.8 ms: 1.01x faster                                                   |
| pickle_list                | 4.16 us                                                                     | 4.13 us: 1.01x faster                                                   |
| deepcopy_reduce            | 2.89 us                                                                     | 2.87 us: 1.01x faster                                                   |
| pprint_safe_repr           | 822 ms                                                                      | 816 ms: 1.01x faster                                                    |
| regex_compile              | 141 ms                                                                      | 140 ms: 1.01x faster                                                    |
| pprint_pformat             | 1.67 sec                                                                    | 1.67 sec: 1.00x faster                                                  |
| pickle_dict                | 29.9 us                                                                     | 29.8 us: 1.00x faster                                                   |
| pathlib                    | 15.7 ms                                                                     | 15.6 ms: 1.00x faster                                                   |
| hexiom                     | 6.31 ms                                                                     | 6.29 ms: 1.00x faster                                                   |
| python_startup             | 13.4 ms                                                                     | 13.4 ms: 1.00x faster                                                   |
| python_startup_no_site     | 8.96 ms                                                                     | 8.95 ms: 1.00x faster                                                   |
| sqlglot_optimize           | 58.3 ms                                                                     | 58.5 ms: 1.00x slower                                                   |
| meteor_contest             | 127 ms                                                                      | 127 ms: 1.00x slower                                                    |
| mdp                        | 2.50 sec                                                                    | 2.51 sec: 1.00x slower                                                  |
| deepcopy                   | 286 us                                                                      | 287 us: 1.00x slower                                                    |
| asyncio_tcp_ssl            | 1.57 sec                                                                    | 1.58 sec: 1.00x slower                                                  |
| sympy_str                  | 291 ms                                                                      | 293 ms: 1.01x slower                                                    |
| comprehensions             | 17.3 us                                                                     | 17.4 us: 1.01x slower                                                   |
| genshi_xml                 | 53.8 ms                                                                     | 54.2 ms: 1.01x slower                                                   |
| json_loads                 | 24.8 us                                                                     | 24.9 us: 1.01x slower                                                   |
| scimark_monte_carlo        | 67.8 ms                                                                     | 68.3 ms: 1.01x slower                                                   |
| async_tree_io_tg           | 778 ms                                                                      | 784 ms: 1.01x slower                                                    |
| float                      | 79.7 ms                                                                     | 80.4 ms: 1.01x slower                                                   |
| typing_runtime_protocols   | 171 us                                                                      | 172 us: 1.01x slower                                                    |
| sympy_integrate            | 23.0 ms                                                                     | 23.2 ms: 1.01x slower                                                   |
| mako                       | 10.2 ms                                                                     | 10.4 ms: 1.01x slower                                                   |
| raytrace                   | 275 ms                                                                      | 278 ms: 1.01x slower                                                    |
| async_tree_memoization_tg  | 387 ms                                                                      | 392 ms: 1.01x slower                                                    |
| logging_simple             | 6.39 us                                                                     | 6.47 us: 1.01x slower                                                   |
| sqlglot_transpile          | 1.82 ms                                                                     | 1.84 ms: 1.01x slower                                                   |
| sqlglot_parse              | 1.44 ms                                                                     | 1.46 ms: 1.01x slower                                                   |
| pidigits                   | 251 ms                                                                      | 254 ms: 1.01x slower                                                    |
| bpe_tokeniser              | 4.89 sec                                                                    | 4.97 sec: 1.02x slower                                                  |
| chaos                      | 62.3 ms                                                                     | 63.2 ms: 1.02x slower                                                   |
| genshi_text                | 24.8 ms                                                                     | 25.2 ms: 1.02x slower                                                   |
| sympy_expand               | 496 ms                                                                      | 504 ms: 1.02x slower                                                    |
| sympy_sum                  | 151 ms                                                                      | 153 ms: 1.02x slower                                                    |
| tornado_http               | 116 ms                                                                      | 118 ms: 1.02x slower                                                    |
| sqlite_synth               | 2.72 us                                                                     | 2.76 us: 1.02x slower                                                   |
| unpickle                   | 15.2 us                                                                     | 15.5 us: 1.02x slower                                                   |
| async_tree_memoization     | 396 ms                                                                      | 403 ms: 1.02x slower                                                    |
| xml_etree_generate         | 83.7 ms                                                                     | 85.3 ms: 1.02x slower                                                   |
| html5lib                   | 71.5 ms                                                                     | 72.9 ms: 1.02x slower                                                   |
| 2to3                       | 281 ms                                                                      | 287 ms: 1.02x slower                                                    |
| async_tree_cpu_io_mixed_tg | 559 ms                                                                      | 570 ms: 1.02x slower                                                    |
| spectral_norm              | 95.2 ms                                                                     | 97.1 ms: 1.02x slower                                                   |
| asyncio_websockets         | 384 ms                                                                      | 392 ms: 1.02x slower                                                    |
| generators                 | 29.0 ms                                                                     | 29.7 ms: 1.02x slower                                                   |
| async_tree_cpu_io_mixed    | 567 ms                                                                      | 580 ms: 1.02x slower                                                    |
| go                         | 136 ms                                                                      | 139 ms: 1.02x slower                                                    |
| nqueens                    | 88.2 ms                                                                     | 90.5 ms: 1.03x slower                                                   |
| deltablue                  | 3.42 ms                                                                     | 3.51 ms: 1.03x slower                                                   |
| async_tree_none            | 317 ms                                                                      | 326 ms: 1.03x slower                                                    |
| thrift                     | 846 us                                                                      | 868 us: 1.03x slower                                                    |
| logging_format             | 6.92 us                                                                     | 7.12 us: 1.03x slower                                                   |
| async_generators           | 350 ms                                                                      | 360 ms: 1.03x slower                                                    |
| richards                   | 50.4 ms                                                                     | 52.0 ms: 1.03x slower                                                   |
| richards_super             | 56.1 ms                                                                     | 57.9 ms: 1.03x slower                                                   |
| scimark_lu                 | 94.7 ms                                                                     | 98.1 ms: 1.04x slower                                                   |
| fannkuch                   | 367 ms                                                                      | 380 ms: 1.04x slower                                                    |
| json_dumps                 | 10.7 ms                                                                     | 11.1 ms: 1.04x slower                                                   |
| django_template            | 39.6 ms                                                                     | 41.3 ms: 1.04x slower                                                   |
| coroutines                 | 21.3 ms                                                                     | 22.3 ms: 1.04x slower                                                   |
| unpickle_pure_python       | 214 us                                                                      | 226 us: 1.05x slower                                                    |
| scimark_sor                | 111 ms                                                                      | 118 ms: 1.07x slower                                                    |
| unpack_sequence            | 46.1 ns                                                                     | 49.4 ns: 1.07x slower                                                   |
| Geometric mean             | (ref)                                                                       | 1.01x slower                                                            |

Benchmark hidden because not significant (23): async_tree_io, create_gc_cycles, xml_etree_parse, xml_etree_iterparse, dulwich_log, pickle, crypto_pyaes, xml_etree_process, tomli_loads, docutils, pickle_pure_python, scimark_fft, json, asyncio_tcp, logging_silent, sqlglot_normalize, pyflate, scimark_sparse_mat_mult, pycparser, bench_mp_pool, bench_thread_pool, pylint, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x
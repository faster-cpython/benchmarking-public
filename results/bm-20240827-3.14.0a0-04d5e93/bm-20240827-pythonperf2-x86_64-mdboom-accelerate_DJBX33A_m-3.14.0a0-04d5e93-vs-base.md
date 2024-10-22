# Results vs. base

- fork: mdboom
- ref: accelerate_DJBX33A_m
- machine: linux-x86_64
- commit hash: 04d5e93
- commit date: 2024-08-27
- overall geometric mean: 1.00x slower
- HPT reliability: 62.47%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240826-pythonperf2-x86_64-python-fe85a8291d9aa11c9ce9-3.14.0a0-fe85a82 | bm-20240827-pythonperf2-x86_64-mdboom-accelerate_DJBX33A_m-3.14.0a0-04d5e93 |
|----------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 281 ms                                                                      | 283 ms: 1.01x slower                                                        |
| docutils       | 2.95 sec                                                                    | 2.97 sec: 1.01x slower                                                      |
| tornado_http   | 116 ms                                                                      | 117 ms: 1.01x slower                                                        |
| Geometric mean | (ref)                                                                       | 1.01x slower                                                                |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20240826-pythonperf2-x86_64-python-fe85a8291d9aa11c9ce9-3.14.0a0-fe85a82 | bm-20240827-pythonperf2-x86_64-mdboom-accelerate_DJBX33A_m-3.14.0a0-04d5e93 |
|---------------------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| asyncio_websockets        | 395 ms                                                                      | 385 ms: 1.03x faster                                                        |
| async_tree_memoization_tg | 392 ms                                                                      | 387 ms: 1.01x faster                                                        |
| async_tree_memoization    | 401 ms                                                                      | 397 ms: 1.01x faster                                                        |
| asyncio_tcp_ssl           | 1.57 sec                                                                    | 1.58 sec: 1.00x slower                                                      |
| coroutines                | 21.3 ms                                                                     | 21.7 ms: 1.02x slower                                                       |
| Geometric mean            | (ref)                                                                       | 1.00x faster                                                                |

Benchmark hidden because not significant (8): async_tree_none, async_tree_cpu_io_mixed_tg, async_tree_none_tg, async_tree_cpu_io_mixed, asyncio_tcp, async_tree_io_tg, async_generators, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240826-pythonperf2-x86_64-python-fe85a8291d9aa11c9ce9-3.14.0a0-fe85a82 | bm-20240827-pythonperf2-x86_64-mdboom-accelerate_DJBX33A_m-3.14.0a0-04d5e93 |
|----------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 79.5 ms                                                                     | 78.4 ms: 1.01x faster                                                       |
| pidigits       | 252 ms                                                                      | 253 ms: 1.00x slower                                                        |
| nbody          | 85.9 ms                                                                     | 86.7 ms: 1.01x slower                                                       |
| Geometric mean | (ref)                                                                       | 1.00x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240826-pythonperf2-x86_64-python-fe85a8291d9aa11c9ce9-3.14.0a0-fe85a82 | bm-20240827-pythonperf2-x86_64-mdboom-accelerate_DJBX33A_m-3.14.0a0-04d5e93 |
|----------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_dna      | 254 ms                                                                      | 233 ms: 1.09x faster                                                        |
| regex_v8       | 27.1 ms                                                                     | 25.7 ms: 1.06x faster                                                       |
| regex_compile  | 141 ms                                                                      | 142 ms: 1.00x slower                                                        |
| Geometric mean | (ref)                                                                       | 1.04x faster                                                                |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20240826-pythonperf2-x86_64-python-fe85a8291d9aa11c9ce9-3.14.0a0-fe85a82 | bm-20240827-pythonperf2-x86_64-mdboom-accelerate_DJBX33A_m-3.14.0a0-04d5e93 |
|---------------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads         | 2.58 sec                                                                    | 2.37 sec: 1.09x faster                                                      |
| json_loads          | 25.1 us                                                                     | 24.8 us: 1.01x faster                                                       |
| xml_etree_iterparse | 100 ms                                                                      | 101 ms: 1.01x slower                                                        |
| pickle_pure_python  | 316 us                                                                      | 318 us: 1.01x slower                                                        |
| xml_etree_process   | 59.5 ms                                                                     | 60.1 ms: 1.01x slower                                                       |
| json_dumps          | 10.6 ms                                                                     | 10.8 ms: 1.02x slower                                                       |
| xml_etree_generate  | 84.7 ms                                                                     | 86.7 ms: 1.02x slower                                                       |
| Geometric mean      | (ref)                                                                       | 1.00x faster                                                                |

Benchmark hidden because not significant (2): unpickle_pure_python, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240826-pythonperf2-x86_64-python-fe85a8291d9aa11c9ce9-3.14.0a0-fe85a82 | bm-20240827-pythonperf2-x86_64-mdboom-accelerate_DJBX33A_m-3.14.0a0-04d5e93 |
|------------------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 13.3 ms                                                                     | 13.4 ms: 1.01x slower                                                       |
| python_startup_no_site | 9.02 ms                                                                     | 9.08 ms: 1.01x slower                                                       |
| Geometric mean         | (ref)                                                                       | 1.01x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240826-pythonperf2-x86_64-python-fe85a8291d9aa11c9ce9-3.14.0a0-fe85a82 | bm-20240827-pythonperf2-x86_64-mdboom-accelerate_DJBX33A_m-3.14.0a0-04d5e93 |
|-----------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| django_template | 40.4 ms                                                                     | 39.6 ms: 1.02x faster                                                       |
| genshi_xml      | 56.2 ms                                                                     | 57.9 ms: 1.03x slower                                                       |
| genshi_text     | 24.6 ms                                                                     | 26.1 ms: 1.06x slower                                                       |
| Geometric mean  | (ref)                                                                       | 1.02x slower                                                                |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                 | bm-20240826-pythonperf2-x86_64-python-fe85a8291d9aa11c9ce9-3.14.0a0-fe85a82 | bm-20240827-pythonperf2-x86_64-mdboom-accelerate_DJBX33A_m-3.14.0a0-04d5e93 |
|---------------------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_dna                 | 254 ms                                                                      | 233 ms: 1.09x faster                                                        |
| tomli_loads               | 2.58 sec                                                                    | 2.37 sec: 1.09x faster                                                      |
| regex_v8                  | 27.1 ms                                                                     | 25.7 ms: 1.06x faster                                                       |
| logging_format            | 7.09 us                                                                     | 6.84 us: 1.04x faster                                                       |
| comprehensions            | 17.5 us                                                                     | 17.0 us: 1.03x faster                                                       |
| asyncio_websockets        | 395 ms                                                                      | 385 ms: 1.03x faster                                                        |
| logging_simple            | 6.44 us                                                                     | 6.29 us: 1.02x faster                                                       |
| sqlglot_normalize         | 120 ms                                                                      | 118 ms: 1.02x faster                                                        |
| django_template           | 40.4 ms                                                                     | 39.6 ms: 1.02x faster                                                       |
| sqlglot_optimize          | 59.2 ms                                                                     | 58.1 ms: 1.02x faster                                                       |
| deepcopy_reduce           | 2.95 us                                                                     | 2.91 us: 1.02x faster                                                       |
| sqlglot_parse             | 1.43 ms                                                                     | 1.41 ms: 1.01x faster                                                       |
| float                     | 79.5 ms                                                                     | 78.4 ms: 1.01x faster                                                       |
| meteor_contest            | 128 ms                                                                      | 127 ms: 1.01x faster                                                        |
| async_tree_memoization_tg | 392 ms                                                                      | 387 ms: 1.01x faster                                                        |
| deepcopy                  | 291 us                                                                      | 287 us: 1.01x faster                                                        |
| json_loads                | 25.1 us                                                                     | 24.8 us: 1.01x faster                                                       |
| gc_traversal              | 4.43 ms                                                                     | 4.38 ms: 1.01x faster                                                       |
| thrift                    | 846 us                                                                      | 837 us: 1.01x faster                                                        |
| async_tree_memoization    | 401 ms                                                                      | 397 ms: 1.01x faster                                                        |
| sqlglot_transpile         | 1.80 ms                                                                     | 1.79 ms: 1.01x faster                                                       |
| scimark_monte_carlo       | 65.7 ms                                                                     | 65.1 ms: 1.01x faster                                                       |
| hexiom                    | 6.29 ms                                                                     | 6.23 ms: 1.01x faster                                                       |
| logging_silent            | 97.9 ns                                                                     | 97.3 ns: 1.01x faster                                                       |
| scimark_fft               | 304 ms                                                                      | 303 ms: 1.01x faster                                                        |
| spectral_norm             | 96.7 ms                                                                     | 97.0 ms: 1.00x slower                                                       |
| pidigits                  | 252 ms                                                                      | 253 ms: 1.00x slower                                                        |
| asyncio_tcp_ssl           | 1.57 sec                                                                    | 1.58 sec: 1.00x slower                                                      |
| regex_compile             | 141 ms                                                                      | 142 ms: 1.00x slower                                                        |
| sympy_sum                 | 150 ms                                                                      | 151 ms: 1.01x slower                                                        |
| python_startup            | 13.3 ms                                                                     | 13.4 ms: 1.01x slower                                                       |
| xml_etree_iterparse       | 100 ms                                                                      | 101 ms: 1.01x slower                                                        |
| docutils                  | 2.95 sec                                                                    | 2.97 sec: 1.01x slower                                                      |
| sympy_str                 | 290 ms                                                                      | 292 ms: 1.01x slower                                                        |
| python_startup_no_site    | 9.02 ms                                                                     | 9.08 ms: 1.01x slower                                                       |
| bpe_tokeniser             | 4.86 sec                                                                    | 4.89 sec: 1.01x slower                                                      |
| scimark_sparse_mat_mult   | 4.33 ms                                                                     | 4.37 ms: 1.01x slower                                                       |
| 2to3                      | 281 ms                                                                      | 283 ms: 1.01x slower                                                        |
| telco                     | 8.26 ms                                                                     | 8.33 ms: 1.01x slower                                                       |
| pickle_pure_python        | 316 us                                                                      | 318 us: 1.01x slower                                                        |
| pathlib                   | 15.8 ms                                                                     | 16.0 ms: 1.01x slower                                                       |
| coverage                  | 81.8 ms                                                                     | 82.6 ms: 1.01x slower                                                       |
| xml_etree_process         | 59.5 ms                                                                     | 60.1 ms: 1.01x slower                                                       |
| nbody                     | 85.9 ms                                                                     | 86.7 ms: 1.01x slower                                                       |
| tornado_http              | 116 ms                                                                      | 117 ms: 1.01x slower                                                        |
| deltablue                 | 3.35 ms                                                                     | 3.39 ms: 1.01x slower                                                       |
| pyflate                   | 471 ms                                                                      | 479 ms: 1.02x slower                                                        |
| deepcopy_memo             | 29.8 us                                                                     | 30.3 us: 1.02x slower                                                       |
| json_dumps                | 10.6 ms                                                                     | 10.8 ms: 1.02x slower                                                       |
| coroutines                | 21.3 ms                                                                     | 21.7 ms: 1.02x slower                                                       |
| go                        | 179 ms                                                                      | 183 ms: 1.02x slower                                                        |
| richards_super            | 55.7 ms                                                                     | 56.9 ms: 1.02x slower                                                       |
| xml_etree_generate        | 84.7 ms                                                                     | 86.7 ms: 1.02x slower                                                       |
| richards                  | 49.6 ms                                                                     | 51.0 ms: 1.03x slower                                                       |
| pycparser                 | 1.23 sec                                                                    | 1.26 sec: 1.03x slower                                                      |
| genshi_xml                | 56.2 ms                                                                     | 57.9 ms: 1.03x slower                                                       |
| generators                | 28.5 ms                                                                     | 29.5 ms: 1.03x slower                                                       |
| typing_runtime_protocols  | 170 us                                                                      | 176 us: 1.04x slower                                                        |
| create_gc_cycles          | 1.89 ms                                                                     | 1.98 ms: 1.05x slower                                                       |
| bench_mp_pool             | 4.48 ms                                                                     | 4.69 ms: 1.05x slower                                                       |
| genshi_text               | 24.6 ms                                                                     | 26.1 ms: 1.06x slower                                                       |
| scimark_sor               | 110 ms                                                                      | 119 ms: 1.08x slower                                                        |
| Geometric mean            | (ref)                                                                       | 1.00x slower                                                                |

Benchmark hidden because not significant (27): regex_effbot, async_tree_none, async_tree_cpu_io_mixed_tg, async_tree_none_tg, raytrace, async_tree_cpu_io_mixed, asyncio_tcp, fannkuch, html5lib, sympy_expand, mako, unpickle_pure_python, crypto_pyaes, async_tree_io_tg, pprint_pformat, json, mdp, async_generators, scimark_lu, pprint_safe_repr, chaos, sympy_integrate, nqueens, xml_etree_parse, bench_thread_pool, pylint, async_tree_io

# HPT report

- Reliability score: 62.47% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x
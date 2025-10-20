# Results vs. base

- fork: python
- ref: bedaea05987738c4c6b9
- machine: linux-x86_64
- commit hash: bedaea0
- commit date: 2025-10-19
- overall geometric mean: 1.005x slower
- HPT reliability: 99.85%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20251019-3.15.0a1+-bedaea0/bm-20251019-pythonperf2-x86_64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0.json | results/bm-20251019-3.15.0a1+-bedaea0-JIT/bm-20251019-pythonperf2-x86_64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 277 ms                                                                                                                  | 281 ms: 1.02x slower                                                                                                        |
| docutils       | 2.83 sec                                                                                                                | 2.89 sec: 1.02x slower                                                                                                      |
| html5lib       | 66.3 ms                                                                                                                 | 64.7 ms: 1.02x faster                                                                                                       |
| Geometric mean | (ref)                                                                                                                   | 1.00x slower                                                                                                                |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | results/bm-20251019-3.15.0a1+-bedaea0/bm-20251019-pythonperf2-x86_64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0.json | results/bm-20251019-3.15.0a1+-bedaea0-JIT/bm-20251019-pythonperf2-x86_64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0.json |
|---------------------------|:-----------------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------------:|
| asyncio_tcp_ssl           | 1.58 sec                                                                                                                | 1.58 sec: 1.00x slower                                                                                                      |
| asyncio_tcp               | 369 ms                                                                                                                  | 370 ms: 1.00x slower                                                                                                        |
| async_tree_memoization_tg | 328 ms                                                                                                                  | 331 ms: 1.01x slower                                                                                                        |
| async_tree_none_tg        | 268 ms                                                                                                                  | 272 ms: 1.01x slower                                                                                                        |
| async_tree_memoization    | 325 ms                                                                                                                  | 331 ms: 1.02x slower                                                                                                        |
| async_tree_none           | 269 ms                                                                                                                  | 274 ms: 1.02x slower                                                                                                        |
| coroutines                | 22.2 ms                                                                                                                 | 22.6 ms: 1.02x slower                                                                                                       |
| async_generators          | 423 ms                                                                                                                  | 447 ms: 1.06x slower                                                                                                        |
| Geometric mean            | (ref)                                                                                                                   | 1.01x slower                                                                                                                |

Benchmark hidden because not significant (5): asyncio_websockets, async_tree_cpu_io_mixed, async_tree_io, async_tree_cpu_io_mixed_tg, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20251019-3.15.0a1+-bedaea0/bm-20251019-pythonperf2-x86_64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0.json | results/bm-20251019-3.15.0a1+-bedaea0-JIT/bm-20251019-pythonperf2-x86_64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------------:|
| pidigits       | 254 ms                                                                                                                  | 255 ms: 1.00x slower                                                                                                        |
| float          | 68.0 ms                                                                                                                 | 69.5 ms: 1.02x slower                                                                                                       |
| Geometric mean | (ref)                                                                                                                   | 1.01x slower                                                                                                                |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20251019-3.15.0a1+-bedaea0/bm-20251019-pythonperf2-x86_64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0.json | results/bm-20251019-3.15.0a1+-bedaea0-JIT/bm-20251019-pythonperf2-x86_64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------------:|
| regex_effbot   | 3.41 ms                                                                                                                 | 3.40 ms: 1.00x faster                                                                                                       |
| regex_v8       | 23.9 ms                                                                                                                 | 24.0 ms: 1.00x slower                                                                                                       |
| regex_compile  | 131 ms                                                                                                                  | 133 ms: 1.01x slower                                                                                                        |
| regex_dna      | 218 ms                                                                                                                  | 223 ms: 1.03x slower                                                                                                        |
| Geometric mean | (ref)                                                                                                                   | 1.01x slower                                                                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20251019-3.15.0a1+-bedaea0/bm-20251019-pythonperf2-x86_64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0.json | results/bm-20251019-3.15.0a1+-bedaea0-JIT/bm-20251019-pythonperf2-x86_64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0.json |
|----------------------|:-----------------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------------:|
| xml_etree_generate   | 83.6 ms                                                                                                                 | 79.4 ms: 1.05x faster                                                                                                       |
| xml_etree_process    | 57.9 ms                                                                                                                 | 55.3 ms: 1.05x faster                                                                                                       |
| tomli_loads          | 1.97 sec                                                                                                                | 1.89 sec: 1.05x faster                                                                                                      |
| unpickle_pure_python | 203 us                                                                                                                  | 194 us: 1.04x faster                                                                                                        |
| unpickle             | 15.1 us                                                                                                                 | 14.6 us: 1.03x faster                                                                                                       |
| unpickle_list        | 4.98 us                                                                                                                 | 4.94 us: 1.01x faster                                                                                                       |
| pickle_dict          | 35.1 us                                                                                                                 | 34.8 us: 1.01x faster                                                                                                       |
| pickle_list          | 5.03 us                                                                                                                 | 4.99 us: 1.01x faster                                                                                                       |
| json_dumps           | 10.2 ms                                                                                                                 | 10.1 ms: 1.00x faster                                                                                                       |
| pickle_pure_python   | 324 us                                                                                                                  | 328 us: 1.01x slower                                                                                                        |
| xml_etree_iterparse  | 96.7 ms                                                                                                                 | 98.4 ms: 1.02x slower                                                                                                       |
| pickle               | 12.4 us                                                                                                                 | 12.8 us: 1.04x slower                                                                                                       |
| Geometric mean       | (ref)                                                                                                                   | 1.01x faster                                                                                                                |

Benchmark hidden because not significant (2): json_loads, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | results/bm-20251019-3.15.0a1+-bedaea0/bm-20251019-pythonperf2-x86_64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0.json | results/bm-20251019-3.15.0a1+-bedaea0-JIT/bm-20251019-pythonperf2-x86_64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0.json |
|------------------------|:-----------------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------------:|
| python_startup_no_site | 8.84 ms                                                                                                                 | 8.82 ms: 1.00x faster                                                                                                       |
| python_startup         | 15.4 ms                                                                                                                 | 15.4 ms: 1.00x faster                                                                                                       |
| Geometric mean         | (ref)                                                                                                                   | 1.00x faster                                                                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20251019-3.15.0a1+-bedaea0/bm-20251019-pythonperf2-x86_64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0.json | results/bm-20251019-3.15.0a1+-bedaea0-JIT/bm-20251019-pythonperf2-x86_64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0.json |
|-----------------|:-----------------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------------:|
| mako            | 10.7 ms                                                                                                                 | 9.82 ms: 1.08x faster                                                                                                       |
| django_template | 35.1 ms                                                                                                                 | 34.6 ms: 1.01x faster                                                                                                       |
| genshi_text     | 23.1 ms                                                                                                                 | 23.5 ms: 1.02x slower                                                                                                       |
| Geometric mean  | (ref)                                                                                                                   | 1.02x faster                                                                                                                |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                 | results/bm-20251019-3.15.0a1+-bedaea0/bm-20251019-pythonperf2-x86_64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0.json | results/bm-20251019-3.15.0a1+-bedaea0-JIT/bm-20251019-pythonperf2-x86_64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0.json |
|---------------------------|:-----------------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------------:|
| mako                      | 10.7 ms                                                                                                                 | 9.82 ms: 1.08x faster                                                                                                       |
| coverage                  | 83.2 ms                                                                                                                 | 77.8 ms: 1.07x faster                                                                                                       |
| xml_etree_generate        | 83.6 ms                                                                                                                 | 79.4 ms: 1.05x faster                                                                                                       |
| pprint_pformat            | 1.55 sec                                                                                                                | 1.48 sec: 1.05x faster                                                                                                      |
| xml_etree_process         | 57.9 ms                                                                                                                 | 55.3 ms: 1.05x faster                                                                                                       |
| tomli_loads               | 1.97 sec                                                                                                                | 1.89 sec: 1.05x faster                                                                                                      |
| unpickle_pure_python      | 203 us                                                                                                                  | 194 us: 1.04x faster                                                                                                        |
| k_core                    | 2.08 sec                                                                                                                | 2.01 sec: 1.04x faster                                                                                                      |
| pprint_safe_repr          | 758 ms                                                                                                                  | 730 ms: 1.04x faster                                                                                                        |
| unpickle                  | 15.1 us                                                                                                                 | 14.6 us: 1.03x faster                                                                                                       |
| connected_components      | 420 ms                                                                                                                  | 410 ms: 1.02x faster                                                                                                        |
| html5lib                  | 66.3 ms                                                                                                                 | 64.7 ms: 1.02x faster                                                                                                       |
| sqlite_synth              | 2.84 us                                                                                                                 | 2.77 us: 1.02x faster                                                                                                       |
| shortest_path             | 451 ms                                                                                                                  | 441 ms: 1.02x faster                                                                                                        |
| bpe_tokeniser             | 4.70 sec                                                                                                                | 4.60 sec: 1.02x faster                                                                                                      |
| nqueens                   | 94.0 ms                                                                                                                 | 92.4 ms: 1.02x faster                                                                                                       |
| django_template           | 35.1 ms                                                                                                                 | 34.6 ms: 1.01x faster                                                                                                       |
| scimark_fft               | 281 ms                                                                                                                  | 278 ms: 1.01x faster                                                                                                        |
| unpickle_list             | 4.98 us                                                                                                                 | 4.94 us: 1.01x faster                                                                                                       |
| pickle_dict               | 35.1 us                                                                                                                 | 34.8 us: 1.01x faster                                                                                                       |
| pickle_list               | 5.03 us                                                                                                                 | 4.99 us: 1.01x faster                                                                                                       |
| gc_traversal              | 6.52 ms                                                                                                                 | 6.49 ms: 1.00x faster                                                                                                       |
| regex_effbot              | 3.41 ms                                                                                                                 | 3.40 ms: 1.00x faster                                                                                                       |
| json_dumps                | 10.2 ms                                                                                                                 | 10.1 ms: 1.00x faster                                                                                                       |
| python_startup_no_site    | 8.84 ms                                                                                                                 | 8.82 ms: 1.00x faster                                                                                                       |
| python_startup            | 15.4 ms                                                                                                                 | 15.4 ms: 1.00x faster                                                                                                       |
| regex_v8                  | 23.9 ms                                                                                                                 | 24.0 ms: 1.00x slower                                                                                                       |
| asyncio_tcp_ssl           | 1.58 sec                                                                                                                | 1.58 sec: 1.00x slower                                                                                                      |
| pidigits                  | 254 ms                                                                                                                  | 255 ms: 1.00x slower                                                                                                        |
| spectral_norm             | 86.9 ms                                                                                                                 | 87.2 ms: 1.00x slower                                                                                                       |
| asyncio_tcp               | 369 ms                                                                                                                  | 370 ms: 1.00x slower                                                                                                        |
| deltablue                 | 3.14 ms                                                                                                                 | 3.16 ms: 1.00x slower                                                                                                       |
| deepcopy                  | 257 us                                                                                                                  | 259 us: 1.01x slower                                                                                                        |
| typing_runtime_protocols  | 166 us                                                                                                                  | 168 us: 1.01x slower                                                                                                        |
| meteor_contest            | 120 ms                                                                                                                  | 121 ms: 1.01x slower                                                                                                        |
| async_tree_memoization_tg | 328 ms                                                                                                                  | 331 ms: 1.01x slower                                                                                                        |
| deepcopy_memo             | 24.8 us                                                                                                                 | 25.1 us: 1.01x slower                                                                                                       |
| create_gc_cycles          | 2.82 ms                                                                                                                 | 2.85 ms: 1.01x slower                                                                                                       |
| sympy_integrate           | 22.0 ms                                                                                                                 | 22.2 ms: 1.01x slower                                                                                                       |
| subparsers                | 44.6 ms                                                                                                                 | 45.1 ms: 1.01x slower                                                                                                       |
| telco                     | 155 ms                                                                                                                  | 157 ms: 1.01x slower                                                                                                        |
| richards                  | 44.1 ms                                                                                                                 | 44.7 ms: 1.01x slower                                                                                                       |
| pickle_pure_python        | 324 us                                                                                                                  | 328 us: 1.01x slower                                                                                                        |
| sympy_sum                 | 148 ms                                                                                                                  | 150 ms: 1.01x slower                                                                                                        |
| async_tree_none_tg        | 268 ms                                                                                                                  | 272 ms: 1.01x slower                                                                                                        |
| regex_compile             | 131 ms                                                                                                                  | 133 ms: 1.01x slower                                                                                                        |
| many_optionals            | 1.22 ms                                                                                                                 | 1.24 ms: 1.02x slower                                                                                                       |
| genshi_text               | 23.1 ms                                                                                                                 | 23.5 ms: 1.02x slower                                                                                                       |
| sqlglot_v2_parse          | 1.28 ms                                                                                                                 | 1.30 ms: 1.02x slower                                                                                                       |
| 2to3                      | 277 ms                                                                                                                  | 281 ms: 1.02x slower                                                                                                        |
| async_tree_memoization    | 325 ms                                                                                                                  | 331 ms: 1.02x slower                                                                                                        |
| async_tree_none           | 269 ms                                                                                                                  | 274 ms: 1.02x slower                                                                                                        |
| dulwich_log               | 59.0 ms                                                                                                                 | 60.0 ms: 1.02x slower                                                                                                       |
| xml_etree_iterparse       | 96.7 ms                                                                                                                 | 98.4 ms: 1.02x slower                                                                                                       |
| coroutines                | 22.2 ms                                                                                                                 | 22.6 ms: 1.02x slower                                                                                                       |
| go                        | 116 ms                                                                                                                  | 118 ms: 1.02x slower                                                                                                        |
| fannkuch                  | 358 ms                                                                                                                  | 365 ms: 1.02x slower                                                                                                        |
| pathlib                   | 15.0 ms                                                                                                                 | 15.3 ms: 1.02x slower                                                                                                       |
| scimark_lu                | 92.7 ms                                                                                                                 | 94.6 ms: 1.02x slower                                                                                                       |
| docutils                  | 2.83 sec                                                                                                                | 2.89 sec: 1.02x slower                                                                                                      |
| sympy_str                 | 284 ms                                                                                                                  | 290 ms: 1.02x slower                                                                                                        |
| sqlglot_v2_transpile      | 1.66 ms                                                                                                                 | 1.69 ms: 1.02x slower                                                                                                       |
| float                     | 68.0 ms                                                                                                                 | 69.5 ms: 1.02x slower                                                                                                       |
| scimark_sor               | 101 ms                                                                                                                  | 104 ms: 1.02x slower                                                                                                        |
| chaos                     | 57.8 ms                                                                                                                 | 59.2 ms: 1.02x slower                                                                                                       |
| sympy_expand              | 485 ms                                                                                                                  | 497 ms: 1.02x slower                                                                                                        |
| regex_dna                 | 218 ms                                                                                                                  | 223 ms: 1.03x slower                                                                                                        |
| raytrace                  | 274 ms                                                                                                                  | 281 ms: 1.03x slower                                                                                                        |
| hexiom                    | 5.72 ms                                                                                                                 | 5.87 ms: 1.03x slower                                                                                                       |
| richards_super            | 50.4 ms                                                                                                                 | 51.8 ms: 1.03x slower                                                                                                       |
| mdp                       | 1.25 sec                                                                                                                | 1.29 sec: 1.03x slower                                                                                                      |
| sqlglot_v2_normalize      | 111 ms                                                                                                                  | 115 ms: 1.03x slower                                                                                                        |
| pickle                    | 12.4 us                                                                                                                 | 12.8 us: 1.04x slower                                                                                                       |
| sqlglot_v2_optimize       | 55.6 ms                                                                                                                 | 57.8 ms: 1.04x slower                                                                                                       |
| async_generators          | 423 ms                                                                                                                  | 447 ms: 1.06x slower                                                                                                        |
| scimark_monte_carlo       | 58.2 ms                                                                                                                 | 62.4 ms: 1.07x slower                                                                                                       |
| scimark_sparse_mat_mult   | 4.51 ms                                                                                                                 | 4.85 ms: 1.08x slower                                                                                                       |
| generators                | 28.4 ms                                                                                                                 | 30.6 ms: 1.08x slower                                                                                                       |
| comprehensions            | 16.0 us                                                                                                                 | 17.4 us: 1.09x slower                                                                                                       |
| unpack_sequence           | 43.2 ns                                                                                                                 | 52.3 ns: 1.21x slower                                                                                                       |
| Geometric mean            | (ref)                                                                                                                   | 1.01x slower                                                                                                                |

Benchmark hidden because not significant (23): logging_silent, asyncio_websockets, json, djangocms, genshi_xml, json_loads, thrift, xml_etree_parse, pycparser, async_tree_cpu_io_mixed, pyflate, deepcopy_reduce, crypto_pyaes, async_tree_io, nbody, logging_simple, async_tree_cpu_io_mixed_tg, sphinx, logging_format, pylint, async_tree_io_tg, bench_thread_pool, bench_mp_pool

- Geometric mean (including insignificant results): 1.005x slower

# HPT report

- Reliability score: 99.85% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.01x
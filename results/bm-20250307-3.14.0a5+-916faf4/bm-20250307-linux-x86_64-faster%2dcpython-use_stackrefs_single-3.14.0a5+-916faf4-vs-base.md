# Results vs. base

- fork: faster-cpython
- ref: use_stackrefs_single
- machine: linux-x86_64
- commit hash: 916faf4
- commit date: 2025-03-07
- overall geometric mean: 1.010x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250303-linux-x86_64-python-b3c18bfd828ba90b9c71-3.14.0a5+-b3c18bf | bm-20250307-linux-x86_64-faster%2dcpython-use_stackrefs_single-3.14.0a5+-916faf4 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 254 ms                                                                 | 256 ms: 1.01x slower                                                             |
| docutils       | 2.60 sec                                                               | 2.64 sec: 1.02x slower                                                           |
| sphinx         | 1.01 sec                                                               | 1.02 sec: 1.01x slower                                                           |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                                     |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20250303-linux-x86_64-python-b3c18bfd828ba90b9c71-3.14.0a5+-b3c18bf | bm-20250307-linux-x86_64-faster%2dcpython-use_stackrefs_single-3.14.0a5+-916faf4 |
|-------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| coroutines              | 24.0 ms                                                                | 24.1 ms: 1.00x slower                                                            |
| async_tree_cpu_io_mixed | 486 ms                                                                 | 489 ms: 1.01x slower                                                             |
| async_generators        | 393 ms                                                                 | 396 ms: 1.01x slower                                                             |
| async_tree_none         | 262 ms                                                                 | 267 ms: 1.02x slower                                                             |
| Geometric mean          | (ref)                                                                  | 1.01x slower                                                                     |

Benchmark hidden because not significant (7): asyncio_websockets, async_tree_memoization_tg, async_tree_cpu_io_mixed_tg, async_tree_memoization, async_tree_io_tg, async_tree_none_tg, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250303-linux-x86_64-python-b3c18bfd828ba90b9c71-3.14.0a5+-b3c18bf | bm-20250307-linux-x86_64-faster%2dcpython-use_stackrefs_single-3.14.0a5+-916faf4 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| pidigits       | 186 ms                                                                 | 188 ms: 1.01x slower                                                             |
| nbody          | 94.2 ms                                                                | 98.1 ms: 1.04x slower                                                            |
| Geometric mean | (ref)                                                                  | 1.02x slower                                                                     |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250303-linux-x86_64-python-b3c18bfd828ba90b9c71-3.14.0a5+-b3c18bf | bm-20250307-linux-x86_64-faster%2dcpython-use_stackrefs_single-3.14.0a5+-916faf4 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_v8       | 25.5 ms                                                                | 25.0 ms: 1.02x faster                                                            |
| regex_dna      | 221 ms                                                                 | 224 ms: 1.01x slower                                                             |
| regex_effbot   | 3.28 ms                                                                | 3.50 ms: 1.07x slower                                                            |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                                     |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250303-linux-x86_64-python-b3c18bfd828ba90b9c71-3.14.0a5+-b3c18bf | bm-20250307-linux-x86_64-faster%2dcpython-use_stackrefs_single-3.14.0a5+-916faf4 |
|----------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| tomli_loads          | 1.98 sec                                                               | 1.95 sec: 1.01x faster                                                           |
| json_loads           | 30.1 us                                                                | 29.9 us: 1.01x faster                                                            |
| unpickle_pure_python | 218 us                                                                 | 217 us: 1.00x faster                                                             |
| json_dumps           | 11.3 ms                                                                | 11.4 ms: 1.01x slower                                                            |
| pickle_pure_python   | 315 us                                                                 | 319 us: 1.01x slower                                                             |
| xml_etree_parse      | 148 ms                                                                 | 150 ms: 1.01x slower                                                             |
| Geometric mean       | (ref)                                                                  | 1.00x slower                                                                     |

Benchmark hidden because not significant (3): xml_etree_iterparse, xml_etree_process, xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250303-linux-x86_64-python-b3c18bfd828ba90b9c71-3.14.0a5+-b3c18bf | bm-20250307-linux-x86_64-faster%2dcpython-use_stackrefs_single-3.14.0a5+-916faf4 |
|------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup         | 13.0 ms                                                                | 13.1 ms: 1.01x slower                                                            |
| python_startup_no_site | 7.12 ms                                                                | 7.19 ms: 1.01x slower                                                            |
| Geometric mean         | (ref)                                                                  | 1.01x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20250303-linux-x86_64-python-b3c18bfd828ba90b9c71-3.14.0a5+-b3c18bf | bm-20250307-linux-x86_64-faster%2dcpython-use_stackrefs_single-3.14.0a5+-916faf4 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| genshi_text    | 21.5 ms                                                                | 21.2 ms: 1.02x faster                                                            |
| genshi_xml     | 49.4 ms                                                                | 49.6 ms: 1.00x slower                                                            |
| mako           | 11.3 ms                                                                | 11.8 ms: 1.04x slower                                                            |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                                     |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                | bm-20250303-linux-x86_64-python-b3c18bfd828ba90b9c71-3.14.0a5+-b3c18bf | bm-20250307-linux-x86_64-faster%2dcpython-use_stackrefs_single-3.14.0a5+-916faf4 |
|--------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| logging_silent           | 102 ns                                                                 | 95.0 ns: 1.07x faster                                                            |
| gc_traversal             | 5.00 ms                                                                | 4.87 ms: 1.03x faster                                                            |
| deepcopy_memo            | 29.7 us                                                                | 29.0 us: 1.02x faster                                                            |
| regex_v8                 | 25.5 ms                                                                | 25.0 ms: 1.02x faster                                                            |
| mdp                      | 2.51 sec                                                               | 2.46 sec: 1.02x faster                                                           |
| richards_super           | 50.3 ms                                                                | 49.5 ms: 1.02x faster                                                            |
| genshi_text              | 21.5 ms                                                                | 21.2 ms: 1.02x faster                                                            |
| richards                 | 43.8 ms                                                                | 43.2 ms: 1.01x faster                                                            |
| tomli_loads              | 1.98 sec                                                               | 1.95 sec: 1.01x faster                                                           |
| scimark_sor              | 118 ms                                                                 | 117 ms: 1.01x faster                                                             |
| go                       | 115 ms                                                                 | 114 ms: 1.01x faster                                                             |
| many_optionals           | 938 us                                                                 | 930 us: 1.01x faster                                                             |
| telco                    | 7.88 ms                                                                | 7.82 ms: 1.01x faster                                                            |
| json_loads               | 30.1 us                                                                | 29.9 us: 1.01x faster                                                            |
| generators               | 28.4 ms                                                                | 28.2 ms: 1.01x faster                                                            |
| unpickle_pure_python     | 218 us                                                                 | 217 us: 1.00x faster                                                             |
| bench_thread_pool        | 870 us                                                                 | 871 us: 1.00x slower                                                             |
| sqlglot_optimize         | 52.5 ms                                                                | 52.6 ms: 1.00x slower                                                            |
| coroutines               | 24.0 ms                                                                | 24.1 ms: 1.00x slower                                                            |
| genshi_xml               | 49.4 ms                                                                | 49.6 ms: 1.00x slower                                                            |
| raytrace                 | 268 ms                                                                 | 269 ms: 1.00x slower                                                             |
| bench_mp_pool            | 81.8 ms                                                                | 82.2 ms: 1.01x slower                                                            |
| create_gc_cycles         | 2.44 ms                                                                | 2.46 ms: 1.01x slower                                                            |
| json_dumps               | 11.3 ms                                                                | 11.4 ms: 1.01x slower                                                            |
| async_tree_cpu_io_mixed  | 486 ms                                                                 | 489 ms: 1.01x slower                                                             |
| deepcopy_reduce          | 2.65 us                                                                | 2.67 us: 1.01x slower                                                            |
| sympy_str                | 265 ms                                                                 | 267 ms: 1.01x slower                                                             |
| logging_simple           | 5.47 us                                                                | 5.52 us: 1.01x slower                                                            |
| dulwich_log              | 64.8 ms                                                                | 65.3 ms: 1.01x slower                                                            |
| python_startup           | 13.0 ms                                                                | 13.1 ms: 1.01x slower                                                            |
| thrift                   | 764 us                                                                 | 770 us: 1.01x slower                                                             |
| 2to3                     | 254 ms                                                                 | 256 ms: 1.01x slower                                                             |
| sqlite_synth             | 2.76 us                                                                | 2.78 us: 1.01x slower                                                            |
| python_startup_no_site   | 7.12 ms                                                                | 7.19 ms: 1.01x slower                                                            |
| async_generators         | 393 ms                                                                 | 396 ms: 1.01x slower                                                             |
| hexiom                   | 6.09 ms                                                                | 6.15 ms: 1.01x slower                                                            |
| sympy_sum                | 147 ms                                                                 | 149 ms: 1.01x slower                                                             |
| sympy_expand             | 452 ms                                                                 | 457 ms: 1.01x slower                                                             |
| scimark_monte_carlo      | 67.0 ms                                                                | 67.8 ms: 1.01x slower                                                            |
| pickle_pure_python       | 315 us                                                                 | 319 us: 1.01x slower                                                             |
| sphinx                   | 1.01 sec                                                               | 1.02 sec: 1.01x slower                                                           |
| pidigits                 | 186 ms                                                                 | 188 ms: 1.01x slower                                                             |
| sympy_integrate          | 19.6 ms                                                                | 19.8 ms: 1.01x slower                                                            |
| regex_dna                | 221 ms                                                                 | 224 ms: 1.01x slower                                                             |
| sqlalchemy_imperative    | 16.3 ms                                                                | 16.5 ms: 1.01x slower                                                            |
| bpe_tokeniser            | 4.50 sec                                                               | 4.56 sec: 1.01x slower                                                           |
| json                     | 5.29 ms                                                                | 5.35 ms: 1.01x slower                                                            |
| xml_etree_parse          | 148 ms                                                                 | 150 ms: 1.01x slower                                                             |
| sqlalchemy_declarative   | 128 ms                                                                 | 129 ms: 1.01x slower                                                             |
| pathlib                  | 16.8 ms                                                                | 17.1 ms: 1.01x slower                                                            |
| meteor_contest           | 105 ms                                                                 | 106 ms: 1.01x slower                                                             |
| pprint_pformat           | 1.45 sec                                                               | 1.47 sec: 1.01x slower                                                           |
| docutils                 | 2.60 sec                                                               | 2.64 sec: 1.02x slower                                                           |
| sqlglot_transpile        | 1.56 ms                                                                | 1.58 ms: 1.02x slower                                                            |
| pprint_safe_repr         | 716 ms                                                                 | 728 ms: 1.02x slower                                                             |
| logging_format           | 6.00 us                                                                | 6.11 us: 1.02x slower                                                            |
| async_tree_none          | 262 ms                                                                 | 267 ms: 1.02x slower                                                             |
| scimark_lu               | 115 ms                                                                 | 117 ms: 1.02x slower                                                             |
| sqlglot_parse            | 1.25 ms                                                                | 1.28 ms: 1.02x slower                                                            |
| scimark_sparse_mat_mult  | 4.66 ms                                                                | 4.76 ms: 1.02x slower                                                            |
| chaos                    | 58.4 ms                                                                | 59.7 ms: 1.02x slower                                                            |
| scimark_fft              | 339 ms                                                                 | 347 ms: 1.02x slower                                                             |
| nqueens                  | 81.8 ms                                                                | 83.8 ms: 1.02x slower                                                            |
| deepcopy                 | 253 us                                                                 | 259 us: 1.02x slower                                                             |
| comprehensions           | 16.2 us                                                                | 16.6 us: 1.03x slower                                                            |
| typing_runtime_protocols | 158 us                                                                 | 163 us: 1.03x slower                                                             |
| shortest_path            | 473 ms                                                                 | 488 ms: 1.03x slower                                                             |
| fannkuch                 | 398 ms                                                                 | 412 ms: 1.04x slower                                                             |
| crypto_pyaes             | 72.7 ms                                                                | 75.4 ms: 1.04x slower                                                            |
| nbody                    | 94.2 ms                                                                | 98.1 ms: 1.04x slower                                                            |
| mako                     | 11.3 ms                                                                | 11.8 ms: 1.04x slower                                                            |
| connected_components     | 436 ms                                                                 | 455 ms: 1.04x slower                                                             |
| pycparser                | 1.12 sec                                                               | 1.19 sec: 1.06x slower                                                           |
| spectral_norm            | 93.1 ms                                                                | 98.8 ms: 1.06x slower                                                            |
| regex_effbot             | 3.28 ms                                                                | 3.50 ms: 1.07x slower                                                            |
| coverage                 | 84.4 ms                                                                | 92.5 ms: 1.10x slower                                                            |
| Geometric mean           | (ref)                                                                  | 1.01x slower                                                                     |

Benchmark hidden because not significant (20): xml_etree_iterparse, float, django_template, deltablue, asyncio_websockets, xml_etree_process, regex_compile, async_tree_memoization_tg, pyflate, sqlglot_normalize, xml_etree_generate, html5lib, async_tree_cpu_io_mixed_tg, subparsers, async_tree_memoization, async_tree_io_tg, async_tree_none_tg, async_tree_io, pylint, k_core

- Geometric mean (including insignificant results): 1.010x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x
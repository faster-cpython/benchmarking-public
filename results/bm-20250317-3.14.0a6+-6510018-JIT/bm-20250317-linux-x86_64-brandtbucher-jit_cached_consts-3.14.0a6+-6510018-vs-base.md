# Results vs. base

- fork: brandtbucher
- ref: jit_cached_consts
- machine: linux-x86_64
- commit hash: 6510018
- commit date: 2025-03-17
- overall geometric mean: 1.010x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250317-linux-x86_64-python-fd545d735d5f9c048f99-3.14.0a6+-fd545d7 | bm-20250317-linux-x86_64-brandtbucher-jit_cached_consts-3.14.0a6+-6510018 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 263 ms                                                                 | 261 ms: 1.01x faster                                                      |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                              |

Benchmark hidden because not significant (3): docutils, html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250317-linux-x86_64-python-fd545d735d5f9c048f99-3.14.0a6+-fd545d7 | bm-20250317-linux-x86_64-brandtbucher-jit_cached_consts-3.14.0a6+-6510018 |
|----------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_none            | 260 ms                                                                 | 255 ms: 1.02x faster                                                      |
| async_tree_memoization     | 319 ms                                                                 | 314 ms: 1.02x faster                                                      |
| async_tree_cpu_io_mixed_tg | 481 ms                                                                 | 475 ms: 1.01x faster                                                      |
| async_tree_cpu_io_mixed    | 497 ms                                                                 | 490 ms: 1.01x faster                                                      |
| async_tree_none_tg         | 251 ms                                                                 | 248 ms: 1.01x faster                                                      |
| async_generators           | 417 ms                                                                 | 415 ms: 1.00x faster                                                      |
| coroutines                 | 23.7 ms                                                                | 24.0 ms: 1.01x slower                                                     |
| Geometric mean             | (ref)                                                                  | 1.01x faster                                                              |

Benchmark hidden because not significant (4): async_tree_memoization_tg, async_tree_io, async_tree_io_tg, asyncio_websockets

Benchmarks with tag 'math':
===========================

Benchmark hidden because not significant (3): float, pidigits, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250317-linux-x86_64-python-fd545d735d5f9c048f99-3.14.0a6+-fd545d7 | bm-20250317-linux-x86_64-brandtbucher-jit_cached_consts-3.14.0a6+-6510018 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_v8       | 23.9 ms                                                                | 23.2 ms: 1.03x faster                                                     |
| regex_dna      | 225 ms                                                                 | 220 ms: 1.02x faster                                                      |
| regex_compile  | 128 ms                                                                 | 126 ms: 1.01x faster                                                      |
| Geometric mean | (ref)                                                                  | 1.02x faster                                                              |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250317-linux-x86_64-python-fd545d735d5f9c048f99-3.14.0a6+-fd545d7 | bm-20250317-linux-x86_64-brandtbucher-jit_cached_consts-3.14.0a6+-6510018 |
|----------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| pickle_pure_python   | 326 us                                                                 | 320 us: 1.02x faster                                                      |
| xml_etree_parse      | 142 ms                                                                 | 139 ms: 1.02x faster                                                      |
| unpickle_pure_python | 216 us                                                                 | 212 us: 1.02x faster                                                      |
| xml_etree_generate   | 80.4 ms                                                                | 79.2 ms: 1.02x faster                                                     |
| json_loads           | 30.2 us                                                                | 29.8 us: 1.01x faster                                                     |
| xml_etree_process    | 56.2 ms                                                                | 55.5 ms: 1.01x faster                                                     |
| xml_etree_iterparse  | 98.7 ms                                                                | 97.6 ms: 1.01x faster                                                     |
| json_dumps           | 11.8 ms                                                                | 11.6 ms: 1.01x faster                                                     |
| Geometric mean       | (ref)                                                                  | 1.01x faster                                                              |

Benchmark hidden because not significant (1): tomli_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250317-linux-x86_64-python-fd545d735d5f9c048f99-3.14.0a6+-fd545d7 | bm-20250317-linux-x86_64-brandtbucher-jit_cached_consts-3.14.0a6+-6510018 |
|------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup_no_site | 8.22 ms                                                                | 8.20 ms: 1.00x faster                                                     |
| python_startup         | 13.1 ms                                                                | 13.1 ms: 1.00x faster                                                     |
| Geometric mean         | (ref)                                                                  | 1.00x faster                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250317-linux-x86_64-python-fd545d735d5f9c048f99-3.14.0a6+-fd545d7 | bm-20250317-linux-x86_64-brandtbucher-jit_cached_consts-3.14.0a6+-6510018 |
|-----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| genshi_text     | 21.6 ms                                                                | 21.2 ms: 1.02x faster                                                     |
| genshi_xml      | 51.0 ms                                                                | 50.3 ms: 1.01x faster                                                     |
| django_template | 31.9 ms                                                                | 31.6 ms: 1.01x faster                                                     |
| Geometric mean  | (ref)                                                                  | 1.01x faster                                                              |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                  | bm-20250317-linux-x86_64-python-fd545d735d5f9c048f99-3.14.0a6+-fd545d7 | bm-20250317-linux-x86_64-brandtbucher-jit_cached_consts-3.14.0a6+-6510018 |
|----------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| deepcopy_memo              | 30.0 us                                                                | 28.5 us: 1.05x faster                                                     |
| scimark_sor                | 121 ms                                                                 | 116 ms: 1.04x faster                                                      |
| scimark_lu                 | 121 ms                                                                 | 117 ms: 1.04x faster                                                      |
| deltablue                  | 3.08 ms                                                                | 2.97 ms: 1.03x faster                                                     |
| logging_silent             | 100 ns                                                                 | 96.7 ns: 1.03x faster                                                     |
| regex_v8                   | 23.9 ms                                                                | 23.2 ms: 1.03x faster                                                     |
| scimark_monte_carlo        | 68.9 ms                                                                | 66.9 ms: 1.03x faster                                                     |
| richards_super             | 40.8 ms                                                                | 39.7 ms: 1.03x faster                                                     |
| richards                   | 35.6 ms                                                                | 34.6 ms: 1.03x faster                                                     |
| subparsers                 | 21.1 ms                                                                | 20.6 ms: 1.02x faster                                                     |
| regex_dna                  | 225 ms                                                                 | 220 ms: 1.02x faster                                                      |
| pickle_pure_python         | 326 us                                                                 | 320 us: 1.02x faster                                                      |
| logging_format             | 6.17 us                                                                | 6.05 us: 1.02x faster                                                     |
| shortest_path              | 498 ms                                                                 | 489 ms: 1.02x faster                                                      |
| xml_etree_parse            | 142 ms                                                                 | 139 ms: 1.02x faster                                                      |
| chaos                      | 60.2 ms                                                                | 59.0 ms: 1.02x faster                                                     |
| logging_simple             | 5.59 us                                                                | 5.48 us: 1.02x faster                                                     |
| mdp                        | 2.50 sec                                                               | 2.46 sec: 1.02x faster                                                    |
| sqlite_synth               | 2.75 us                                                                | 2.70 us: 1.02x faster                                                     |
| hexiom                     | 6.90 ms                                                                | 6.77 ms: 1.02x faster                                                     |
| thrift                     | 779 us                                                                 | 765 us: 1.02x faster                                                      |
| genshi_text                | 21.6 ms                                                                | 21.2 ms: 1.02x faster                                                     |
| pathlib                    | 16.7 ms                                                                | 16.4 ms: 1.02x faster                                                     |
| sqlglot_v2_parse           | 1.30 ms                                                                | 1.27 ms: 1.02x faster                                                     |
| raytrace                   | 270 ms                                                                 | 265 ms: 1.02x faster                                                      |
| nqueens                    | 85.9 ms                                                                | 84.4 ms: 1.02x faster                                                     |
| async_tree_none            | 260 ms                                                                 | 255 ms: 1.02x faster                                                      |
| sqlglot_v2_normalize       | 109 ms                                                                 | 107 ms: 1.02x faster                                                      |
| generators                 | 28.3 ms                                                                | 27.9 ms: 1.02x faster                                                     |
| unpickle_pure_python       | 216 us                                                                 | 212 us: 1.02x faster                                                      |
| xml_etree_generate         | 80.4 ms                                                                | 79.2 ms: 1.02x faster                                                     |
| async_tree_memoization     | 319 ms                                                                 | 314 ms: 1.02x faster                                                      |
| deepcopy_reduce            | 2.71 us                                                                | 2.67 us: 1.02x faster                                                     |
| async_tree_cpu_io_mixed_tg | 481 ms                                                                 | 475 ms: 1.01x faster                                                      |
| genshi_xml                 | 51.0 ms                                                                | 50.3 ms: 1.01x faster                                                     |
| pprint_safe_repr           | 755 ms                                                                 | 745 ms: 1.01x faster                                                      |
| async_tree_cpu_io_mixed    | 497 ms                                                                 | 490 ms: 1.01x faster                                                      |
| json_loads                 | 30.2 us                                                                | 29.8 us: 1.01x faster                                                     |
| xml_etree_process          | 56.2 ms                                                                | 55.5 ms: 1.01x faster                                                     |
| regex_compile              | 128 ms                                                                 | 126 ms: 1.01x faster                                                      |
| deepcopy                   | 257 us                                                                 | 254 us: 1.01x faster                                                      |
| sqlalchemy_imperative      | 17.1 ms                                                                | 16.9 ms: 1.01x faster                                                     |
| crypto_pyaes               | 79.0 ms                                                                | 78.1 ms: 1.01x faster                                                     |
| xml_etree_iterparse        | 98.7 ms                                                                | 97.6 ms: 1.01x faster                                                     |
| typing_runtime_protocols   | 170 us                                                                 | 168 us: 1.01x faster                                                      |
| bench_thread_pool          | 883 us                                                                 | 874 us: 1.01x faster                                                      |
| sqlglot_v2_optimize        | 54.2 ms                                                                | 53.6 ms: 1.01x faster                                                     |
| json_dumps                 | 11.8 ms                                                                | 11.6 ms: 1.01x faster                                                     |
| spectral_norm              | 95.2 ms                                                                | 94.3 ms: 1.01x faster                                                     |
| sqlglot_v2_transpile       | 1.61 ms                                                                | 1.60 ms: 1.01x faster                                                     |
| scimark_sparse_mat_mult    | 4.76 ms                                                                | 4.71 ms: 1.01x faster                                                     |
| async_tree_none_tg         | 251 ms                                                                 | 248 ms: 1.01x faster                                                      |
| telco                      | 7.87 ms                                                                | 7.80 ms: 1.01x faster                                                     |
| connected_components       | 459 ms                                                                 | 456 ms: 1.01x faster                                                      |
| json                       | 5.36 ms                                                                | 5.32 ms: 1.01x faster                                                     |
| 2to3                       | 263 ms                                                                 | 261 ms: 1.01x faster                                                      |
| sympy_expand               | 474 ms                                                                 | 471 ms: 1.01x faster                                                      |
| django_template            | 31.9 ms                                                                | 31.6 ms: 1.01x faster                                                     |
| sympy_integrate            | 20.3 ms                                                                | 20.1 ms: 1.01x faster                                                     |
| bpe_tokeniser              | 4.61 sec                                                               | 4.59 sec: 1.01x faster                                                    |
| sqlalchemy_declarative     | 133 ms                                                                 | 132 ms: 1.00x faster                                                      |
| async_generators           | 417 ms                                                                 | 415 ms: 1.00x faster                                                      |
| python_startup_no_site     | 8.22 ms                                                                | 8.20 ms: 1.00x faster                                                     |
| python_startup             | 13.1 ms                                                                | 13.1 ms: 1.00x faster                                                     |
| pyflate                    | 447 ms                                                                 | 449 ms: 1.00x slower                                                      |
| scimark_fft                | 308 ms                                                                 | 310 ms: 1.01x slower                                                      |
| gc_traversal               | 4.85 ms                                                                | 4.91 ms: 1.01x slower                                                     |
| coroutines                 | 23.7 ms                                                                | 24.0 ms: 1.01x slower                                                     |
| Geometric mean             | (ref)                                                                  | 1.01x faster                                                              |

Benchmark hidden because not significant (28): async_tree_memoization_tg, pycparser, async_tree_io, async_tree_io_tg, sphinx, meteor_contest, k_core, go, float, pylint, many_optionals, bench_mp_pool, dulwich_log, comprehensions, sympy_sum, tomli_loads, asyncio_websockets, regex_effbot, coverage, sympy_str, create_gc_cycles, mako, pidigits, docutils, html5lib, pprint_pformat, nbody, fannkuch

- Geometric mean (including insignificant results): 1.010x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x
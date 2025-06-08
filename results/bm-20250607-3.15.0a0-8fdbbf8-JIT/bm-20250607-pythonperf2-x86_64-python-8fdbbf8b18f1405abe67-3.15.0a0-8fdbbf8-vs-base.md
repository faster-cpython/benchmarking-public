# Results vs. base

- fork: python
- ref: 8fdbbf8b18f1405abe67
- machine: linux-x86_64
- commit hash: 8fdbbf8
- commit date: 2025-06-07
- overall geometric mean: 1.005x faster
- HPT reliability: 99.98%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20250607-3.15.0a0-8fdbbf8/bm-20250607-pythonperf2-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8.json | results/bm-20250607-3.15.0a0-8fdbbf8-JIT/bm-20250607-pythonperf2-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8.json |
|----------------|:---------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 313 ms                                                                                                                | 320 ms: 1.02x slower                                                                                                      |
| docutils       | 3.10 sec                                                                                                              | 3.14 sec: 1.01x slower                                                                                                    |
| html5lib       | 71.7 ms                                                                                                               | 70.7 ms: 1.01x faster                                                                                                     |
| sphinx         | 1.20 sec                                                                                                              | 1.22 sec: 1.01x slower                                                                                                    |
| Geometric mean | (ref)                                                                                                                 | 1.01x slower                                                                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | results/bm-20250607-3.15.0a0-8fdbbf8/bm-20250607-pythonperf2-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8.json | results/bm-20250607-3.15.0a0-8fdbbf8-JIT/bm-20250607-pythonperf2-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8.json |
|----------------------------|:---------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| coroutines                 | 24.4 ms                                                                                                               | 24.0 ms: 1.02x faster                                                                                                     |
| async_tree_none_tg         | 298 ms                                                                                                                | 299 ms: 1.00x slower                                                                                                      |
| asyncio_tcp_ssl            | 1.59 sec                                                                                                              | 1.59 sec: 1.00x slower                                                                                                    |
| asyncio_tcp                | 373 ms                                                                                                                | 375 ms: 1.01x slower                                                                                                      |
| async_tree_memoization     | 359 ms                                                                                                                | 364 ms: 1.01x slower                                                                                                      |
| async_tree_none            | 309 ms                                                                                                                | 313 ms: 1.01x slower                                                                                                      |
| asyncio_websockets         | 382 ms                                                                                                                | 388 ms: 1.02x slower                                                                                                      |
| async_tree_cpu_io_mixed_tg | 649 ms                                                                                                                | 675 ms: 1.04x slower                                                                                                      |
| async_tree_cpu_io_mixed    | 646 ms                                                                                                                | 672 ms: 1.04x slower                                                                                                      |
| async_generators           | 445 ms                                                                                                                | 475 ms: 1.07x slower                                                                                                      |
| Geometric mean             | (ref)                                                                                                                 | 1.01x slower                                                                                                              |

Benchmark hidden because not significant (3): async_tree_io_tg, async_tree_memoization_tg, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20250607-3.15.0a0-8fdbbf8/bm-20250607-pythonperf2-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8.json | results/bm-20250607-3.15.0a0-8fdbbf8-JIT/bm-20250607-pythonperf2-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8.json |
|----------------|:---------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| float          | 80.7 ms                                                                                                               | 72.3 ms: 1.12x faster                                                                                                     |
| pidigits       | 253 ms                                                                                                                | 254 ms: 1.00x slower                                                                                                      |
| nbody          | 100 ms                                                                                                                | 108 ms: 1.08x slower                                                                                                      |
| Geometric mean | (ref)                                                                                                                 | 1.01x faster                                                                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20250607-3.15.0a0-8fdbbf8/bm-20250607-pythonperf2-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8.json | results/bm-20250607-3.15.0a0-8fdbbf8-JIT/bm-20250607-pythonperf2-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8.json |
|----------------|:---------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| regex_compile  | 154 ms                                                                                                                | 156 ms: 1.01x slower                                                                                                      |
| Geometric mean | (ref)                                                                                                                 | 1.00x slower                                                                                                              |

Benchmark hidden because not significant (3): regex_dna, regex_effbot, regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20250607-3.15.0a0-8fdbbf8/bm-20250607-pythonperf2-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8.json | results/bm-20250607-3.15.0a0-8fdbbf8-JIT/bm-20250607-pythonperf2-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8.json |
|----------------------|:---------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| unpickle_pure_python | 244 us                                                                                                                | 238 us: 1.03x faster                                                                                                      |
| pickle_list          | 6.00 us                                                                                                               | 5.90 us: 1.02x faster                                                                                                     |
| tomli_loads          | 2.37 sec                                                                                                              | 2.33 sec: 1.01x faster                                                                                                    |
| json_loads           | 29.6 us                                                                                                               | 29.2 us: 1.01x faster                                                                                                     |
| xml_etree_process    | 72.1 ms                                                                                                               | 71.4 ms: 1.01x faster                                                                                                     |
| pickle_pure_python   | 384 us                                                                                                                | 385 us: 1.00x slower                                                                                                      |
| unpickle_list        | 5.56 us                                                                                                               | 5.58 us: 1.00x slower                                                                                                     |
| xml_etree_iterparse  | 115 ms                                                                                                                | 115 ms: 1.00x slower                                                                                                      |
| pickle_dict          | 35.5 us                                                                                                               | 36.1 us: 1.02x slower                                                                                                     |
| pickle               | 14.4 us                                                                                                               | 14.7 us: 1.02x slower                                                                                                     |
| json_dumps           | 13.9 ms                                                                                                               | 14.5 ms: 1.04x slower                                                                                                     |
| xml_etree_parse      | 163 ms                                                                                                                | 170 ms: 1.04x slower                                                                                                      |
| Geometric mean       | (ref)                                                                                                                 | 1.00x slower                                                                                                              |

Benchmark hidden because not significant (2): xml_etree_generate, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | results/bm-20250607-3.15.0a0-8fdbbf8/bm-20250607-pythonperf2-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8.json | results/bm-20250607-3.15.0a0-8fdbbf8-JIT/bm-20250607-pythonperf2-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8.json |
|------------------------|:---------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| python_startup         | 16.4 ms                                                                                                               | 16.5 ms: 1.00x slower                                                                                                     |
| python_startup_no_site | 9.39 ms                                                                                                               | 9.43 ms: 1.00x slower                                                                                                     |
| Geometric mean         | (ref)                                                                                                                 | 1.00x slower                                                                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20250607-3.15.0a0-8fdbbf8/bm-20250607-pythonperf2-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8.json | results/bm-20250607-3.15.0a0-8fdbbf8-JIT/bm-20250607-pythonperf2-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8.json |
|-----------------|:---------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| mako            | 13.0 ms                                                                                                               | 13.4 ms: 1.03x slower                                                                                                     |
| django_template | 41.6 ms                                                                                                               | 43.0 ms: 1.03x slower                                                                                                     |
| genshi_text     | 27.5 ms                                                                                                               | 28.9 ms: 1.05x slower                                                                                                     |
| genshi_xml      | 60.0 ms                                                                                                               | 64.1 ms: 1.07x slower                                                                                                     |
| Geometric mean  | (ref)                                                                                                                 | 1.05x slower                                                                                                              |

All benchmarks:
===============

| Benchmark                  | results/bm-20250607-3.15.0a0-8fdbbf8/bm-20250607-pythonperf2-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8.json | results/bm-20250607-3.15.0a0-8fdbbf8-JIT/bm-20250607-pythonperf2-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8.json |
|----------------------------|:---------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| richards                   | 53.5 ms                                                                                                               | 41.1 ms: 1.30x faster                                                                                                     |
| richards_super             | 60.5 ms                                                                                                               | 48.6 ms: 1.25x faster                                                                                                     |
| float                      | 80.7 ms                                                                                                               | 72.3 ms: 1.12x faster                                                                                                     |
| gc_traversal               | 5.94 ms                                                                                                               | 5.59 ms: 1.06x faster                                                                                                     |
| deltablue                  | 3.50 ms                                                                                                               | 3.34 ms: 1.05x faster                                                                                                     |
| deepcopy_memo              | 32.8 us                                                                                                               | 31.5 us: 1.04x faster                                                                                                     |
| k_core                     | 2.17 sec                                                                                                              | 2.09 sec: 1.04x faster                                                                                                    |
| unpickle_pure_python       | 244 us                                                                                                                | 238 us: 1.03x faster                                                                                                      |
| scimark_sparse_mat_mult    | 6.50 ms                                                                                                               | 6.34 ms: 1.02x faster                                                                                                     |
| pyflate                    | 477 ms                                                                                                                | 466 ms: 1.02x faster                                                                                                      |
| scimark_lu                 | 121 ms                                                                                                                | 119 ms: 1.02x faster                                                                                                      |
| coroutines                 | 24.4 ms                                                                                                               | 24.0 ms: 1.02x faster                                                                                                     |
| pickle_list                | 6.00 us                                                                                                               | 5.90 us: 1.02x faster                                                                                                     |
| shortest_path              | 461 ms                                                                                                                | 454 ms: 1.02x faster                                                                                                      |
| sqlite_synth               | 3.40 us                                                                                                               | 3.35 us: 1.01x faster                                                                                                     |
| html5lib                   | 71.7 ms                                                                                                               | 70.7 ms: 1.01x faster                                                                                                     |
| tomli_loads                | 2.37 sec                                                                                                              | 2.33 sec: 1.01x faster                                                                                                    |
| pycparser                  | 1.35 sec                                                                                                              | 1.33 sec: 1.01x faster                                                                                                    |
| json_loads                 | 29.6 us                                                                                                               | 29.2 us: 1.01x faster                                                                                                     |
| deepcopy_reduce            | 3.58 us                                                                                                               | 3.53 us: 1.01x faster                                                                                                     |
| connected_components       | 431 ms                                                                                                                | 427 ms: 1.01x faster                                                                                                      |
| pprint_pformat             | 2.12 sec                                                                                                              | 2.10 sec: 1.01x faster                                                                                                    |
| xml_etree_process          | 72.1 ms                                                                                                               | 71.4 ms: 1.01x faster                                                                                                     |
| create_gc_cycles           | 2.93 ms                                                                                                               | 2.92 ms: 1.00x faster                                                                                                     |
| pidigits                   | 253 ms                                                                                                                | 254 ms: 1.00x slower                                                                                                      |
| scimark_sor                | 129 ms                                                                                                                | 129 ms: 1.00x slower                                                                                                      |
| scimark_fft                | 391 ms                                                                                                                | 392 ms: 1.00x slower                                                                                                      |
| pickle_pure_python         | 384 us                                                                                                                | 385 us: 1.00x slower                                                                                                      |
| python_startup             | 16.4 ms                                                                                                               | 16.5 ms: 1.00x slower                                                                                                     |
| python_startup_no_site     | 9.39 ms                                                                                                               | 9.43 ms: 1.00x slower                                                                                                     |
| unpickle_list              | 5.56 us                                                                                                               | 5.58 us: 1.00x slower                                                                                                     |
| async_tree_none_tg         | 298 ms                                                                                                                | 299 ms: 1.00x slower                                                                                                      |
| xml_etree_iterparse        | 115 ms                                                                                                                | 115 ms: 1.00x slower                                                                                                      |
| asyncio_tcp_ssl            | 1.59 sec                                                                                                              | 1.59 sec: 1.00x slower                                                                                                    |
| pathlib                    | 19.9 ms                                                                                                               | 20.0 ms: 1.01x slower                                                                                                     |
| asyncio_tcp                | 373 ms                                                                                                                | 375 ms: 1.01x slower                                                                                                      |
| dulwich_log                | 63.3 ms                                                                                                               | 63.7 ms: 1.01x slower                                                                                                     |
| sympy_sum                  | 170 ms                                                                                                                | 172 ms: 1.01x slower                                                                                                      |
| sqlglot_v2_normalize       | 136 ms                                                                                                                | 137 ms: 1.01x slower                                                                                                      |
| regex_compile              | 154 ms                                                                                                                | 156 ms: 1.01x slower                                                                                                      |
| logging_silent             | 671 ns                                                                                                                | 677 ns: 1.01x slower                                                                                                      |
| djangocms                  | 65.6 us                                                                                                               | 66.3 us: 1.01x slower                                                                                                     |
| bpe_tokeniser              | 5.63 sec                                                                                                              | 5.70 sec: 1.01x slower                                                                                                    |
| bench_thread_pool          | 1.05 ms                                                                                                               | 1.06 ms: 1.01x slower                                                                                                     |
| deepcopy                   | 322 us                                                                                                                | 326 us: 1.01x slower                                                                                                      |
| async_tree_memoization     | 359 ms                                                                                                                | 364 ms: 1.01x slower                                                                                                      |
| sphinx                     | 1.20 sec                                                                                                              | 1.22 sec: 1.01x slower                                                                                                    |
| docutils                   | 3.10 sec                                                                                                              | 3.14 sec: 1.01x slower                                                                                                    |
| sqlglot_v2_optimize        | 67.1 ms                                                                                                               | 68.1 ms: 1.01x slower                                                                                                     |
| sympy_str                  | 333 ms                                                                                                                | 338 ms: 1.01x slower                                                                                                      |
| logging_format             | 8.39 us                                                                                                               | 8.51 us: 1.01x slower                                                                                                     |
| async_tree_none            | 309 ms                                                                                                                | 313 ms: 1.01x slower                                                                                                      |
| asyncio_websockets         | 382 ms                                                                                                                | 388 ms: 1.02x slower                                                                                                      |
| logging_simple             | 7.57 us                                                                                                               | 7.69 us: 1.02x slower                                                                                                     |
| subparsers                 | 28.2 ms                                                                                                               | 28.6 ms: 1.02x slower                                                                                                     |
| pickle_dict                | 35.5 us                                                                                                               | 36.1 us: 1.02x slower                                                                                                     |
| pickle                     | 14.4 us                                                                                                               | 14.7 us: 1.02x slower                                                                                                     |
| sqlglot_v2_parse           | 1.51 ms                                                                                                               | 1.54 ms: 1.02x slower                                                                                                     |
| 2to3                       | 313 ms                                                                                                                | 320 ms: 1.02x slower                                                                                                      |
| sympy_expand               | 574 ms                                                                                                                | 588 ms: 1.02x slower                                                                                                      |
| sympy_integrate            | 23.8 ms                                                                                                               | 24.4 ms: 1.03x slower                                                                                                     |
| meteor_contest             | 140 ms                                                                                                                | 144 ms: 1.03x slower                                                                                                      |
| sqlglot_v2_transpile       | 1.91 ms                                                                                                               | 1.97 ms: 1.03x slower                                                                                                     |
| many_optionals             | 1.12 ms                                                                                                               | 1.16 ms: 1.03x slower                                                                                                     |
| mdp                        | 1.54 sec                                                                                                              | 1.59 sec: 1.03x slower                                                                                                    |
| raytrace                   | 327 ms                                                                                                                | 337 ms: 1.03x slower                                                                                                      |
| thrift                     | 1.03 ms                                                                                                               | 1.06 ms: 1.03x slower                                                                                                     |
| mako                       | 13.0 ms                                                                                                               | 13.4 ms: 1.03x slower                                                                                                     |
| django_template            | 41.6 ms                                                                                                               | 43.0 ms: 1.03x slower                                                                                                     |
| typing_runtime_protocols   | 209 us                                                                                                                | 216 us: 1.03x slower                                                                                                      |
| nqueens                    | 107 ms                                                                                                                | 111 ms: 1.04x slower                                                                                                      |
| fannkuch                   | 464 ms                                                                                                                | 483 ms: 1.04x slower                                                                                                      |
| async_tree_cpu_io_mixed_tg | 649 ms                                                                                                                | 675 ms: 1.04x slower                                                                                                      |
| async_tree_cpu_io_mixed    | 646 ms                                                                                                                | 672 ms: 1.04x slower                                                                                                      |
| json_dumps                 | 13.9 ms                                                                                                               | 14.5 ms: 1.04x slower                                                                                                     |
| xml_etree_parse            | 163 ms                                                                                                                | 170 ms: 1.04x slower                                                                                                      |
| coverage                   | 96.1 ms                                                                                                               | 101 ms: 1.05x slower                                                                                                      |
| spectral_norm              | 116 ms                                                                                                                | 122 ms: 1.05x slower                                                                                                      |
| crypto_pyaes               | 89.0 ms                                                                                                               | 93.4 ms: 1.05x slower                                                                                                     |
| genshi_text                | 27.5 ms                                                                                                               | 28.9 ms: 1.05x slower                                                                                                     |
| async_generators           | 445 ms                                                                                                                | 475 ms: 1.07x slower                                                                                                      |
| genshi_xml                 | 60.0 ms                                                                                                               | 64.1 ms: 1.07x slower                                                                                                     |
| nbody                      | 100 ms                                                                                                                | 108 ms: 1.08x slower                                                                                                      |
| hexiom                     | 6.52 ms                                                                                                               | 7.03 ms: 1.08x slower                                                                                                     |
| generators                 | 31.3 ms                                                                                                               | 34.8 ms: 1.11x slower                                                                                                     |
| go                         | 127 ms                                                                                                                | 143 ms: 1.12x slower                                                                                                      |
| comprehensions             | 18.9 us                                                                                                               | 21.3 us: 1.12x slower                                                                                                     |
| unpack_sequence            | 52.3 ns                                                                                                               | 67.1 ns: 1.28x slower                                                                                                     |
| bench_mp_pool              | 1.21 sec                                                                                                              | 2.14 sec: 1.77x slower                                                                                                    |
| Geometric mean             | (ref)                                                                                                                 | 1.02x slower                                                                                                              |

Benchmark hidden because not significant (14): pprint_safe_repr, xml_etree_generate, unpickle, regex_dna, regex_effbot, chaos, async_tree_io_tg, json, regex_v8, async_tree_memoization_tg, telco, scimark_monte_carlo, async_tree_io, pylint

- Geometric mean (including insignificant results): 1.005x faster

# HPT report

- Reliability score: 99.98% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.02x
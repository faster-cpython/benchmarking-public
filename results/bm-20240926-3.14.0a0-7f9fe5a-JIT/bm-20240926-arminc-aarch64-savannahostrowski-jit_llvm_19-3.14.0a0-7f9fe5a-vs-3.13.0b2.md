# Results vs. 3.13.0b2

- fork: savannahostrowski
- ref: jit_llvm_19
- machine: linux-aarch64
- commit hash: 7f9fe5a
- commit date: 2024-09-26
- overall geometric mean: 1.07x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x slower
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240926-arminc-aarch64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 305 ms                                                       | 374 ms: 1.23x slower                                                      |
| docutils       | 3.10 sec                                                     | 3.85 sec: 1.24x slower                                                    |
| html5lib       | 66.1 ms                                                      | 71.3 ms: 1.08x slower                                                     |
| tornado_http   | 128 ms                                                       | 146 ms: 1.14x slower                                                      |
| Geometric mean | (ref)                                                        | 1.17x slower                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240926-arminc-aarch64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|----------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_none            | 492 ms                                                       | 435 ms: 1.13x faster                                                      |
| async_tree_none_tg         | 476 ms                                                       | 421 ms: 1.13x faster                                                      |
| async_tree_memoization     | 645 ms                                                       | 582 ms: 1.11x faster                                                      |
| async_tree_io_tg           | 1.27 sec                                                     | 1.18 sec: 1.08x faster                                                    |
| async_tree_memoization_tg  | 604 ms                                                       | 562 ms: 1.08x faster                                                      |
| async_tree_io              | 1.22 sec                                                     | 1.15 sec: 1.07x faster                                                    |
| async_tree_cpu_io_mixed    | 791 ms                                                       | 746 ms: 1.06x faster                                                      |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 743 ms: 1.03x faster                                                      |
| Geometric mean             | (ref)                                                        | 1.09x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240926-arminc-aarch64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| float          | 91.4 ms                                                      | 87.4 ms: 1.05x faster                                                     |
| Geometric mean | (ref)                                                        | 1.02x faster                                                              |

Benchmark hidden because not significant (2): nbody, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240926-arminc-aarch64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_compile  | 128 ms                                                       | 189 ms: 1.48x slower                                                      |
| Geometric mean | (ref)                                                        | 1.10x slower                                                              |

Benchmark hidden because not significant (3): regex_v8, regex_dna, regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240926-arminc-aarch64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|----------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| unpickle             | 19.8 us                                                      | 19.3 us: 1.03x faster                                                     |
| json_loads           | 32.1 us                                                      | 31.4 us: 1.02x faster                                                     |
| pickle_list          | 5.27 us                                                      | 5.16 us: 1.02x faster                                                     |
| unpickle_list        | 6.52 us                                                      | 6.40 us: 1.02x faster                                                     |
| xml_etree_iterparse  | 147 ms                                                       | 148 ms: 1.01x slower                                                      |
| pickle_dict          | 37.6 us                                                      | 38.4 us: 1.02x slower                                                     |
| pickle               | 13.4 us                                                      | 13.6 us: 1.02x slower                                                     |
| json_dumps           | 13.1 ms                                                      | 13.5 ms: 1.03x slower                                                     |
| unpickle_pure_python | 251 us                                                       | 263 us: 1.04x slower                                                      |
| pickle_pure_python   | 359 us                                                       | 377 us: 1.05x slower                                                      |
| Geometric mean       | (ref)                                                        | 1.00x slower                                                              |

Benchmark hidden because not significant (4): xml_etree_process, xml_etree_parse, xml_etree_generate, tomli_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240926-arminc-aarch64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 13.0 ms                                                      | 13.1 ms: 1.01x slower                                                     |
| python_startup_no_site | 8.60 ms                                                      | 8.72 ms: 1.01x slower                                                     |
| Geometric mean         | (ref)                                                        | 1.01x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240926-arminc-aarch64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|-----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| django_template | 42.3 ms                                                      | 50.0 ms: 1.18x slower                                                     |
| genshi_text     | 27.4 ms                                                      | 34.6 ms: 1.26x slower                                                     |
| genshi_xml      | 60.4 ms                                                      | 80.5 ms: 1.33x slower                                                     |
| Geometric mean  | (ref)                                                        | 1.18x slower                                                              |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240926-arminc-aarch64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|----------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| deepcopy_memo              | 50.8 us                                                      | 36.5 us: 1.39x faster                                                     |
| deepcopy                   | 448 us                                                       | 385 us: 1.16x faster                                                      |
| async_tree_none            | 492 ms                                                       | 435 ms: 1.13x faster                                                      |
| async_tree_none_tg         | 476 ms                                                       | 421 ms: 1.13x faster                                                      |
| async_tree_memoization     | 645 ms                                                       | 582 ms: 1.11x faster                                                      |
| async_tree_io_tg           | 1.27 sec                                                     | 1.18 sec: 1.08x faster                                                    |
| async_tree_memoization_tg  | 604 ms                                                       | 562 ms: 1.08x faster                                                      |
| deepcopy_reduce            | 4.04 us                                                      | 3.79 us: 1.07x faster                                                     |
| async_tree_io              | 1.22 sec                                                     | 1.15 sec: 1.07x faster                                                    |
| scimark_sor                | 159 ms                                                       | 150 ms: 1.07x faster                                                      |
| async_tree_cpu_io_mixed    | 791 ms                                                       | 746 ms: 1.06x faster                                                      |
| float                      | 91.4 ms                                                      | 87.4 ms: 1.05x faster                                                     |
| pathlib                    | 22.8 ms                                                      | 21.8 ms: 1.05x faster                                                     |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 743 ms: 1.03x faster                                                      |
| sqlite_synth               | 3.90 us                                                      | 3.80 us: 1.03x faster                                                     |
| unpickle                   | 19.8 us                                                      | 19.3 us: 1.03x faster                                                     |
| json_loads                 | 32.1 us                                                      | 31.4 us: 1.02x faster                                                     |
| pickle_list                | 5.27 us                                                      | 5.16 us: 1.02x faster                                                     |
| coroutines                 | 29.0 ms                                                      | 28.4 ms: 1.02x faster                                                     |
| unpickle_list              | 6.52 us                                                      | 6.40 us: 1.02x faster                                                     |
| bpe_tokeniser              | 5.83 sec                                                     | 5.86 sec: 1.00x slower                                                    |
| asyncio_tcp_ssl            | 2.21 sec                                                     | 2.23 sec: 1.01x slower                                                    |
| python_startup             | 13.0 ms                                                      | 13.1 ms: 1.01x slower                                                     |
| xml_etree_iterparse        | 147 ms                                                       | 148 ms: 1.01x slower                                                      |
| python_startup_no_site     | 8.60 ms                                                      | 8.72 ms: 1.01x slower                                                     |
| logging_silent             | 133 ns                                                       | 136 ns: 1.02x slower                                                      |
| coverage                   | 98.4 ms                                                      | 100 ms: 1.02x slower                                                      |
| pickle_dict                | 37.6 us                                                      | 38.4 us: 1.02x slower                                                     |
| pickle                     | 13.4 us                                                      | 13.6 us: 1.02x slower                                                     |
| spectral_norm              | 141 ms                                                       | 144 ms: 1.02x slower                                                      |
| json_dumps                 | 13.1 ms                                                      | 13.5 ms: 1.03x slower                                                     |
| async_generators           | 488 ms                                                       | 506 ms: 1.04x slower                                                      |
| scimark_sparse_mat_mult    | 6.55 ms                                                      | 6.80 ms: 1.04x slower                                                     |
| logging_simple             | 7.21 us                                                      | 7.48 us: 1.04x slower                                                     |
| mdp                        | 3.33 sec                                                     | 3.47 sec: 1.04x slower                                                    |
| asyncio_tcp                | 584 ms                                                       | 610 ms: 1.04x slower                                                      |
| unpickle_pure_python       | 251 us                                                       | 263 us: 1.04x slower                                                      |
| logging_format             | 7.82 us                                                      | 8.19 us: 1.05x slower                                                     |
| pickle_pure_python         | 359 us                                                       | 377 us: 1.05x slower                                                      |
| scimark_lu                 | 141 ms                                                       | 149 ms: 1.05x slower                                                      |
| bench_mp_pool              | 7.03 ms                                                      | 7.42 ms: 1.06x slower                                                     |
| bench_thread_pool          | 1.26 ms                                                      | 1.33 ms: 1.06x slower                                                     |
| typing_runtime_protocols   | 193 us                                                       | 207 us: 1.07x slower                                                      |
| crypto_pyaes               | 82.0 ms                                                      | 87.9 ms: 1.07x slower                                                     |
| html5lib                   | 66.1 ms                                                      | 71.3 ms: 1.08x slower                                                     |
| meteor_contest             | 113 ms                                                       | 123 ms: 1.09x slower                                                      |
| fannkuch                   | 451 ms                                                       | 490 ms: 1.09x slower                                                      |
| scimark_monte_carlo        | 82.3 ms                                                      | 91.0 ms: 1.11x slower                                                     |
| pyflate                    | 557 ms                                                       | 623 ms: 1.12x slower                                                      |
| deltablue                  | 3.88 ms                                                      | 4.34 ms: 1.12x slower                                                     |
| tornado_http               | 128 ms                                                       | 146 ms: 1.14x slower                                                      |
| go                         | 161 ms                                                       | 185 ms: 1.15x slower                                                      |
| raytrace                   | 297 ms                                                       | 342 ms: 1.15x slower                                                      |
| sqlglot_normalize          | 129 ms                                                       | 149 ms: 1.15x slower                                                      |
| richards                   | 55.9 ms                                                      | 64.8 ms: 1.16x slower                                                     |
| richards_super             | 62.3 ms                                                      | 72.8 ms: 1.17x slower                                                     |
| comprehensions             | 20.5 us                                                      | 24.1 us: 1.17x slower                                                     |
| django_template            | 42.3 ms                                                      | 50.0 ms: 1.18x slower                                                     |
| nqueens                    | 98.9 ms                                                      | 119 ms: 1.20x slower                                                      |
| sqlglot_parse              | 1.42 ms                                                      | 1.72 ms: 1.21x slower                                                     |
| pycparser                  | 1.22 sec                                                     | 1.48 sec: 1.21x slower                                                    |
| 2to3                       | 305 ms                                                       | 374 ms: 1.23x slower                                                      |
| docutils                   | 3.10 sec                                                     | 3.85 sec: 1.24x slower                                                    |
| sqlglot_optimize           | 62.6 ms                                                      | 79.0 ms: 1.26x slower                                                     |
| genshi_text                | 27.4 ms                                                      | 34.6 ms: 1.26x slower                                                     |
| sqlglot_transpile          | 1.71 ms                                                      | 2.16 ms: 1.26x slower                                                     |
| pprint_pformat             | 1.93 sec                                                     | 2.50 sec: 1.29x slower                                                    |
| chaos                      | 68.3 ms                                                      | 88.7 ms: 1.30x slower                                                     |
| pprint_safe_repr           | 933 ms                                                       | 1.21 sec: 1.30x slower                                                    |
| sympy_expand               | 457 ms                                                       | 600 ms: 1.31x slower                                                      |
| genshi_xml                 | 60.4 ms                                                      | 80.5 ms: 1.33x slower                                                     |
| sympy_integrate            | 20.9 ms                                                      | 28.2 ms: 1.35x slower                                                     |
| sympy_str                  | 265 ms                                                       | 359 ms: 1.35x slower                                                      |
| hexiom                     | 7.08 ms                                                      | 9.84 ms: 1.39x slower                                                     |
| dulwich_log                | 58.5 ms                                                      | 82.2 ms: 1.41x slower                                                     |
| pylint                     | 337 ms                                                       | 474 ms: 1.41x slower                                                      |
| sympy_sum                  | 144 ms                                                       | 208 ms: 1.45x slower                                                      |
| regex_compile              | 128 ms                                                       | 189 ms: 1.48x slower                                                      |
| generators                 | 37.1 ms                                                      | 56.9 ms: 1.53x slower                                                     |
| Geometric mean             | (ref)                                                        | 1.07x slower                                                              |

Benchmark hidden because not significant (17): xml_etree_process, mako, nbody, create_gc_cycles, regex_v8, xml_etree_parse, xml_etree_generate, pidigits, thrift, telco, json, regex_dna, gc_traversal, tomli_loads, regex_effbot, scimark_fft, asyncio_websockets
Ignored benchmarks (6) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2
Ignored benchmarks (1) of results/bm-20240926-3.14.0a0-7f9fe5a-JIT/bm-20240926-arminc-aarch64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a.json: unpack_sequence

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.02x
- 95% likely to have a slowdown of 1.02x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: 1.09x
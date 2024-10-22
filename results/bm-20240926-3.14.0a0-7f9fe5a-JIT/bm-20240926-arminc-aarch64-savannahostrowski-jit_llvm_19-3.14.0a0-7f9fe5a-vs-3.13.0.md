# Results vs. 3.13.0

- fork: savannahostrowski
- ref: jit_llvm_19
- machine: linux-aarch64
- commit hash: 7f9fe5a
- commit date: 2024-09-26
- overall geometric mean: 1.09x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x slower
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240926-arminc-aarch64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|----------------|:--------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 306 ms                                                   | 374 ms: 1.22x slower                                                      |
| docutils       | 2.91 sec                                                 | 3.85 sec: 1.33x slower                                                    |
| html5lib       | 64.3 ms                                                  | 71.3 ms: 1.11x slower                                                     |
| tornado_http   | 131 ms                                                   | 146 ms: 1.11x slower                                                      |
| Geometric mean | (ref)                                                    | 1.19x slower                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240926-arminc-aarch64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|---------------------------|:--------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_memoization_tg | 649 ms                                                   | 562 ms: 1.16x faster                                                      |
| async_tree_none           | 493 ms                                                   | 435 ms: 1.14x faster                                                      |
| async_tree_none_tg        | 467 ms                                                   | 421 ms: 1.11x faster                                                      |
| async_tree_memoization    | 626 ms                                                   | 582 ms: 1.08x faster                                                      |
| async_tree_cpu_io_mixed   | 764 ms                                                   | 746 ms: 1.02x faster                                                      |
| asyncio_websockets        | 656 ms                                                   | 661 ms: 1.01x slower                                                      |
| async_generators          | 496 ms                                                   | 506 ms: 1.02x slower                                                      |
| asyncio_tcp_ssl           | 2.18 sec                                                 | 2.23 sec: 1.02x slower                                                    |
| async_tree_io             | 1.11 sec                                                 | 1.15 sec: 1.04x slower                                                    |
| asyncio_tcp               | 568 ms                                                   | 610 ms: 1.07x slower                                                      |
| async_tree_io_tg          | 1.09 sec                                                 | 1.18 sec: 1.08x slower                                                    |
| Geometric mean            | (ref)                                                    | 1.02x faster                                                              |

Benchmark hidden because not significant (2): coroutines, async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240926-arminc-aarch64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|----------------|:--------------------------------------------------------:|:-------------------------------------------------------------------------:|
| float          | 94.4 ms                                                  | 87.4 ms: 1.08x faster                                                     |
| Geometric mean | (ref)                                                    | 1.03x faster                                                              |

Benchmark hidden because not significant (2): nbody, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240926-arminc-aarch64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|----------------|:--------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_v8       | 31.5 ms                                                  | 31.0 ms: 1.02x faster                                                     |
| regex_effbot   | 4.87 ms                                                  | 5.00 ms: 1.03x slower                                                     |
| regex_dna      | 246 ms                                                   | 259 ms: 1.05x slower                                                      |
| regex_compile  | 128 ms                                                   | 189 ms: 1.47x slower                                                      |
| Geometric mean | (ref)                                                    | 1.12x slower                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240926-arminc-aarch64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|----------------------|:--------------------------------------------------------:|:-------------------------------------------------------------------------:|
| unpickle             | 20.2 us                                                  | 19.3 us: 1.05x faster                                                     |
| unpickle_list        | 6.65 us                                                  | 6.40 us: 1.04x faster                                                     |
| pickle_list          | 5.34 us                                                  | 5.16 us: 1.03x faster                                                     |
| xml_etree_iterparse  | 147 ms                                                   | 148 ms: 1.01x slower                                                      |
| pickle               | 13.5 us                                                  | 13.6 us: 1.01x slower                                                     |
| xml_etree_parse      | 188 ms                                                   | 191 ms: 1.02x slower                                                      |
| tomli_loads          | 2.53 sec                                                 | 2.58 sec: 1.02x slower                                                    |
| unpickle_pure_python | 254 us                                                   | 263 us: 1.03x slower                                                      |
| pickle_pure_python   | 359 us                                                   | 377 us: 1.05x slower                                                      |
| Geometric mean       | (ref)                                                    | 1.00x slower                                                              |

Benchmark hidden because not significant (5): xml_etree_process, json_loads, xml_etree_generate, pickle_dict, json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240926-arminc-aarch64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|----------------|:--------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup | 13.3 ms                                                  | 13.1 ms: 1.01x faster                                                     |
| Geometric mean | (ref)                                                    | 1.01x faster                                                              |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240926-arminc-aarch64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|-----------------|:--------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako            | 13.3 ms                                                  | 13.0 ms: 1.02x faster                                                     |
| django_template | 42.3 ms                                                  | 50.0 ms: 1.18x slower                                                     |
| genshi_text     | 27.7 ms                                                  | 34.6 ms: 1.25x slower                                                     |
| genshi_xml      | 60.2 ms                                                  | 80.5 ms: 1.34x slower                                                     |
| Geometric mean  | (ref)                                                    | 1.18x slower                                                              |

All benchmarks:
===============

| Benchmark                 | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240926-arminc-aarch64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|---------------------------|:--------------------------------------------------------:|:-------------------------------------------------------------------------:|
| deepcopy_memo             | 51.0 us                                                  | 36.5 us: 1.40x faster                                                     |
| deepcopy                  | 451 us                                                   | 385 us: 1.17x faster                                                      |
| async_tree_memoization_tg | 649 ms                                                   | 562 ms: 1.16x faster                                                      |
| async_tree_none           | 493 ms                                                   | 435 ms: 1.14x faster                                                      |
| async_tree_none_tg        | 467 ms                                                   | 421 ms: 1.11x faster                                                      |
| float                     | 94.4 ms                                                  | 87.4 ms: 1.08x faster                                                     |
| async_tree_memoization    | 626 ms                                                   | 582 ms: 1.08x faster                                                      |
| deepcopy_reduce           | 4.07 us                                                  | 3.79 us: 1.07x faster                                                     |
| scimark_sor               | 159 ms                                                   | 150 ms: 1.06x faster                                                      |
| unpickle                  | 20.2 us                                                  | 19.3 us: 1.05x faster                                                     |
| unpickle_list             | 6.65 us                                                  | 6.40 us: 1.04x faster                                                     |
| pickle_list               | 5.34 us                                                  | 5.16 us: 1.03x faster                                                     |
| pathlib                   | 22.4 ms                                                  | 21.8 ms: 1.03x faster                                                     |
| async_tree_cpu_io_mixed   | 764 ms                                                   | 746 ms: 1.02x faster                                                      |
| mako                      | 13.3 ms                                                  | 13.0 ms: 1.02x faster                                                     |
| regex_v8                  | 31.5 ms                                                  | 31.0 ms: 1.02x faster                                                     |
| python_startup            | 13.3 ms                                                  | 13.1 ms: 1.01x faster                                                     |
| bpe_tokeniser             | 5.90 sec                                                 | 5.86 sec: 1.01x faster                                                    |
| asyncio_websockets        | 656 ms                                                   | 661 ms: 1.01x slower                                                      |
| xml_etree_iterparse       | 147 ms                                                   | 148 ms: 1.01x slower                                                      |
| pickle                    | 13.5 us                                                  | 13.6 us: 1.01x slower                                                     |
| xml_etree_parse           | 188 ms                                                   | 191 ms: 1.02x slower                                                      |
| thrift                    | 946 us                                                   | 961 us: 1.02x slower                                                      |
| bench_mp_pool             | 7.30 ms                                                  | 7.42 ms: 1.02x slower                                                     |
| coverage                  | 98.5 ms                                                  | 100 ms: 1.02x slower                                                      |
| async_generators          | 496 ms                                                   | 506 ms: 1.02x slower                                                      |
| tomli_loads               | 2.53 sec                                                 | 2.58 sec: 1.02x slower                                                    |
| asyncio_tcp_ssl           | 2.18 sec                                                 | 2.23 sec: 1.02x slower                                                    |
| spectral_norm             | 141 ms                                                   | 144 ms: 1.02x slower                                                      |
| regex_effbot              | 4.87 ms                                                  | 5.00 ms: 1.03x slower                                                     |
| telco                     | 9.73 ms                                                  | 10.0 ms: 1.03x slower                                                     |
| mdp                       | 3.36 sec                                                 | 3.47 sec: 1.03x slower                                                    |
| unpickle_pure_python      | 254 us                                                   | 263 us: 1.03x slower                                                      |
| scimark_sparse_mat_mult   | 6.58 ms                                                  | 6.80 ms: 1.03x slower                                                     |
| async_tree_io             | 1.11 sec                                                 | 1.15 sec: 1.04x slower                                                    |
| bench_thread_pool         | 1.28 ms                                                  | 1.33 ms: 1.04x slower                                                     |
| logging_format            | 7.83 us                                                  | 8.19 us: 1.05x slower                                                     |
| pickle_pure_python        | 359 us                                                   | 377 us: 1.05x slower                                                      |
| regex_dna                 | 246 ms                                                   | 259 ms: 1.05x slower                                                      |
| logging_simple            | 7.04 us                                                  | 7.48 us: 1.06x slower                                                     |
| crypto_pyaes              | 82.7 ms                                                  | 87.9 ms: 1.06x slower                                                     |
| scimark_lu                | 139 ms                                                   | 149 ms: 1.07x slower                                                      |
| asyncio_tcp               | 568 ms                                                   | 610 ms: 1.07x slower                                                      |
| typing_runtime_protocols  | 192 us                                                   | 207 us: 1.08x slower                                                      |
| async_tree_io_tg          | 1.09 sec                                                 | 1.18 sec: 1.08x slower                                                    |
| fannkuch                  | 452 ms                                                   | 490 ms: 1.08x slower                                                      |
| meteor_contest            | 113 ms                                                   | 123 ms: 1.09x slower                                                      |
| scimark_monte_carlo       | 83.8 ms                                                  | 91.0 ms: 1.09x slower                                                     |
| create_gc_cycles          | 2.12 ms                                                  | 2.32 ms: 1.09x slower                                                     |
| html5lib                  | 64.3 ms                                                  | 71.3 ms: 1.11x slower                                                     |
| tornado_http              | 131 ms                                                   | 146 ms: 1.11x slower                                                      |
| pyflate                   | 556 ms                                                   | 623 ms: 1.12x slower                                                      |
| deltablue                 | 3.85 ms                                                  | 4.34 ms: 1.13x slower                                                     |
| go                        | 163 ms                                                   | 185 ms: 1.14x slower                                                      |
| gc_traversal              | 4.53 ms                                                  | 5.19 ms: 1.15x slower                                                     |
| raytrace                  | 298 ms                                                   | 342 ms: 1.15x slower                                                      |
| sqlglot_normalize         | 128 ms                                                   | 149 ms: 1.16x slower                                                      |
| pycparser                 | 1.26 sec                                                 | 1.48 sec: 1.17x slower                                                    |
| comprehensions            | 20.4 us                                                  | 24.1 us: 1.18x slower                                                     |
| django_template           | 42.3 ms                                                  | 50.0 ms: 1.18x slower                                                     |
| nqueens                   | 98.7 ms                                                  | 119 ms: 1.21x slower                                                      |
| richards_super            | 60.3 ms                                                  | 72.8 ms: 1.21x slower                                                     |
| richards                  | 53.5 ms                                                  | 64.8 ms: 1.21x slower                                                     |
| 2to3                      | 306 ms                                                   | 374 ms: 1.22x slower                                                      |
| sqlglot_parse             | 1.38 ms                                                  | 1.72 ms: 1.24x slower                                                     |
| sqlglot_transpile         | 1.73 ms                                                  | 2.16 ms: 1.25x slower                                                     |
| genshi_text               | 27.7 ms                                                  | 34.6 ms: 1.25x slower                                                     |
| sqlglot_optimize          | 62.4 ms                                                  | 79.0 ms: 1.27x slower                                                     |
| chaos                     | 68.8 ms                                                  | 88.7 ms: 1.29x slower                                                     |
| pprint_safe_repr          | 926 ms                                                   | 1.21 sec: 1.31x slower                                                    |
| pprint_pformat            | 1.90 sec                                                 | 2.50 sec: 1.32x slower                                                    |
| sympy_expand              | 455 ms                                                   | 600 ms: 1.32x slower                                                      |
| docutils                  | 2.91 sec                                                 | 3.85 sec: 1.33x slower                                                    |
| genshi_xml                | 60.2 ms                                                  | 80.5 ms: 1.34x slower                                                     |
| sympy_integrate           | 21.0 ms                                                  | 28.2 ms: 1.34x slower                                                     |
| sympy_str                 | 264 ms                                                   | 359 ms: 1.36x slower                                                      |
| hexiom                    | 7.13 ms                                                  | 9.84 ms: 1.38x slower                                                     |
| pylint                    | 343 ms                                                   | 474 ms: 1.38x slower                                                      |
| sympy_sum                 | 143 ms                                                   | 208 ms: 1.45x slower                                                      |
| regex_compile             | 128 ms                                                   | 189 ms: 1.47x slower                                                      |
| generators                | 37.8 ms                                                  | 56.9 ms: 1.50x slower                                                     |
| unpack_sequence           | 57.2 ns                                                  | 147 ns: 2.58x slower                                                      |
| Geometric mean            | (ref)                                                    | 1.09x slower                                                              |

Benchmark hidden because not significant (14): xml_etree_process, sqlite_synth, nbody, python_startup_no_site, json_loads, pidigits, xml_etree_generate, scimark_fft, logging_silent, pickle_dict, json, coroutines, json_dumps, async_tree_cpu_io_mixed_tg
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2
Ignored benchmarks (1) of results/bm-20240926-3.14.0a0-7f9fe5a-JIT/bm-20240926-arminc-aarch64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a.json: dulwich_log

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.04x
- 95% likely to have a slowdown of 1.03x
- 99% likely to have a slowdown of 1.02x

# Memory
- memory change: 1.10x
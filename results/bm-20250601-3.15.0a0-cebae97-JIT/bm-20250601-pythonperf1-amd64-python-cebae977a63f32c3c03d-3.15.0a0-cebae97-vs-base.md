# Results vs. base

- fork: python
- ref: cebae977a63f32c3c03d
- machine: windows-amd64
- commit hash: cebae97
- commit date: 2025-06-01
- overall geometric mean: 1.449x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20250601-3.15.0a0-cebae97/bm-20250601-pythonperf1-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json | results/bm-20250601-3.15.0a0-cebae97-JIT/bm-20250601-pythonperf1-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json |
|----------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 292 ms                                                                                                               | 286 ms: 1.02x faster                                                                                                     |
| html5lib       | 50.8 ms                                                                                                              | 51.3 ms: 1.01x slower                                                                                                    |
| Geometric mean | (ref)                                                                                                                | 1.00x faster                                                                                                             |

Benchmark hidden because not significant (2): docutils, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | results/bm-20250601-3.15.0a0-cebae97/bm-20250601-pythonperf1-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json | results/bm-20250601-3.15.0a0-cebae97-JIT/bm-20250601-pythonperf1-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json |
|----------------------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| async_tree_none            | 242 ms                                                                                                               | 230 ms: 1.05x faster                                                                                                     |
| async_tree_memoization     | 296 ms                                                                                                               | 282 ms: 1.05x faster                                                                                                     |
| async_tree_cpu_io_mixed    | 443 ms                                                                                                               | 426 ms: 1.04x faster                                                                                                     |
| async_tree_cpu_io_mixed_tg | 439 ms                                                                                                               | 424 ms: 1.03x faster                                                                                                     |
| async_tree_none_tg         | 234 ms                                                                                                               | 228 ms: 1.03x faster                                                                                                     |
| async_tree_io_tg           | 554 ms                                                                                                               | 538 ms: 1.03x faster                                                                                                     |
| async_tree_memoization_tg  | 286 ms                                                                                                               | 280 ms: 1.02x faster                                                                                                     |
| async_tree_io              | 548 ms                                                                                                               | 536 ms: 1.02x faster                                                                                                     |
| coroutines                 | 25.6 ms                                                                                                              | 25.1 ms: 1.02x faster                                                                                                    |
| async_generators           | 343 ms                                                                                                               | 353 ms: 1.03x slower                                                                                                     |
| asyncio_tcp_ssl            | 1.36 sec                                                                                                             | 1.49 sec: 1.10x slower                                                                                                   |
| asyncio_tcp                | 422 ms                                                                                                               | 560 ms: 1.33x slower                                                                                                     |
| Geometric mean             | (ref)                                                                                                                | 1.01x slower                                                                                                             |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20250601-3.15.0a0-cebae97/bm-20250601-pythonperf1-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json | results/bm-20250601-3.15.0a0-cebae97-JIT/bm-20250601-pythonperf1-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json |
|----------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| nbody          | 105 ms                                                                                                               | 55.8 ms: 1.88x faster                                                                                                    |
| pidigits       | 145 ms                                                                                                               | 146 ms: 1.01x slower                                                                                                     |
| float          | 77.0 ms                                                                                                              | 78.8 ms: 1.02x slower                                                                                                    |
| Geometric mean | (ref)                                                                                                                | 1.22x faster                                                                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20250601-3.15.0a0-cebae97/bm-20250601-pythonperf1-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json | results/bm-20250601-3.15.0a0-cebae97-JIT/bm-20250601-pythonperf1-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json |
|----------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| regex_compile  | 124 ms                                                                                                               | 112 ms: 1.11x faster                                                                                                     |
| regex_v8       | 16.6 ms                                                                                                              | 16.4 ms: 1.02x faster                                                                                                    |
| regex_effbot   | 1.80 ms                                                                                                              | 1.78 ms: 1.01x faster                                                                                                    |
| Geometric mean | (ref)                                                                                                                | 1.03x faster                                                                                                             |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20250601-3.15.0a0-cebae97/bm-20250601-pythonperf1-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json | results/bm-20250601-3.15.0a0-cebae97-JIT/bm-20250601-pythonperf1-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json |
|----------------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| unpickle_pure_python | 275 us                                                                                                               | 156 us: 1.76x faster                                                                                                     |
| tomli_loads          | 2.10 sec                                                                                                             | 1.55 sec: 1.35x faster                                                                                                   |
| xml_etree_generate   | 89.7 ms                                                                                                              | 70.0 ms: 1.28x faster                                                                                                    |
| xml_etree_process    | 64.8 ms                                                                                                              | 50.8 ms: 1.27x faster                                                                                                    |
| pickle_pure_python   | 359 us                                                                                                               | 319 us: 1.13x faster                                                                                                     |
| xml_etree_iterparse  | 90.2 ms                                                                                                              | 85.0 ms: 1.06x faster                                                                                                    |
| xml_etree_parse      | 108 ms                                                                                                               | 103 ms: 1.04x faster                                                                                                     |
| unpickle_list        | 3.14 us                                                                                                              | 3.07 us: 1.02x faster                                                                                                    |
| unpickle             | 11.4 us                                                                                                              | 11.2 us: 1.02x faster                                                                                                    |
| pickle_dict          | 22.5 us                                                                                                              | 22.0 us: 1.02x faster                                                                                                    |
| Geometric mean       | (ref)                                                                                                                | 1.13x faster                                                                                                             |

Benchmark hidden because not significant (4): json_loads, pickle_list, pickle, json_dumps

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup, python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20250601-3.15.0a0-cebae97/bm-20250601-pythonperf1-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json | results/bm-20250601-3.15.0a0-cebae97-JIT/bm-20250601-pythonperf1-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json |
|-----------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| mako            | 12.5 ms                                                                                                              | 7.09 ms: 1.76x faster                                                                                                    |
| genshi_xml      | 49.1 ms                                                                                                              | 49.3 ms: 1.00x slower                                                                                                    |
| django_template | 37.2 ms                                                                                                              | 37.3 ms: 1.00x slower                                                                                                    |
| genshi_text     | 23.8 ms                                                                                                              | 24.2 ms: 1.02x slower                                                                                                    |
| Geometric mean  | (ref)                                                                                                                | 1.14x faster                                                                                                             |

All benchmarks:
===============

| Benchmark                  | results/bm-20250601-3.15.0a0-cebae97/bm-20250601-pythonperf1-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json | results/bm-20250601-3.15.0a0-cebae97-JIT/bm-20250601-pythonperf1-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json |
|----------------------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| pprint_pformat             | 1.74 sec                                                                                                             | 1.56 us: 1114434.79x faster                                                                                              |
| pprint_safe_repr           | 848 ms                                                                                                               | 904 ns: 938600.09x faster                                                                                                |
| nbody                      | 105 ms                                                                                                               | 55.8 ms: 1.88x faster                                                                                                    |
| unpickle_pure_python       | 275 us                                                                                                               | 156 us: 1.76x faster                                                                                                     |
| mako                       | 12.5 ms                                                                                                              | 7.09 ms: 1.76x faster                                                                                                    |
| scimark_sparse_mat_mult    | 4.14 ms                                                                                                              | 2.61 ms: 1.59x faster                                                                                                    |
| scimark_fft                | 274 ms                                                                                                               | 184 ms: 1.49x faster                                                                                                     |
| fannkuch                   | 420 ms                                                                                                               | 286 ms: 1.47x faster                                                                                                     |
| bpe_tokeniser              | 4.40 sec                                                                                                             | 3.03 sec: 1.45x faster                                                                                                   |
| tomli_loads                | 2.10 sec                                                                                                             | 1.55 sec: 1.35x faster                                                                                                   |
| xml_etree_generate         | 89.7 ms                                                                                                              | 70.0 ms: 1.28x faster                                                                                                    |
| crypto_pyaes               | 79.3 ms                                                                                                              | 62.2 ms: 1.27x faster                                                                                                    |
| xml_etree_process          | 64.8 ms                                                                                                              | 50.8 ms: 1.27x faster                                                                                                    |
| comprehensions             | 19.6 us                                                                                                              | 15.5 us: 1.27x faster                                                                                                    |
| telco                      | 6.25 ms                                                                                                              | 5.14 ms: 1.22x faster                                                                                                    |
| sqlglot_v2_parse           | 1.34 ms                                                                                                              | 1.12 ms: 1.19x faster                                                                                                    |
| pyflate                    | 455 ms                                                                                                               | 383 ms: 1.19x faster                                                                                                     |
| sqlglot_v2_transpile       | 1.62 ms                                                                                                              | 1.40 ms: 1.15x faster                                                                                                    |
| meteor_contest             | 94.4 ms                                                                                                              | 82.1 ms: 1.15x faster                                                                                                    |
| pickle_pure_python         | 359 us                                                                                                               | 319 us: 1.13x faster                                                                                                     |
| unpack_sequence            | 81.9 ns                                                                                                              | 72.9 ns: 1.12x faster                                                                                                    |
| regex_compile              | 124 ms                                                                                                               | 112 ms: 1.11x faster                                                                                                     |
| k_core                     | 1.83 sec                                                                                                             | 1.67 sec: 1.10x faster                                                                                                   |
| connected_components       | 350 ms                                                                                                               | 318 ms: 1.10x faster                                                                                                     |
| sqlite_synth               | 1.87 us                                                                                                              | 1.72 us: 1.09x faster                                                                                                    |
| typing_runtime_protocols   | 155 us                                                                                                               | 144 us: 1.07x faster                                                                                                     |
| shortest_path              | 381 ms                                                                                                               | 358 ms: 1.06x faster                                                                                                     |
| xml_etree_iterparse        | 90.2 ms                                                                                                              | 85.0 ms: 1.06x faster                                                                                                    |
| pycparser                  | 985 ms                                                                                                               | 932 ms: 1.06x faster                                                                                                     |
| async_tree_none            | 242 ms                                                                                                               | 230 ms: 1.05x faster                                                                                                     |
| async_tree_memoization     | 296 ms                                                                                                               | 282 ms: 1.05x faster                                                                                                     |
| xml_etree_parse            | 108 ms                                                                                                               | 103 ms: 1.04x faster                                                                                                     |
| nqueens                    | 94.2 ms                                                                                                              | 90.5 ms: 1.04x faster                                                                                                    |
| async_tree_cpu_io_mixed    | 443 ms                                                                                                               | 426 ms: 1.04x faster                                                                                                     |
| sqlglot_v2_optimize        | 50.4 ms                                                                                                              | 48.5 ms: 1.04x faster                                                                                                    |
| async_tree_cpu_io_mixed_tg | 439 ms                                                                                                               | 424 ms: 1.03x faster                                                                                                     |
| async_tree_none_tg         | 234 ms                                                                                                               | 228 ms: 1.03x faster                                                                                                     |
| async_tree_io_tg           | 554 ms                                                                                                               | 538 ms: 1.03x faster                                                                                                     |
| bench_thread_pool          | 1.00 ms                                                                                                              | 977 us: 1.03x faster                                                                                                     |
| gc_traversal               | 2.82 ms                                                                                                              | 2.75 ms: 1.02x faster                                                                                                    |
| unpickle_list              | 3.14 us                                                                                                              | 3.07 us: 1.02x faster                                                                                                    |
| unpickle                   | 11.4 us                                                                                                              | 11.2 us: 1.02x faster                                                                                                    |
| async_tree_memoization_tg  | 286 ms                                                                                                               | 280 ms: 1.02x faster                                                                                                     |
| async_tree_io              | 548 ms                                                                                                               | 536 ms: 1.02x faster                                                                                                     |
| 2to3                       | 292 ms                                                                                                               | 286 ms: 1.02x faster                                                                                                     |
| pickle_dict                | 22.5 us                                                                                                              | 22.0 us: 1.02x faster                                                                                                    |
| sympy_sum                  | 115 ms                                                                                                               | 113 ms: 1.02x faster                                                                                                     |
| coroutines                 | 25.6 ms                                                                                                              | 25.1 ms: 1.02x faster                                                                                                    |
| regex_v8                   | 16.6 ms                                                                                                              | 16.4 ms: 1.02x faster                                                                                                    |
| sqlglot_v2_normalize       | 104 ms                                                                                                               | 102 ms: 1.02x faster                                                                                                     |
| create_gc_cycles           | 1.45 ms                                                                                                              | 1.43 ms: 1.01x faster                                                                                                    |
| chaos                      | 65.8 ms                                                                                                              | 65.0 ms: 1.01x faster                                                                                                    |
| scimark_sor                | 133 ms                                                                                                               | 131 ms: 1.01x faster                                                                                                     |
| regex_effbot               | 1.80 ms                                                                                                              | 1.78 ms: 1.01x faster                                                                                                    |
| pathlib                    | 34.2 ms                                                                                                              | 33.9 ms: 1.01x faster                                                                                                    |
| spectral_norm              | 117 ms                                                                                                               | 116 ms: 1.01x faster                                                                                                     |
| raytrace                   | 302 ms                                                                                                               | 299 ms: 1.01x faster                                                                                                     |
| subparsers                 | 22.7 ms                                                                                                              | 22.6 ms: 1.01x faster                                                                                                    |
| go                         | 133 ms                                                                                                               | 133 ms: 1.00x faster                                                                                                     |
| deltablue                  | 4.31 ms                                                                                                              | 4.29 ms: 1.00x faster                                                                                                    |
| genshi_xml                 | 49.1 ms                                                                                                              | 49.3 ms: 1.00x slower                                                                                                    |
| django_template            | 37.2 ms                                                                                                              | 37.3 ms: 1.00x slower                                                                                                    |
| logging_silent             | 494 ns                                                                                                               | 497 ns: 1.01x slower                                                                                                     |
| pidigits                   | 145 ms                                                                                                               | 146 ms: 1.01x slower                                                                                                     |
| sympy_integrate            | 16.6 ms                                                                                                              | 16.7 ms: 1.01x slower                                                                                                    |
| html5lib                   | 50.8 ms                                                                                                              | 51.3 ms: 1.01x slower                                                                                                    |
| richards                   | 50.8 ms                                                                                                              | 51.2 ms: 1.01x slower                                                                                                    |
| coverage                   | 475 ms                                                                                                               | 479 ms: 1.01x slower                                                                                                     |
| sympy_str                  | 234 ms                                                                                                               | 236 ms: 1.01x slower                                                                                                     |
| richards_super             | 57.4 ms                                                                                                              | 58.1 ms: 1.01x slower                                                                                                    |
| mdp                        | 1.18 sec                                                                                                             | 1.20 sec: 1.01x slower                                                                                                   |
| genshi_text                | 23.8 ms                                                                                                              | 24.2 ms: 1.02x slower                                                                                                    |
| dulwich_log                | 51.1 ms                                                                                                              | 52.0 ms: 1.02x slower                                                                                                    |
| scimark_monte_carlo        | 72.5 ms                                                                                                              | 73.8 ms: 1.02x slower                                                                                                    |
| deepcopy_reduce            | 2.74 us                                                                                                              | 2.80 us: 1.02x slower                                                                                                    |
| deepcopy                   | 265 us                                                                                                               | 270 us: 1.02x slower                                                                                                     |
| scimark_lu                 | 117 ms                                                                                                               | 120 ms: 1.02x slower                                                                                                     |
| float                      | 77.0 ms                                                                                                              | 78.8 ms: 1.02x slower                                                                                                    |
| async_generators           | 343 ms                                                                                                               | 353 ms: 1.03x slower                                                                                                     |
| json                       | 3.94 ms                                                                                                              | 4.06 ms: 1.03x slower                                                                                                    |
| deepcopy_memo              | 33.3 us                                                                                                              | 34.2 us: 1.03x slower                                                                                                    |
| many_optionals             | 546 us                                                                                                               | 563 us: 1.03x slower                                                                                                     |
| sympy_expand               | 400 ms                                                                                                               | 416 ms: 1.04x slower                                                                                                     |
| hexiom                     | 7.39 ms                                                                                                              | 7.72 ms: 1.04x slower                                                                                                    |
| generators                 | 34.3 ms                                                                                                              | 36.5 ms: 1.06x slower                                                                                                    |
| asyncio_tcp_ssl            | 1.36 sec                                                                                                             | 1.49 sec: 1.10x slower                                                                                                   |
| asyncio_tcp                | 422 ms                                                                                                               | 560 ms: 1.33x slower                                                                                                     |
| Geometric mean             | (ref)                                                                                                                | 1.39x faster                                                                                                             |

Benchmark hidden because not significant (15): python_startup, logging_format, json_loads, pickle_list, regex_dna, docutils, pickle, thrift, python_startup_no_site, logging_simple, bench_mp_pool, asyncio_websockets, json_dumps, sphinx, pylint

- Geometric mean (including insignificant results): 1.449x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown
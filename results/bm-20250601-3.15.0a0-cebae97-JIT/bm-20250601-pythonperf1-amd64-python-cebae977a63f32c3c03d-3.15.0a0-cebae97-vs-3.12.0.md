# Results vs. 3.12.0

- fork: python
- ref: cebae977a63f32c3c03d
- machine: windows-amd64
- commit hash: cebae97
- commit date: 2025-06-01
- overall geometric mean: 1.120x faster
- HPT reliability: 99.86%
- HPT 99th percentile: 1.07x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250601-pythonperf1-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 286 ms: 1.31x slower                                                       |
| docutils       | 1.66 sec                                                    | 2.06 sec: 1.24x slower                                                     |
| Geometric mean | (ref)                                                       | 1.28x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250601-pythonperf1-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 538 ms: 1.43x faster                                                       |
| async_tree_io              | 731 ms                                                      | 536 ms: 1.37x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 280 ms: 1.31x faster                                                       |
| async_tree_none            | 291 ms                                                      | 230 ms: 1.27x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 228 ms: 1.25x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 282 ms: 1.20x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 424 ms: 1.18x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 426 ms: 1.15x faster                                                       |
| Geometric mean             | (ref)                                                       | 1.27x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250601-pythonperf1-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 71.9 ms                                                     | 55.8 ms: 1.29x faster                                                      |
| pidigits       | 152 ms                                                      | 146 ms: 1.04x faster                                                       |
| float          | 56.8 ms                                                     | 78.8 ms: 1.39x slower                                                      |
| Geometric mean | (ref)                                                       | 1.01x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250601-pythonperf1-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_dna      | 126 ms                                                      | 117 ms: 1.08x faster                                                       |
| regex_effbot   | 1.62 ms                                                     | 1.78 ms: 1.10x slower                                                      |
| regex_v8       | 14.2 ms                                                     | 16.4 ms: 1.15x slower                                                      |
| regex_compile  | 87.5 ms                                                     | 112 ms: 1.28x slower                                                       |
| Geometric mean | (ref)                                                       | 1.11x slower                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250601-pythonperf1-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| xml_etree_parse      | 93.0 ms                                                     | 103 ms: 1.11x slower                                                       |
| unpickle_list        | 2.75 us                                                     | 3.07 us: 1.12x slower                                                      |
| tomli_loads          | 1.37 sec                                                    | 1.55 sec: 1.13x slower                                                     |
| unpickle_pure_python | 133 us                                                      | 156 us: 1.17x slower                                                       |
| pickle_dict          | 18.4 us                                                     | 22.0 us: 1.20x slower                                                      |
| xml_etree_generate   | 55.8 ms                                                     | 70.0 ms: 1.25x slower                                                      |
| pickle               | 7.43 us                                                     | 9.47 us: 1.27x slower                                                      |
| xml_etree_iterparse  | 65.2 ms                                                     | 85.0 ms: 1.30x slower                                                      |
| xml_etree_process    | 37.7 ms                                                     | 50.8 ms: 1.35x slower                                                      |
| unpickle             | 8.18 us                                                     | 11.2 us: 1.36x slower                                                      |
| pickle_list          | 2.83 us                                                     | 3.95 us: 1.40x slower                                                      |
| json_loads           | 13.9 us                                                     | 20.4 us: 1.47x slower                                                      |
| json_dumps           | 5.70 ms                                                     | 8.78 ms: 1.54x slower                                                      |
| pickle_pure_python   | 195 us                                                      | 319 us: 1.63x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.30x slower                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250601-pythonperf1-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 20.2 ms: 1.24x slower                                                      |
| python_startup         | 19.5 ms                                                     | 27.2 ms: 1.40x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.32x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250601-pythonperf1-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| django_template | 22.9 ms                                                     | 37.3 ms: 1.63x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.28x slower                                                               |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250601-pythonperf1-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pprint_pformat             | 1.05 sec                                                    | 1.56 us: 669514.61x faster                                                 |
| pprint_safe_repr           | 513 ms                                                      | 904 ns: 567854.89x faster                                                  |
| pathlib                    | 80.5 ms                                                     | 33.9 ms: 2.38x faster                                                      |
| async_tree_io_tg           | 771 ms                                                      | 538 ms: 1.43x faster                                                       |
| asyncio_tcp_ssl            | 2.10 sec                                                    | 1.49 sec: 1.40x faster                                                     |
| async_tree_io              | 731 ms                                                      | 536 ms: 1.37x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 280 ms: 1.31x faster                                                       |
| nbody                      | 71.9 ms                                                     | 55.8 ms: 1.29x faster                                                      |
| async_tree_none            | 291 ms                                                      | 230 ms: 1.27x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 228 ms: 1.25x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 282 ms: 1.20x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 424 ms: 1.18x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 426 ms: 1.15x faster                                                       |
| mdp                        | 1.37 sec                                                    | 1.20 sec: 1.15x faster                                                     |
| regex_dna                  | 126 ms                                                      | 117 ms: 1.08x faster                                                       |
| pidigits                   | 152 ms                                                      | 146 ms: 1.04x faster                                                       |
| sqlite_synth               | 1.76 us                                                     | 1.72 us: 1.02x faster                                                      |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.61 ms: 1.02x slower                                                      |
| comprehensions             | 14.1 us                                                     | 15.5 us: 1.09x slower                                                      |
| regex_effbot               | 1.62 ms                                                     | 1.78 ms: 1.10x slower                                                      |
| meteor_contest             | 74.6 ms                                                     | 82.1 ms: 1.10x slower                                                      |
| xml_etree_parse            | 93.0 ms                                                     | 103 ms: 1.11x slower                                                       |
| unpickle_list              | 2.75 us                                                     | 3.07 us: 1.12x slower                                                      |
| tomli_loads                | 1.37 sec                                                    | 1.55 sec: 1.13x slower                                                     |
| deepcopy                   | 238 us                                                      | 270 us: 1.14x slower                                                       |
| bench_thread_pool          | 857 us                                                      | 977 us: 1.14x slower                                                       |
| regex_v8                   | 14.2 ms                                                     | 16.4 ms: 1.15x slower                                                      |
| asyncio_tcp                | 487 ms                                                      | 560 ms: 1.15x slower                                                       |
| fannkuch                   | 247 ms                                                      | 286 ms: 1.16x slower                                                       |
| unpickle_pure_python       | 133 us                                                      | 156 us: 1.17x slower                                                       |
| dulwich_log                | 44.3 ms                                                     | 52.0 ms: 1.17x slower                                                      |
| pickle_dict                | 18.4 us                                                     | 22.0 us: 1.20x slower                                                      |
| sympy_sum                  | 91.5 ms                                                     | 113 ms: 1.24x slower                                                       |
| docutils                   | 1.66 sec                                                    | 2.06 sec: 1.24x slower                                                     |
| python_startup_no_site     | 16.2 ms                                                     | 20.2 ms: 1.24x slower                                                      |
| telco                      | 4.13 ms                                                     | 5.14 ms: 1.24x slower                                                      |
| xml_etree_generate         | 55.8 ms                                                     | 70.0 ms: 1.25x slower                                                      |
| pickle                     | 7.43 us                                                     | 9.47 us: 1.27x slower                                                      |
| regex_compile              | 87.5 ms                                                     | 112 ms: 1.28x slower                                                       |
| crypto_pyaes               | 48.5 ms                                                     | 62.2 ms: 1.28x slower                                                      |
| sympy_integrate            | 13.0 ms                                                     | 16.7 ms: 1.29x slower                                                      |
| pyflate                    | 295 ms                                                      | 383 ms: 1.30x slower                                                       |
| xml_etree_iterparse        | 65.2 ms                                                     | 85.0 ms: 1.30x slower                                                      |
| 2to3                       | 218 ms                                                      | 286 ms: 1.31x slower                                                       |
| json                       | 3.05 ms                                                     | 4.06 ms: 1.33x slower                                                      |
| pycparser                  | 699 ms                                                      | 932 ms: 1.33x slower                                                       |
| deepcopy_reduce            | 2.09 us                                                     | 2.80 us: 1.34x slower                                                      |
| xml_etree_process          | 37.7 ms                                                     | 50.8 ms: 1.35x slower                                                      |
| sympy_str                  | 175 ms                                                      | 236 ms: 1.35x slower                                                       |
| unpickle                   | 8.18 us                                                     | 11.2 us: 1.36x slower                                                      |
| float                      | 56.8 ms                                                     | 78.8 ms: 1.39x slower                                                      |
| python_startup             | 19.5 ms                                                     | 27.2 ms: 1.40x slower                                                      |
| pickle_list                | 2.83 us                                                     | 3.95 us: 1.40x slower                                                      |
| nqueens                    | 62.8 ms                                                     | 90.5 ms: 1.44x slower                                                      |
| deepcopy_memo              | 23.7 us                                                     | 34.2 us: 1.44x slower                                                      |
| go                         | 91.6 ms                                                     | 133 ms: 1.45x slower                                                       |
| sympy_expand               | 284 ms                                                      | 416 ms: 1.47x slower                                                       |
| logging_format             | 6.72 us                                                     | 9.85 us: 1.47x slower                                                      |
| json_loads                 | 13.9 us                                                     | 20.4 us: 1.47x slower                                                      |
| async_generators           | 239 ms                                                      | 353 ms: 1.47x slower                                                       |
| logging_simple             | 6.28 us                                                     | 9.39 us: 1.50x slower                                                      |
| chaos                      | 43.3 ms                                                     | 65.0 ms: 1.50x slower                                                      |
| bench_mp_pool              | 69.2 ms                                                     | 104 ms: 1.50x slower                                                       |
| typing_runtime_protocols   | 95.1 us                                                     | 144 us: 1.52x slower                                                       |
| json_dumps                 | 5.70 ms                                                     | 8.78 ms: 1.54x slower                                                      |
| raytrace                   | 192 ms                                                      | 299 ms: 1.55x slower                                                       |
| generators                 | 22.5 ms                                                     | 36.5 ms: 1.62x slower                                                      |
| django_template            | 22.9 ms                                                     | 37.3 ms: 1.63x slower                                                      |
| pickle_pure_python         | 195 us                                                      | 319 us: 1.63x slower                                                       |
| scimark_sor                | 78.8 ms                                                     | 131 ms: 1.66x slower                                                       |
| scimark_monte_carlo        | 43.7 ms                                                     | 73.8 ms: 1.69x slower                                                      |
| spectral_norm              | 66.9 ms                                                     | 116 ms: 1.73x slower                                                       |
| coroutines                 | 14.3 ms                                                     | 25.1 ms: 1.76x slower                                                      |
| richards                   | 28.4 ms                                                     | 51.2 ms: 1.81x slower                                                      |
| gc_traversal               | 1.52 ms                                                     | 2.75 ms: 1.81x slower                                                      |
| richards_super             | 32.1 ms                                                     | 58.1 ms: 1.81x slower                                                      |
| hexiom                     | 4.10 ms                                                     | 7.72 ms: 1.88x slower                                                      |
| create_gc_cycles           | 752 us                                                      | 1.43 ms: 1.90x slower                                                      |
| unpack_sequence            | 37.5 ns                                                     | 72.9 ns: 1.95x slower                                                      |
| deltablue                  | 2.16 ms                                                     | 4.29 ms: 1.99x slower                                                      |
| scimark_lu                 | 58.9 ms                                                     | 120 ms: 2.04x slower                                                       |
| logging_silent             | 60.5 ns                                                     | 497 ns: 8.22x slower                                                       |
| coverage                   | 40.8 ms                                                     | 479 ms: 11.74x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.05x faster                                                               |

Benchmark hidden because not significant (2): scimark_fft, mako
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (17) of results/bm-20250601-3.15.0a0-cebae97-JIT/bm-20250601-pythonperf1-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.120x faster

# HPT report

- Reliability score: 99.86% likely to be slow
- 90% likely to have a slowdown of 1.15x
- 95% likely to have a slowdown of 1.13x
- 99% likely to have a slowdown of 1.07x

# Memory
- memory change: unknown
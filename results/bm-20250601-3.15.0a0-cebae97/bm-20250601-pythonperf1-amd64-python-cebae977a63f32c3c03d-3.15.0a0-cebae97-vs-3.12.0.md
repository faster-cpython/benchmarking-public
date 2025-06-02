# Results vs. 3.12.0

- fork: python
- ref: cebae977a63f32c3c03d
- machine: windows-amd64
- commit hash: cebae97
- commit date: 2025-06-01
- overall geometric mean: 1.280x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.26x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250601-pythonperf1-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 292 ms: 1.34x slower                                                       |
| docutils       | 1.66 sec                                                    | 2.06 sec: 1.24x slower                                                     |
| Geometric mean | (ref)                                                       | 1.29x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250601-pythonperf1-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 554 ms: 1.39x faster                                                       |
| async_tree_io              | 731 ms                                                      | 548 ms: 1.34x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 286 ms: 1.28x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 234 ms: 1.22x faster                                                       |
| async_tree_none            | 291 ms                                                      | 242 ms: 1.20x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 296 ms: 1.15x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 439 ms: 1.14x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 443 ms: 1.11x faster                                                       |
| Geometric mean             | (ref)                                                       | 1.23x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250601-pythonperf1-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pidigits       | 152 ms                                                      | 145 ms: 1.05x faster                                                       |
| float          | 56.8 ms                                                     | 77.0 ms: 1.36x slower                                                      |
| nbody          | 71.9 ms                                                     | 105 ms: 1.46x slower                                                       |
| Geometric mean | (ref)                                                       | 1.24x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250601-pythonperf1-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_dna      | 126 ms                                                      | 117 ms: 1.08x faster                                                       |
| regex_effbot   | 1.62 ms                                                     | 1.80 ms: 1.11x slower                                                      |
| regex_v8       | 14.2 ms                                                     | 16.6 ms: 1.17x slower                                                      |
| regex_compile  | 87.5 ms                                                     | 124 ms: 1.42x slower                                                       |
| Geometric mean | (ref)                                                       | 1.14x slower                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250601-pythonperf1-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| unpickle_list        | 2.75 us                                                     | 3.14 us: 1.14x slower                                                      |
| xml_etree_parse      | 93.0 ms                                                     | 108 ms: 1.16x slower                                                       |
| pickle_dict          | 18.4 us                                                     | 22.5 us: 1.22x slower                                                      |
| pickle               | 7.43 us                                                     | 9.46 us: 1.27x slower                                                      |
| xml_etree_iterparse  | 65.2 ms                                                     | 90.2 ms: 1.38x slower                                                      |
| unpickle             | 8.18 us                                                     | 11.4 us: 1.39x slower                                                      |
| pickle_list          | 2.83 us                                                     | 3.96 us: 1.40x slower                                                      |
| json_loads           | 13.9 us                                                     | 20.5 us: 1.47x slower                                                      |
| json_dumps           | 5.70 ms                                                     | 8.73 ms: 1.53x slower                                                      |
| tomli_loads          | 1.37 sec                                                    | 2.10 sec: 1.53x slower                                                     |
| xml_etree_generate   | 55.8 ms                                                     | 89.7 ms: 1.61x slower                                                      |
| xml_etree_process    | 37.7 ms                                                     | 64.8 ms: 1.72x slower                                                      |
| pickle_pure_python   | 195 us                                                      | 359 us: 1.84x slower                                                       |
| unpickle_pure_python | 133 us                                                      | 275 us: 2.06x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.46x slower                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250601-pythonperf1-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 20.2 ms: 1.24x slower                                                      |
| python_startup         | 19.5 ms                                                     | 27.4 ms: 1.41x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.32x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250601-pythonperf1-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| django_template | 22.9 ms                                                     | 37.2 ms: 1.62x slower                                                      |
| mako            | 7.09 ms                                                     | 12.5 ms: 1.77x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.69x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250601-pythonperf1-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pathlib                    | 80.5 ms                                                     | 34.2 ms: 2.35x faster                                                      |
| asyncio_tcp_ssl            | 2.10 sec                                                    | 1.36 sec: 1.54x faster                                                     |
| async_tree_io_tg           | 771 ms                                                      | 554 ms: 1.39x faster                                                       |
| async_tree_io              | 731 ms                                                      | 548 ms: 1.34x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 286 ms: 1.28x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 234 ms: 1.22x faster                                                       |
| async_tree_none            | 291 ms                                                      | 242 ms: 1.20x faster                                                       |
| mdp                        | 1.37 sec                                                    | 1.18 sec: 1.16x faster                                                     |
| asyncio_tcp                | 487 ms                                                      | 422 ms: 1.15x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 296 ms: 1.15x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 439 ms: 1.14x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 443 ms: 1.11x faster                                                       |
| regex_dna                  | 126 ms                                                      | 117 ms: 1.08x faster                                                       |
| pidigits                   | 152 ms                                                      | 145 ms: 1.05x faster                                                       |
| sqlite_synth               | 1.76 us                                                     | 1.87 us: 1.06x slower                                                      |
| deepcopy                   | 238 us                                                      | 265 us: 1.11x slower                                                       |
| regex_effbot               | 1.62 ms                                                     | 1.80 ms: 1.11x slower                                                      |
| unpickle_list              | 2.75 us                                                     | 3.14 us: 1.14x slower                                                      |
| dulwich_log                | 44.3 ms                                                     | 51.1 ms: 1.15x slower                                                      |
| xml_etree_parse            | 93.0 ms                                                     | 108 ms: 1.16x slower                                                       |
| regex_v8                   | 14.2 ms                                                     | 16.6 ms: 1.17x slower                                                      |
| bench_thread_pool          | 857 us                                                      | 1.00 ms: 1.17x slower                                                      |
| pickle_dict                | 18.4 us                                                     | 22.5 us: 1.22x slower                                                      |
| python_startup_no_site     | 16.2 ms                                                     | 20.2 ms: 1.24x slower                                                      |
| docutils                   | 1.66 sec                                                    | 2.06 sec: 1.24x slower                                                     |
| sympy_sum                  | 91.5 ms                                                     | 115 ms: 1.26x slower                                                       |
| meteor_contest             | 74.6 ms                                                     | 94.4 ms: 1.27x slower                                                      |
| pickle                     | 7.43 us                                                     | 9.46 us: 1.27x slower                                                      |
| sympy_integrate            | 13.0 ms                                                     | 16.6 ms: 1.28x slower                                                      |
| json                       | 3.05 ms                                                     | 3.94 ms: 1.29x slower                                                      |
| deepcopy_reduce            | 2.09 us                                                     | 2.74 us: 1.31x slower                                                      |
| sympy_str                  | 175 ms                                                      | 234 ms: 1.33x slower                                                       |
| 2to3                       | 218 ms                                                      | 292 ms: 1.34x slower                                                       |
| float                      | 56.8 ms                                                     | 77.0 ms: 1.36x slower                                                      |
| xml_etree_iterparse        | 65.2 ms                                                     | 90.2 ms: 1.38x slower                                                      |
| comprehensions             | 14.1 us                                                     | 19.6 us: 1.39x slower                                                      |
| unpickle                   | 8.18 us                                                     | 11.4 us: 1.39x slower                                                      |
| pickle_list                | 2.83 us                                                     | 3.96 us: 1.40x slower                                                      |
| deepcopy_memo              | 23.7 us                                                     | 33.3 us: 1.40x slower                                                      |
| python_startup             | 19.5 ms                                                     | 27.4 ms: 1.41x slower                                                      |
| pycparser                  | 699 ms                                                      | 985 ms: 1.41x slower                                                       |
| sympy_expand               | 284 ms                                                      | 400 ms: 1.41x slower                                                       |
| regex_compile              | 87.5 ms                                                     | 124 ms: 1.42x slower                                                       |
| async_generators           | 239 ms                                                      | 343 ms: 1.43x slower                                                       |
| go                         | 91.6 ms                                                     | 133 ms: 1.46x slower                                                       |
| nbody                      | 71.9 ms                                                     | 105 ms: 1.46x slower                                                       |
| logging_format             | 6.72 us                                                     | 9.89 us: 1.47x slower                                                      |
| json_loads                 | 13.9 us                                                     | 20.5 us: 1.47x slower                                                      |
| scimark_fft                | 184 ms                                                      | 274 ms: 1.49x slower                                                       |
| logging_simple             | 6.28 us                                                     | 9.36 us: 1.49x slower                                                      |
| bench_mp_pool              | 69.2 ms                                                     | 103 ms: 1.49x slower                                                       |
| nqueens                    | 62.8 ms                                                     | 94.2 ms: 1.50x slower                                                      |
| telco                      | 4.13 ms                                                     | 6.25 ms: 1.51x slower                                                      |
| chaos                      | 43.3 ms                                                     | 65.8 ms: 1.52x slower                                                      |
| generators                 | 22.5 ms                                                     | 34.3 ms: 1.52x slower                                                      |
| json_dumps                 | 5.70 ms                                                     | 8.73 ms: 1.53x slower                                                      |
| tomli_loads                | 1.37 sec                                                    | 2.10 sec: 1.53x slower                                                     |
| pyflate                    | 295 ms                                                      | 455 ms: 1.54x slower                                                       |
| raytrace                   | 192 ms                                                      | 302 ms: 1.57x slower                                                       |
| xml_etree_generate         | 55.8 ms                                                     | 89.7 ms: 1.61x slower                                                      |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 4.14 ms: 1.62x slower                                                      |
| django_template            | 22.9 ms                                                     | 37.2 ms: 1.62x slower                                                      |
| typing_runtime_protocols   | 95.1 us                                                     | 155 us: 1.63x slower                                                       |
| crypto_pyaes               | 48.5 ms                                                     | 79.3 ms: 1.63x slower                                                      |
| pprint_safe_repr           | 513 ms                                                      | 848 ms: 1.65x slower                                                       |
| scimark_monte_carlo        | 43.7 ms                                                     | 72.5 ms: 1.66x slower                                                      |
| pprint_pformat             | 1.05 sec                                                    | 1.74 sec: 1.66x slower                                                     |
| scimark_sor                | 78.8 ms                                                     | 133 ms: 1.68x slower                                                       |
| fannkuch                   | 247 ms                                                      | 420 ms: 1.70x slower                                                       |
| xml_etree_process          | 37.7 ms                                                     | 64.8 ms: 1.72x slower                                                      |
| spectral_norm              | 66.9 ms                                                     | 117 ms: 1.75x slower                                                       |
| mako                       | 7.09 ms                                                     | 12.5 ms: 1.77x slower                                                      |
| richards_super             | 32.1 ms                                                     | 57.4 ms: 1.79x slower                                                      |
| richards                   | 28.4 ms                                                     | 50.8 ms: 1.79x slower                                                      |
| coroutines                 | 14.3 ms                                                     | 25.6 ms: 1.80x slower                                                      |
| hexiom                     | 4.10 ms                                                     | 7.39 ms: 1.80x slower                                                      |
| pickle_pure_python         | 195 us                                                      | 359 us: 1.84x slower                                                       |
| gc_traversal               | 1.52 ms                                                     | 2.82 ms: 1.85x slower                                                      |
| create_gc_cycles           | 752 us                                                      | 1.45 ms: 1.92x slower                                                      |
| scimark_lu                 | 58.9 ms                                                     | 117 ms: 1.99x slower                                                       |
| deltablue                  | 2.16 ms                                                     | 4.31 ms: 2.00x slower                                                      |
| unpickle_pure_python       | 133 us                                                      | 275 us: 2.06x slower                                                       |
| unpack_sequence            | 37.5 ns                                                     | 81.9 ns: 2.19x slower                                                      |
| logging_silent             | 60.5 ns                                                     | 494 ns: 8.17x slower                                                       |
| coverage                   | 40.8 ms                                                     | 475 ms: 11.63x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.40x slower                                                               |
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (17) of results/bm-20250601-3.15.0a0-cebae97/bm-20250601-pythonperf1-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.280x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.34x
- 95% likely to have a slowdown of 1.32x
- 99% likely to have a slowdown of 1.26x

# Memory
- memory change: unknown
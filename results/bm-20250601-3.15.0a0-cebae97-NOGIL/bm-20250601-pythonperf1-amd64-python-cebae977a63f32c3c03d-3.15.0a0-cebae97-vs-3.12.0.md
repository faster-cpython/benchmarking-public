# Results vs. 3.12.0

- fork: python
- ref: cebae977a63f32c3c03d
- machine: windows-amd64
- commit hash: cebae97
- commit date: 2025-06-01
- overall geometric mean: 1.406x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.54x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250601-pythonperf1-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 338 ms: 1.55x slower                                                       |
| docutils       | 1.66 sec                                                    | 4.14 sec: 2.50x slower                                                     |
| Geometric mean | (ref)                                                       | 1.97x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250601-pythonperf1-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 549 ms: 1.41x faster                                                       |
| async_tree_io              | 731 ms                                                      | 575 ms: 1.27x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 310 ms: 1.18x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 246 ms: 1.16x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 452 ms: 1.11x faster                                                       |
| async_tree_none            | 291 ms                                                      | 273 ms: 1.07x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 480 ms: 1.02x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 333 ms: 1.02x faster                                                       |
| Geometric mean             | (ref)                                                       | 1.15x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250601-pythonperf1-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pidigits       | 152 ms                                                      | 141 ms: 1.08x faster                                                       |
| float          | 56.8 ms                                                     | 97.2 ms: 1.71x slower                                                      |
| nbody          | 71.9 ms                                                     | 179 ms: 2.50x slower                                                       |
| Geometric mean | (ref)                                                       | 1.58x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250601-pythonperf1-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_dna      | 126 ms                                                      | 113 ms: 1.12x faster                                                       |
| regex_effbot   | 1.62 ms                                                     | 1.82 ms: 1.12x slower                                                      |
| regex_v8       | 14.2 ms                                                     | 16.9 ms: 1.18x slower                                                      |
| regex_compile  | 87.5 ms                                                     | 160 ms: 1.83x slower                                                       |
| Geometric mean | (ref)                                                       | 1.22x slower                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250601-pythonperf1-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pickle_dict          | 18.4 us                                                     | 21.3 us: 1.16x slower                                                      |
| xml_etree_parse      | 93.0 ms                                                     | 111 ms: 1.19x slower                                                       |
| unpickle_list        | 2.75 us                                                     | 3.47 us: 1.26x slower                                                      |
| pickle               | 7.43 us                                                     | 9.53 us: 1.28x slower                                                      |
| pickle_list          | 2.83 us                                                     | 3.73 us: 1.32x slower                                                      |
| xml_etree_iterparse  | 65.2 ms                                                     | 93.9 ms: 1.44x slower                                                      |
| unpickle             | 8.18 us                                                     | 12.7 us: 1.55x slower                                                      |
| json_loads           | 13.9 us                                                     | 22.3 us: 1.61x slower                                                      |
| json_dumps           | 5.70 ms                                                     | 9.47 ms: 1.66x slower                                                      |
| xml_etree_generate   | 55.8 ms                                                     | 110 ms: 1.98x slower                                                       |
| xml_etree_process    | 37.7 ms                                                     | 79.8 ms: 2.12x slower                                                      |
| pickle_pure_python   | 195 us                                                      | 454 us: 2.32x slower                                                       |
| unpickle_pure_python | 133 us                                                      | 364 us: 2.74x slower                                                       |
| tomli_loads          | 1.37 sec                                                    | 5.09 sec: 3.72x slower                                                     |
| Geometric mean       | (ref)                                                       | 1.70x slower                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250601-pythonperf1-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 20.2 ms: 1.24x slower                                                      |
| python_startup         | 19.5 ms                                                     | 27.9 ms: 1.43x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.33x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250601-pythonperf1-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| django_template | 22.9 ms                                                     | 45.9 ms: 2.00x slower                                                      |
| mako            | 7.09 ms                                                     | 16.9 ms: 2.39x slower                                                      |
| Geometric mean  | (ref)                                                       | 2.19x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250601-pythonperf1-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pathlib                    | 80.5 ms                                                     | 35.3 ms: 2.28x faster                                                      |
| async_tree_io_tg           | 771 ms                                                      | 549 ms: 1.41x faster                                                       |
| async_tree_io              | 731 ms                                                      | 575 ms: 1.27x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 310 ms: 1.18x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 246 ms: 1.16x faster                                                       |
| regex_dna                  | 126 ms                                                      | 113 ms: 1.12x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 452 ms: 1.11x faster                                                       |
| pidigits                   | 152 ms                                                      | 141 ms: 1.08x faster                                                       |
| async_tree_none            | 291 ms                                                      | 273 ms: 1.07x faster                                                       |
| sqlite_synth               | 1.76 us                                                     | 1.69 us: 1.04x faster                                                      |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 480 ms: 1.02x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 333 ms: 1.02x faster                                                       |
| asyncio_tcp                | 487 ms                                                      | 539 ms: 1.11x slower                                                       |
| regex_effbot               | 1.62 ms                                                     | 1.82 ms: 1.12x slower                                                      |
| pickle_dict                | 18.4 us                                                     | 21.3 us: 1.16x slower                                                      |
| regex_v8                   | 14.2 ms                                                     | 16.9 ms: 1.18x slower                                                      |
| gc_traversal               | 1.52 ms                                                     | 1.80 ms: 1.18x slower                                                      |
| xml_etree_parse            | 93.0 ms                                                     | 111 ms: 1.19x slower                                                       |
| asyncio_tcp_ssl            | 2.10 sec                                                    | 2.56 sec: 1.22x slower                                                     |
| python_startup_no_site     | 16.2 ms                                                     | 20.2 ms: 1.24x slower                                                      |
| unpickle_list              | 2.75 us                                                     | 3.47 us: 1.26x slower                                                      |
| bench_mp_pool              | 69.2 ms                                                     | 88.6 ms: 1.28x slower                                                      |
| pickle                     | 7.43 us                                                     | 9.53 us: 1.28x slower                                                      |
| dulwich_log                | 44.3 ms                                                     | 56.8 ms: 1.28x slower                                                      |
| pickle_list                | 2.83 us                                                     | 3.73 us: 1.32x slower                                                      |
| json                       | 3.05 ms                                                     | 4.14 ms: 1.36x slower                                                      |
| deepcopy                   | 238 us                                                      | 334 us: 1.40x slower                                                       |
| python_startup             | 19.5 ms                                                     | 27.9 ms: 1.43x slower                                                      |
| xml_etree_iterparse        | 65.2 ms                                                     | 93.9 ms: 1.44x slower                                                      |
| bench_thread_pool          | 857 us                                                      | 1.24 ms: 1.45x slower                                                      |
| create_gc_cycles           | 752 us                                                      | 1.13 ms: 1.50x slower                                                      |
| 2to3                       | 218 ms                                                      | 338 ms: 1.55x slower                                                       |
| unpickle                   | 8.18 us                                                     | 12.7 us: 1.55x slower                                                      |
| sympy_sum                  | 91.5 ms                                                     | 145 ms: 1.58x slower                                                       |
| json_loads                 | 13.9 us                                                     | 22.3 us: 1.61x slower                                                      |
| meteor_contest             | 74.6 ms                                                     | 120 ms: 1.61x slower                                                       |
| sympy_integrate            | 13.0 ms                                                     | 20.9 ms: 1.62x slower                                                      |
| deepcopy_reduce            | 2.09 us                                                     | 3.48 us: 1.66x slower                                                      |
| json_dumps                 | 5.70 ms                                                     | 9.47 ms: 1.66x slower                                                      |
| sympy_str                  | 175 ms                                                      | 292 ms: 1.67x slower                                                       |
| mdp                        | 1.37 sec                                                    | 2.30 sec: 1.68x slower                                                     |
| float                      | 56.8 ms                                                     | 97.2 ms: 1.71x slower                                                      |
| async_generators           | 239 ms                                                      | 412 ms: 1.72x slower                                                       |
| sympy_expand               | 284 ms                                                      | 491 ms: 1.73x slower                                                       |
| generators                 | 22.5 ms                                                     | 39.3 ms: 1.75x slower                                                      |
| logging_format             | 6.72 us                                                     | 11.8 us: 1.76x slower                                                      |
| logging_simple             | 6.28 us                                                     | 11.2 us: 1.78x slower                                                      |
| regex_compile              | 87.5 ms                                                     | 160 ms: 1.83x slower                                                       |
| comprehensions             | 14.1 us                                                     | 25.9 us: 1.83x slower                                                      |
| deepcopy_memo              | 23.7 us                                                     | 43.7 us: 1.84x slower                                                      |
| telco                      | 4.13 ms                                                     | 8.09 ms: 1.96x slower                                                      |
| xml_etree_generate         | 55.8 ms                                                     | 110 ms: 1.98x slower                                                       |
| django_template            | 22.9 ms                                                     | 45.9 ms: 2.00x slower                                                      |
| nqueens                    | 62.8 ms                                                     | 127 ms: 2.03x slower                                                       |
| go                         | 91.6 ms                                                     | 189 ms: 2.06x slower                                                       |
| coverage                   | 40.8 ms                                                     | 84.5 ms: 2.07x slower                                                      |
| raytrace                   | 192 ms                                                      | 403 ms: 2.09x slower                                                       |
| xml_etree_process          | 37.7 ms                                                     | 79.8 ms: 2.12x slower                                                      |
| typing_runtime_protocols   | 95.1 us                                                     | 202 us: 2.12x slower                                                       |
| pyflate                    | 295 ms                                                      | 626 ms: 2.12x slower                                                       |
| chaos                      | 43.3 ms                                                     | 95.4 ms: 2.20x slower                                                      |
| unpack_sequence            | 37.5 ns                                                     | 82.8 ns: 2.21x slower                                                      |
| scimark_fft                | 184 ms                                                      | 415 ms: 2.25x slower                                                       |
| coroutines                 | 14.3 ms                                                     | 32.4 ms: 2.27x slower                                                      |
| pickle_pure_python         | 195 us                                                      | 454 us: 2.32x slower                                                       |
| mako                       | 7.09 ms                                                     | 16.9 ms: 2.39x slower                                                      |
| scimark_sor                | 78.8 ms                                                     | 190 ms: 2.41x slower                                                       |
| fannkuch                   | 247 ms                                                      | 596 ms: 2.42x slower                                                       |
| scimark_monte_carlo        | 43.7 ms                                                     | 107 ms: 2.45x slower                                                       |
| richards                   | 28.4 ms                                                     | 69.7 ms: 2.46x slower                                                      |
| richards_super             | 32.1 ms                                                     | 79.2 ms: 2.47x slower                                                      |
| crypto_pyaes               | 48.5 ms                                                     | 120 ms: 2.47x slower                                                       |
| pycparser                  | 699 ms                                                      | 1.73 sec: 2.48x slower                                                     |
| docutils                   | 1.66 sec                                                    | 4.14 sec: 2.50x slower                                                     |
| nbody                      | 71.9 ms                                                     | 179 ms: 2.50x slower                                                       |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 6.43 ms: 2.52x slower                                                      |
| spectral_norm              | 66.9 ms                                                     | 170 ms: 2.53x slower                                                       |
| hexiom                     | 4.10 ms                                                     | 10.6 ms: 2.60x slower                                                      |
| deltablue                  | 2.16 ms                                                     | 5.88 ms: 2.72x slower                                                      |
| unpickle_pure_python       | 133 us                                                      | 364 us: 2.74x slower                                                       |
| scimark_lu                 | 58.9 ms                                                     | 167 ms: 2.83x slower                                                       |
| pprint_safe_repr           | 513 ms                                                      | 1.50 sec: 2.92x slower                                                     |
| tomli_loads                | 1.37 sec                                                    | 5.09 sec: 3.72x slower                                                     |
| pprint_pformat             | 1.05 sec                                                    | 4.25 sec: 4.06x slower                                                     |
| logging_silent             | 60.5 ns                                                     | 577 ns: 9.53x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.69x slower                                                               |
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (17) of results/bm-20250601-3.15.0a0-cebae97-NOGIL/bm-20250601-pythonperf1-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.406x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.67x
- 95% likely to have a slowdown of 1.62x
- 99% likely to have a slowdown of 1.54x

# Memory
- memory change: unknown
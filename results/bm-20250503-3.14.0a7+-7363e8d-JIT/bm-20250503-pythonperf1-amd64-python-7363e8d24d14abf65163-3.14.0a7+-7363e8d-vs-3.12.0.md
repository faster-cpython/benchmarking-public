# Results vs. 3.12.0

- fork: python
- ref: 7363e8d24d14abf65163
- machine: windows-amd64
- commit hash: 7363e8d
- commit date: 2025-05-03
- overall geometric mean: 1.086x faster
- HPT reliability: 99.94%
- HPT 99th percentile: 1.01x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250503-pythonperf1-amd64-python-7363e8d24d14abf65163-3.14.0a7+-7363e8d |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 223 ms: 1.02x slower                                                        |
| docutils       | 1.66 sec                                                    | 1.72 sec: 1.03x slower                                                      |
| Geometric mean | (ref)                                                       | 1.03x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250503-pythonperf1-amd64-python-7363e8d24d14abf65163-3.14.0a7+-7363e8d |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 400 ms: 1.93x faster                                                        |
| async_tree_io              | 731 ms                                                      | 415 ms: 1.76x faster                                                        |
| async_tree_memoization_tg  | 367 ms                                                      | 211 ms: 1.74x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 172 ms: 1.66x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 207 ms: 1.64x faster                                                        |
| async_tree_none            | 291 ms                                                      | 181 ms: 1.61x faster                                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 341 ms: 1.47x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 335 ms: 1.46x faster                                                        |
| Geometric mean             | (ref)                                                       | 1.65x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250503-pythonperf1-amd64-python-7363e8d24d14abf65163-3.14.0a7+-7363e8d |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 71.9 ms                                                     | 56.9 ms: 1.26x faster                                                       |
| float          | 56.8 ms                                                     | 45.3 ms: 1.25x faster                                                       |
| pidigits       | 152 ms                                                      | 149 ms: 1.02x faster                                                        |
| Geometric mean | (ref)                                                       | 1.17x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250503-pythonperf1-amd64-python-7363e8d24d14abf65163-3.14.0a7+-7363e8d |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 87.5 ms                                                     | 81.5 ms: 1.07x faster                                                       |
| regex_effbot   | 1.62 ms                                                     | 1.58 ms: 1.03x faster                                                       |
| regex_dna      | 126 ms                                                      | 123 ms: 1.02x faster                                                        |
| Geometric mean | (ref)                                                       | 1.03x faster                                                                |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250503-pythonperf1-amd64-python-7363e8d24d14abf65163-3.14.0a7+-7363e8d |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 1.37 sec                                                    | 1.22 sec: 1.12x faster                                                      |
| unpickle_pure_python | 133 us                                                      | 119 us: 1.12x faster                                                        |
| xml_etree_generate   | 55.8 ms                                                     | 51.7 ms: 1.08x faster                                                       |
| xml_etree_parse      | 93.0 ms                                                     | 90.0 ms: 1.03x faster                                                       |
| xml_etree_process    | 37.7 ms                                                     | 36.5 ms: 1.03x faster                                                       |
| xml_etree_iterparse  | 65.2 ms                                                     | 64.1 ms: 1.02x faster                                                       |
| unpickle_list        | 2.75 us                                                     | 2.86 us: 1.04x slower                                                       |
| unpickle             | 8.18 us                                                     | 8.61 us: 1.05x slower                                                       |
| json_loads           | 13.9 us                                                     | 14.9 us: 1.07x slower                                                       |
| pickle_dict          | 18.4 us                                                     | 19.7 us: 1.07x slower                                                       |
| pickle               | 7.43 us                                                     | 7.97 us: 1.07x slower                                                       |
| pickle_pure_python   | 195 us                                                      | 215 us: 1.10x slower                                                        |
| json_dumps           | 5.70 ms                                                     | 6.74 ms: 1.18x slower                                                       |
| pickle_list          | 2.83 us                                                     | 3.38 us: 1.20x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.03x slower                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250503-pythonperf1-amd64-python-7363e8d24d14abf65163-3.14.0a7+-7363e8d |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 19.2 ms: 1.18x slower                                                       |
| python_startup         | 19.5 ms                                                     | 25.7 ms: 1.32x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.25x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250503-pythonperf1-amd64-python-7363e8d24d14abf65163-3.14.0a7+-7363e8d |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 5.60 ms: 1.27x faster                                                       |
| django_template | 22.9 ms                                                     | 24.7 ms: 1.07x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.09x faster                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250503-pythonperf1-amd64-python-7363e8d24d14abf65163-3.14.0a7+-7363e8d |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pathlib                    | 80.5 ms                                                     | 32.1 ms: 2.50x faster                                                       |
| async_tree_io_tg           | 771 ms                                                      | 400 ms: 1.93x faster                                                        |
| async_tree_io              | 731 ms                                                      | 415 ms: 1.76x faster                                                        |
| async_tree_memoization_tg  | 367 ms                                                      | 211 ms: 1.74x faster                                                        |
| mdp                        | 1.37 sec                                                    | 817 ms: 1.68x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 172 ms: 1.66x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 207 ms: 1.64x faster                                                        |
| async_tree_none            | 291 ms                                                      | 181 ms: 1.61x faster                                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 341 ms: 1.47x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 335 ms: 1.46x faster                                                        |
| asyncio_tcp_ssl            | 2.10 sec                                                    | 1.47 sec: 1.42x faster                                                      |
| deepcopy                   | 238 us                                                      | 181 us: 1.31x faster                                                        |
| mako                       | 7.09 ms                                                     | 5.60 ms: 1.27x faster                                                       |
| nbody                      | 71.9 ms                                                     | 56.9 ms: 1.26x faster                                                       |
| float                      | 56.8 ms                                                     | 45.3 ms: 1.25x faster                                                       |
| comprehensions             | 14.1 us                                                     | 11.9 us: 1.19x faster                                                       |
| scimark_fft                | 184 ms                                                      | 162 ms: 1.14x faster                                                        |
| go                         | 91.6 ms                                                     | 80.7 ms: 1.13x faster                                                       |
| sqlite_synth               | 1.76 us                                                     | 1.56 us: 1.13x faster                                                       |
| generators                 | 22.5 ms                                                     | 19.9 ms: 1.13x faster                                                       |
| tomli_loads                | 1.37 sec                                                    | 1.22 sec: 1.12x faster                                                      |
| pyflate                    | 295 ms                                                      | 263 ms: 1.12x faster                                                        |
| unpickle_pure_python       | 133 us                                                      | 119 us: 1.12x faster                                                        |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.30 ms: 1.11x faster                                                       |
| deepcopy_memo              | 23.7 us                                                     | 21.6 us: 1.10x faster                                                       |
| pprint_pformat             | 1.05 sec                                                    | 957 ms: 1.09x faster                                                        |
| deepcopy_reduce            | 2.09 us                                                     | 1.92 us: 1.09x faster                                                       |
| chaos                      | 43.3 ms                                                     | 39.8 ms: 1.09x faster                                                       |
| xml_etree_generate         | 55.8 ms                                                     | 51.7 ms: 1.08x faster                                                       |
| regex_compile              | 87.5 ms                                                     | 81.5 ms: 1.07x faster                                                       |
| raytrace                   | 192 ms                                                      | 179 ms: 1.07x faster                                                        |
| pprint_safe_repr           | 513 ms                                                      | 486 ms: 1.06x faster                                                        |
| spectral_norm              | 66.9 ms                                                     | 63.6 ms: 1.05x faster                                                       |
| logging_silent             | 60.5 ns                                                     | 57.7 ns: 1.05x faster                                                       |
| crypto_pyaes               | 48.5 ms                                                     | 46.6 ms: 1.04x faster                                                       |
| xml_etree_parse            | 93.0 ms                                                     | 90.0 ms: 1.03x faster                                                       |
| xml_etree_process          | 37.7 ms                                                     | 36.5 ms: 1.03x faster                                                       |
| regex_effbot               | 1.62 ms                                                     | 1.58 ms: 1.03x faster                                                       |
| sympy_sum                  | 91.5 ms                                                     | 89.2 ms: 1.03x faster                                                       |
| dulwich_log                | 44.3 ms                                                     | 43.2 ms: 1.03x faster                                                       |
| regex_dna                  | 126 ms                                                      | 123 ms: 1.02x faster                                                        |
| scimark_monte_carlo        | 43.7 ms                                                     | 42.7 ms: 1.02x faster                                                       |
| pidigits                   | 152 ms                                                      | 149 ms: 1.02x faster                                                        |
| nqueens                    | 62.8 ms                                                     | 61.6 ms: 1.02x faster                                                       |
| xml_etree_iterparse        | 65.2 ms                                                     | 64.1 ms: 1.02x faster                                                       |
| sympy_integrate            | 13.0 ms                                                     | 12.9 ms: 1.00x faster                                                       |
| coroutines                 | 14.3 ms                                                     | 14.3 ms: 1.01x slower                                                       |
| logging_format             | 6.72 us                                                     | 6.75 us: 1.01x slower                                                       |
| fannkuch                   | 247 ms                                                      | 249 ms: 1.01x slower                                                        |
| json                       | 3.05 ms                                                     | 3.10 ms: 1.02x slower                                                       |
| scimark_lu                 | 58.9 ms                                                     | 59.9 ms: 1.02x slower                                                       |
| deltablue                  | 2.16 ms                                                     | 2.21 ms: 1.02x slower                                                       |
| 2to3                       | 218 ms                                                      | 223 ms: 1.02x slower                                                        |
| bench_thread_pool          | 857 us                                                      | 878 us: 1.02x slower                                                        |
| async_generators           | 239 ms                                                      | 247 ms: 1.03x slower                                                        |
| docutils                   | 1.66 sec                                                    | 1.72 sec: 1.03x slower                                                      |
| meteor_contest             | 74.6 ms                                                     | 77.3 ms: 1.04x slower                                                       |
| unpickle_list              | 2.75 us                                                     | 2.86 us: 1.04x slower                                                       |
| unpickle                   | 8.18 us                                                     | 8.61 us: 1.05x slower                                                       |
| pycparser                  | 699 ms                                                      | 739 ms: 1.06x slower                                                        |
| json_loads                 | 13.9 us                                                     | 14.9 us: 1.07x slower                                                       |
| sympy_expand               | 284 ms                                                      | 304 ms: 1.07x slower                                                        |
| telco                      | 4.13 ms                                                     | 4.42 ms: 1.07x slower                                                       |
| pickle_dict                | 18.4 us                                                     | 19.7 us: 1.07x slower                                                       |
| pickle                     | 7.43 us                                                     | 7.97 us: 1.07x slower                                                       |
| django_template            | 22.9 ms                                                     | 24.7 ms: 1.07x slower                                                       |
| hexiom                     | 4.10 ms                                                     | 4.44 ms: 1.08x slower                                                       |
| unpack_sequence            | 37.5 ns                                                     | 40.9 ns: 1.09x slower                                                       |
| pickle_pure_python         | 195 us                                                      | 215 us: 1.10x slower                                                        |
| asyncio_tcp                | 487 ms                                                      | 540 ms: 1.11x slower                                                        |
| python_startup_no_site     | 16.2 ms                                                     | 19.2 ms: 1.18x slower                                                       |
| json_dumps                 | 5.70 ms                                                     | 6.74 ms: 1.18x slower                                                       |
| typing_runtime_protocols   | 95.1 us                                                     | 114 us: 1.20x slower                                                        |
| pickle_list                | 2.83 us                                                     | 3.38 us: 1.20x slower                                                       |
| coverage                   | 40.8 ms                                                     | 51.4 ms: 1.26x slower                                                       |
| bench_mp_pool              | 69.2 ms                                                     | 89.7 ms: 1.30x slower                                                       |
| python_startup             | 19.5 ms                                                     | 25.7 ms: 1.32x slower                                                       |
| gc_traversal               | 1.52 ms                                                     | 2.08 ms: 1.37x slower                                                       |
| create_gc_cycles           | 752 us                                                      | 1.26 ms: 1.67x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.07x faster                                                                |

Benchmark hidden because not significant (6): sympy_str, richards, logging_simple, scimark_sor, richards_super, regex_v8
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20250503-3.14.0a7+-7363e8d-JIT/bm-20250503-pythonperf1-amd64-python-7363e8d24d14abf65163-3.14.0a7+-7363e8d.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.086x faster

# HPT report

- Reliability score: 99.94% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: unknown
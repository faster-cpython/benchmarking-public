# Results vs. 3.12.0

- fork: python
- ref: 7363e8d24d14abf65163
- machine: windows-amd64
- commit hash: 7363e8d
- commit date: 2025-05-03
- overall geometric mean: 1.255x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.17x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250503-pythonperf1-amd64-python-7363e8d24d14abf65163-3.14.0a7+-7363e8d |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 205 ms: 1.06x faster                                                        |
| docutils       | 1.66 sec                                                    | 1.59 sec: 1.05x faster                                                      |
| Geometric mean | (ref)                                                       | 1.06x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250503-pythonperf1-amd64-python-7363e8d24d14abf65163-3.14.0a7+-7363e8d |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 355 ms: 2.17x faster                                                        |
| async_tree_io              | 731 ms                                                      | 347 ms: 2.11x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 149 ms: 1.91x faster                                                        |
| async_tree_memoization_tg  | 367 ms                                                      | 196 ms: 1.87x faster                                                        |
| async_tree_none            | 291 ms                                                      | 157 ms: 1.86x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 184 ms: 1.84x faster                                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 322 ms: 1.56x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 317 ms: 1.54x faster                                                        |
| Geometric mean             | (ref)                                                       | 1.85x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250503-pythonperf1-amd64-python-7363e8d24d14abf65163-3.14.0a7+-7363e8d |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 37.9 ms: 1.50x faster                                                       |
| nbody          | 71.9 ms                                                     | 52.2 ms: 1.38x faster                                                       |
| pidigits       | 152 ms                                                      | 146 ms: 1.04x faster                                                        |
| Geometric mean | (ref)                                                       | 1.29x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250503-pythonperf1-amd64-python-7363e8d24d14abf65163-3.14.0a7+-7363e8d |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 87.5 ms                                                     | 68.6 ms: 1.28x faster                                                       |
| regex_v8       | 14.2 ms                                                     | 13.8 ms: 1.03x faster                                                       |
| regex_dna      | 126 ms                                                      | 127 ms: 1.01x slower                                                        |
| regex_effbot   | 1.62 ms                                                     | 1.76 ms: 1.09x slower                                                       |
| Geometric mean | (ref)                                                       | 1.05x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250503-pythonperf1-amd64-python-7363e8d24d14abf65163-3.14.0a7+-7363e8d |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pickle_dict          | 18.4 us                                                     | 12.2 us: 1.51x faster                                                       |
| pickle_list          | 2.83 us                                                     | 2.16 us: 1.31x faster                                                       |
| tomli_loads          | 1.37 sec                                                    | 1.06 sec: 1.30x faster                                                      |
| unpickle_pure_python | 133 us                                                      | 104 us: 1.28x faster                                                        |
| unpickle_list        | 2.75 us                                                     | 2.30 us: 1.20x faster                                                       |
| pickle               | 7.43 us                                                     | 6.22 us: 1.20x faster                                                       |
| pickle_pure_python   | 195 us                                                      | 169 us: 1.16x faster                                                        |
| xml_etree_generate   | 55.8 ms                                                     | 48.3 ms: 1.16x faster                                                       |
| xml_etree_process    | 37.7 ms                                                     | 33.5 ms: 1.13x faster                                                       |
| unpickle             | 8.18 us                                                     | 7.73 us: 1.06x faster                                                       |
| xml_etree_iterparse  | 65.2 ms                                                     | 63.2 ms: 1.03x faster                                                       |
| xml_etree_parse      | 93.0 ms                                                     | 93.8 ms: 1.01x slower                                                       |
| json_dumps           | 5.70 ms                                                     | 5.79 ms: 1.02x slower                                                       |
| json_loads           | 13.9 us                                                     | 14.4 us: 1.04x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.15x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250503-pythonperf1-amd64-python-7363e8d24d14abf65163-3.14.0a7+-7363e8d |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 20.2 ms: 1.24x slower                                                       |
| python_startup         | 19.5 ms                                                     | 27.0 ms: 1.38x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.31x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250503-pythonperf1-amd64-python-7363e8d24d14abf65163-3.14.0a7+-7363e8d |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 5.93 ms: 1.19x faster                                                       |
| django_template | 22.9 ms                                                     | 20.0 ms: 1.15x faster                                                       |
| Geometric mean  | (ref)                                                       | 1.17x faster                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250503-pythonperf1-amd64-python-7363e8d24d14abf65163-3.14.0a7+-7363e8d |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pathlib                    | 80.5 ms                                                     | 30.7 ms: 2.62x faster                                                       |
| async_tree_io_tg           | 771 ms                                                      | 355 ms: 2.17x faster                                                        |
| async_tree_io              | 731 ms                                                      | 347 ms: 2.11x faster                                                        |
| mdp                        | 1.37 sec                                                    | 682 ms: 2.01x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 149 ms: 1.91x faster                                                        |
| async_tree_memoization_tg  | 367 ms                                                      | 196 ms: 1.87x faster                                                        |
| async_tree_none            | 291 ms                                                      | 157 ms: 1.86x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 184 ms: 1.84x faster                                                        |
| deepcopy_memo              | 23.7 us                                                     | 13.4 us: 1.77x faster                                                       |
| deepcopy                   | 238 us                                                      | 141 us: 1.69x faster                                                        |
| comprehensions             | 14.1 us                                                     | 8.59 us: 1.64x faster                                                       |
| scimark_sor                | 78.8 ms                                                     | 49.0 ms: 1.61x faster                                                       |
| asyncio_tcp_ssl            | 2.10 sec                                                    | 1.33 sec: 1.58x faster                                                      |
| scimark_monte_carlo        | 43.7 ms                                                     | 28.0 ms: 1.56x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 322 ms: 1.56x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 317 ms: 1.54x faster                                                        |
| go                         | 91.6 ms                                                     | 59.7 ms: 1.53x faster                                                       |
| generators                 | 22.5 ms                                                     | 14.8 ms: 1.52x faster                                                       |
| pickle_dict                | 18.4 us                                                     | 12.2 us: 1.51x faster                                                       |
| float                      | 56.8 ms                                                     | 37.9 ms: 1.50x faster                                                       |
| deepcopy_reduce            | 2.09 us                                                     | 1.49 us: 1.41x faster                                                       |
| logging_silent             | 60.5 ns                                                     | 43.1 ns: 1.40x faster                                                       |
| hexiom                     | 4.10 ms                                                     | 2.94 ms: 1.40x faster                                                       |
| spectral_norm              | 66.9 ms                                                     | 48.1 ms: 1.39x faster                                                       |
| deltablue                  | 2.16 ms                                                     | 1.55 ms: 1.39x faster                                                       |
| chaos                      | 43.3 ms                                                     | 31.4 ms: 1.38x faster                                                       |
| nbody                      | 71.9 ms                                                     | 52.2 ms: 1.38x faster                                                       |
| pprint_safe_repr           | 513 ms                                                      | 383 ms: 1.34x faster                                                        |
| raytrace                   | 192 ms                                                      | 144 ms: 1.33x faster                                                        |
| pprint_pformat             | 1.05 sec                                                    | 786 ms: 1.33x faster                                                        |
| richards                   | 28.4 ms                                                     | 21.4 ms: 1.33x faster                                                       |
| nqueens                    | 62.8 ms                                                     | 47.5 ms: 1.32x faster                                                       |
| pickle_list                | 2.83 us                                                     | 2.16 us: 1.31x faster                                                       |
| tomli_loads                | 1.37 sec                                                    | 1.06 sec: 1.30x faster                                                      |
| richards_super             | 32.1 ms                                                     | 24.8 ms: 1.29x faster                                                       |
| coroutines                 | 14.3 ms                                                     | 11.1 ms: 1.29x faster                                                       |
| unpickle_pure_python       | 133 us                                                      | 104 us: 1.28x faster                                                        |
| scimark_lu                 | 58.9 ms                                                     | 46.0 ms: 1.28x faster                                                       |
| regex_compile              | 87.5 ms                                                     | 68.6 ms: 1.28x faster                                                       |
| pyflate                    | 295 ms                                                      | 232 ms: 1.27x faster                                                        |
| unpack_sequence            | 37.5 ns                                                     | 29.6 ns: 1.27x faster                                                       |
| scimark_fft                | 184 ms                                                      | 146 ms: 1.26x faster                                                        |
| fannkuch                   | 247 ms                                                      | 197 ms: 1.25x faster                                                        |
| crypto_pyaes               | 48.5 ms                                                     | 39.1 ms: 1.24x faster                                                       |
| async_generators           | 239 ms                                                      | 195 ms: 1.23x faster                                                        |
| unpickle_list              | 2.75 us                                                     | 2.30 us: 1.20x faster                                                       |
| pickle                     | 7.43 us                                                     | 6.22 us: 1.20x faster                                                       |
| mako                       | 7.09 ms                                                     | 5.93 ms: 1.19x faster                                                       |
| sympy_sum                  | 91.5 ms                                                     | 78.2 ms: 1.17x faster                                                       |
| sqlite_synth               | 1.76 us                                                     | 1.51 us: 1.17x faster                                                       |
| sympy_str                  | 175 ms                                                      | 150 ms: 1.17x faster                                                        |
| pickle_pure_python         | 195 us                                                      | 169 us: 1.16x faster                                                        |
| xml_etree_generate         | 55.8 ms                                                     | 48.3 ms: 1.16x faster                                                       |
| sympy_integrate            | 13.0 ms                                                     | 11.2 ms: 1.15x faster                                                       |
| django_template            | 22.9 ms                                                     | 20.0 ms: 1.15x faster                                                       |
| dulwich_log                | 44.3 ms                                                     | 38.9 ms: 1.14x faster                                                       |
| asyncio_tcp                | 487 ms                                                      | 429 ms: 1.14x faster                                                        |
| xml_etree_process          | 37.7 ms                                                     | 33.5 ms: 1.13x faster                                                       |
| logging_simple             | 6.28 us                                                     | 5.60 us: 1.12x faster                                                       |
| logging_format             | 6.72 us                                                     | 6.00 us: 1.12x faster                                                       |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.30 ms: 1.11x faster                                                       |
| meteor_contest             | 74.6 ms                                                     | 67.2 ms: 1.11x faster                                                       |
| sympy_expand               | 284 ms                                                      | 256 ms: 1.11x faster                                                        |
| pycparser                  | 699 ms                                                      | 649 ms: 1.08x faster                                                        |
| 2to3                       | 218 ms                                                      | 205 ms: 1.06x faster                                                        |
| unpickle                   | 8.18 us                                                     | 7.73 us: 1.06x faster                                                       |
| typing_runtime_protocols   | 95.1 us                                                     | 90.7 us: 1.05x faster                                                       |
| docutils                   | 1.66 sec                                                    | 1.59 sec: 1.05x faster                                                      |
| json                       | 3.05 ms                                                     | 2.92 ms: 1.04x faster                                                       |
| pidigits                   | 152 ms                                                      | 146 ms: 1.04x faster                                                        |
| regex_v8                   | 14.2 ms                                                     | 13.8 ms: 1.03x faster                                                       |
| xml_etree_iterparse        | 65.2 ms                                                     | 63.2 ms: 1.03x faster                                                       |
| telco                      | 4.13 ms                                                     | 4.08 ms: 1.01x faster                                                       |
| regex_dna                  | 126 ms                                                      | 127 ms: 1.01x slower                                                        |
| coverage                   | 40.8 ms                                                     | 41.1 ms: 1.01x slower                                                       |
| xml_etree_parse            | 93.0 ms                                                     | 93.8 ms: 1.01x slower                                                       |
| json_dumps                 | 5.70 ms                                                     | 5.79 ms: 1.02x slower                                                       |
| json_loads                 | 13.9 us                                                     | 14.4 us: 1.04x slower                                                       |
| regex_effbot               | 1.62 ms                                                     | 1.76 ms: 1.09x slower                                                       |
| python_startup_no_site     | 16.2 ms                                                     | 20.2 ms: 1.24x slower                                                       |
| bench_mp_pool              | 69.2 ms                                                     | 90.3 ms: 1.31x slower                                                       |
| python_startup             | 19.5 ms                                                     | 27.0 ms: 1.38x slower                                                       |
| create_gc_cycles           | 752 us                                                      | 1.38 ms: 1.83x slower                                                       |
| gc_traversal               | 1.52 ms                                                     | 2.87 ms: 1.89x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.25x faster                                                                |

Benchmark hidden because not significant (1): bench_thread_pool
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20250503-3.14.0a7+-7363e8d-CLANG/bm-20250503-pythonperf1-amd64-python-7363e8d24d14abf65163-3.14.0a7+-7363e8d.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.255x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.23x
- 95% likely to have a speedup of 1.22x
- 99% likely to have a speedup of 1.17x

# Memory
- memory change: unknown
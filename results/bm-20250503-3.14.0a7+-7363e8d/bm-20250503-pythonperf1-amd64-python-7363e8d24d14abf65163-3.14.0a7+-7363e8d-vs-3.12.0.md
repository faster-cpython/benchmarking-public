# Results vs. 3.12.0

- fork: python
- ref: 7363e8d24d14abf65163
- machine: windows-amd64
- commit hash: 7363e8d
- commit date: 2025-05-03
- overall geometric mean: 1.084x faster
- HPT reliability: 99.99%
- HPT 99th percentile: 1.02x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250503-pythonperf1-amd64-python-7363e8d24d14abf65163-3.14.0a7+-7363e8d |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 223 ms: 1.02x slower                                                        |
| Geometric mean | (ref)                                                       | 1.01x slower                                                                |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250503-pythonperf1-amd64-python-7363e8d24d14abf65163-3.14.0a7+-7363e8d |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 400 ms: 1.93x faster                                                        |
| async_tree_io              | 731 ms                                                      | 413 ms: 1.77x faster                                                        |
| async_tree_memoization_tg  | 367 ms                                                      | 211 ms: 1.74x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 172 ms: 1.65x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 207 ms: 1.64x faster                                                        |
| async_tree_none            | 291 ms                                                      | 182 ms: 1.60x faster                                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 344 ms: 1.46x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 337 ms: 1.45x faster                                                        |
| Geometric mean             | (ref)                                                       | 1.65x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250503-pythonperf1-amd64-python-7363e8d24d14abf65163-3.14.0a7+-7363e8d |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 43.9 ms: 1.29x faster                                                       |
| nbody          | 71.9 ms                                                     | 63.2 ms: 1.14x faster                                                       |
| pidigits       | 152 ms                                                      | 149 ms: 1.02x faster                                                        |
| Geometric mean | (ref)                                                       | 1.15x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250503-pythonperf1-amd64-python-7363e8d24d14abf65163-3.14.0a7+-7363e8d |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 87.5 ms                                                     | 81.4 ms: 1.08x faster                                                       |
| regex_dna      | 126 ms                                                      | 120 ms: 1.06x faster                                                        |
| regex_effbot   | 1.62 ms                                                     | 1.57 ms: 1.03x faster                                                       |
| regex_v8       | 14.2 ms                                                     | 15.1 ms: 1.06x slower                                                       |
| Geometric mean | (ref)                                                       | 1.03x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250503-pythonperf1-amd64-python-7363e8d24d14abf65163-3.14.0a7+-7363e8d |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_parse      | 93.0 ms                                                     | 90.7 ms: 1.03x faster                                                       |
| xml_etree_iterparse  | 65.2 ms                                                     | 64.2 ms: 1.02x faster                                                       |
| unpickle_pure_python | 133 us                                                      | 134 us: 1.01x slower                                                        |
| xml_etree_generate   | 55.8 ms                                                     | 56.3 ms: 1.01x slower                                                       |
| tomli_loads          | 1.37 sec                                                    | 1.39 sec: 1.01x slower                                                      |
| unpickle             | 8.18 us                                                     | 8.55 us: 1.04x slower                                                       |
| json_loads           | 13.9 us                                                     | 14.6 us: 1.05x slower                                                       |
| unpickle_list        | 2.75 us                                                     | 2.90 us: 1.06x slower                                                       |
| xml_etree_process    | 37.7 ms                                                     | 40.0 ms: 1.06x slower                                                       |
| pickle               | 7.43 us                                                     | 8.01 us: 1.08x slower                                                       |
| pickle_pure_python   | 195 us                                                      | 213 us: 1.09x slower                                                        |
| pickle_dict          | 18.4 us                                                     | 21.3 us: 1.16x slower                                                       |
| json_dumps           | 5.70 ms                                                     | 6.80 ms: 1.19x slower                                                       |
| pickle_list          | 2.83 us                                                     | 3.57 us: 1.26x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.07x slower                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250503-pythonperf1-amd64-python-7363e8d24d14abf65163-3.14.0a7+-7363e8d |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 19.7 ms: 1.21x slower                                                       |
| python_startup         | 19.5 ms                                                     | 26.4 ms: 1.36x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.28x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250503-pythonperf1-amd64-python-7363e8d24d14abf65163-3.14.0a7+-7363e8d |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 6.70 ms: 1.06x faster                                                       |
| django_template | 22.9 ms                                                     | 24.3 ms: 1.06x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.00x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250503-pythonperf1-amd64-python-7363e8d24d14abf65163-3.14.0a7+-7363e8d |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pathlib                    | 80.5 ms                                                     | 32.4 ms: 2.48x faster                                                       |
| async_tree_io_tg           | 771 ms                                                      | 400 ms: 1.93x faster                                                        |
| async_tree_io              | 731 ms                                                      | 413 ms: 1.77x faster                                                        |
| async_tree_memoization_tg  | 367 ms                                                      | 211 ms: 1.74x faster                                                        |
| mdp                        | 1.37 sec                                                    | 791 ms: 1.73x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 172 ms: 1.65x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 207 ms: 1.64x faster                                                        |
| async_tree_none            | 291 ms                                                      | 182 ms: 1.60x faster                                                        |
| asyncio_tcp_ssl            | 2.10 sec                                                    | 1.34 sec: 1.57x faster                                                      |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 344 ms: 1.46x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 337 ms: 1.45x faster                                                        |
| deepcopy                   | 238 us                                                      | 177 us: 1.35x faster                                                        |
| float                      | 56.8 ms                                                     | 43.9 ms: 1.29x faster                                                       |
| deepcopy_memo              | 23.7 us                                                     | 18.5 us: 1.28x faster                                                       |
| comprehensions             | 14.1 us                                                     | 11.4 us: 1.24x faster                                                       |
| spectral_norm              | 66.9 ms                                                     | 56.3 ms: 1.19x faster                                                       |
| go                         | 91.6 ms                                                     | 77.9 ms: 1.18x faster                                                       |
| generators                 | 22.5 ms                                                     | 19.5 ms: 1.16x faster                                                       |
| asyncio_tcp                | 487 ms                                                      | 423 ms: 1.15x faster                                                        |
| nbody                      | 71.9 ms                                                     | 63.2 ms: 1.14x faster                                                       |
| chaos                      | 43.3 ms                                                     | 38.4 ms: 1.13x faster                                                       |
| deepcopy_reduce            | 2.09 us                                                     | 1.86 us: 1.13x faster                                                       |
| unpack_sequence            | 37.5 ns                                                     | 33.3 ns: 1.13x faster                                                       |
| sqlite_synth               | 1.76 us                                                     | 1.58 us: 1.12x faster                                                       |
| scimark_monte_carlo        | 43.7 ms                                                     | 40.4 ms: 1.08x faster                                                       |
| logging_silent             | 60.5 ns                                                     | 56.2 ns: 1.08x faster                                                       |
| regex_compile              | 87.5 ms                                                     | 81.4 ms: 1.08x faster                                                       |
| raytrace                   | 192 ms                                                      | 182 ms: 1.06x faster                                                        |
| regex_dna                  | 126 ms                                                      | 120 ms: 1.06x faster                                                        |
| mako                       | 7.09 ms                                                     | 6.70 ms: 1.06x faster                                                       |
| pyflate                    | 295 ms                                                      | 280 ms: 1.05x faster                                                        |
| scimark_sor                | 78.8 ms                                                     | 75.1 ms: 1.05x faster                                                       |
| dulwich_log                | 44.3 ms                                                     | 42.3 ms: 1.05x faster                                                       |
| pprint_pformat             | 1.05 sec                                                    | 1.00 sec: 1.04x faster                                                      |
| scimark_lu                 | 58.9 ms                                                     | 56.5 ms: 1.04x faster                                                       |
| sympy_sum                  | 91.5 ms                                                     | 88.1 ms: 1.04x faster                                                       |
| coroutines                 | 14.3 ms                                                     | 13.7 ms: 1.04x faster                                                       |
| async_generators           | 239 ms                                                      | 231 ms: 1.04x faster                                                        |
| pprint_safe_repr           | 513 ms                                                      | 496 ms: 1.04x faster                                                        |
| regex_effbot               | 1.62 ms                                                     | 1.57 ms: 1.03x faster                                                       |
| sympy_integrate            | 13.0 ms                                                     | 12.6 ms: 1.03x faster                                                       |
| richards_super             | 32.1 ms                                                     | 31.1 ms: 1.03x faster                                                       |
| nqueens                    | 62.8 ms                                                     | 60.9 ms: 1.03x faster                                                       |
| xml_etree_parse            | 93.0 ms                                                     | 90.7 ms: 1.03x faster                                                       |
| pidigits                   | 152 ms                                                      | 149 ms: 1.02x faster                                                        |
| richards                   | 28.4 ms                                                     | 27.8 ms: 1.02x faster                                                       |
| sympy_str                  | 175 ms                                                      | 172 ms: 1.02x faster                                                        |
| hexiom                     | 4.10 ms                                                     | 4.03 ms: 1.02x faster                                                       |
| scimark_fft                | 184 ms                                                      | 181 ms: 1.02x faster                                                        |
| xml_etree_iterparse        | 65.2 ms                                                     | 64.2 ms: 1.02x faster                                                       |
| crypto_pyaes               | 48.5 ms                                                     | 47.8 ms: 1.02x faster                                                       |
| unpickle_pure_python       | 133 us                                                      | 134 us: 1.01x slower                                                        |
| xml_etree_generate         | 55.8 ms                                                     | 56.3 ms: 1.01x slower                                                       |
| json                       | 3.05 ms                                                     | 3.08 ms: 1.01x slower                                                       |
| tomli_loads                | 1.37 sec                                                    | 1.39 sec: 1.01x slower                                                      |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.61 ms: 1.02x slower                                                       |
| pycparser                  | 699 ms                                                      | 712 ms: 1.02x slower                                                        |
| logging_simple             | 6.28 us                                                     | 6.40 us: 1.02x slower                                                       |
| 2to3                       | 218 ms                                                      | 223 ms: 1.02x slower                                                        |
| logging_format             | 6.72 us                                                     | 6.87 us: 1.02x slower                                                       |
| fannkuch                   | 247 ms                                                      | 254 ms: 1.03x slower                                                        |
| bench_thread_pool          | 857 us                                                      | 889 us: 1.04x slower                                                        |
| unpickle                   | 8.18 us                                                     | 8.55 us: 1.04x slower                                                       |
| sympy_expand               | 284 ms                                                      | 297 ms: 1.05x slower                                                        |
| json_loads                 | 13.9 us                                                     | 14.6 us: 1.05x slower                                                       |
| unpickle_list              | 2.75 us                                                     | 2.90 us: 1.06x slower                                                       |
| django_template            | 22.9 ms                                                     | 24.3 ms: 1.06x slower                                                       |
| xml_etree_process          | 37.7 ms                                                     | 40.0 ms: 1.06x slower                                                       |
| regex_v8                   | 14.2 ms                                                     | 15.1 ms: 1.06x slower                                                       |
| pickle                     | 7.43 us                                                     | 8.01 us: 1.08x slower                                                       |
| pickle_pure_python         | 195 us                                                      | 213 us: 1.09x slower                                                        |
| telco                      | 4.13 ms                                                     | 4.64 ms: 1.12x slower                                                       |
| typing_runtime_protocols   | 95.1 us                                                     | 109 us: 1.14x slower                                                        |
| pickle_dict                | 18.4 us                                                     | 21.3 us: 1.16x slower                                                       |
| json_dumps                 | 5.70 ms                                                     | 6.80 ms: 1.19x slower                                                       |
| python_startup_no_site     | 16.2 ms                                                     | 19.7 ms: 1.21x slower                                                       |
| coverage                   | 40.8 ms                                                     | 51.6 ms: 1.26x slower                                                       |
| pickle_list                | 2.83 us                                                     | 3.57 us: 1.26x slower                                                       |
| bench_mp_pool              | 69.2 ms                                                     | 90.1 ms: 1.30x slower                                                       |
| python_startup             | 19.5 ms                                                     | 26.4 ms: 1.36x slower                                                       |
| gc_traversal               | 1.52 ms                                                     | 2.09 ms: 1.37x slower                                                       |
| create_gc_cycles           | 752 us                                                      | 1.27 ms: 1.69x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.07x faster                                                                |

Benchmark hidden because not significant (3): meteor_contest, deltablue, docutils
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20250503-3.14.0a7+-7363e8d/bm-20250503-pythonperf1-amd64-python-7363e8d24d14abf65163-3.14.0a7+-7363e8d.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.084x faster

# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: unknown
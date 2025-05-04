# Results vs. 3.12.0

- fork: python
- ref: 7363e8d24d14abf65163
- machine: windows-amd64
- commit hash: 7363e8d
- commit date: 2025-05-03
- overall geometric mean: 1.010x faster
- HPT reliability: 96.00%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250503-pythonperf1-amd64-python-7363e8d24d14abf65163-3.14.0a7+-7363e8d |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 227 ms: 1.04x slower                                                        |
| docutils       | 1.66 sec                                                    | 2.98 sec: 1.79x slower                                                      |
| Geometric mean | (ref)                                                       | 1.37x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250503-pythonperf1-amd64-python-7363e8d24d14abf65163-3.14.0a7+-7363e8d |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 330 ms: 2.34x faster                                                        |
| async_tree_io              | 731 ms                                                      | 354 ms: 2.07x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 147 ms: 1.94x faster                                                        |
| async_tree_memoization_tg  | 367 ms                                                      | 190 ms: 1.93x faster                                                        |
| async_tree_none            | 291 ms                                                      | 169 ms: 1.72x faster                                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 310 ms: 1.62x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 209 ms: 1.62x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 332 ms: 1.47x faster                                                        |
| Geometric mean             | (ref)                                                       | 1.82x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250503-pythonperf1-amd64-python-7363e8d24d14abf65163-3.14.0a7+-7363e8d |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 45.3 ms: 1.25x faster                                                       |
| pidigits       | 152 ms                                                      | 139 ms: 1.09x faster                                                        |
| nbody          | 71.9 ms                                                     | 78.9 ms: 1.10x slower                                                       |
| Geometric mean | (ref)                                                       | 1.08x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250503-pythonperf1-amd64-python-7363e8d24d14abf65163-3.14.0a7+-7363e8d |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_dna      | 126 ms                                                      | 113 ms: 1.11x faster                                                        |
| regex_v8       | 14.2 ms                                                     | 13.1 ms: 1.08x faster                                                       |
| regex_effbot   | 1.62 ms                                                     | 1.57 ms: 1.03x faster                                                       |
| regex_compile  | 87.5 ms                                                     | 90.8 ms: 1.04x slower                                                       |
| Geometric mean | (ref)                                                       | 1.05x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250503-pythonperf1-amd64-python-7363e8d24d14abf65163-3.14.0a7+-7363e8d |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_iterparse  | 65.2 ms                                                     | 58.4 ms: 1.12x faster                                                       |
| xml_etree_parse      | 93.0 ms                                                     | 90.6 ms: 1.03x faster                                                       |
| xml_etree_generate   | 55.8 ms                                                     | 60.7 ms: 1.09x slower                                                       |
| unpickle_pure_python | 133 us                                                      | 148 us: 1.11x slower                                                        |
| pickle_dict          | 18.4 us                                                     | 20.9 us: 1.13x slower                                                       |
| pickle               | 7.43 us                                                     | 8.47 us: 1.14x slower                                                       |
| pickle_pure_python   | 195 us                                                      | 223 us: 1.14x slower                                                        |
| xml_etree_process    | 37.7 ms                                                     | 43.3 ms: 1.15x slower                                                       |
| pickle_list          | 2.83 us                                                     | 3.39 us: 1.20x slower                                                       |
| unpickle             | 8.18 us                                                     | 9.83 us: 1.20x slower                                                       |
| json_loads           | 13.9 us                                                     | 17.0 us: 1.22x slower                                                       |
| unpickle_list        | 2.75 us                                                     | 3.38 us: 1.23x slower                                                       |
| json_dumps           | 5.70 ms                                                     | 7.22 ms: 1.27x slower                                                       |
| tomli_loads          | 1.37 sec                                                    | 2.59 sec: 1.89x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.17x slower                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250503-pythonperf1-amd64-python-7363e8d24d14abf65163-3.14.0a7+-7363e8d |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 19.5 ms: 1.20x slower                                                       |
| python_startup         | 19.5 ms                                                     | 25.8 ms: 1.33x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.26x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250503-pythonperf1-amd64-python-7363e8d24d14abf65163-3.14.0a7+-7363e8d |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| django_template | 22.9 ms                                                     | 26.2 ms: 1.14x slower                                                       |
| mako            | 7.09 ms                                                     | 9.76 ms: 1.38x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.25x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250503-pythonperf1-amd64-python-7363e8d24d14abf65163-3.14.0a7+-7363e8d |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pathlib                    | 80.5 ms                                                     | 32.2 ms: 2.50x faster                                                       |
| async_tree_io_tg           | 771 ms                                                      | 330 ms: 2.34x faster                                                        |
| async_tree_io              | 731 ms                                                      | 354 ms: 2.07x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 147 ms: 1.94x faster                                                        |
| async_tree_memoization_tg  | 367 ms                                                      | 190 ms: 1.93x faster                                                        |
| async_tree_none            | 291 ms                                                      | 169 ms: 1.72x faster                                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 310 ms: 1.62x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 209 ms: 1.62x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 332 ms: 1.47x faster                                                        |
| gc_traversal               | 1.52 ms                                                     | 1.14 ms: 1.33x faster                                                       |
| sqlite_synth               | 1.76 us                                                     | 1.37 us: 1.29x faster                                                       |
| mdp                        | 1.37 sec                                                    | 1.08 sec: 1.27x faster                                                      |
| float                      | 56.8 ms                                                     | 45.3 ms: 1.25x faster                                                       |
| deepcopy                   | 238 us                                                      | 192 us: 1.24x faster                                                        |
| deepcopy_memo              | 23.7 us                                                     | 20.7 us: 1.14x faster                                                       |
| xml_etree_iterparse        | 65.2 ms                                                     | 58.4 ms: 1.12x faster                                                       |
| regex_dna                  | 126 ms                                                      | 113 ms: 1.11x faster                                                        |
| comprehensions             | 14.1 us                                                     | 12.8 us: 1.10x faster                                                       |
| pidigits                   | 152 ms                                                      | 139 ms: 1.09x faster                                                        |
| regex_v8                   | 14.2 ms                                                     | 13.1 ms: 1.08x faster                                                       |
| coroutines                 | 14.3 ms                                                     | 13.2 ms: 1.08x faster                                                       |
| dulwich_log                | 44.3 ms                                                     | 42.4 ms: 1.04x faster                                                       |
| regex_effbot               | 1.62 ms                                                     | 1.57 ms: 1.03x faster                                                       |
| deepcopy_reduce            | 2.09 us                                                     | 2.04 us: 1.03x faster                                                       |
| xml_etree_parse            | 93.0 ms                                                     | 90.6 ms: 1.03x faster                                                       |
| generators                 | 22.5 ms                                                     | 22.1 ms: 1.02x faster                                                       |
| logging_silent             | 60.5 ns                                                     | 59.5 ns: 1.02x faster                                                       |
| go                         | 91.6 ms                                                     | 92.6 ms: 1.01x slower                                                       |
| logging_simple             | 6.28 us                                                     | 6.41 us: 1.02x slower                                                       |
| spectral_norm              | 66.9 ms                                                     | 68.5 ms: 1.02x slower                                                       |
| logging_format             | 6.72 us                                                     | 6.89 us: 1.03x slower                                                       |
| pycparser                  | 699 ms                                                      | 719 ms: 1.03x slower                                                        |
| sympy_sum                  | 91.5 ms                                                     | 94.8 ms: 1.04x slower                                                       |
| regex_compile              | 87.5 ms                                                     | 90.8 ms: 1.04x slower                                                       |
| 2to3                       | 218 ms                                                      | 227 ms: 1.04x slower                                                        |
| json                       | 3.05 ms                                                     | 3.21 ms: 1.05x slower                                                       |
| raytrace                   | 192 ms                                                      | 203 ms: 1.06x slower                                                        |
| scimark_lu                 | 58.9 ms                                                     | 62.2 ms: 1.06x slower                                                       |
| sympy_str                  | 175 ms                                                      | 186 ms: 1.06x slower                                                        |
| scimark_fft                | 184 ms                                                      | 196 ms: 1.06x slower                                                        |
| sympy_integrate            | 13.0 ms                                                     | 13.9 ms: 1.07x slower                                                       |
| pyflate                    | 295 ms                                                      | 318 ms: 1.08x slower                                                        |
| xml_etree_generate         | 55.8 ms                                                     | 60.7 ms: 1.09x slower                                                       |
| scimark_sor                | 78.8 ms                                                     | 85.8 ms: 1.09x slower                                                       |
| deltablue                  | 2.16 ms                                                     | 2.36 ms: 1.09x slower                                                       |
| nbody                      | 71.9 ms                                                     | 78.9 ms: 1.10x slower                                                       |
| nqueens                    | 62.8 ms                                                     | 69.2 ms: 1.10x slower                                                       |
| hexiom                     | 4.10 ms                                                     | 4.52 ms: 1.10x slower                                                       |
| scimark_monte_carlo        | 43.7 ms                                                     | 48.3 ms: 1.10x slower                                                       |
| async_generators           | 239 ms                                                      | 264 ms: 1.10x slower                                                        |
| pprint_safe_repr           | 513 ms                                                      | 569 ms: 1.11x slower                                                        |
| bench_mp_pool              | 69.2 ms                                                     | 76.7 ms: 1.11x slower                                                       |
| sympy_expand               | 284 ms                                                      | 315 ms: 1.11x slower                                                        |
| unpickle_pure_python       | 133 us                                                      | 148 us: 1.11x slower                                                        |
| asyncio_tcp_ssl            | 2.10 sec                                                    | 2.33 sec: 1.11x slower                                                      |
| richards                   | 28.4 ms                                                     | 32.2 ms: 1.13x slower                                                       |
| pickle_dict                | 18.4 us                                                     | 20.9 us: 1.13x slower                                                       |
| unpack_sequence            | 37.5 ns                                                     | 42.6 ns: 1.14x slower                                                       |
| pickle                     | 7.43 us                                                     | 8.47 us: 1.14x slower                                                       |
| pickle_pure_python         | 195 us                                                      | 223 us: 1.14x slower                                                        |
| django_template            | 22.9 ms                                                     | 26.2 ms: 1.14x slower                                                       |
| xml_etree_process          | 37.7 ms                                                     | 43.3 ms: 1.15x slower                                                       |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.98 ms: 1.16x slower                                                       |
| richards_super             | 32.1 ms                                                     | 37.5 ms: 1.17x slower                                                       |
| crypto_pyaes               | 48.5 ms                                                     | 57.1 ms: 1.18x slower                                                       |
| meteor_contest             | 74.6 ms                                                     | 88.8 ms: 1.19x slower                                                       |
| fannkuch                   | 247 ms                                                      | 295 ms: 1.20x slower                                                        |
| python_startup_no_site     | 16.2 ms                                                     | 19.5 ms: 1.20x slower                                                       |
| pickle_list                | 2.83 us                                                     | 3.39 us: 1.20x slower                                                       |
| unpickle                   | 8.18 us                                                     | 9.83 us: 1.20x slower                                                       |
| json_loads                 | 13.9 us                                                     | 17.0 us: 1.22x slower                                                       |
| unpickle_list              | 2.75 us                                                     | 3.38 us: 1.23x slower                                                       |
| telco                      | 4.13 ms                                                     | 5.17 ms: 1.25x slower                                                       |
| json_dumps                 | 5.70 ms                                                     | 7.22 ms: 1.27x slower                                                       |
| bench_thread_pool          | 857 us                                                      | 1.10 ms: 1.29x slower                                                       |
| create_gc_cycles           | 752 us                                                      | 982 us: 1.31x slower                                                        |
| python_startup             | 19.5 ms                                                     | 25.8 ms: 1.33x slower                                                       |
| typing_runtime_protocols   | 95.1 us                                                     | 130 us: 1.37x slower                                                        |
| mako                       | 7.09 ms                                                     | 9.76 ms: 1.38x slower                                                       |
| coverage                   | 40.8 ms                                                     | 67.2 ms: 1.65x slower                                                       |
| pprint_pformat             | 1.05 sec                                                    | 1.85 sec: 1.77x slower                                                      |
| docutils                   | 1.66 sec                                                    | 2.98 sec: 1.79x slower                                                      |
| tomli_loads                | 1.37 sec                                                    | 2.59 sec: 1.89x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.01x slower                                                                |

Benchmark hidden because not significant (2): asyncio_tcp, chaos
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (17) of results/bm-20250503-3.14.0a7+-7363e8d-NOGIL/bm-20250503-pythonperf1-amd64-python-7363e8d24d14abf65163-3.14.0a7+-7363e8d.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.010x faster

# HPT report

- Reliability score: 96.00% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown
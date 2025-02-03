# Results vs. 3.12.0

- fork: python
- ref: cf4c4ecc26c7e3b89f2e
- machine: windows-amd64
- commit hash: cf4c4ec
- commit date: 2025-02-01
- overall geometric mean: 1.089x faster
- HPT reliability: 99.79%
- HPT 99th percentile: 1.01x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250201-pythonperf1-amd64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 221 ms: 1.01x slower                                                        |
| docutils       | 1.66 sec                                                    | 1.73 sec: 1.04x slower                                                      |
| Geometric mean | (ref)                                                       | 1.03x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250201-pythonperf1-amd64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 394 ms: 1.96x faster                                                        |
| async_tree_io              | 731 ms                                                      | 404 ms: 1.81x faster                                                        |
| async_tree_memoization_tg  | 367 ms                                                      | 214 ms: 1.72x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 167 ms: 1.71x faster                                                        |
| async_tree_none            | 291 ms                                                      | 178 ms: 1.64x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 213 ms: 1.59x faster                                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 336 ms: 1.50x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 339 ms: 1.44x faster                                                        |
| Geometric mean             | (ref)                                                       | 1.66x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250201-pythonperf1-amd64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 37.0 ms: 1.53x faster                                                       |
| nbody          | 71.9 ms                                                     | 50.4 ms: 1.43x faster                                                       |
| pidigits       | 152 ms                                                      | 150 ms: 1.01x faster                                                        |
| Geometric mean | (ref)                                                       | 1.30x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250201-pythonperf1-amd64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_effbot   | 1.62 ms                                                     | 1.42 ms: 1.14x faster                                                       |
| regex_dna      | 126 ms                                                      | 115 ms: 1.10x faster                                                        |
| regex_compile  | 87.5 ms                                                     | 81.1 ms: 1.08x faster                                                       |
| regex_v8       | 14.2 ms                                                     | 14.8 ms: 1.04x slower                                                       |
| Geometric mean | (ref)                                                       | 1.07x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250201-pythonperf1-amd64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpickle_pure_python | 133 us                                                      | 110 us: 1.21x faster                                                        |
| tomli_loads          | 1.37 sec                                                    | 1.13 sec: 1.21x faster                                                      |
| xml_etree_generate   | 55.8 ms                                                     | 50.3 ms: 1.11x faster                                                       |
| xml_etree_iterparse  | 65.2 ms                                                     | 59.6 ms: 1.09x faster                                                       |
| xml_etree_parse      | 93.0 ms                                                     | 88.1 ms: 1.06x faster                                                       |
| xml_etree_process    | 37.7 ms                                                     | 35.8 ms: 1.05x faster                                                       |
| unpickle_list        | 2.75 us                                                     | 2.67 us: 1.03x faster                                                       |
| pickle_pure_python   | 195 us                                                      | 198 us: 1.01x slower                                                        |
| unpickle             | 8.18 us                                                     | 8.77 us: 1.07x slower                                                       |
| pickle               | 7.43 us                                                     | 8.11 us: 1.09x slower                                                       |
| pickle_list          | 2.83 us                                                     | 3.08 us: 1.09x slower                                                       |
| json_dumps           | 5.70 ms                                                     | 6.24 ms: 1.10x slower                                                       |
| json_loads           | 13.9 us                                                     | 15.5 us: 1.12x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.02x faster                                                                |

Benchmark hidden because not significant (1): pickle_dict

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250201-pythonperf1-amd64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 19.7 ms: 1.21x slower                                                       |
| python_startup         | 19.5 ms                                                     | 26.1 ms: 1.34x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.27x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250201-pythonperf1-amd64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 5.26 ms: 1.35x faster                                                       |
| django_template | 22.9 ms                                                     | 26.1 ms: 1.14x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.09x faster                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250201-pythonperf1-amd64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 394 ms: 1.96x faster                                                        |
| async_tree_io              | 731 ms                                                      | 404 ms: 1.81x faster                                                        |
| async_tree_memoization_tg  | 367 ms                                                      | 214 ms: 1.72x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 167 ms: 1.71x faster                                                        |
| async_tree_none            | 291 ms                                                      | 178 ms: 1.64x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 213 ms: 1.59x faster                                                        |
| float                      | 56.8 ms                                                     | 37.0 ms: 1.53x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 336 ms: 1.50x faster                                                        |
| spectral_norm              | 66.9 ms                                                     | 46.3 ms: 1.45x faster                                                       |
| asyncio_tcp_ssl            | 2.10 sec                                                    | 1.45 sec: 1.44x faster                                                      |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 339 ms: 1.44x faster                                                        |
| deepcopy_memo              | 23.7 us                                                     | 16.5 us: 1.43x faster                                                       |
| nbody                      | 71.9 ms                                                     | 50.4 ms: 1.43x faster                                                       |
| scimark_sor                | 78.8 ms                                                     | 57.5 ms: 1.37x faster                                                       |
| mako                       | 7.09 ms                                                     | 5.26 ms: 1.35x faster                                                       |
| pathlib                    | 80.5 ms                                                     | 60.7 ms: 1.33x faster                                                       |
| deepcopy                   | 238 us                                                      | 185 us: 1.29x faster                                                        |
| scimark_fft                | 184 ms                                                      | 146 ms: 1.26x faster                                                        |
| comprehensions             | 14.1 us                                                     | 11.3 us: 1.25x faster                                                       |
| scimark_monte_carlo        | 43.7 ms                                                     | 35.9 ms: 1.22x faster                                                       |
| unpickle_pure_python       | 133 us                                                      | 110 us: 1.21x faster                                                        |
| tomli_loads                | 1.37 sec                                                    | 1.13 sec: 1.21x faster                                                      |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.15 ms: 1.19x faster                                                       |
| regex_effbot               | 1.62 ms                                                     | 1.42 ms: 1.14x faster                                                       |
| sqlite_synth               | 1.76 us                                                     | 1.56 us: 1.13x faster                                                       |
| deepcopy_reduce            | 2.09 us                                                     | 1.87 us: 1.12x faster                                                       |
| logging_silent             | 60.5 ns                                                     | 54.0 ns: 1.12x faster                                                       |
| coroutines                 | 14.3 ms                                                     | 12.8 ms: 1.11x faster                                                       |
| xml_etree_generate         | 55.8 ms                                                     | 50.3 ms: 1.11x faster                                                       |
| pyflate                    | 295 ms                                                      | 267 ms: 1.10x faster                                                        |
| regex_dna                  | 126 ms                                                      | 115 ms: 1.10x faster                                                        |
| xml_etree_iterparse        | 65.2 ms                                                     | 59.6 ms: 1.09x faster                                                       |
| regex_compile              | 87.5 ms                                                     | 81.1 ms: 1.08x faster                                                       |
| crypto_pyaes               | 48.5 ms                                                     | 45.4 ms: 1.07x faster                                                       |
| chaos                      | 43.3 ms                                                     | 40.7 ms: 1.07x faster                                                       |
| xml_etree_parse            | 93.0 ms                                                     | 88.1 ms: 1.06x faster                                                       |
| xml_etree_process          | 37.7 ms                                                     | 35.8 ms: 1.05x faster                                                       |
| go                         | 91.6 ms                                                     | 87.0 ms: 1.05x faster                                                       |
| dulwich_log                | 44.3 ms                                                     | 42.6 ms: 1.04x faster                                                       |
| fannkuch                   | 247 ms                                                      | 237 ms: 1.04x faster                                                        |
| pprint_pformat             | 1.05 sec                                                    | 1.01 sec: 1.03x faster                                                      |
| unpickle_list              | 2.75 us                                                     | 2.67 us: 1.03x faster                                                       |
| async_generators           | 239 ms                                                      | 233 ms: 1.03x faster                                                        |
| scimark_lu                 | 58.9 ms                                                     | 57.3 ms: 1.03x faster                                                       |
| logging_simple             | 6.28 us                                                     | 6.15 us: 1.02x faster                                                       |
| logging_format             | 6.72 us                                                     | 6.59 us: 1.02x faster                                                       |
| nqueens                    | 62.8 ms                                                     | 61.7 ms: 1.02x faster                                                       |
| sympy_sum                  | 91.5 ms                                                     | 90.3 ms: 1.01x faster                                                       |
| pidigits                   | 152 ms                                                      | 150 ms: 1.01x faster                                                        |
| sqlglot_transpile          | 1.02 ms                                                     | 1.03 ms: 1.01x slower                                                       |
| json                       | 3.05 ms                                                     | 3.08 ms: 1.01x slower                                                       |
| pickle_pure_python         | 195 us                                                      | 198 us: 1.01x slower                                                        |
| pycparser                  | 699 ms                                                      | 707 ms: 1.01x slower                                                        |
| 2to3                       | 218 ms                                                      | 221 ms: 1.01x slower                                                        |
| meteor_contest             | 74.6 ms                                                     | 76.2 ms: 1.02x slower                                                       |
| sympy_integrate            | 13.0 ms                                                     | 13.3 ms: 1.03x slower                                                       |
| pprint_safe_repr           | 513 ms                                                      | 532 ms: 1.04x slower                                                        |
| regex_v8                   | 14.2 ms                                                     | 14.8 ms: 1.04x slower                                                       |
| docutils                   | 1.66 sec                                                    | 1.73 sec: 1.04x slower                                                      |
| sqlglot_normalize          | 187 ms                                                      | 196 ms: 1.05x slower                                                        |
| telco                      | 4.13 ms                                                     | 4.33 ms: 1.05x slower                                                       |
| sqlglot_optimize           | 34.5 ms                                                     | 36.4 ms: 1.05x slower                                                       |
| sympy_expand               | 284 ms                                                      | 300 ms: 1.06x slower                                                        |
| generators                 | 22.5 ms                                                     | 24.0 ms: 1.07x slower                                                       |
| raytrace                   | 192 ms                                                      | 206 ms: 1.07x slower                                                        |
| unpickle                   | 8.18 us                                                     | 8.77 us: 1.07x slower                                                       |
| pickle                     | 7.43 us                                                     | 8.11 us: 1.09x slower                                                       |
| pickle_list                | 2.83 us                                                     | 3.08 us: 1.09x slower                                                       |
| json_dumps                 | 5.70 ms                                                     | 6.24 ms: 1.10x slower                                                       |
| typing_runtime_protocols   | 95.1 us                                                     | 105 us: 1.11x slower                                                        |
| asyncio_tcp                | 487 ms                                                      | 543 ms: 1.11x slower                                                        |
| richards_super             | 32.1 ms                                                     | 35.8 ms: 1.11x slower                                                       |
| json_loads                 | 13.9 us                                                     | 15.5 us: 1.12x slower                                                       |
| unpack_sequence            | 37.5 ns                                                     | 41.9 ns: 1.12x slower                                                       |
| richards                   | 28.4 ms                                                     | 32.0 ms: 1.13x slower                                                       |
| coverage                   | 40.8 ms                                                     | 46.1 ms: 1.13x slower                                                       |
| django_template            | 22.9 ms                                                     | 26.1 ms: 1.14x slower                                                       |
| hexiom                     | 4.10 ms                                                     | 4.89 ms: 1.19x slower                                                       |
| mdp                        | 1.37 sec                                                    | 1.65 sec: 1.20x slower                                                      |
| python_startup_no_site     | 16.2 ms                                                     | 19.7 ms: 1.21x slower                                                       |
| bench_mp_pool              | 69.2 ms                                                     | 89.6 ms: 1.30x slower                                                       |
| gc_traversal               | 1.52 ms                                                     | 2.03 ms: 1.33x slower                                                       |
| python_startup             | 19.5 ms                                                     | 26.1 ms: 1.34x slower                                                       |
| create_gc_cycles           | 752 us                                                      | 1.23 ms: 1.63x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.07x faster                                                                |

Benchmark hidden because not significant (5): bench_thread_pool, deltablue, pickle_dict, sympy_str, sqlglot_parse
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (13) of results/bm-20250201-3.14.0a4+-cf4c4ec-JIT/bm-20250201-pythonperf1-amd64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.089x faster

# HPT report

- Reliability score: 99.79% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: unknown
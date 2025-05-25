# Results vs. 3.12.0

- fork: python
- ref: 2fd09b011031f3c00c34
- machine: windows-amd64
- commit hash: 2fd09b0
- commit date: 2025-05-24
- overall geometric mean: 1.009x slower
- HPT reliability: 97.27%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250524-pythonperf1-amd64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 226 ms: 1.04x slower                                                       |
| docutils       | 1.66 sec                                                    | 2.93 sec: 1.76x slower                                                     |
| Geometric mean | (ref)                                                       | 1.35x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250524-pythonperf1-amd64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 330 ms: 2.34x faster                                                       |
| async_tree_io              | 731 ms                                                      | 351 ms: 2.08x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 148 ms: 1.93x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 191 ms: 1.92x faster                                                       |
| async_tree_none            | 291 ms                                                      | 172 ms: 1.70x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 310 ms: 1.62x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 212 ms: 1.60x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 331 ms: 1.48x faster                                                       |
| Geometric mean             | (ref)                                                       | 1.81x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250524-pythonperf1-amd64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 46.2 ms: 1.23x faster                                                      |
| pidigits       | 152 ms                                                      | 135 ms: 1.13x faster                                                       |
| nbody          | 71.9 ms                                                     | 81.6 ms: 1.13x slower                                                      |
| Geometric mean | (ref)                                                       | 1.07x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250524-pythonperf1-amd64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_dna      | 126 ms                                                      | 114 ms: 1.11x faster                                                       |
| regex_v8       | 14.2 ms                                                     | 13.3 ms: 1.07x faster                                                      |
| regex_effbot   | 1.62 ms                                                     | 1.54 ms: 1.05x faster                                                      |
| regex_compile  | 87.5 ms                                                     | 95.8 ms: 1.09x slower                                                      |
| Geometric mean | (ref)                                                       | 1.03x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250524-pythonperf1-amd64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| xml_etree_iterparse  | 65.2 ms                                                     | 57.4 ms: 1.14x faster                                                      |
| xml_etree_parse      | 93.0 ms                                                     | 90.3 ms: 1.03x faster                                                      |
| pickle_list          | 2.83 us                                                     | 3.03 us: 1.07x slower                                                      |
| pickle               | 7.43 us                                                     | 8.01 us: 1.08x slower                                                      |
| pickle_dict          | 18.4 us                                                     | 20.1 us: 1.09x slower                                                      |
| unpickle_list        | 2.75 us                                                     | 3.04 us: 1.11x slower                                                      |
| xml_etree_generate   | 55.8 ms                                                     | 63.6 ms: 1.14x slower                                                      |
| unpickle_pure_python | 133 us                                                      | 153 us: 1.15x slower                                                       |
| json_dumps           | 5.70 ms                                                     | 6.72 ms: 1.18x slower                                                      |
| pickle_pure_python   | 195 us                                                      | 232 us: 1.19x slower                                                       |
| xml_etree_process    | 37.7 ms                                                     | 45.1 ms: 1.20x slower                                                      |
| json_loads           | 13.9 us                                                     | 16.8 us: 1.21x slower                                                      |
| unpickle             | 8.18 us                                                     | 10.6 us: 1.29x slower                                                      |
| tomli_loads          | 1.37 sec                                                    | 2.68 sec: 1.96x slower                                                     |
| Geometric mean       | (ref)                                                       | 1.16x slower                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250524-pythonperf1-amd64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 18.4 ms: 1.13x slower                                                      |
| python_startup         | 19.5 ms                                                     | 24.6 ms: 1.26x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.20x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250524-pythonperf1-amd64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| django_template | 22.9 ms                                                     | 27.5 ms: 1.20x slower                                                      |
| mako            | 7.09 ms                                                     | 9.66 ms: 1.36x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.28x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250524-pythonperf1-amd64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pathlib                    | 80.5 ms                                                     | 29.8 ms: 2.70x faster                                                      |
| async_tree_io_tg           | 771 ms                                                      | 330 ms: 2.34x faster                                                       |
| async_tree_io              | 731 ms                                                      | 351 ms: 2.08x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 148 ms: 1.93x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 191 ms: 1.92x faster                                                       |
| async_tree_none            | 291 ms                                                      | 172 ms: 1.70x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 310 ms: 1.62x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 212 ms: 1.60x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 331 ms: 1.48x faster                                                       |
| sqlite_synth               | 1.76 us                                                     | 1.33 us: 1.32x faster                                                      |
| gc_traversal               | 1.52 ms                                                     | 1.17 ms: 1.30x faster                                                      |
| float                      | 56.8 ms                                                     | 46.2 ms: 1.23x faster                                                      |
| deepcopy                   | 238 us                                                      | 203 us: 1.17x faster                                                       |
| mdp                        | 1.37 sec                                                    | 1.17 sec: 1.17x faster                                                     |
| xml_etree_iterparse        | 65.2 ms                                                     | 57.4 ms: 1.14x faster                                                      |
| pidigits                   | 152 ms                                                      | 135 ms: 1.13x faster                                                       |
| asyncio_tcp                | 487 ms                                                      | 439 ms: 1.11x faster                                                       |
| regex_dna                  | 126 ms                                                      | 114 ms: 1.11x faster                                                       |
| deepcopy_memo              | 23.7 us                                                     | 21.8 us: 1.09x faster                                                      |
| comprehensions             | 14.1 us                                                     | 13.1 us: 1.08x faster                                                      |
| regex_v8                   | 14.2 ms                                                     | 13.3 ms: 1.07x faster                                                      |
| dulwich_log                | 44.3 ms                                                     | 41.3 ms: 1.07x faster                                                      |
| coroutines                 | 14.3 ms                                                     | 13.3 ms: 1.07x faster                                                      |
| regex_effbot               | 1.62 ms                                                     | 1.54 ms: 1.05x faster                                                      |
| xml_etree_parse            | 93.0 ms                                                     | 90.3 ms: 1.03x faster                                                      |
| generators                 | 22.5 ms                                                     | 22.2 ms: 1.01x faster                                                      |
| go                         | 91.6 ms                                                     | 93.4 ms: 1.02x slower                                                      |
| deepcopy_reduce            | 2.09 us                                                     | 2.14 us: 1.02x slower                                                      |
| spectral_norm              | 66.9 ms                                                     | 69.2 ms: 1.03x slower                                                      |
| unpack_sequence            | 37.5 ns                                                     | 38.8 ns: 1.04x slower                                                      |
| 2to3                       | 218 ms                                                      | 226 ms: 1.04x slower                                                       |
| pycparser                  | 699 ms                                                      | 725 ms: 1.04x slower                                                       |
| chaos                      | 43.3 ms                                                     | 45.4 ms: 1.05x slower                                                      |
| json                       | 3.05 ms                                                     | 3.24 ms: 1.06x slower                                                      |
| sympy_sum                  | 91.5 ms                                                     | 97.4 ms: 1.06x slower                                                      |
| pickle_list                | 2.83 us                                                     | 3.03 us: 1.07x slower                                                      |
| pickle                     | 7.43 us                                                     | 8.01 us: 1.08x slower                                                      |
| sympy_str                  | 175 ms                                                      | 190 ms: 1.09x slower                                                       |
| pyflate                    | 295 ms                                                      | 320 ms: 1.09x slower                                                       |
| pickle_dict                | 18.4 us                                                     | 20.1 us: 1.09x slower                                                      |
| bench_mp_pool              | 69.2 ms                                                     | 75.7 ms: 1.09x slower                                                      |
| regex_compile              | 87.5 ms                                                     | 95.8 ms: 1.09x slower                                                      |
| scimark_sor                | 78.8 ms                                                     | 86.4 ms: 1.10x slower                                                      |
| scimark_lu                 | 58.9 ms                                                     | 64.6 ms: 1.10x slower                                                      |
| sympy_integrate            | 13.0 ms                                                     | 14.2 ms: 1.10x slower                                                      |
| unpickle_list              | 2.75 us                                                     | 3.04 us: 1.11x slower                                                      |
| raytrace                   | 192 ms                                                      | 214 ms: 1.11x slower                                                       |
| nqueens                    | 62.8 ms                                                     | 70.8 ms: 1.13x slower                                                      |
| logging_format             | 6.72 us                                                     | 7.60 us: 1.13x slower                                                      |
| scimark_fft                | 184 ms                                                      | 209 ms: 1.13x slower                                                       |
| python_startup_no_site     | 16.2 ms                                                     | 18.4 ms: 1.13x slower                                                      |
| logging_simple             | 6.28 us                                                     | 7.12 us: 1.13x slower                                                      |
| nbody                      | 71.9 ms                                                     | 81.6 ms: 1.13x slower                                                      |
| deltablue                  | 2.16 ms                                                     | 2.46 ms: 1.14x slower                                                      |
| xml_etree_generate         | 55.8 ms                                                     | 63.6 ms: 1.14x slower                                                      |
| async_generators           | 239 ms                                                      | 273 ms: 1.14x slower                                                       |
| hexiom                     | 4.10 ms                                                     | 4.69 ms: 1.14x slower                                                      |
| crypto_pyaes               | 48.5 ms                                                     | 55.5 ms: 1.14x slower                                                      |
| sympy_expand               | 284 ms                                                      | 326 ms: 1.15x slower                                                       |
| unpickle_pure_python       | 133 us                                                      | 153 us: 1.15x slower                                                       |
| scimark_monte_carlo        | 43.7 ms                                                     | 51.4 ms: 1.18x slower                                                      |
| json_dumps                 | 5.70 ms                                                     | 6.72 ms: 1.18x slower                                                      |
| meteor_contest             | 74.6 ms                                                     | 88.3 ms: 1.18x slower                                                      |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 3.04 ms: 1.19x slower                                                      |
| pickle_pure_python         | 195 us                                                      | 232 us: 1.19x slower                                                       |
| richards                   | 28.4 ms                                                     | 33.8 ms: 1.19x slower                                                      |
| xml_etree_process          | 37.7 ms                                                     | 45.1 ms: 1.20x slower                                                      |
| django_template            | 22.9 ms                                                     | 27.5 ms: 1.20x slower                                                      |
| fannkuch                   | 247 ms                                                      | 296 ms: 1.20x slower                                                       |
| json_loads                 | 13.9 us                                                     | 16.8 us: 1.21x slower                                                      |
| pprint_safe_repr           | 513 ms                                                      | 628 ms: 1.22x slower                                                       |
| richards_super             | 32.1 ms                                                     | 39.7 ms: 1.24x slower                                                      |
| python_startup             | 19.5 ms                                                     | 24.6 ms: 1.26x slower                                                      |
| telco                      | 4.13 ms                                                     | 5.32 ms: 1.29x slower                                                      |
| unpickle                   | 8.18 us                                                     | 10.6 us: 1.29x slower                                                      |
| bench_thread_pool          | 857 us                                                      | 1.12 ms: 1.31x slower                                                      |
| create_gc_cycles           | 752 us                                                      | 1.00 ms: 1.34x slower                                                      |
| mako                       | 7.09 ms                                                     | 9.66 ms: 1.36x slower                                                      |
| typing_runtime_protocols   | 95.1 us                                                     | 133 us: 1.40x slower                                                       |
| coverage                   | 40.8 ms                                                     | 66.7 ms: 1.63x slower                                                      |
| docutils                   | 1.66 sec                                                    | 2.93 sec: 1.76x slower                                                     |
| tomli_loads                | 1.37 sec                                                    | 2.68 sec: 1.96x slower                                                     |
| pprint_pformat             | 1.05 sec                                                    | 2.13 sec: 2.04x slower                                                     |
| logging_silent             | 60.5 ns                                                     | 371 ns: 6.14x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.05x slower                                                               |

Benchmark hidden because not significant (1): asyncio_tcp_ssl
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (17) of results/bm-20250524-3.15.0a0-2fd09b0-NOGIL/bm-20250524-pythonperf1-amd64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.009x slower

# HPT report

- Reliability score: 97.27% likely to be slow
- 90% likely to have a slowdown of 1.03x
- 95% likely to have a slowdown of 1.02x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown
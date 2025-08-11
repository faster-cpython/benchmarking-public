# Results vs. 3.12.0

- fork: python
- ref: 046a4e39b3f8ac5cb13e
- machine: windows-amd64
- commit hash: 046a4e3
- commit date: 2025-08-09
- overall geometric mean: 1.010x slower
- HPT reliability: 98.41%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250809-pythonperf1-amd64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 225 ms: 1.03x slower                                                       |
| docutils       | 1.66 sec                                                    | 2.79 sec: 1.68x slower                                                     |
| Geometric mean | (ref)                                                       | 1.32x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250809-pythonperf1-amd64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 328 ms: 2.35x faster                                                       |
| async_tree_io              | 731 ms                                                      | 352 ms: 2.08x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 148 ms: 1.93x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 190 ms: 1.93x faster                                                       |
| async_tree_none            | 291 ms                                                      | 171 ms: 1.71x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 303 ms: 1.65x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 210 ms: 1.62x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 325 ms: 1.51x faster                                                       |
| Geometric mean             | (ref)                                                       | 1.83x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250809-pythonperf1-amd64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 45.8 ms: 1.24x faster                                                      |
| pidigits       | 152 ms                                                      | 136 ms: 1.12x faster                                                       |
| nbody          | 71.9 ms                                                     | 85.0 ms: 1.18x slower                                                      |
| Geometric mean | (ref)                                                       | 1.05x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250809-pythonperf1-amd64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_dna      | 126 ms                                                      | 113 ms: 1.12x faster                                                       |
| regex_v8       | 14.2 ms                                                     | 13.1 ms: 1.09x faster                                                      |
| regex_compile  | 87.5 ms                                                     | 93.6 ms: 1.07x slower                                                      |
| Geometric mean | (ref)                                                       | 1.03x faster                                                               |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250809-pythonperf1-amd64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| xml_etree_iterparse  | 65.2 ms                                                     | 57.4 ms: 1.14x faster                                                      |
| xml_etree_parse      | 93.0 ms                                                     | 89.4 ms: 1.04x faster                                                      |
| json_dumps           | 5.70 ms                                                     | 5.89 ms: 1.03x slower                                                      |
| pickle_list          | 2.83 us                                                     | 2.93 us: 1.04x slower                                                      |
| pickle               | 7.43 us                                                     | 7.72 us: 1.04x slower                                                      |
| pickle_dict          | 18.4 us                                                     | 19.8 us: 1.08x slower                                                      |
| xml_etree_generate   | 55.8 ms                                                     | 61.9 ms: 1.11x slower                                                      |
| unpickle_list        | 2.75 us                                                     | 3.07 us: 1.12x slower                                                      |
| json_loads           | 13.9 us                                                     | 15.6 us: 1.12x slower                                                      |
| xml_etree_process    | 37.7 ms                                                     | 44.3 ms: 1.17x slower                                                      |
| unpickle_pure_python | 133 us                                                      | 160 us: 1.20x slower                                                       |
| pickle_pure_python   | 195 us                                                      | 237 us: 1.21x slower                                                       |
| unpickle             | 8.18 us                                                     | 10.1 us: 1.24x slower                                                      |
| tomli_loads          | 1.37 sec                                                    | 2.67 sec: 1.96x slower                                                     |
| Geometric mean       | (ref)                                                       | 1.13x slower                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250809-pythonperf1-amd64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 19.8 ms: 1.22x slower                                                      |
| python_startup         | 19.5 ms                                                     | 26.5 ms: 1.36x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.29x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250809-pythonperf1-amd64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| django_template | 22.9 ms                                                     | 26.9 ms: 1.17x slower                                                      |
| mako            | 7.09 ms                                                     | 9.93 ms: 1.40x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.28x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250809-pythonperf1-amd64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 328 ms: 2.35x faster                                                       |
| pathlib                    | 80.5 ms                                                     | 36.1 ms: 2.23x faster                                                      |
| async_tree_io              | 731 ms                                                      | 352 ms: 2.08x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 148 ms: 1.93x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 190 ms: 1.93x faster                                                       |
| async_tree_none            | 291 ms                                                      | 171 ms: 1.71x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 303 ms: 1.65x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 210 ms: 1.62x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 325 ms: 1.51x faster                                                       |
| sqlite_synth               | 1.76 us                                                     | 1.36 us: 1.29x faster                                                      |
| gc_traversal               | 1.52 ms                                                     | 1.20 ms: 1.26x faster                                                      |
| float                      | 56.8 ms                                                     | 45.8 ms: 1.24x faster                                                      |
| mdp                        | 1.37 sec                                                    | 1.15 sec: 1.20x faster                                                     |
| comprehensions             | 14.1 us                                                     | 12.2 us: 1.16x faster                                                      |
| deepcopy                   | 238 us                                                      | 207 us: 1.15x faster                                                       |
| xml_etree_iterparse        | 65.2 ms                                                     | 57.4 ms: 1.14x faster                                                      |
| pidigits                   | 152 ms                                                      | 136 ms: 1.12x faster                                                       |
| regex_dna                  | 126 ms                                                      | 113 ms: 1.12x faster                                                       |
| deepcopy_memo              | 23.7 us                                                     | 21.5 us: 1.10x faster                                                      |
| regex_v8                   | 14.2 ms                                                     | 13.1 ms: 1.09x faster                                                      |
| dulwich_log                | 44.3 ms                                                     | 41.9 ms: 1.06x faster                                                      |
| xml_etree_parse            | 93.0 ms                                                     | 89.4 ms: 1.04x faster                                                      |
| go                         | 91.6 ms                                                     | 92.3 ms: 1.01x slower                                                      |
| logging_silent             | 60.5 ns                                                     | 61.4 ns: 1.01x slower                                                      |
| deepcopy_reduce            | 2.09 us                                                     | 2.14 us: 1.02x slower                                                      |
| 2to3                       | 218 ms                                                      | 225 ms: 1.03x slower                                                       |
| json_dumps                 | 5.70 ms                                                     | 5.89 ms: 1.03x slower                                                      |
| pickle_list                | 2.83 us                                                     | 2.93 us: 1.04x slower                                                      |
| pickle                     | 7.43 us                                                     | 7.72 us: 1.04x slower                                                      |
| unpack_sequence            | 37.5 ns                                                     | 39.1 ns: 1.04x slower                                                      |
| generators                 | 22.5 ms                                                     | 23.6 ms: 1.05x slower                                                      |
| sympy_sum                  | 91.5 ms                                                     | 95.8 ms: 1.05x slower                                                      |
| pycparser                  | 699 ms                                                      | 738 ms: 1.06x slower                                                       |
| logging_simple             | 6.28 us                                                     | 6.65 us: 1.06x slower                                                      |
| logging_format             | 6.72 us                                                     | 7.14 us: 1.06x slower                                                      |
| sympy_str                  | 175 ms                                                      | 187 ms: 1.07x slower                                                       |
| async_generators           | 239 ms                                                      | 256 ms: 1.07x slower                                                       |
| regex_compile              | 87.5 ms                                                     | 93.6 ms: 1.07x slower                                                      |
| coroutines                 | 14.3 ms                                                     | 15.3 ms: 1.07x slower                                                      |
| pickle_dict                | 18.4 us                                                     | 19.8 us: 1.08x slower                                                      |
| sympy_integrate            | 13.0 ms                                                     | 14.0 ms: 1.08x slower                                                      |
| raytrace                   | 192 ms                                                      | 208 ms: 1.08x slower                                                       |
| chaos                      | 43.3 ms                                                     | 47.0 ms: 1.08x slower                                                      |
| pyflate                    | 295 ms                                                      | 321 ms: 1.09x slower                                                       |
| pprint_safe_repr           | 513 ms                                                      | 567 ms: 1.10x slower                                                       |
| xml_etree_generate         | 55.8 ms                                                     | 61.9 ms: 1.11x slower                                                      |
| unpickle_list              | 2.75 us                                                     | 3.07 us: 1.12x slower                                                      |
| scimark_lu                 | 58.9 ms                                                     | 65.8 ms: 1.12x slower                                                      |
| asyncio_tcp                | 487 ms                                                      | 547 ms: 1.12x slower                                                       |
| json_loads                 | 13.9 us                                                     | 15.6 us: 1.12x slower                                                      |
| asyncio_tcp_ssl            | 2.10 sec                                                    | 2.37 sec: 1.13x slower                                                     |
| deltablue                  | 2.16 ms                                                     | 2.45 ms: 1.13x slower                                                      |
| sympy_expand               | 284 ms                                                      | 325 ms: 1.14x slower                                                       |
| bench_mp_pool              | 69.2 ms                                                     | 79.2 ms: 1.15x slower                                                      |
| scimark_sor                | 78.8 ms                                                     | 90.3 ms: 1.15x slower                                                      |
| meteor_contest             | 74.6 ms                                                     | 85.6 ms: 1.15x slower                                                      |
| spectral_norm              | 66.9 ms                                                     | 77.1 ms: 1.15x slower                                                      |
| hexiom                     | 4.10 ms                                                     | 4.74 ms: 1.16x slower                                                      |
| scimark_monte_carlo        | 43.7 ms                                                     | 50.7 ms: 1.16x slower                                                      |
| django_template            | 22.9 ms                                                     | 26.9 ms: 1.17x slower                                                      |
| xml_etree_process          | 37.7 ms                                                     | 44.3 ms: 1.17x slower                                                      |
| scimark_fft                | 184 ms                                                      | 217 ms: 1.18x slower                                                       |
| crypto_pyaes               | 48.5 ms                                                     | 57.1 ms: 1.18x slower                                                      |
| richards                   | 28.4 ms                                                     | 33.5 ms: 1.18x slower                                                      |
| nbody                      | 71.9 ms                                                     | 85.0 ms: 1.18x slower                                                      |
| nqueens                    | 62.8 ms                                                     | 74.7 ms: 1.19x slower                                                      |
| unpickle_pure_python       | 133 us                                                      | 160 us: 1.20x slower                                                       |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 3.09 ms: 1.21x slower                                                      |
| pickle_pure_python         | 195 us                                                      | 237 us: 1.21x slower                                                       |
| richards_super             | 32.1 ms                                                     | 39.1 ms: 1.22x slower                                                      |
| python_startup_no_site     | 16.2 ms                                                     | 19.8 ms: 1.22x slower                                                      |
| unpickle                   | 8.18 us                                                     | 10.1 us: 1.24x slower                                                      |
| telco                      | 4.13 ms                                                     | 5.19 ms: 1.26x slower                                                      |
| bench_thread_pool          | 857 us                                                      | 1.09 ms: 1.27x slower                                                      |
| fannkuch                   | 247 ms                                                      | 316 ms: 1.28x slower                                                       |
| create_gc_cycles           | 752 us                                                      | 1.02 ms: 1.36x slower                                                      |
| python_startup             | 19.5 ms                                                     | 26.5 ms: 1.36x slower                                                      |
| mako                       | 7.09 ms                                                     | 9.93 ms: 1.40x slower                                                      |
| typing_runtime_protocols   | 95.1 us                                                     | 134 us: 1.41x slower                                                       |
| pprint_pformat             | 1.05 sec                                                    | 1.69 sec: 1.62x slower                                                     |
| coverage                   | 40.8 ms                                                     | 66.6 ms: 1.63x slower                                                      |
| docutils                   | 1.66 sec                                                    | 2.79 sec: 1.68x slower                                                     |
| tomli_loads                | 1.37 sec                                                    | 2.67 sec: 1.96x slower                                                     |
| Geometric mean             | (ref)                                                       | 1.03x slower                                                               |

Benchmark hidden because not significant (2): regex_effbot, json
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (17) of results/bm-20250809-3.15.0a0-046a4e3-NOGIL/bm-20250809-pythonperf1-amd64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.010x slower

# HPT report

- Reliability score: 98.41% likely to be slow
- 90% likely to have a slowdown of 1.04x
- 95% likely to have a slowdown of 1.03x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown
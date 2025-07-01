# Results vs. 3.12.0

- fork: python
- ref: 75f40595e555e7d016cf
- machine: windows-amd64
- commit hash: 75f4059
- commit date: 2025-06-30
- overall geometric mean: 1.021x slower
- HPT reliability: 99.00%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250630-pythonperf1-amd64-python-75f40595e555e7d016cf-3.15.0a0-75f4059 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 230 ms: 1.06x slower                                                       |
| docutils       | 1.66 sec                                                    | 2.93 sec: 1.76x slower                                                     |
| Geometric mean | (ref)                                                       | 1.36x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250630-pythonperf1-amd64-python-75f40595e555e7d016cf-3.15.0a0-75f4059 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 337 ms: 2.29x faster                                                       |
| async_tree_io              | 731 ms                                                      | 361 ms: 2.03x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 152 ms: 1.87x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 196 ms: 1.87x faster                                                       |
| async_tree_none            | 291 ms                                                      | 175 ms: 1.67x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 318 ms: 1.58x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 216 ms: 1.57x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 340 ms: 1.44x faster                                                       |
| Geometric mean             | (ref)                                                       | 1.77x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250630-pythonperf1-amd64-python-75f40595e555e7d016cf-3.15.0a0-75f4059 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 46.2 ms: 1.23x faster                                                      |
| pidigits       | 152 ms                                                      | 137 ms: 1.11x faster                                                       |
| nbody          | 71.9 ms                                                     | 83.3 ms: 1.16x slower                                                      |
| Geometric mean | (ref)                                                       | 1.06x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250630-pythonperf1-amd64-python-75f40595e555e7d016cf-3.15.0a0-75f4059 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_dna      | 126 ms                                                      | 114 ms: 1.11x faster                                                       |
| regex_v8       | 14.2 ms                                                     | 13.6 ms: 1.05x faster                                                      |
| regex_compile  | 87.5 ms                                                     | 96.3 ms: 1.10x slower                                                      |
| Geometric mean | (ref)                                                       | 1.01x faster                                                               |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250630-pythonperf1-amd64-python-75f40595e555e7d016cf-3.15.0a0-75f4059 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| xml_etree_iterparse  | 65.2 ms                                                     | 58.6 ms: 1.11x faster                                                      |
| xml_etree_parse      | 93.0 ms                                                     | 90.7 ms: 1.03x faster                                                      |
| pickle_list          | 2.83 us                                                     | 3.05 us: 1.08x slower                                                      |
| pickle_dict          | 18.4 us                                                     | 20.6 us: 1.12x slower                                                      |
| unpickle_list        | 2.75 us                                                     | 3.09 us: 1.13x slower                                                      |
| pickle               | 7.43 us                                                     | 8.39 us: 1.13x slower                                                      |
| json_loads           | 13.9 us                                                     | 16.0 us: 1.15x slower                                                      |
| xml_etree_generate   | 55.8 ms                                                     | 64.4 ms: 1.15x slower                                                      |
| unpickle_pure_python | 133 us                                                      | 156 us: 1.17x slower                                                       |
| json_dumps           | 5.70 ms                                                     | 6.68 ms: 1.17x slower                                                      |
| pickle_pure_python   | 195 us                                                      | 234 us: 1.20x slower                                                       |
| xml_etree_process    | 37.7 ms                                                     | 45.8 ms: 1.21x slower                                                      |
| unpickle             | 8.18 us                                                     | 10.2 us: 1.25x slower                                                      |
| tomli_loads          | 1.37 sec                                                    | 2.71 sec: 1.98x slower                                                     |
| Geometric mean       | (ref)                                                       | 1.17x slower                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250630-pythonperf1-amd64-python-75f40595e555e7d016cf-3.15.0a0-75f4059 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 19.6 ms: 1.20x slower                                                      |
| python_startup         | 19.5 ms                                                     | 25.9 ms: 1.33x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.27x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250630-pythonperf1-amd64-python-75f40595e555e7d016cf-3.15.0a0-75f4059 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| django_template | 22.9 ms                                                     | 27.6 ms: 1.20x slower                                                      |
| mako            | 7.09 ms                                                     | 9.77 ms: 1.38x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.29x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250630-pythonperf1-amd64-python-75f40595e555e7d016cf-3.15.0a0-75f4059 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pathlib                    | 80.5 ms                                                     | 32.1 ms: 2.51x faster                                                      |
| async_tree_io_tg           | 771 ms                                                      | 337 ms: 2.29x faster                                                       |
| async_tree_io              | 731 ms                                                      | 361 ms: 2.03x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 152 ms: 1.87x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 196 ms: 1.87x faster                                                       |
| async_tree_none            | 291 ms                                                      | 175 ms: 1.67x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 318 ms: 1.58x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 216 ms: 1.57x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 340 ms: 1.44x faster                                                       |
| sqlite_synth               | 1.76 us                                                     | 1.33 us: 1.32x faster                                                      |
| float                      | 56.8 ms                                                     | 46.2 ms: 1.23x faster                                                      |
| gc_traversal               | 1.52 ms                                                     | 1.24 ms: 1.23x faster                                                      |
| mdp                        | 1.37 sec                                                    | 1.15 sec: 1.19x faster                                                     |
| comprehensions             | 14.1 us                                                     | 12.1 us: 1.17x faster                                                      |
| deepcopy                   | 238 us                                                      | 205 us: 1.16x faster                                                       |
| deepcopy_memo              | 23.7 us                                                     | 21.2 us: 1.12x faster                                                      |
| xml_etree_iterparse        | 65.2 ms                                                     | 58.6 ms: 1.11x faster                                                      |
| pidigits                   | 152 ms                                                      | 137 ms: 1.11x faster                                                       |
| regex_dna                  | 126 ms                                                      | 114 ms: 1.11x faster                                                       |
| regex_v8                   | 14.2 ms                                                     | 13.6 ms: 1.05x faster                                                      |
| dulwich_log                | 44.3 ms                                                     | 43.1 ms: 1.03x faster                                                      |
| xml_etree_parse            | 93.0 ms                                                     | 90.7 ms: 1.03x faster                                                      |
| unpack_sequence            | 37.5 ns                                                     | 37.8 ns: 1.01x slower                                                      |
| json                       | 3.05 ms                                                     | 3.10 ms: 1.02x slower                                                      |
| deepcopy_reduce            | 2.09 us                                                     | 2.13 us: 1.02x slower                                                      |
| go                         | 91.6 ms                                                     | 93.7 ms: 1.02x slower                                                      |
| generators                 | 22.5 ms                                                     | 23.2 ms: 1.03x slower                                                      |
| coroutines                 | 14.3 ms                                                     | 14.8 ms: 1.04x slower                                                      |
| logging_silent             | 60.5 ns                                                     | 63.1 ns: 1.04x slower                                                      |
| 2to3                       | 218 ms                                                      | 230 ms: 1.06x slower                                                       |
| pycparser                  | 699 ms                                                      | 738 ms: 1.06x slower                                                       |
| pyflate                    | 295 ms                                                      | 315 ms: 1.07x slower                                                       |
| pickle_list                | 2.83 us                                                     | 3.05 us: 1.08x slower                                                      |
| chaos                      | 43.3 ms                                                     | 46.9 ms: 1.08x slower                                                      |
| logging_simple             | 6.28 us                                                     | 6.81 us: 1.09x slower                                                      |
| logging_format             | 6.72 us                                                     | 7.31 us: 1.09x slower                                                      |
| sympy_sum                  | 91.5 ms                                                     | 99.7 ms: 1.09x slower                                                      |
| sympy_str                  | 175 ms                                                      | 191 ms: 1.09x slower                                                       |
| regex_compile              | 87.5 ms                                                     | 96.3 ms: 1.10x slower                                                      |
| sympy_integrate            | 13.0 ms                                                     | 14.3 ms: 1.10x slower                                                      |
| raytrace                   | 192 ms                                                      | 213 ms: 1.11x slower                                                       |
| asyncio_tcp_ssl            | 2.10 sec                                                    | 2.32 sec: 1.11x slower                                                     |
| pprint_safe_repr           | 513 ms                                                      | 569 ms: 1.11x slower                                                       |
| async_generators           | 239 ms                                                      | 266 ms: 1.11x slower                                                       |
| spectral_norm              | 66.9 ms                                                     | 74.4 ms: 1.11x slower                                                      |
| pickle_dict                | 18.4 us                                                     | 20.6 us: 1.12x slower                                                      |
| scimark_lu                 | 58.9 ms                                                     | 65.9 ms: 1.12x slower                                                      |
| unpickle_list              | 2.75 us                                                     | 3.09 us: 1.13x slower                                                      |
| hexiom                     | 4.10 ms                                                     | 4.62 ms: 1.13x slower                                                      |
| pickle                     | 7.43 us                                                     | 8.39 us: 1.13x slower                                                      |
| scimark_sor                | 78.8 ms                                                     | 88.9 ms: 1.13x slower                                                      |
| scimark_monte_carlo        | 43.7 ms                                                     | 49.7 ms: 1.14x slower                                                      |
| json_loads                 | 13.9 us                                                     | 16.0 us: 1.15x slower                                                      |
| deltablue                  | 2.16 ms                                                     | 2.48 ms: 1.15x slower                                                      |
| xml_etree_generate         | 55.8 ms                                                     | 64.4 ms: 1.15x slower                                                      |
| bench_mp_pool              | 69.2 ms                                                     | 80.1 ms: 1.16x slower                                                      |
| nbody                      | 71.9 ms                                                     | 83.3 ms: 1.16x slower                                                      |
| meteor_contest             | 74.6 ms                                                     | 86.8 ms: 1.16x slower                                                      |
| crypto_pyaes               | 48.5 ms                                                     | 56.4 ms: 1.16x slower                                                      |
| unpickle_pure_python       | 133 us                                                      | 156 us: 1.17x slower                                                       |
| nqueens                    | 62.8 ms                                                     | 73.4 ms: 1.17x slower                                                      |
| sympy_expand               | 284 ms                                                      | 332 ms: 1.17x slower                                                       |
| json_dumps                 | 5.70 ms                                                     | 6.68 ms: 1.17x slower                                                      |
| scimark_fft                | 184 ms                                                      | 219 ms: 1.19x slower                                                       |
| pickle_pure_python         | 195 us                                                      | 234 us: 1.20x slower                                                       |
| richards                   | 28.4 ms                                                     | 34.0 ms: 1.20x slower                                                      |
| django_template            | 22.9 ms                                                     | 27.6 ms: 1.20x slower                                                      |
| python_startup_no_site     | 16.2 ms                                                     | 19.6 ms: 1.20x slower                                                      |
| fannkuch                   | 247 ms                                                      | 299 ms: 1.21x slower                                                       |
| xml_etree_process          | 37.7 ms                                                     | 45.8 ms: 1.21x slower                                                      |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 3.12 ms: 1.22x slower                                                      |
| richards_super             | 32.1 ms                                                     | 39.7 ms: 1.24x slower                                                      |
| unpickle                   | 8.18 us                                                     | 10.2 us: 1.25x slower                                                      |
| bench_thread_pool          | 857 us                                                      | 1.08 ms: 1.26x slower                                                      |
| python_startup             | 19.5 ms                                                     | 25.9 ms: 1.33x slower                                                      |
| telco                      | 4.13 ms                                                     | 5.55 ms: 1.34x slower                                                      |
| typing_runtime_protocols   | 95.1 us                                                     | 131 us: 1.38x slower                                                       |
| mako                       | 7.09 ms                                                     | 9.77 ms: 1.38x slower                                                      |
| create_gc_cycles           | 752 us                                                      | 1.06 ms: 1.41x slower                                                      |
| coverage                   | 40.8 ms                                                     | 67.6 ms: 1.65x slower                                                      |
| pprint_pformat             | 1.05 sec                                                    | 1.77 sec: 1.70x slower                                                     |
| docutils                   | 1.66 sec                                                    | 2.93 sec: 1.76x slower                                                     |
| tomli_loads                | 1.37 sec                                                    | 2.71 sec: 1.98x slower                                                     |
| Geometric mean             | (ref)                                                       | 1.03x slower                                                               |

Benchmark hidden because not significant (2): asyncio_tcp, regex_effbot
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (17) of results/bm-20250630-3.15.0a0-75f4059-NOGIL/bm-20250630-pythonperf1-amd64-python-75f40595e555e7d016cf-3.15.0a0-75f4059.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.021x slower

# HPT report

- Reliability score: 99.00% likely to be slow
- 90% likely to have a slowdown of 1.05x
- 95% likely to have a slowdown of 1.03x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown
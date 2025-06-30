# Results vs. 3.12.0

- fork: python
- ref: 75f40595e555e7d016cf
- machine: windows-amd64
- commit hash: 75f4059
- commit date: 2025-06-30
- overall geometric mean: 1.110x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250630-pythonperf1-amd64-python-75f40595e555e7d016cf-3.15.0a0-75f4059 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 221 ms: 1.01x slower                                                       |
| docutils       | 1.66 sec                                                    | 1.68 sec: 1.01x slower                                                     |
| Geometric mean | (ref)                                                       | 1.01x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250630-pythonperf1-amd64-python-75f40595e555e7d016cf-3.15.0a0-75f4059 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 391 ms: 1.97x faster                                                       |
| async_tree_io              | 731 ms                                                      | 400 ms: 1.83x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 212 ms: 1.73x faster                                                       |
| async_tree_none            | 291 ms                                                      | 171 ms: 1.70x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 169 ms: 1.69x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 208 ms: 1.63x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 329 ms: 1.48x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 344 ms: 1.46x faster                                                       |
| Geometric mean             | (ref)                                                       | 1.68x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250630-pythonperf1-amd64-python-75f40595e555e7d016cf-3.15.0a0-75f4059 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 71.9 ms                                                     | 53.7 ms: 1.34x faster                                                      |
| float          | 56.8 ms                                                     | 44.9 ms: 1.26x faster                                                      |
| pidigits       | 152 ms                                                      | 147 ms: 1.03x faster                                                       |
| Geometric mean | (ref)                                                       | 1.20x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250630-pythonperf1-amd64-python-75f40595e555e7d016cf-3.15.0a0-75f4059 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 87.5 ms                                                     | 78.9 ms: 1.11x faster                                                      |
| regex_dna      | 126 ms                                                      | 120 ms: 1.06x faster                                                       |
| regex_v8       | 14.2 ms                                                     | 14.0 ms: 1.02x faster                                                      |
| Geometric mean | (ref)                                                       | 1.04x faster                                                               |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250630-pythonperf1-amd64-python-75f40595e555e7d016cf-3.15.0a0-75f4059 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| unpickle_pure_python | 133 us                                                      | 108 us: 1.23x faster                                                       |
| tomli_loads          | 1.37 sec                                                    | 1.14 sec: 1.20x faster                                                     |
| xml_etree_generate   | 55.8 ms                                                     | 51.2 ms: 1.09x faster                                                      |
| xml_etree_process    | 37.7 ms                                                     | 35.9 ms: 1.05x faster                                                      |
| xml_etree_parse      | 93.0 ms                                                     | 88.9 ms: 1.05x faster                                                      |
| xml_etree_iterparse  | 65.2 ms                                                     | 63.9 ms: 1.02x faster                                                      |
| unpickle_list        | 2.75 us                                                     | 2.79 us: 1.01x slower                                                      |
| pickle               | 7.43 us                                                     | 7.60 us: 1.02x slower                                                      |
| json_loads           | 13.9 us                                                     | 14.4 us: 1.04x slower                                                      |
| unpickle             | 8.18 us                                                     | 8.54 us: 1.04x slower                                                      |
| pickle_pure_python   | 195 us                                                      | 205 us: 1.05x slower                                                       |
| pickle_dict          | 18.4 us                                                     | 19.9 us: 1.08x slower                                                      |
| json_dumps           | 5.70 ms                                                     | 6.28 ms: 1.10x slower                                                      |
| pickle_list          | 2.83 us                                                     | 3.43 us: 1.21x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.00x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250630-pythonperf1-amd64-python-75f40595e555e7d016cf-3.15.0a0-75f4059 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 19.5 ms: 1.20x slower                                                      |
| python_startup         | 19.5 ms                                                     | 26.0 ms: 1.34x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.26x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250630-pythonperf1-amd64-python-75f40595e555e7d016cf-3.15.0a0-75f4059 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 5.39 ms: 1.32x faster                                                      |
| django_template | 22.9 ms                                                     | 24.3 ms: 1.06x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.11x faster                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250630-pythonperf1-amd64-python-75f40595e555e7d016cf-3.15.0a0-75f4059 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pathlib                    | 80.5 ms                                                     | 31.7 ms: 2.54x faster                                                      |
| async_tree_io_tg           | 771 ms                                                      | 391 ms: 1.97x faster                                                       |
| async_tree_io              | 731 ms                                                      | 400 ms: 1.83x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 212 ms: 1.73x faster                                                       |
| mdp                        | 1.37 sec                                                    | 803 ms: 1.71x faster                                                       |
| async_tree_none            | 291 ms                                                      | 171 ms: 1.70x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 169 ms: 1.69x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 208 ms: 1.63x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 329 ms: 1.48x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 344 ms: 1.46x faster                                                       |
| asyncio_tcp_ssl            | 2.10 sec                                                    | 1.45 sec: 1.44x faster                                                     |
| deepcopy                   | 238 us                                                      | 169 us: 1.41x faster                                                       |
| nbody                      | 71.9 ms                                                     | 53.7 ms: 1.34x faster                                                      |
| deepcopy_memo              | 23.7 us                                                     | 18.0 us: 1.32x faster                                                      |
| mako                       | 7.09 ms                                                     | 5.39 ms: 1.32x faster                                                      |
| comprehensions             | 14.1 us                                                     | 10.7 us: 1.32x faster                                                      |
| float                      | 56.8 ms                                                     | 44.9 ms: 1.26x faster                                                      |
| unpickle_pure_python       | 133 us                                                      | 108 us: 1.23x faster                                                       |
| scimark_fft                | 184 ms                                                      | 151 ms: 1.22x faster                                                       |
| tomli_loads                | 1.37 sec                                                    | 1.14 sec: 1.20x faster                                                     |
| go                         | 91.6 ms                                                     | 78.8 ms: 1.16x faster                                                      |
| generators                 | 22.5 ms                                                     | 19.7 ms: 1.14x faster                                                      |
| pyflate                    | 295 ms                                                      | 258 ms: 1.14x faster                                                       |
| pprint_safe_repr           | 513 ms                                                      | 453 ms: 1.13x faster                                                       |
| deepcopy_reduce            | 2.09 us                                                     | 1.85 us: 1.13x faster                                                      |
| sqlite_synth               | 1.76 us                                                     | 1.56 us: 1.13x faster                                                      |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.27 ms: 1.12x faster                                                      |
| pprint_pformat             | 1.05 sec                                                    | 931 ms: 1.12x faster                                                       |
| regex_compile              | 87.5 ms                                                     | 78.9 ms: 1.11x faster                                                      |
| xml_etree_generate         | 55.8 ms                                                     | 51.2 ms: 1.09x faster                                                      |
| logging_silent             | 60.5 ns                                                     | 55.6 ns: 1.09x faster                                                      |
| fannkuch                   | 247 ms                                                      | 228 ms: 1.08x faster                                                       |
| dulwich_log                | 44.3 ms                                                     | 41.1 ms: 1.08x faster                                                      |
| raytrace                   | 192 ms                                                      | 179 ms: 1.07x faster                                                       |
| scimark_monte_carlo        | 43.7 ms                                                     | 41.1 ms: 1.06x faster                                                      |
| chaos                      | 43.3 ms                                                     | 40.8 ms: 1.06x faster                                                      |
| regex_dna                  | 126 ms                                                      | 120 ms: 1.06x faster                                                       |
| spectral_norm              | 66.9 ms                                                     | 63.5 ms: 1.05x faster                                                      |
| sympy_sum                  | 91.5 ms                                                     | 87.0 ms: 1.05x faster                                                      |
| xml_etree_process          | 37.7 ms                                                     | 35.9 ms: 1.05x faster                                                      |
| meteor_contest             | 74.6 ms                                                     | 71.1 ms: 1.05x faster                                                      |
| xml_etree_parse            | 93.0 ms                                                     | 88.9 ms: 1.05x faster                                                      |
| nqueens                    | 62.8 ms                                                     | 60.2 ms: 1.04x faster                                                      |
| crypto_pyaes               | 48.5 ms                                                     | 46.6 ms: 1.04x faster                                                      |
| pidigits                   | 152 ms                                                      | 147 ms: 1.03x faster                                                       |
| sympy_integrate            | 13.0 ms                                                     | 12.6 ms: 1.03x faster                                                      |
| sympy_str                  | 175 ms                                                      | 172 ms: 1.02x faster                                                       |
| richards                   | 28.4 ms                                                     | 27.8 ms: 1.02x faster                                                      |
| xml_etree_iterparse        | 65.2 ms                                                     | 63.9 ms: 1.02x faster                                                      |
| regex_v8                   | 14.2 ms                                                     | 14.0 ms: 1.02x faster                                                      |
| json                       | 3.05 ms                                                     | 3.01 ms: 1.01x faster                                                      |
| logging_format             | 6.72 us                                                     | 6.65 us: 1.01x faster                                                      |
| richards_super             | 32.1 ms                                                     | 31.8 ms: 1.01x faster                                                      |
| logging_simple             | 6.28 us                                                     | 6.24 us: 1.01x faster                                                      |
| scimark_sor                | 78.8 ms                                                     | 79.3 ms: 1.01x slower                                                      |
| docutils                   | 1.66 sec                                                    | 1.68 sec: 1.01x slower                                                     |
| 2to3                       | 218 ms                                                      | 221 ms: 1.01x slower                                                       |
| unpickle_list              | 2.75 us                                                     | 2.79 us: 1.01x slower                                                      |
| coroutines                 | 14.3 ms                                                     | 14.5 ms: 1.02x slower                                                      |
| pickle                     | 7.43 us                                                     | 7.60 us: 1.02x slower                                                      |
| hexiom                     | 4.10 ms                                                     | 4.19 ms: 1.02x slower                                                      |
| unpack_sequence            | 37.5 ns                                                     | 38.5 ns: 1.03x slower                                                      |
| scimark_lu                 | 58.9 ms                                                     | 60.9 ms: 1.03x slower                                                      |
| async_generators           | 239 ms                                                      | 248 ms: 1.04x slower                                                       |
| json_loads                 | 13.9 us                                                     | 14.4 us: 1.04x slower                                                      |
| sympy_expand               | 284 ms                                                      | 296 ms: 1.04x slower                                                       |
| unpickle                   | 8.18 us                                                     | 8.54 us: 1.04x slower                                                      |
| deltablue                  | 2.16 ms                                                     | 2.26 ms: 1.05x slower                                                      |
| pickle_pure_python         | 195 us                                                      | 205 us: 1.05x slower                                                       |
| asyncio_tcp                | 487 ms                                                      | 514 ms: 1.05x slower                                                       |
| django_template            | 22.9 ms                                                     | 24.3 ms: 1.06x slower                                                      |
| telco                      | 4.13 ms                                                     | 4.41 ms: 1.07x slower                                                      |
| pickle_dict                | 18.4 us                                                     | 19.9 us: 1.08x slower                                                      |
| typing_runtime_protocols   | 95.1 us                                                     | 103 us: 1.08x slower                                                       |
| json_dumps                 | 5.70 ms                                                     | 6.28 ms: 1.10x slower                                                      |
| python_startup_no_site     | 16.2 ms                                                     | 19.5 ms: 1.20x slower                                                      |
| pickle_list                | 2.83 us                                                     | 3.43 us: 1.21x slower                                                      |
| coverage                   | 40.8 ms                                                     | 51.3 ms: 1.26x slower                                                      |
| python_startup             | 19.5 ms                                                     | 26.0 ms: 1.34x slower                                                      |
| bench_mp_pool              | 69.2 ms                                                     | 95.6 ms: 1.38x slower                                                      |
| gc_traversal               | 1.52 ms                                                     | 2.18 ms: 1.43x slower                                                      |
| create_gc_cycles           | 752 us                                                      | 1.33 ms: 1.77x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.09x faster                                                               |

Benchmark hidden because not significant (3): pycparser, bench_thread_pool, regex_effbot
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (17) of results/bm-20250630-3.15.0a0-75f4059-JIT/bm-20250630-pythonperf1-amd64-python-75f40595e555e7d016cf-3.15.0a0-75f4059.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.110x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: unknown
# Results vs. 3.12.0

- fork: python
- ref: 719e5c3f7111bcda5eee
- machine: windows-amd64
- commit hash: 719e5c3
- commit date: 2025-08-19
- overall geometric mean: 1.128x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250819-pythonperf1-amd64-python-719e5c3f7111bcda5eee-3.15.0a0-719e5c3 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 221 ms: 1.02x slower                                                       |
| docutils       | 1.66 sec                                                    | 1.68 sec: 1.01x slower                                                     |
| Geometric mean | (ref)                                                       | 1.01x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250819-pythonperf1-amd64-python-719e5c3f7111bcda5eee-3.15.0a0-719e5c3 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 386 ms: 2.00x faster                                                       |
| async_tree_io              | 731 ms                                                      | 389 ms: 1.88x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 210 ms: 1.74x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 167 ms: 1.70x faster                                                       |
| async_tree_none            | 291 ms                                                      | 172 ms: 1.70x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 204 ms: 1.66x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 334 ms: 1.50x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 330 ms: 1.48x faster                                                       |
| Geometric mean             | (ref)                                                       | 1.70x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250819-pythonperf1-amd64-python-719e5c3f7111bcda5eee-3.15.0a0-719e5c3 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 71.9 ms                                                     | 53.4 ms: 1.35x faster                                                      |
| float          | 56.8 ms                                                     | 43.5 ms: 1.31x faster                                                      |
| pidigits       | 152 ms                                                      | 146 ms: 1.04x faster                                                       |
| Geometric mean | (ref)                                                       | 1.22x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250819-pythonperf1-amd64-python-719e5c3f7111bcda5eee-3.15.0a0-719e5c3 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 87.5 ms                                                     | 78.4 ms: 1.12x faster                                                      |
| regex_dna      | 126 ms                                                      | 120 ms: 1.05x faster                                                       |
| regex_effbot   | 1.62 ms                                                     | 1.55 ms: 1.04x faster                                                      |
| regex_v8       | 14.2 ms                                                     | 15.5 ms: 1.09x slower                                                      |
| Geometric mean | (ref)                                                       | 1.03x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250819-pythonperf1-amd64-python-719e5c3f7111bcda5eee-3.15.0a0-719e5c3 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| unpickle_pure_python | 133 us                                                      | 106 us: 1.26x faster                                                       |
| tomli_loads          | 1.37 sec                                                    | 1.11 sec: 1.24x faster                                                     |
| xml_etree_generate   | 55.8 ms                                                     | 50.7 ms: 1.10x faster                                                      |
| xml_etree_process    | 37.7 ms                                                     | 35.2 ms: 1.07x faster                                                      |
| xml_etree_parse      | 93.0 ms                                                     | 88.0 ms: 1.06x faster                                                      |
| json_dumps           | 5.70 ms                                                     | 5.40 ms: 1.05x faster                                                      |
| xml_etree_iterparse  | 65.2 ms                                                     | 63.2 ms: 1.03x faster                                                      |
| pickle_pure_python   | 195 us                                                      | 205 us: 1.05x slower                                                       |
| json_loads           | 13.9 us                                                     | 14.7 us: 1.06x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.07x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250819-pythonperf1-amd64-python-719e5c3f7111bcda5eee-3.15.0a0-719e5c3 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 19.4 ms: 1.19x slower                                                      |
| python_startup         | 19.5 ms                                                     | 25.8 ms: 1.32x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.26x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250819-pythonperf1-amd64-python-719e5c3f7111bcda5eee-3.15.0a0-719e5c3 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 5.41 ms: 1.31x faster                                                      |
| django_template | 22.9 ms                                                     | 24.3 ms: 1.06x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.11x faster                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250819-pythonperf1-amd64-python-719e5c3f7111bcda5eee-3.15.0a0-719e5c3 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pathlib                    | 80.5 ms                                                     | 29.1 ms: 2.76x faster                                                      |
| async_tree_io_tg           | 771 ms                                                      | 386 ms: 2.00x faster                                                       |
| async_tree_io              | 731 ms                                                      | 389 ms: 1.88x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 210 ms: 1.74x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 167 ms: 1.70x faster                                                       |
| async_tree_none            | 291 ms                                                      | 172 ms: 1.70x faster                                                       |
| mdp                        | 1.37 sec                                                    | 811 ms: 1.69x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 204 ms: 1.66x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 334 ms: 1.50x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 330 ms: 1.48x faster                                                       |
| deepcopy                   | 238 us                                                      | 169 us: 1.41x faster                                                       |
| nbody                      | 71.9 ms                                                     | 53.4 ms: 1.35x faster                                                      |
| comprehensions             | 14.1 us                                                     | 10.7 us: 1.33x faster                                                      |
| mako                       | 7.09 ms                                                     | 5.41 ms: 1.31x faster                                                      |
| float                      | 56.8 ms                                                     | 43.5 ms: 1.31x faster                                                      |
| deepcopy_memo              | 23.7 us                                                     | 18.2 us: 1.31x faster                                                      |
| unpickle_pure_python       | 133 us                                                      | 106 us: 1.26x faster                                                       |
| tomli_loads                | 1.37 sec                                                    | 1.11 sec: 1.24x faster                                                     |
| pprint_safe_repr           | 513 ms                                                      | 423 ms: 1.21x faster                                                       |
| pprint_pformat             | 1.05 sec                                                    | 865 ms: 1.21x faster                                                       |
| scimark_fft                | 184 ms                                                      | 153 ms: 1.21x faster                                                       |
| go                         | 91.6 ms                                                     | 76.0 ms: 1.20x faster                                                      |
| fannkuch                   | 247 ms                                                      | 214 ms: 1.16x faster                                                       |
| generators                 | 22.5 ms                                                     | 19.6 ms: 1.15x faster                                                      |
| deepcopy_reduce            | 2.09 us                                                     | 1.84 us: 1.14x faster                                                      |
| sqlite_synth               | 1.76 us                                                     | 1.55 us: 1.14x faster                                                      |
| logging_silent             | 60.5 ns                                                     | 53.8 ns: 1.12x faster                                                      |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.28 ms: 1.12x faster                                                      |
| regex_compile              | 87.5 ms                                                     | 78.4 ms: 1.12x faster                                                      |
| pyflate                    | 295 ms                                                      | 264 ms: 1.12x faster                                                       |
| scimark_monte_carlo        | 43.7 ms                                                     | 39.7 ms: 1.10x faster                                                      |
| xml_etree_generate         | 55.8 ms                                                     | 50.7 ms: 1.10x faster                                                      |
| dulwich_log                | 44.3 ms                                                     | 40.5 ms: 1.09x faster                                                      |
| xml_etree_process          | 37.7 ms                                                     | 35.2 ms: 1.07x faster                                                      |
| chaos                      | 43.3 ms                                                     | 40.6 ms: 1.07x faster                                                      |
| raytrace                   | 192 ms                                                      | 181 ms: 1.06x faster                                                       |
| crypto_pyaes               | 48.5 ms                                                     | 45.6 ms: 1.06x faster                                                      |
| richards                   | 28.4 ms                                                     | 26.8 ms: 1.06x faster                                                      |
| meteor_contest             | 74.6 ms                                                     | 70.5 ms: 1.06x faster                                                      |
| xml_etree_parse            | 93.0 ms                                                     | 88.0 ms: 1.06x faster                                                      |
| logging_simple             | 6.28 us                                                     | 5.95 us: 1.06x faster                                                      |
| json_dumps                 | 5.70 ms                                                     | 5.40 ms: 1.05x faster                                                      |
| richards_super             | 32.1 ms                                                     | 30.5 ms: 1.05x faster                                                      |
| logging_format             | 6.72 us                                                     | 6.38 us: 1.05x faster                                                      |
| regex_dna                  | 126 ms                                                      | 120 ms: 1.05x faster                                                       |
| sympy_sum                  | 91.5 ms                                                     | 87.7 ms: 1.04x faster                                                      |
| regex_effbot               | 1.62 ms                                                     | 1.55 ms: 1.04x faster                                                      |
| pidigits                   | 152 ms                                                      | 146 ms: 1.04x faster                                                       |
| spectral_norm              | 66.9 ms                                                     | 64.9 ms: 1.03x faster                                                      |
| xml_etree_iterparse        | 65.2 ms                                                     | 63.2 ms: 1.03x faster                                                      |
| scimark_sor                | 78.8 ms                                                     | 76.5 ms: 1.03x faster                                                      |
| nqueens                    | 62.8 ms                                                     | 61.0 ms: 1.03x faster                                                      |
| hexiom                     | 4.10 ms                                                     | 4.00 ms: 1.03x faster                                                      |
| sympy_integrate            | 13.0 ms                                                     | 12.7 ms: 1.02x faster                                                      |
| sympy_str                  | 175 ms                                                      | 172 ms: 1.02x faster                                                       |
| telco                      | 4.13 ms                                                     | 4.06 ms: 1.02x faster                                                      |
| coroutines                 | 14.3 ms                                                     | 14.2 ms: 1.01x faster                                                      |
| docutils                   | 1.66 sec                                                    | 1.68 sec: 1.01x slower                                                     |
| deltablue                  | 2.16 ms                                                     | 2.19 ms: 1.01x slower                                                      |
| 2to3                       | 218 ms                                                      | 221 ms: 1.02x slower                                                       |
| scimark_lu                 | 58.9 ms                                                     | 60.1 ms: 1.02x slower                                                      |
| async_generators           | 239 ms                                                      | 245 ms: 1.02x slower                                                       |
| json                       | 3.05 ms                                                     | 3.13 ms: 1.03x slower                                                      |
| sympy_expand               | 284 ms                                                      | 295 ms: 1.04x slower                                                       |
| pycparser                  | 699 ms                                                      | 727 ms: 1.04x slower                                                       |
| pickle_pure_python         | 195 us                                                      | 205 us: 1.05x slower                                                       |
| json_loads                 | 13.9 us                                                     | 14.7 us: 1.06x slower                                                      |
| django_template            | 22.9 ms                                                     | 24.3 ms: 1.06x slower                                                      |
| regex_v8                   | 14.2 ms                                                     | 15.5 ms: 1.09x slower                                                      |
| typing_runtime_protocols   | 95.1 us                                                     | 104 us: 1.09x slower                                                       |
| python_startup_no_site     | 16.2 ms                                                     | 19.4 ms: 1.19x slower                                                      |
| coverage                   | 40.8 ms                                                     | 51.9 ms: 1.27x slower                                                      |
| python_startup             | 19.5 ms                                                     | 25.8 ms: 1.32x slower                                                      |
| gc_traversal               | 1.52 ms                                                     | 2.12 ms: 1.39x slower                                                      |
| create_gc_cycles           | 752 us                                                      | 1.30 ms: 1.72x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.13x faster                                                               |
Ignored benchmarks (21) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (17) of results/bm-20250819-3.15.0a0-719e5c3-JIT/bm-20250819-pythonperf1-amd64-python-719e5c3f7111bcda5eee-3.15.0a0-719e5c3.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.128x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: unknown
# Results vs. 3.12.0

- fork: python
- ref: d6dd64ac654898b4ce71
- machine: windows-amd64
- commit hash: d6dd64a
- commit date: 2025-10-12
- overall geometric mean: 1.163x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20251012-pythonperf1-amd64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 212 ms: 1.03x faster                                                       |
| docutils       | 1.66 sec                                                    | 1.60 sec: 1.04x faster                                                     |
| Geometric mean | (ref)                                                       | 1.03x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20251012-pythonperf1-amd64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 376 ms: 2.05x faster                                                       |
| async_tree_io              | 731 ms                                                      | 385 ms: 1.90x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 210 ms: 1.75x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 164 ms: 1.74x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 198 ms: 1.71x faster                                                       |
| async_tree_none            | 291 ms                                                      | 172 ms: 1.70x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 340 ms: 1.48x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 334 ms: 1.47x faster                                                       |
| Geometric mean             | (ref)                                                       | 1.71x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20251012-pythonperf1-amd64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 71.9 ms                                                     | 54.5 ms: 1.32x faster                                                      |
| float          | 56.8 ms                                                     | 43.8 ms: 1.30x faster                                                      |
| pidigits       | 152 ms                                                      | 147 ms: 1.04x faster                                                       |
| Geometric mean | (ref)                                                       | 1.21x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20251012-pythonperf1-amd64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 87.5 ms                                                     | 75.9 ms: 1.15x faster                                                      |
| regex_dna      | 126 ms                                                      | 118 ms: 1.07x faster                                                       |
| regex_v8       | 14.2 ms                                                     | 13.6 ms: 1.05x faster                                                      |
| regex_effbot   | 1.62 ms                                                     | 1.56 ms: 1.04x faster                                                      |
| Geometric mean | (ref)                                                       | 1.08x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20251012-pythonperf1-amd64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| tomli_loads          | 1.37 sec                                                    | 1.09 sec: 1.25x faster                                                     |
| unpickle_pure_python | 133 us                                                      | 107 us: 1.25x faster                                                       |
| xml_etree_generate   | 55.8 ms                                                     | 49.2 ms: 1.14x faster                                                      |
| xml_etree_process    | 37.7 ms                                                     | 34.8 ms: 1.08x faster                                                      |
| xml_etree_parse      | 93.0 ms                                                     | 87.9 ms: 1.06x faster                                                      |
| xml_etree_iterparse  | 65.2 ms                                                     | 62.7 ms: 1.04x faster                                                      |
| json_dumps           | 5.70 ms                                                     | 5.52 ms: 1.03x faster                                                      |
| pickle_pure_python   | 195 us                                                      | 194 us: 1.01x faster                                                       |
| pickle               | 7.43 us                                                     | 7.67 us: 1.03x slower                                                      |
| pickle_dict          | 18.4 us                                                     | 19.1 us: 1.04x slower                                                      |
| unpickle             | 8.18 us                                                     | 8.48 us: 1.04x slower                                                      |
| pickle_list          | 2.83 us                                                     | 3.22 us: 1.14x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.04x faster                                                               |

Benchmark hidden because not significant (2): json_loads, unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20251012-pythonperf1-amd64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 18.9 ms: 1.16x slower                                                      |
| python_startup         | 19.5 ms                                                     | 25.1 ms: 1.29x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.22x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20251012-pythonperf1-amd64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 5.28 ms: 1.34x faster                                                      |
| django_template | 22.9 ms                                                     | 24.2 ms: 1.05x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.13x faster                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20251012-pythonperf1-amd64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pathlib                    | 80.5 ms                                                     | 28.8 ms: 2.79x faster                                                      |
| async_tree_io_tg           | 771 ms                                                      | 376 ms: 2.05x faster                                                       |
| async_tree_io              | 731 ms                                                      | 385 ms: 1.90x faster                                                       |
| mdp                        | 1.37 sec                                                    | 781 ms: 1.76x faster                                                       |
| deepcopy_memo              | 23.7 us                                                     | 13.5 us: 1.75x faster                                                      |
| async_tree_memoization_tg  | 367 ms                                                      | 210 ms: 1.75x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 164 ms: 1.74x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 198 ms: 1.71x faster                                                       |
| async_tree_none            | 291 ms                                                      | 172 ms: 1.70x faster                                                       |
| spectral_norm              | 66.9 ms                                                     | 43.0 ms: 1.56x faster                                                      |
| asyncio_tcp_ssl            | 2.10 sec                                                    | 1.40 sec: 1.50x faster                                                     |
| deepcopy                   | 238 us                                                      | 159 us: 1.50x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 340 ms: 1.48x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 334 ms: 1.47x faster                                                       |
| scimark_fft                | 184 ms                                                      | 134 ms: 1.38x faster                                                       |
| comprehensions             | 14.1 us                                                     | 10.5 us: 1.34x faster                                                      |
| mako                       | 7.09 ms                                                     | 5.28 ms: 1.34x faster                                                      |
| nbody                      | 71.9 ms                                                     | 54.5 ms: 1.32x faster                                                      |
| float                      | 56.8 ms                                                     | 43.8 ms: 1.30x faster                                                      |
| pprint_pformat             | 1.05 sec                                                    | 834 ms: 1.25x faster                                                       |
| tomli_loads                | 1.37 sec                                                    | 1.09 sec: 1.25x faster                                                     |
| unpickle_pure_python       | 133 us                                                      | 107 us: 1.25x faster                                                       |
| pprint_safe_repr           | 513 ms                                                      | 411 ms: 1.25x faster                                                       |
| go                         | 91.6 ms                                                     | 74.6 ms: 1.23x faster                                                      |
| deepcopy_reduce            | 2.09 us                                                     | 1.72 us: 1.21x faster                                                      |
| pyflate                    | 295 ms                                                      | 250 ms: 1.18x faster                                                       |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.19 ms: 1.17x faster                                                      |
| dulwich_log                | 44.3 ms                                                     | 38.0 ms: 1.17x faster                                                      |
| fannkuch                   | 247 ms                                                      | 213 ms: 1.16x faster                                                       |
| sqlite_synth               | 1.76 us                                                     | 1.53 us: 1.15x faster                                                      |
| regex_compile              | 87.5 ms                                                     | 75.9 ms: 1.15x faster                                                      |
| generators                 | 22.5 ms                                                     | 19.6 ms: 1.15x faster                                                      |
| xml_etree_generate         | 55.8 ms                                                     | 49.2 ms: 1.14x faster                                                      |
| raytrace                   | 192 ms                                                      | 172 ms: 1.12x faster                                                       |
| logging_silent             | 60.5 ns                                                     | 54.7 ns: 1.11x faster                                                      |
| crypto_pyaes               | 48.5 ms                                                     | 44.4 ms: 1.09x faster                                                      |
| logging_simple             | 6.28 us                                                     | 5.77 us: 1.09x faster                                                      |
| sympy_sum                  | 91.5 ms                                                     | 84.4 ms: 1.08x faster                                                      |
| logging_format             | 6.72 us                                                     | 6.20 us: 1.08x faster                                                      |
| xml_etree_process          | 37.7 ms                                                     | 34.8 ms: 1.08x faster                                                      |
| scimark_monte_carlo        | 43.7 ms                                                     | 40.6 ms: 1.08x faster                                                      |
| regex_dna                  | 126 ms                                                      | 118 ms: 1.07x faster                                                       |
| richards_super             | 32.1 ms                                                     | 30.0 ms: 1.07x faster                                                      |
| richards                   | 28.4 ms                                                     | 26.6 ms: 1.07x faster                                                      |
| chaos                      | 43.3 ms                                                     | 40.6 ms: 1.07x faster                                                      |
| telco                      | 4.13 ms                                                     | 3.90 ms: 1.06x faster                                                      |
| sympy_str                  | 175 ms                                                      | 165 ms: 1.06x faster                                                       |
| xml_etree_parse            | 93.0 ms                                                     | 87.9 ms: 1.06x faster                                                      |
| nqueens                    | 62.8 ms                                                     | 59.4 ms: 1.06x faster                                                      |
| json                       | 3.05 ms                                                     | 2.89 ms: 1.05x faster                                                      |
| unpack_sequence            | 37.5 ns                                                     | 35.6 ns: 1.05x faster                                                      |
| regex_v8                   | 14.2 ms                                                     | 13.6 ms: 1.05x faster                                                      |
| sympy_integrate            | 13.0 ms                                                     | 12.4 ms: 1.05x faster                                                      |
| meteor_contest             | 74.6 ms                                                     | 71.8 ms: 1.04x faster                                                      |
| xml_etree_iterparse        | 65.2 ms                                                     | 62.7 ms: 1.04x faster                                                      |
| pidigits                   | 152 ms                                                      | 147 ms: 1.04x faster                                                       |
| regex_effbot               | 1.62 ms                                                     | 1.56 ms: 1.04x faster                                                      |
| scimark_sor                | 78.8 ms                                                     | 76.0 ms: 1.04x faster                                                      |
| docutils                   | 1.66 sec                                                    | 1.60 sec: 1.04x faster                                                     |
| bench_thread_pool          | 857 us                                                      | 828 us: 1.03x faster                                                       |
| json_dumps                 | 5.70 ms                                                     | 5.52 ms: 1.03x faster                                                      |
| 2to3                       | 218 ms                                                      | 212 ms: 1.03x faster                                                       |
| hexiom                     | 4.10 ms                                                     | 4.00 ms: 1.02x faster                                                      |
| async_generators           | 239 ms                                                      | 236 ms: 1.02x faster                                                       |
| deltablue                  | 2.16 ms                                                     | 2.14 ms: 1.01x faster                                                      |
| pickle_pure_python         | 195 us                                                      | 194 us: 1.01x faster                                                       |
| coroutines                 | 14.3 ms                                                     | 14.6 ms: 1.02x slower                                                      |
| pickle                     | 7.43 us                                                     | 7.67 us: 1.03x slower                                                      |
| pickle_dict                | 18.4 us                                                     | 19.1 us: 1.04x slower                                                      |
| unpickle                   | 8.18 us                                                     | 8.48 us: 1.04x slower                                                      |
| django_template            | 22.9 ms                                                     | 24.2 ms: 1.05x slower                                                      |
| scimark_lu                 | 58.9 ms                                                     | 62.2 ms: 1.06x slower                                                      |
| typing_runtime_protocols   | 95.1 us                                                     | 105 us: 1.10x slower                                                       |
| pickle_list                | 2.83 us                                                     | 3.22 us: 1.14x slower                                                      |
| python_startup_no_site     | 16.2 ms                                                     | 18.9 ms: 1.16x slower                                                      |
| coverage                   | 40.8 ms                                                     | 50.3 ms: 1.23x slower                                                      |
| bench_mp_pool              | 69.2 ms                                                     | 88.5 ms: 1.28x slower                                                      |
| python_startup             | 19.5 ms                                                     | 25.1 ms: 1.29x slower                                                      |
| gc_traversal               | 1.52 ms                                                     | 2.09 ms: 1.37x slower                                                      |
| create_gc_cycles           | 752 us                                                      | 1.25 ms: 1.67x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.14x faster                                                               |

Benchmark hidden because not significant (5): json_loads, unpickle_list, asyncio_tcp, sympy_expand, pycparser
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (17) of results/bm-20251012-3.15.0a0-d6dd64a-JIT/bm-20251012-pythonperf1-amd64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.163x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.08x
- 95% likely to have a speedup of 1.07x
- 99% likely to have a speedup of 1.06x

# Memory
- memory change: unknown
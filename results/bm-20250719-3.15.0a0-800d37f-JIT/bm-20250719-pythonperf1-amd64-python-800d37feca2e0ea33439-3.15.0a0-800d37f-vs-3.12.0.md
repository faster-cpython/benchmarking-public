# Results vs. 3.12.0

- fork: python
- ref: 800d37feca2e0ea33439
- machine: windows-amd64
- commit hash: 800d37f
- commit date: 2025-07-19
- overall geometric mean: 1.128x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250719-pythonperf1-amd64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 221 ms: 1.01x slower                                                       |
| docutils       | 1.66 sec                                                    | 1.64 sec: 1.01x faster                                                     |
| Geometric mean | (ref)                                                       | 1.00x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250719-pythonperf1-amd64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 388 ms: 1.99x faster                                                       |
| async_tree_io              | 731 ms                                                      | 392 ms: 1.87x faster                                                       |
| async_tree_none            | 291 ms                                                      | 166 ms: 1.75x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 210 ms: 1.75x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 166 ms: 1.71x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 202 ms: 1.68x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 338 ms: 1.48x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 332 ms: 1.48x faster                                                       |
| Geometric mean             | (ref)                                                       | 1.71x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250719-pythonperf1-amd64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 71.9 ms                                                     | 54.5 ms: 1.32x faster                                                      |
| float          | 56.8 ms                                                     | 43.5 ms: 1.31x faster                                                      |
| pidigits       | 152 ms                                                      | 145 ms: 1.05x faster                                                       |
| Geometric mean | (ref)                                                       | 1.22x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250719-pythonperf1-amd64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 87.5 ms                                                     | 78.8 ms: 1.11x faster                                                      |
| regex_dna      | 126 ms                                                      | 120 ms: 1.05x faster                                                       |
| regex_effbot   | 1.62 ms                                                     | 1.59 ms: 1.02x faster                                                      |
| regex_v8       | 14.2 ms                                                     | 14.0 ms: 1.02x faster                                                      |
| Geometric mean | (ref)                                                       | 1.05x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250719-pythonperf1-amd64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| unpickle_pure_python | 133 us                                                      | 105 us: 1.27x faster                                                       |
| tomli_loads          | 1.37 sec                                                    | 1.10 sec: 1.25x faster                                                     |
| xml_etree_generate   | 55.8 ms                                                     | 50.2 ms: 1.11x faster                                                      |
| xml_etree_process    | 37.7 ms                                                     | 34.9 ms: 1.08x faster                                                      |
| xml_etree_parse      | 93.0 ms                                                     | 87.7 ms: 1.06x faster                                                      |
| xml_etree_iterparse  | 65.2 ms                                                     | 63.4 ms: 1.03x faster                                                      |
| pickle               | 7.43 us                                                     | 7.68 us: 1.03x slower                                                      |
| pickle_pure_python   | 195 us                                                      | 203 us: 1.04x slower                                                       |
| unpickle             | 8.18 us                                                     | 8.54 us: 1.04x slower                                                      |
| json_loads           | 13.9 us                                                     | 14.7 us: 1.06x slower                                                      |
| pickle_dict          | 18.4 us                                                     | 19.6 us: 1.07x slower                                                      |
| json_dumps           | 5.70 ms                                                     | 6.28 ms: 1.10x slower                                                      |
| pickle_list          | 2.83 us                                                     | 3.26 us: 1.15x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.02x faster                                                               |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250719-pythonperf1-amd64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 19.2 ms: 1.18x slower                                                      |
| python_startup         | 19.5 ms                                                     | 25.0 ms: 1.29x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.23x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250719-pythonperf1-amd64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 5.32 ms: 1.33x faster                                                      |
| django_template | 22.9 ms                                                     | 24.1 ms: 1.05x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.13x faster                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250719-pythonperf1-amd64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pathlib                    | 80.5 ms                                                     | 30.1 ms: 2.67x faster                                                      |
| async_tree_io_tg           | 771 ms                                                      | 388 ms: 1.99x faster                                                       |
| async_tree_io              | 731 ms                                                      | 392 ms: 1.87x faster                                                       |
| async_tree_none            | 291 ms                                                      | 166 ms: 1.75x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 210 ms: 1.75x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 166 ms: 1.71x faster                                                       |
| mdp                        | 1.37 sec                                                    | 802 ms: 1.71x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 202 ms: 1.68x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 338 ms: 1.48x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 332 ms: 1.48x faster                                                       |
| asyncio_tcp_ssl            | 2.10 sec                                                    | 1.42 sec: 1.47x faster                                                     |
| deepcopy                   | 238 us                                                      | 170 us: 1.40x faster                                                       |
| comprehensions             | 14.1 us                                                     | 10.3 us: 1.38x faster                                                      |
| mako                       | 7.09 ms                                                     | 5.32 ms: 1.33x faster                                                      |
| nbody                      | 71.9 ms                                                     | 54.5 ms: 1.32x faster                                                      |
| deepcopy_memo              | 23.7 us                                                     | 18.0 us: 1.31x faster                                                      |
| float                      | 56.8 ms                                                     | 43.5 ms: 1.31x faster                                                      |
| unpickle_pure_python       | 133 us                                                      | 105 us: 1.27x faster                                                       |
| tomli_loads                | 1.37 sec                                                    | 1.10 sec: 1.25x faster                                                     |
| scimark_fft                | 184 ms                                                      | 151 ms: 1.22x faster                                                       |
| go                         | 91.6 ms                                                     | 75.7 ms: 1.21x faster                                                      |
| pyflate                    | 295 ms                                                      | 251 ms: 1.18x faster                                                       |
| fannkuch                   | 247 ms                                                      | 211 ms: 1.17x faster                                                       |
| deepcopy_reduce            | 2.09 us                                                     | 1.82 us: 1.15x faster                                                      |
| pprint_pformat             | 1.05 sec                                                    | 911 ms: 1.15x faster                                                       |
| sqlite_synth               | 1.76 us                                                     | 1.54 us: 1.14x faster                                                      |
| pprint_safe_repr           | 513 ms                                                      | 450 ms: 1.14x faster                                                       |
| generators                 | 22.5 ms                                                     | 19.8 ms: 1.14x faster                                                      |
| unpack_sequence            | 37.5 ns                                                     | 33.3 ns: 1.13x faster                                                      |
| logging_silent             | 60.5 ns                                                     | 54.0 ns: 1.12x faster                                                      |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.28 ms: 1.12x faster                                                      |
| xml_etree_generate         | 55.8 ms                                                     | 50.2 ms: 1.11x faster                                                      |
| regex_compile              | 87.5 ms                                                     | 78.8 ms: 1.11x faster                                                      |
| dulwich_log                | 44.3 ms                                                     | 40.4 ms: 1.10x faster                                                      |
| scimark_monte_carlo        | 43.7 ms                                                     | 40.1 ms: 1.09x faster                                                      |
| xml_etree_process          | 37.7 ms                                                     | 34.9 ms: 1.08x faster                                                      |
| chaos                      | 43.3 ms                                                     | 40.3 ms: 1.07x faster                                                      |
| raytrace                   | 192 ms                                                      | 180 ms: 1.07x faster                                                       |
| xml_etree_parse            | 93.0 ms                                                     | 87.7 ms: 1.06x faster                                                      |
| nqueens                    | 62.8 ms                                                     | 59.3 ms: 1.06x faster                                                      |
| meteor_contest             | 74.6 ms                                                     | 70.5 ms: 1.06x faster                                                      |
| regex_dna                  | 126 ms                                                      | 120 ms: 1.05x faster                                                       |
| pidigits                   | 152 ms                                                      | 145 ms: 1.05x faster                                                       |
| crypto_pyaes               | 48.5 ms                                                     | 46.3 ms: 1.05x faster                                                      |
| sympy_sum                  | 91.5 ms                                                     | 87.6 ms: 1.05x faster                                                      |
| logging_simple             | 6.28 us                                                     | 6.03 us: 1.04x faster                                                      |
| sympy_str                  | 175 ms                                                      | 169 ms: 1.04x faster                                                       |
| spectral_norm              | 66.9 ms                                                     | 64.9 ms: 1.03x faster                                                      |
| hexiom                     | 4.10 ms                                                     | 3.98 ms: 1.03x faster                                                      |
| logging_format             | 6.72 us                                                     | 6.54 us: 1.03x faster                                                      |
| xml_etree_iterparse        | 65.2 ms                                                     | 63.4 ms: 1.03x faster                                                      |
| scimark_sor                | 78.8 ms                                                     | 76.7 ms: 1.03x faster                                                      |
| regex_effbot               | 1.62 ms                                                     | 1.59 ms: 1.02x faster                                                      |
| regex_v8                   | 14.2 ms                                                     | 14.0 ms: 1.02x faster                                                      |
| sympy_integrate            | 13.0 ms                                                     | 12.7 ms: 1.02x faster                                                      |
| docutils                   | 1.66 sec                                                    | 1.64 sec: 1.01x faster                                                     |
| richards                   | 28.4 ms                                                     | 28.1 ms: 1.01x faster                                                      |
| richards_super             | 32.1 ms                                                     | 31.8 ms: 1.01x faster                                                      |
| async_generators           | 239 ms                                                      | 243 ms: 1.01x slower                                                       |
| 2to3                       | 218 ms                                                      | 221 ms: 1.01x slower                                                       |
| json                       | 3.05 ms                                                     | 3.09 ms: 1.01x slower                                                      |
| deltablue                  | 2.16 ms                                                     | 2.19 ms: 1.02x slower                                                      |
| sympy_expand               | 284 ms                                                      | 290 ms: 1.02x slower                                                       |
| telco                      | 4.13 ms                                                     | 4.24 ms: 1.03x slower                                                      |
| pickle                     | 7.43 us                                                     | 7.68 us: 1.03x slower                                                      |
| pickle_pure_python         | 195 us                                                      | 203 us: 1.04x slower                                                       |
| asyncio_tcp                | 487 ms                                                      | 506 ms: 1.04x slower                                                       |
| unpickle                   | 8.18 us                                                     | 8.54 us: 1.04x slower                                                      |
| django_template            | 22.9 ms                                                     | 24.1 ms: 1.05x slower                                                      |
| json_loads                 | 13.9 us                                                     | 14.7 us: 1.06x slower                                                      |
| typing_runtime_protocols   | 95.1 us                                                     | 101 us: 1.06x slower                                                       |
| pickle_dict                | 18.4 us                                                     | 19.6 us: 1.07x slower                                                      |
| json_dumps                 | 5.70 ms                                                     | 6.28 ms: 1.10x slower                                                      |
| pickle_list                | 2.83 us                                                     | 3.26 us: 1.15x slower                                                      |
| python_startup_no_site     | 16.2 ms                                                     | 19.2 ms: 1.18x slower                                                      |
| coverage                   | 40.8 ms                                                     | 49.4 ms: 1.21x slower                                                      |
| python_startup             | 19.5 ms                                                     | 25.0 ms: 1.29x slower                                                      |
| bench_mp_pool              | 69.2 ms                                                     | 94.3 ms: 1.36x slower                                                      |
| gc_traversal               | 1.52 ms                                                     | 2.10 ms: 1.38x slower                                                      |
| create_gc_cycles           | 752 us                                                      | 1.31 ms: 1.75x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.11x faster                                                               |

Benchmark hidden because not significant (5): pycparser, unpickle_list, coroutines, scimark_lu, bench_thread_pool
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (17) of results/bm-20250719-3.15.0a0-800d37f-JIT/bm-20250719-pythonperf1-amd64-python-800d37feca2e0ea33439-3.15.0a0-800d37f.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.128x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: unknown
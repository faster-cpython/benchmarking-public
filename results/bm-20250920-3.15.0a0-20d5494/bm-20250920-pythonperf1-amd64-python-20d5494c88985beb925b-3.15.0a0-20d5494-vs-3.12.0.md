# Results vs. 3.12.0

- fork: python
- ref: 20d5494c88985beb925b
- machine: windows-amd64
- commit hash: 20d5494
- commit date: 2025-09-20
- overall geometric mean: 1.091x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250920-pythonperf1-amd64-python-20d5494c88985beb925b-3.15.0a0-20d5494 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| docutils       | 1.66 sec                                                    | 1.60 sec: 1.04x faster                                                     |
| Geometric mean | (ref)                                                       | 1.02x faster                                                               |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250920-pythonperf1-amd64-python-20d5494c88985beb925b-3.15.0a0-20d5494 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 432 ms: 1.79x faster                                                       |
| async_tree_io              | 731 ms                                                      | 444 ms: 1.65x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 238 ms: 1.54x faster                                                       |
| async_tree_none            | 291 ms                                                      | 199 ms: 1.47x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 195 ms: 1.47x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 233 ms: 1.46x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 355 ms: 1.41x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 350 ms: 1.40x faster                                                       |
| Geometric mean             | (ref)                                                       | 1.52x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250920-pythonperf1-amd64-python-20d5494c88985beb925b-3.15.0a0-20d5494 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 43.7 ms: 1.30x faster                                                      |
| nbody          | 71.9 ms                                                     | 63.7 ms: 1.13x faster                                                      |
| pidigits       | 152 ms                                                      | 148 ms: 1.03x faster                                                       |
| Geometric mean | (ref)                                                       | 1.15x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250920-pythonperf1-amd64-python-20d5494c88985beb925b-3.15.0a0-20d5494 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 87.5 ms                                                     | 79.7 ms: 1.10x faster                                                      |
| regex_effbot   | 1.62 ms                                                     | 1.48 ms: 1.10x faster                                                      |
| regex_dna      | 126 ms                                                      | 118 ms: 1.07x faster                                                       |
| Geometric mean | (ref)                                                       | 1.07x faster                                                               |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250920-pythonperf1-amd64-python-20d5494c88985beb925b-3.15.0a0-20d5494 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| xml_etree_parse      | 93.0 ms                                                     | 86.8 ms: 1.07x faster                                                      |
| json_dumps           | 5.70 ms                                                     | 5.42 ms: 1.05x faster                                                      |
| xml_etree_iterparse  | 65.2 ms                                                     | 62.1 ms: 1.05x faster                                                      |
| xml_etree_generate   | 55.8 ms                                                     | 55.2 ms: 1.01x faster                                                      |
| json_loads           | 13.9 us                                                     | 14.0 us: 1.01x slower                                                      |
| unpickle             | 8.18 us                                                     | 8.38 us: 1.02x slower                                                      |
| unpickle_pure_python | 133 us                                                      | 137 us: 1.03x slower                                                       |
| xml_etree_process    | 37.7 ms                                                     | 39.0 ms: 1.03x slower                                                      |
| pickle               | 7.43 us                                                     | 7.87 us: 1.06x slower                                                      |
| pickle_pure_python   | 195 us                                                      | 212 us: 1.09x slower                                                       |
| unpickle_list        | 2.75 us                                                     | 2.99 us: 1.09x slower                                                      |
| pickle_dict          | 18.4 us                                                     | 20.7 us: 1.13x slower                                                      |
| pickle_list          | 2.83 us                                                     | 3.40 us: 1.20x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.03x slower                                                               |

Benchmark hidden because not significant (1): tomli_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250920-pythonperf1-amd64-python-20d5494c88985beb925b-3.15.0a0-20d5494 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 18.7 ms: 1.15x slower                                                      |
| python_startup         | 19.5 ms                                                     | 25.2 ms: 1.30x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.22x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250920-pythonperf1-amd64-python-20d5494c88985beb925b-3.15.0a0-20d5494 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 6.70 ms: 1.06x faster                                                      |
| django_template | 22.9 ms                                                     | 24.7 ms: 1.07x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.01x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250920-pythonperf1-amd64-python-20d5494c88985beb925b-3.15.0a0-20d5494 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pathlib                    | 80.5 ms                                                     | 29.9 ms: 2.70x faster                                                      |
| async_tree_io_tg           | 771 ms                                                      | 432 ms: 1.79x faster                                                       |
| mdp                        | 1.37 sec                                                    | 792 ms: 1.73x faster                                                       |
| async_tree_io              | 731 ms                                                      | 444 ms: 1.65x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 238 ms: 1.54x faster                                                       |
| asyncio_tcp_ssl            | 2.10 sec                                                    | 1.38 sec: 1.51x faster                                                     |
| async_tree_none            | 291 ms                                                      | 199 ms: 1.47x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 195 ms: 1.47x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 233 ms: 1.46x faster                                                       |
| deepcopy                   | 238 us                                                      | 168 us: 1.42x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 355 ms: 1.41x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 350 ms: 1.40x faster                                                       |
| deepcopy_memo              | 23.7 us                                                     | 17.7 us: 1.34x faster                                                      |
| float                      | 56.8 ms                                                     | 43.7 ms: 1.30x faster                                                      |
| comprehensions             | 14.1 us                                                     | 11.2 us: 1.26x faster                                                      |
| go                         | 91.6 ms                                                     | 76.6 ms: 1.20x faster                                                      |
| deepcopy_reduce            | 2.09 us                                                     | 1.81 us: 1.16x faster                                                      |
| generators                 | 22.5 ms                                                     | 19.5 ms: 1.16x faster                                                      |
| dulwich_log                | 44.3 ms                                                     | 38.4 ms: 1.15x faster                                                      |
| sqlite_synth               | 1.76 us                                                     | 1.56 us: 1.13x faster                                                      |
| nbody                      | 71.9 ms                                                     | 63.7 ms: 1.13x faster                                                      |
| regex_compile              | 87.5 ms                                                     | 79.7 ms: 1.10x faster                                                      |
| scimark_monte_carlo        | 43.7 ms                                                     | 39.8 ms: 1.10x faster                                                      |
| regex_effbot               | 1.62 ms                                                     | 1.48 ms: 1.10x faster                                                      |
| logging_silent             | 60.5 ns                                                     | 55.2 ns: 1.10x faster                                                      |
| sympy_sum                  | 91.5 ms                                                     | 84.4 ms: 1.08x faster                                                      |
| xml_etree_parse            | 93.0 ms                                                     | 86.8 ms: 1.07x faster                                                      |
| regex_dna                  | 126 ms                                                      | 118 ms: 1.07x faster                                                       |
| sympy_integrate            | 13.0 ms                                                     | 12.2 ms: 1.06x faster                                                      |
| scimark_sor                | 78.8 ms                                                     | 74.2 ms: 1.06x faster                                                      |
| sympy_str                  | 175 ms                                                      | 166 ms: 1.06x faster                                                       |
| mako                       | 7.09 ms                                                     | 6.70 ms: 1.06x faster                                                      |
| pprint_safe_repr           | 513 ms                                                      | 487 ms: 1.05x faster                                                       |
| pprint_pformat             | 1.05 sec                                                    | 993 ms: 1.05x faster                                                       |
| logging_simple             | 6.28 us                                                     | 5.97 us: 1.05x faster                                                      |
| json_dumps                 | 5.70 ms                                                     | 5.42 ms: 1.05x faster                                                      |
| xml_etree_iterparse        | 65.2 ms                                                     | 62.1 ms: 1.05x faster                                                      |
| logging_format             | 6.72 us                                                     | 6.42 us: 1.05x faster                                                      |
| json                       | 3.05 ms                                                     | 2.92 ms: 1.05x faster                                                      |
| pyflate                    | 295 ms                                                      | 282 ms: 1.04x faster                                                       |
| chaos                      | 43.3 ms                                                     | 41.5 ms: 1.04x faster                                                      |
| richards                   | 28.4 ms                                                     | 27.2 ms: 1.04x faster                                                      |
| richards_super             | 32.1 ms                                                     | 30.8 ms: 1.04x faster                                                      |
| docutils                   | 1.66 sec                                                    | 1.60 sec: 1.04x faster                                                     |
| async_generators           | 239 ms                                                      | 231 ms: 1.04x faster                                                       |
| pidigits                   | 152 ms                                                      | 148 ms: 1.03x faster                                                       |
| raytrace                   | 192 ms                                                      | 188 ms: 1.03x faster                                                       |
| spectral_norm              | 66.9 ms                                                     | 65.3 ms: 1.02x faster                                                      |
| scimark_lu                 | 58.9 ms                                                     | 57.8 ms: 1.02x faster                                                      |
| meteor_contest             | 74.6 ms                                                     | 73.6 ms: 1.01x faster                                                      |
| crypto_pyaes               | 48.5 ms                                                     | 47.9 ms: 1.01x faster                                                      |
| xml_etree_generate         | 55.8 ms                                                     | 55.2 ms: 1.01x faster                                                      |
| sympy_expand               | 284 ms                                                      | 281 ms: 1.01x faster                                                       |
| nqueens                    | 62.8 ms                                                     | 62.3 ms: 1.01x faster                                                      |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.54 ms: 1.01x faster                                                      |
| json_loads                 | 13.9 us                                                     | 14.0 us: 1.01x slower                                                      |
| unpack_sequence            | 37.5 ns                                                     | 38.0 ns: 1.01x slower                                                      |
| scimark_fft                | 184 ms                                                      | 187 ms: 1.02x slower                                                       |
| pycparser                  | 699 ms                                                      | 711 ms: 1.02x slower                                                       |
| unpickle                   | 8.18 us                                                     | 8.38 us: 1.02x slower                                                      |
| unpickle_pure_python       | 133 us                                                      | 137 us: 1.03x slower                                                       |
| hexiom                     | 4.10 ms                                                     | 4.21 ms: 1.03x slower                                                      |
| asyncio_tcp                | 487 ms                                                      | 501 ms: 1.03x slower                                                       |
| xml_etree_process          | 37.7 ms                                                     | 39.0 ms: 1.03x slower                                                      |
| telco                      | 4.13 ms                                                     | 4.29 ms: 1.04x slower                                                      |
| deltablue                  | 2.16 ms                                                     | 2.25 ms: 1.04x slower                                                      |
| coroutines                 | 14.3 ms                                                     | 14.9 ms: 1.05x slower                                                      |
| pickle                     | 7.43 us                                                     | 7.87 us: 1.06x slower                                                      |
| fannkuch                   | 247 ms                                                      | 263 ms: 1.07x slower                                                       |
| django_template            | 22.9 ms                                                     | 24.7 ms: 1.07x slower                                                      |
| pickle_pure_python         | 195 us                                                      | 212 us: 1.09x slower                                                       |
| unpickle_list              | 2.75 us                                                     | 2.99 us: 1.09x slower                                                      |
| typing_runtime_protocols   | 95.1 us                                                     | 104 us: 1.09x slower                                                       |
| pickle_dict                | 18.4 us                                                     | 20.7 us: 1.13x slower                                                      |
| python_startup_no_site     | 16.2 ms                                                     | 18.7 ms: 1.15x slower                                                      |
| pickle_list                | 2.83 us                                                     | 3.40 us: 1.20x slower                                                      |
| coverage                   | 40.8 ms                                                     | 49.4 ms: 1.21x slower                                                      |
| python_startup             | 19.5 ms                                                     | 25.2 ms: 1.30x slower                                                      |
| bench_mp_pool              | 69.2 ms                                                     | 90.0 ms: 1.30x slower                                                      |
| gc_traversal               | 1.52 ms                                                     | 2.05 ms: 1.35x slower                                                      |
| create_gc_cycles           | 752 us                                                      | 1.25 ms: 1.66x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.07x faster                                                               |

Benchmark hidden because not significant (4): regex_v8, 2to3, bench_thread_pool, tomli_loads
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (17) of results/bm-20250920-3.15.0a0-20d5494/bm-20250920-pythonperf1-amd64-python-20d5494c88985beb925b-3.15.0a0-20d5494.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.091x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: unknown
# Results vs. 3.12.0

- fork: python
- ref: 800d37feca2e0ea33439
- machine: windows-amd64
- commit hash: 800d37f
- commit date: 2025-07-19
- overall geometric mean: 1.099x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250719-pythonperf1-amd64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 220 ms: 1.01x slower                                                       |
| docutils       | 1.66 sec                                                    | 1.60 sec: 1.04x faster                                                     |
| Geometric mean | (ref)                                                       | 1.01x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250719-pythonperf1-amd64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 385 ms: 2.01x faster                                                       |
| async_tree_io              | 731 ms                                                      | 392 ms: 1.86x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 206 ms: 1.78x faster                                                       |
| async_tree_none            | 291 ms                                                      | 168 ms: 1.74x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 168 ms: 1.70x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 202 ms: 1.68x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 333 ms: 1.51x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 329 ms: 1.49x faster                                                       |
| Geometric mean             | (ref)                                                       | 1.71x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250719-pythonperf1-amd64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 42.7 ms: 1.33x faster                                                      |
| nbody          | 71.9 ms                                                     | 65.5 ms: 1.10x faster                                                      |
| pidigits       | 152 ms                                                      | 145 ms: 1.05x faster                                                       |
| Geometric mean | (ref)                                                       | 1.15x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250719-pythonperf1-amd64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 87.5 ms                                                     | 78.8 ms: 1.11x faster                                                      |
| regex_effbot   | 1.62 ms                                                     | 1.47 ms: 1.10x faster                                                      |
| regex_dna      | 126 ms                                                      | 120 ms: 1.05x faster                                                       |
| regex_v8       | 14.2 ms                                                     | 13.9 ms: 1.03x faster                                                      |
| Geometric mean | (ref)                                                       | 1.07x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250719-pythonperf1-amd64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| xml_etree_parse      | 93.0 ms                                                     | 88.4 ms: 1.05x faster                                                      |
| xml_etree_iterparse  | 65.2 ms                                                     | 63.3 ms: 1.03x faster                                                      |
| xml_etree_generate   | 55.8 ms                                                     | 54.9 ms: 1.02x faster                                                      |
| unpickle_pure_python | 133 us                                                      | 132 us: 1.01x faster                                                       |
| tomli_loads          | 1.37 sec                                                    | 1.39 sec: 1.02x slower                                                     |
| xml_etree_process    | 37.7 ms                                                     | 38.4 ms: 1.02x slower                                                      |
| json_loads           | 13.9 us                                                     | 14.2 us: 1.02x slower                                                      |
| pickle               | 7.43 us                                                     | 7.85 us: 1.06x slower                                                      |
| unpickle             | 8.18 us                                                     | 8.65 us: 1.06x slower                                                      |
| unpickle_list        | 2.75 us                                                     | 2.95 us: 1.07x slower                                                      |
| pickle_pure_python   | 195 us                                                      | 212 us: 1.08x slower                                                       |
| json_dumps           | 5.70 ms                                                     | 6.17 ms: 1.08x slower                                                      |
| pickle_dict          | 18.4 us                                                     | 20.1 us: 1.09x slower                                                      |
| pickle_list          | 2.83 us                                                     | 3.42 us: 1.21x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.04x slower                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250719-pythonperf1-amd64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 19.7 ms: 1.21x slower                                                      |
| python_startup         | 19.5 ms                                                     | 25.7 ms: 1.32x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.27x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250719-pythonperf1-amd64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 6.44 ms: 1.10x faster                                                      |
| django_template | 22.9 ms                                                     | 24.5 ms: 1.07x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.01x faster                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250719-pythonperf1-amd64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pathlib                    | 80.5 ms                                                     | 30.4 ms: 2.64x faster                                                      |
| async_tree_io_tg           | 771 ms                                                      | 385 ms: 2.01x faster                                                       |
| async_tree_io              | 731 ms                                                      | 392 ms: 1.86x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 206 ms: 1.78x faster                                                       |
| async_tree_none            | 291 ms                                                      | 168 ms: 1.74x faster                                                       |
| mdp                        | 1.37 sec                                                    | 804 ms: 1.71x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 168 ms: 1.70x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 202 ms: 1.68x faster                                                       |
| asyncio_tcp_ssl            | 2.10 sec                                                    | 1.27 sec: 1.65x faster                                                     |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 333 ms: 1.51x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 329 ms: 1.49x faster                                                       |
| deepcopy                   | 238 us                                                      | 167 us: 1.42x faster                                                       |
| deepcopy_memo              | 23.7 us                                                     | 17.5 us: 1.36x faster                                                      |
| float                      | 56.8 ms                                                     | 42.7 ms: 1.33x faster                                                      |
| comprehensions             | 14.1 us                                                     | 10.7 us: 1.32x faster                                                      |
| asyncio_tcp                | 487 ms                                                      | 400 ms: 1.22x faster                                                       |
| go                         | 91.6 ms                                                     | 77.0 ms: 1.19x faster                                                      |
| deepcopy_reduce            | 2.09 us                                                     | 1.80 us: 1.16x faster                                                      |
| generators                 | 22.5 ms                                                     | 19.4 ms: 1.16x faster                                                      |
| regex_compile              | 87.5 ms                                                     | 78.8 ms: 1.11x faster                                                      |
| sqlite_synth               | 1.76 us                                                     | 1.59 us: 1.11x faster                                                      |
| mako                       | 7.09 ms                                                     | 6.44 ms: 1.10x faster                                                      |
| regex_effbot               | 1.62 ms                                                     | 1.47 ms: 1.10x faster                                                      |
| nbody                      | 71.9 ms                                                     | 65.5 ms: 1.10x faster                                                      |
| logging_silent             | 60.5 ns                                                     | 55.1 ns: 1.10x faster                                                      |
| dulwich_log                | 44.3 ms                                                     | 40.5 ms: 1.09x faster                                                      |
| raytrace                   | 192 ms                                                      | 181 ms: 1.07x faster                                                       |
| scimark_monte_carlo        | 43.7 ms                                                     | 41.1 ms: 1.07x faster                                                      |
| chaos                      | 43.3 ms                                                     | 40.9 ms: 1.06x faster                                                      |
| richards                   | 28.4 ms                                                     | 26.8 ms: 1.06x faster                                                      |
| regex_dna                  | 126 ms                                                      | 120 ms: 1.05x faster                                                       |
| sympy_integrate            | 13.0 ms                                                     | 12.3 ms: 1.05x faster                                                      |
| xml_etree_parse            | 93.0 ms                                                     | 88.4 ms: 1.05x faster                                                      |
| pidigits                   | 152 ms                                                      | 145 ms: 1.05x faster                                                       |
| pprint_safe_repr           | 513 ms                                                      | 490 ms: 1.05x faster                                                       |
| sympy_sum                  | 91.5 ms                                                     | 87.6 ms: 1.04x faster                                                      |
| pprint_pformat             | 1.05 sec                                                    | 1.00 sec: 1.04x faster                                                     |
| sympy_str                  | 175 ms                                                      | 168 ms: 1.04x faster                                                       |
| logging_format             | 6.72 us                                                     | 6.46 us: 1.04x faster                                                      |
| logging_simple             | 6.28 us                                                     | 6.04 us: 1.04x faster                                                      |
| meteor_contest             | 74.6 ms                                                     | 71.9 ms: 1.04x faster                                                      |
| docutils                   | 1.66 sec                                                    | 1.60 sec: 1.04x faster                                                     |
| richards_super             | 32.1 ms                                                     | 31.0 ms: 1.04x faster                                                      |
| pyflate                    | 295 ms                                                      | 285 ms: 1.03x faster                                                       |
| unpack_sequence            | 37.5 ns                                                     | 36.3 ns: 1.03x faster                                                      |
| async_generators           | 239 ms                                                      | 232 ms: 1.03x faster                                                       |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.48 ms: 1.03x faster                                                      |
| xml_etree_iterparse        | 65.2 ms                                                     | 63.3 ms: 1.03x faster                                                      |
| regex_v8                   | 14.2 ms                                                     | 13.9 ms: 1.03x faster                                                      |
| scimark_sor                | 78.8 ms                                                     | 77.0 ms: 1.02x faster                                                      |
| spectral_norm              | 66.9 ms                                                     | 65.6 ms: 1.02x faster                                                      |
| nqueens                    | 62.8 ms                                                     | 61.5 ms: 1.02x faster                                                      |
| json                       | 3.05 ms                                                     | 2.99 ms: 1.02x faster                                                      |
| xml_etree_generate         | 55.8 ms                                                     | 54.9 ms: 1.02x faster                                                      |
| hexiom                     | 4.10 ms                                                     | 4.03 ms: 1.02x faster                                                      |
| scimark_lu                 | 58.9 ms                                                     | 58.3 ms: 1.01x faster                                                      |
| unpickle_pure_python       | 133 us                                                      | 132 us: 1.01x faster                                                       |
| crypto_pyaes               | 48.5 ms                                                     | 48.7 ms: 1.00x slower                                                      |
| coroutines                 | 14.3 ms                                                     | 14.3 ms: 1.01x slower                                                      |
| deltablue                  | 2.16 ms                                                     | 2.17 ms: 1.01x slower                                                      |
| 2to3                       | 218 ms                                                      | 220 ms: 1.01x slower                                                       |
| tomli_loads                | 1.37 sec                                                    | 1.39 sec: 1.02x slower                                                     |
| xml_etree_process          | 37.7 ms                                                     | 38.4 ms: 1.02x slower                                                      |
| json_loads                 | 13.9 us                                                     | 14.2 us: 1.02x slower                                                      |
| scimark_fft                | 184 ms                                                      | 189 ms: 1.02x slower                                                       |
| pickle                     | 7.43 us                                                     | 7.85 us: 1.06x slower                                                      |
| unpickle                   | 8.18 us                                                     | 8.65 us: 1.06x slower                                                      |
| typing_runtime_protocols   | 95.1 us                                                     | 101 us: 1.07x slower                                                       |
| django_template            | 22.9 ms                                                     | 24.5 ms: 1.07x slower                                                      |
| unpickle_list              | 2.75 us                                                     | 2.95 us: 1.07x slower                                                      |
| telco                      | 4.13 ms                                                     | 4.47 ms: 1.08x slower                                                      |
| pickle_pure_python         | 195 us                                                      | 212 us: 1.08x slower                                                       |
| json_dumps                 | 5.70 ms                                                     | 6.17 ms: 1.08x slower                                                      |
| pickle_dict                | 18.4 us                                                     | 20.1 us: 1.09x slower                                                      |
| fannkuch                   | 247 ms                                                      | 270 ms: 1.09x slower                                                       |
| pickle_list                | 2.83 us                                                     | 3.42 us: 1.21x slower                                                      |
| python_startup_no_site     | 16.2 ms                                                     | 19.7 ms: 1.21x slower                                                      |
| coverage                   | 40.8 ms                                                     | 49.6 ms: 1.22x slower                                                      |
| python_startup             | 19.5 ms                                                     | 25.7 ms: 1.32x slower                                                      |
| bench_mp_pool              | 69.2 ms                                                     | 94.5 ms: 1.37x slower                                                      |
| gc_traversal               | 1.52 ms                                                     | 2.16 ms: 1.42x slower                                                      |
| create_gc_cycles           | 752 us                                                      | 1.33 ms: 1.77x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.09x faster                                                               |

Benchmark hidden because not significant (3): bench_thread_pool, pycparser, sympy_expand
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (17) of results/bm-20250719-3.15.0a0-800d37f/bm-20250719-pythonperf1-amd64-python-800d37feca2e0ea33439-3.15.0a0-800d37f.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.099x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: unknown
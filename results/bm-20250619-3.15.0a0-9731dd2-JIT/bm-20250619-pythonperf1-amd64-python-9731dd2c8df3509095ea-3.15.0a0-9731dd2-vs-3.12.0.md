# Results vs. 3.12.0

- fork: python
- ref: 9731dd2c8df3509095ea
- machine: windows-amd64
- commit hash: 9731dd2
- commit date: 2025-06-19
- overall geometric mean: 1.106x faster
- HPT reliability: 99.99%
- HPT 99th percentile: 1.02x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250619-pythonperf1-amd64-python-9731dd2c8df3509095ea-3.15.0a0-9731dd2 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 221 ms: 1.01x slower                                                       |
| docutils       | 1.66 sec                                                    | 1.69 sec: 1.02x slower                                                     |
| Geometric mean | (ref)                                                       | 1.01x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250619-pythonperf1-amd64-python-9731dd2c8df3509095ea-3.15.0a0-9731dd2 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 390 ms: 1.98x faster                                                       |
| async_tree_io              | 731 ms                                                      | 395 ms: 1.85x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 210 ms: 1.75x faster                                                       |
| async_tree_none            | 291 ms                                                      | 169 ms: 1.72x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 167 ms: 1.70x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 207 ms: 1.64x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 327 ms: 1.50x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 338 ms: 1.48x faster                                                       |
| Geometric mean             | (ref)                                                       | 1.70x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250619-pythonperf1-amd64-python-9731dd2c8df3509095ea-3.15.0a0-9731dd2 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 71.9 ms                                                     | 52.4 ms: 1.37x faster                                                      |
| float          | 56.8 ms                                                     | 43.8 ms: 1.30x faster                                                      |
| pidigits       | 152 ms                                                      | 150 ms: 1.01x faster                                                       |
| Geometric mean | (ref)                                                       | 1.22x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250619-pythonperf1-amd64-python-9731dd2c8df3509095ea-3.15.0a0-9731dd2 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 87.5 ms                                                     | 78.2 ms: 1.12x faster                                                      |
| regex_dna      | 126 ms                                                      | 118 ms: 1.07x faster                                                       |
| regex_effbot   | 1.62 ms                                                     | 1.60 ms: 1.01x faster                                                      |
| Geometric mean | (ref)                                                       | 1.05x faster                                                               |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250619-pythonperf1-amd64-python-9731dd2c8df3509095ea-3.15.0a0-9731dd2 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| unpickle_pure_python | 133 us                                                      | 112 us: 1.19x faster                                                       |
| tomli_loads          | 1.37 sec                                                    | 1.16 sec: 1.18x faster                                                     |
| xml_etree_generate   | 55.8 ms                                                     | 51.1 ms: 1.09x faster                                                      |
| xml_etree_parse      | 93.0 ms                                                     | 88.8 ms: 1.05x faster                                                      |
| xml_etree_process    | 37.7 ms                                                     | 36.2 ms: 1.04x faster                                                      |
| xml_etree_iterparse  | 65.2 ms                                                     | 63.8 ms: 1.02x faster                                                      |
| json_loads           | 13.9 us                                                     | 14.5 us: 1.04x slower                                                      |
| pickle_pure_python   | 195 us                                                      | 207 us: 1.06x slower                                                       |
| json_dumps           | 5.70 ms                                                     | 6.15 ms: 1.08x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.04x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250619-pythonperf1-amd64-python-9731dd2c8df3509095ea-3.15.0a0-9731dd2 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 19.4 ms: 1.20x slower                                                      |
| python_startup         | 19.5 ms                                                     | 26.2 ms: 1.35x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.27x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250619-pythonperf1-amd64-python-9731dd2c8df3509095ea-3.15.0a0-9731dd2 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 5.67 ms: 1.25x faster                                                      |
| django_template | 22.9 ms                                                     | 24.1 ms: 1.05x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.09x faster                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250619-pythonperf1-amd64-python-9731dd2c8df3509095ea-3.15.0a0-9731dd2 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pathlib                    | 80.5 ms                                                     | 33.1 ms: 2.43x faster                                                      |
| async_tree_io_tg           | 771 ms                                                      | 390 ms: 1.98x faster                                                       |
| async_tree_io              | 731 ms                                                      | 395 ms: 1.85x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 210 ms: 1.75x faster                                                       |
| async_tree_none            | 291 ms                                                      | 169 ms: 1.72x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 167 ms: 1.70x faster                                                       |
| mdp                        | 1.37 sec                                                    | 812 ms: 1.69x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 207 ms: 1.64x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 327 ms: 1.50x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 338 ms: 1.48x faster                                                       |
| deepcopy                   | 238 us                                                      | 169 us: 1.41x faster                                                       |
| nbody                      | 71.9 ms                                                     | 52.4 ms: 1.37x faster                                                      |
| deepcopy_memo              | 23.7 us                                                     | 18.0 us: 1.31x faster                                                      |
| float                      | 56.8 ms                                                     | 43.8 ms: 1.30x faster                                                      |
| comprehensions             | 14.1 us                                                     | 10.9 us: 1.29x faster                                                      |
| mako                       | 7.09 ms                                                     | 5.67 ms: 1.25x faster                                                      |
| scimark_fft                | 184 ms                                                      | 153 ms: 1.21x faster                                                       |
| go                         | 91.6 ms                                                     | 77.0 ms: 1.19x faster                                                      |
| unpickle_pure_python       | 133 us                                                      | 112 us: 1.19x faster                                                       |
| tomli_loads                | 1.37 sec                                                    | 1.16 sec: 1.18x faster                                                     |
| deepcopy_reduce            | 2.09 us                                                     | 1.80 us: 1.16x faster                                                      |
| sqlite_synth               | 1.76 us                                                     | 1.54 us: 1.14x faster                                                      |
| pyflate                    | 295 ms                                                      | 258 ms: 1.14x faster                                                       |
| generators                 | 22.5 ms                                                     | 19.8 ms: 1.14x faster                                                      |
| regex_compile              | 87.5 ms                                                     | 78.2 ms: 1.12x faster                                                      |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.29 ms: 1.11x faster                                                      |
| scimark_monte_carlo        | 43.7 ms                                                     | 39.8 ms: 1.10x faster                                                      |
| xml_etree_generate         | 55.8 ms                                                     | 51.1 ms: 1.09x faster                                                      |
| raytrace                   | 192 ms                                                      | 177 ms: 1.08x faster                                                       |
| regex_dna                  | 126 ms                                                      | 118 ms: 1.07x faster                                                       |
| dulwich_log                | 44.3 ms                                                     | 41.4 ms: 1.07x faster                                                      |
| chaos                      | 43.3 ms                                                     | 40.5 ms: 1.07x faster                                                      |
| xml_etree_parse            | 93.0 ms                                                     | 88.8 ms: 1.05x faster                                                      |
| nqueens                    | 62.8 ms                                                     | 59.9 ms: 1.05x faster                                                      |
| sympy_sum                  | 91.5 ms                                                     | 87.8 ms: 1.04x faster                                                      |
| richards_super             | 32.1 ms                                                     | 30.8 ms: 1.04x faster                                                      |
| xml_etree_process          | 37.7 ms                                                     | 36.2 ms: 1.04x faster                                                      |
| richards                   | 28.4 ms                                                     | 27.3 ms: 1.04x faster                                                      |
| scimark_sor                | 78.8 ms                                                     | 75.9 ms: 1.04x faster                                                      |
| crypto_pyaes               | 48.5 ms                                                     | 47.2 ms: 1.03x faster                                                      |
| xml_etree_iterparse        | 65.2 ms                                                     | 63.8 ms: 1.02x faster                                                      |
| sympy_integrate            | 13.0 ms                                                     | 12.7 ms: 1.02x faster                                                      |
| sympy_str                  | 175 ms                                                      | 172 ms: 1.02x faster                                                       |
| meteor_contest             | 74.6 ms                                                     | 73.5 ms: 1.01x faster                                                      |
| pidigits                   | 152 ms                                                      | 150 ms: 1.01x faster                                                       |
| fannkuch                   | 247 ms                                                      | 243 ms: 1.01x faster                                                       |
| regex_effbot               | 1.62 ms                                                     | 1.60 ms: 1.01x faster                                                      |
| spectral_norm              | 66.9 ms                                                     | 66.5 ms: 1.01x faster                                                      |
| pprint_pformat             | 1.05 sec                                                    | 1.06 sec: 1.01x slower                                                     |
| deltablue                  | 2.16 ms                                                     | 2.18 ms: 1.01x slower                                                      |
| coroutines                 | 14.3 ms                                                     | 14.4 ms: 1.01x slower                                                      |
| async_generators           | 239 ms                                                      | 242 ms: 1.01x slower                                                       |
| 2to3                       | 218 ms                                                      | 221 ms: 1.01x slower                                                       |
| docutils                   | 1.66 sec                                                    | 1.69 sec: 1.02x slower                                                     |
| logging_simple             | 6.28 us                                                     | 6.38 us: 1.02x slower                                                      |
| json                       | 3.05 ms                                                     | 3.10 ms: 1.02x slower                                                      |
| hexiom                     | 4.10 ms                                                     | 4.21 ms: 1.03x slower                                                      |
| scimark_lu                 | 58.9 ms                                                     | 60.6 ms: 1.03x slower                                                      |
| logging_format             | 6.72 us                                                     | 6.95 us: 1.03x slower                                                      |
| json_loads                 | 13.9 us                                                     | 14.5 us: 1.04x slower                                                      |
| sympy_expand               | 284 ms                                                      | 296 ms: 1.04x slower                                                       |
| django_template            | 22.9 ms                                                     | 24.1 ms: 1.05x slower                                                      |
| telco                      | 4.13 ms                                                     | 4.36 ms: 1.06x slower                                                      |
| pickle_pure_python         | 195 us                                                      | 207 us: 1.06x slower                                                       |
| json_dumps                 | 5.70 ms                                                     | 6.15 ms: 1.08x slower                                                      |
| typing_runtime_protocols   | 95.1 us                                                     | 105 us: 1.10x slower                                                       |
| python_startup_no_site     | 16.2 ms                                                     | 19.4 ms: 1.20x slower                                                      |
| coverage                   | 40.8 ms                                                     | 51.8 ms: 1.27x slower                                                      |
| python_startup             | 19.5 ms                                                     | 26.2 ms: 1.35x slower                                                      |
| gc_traversal               | 1.52 ms                                                     | 2.22 ms: 1.46x slower                                                      |
| create_gc_cycles           | 752 us                                                      | 1.32 ms: 1.76x slower                                                      |
| logging_silent             | 60.5 ns                                                     | 319 ns: 5.27x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.08x faster                                                               |

Benchmark hidden because not significant (3): regex_v8, pprint_safe_repr, pycparser
Ignored benchmarks (21) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (17) of results/bm-20250619-3.15.0a0-9731dd2-JIT/bm-20250619-pythonperf1-amd64-python-9731dd2c8df3509095ea-3.15.0a0-9731dd2.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.106x faster

# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: unknown
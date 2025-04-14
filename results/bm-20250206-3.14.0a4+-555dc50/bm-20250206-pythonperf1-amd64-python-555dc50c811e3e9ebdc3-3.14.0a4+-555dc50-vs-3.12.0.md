# Results vs. 3.12.0

- fork: python
- ref: 555dc50c811e3e9ebdc3
- machine: windows-amd64
- commit hash: 555dc50
- commit date: 2025-02-06
- overall geometric mean: 1.042x faster
- HPT reliability: 73.97%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250206-pythonperf1-amd64-python-555dc50c811e3e9ebdc3-3.14.0a4+-555dc50 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 227 ms: 1.04x slower                                                        |
| docutils       | 1.66 sec                                                    | 1.64 sec: 1.01x faster                                                      |
| Geometric mean | (ref)                                                       | 1.02x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250206-pythonperf1-amd64-python-555dc50c811e3e9ebdc3-3.14.0a4+-555dc50 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 406 ms: 1.90x faster                                                        |
| async_tree_io              | 731 ms                                                      | 423 ms: 1.73x faster                                                        |
| async_tree_memoization_tg  | 367 ms                                                      | 225 ms: 1.63x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 177 ms: 1.61x faster                                                        |
| async_tree_none            | 291 ms                                                      | 189 ms: 1.54x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 223 ms: 1.52x faster                                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 343 ms: 1.46x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 339 ms: 1.44x faster                                                        |
| Geometric mean             | (ref)                                                       | 1.60x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250206-pythonperf1-amd64-python-555dc50c811e3e9ebdc3-3.14.0a4+-555dc50 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 45.8 ms: 1.24x faster                                                       |
| pidigits       | 152 ms                                                      | 151 ms: 1.01x faster                                                        |
| Geometric mean | (ref)                                                       | 1.08x faster                                                                |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250206-pythonperf1-amd64-python-555dc50c811e3e9ebdc3-3.14.0a4+-555dc50 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_effbot   | 1.62 ms                                                     | 1.44 ms: 1.12x faster                                                       |
| regex_dna      | 126 ms                                                      | 115 ms: 1.10x faster                                                        |
| regex_compile  | 87.5 ms                                                     | 85.6 ms: 1.02x faster                                                       |
| Geometric mean | (ref)                                                       | 1.06x faster                                                                |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250206-pythonperf1-amd64-python-555dc50c811e3e9ebdc3-3.14.0a4+-555dc50 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_parse      | 93.0 ms                                                     | 90.5 ms: 1.03x faster                                                       |
| xml_etree_iterparse  | 65.2 ms                                                     | 63.4 ms: 1.03x faster                                                       |
| xml_etree_generate   | 55.8 ms                                                     | 56.4 ms: 1.01x slower                                                       |
| tomli_loads          | 1.37 sec                                                    | 1.39 sec: 1.02x slower                                                      |
| xml_etree_process    | 37.7 ms                                                     | 39.5 ms: 1.05x slower                                                       |
| pickle_pure_python   | 195 us                                                      | 218 us: 1.11x slower                                                        |
| unpickle_pure_python | 133 us                                                      | 148 us: 1.11x slower                                                        |
| json_loads           | 13.9 us                                                     | 15.5 us: 1.12x slower                                                       |
| json_dumps           | 5.70 ms                                                     | 6.72 ms: 1.18x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.06x slower                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250206-pythonperf1-amd64-python-555dc50c811e3e9ebdc3-3.14.0a4+-555dc50 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 19.7 ms: 1.21x slower                                                       |
| python_startup         | 19.5 ms                                                     | 26.1 ms: 1.34x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.27x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250206-pythonperf1-amd64-python-555dc50c811e3e9ebdc3-3.14.0a4+-555dc50 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 6.74 ms: 1.05x faster                                                       |
| django_template | 22.9 ms                                                     | 25.1 ms: 1.09x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.02x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250206-pythonperf1-amd64-python-555dc50c811e3e9ebdc3-3.14.0a4+-555dc50 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 406 ms: 1.90x faster                                                        |
| async_tree_io              | 731 ms                                                      | 423 ms: 1.73x faster                                                        |
| async_tree_memoization_tg  | 367 ms                                                      | 225 ms: 1.63x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 177 ms: 1.61x faster                                                        |
| async_tree_none            | 291 ms                                                      | 189 ms: 1.54x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 223 ms: 1.52x faster                                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 343 ms: 1.46x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 339 ms: 1.44x faster                                                        |
| pathlib                    | 80.5 ms                                                     | 60.9 ms: 1.32x faster                                                       |
| deepcopy                   | 238 us                                                      | 183 us: 1.30x faster                                                        |
| comprehensions             | 14.1 us                                                     | 11.1 us: 1.27x faster                                                       |
| float                      | 56.8 ms                                                     | 45.8 ms: 1.24x faster                                                       |
| deepcopy_memo              | 23.7 us                                                     | 19.2 us: 1.24x faster                                                       |
| spectral_norm              | 66.9 ms                                                     | 57.9 ms: 1.16x faster                                                       |
| deepcopy_reduce            | 2.09 us                                                     | 1.86 us: 1.13x faster                                                       |
| sqlite_synth               | 1.76 us                                                     | 1.57 us: 1.12x faster                                                       |
| regex_effbot               | 1.62 ms                                                     | 1.44 ms: 1.12x faster                                                       |
| generators                 | 22.5 ms                                                     | 20.2 ms: 1.11x faster                                                       |
| coroutines                 | 14.3 ms                                                     | 12.9 ms: 1.10x faster                                                       |
| regex_dna                  | 126 ms                                                      | 115 ms: 1.10x faster                                                        |
| async_generators           | 239 ms                                                      | 221 ms: 1.08x faster                                                        |
| go                         | 91.6 ms                                                     | 85.7 ms: 1.07x faster                                                       |
| mako                       | 7.09 ms                                                     | 6.74 ms: 1.05x faster                                                       |
| chaos                      | 43.3 ms                                                     | 41.3 ms: 1.05x faster                                                       |
| logging_silent             | 60.5 ns                                                     | 57.8 ns: 1.05x faster                                                       |
| dulwich_log                | 44.3 ms                                                     | 42.5 ms: 1.04x faster                                                       |
| crypto_pyaes               | 48.5 ms                                                     | 47.0 ms: 1.03x faster                                                       |
| xml_etree_parse            | 93.0 ms                                                     | 90.5 ms: 1.03x faster                                                       |
| xml_etree_iterparse        | 65.2 ms                                                     | 63.4 ms: 1.03x faster                                                       |
| regex_compile              | 87.5 ms                                                     | 85.6 ms: 1.02x faster                                                       |
| sympy_sum                  | 91.5 ms                                                     | 90.2 ms: 1.02x faster                                                       |
| nqueens                    | 62.8 ms                                                     | 62.0 ms: 1.01x faster                                                       |
| docutils                   | 1.66 sec                                                    | 1.64 sec: 1.01x faster                                                      |
| pidigits                   | 152 ms                                                      | 151 ms: 1.01x faster                                                        |
| deltablue                  | 2.16 ms                                                     | 2.15 ms: 1.01x faster                                                       |
| pyflate                    | 295 ms                                                      | 296 ms: 1.01x slower                                                        |
| logging_simple             | 6.28 us                                                     | 6.33 us: 1.01x slower                                                       |
| xml_etree_generate         | 55.8 ms                                                     | 56.4 ms: 1.01x slower                                                       |
| sqlglot_optimize           | 34.5 ms                                                     | 34.9 ms: 1.01x slower                                                       |
| sqlglot_normalize          | 187 ms                                                      | 189 ms: 1.01x slower                                                        |
| richards                   | 28.4 ms                                                     | 28.7 ms: 1.01x slower                                                       |
| meteor_contest             | 74.6 ms                                                     | 75.6 ms: 1.01x slower                                                       |
| sympy_integrate            | 13.0 ms                                                     | 13.2 ms: 1.02x slower                                                       |
| tomli_loads                | 1.37 sec                                                    | 1.39 sec: 1.02x slower                                                      |
| richards_super             | 32.1 ms                                                     | 32.8 ms: 1.02x slower                                                       |
| scimark_monte_carlo        | 43.7 ms                                                     | 44.7 ms: 1.02x slower                                                       |
| pprint_safe_repr           | 513 ms                                                      | 527 ms: 1.03x slower                                                        |
| pycparser                  | 699 ms                                                      | 717 ms: 1.03x slower                                                        |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.63 ms: 1.03x slower                                                       |
| scimark_lu                 | 58.9 ms                                                     | 60.8 ms: 1.03x slower                                                       |
| hexiom                     | 4.10 ms                                                     | 4.24 ms: 1.03x slower                                                       |
| sqlglot_transpile          | 1.02 ms                                                     | 1.06 ms: 1.03x slower                                                       |
| 2to3                       | 218 ms                                                      | 227 ms: 1.04x slower                                                        |
| xml_etree_process          | 37.7 ms                                                     | 39.5 ms: 1.05x slower                                                       |
| json                       | 3.05 ms                                                     | 3.21 ms: 1.05x slower                                                       |
| sqlglot_parse              | 804 us                                                      | 852 us: 1.06x slower                                                        |
| sympy_expand               | 284 ms                                                      | 301 ms: 1.06x slower                                                        |
| fannkuch                   | 247 ms                                                      | 262 ms: 1.06x slower                                                        |
| scimark_sor                | 78.8 ms                                                     | 85.4 ms: 1.08x slower                                                       |
| django_template            | 22.9 ms                                                     | 25.1 ms: 1.09x slower                                                       |
| typing_runtime_protocols   | 95.1 us                                                     | 105 us: 1.11x slower                                                        |
| pickle_pure_python         | 195 us                                                      | 218 us: 1.11x slower                                                        |
| unpickle_pure_python       | 133 us                                                      | 148 us: 1.11x slower                                                        |
| json_loads                 | 13.9 us                                                     | 15.5 us: 1.12x slower                                                       |
| telco                      | 4.13 ms                                                     | 4.70 ms: 1.14x slower                                                       |
| mdp                        | 1.37 sec                                                    | 1.58 sec: 1.15x slower                                                      |
| coverage                   | 40.8 ms                                                     | 47.7 ms: 1.17x slower                                                       |
| json_dumps                 | 5.70 ms                                                     | 6.72 ms: 1.18x slower                                                       |
| python_startup_no_site     | 16.2 ms                                                     | 19.7 ms: 1.21x slower                                                       |
| bench_mp_pool              | 69.2 ms                                                     | 89.4 ms: 1.29x slower                                                       |
| gc_traversal               | 1.52 ms                                                     | 2.00 ms: 1.31x slower                                                       |
| python_startup             | 19.5 ms                                                     | 26.1 ms: 1.34x slower                                                       |
| create_gc_cycles           | 752 us                                                      | 1.21 ms: 1.61x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.04x faster                                                                |

Benchmark hidden because not significant (8): bench_thread_pool, nbody, sympy_str, pprint_pformat, scimark_fft, regex_v8, logging_format, raytrace
Ignored benchmarks (15) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (13) of results/bm-20250206-3.14.0a4+-555dc50/bm-20250206-pythonperf1-amd64-python-555dc50c811e3e9ebdc3-3.14.0a4+-555dc50.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.042x faster

# HPT report

- Reliability score: 73.97% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown
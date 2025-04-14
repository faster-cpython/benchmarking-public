# Results vs. 3.12.0

- fork: python
- ref: 3f2cfd0462e13368092a
- machine: windows-amd64
- commit hash: 3f2cfd0
- commit date: 2025-01-25
- overall geometric mean: 1.014x slower
- HPT reliability: 99.06%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250125-pythonperf1-amd64-python-3f2cfd0462e13368092a-3.14.0a4+-3f2cfd0 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 232 ms: 1.06x slower                                                        |
| docutils       | 1.66 sec                                                    | 1.69 sec: 1.01x slower                                                      |
| Geometric mean | (ref)                                                       | 1.04x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250125-pythonperf1-amd64-python-3f2cfd0462e13368092a-3.14.0a4+-3f2cfd0 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 435 ms: 1.77x faster                                                        |
| async_tree_io              | 731 ms                                                      | 434 ms: 1.68x faster                                                        |
| async_tree_memoization_tg  | 367 ms                                                      | 224 ms: 1.64x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 185 ms: 1.54x faster                                                        |
| async_tree_none            | 291 ms                                                      | 199 ms: 1.46x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 233 ms: 1.46x faster                                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 353 ms: 1.42x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 356 ms: 1.37x faster                                                        |
| Geometric mean             | (ref)                                                       | 1.54x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250125-pythonperf1-amd64-python-3f2cfd0462e13368092a-3.14.0a4+-3f2cfd0 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 51.8 ms: 1.10x faster                                                       |
| pidigits       | 152 ms                                                      | 147 ms: 1.03x faster                                                        |
| nbody          | 71.9 ms                                                     | 77.7 ms: 1.08x slower                                                       |
| Geometric mean | (ref)                                                       | 1.02x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250125-pythonperf1-amd64-python-3f2cfd0462e13368092a-3.14.0a4+-3f2cfd0 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_effbot   | 1.62 ms                                                     | 1.47 ms: 1.10x faster                                                       |
| regex_dna      | 126 ms                                                      | 123 ms: 1.03x faster                                                        |
| regex_compile  | 87.5 ms                                                     | 89.2 ms: 1.02x slower                                                       |
| regex_v8       | 14.2 ms                                                     | 15.8 ms: 1.11x slower                                                       |
| Geometric mean | (ref)                                                       | 1.00x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250125-pythonperf1-amd64-python-3f2cfd0462e13368092a-3.14.0a4+-3f2cfd0 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_parse      | 93.0 ms                                                     | 89.0 ms: 1.05x faster                                                       |
| pickle_dict          | 18.4 us                                                     | 18.2 us: 1.01x faster                                                       |
| unpickle_list        | 2.75 us                                                     | 2.81 us: 1.02x slower                                                       |
| unpickle             | 8.18 us                                                     | 8.58 us: 1.05x slower                                                       |
| xml_etree_generate   | 55.8 ms                                                     | 59.1 ms: 1.06x slower                                                       |
| tomli_loads          | 1.37 sec                                                    | 1.46 sec: 1.07x slower                                                      |
| json_loads           | 13.9 us                                                     | 14.9 us: 1.07x slower                                                       |
| pickle               | 7.43 us                                                     | 8.00 us: 1.08x slower                                                       |
| pickle_list          | 2.83 us                                                     | 3.07 us: 1.09x slower                                                       |
| xml_etree_process    | 37.7 ms                                                     | 41.9 ms: 1.11x slower                                                       |
| json_dumps           | 5.70 ms                                                     | 6.85 ms: 1.20x slower                                                       |
| pickle_pure_python   | 195 us                                                      | 242 us: 1.24x slower                                                        |
| unpickle_pure_python | 133 us                                                      | 165 us: 1.24x slower                                                        |
| Geometric mean       | (ref)                                                       | 1.08x slower                                                                |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250125-pythonperf1-amd64-python-3f2cfd0462e13368092a-3.14.0a4+-3f2cfd0 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 17.9 ms: 1.10x slower                                                       |
| python_startup         | 19.5 ms                                                     | 24.3 ms: 1.25x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.18x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250125-pythonperf1-amd64-python-3f2cfd0462e13368092a-3.14.0a4+-3f2cfd0 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| django_template | 22.9 ms                                                     | 26.4 ms: 1.15x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.08x slower                                                                |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250125-pythonperf1-amd64-python-3f2cfd0462e13368092a-3.14.0a4+-3f2cfd0 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 435 ms: 1.77x faster                                                        |
| async_tree_io              | 731 ms                                                      | 434 ms: 1.68x faster                                                        |
| async_tree_memoization_tg  | 367 ms                                                      | 224 ms: 1.64x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 185 ms: 1.54x faster                                                        |
| asyncio_tcp_ssl            | 2.10 sec                                                    | 1.42 sec: 1.48x faster                                                      |
| async_tree_none            | 291 ms                                                      | 199 ms: 1.46x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 233 ms: 1.46x faster                                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 353 ms: 1.42x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 356 ms: 1.37x faster                                                        |
| deepcopy                   | 238 us                                                      | 189 us: 1.26x faster                                                        |
| comprehensions             | 14.1 us                                                     | 12.7 us: 1.12x faster                                                       |
| regex_effbot               | 1.62 ms                                                     | 1.47 ms: 1.10x faster                                                       |
| float                      | 56.8 ms                                                     | 51.8 ms: 1.10x faster                                                       |
| deepcopy_memo              | 23.7 us                                                     | 21.6 us: 1.10x faster                                                       |
| sqlite_synth               | 1.76 us                                                     | 1.62 us: 1.09x faster                                                       |
| deepcopy_reduce            | 2.09 us                                                     | 1.95 us: 1.07x faster                                                       |
| async_generators           | 239 ms                                                      | 227 ms: 1.05x faster                                                        |
| xml_etree_parse            | 93.0 ms                                                     | 89.0 ms: 1.05x faster                                                       |
| dulwich_log                | 44.3 ms                                                     | 42.6 ms: 1.04x faster                                                       |
| pathlib                    | 80.5 ms                                                     | 77.7 ms: 1.03x faster                                                       |
| pidigits                   | 152 ms                                                      | 147 ms: 1.03x faster                                                        |
| spectral_norm              | 66.9 ms                                                     | 65.0 ms: 1.03x faster                                                       |
| bench_thread_pool          | 857 us                                                      | 834 us: 1.03x faster                                                        |
| regex_dna                  | 126 ms                                                      | 123 ms: 1.03x faster                                                        |
| generators                 | 22.5 ms                                                     | 22.0 ms: 1.02x faster                                                       |
| pickle_dict                | 18.4 us                                                     | 18.2 us: 1.01x faster                                                       |
| chaos                      | 43.3 ms                                                     | 43.1 ms: 1.01x faster                                                       |
| sympy_sum                  | 91.5 ms                                                     | 91.0 ms: 1.01x faster                                                       |
| crypto_pyaes               | 48.5 ms                                                     | 49.2 ms: 1.01x slower                                                       |
| docutils                   | 1.66 sec                                                    | 1.69 sec: 1.01x slower                                                      |
| regex_compile              | 87.5 ms                                                     | 89.2 ms: 1.02x slower                                                       |
| go                         | 91.6 ms                                                     | 93.4 ms: 1.02x slower                                                       |
| unpickle_list              | 2.75 us                                                     | 2.81 us: 1.02x slower                                                       |
| logging_format             | 6.72 us                                                     | 6.87 us: 1.02x slower                                                       |
| sympy_str                  | 175 ms                                                      | 180 ms: 1.03x slower                                                        |
| logging_simple             | 6.28 us                                                     | 6.45 us: 1.03x slower                                                       |
| coroutines                 | 14.3 ms                                                     | 14.8 ms: 1.04x slower                                                       |
| meteor_contest             | 74.6 ms                                                     | 77.6 ms: 1.04x slower                                                       |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.68 ms: 1.05x slower                                                       |
| unpickle                   | 8.18 us                                                     | 8.58 us: 1.05x slower                                                       |
| xml_etree_generate         | 55.8 ms                                                     | 59.1 ms: 1.06x slower                                                       |
| 2to3                       | 218 ms                                                      | 232 ms: 1.06x slower                                                        |
| nqueens                    | 62.8 ms                                                     | 66.8 ms: 1.06x slower                                                       |
| sympy_integrate            | 13.0 ms                                                     | 13.8 ms: 1.07x slower                                                       |
| sqlglot_optimize           | 34.5 ms                                                     | 36.8 ms: 1.07x slower                                                       |
| tomli_loads                | 1.37 sec                                                    | 1.46 sec: 1.07x slower                                                      |
| json_loads                 | 13.9 us                                                     | 14.9 us: 1.07x slower                                                       |
| pickle                     | 7.43 us                                                     | 8.00 us: 1.08x slower                                                       |
| raytrace                   | 192 ms                                                      | 207 ms: 1.08x slower                                                        |
| sqlglot_normalize          | 187 ms                                                      | 201 ms: 1.08x slower                                                        |
| pyflate                    | 295 ms                                                      | 318 ms: 1.08x slower                                                        |
| nbody                      | 71.9 ms                                                     | 77.7 ms: 1.08x slower                                                       |
| pprint_pformat             | 1.05 sec                                                    | 1.13 sec: 1.08x slower                                                      |
| sympy_expand               | 284 ms                                                      | 308 ms: 1.08x slower                                                        |
| pickle_list                | 2.83 us                                                     | 3.07 us: 1.09x slower                                                       |
| pprint_safe_repr           | 513 ms                                                      | 563 ms: 1.10x slower                                                        |
| scimark_fft                | 184 ms                                                      | 203 ms: 1.10x slower                                                        |
| python_startup_no_site     | 16.2 ms                                                     | 17.9 ms: 1.10x slower                                                       |
| xml_etree_process          | 37.7 ms                                                     | 41.9 ms: 1.11x slower                                                       |
| regex_v8                   | 14.2 ms                                                     | 15.8 ms: 1.11x slower                                                       |
| sqlglot_transpile          | 1.02 ms                                                     | 1.14 ms: 1.11x slower                                                       |
| deltablue                  | 2.16 ms                                                     | 2.41 ms: 1.11x slower                                                       |
| pycparser                  | 699 ms                                                      | 785 ms: 1.12x slower                                                        |
| unpack_sequence            | 37.5 ns                                                     | 42.3 ns: 1.13x slower                                                       |
| asyncio_tcp                | 487 ms                                                      | 554 ms: 1.14x slower                                                        |
| scimark_monte_carlo        | 43.7 ms                                                     | 49.7 ms: 1.14x slower                                                       |
| sqlglot_parse              | 804 us                                                      | 921 us: 1.15x slower                                                        |
| django_template            | 22.9 ms                                                     | 26.4 ms: 1.15x slower                                                       |
| mdp                        | 1.37 sec                                                    | 1.58 sec: 1.15x slower                                                      |
| richards                   | 28.4 ms                                                     | 32.7 ms: 1.15x slower                                                       |
| richards_super             | 32.1 ms                                                     | 37.2 ms: 1.16x slower                                                       |
| fannkuch                   | 247 ms                                                      | 286 ms: 1.16x slower                                                        |
| hexiom                     | 4.10 ms                                                     | 4.76 ms: 1.16x slower                                                       |
| typing_runtime_protocols   | 95.1 us                                                     | 111 us: 1.16x slower                                                        |
| logging_silent             | 60.5 ns                                                     | 71.2 ns: 1.18x slower                                                       |
| telco                      | 4.13 ms                                                     | 4.90 ms: 1.19x slower                                                       |
| coverage                   | 40.8 ms                                                     | 48.5 ms: 1.19x slower                                                       |
| scimark_sor                | 78.8 ms                                                     | 94.0 ms: 1.19x slower                                                       |
| scimark_lu                 | 58.9 ms                                                     | 70.3 ms: 1.19x slower                                                       |
| json_dumps                 | 5.70 ms                                                     | 6.85 ms: 1.20x slower                                                       |
| pickle_pure_python         | 195 us                                                      | 242 us: 1.24x slower                                                        |
| unpickle_pure_python       | 133 us                                                      | 165 us: 1.24x slower                                                        |
| python_startup             | 19.5 ms                                                     | 24.3 ms: 1.25x slower                                                       |
| bench_mp_pool              | 69.2 ms                                                     | 87.7 ms: 1.27x slower                                                       |
| gc_traversal               | 1.52 ms                                                     | 1.99 ms: 1.30x slower                                                       |
| create_gc_cycles           | 752 us                                                      | 1.22 ms: 1.62x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.02x slower                                                                |

Benchmark hidden because not significant (3): json, xml_etree_iterparse, mako
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (13) of results/bm-20250125-3.14.0a4+-3f2cfd0/bm-20250125-pythonperf1-amd64-python-3f2cfd0462e13368092a-3.14.0a4+-3f2cfd0.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.014x slower

# HPT report

- Reliability score: 99.06% likely to be slow
- 90% likely to have a slowdown of 1.02x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown
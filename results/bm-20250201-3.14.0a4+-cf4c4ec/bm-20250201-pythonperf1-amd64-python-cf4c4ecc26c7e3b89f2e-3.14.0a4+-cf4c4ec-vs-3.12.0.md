# Results vs. 3.12.0

- fork: python
- ref: cf4c4ecc26c7e3b89f2e
- machine: windows-amd64
- commit hash: cf4c4ec
- commit date: 2025-02-01
- overall geometric mean: 1.067x faster
- HPT reliability: 99.99%
- HPT 99th percentile: 1.01x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250201-pythonperf1-amd64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 222 ms: 1.02x slower                                                        |
| docutils       | 1.66 sec                                                    | 1.64 sec: 1.01x faster                                                      |
| Geometric mean | (ref)                                                       | 1.00x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250201-pythonperf1-amd64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 400 ms: 1.93x faster                                                        |
| async_tree_io              | 731 ms                                                      | 400 ms: 1.83x faster                                                        |
| async_tree_memoization_tg  | 367 ms                                                      | 211 ms: 1.73x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 172 ms: 1.65x faster                                                        |
| async_tree_none            | 291 ms                                                      | 181 ms: 1.61x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 217 ms: 1.56x faster                                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 340 ms: 1.48x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 339 ms: 1.45x faster                                                        |
| Geometric mean             | (ref)                                                       | 1.65x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250201-pythonperf1-amd64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 45.0 ms: 1.26x faster                                                       |
| nbody          | 71.9 ms                                                     | 64.2 ms: 1.12x faster                                                       |
| pidigits       | 152 ms                                                      | 151 ms: 1.01x faster                                                        |
| Geometric mean | (ref)                                                       | 1.13x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250201-pythonperf1-amd64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_effbot   | 1.62 ms                                                     | 1.48 ms: 1.09x faster                                                       |
| regex_dna      | 126 ms                                                      | 117 ms: 1.08x faster                                                        |
| regex_compile  | 87.5 ms                                                     | 81.6 ms: 1.07x faster                                                       |
| regex_v8       | 14.2 ms                                                     | 15.3 ms: 1.07x slower                                                       |
| Geometric mean | (ref)                                                       | 1.04x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250201-pythonperf1-amd64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 1.37 sec                                                    | 1.31 sec: 1.04x faster                                                      |
| xml_etree_parse      | 93.0 ms                                                     | 89.4 ms: 1.04x faster                                                       |
| xml_etree_iterparse  | 65.2 ms                                                     | 62.8 ms: 1.04x faster                                                       |
| xml_etree_generate   | 55.8 ms                                                     | 54.8 ms: 1.02x faster                                                       |
| pickle_dict          | 18.4 us                                                     | 18.1 us: 1.02x faster                                                       |
| xml_etree_process    | 37.7 ms                                                     | 38.6 ms: 1.02x slower                                                       |
| unpickle_pure_python | 133 us                                                      | 140 us: 1.05x slower                                                        |
| unpickle             | 8.18 us                                                     | 8.61 us: 1.05x slower                                                       |
| pickle_pure_python   | 195 us                                                      | 210 us: 1.08x slower                                                        |
| pickle               | 7.43 us                                                     | 8.01 us: 1.08x slower                                                       |
| pickle_list          | 2.83 us                                                     | 3.08 us: 1.09x slower                                                       |
| json_loads           | 13.9 us                                                     | 15.4 us: 1.10x slower                                                       |
| json_dumps           | 5.70 ms                                                     | 6.64 ms: 1.17x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.03x slower                                                                |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250201-pythonperf1-amd64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 19.1 ms: 1.17x slower                                                       |
| python_startup         | 19.5 ms                                                     | 24.9 ms: 1.28x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.23x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250201-pythonperf1-amd64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 6.69 ms: 1.06x faster                                                       |
| django_template | 22.9 ms                                                     | 23.5 ms: 1.03x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.02x faster                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250201-pythonperf1-amd64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 400 ms: 1.93x faster                                                        |
| async_tree_io              | 731 ms                                                      | 400 ms: 1.83x faster                                                        |
| async_tree_memoization_tg  | 367 ms                                                      | 211 ms: 1.73x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 172 ms: 1.65x faster                                                        |
| async_tree_none            | 291 ms                                                      | 181 ms: 1.61x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 217 ms: 1.56x faster                                                        |
| asyncio_tcp_ssl            | 2.10 sec                                                    | 1.35 sec: 1.56x faster                                                      |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 340 ms: 1.48x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 339 ms: 1.45x faster                                                        |
| deepcopy                   | 238 us                                                      | 174 us: 1.37x faster                                                        |
| pathlib                    | 80.5 ms                                                     | 60.6 ms: 1.33x faster                                                       |
| comprehensions             | 14.1 us                                                     | 11.0 us: 1.28x faster                                                       |
| float                      | 56.8 ms                                                     | 45.0 ms: 1.26x faster                                                       |
| generators                 | 22.5 ms                                                     | 18.0 ms: 1.25x faster                                                       |
| deepcopy_memo              | 23.7 us                                                     | 18.9 us: 1.25x faster                                                       |
| spectral_norm              | 66.9 ms                                                     | 57.8 ms: 1.16x faster                                                       |
| deepcopy_reduce            | 2.09 us                                                     | 1.81 us: 1.15x faster                                                       |
| go                         | 91.6 ms                                                     | 80.7 ms: 1.14x faster                                                       |
| nbody                      | 71.9 ms                                                     | 64.2 ms: 1.12x faster                                                       |
| sqlite_synth               | 1.76 us                                                     | 1.57 us: 1.12x faster                                                       |
| async_generators           | 239 ms                                                      | 216 ms: 1.11x faster                                                        |
| chaos                      | 43.3 ms                                                     | 39.5 ms: 1.10x faster                                                       |
| regex_effbot               | 1.62 ms                                                     | 1.48 ms: 1.09x faster                                                       |
| regex_dna                  | 126 ms                                                      | 117 ms: 1.08x faster                                                        |
| coroutines                 | 14.3 ms                                                     | 13.2 ms: 1.08x faster                                                       |
| asyncio_tcp                | 487 ms                                                      | 452 ms: 1.08x faster                                                        |
| regex_compile              | 87.5 ms                                                     | 81.6 ms: 1.07x faster                                                       |
| dulwich_log                | 44.3 ms                                                     | 41.4 ms: 1.07x faster                                                       |
| mako                       | 7.09 ms                                                     | 6.69 ms: 1.06x faster                                                       |
| nqueens                    | 62.8 ms                                                     | 59.4 ms: 1.06x faster                                                       |
| raytrace                   | 192 ms                                                      | 182 ms: 1.06x faster                                                        |
| sympy_sum                  | 91.5 ms                                                     | 87.0 ms: 1.05x faster                                                       |
| tomli_loads                | 1.37 sec                                                    | 1.31 sec: 1.04x faster                                                      |
| xml_etree_parse            | 93.0 ms                                                     | 89.4 ms: 1.04x faster                                                       |
| deltablue                  | 2.16 ms                                                     | 2.08 ms: 1.04x faster                                                       |
| crypto_pyaes               | 48.5 ms                                                     | 46.8 ms: 1.04x faster                                                       |
| xml_etree_iterparse        | 65.2 ms                                                     | 62.8 ms: 1.04x faster                                                       |
| sympy_str                  | 175 ms                                                      | 170 ms: 1.03x faster                                                        |
| bench_thread_pool          | 857 us                                                      | 836 us: 1.02x faster                                                        |
| sqlglot_optimize           | 34.5 ms                                                     | 33.8 ms: 1.02x faster                                                       |
| sqlglot_normalize          | 187 ms                                                      | 183 ms: 1.02x faster                                                        |
| xml_etree_generate         | 55.8 ms                                                     | 54.8 ms: 1.02x faster                                                       |
| logging_simple             | 6.28 us                                                     | 6.16 us: 1.02x faster                                                       |
| pyflate                    | 295 ms                                                      | 290 ms: 1.02x faster                                                        |
| pickle_dict                | 18.4 us                                                     | 18.1 us: 1.02x faster                                                       |
| logging_format             | 6.72 us                                                     | 6.61 us: 1.02x faster                                                       |
| scimark_fft                | 184 ms                                                      | 182 ms: 1.01x faster                                                        |
| richards                   | 28.4 ms                                                     | 28.1 ms: 1.01x faster                                                       |
| docutils                   | 1.66 sec                                                    | 1.64 sec: 1.01x faster                                                      |
| pidigits                   | 152 ms                                                      | 151 ms: 1.01x faster                                                        |
| richards_super             | 32.1 ms                                                     | 31.8 ms: 1.01x faster                                                       |
| pprint_pformat             | 1.05 sec                                                    | 1.04 sec: 1.01x faster                                                      |
| meteor_contest             | 74.6 ms                                                     | 74.2 ms: 1.01x faster                                                       |
| scimark_monte_carlo        | 43.7 ms                                                     | 44.0 ms: 1.01x slower                                                       |
| logging_silent             | 60.5 ns                                                     | 60.8 ns: 1.01x slower                                                       |
| scimark_lu                 | 58.9 ms                                                     | 59.3 ms: 1.01x slower                                                       |
| sqlglot_parse              | 804 us                                                      | 819 us: 1.02x slower                                                        |
| 2to3                       | 218 ms                                                      | 222 ms: 1.02x slower                                                        |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.61 ms: 1.02x slower                                                       |
| pycparser                  | 699 ms                                                      | 713 ms: 1.02x slower                                                        |
| json                       | 3.05 ms                                                     | 3.11 ms: 1.02x slower                                                       |
| xml_etree_process          | 37.7 ms                                                     | 38.6 ms: 1.02x slower                                                       |
| django_template            | 22.9 ms                                                     | 23.5 ms: 1.03x slower                                                       |
| sympy_expand               | 284 ms                                                      | 293 ms: 1.03x slower                                                        |
| scimark_sor                | 78.8 ms                                                     | 82.2 ms: 1.04x slower                                                       |
| unpickle_pure_python       | 133 us                                                      | 140 us: 1.05x slower                                                        |
| fannkuch                   | 247 ms                                                      | 259 ms: 1.05x slower                                                        |
| unpickle                   | 8.18 us                                                     | 8.61 us: 1.05x slower                                                       |
| mdp                        | 1.37 sec                                                    | 1.46 sec: 1.07x slower                                                      |
| regex_v8                   | 14.2 ms                                                     | 15.3 ms: 1.07x slower                                                       |
| pickle_pure_python         | 195 us                                                      | 210 us: 1.08x slower                                                        |
| pickle                     | 7.43 us                                                     | 8.01 us: 1.08x slower                                                       |
| typing_runtime_protocols   | 95.1 us                                                     | 103 us: 1.08x slower                                                        |
| pickle_list                | 2.83 us                                                     | 3.08 us: 1.09x slower                                                       |
| json_loads                 | 13.9 us                                                     | 15.4 us: 1.10x slower                                                       |
| unpack_sequence            | 37.5 ns                                                     | 42.1 ns: 1.12x slower                                                       |
| telco                      | 4.13 ms                                                     | 4.66 ms: 1.13x slower                                                       |
| coverage                   | 40.8 ms                                                     | 47.1 ms: 1.15x slower                                                       |
| json_dumps                 | 5.70 ms                                                     | 6.64 ms: 1.17x slower                                                       |
| python_startup_no_site     | 16.2 ms                                                     | 19.1 ms: 1.17x slower                                                       |
| python_startup             | 19.5 ms                                                     | 24.9 ms: 1.28x slower                                                       |
| bench_mp_pool              | 69.2 ms                                                     | 89.2 ms: 1.29x slower                                                       |
| gc_traversal               | 1.52 ms                                                     | 2.02 ms: 1.33x slower                                                       |
| create_gc_cycles           | 752 us                                                      | 1.22 ms: 1.62x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.06x faster                                                                |

Benchmark hidden because not significant (5): hexiom, sqlglot_transpile, sympy_integrate, pprint_safe_repr, unpickle_list
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (13) of results/bm-20250201-3.14.0a4+-cf4c4ec/bm-20250201-pythonperf1-amd64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.067x faster

# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: unknown
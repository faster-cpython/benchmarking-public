# Results vs. 3.12.0

- fork: python
- ref: bedaea05987738c4c6b9
- machine: windows-amd64
- commit hash: bedaea0
- commit date: 2025-10-19
- overall geometric mean: 1.023x faster
- HPT reliability: 95.01%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20251019-pythonperf1-amd64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 220 ms: 1.01x slower                                                        |
| docutils       | 1.66 sec                                                    | 2.82 sec: 1.70x slower                                                      |
| Geometric mean | (ref)                                                       | 1.31x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20251019-pythonperf1-amd64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 323 ms: 2.39x faster                                                        |
| async_tree_io              | 731 ms                                                      | 344 ms: 2.12x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 145 ms: 1.96x faster                                                        |
| async_tree_memoization_tg  | 367 ms                                                      | 191 ms: 1.92x faster                                                        |
| async_tree_none            | 291 ms                                                      | 169 ms: 1.73x faster                                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 303 ms: 1.66x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 206 ms: 1.65x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 324 ms: 1.51x faster                                                        |
| Geometric mean             | (ref)                                                       | 1.85x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20251019-pythonperf1-amd64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 46.2 ms: 1.23x faster                                                       |
| pidigits       | 152 ms                                                      | 136 ms: 1.12x faster                                                        |
| nbody          | 71.9 ms                                                     | 76.7 ms: 1.07x slower                                                       |
| Geometric mean | (ref)                                                       | 1.09x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20251019-pythonperf1-amd64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_dna      | 126 ms                                                      | 112 ms: 1.13x faster                                                        |
| regex_v8       | 14.2 ms                                                     | 13.2 ms: 1.08x faster                                                       |
| regex_effbot   | 1.62 ms                                                     | 1.57 ms: 1.03x faster                                                       |
| regex_compile  | 87.5 ms                                                     | 89.8 ms: 1.03x slower                                                       |
| Geometric mean | (ref)                                                       | 1.05x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20251019-pythonperf1-amd64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_iterparse  | 65.2 ms                                                     | 59.9 ms: 1.09x faster                                                       |
| json_dumps           | 5.70 ms                                                     | 5.97 ms: 1.05x slower                                                       |
| pickle               | 7.43 us                                                     | 7.82 us: 1.05x slower                                                       |
| pickle_list          | 2.83 us                                                     | 3.03 us: 1.07x slower                                                       |
| unpickle_list        | 2.75 us                                                     | 3.02 us: 1.10x slower                                                       |
| pickle_dict          | 18.4 us                                                     | 20.3 us: 1.11x slower                                                       |
| xml_etree_generate   | 55.8 ms                                                     | 61.9 ms: 1.11x slower                                                       |
| unpickle_pure_python | 133 us                                                      | 148 us: 1.11x slower                                                        |
| pickle_pure_python   | 195 us                                                      | 223 us: 1.14x slower                                                        |
| json_loads           | 13.9 us                                                     | 15.9 us: 1.15x slower                                                       |
| xml_etree_process    | 37.7 ms                                                     | 43.2 ms: 1.15x slower                                                       |
| unpickle             | 8.18 us                                                     | 10.1 us: 1.23x slower                                                       |
| tomli_loads          | 1.37 sec                                                    | 2.32 sec: 1.70x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.12x slower                                                                |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20251019-pythonperf1-amd64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 19.2 ms: 1.18x slower                                                       |
| python_startup         | 19.5 ms                                                     | 25.9 ms: 1.33x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.25x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20251019-pythonperf1-amd64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| django_template | 22.9 ms                                                     | 26.1 ms: 1.14x slower                                                       |
| mako            | 7.09 ms                                                     | 10.1 ms: 1.42x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.27x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20251019-pythonperf1-amd64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pathlib                    | 80.5 ms                                                     | 28.8 ms: 2.79x faster                                                       |
| async_tree_io_tg           | 771 ms                                                      | 323 ms: 2.39x faster                                                        |
| async_tree_io              | 731 ms                                                      | 344 ms: 2.12x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 145 ms: 1.96x faster                                                        |
| async_tree_memoization_tg  | 367 ms                                                      | 191 ms: 1.92x faster                                                        |
| async_tree_none            | 291 ms                                                      | 169 ms: 1.73x faster                                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 303 ms: 1.66x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 206 ms: 1.65x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 324 ms: 1.51x faster                                                        |
| sqlite_synth               | 1.76 us                                                     | 1.34 us: 1.31x faster                                                       |
| mdp                        | 1.37 sec                                                    | 1.05 sec: 1.30x faster                                                      |
| deepcopy                   | 238 us                                                      | 183 us: 1.30x faster                                                        |
| deepcopy_memo              | 23.7 us                                                     | 18.6 us: 1.27x faster                                                       |
| float                      | 56.8 ms                                                     | 46.2 ms: 1.23x faster                                                       |
| comprehensions             | 14.1 us                                                     | 11.5 us: 1.23x faster                                                       |
| gc_traversal               | 1.52 ms                                                     | 1.31 ms: 1.16x faster                                                       |
| regex_dna                  | 126 ms                                                      | 112 ms: 1.13x faster                                                        |
| pidigits                   | 152 ms                                                      | 136 ms: 1.12x faster                                                        |
| xml_etree_iterparse        | 65.2 ms                                                     | 59.9 ms: 1.09x faster                                                       |
| asyncio_tcp                | 487 ms                                                      | 449 ms: 1.09x faster                                                        |
| dulwich_log                | 44.3 ms                                                     | 40.8 ms: 1.09x faster                                                       |
| regex_v8                   | 14.2 ms                                                     | 13.2 ms: 1.08x faster                                                       |
| generators                 | 22.5 ms                                                     | 21.0 ms: 1.07x faster                                                       |
| deepcopy_reduce            | 2.09 us                                                     | 1.96 us: 1.07x faster                                                       |
| coroutines                 | 14.3 ms                                                     | 13.7 ms: 1.04x faster                                                       |
| regex_effbot               | 1.62 ms                                                     | 1.57 ms: 1.03x faster                                                       |
| go                         | 91.6 ms                                                     | 89.4 ms: 1.02x faster                                                       |
| unpack_sequence            | 37.5 ns                                                     | 36.7 ns: 1.02x faster                                                       |
| logging_silent             | 60.5 ns                                                     | 59.9 ns: 1.01x faster                                                       |
| 2to3                       | 218 ms                                                      | 220 ms: 1.01x slower                                                        |
| scimark_fft                | 184 ms                                                      | 187 ms: 1.01x slower                                                        |
| regex_compile              | 87.5 ms                                                     | 89.8 ms: 1.03x slower                                                       |
| sympy_sum                  | 91.5 ms                                                     | 94.7 ms: 1.04x slower                                                       |
| logging_simple             | 6.28 us                                                     | 6.53 us: 1.04x slower                                                       |
| pyflate                    | 295 ms                                                      | 307 ms: 1.04x slower                                                        |
| pprint_safe_repr           | 513 ms                                                      | 536 ms: 1.04x slower                                                        |
| logging_format             | 6.72 us                                                     | 7.04 us: 1.05x slower                                                       |
| json_dumps                 | 5.70 ms                                                     | 5.97 ms: 1.05x slower                                                       |
| async_generators           | 239 ms                                                      | 252 ms: 1.05x slower                                                        |
| pickle                     | 7.43 us                                                     | 7.82 us: 1.05x slower                                                       |
| chaos                      | 43.3 ms                                                     | 45.6 ms: 1.05x slower                                                       |
| sympy_str                  | 175 ms                                                      | 185 ms: 1.05x slower                                                        |
| scimark_sor                | 78.8 ms                                                     | 83.3 ms: 1.06x slower                                                       |
| spectral_norm              | 66.9 ms                                                     | 70.8 ms: 1.06x slower                                                       |
| nbody                      | 71.9 ms                                                     | 76.7 ms: 1.07x slower                                                       |
| sympy_integrate            | 13.0 ms                                                     | 13.8 ms: 1.07x slower                                                       |
| hexiom                     | 4.10 ms                                                     | 4.39 ms: 1.07x slower                                                       |
| scimark_lu                 | 58.9 ms                                                     | 63.0 ms: 1.07x slower                                                       |
| bench_mp_pool              | 69.2 ms                                                     | 74.2 ms: 1.07x slower                                                       |
| pickle_list                | 2.83 us                                                     | 3.03 us: 1.07x slower                                                       |
| raytrace                   | 192 ms                                                      | 208 ms: 1.08x slower                                                        |
| deltablue                  | 2.16 ms                                                     | 2.35 ms: 1.09x slower                                                       |
| unpickle_list              | 2.75 us                                                     | 3.02 us: 1.10x slower                                                       |
| pickle_dict                | 18.4 us                                                     | 20.3 us: 1.11x slower                                                       |
| xml_etree_generate         | 55.8 ms                                                     | 61.9 ms: 1.11x slower                                                       |
| sympy_expand               | 284 ms                                                      | 315 ms: 1.11x slower                                                        |
| unpickle_pure_python       | 133 us                                                      | 148 us: 1.11x slower                                                        |
| scimark_monte_carlo        | 43.7 ms                                                     | 49.4 ms: 1.13x slower                                                       |
| nqueens                    | 62.8 ms                                                     | 71.4 ms: 1.14x slower                                                       |
| django_template            | 22.9 ms                                                     | 26.1 ms: 1.14x slower                                                       |
| meteor_contest             | 74.6 ms                                                     | 85.1 ms: 1.14x slower                                                       |
| pickle_pure_python         | 195 us                                                      | 223 us: 1.14x slower                                                        |
| json_loads                 | 13.9 us                                                     | 15.9 us: 1.15x slower                                                       |
| xml_etree_process          | 37.7 ms                                                     | 43.2 ms: 1.15x slower                                                       |
| richards                   | 28.4 ms                                                     | 32.9 ms: 1.16x slower                                                       |
| crypto_pyaes               | 48.5 ms                                                     | 56.3 ms: 1.16x slower                                                       |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 3.00 ms: 1.17x slower                                                       |
| python_startup_no_site     | 16.2 ms                                                     | 19.2 ms: 1.18x slower                                                       |
| bench_thread_pool          | 857 us                                                      | 1.02 ms: 1.19x slower                                                       |
| richards_super             | 32.1 ms                                                     | 38.5 ms: 1.20x slower                                                       |
| telco                      | 4.13 ms                                                     | 5.02 ms: 1.22x slower                                                       |
| unpickle                   | 8.18 us                                                     | 10.1 us: 1.23x slower                                                       |
| fannkuch                   | 247 ms                                                      | 310 ms: 1.26x slower                                                        |
| typing_runtime_protocols   | 95.1 us                                                     | 126 us: 1.32x slower                                                        |
| python_startup             | 19.5 ms                                                     | 25.9 ms: 1.33x slower                                                       |
| create_gc_cycles           | 752 us                                                      | 1.03 ms: 1.37x slower                                                       |
| mako                       | 7.09 ms                                                     | 10.1 ms: 1.42x slower                                                       |
| pprint_pformat             | 1.05 sec                                                    | 1.62 sec: 1.55x slower                                                      |
| coverage                   | 40.8 ms                                                     | 67.1 ms: 1.64x slower                                                       |
| tomli_loads                | 1.37 sec                                                    | 2.32 sec: 1.70x slower                                                      |
| docutils                   | 1.66 sec                                                    | 2.82 sec: 1.70x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.01x faster                                                                |

Benchmark hidden because not significant (4): json, xml_etree_parse, pycparser, asyncio_tcp_ssl
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (17) of results/bm-20251019-3.15.0a1+-bedaea0-NOGIL/bm-20251019-pythonperf1-amd64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.023x faster

# HPT report

- Reliability score: 95.01% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown
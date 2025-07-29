# Results vs. 3.12.0

- fork: faster-cpython
- ref: check_periodic_at_en
- machine: windows-amd64
- commit hash: 021fc09
- commit date: 2025-07-25
- overall geometric mean: 1.016x slower
- HPT reliability: 89.84%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250725-pythonperf1-amd64-faster%2dcpython-check_periodic_at_en-3.15.0a0-021fc09 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 250 ms: 1.15x slower                                                                 |
| docutils       | 1.66 sec                                                    | 1.77 sec: 1.07x slower                                                               |
| Geometric mean | (ref)                                                       | 1.11x slower                                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250725-pythonperf1-amd64-faster%2dcpython-check_periodic_at_en-3.15.0a0-021fc09 |
|----------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 426 ms: 1.81x faster                                                                 |
| async_tree_io              | 731 ms                                                      | 438 ms: 1.67x faster                                                                 |
| async_tree_memoization_tg  | 367 ms                                                      | 221 ms: 1.66x faster                                                                 |
| async_tree_none_tg         | 285 ms                                                      | 185 ms: 1.54x faster                                                                 |
| async_tree_memoization     | 339 ms                                                      | 223 ms: 1.52x faster                                                                 |
| async_tree_none            | 291 ms                                                      | 192 ms: 1.51x faster                                                                 |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 355 ms: 1.41x faster                                                                 |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 350 ms: 1.40x faster                                                                 |
| Geometric mean             | (ref)                                                       | 1.56x faster                                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250725-pythonperf1-amd64-faster%2dcpython-check_periodic_at_en-3.15.0a0-021fc09 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 45.7 ms: 1.24x faster                                                                |
| pidigits       | 152 ms                                                      | 150 ms: 1.01x faster                                                                 |
| nbody          | 71.9 ms                                                     | 87.0 ms: 1.21x slower                                                                |
| Geometric mean | (ref)                                                       | 1.01x faster                                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250725-pythonperf1-amd64-faster%2dcpython-check_periodic_at_en-3.15.0a0-021fc09 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| regex_effbot   | 1.62 ms                                                     | 1.53 ms: 1.06x faster                                                                |
| regex_dna      | 126 ms                                                      | 125 ms: 1.01x faster                                                                 |
| regex_compile  | 87.5 ms                                                     | 95.1 ms: 1.09x slower                                                                |
| Geometric mean | (ref)                                                       | 1.00x slower                                                                         |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250725-pythonperf1-amd64-faster%2dcpython-check_periodic_at_en-3.15.0a0-021fc09 |
|----------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| xml_etree_parse      | 93.0 ms                                                     | 91.4 ms: 1.02x faster                                                                |
| json_loads           | 13.9 us                                                     | 14.5 us: 1.04x slower                                                                |
| xml_etree_iterparse  | 65.2 ms                                                     | 70.5 ms: 1.08x slower                                                                |
| json_dumps           | 5.70 ms                                                     | 6.30 ms: 1.11x slower                                                                |
| xml_etree_generate   | 55.8 ms                                                     | 65.1 ms: 1.17x slower                                                                |
| xml_etree_process    | 37.7 ms                                                     | 45.6 ms: 1.21x slower                                                                |
| tomli_loads          | 1.37 sec                                                    | 1.70 sec: 1.24x slower                                                               |
| pickle_pure_python   | 195 us                                                      | 249 us: 1.27x slower                                                                 |
| unpickle_pure_python | 133 us                                                      | 209 us: 1.57x slower                                                                 |
| Geometric mean       | (ref)                                                       | 1.18x slower                                                                         |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250725-pythonperf1-amd64-faster%2dcpython-check_periodic_at_en-3.15.0a0-021fc09 |
|------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 20.2 ms: 1.25x slower                                                                |
| python_startup         | 19.5 ms                                                     | 27.4 ms: 1.41x slower                                                                |
| Geometric mean         | (ref)                                                       | 1.32x slower                                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250725-pythonperf1-amd64-faster%2dcpython-check_periodic_at_en-3.15.0a0-021fc09 |
|-----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| django_template | 22.9 ms                                                     | 26.1 ms: 1.14x slower                                                                |
| mako            | 7.09 ms                                                     | 8.86 ms: 1.25x slower                                                                |
| Geometric mean  | (ref)                                                       | 1.19x slower                                                                         |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250725-pythonperf1-amd64-faster%2dcpython-check_periodic_at_en-3.15.0a0-021fc09 |
|----------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| pathlib                    | 80.5 ms                                                     | 33.4 ms: 2.41x faster                                                                |
| async_tree_io_tg           | 771 ms                                                      | 426 ms: 1.81x faster                                                                 |
| async_tree_io              | 731 ms                                                      | 438 ms: 1.67x faster                                                                 |
| async_tree_memoization_tg  | 367 ms                                                      | 221 ms: 1.66x faster                                                                 |
| mdp                        | 1.37 sec                                                    | 862 ms: 1.59x faster                                                                 |
| async_tree_none_tg         | 285 ms                                                      | 185 ms: 1.54x faster                                                                 |
| async_tree_memoization     | 339 ms                                                      | 223 ms: 1.52x faster                                                                 |
| async_tree_none            | 291 ms                                                      | 192 ms: 1.51x faster                                                                 |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 355 ms: 1.41x faster                                                                 |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 350 ms: 1.40x faster                                                                 |
| deepcopy                   | 238 us                                                      | 183 us: 1.30x faster                                                                 |
| deepcopy_memo              | 23.7 us                                                     | 18.9 us: 1.26x faster                                                                |
| float                      | 56.8 ms                                                     | 45.7 ms: 1.24x faster                                                                |
| generators                 | 22.5 ms                                                     | 20.3 ms: 1.11x faster                                                                |
| deepcopy_reduce            | 2.09 us                                                     | 1.89 us: 1.11x faster                                                                |
| sqlite_synth               | 1.76 us                                                     | 1.60 us: 1.10x faster                                                                |
| go                         | 91.6 ms                                                     | 83.6 ms: 1.09x faster                                                                |
| regex_effbot               | 1.62 ms                                                     | 1.53 ms: 1.06x faster                                                                |
| logging_silent             | 60.5 ns                                                     | 58.6 ns: 1.03x faster                                                                |
| scimark_monte_carlo        | 43.7 ms                                                     | 42.6 ms: 1.03x faster                                                                |
| spectral_norm              | 66.9 ms                                                     | 65.6 ms: 1.02x faster                                                                |
| xml_etree_parse            | 93.0 ms                                                     | 91.4 ms: 1.02x faster                                                                |
| pidigits                   | 152 ms                                                      | 150 ms: 1.01x faster                                                                 |
| regex_dna                  | 126 ms                                                      | 125 ms: 1.01x faster                                                                 |
| richards                   | 28.4 ms                                                     | 28.7 ms: 1.01x slower                                                                |
| richards_super             | 32.1 ms                                                     | 32.5 ms: 1.01x slower                                                                |
| logging_simple             | 6.28 us                                                     | 6.44 us: 1.03x slower                                                                |
| sympy_sum                  | 91.5 ms                                                     | 94.4 ms: 1.03x slower                                                                |
| coroutines                 | 14.3 ms                                                     | 14.8 ms: 1.03x slower                                                                |
| json_loads                 | 13.9 us                                                     | 14.5 us: 1.04x slower                                                                |
| scimark_lu                 | 58.9 ms                                                     | 61.3 ms: 1.04x slower                                                                |
| sympy_integrate            | 13.0 ms                                                     | 13.5 ms: 1.04x slower                                                                |
| logging_format             | 6.72 us                                                     | 7.02 us: 1.05x slower                                                                |
| sympy_str                  | 175 ms                                                      | 185 ms: 1.05x slower                                                                 |
| docutils                   | 1.66 sec                                                    | 1.77 sec: 1.07x slower                                                               |
| xml_etree_iterparse        | 65.2 ms                                                     | 70.5 ms: 1.08x slower                                                                |
| async_generators           | 239 ms                                                      | 259 ms: 1.08x slower                                                                 |
| regex_compile              | 87.5 ms                                                     | 95.1 ms: 1.09x slower                                                                |
| deltablue                  | 2.16 ms                                                     | 2.37 ms: 1.10x slower                                                                |
| json_dumps                 | 5.70 ms                                                     | 6.30 ms: 1.11x slower                                                                |
| hexiom                     | 4.10 ms                                                     | 4.60 ms: 1.12x slower                                                                |
| nqueens                    | 62.8 ms                                                     | 70.6 ms: 1.12x slower                                                                |
| django_template            | 22.9 ms                                                     | 26.1 ms: 1.14x slower                                                                |
| pyflate                    | 295 ms                                                      | 338 ms: 1.15x slower                                                                 |
| 2to3                       | 218 ms                                                      | 250 ms: 1.15x slower                                                                 |
| sympy_expand               | 284 ms                                                      | 326 ms: 1.15x slower                                                                 |
| meteor_contest             | 74.6 ms                                                     | 86.2 ms: 1.16x slower                                                                |
| xml_etree_generate         | 55.8 ms                                                     | 65.1 ms: 1.17x slower                                                                |
| comprehensions             | 14.1 us                                                     | 16.6 us: 1.17x slower                                                                |
| pprint_pformat             | 1.05 sec                                                    | 1.25 sec: 1.20x slower                                                               |
| scimark_fft                | 184 ms                                                      | 221 ms: 1.20x slower                                                                 |
| xml_etree_process          | 37.7 ms                                                     | 45.6 ms: 1.21x slower                                                                |
| nbody                      | 71.9 ms                                                     | 87.0 ms: 1.21x slower                                                                |
| telco                      | 4.13 ms                                                     | 5.01 ms: 1.21x slower                                                                |
| pycparser                  | 699 ms                                                      | 853 ms: 1.22x slower                                                                 |
| pprint_safe_repr           | 513 ms                                                      | 632 ms: 1.23x slower                                                                 |
| tomli_loads                | 1.37 sec                                                    | 1.70 sec: 1.24x slower                                                               |
| python_startup_no_site     | 16.2 ms                                                     | 20.2 ms: 1.25x slower                                                                |
| mako                       | 7.09 ms                                                     | 8.86 ms: 1.25x slower                                                                |
| pickle_pure_python         | 195 us                                                      | 249 us: 1.27x slower                                                                 |
| coverage                   | 40.8 ms                                                     | 53.0 ms: 1.30x slower                                                                |
| typing_runtime_protocols   | 95.1 us                                                     | 124 us: 1.30x slower                                                                 |
| crypto_pyaes               | 48.5 ms                                                     | 64.6 ms: 1.33x slower                                                                |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 3.58 ms: 1.40x slower                                                                |
| python_startup             | 19.5 ms                                                     | 27.4 ms: 1.41x slower                                                                |
| fannkuch                   | 247 ms                                                      | 354 ms: 1.44x slower                                                                 |
| gc_traversal               | 1.52 ms                                                     | 2.19 ms: 1.44x slower                                                                |
| unpickle_pure_python       | 133 us                                                      | 209 us: 1.57x slower                                                                 |
| create_gc_cycles           | 752 us                                                      | 1.37 ms: 1.82x slower                                                                |
| Geometric mean             | (ref)                                                       | 1.02x slower                                                                         |

Benchmark hidden because not significant (6): json, regex_v8, raytrace, scimark_sor, dulwich_log, chaos
Ignored benchmarks (21) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (17) of results/bm-20250725-3.15.0a0-021fc09-PYTHON_UOPS/bm-20250725-pythonperf1-amd64-faster%2dcpython-check_periodic_at_en-3.15.0a0-021fc09.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.016x slower

# HPT report

- Reliability score: 89.84% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown
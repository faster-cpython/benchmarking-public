# Results vs. 3.12.0

- fork: python
- ref: ae4d27eba7c746463c62
- machine: windows-amd64
- commit hash: ae4d27e
- commit date: 2025-07-24
- overall geometric mean: 1.108x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250724-pythonperf1-amd64-python-ae4d27eba7c746463c62-3.15.0a0-ae4d27e |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 223 ms: 1.02x slower                                                       |
| Geometric mean | (ref)                                                       | 1.01x slower                                                               |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250724-pythonperf1-amd64-python-ae4d27eba7c746463c62-3.15.0a0-ae4d27e |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 388 ms: 1.99x faster                                                       |
| async_tree_io              | 731 ms                                                      | 392 ms: 1.86x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 166 ms: 1.72x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 217 ms: 1.69x faster                                                       |
| async_tree_none            | 291 ms                                                      | 178 ms: 1.64x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 211 ms: 1.61x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 338 ms: 1.45x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 348 ms: 1.44x faster                                                       |
| Geometric mean             | (ref)                                                       | 1.67x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250724-pythonperf1-amd64-python-ae4d27eba7c746463c62-3.15.0a0-ae4d27e |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 71.9 ms                                                     | 55.7 ms: 1.29x faster                                                      |
| float          | 56.8 ms                                                     | 45.6 ms: 1.25x faster                                                      |
| pidigits       | 152 ms                                                      | 146 ms: 1.04x faster                                                       |
| Geometric mean | (ref)                                                       | 1.19x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250724-pythonperf1-amd64-python-ae4d27eba7c746463c62-3.15.0a0-ae4d27e |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 87.5 ms                                                     | 81.4 ms: 1.08x faster                                                      |
| regex_dna      | 126 ms                                                      | 118 ms: 1.07x faster                                                       |
| regex_v8       | 14.2 ms                                                     | 13.8 ms: 1.03x faster                                                      |
| Geometric mean | (ref)                                                       | 1.05x faster                                                               |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250724-pythonperf1-amd64-python-ae4d27eba7c746463c62-3.15.0a0-ae4d27e |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| unpickle_pure_python | 133 us                                                      | 106 us: 1.26x faster                                                       |
| tomli_loads          | 1.37 sec                                                    | 1.13 sec: 1.21x faster                                                     |
| xml_etree_generate   | 55.8 ms                                                     | 52.4 ms: 1.07x faster                                                      |
| xml_etree_process    | 37.7 ms                                                     | 36.3 ms: 1.04x faster                                                      |
| xml_etree_parse      | 93.0 ms                                                     | 94.6 ms: 1.02x slower                                                      |
| xml_etree_iterparse  | 65.2 ms                                                     | 67.0 ms: 1.03x slower                                                      |
| json_loads           | 13.9 us                                                     | 14.5 us: 1.04x slower                                                      |
| pickle_pure_python   | 195 us                                                      | 210 us: 1.07x slower                                                       |
| json_dumps           | 5.70 ms                                                     | 6.39 ms: 1.12x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.03x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250724-pythonperf1-amd64-python-ae4d27eba7c746463c62-3.15.0a0-ae4d27e |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 20.0 ms: 1.23x slower                                                      |
| python_startup         | 19.5 ms                                                     | 26.7 ms: 1.37x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.30x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250724-pythonperf1-amd64-python-ae4d27eba7c746463c62-3.15.0a0-ae4d27e |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 5.48 ms: 1.29x faster                                                      |
| django_template | 22.9 ms                                                     | 24.5 ms: 1.07x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.10x faster                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250724-pythonperf1-amd64-python-ae4d27eba7c746463c62-3.15.0a0-ae4d27e |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pathlib                    | 80.5 ms                                                     | 32.9 ms: 2.44x faster                                                      |
| async_tree_io_tg           | 771 ms                                                      | 388 ms: 1.99x faster                                                       |
| async_tree_io              | 731 ms                                                      | 392 ms: 1.86x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 166 ms: 1.72x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 217 ms: 1.69x faster                                                       |
| mdp                        | 1.37 sec                                                    | 815 ms: 1.68x faster                                                       |
| async_tree_none            | 291 ms                                                      | 178 ms: 1.64x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 211 ms: 1.61x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 338 ms: 1.45x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 348 ms: 1.44x faster                                                       |
| deepcopy                   | 238 us                                                      | 176 us: 1.35x faster                                                       |
| comprehensions             | 14.1 us                                                     | 10.6 us: 1.33x faster                                                      |
| mako                       | 7.09 ms                                                     | 5.48 ms: 1.29x faster                                                      |
| nbody                      | 71.9 ms                                                     | 55.7 ms: 1.29x faster                                                      |
| unpickle_pure_python       | 133 us                                                      | 106 us: 1.26x faster                                                       |
| float                      | 56.8 ms                                                     | 45.6 ms: 1.25x faster                                                      |
| deepcopy_memo              | 23.7 us                                                     | 19.2 us: 1.23x faster                                                      |
| scimark_fft                | 184 ms                                                      | 151 ms: 1.22x faster                                                       |
| tomli_loads                | 1.37 sec                                                    | 1.13 sec: 1.21x faster                                                     |
| pprint_pformat             | 1.05 sec                                                    | 896 ms: 1.17x faster                                                       |
| go                         | 91.6 ms                                                     | 79.0 ms: 1.16x faster                                                      |
| generators                 | 22.5 ms                                                     | 19.5 ms: 1.16x faster                                                      |
| fannkuch                   | 247 ms                                                      | 213 ms: 1.16x faster                                                       |
| pyflate                    | 295 ms                                                      | 255 ms: 1.15x faster                                                       |
| pprint_safe_repr           | 513 ms                                                      | 446 ms: 1.15x faster                                                       |
| sqlite_synth               | 1.76 us                                                     | 1.55 us: 1.14x faster                                                      |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.28 ms: 1.12x faster                                                      |
| deepcopy_reduce            | 2.09 us                                                     | 1.92 us: 1.09x faster                                                      |
| scimark_monte_carlo        | 43.7 ms                                                     | 40.5 ms: 1.08x faster                                                      |
| regex_compile              | 87.5 ms                                                     | 81.4 ms: 1.08x faster                                                      |
| regex_dna                  | 126 ms                                                      | 118 ms: 1.07x faster                                                       |
| xml_etree_generate         | 55.8 ms                                                     | 52.4 ms: 1.07x faster                                                      |
| crypto_pyaes               | 48.5 ms                                                     | 45.9 ms: 1.06x faster                                                      |
| logging_silent             | 60.5 ns                                                     | 57.3 ns: 1.06x faster                                                      |
| raytrace                   | 192 ms                                                      | 184 ms: 1.05x faster                                                       |
| dulwich_log                | 44.3 ms                                                     | 42.3 ms: 1.05x faster                                                      |
| meteor_contest             | 74.6 ms                                                     | 71.4 ms: 1.05x faster                                                      |
| pidigits                   | 152 ms                                                      | 146 ms: 1.04x faster                                                       |
| sympy_sum                  | 91.5 ms                                                     | 88.0 ms: 1.04x faster                                                      |
| xml_etree_process          | 37.7 ms                                                     | 36.3 ms: 1.04x faster                                                      |
| regex_v8                   | 14.2 ms                                                     | 13.8 ms: 1.03x faster                                                      |
| richards_super             | 32.1 ms                                                     | 31.2 ms: 1.03x faster                                                      |
| chaos                      | 43.3 ms                                                     | 42.1 ms: 1.03x faster                                                      |
| sympy_str                  | 175 ms                                                      | 171 ms: 1.03x faster                                                       |
| spectral_norm              | 66.9 ms                                                     | 65.5 ms: 1.02x faster                                                      |
| richards                   | 28.4 ms                                                     | 27.9 ms: 1.02x faster                                                      |
| sympy_integrate            | 13.0 ms                                                     | 12.8 ms: 1.01x faster                                                      |
| xml_etree_parse            | 93.0 ms                                                     | 94.6 ms: 1.02x slower                                                      |
| logging_simple             | 6.28 us                                                     | 6.40 us: 1.02x slower                                                      |
| telco                      | 4.13 ms                                                     | 4.22 ms: 1.02x slower                                                      |
| 2to3                       | 218 ms                                                      | 223 ms: 1.02x slower                                                       |
| xml_etree_iterparse        | 65.2 ms                                                     | 67.0 ms: 1.03x slower                                                      |
| scimark_lu                 | 58.9 ms                                                     | 60.8 ms: 1.03x slower                                                      |
| deltablue                  | 2.16 ms                                                     | 2.24 ms: 1.04x slower                                                      |
| coroutines                 | 14.3 ms                                                     | 14.8 ms: 1.04x slower                                                      |
| json_loads                 | 13.9 us                                                     | 14.5 us: 1.04x slower                                                      |
| async_generators           | 239 ms                                                      | 249 ms: 1.04x slower                                                       |
| hexiom                     | 4.10 ms                                                     | 4.28 ms: 1.04x slower                                                      |
| sympy_expand               | 284 ms                                                      | 298 ms: 1.05x slower                                                       |
| django_template            | 22.9 ms                                                     | 24.5 ms: 1.07x slower                                                      |
| pickle_pure_python         | 195 us                                                      | 210 us: 1.07x slower                                                       |
| typing_runtime_protocols   | 95.1 us                                                     | 104 us: 1.09x slower                                                       |
| json_dumps                 | 5.70 ms                                                     | 6.39 ms: 1.12x slower                                                      |
| coverage                   | 40.8 ms                                                     | 49.4 ms: 1.21x slower                                                      |
| python_startup_no_site     | 16.2 ms                                                     | 20.0 ms: 1.23x slower                                                      |
| python_startup             | 19.5 ms                                                     | 26.7 ms: 1.37x slower                                                      |
| gc_traversal               | 1.52 ms                                                     | 2.16 ms: 1.42x slower                                                      |
| create_gc_cycles           | 752 us                                                      | 1.37 ms: 1.82x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.10x faster                                                               |

Benchmark hidden because not significant (7): regex_effbot, docutils, nqueens, pycparser, json, scimark_sor, logging_format
Ignored benchmarks (21) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (17) of results/bm-20250724-3.15.0a0-ae4d27e-JIT/bm-20250724-pythonperf1-amd64-python-ae4d27eba7c746463c62-3.15.0a0-ae4d27e.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.108x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: unknown
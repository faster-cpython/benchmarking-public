# Results vs. 3.12.0

- fork: python
- ref: 0f866cbfefd797b4dae2
- machine: windows-amd64
- commit hash: 0f866cb
- commit date: 2025-06-10
- overall geometric mean: 1.110x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250610-pythonperf1-amd64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 221 ms: 1.02x slower                                                       |
| Geometric mean | (ref)                                                       | 1.01x slower                                                               |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250610-pythonperf1-amd64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 391 ms: 1.97x faster                                                       |
| async_tree_io              | 731 ms                                                      | 398 ms: 1.84x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 212 ms: 1.73x faster                                                       |
| async_tree_none            | 291 ms                                                      | 169 ms: 1.73x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 168 ms: 1.70x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 205 ms: 1.65x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 335 ms: 1.46x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 345 ms: 1.46x faster                                                       |
| Geometric mean             | (ref)                                                       | 1.68x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250610-pythonperf1-amd64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 43.8 ms: 1.30x faster                                                      |
| nbody          | 71.9 ms                                                     | 58.5 ms: 1.23x faster                                                      |
| pidigits       | 152 ms                                                      | 149 ms: 1.02x faster                                                       |
| Geometric mean | (ref)                                                       | 1.18x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250610-pythonperf1-amd64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 87.5 ms                                                     | 78.3 ms: 1.12x faster                                                      |
| regex_dna      | 126 ms                                                      | 119 ms: 1.06x faster                                                       |
| regex_effbot   | 1.62 ms                                                     | 1.56 ms: 1.04x faster                                                      |
| regex_v8       | 14.2 ms                                                     | 14.1 ms: 1.01x faster                                                      |
| Geometric mean | (ref)                                                       | 1.06x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250610-pythonperf1-amd64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| tomli_loads          | 1.37 sec                                                    | 1.15 sec: 1.19x faster                                                     |
| unpickle_pure_python | 133 us                                                      | 112 us: 1.18x faster                                                       |
| xml_etree_generate   | 55.8 ms                                                     | 51.5 ms: 1.08x faster                                                      |
| xml_etree_process    | 37.7 ms                                                     | 36.3 ms: 1.04x faster                                                      |
| xml_etree_parse      | 93.0 ms                                                     | 91.2 ms: 1.02x faster                                                      |
| xml_etree_iterparse  | 65.2 ms                                                     | 64.4 ms: 1.01x faster                                                      |
| json_loads           | 13.9 us                                                     | 14.4 us: 1.03x slower                                                      |
| pickle_pure_python   | 195 us                                                      | 204 us: 1.04x slower                                                       |
| json_dumps           | 5.70 ms                                                     | 6.27 ms: 1.10x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.04x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250610-pythonperf1-amd64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 19.5 ms: 1.20x slower                                                      |
| python_startup         | 19.5 ms                                                     | 26.0 ms: 1.34x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.27x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250610-pythonperf1-amd64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 5.61 ms: 1.26x faster                                                      |
| django_template | 22.9 ms                                                     | 23.9 ms: 1.04x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.10x faster                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250610-pythonperf1-amd64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pathlib                    | 80.5 ms                                                     | 31.9 ms: 2.53x faster                                                      |
| async_tree_io_tg           | 771 ms                                                      | 391 ms: 1.97x faster                                                       |
| async_tree_io              | 731 ms                                                      | 398 ms: 1.84x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 212 ms: 1.73x faster                                                       |
| async_tree_none            | 291 ms                                                      | 169 ms: 1.73x faster                                                       |
| mdp                        | 1.37 sec                                                    | 806 ms: 1.70x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 168 ms: 1.70x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 205 ms: 1.65x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 335 ms: 1.46x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 345 ms: 1.46x faster                                                       |
| deepcopy                   | 238 us                                                      | 168 us: 1.41x faster                                                       |
| float                      | 56.8 ms                                                     | 43.8 ms: 1.30x faster                                                      |
| deepcopy_memo              | 23.7 us                                                     | 18.3 us: 1.29x faster                                                      |
| comprehensions             | 14.1 us                                                     | 10.9 us: 1.29x faster                                                      |
| mako                       | 7.09 ms                                                     | 5.61 ms: 1.26x faster                                                      |
| nbody                      | 71.9 ms                                                     | 58.5 ms: 1.23x faster                                                      |
| go                         | 91.6 ms                                                     | 76.3 ms: 1.20x faster                                                      |
| scimark_fft                | 184 ms                                                      | 154 ms: 1.20x faster                                                       |
| tomli_loads                | 1.37 sec                                                    | 1.15 sec: 1.19x faster                                                     |
| unpickle_pure_python       | 133 us                                                      | 112 us: 1.18x faster                                                       |
| deepcopy_reduce            | 2.09 us                                                     | 1.80 us: 1.16x faster                                                      |
| generators                 | 22.5 ms                                                     | 19.6 ms: 1.15x faster                                                      |
| pyflate                    | 295 ms                                                      | 261 ms: 1.13x faster                                                       |
| sqlite_synth               | 1.76 us                                                     | 1.56 us: 1.13x faster                                                      |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.27 ms: 1.13x faster                                                      |
| regex_compile              | 87.5 ms                                                     | 78.3 ms: 1.12x faster                                                      |
| spectral_norm              | 66.9 ms                                                     | 59.9 ms: 1.12x faster                                                      |
| chaos                      | 43.3 ms                                                     | 38.9 ms: 1.12x faster                                                      |
| xml_etree_generate         | 55.8 ms                                                     | 51.5 ms: 1.08x faster                                                      |
| raytrace                   | 192 ms                                                      | 178 ms: 1.08x faster                                                       |
| dulwich_log                | 44.3 ms                                                     | 41.1 ms: 1.08x faster                                                      |
| scimark_monte_carlo        | 43.7 ms                                                     | 40.8 ms: 1.07x faster                                                      |
| regex_dna                  | 126 ms                                                      | 119 ms: 1.06x faster                                                       |
| nqueens                    | 62.8 ms                                                     | 59.7 ms: 1.05x faster                                                      |
| sympy_sum                  | 91.5 ms                                                     | 87.5 ms: 1.05x faster                                                      |
| scimark_sor                | 78.8 ms                                                     | 75.5 ms: 1.04x faster                                                      |
| richards_super             | 32.1 ms                                                     | 30.9 ms: 1.04x faster                                                      |
| xml_etree_process          | 37.7 ms                                                     | 36.3 ms: 1.04x faster                                                      |
| richards                   | 28.4 ms                                                     | 27.3 ms: 1.04x faster                                                      |
| regex_effbot               | 1.62 ms                                                     | 1.56 ms: 1.04x faster                                                      |
| coroutines                 | 14.3 ms                                                     | 13.8 ms: 1.03x faster                                                      |
| crypto_pyaes               | 48.5 ms                                                     | 47.1 ms: 1.03x faster                                                      |
| sympy_integrate            | 13.0 ms                                                     | 12.6 ms: 1.03x faster                                                      |
| pidigits                   | 152 ms                                                      | 149 ms: 1.02x faster                                                       |
| xml_etree_parse            | 93.0 ms                                                     | 91.2 ms: 1.02x faster                                                      |
| sympy_str                  | 175 ms                                                      | 172 ms: 1.02x faster                                                       |
| meteor_contest             | 74.6 ms                                                     | 73.2 ms: 1.02x faster                                                      |
| xml_etree_iterparse        | 65.2 ms                                                     | 64.4 ms: 1.01x faster                                                      |
| fannkuch                   | 247 ms                                                      | 244 ms: 1.01x faster                                                       |
| regex_v8                   | 14.2 ms                                                     | 14.1 ms: 1.01x faster                                                      |
| logging_format             | 6.72 us                                                     | 6.79 us: 1.01x slower                                                      |
| logging_simple             | 6.28 us                                                     | 6.35 us: 1.01x slower                                                      |
| pprint_pformat             | 1.05 sec                                                    | 1.06 sec: 1.01x slower                                                     |
| async_generators           | 239 ms                                                      | 243 ms: 1.01x slower                                                       |
| 2to3                       | 218 ms                                                      | 221 ms: 1.02x slower                                                       |
| pprint_safe_repr           | 513 ms                                                      | 524 ms: 1.02x slower                                                       |
| deltablue                  | 2.16 ms                                                     | 2.21 ms: 1.02x slower                                                      |
| json_loads                 | 13.9 us                                                     | 14.4 us: 1.03x slower                                                      |
| pickle_pure_python         | 195 us                                                      | 204 us: 1.04x slower                                                       |
| django_template            | 22.9 ms                                                     | 23.9 ms: 1.04x slower                                                      |
| sympy_expand               | 284 ms                                                      | 296 ms: 1.04x slower                                                       |
| telco                      | 4.13 ms                                                     | 4.37 ms: 1.06x slower                                                      |
| json_dumps                 | 5.70 ms                                                     | 6.27 ms: 1.10x slower                                                      |
| typing_runtime_protocols   | 95.1 us                                                     | 106 us: 1.11x slower                                                       |
| coverage                   | 40.8 ms                                                     | 47.9 ms: 1.17x slower                                                      |
| python_startup_no_site     | 16.2 ms                                                     | 19.5 ms: 1.20x slower                                                      |
| python_startup             | 19.5 ms                                                     | 26.0 ms: 1.34x slower                                                      |
| gc_traversal               | 1.52 ms                                                     | 2.15 ms: 1.41x slower                                                      |
| create_gc_cycles           | 752 us                                                      | 1.33 ms: 1.76x slower                                                      |
| logging_silent             | 60.5 ns                                                     | 316 ns: 5.23x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.08x faster                                                               |

Benchmark hidden because not significant (5): docutils, scimark_lu, pycparser, hexiom, json
Ignored benchmarks (21) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (17) of results/bm-20250610-3.15.0a0-0f866cb-JIT/bm-20250610-pythonperf1-amd64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.110x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: unknown
# Results vs. 3.12.0

- fork: python
- ref: 0f866cbfefd797b4dae2
- machine: windows-amd64
- commit hash: 0f866cb
- commit date: 2025-06-10
- overall geometric mean: 1.104x faster
- HPT reliability: 99.99%
- HPT 99th percentile: 1.02x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250610-pythonperf1-amd64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 220 ms: 1.01x slower                                                       |
| docutils       | 1.66 sec                                                    | 1.68 sec: 1.01x slower                                                     |
| Geometric mean | (ref)                                                       | 1.01x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250610-pythonperf1-amd64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 391 ms: 1.97x faster                                                       |
| async_tree_io              | 731 ms                                                      | 396 ms: 1.85x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 211 ms: 1.74x faster                                                       |
| async_tree_none            | 291 ms                                                      | 169 ms: 1.72x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 168 ms: 1.70x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 206 ms: 1.65x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 331 ms: 1.48x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 345 ms: 1.46x faster                                                       |
| Geometric mean             | (ref)                                                       | 1.69x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250610-pythonperf1-amd64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 43.8 ms: 1.30x faster                                                      |
| nbody          | 71.9 ms                                                     | 57.7 ms: 1.25x faster                                                      |
| pidigits       | 152 ms                                                      | 149 ms: 1.02x faster                                                       |
| Geometric mean | (ref)                                                       | 1.18x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250610-pythonperf1-amd64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 87.5 ms                                                     | 78.8 ms: 1.11x faster                                                      |
| regex_dna      | 126 ms                                                      | 120 ms: 1.05x faster                                                       |
| regex_effbot   | 1.62 ms                                                     | 1.63 ms: 1.01x slower                                                      |
| Geometric mean | (ref)                                                       | 1.04x faster                                                               |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250610-pythonperf1-amd64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| tomli_loads          | 1.37 sec                                                    | 1.16 sec: 1.18x faster                                                     |
| unpickle_pure_python | 133 us                                                      | 114 us: 1.16x faster                                                       |
| xml_etree_generate   | 55.8 ms                                                     | 52.2 ms: 1.07x faster                                                      |
| xml_etree_parse      | 93.0 ms                                                     | 87.5 ms: 1.06x faster                                                      |
| xml_etree_process    | 37.7 ms                                                     | 36.7 ms: 1.03x faster                                                      |
| json_loads           | 13.9 us                                                     | 14.6 us: 1.05x slower                                                      |
| pickle_pure_python   | 195 us                                                      | 206 us: 1.06x slower                                                       |
| json_dumps           | 5.70 ms                                                     | 6.32 ms: 1.11x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.03x faster                                                               |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250610-pythonperf1-amd64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 19.2 ms: 1.18x slower                                                      |
| python_startup         | 19.5 ms                                                     | 25.8 ms: 1.33x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.25x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250610-pythonperf1-amd64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 5.42 ms: 1.31x faster                                                      |
| django_template | 22.9 ms                                                     | 24.2 ms: 1.06x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.11x faster                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250610-pythonperf1-amd64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pathlib                    | 80.5 ms                                                     | 31.7 ms: 2.54x faster                                                      |
| async_tree_io_tg           | 771 ms                                                      | 391 ms: 1.97x faster                                                       |
| async_tree_io              | 731 ms                                                      | 396 ms: 1.85x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 211 ms: 1.74x faster                                                       |
| async_tree_none            | 291 ms                                                      | 169 ms: 1.72x faster                                                       |
| mdp                        | 1.37 sec                                                    | 802 ms: 1.71x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 168 ms: 1.70x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 206 ms: 1.65x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 331 ms: 1.48x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 345 ms: 1.46x faster                                                       |
| deepcopy                   | 238 us                                                      | 167 us: 1.42x faster                                                       |
| deepcopy_memo              | 23.7 us                                                     | 17.8 us: 1.34x faster                                                      |
| mako                       | 7.09 ms                                                     | 5.42 ms: 1.31x faster                                                      |
| float                      | 56.8 ms                                                     | 43.8 ms: 1.30x faster                                                      |
| comprehensions             | 14.1 us                                                     | 10.9 us: 1.30x faster                                                      |
| nbody                      | 71.9 ms                                                     | 57.7 ms: 1.25x faster                                                      |
| tomli_loads                | 1.37 sec                                                    | 1.16 sec: 1.18x faster                                                     |
| go                         | 91.6 ms                                                     | 78.0 ms: 1.17x faster                                                      |
| unpickle_pure_python       | 133 us                                                      | 114 us: 1.16x faster                                                       |
| scimark_fft                | 184 ms                                                      | 160 ms: 1.15x faster                                                       |
| deepcopy_reduce            | 2.09 us                                                     | 1.81 us: 1.15x faster                                                      |
| sqlite_synth               | 1.76 us                                                     | 1.56 us: 1.13x faster                                                      |
| generators                 | 22.5 ms                                                     | 20.0 ms: 1.13x faster                                                      |
| pyflate                    | 295 ms                                                      | 264 ms: 1.12x faster                                                       |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.30 ms: 1.11x faster                                                      |
| regex_compile              | 87.5 ms                                                     | 78.8 ms: 1.11x faster                                                      |
| chaos                      | 43.3 ms                                                     | 39.5 ms: 1.10x faster                                                      |
| spectral_norm              | 66.9 ms                                                     | 61.5 ms: 1.09x faster                                                      |
| dulwich_log                | 44.3 ms                                                     | 41.3 ms: 1.07x faster                                                      |
| xml_etree_generate         | 55.8 ms                                                     | 52.2 ms: 1.07x faster                                                      |
| xml_etree_parse            | 93.0 ms                                                     | 87.5 ms: 1.06x faster                                                      |
| raytrace                   | 192 ms                                                      | 181 ms: 1.06x faster                                                       |
| nqueens                    | 62.8 ms                                                     | 59.2 ms: 1.06x faster                                                      |
| regex_dna                  | 126 ms                                                      | 120 ms: 1.05x faster                                                       |
| sympy_sum                  | 91.5 ms                                                     | 87.3 ms: 1.05x faster                                                      |
| crypto_pyaes               | 48.5 ms                                                     | 46.9 ms: 1.03x faster                                                      |
| scimark_monte_carlo        | 43.7 ms                                                     | 42.4 ms: 1.03x faster                                                      |
| sympy_str                  | 175 ms                                                      | 170 ms: 1.03x faster                                                       |
| xml_etree_process          | 37.7 ms                                                     | 36.7 ms: 1.03x faster                                                      |
| sympy_integrate            | 13.0 ms                                                     | 12.6 ms: 1.03x faster                                                      |
| fannkuch                   | 247 ms                                                      | 241 ms: 1.03x faster                                                       |
| scimark_sor                | 78.8 ms                                                     | 77.1 ms: 1.02x faster                                                      |
| pidigits                   | 152 ms                                                      | 149 ms: 1.02x faster                                                       |
| meteor_contest             | 74.6 ms                                                     | 73.3 ms: 1.02x faster                                                      |
| coroutines                 | 14.3 ms                                                     | 14.1 ms: 1.01x faster                                                      |
| richards_super             | 32.1 ms                                                     | 31.6 ms: 1.01x faster                                                      |
| richards                   | 28.4 ms                                                     | 28.1 ms: 1.01x faster                                                      |
| regex_effbot               | 1.62 ms                                                     | 1.63 ms: 1.01x slower                                                      |
| logging_simple             | 6.28 us                                                     | 6.32 us: 1.01x slower                                                      |
| docutils                   | 1.66 sec                                                    | 1.68 sec: 1.01x slower                                                     |
| async_generators           | 239 ms                                                      | 242 ms: 1.01x slower                                                       |
| 2to3                       | 218 ms                                                      | 220 ms: 1.01x slower                                                       |
| pprint_safe_repr           | 513 ms                                                      | 520 ms: 1.01x slower                                                       |
| json                       | 3.05 ms                                                     | 3.11 ms: 1.02x slower                                                      |
| pprint_pformat             | 1.05 sec                                                    | 1.07 sec: 1.02x slower                                                     |
| hexiom                     | 4.10 ms                                                     | 4.21 ms: 1.03x slower                                                      |
| scimark_lu                 | 58.9 ms                                                     | 60.5 ms: 1.03x slower                                                      |
| sympy_expand               | 284 ms                                                      | 295 ms: 1.04x slower                                                       |
| deltablue                  | 2.16 ms                                                     | 2.26 ms: 1.05x slower                                                      |
| json_loads                 | 13.9 us                                                     | 14.6 us: 1.05x slower                                                      |
| telco                      | 4.13 ms                                                     | 4.36 ms: 1.05x slower                                                      |
| django_template            | 22.9 ms                                                     | 24.2 ms: 1.06x slower                                                      |
| pickle_pure_python         | 195 us                                                      | 206 us: 1.06x slower                                                       |
| typing_runtime_protocols   | 95.1 us                                                     | 104 us: 1.10x slower                                                       |
| json_dumps                 | 5.70 ms                                                     | 6.32 ms: 1.11x slower                                                      |
| python_startup_no_site     | 16.2 ms                                                     | 19.2 ms: 1.18x slower                                                      |
| coverage                   | 40.8 ms                                                     | 50.5 ms: 1.24x slower                                                      |
| python_startup             | 19.5 ms                                                     | 25.8 ms: 1.33x slower                                                      |
| gc_traversal               | 1.52 ms                                                     | 2.14 ms: 1.41x slower                                                      |
| create_gc_cycles           | 752 us                                                      | 1.34 ms: 1.78x slower                                                      |
| logging_silent             | 60.5 ns                                                     | 322 ns: 5.32x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.08x faster                                                               |

Benchmark hidden because not significant (4): xml_etree_iterparse, regex_v8, pycparser, logging_format
Ignored benchmarks (21) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (17) of results/bm-20250610-3.15.0a0-0f866cb-JIT/bm-20250610-pythonperf1-amd64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.104x faster

# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: unknown
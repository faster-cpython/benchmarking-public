# Results vs. 3.12.0

- fork: python
- ref: afc5ab6cce9d7095b99c
- machine: windows-amd64
- commit hash: afc5ab6
- commit date: 2025-06-13
- overall geometric mean: 1.062x faster
- HPT reliability: 99.95%
- HPT 99th percentile: 1.01x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250613-pythonperf1-amd64-python-afc5ab6cce9d7095b99c-3.15.0a0-afc5ab6 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 221 ms: 1.01x slower                                                       |
| docutils       | 1.66 sec                                                    | 1.63 sec: 1.02x faster                                                     |
| Geometric mean | (ref)                                                       | 1.00x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250613-pythonperf1-amd64-python-afc5ab6cce9d7095b99c-3.15.0a0-afc5ab6 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 392 ms: 1.97x faster                                                       |
| async_tree_io              | 731 ms                                                      | 403 ms: 1.81x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 212 ms: 1.73x faster                                                       |
| async_tree_none            | 291 ms                                                      | 172 ms: 1.69x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 170 ms: 1.68x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 210 ms: 1.62x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 331 ms: 1.48x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 343 ms: 1.46x faster                                                       |
| Geometric mean             | (ref)                                                       | 1.67x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250613-pythonperf1-amd64-python-afc5ab6cce9d7095b99c-3.15.0a0-afc5ab6 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 44.5 ms: 1.28x faster                                                      |
| nbody          | 71.9 ms                                                     | 67.5 ms: 1.07x faster                                                      |
| pidigits       | 152 ms                                                      | 149 ms: 1.02x faster                                                       |
| Geometric mean | (ref)                                                       | 1.12x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250613-pythonperf1-amd64-python-afc5ab6cce9d7095b99c-3.15.0a0-afc5ab6 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_effbot   | 1.62 ms                                                     | 1.47 ms: 1.10x faster                                                      |
| regex_compile  | 87.5 ms                                                     | 80.6 ms: 1.09x faster                                                      |
| regex_dna      | 126 ms                                                      | 117 ms: 1.08x faster                                                       |
| regex_v8       | 14.2 ms                                                     | 13.5 ms: 1.06x faster                                                      |
| Geometric mean | (ref)                                                       | 1.08x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250613-pythonperf1-amd64-python-afc5ab6cce9d7095b99c-3.15.0a0-afc5ab6 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| xml_etree_parse      | 93.0 ms                                                     | 88.3 ms: 1.05x faster                                                      |
| xml_etree_generate   | 55.8 ms                                                     | 56.4 ms: 1.01x slower                                                      |
| tomli_loads          | 1.37 sec                                                    | 1.39 sec: 1.01x slower                                                     |
| unpickle_pure_python | 133 us                                                      | 136 us: 1.02x slower                                                       |
| json_loads           | 13.9 us                                                     | 14.3 us: 1.03x slower                                                      |
| xml_etree_process    | 37.7 ms                                                     | 39.3 ms: 1.04x slower                                                      |
| json_dumps           | 5.70 ms                                                     | 6.27 ms: 1.10x slower                                                      |
| pickle_pure_python   | 195 us                                                      | 216 us: 1.11x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.03x slower                                                               |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250613-pythonperf1-amd64-python-afc5ab6cce9d7095b99c-3.15.0a0-afc5ab6 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 19.3 ms: 1.19x slower                                                      |
| python_startup         | 19.5 ms                                                     | 26.2 ms: 1.35x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.26x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250613-pythonperf1-amd64-python-afc5ab6cce9d7095b99c-3.15.0a0-afc5ab6 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 6.64 ms: 1.07x faster                                                      |
| django_template | 22.9 ms                                                     | 23.9 ms: 1.04x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.01x faster                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250613-pythonperf1-amd64-python-afc5ab6cce9d7095b99c-3.15.0a0-afc5ab6 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pathlib                    | 80.5 ms                                                     | 31.3 ms: 2.57x faster                                                      |
| async_tree_io_tg           | 771 ms                                                      | 392 ms: 1.97x faster                                                       |
| async_tree_io              | 731 ms                                                      | 403 ms: 1.81x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 212 ms: 1.73x faster                                                       |
| mdp                        | 1.37 sec                                                    | 805 ms: 1.70x faster                                                       |
| async_tree_none            | 291 ms                                                      | 172 ms: 1.69x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 170 ms: 1.68x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 210 ms: 1.62x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 331 ms: 1.48x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 343 ms: 1.46x faster                                                       |
| deepcopy                   | 238 us                                                      | 174 us: 1.37x faster                                                       |
| comprehensions             | 14.1 us                                                     | 10.7 us: 1.33x faster                                                      |
| deepcopy_memo              | 23.7 us                                                     | 18.4 us: 1.29x faster                                                      |
| float                      | 56.8 ms                                                     | 44.5 ms: 1.28x faster                                                      |
| go                         | 91.6 ms                                                     | 76.8 ms: 1.19x faster                                                      |
| generators                 | 22.5 ms                                                     | 19.4 ms: 1.16x faster                                                      |
| spectral_norm              | 66.9 ms                                                     | 58.1 ms: 1.15x faster                                                      |
| deepcopy_reduce            | 2.09 us                                                     | 1.84 us: 1.14x faster                                                      |
| sqlite_synth               | 1.76 us                                                     | 1.58 us: 1.11x faster                                                      |
| regex_effbot               | 1.62 ms                                                     | 1.47 ms: 1.10x faster                                                      |
| chaos                      | 43.3 ms                                                     | 39.5 ms: 1.10x faster                                                      |
| regex_compile              | 87.5 ms                                                     | 80.6 ms: 1.09x faster                                                      |
| dulwich_log                | 44.3 ms                                                     | 40.9 ms: 1.08x faster                                                      |
| regex_dna                  | 126 ms                                                      | 117 ms: 1.08x faster                                                       |
| raytrace                   | 192 ms                                                      | 180 ms: 1.07x faster                                                       |
| mako                       | 7.09 ms                                                     | 6.64 ms: 1.07x faster                                                      |
| nbody                      | 71.9 ms                                                     | 67.5 ms: 1.07x faster                                                      |
| regex_v8                   | 14.2 ms                                                     | 13.5 ms: 1.06x faster                                                      |
| nqueens                    | 62.8 ms                                                     | 59.5 ms: 1.05x faster                                                      |
| xml_etree_parse            | 93.0 ms                                                     | 88.3 ms: 1.05x faster                                                      |
| sympy_integrate            | 13.0 ms                                                     | 12.4 ms: 1.04x faster                                                      |
| sympy_sum                  | 91.5 ms                                                     | 87.7 ms: 1.04x faster                                                      |
| scimark_monte_carlo        | 43.7 ms                                                     | 42.1 ms: 1.04x faster                                                      |
| sympy_str                  | 175 ms                                                      | 169 ms: 1.04x faster                                                       |
| coroutines                 | 14.3 ms                                                     | 13.8 ms: 1.03x faster                                                      |
| meteor_contest             | 74.6 ms                                                     | 72.7 ms: 1.03x faster                                                      |
| pidigits                   | 152 ms                                                      | 149 ms: 1.02x faster                                                       |
| async_generators           | 239 ms                                                      | 234 ms: 1.02x faster                                                       |
| scimark_sor                | 78.8 ms                                                     | 77.1 ms: 1.02x faster                                                      |
| crypto_pyaes               | 48.5 ms                                                     | 47.6 ms: 1.02x faster                                                      |
| docutils                   | 1.66 sec                                                    | 1.63 sec: 1.02x faster                                                     |
| richards                   | 28.4 ms                                                     | 27.9 ms: 1.02x faster                                                      |
| logging_format             | 6.72 us                                                     | 6.60 us: 1.02x faster                                                      |
| pyflate                    | 295 ms                                                      | 290 ms: 1.02x faster                                                       |
| scimark_fft                | 184 ms                                                      | 182 ms: 1.01x faster                                                       |
| richards_super             | 32.1 ms                                                     | 31.7 ms: 1.01x faster                                                      |
| logging_simple             | 6.28 us                                                     | 6.20 us: 1.01x faster                                                      |
| sympy_expand               | 284 ms                                                      | 285 ms: 1.01x slower                                                       |
| xml_etree_generate         | 55.8 ms                                                     | 56.4 ms: 1.01x slower                                                      |
| scimark_lu                 | 58.9 ms                                                     | 59.6 ms: 1.01x slower                                                      |
| 2to3                       | 218 ms                                                      | 221 ms: 1.01x slower                                                       |
| tomli_loads                | 1.37 sec                                                    | 1.39 sec: 1.01x slower                                                     |
| pycparser                  | 699 ms                                                      | 709 ms: 1.01x slower                                                       |
| unpickle_pure_python       | 133 us                                                      | 136 us: 1.02x slower                                                       |
| json_loads                 | 13.9 us                                                     | 14.3 us: 1.03x slower                                                      |
| fannkuch                   | 247 ms                                                      | 253 ms: 1.03x slower                                                       |
| deltablue                  | 2.16 ms                                                     | 2.22 ms: 1.03x slower                                                      |
| xml_etree_process          | 37.7 ms                                                     | 39.3 ms: 1.04x slower                                                      |
| django_template            | 22.9 ms                                                     | 23.9 ms: 1.04x slower                                                      |
| pprint_safe_repr           | 513 ms                                                      | 553 ms: 1.08x slower                                                       |
| pprint_pformat             | 1.05 sec                                                    | 1.13 sec: 1.08x slower                                                     |
| typing_runtime_protocols   | 95.1 us                                                     | 104 us: 1.10x slower                                                       |
| json_dumps                 | 5.70 ms                                                     | 6.27 ms: 1.10x slower                                                      |
| pickle_pure_python         | 195 us                                                      | 216 us: 1.11x slower                                                       |
| telco                      | 4.13 ms                                                     | 4.67 ms: 1.13x slower                                                      |
| python_startup_no_site     | 16.2 ms                                                     | 19.3 ms: 1.19x slower                                                      |
| python_startup             | 19.5 ms                                                     | 26.2 ms: 1.35x slower                                                      |
| gc_traversal               | 1.52 ms                                                     | 2.16 ms: 1.42x slower                                                      |
| create_gc_cycles           | 752 us                                                      | 1.32 ms: 1.76x slower                                                      |
| logging_silent             | 60.5 ns                                                     | 322 ns: 5.32x slower                                                       |
| coverage                   | 40.8 ms                                                     | 296 ms: 7.24x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.04x faster                                                               |

Benchmark hidden because not significant (4): xml_etree_iterparse, hexiom, scimark_sparse_mat_mult, json
Ignored benchmarks (21) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (17) of results/bm-20250613-3.15.0a0-afc5ab6/bm-20250613-pythonperf1-amd64-python-afc5ab6cce9d7095b99c-3.15.0a0-afc5ab6.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.062x faster

# HPT report

- Reliability score: 99.95% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: unknown
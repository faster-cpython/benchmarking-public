# Results vs. 3.12.0

- fork: python
- ref: a4625d597f9fc2d083fb
- machine: windows-amd64
- commit hash: a4625d5
- commit date: 2025-06-26
- overall geometric mean: 1.085x faster
- HPT reliability: 99.94%
- HPT 99th percentile: 1.01x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250626-pythonperf1-amd64-python-a4625d597f9fc2d083fb-3.15.0a0-a4625d5 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 221 ms: 1.02x slower                                                       |
| docutils       | 1.66 sec                                                    | 1.62 sec: 1.02x faster                                                     |
| Geometric mean | (ref)                                                       | 1.00x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250626-pythonperf1-amd64-python-a4625d597f9fc2d083fb-3.15.0a0-a4625d5 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 398 ms: 1.94x faster                                                       |
| async_tree_io              | 731 ms                                                      | 401 ms: 1.82x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 213 ms: 1.72x faster                                                       |
| async_tree_none            | 291 ms                                                      | 173 ms: 1.69x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 170 ms: 1.67x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 210 ms: 1.62x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 333 ms: 1.47x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 345 ms: 1.45x faster                                                       |
| Geometric mean             | (ref)                                                       | 1.67x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250626-pythonperf1-amd64-python-a4625d597f9fc2d083fb-3.15.0a0-a4625d5 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 44.0 ms: 1.29x faster                                                      |
| nbody          | 71.9 ms                                                     | 65.4 ms: 1.10x faster                                                      |
| pidigits       | 152 ms                                                      | 147 ms: 1.04x faster                                                       |
| Geometric mean | (ref)                                                       | 1.14x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250626-pythonperf1-amd64-python-a4625d597f9fc2d083fb-3.15.0a0-a4625d5 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 87.5 ms                                                     | 80.6 ms: 1.09x faster                                                      |
| regex_effbot   | 1.62 ms                                                     | 1.51 ms: 1.07x faster                                                      |
| regex_dna      | 126 ms                                                      | 120 ms: 1.05x faster                                                       |
| Geometric mean | (ref)                                                       | 1.05x faster                                                               |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250626-pythonperf1-amd64-python-a4625d597f9fc2d083fb-3.15.0a0-a4625d5 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| xml_etree_parse      | 93.0 ms                                                     | 88.8 ms: 1.05x faster                                                      |
| unpickle_pure_python | 133 us                                                      | 134 us: 1.00x slower                                                       |
| xml_etree_generate   | 55.8 ms                                                     | 56.4 ms: 1.01x slower                                                      |
| xml_etree_process    | 37.7 ms                                                     | 38.9 ms: 1.03x slower                                                      |
| json_loads           | 13.9 us                                                     | 14.4 us: 1.04x slower                                                      |
| tomli_loads          | 1.37 sec                                                    | 1.42 sec: 1.04x slower                                                     |
| pickle_pure_python   | 195 us                                                      | 213 us: 1.09x slower                                                       |
| json_dumps           | 5.70 ms                                                     | 6.35 ms: 1.12x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.03x slower                                                               |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250626-pythonperf1-amd64-python-a4625d597f9fc2d083fb-3.15.0a0-a4625d5 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 19.5 ms: 1.20x slower                                                      |
| python_startup         | 19.5 ms                                                     | 25.9 ms: 1.33x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.26x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250626-pythonperf1-amd64-python-a4625d597f9fc2d083fb-3.15.0a0-a4625d5 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 6.72 ms: 1.06x faster                                                      |
| django_template | 22.9 ms                                                     | 24.5 ms: 1.07x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.01x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250626-pythonperf1-amd64-python-a4625d597f9fc2d083fb-3.15.0a0-a4625d5 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pathlib                    | 80.5 ms                                                     | 31.8 ms: 2.53x faster                                                      |
| async_tree_io_tg           | 771 ms                                                      | 398 ms: 1.94x faster                                                       |
| async_tree_io              | 731 ms                                                      | 401 ms: 1.82x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 213 ms: 1.72x faster                                                       |
| mdp                        | 1.37 sec                                                    | 800 ms: 1.71x faster                                                       |
| async_tree_none            | 291 ms                                                      | 173 ms: 1.69x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 170 ms: 1.67x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 210 ms: 1.62x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 333 ms: 1.47x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 345 ms: 1.45x faster                                                       |
| deepcopy                   | 238 us                                                      | 169 us: 1.41x faster                                                       |
| comprehensions             | 14.1 us                                                     | 10.8 us: 1.31x faster                                                      |
| float                      | 56.8 ms                                                     | 44.0 ms: 1.29x faster                                                      |
| deepcopy_memo              | 23.7 us                                                     | 18.5 us: 1.28x faster                                                      |
| go                         | 91.6 ms                                                     | 77.6 ms: 1.18x faster                                                      |
| generators                 | 22.5 ms                                                     | 19.2 ms: 1.17x faster                                                      |
| deepcopy_reduce            | 2.09 us                                                     | 1.80 us: 1.16x faster                                                      |
| sqlite_synth               | 1.76 us                                                     | 1.60 us: 1.10x faster                                                      |
| nbody                      | 71.9 ms                                                     | 65.4 ms: 1.10x faster                                                      |
| regex_compile              | 87.5 ms                                                     | 80.6 ms: 1.09x faster                                                      |
| dulwich_log                | 44.3 ms                                                     | 41.2 ms: 1.08x faster                                                      |
| raytrace                   | 192 ms                                                      | 179 ms: 1.07x faster                                                       |
| scimark_monte_carlo        | 43.7 ms                                                     | 40.8 ms: 1.07x faster                                                      |
| regex_effbot               | 1.62 ms                                                     | 1.51 ms: 1.07x faster                                                      |
| mako                       | 7.09 ms                                                     | 6.72 ms: 1.06x faster                                                      |
| chaos                      | 43.3 ms                                                     | 41.1 ms: 1.05x faster                                                      |
| logging_silent             | 60.5 ns                                                     | 57.6 ns: 1.05x faster                                                      |
| regex_dna                  | 126 ms                                                      | 120 ms: 1.05x faster                                                       |
| sympy_sum                  | 91.5 ms                                                     | 87.3 ms: 1.05x faster                                                      |
| xml_etree_parse            | 93.0 ms                                                     | 88.8 ms: 1.05x faster                                                      |
| pprint_safe_repr           | 513 ms                                                      | 492 ms: 1.04x faster                                                       |
| richards                   | 28.4 ms                                                     | 27.3 ms: 1.04x faster                                                      |
| meteor_contest             | 74.6 ms                                                     | 71.9 ms: 1.04x faster                                                      |
| pidigits                   | 152 ms                                                      | 147 ms: 1.04x faster                                                       |
| pprint_pformat             | 1.05 sec                                                    | 1.01 sec: 1.03x faster                                                     |
| spectral_norm              | 66.9 ms                                                     | 64.9 ms: 1.03x faster                                                      |
| sympy_str                  | 175 ms                                                      | 170 ms: 1.03x faster                                                       |
| sympy_integrate            | 13.0 ms                                                     | 12.6 ms: 1.03x faster                                                      |
| richards_super             | 32.1 ms                                                     | 31.2 ms: 1.03x faster                                                      |
| logging_simple             | 6.28 us                                                     | 6.13 us: 1.02x faster                                                      |
| logging_format             | 6.72 us                                                     | 6.56 us: 1.02x faster                                                      |
| docutils                   | 1.66 sec                                                    | 1.62 sec: 1.02x faster                                                     |
| nqueens                    | 62.8 ms                                                     | 61.6 ms: 1.02x faster                                                      |
| crypto_pyaes               | 48.5 ms                                                     | 47.6 ms: 1.02x faster                                                      |
| async_generators           | 239 ms                                                      | 236 ms: 1.01x faster                                                       |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.53 ms: 1.01x faster                                                      |
| unpickle_pure_python       | 133 us                                                      | 134 us: 1.00x slower                                                       |
| xml_etree_generate         | 55.8 ms                                                     | 56.4 ms: 1.01x slower                                                      |
| deltablue                  | 2.16 ms                                                     | 2.19 ms: 1.02x slower                                                      |
| 2to3                       | 218 ms                                                      | 221 ms: 1.02x slower                                                       |
| scimark_lu                 | 58.9 ms                                                     | 60.0 ms: 1.02x slower                                                      |
| scimark_fft                | 184 ms                                                      | 190 ms: 1.03x slower                                                       |
| sympy_expand               | 284 ms                                                      | 292 ms: 1.03x slower                                                       |
| xml_etree_process          | 37.7 ms                                                     | 38.9 ms: 1.03x slower                                                      |
| json_loads                 | 13.9 us                                                     | 14.4 us: 1.04x slower                                                      |
| tomli_loads                | 1.37 sec                                                    | 1.42 sec: 1.04x slower                                                     |
| coroutines                 | 14.3 ms                                                     | 14.8 ms: 1.04x slower                                                      |
| fannkuch                   | 247 ms                                                      | 261 ms: 1.06x slower                                                       |
| django_template            | 22.9 ms                                                     | 24.5 ms: 1.07x slower                                                      |
| typing_runtime_protocols   | 95.1 us                                                     | 102 us: 1.07x slower                                                       |
| pickle_pure_python         | 195 us                                                      | 213 us: 1.09x slower                                                       |
| telco                      | 4.13 ms                                                     | 4.60 ms: 1.11x slower                                                      |
| json_dumps                 | 5.70 ms                                                     | 6.35 ms: 1.12x slower                                                      |
| python_startup_no_site     | 16.2 ms                                                     | 19.5 ms: 1.20x slower                                                      |
| coverage                   | 40.8 ms                                                     | 51.6 ms: 1.27x slower                                                      |
| python_startup             | 19.5 ms                                                     | 25.9 ms: 1.33x slower                                                      |
| gc_traversal               | 1.52 ms                                                     | 2.11 ms: 1.38x slower                                                      |
| create_gc_cycles           | 752 us                                                      | 1.31 ms: 1.75x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.09x faster                                                               |

Benchmark hidden because not significant (7): xml_etree_iterparse, pyflate, json, hexiom, pycparser, scimark_sor, regex_v8
Ignored benchmarks (21) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (17) of results/bm-20250626-3.15.0a0-a4625d5/bm-20250626-pythonperf1-amd64-python-a4625d597f9fc2d083fb-3.15.0a0-a4625d5.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.085x faster

# HPT report

- Reliability score: 99.94% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: unknown
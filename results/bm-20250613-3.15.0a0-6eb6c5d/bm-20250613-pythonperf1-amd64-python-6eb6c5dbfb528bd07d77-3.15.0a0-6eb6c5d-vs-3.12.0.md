# Results vs. 3.12.0

- fork: python
- ref: 6eb6c5dbfb528bd07d77
- machine: windows-amd64
- commit hash: 6eb6c5d
- commit date: 2025-06-13
- overall geometric mean: 1.054x faster
- HPT reliability: 99.68%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250613-pythonperf1-amd64-python-6eb6c5dbfb528bd07d77-3.15.0a0-6eb6c5d |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 223 ms: 1.02x slower                                                       |
| docutils       | 1.66 sec                                                    | 1.65 sec: 1.01x faster                                                     |
| Geometric mean | (ref)                                                       | 1.01x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250613-pythonperf1-amd64-python-6eb6c5dbfb528bd07d77-3.15.0a0-6eb6c5d |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 395 ms: 1.95x faster                                                       |
| async_tree_io              | 731 ms                                                      | 397 ms: 1.84x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 212 ms: 1.73x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 170 ms: 1.68x faster                                                       |
| async_tree_none            | 291 ms                                                      | 179 ms: 1.63x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 210 ms: 1.62x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 341 ms: 1.47x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 334 ms: 1.46x faster                                                       |
| Geometric mean             | (ref)                                                       | 1.67x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250613-pythonperf1-amd64-python-6eb6c5dbfb528bd07d77-3.15.0a0-6eb6c5d |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 44.9 ms: 1.27x faster                                                      |
| nbody          | 71.9 ms                                                     | 65.2 ms: 1.10x faster                                                      |
| pidigits       | 152 ms                                                      | 149 ms: 1.02x faster                                                       |
| Geometric mean | (ref)                                                       | 1.13x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250613-pythonperf1-amd64-python-6eb6c5dbfb528bd07d77-3.15.0a0-6eb6c5d |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 87.5 ms                                                     | 80.2 ms: 1.09x faster                                                      |
| regex_dna      | 126 ms                                                      | 119 ms: 1.06x faster                                                       |
| regex_effbot   | 1.62 ms                                                     | 1.53 ms: 1.05x faster                                                      |
| regex_v8       | 14.2 ms                                                     | 14.0 ms: 1.02x faster                                                      |
| Geometric mean | (ref)                                                       | 1.05x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250613-pythonperf1-amd64-python-6eb6c5dbfb528bd07d77-3.15.0a0-6eb6c5d |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| xml_etree_parse      | 93.0 ms                                                     | 89.3 ms: 1.04x faster                                                      |
| xml_etree_generate   | 55.8 ms                                                     | 56.7 ms: 1.02x slower                                                      |
| tomli_loads          | 1.37 sec                                                    | 1.39 sec: 1.02x slower                                                     |
| json_loads           | 13.9 us                                                     | 14.2 us: 1.02x slower                                                      |
| unpickle_pure_python | 133 us                                                      | 137 us: 1.03x slower                                                       |
| xml_etree_process    | 37.7 ms                                                     | 39.6 ms: 1.05x slower                                                      |
| pickle_pure_python   | 195 us                                                      | 214 us: 1.10x slower                                                       |
| json_dumps           | 5.70 ms                                                     | 6.26 ms: 1.10x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.03x slower                                                               |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250613-pythonperf1-amd64-python-6eb6c5dbfb528bd07d77-3.15.0a0-6eb6c5d |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 19.3 ms: 1.19x slower                                                      |
| python_startup         | 19.5 ms                                                     | 26.0 ms: 1.34x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.26x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250613-pythonperf1-amd64-python-6eb6c5dbfb528bd07d77-3.15.0a0-6eb6c5d |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 6.65 ms: 1.07x faster                                                      |
| django_template | 22.9 ms                                                     | 24.4 ms: 1.07x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.00x faster                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250613-pythonperf1-amd64-python-6eb6c5dbfb528bd07d77-3.15.0a0-6eb6c5d |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pathlib                    | 80.5 ms                                                     | 32.0 ms: 2.51x faster                                                      |
| async_tree_io_tg           | 771 ms                                                      | 395 ms: 1.95x faster                                                       |
| async_tree_io              | 731 ms                                                      | 397 ms: 1.84x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 212 ms: 1.73x faster                                                       |
| mdp                        | 1.37 sec                                                    | 808 ms: 1.70x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 170 ms: 1.68x faster                                                       |
| async_tree_none            | 291 ms                                                      | 179 ms: 1.63x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 210 ms: 1.62x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 341 ms: 1.47x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 334 ms: 1.46x faster                                                       |
| deepcopy                   | 238 us                                                      | 171 us: 1.39x faster                                                       |
| deepcopy_memo              | 23.7 us                                                     | 18.4 us: 1.29x faster                                                      |
| comprehensions             | 14.1 us                                                     | 11.0 us: 1.29x faster                                                      |
| float                      | 56.8 ms                                                     | 44.9 ms: 1.27x faster                                                      |
| go                         | 91.6 ms                                                     | 77.5 ms: 1.18x faster                                                      |
| deepcopy_reduce            | 2.09 us                                                     | 1.83 us: 1.15x faster                                                      |
| generators                 | 22.5 ms                                                     | 19.9 ms: 1.13x faster                                                      |
| spectral_norm              | 66.9 ms                                                     | 59.2 ms: 1.13x faster                                                      |
| sqlite_synth               | 1.76 us                                                     | 1.59 us: 1.10x faster                                                      |
| nbody                      | 71.9 ms                                                     | 65.2 ms: 1.10x faster                                                      |
| regex_compile              | 87.5 ms                                                     | 80.2 ms: 1.09x faster                                                      |
| chaos                      | 43.3 ms                                                     | 39.9 ms: 1.09x faster                                                      |
| scimark_monte_carlo        | 43.7 ms                                                     | 40.4 ms: 1.08x faster                                                      |
| dulwich_log                | 44.3 ms                                                     | 41.1 ms: 1.08x faster                                                      |
| mako                       | 7.09 ms                                                     | 6.65 ms: 1.07x faster                                                      |
| regex_dna                  | 126 ms                                                      | 119 ms: 1.06x faster                                                       |
| regex_effbot               | 1.62 ms                                                     | 1.53 ms: 1.05x faster                                                      |
| raytrace                   | 192 ms                                                      | 184 ms: 1.05x faster                                                       |
| xml_etree_parse            | 93.0 ms                                                     | 89.3 ms: 1.04x faster                                                      |
| async_generators           | 239 ms                                                      | 231 ms: 1.04x faster                                                       |
| sympy_sum                  | 91.5 ms                                                     | 88.3 ms: 1.04x faster                                                      |
| scimark_sor                | 78.8 ms                                                     | 76.1 ms: 1.04x faster                                                      |
| sympy_integrate            | 13.0 ms                                                     | 12.5 ms: 1.03x faster                                                      |
| crypto_pyaes               | 48.5 ms                                                     | 47.0 ms: 1.03x faster                                                      |
| nqueens                    | 62.8 ms                                                     | 61.2 ms: 1.03x faster                                                      |
| meteor_contest             | 74.6 ms                                                     | 72.7 ms: 1.03x faster                                                      |
| richards                   | 28.4 ms                                                     | 27.7 ms: 1.02x faster                                                      |
| pidigits                   | 152 ms                                                      | 149 ms: 1.02x faster                                                       |
| richards_super             | 32.1 ms                                                     | 31.5 ms: 1.02x faster                                                      |
| sympy_str                  | 175 ms                                                      | 172 ms: 1.02x faster                                                       |
| pyflate                    | 295 ms                                                      | 289 ms: 1.02x faster                                                       |
| regex_v8                   | 14.2 ms                                                     | 14.0 ms: 1.02x faster                                                      |
| scimark_fft                | 184 ms                                                      | 182 ms: 1.01x faster                                                       |
| docutils                   | 1.66 sec                                                    | 1.65 sec: 1.01x faster                                                     |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.55 ms: 1.00x faster                                                      |
| scimark_lu                 | 58.9 ms                                                     | 59.5 ms: 1.01x slower                                                      |
| hexiom                     | 4.10 ms                                                     | 4.15 ms: 1.01x slower                                                      |
| xml_etree_generate         | 55.8 ms                                                     | 56.7 ms: 1.02x slower                                                      |
| tomli_loads                | 1.37 sec                                                    | 1.39 sec: 1.02x slower                                                     |
| 2to3                       | 218 ms                                                      | 223 ms: 1.02x slower                                                       |
| json_loads                 | 13.9 us                                                     | 14.2 us: 1.02x slower                                                      |
| coroutines                 | 14.3 ms                                                     | 14.6 ms: 1.02x slower                                                      |
| logging_simple             | 6.28 us                                                     | 6.46 us: 1.03x slower                                                      |
| logging_format             | 6.72 us                                                     | 6.91 us: 1.03x slower                                                      |
| unpickle_pure_python       | 133 us                                                      | 137 us: 1.03x slower                                                       |
| pycparser                  | 699 ms                                                      | 724 ms: 1.04x slower                                                       |
| sympy_expand               | 284 ms                                                      | 295 ms: 1.04x slower                                                       |
| deltablue                  | 2.16 ms                                                     | 2.26 ms: 1.04x slower                                                      |
| fannkuch                   | 247 ms                                                      | 258 ms: 1.05x slower                                                       |
| xml_etree_process          | 37.7 ms                                                     | 39.6 ms: 1.05x slower                                                      |
| django_template            | 22.9 ms                                                     | 24.4 ms: 1.07x slower                                                      |
| pprint_safe_repr           | 513 ms                                                      | 548 ms: 1.07x slower                                                       |
| pprint_pformat             | 1.05 sec                                                    | 1.12 sec: 1.07x slower                                                     |
| pickle_pure_python         | 195 us                                                      | 214 us: 1.10x slower                                                       |
| json_dumps                 | 5.70 ms                                                     | 6.26 ms: 1.10x slower                                                      |
| typing_runtime_protocols   | 95.1 us                                                     | 105 us: 1.10x slower                                                       |
| telco                      | 4.13 ms                                                     | 4.64 ms: 1.12x slower                                                      |
| python_startup_no_site     | 16.2 ms                                                     | 19.3 ms: 1.19x slower                                                      |
| python_startup             | 19.5 ms                                                     | 26.0 ms: 1.34x slower                                                      |
| gc_traversal               | 1.52 ms                                                     | 2.14 ms: 1.41x slower                                                      |
| create_gc_cycles           | 752 us                                                      | 1.32 ms: 1.76x slower                                                      |
| logging_silent             | 60.5 ns                                                     | 321 ns: 5.31x slower                                                       |
| coverage                   | 40.8 ms                                                     | 296 ms: 7.25x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.03x faster                                                               |

Benchmark hidden because not significant (2): json, xml_etree_iterparse
Ignored benchmarks (21) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (17) of results/bm-20250613-3.15.0a0-6eb6c5d/bm-20250613-pythonperf1-amd64-python-6eb6c5dbfb528bd07d77-3.15.0a0-6eb6c5d.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.054x faster

# HPT report

- Reliability score: 99.68% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown
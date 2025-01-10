# Results vs. 3.12.0

- fork: Fidget-Spinner
- ref: tail_call
- machine: windows-amd64
- commit hash: ac80cdd
- commit date: 2025-01-10
- overall geometric mean: 1.010x slower
- HPT reliability: 99.13%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250110-pythonperf1-amd64-Fidget%2dSpinner-tail_call-3.14.0a3+-ac80cdd |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 231 ms: 1.06x slower                                                       |
| docutils       | 1.66 sec                                                    | 1.71 sec: 1.03x slower                                                     |
| Geometric mean | (ref)                                                       | 1.04x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250110-pythonperf1-amd64-Fidget%2dSpinner-tail_call-3.14.0a3+-ac80cdd |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 412 ms: 1.87x faster                                                       |
| async_tree_io              | 731 ms                                                      | 421 ms: 1.74x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 216 ms: 1.70x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 177 ms: 1.61x faster                                                       |
| async_tree_none            | 291 ms                                                      | 189 ms: 1.54x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 233 ms: 1.46x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 350 ms: 1.44x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 354 ms: 1.38x faster                                                       |
| Geometric mean             | (ref)                                                       | 1.58x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250110-pythonperf1-amd64-Fidget%2dSpinner-tail_call-3.14.0a3+-ac80cdd |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 53.0 ms: 1.07x faster                                                      |
| pidigits       | 152 ms                                                      | 148 ms: 1.03x faster                                                       |
| nbody          | 71.9 ms                                                     | 79.7 ms: 1.11x slower                                                      |
| Geometric mean | (ref)                                                       | 1.00x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250110-pythonperf1-amd64-Fidget%2dSpinner-tail_call-3.14.0a3+-ac80cdd |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_effbot   | 1.62 ms                                                     | 1.48 ms: 1.09x faster                                                      |
| regex_dna      | 126 ms                                                      | 122 ms: 1.04x faster                                                       |
| regex_compile  | 87.5 ms                                                     | 89.7 ms: 1.02x slower                                                      |
| regex_v8       | 14.2 ms                                                     | 24.6 ms: 1.73x slower                                                      |
| Geometric mean | (ref)                                                       | 1.12x slower                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250110-pythonperf1-amd64-Fidget%2dSpinner-tail_call-3.14.0a3+-ac80cdd |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| xml_etree_parse      | 93.0 ms                                                     | 89.9 ms: 1.03x faster                                                      |
| xml_etree_iterparse  | 65.2 ms                                                     | 63.8 ms: 1.02x faster                                                      |
| xml_etree_generate   | 55.8 ms                                                     | 58.1 ms: 1.04x slower                                                      |
| json_loads           | 13.9 us                                                     | 14.8 us: 1.07x slower                                                      |
| tomli_loads          | 1.37 sec                                                    | 1.47 sec: 1.08x slower                                                     |
| xml_etree_process    | 37.7 ms                                                     | 41.5 ms: 1.10x slower                                                      |
| unpickle_pure_python | 133 us                                                      | 153 us: 1.15x slower                                                       |
| json_dumps           | 5.70 ms                                                     | 6.81 ms: 1.20x slower                                                      |
| pickle_pure_python   | 195 us                                                      | 234 us: 1.20x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.08x slower                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250110-pythonperf1-amd64-Fidget%2dSpinner-tail_call-3.14.0a3+-ac80cdd |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 18.1 ms: 1.12x slower                                                      |
| python_startup         | 19.5 ms                                                     | 24.6 ms: 1.26x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.19x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250110-pythonperf1-amd64-Fidget%2dSpinner-tail_call-3.14.0a3+-ac80cdd |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| django_template | 22.9 ms                                                     | 25.7 ms: 1.12x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.06x slower                                                               |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250110-pythonperf1-amd64-Fidget%2dSpinner-tail_call-3.14.0a3+-ac80cdd |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 412 ms: 1.87x faster                                                       |
| async_tree_io              | 731 ms                                                      | 421 ms: 1.74x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 216 ms: 1.70x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 177 ms: 1.61x faster                                                       |
| async_tree_none            | 291 ms                                                      | 189 ms: 1.54x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 233 ms: 1.46x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 350 ms: 1.44x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 354 ms: 1.38x faster                                                       |
| deepcopy                   | 238 us                                                      | 188 us: 1.27x faster                                                       |
| comprehensions             | 14.1 us                                                     | 12.7 us: 1.12x faster                                                      |
| regex_effbot               | 1.62 ms                                                     | 1.48 ms: 1.09x faster                                                      |
| deepcopy_reduce            | 2.09 us                                                     | 1.92 us: 1.09x faster                                                      |
| sqlite_synth               | 1.76 us                                                     | 1.61 us: 1.09x faster                                                      |
| deepcopy_memo              | 23.7 us                                                     | 21.9 us: 1.08x faster                                                      |
| float                      | 56.8 ms                                                     | 53.0 ms: 1.07x faster                                                      |
| coroutines                 | 14.3 ms                                                     | 13.5 ms: 1.06x faster                                                      |
| generators                 | 22.5 ms                                                     | 21.6 ms: 1.04x faster                                                      |
| regex_dna                  | 126 ms                                                      | 122 ms: 1.04x faster                                                       |
| xml_etree_parse            | 93.0 ms                                                     | 89.9 ms: 1.03x faster                                                      |
| pidigits                   | 152 ms                                                      | 148 ms: 1.03x faster                                                       |
| spectral_norm              | 66.9 ms                                                     | 65.1 ms: 1.03x faster                                                      |
| bench_thread_pool          | 857 us                                                      | 838 us: 1.02x faster                                                       |
| xml_etree_iterparse        | 65.2 ms                                                     | 63.8 ms: 1.02x faster                                                      |
| dulwich_log                | 44.3 ms                                                     | 43.4 ms: 1.02x faster                                                      |
| async_generators           | 239 ms                                                      | 236 ms: 1.01x faster                                                       |
| pathlib                    | 80.5 ms                                                     | 79.8 ms: 1.01x faster                                                      |
| regex_compile              | 87.5 ms                                                     | 89.7 ms: 1.02x slower                                                      |
| docutils                   | 1.66 sec                                                    | 1.71 sec: 1.03x slower                                                     |
| go                         | 91.6 ms                                                     | 94.3 ms: 1.03x slower                                                      |
| sympy_str                  | 175 ms                                                      | 181 ms: 1.03x slower                                                       |
| crypto_pyaes               | 48.5 ms                                                     | 50.0 ms: 1.03x slower                                                      |
| nqueens                    | 62.8 ms                                                     | 64.9 ms: 1.03x slower                                                      |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.64 ms: 1.03x slower                                                      |
| xml_etree_generate         | 55.8 ms                                                     | 58.1 ms: 1.04x slower                                                      |
| scimark_fft                | 184 ms                                                      | 193 ms: 1.05x slower                                                       |
| sqlglot_optimize           | 34.5 ms                                                     | 36.2 ms: 1.05x slower                                                      |
| sqlglot_normalize          | 187 ms                                                      | 197 ms: 1.05x slower                                                       |
| chaos                      | 43.3 ms                                                     | 45.6 ms: 1.05x slower                                                      |
| logging_format             | 6.72 us                                                     | 7.07 us: 1.05x slower                                                      |
| sympy_integrate            | 13.0 ms                                                     | 13.7 ms: 1.05x slower                                                      |
| meteor_contest             | 74.6 ms                                                     | 78.9 ms: 1.06x slower                                                      |
| 2to3                       | 218 ms                                                      | 231 ms: 1.06x slower                                                       |
| logging_simple             | 6.28 us                                                     | 6.65 us: 1.06x slower                                                      |
| json_loads                 | 13.9 us                                                     | 14.8 us: 1.07x slower                                                      |
| mdp                        | 1.37 sec                                                    | 1.47 sec: 1.07x slower                                                     |
| pprint_safe_repr           | 513 ms                                                      | 552 ms: 1.08x slower                                                       |
| tomli_loads                | 1.37 sec                                                    | 1.47 sec: 1.08x slower                                                     |
| pprint_pformat             | 1.05 sec                                                    | 1.13 sec: 1.08x slower                                                     |
| pycparser                  | 699 ms                                                      | 760 ms: 1.09x slower                                                       |
| sympy_expand               | 284 ms                                                      | 310 ms: 1.09x slower                                                       |
| raytrace                   | 192 ms                                                      | 211 ms: 1.09x slower                                                       |
| sqlglot_transpile          | 1.02 ms                                                     | 1.12 ms: 1.10x slower                                                      |
| xml_etree_process          | 37.7 ms                                                     | 41.5 ms: 1.10x slower                                                      |
| scimark_lu                 | 58.9 ms                                                     | 64.8 ms: 1.10x slower                                                      |
| nbody                      | 71.9 ms                                                     | 79.7 ms: 1.11x slower                                                      |
| deltablue                  | 2.16 ms                                                     | 2.40 ms: 1.11x slower                                                      |
| python_startup_no_site     | 16.2 ms                                                     | 18.1 ms: 1.12x slower                                                      |
| django_template            | 22.9 ms                                                     | 25.7 ms: 1.12x slower                                                      |
| pyflate                    | 295 ms                                                      | 331 ms: 1.12x slower                                                       |
| fannkuch                   | 247 ms                                                      | 277 ms: 1.12x slower                                                       |
| sqlglot_parse              | 804 us                                                      | 912 us: 1.13x slower                                                       |
| logging_silent             | 60.5 ns                                                     | 69.1 ns: 1.14x slower                                                      |
| scimark_monte_carlo        | 43.7 ms                                                     | 50.0 ms: 1.14x slower                                                      |
| hexiom                     | 4.10 ms                                                     | 4.69 ms: 1.14x slower                                                      |
| richards_super             | 32.1 ms                                                     | 36.9 ms: 1.15x slower                                                      |
| unpickle_pure_python       | 133 us                                                      | 153 us: 1.15x slower                                                       |
| telco                      | 4.13 ms                                                     | 4.81 ms: 1.16x slower                                                      |
| richards                   | 28.4 ms                                                     | 33.1 ms: 1.16x slower                                                      |
| typing_runtime_protocols   | 95.1 us                                                     | 111 us: 1.17x slower                                                       |
| scimark_sor                | 78.8 ms                                                     | 92.9 ms: 1.18x slower                                                      |
| json_dumps                 | 5.70 ms                                                     | 6.81 ms: 1.20x slower                                                      |
| pickle_pure_python         | 195 us                                                      | 234 us: 1.20x slower                                                       |
| coverage                   | 40.8 ms                                                     | 49.3 ms: 1.21x slower                                                      |
| python_startup             | 19.5 ms                                                     | 24.6 ms: 1.26x slower                                                      |
| bench_mp_pool              | 69.2 ms                                                     | 89.4 ms: 1.29x slower                                                      |
| gc_traversal               | 1.52 ms                                                     | 1.99 ms: 1.31x slower                                                      |
| create_gc_cycles           | 752 us                                                      | 1.24 ms: 1.65x slower                                                      |
| regex_v8                   | 14.2 ms                                                     | 24.6 ms: 1.73x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.02x slower                                                               |

Benchmark hidden because not significant (3): json, mako, sympy_sum
Ignored benchmarks (15) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (13) of results/bm-20250110-3.14.0a3+-ac80cdd/bm-20250110-pythonperf1-amd64-Fidget%2dSpinner-tail_call-3.14.0a3+-ac80cdd.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.010x slower

# HPT report

- Reliability score: 99.13% likely to be slow
- 90% likely to have a slowdown of 1.02x
- 95% likely to have a slowdown of 1.02x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown
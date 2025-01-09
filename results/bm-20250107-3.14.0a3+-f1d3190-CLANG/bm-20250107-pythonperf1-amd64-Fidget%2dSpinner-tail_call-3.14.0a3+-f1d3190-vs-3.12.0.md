# Results vs. 3.12.0

- fork: Fidget-Spinner
- ref: tail_call
- machine: windows-amd64
- commit hash: f1d3190
- commit date: 2025-01-07
- overall geometric mean: 1.081x faster
- HPT reliability: 99.98%
- HPT 99th percentile: 1.02x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250107-pythonperf1-amd64-Fidget%2dSpinner-tail_call-3.14.0a3+-f1d3190 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 225 ms: 1.03x slower                                                       |
| docutils       | 1.66 sec                                                    | 1.71 sec: 1.03x slower                                                     |
| Geometric mean | (ref)                                                       | 1.03x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250107-pythonperf1-amd64-Fidget%2dSpinner-tail_call-3.14.0a3+-f1d3190 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 364 ms: 2.12x faster                                                       |
| async_tree_io              | 731 ms                                                      | 363 ms: 2.02x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 154 ms: 1.85x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 203 ms: 1.81x faster                                                       |
| async_tree_none            | 291 ms                                                      | 161 ms: 1.81x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 203 ms: 1.67x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 365 ms: 1.38x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 369 ms: 1.33x faster                                                       |
| Geometric mean             | (ref)                                                       | 1.73x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250107-pythonperf1-amd64-Fidget%2dSpinner-tail_call-3.14.0a3+-f1d3190 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 71.9 ms                                                     | 55.8 ms: 1.29x faster                                                      |
| float          | 56.8 ms                                                     | 45.8 ms: 1.24x faster                                                      |
| pidigits       | 152 ms                                                      | 155 ms: 1.02x slower                                                       |
| Geometric mean | (ref)                                                       | 1.16x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250107-pythonperf1-amd64-Fidget%2dSpinner-tail_call-3.14.0a3+-f1d3190 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 87.5 ms                                                     | 77.2 ms: 1.13x faster                                                      |
| regex_dna      | 126 ms                                                      | 139 ms: 1.10x slower                                                       |
| regex_effbot   | 1.62 ms                                                     | 1.99 ms: 1.23x slower                                                      |
| regex_v8       | 14.2 ms                                                     | 23.7 ms: 1.66x slower                                                      |
| Geometric mean | (ref)                                                       | 1.19x slower                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250107-pythonperf1-amd64-Fidget%2dSpinner-tail_call-3.14.0a3+-f1d3190 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| tomli_loads          | 1.37 sec                                                    | 1.15 sec: 1.19x faster                                                     |
| unpickle_pure_python | 133 us                                                      | 126 us: 1.05x faster                                                       |
| pickle_pure_python   | 195 us                                                      | 189 us: 1.03x faster                                                       |
| xml_etree_parse      | 93.0 ms                                                     | 97.9 ms: 1.05x slower                                                      |
| xml_etree_process    | 37.7 ms                                                     | 40.9 ms: 1.09x slower                                                      |
| xml_etree_generate   | 55.8 ms                                                     | 61.4 ms: 1.10x slower                                                      |
| json_dumps           | 5.70 ms                                                     | 7.33 ms: 1.29x slower                                                      |
| json_loads           | 13.9 us                                                     | 19.8 us: 1.43x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.07x slower                                                               |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250107-pythonperf1-amd64-Fidget%2dSpinner-tail_call-3.14.0a3+-f1d3190 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 18.9 ms: 1.16x slower                                                      |
| python_startup         | 19.5 ms                                                     | 25.5 ms: 1.31x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.23x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250107-pythonperf1-amd64-Fidget%2dSpinner-tail_call-3.14.0a3+-f1d3190 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 7.19 ms: 1.01x slower                                                      |
| django_template | 22.9 ms                                                     | 23.3 ms: 1.02x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.02x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250107-pythonperf1-amd64-Fidget%2dSpinner-tail_call-3.14.0a3+-f1d3190 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 364 ms: 2.12x faster                                                       |
| async_tree_io              | 731 ms                                                      | 363 ms: 2.02x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 154 ms: 1.85x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 203 ms: 1.81x faster                                                       |
| async_tree_none            | 291 ms                                                      | 161 ms: 1.81x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 203 ms: 1.67x faster                                                       |
| generators                 | 22.5 ms                                                     | 15.1 ms: 1.50x faster                                                      |
| deepcopy                   | 238 us                                                      | 163 us: 1.46x faster                                                       |
| deepcopy_memo              | 23.7 us                                                     | 16.8 us: 1.41x faster                                                      |
| go                         | 91.6 ms                                                     | 64.8 ms: 1.41x faster                                                      |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 365 ms: 1.38x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 369 ms: 1.33x faster                                                       |
| scimark_sor                | 78.8 ms                                                     | 60.3 ms: 1.31x faster                                                      |
| comprehensions             | 14.1 us                                                     | 10.8 us: 1.30x faster                                                      |
| nbody                      | 71.9 ms                                                     | 55.8 ms: 1.29x faster                                                      |
| deltablue                  | 2.16 ms                                                     | 1.71 ms: 1.26x faster                                                      |
| scimark_monte_carlo        | 43.7 ms                                                     | 35.0 ms: 1.25x faster                                                      |
| float                      | 56.8 ms                                                     | 45.8 ms: 1.24x faster                                                      |
| deepcopy_reduce            | 2.09 us                                                     | 1.73 us: 1.21x faster                                                      |
| raytrace                   | 192 ms                                                      | 162 ms: 1.19x faster                                                       |
| tomli_loads                | 1.37 sec                                                    | 1.15 sec: 1.19x faster                                                     |
| spectral_norm              | 66.9 ms                                                     | 56.4 ms: 1.19x faster                                                      |
| hexiom                     | 4.10 ms                                                     | 3.48 ms: 1.18x faster                                                      |
| logging_silent             | 60.5 ns                                                     | 51.3 ns: 1.18x faster                                                      |
| coroutines                 | 14.3 ms                                                     | 12.3 ms: 1.16x faster                                                      |
| chaos                      | 43.3 ms                                                     | 37.9 ms: 1.14x faster                                                      |
| regex_compile              | 87.5 ms                                                     | 77.2 ms: 1.13x faster                                                      |
| scimark_fft                | 184 ms                                                      | 164 ms: 1.13x faster                                                       |
| richards                   | 28.4 ms                                                     | 25.3 ms: 1.12x faster                                                      |
| richards_super             | 32.1 ms                                                     | 28.8 ms: 1.11x faster                                                      |
| dulwich_log                | 44.3 ms                                                     | 39.9 ms: 1.11x faster                                                      |
| sqlglot_parse              | 804 us                                                      | 726 us: 1.11x faster                                                       |
| scimark_lu                 | 58.9 ms                                                     | 53.4 ms: 1.10x faster                                                      |
| pprint_pformat             | 1.05 sec                                                    | 952 ms: 1.10x faster                                                       |
| nqueens                    | 62.8 ms                                                     | 57.4 ms: 1.09x faster                                                      |
| pprint_safe_repr           | 513 ms                                                      | 472 ms: 1.09x faster                                                       |
| logging_simple             | 6.28 us                                                     | 5.84 us: 1.07x faster                                                      |
| sqlglot_transpile          | 1.02 ms                                                     | 961 us: 1.06x faster                                                       |
| logging_format             | 6.72 us                                                     | 6.33 us: 1.06x faster                                                      |
| pyflate                    | 295 ms                                                      | 279 ms: 1.06x faster                                                       |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.42 ms: 1.06x faster                                                      |
| unpickle_pure_python       | 133 us                                                      | 126 us: 1.05x faster                                                       |
| sympy_sum                  | 91.5 ms                                                     | 87.0 ms: 1.05x faster                                                      |
| meteor_contest             | 74.6 ms                                                     | 71.6 ms: 1.04x faster                                                      |
| sqlite_synth               | 1.76 us                                                     | 1.69 us: 1.04x faster                                                      |
| fannkuch                   | 247 ms                                                      | 237 ms: 1.04x faster                                                       |
| sympy_str                  | 175 ms                                                      | 169 ms: 1.04x faster                                                       |
| pickle_pure_python         | 195 us                                                      | 189 us: 1.03x faster                                                       |
| sqlglot_normalize          | 187 ms                                                      | 181 ms: 1.03x faster                                                       |
| pycparser                  | 699 ms                                                      | 680 ms: 1.03x faster                                                       |
| async_generators           | 239 ms                                                      | 233 ms: 1.03x faster                                                       |
| bench_thread_pool          | 857 us                                                      | 840 us: 1.02x faster                                                       |
| crypto_pyaes               | 48.5 ms                                                     | 47.7 ms: 1.02x faster                                                      |
| sqlglot_optimize           | 34.5 ms                                                     | 33.9 ms: 1.02x faster                                                      |
| pathlib                    | 80.5 ms                                                     | 79.5 ms: 1.01x faster                                                      |
| sympy_integrate            | 13.0 ms                                                     | 12.9 ms: 1.01x faster                                                      |
| mako                       | 7.09 ms                                                     | 7.19 ms: 1.01x slower                                                      |
| pidigits                   | 152 ms                                                      | 155 ms: 1.02x slower                                                       |
| django_template            | 22.9 ms                                                     | 23.3 ms: 1.02x slower                                                      |
| docutils                   | 1.66 sec                                                    | 1.71 sec: 1.03x slower                                                     |
| 2to3                       | 218 ms                                                      | 225 ms: 1.03x slower                                                       |
| sympy_expand               | 284 ms                                                      | 293 ms: 1.03x slower                                                       |
| xml_etree_parse            | 93.0 ms                                                     | 97.9 ms: 1.05x slower                                                      |
| xml_etree_process          | 37.7 ms                                                     | 40.9 ms: 1.09x slower                                                      |
| regex_dna                  | 126 ms                                                      | 139 ms: 1.10x slower                                                       |
| xml_etree_generate         | 55.8 ms                                                     | 61.4 ms: 1.10x slower                                                      |
| typing_runtime_protocols   | 95.1 us                                                     | 107 us: 1.13x slower                                                       |
| python_startup_no_site     | 16.2 ms                                                     | 18.9 ms: 1.16x slower                                                      |
| json                       | 3.05 ms                                                     | 3.58 ms: 1.18x slower                                                      |
| mdp                        | 1.37 sec                                                    | 1.62 sec: 1.18x slower                                                     |
| telco                      | 4.13 ms                                                     | 4.92 ms: 1.19x slower                                                      |
| regex_effbot               | 1.62 ms                                                     | 1.99 ms: 1.23x slower                                                      |
| coverage                   | 40.8 ms                                                     | 50.5 ms: 1.24x slower                                                      |
| json_dumps                 | 5.70 ms                                                     | 7.33 ms: 1.29x slower                                                      |
| python_startup             | 19.5 ms                                                     | 25.5 ms: 1.31x slower                                                      |
| bench_mp_pool              | 69.2 ms                                                     | 93.3 ms: 1.35x slower                                                      |
| json_loads                 | 13.9 us                                                     | 19.8 us: 1.43x slower                                                      |
| regex_v8                   | 14.2 ms                                                     | 23.7 ms: 1.66x slower                                                      |
| create_gc_cycles           | 752 us                                                      | 1.37 ms: 1.82x slower                                                      |
| gc_traversal               | 1.52 ms                                                     | 2.85 ms: 1.88x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.07x faster                                                               |

Benchmark hidden because not significant (1): xml_etree_iterparse
Ignored benchmarks (15) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (13) of results/bm-20250107-3.14.0a3+-f1d3190-CLANG/bm-20250107-pythonperf1-amd64-Fidget%2dSpinner-tail_call-3.14.0a3+-f1d3190.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.081x faster

# HPT report

- Reliability score: 99.98% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: unknown
# Results vs. 3.12.0

- fork: python
- ref: d6dd64ac654898b4ce71
- machine: windows-amd64
- commit hash: d6dd64a
- commit date: 2025-10-12
- overall geometric mean: 1.030x faster
- HPT reliability: 90.24%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20251012-pythonperf1-amd64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| docutils       | 1.66 sec                                                    | 2.86 sec: 1.72x slower                                                     |
| Geometric mean | (ref)                                                       | 1.31x slower                                                               |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20251012-pythonperf1-amd64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 318 ms: 2.42x faster                                                       |
| async_tree_io              | 731 ms                                                      | 339 ms: 2.15x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 145 ms: 1.96x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 188 ms: 1.95x faster                                                       |
| async_tree_none            | 291 ms                                                      | 165 ms: 1.77x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 303 ms: 1.66x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 211 ms: 1.61x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 323 ms: 1.51x faster                                                       |
| Geometric mean             | (ref)                                                       | 1.86x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20251012-pythonperf1-amd64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 45.2 ms: 1.26x faster                                                      |
| pidigits       | 152 ms                                                      | 136 ms: 1.12x faster                                                       |
| nbody          | 71.9 ms                                                     | 78.2 ms: 1.09x slower                                                      |
| Geometric mean | (ref)                                                       | 1.09x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20251012-pythonperf1-amd64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_dna      | 126 ms                                                      | 114 ms: 1.11x faster                                                       |
| regex_v8       | 14.2 ms                                                     | 13.2 ms: 1.08x faster                                                      |
| regex_compile  | 87.5 ms                                                     | 89.2 ms: 1.02x slower                                                      |
| regex_effbot   | 1.62 ms                                                     | 1.66 ms: 1.03x slower                                                      |
| Geometric mean | (ref)                                                       | 1.04x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20251012-pythonperf1-amd64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| xml_etree_iterparse  | 65.2 ms                                                     | 58.3 ms: 1.12x faster                                                      |
| xml_etree_parse      | 93.0 ms                                                     | 89.3 ms: 1.04x faster                                                      |
| pickle               | 7.43 us                                                     | 7.82 us: 1.05x slower                                                      |
| json_dumps           | 5.70 ms                                                     | 6.04 ms: 1.06x slower                                                      |
| xml_etree_generate   | 55.8 ms                                                     | 60.6 ms: 1.08x slower                                                      |
| unpickle_pure_python | 133 us                                                      | 146 us: 1.09x slower                                                       |
| pickle_dict          | 18.4 us                                                     | 20.3 us: 1.10x slower                                                      |
| pickle_list          | 2.83 us                                                     | 3.14 us: 1.11x slower                                                      |
| pickle_pure_python   | 195 us                                                      | 222 us: 1.14x slower                                                       |
| json_loads           | 13.9 us                                                     | 16.1 us: 1.16x slower                                                      |
| unpickle_list        | 2.75 us                                                     | 3.23 us: 1.17x slower                                                      |
| unpickle             | 8.18 us                                                     | 9.61 us: 1.17x slower                                                      |
| xml_etree_process    | 37.7 ms                                                     | 44.5 ms: 1.18x slower                                                      |
| tomli_loads          | 1.37 sec                                                    | 2.28 sec: 1.66x slower                                                     |
| Geometric mean       | (ref)                                                       | 1.12x slower                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20251012-pythonperf1-amd64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 19.2 ms: 1.18x slower                                                      |
| python_startup         | 19.5 ms                                                     | 25.6 ms: 1.32x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.25x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20251012-pythonperf1-amd64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| django_template | 22.9 ms                                                     | 25.6 ms: 1.11x slower                                                      |
| mako            | 7.09 ms                                                     | 10.1 ms: 1.42x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.26x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20251012-pythonperf1-amd64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pathlib                    | 80.5 ms                                                     | 28.9 ms: 2.79x faster                                                      |
| async_tree_io_tg           | 771 ms                                                      | 318 ms: 2.42x faster                                                       |
| async_tree_io              | 731 ms                                                      | 339 ms: 2.15x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 145 ms: 1.96x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 188 ms: 1.95x faster                                                       |
| async_tree_none            | 291 ms                                                      | 165 ms: 1.77x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 303 ms: 1.66x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 211 ms: 1.61x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 323 ms: 1.51x faster                                                       |
| mdp                        | 1.37 sec                                                    | 1.05 sec: 1.30x faster                                                     |
| deepcopy                   | 238 us                                                      | 184 us: 1.29x faster                                                       |
| deepcopy_memo              | 23.7 us                                                     | 18.4 us: 1.29x faster                                                      |
| sqlite_synth               | 1.76 us                                                     | 1.38 us: 1.28x faster                                                      |
| float                      | 56.8 ms                                                     | 45.2 ms: 1.26x faster                                                      |
| gc_traversal               | 1.52 ms                                                     | 1.22 ms: 1.25x faster                                                      |
| comprehensions             | 14.1 us                                                     | 11.7 us: 1.21x faster                                                      |
| pidigits                   | 152 ms                                                      | 136 ms: 1.12x faster                                                       |
| xml_etree_iterparse        | 65.2 ms                                                     | 58.3 ms: 1.12x faster                                                      |
| regex_dna                  | 126 ms                                                      | 114 ms: 1.11x faster                                                       |
| dulwich_log                | 44.3 ms                                                     | 40.7 ms: 1.09x faster                                                      |
| regex_v8                   | 14.2 ms                                                     | 13.2 ms: 1.08x faster                                                      |
| generators                 | 22.5 ms                                                     | 21.0 ms: 1.07x faster                                                      |
| asyncio_tcp                | 487 ms                                                      | 456 ms: 1.07x faster                                                       |
| unpack_sequence            | 37.5 ns                                                     | 35.1 ns: 1.07x faster                                                      |
| deepcopy_reduce            | 2.09 us                                                     | 1.99 us: 1.05x faster                                                      |
| xml_etree_parse            | 93.0 ms                                                     | 89.3 ms: 1.04x faster                                                      |
| go                         | 91.6 ms                                                     | 90.0 ms: 1.02x faster                                                      |
| pycparser                  | 699 ms                                                      | 687 ms: 1.02x faster                                                       |
| logging_silent             | 60.5 ns                                                     | 59.8 ns: 1.01x faster                                                      |
| pyflate                    | 295 ms                                                      | 296 ms: 1.01x slower                                                       |
| spectral_norm              | 66.9 ms                                                     | 67.7 ms: 1.01x slower                                                      |
| scimark_fft                | 184 ms                                                      | 188 ms: 1.02x slower                                                       |
| regex_compile              | 87.5 ms                                                     | 89.2 ms: 1.02x slower                                                      |
| json                       | 3.05 ms                                                     | 3.11 ms: 1.02x slower                                                      |
| regex_effbot               | 1.62 ms                                                     | 1.66 ms: 1.03x slower                                                      |
| sympy_sum                  | 91.5 ms                                                     | 93.9 ms: 1.03x slower                                                      |
| scimark_sor                | 78.8 ms                                                     | 80.9 ms: 1.03x slower                                                      |
| sympy_str                  | 175 ms                                                      | 181 ms: 1.04x slower                                                       |
| logging_format             | 6.72 us                                                     | 6.97 us: 1.04x slower                                                      |
| pprint_safe_repr           | 513 ms                                                      | 533 ms: 1.04x slower                                                       |
| async_generators           | 239 ms                                                      | 249 ms: 1.04x slower                                                       |
| logging_simple             | 6.28 us                                                     | 6.54 us: 1.04x slower                                                      |
| chaos                      | 43.3 ms                                                     | 45.6 ms: 1.05x slower                                                      |
| pickle                     | 7.43 us                                                     | 7.82 us: 1.05x slower                                                      |
| sympy_integrate            | 13.0 ms                                                     | 13.7 ms: 1.06x slower                                                      |
| json_dumps                 | 5.70 ms                                                     | 6.04 ms: 1.06x slower                                                      |
| raytrace                   | 192 ms                                                      | 206 ms: 1.07x slower                                                       |
| deltablue                  | 2.16 ms                                                     | 2.32 ms: 1.07x slower                                                      |
| hexiom                     | 4.10 ms                                                     | 4.40 ms: 1.07x slower                                                      |
| bench_mp_pool              | 69.2 ms                                                     | 74.5 ms: 1.08x slower                                                      |
| xml_etree_generate         | 55.8 ms                                                     | 60.6 ms: 1.08x slower                                                      |
| nbody                      | 71.9 ms                                                     | 78.2 ms: 1.09x slower                                                      |
| sympy_expand               | 284 ms                                                      | 309 ms: 1.09x slower                                                       |
| scimark_lu                 | 58.9 ms                                                     | 64.4 ms: 1.09x slower                                                      |
| unpickle_pure_python       | 133 us                                                      | 146 us: 1.09x slower                                                       |
| pickle_dict                | 18.4 us                                                     | 20.3 us: 1.10x slower                                                      |
| richards                   | 28.4 ms                                                     | 31.4 ms: 1.11x slower                                                      |
| pickle_list                | 2.83 us                                                     | 3.14 us: 1.11x slower                                                      |
| django_template            | 22.9 ms                                                     | 25.6 ms: 1.11x slower                                                      |
| scimark_monte_carlo        | 43.7 ms                                                     | 48.9 ms: 1.12x slower                                                      |
| nqueens                    | 62.8 ms                                                     | 71.0 ms: 1.13x slower                                                      |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.90 ms: 1.13x slower                                                      |
| pickle_pure_python         | 195 us                                                      | 222 us: 1.14x slower                                                       |
| meteor_contest             | 74.6 ms                                                     | 85.4 ms: 1.14x slower                                                      |
| richards_super             | 32.1 ms                                                     | 36.8 ms: 1.15x slower                                                      |
| json_loads                 | 13.9 us                                                     | 16.1 us: 1.16x slower                                                      |
| crypto_pyaes               | 48.5 ms                                                     | 56.3 ms: 1.16x slower                                                      |
| unpickle_list              | 2.75 us                                                     | 3.23 us: 1.17x slower                                                      |
| unpickle                   | 8.18 us                                                     | 9.61 us: 1.17x slower                                                      |
| telco                      | 4.13 ms                                                     | 4.87 ms: 1.18x slower                                                      |
| xml_etree_process          | 37.7 ms                                                     | 44.5 ms: 1.18x slower                                                      |
| python_startup_no_site     | 16.2 ms                                                     | 19.2 ms: 1.18x slower                                                      |
| bench_thread_pool          | 857 us                                                      | 1.02 ms: 1.19x slower                                                      |
| fannkuch                   | 247 ms                                                      | 300 ms: 1.22x slower                                                       |
| python_startup             | 19.5 ms                                                     | 25.6 ms: 1.32x slower                                                      |
| typing_runtime_protocols   | 95.1 us                                                     | 127 us: 1.33x slower                                                       |
| create_gc_cycles           | 752 us                                                      | 1.02 ms: 1.36x slower                                                      |
| mako                       | 7.09 ms                                                     | 10.1 ms: 1.42x slower                                                      |
| pprint_pformat             | 1.05 sec                                                    | 1.59 sec: 1.52x slower                                                     |
| tomli_loads                | 1.37 sec                                                    | 2.28 sec: 1.66x slower                                                     |
| coverage                   | 40.8 ms                                                     | 68.2 ms: 1.67x slower                                                      |
| docutils                   | 1.66 sec                                                    | 2.86 sec: 1.72x slower                                                     |
| Geometric mean             | (ref)                                                       | 1.02x faster                                                               |

Benchmark hidden because not significant (3): coroutines, 2to3, asyncio_tcp_ssl
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (17) of results/bm-20251012-3.15.0a0-d6dd64a-NOGIL/bm-20251012-pythonperf1-amd64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.030x faster

# HPT report

- Reliability score: 90.24% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown
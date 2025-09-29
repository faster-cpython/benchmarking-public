# Results vs. 3.12.0

- fork: python
- ref: 48d0d0dd9733eae4935f
- machine: windows-amd64
- commit hash: 48d0d0d
- commit date: 2025-09-26
- overall geometric mean: 1.153x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250926-pythonperf1-amd64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 214 ms: 1.02x faster                                                       |
| docutils       | 1.66 sec                                                    | 1.62 sec: 1.03x faster                                                     |
| Geometric mean | (ref)                                                       | 1.02x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250926-pythonperf1-amd64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 377 ms: 2.05x faster                                                       |
| async_tree_io              | 731 ms                                                      | 381 ms: 1.92x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 209 ms: 1.75x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 164 ms: 1.74x faster                                                       |
| async_tree_none            | 291 ms                                                      | 170 ms: 1.71x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 199 ms: 1.70x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 333 ms: 1.51x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 329 ms: 1.49x faster                                                       |
| Geometric mean             | (ref)                                                       | 1.72x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250926-pythonperf1-amd64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 39.8 ms: 1.43x faster                                                      |
| nbody          | 71.9 ms                                                     | 55.8 ms: 1.29x faster                                                      |
| pidigits       | 152 ms                                                      | 146 ms: 1.04x faster                                                       |
| Geometric mean | (ref)                                                       | 1.24x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250926-pythonperf1-amd64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 87.5 ms                                                     | 77.3 ms: 1.13x faster                                                      |
| regex_dna      | 126 ms                                                      | 115 ms: 1.10x faster                                                       |
| regex_v8       | 14.2 ms                                                     | 13.3 ms: 1.07x faster                                                      |
| Geometric mean | (ref)                                                       | 1.08x faster                                                               |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250926-pythonperf1-amd64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| unpickle_pure_python | 133 us                                                      | 105 us: 1.27x faster                                                       |
| tomli_loads          | 1.37 sec                                                    | 1.08 sec: 1.27x faster                                                     |
| xml_etree_generate   | 55.8 ms                                                     | 50.0 ms: 1.12x faster                                                      |
| json_dumps           | 5.70 ms                                                     | 5.31 ms: 1.07x faster                                                      |
| xml_etree_parse      | 93.0 ms                                                     | 87.6 ms: 1.06x faster                                                      |
| xml_etree_iterparse  | 65.2 ms                                                     | 61.5 ms: 1.06x faster                                                      |
| xml_etree_process    | 37.7 ms                                                     | 35.7 ms: 1.06x faster                                                      |
| pickle_pure_python   | 195 us                                                      | 198 us: 1.01x slower                                                       |
| pickle               | 7.43 us                                                     | 7.65 us: 1.03x slower                                                      |
| pickle_dict          | 18.4 us                                                     | 19.2 us: 1.04x slower                                                      |
| unpickle             | 8.18 us                                                     | 8.69 us: 1.06x slower                                                      |
| pickle_list          | 2.83 us                                                     | 3.26 us: 1.15x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.04x faster                                                               |

Benchmark hidden because not significant (2): unpickle_list, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250926-pythonperf1-amd64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 19.1 ms: 1.17x slower                                                      |
| python_startup         | 19.5 ms                                                     | 25.2 ms: 1.30x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.23x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250926-pythonperf1-amd64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 5.34 ms: 1.33x faster                                                      |
| django_template | 22.9 ms                                                     | 24.0 ms: 1.05x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.13x faster                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250926-pythonperf1-amd64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pathlib                    | 80.5 ms                                                     | 28.9 ms: 2.79x faster                                                      |
| async_tree_io_tg           | 771 ms                                                      | 377 ms: 2.05x faster                                                       |
| async_tree_io              | 731 ms                                                      | 381 ms: 1.92x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 209 ms: 1.75x faster                                                       |
| mdp                        | 1.37 sec                                                    | 786 ms: 1.75x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 164 ms: 1.74x faster                                                       |
| async_tree_none            | 291 ms                                                      | 170 ms: 1.71x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 199 ms: 1.70x faster                                                       |
| asyncio_tcp_ssl            | 2.10 sec                                                    | 1.30 sec: 1.61x faster                                                     |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 333 ms: 1.51x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 329 ms: 1.49x faster                                                       |
| deepcopy                   | 238 us                                                      | 164 us: 1.46x faster                                                       |
| float                      | 56.8 ms                                                     | 39.8 ms: 1.43x faster                                                      |
| deepcopy_memo              | 23.7 us                                                     | 17.2 us: 1.38x faster                                                      |
| scimark_fft                | 184 ms                                                      | 134 ms: 1.38x faster                                                       |
| comprehensions             | 14.1 us                                                     | 10.5 us: 1.35x faster                                                      |
| mako                       | 7.09 ms                                                     | 5.34 ms: 1.33x faster                                                      |
| nbody                      | 71.9 ms                                                     | 55.8 ms: 1.29x faster                                                      |
| unpickle_pure_python       | 133 us                                                      | 105 us: 1.27x faster                                                       |
| tomli_loads                | 1.37 sec                                                    | 1.08 sec: 1.27x faster                                                     |
| go                         | 91.6 ms                                                     | 76.7 ms: 1.19x faster                                                      |
| fannkuch                   | 247 ms                                                      | 207 ms: 1.19x faster                                                       |
| deepcopy_reduce            | 2.09 us                                                     | 1.76 us: 1.19x faster                                                      |
| pprint_safe_repr           | 513 ms                                                      | 433 ms: 1.19x faster                                                       |
| pyflate                    | 295 ms                                                      | 250 ms: 1.18x faster                                                       |
| pprint_pformat             | 1.05 sec                                                    | 886 ms: 1.18x faster                                                       |
| generators                 | 22.5 ms                                                     | 19.3 ms: 1.17x faster                                                      |
| asyncio_tcp                | 487 ms                                                      | 418 ms: 1.17x faster                                                       |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.21 ms: 1.16x faster                                                      |
| dulwich_log                | 44.3 ms                                                     | 38.6 ms: 1.15x faster                                                      |
| regex_compile              | 87.5 ms                                                     | 77.3 ms: 1.13x faster                                                      |
| unpack_sequence            | 37.5 ns                                                     | 33.2 ns: 1.13x faster                                                      |
| sqlite_synth               | 1.76 us                                                     | 1.57 us: 1.12x faster                                                      |
| xml_etree_generate         | 55.8 ms                                                     | 50.0 ms: 1.12x faster                                                      |
| logging_silent             | 60.5 ns                                                     | 54.3 ns: 1.11x faster                                                      |
| raytrace                   | 192 ms                                                      | 173 ms: 1.11x faster                                                       |
| spectral_norm              | 66.9 ms                                                     | 60.5 ms: 1.11x faster                                                      |
| regex_dna                  | 126 ms                                                      | 115 ms: 1.10x faster                                                       |
| json                       | 3.05 ms                                                     | 2.80 ms: 1.09x faster                                                      |
| crypto_pyaes               | 48.5 ms                                                     | 44.6 ms: 1.09x faster                                                      |
| sympy_sum                  | 91.5 ms                                                     | 84.2 ms: 1.09x faster                                                      |
| chaos                      | 43.3 ms                                                     | 40.2 ms: 1.08x faster                                                      |
| json_dumps                 | 5.70 ms                                                     | 5.31 ms: 1.07x faster                                                      |
| scimark_monte_carlo        | 43.7 ms                                                     | 40.9 ms: 1.07x faster                                                      |
| regex_v8                   | 14.2 ms                                                     | 13.3 ms: 1.07x faster                                                      |
| xml_etree_parse            | 93.0 ms                                                     | 87.6 ms: 1.06x faster                                                      |
| xml_etree_iterparse        | 65.2 ms                                                     | 61.5 ms: 1.06x faster                                                      |
| sympy_str                  | 175 ms                                                      | 165 ms: 1.06x faster                                                       |
| richards                   | 28.4 ms                                                     | 26.8 ms: 1.06x faster                                                      |
| xml_etree_process          | 37.7 ms                                                     | 35.7 ms: 1.06x faster                                                      |
| nqueens                    | 62.8 ms                                                     | 59.7 ms: 1.05x faster                                                      |
| scimark_sor                | 78.8 ms                                                     | 75.0 ms: 1.05x faster                                                      |
| richards_super             | 32.1 ms                                                     | 30.6 ms: 1.05x faster                                                      |
| sympy_integrate            | 13.0 ms                                                     | 12.4 ms: 1.05x faster                                                      |
| hexiom                     | 4.10 ms                                                     | 3.92 ms: 1.05x faster                                                      |
| meteor_contest             | 74.6 ms                                                     | 71.4 ms: 1.04x faster                                                      |
| telco                      | 4.13 ms                                                     | 3.96 ms: 1.04x faster                                                      |
| pidigits                   | 152 ms                                                      | 146 ms: 1.04x faster                                                       |
| scimark_lu                 | 58.9 ms                                                     | 56.7 ms: 1.04x faster                                                      |
| logging_simple             | 6.28 us                                                     | 6.09 us: 1.03x faster                                                      |
| docutils                   | 1.66 sec                                                    | 1.62 sec: 1.03x faster                                                     |
| bench_thread_pool          | 857 us                                                      | 834 us: 1.03x faster                                                       |
| coroutines                 | 14.3 ms                                                     | 13.9 ms: 1.03x faster                                                      |
| pycparser                  | 699 ms                                                      | 682 ms: 1.03x faster                                                       |
| logging_format             | 6.72 us                                                     | 6.57 us: 1.02x faster                                                      |
| 2to3                       | 218 ms                                                      | 214 ms: 1.02x faster                                                       |
| pickle_pure_python         | 195 us                                                      | 198 us: 1.01x slower                                                       |
| deltablue                  | 2.16 ms                                                     | 2.19 ms: 1.01x slower                                                      |
| pickle                     | 7.43 us                                                     | 7.65 us: 1.03x slower                                                      |
| pickle_dict                | 18.4 us                                                     | 19.2 us: 1.04x slower                                                      |
| django_template            | 22.9 ms                                                     | 24.0 ms: 1.05x slower                                                      |
| unpickle                   | 8.18 us                                                     | 8.69 us: 1.06x slower                                                      |
| typing_runtime_protocols   | 95.1 us                                                     | 102 us: 1.07x slower                                                       |
| pickle_list                | 2.83 us                                                     | 3.26 us: 1.15x slower                                                      |
| python_startup_no_site     | 16.2 ms                                                     | 19.1 ms: 1.17x slower                                                      |
| coverage                   | 40.8 ms                                                     | 49.0 ms: 1.20x slower                                                      |
| bench_mp_pool              | 69.2 ms                                                     | 88.8 ms: 1.28x slower                                                      |
| python_startup             | 19.5 ms                                                     | 25.2 ms: 1.30x slower                                                      |
| gc_traversal               | 1.52 ms                                                     | 2.12 ms: 1.39x slower                                                      |
| create_gc_cycles           | 752 us                                                      | 1.25 ms: 1.67x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.14x faster                                                               |

Benchmark hidden because not significant (5): regex_effbot, unpickle_list, json_loads, async_generators, sympy_expand
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (17) of results/bm-20250926-3.15.0a0-48d0d0d-JIT/bm-20250926-pythonperf1-amd64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.153x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.08x
- 95% likely to have a speedup of 1.07x
- 99% likely to have a speedup of 1.06x

# Memory
- memory change: unknown
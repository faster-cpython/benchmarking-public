# Results vs. 3.12.0

- fork: python
- ref: 6fcac09401e336b25833
- machine: windows-amd64
- commit hash: 6fcac09
- commit date: 2025-08-23
- overall geometric mean: 1.151x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.07x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250823-pythonperf1-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 214 ms: 1.02x faster                                                       |
| docutils       | 1.66 sec                                                    | 1.61 sec: 1.03x faster                                                     |
| Geometric mean | (ref)                                                       | 1.02x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250823-pythonperf1-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 377 ms: 2.04x faster                                                       |
| async_tree_io              | 731 ms                                                      | 383 ms: 1.91x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 208 ms: 1.76x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 164 ms: 1.74x faster                                                       |
| async_tree_none            | 291 ms                                                      | 168 ms: 1.73x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 197 ms: 1.72x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 336 ms: 1.50x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 330 ms: 1.48x faster                                                       |
| Geometric mean             | (ref)                                                       | 1.73x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250823-pythonperf1-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 42.9 ms: 1.32x faster                                                      |
| nbody          | 71.9 ms                                                     | 60.0 ms: 1.20x faster                                                      |
| pidigits       | 152 ms                                                      | 144 ms: 1.06x faster                                                       |
| Geometric mean | (ref)                                                       | 1.19x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250823-pythonperf1-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 87.5 ms                                                     | 77.4 ms: 1.13x faster                                                      |
| regex_dna      | 126 ms                                                      | 116 ms: 1.09x faster                                                       |
| regex_v8       | 14.2 ms                                                     | 13.5 ms: 1.05x faster                                                      |
| regex_effbot   | 1.62 ms                                                     | 1.55 ms: 1.04x faster                                                      |
| Geometric mean | (ref)                                                       | 1.08x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250823-pythonperf1-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| unpickle_pure_python | 133 us                                                      | 104 us: 1.28x faster                                                       |
| tomli_loads          | 1.37 sec                                                    | 1.08 sec: 1.27x faster                                                     |
| xml_etree_generate   | 55.8 ms                                                     | 49.8 ms: 1.12x faster                                                      |
| xml_etree_parse      | 93.0 ms                                                     | 85.5 ms: 1.09x faster                                                      |
| xml_etree_process    | 37.7 ms                                                     | 34.7 ms: 1.09x faster                                                      |
| json_dumps           | 5.70 ms                                                     | 5.31 ms: 1.07x faster                                                      |
| xml_etree_iterparse  | 65.2 ms                                                     | 61.6 ms: 1.06x faster                                                      |
| unpickle_list        | 2.75 us                                                     | 2.70 us: 1.02x faster                                                      |
| pickle               | 7.43 us                                                     | 7.46 us: 1.00x slower                                                      |
| pickle_pure_python   | 195 us                                                      | 197 us: 1.01x slower                                                       |
| json_loads           | 13.9 us                                                     | 14.1 us: 1.01x slower                                                      |
| unpickle             | 8.18 us                                                     | 8.43 us: 1.03x slower                                                      |
| pickle_dict          | 18.4 us                                                     | 19.3 us: 1.05x slower                                                      |
| pickle_list          | 2.83 us                                                     | 3.30 us: 1.17x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.05x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250823-pythonperf1-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 19.2 ms: 1.18x slower                                                      |
| python_startup         | 19.5 ms                                                     | 25.2 ms: 1.29x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.24x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250823-pythonperf1-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 5.21 ms: 1.36x faster                                                      |
| django_template | 22.9 ms                                                     | 23.9 ms: 1.04x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.14x faster                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250823-pythonperf1-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pathlib                    | 80.5 ms                                                     | 30.1 ms: 2.68x faster                                                      |
| async_tree_io_tg           | 771 ms                                                      | 377 ms: 2.04x faster                                                       |
| async_tree_io              | 731 ms                                                      | 383 ms: 1.91x faster                                                       |
| mdp                        | 1.37 sec                                                    | 777 ms: 1.77x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 208 ms: 1.76x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 164 ms: 1.74x faster                                                       |
| async_tree_none            | 291 ms                                                      | 168 ms: 1.73x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 197 ms: 1.72x faster                                                       |
| asyncio_tcp_ssl            | 2.10 sec                                                    | 1.24 sec: 1.69x faster                                                     |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 336 ms: 1.50x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 330 ms: 1.48x faster                                                       |
| deepcopy                   | 238 us                                                      | 168 us: 1.42x faster                                                       |
| comprehensions             | 14.1 us                                                     | 10.3 us: 1.38x faster                                                      |
| mako                       | 7.09 ms                                                     | 5.21 ms: 1.36x faster                                                      |
| float                      | 56.8 ms                                                     | 42.9 ms: 1.32x faster                                                      |
| deepcopy_memo              | 23.7 us                                                     | 18.2 us: 1.30x faster                                                      |
| unpickle_pure_python       | 133 us                                                      | 104 us: 1.28x faster                                                       |
| tomli_loads                | 1.37 sec                                                    | 1.08 sec: 1.27x faster                                                     |
| asyncio_tcp                | 487 ms                                                      | 389 ms: 1.25x faster                                                       |
| scimark_fft                | 184 ms                                                      | 148 ms: 1.25x faster                                                       |
| pprint_safe_repr           | 513 ms                                                      | 414 ms: 1.24x faster                                                       |
| pprint_pformat             | 1.05 sec                                                    | 849 ms: 1.23x faster                                                       |
| go                         | 91.6 ms                                                     | 74.9 ms: 1.22x faster                                                      |
| nbody                      | 71.9 ms                                                     | 60.0 ms: 1.20x faster                                                      |
| generators                 | 22.5 ms                                                     | 19.1 ms: 1.18x faster                                                      |
| fannkuch                   | 247 ms                                                      | 210 ms: 1.18x faster                                                       |
| sqlite_synth               | 1.76 us                                                     | 1.52 us: 1.16x faster                                                      |
| deepcopy_reduce            | 2.09 us                                                     | 1.82 us: 1.15x faster                                                      |
| pyflate                    | 295 ms                                                      | 256 ms: 1.15x faster                                                       |
| unpack_sequence            | 37.5 ns                                                     | 33.0 ns: 1.14x faster                                                      |
| dulwich_log                | 44.3 ms                                                     | 39.1 ms: 1.13x faster                                                      |
| regex_compile              | 87.5 ms                                                     | 77.4 ms: 1.13x faster                                                      |
| logging_silent             | 60.5 ns                                                     | 53.5 ns: 1.13x faster                                                      |
| xml_etree_generate         | 55.8 ms                                                     | 49.8 ms: 1.12x faster                                                      |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.28 ms: 1.12x faster                                                      |
| scimark_monte_carlo        | 43.7 ms                                                     | 39.1 ms: 1.12x faster                                                      |
| crypto_pyaes               | 48.5 ms                                                     | 44.2 ms: 1.10x faster                                                      |
| chaos                      | 43.3 ms                                                     | 39.6 ms: 1.09x faster                                                      |
| regex_dna                  | 126 ms                                                      | 116 ms: 1.09x faster                                                       |
| raytrace                   | 192 ms                                                      | 176 ms: 1.09x faster                                                       |
| xml_etree_parse            | 93.0 ms                                                     | 85.5 ms: 1.09x faster                                                      |
| xml_etree_process          | 37.7 ms                                                     | 34.7 ms: 1.09x faster                                                      |
| sympy_sum                  | 91.5 ms                                                     | 84.5 ms: 1.08x faster                                                      |
| telco                      | 4.13 ms                                                     | 3.82 ms: 1.08x faster                                                      |
| richards                   | 28.4 ms                                                     | 26.3 ms: 1.08x faster                                                      |
| spectral_norm              | 66.9 ms                                                     | 62.1 ms: 1.08x faster                                                      |
| json_dumps                 | 5.70 ms                                                     | 5.31 ms: 1.07x faster                                                      |
| logging_simple             | 6.28 us                                                     | 5.89 us: 1.07x faster                                                      |
| richards_super             | 32.1 ms                                                     | 30.1 ms: 1.06x faster                                                      |
| nqueens                    | 62.8 ms                                                     | 59.2 ms: 1.06x faster                                                      |
| pidigits                   | 152 ms                                                      | 144 ms: 1.06x faster                                                       |
| meteor_contest             | 74.6 ms                                                     | 70.5 ms: 1.06x faster                                                      |
| logging_format             | 6.72 us                                                     | 6.35 us: 1.06x faster                                                      |
| xml_etree_iterparse        | 65.2 ms                                                     | 61.6 ms: 1.06x faster                                                      |
| scimark_sor                | 78.8 ms                                                     | 74.7 ms: 1.05x faster                                                      |
| regex_v8                   | 14.2 ms                                                     | 13.5 ms: 1.05x faster                                                      |
| sympy_integrate            | 13.0 ms                                                     | 12.3 ms: 1.05x faster                                                      |
| hexiom                     | 4.10 ms                                                     | 3.91 ms: 1.05x faster                                                      |
| sympy_str                  | 175 ms                                                      | 167 ms: 1.05x faster                                                       |
| regex_effbot               | 1.62 ms                                                     | 1.55 ms: 1.04x faster                                                      |
| docutils                   | 1.66 sec                                                    | 1.61 sec: 1.03x faster                                                     |
| scimark_lu                 | 58.9 ms                                                     | 57.8 ms: 1.02x faster                                                      |
| 2to3                       | 218 ms                                                      | 214 ms: 1.02x faster                                                       |
| unpickle_list              | 2.75 us                                                     | 2.70 us: 1.02x faster                                                      |
| async_generators           | 239 ms                                                      | 237 ms: 1.01x faster                                                       |
| json                       | 3.05 ms                                                     | 3.02 ms: 1.01x faster                                                      |
| pickle                     | 7.43 us                                                     | 7.46 us: 1.00x slower                                                      |
| pickle_pure_python         | 195 us                                                      | 197 us: 1.01x slower                                                       |
| json_loads                 | 13.9 us                                                     | 14.1 us: 1.01x slower                                                      |
| sympy_expand               | 284 ms                                                      | 288 ms: 1.01x slower                                                       |
| coroutines                 | 14.3 ms                                                     | 14.5 ms: 1.02x slower                                                      |
| unpickle                   | 8.18 us                                                     | 8.43 us: 1.03x slower                                                      |
| django_template            | 22.9 ms                                                     | 23.9 ms: 1.04x slower                                                      |
| pickle_dict                | 18.4 us                                                     | 19.3 us: 1.05x slower                                                      |
| typing_runtime_protocols   | 95.1 us                                                     | 100 us: 1.06x slower                                                       |
| coverage                   | 40.8 ms                                                     | 47.4 ms: 1.16x slower                                                      |
| pickle_list                | 2.83 us                                                     | 3.30 us: 1.17x slower                                                      |
| python_startup_no_site     | 16.2 ms                                                     | 19.2 ms: 1.18x slower                                                      |
| python_startup             | 19.5 ms                                                     | 25.2 ms: 1.29x slower                                                      |
| bench_mp_pool              | 69.2 ms                                                     | 92.2 ms: 1.33x slower                                                      |
| gc_traversal               | 1.52 ms                                                     | 2.11 ms: 1.39x slower                                                      |
| create_gc_cycles           | 752 us                                                      | 1.28 ms: 1.70x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.14x faster                                                               |

Benchmark hidden because not significant (3): bench_thread_pool, pycparser, deltablue
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (17) of results/bm-20250823-3.15.0a0-6fcac09-JIT/bm-20250823-pythonperf1-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.151x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.08x
- 95% likely to have a speedup of 1.08x
- 99% likely to have a speedup of 1.07x

# Memory
- memory change: unknown
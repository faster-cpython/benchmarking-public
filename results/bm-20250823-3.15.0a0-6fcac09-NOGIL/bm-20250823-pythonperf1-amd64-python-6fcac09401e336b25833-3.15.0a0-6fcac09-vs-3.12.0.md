# Results vs. 3.12.0

- fork: python
- ref: 6fcac09401e336b25833
- machine: windows-amd64
- commit hash: 6fcac09
- commit date: 2025-08-23
- overall geometric mean: 1.005x faster
- HPT reliability: 97.58%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250823-pythonperf1-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 221 ms: 1.01x slower                                                       |
| docutils       | 1.66 sec                                                    | 2.74 sec: 1.65x slower                                                     |
| Geometric mean | (ref)                                                       | 1.29x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250823-pythonperf1-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 323 ms: 2.39x faster                                                       |
| async_tree_io              | 731 ms                                                      | 346 ms: 2.11x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 145 ms: 1.97x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 189 ms: 1.94x faster                                                       |
| async_tree_none            | 291 ms                                                      | 170 ms: 1.71x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 305 ms: 1.65x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 209 ms: 1.62x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 325 ms: 1.50x faster                                                       |
| Geometric mean             | (ref)                                                       | 1.84x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250823-pythonperf1-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 45.9 ms: 1.24x faster                                                      |
| pidigits       | 152 ms                                                      | 134 ms: 1.13x faster                                                       |
| nbody          | 71.9 ms                                                     | 80.1 ms: 1.11x slower                                                      |
| Geometric mean | (ref)                                                       | 1.08x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250823-pythonperf1-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_dna      | 126 ms                                                      | 114 ms: 1.11x faster                                                       |
| regex_v8       | 14.2 ms                                                     | 13.3 ms: 1.07x faster                                                      |
| regex_compile  | 87.5 ms                                                     | 94.1 ms: 1.08x slower                                                      |
| Geometric mean | (ref)                                                       | 1.02x faster                                                               |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250823-pythonperf1-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| xml_etree_iterparse  | 65.2 ms                                                     | 57.2 ms: 1.14x faster                                                      |
| xml_etree_parse      | 93.0 ms                                                     | 89.5 ms: 1.04x faster                                                      |
| json_dumps           | 5.70 ms                                                     | 5.94 ms: 1.04x slower                                                      |
| pickle               | 7.43 us                                                     | 7.82 us: 1.05x slower                                                      |
| pickle_list          | 2.83 us                                                     | 2.99 us: 1.06x slower                                                      |
| pickle_dict          | 18.4 us                                                     | 19.8 us: 1.08x slower                                                      |
| xml_etree_generate   | 55.8 ms                                                     | 62.3 ms: 1.12x slower                                                      |
| unpickle_list        | 2.75 us                                                     | 3.13 us: 1.14x slower                                                      |
| json_loads           | 13.9 us                                                     | 15.9 us: 1.14x slower                                                      |
| unpickle_pure_python | 133 us                                                      | 157 us: 1.18x slower                                                       |
| xml_etree_process    | 37.7 ms                                                     | 44.7 ms: 1.19x slower                                                      |
| pickle_pure_python   | 195 us                                                      | 232 us: 1.19x slower                                                       |
| unpickle             | 8.18 us                                                     | 10.2 us: 1.24x slower                                                      |
| tomli_loads          | 1.37 sec                                                    | 2.60 sec: 1.90x slower                                                     |
| Geometric mean       | (ref)                                                       | 1.14x slower                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250823-pythonperf1-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 19.3 ms: 1.19x slower                                                      |
| python_startup         | 19.5 ms                                                     | 25.4 ms: 1.31x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.25x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250823-pythonperf1-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| django_template | 22.9 ms                                                     | 27.2 ms: 1.19x slower                                                      |
| mako            | 7.09 ms                                                     | 10.1 ms: 1.42x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.30x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250823-pythonperf1-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pathlib                    | 80.5 ms                                                     | 29.7 ms: 2.71x faster                                                      |
| async_tree_io_tg           | 771 ms                                                      | 323 ms: 2.39x faster                                                       |
| async_tree_io              | 731 ms                                                      | 346 ms: 2.11x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 145 ms: 1.97x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 189 ms: 1.94x faster                                                       |
| async_tree_none            | 291 ms                                                      | 170 ms: 1.71x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 305 ms: 1.65x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 209 ms: 1.62x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 325 ms: 1.50x faster                                                       |
| sqlite_synth               | 1.76 us                                                     | 1.34 us: 1.31x faster                                                      |
| gc_traversal               | 1.52 ms                                                     | 1.19 ms: 1.28x faster                                                      |
| mdp                        | 1.37 sec                                                    | 1.08 sec: 1.27x faster                                                     |
| float                      | 56.8 ms                                                     | 45.9 ms: 1.24x faster                                                      |
| comprehensions             | 14.1 us                                                     | 12.2 us: 1.16x faster                                                      |
| deepcopy                   | 238 us                                                      | 205 us: 1.16x faster                                                       |
| xml_etree_iterparse        | 65.2 ms                                                     | 57.2 ms: 1.14x faster                                                      |
| pidigits                   | 152 ms                                                      | 134 ms: 1.13x faster                                                       |
| regex_dna                  | 126 ms                                                      | 114 ms: 1.11x faster                                                       |
| asyncio_tcp                | 487 ms                                                      | 439 ms: 1.11x faster                                                       |
| deepcopy_memo              | 23.7 us                                                     | 21.4 us: 1.11x faster                                                      |
| dulwich_log                | 44.3 ms                                                     | 40.8 ms: 1.08x faster                                                      |
| regex_v8                   | 14.2 ms                                                     | 13.3 ms: 1.07x faster                                                      |
| xml_etree_parse            | 93.0 ms                                                     | 89.5 ms: 1.04x faster                                                      |
| json                       | 3.05 ms                                                     | 3.08 ms: 1.01x slower                                                      |
| 2to3                       | 218 ms                                                      | 221 ms: 1.01x slower                                                       |
| logging_silent             | 60.5 ns                                                     | 61.2 ns: 1.01x slower                                                      |
| unpack_sequence            | 37.5 ns                                                     | 38.0 ns: 1.01x slower                                                      |
| coroutines                 | 14.3 ms                                                     | 14.5 ms: 1.02x slower                                                      |
| pycparser                  | 699 ms                                                      | 720 ms: 1.03x slower                                                       |
| generators                 | 22.5 ms                                                     | 23.2 ms: 1.03x slower                                                      |
| deepcopy_reduce            | 2.09 us                                                     | 2.16 us: 1.03x slower                                                      |
| async_generators           | 239 ms                                                      | 248 ms: 1.04x slower                                                       |
| sympy_sum                  | 91.5 ms                                                     | 95.2 ms: 1.04x slower                                                      |
| json_dumps                 | 5.70 ms                                                     | 5.94 ms: 1.04x slower                                                      |
| pickle                     | 7.43 us                                                     | 7.82 us: 1.05x slower                                                      |
| logging_format             | 6.72 us                                                     | 7.09 us: 1.06x slower                                                      |
| sympy_str                  | 175 ms                                                      | 185 ms: 1.06x slower                                                       |
| pyflate                    | 295 ms                                                      | 311 ms: 1.06x slower                                                       |
| pickle_list                | 2.83 us                                                     | 2.99 us: 1.06x slower                                                      |
| sympy_integrate            | 13.0 ms                                                     | 13.8 ms: 1.06x slower                                                      |
| spectral_norm              | 66.9 ms                                                     | 71.1 ms: 1.06x slower                                                      |
| logging_simple             | 6.28 us                                                     | 6.67 us: 1.06x slower                                                      |
| chaos                      | 43.3 ms                                                     | 46.5 ms: 1.07x slower                                                      |
| regex_compile              | 87.5 ms                                                     | 94.1 ms: 1.08x slower                                                      |
| pickle_dict                | 18.4 us                                                     | 19.8 us: 1.08x slower                                                      |
| raytrace                   | 192 ms                                                      | 208 ms: 1.08x slower                                                       |
| scimark_sor                | 78.8 ms                                                     | 86.6 ms: 1.10x slower                                                      |
| scimark_lu                 | 58.9 ms                                                     | 65.0 ms: 1.10x slower                                                      |
| sympy_expand               | 284 ms                                                      | 315 ms: 1.11x slower                                                       |
| nbody                      | 71.9 ms                                                     | 80.1 ms: 1.11x slower                                                      |
| xml_etree_generate         | 55.8 ms                                                     | 62.3 ms: 1.12x slower                                                      |
| pprint_safe_repr           | 513 ms                                                      | 573 ms: 1.12x slower                                                       |
| bench_mp_pool              | 69.2 ms                                                     | 77.6 ms: 1.12x slower                                                      |
| deltablue                  | 2.16 ms                                                     | 2.44 ms: 1.13x slower                                                      |
| unpickle_list              | 2.75 us                                                     | 3.13 us: 1.14x slower                                                      |
| hexiom                     | 4.10 ms                                                     | 4.67 ms: 1.14x slower                                                      |
| nqueens                    | 62.8 ms                                                     | 71.6 ms: 1.14x slower                                                      |
| json_loads                 | 13.9 us                                                     | 15.9 us: 1.14x slower                                                      |
| meteor_contest             | 74.6 ms                                                     | 85.5 ms: 1.15x slower                                                      |
| crypto_pyaes               | 48.5 ms                                                     | 55.7 ms: 1.15x slower                                                      |
| telco                      | 4.13 ms                                                     | 4.76 ms: 1.15x slower                                                      |
| scimark_monte_carlo        | 43.7 ms                                                     | 50.8 ms: 1.16x slower                                                      |
| scimark_fft                | 184 ms                                                      | 216 ms: 1.17x slower                                                       |
| unpickle_pure_python       | 133 us                                                      | 157 us: 1.18x slower                                                       |
| xml_etree_process          | 37.7 ms                                                     | 44.7 ms: 1.19x slower                                                      |
| django_template            | 22.9 ms                                                     | 27.2 ms: 1.19x slower                                                      |
| pickle_pure_python         | 195 us                                                      | 232 us: 1.19x slower                                                       |
| python_startup_no_site     | 16.2 ms                                                     | 19.3 ms: 1.19x slower                                                      |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 3.09 ms: 1.21x slower                                                      |
| fannkuch                   | 247 ms                                                      | 302 ms: 1.23x slower                                                       |
| unpickle                   | 8.18 us                                                     | 10.2 us: 1.24x slower                                                      |
| richards                   | 28.4 ms                                                     | 35.4 ms: 1.25x slower                                                      |
| bench_thread_pool          | 857 us                                                      | 1.07 ms: 1.25x slower                                                      |
| richards_super             | 32.1 ms                                                     | 41.1 ms: 1.28x slower                                                      |
| python_startup             | 19.5 ms                                                     | 25.4 ms: 1.31x slower                                                      |
| create_gc_cycles           | 752 us                                                      | 995 us: 1.32x slower                                                       |
| typing_runtime_protocols   | 95.1 us                                                     | 131 us: 1.38x slower                                                       |
| mako                       | 7.09 ms                                                     | 10.1 ms: 1.42x slower                                                      |
| pprint_pformat             | 1.05 sec                                                    | 1.69 sec: 1.62x slower                                                     |
| coverage                   | 40.8 ms                                                     | 67.3 ms: 1.65x slower                                                      |
| docutils                   | 1.66 sec                                                    | 2.74 sec: 1.65x slower                                                     |
| tomli_loads                | 1.37 sec                                                    | 2.60 sec: 1.90x slower                                                     |
| Geometric mean             | (ref)                                                       | 1.01x slower                                                               |

Benchmark hidden because not significant (3): asyncio_tcp_ssl, go, regex_effbot
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (17) of results/bm-20250823-3.15.0a0-6fcac09-NOGIL/bm-20250823-pythonperf1-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.005x faster

# HPT report

- Reliability score: 97.58% likely to be slow
- 90% likely to have a slowdown of 1.02x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown
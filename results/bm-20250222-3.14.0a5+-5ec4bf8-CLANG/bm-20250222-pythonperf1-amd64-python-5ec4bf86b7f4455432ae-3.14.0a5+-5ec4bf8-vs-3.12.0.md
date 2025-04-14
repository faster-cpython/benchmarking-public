# Results vs. 3.12.0

- fork: python
- ref: 5ec4bf86b7f4455432ae
- machine: windows-amd64
- commit hash: 5ec4bf8
- commit date: 2025-02-22
- overall geometric mean: 1.043x faster
- HPT reliability: 70.57%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250222-pythonperf1-amd64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 225 ms: 1.03x slower                                                        |
| docutils       | 1.66 sec                                                    | 1.74 sec: 1.05x slower                                                      |
| Geometric mean | (ref)                                                       | 1.04x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250222-pythonperf1-amd64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 392 ms: 1.96x faster                                                        |
| async_tree_io              | 731 ms                                                      | 402 ms: 1.82x faster                                                        |
| async_tree_memoization_tg  | 367 ms                                                      | 203 ms: 1.81x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 168 ms: 1.70x faster                                                        |
| async_tree_none            | 291 ms                                                      | 175 ms: 1.67x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 205 ms: 1.65x faster                                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 359 ms: 1.40x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 354 ms: 1.38x faster                                                        |
| Geometric mean             | (ref)                                                       | 1.66x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250222-pythonperf1-amd64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 44.4 ms: 1.28x faster                                                       |
| nbody          | 71.9 ms                                                     | 62.8 ms: 1.14x faster                                                       |
| pidigits       | 152 ms                                                      | 154 ms: 1.01x slower                                                        |
| Geometric mean | (ref)                                                       | 1.13x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250222-pythonperf1-amd64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 87.5 ms                                                     | 84.2 ms: 1.04x faster                                                       |
| regex_dna      | 126 ms                                                      | 132 ms: 1.05x slower                                                        |
| regex_v8       | 14.2 ms                                                     | 16.7 ms: 1.17x slower                                                       |
| regex_effbot   | 1.62 ms                                                     | 1.95 ms: 1.20x slower                                                       |
| Geometric mean | (ref)                                                       | 1.09x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250222-pythonperf1-amd64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pickle_dict          | 18.4 us                                                     | 15.6 us: 1.18x faster                                                       |
| unpickle_list        | 2.75 us                                                     | 2.47 us: 1.11x faster                                                       |
| tomli_loads          | 1.37 sec                                                    | 1.32 sec: 1.04x faster                                                      |
| pickle_list          | 2.83 us                                                     | 2.93 us: 1.04x slower                                                       |
| pickle               | 7.43 us                                                     | 7.80 us: 1.05x slower                                                       |
| xml_etree_iterparse  | 65.2 ms                                                     | 68.8 ms: 1.06x slower                                                       |
| pickle_pure_python   | 195 us                                                      | 210 us: 1.07x slower                                                        |
| xml_etree_parse      | 93.0 ms                                                     | 103 ms: 1.10x slower                                                        |
| unpickle_pure_python | 133 us                                                      | 147 us: 1.11x slower                                                        |
| xml_etree_generate   | 55.8 ms                                                     | 63.8 ms: 1.14x slower                                                       |
| unpickle             | 8.18 us                                                     | 9.50 us: 1.16x slower                                                       |
| xml_etree_process    | 37.7 ms                                                     | 45.1 ms: 1.19x slower                                                       |
| json_dumps           | 5.70 ms                                                     | 7.83 ms: 1.37x slower                                                       |
| json_loads           | 13.9 us                                                     | 19.5 us: 1.40x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.09x slower                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250222-pythonperf1-amd64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 19.4 ms: 1.20x slower                                                       |
| python_startup         | 19.5 ms                                                     | 25.8 ms: 1.33x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.26x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250222-pythonperf1-amd64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 7.32 ms: 1.03x slower                                                       |
| django_template | 22.9 ms                                                     | 24.2 ms: 1.06x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.04x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250222-pythonperf1-amd64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pathlib                    | 80.5 ms                                                     | 30.0 ms: 2.69x faster                                                       |
| async_tree_io_tg           | 771 ms                                                      | 392 ms: 1.96x faster                                                        |
| async_tree_io              | 731 ms                                                      | 402 ms: 1.82x faster                                                        |
| async_tree_memoization_tg  | 367 ms                                                      | 203 ms: 1.81x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 168 ms: 1.70x faster                                                        |
| async_tree_none            | 291 ms                                                      | 175 ms: 1.67x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 205 ms: 1.65x faster                                                        |
| asyncio_tcp_ssl            | 2.10 sec                                                    | 1.30 sec: 1.62x faster                                                      |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 359 ms: 1.40x faster                                                        |
| unpack_sequence            | 37.5 ns                                                     | 27.0 ns: 1.39x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 354 ms: 1.38x faster                                                        |
| deepcopy                   | 238 us                                                      | 177 us: 1.34x faster                                                        |
| generators                 | 22.5 ms                                                     | 17.1 ms: 1.32x faster                                                       |
| float                      | 56.8 ms                                                     | 44.4 ms: 1.28x faster                                                       |
| go                         | 91.6 ms                                                     | 71.6 ms: 1.28x faster                                                       |
| deepcopy_memo              | 23.7 us                                                     | 18.9 us: 1.25x faster                                                       |
| asyncio_tcp                | 487 ms                                                      | 389 ms: 1.25x faster                                                        |
| comprehensions             | 14.1 us                                                     | 11.4 us: 1.24x faster                                                       |
| pickle_dict                | 18.4 us                                                     | 15.6 us: 1.18x faster                                                       |
| deltablue                  | 2.16 ms                                                     | 1.84 ms: 1.17x faster                                                       |
| spectral_norm              | 66.9 ms                                                     | 58.4 ms: 1.15x faster                                                       |
| nbody                      | 71.9 ms                                                     | 62.8 ms: 1.14x faster                                                       |
| raytrace                   | 192 ms                                                      | 168 ms: 1.14x faster                                                        |
| scimark_sor                | 78.8 ms                                                     | 69.2 ms: 1.14x faster                                                       |
| scimark_monte_carlo        | 43.7 ms                                                     | 39.0 ms: 1.12x faster                                                       |
| unpickle_list              | 2.75 us                                                     | 2.47 us: 1.11x faster                                                       |
| chaos                      | 43.3 ms                                                     | 39.1 ms: 1.11x faster                                                       |
| deepcopy_reduce            | 2.09 us                                                     | 1.89 us: 1.11x faster                                                       |
| sqlite_synth               | 1.76 us                                                     | 1.60 us: 1.10x faster                                                       |
| coroutines                 | 14.3 ms                                                     | 13.0 ms: 1.10x faster                                                       |
| async_generators           | 239 ms                                                      | 219 ms: 1.09x faster                                                        |
| dulwich_log                | 44.3 ms                                                     | 41.7 ms: 1.06x faster                                                       |
| regex_compile              | 87.5 ms                                                     | 84.2 ms: 1.04x faster                                                       |
| tomli_loads                | 1.37 sec                                                    | 1.32 sec: 1.04x faster                                                      |
| hexiom                     | 4.10 ms                                                     | 3.98 ms: 1.03x faster                                                       |
| scimark_fft                | 184 ms                                                      | 181 ms: 1.02x faster                                                        |
| pyflate                    | 295 ms                                                      | 290 ms: 1.02x faster                                                        |
| meteor_contest             | 74.6 ms                                                     | 73.3 ms: 1.02x faster                                                       |
| logging_format             | 6.72 us                                                     | 6.61 us: 1.02x faster                                                       |
| logging_simple             | 6.28 us                                                     | 6.18 us: 1.02x faster                                                       |
| logging_silent             | 60.5 ns                                                     | 60.0 ns: 1.01x faster                                                       |
| sympy_sum                  | 91.5 ms                                                     | 91.0 ms: 1.01x faster                                                       |
| sqlglot_parse              | 804 us                                                      | 808 us: 1.00x slower                                                        |
| richards_super             | 32.1 ms                                                     | 32.2 ms: 1.00x slower                                                       |
| pidigits                   | 152 ms                                                      | 154 ms: 1.01x slower                                                        |
| pprint_pformat             | 1.05 sec                                                    | 1.06 sec: 1.01x slower                                                      |
| pprint_safe_repr           | 513 ms                                                      | 520 ms: 1.01x slower                                                        |
| pycparser                  | 699 ms                                                      | 709 ms: 1.01x slower                                                        |
| sqlglot_normalize          | 187 ms                                                      | 191 ms: 1.02x slower                                                        |
| sqlglot_optimize           | 34.5 ms                                                     | 35.3 ms: 1.02x slower                                                       |
| bench_thread_pool          | 857 us                                                      | 879 us: 1.03x slower                                                        |
| sympy_integrate            | 13.0 ms                                                     | 13.3 ms: 1.03x slower                                                       |
| mako                       | 7.09 ms                                                     | 7.32 ms: 1.03x slower                                                       |
| 2to3                       | 218 ms                                                      | 225 ms: 1.03x slower                                                        |
| pickle_list                | 2.83 us                                                     | 2.93 us: 1.04x slower                                                       |
| docutils                   | 1.66 sec                                                    | 1.74 sec: 1.05x slower                                                      |
| regex_dna                  | 126 ms                                                      | 132 ms: 1.05x slower                                                        |
| pickle                     | 7.43 us                                                     | 7.80 us: 1.05x slower                                                       |
| django_template            | 22.9 ms                                                     | 24.2 ms: 1.06x slower                                                       |
| xml_etree_iterparse        | 65.2 ms                                                     | 68.8 ms: 1.06x slower                                                       |
| sympy_expand               | 284 ms                                                      | 301 ms: 1.06x slower                                                        |
| scimark_lu                 | 58.9 ms                                                     | 63.1 ms: 1.07x slower                                                       |
| crypto_pyaes               | 48.5 ms                                                     | 52.0 ms: 1.07x slower                                                       |
| pickle_pure_python         | 195 us                                                      | 210 us: 1.07x slower                                                        |
| xml_etree_parse            | 93.0 ms                                                     | 103 ms: 1.10x slower                                                        |
| unpickle_pure_python       | 133 us                                                      | 147 us: 1.11x slower                                                        |
| fannkuch                   | 247 ms                                                      | 277 ms: 1.12x slower                                                        |
| xml_etree_generate         | 55.8 ms                                                     | 63.8 ms: 1.14x slower                                                       |
| unpickle                   | 8.18 us                                                     | 9.50 us: 1.16x slower                                                       |
| json                       | 3.05 ms                                                     | 3.55 ms: 1.16x slower                                                       |
| regex_v8                   | 14.2 ms                                                     | 16.7 ms: 1.17x slower                                                       |
| typing_runtime_protocols   | 95.1 us                                                     | 112 us: 1.18x slower                                                        |
| xml_etree_process          | 37.7 ms                                                     | 45.1 ms: 1.19x slower                                                       |
| python_startup_no_site     | 16.2 ms                                                     | 19.4 ms: 1.20x slower                                                       |
| mdp                        | 1.37 sec                                                    | 1.65 sec: 1.20x slower                                                      |
| regex_effbot               | 1.62 ms                                                     | 1.95 ms: 1.20x slower                                                       |
| telco                      | 4.13 ms                                                     | 5.10 ms: 1.23x slower                                                       |
| bench_mp_pool              | 69.2 ms                                                     | 89.9 ms: 1.30x slower                                                       |
| coverage                   | 40.8 ms                                                     | 53.1 ms: 1.30x slower                                                       |
| python_startup             | 19.5 ms                                                     | 25.8 ms: 1.33x slower                                                       |
| json_dumps                 | 5.70 ms                                                     | 7.83 ms: 1.37x slower                                                       |
| json_loads                 | 13.9 us                                                     | 19.5 us: 1.40x slower                                                       |
| gc_traversal               | 1.52 ms                                                     | 2.55 ms: 1.67x slower                                                       |
| create_gc_cycles           | 752 us                                                      | 1.33 ms: 1.77x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.05x faster                                                                |

Benchmark hidden because not significant (5): richards, scimark_sparse_mat_mult, sqlglot_transpile, nqueens, sympy_str
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (13) of results/bm-20250222-3.14.0a5+-5ec4bf8-CLANG/bm-20250222-pythonperf1-amd64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.043x faster

# HPT report

- Reliability score: 70.57% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown
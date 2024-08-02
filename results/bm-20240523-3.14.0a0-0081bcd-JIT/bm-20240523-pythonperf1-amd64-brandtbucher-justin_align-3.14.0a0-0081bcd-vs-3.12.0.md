# Results vs. 3.12.0

- fork: brandtbucher
- ref: justin_align
- machine: windows-amd64
- commit hash: 0081bcd
- commit date: 2024-05-23
- overall geometric mean: 1.05x faster
- HPT reliability: 99.56%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240523-pythonperf1-amd64-brandtbucher-justin_align-3.14.0a0-0081bcd |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 233 ms: 1.07x slower                                                     |
| chameleon      | 4.98 ms                                                     | 5.08 ms: 1.02x slower                                                    |
| docutils       | 1.66 sec                                                    | 1.77 sec: 1.07x slower                                                   |
| tornado_http   | 89.5 ms                                                     | 85.4 ms: 1.05x faster                                                    |
| Geometric mean | (ref)                                                       | 1.03x slower                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240523-pythonperf1-amd64-brandtbucher-justin_align-3.14.0a0-0081bcd |
|----------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 367 ms                                                      | 275 ms: 1.34x faster                                                     |
| async_tree_none_tg         | 285 ms                                                      | 218 ms: 1.31x faster                                                     |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 389 ms: 1.29x faster                                                     |
| async_tree_none            | 291 ms                                                      | 233 ms: 1.25x faster                                                     |
| async_tree_io_tg           | 771 ms                                                      | 625 ms: 1.23x faster                                                     |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 404 ms: 1.21x faster                                                     |
| async_tree_memoization     | 339 ms                                                      | 283 ms: 1.20x faster                                                     |
| async_tree_io              | 731 ms                                                      | 611 ms: 1.20x faster                                                     |
| Geometric mean             | (ref)                                                       | 1.25x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240523-pythonperf1-amd64-brandtbucher-justin_align-3.14.0a0-0081bcd |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------:|
| nbody          | 71.9 ms                                                     | 51.1 ms: 1.41x faster                                                    |
| float          | 56.8 ms                                                     | 44.6 ms: 1.27x faster                                                    |
| pidigits       | 152 ms                                                      | 149 ms: 1.02x faster                                                     |
| Geometric mean | (ref)                                                       | 1.22x faster                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240523-pythonperf1-amd64-brandtbucher-justin_align-3.14.0a0-0081bcd |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_dna      | 126 ms                                                      | 121 ms: 1.04x faster                                                     |
| regex_effbot   | 1.62 ms                                                     | 1.58 ms: 1.02x faster                                                    |
| regex_v8       | 14.2 ms                                                     | 14.8 ms: 1.04x slower                                                    |
| Geometric mean | (ref)                                                       | 1.01x faster                                                             |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240523-pythonperf1-amd64-brandtbucher-justin_align-3.14.0a0-0081bcd |
|----------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------:|
| pickle_pure_python   | 195 us                                                      | 173 us: 1.13x faster                                                     |
| tomli_loads          | 1.37 sec                                                    | 1.24 sec: 1.11x faster                                                   |
| xml_etree_iterparse  | 65.2 ms                                                     | 59.8 ms: 1.09x faster                                                    |
| xml_etree_generate   | 55.8 ms                                                     | 51.5 ms: 1.08x faster                                                    |
| unpickle_pure_python | 133 us                                                      | 127 us: 1.05x faster                                                     |
| xml_etree_process    | 37.7 ms                                                     | 36.4 ms: 1.04x faster                                                    |
| xml_etree_parse      | 93.0 ms                                                     | 89.9 ms: 1.03x faster                                                    |
| pickle_dict          | 18.4 us                                                     | 17.8 us: 1.03x faster                                                    |
| json_dumps           | 5.70 ms                                                     | 5.65 ms: 1.01x faster                                                    |
| unpickle_list        | 2.75 us                                                     | 2.79 us: 1.02x slower                                                    |
| pickle               | 7.43 us                                                     | 7.55 us: 1.02x slower                                                    |
| unpickle             | 8.18 us                                                     | 8.68 us: 1.06x slower                                                    |
| Geometric mean       | (ref)                                                       | 1.03x faster                                                             |

Benchmark hidden because not significant (2): json_loads, pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240523-pythonperf1-amd64-brandtbucher-justin_align-3.14.0a0-0081bcd |
|------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 18.2 ms: 1.12x slower                                                    |
| python_startup         | 19.5 ms                                                     | 21.8 ms: 1.12x slower                                                    |
| Geometric mean         | (ref)                                                       | 1.12x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240523-pythonperf1-amd64-brandtbucher-justin_align-3.14.0a0-0081bcd |
|-----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 5.00 ms: 1.42x faster                                                    |
| django_template | 22.9 ms                                                     | 25.6 ms: 1.11x slower                                                    |
| Geometric mean  | (ref)                                                       | 1.13x faster                                                             |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240523-pythonperf1-amd64-brandtbucher-justin_align-3.14.0a0-0081bcd |
|----------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------:|
| asyncio_tcp_ssl            | 2.10 sec                                                    | 1.45 sec: 1.44x faster                                                   |
| mako                       | 7.09 ms                                                     | 5.00 ms: 1.42x faster                                                    |
| nbody                      | 71.9 ms                                                     | 51.1 ms: 1.41x faster                                                    |
| spectral_norm              | 66.9 ms                                                     | 47.8 ms: 1.40x faster                                                    |
| comprehensions             | 14.1 us                                                     | 10.3 us: 1.38x faster                                                    |
| async_tree_memoization_tg  | 367 ms                                                      | 275 ms: 1.34x faster                                                     |
| async_tree_none_tg         | 285 ms                                                      | 218 ms: 1.31x faster                                                     |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 389 ms: 1.29x faster                                                     |
| float                      | 56.8 ms                                                     | 44.6 ms: 1.27x faster                                                    |
| async_tree_none            | 291 ms                                                      | 233 ms: 1.25x faster                                                     |
| scimark_fft                | 184 ms                                                      | 149 ms: 1.24x faster                                                     |
| async_tree_io_tg           | 771 ms                                                      | 625 ms: 1.23x faster                                                     |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 404 ms: 1.21x faster                                                     |
| async_tree_memoization     | 339 ms                                                      | 283 ms: 1.20x faster                                                     |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.14 ms: 1.20x faster                                                    |
| async_tree_io              | 731 ms                                                      | 611 ms: 1.20x faster                                                     |
| crypto_pyaes               | 48.5 ms                                                     | 41.0 ms: 1.18x faster                                                    |
| deepcopy_memo              | 23.7 us                                                     | 20.3 us: 1.17x faster                                                    |
| scimark_monte_carlo        | 43.7 ms                                                     | 37.9 ms: 1.15x faster                                                    |
| pyflate                    | 295 ms                                                      | 259 ms: 1.14x faster                                                     |
| pprint_pformat             | 1.05 sec                                                    | 920 ms: 1.14x faster                                                     |
| pprint_safe_repr           | 513 ms                                                      | 453 ms: 1.13x faster                                                     |
| pickle_pure_python         | 195 us                                                      | 173 us: 1.13x faster                                                     |
| tomli_loads                | 1.37 sec                                                    | 1.24 sec: 1.11x faster                                                   |
| raytrace                   | 192 ms                                                      | 176 ms: 1.09x faster                                                     |
| xml_etree_iterparse        | 65.2 ms                                                     | 59.8 ms: 1.09x faster                                                    |
| logging_silent             | 60.5 ns                                                     | 55.5 ns: 1.09x faster                                                    |
| sqlite_synth               | 1.76 us                                                     | 1.62 us: 1.09x faster                                                    |
| chaos                      | 43.3 ms                                                     | 39.9 ms: 1.09x faster                                                    |
| logging_simple             | 6.28 us                                                     | 5.79 us: 1.08x faster                                                    |
| xml_etree_generate         | 55.8 ms                                                     | 51.5 ms: 1.08x faster                                                    |
| logging_format             | 6.72 us                                                     | 6.23 us: 1.08x faster                                                    |
| fannkuch                   | 247 ms                                                      | 230 ms: 1.07x faster                                                     |
| json                       | 3.05 ms                                                     | 2.88 ms: 1.06x faster                                                    |
| generators                 | 22.5 ms                                                     | 21.3 ms: 1.06x faster                                                    |
| tornado_http               | 89.5 ms                                                     | 85.4 ms: 1.05x faster                                                    |
| unpickle_pure_python       | 133 us                                                      | 127 us: 1.05x faster                                                     |
| nqueens                    | 62.8 ms                                                     | 60.1 ms: 1.05x faster                                                    |
| coroutines                 | 14.3 ms                                                     | 13.7 ms: 1.04x faster                                                    |
| regex_dna                  | 126 ms                                                      | 121 ms: 1.04x faster                                                     |
| xml_etree_process          | 37.7 ms                                                     | 36.4 ms: 1.04x faster                                                    |
| meteor_contest             | 74.6 ms                                                     | 72.1 ms: 1.04x faster                                                    |
| xml_etree_parse            | 93.0 ms                                                     | 89.9 ms: 1.03x faster                                                    |
| pickle_dict                | 18.4 us                                                     | 17.8 us: 1.03x faster                                                    |
| bench_thread_pool          | 857 us                                                      | 833 us: 1.03x faster                                                     |
| regex_effbot               | 1.62 ms                                                     | 1.58 ms: 1.02x faster                                                    |
| pathlib                    | 80.5 ms                                                     | 78.7 ms: 1.02x faster                                                    |
| pidigits                   | 152 ms                                                      | 149 ms: 1.02x faster                                                     |
| json_dumps                 | 5.70 ms                                                     | 5.65 ms: 1.01x faster                                                    |
| sqlglot_transpile          | 1.02 ms                                                     | 1.03 ms: 1.01x slower                                                    |
| bench_mp_pool              | 69.2 ms                                                     | 70.1 ms: 1.01x slower                                                    |
| unpickle_list              | 2.75 us                                                     | 2.79 us: 1.02x slower                                                    |
| pickle                     | 7.43 us                                                     | 7.55 us: 1.02x slower                                                    |
| deepcopy                   | 238 us                                                      | 242 us: 1.02x slower                                                     |
| sympy_str                  | 175 ms                                                      | 178 ms: 1.02x slower                                                     |
| sympy_sum                  | 91.5 ms                                                     | 93.3 ms: 1.02x slower                                                    |
| chameleon                  | 4.98 ms                                                     | 5.08 ms: 1.02x slower                                                    |
| gc_traversal               | 1.52 ms                                                     | 1.55 ms: 1.02x slower                                                    |
| go                         | 91.6 ms                                                     | 94.5 ms: 1.03x slower                                                    |
| richards                   | 28.4 ms                                                     | 29.5 ms: 1.04x slower                                                    |
| regex_v8                   | 14.2 ms                                                     | 14.8 ms: 1.04x slower                                                    |
| richards_super             | 32.1 ms                                                     | 33.4 ms: 1.04x slower                                                    |
| scimark_sor                | 78.8 ms                                                     | 83.4 ms: 1.06x slower                                                    |
| unpickle                   | 8.18 us                                                     | 8.68 us: 1.06x slower                                                    |
| sqlglot_optimize           | 34.5 ms                                                     | 36.7 ms: 1.06x slower                                                    |
| async_generators           | 239 ms                                                      | 254 ms: 1.06x slower                                                     |
| docutils                   | 1.66 sec                                                    | 1.77 sec: 1.07x slower                                                   |
| 2to3                       | 218 ms                                                      | 233 ms: 1.07x slower                                                     |
| sympy_integrate            | 13.0 ms                                                     | 13.9 ms: 1.07x slower                                                    |
| mdp                        | 1.37 sec                                                    | 1.49 sec: 1.09x slower                                                   |
| deltablue                  | 2.16 ms                                                     | 2.37 ms: 1.10x slower                                                    |
| sympy_expand               | 284 ms                                                      | 312 ms: 1.10x slower                                                     |
| telco                      | 4.13 ms                                                     | 4.57 ms: 1.11x slower                                                    |
| django_template            | 22.9 ms                                                     | 25.6 ms: 1.11x slower                                                    |
| python_startup_no_site     | 16.2 ms                                                     | 18.2 ms: 1.12x slower                                                    |
| python_startup             | 19.5 ms                                                     | 21.8 ms: 1.12x slower                                                    |
| coverage                   | 40.8 ms                                                     | 46.0 ms: 1.13x slower                                                    |
| hexiom                     | 4.10 ms                                                     | 4.66 ms: 1.14x slower                                                    |
| pycparser                  | 699 ms                                                      | 803 ms: 1.15x slower                                                     |
| scimark_lu                 | 58.9 ms                                                     | 67.8 ms: 1.15x slower                                                    |
| typing_runtime_protocols   | 95.1 us                                                     | 113 us: 1.18x slower                                                     |
| create_gc_cycles           | 752 us                                                      | 904 us: 1.20x slower                                                     |
| Geometric mean             | (ref)                                                       | 1.05x faster                                                             |

Benchmark hidden because not significant (6): asyncio_tcp, regex_compile, deepcopy_reduce, sqlglot_parse, json_loads, pickle_list
Ignored benchmarks (8) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, dask, dulwich_log, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, unpack_sequence
Ignored benchmarks (6) of results/bm-20240523-3.14.0a0-0081bcd-JIT/bm-20240523-pythonperf1-amd64-brandtbucher-justin_align-3.14.0a0-0081bcd.json: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 99.56% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown
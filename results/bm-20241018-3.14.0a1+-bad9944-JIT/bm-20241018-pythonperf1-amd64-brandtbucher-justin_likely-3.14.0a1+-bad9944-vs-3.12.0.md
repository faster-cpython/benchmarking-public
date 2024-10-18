# Results vs. 3.12.0

- fork: brandtbucher
- ref: justin_likely
- machine: windows-amd64
- commit hash: bad9944
- commit date: 2024-10-18
- overall geometric mean: 1.00x slower
- HPT reliability: 54.72%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241018-pythonperf1-amd64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 250 ms: 1.15x slower                                                       |
| docutils       | 1.66 sec                                                    | 1.93 sec: 1.16x slower                                                     |
| tornado_http   | 89.5 ms                                                     | 99.5 ms: 1.11x slower                                                      |
| Geometric mean | (ref)                                                       | 1.14x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241018-pythonperf1-amd64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 367 ms                                                      | 260 ms: 1.41x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 210 ms: 1.36x faster                                                       |
| async_tree_none            | 291 ms                                                      | 220 ms: 1.32x faster                                                       |
| async_tree_io              | 731 ms                                                      | 554 ms: 1.32x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 385 ms: 1.27x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 399 ms: 1.26x faster                                                       |
| async_tree_io_tg           | 771 ms                                                      | 632 ms: 1.22x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 281 ms: 1.21x faster                                                       |
| Geometric mean             | (ref)                                                       | 1.29x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241018-pythonperf1-amd64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 71.9 ms                                                     | 55.0 ms: 1.31x faster                                                      |
| float          | 56.8 ms                                                     | 46.5 ms: 1.22x faster                                                      |
| pidigits       | 152 ms                                                      | 147 ms: 1.03x faster                                                       |
| Geometric mean | (ref)                                                       | 1.18x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241018-pythonperf1-amd64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_dna      | 126 ms                                                      | 117 ms: 1.08x faster                                                       |
| regex_v8       | 14.2 ms                                                     | 14.8 ms: 1.04x slower                                                      |
| regex_compile  | 87.5 ms                                                     | 92.9 ms: 1.06x slower                                                      |
| Geometric mean | (ref)                                                       | 1.00x slower                                                               |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241018-pythonperf1-amd64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| xml_etree_generate   | 55.8 ms                                                     | 51.5 ms: 1.08x faster                                                      |
| tomli_loads          | 1.37 sec                                                    | 1.29 sec: 1.06x faster                                                     |
| xml_etree_process    | 37.7 ms                                                     | 36.5 ms: 1.03x faster                                                      |
| xml_etree_iterparse  | 65.2 ms                                                     | 63.5 ms: 1.03x faster                                                      |
| pickle_dict          | 18.4 us                                                     | 18.0 us: 1.02x faster                                                      |
| pickle               | 7.43 us                                                     | 7.52 us: 1.01x slower                                                      |
| pickle_pure_python   | 195 us                                                      | 198 us: 1.01x slower                                                       |
| xml_etree_parse      | 93.0 ms                                                     | 95.9 ms: 1.03x slower                                                      |
| json_loads           | 13.9 us                                                     | 14.4 us: 1.03x slower                                                      |
| unpickle_list        | 2.75 us                                                     | 2.87 us: 1.05x slower                                                      |
| unpickle_pure_python | 133 us                                                      | 143 us: 1.07x slower                                                       |
| json_dumps           | 5.70 ms                                                     | 6.16 ms: 1.08x slower                                                      |
| unpickle             | 8.18 us                                                     | 8.99 us: 1.10x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.01x slower                                                               |

Benchmark hidden because not significant (1): pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241018-pythonperf1-amd64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 18.7 ms: 1.15x slower                                                      |
| python_startup         | 19.5 ms                                                     | 24.4 ms: 1.25x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.20x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241018-pythonperf1-amd64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 5.13 ms: 1.38x faster                                                      |
| django_template | 22.9 ms                                                     | 27.7 ms: 1.21x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.07x faster                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241018-pythonperf1-amd64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 367 ms                                                      | 260 ms: 1.41x faster                                                       |
| deepcopy_memo              | 23.7 us                                                     | 16.8 us: 1.41x faster                                                      |
| mako                       | 7.09 ms                                                     | 5.13 ms: 1.38x faster                                                      |
| asyncio_tcp_ssl            | 2.10 sec                                                    | 1.54 sec: 1.36x faster                                                     |
| async_tree_none_tg         | 285 ms                                                      | 210 ms: 1.36x faster                                                       |
| async_tree_none            | 291 ms                                                      | 220 ms: 1.32x faster                                                       |
| async_tree_io              | 731 ms                                                      | 554 ms: 1.32x faster                                                       |
| nbody                      | 71.9 ms                                                     | 55.0 ms: 1.31x faster                                                      |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 385 ms: 1.27x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 399 ms: 1.26x faster                                                       |
| spectral_norm              | 66.9 ms                                                     | 53.9 ms: 1.24x faster                                                      |
| deepcopy                   | 238 us                                                      | 194 us: 1.23x faster                                                       |
| float                      | 56.8 ms                                                     | 46.5 ms: 1.22x faster                                                      |
| async_tree_io_tg           | 771 ms                                                      | 632 ms: 1.22x faster                                                       |
| scimark_sor                | 78.8 ms                                                     | 65.1 ms: 1.21x faster                                                      |
| async_tree_memoization     | 339 ms                                                      | 281 ms: 1.21x faster                                                       |
| crypto_pyaes               | 48.5 ms                                                     | 40.8 ms: 1.19x faster                                                      |
| comprehensions             | 14.1 us                                                     | 11.9 us: 1.19x faster                                                      |
| scimark_monte_carlo        | 43.7 ms                                                     | 37.1 ms: 1.18x faster                                                      |
| scimark_fft                | 184 ms                                                      | 157 ms: 1.17x faster                                                       |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.23 ms: 1.15x faster                                                      |
| deepcopy_reduce            | 2.09 us                                                     | 1.88 us: 1.11x faster                                                      |
| sqlite_synth               | 1.76 us                                                     | 1.59 us: 1.11x faster                                                      |
| xml_etree_generate         | 55.8 ms                                                     | 51.5 ms: 1.08x faster                                                      |
| regex_dna                  | 126 ms                                                      | 117 ms: 1.08x faster                                                       |
| logging_silent             | 60.5 ns                                                     | 56.1 ns: 1.08x faster                                                      |
| pprint_pformat             | 1.05 sec                                                    | 972 ms: 1.08x faster                                                       |
| dulwich_log                | 44.3 ms                                                     | 41.2 ms: 1.07x faster                                                      |
| pprint_safe_repr           | 513 ms                                                      | 480 ms: 1.07x faster                                                       |
| scimark_lu                 | 58.9 ms                                                     | 55.2 ms: 1.07x faster                                                      |
| tomli_loads                | 1.37 sec                                                    | 1.29 sec: 1.06x faster                                                     |
| json                       | 3.05 ms                                                     | 2.95 ms: 1.03x faster                                                      |
| xml_etree_process          | 37.7 ms                                                     | 36.5 ms: 1.03x faster                                                      |
| pidigits                   | 152 ms                                                      | 147 ms: 1.03x faster                                                       |
| xml_etree_iterparse        | 65.2 ms                                                     | 63.5 ms: 1.03x faster                                                      |
| fannkuch                   | 247 ms                                                      | 240 ms: 1.03x faster                                                       |
| chaos                      | 43.3 ms                                                     | 42.2 ms: 1.03x faster                                                      |
| pickle_dict                | 18.4 us                                                     | 18.0 us: 1.02x faster                                                      |
| coroutines                 | 14.3 ms                                                     | 14.1 ms: 1.01x faster                                                      |
| logging_format             | 6.72 us                                                     | 6.67 us: 1.01x faster                                                      |
| go                         | 91.6 ms                                                     | 92.0 ms: 1.00x slower                                                      |
| pickle                     | 7.43 us                                                     | 7.52 us: 1.01x slower                                                      |
| nqueens                    | 62.8 ms                                                     | 63.7 ms: 1.01x slower                                                      |
| pickle_pure_python         | 195 us                                                      | 198 us: 1.01x slower                                                       |
| meteor_contest             | 74.6 ms                                                     | 76.0 ms: 1.02x slower                                                      |
| xml_etree_parse            | 93.0 ms                                                     | 95.9 ms: 1.03x slower                                                      |
| json_loads                 | 13.9 us                                                     | 14.4 us: 1.03x slower                                                      |
| regex_v8                   | 14.2 ms                                                     | 14.8 ms: 1.04x slower                                                      |
| unpickle_list              | 2.75 us                                                     | 2.87 us: 1.05x slower                                                      |
| pycparser                  | 699 ms                                                      | 740 ms: 1.06x slower                                                       |
| regex_compile              | 87.5 ms                                                     | 92.9 ms: 1.06x slower                                                      |
| generators                 | 22.5 ms                                                     | 23.9 ms: 1.06x slower                                                      |
| unpickle_pure_python       | 133 us                                                      | 143 us: 1.07x slower                                                       |
| json_dumps                 | 5.70 ms                                                     | 6.16 ms: 1.08x slower                                                      |
| deltablue                  | 2.16 ms                                                     | 2.35 ms: 1.09x slower                                                      |
| unpickle                   | 8.18 us                                                     | 8.99 us: 1.10x slower                                                      |
| telco                      | 4.13 ms                                                     | 4.56 ms: 1.10x slower                                                      |
| raytrace                   | 192 ms                                                      | 213 ms: 1.11x slower                                                       |
| tornado_http               | 89.5 ms                                                     | 99.5 ms: 1.11x slower                                                      |
| sympy_str                  | 175 ms                                                      | 195 ms: 1.12x slower                                                       |
| mdp                        | 1.37 sec                                                    | 1.53 sec: 1.12x slower                                                     |
| async_generators           | 239 ms                                                      | 268 ms: 1.12x slower                                                       |
| sqlglot_parse              | 804 us                                                      | 908 us: 1.13x slower                                                       |
| sqlglot_normalize          | 187 ms                                                      | 212 ms: 1.13x slower                                                       |
| sympy_sum                  | 91.5 ms                                                     | 104 ms: 1.14x slower                                                       |
| 2to3                       | 218 ms                                                      | 250 ms: 1.15x slower                                                       |
| python_startup_no_site     | 16.2 ms                                                     | 18.7 ms: 1.15x slower                                                      |
| docutils                   | 1.66 sec                                                    | 1.93 sec: 1.16x slower                                                     |
| sympy_expand               | 284 ms                                                      | 332 ms: 1.17x slower                                                       |
| sqlglot_transpile          | 1.02 ms                                                     | 1.21 ms: 1.19x slower                                                      |
| richards_super             | 32.1 ms                                                     | 38.6 ms: 1.20x slower                                                      |
| coverage                   | 40.8 ms                                                     | 49.2 ms: 1.21x slower                                                      |
| django_template            | 22.9 ms                                                     | 27.7 ms: 1.21x slower                                                      |
| richards                   | 28.4 ms                                                     | 34.3 ms: 1.21x slower                                                      |
| sympy_integrate            | 13.0 ms                                                     | 15.9 ms: 1.23x slower                                                      |
| typing_runtime_protocols   | 95.1 us                                                     | 118 us: 1.24x slower                                                       |
| python_startup             | 19.5 ms                                                     | 24.4 ms: 1.25x slower                                                      |
| sqlglot_optimize           | 34.5 ms                                                     | 43.4 ms: 1.26x slower                                                      |
| hexiom                     | 4.10 ms                                                     | 5.25 ms: 1.28x slower                                                      |
| gc_traversal               | 1.52 ms                                                     | 1.96 ms: 1.29x slower                                                      |
| bench_mp_pool              | 69.2 ms                                                     | 89.7 ms: 1.30x slower                                                      |
| asyncio_tcp                | 487 ms                                                      | 650 ms: 1.33x slower                                                       |
| unpack_sequence            | 37.5 ns                                                     | 59.5 ns: 1.59x slower                                                      |
| create_gc_cycles           | 752 us                                                      | 1.41 ms: 1.87x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.00x slower                                                               |

Benchmark hidden because not significant (6): bench_thread_pool, regex_effbot, logging_simple, pickle_list, pathlib, pyflate
Ignored benchmarks (6) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (6) of results/bm-20241018-3.14.0a1+-bad9944-JIT/bm-20241018-pythonperf1-amd64-brandtbucher-justin_likely-3.14.0a1+-bad9944.json: genshi_text, genshi_xml, html5lib, pylint, sphinx, thrift

# HPT report

- Reliability score: 54.72% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown
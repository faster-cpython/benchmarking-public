# Results vs. 3.12.0

- fork: python
- ref: caf6064a1bc15ac344af
- machine: windows-amd64
- commit hash: caf6064
- commit date: 2024-05-18
- overall geometric mean: 1.05x faster
- HPT reliability: 99.27%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240518-pythonperf1-amd64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 232 ms: 1.07x slower                                                       |
| chameleon      | 4.98 ms                                                     | 5.11 ms: 1.03x slower                                                      |
| docutils       | 1.66 sec                                                    | 1.76 sec: 1.06x slower                                                     |
| tornado_http   | 89.5 ms                                                     | 84.9 ms: 1.05x faster                                                      |
| Geometric mean | (ref)                                                       | 1.02x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240518-pythonperf1-amd64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 367 ms                                                      | 269 ms: 1.37x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 211 ms: 1.35x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 388 ms: 1.30x faster                                                       |
| async_tree_none            | 291 ms                                                      | 226 ms: 1.29x faster                                                       |
| async_tree_io_tg           | 771 ms                                                      | 612 ms: 1.26x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 272 ms: 1.25x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 394 ms: 1.24x faster                                                       |
| async_tree_io              | 731 ms                                                      | 598 ms: 1.22x faster                                                       |
| Geometric mean             | (ref)                                                       | 1.28x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240518-pythonperf1-amd64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 71.9 ms                                                     | 50.5 ms: 1.42x faster                                                      |
| float          | 56.8 ms                                                     | 44.2 ms: 1.28x faster                                                      |
| pidigits       | 152 ms                                                      | 149 ms: 1.02x faster                                                       |
| Geometric mean | (ref)                                                       | 1.23x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240518-pythonperf1-amd64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_dna      | 126 ms                                                      | 119 ms: 1.06x faster                                                       |
| regex_effbot   | 1.62 ms                                                     | 1.57 ms: 1.03x faster                                                      |
| regex_compile  | 87.5 ms                                                     | 87.2 ms: 1.00x faster                                                      |
| regex_v8       | 14.2 ms                                                     | 14.3 ms: 1.01x slower                                                      |
| Geometric mean | (ref)                                                       | 1.02x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240518-pythonperf1-amd64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pickle_pure_python   | 195 us                                                      | 173 us: 1.13x faster                                                       |
| tomli_loads          | 1.37 sec                                                    | 1.23 sec: 1.11x faster                                                     |
| xml_etree_iterparse  | 65.2 ms                                                     | 60.1 ms: 1.08x faster                                                      |
| xml_etree_generate   | 55.8 ms                                                     | 51.8 ms: 1.08x faster                                                      |
| unpickle_pure_python | 133 us                                                      | 125 us: 1.06x faster                                                       |
| pickle_dict          | 18.4 us                                                     | 17.5 us: 1.05x faster                                                      |
| xml_etree_process    | 37.7 ms                                                     | 36.4 ms: 1.04x faster                                                      |
| xml_etree_parse      | 93.0 ms                                                     | 91.5 ms: 1.02x faster                                                      |
| pickle               | 7.43 us                                                     | 7.37 us: 1.01x faster                                                      |
| json_dumps           | 5.70 ms                                                     | 5.75 ms: 1.01x slower                                                      |
| json_loads           | 13.9 us                                                     | 14.1 us: 1.01x slower                                                      |
| pickle_list          | 2.83 us                                                     | 2.90 us: 1.03x slower                                                      |
| unpickle_list        | 2.75 us                                                     | 2.87 us: 1.04x slower                                                      |
| unpickle             | 8.18 us                                                     | 8.69 us: 1.06x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.03x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240518-pythonperf1-amd64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 18.1 ms: 1.11x slower                                                      |
| python_startup         | 19.5 ms                                                     | 21.8 ms: 1.12x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.12x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240518-pythonperf1-amd64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 5.17 ms: 1.37x faster                                                      |
| django_template | 22.9 ms                                                     | 25.6 ms: 1.12x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.11x faster                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240518-pythonperf1-amd64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| spectral_norm              | 66.9 ms                                                     | 45.1 ms: 1.49x faster                                                      |
| asyncio_tcp_ssl            | 2.10 sec                                                    | 1.46 sec: 1.43x faster                                                     |
| nbody                      | 71.9 ms                                                     | 50.5 ms: 1.42x faster                                                      |
| comprehensions             | 14.1 us                                                     | 10.3 us: 1.37x faster                                                      |
| mako                       | 7.09 ms                                                     | 5.17 ms: 1.37x faster                                                      |
| async_tree_memoization_tg  | 367 ms                                                      | 269 ms: 1.37x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 211 ms: 1.35x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 388 ms: 1.30x faster                                                       |
| async_tree_none            | 291 ms                                                      | 226 ms: 1.29x faster                                                       |
| float                      | 56.8 ms                                                     | 44.2 ms: 1.28x faster                                                      |
| async_tree_io_tg           | 771 ms                                                      | 612 ms: 1.26x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 272 ms: 1.25x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 394 ms: 1.24x faster                                                       |
| async_tree_io              | 731 ms                                                      | 598 ms: 1.22x faster                                                       |
| scimark_fft                | 184 ms                                                      | 151 ms: 1.22x faster                                                       |
| crypto_pyaes               | 48.5 ms                                                     | 41.0 ms: 1.18x faster                                                      |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.17 ms: 1.18x faster                                                      |
| deepcopy_memo              | 23.7 us                                                     | 20.6 us: 1.15x faster                                                      |
| pyflate                    | 295 ms                                                      | 257 ms: 1.15x faster                                                       |
| scimark_monte_carlo        | 43.7 ms                                                     | 38.5 ms: 1.14x faster                                                      |
| pickle_pure_python         | 195 us                                                      | 173 us: 1.13x faster                                                       |
| sqlite_synth               | 1.76 us                                                     | 1.56 us: 1.13x faster                                                      |
| pprint_safe_repr           | 513 ms                                                      | 459 ms: 1.12x faster                                                       |
| tomli_loads                | 1.37 sec                                                    | 1.23 sec: 1.11x faster                                                     |
| fannkuch                   | 247 ms                                                      | 222 ms: 1.11x faster                                                       |
| pprint_pformat             | 1.05 sec                                                    | 945 ms: 1.11x faster                                                       |
| chaos                      | 43.3 ms                                                     | 39.2 ms: 1.11x faster                                                      |
| raytrace                   | 192 ms                                                      | 176 ms: 1.09x faster                                                       |
| logging_simple             | 6.28 us                                                     | 5.75 us: 1.09x faster                                                      |
| xml_etree_iterparse        | 65.2 ms                                                     | 60.1 ms: 1.08x faster                                                      |
| coroutines                 | 14.3 ms                                                     | 13.2 ms: 1.08x faster                                                      |
| logging_format             | 6.72 us                                                     | 6.21 us: 1.08x faster                                                      |
| logging_silent             | 60.5 ns                                                     | 56.0 ns: 1.08x faster                                                      |
| xml_etree_generate         | 55.8 ms                                                     | 51.8 ms: 1.08x faster                                                      |
| unpickle_pure_python       | 133 us                                                      | 125 us: 1.06x faster                                                       |
| regex_dna                  | 126 ms                                                      | 119 ms: 1.06x faster                                                       |
| tornado_http               | 89.5 ms                                                     | 84.9 ms: 1.05x faster                                                      |
| pickle_dict                | 18.4 us                                                     | 17.5 us: 1.05x faster                                                      |
| json                       | 3.05 ms                                                     | 2.92 ms: 1.05x faster                                                      |
| generators                 | 22.5 ms                                                     | 21.6 ms: 1.04x faster                                                      |
| xml_etree_process          | 37.7 ms                                                     | 36.4 ms: 1.04x faster                                                      |
| regex_effbot               | 1.62 ms                                                     | 1.57 ms: 1.03x faster                                                      |
| nqueens                    | 62.8 ms                                                     | 61.0 ms: 1.03x faster                                                      |
| pathlib                    | 80.5 ms                                                     | 78.8 ms: 1.02x faster                                                      |
| pidigits                   | 152 ms                                                      | 149 ms: 1.02x faster                                                       |
| xml_etree_parse            | 93.0 ms                                                     | 91.5 ms: 1.02x faster                                                      |
| deepcopy_reduce            | 2.09 us                                                     | 2.07 us: 1.01x faster                                                      |
| pickle                     | 7.43 us                                                     | 7.37 us: 1.01x faster                                                      |
| sqlglot_parse              | 804 us                                                      | 799 us: 1.01x faster                                                       |
| regex_compile              | 87.5 ms                                                     | 87.2 ms: 1.00x faster                                                      |
| regex_v8                   | 14.2 ms                                                     | 14.3 ms: 1.01x slower                                                      |
| json_dumps                 | 5.70 ms                                                     | 5.75 ms: 1.01x slower                                                      |
| sympy_sum                  | 91.5 ms                                                     | 92.5 ms: 1.01x slower                                                      |
| sympy_str                  | 175 ms                                                      | 177 ms: 1.01x slower                                                       |
| sqlglot_transpile          | 1.02 ms                                                     | 1.03 ms: 1.01x slower                                                      |
| json_loads                 | 13.9 us                                                     | 14.1 us: 1.01x slower                                                      |
| gc_traversal               | 1.52 ms                                                     | 1.55 ms: 1.02x slower                                                      |
| go                         | 91.6 ms                                                     | 93.8 ms: 1.02x slower                                                      |
| chameleon                  | 4.98 ms                                                     | 5.11 ms: 1.03x slower                                                      |
| pickle_list                | 2.83 us                                                     | 2.90 us: 1.03x slower                                                      |
| bench_mp_pool              | 69.2 ms                                                     | 71.3 ms: 1.03x slower                                                      |
| richards_super             | 32.1 ms                                                     | 33.3 ms: 1.04x slower                                                      |
| richards                   | 28.4 ms                                                     | 29.5 ms: 1.04x slower                                                      |
| unpickle_list              | 2.75 us                                                     | 2.87 us: 1.04x slower                                                      |
| scimark_sor                | 78.8 ms                                                     | 82.8 ms: 1.05x slower                                                      |
| docutils                   | 1.66 sec                                                    | 1.76 sec: 1.06x slower                                                     |
| unpickle                   | 8.18 us                                                     | 8.69 us: 1.06x slower                                                      |
| sqlglot_optimize           | 34.5 ms                                                     | 36.7 ms: 1.06x slower                                                      |
| 2to3                       | 218 ms                                                      | 232 ms: 1.07x slower                                                       |
| pycparser                  | 699 ms                                                      | 750 ms: 1.07x slower                                                       |
| async_generators           | 239 ms                                                      | 257 ms: 1.07x slower                                                       |
| sympy_integrate            | 13.0 ms                                                     | 14.0 ms: 1.08x slower                                                      |
| deltablue                  | 2.16 ms                                                     | 2.33 ms: 1.08x slower                                                      |
| mdp                        | 1.37 sec                                                    | 1.48 sec: 1.08x slower                                                     |
| telco                      | 4.13 ms                                                     | 4.48 ms: 1.09x slower                                                      |
| sympy_expand               | 284 ms                                                      | 309 ms: 1.09x slower                                                       |
| python_startup_no_site     | 16.2 ms                                                     | 18.1 ms: 1.11x slower                                                      |
| django_template            | 22.9 ms                                                     | 25.6 ms: 1.12x slower                                                      |
| python_startup             | 19.5 ms                                                     | 21.8 ms: 1.12x slower                                                      |
| coverage                   | 40.8 ms                                                     | 45.8 ms: 1.12x slower                                                      |
| hexiom                     | 4.10 ms                                                     | 4.65 ms: 1.14x slower                                                      |
| typing_runtime_protocols   | 95.1 us                                                     | 111 us: 1.17x slower                                                       |
| scimark_lu                 | 58.9 ms                                                     | 69.9 ms: 1.19x slower                                                      |
| create_gc_cycles           | 752 us                                                      | 907 us: 1.21x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.05x faster                                                               |

Benchmark hidden because not significant (4): bench_thread_pool, asyncio_tcp, meteor_contest, deepcopy
Ignored benchmarks (8) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, dask, dulwich_log, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, unpack_sequence
Ignored benchmarks (6) of results/bm-20240518-3.14.0a0-caf6064-JIT/bm-20240518-pythonperf1-amd64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064.json: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 99.27% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown
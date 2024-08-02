# Results vs. 3.12.0

- fork: python
- ref: caf6064a1bc15ac344af
- machine: windows-amd64
- commit hash: caf6064
- commit date: 2024-05-18
- overall geometric mean: 1.07x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240518-pythonperf1-amd64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 207 ms: 1.05x faster                                                       |
| chameleon      | 4.98 ms                                                     | 4.79 ms: 1.04x faster                                                      |
| docutils       | 1.66 sec                                                    | 1.60 sec: 1.03x faster                                                     |
| tornado_http   | 89.5 ms                                                     | 82.3 ms: 1.09x faster                                                      |
| Geometric mean | (ref)                                                       | 1.05x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240518-pythonperf1-amd64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 367 ms                                                      | 252 ms: 1.46x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 205 ms: 1.39x faster                                                       |
| async_tree_none            | 291 ms                                                      | 215 ms: 1.36x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 384 ms: 1.31x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 260 ms: 1.30x faster                                                       |
| async_tree_io_tg           | 771 ms                                                      | 598 ms: 1.29x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 384 ms: 1.27x faster                                                       |
| async_tree_io              | 731 ms                                                      | 578 ms: 1.27x faster                                                       |
| Geometric mean             | (ref)                                                       | 1.33x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240518-pythonperf1-amd64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 51.2 ms: 1.11x faster                                                      |
| nbody          | 71.9 ms                                                     | 69.4 ms: 1.04x faster                                                      |
| pidigits       | 152 ms                                                      | 150 ms: 1.01x faster                                                       |
| Geometric mean | (ref)                                                       | 1.05x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240518-pythonperf1-amd64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 87.5 ms                                                     | 77.9 ms: 1.12x faster                                                      |
| regex_dna      | 126 ms                                                      | 119 ms: 1.07x faster                                                       |
| regex_effbot   | 1.62 ms                                                     | 1.58 ms: 1.02x faster                                                      |
| regex_v8       | 14.2 ms                                                     | 14.8 ms: 1.04x slower                                                      |
| Geometric mean | (ref)                                                       | 1.04x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240518-pythonperf1-amd64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pickle_pure_python   | 195 us                                                      | 176 us: 1.11x faster                                                       |
| unpickle_pure_python | 133 us                                                      | 126 us: 1.06x faster                                                       |
| xml_etree_generate   | 55.8 ms                                                     | 52.9 ms: 1.06x faster                                                      |
| xml_etree_iterparse  | 65.2 ms                                                     | 62.8 ms: 1.04x faster                                                      |
| xml_etree_process    | 37.7 ms                                                     | 36.4 ms: 1.03x faster                                                      |
| xml_etree_parse      | 93.0 ms                                                     | 90.5 ms: 1.03x faster                                                      |
| pickle               | 7.43 us                                                     | 7.25 us: 1.02x faster                                                      |
| json_dumps           | 5.70 ms                                                     | 5.57 ms: 1.02x faster                                                      |
| pickle_dict          | 18.4 us                                                     | 18.2 us: 1.01x faster                                                      |
| tomli_loads          | 1.37 sec                                                    | 1.36 sec: 1.01x faster                                                     |
| unpickle_list        | 2.75 us                                                     | 2.81 us: 1.02x slower                                                      |
| unpickle             | 8.18 us                                                     | 8.56 us: 1.05x slower                                                      |
| pickle_list          | 2.83 us                                                     | 3.23 us: 1.14x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.01x faster                                                               |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240518-pythonperf1-amd64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 16.4 ms: 1.01x slower                                                      |
| python_startup         | 19.5 ms                                                     | 20.0 ms: 1.03x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.02x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240518-pythonperf1-amd64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 6.53 ms: 1.09x faster                                                      |
| django_template | 22.9 ms                                                     | 21.8 ms: 1.05x faster                                                      |
| Geometric mean  | (ref)                                                       | 1.07x faster                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240518-pythonperf1-amd64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 367 ms                                                      | 252 ms: 1.46x faster                                                       |
| asyncio_tcp_ssl            | 2.10 sec                                                    | 1.49 sec: 1.40x faster                                                     |
| async_tree_none_tg         | 285 ms                                                      | 205 ms: 1.39x faster                                                       |
| async_tree_none            | 291 ms                                                      | 215 ms: 1.36x faster                                                       |
| comprehensions             | 14.1 us                                                     | 10.4 us: 1.35x faster                                                      |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 384 ms: 1.31x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 260 ms: 1.30x faster                                                       |
| async_tree_io_tg           | 771 ms                                                      | 598 ms: 1.29x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 384 ms: 1.27x faster                                                       |
| async_tree_io              | 731 ms                                                      | 578 ms: 1.27x faster                                                       |
| raytrace                   | 192 ms                                                      | 161 ms: 1.19x faster                                                       |
| logging_silent             | 60.5 ns                                                     | 53.6 ns: 1.13x faster                                                      |
| regex_compile              | 87.5 ms                                                     | 77.9 ms: 1.12x faster                                                      |
| generators                 | 22.5 ms                                                     | 20.1 ms: 1.12x faster                                                      |
| chaos                      | 43.3 ms                                                     | 38.7 ms: 1.12x faster                                                      |
| deltablue                  | 2.16 ms                                                     | 1.94 ms: 1.12x faster                                                      |
| coroutines                 | 14.3 ms                                                     | 12.8 ms: 1.11x faster                                                      |
| pickle_pure_python         | 195 us                                                      | 176 us: 1.11x faster                                                       |
| float                      | 56.8 ms                                                     | 51.2 ms: 1.11x faster                                                      |
| logging_simple             | 6.28 us                                                     | 5.67 us: 1.11x faster                                                      |
| logging_format             | 6.72 us                                                     | 6.08 us: 1.10x faster                                                      |
| nqueens                    | 62.8 ms                                                     | 57.1 ms: 1.10x faster                                                      |
| sympy_sum                  | 91.5 ms                                                     | 83.9 ms: 1.09x faster                                                      |
| tornado_http               | 89.5 ms                                                     | 82.3 ms: 1.09x faster                                                      |
| hexiom                     | 4.10 ms                                                     | 3.77 ms: 1.09x faster                                                      |
| deepcopy                   | 238 us                                                      | 219 us: 1.09x faster                                                       |
| sqlite_synth               | 1.76 us                                                     | 1.62 us: 1.09x faster                                                      |
| go                         | 91.6 ms                                                     | 84.3 ms: 1.09x faster                                                      |
| mako                       | 7.09 ms                                                     | 6.53 ms: 1.09x faster                                                      |
| sympy_str                  | 175 ms                                                      | 162 ms: 1.08x faster                                                       |
| sqlglot_normalize          | 187 ms                                                      | 173 ms: 1.08x faster                                                       |
| richards_super             | 32.1 ms                                                     | 29.8 ms: 1.08x faster                                                      |
| richards                   | 28.4 ms                                                     | 26.6 ms: 1.07x faster                                                      |
| sqlglot_parse              | 804 us                                                      | 754 us: 1.07x faster                                                       |
| regex_dna                  | 126 ms                                                      | 119 ms: 1.07x faster                                                       |
| bench_thread_pool          | 857 us                                                      | 804 us: 1.07x faster                                                       |
| deepcopy_reduce            | 2.09 us                                                     | 1.97 us: 1.07x faster                                                      |
| scimark_monte_carlo        | 43.7 ms                                                     | 41.1 ms: 1.06x faster                                                      |
| unpickle_pure_python       | 133 us                                                      | 126 us: 1.06x faster                                                       |
| sqlglot_transpile          | 1.02 ms                                                     | 963 us: 1.06x faster                                                       |
| pprint_safe_repr           | 513 ms                                                      | 485 ms: 1.06x faster                                                       |
| pprint_pformat             | 1.05 sec                                                    | 989 ms: 1.06x faster                                                       |
| xml_etree_generate         | 55.8 ms                                                     | 52.9 ms: 1.06x faster                                                      |
| sympy_integrate            | 13.0 ms                                                     | 12.3 ms: 1.05x faster                                                      |
| scimark_lu                 | 58.9 ms                                                     | 55.8 ms: 1.05x faster                                                      |
| sqlglot_optimize           | 34.5 ms                                                     | 32.8 ms: 1.05x faster                                                      |
| 2to3                       | 218 ms                                                      | 207 ms: 1.05x faster                                                       |
| django_template            | 22.9 ms                                                     | 21.8 ms: 1.05x faster                                                      |
| sympy_expand               | 284 ms                                                      | 270 ms: 1.05x faster                                                       |
| async_generators           | 239 ms                                                      | 228 ms: 1.05x faster                                                       |
| bench_mp_pool              | 69.2 ms                                                     | 66.0 ms: 1.05x faster                                                      |
| crypto_pyaes               | 48.5 ms                                                     | 46.5 ms: 1.04x faster                                                      |
| chameleon                  | 4.98 ms                                                     | 4.79 ms: 1.04x faster                                                      |
| xml_etree_iterparse        | 65.2 ms                                                     | 62.8 ms: 1.04x faster                                                      |
| nbody                      | 71.9 ms                                                     | 69.4 ms: 1.04x faster                                                      |
| docutils                   | 1.66 sec                                                    | 1.60 sec: 1.03x faster                                                     |
| xml_etree_process          | 37.7 ms                                                     | 36.4 ms: 1.03x faster                                                      |
| pyflate                    | 295 ms                                                      | 286 ms: 1.03x faster                                                       |
| deepcopy_memo              | 23.7 us                                                     | 23.0 us: 1.03x faster                                                      |
| spectral_norm              | 66.9 ms                                                     | 65.1 ms: 1.03x faster                                                      |
| xml_etree_parse            | 93.0 ms                                                     | 90.5 ms: 1.03x faster                                                      |
| pickle                     | 7.43 us                                                     | 7.25 us: 1.02x faster                                                      |
| regex_effbot               | 1.62 ms                                                     | 1.58 ms: 1.02x faster                                                      |
| json_dumps                 | 5.70 ms                                                     | 5.57 ms: 1.02x faster                                                      |
| scimark_fft                | 184 ms                                                      | 181 ms: 1.02x faster                                                       |
| scimark_sor                | 78.8 ms                                                     | 77.3 ms: 1.02x faster                                                      |
| mdp                        | 1.37 sec                                                    | 1.35 sec: 1.02x faster                                                     |
| meteor_contest             | 74.6 ms                                                     | 73.4 ms: 1.02x faster                                                      |
| pathlib                    | 80.5 ms                                                     | 79.2 ms: 1.02x faster                                                      |
| pidigits                   | 152 ms                                                      | 150 ms: 1.01x faster                                                       |
| pickle_dict                | 18.4 us                                                     | 18.2 us: 1.01x faster                                                      |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.54 ms: 1.01x faster                                                      |
| tomli_loads                | 1.37 sec                                                    | 1.36 sec: 1.01x faster                                                     |
| python_startup_no_site     | 16.2 ms                                                     | 16.4 ms: 1.01x slower                                                      |
| gc_traversal               | 1.52 ms                                                     | 1.55 ms: 1.02x slower                                                      |
| unpickle_list              | 2.75 us                                                     | 2.81 us: 1.02x slower                                                      |
| python_startup             | 19.5 ms                                                     | 20.0 ms: 1.03x slower                                                      |
| regex_v8                   | 14.2 ms                                                     | 14.8 ms: 1.04x slower                                                      |
| fannkuch                   | 247 ms                                                      | 256 ms: 1.04x slower                                                       |
| unpickle                   | 8.18 us                                                     | 8.56 us: 1.05x slower                                                      |
| typing_runtime_protocols   | 95.1 us                                                     | 99.7 us: 1.05x slower                                                      |
| coverage                   | 40.8 ms                                                     | 44.5 ms: 1.09x slower                                                      |
| telco                      | 4.13 ms                                                     | 4.68 ms: 1.13x slower                                                      |
| pickle_list                | 2.83 us                                                     | 3.23 us: 1.14x slower                                                      |
| create_gc_cycles           | 752 us                                                      | 888 us: 1.18x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.07x faster                                                               |

Benchmark hidden because not significant (4): asyncio_tcp, json, json_loads, pycparser
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, dask, dulwich_log, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (6) of results/bm-20240518-3.14.0a0-caf6064/bm-20240518-pythonperf1-amd64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064.json: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: unknown
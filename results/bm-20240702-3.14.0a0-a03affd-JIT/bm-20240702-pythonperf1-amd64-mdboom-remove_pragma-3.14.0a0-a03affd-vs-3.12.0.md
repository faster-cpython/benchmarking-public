# Results vs. 3.12.0

- fork: mdboom
- ref: remove_pragma
- machine: windows-amd64
- commit hash: a03affd
- commit date: 2024-07-02
- overall geometric mean: 1.05x faster
- HPT reliability: 94.22%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240702-pythonperf1-amd64-mdboom-remove_pragma-3.14.0a0-a03affd |
|----------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 236 ms: 1.08x slower                                                |
| docutils       | 1.66 sec                                                    | 1.79 sec: 1.08x slower                                              |
| tornado_http   | 89.5 ms                                                     | 85.0 ms: 1.05x faster                                               |
| Geometric mean | (ref)                                                       | 1.03x slower                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240702-pythonperf1-amd64-mdboom-remove_pragma-3.14.0a0-a03affd |
|----------------------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_none_tg         | 285 ms                                                      | 192 ms: 1.49x faster                                                |
| async_tree_memoization_tg  | 367 ms                                                      | 247 ms: 1.48x faster                                                |
| async_tree_io_tg           | 771 ms                                                      | 529 ms: 1.46x faster                                                |
| async_tree_none            | 291 ms                                                      | 212 ms: 1.37x faster                                                |
| async_tree_io              | 731 ms                                                      | 541 ms: 1.35x faster                                                |
| async_tree_memoization     | 339 ms                                                      | 259 ms: 1.31x faster                                                |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 386 ms: 1.30x faster                                                |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 385 ms: 1.27x faster                                                |
| Geometric mean             | (ref)                                                       | 1.38x faster                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240702-pythonperf1-amd64-mdboom-remove_pragma-3.14.0a0-a03affd |
|----------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------:|
| nbody          | 71.9 ms                                                     | 49.7 ms: 1.45x faster                                               |
| float          | 56.8 ms                                                     | 46.1 ms: 1.23x faster                                               |
| pidigits       | 152 ms                                                      | 149 ms: 1.02x faster                                                |
| Geometric mean | (ref)                                                       | 1.22x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240702-pythonperf1-amd64-mdboom-remove_pragma-3.14.0a0-a03affd |
|----------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_dna      | 126 ms                                                      | 122 ms: 1.04x faster                                                |
| regex_effbot   | 1.62 ms                                                     | 1.59 ms: 1.02x faster                                               |
| regex_compile  | 87.5 ms                                                     | 90.2 ms: 1.03x slower                                               |
| regex_v8       | 14.2 ms                                                     | 19.9 ms: 1.40x slower                                               |
| Geometric mean | (ref)                                                       | 1.08x slower                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240702-pythonperf1-amd64-mdboom-remove_pragma-3.14.0a0-a03affd |
|----------------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------:|
| xml_etree_iterparse  | 65.2 ms                                                     | 60.6 ms: 1.08x faster                                               |
| pickle_pure_python   | 195 us                                                      | 182 us: 1.07x faster                                                |
| tomli_loads          | 1.37 sec                                                    | 1.29 sec: 1.06x faster                                              |
| xml_etree_generate   | 55.8 ms                                                     | 53.4 ms: 1.05x faster                                               |
| xml_etree_parse      | 93.0 ms                                                     | 92.0 ms: 1.01x faster                                               |
| unpickle_pure_python | 133 us                                                      | 136 us: 1.02x slower                                                |
| xml_etree_process    | 37.7 ms                                                     | 38.5 ms: 1.02x slower                                               |
| json_loads           | 13.9 us                                                     | 14.3 us: 1.03x slower                                               |
| json_dumps           | 5.70 ms                                                     | 5.86 ms: 1.03x slower                                               |
| Geometric mean       | (ref)                                                       | 1.02x faster                                                        |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240702-pythonperf1-amd64-mdboom-remove_pragma-3.14.0a0-a03affd |
|------------------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 17.3 ms: 1.07x slower                                               |
| python_startup         | 19.5 ms                                                     | 21.1 ms: 1.08x slower                                               |
| Geometric mean         | (ref)                                                       | 1.08x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240702-pythonperf1-amd64-mdboom-remove_pragma-3.14.0a0-a03affd |
|-----------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 5.30 ms: 1.34x faster                                               |
| django_template | 22.9 ms                                                     | 26.3 ms: 1.15x slower                                               |
| Geometric mean  | (ref)                                                       | 1.08x faster                                                        |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240702-pythonperf1-amd64-mdboom-remove_pragma-3.14.0a0-a03affd |
|----------------------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------:|
| asyncio_tcp_ssl            | 2.10 sec                                                    | 1.39 sec: 1.51x faster                                              |
| deepcopy_memo              | 23.7 us                                                     | 15.9 us: 1.49x faster                                               |
| async_tree_none_tg         | 285 ms                                                      | 192 ms: 1.49x faster                                                |
| async_tree_memoization_tg  | 367 ms                                                      | 247 ms: 1.48x faster                                                |
| spectral_norm              | 66.9 ms                                                     | 45.6 ms: 1.47x faster                                               |
| async_tree_io_tg           | 771 ms                                                      | 529 ms: 1.46x faster                                                |
| nbody                      | 71.9 ms                                                     | 49.7 ms: 1.45x faster                                               |
| async_tree_none            | 291 ms                                                      | 212 ms: 1.37x faster                                                |
| comprehensions             | 14.1 us                                                     | 10.5 us: 1.35x faster                                               |
| async_tree_io              | 731 ms                                                      | 541 ms: 1.35x faster                                                |
| mako                       | 7.09 ms                                                     | 5.30 ms: 1.34x faster                                               |
| deepcopy                   | 238 us                                                      | 181 us: 1.31x faster                                                |
| async_tree_memoization     | 339 ms                                                      | 259 ms: 1.31x faster                                                |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 386 ms: 1.30x faster                                                |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 385 ms: 1.27x faster                                                |
| scimark_fft                | 184 ms                                                      | 147 ms: 1.25x faster                                                |
| float                      | 56.8 ms                                                     | 46.1 ms: 1.23x faster                                               |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.08 ms: 1.23x faster                                               |
| crypto_pyaes               | 48.5 ms                                                     | 41.1 ms: 1.18x faster                                               |
| scimark_monte_carlo        | 43.7 ms                                                     | 38.6 ms: 1.13x faster                                               |
| pyflate                    | 295 ms                                                      | 261 ms: 1.13x faster                                                |
| fannkuch                   | 247 ms                                                      | 220 ms: 1.12x faster                                                |
| deepcopy_reduce            | 2.09 us                                                     | 1.87 us: 1.12x faster                                               |
| bench_thread_pool          | 857 us                                                      | 792 us: 1.08x faster                                                |
| xml_etree_iterparse        | 65.2 ms                                                     | 60.6 ms: 1.08x faster                                               |
| pickle_pure_python         | 195 us                                                      | 182 us: 1.07x faster                                                |
| chaos                      | 43.3 ms                                                     | 40.5 ms: 1.07x faster                                               |
| logging_silent             | 60.5 ns                                                     | 56.7 ns: 1.07x faster                                               |
| logging_format             | 6.72 us                                                     | 6.31 us: 1.06x faster                                               |
| pprint_safe_repr           | 513 ms                                                      | 482 ms: 1.06x faster                                                |
| logging_simple             | 6.28 us                                                     | 5.91 us: 1.06x faster                                               |
| tomli_loads                | 1.37 sec                                                    | 1.29 sec: 1.06x faster                                              |
| pathlib                    | 80.5 ms                                                     | 76.1 ms: 1.06x faster                                               |
| tornado_http               | 89.5 ms                                                     | 85.0 ms: 1.05x faster                                               |
| xml_etree_generate         | 55.8 ms                                                     | 53.4 ms: 1.05x faster                                               |
| pprint_pformat             | 1.05 sec                                                    | 1.00 sec: 1.04x faster                                              |
| regex_dna                  | 126 ms                                                      | 122 ms: 1.04x faster                                                |
| raytrace                   | 192 ms                                                      | 186 ms: 1.03x faster                                                |
| json                       | 3.05 ms                                                     | 2.96 ms: 1.03x faster                                               |
| pidigits                   | 152 ms                                                      | 149 ms: 1.02x faster                                                |
| nqueens                    | 62.8 ms                                                     | 61.7 ms: 1.02x faster                                               |
| regex_effbot               | 1.62 ms                                                     | 1.59 ms: 1.02x faster                                               |
| xml_etree_parse            | 93.0 ms                                                     | 92.0 ms: 1.01x faster                                               |
| meteor_contest             | 74.6 ms                                                     | 75.0 ms: 1.00x slower                                               |
| bench_mp_pool              | 69.2 ms                                                     | 69.6 ms: 1.01x slower                                               |
| unpickle_pure_python       | 133 us                                                      | 136 us: 1.02x slower                                                |
| mdp                        | 1.37 sec                                                    | 1.40 sec: 1.02x slower                                              |
| xml_etree_process          | 37.7 ms                                                     | 38.5 ms: 1.02x slower                                               |
| json_loads                 | 13.9 us                                                     | 14.3 us: 1.03x slower                                               |
| gc_traversal               | 1.52 ms                                                     | 1.56 ms: 1.03x slower                                               |
| sqlglot_parse              | 804 us                                                      | 827 us: 1.03x slower                                                |
| json_dumps                 | 5.70 ms                                                     | 5.86 ms: 1.03x slower                                               |
| regex_compile              | 87.5 ms                                                     | 90.2 ms: 1.03x slower                                               |
| sympy_sum                  | 91.5 ms                                                     | 94.4 ms: 1.03x slower                                               |
| sqlglot_transpile          | 1.02 ms                                                     | 1.06 ms: 1.04x slower                                               |
| sqlglot_normalize          | 187 ms                                                      | 196 ms: 1.05x slower                                                |
| sympy_str                  | 175 ms                                                      | 183 ms: 1.05x slower                                                |
| go                         | 91.6 ms                                                     | 96.8 ms: 1.06x slower                                               |
| sqlglot_optimize           | 34.5 ms                                                     | 36.6 ms: 1.06x slower                                               |
| python_startup_no_site     | 16.2 ms                                                     | 17.3 ms: 1.07x slower                                               |
| generators                 | 22.5 ms                                                     | 24.1 ms: 1.07x slower                                               |
| deltablue                  | 2.16 ms                                                     | 2.32 ms: 1.07x slower                                               |
| docutils                   | 1.66 sec                                                    | 1.79 sec: 1.08x slower                                              |
| richards                   | 28.4 ms                                                     | 30.6 ms: 1.08x slower                                               |
| 2to3                       | 218 ms                                                      | 236 ms: 1.08x slower                                                |
| python_startup             | 19.5 ms                                                     | 21.1 ms: 1.08x slower                                               |
| sympy_integrate            | 13.0 ms                                                     | 14.1 ms: 1.09x slower                                               |
| richards_super             | 32.1 ms                                                     | 35.0 ms: 1.09x slower                                               |
| telco                      | 4.13 ms                                                     | 4.56 ms: 1.10x slower                                               |
| sympy_expand               | 284 ms                                                      | 316 ms: 1.11x slower                                                |
| async_generators           | 239 ms                                                      | 270 ms: 1.13x slower                                                |
| coverage                   | 40.8 ms                                                     | 46.2 ms: 1.13x slower                                               |
| hexiom                     | 4.10 ms                                                     | 4.69 ms: 1.14x slower                                               |
| django_template            | 22.9 ms                                                     | 26.3 ms: 1.15x slower                                               |
| scimark_sor                | 78.8 ms                                                     | 92.0 ms: 1.17x slower                                               |
| typing_runtime_protocols   | 95.1 us                                                     | 114 us: 1.20x slower                                                |
| create_gc_cycles           | 752 us                                                      | 904 us: 1.20x slower                                                |
| pycparser                  | 699 ms                                                      | 862 ms: 1.23x slower                                                |
| scimark_lu                 | 58.9 ms                                                     | 76.4 ms: 1.30x slower                                               |
| regex_v8                   | 14.2 ms                                                     | 19.9 ms: 1.40x slower                                               |
| Geometric mean             | (ref)                                                       | 1.05x faster                                                        |

Benchmark hidden because not significant (2): asyncio_tcp, coroutines
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, dulwich_log, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240702-3.14.0a0-a03affd-JIT/bm-20240702-pythonperf1-amd64-mdboom-remove_pragma-3.14.0a0-a03affd.json: genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 94.22% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown
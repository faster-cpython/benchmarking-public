# Results vs. 3.12.0

- fork: faster-cpython
- ref: specialize_binary_op
- machine: windows-amd64
- commit hash: 8183250
- commit date: 2024-03-27
- overall geometric mean: 1.05x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240327-pythonperf1-amd64-faster%2dcpython-specialize_binary_op-3.13.0a5+-8183250 |
|----------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 213 ms: 1.02x faster                                                                  |
| chameleon      | 4.98 ms                                                     | 4.76 ms: 1.05x faster                                                                 |
| docutils       | 1.66 sec                                                    | 1.63 sec: 1.02x faster                                                                |
| tornado_http   | 89.5 ms                                                     | 84.0 ms: 1.07x faster                                                                 |
| Geometric mean | (ref)                                                       | 1.04x faster                                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240327-pythonperf1-amd64-faster%2dcpython-specialize_binary_op-3.13.0a5+-8183250 |
|----------------------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 562 ms: 1.37x faster                                                                  |
| async_tree_memoization_tg  | 367 ms                                                      | 269 ms: 1.36x faster                                                                  |
| async_tree_none_tg         | 285 ms                                                      | 210 ms: 1.36x faster                                                                  |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 383 ms: 1.31x faster                                                                  |
| async_tree_none            | 291 ms                                                      | 223 ms: 1.31x faster                                                                  |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 382 ms: 1.28x faster                                                                  |
| async_tree_io              | 731 ms                                                      | 585 ms: 1.25x faster                                                                  |
| async_tree_memoization     | 339 ms                                                      | 276 ms: 1.23x faster                                                                  |
| Geometric mean             | (ref)                                                       | 1.31x faster                                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240327-pythonperf1-amd64-faster%2dcpython-specialize_binary_op-3.13.0a5+-8183250 |
|----------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 51.8 ms: 1.10x faster                                                                 |
| pidigits       | 152 ms                                                      | 147 ms: 1.04x faster                                                                  |
| nbody          | 71.9 ms                                                     | 77.5 ms: 1.08x slower                                                                 |
| Geometric mean | (ref)                                                       | 1.02x faster                                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240327-pythonperf1-amd64-faster%2dcpython-specialize_binary_op-3.13.0a5+-8183250 |
|----------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| regex_dna      | 126 ms                                                      | 115 ms: 1.10x faster                                                                  |
| regex_compile  | 87.5 ms                                                     | 81.3 ms: 1.08x faster                                                                 |
| regex_effbot   | 1.62 ms                                                     | 1.55 ms: 1.05x faster                                                                 |
| regex_v8       | 14.2 ms                                                     | 16.3 ms: 1.15x slower                                                                 |
| Geometric mean | (ref)                                                       | 1.02x faster                                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240327-pythonperf1-amd64-faster%2dcpython-specialize_binary_op-3.13.0a5+-8183250 |
|----------------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| pickle_pure_python   | 195 us                                                      | 179 us: 1.09x faster                                                                  |
| unpickle_pure_python | 133 us                                                      | 127 us: 1.05x faster                                                                  |
| xml_etree_generate   | 55.8 ms                                                     | 54.3 ms: 1.03x faster                                                                 |
| json_dumps           | 5.70 ms                                                     | 5.55 ms: 1.03x faster                                                                 |
| pickle               | 7.43 us                                                     | 7.26 us: 1.02x faster                                                                 |
| xml_etree_iterparse  | 65.2 ms                                                     | 63.7 ms: 1.02x faster                                                                 |
| pickle_dict          | 18.4 us                                                     | 18.1 us: 1.01x faster                                                                 |
| xml_etree_process    | 37.7 ms                                                     | 37.3 ms: 1.01x faster                                                                 |
| xml_etree_parse      | 93.0 ms                                                     | 93.8 ms: 1.01x slower                                                                 |
| json_loads           | 13.9 us                                                     | 14.1 us: 1.01x slower                                                                 |
| pickle_list          | 2.83 us                                                     | 2.87 us: 1.02x slower                                                                 |
| unpickle_list        | 2.75 us                                                     | 2.82 us: 1.02x slower                                                                 |
| unpickle             | 8.18 us                                                     | 8.47 us: 1.03x slower                                                                 |
| tomli_loads          | 1.37 sec                                                    | 1.47 sec: 1.08x slower                                                                |
| Geometric mean       | (ref)                                                       | 1.01x faster                                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240327-pythonperf1-amd64-faster%2dcpython-specialize_binary_op-3.13.0a5+-8183250 |
|------------------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| python_startup         | 19.5 ms                                                     | 20.4 ms: 1.05x slower                                                                 |
| python_startup_no_site | 16.2 ms                                                     | 17.9 ms: 1.10x slower                                                                 |
| Geometric mean         | (ref)                                                       | 1.07x slower                                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240327-pythonperf1-amd64-faster%2dcpython-specialize_binary_op-3.13.0a5+-8183250 |
|-----------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 6.35 ms: 1.12x faster                                                                 |
| django_template | 22.9 ms                                                     | 22.6 ms: 1.02x faster                                                                 |
| Geometric mean  | (ref)                                                       | 1.06x faster                                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240327-pythonperf1-amd64-faster%2dcpython-specialize_binary_op-3.13.0a5+-8183250 |
|----------------------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 562 ms: 1.37x faster                                                                  |
| async_tree_memoization_tg  | 367 ms                                                      | 269 ms: 1.36x faster                                                                  |
| async_tree_none_tg         | 285 ms                                                      | 210 ms: 1.36x faster                                                                  |
| typing_runtime_protocols   | 95.1 us                                                     | 71.6 us: 1.33x faster                                                                 |
| comprehensions             | 14.1 us                                                     | 10.7 us: 1.32x faster                                                                 |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 383 ms: 1.31x faster                                                                  |
| async_tree_none            | 291 ms                                                      | 223 ms: 1.31x faster                                                                  |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 382 ms: 1.28x faster                                                                  |
| async_tree_io              | 731 ms                                                      | 585 ms: 1.25x faster                                                                  |
| async_tree_memoization     | 339 ms                                                      | 276 ms: 1.23x faster                                                                  |
| asyncio_tcp_ssl            | 2.10 sec                                                    | 1.74 sec: 1.20x faster                                                                |
| mypy2                      | 509 ms                                                      | 438 ms: 1.16x faster                                                                  |
| raytrace                   | 192 ms                                                      | 169 ms: 1.14x faster                                                                  |
| mako                       | 7.09 ms                                                     | 6.35 ms: 1.12x faster                                                                 |
| sympy_str                  | 175 ms                                                      | 159 ms: 1.10x faster                                                                  |
| regex_dna                  | 126 ms                                                      | 115 ms: 1.10x faster                                                                  |
| sympy_sum                  | 91.5 ms                                                     | 83.5 ms: 1.10x faster                                                                 |
| float                      | 56.8 ms                                                     | 51.8 ms: 1.10x faster                                                                 |
| deepcopy                   | 238 us                                                      | 217 us: 1.10x faster                                                                  |
| pickle_pure_python         | 195 us                                                      | 179 us: 1.09x faster                                                                  |
| deepcopy_memo              | 23.7 us                                                     | 21.7 us: 1.09x faster                                                                 |
| sqlite_synth               | 1.76 us                                                     | 1.62 us: 1.09x faster                                                                 |
| hexiom                     | 4.10 ms                                                     | 3.78 ms: 1.09x faster                                                                 |
| dulwich_log                | 44.3 ms                                                     | 40.9 ms: 1.08x faster                                                                 |
| bench_mp_pool              | 69.2 ms                                                     | 63.9 ms: 1.08x faster                                                                 |
| deepcopy_reduce            | 2.09 us                                                     | 1.94 us: 1.08x faster                                                                 |
| regex_compile              | 87.5 ms                                                     | 81.3 ms: 1.08x faster                                                                 |
| bench_thread_pool          | 857 us                                                      | 801 us: 1.07x faster                                                                  |
| logging_silent             | 60.5 ns                                                     | 56.6 ns: 1.07x faster                                                                 |
| tornado_http               | 89.5 ms                                                     | 84.0 ms: 1.07x faster                                                                 |
| pprint_pformat             | 1.05 sec                                                    | 985 ms: 1.06x faster                                                                  |
| deltablue                  | 2.16 ms                                                     | 2.04 ms: 1.06x faster                                                                 |
| pprint_safe_repr           | 513 ms                                                      | 485 ms: 1.06x faster                                                                  |
| sympy_expand               | 284 ms                                                      | 270 ms: 1.05x faster                                                                  |
| sympy_integrate            | 13.0 ms                                                     | 12.3 ms: 1.05x faster                                                                 |
| unpickle_pure_python       | 133 us                                                      | 127 us: 1.05x faster                                                                  |
| sqlglot_normalize          | 187 ms                                                      | 178 ms: 1.05x faster                                                                  |
| regex_effbot               | 1.62 ms                                                     | 1.55 ms: 1.05x faster                                                                 |
| chameleon                  | 4.98 ms                                                     | 4.76 ms: 1.05x faster                                                                 |
| json                       | 3.05 ms                                                     | 2.92 ms: 1.04x faster                                                                 |
| meteor_contest             | 74.6 ms                                                     | 71.5 ms: 1.04x faster                                                                 |
| crypto_pyaes               | 48.5 ms                                                     | 46.7 ms: 1.04x faster                                                                 |
| pathlib                    | 80.5 ms                                                     | 77.5 ms: 1.04x faster                                                                 |
| generators                 | 22.5 ms                                                     | 21.7 ms: 1.04x faster                                                                 |
| go                         | 91.6 ms                                                     | 88.4 ms: 1.04x faster                                                                 |
| pidigits                   | 152 ms                                                      | 147 ms: 1.04x faster                                                                  |
| sqlglot_transpile          | 1.02 ms                                                     | 990 us: 1.03x faster                                                                  |
| create_gc_cycles           | 752 us                                                      | 729 us: 1.03x faster                                                                  |
| gc_traversal               | 1.52 ms                                                     | 1.48 ms: 1.03x faster                                                                 |
| chaos                      | 43.3 ms                                                     | 42.0 ms: 1.03x faster                                                                 |
| scimark_lu                 | 58.9 ms                                                     | 57.1 ms: 1.03x faster                                                                 |
| xml_etree_generate         | 55.8 ms                                                     | 54.3 ms: 1.03x faster                                                                 |
| async_generators           | 239 ms                                                      | 233 ms: 1.03x faster                                                                  |
| scimark_monte_carlo        | 43.7 ms                                                     | 42.6 ms: 1.03x faster                                                                 |
| json_dumps                 | 5.70 ms                                                     | 5.55 ms: 1.03x faster                                                                 |
| sqlglot_parse              | 804 us                                                      | 784 us: 1.03x faster                                                                  |
| unpack_sequence            | 37.5 ns                                                     | 36.6 ns: 1.02x faster                                                                 |
| pickle                     | 7.43 us                                                     | 7.26 us: 1.02x faster                                                                 |
| 2to3                       | 218 ms                                                      | 213 ms: 1.02x faster                                                                  |
| sqlglot_optimize           | 34.5 ms                                                     | 33.8 ms: 1.02x faster                                                                 |
| xml_etree_iterparse        | 65.2 ms                                                     | 63.7 ms: 1.02x faster                                                                 |
| docutils                   | 1.66 sec                                                    | 1.63 sec: 1.02x faster                                                                |
| django_template            | 22.9 ms                                                     | 22.6 ms: 1.02x faster                                                                 |
| pickle_dict                | 18.4 us                                                     | 18.1 us: 1.01x faster                                                                 |
| logging_simple             | 6.28 us                                                     | 6.18 us: 1.01x faster                                                                 |
| xml_etree_process          | 37.7 ms                                                     | 37.3 ms: 1.01x faster                                                                 |
| logging_format             | 6.72 us                                                     | 6.65 us: 1.01x faster                                                                 |
| xml_etree_parse            | 93.0 ms                                                     | 93.8 ms: 1.01x slower                                                                 |
| coroutines                 | 14.3 ms                                                     | 14.4 ms: 1.01x slower                                                                 |
| richards                   | 28.4 ms                                                     | 28.6 ms: 1.01x slower                                                                 |
| json_loads                 | 13.9 us                                                     | 14.1 us: 1.01x slower                                                                 |
| pickle_list                | 2.83 us                                                     | 2.87 us: 1.02x slower                                                                 |
| aiohttp                    | 884 us                                                      | 901 us: 1.02x slower                                                                  |
| unpickle_list              | 2.75 us                                                     | 2.82 us: 1.02x slower                                                                 |
| pyflate                    | 295 ms                                                      | 302 ms: 1.03x slower                                                                  |
| unpickle                   | 8.18 us                                                     | 8.47 us: 1.03x slower                                                                 |
| python_startup             | 19.5 ms                                                     | 20.4 ms: 1.05x slower                                                                 |
| mdp                        | 1.37 sec                                                    | 1.46 sec: 1.06x slower                                                                |
| tomli_loads                | 1.37 sec                                                    | 1.47 sec: 1.08x slower                                                                |
| nbody                      | 71.9 ms                                                     | 77.5 ms: 1.08x slower                                                                 |
| scimark_sor                | 78.8 ms                                                     | 85.2 ms: 1.08x slower                                                                 |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.81 ms: 1.10x slower                                                                 |
| python_startup_no_site     | 16.2 ms                                                     | 17.9 ms: 1.10x slower                                                                 |
| fannkuch                   | 247 ms                                                      | 274 ms: 1.11x slower                                                                  |
| spectral_norm              | 66.9 ms                                                     | 75.0 ms: 1.12x slower                                                                 |
| scimark_fft                | 184 ms                                                      | 209 ms: 1.14x slower                                                                  |
| regex_v8                   | 14.2 ms                                                     | 16.3 ms: 1.15x slower                                                                 |
| coverage                   | 40.8 ms                                                     | 46.8 ms: 1.15x slower                                                                 |
| telco                      | 4.13 ms                                                     | 4.88 ms: 1.18x slower                                                                 |
| Geometric mean             | (ref)                                                       | 1.05x faster                                                                          |

Benchmark hidden because not significant (4): pycparser, asyncio_tcp, nqueens, richards_super
Ignored benchmarks (3) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: dask, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of results/bm-20240327-3.13.0a5+-8183250/bm-20240327-pythonperf1-amd64-faster%2dcpython-specialize_binary_op-3.13.0a5+-8183250.json: genshi_text, genshi_xml, html5lib, pylint, thrift


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.02x


# Memory

- memory change: unknown
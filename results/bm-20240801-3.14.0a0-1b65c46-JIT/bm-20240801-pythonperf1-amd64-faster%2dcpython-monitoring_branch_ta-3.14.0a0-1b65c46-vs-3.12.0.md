# Results vs. 3.12.0

- fork: faster-cpython
- ref: monitoring_branch_ta
- machine: windows-amd64
- commit hash: 1b65c46
- commit date: 2024-08-01
- overall geometric mean: 1.05x faster
- HPT reliability: 83.22%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240801-pythonperf1-amd64-faster%2dcpython-monitoring_branch_ta-3.14.0a0-1b65c46 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 240 ms: 1.10x slower                                                                 |
| docutils       | 1.66 sec                                                    | 1.83 sec: 1.10x slower                                                               |
| tornado_http   | 89.5 ms                                                     | 96.0 ms: 1.07x slower                                                                |
| Geometric mean | (ref)                                                       | 1.09x slower                                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240801-pythonperf1-amd64-faster%2dcpython-monitoring_branch_ta-3.14.0a0-1b65c46 |
|----------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| async_tree_none_tg         | 285 ms                                                      | 193 ms: 1.48x faster                                                                 |
| async_tree_memoization_tg  | 367 ms                                                      | 250 ms: 1.47x faster                                                                 |
| async_tree_io_tg           | 771 ms                                                      | 541 ms: 1.43x faster                                                                 |
| async_tree_none            | 291 ms                                                      | 215 ms: 1.35x faster                                                                 |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 381 ms: 1.32x faster                                                                 |
| async_tree_io              | 731 ms                                                      | 561 ms: 1.30x faster                                                                 |
| async_tree_memoization     | 339 ms                                                      | 267 ms: 1.27x faster                                                                 |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 396 ms: 1.24x faster                                                                 |
| Geometric mean             | (ref)                                                       | 1.35x faster                                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240801-pythonperf1-amd64-faster%2dcpython-monitoring_branch_ta-3.14.0a0-1b65c46 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| nbody          | 71.9 ms                                                     | 49.7 ms: 1.45x faster                                                                |
| float          | 56.8 ms                                                     | 45.3 ms: 1.25x faster                                                                |
| pidigits       | 152 ms                                                      | 150 ms: 1.02x faster                                                                 |
| Geometric mean | (ref)                                                       | 1.23x faster                                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240801-pythonperf1-amd64-faster%2dcpython-monitoring_branch_ta-3.14.0a0-1b65c46 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| regex_dna      | 126 ms                                                      | 116 ms: 1.09x faster                                                                 |
| regex_effbot   | 1.62 ms                                                     | 1.56 ms: 1.04x faster                                                                |
| regex_v8       | 14.2 ms                                                     | 14.4 ms: 1.01x slower                                                                |
| regex_compile  | 87.5 ms                                                     | 90.5 ms: 1.03x slower                                                                |
| Geometric mean | (ref)                                                       | 1.02x faster                                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240801-pythonperf1-amd64-faster%2dcpython-monitoring_branch_ta-3.14.0a0-1b65c46 |
|----------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| xml_etree_generate   | 55.8 ms                                                     | 51.4 ms: 1.09x faster                                                                |
| tomli_loads          | 1.37 sec                                                    | 1.28 sec: 1.07x faster                                                               |
| xml_etree_iterparse  | 65.2 ms                                                     | 61.2 ms: 1.07x faster                                                                |
| pickle_pure_python   | 195 us                                                      | 187 us: 1.04x faster                                                                 |
| xml_etree_process    | 37.7 ms                                                     | 37.3 ms: 1.01x faster                                                                |
| unpickle_pure_python | 133 us                                                      | 135 us: 1.01x slower                                                                 |
| json_loads           | 13.9 us                                                     | 14.1 us: 1.02x slower                                                                |
| json_dumps           | 5.70 ms                                                     | 6.10 ms: 1.07x slower                                                                |
| Geometric mean       | (ref)                                                       | 1.02x faster                                                                         |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240801-pythonperf1-amd64-faster%2dcpython-monitoring_branch_ta-3.14.0a0-1b65c46 |
|------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 18.7 ms: 1.15x slower                                                                |
| python_startup         | 19.5 ms                                                     | 22.7 ms: 1.16x slower                                                                |
| Geometric mean         | (ref)                                                       | 1.16x slower                                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240801-pythonperf1-amd64-faster%2dcpython-monitoring_branch_ta-3.14.0a0-1b65c46 |
|-----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 5.10 ms: 1.39x faster                                                                |
| django_template | 22.9 ms                                                     | 25.6 ms: 1.11x slower                                                                |
| Geometric mean  | (ref)                                                       | 1.12x faster                                                                         |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240801-pythonperf1-amd64-faster%2dcpython-monitoring_branch_ta-3.14.0a0-1b65c46 |
|----------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| asyncio_tcp_ssl            | 2.10 sec                                                    | 1.41 sec: 1.48x faster                                                               |
| async_tree_none_tg         | 285 ms                                                      | 193 ms: 1.48x faster                                                                 |
| deepcopy_memo              | 23.7 us                                                     | 16.1 us: 1.47x faster                                                                |
| async_tree_memoization_tg  | 367 ms                                                      | 250 ms: 1.47x faster                                                                 |
| spectral_norm              | 66.9 ms                                                     | 45.7 ms: 1.46x faster                                                                |
| nbody                      | 71.9 ms                                                     | 49.7 ms: 1.45x faster                                                                |
| async_tree_io_tg           | 771 ms                                                      | 541 ms: 1.43x faster                                                                 |
| mako                       | 7.09 ms                                                     | 5.10 ms: 1.39x faster                                                                |
| comprehensions             | 14.1 us                                                     | 10.4 us: 1.36x faster                                                                |
| async_tree_none            | 291 ms                                                      | 215 ms: 1.35x faster                                                                 |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 381 ms: 1.32x faster                                                                 |
| async_tree_io              | 731 ms                                                      | 561 ms: 1.30x faster                                                                 |
| deepcopy                   | 238 us                                                      | 187 us: 1.27x faster                                                                 |
| async_tree_memoization     | 339 ms                                                      | 267 ms: 1.27x faster                                                                 |
| scimark_fft                | 184 ms                                                      | 147 ms: 1.26x faster                                                                 |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.04 ms: 1.26x faster                                                                |
| float                      | 56.8 ms                                                     | 45.3 ms: 1.25x faster                                                                |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 396 ms: 1.24x faster                                                                 |
| crypto_pyaes               | 48.5 ms                                                     | 40.8 ms: 1.19x faster                                                                |
| pyflate                    | 295 ms                                                      | 253 ms: 1.16x faster                                                                 |
| scimark_monte_carlo        | 43.7 ms                                                     | 38.2 ms: 1.14x faster                                                                |
| deepcopy_reduce            | 2.09 us                                                     | 1.85 us: 1.13x faster                                                                |
| fannkuch                   | 247 ms                                                      | 219 ms: 1.13x faster                                                                 |
| regex_dna                  | 126 ms                                                      | 116 ms: 1.09x faster                                                                 |
| xml_etree_generate         | 55.8 ms                                                     | 51.4 ms: 1.09x faster                                                                |
| chaos                      | 43.3 ms                                                     | 39.9 ms: 1.09x faster                                                                |
| pprint_safe_repr           | 513 ms                                                      | 477 ms: 1.08x faster                                                                 |
| pprint_pformat             | 1.05 sec                                                    | 973 ms: 1.07x faster                                                                 |
| tomli_loads                | 1.37 sec                                                    | 1.28 sec: 1.07x faster                                                               |
| xml_etree_iterparse        | 65.2 ms                                                     | 61.2 ms: 1.07x faster                                                                |
| bench_thread_pool          | 857 us                                                      | 807 us: 1.06x faster                                                                 |
| logging_silent             | 60.5 ns                                                     | 57.3 ns: 1.05x faster                                                                |
| meteor_contest             | 74.6 ms                                                     | 71.1 ms: 1.05x faster                                                                |
| pickle_pure_python         | 195 us                                                      | 187 us: 1.04x faster                                                                 |
| logging_format             | 6.72 us                                                     | 6.45 us: 1.04x faster                                                                |
| logging_simple             | 6.28 us                                                     | 6.03 us: 1.04x faster                                                                |
| regex_effbot               | 1.62 ms                                                     | 1.56 ms: 1.04x faster                                                                |
| coroutines                 | 14.3 ms                                                     | 13.8 ms: 1.03x faster                                                                |
| dulwich_log                | 44.3 ms                                                     | 43.2 ms: 1.03x faster                                                                |
| pidigits                   | 152 ms                                                      | 150 ms: 1.02x faster                                                                 |
| xml_etree_process          | 37.7 ms                                                     | 37.3 ms: 1.01x faster                                                                |
| generators                 | 22.5 ms                                                     | 22.2 ms: 1.01x faster                                                                |
| regex_v8                   | 14.2 ms                                                     | 14.4 ms: 1.01x slower                                                                |
| pathlib                    | 80.5 ms                                                     | 81.1 ms: 1.01x slower                                                                |
| nqueens                    | 62.8 ms                                                     | 63.5 ms: 1.01x slower                                                                |
| unpickle_pure_python       | 133 us                                                      | 135 us: 1.01x slower                                                                 |
| raytrace                   | 192 ms                                                      | 195 ms: 1.01x slower                                                                 |
| json_loads                 | 13.9 us                                                     | 14.1 us: 1.02x slower                                                                |
| gc_traversal               | 1.52 ms                                                     | 1.56 ms: 1.03x slower                                                                |
| regex_compile              | 87.5 ms                                                     | 90.5 ms: 1.03x slower                                                                |
| sqlglot_parse              | 804 us                                                      | 837 us: 1.04x slower                                                                 |
| sqlglot_normalize          | 187 ms                                                      | 195 ms: 1.04x slower                                                                 |
| sqlglot_transpile          | 1.02 ms                                                     | 1.08 ms: 1.06x slower                                                                |
| json_dumps                 | 5.70 ms                                                     | 6.10 ms: 1.07x slower                                                                |
| sympy_sum                  | 91.5 ms                                                     | 98.0 ms: 1.07x slower                                                                |
| sqlglot_optimize           | 34.5 ms                                                     | 37.0 ms: 1.07x slower                                                                |
| tornado_http               | 89.5 ms                                                     | 96.0 ms: 1.07x slower                                                                |
| async_generators           | 239 ms                                                      | 258 ms: 1.08x slower                                                                 |
| sympy_str                  | 175 ms                                                      | 190 ms: 1.08x slower                                                                 |
| telco                      | 4.13 ms                                                     | 4.51 ms: 1.09x slower                                                                |
| deltablue                  | 2.16 ms                                                     | 2.37 ms: 1.10x slower                                                                |
| 2to3                       | 218 ms                                                      | 240 ms: 1.10x slower                                                                 |
| docutils                   | 1.66 sec                                                    | 1.83 sec: 1.10x slower                                                               |
| richards                   | 28.4 ms                                                     | 31.3 ms: 1.10x slower                                                                |
| go                         | 91.6 ms                                                     | 101 ms: 1.11x slower                                                                 |
| bench_mp_pool              | 69.2 ms                                                     | 76.7 ms: 1.11x slower                                                                |
| richards_super             | 32.1 ms                                                     | 35.6 ms: 1.11x slower                                                                |
| asyncio_tcp                | 487 ms                                                      | 542 ms: 1.11x slower                                                                 |
| django_template            | 22.9 ms                                                     | 25.6 ms: 1.11x slower                                                                |
| mdp                        | 1.37 sec                                                    | 1.55 sec: 1.13x slower                                                               |
| sympy_integrate            | 13.0 ms                                                     | 14.9 ms: 1.15x slower                                                                |
| python_startup_no_site     | 16.2 ms                                                     | 18.7 ms: 1.15x slower                                                                |
| coverage                   | 40.8 ms                                                     | 47.0 ms: 1.15x slower                                                                |
| sympy_expand               | 284 ms                                                      | 329 ms: 1.16x slower                                                                 |
| hexiom                     | 4.10 ms                                                     | 4.77 ms: 1.16x slower                                                                |
| python_startup             | 19.5 ms                                                     | 22.7 ms: 1.16x slower                                                                |
| scimark_sor                | 78.8 ms                                                     | 92.0 ms: 1.17x slower                                                                |
| create_gc_cycles           | 752 us                                                      | 907 us: 1.21x slower                                                                 |
| scimark_lu                 | 58.9 ms                                                     | 71.5 ms: 1.22x slower                                                                |
| typing_runtime_protocols   | 95.1 us                                                     | 116 us: 1.22x slower                                                                 |
| Geometric mean             | (ref)                                                       | 1.05x faster                                                                         |

Benchmark hidden because not significant (3): pycparser, xml_etree_parse, json
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240801-3.14.0a0-1b65c46-JIT/bm-20240801-pythonperf1-amd64-faster%2dcpython-monitoring_branch_ta-3.14.0a0-1b65c46.json: genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 83.22% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown
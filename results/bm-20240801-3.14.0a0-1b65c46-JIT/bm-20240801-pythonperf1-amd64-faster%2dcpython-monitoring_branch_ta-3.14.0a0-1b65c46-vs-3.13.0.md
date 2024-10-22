# Results vs. 3.13.0

- fork: faster-cpython
- ref: monitoring_branch_ta
- machine: windows-amd64
- commit hash: 1b65c46
- commit date: 2024-08-01
- overall geometric mean: 1.00x faster
- HPT reliability: 99.63%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240801-pythonperf1-amd64-faster%2dcpython-monitoring_branch_ta-3.14.0a0-1b65c46 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| 2to3           | 217 ms                                                      | 240 ms: 1.11x slower                                                                 |
| docutils       | 1.57 sec                                                    | 1.83 sec: 1.16x slower                                                               |
| html5lib       | 38.6 ms                                                     | 41.9 ms: 1.09x slower                                                                |
| tornado_http   | 92.8 ms                                                     | 96.0 ms: 1.03x slower                                                                |
| Geometric mean | (ref)                                                       | 1.10x slower                                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240801-pythonperf1-amd64-faster%2dcpython-monitoring_branch_ta-3.14.0a0-1b65c46 |
|----------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| asyncio_tcp                | 654 ms                                                      | 542 ms: 1.21x faster                                                                 |
| asyncio_tcp_ssl            | 1.64 sec                                                    | 1.41 sec: 1.16x faster                                                               |
| async_tree_memoization_tg  | 288 ms                                                      | 250 ms: 1.15x faster                                                                 |
| async_tree_none_tg         | 206 ms                                                      | 193 ms: 1.07x faster                                                                 |
| async_tree_none            | 223 ms                                                      | 215 ms: 1.04x faster                                                                 |
| async_tree_cpu_io_mixed_tg | 375 ms                                                      | 381 ms: 1.02x slower                                                                 |
| async_tree_cpu_io_mixed    | 387 ms                                                      | 396 ms: 1.02x slower                                                                 |
| async_tree_io_tg           | 512 ms                                                      | 541 ms: 1.05x slower                                                                 |
| async_tree_io              | 521 ms                                                      | 561 ms: 1.08x slower                                                                 |
| coroutines                 | 12.5 ms                                                     | 13.8 ms: 1.10x slower                                                                |
| async_generators           | 223 ms                                                      | 258 ms: 1.16x slower                                                                 |
| Geometric mean             | (ref)                                                       | 1.02x faster                                                                         |

Benchmark hidden because not significant (1): async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240801-pythonperf1-amd64-faster%2dcpython-monitoring_branch_ta-3.14.0a0-1b65c46 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| nbody          | 64.5 ms                                                     | 49.7 ms: 1.30x faster                                                                |
| float          | 48.1 ms                                                     | 45.3 ms: 1.06x faster                                                                |
| pidigits       | 148 ms                                                      | 150 ms: 1.01x slower                                                                 |
| Geometric mean | (ref)                                                       | 1.11x faster                                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240801-pythonperf1-amd64-faster%2dcpython-monitoring_branch_ta-3.14.0a0-1b65c46 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| regex_effbot   | 1.62 ms                                                     | 1.56 ms: 1.04x faster                                                                |
| regex_v8       | 14.7 ms                                                     | 14.4 ms: 1.02x faster                                                                |
| regex_dna      | 114 ms                                                      | 116 ms: 1.01x slower                                                                 |
| regex_compile  | 80.1 ms                                                     | 90.5 ms: 1.13x slower                                                                |
| Geometric mean | (ref)                                                       | 1.02x slower                                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240801-pythonperf1-amd64-faster%2dcpython-monitoring_branch_ta-3.14.0a0-1b65c46 |
|----------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| tomli_loads          | 1.36 sec                                                    | 1.28 sec: 1.07x faster                                                               |
| xml_etree_generate   | 53.3 ms                                                     | 51.4 ms: 1.04x faster                                                                |
| xml_etree_iterparse  | 62.3 ms                                                     | 61.2 ms: 1.02x faster                                                                |
| json_loads           | 14.3 us                                                     | 14.1 us: 1.01x faster                                                                |
| xml_etree_process    | 36.5 ms                                                     | 37.3 ms: 1.02x slower                                                                |
| pickle_pure_python   | 183 us                                                      | 187 us: 1.02x slower                                                                 |
| json_dumps           | 5.76 ms                                                     | 6.10 ms: 1.06x slower                                                                |
| unpickle_pure_python | 127 us                                                      | 135 us: 1.07x slower                                                                 |
| Geometric mean       | (ref)                                                       | 1.00x slower                                                                         |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240801-pythonperf1-amd64-faster%2dcpython-monitoring_branch_ta-3.14.0a0-1b65c46 |
|------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| python_startup         | 22.2 ms                                                     | 22.7 ms: 1.02x slower                                                                |
| python_startup_no_site | 17.8 ms                                                     | 18.7 ms: 1.05x slower                                                                |
| Geometric mean         | (ref)                                                       | 1.04x slower                                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240801-pythonperf1-amd64-faster%2dcpython-monitoring_branch_ta-3.14.0a0-1b65c46 |
|-----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| mako            | 6.24 ms                                                     | 5.10 ms: 1.22x faster                                                                |
| django_template | 21.8 ms                                                     | 25.6 ms: 1.17x slower                                                                |
| genshi_xml      | 32.8 ms                                                     | 38.6 ms: 1.18x slower                                                                |
| genshi_text     | 14.9 ms                                                     | 17.8 ms: 1.20x slower                                                                |
| Geometric mean  | (ref)                                                       | 1.08x slower                                                                         |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240801-pythonperf1-amd64-faster%2dcpython-monitoring_branch_ta-3.14.0a0-1b65c46 |
|----------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| thrift                     | 8.68 ms                                                     | 519 us: 16.73x faster                                                                |
| deepcopy_memo              | 21.8 us                                                     | 16.1 us: 1.35x faster                                                                |
| nbody                      | 64.5 ms                                                     | 49.7 ms: 1.30x faster                                                                |
| spectral_norm              | 59.2 ms                                                     | 45.7 ms: 1.30x faster                                                                |
| mako                       | 6.24 ms                                                     | 5.10 ms: 1.22x faster                                                                |
| asyncio_tcp                | 654 ms                                                      | 542 ms: 1.21x faster                                                                 |
| deepcopy                   | 223 us                                                      | 187 us: 1.19x faster                                                                 |
| scimark_fft                | 174 ms                                                      | 147 ms: 1.19x faster                                                                 |
| asyncio_tcp_ssl            | 1.64 sec                                                    | 1.41 sec: 1.16x faster                                                               |
| async_tree_memoization_tg  | 288 ms                                                      | 250 ms: 1.15x faster                                                                 |
| scimark_sparse_mat_mult    | 2.34 ms                                                     | 2.04 ms: 1.15x faster                                                                |
| fannkuch                   | 245 ms                                                      | 219 ms: 1.12x faster                                                                 |
| deepcopy_reduce            | 2.02 us                                                     | 1.85 us: 1.09x faster                                                                |
| pycparser                  | 758 ms                                                      | 695 ms: 1.09x faster                                                                 |
| pyflate                    | 275 ms                                                      | 253 ms: 1.09x faster                                                                 |
| telco                      | 4.85 ms                                                     | 4.51 ms: 1.07x faster                                                                |
| tomli_loads                | 1.36 sec                                                    | 1.28 sec: 1.07x faster                                                               |
| async_tree_none_tg         | 206 ms                                                      | 193 ms: 1.07x faster                                                                 |
| float                      | 48.1 ms                                                     | 45.3 ms: 1.06x faster                                                                |
| scimark_monte_carlo        | 40.3 ms                                                     | 38.2 ms: 1.05x faster                                                                |
| crypto_pyaes               | 42.8 ms                                                     | 40.8 ms: 1.05x faster                                                                |
| async_tree_none            | 223 ms                                                      | 215 ms: 1.04x faster                                                                 |
| xml_etree_generate         | 53.3 ms                                                     | 51.4 ms: 1.04x faster                                                                |
| regex_effbot               | 1.62 ms                                                     | 1.56 ms: 1.04x faster                                                                |
| pprint_safe_repr           | 493 ms                                                      | 477 ms: 1.03x faster                                                                 |
| bench_thread_pool          | 828 us                                                      | 807 us: 1.03x faster                                                                 |
| regex_v8                   | 14.7 ms                                                     | 14.4 ms: 1.02x faster                                                                |
| pprint_pformat             | 991 ms                                                      | 973 ms: 1.02x faster                                                                 |
| xml_etree_iterparse        | 62.3 ms                                                     | 61.2 ms: 1.02x faster                                                                |
| meteor_contest             | 72.3 ms                                                     | 71.1 ms: 1.02x faster                                                                |
| json_loads                 | 14.3 us                                                     | 14.1 us: 1.01x faster                                                                |
| gc_traversal               | 1.55 ms                                                     | 1.56 ms: 1.01x slower                                                                |
| coverage                   | 46.7 ms                                                     | 47.0 ms: 1.01x slower                                                                |
| pidigits                   | 148 ms                                                      | 150 ms: 1.01x slower                                                                 |
| regex_dna                  | 114 ms                                                      | 116 ms: 1.01x slower                                                                 |
| async_tree_cpu_io_mixed_tg | 375 ms                                                      | 381 ms: 1.02x slower                                                                 |
| xml_etree_process          | 36.5 ms                                                     | 37.3 ms: 1.02x slower                                                                |
| json                       | 2.98 ms                                                     | 3.04 ms: 1.02x slower                                                                |
| pickle_pure_python         | 183 us                                                      | 187 us: 1.02x slower                                                                 |
| python_startup             | 22.2 ms                                                     | 22.7 ms: 1.02x slower                                                                |
| async_tree_cpu_io_mixed    | 387 ms                                                      | 396 ms: 1.02x slower                                                                 |
| tornado_http               | 92.8 ms                                                     | 96.0 ms: 1.03x slower                                                                |
| logging_format             | 6.15 us                                                     | 6.45 us: 1.05x slower                                                                |
| python_startup_no_site     | 17.8 ms                                                     | 18.7 ms: 1.05x slower                                                                |
| logging_simple             | 5.72 us                                                     | 6.03 us: 1.05x slower                                                                |
| chaos                      | 37.9 ms                                                     | 39.9 ms: 1.05x slower                                                                |
| async_tree_io_tg           | 512 ms                                                      | 541 ms: 1.05x slower                                                                 |
| json_dumps                 | 5.76 ms                                                     | 6.10 ms: 1.06x slower                                                                |
| unpickle_pure_python       | 127 us                                                      | 135 us: 1.07x slower                                                                 |
| dulwich_log                | 40.4 ms                                                     | 43.2 ms: 1.07x slower                                                                |
| async_tree_io              | 521 ms                                                      | 561 ms: 1.08x slower                                                                 |
| html5lib                   | 38.6 ms                                                     | 41.9 ms: 1.09x slower                                                                |
| create_gc_cycles           | 829 us                                                      | 907 us: 1.09x slower                                                                 |
| coroutines                 | 12.5 ms                                                     | 13.8 ms: 1.10x slower                                                                |
| sqlglot_parse              | 761 us                                                      | 837 us: 1.10x slower                                                                 |
| bench_mp_pool              | 69.6 ms                                                     | 76.7 ms: 1.10x slower                                                                |
| 2to3                       | 217 ms                                                      | 240 ms: 1.11x slower                                                                 |
| sqlglot_optimize           | 33.1 ms                                                     | 37.0 ms: 1.12x slower                                                                |
| mdp                        | 1.38 sec                                                    | 1.55 sec: 1.12x slower                                                               |
| logging_silent             | 51.0 ns                                                     | 57.3 ns: 1.12x slower                                                                |
| regex_compile              | 80.1 ms                                                     | 90.5 ms: 1.13x slower                                                                |
| sympy_sum                  | 86.4 ms                                                     | 98.0 ms: 1.13x slower                                                                |
| sqlglot_transpile          | 952 us                                                      | 1.08 ms: 1.14x slower                                                                |
| sqlglot_normalize          | 171 ms                                                      | 195 ms: 1.14x slower                                                                 |
| sympy_str                  | 166 ms                                                      | 190 ms: 1.14x slower                                                                 |
| generators                 | 19.5 ms                                                     | 22.2 ms: 1.14x slower                                                                |
| nqueens                    | 55.5 ms                                                     | 63.5 ms: 1.14x slower                                                                |
| sympy_expand               | 285 ms                                                      | 329 ms: 1.15x slower                                                                 |
| typing_runtime_protocols   | 100 us                                                      | 116 us: 1.15x slower                                                                 |
| async_generators           | 223 ms                                                      | 258 ms: 1.16x slower                                                                 |
| docutils                   | 1.57 sec                                                    | 1.83 sec: 1.16x slower                                                               |
| django_template            | 21.8 ms                                                     | 25.6 ms: 1.17x slower                                                                |
| genshi_xml                 | 32.8 ms                                                     | 38.6 ms: 1.18x slower                                                                |
| genshi_text                | 14.9 ms                                                     | 17.8 ms: 1.20x slower                                                                |
| go                         | 84.6 ms                                                     | 101 ms: 1.20x slower                                                                 |
| pylint                     | 211 ms                                                      | 253 ms: 1.20x slower                                                                 |
| richards                   | 26.0 ms                                                     | 31.3 ms: 1.20x slower                                                                |
| sympy_integrate            | 12.3 ms                                                     | 14.9 ms: 1.21x slower                                                                |
| richards_super             | 29.3 ms                                                     | 35.6 ms: 1.21x slower                                                                |
| raytrace                   | 156 ms                                                      | 195 ms: 1.25x slower                                                                 |
| deltablue                  | 1.86 ms                                                     | 2.37 ms: 1.27x slower                                                                |
| scimark_sor                | 72.0 ms                                                     | 92.0 ms: 1.28x slower                                                                |
| hexiom                     | 3.69 ms                                                     | 4.77 ms: 1.29x slower                                                                |
| scimark_lu                 | 54.0 ms                                                     | 71.5 ms: 1.32x slower                                                                |
| Geometric mean             | (ref)                                                       | 1.00x faster                                                                         |

Benchmark hidden because not significant (4): async_tree_memoization, xml_etree_parse, pathlib, comprehensions
Ignored benchmarks (11) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 99.63% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown
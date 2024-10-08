# Results vs. 3.13.0b2

- fork: brandtbucher
- ref: faster_jit_builds
- machine: windows-amd64
- commit hash: 60b7e71
- commit date: 2024-07-27
- overall geometric mean: 1.01x faster
- HPT reliability: 97.35%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240727-pythonperf1-amd64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|----------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| 2to3           | 207 ms                                                          | 238 ms: 1.15x slower                                                          |
| docutils       | 1.63 sec                                                        | 1.83 sec: 1.12x slower                                                        |
| html5lib       | 35.0 ms                                                         | 40.1 ms: 1.14x slower                                                         |
| tornado_http   | 81.8 ms                                                         | 94.0 ms: 1.15x slower                                                         |
| Geometric mean | (ref)                                                           | 1.14x slower                                                                  |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240727-pythonperf1-amd64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|---------------------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| async_tree_io_tg          | 605 ms                                                          | 526 ms: 1.15x faster                                                          |
| async_tree_io             | 588 ms                                                          | 536 ms: 1.10x faster                                                          |
| async_tree_none_tg        | 202 ms                                                          | 187 ms: 1.08x faster                                                          |
| async_tree_memoization_tg | 258 ms                                                          | 242 ms: 1.07x faster                                                          |
| async_tree_none           | 218 ms                                                          | 208 ms: 1.05x faster                                                          |
| async_tree_memoization    | 264 ms                                                          | 255 ms: 1.04x faster                                                          |
| Geometric mean            | (ref)                                                           | 1.06x faster                                                                  |

Benchmark hidden because not significant (2): async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240727-pythonperf1-amd64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|----------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| nbody          | 67.6 ms                                                         | 50.9 ms: 1.33x faster                                                         |
| float          | 49.7 ms                                                         | 43.9 ms: 1.13x faster                                                         |
| pidigits       | 150 ms                                                          | 150 ms: 1.00x slower                                                          |
| Geometric mean | (ref)                                                           | 1.14x faster                                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240727-pythonperf1-amd64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|----------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| regex_effbot   | 1.58 ms                                                         | 1.60 ms: 1.01x slower                                                         |
| regex_dna      | 119 ms                                                          | 121 ms: 1.01x slower                                                          |
| regex_compile  | 78.0 ms                                                         | 89.4 ms: 1.15x slower                                                         |
| Geometric mean | (ref)                                                           | 1.04x slower                                                                  |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240727-pythonperf1-amd64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|----------------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| tomli_loads          | 1.35 sec                                                        | 1.25 sec: 1.08x faster                                                        |
| xml_etree_generate   | 53.2 ms                                                         | 52.5 ms: 1.01x faster                                                         |
| xml_etree_iterparse  | 62.3 ms                                                         | 61.8 ms: 1.01x faster                                                         |
| xml_etree_parse      | 90.9 ms                                                         | 92.7 ms: 1.02x slower                                                         |
| xml_etree_process    | 36.4 ms                                                         | 37.2 ms: 1.02x slower                                                         |
| pickle_pure_python   | 175 us                                                          | 181 us: 1.03x slower                                                          |
| json_dumps           | 5.61 ms                                                         | 5.80 ms: 1.03x slower                                                         |
| unpickle_pure_python | 122 us                                                          | 130 us: 1.07x slower                                                          |
| Geometric mean       | (ref)                                                           | 1.01x slower                                                                  |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240727-pythonperf1-amd64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|------------------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| python_startup         | 20.3 ms                                                         | 22.0 ms: 1.08x slower                                                         |
| python_startup_no_site | 16.2 ms                                                         | 18.2 ms: 1.13x slower                                                         |
| Geometric mean         | (ref)                                                           | 1.10x slower                                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240727-pythonperf1-amd64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|-----------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| mako            | 6.36 ms                                                         | 4.98 ms: 1.28x faster                                                         |
| django_template | 21.7 ms                                                         | 25.5 ms: 1.18x slower                                                         |
| genshi_text     | 14.4 ms                                                         | 17.7 ms: 1.23x slower                                                         |
| genshi_xml      | 31.6 ms                                                         | 44.7 ms: 1.41x slower                                                         |
| Geometric mean  | (ref)                                                           | 1.13x slower                                                                  |

All benchmarks:
===============

| Benchmark                 | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240727-pythonperf1-amd64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|---------------------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| thrift                    | 8.11 ms                                                         | 502 us: 16.14x faster                                                         |
| deepcopy_memo             | 22.1 us                                                         | 15.5 us: 1.43x faster                                                         |
| spectral_norm             | 63.7 ms                                                         | 46.1 ms: 1.38x faster                                                         |
| nbody                     | 67.6 ms                                                         | 50.9 ms: 1.33x faster                                                         |
| mako                      | 6.36 ms                                                         | 4.98 ms: 1.28x faster                                                         |
| scimark_sparse_mat_mult   | 2.50 ms                                                         | 2.01 ms: 1.24x faster                                                         |
| deepcopy                  | 220 us                                                          | 182 us: 1.21x faster                                                          |
| async_tree_io_tg          | 605 ms                                                          | 526 ms: 1.15x faster                                                          |
| scimark_fft               | 171 ms                                                          | 149 ms: 1.15x faster                                                          |
| float                     | 49.7 ms                                                         | 43.9 ms: 1.13x faster                                                         |
| pyflate                   | 279 ms                                                          | 247 ms: 1.13x faster                                                          |
| crypto_pyaes              | 45.5 ms                                                         | 40.5 ms: 1.12x faster                                                         |
| fannkuch                  | 243 ms                                                          | 219 ms: 1.11x faster                                                          |
| async_tree_io             | 588 ms                                                          | 536 ms: 1.10x faster                                                          |
| deepcopy_reduce           | 1.99 us                                                         | 1.83 us: 1.09x faster                                                         |
| async_tree_none_tg        | 202 ms                                                          | 187 ms: 1.08x faster                                                          |
| tomli_loads               | 1.35 sec                                                        | 1.25 sec: 1.08x faster                                                        |
| json                      | 3.19 ms                                                         | 2.97 ms: 1.07x faster                                                         |
| async_tree_memoization_tg | 258 ms                                                          | 242 ms: 1.07x faster                                                          |
| pycparser                 | 754 ms                                                          | 708 ms: 1.06x faster                                                          |
| async_tree_none           | 218 ms                                                          | 208 ms: 1.05x faster                                                          |
| scimark_monte_carlo       | 39.1 ms                                                         | 37.4 ms: 1.05x faster                                                         |
| telco                     | 4.67 ms                                                         | 4.47 ms: 1.05x faster                                                         |
| async_tree_memoization    | 264 ms                                                          | 255 ms: 1.04x faster                                                          |
| pprint_pformat            | 966 ms                                                          | 950 ms: 1.02x faster                                                          |
| comprehensions            | 10.4 us                                                         | 10.2 us: 1.01x faster                                                         |
| xml_etree_generate        | 53.2 ms                                                         | 52.5 ms: 1.01x faster                                                         |
| pprint_safe_repr          | 474 ms                                                          | 468 ms: 1.01x faster                                                          |
| xml_etree_iterparse       | 62.3 ms                                                         | 61.8 ms: 1.01x faster                                                         |
| pidigits                  | 150 ms                                                          | 150 ms: 1.00x slower                                                          |
| regex_effbot              | 1.58 ms                                                         | 1.60 ms: 1.01x slower                                                         |
| gc_traversal              | 1.55 ms                                                         | 1.58 ms: 1.01x slower                                                         |
| regex_dna                 | 119 ms                                                          | 121 ms: 1.01x slower                                                          |
| xml_etree_parse           | 90.9 ms                                                         | 92.7 ms: 1.02x slower                                                         |
| xml_etree_process         | 36.4 ms                                                         | 37.2 ms: 1.02x slower                                                         |
| create_gc_cycles          | 888 us                                                          | 910 us: 1.02x slower                                                          |
| meteor_contest            | 69.9 ms                                                         | 71.8 ms: 1.03x slower                                                         |
| pickle_pure_python        | 175 us                                                          | 181 us: 1.03x slower                                                          |
| json_dumps                | 5.61 ms                                                         | 5.80 ms: 1.03x slower                                                         |
| chaos                     | 38.4 ms                                                         | 39.7 ms: 1.04x slower                                                         |
| nqueens                   | 56.7 ms                                                         | 59.0 ms: 1.04x slower                                                         |
| coroutines                | 12.8 ms                                                         | 13.3 ms: 1.04x slower                                                         |
| logging_silent            | 52.9 ns                                                         | 55.4 ns: 1.05x slower                                                         |
| bench_thread_pool         | 768 us                                                          | 815 us: 1.06x slower                                                          |
| unpickle_pure_python      | 122 us                                                          | 130 us: 1.07x slower                                                          |
| pathlib                   | 75.9 ms                                                         | 81.4 ms: 1.07x slower                                                         |
| sqlglot_parse             | 748 us                                                          | 808 us: 1.08x slower                                                          |
| raytrace                  | 162 ms                                                          | 176 ms: 1.08x slower                                                          |
| python_startup            | 20.3 ms                                                         | 22.0 ms: 1.08x slower                                                         |
| sqlglot_transpile         | 955 us                                                          | 1.04 ms: 1.09x slower                                                         |
| dulwich_log               | 38.0 ms                                                         | 41.8 ms: 1.10x slower                                                         |
| generators                | 19.6 ms                                                         | 21.6 ms: 1.10x slower                                                         |
| mdp                       | 1.31 sec                                                        | 1.45 sec: 1.11x slower                                                        |
| richards_super            | 30.2 ms                                                         | 33.5 ms: 1.11x slower                                                         |
| sqlglot_normalize         | 173 ms                                                          | 192 ms: 1.11x slower                                                          |
| sqlglot_optimize          | 32.7 ms                                                         | 36.4 ms: 1.11x slower                                                         |
| coverage                  | 42.1 ms                                                         | 47.0 ms: 1.12x slower                                                         |
| sympy_sum                 | 84.4 ms                                                         | 94.5 ms: 1.12x slower                                                         |
| richards                  | 26.7 ms                                                         | 29.9 ms: 1.12x slower                                                         |
| bench_mp_pool             | 64.8 ms                                                         | 72.6 ms: 1.12x slower                                                         |
| docutils                  | 1.63 sec                                                        | 1.83 sec: 1.12x slower                                                        |
| python_startup_no_site    | 16.2 ms                                                         | 18.2 ms: 1.13x slower                                                         |
| asyncio_tcp               | 471 ms                                                          | 531 ms: 1.13x slower                                                          |
| async_generators          | 223 ms                                                          | 252 ms: 1.13x slower                                                          |
| deltablue                 | 1.88 ms                                                         | 2.14 ms: 1.14x slower                                                         |
| scimark_sor               | 75.3 ms                                                         | 86.1 ms: 1.14x slower                                                         |
| html5lib                  | 35.0 ms                                                         | 40.1 ms: 1.14x slower                                                         |
| sympy_str                 | 159 ms                                                          | 182 ms: 1.15x slower                                                          |
| regex_compile             | 78.0 ms                                                         | 89.4 ms: 1.15x slower                                                         |
| tornado_http              | 81.8 ms                                                         | 94.0 ms: 1.15x slower                                                         |
| 2to3                      | 207 ms                                                          | 238 ms: 1.15x slower                                                          |
| go                        | 82.1 ms                                                         | 95.4 ms: 1.16x slower                                                         |
| sympy_expand              | 271 ms                                                          | 315 ms: 1.16x slower                                                          |
| sympy_integrate           | 12.2 ms                                                         | 14.2 ms: 1.16x slower                                                         |
| typing_runtime_protocols  | 101 us                                                          | 118 us: 1.17x slower                                                          |
| django_template           | 21.7 ms                                                         | 25.5 ms: 1.18x slower                                                         |
| pylint                    | 205 ms                                                          | 246 ms: 1.20x slower                                                          |
| genshi_text               | 14.4 ms                                                         | 17.7 ms: 1.23x slower                                                         |
| hexiom                    | 3.72 ms                                                         | 4.65 ms: 1.25x slower                                                         |
| scimark_lu                | 56.6 ms                                                         | 72.0 ms: 1.27x slower                                                         |
| genshi_xml                | 31.6 ms                                                         | 44.7 ms: 1.41x slower                                                         |
| Geometric mean            | (ref)                                                           | 1.01x faster                                                                  |

Benchmark hidden because not significant (7): async_tree_cpu_io_mixed, regex_v8, asyncio_tcp_ssl, logging_format, logging_simple, json_loads, async_tree_cpu_io_mixed_tg
Ignored benchmarks (10) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 97.35% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown
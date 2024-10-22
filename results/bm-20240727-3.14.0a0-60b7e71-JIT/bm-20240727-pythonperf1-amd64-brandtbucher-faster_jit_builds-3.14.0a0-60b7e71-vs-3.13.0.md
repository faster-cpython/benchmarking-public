# Results vs. 3.13.0

- fork: brandtbucher
- ref: faster_jit_builds
- machine: windows-amd64
- commit hash: 60b7e71
- commit date: 2024-07-27
- overall geometric mean: 1.02x faster
- HPT reliability: 97.89%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240727-pythonperf1-amd64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| 2to3           | 217 ms                                                      | 238 ms: 1.10x slower                                                          |
| docutils       | 1.57 sec                                                    | 1.83 sec: 1.16x slower                                                        |
| html5lib       | 38.6 ms                                                     | 40.1 ms: 1.04x slower                                                         |
| tornado_http   | 92.8 ms                                                     | 94.0 ms: 1.01x slower                                                         |
| Geometric mean | (ref)                                                       | 1.08x slower                                                                  |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240727-pythonperf1-amd64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|----------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| asyncio_tcp                | 654 ms                                                      | 531 ms: 1.23x faster                                                          |
| async_tree_memoization_tg  | 288 ms                                                      | 242 ms: 1.19x faster                                                          |
| asyncio_tcp_ssl            | 1.64 sec                                                    | 1.46 sec: 1.12x faster                                                        |
| async_tree_none_tg         | 206 ms                                                      | 187 ms: 1.10x faster                                                          |
| async_tree_none            | 223 ms                                                      | 208 ms: 1.07x faster                                                          |
| async_tree_memoization     | 271 ms                                                      | 255 ms: 1.06x faster                                                          |
| async_tree_cpu_io_mixed_tg | 375 ms                                                      | 384 ms: 1.03x slower                                                          |
| async_tree_io_tg           | 512 ms                                                      | 526 ms: 1.03x slower                                                          |
| async_tree_io              | 521 ms                                                      | 536 ms: 1.03x slower                                                          |
| coroutines                 | 12.5 ms                                                     | 13.3 ms: 1.06x slower                                                         |
| async_generators           | 223 ms                                                      | 252 ms: 1.13x slower                                                          |
| Geometric mean             | (ref)                                                       | 1.04x faster                                                                  |

Benchmark hidden because not significant (1): async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240727-pythonperf1-amd64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| nbody          | 64.5 ms                                                     | 50.9 ms: 1.27x faster                                                         |
| float          | 48.1 ms                                                     | 43.9 ms: 1.10x faster                                                         |
| pidigits       | 148 ms                                                      | 150 ms: 1.01x slower                                                          |
| Geometric mean | (ref)                                                       | 1.11x faster                                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240727-pythonperf1-amd64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| regex_effbot   | 1.62 ms                                                     | 1.60 ms: 1.01x faster                                                         |
| regex_dna      | 114 ms                                                      | 121 ms: 1.05x slower                                                          |
| regex_v8       | 14.7 ms                                                     | 15.5 ms: 1.06x slower                                                         |
| regex_compile  | 80.1 ms                                                     | 89.4 ms: 1.12x slower                                                         |
| Geometric mean | (ref)                                                       | 1.05x slower                                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240727-pythonperf1-amd64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|----------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| tomli_loads          | 1.36 sec                                                    | 1.25 sec: 1.09x faster                                                        |
| xml_etree_generate   | 53.3 ms                                                     | 52.5 ms: 1.02x faster                                                         |
| pickle_pure_python   | 183 us                                                      | 181 us: 1.01x faster                                                          |
| json_loads           | 14.3 us                                                     | 14.2 us: 1.01x faster                                                         |
| json_dumps           | 5.76 ms                                                     | 5.80 ms: 1.01x slower                                                         |
| xml_etree_process    | 36.5 ms                                                     | 37.2 ms: 1.02x slower                                                         |
| unpickle_pure_python | 127 us                                                      | 130 us: 1.02x slower                                                          |
| Geometric mean       | (ref)                                                       | 1.01x faster                                                                  |

Benchmark hidden because not significant (2): xml_etree_iterparse, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240727-pythonperf1-amd64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| python_startup         | 22.2 ms                                                     | 22.0 ms: 1.01x faster                                                         |
| python_startup_no_site | 17.8 ms                                                     | 18.2 ms: 1.03x slower                                                         |
| Geometric mean         | (ref)                                                       | 1.01x slower                                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240727-pythonperf1-amd64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|-----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| mako            | 6.24 ms                                                     | 4.98 ms: 1.25x faster                                                         |
| django_template | 21.8 ms                                                     | 25.5 ms: 1.17x slower                                                         |
| genshi_text     | 14.9 ms                                                     | 17.7 ms: 1.19x slower                                                         |
| genshi_xml      | 32.8 ms                                                     | 44.7 ms: 1.36x slower                                                         |
| Geometric mean  | (ref)                                                       | 1.11x slower                                                                  |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240727-pythonperf1-amd64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|----------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| thrift                     | 8.68 ms                                                     | 502 us: 17.28x faster                                                         |
| deepcopy_memo              | 21.8 us                                                     | 15.5 us: 1.41x faster                                                         |
| spectral_norm              | 59.2 ms                                                     | 46.1 ms: 1.28x faster                                                         |
| nbody                      | 64.5 ms                                                     | 50.9 ms: 1.27x faster                                                         |
| mako                       | 6.24 ms                                                     | 4.98 ms: 1.25x faster                                                         |
| asyncio_tcp                | 654 ms                                                      | 531 ms: 1.23x faster                                                          |
| deepcopy                   | 223 us                                                      | 182 us: 1.23x faster                                                          |
| async_tree_memoization_tg  | 288 ms                                                      | 242 ms: 1.19x faster                                                          |
| scimark_fft                | 174 ms                                                      | 149 ms: 1.17x faster                                                          |
| scimark_sparse_mat_mult    | 2.34 ms                                                     | 2.01 ms: 1.16x faster                                                         |
| asyncio_tcp_ssl            | 1.64 sec                                                    | 1.46 sec: 1.12x faster                                                        |
| fannkuch                   | 245 ms                                                      | 219 ms: 1.12x faster                                                          |
| pyflate                    | 275 ms                                                      | 247 ms: 1.11x faster                                                          |
| deepcopy_reduce            | 2.02 us                                                     | 1.83 us: 1.11x faster                                                         |
| async_tree_none_tg         | 206 ms                                                      | 187 ms: 1.10x faster                                                          |
| float                      | 48.1 ms                                                     | 43.9 ms: 1.10x faster                                                         |
| tomli_loads                | 1.36 sec                                                    | 1.25 sec: 1.09x faster                                                        |
| telco                      | 4.85 ms                                                     | 4.47 ms: 1.09x faster                                                         |
| scimark_monte_carlo        | 40.3 ms                                                     | 37.4 ms: 1.08x faster                                                         |
| async_tree_none            | 223 ms                                                      | 208 ms: 1.07x faster                                                          |
| pycparser                  | 758 ms                                                      | 708 ms: 1.07x faster                                                          |
| async_tree_memoization     | 271 ms                                                      | 255 ms: 1.06x faster                                                          |
| crypto_pyaes               | 42.8 ms                                                     | 40.5 ms: 1.06x faster                                                         |
| pprint_safe_repr           | 493 ms                                                      | 468 ms: 1.05x faster                                                          |
| pprint_pformat             | 991 ms                                                      | 950 ms: 1.04x faster                                                          |
| xml_etree_generate         | 53.3 ms                                                     | 52.5 ms: 1.02x faster                                                         |
| regex_effbot               | 1.62 ms                                                     | 1.60 ms: 1.01x faster                                                         |
| pickle_pure_python         | 183 us                                                      | 181 us: 1.01x faster                                                          |
| python_startup             | 22.2 ms                                                     | 22.0 ms: 1.01x faster                                                         |
| json_loads                 | 14.3 us                                                     | 14.2 us: 1.01x faster                                                         |
| meteor_contest             | 72.3 ms                                                     | 71.8 ms: 1.01x faster                                                         |
| coverage                   | 46.7 ms                                                     | 47.0 ms: 1.01x slower                                                         |
| json_dumps                 | 5.76 ms                                                     | 5.80 ms: 1.01x slower                                                         |
| pidigits                   | 148 ms                                                      | 150 ms: 1.01x slower                                                          |
| tornado_http               | 92.8 ms                                                     | 94.0 ms: 1.01x slower                                                         |
| logging_simple             | 5.72 us                                                     | 5.80 us: 1.01x slower                                                         |
| gc_traversal               | 1.55 ms                                                     | 1.58 ms: 1.01x slower                                                         |
| logging_format             | 6.15 us                                                     | 6.24 us: 1.01x slower                                                         |
| xml_etree_process          | 36.5 ms                                                     | 37.2 ms: 1.02x slower                                                         |
| unpickle_pure_python       | 127 us                                                      | 130 us: 1.02x slower                                                          |
| async_tree_cpu_io_mixed_tg | 375 ms                                                      | 384 ms: 1.03x slower                                                          |
| python_startup_no_site     | 17.8 ms                                                     | 18.2 ms: 1.03x slower                                                         |
| async_tree_io_tg           | 512 ms                                                      | 526 ms: 1.03x slower                                                          |
| async_tree_io              | 521 ms                                                      | 536 ms: 1.03x slower                                                          |
| dulwich_log                | 40.4 ms                                                     | 41.8 ms: 1.04x slower                                                         |
| html5lib                   | 38.6 ms                                                     | 40.1 ms: 1.04x slower                                                         |
| bench_mp_pool              | 69.6 ms                                                     | 72.6 ms: 1.04x slower                                                         |
| chaos                      | 37.9 ms                                                     | 39.7 ms: 1.05x slower                                                         |
| mdp                        | 1.38 sec                                                    | 1.45 sec: 1.05x slower                                                        |
| regex_dna                  | 114 ms                                                      | 121 ms: 1.05x slower                                                          |
| coroutines                 | 12.5 ms                                                     | 13.3 ms: 1.06x slower                                                         |
| regex_v8                   | 14.7 ms                                                     | 15.5 ms: 1.06x slower                                                         |
| sqlglot_parse              | 761 us                                                      | 808 us: 1.06x slower                                                          |
| nqueens                    | 55.5 ms                                                     | 59.0 ms: 1.06x slower                                                         |
| logging_silent             | 51.0 ns                                                     | 55.4 ns: 1.09x slower                                                         |
| sqlglot_transpile          | 952 us                                                      | 1.04 ms: 1.09x slower                                                         |
| sympy_sum                  | 86.4 ms                                                     | 94.5 ms: 1.09x slower                                                         |
| sympy_str                  | 166 ms                                                      | 182 ms: 1.10x slower                                                          |
| create_gc_cycles           | 829 us                                                      | 910 us: 1.10x slower                                                          |
| 2to3                       | 217 ms                                                      | 238 ms: 1.10x slower                                                          |
| sqlglot_optimize           | 33.1 ms                                                     | 36.4 ms: 1.10x slower                                                         |
| sympy_expand               | 285 ms                                                      | 315 ms: 1.10x slower                                                          |
| generators                 | 19.5 ms                                                     | 21.6 ms: 1.11x slower                                                         |
| regex_compile              | 80.1 ms                                                     | 89.4 ms: 1.12x slower                                                         |
| sqlglot_normalize          | 171 ms                                                      | 192 ms: 1.12x slower                                                          |
| raytrace                   | 156 ms                                                      | 176 ms: 1.12x slower                                                          |
| go                         | 84.6 ms                                                     | 95.4 ms: 1.13x slower                                                         |
| async_generators           | 223 ms                                                      | 252 ms: 1.13x slower                                                          |
| richards_super             | 29.3 ms                                                     | 33.5 ms: 1.14x slower                                                         |
| richards                   | 26.0 ms                                                     | 29.9 ms: 1.15x slower                                                         |
| deltablue                  | 1.86 ms                                                     | 2.14 ms: 1.15x slower                                                         |
| sympy_integrate            | 12.3 ms                                                     | 14.2 ms: 1.16x slower                                                         |
| docutils                   | 1.57 sec                                                    | 1.83 sec: 1.16x slower                                                        |
| pylint                     | 211 ms                                                      | 246 ms: 1.17x slower                                                          |
| django_template            | 21.8 ms                                                     | 25.5 ms: 1.17x slower                                                         |
| typing_runtime_protocols   | 100 us                                                      | 118 us: 1.17x slower                                                          |
| genshi_text                | 14.9 ms                                                     | 17.7 ms: 1.19x slower                                                         |
| scimark_sor                | 72.0 ms                                                     | 86.1 ms: 1.20x slower                                                         |
| hexiom                     | 3.69 ms                                                     | 4.65 ms: 1.26x slower                                                         |
| scimark_lu                 | 54.0 ms                                                     | 72.0 ms: 1.33x slower                                                         |
| genshi_xml                 | 32.8 ms                                                     | 44.7 ms: 1.36x slower                                                         |
| Geometric mean             | (ref)                                                       | 1.02x faster                                                                  |

Benchmark hidden because not significant (7): bench_thread_pool, async_tree_cpu_io_mixed, xml_etree_iterparse, xml_etree_parse, json, comprehensions, pathlib
Ignored benchmarks (11) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 97.89% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown
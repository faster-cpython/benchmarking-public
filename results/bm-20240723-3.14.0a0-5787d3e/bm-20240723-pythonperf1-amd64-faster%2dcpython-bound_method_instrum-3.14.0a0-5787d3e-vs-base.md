# Results vs. base

- fork: faster-cpython
- ref: bound_method_instrum
- machine: windows-amd64
- commit hash: 5787d3e
- commit date: 2024-07-23
- overall geometric mean: 1.04x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240723-pythonperf1-amd64-python-2c1b1e7a07eba0138b98-3.14.0a0-2c1b1e7 | bm-20240723-pythonperf1-amd64-faster%2dcpython-bound_method_instrum-3.14.0a0-5787d3e |
|----------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| 2to3           | 220 ms                                                                     | 227 ms: 1.03x slower                                                                 |
| docutils       | 1.67 sec                                                                   | 1.69 sec: 1.01x slower                                                               |
| html5lib       | 39.4 ms                                                                    | 41.4 ms: 1.05x slower                                                                |
| Geometric mean | (ref)                                                                      | 1.02x slower                                                                         |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240723-pythonperf1-amd64-python-2c1b1e7a07eba0138b98-3.14.0a0-2c1b1e7 | bm-20240723-pythonperf1-amd64-faster%2dcpython-bound_method_instrum-3.14.0a0-5787d3e |
|----------------------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed_tg | 383 ms                                                                     | 387 ms: 1.01x slower                                                                 |
| async_generators           | 241 ms                                                                     | 245 ms: 1.02x slower                                                                 |
| coroutines                 | 13.2 ms                                                                    | 13.5 ms: 1.02x slower                                                                |
| async_tree_io              | 530 ms                                                                     | 547 ms: 1.03x slower                                                                 |
| async_tree_none            | 207 ms                                                                     | 214 ms: 1.03x slower                                                                 |
| asyncio_tcp_ssl            | 1.63 sec                                                                   | 1.79 sec: 1.09x slower                                                               |
| Geometric mean             | (ref)                                                                      | 1.03x slower                                                                         |

Benchmark hidden because not significant (6): async_tree_cpu_io_mixed, asyncio_tcp, async_tree_memoization_tg, async_tree_io_tg, async_tree_memoization, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240723-pythonperf1-amd64-python-2c1b1e7a07eba0138b98-3.14.0a0-2c1b1e7 | bm-20240723-pythonperf1-amd64-faster%2dcpython-bound_method_instrum-3.14.0a0-5787d3e |
|----------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| pidigits       | 150 ms                                                                     | 151 ms: 1.00x slower                                                                 |
| float          | 54.3 ms                                                                    | 56.3 ms: 1.04x slower                                                                |
| nbody          | 75.2 ms                                                                    | 83.8 ms: 1.11x slower                                                                |
| Geometric mean | (ref)                                                                      | 1.05x slower                                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240723-pythonperf1-amd64-python-2c1b1e7a07eba0138b98-3.14.0a0-2c1b1e7 | bm-20240723-pythonperf1-amd64-faster%2dcpython-bound_method_instrum-3.14.0a0-5787d3e |
|----------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| regex_v8       | 15.8 ms                                                                    | 14.6 ms: 1.09x faster                                                                |
| regex_dna      | 119 ms                                                                     | 120 ms: 1.01x slower                                                                 |
| regex_compile  | 85.0 ms                                                                    | 90.4 ms: 1.06x slower                                                                |
| Geometric mean | (ref)                                                                      | 1.00x faster                                                                         |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240723-pythonperf1-amd64-python-2c1b1e7a07eba0138b98-3.14.0a0-2c1b1e7 | bm-20240723-pythonperf1-amd64-faster%2dcpython-bound_method_instrum-3.14.0a0-5787d3e |
|----------------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| json_loads           | 14.5 us                                                                    | 14.0 us: 1.04x faster                                                                |
| xml_etree_parse      | 93.2 ms                                                                    | 91.9 ms: 1.01x faster                                                                |
| xml_etree_iterparse  | 64.8 ms                                                                    | 66.3 ms: 1.02x slower                                                                |
| json_dumps           | 5.80 ms                                                                    | 6.00 ms: 1.03x slower                                                                |
| xml_etree_generate   | 56.0 ms                                                                    | 58.1 ms: 1.04x slower                                                                |
| xml_etree_process    | 38.5 ms                                                                    | 40.6 ms: 1.06x slower                                                                |
| tomli_loads          | 1.49 sec                                                                   | 1.57 sec: 1.06x slower                                                               |
| pickle_pure_python   | 193 us                                                                     | 209 us: 1.08x slower                                                                 |
| unpickle_pure_python | 136 us                                                                     | 150 us: 1.11x slower                                                                 |
| Geometric mean       | (ref)                                                                      | 1.04x slower                                                                         |

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup_no_site, python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240723-pythonperf1-amd64-python-2c1b1e7a07eba0138b98-3.14.0a0-2c1b1e7 | bm-20240723-pythonperf1-amd64-faster%2dcpython-bound_method_instrum-3.14.0a0-5787d3e |
|-----------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| django_template | 22.9 ms                                                                    | 23.7 ms: 1.04x slower                                                                |
| genshi_xml      | 33.8 ms                                                                    | 36.3 ms: 1.07x slower                                                                |
| genshi_text     | 15.5 ms                                                                    | 16.7 ms: 1.08x slower                                                                |
| mako            | 6.88 ms                                                                    | 7.48 ms: 1.09x slower                                                                |
| Geometric mean  | (ref)                                                                      | 1.07x slower                                                                         |

All benchmarks:
===============

| Benchmark                  | bm-20240723-pythonperf1-amd64-python-2c1b1e7a07eba0138b98-3.14.0a0-2c1b1e7 | bm-20240723-pythonperf1-amd64-faster%2dcpython-bound_method_instrum-3.14.0a0-5787d3e |
|----------------------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| pycparser                  | 852 ms                                                                     | 781 ms: 1.09x faster                                                                 |
| regex_v8                   | 15.8 ms                                                                    | 14.6 ms: 1.09x faster                                                                |
| mdp                        | 1.47 sec                                                                   | 1.40 sec: 1.05x faster                                                               |
| json_loads                 | 14.5 us                                                                    | 14.0 us: 1.04x faster                                                                |
| xml_etree_parse            | 93.2 ms                                                                    | 91.9 ms: 1.01x faster                                                                |
| json                       | 2.96 ms                                                                    | 2.93 ms: 1.01x faster                                                                |
| scimark_sparse_mat_mult    | 2.91 ms                                                                    | 2.90 ms: 1.00x faster                                                                |
| pidigits                   | 150 ms                                                                     | 151 ms: 1.00x slower                                                                 |
| regex_dna                  | 119 ms                                                                     | 120 ms: 1.01x slower                                                                 |
| meteor_contest             | 74.9 ms                                                                    | 75.6 ms: 1.01x slower                                                                |
| docutils                   | 1.67 sec                                                                   | 1.69 sec: 1.01x slower                                                               |
| telco                      | 4.81 ms                                                                    | 4.87 ms: 1.01x slower                                                                |
| async_tree_cpu_io_mixed_tg | 383 ms                                                                     | 387 ms: 1.01x slower                                                                 |
| sympy_sum                  | 88.0 ms                                                                    | 89.3 ms: 1.02x slower                                                                |
| async_generators           | 241 ms                                                                     | 245 ms: 1.02x slower                                                                 |
| bench_thread_pool          | 793 us                                                                     | 806 us: 1.02x slower                                                                 |
| coverage                   | 46.5 ms                                                                    | 47.4 ms: 1.02x slower                                                                |
| sympy_expand               | 292 ms                                                                     | 298 ms: 1.02x slower                                                                 |
| generators                 | 20.7 ms                                                                    | 21.2 ms: 1.02x slower                                                                |
| sympy_integrate            | 12.7 ms                                                                    | 13.0 ms: 1.02x slower                                                                |
| sympy_str                  | 170 ms                                                                     | 174 ms: 1.02x slower                                                                 |
| xml_etree_iterparse        | 64.8 ms                                                                    | 66.3 ms: 1.02x slower                                                                |
| coroutines                 | 13.2 ms                                                                    | 13.5 ms: 1.02x slower                                                                |
| sqlglot_optimize           | 33.6 ms                                                                    | 34.6 ms: 1.03x slower                                                                |
| thrift                     | 514 us                                                                     | 530 us: 1.03x slower                                                                 |
| sqlglot_normalize          | 178 ms                                                                     | 184 ms: 1.03x slower                                                                 |
| 2to3                       | 220 ms                                                                     | 227 ms: 1.03x slower                                                                 |
| async_tree_io              | 530 ms                                                                     | 547 ms: 1.03x slower                                                                 |
| scimark_monte_carlo        | 48.6 ms                                                                    | 50.1 ms: 1.03x slower                                                                |
| async_tree_none            | 207 ms                                                                     | 214 ms: 1.03x slower                                                                 |
| json_dumps                 | 5.80 ms                                                                    | 6.00 ms: 1.03x slower                                                                |
| fannkuch                   | 290 ms                                                                     | 300 ms: 1.03x slower                                                                 |
| typing_runtime_protocols   | 104 us                                                                     | 108 us: 1.04x slower                                                                 |
| float                      | 54.3 ms                                                                    | 56.3 ms: 1.04x slower                                                                |
| xml_etree_generate         | 56.0 ms                                                                    | 58.1 ms: 1.04x slower                                                                |
| django_template            | 22.9 ms                                                                    | 23.7 ms: 1.04x slower                                                                |
| nqueens                    | 60.8 ms                                                                    | 63.2 ms: 1.04x slower                                                                |
| deepcopy                   | 177 us                                                                     | 184 us: 1.04x slower                                                                 |
| deepcopy_reduce            | 1.80 us                                                                    | 1.89 us: 1.05x slower                                                                |
| sqlglot_transpile          | 1.04 ms                                                                    | 1.10 ms: 1.05x slower                                                                |
| crypto_pyaes               | 47.7 ms                                                                    | 50.2 ms: 1.05x slower                                                                |
| html5lib                   | 39.4 ms                                                                    | 41.4 ms: 1.05x slower                                                                |
| logging_simple             | 5.88 us                                                                    | 6.20 us: 1.05x slower                                                                |
| pyflate                    | 299 ms                                                                     | 316 ms: 1.05x slower                                                                 |
| logging_format             | 6.33 us                                                                    | 6.68 us: 1.06x slower                                                                |
| xml_etree_process          | 38.5 ms                                                                    | 40.6 ms: 1.06x slower                                                                |
| tomli_loads                | 1.49 sec                                                                   | 1.57 sec: 1.06x slower                                                               |
| comprehensions             | 11.0 us                                                                    | 11.6 us: 1.06x slower                                                                |
| scimark_fft                | 207 ms                                                                     | 219 ms: 1.06x slower                                                                 |
| raytrace                   | 169 ms                                                                     | 179 ms: 1.06x slower                                                                 |
| sqlglot_parse              | 843 us                                                                     | 893 us: 1.06x slower                                                                 |
| regex_compile              | 85.0 ms                                                                    | 90.4 ms: 1.06x slower                                                                |
| pprint_safe_repr           | 528 ms                                                                     | 563 ms: 1.07x slower                                                                 |
| chaos                      | 41.4 ms                                                                    | 44.5 ms: 1.07x slower                                                                |
| genshi_xml                 | 33.8 ms                                                                    | 36.3 ms: 1.07x slower                                                                |
| genshi_text                | 15.5 ms                                                                    | 16.7 ms: 1.08x slower                                                                |
| pickle_pure_python         | 193 us                                                                     | 209 us: 1.08x slower                                                                 |
| pprint_pformat             | 1.06 sec                                                                   | 1.15 sec: 1.08x slower                                                               |
| go                         | 88.1 ms                                                                    | 95.5 ms: 1.08x slower                                                                |
| spectral_norm              | 67.8 ms                                                                    | 73.5 ms: 1.08x slower                                                                |
| mako                       | 6.88 ms                                                                    | 7.48 ms: 1.09x slower                                                                |
| asyncio_tcp_ssl            | 1.63 sec                                                                   | 1.79 sec: 1.09x slower                                                               |
| scimark_sor                | 83.0 ms                                                                    | 90.9 ms: 1.10x slower                                                                |
| logging_silent             | 57.1 ns                                                                    | 62.6 ns: 1.10x slower                                                                |
| unpickle_pure_python       | 136 us                                                                     | 150 us: 1.11x slower                                                                 |
| scimark_lu                 | 59.4 ms                                                                    | 65.9 ms: 1.11x slower                                                                |
| deltablue                  | 1.99 ms                                                                    | 2.21 ms: 1.11x slower                                                                |
| richards_super             | 31.6 ms                                                                    | 35.1 ms: 1.11x slower                                                                |
| nbody                      | 75.2 ms                                                                    | 83.8 ms: 1.11x slower                                                                |
| hexiom                     | 3.98 ms                                                                    | 4.46 ms: 1.12x slower                                                                |
| richards                   | 27.8 ms                                                                    | 31.4 ms: 1.13x slower                                                                |
| deepcopy_memo              | 18.9 us                                                                    | 21.7 us: 1.15x slower                                                                |
| Geometric mean             | (ref)                                                                      | 1.04x slower                                                                         |

Benchmark hidden because not significant (15): python_startup_no_site, python_startup, bench_mp_pool, gc_traversal, pathlib, async_tree_cpu_io_mixed, regex_effbot, create_gc_cycles, tornado_http, asyncio_tcp, pylint, async_tree_memoization_tg, async_tree_io_tg, async_tree_memoization, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.02x
- 95% likely to have a slowdown of 1.02x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: unknown
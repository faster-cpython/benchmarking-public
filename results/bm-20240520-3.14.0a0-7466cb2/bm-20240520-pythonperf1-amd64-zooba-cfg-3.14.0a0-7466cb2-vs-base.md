# Results vs. base

- fork: zooba
- ref: cfg
- machine: windows-amd64
- commit hash: 7466cb2
- commit date: 2024-05-20
- overall geometric mean: 1.07x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240518-pythonperf1-amd64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 | bm-20240520-pythonperf1-amd64-zooba-cfg-3.14.0a0-7466cb2 |
|----------------|:--------------------------------------------------------------------------:|:--------------------------------------------------------:|
| 2to3           | 207 ms                                                                     | 215 ms: 1.04x slower                                     |
| chameleon      | 4.79 ms                                                                    | 5.03 ms: 1.05x slower                                    |
| docutils       | 1.60 sec                                                                   | 1.74 sec: 1.08x slower                                   |
| html5lib       | 35.6 ms                                                                    | 39.1 ms: 1.10x slower                                    |
| tornado_http   | 82.3 ms                                                                    | 86.1 ms: 1.05x slower                                    |
| Geometric mean | (ref)                                                                      | 1.06x slower                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240518-pythonperf1-amd64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 | bm-20240520-pythonperf1-amd64-zooba-cfg-3.14.0a0-7466cb2 |
|----------------------------|:--------------------------------------------------------------------------:|:--------------------------------------------------------:|
| async_tree_cpu_io_mixed_tg | 384 ms                                                                     | 405 ms: 1.06x slower                                     |
| async_tree_io              | 578 ms                                                                     | 618 ms: 1.07x slower                                     |
| async_tree_io_tg           | 598 ms                                                                     | 640 ms: 1.07x slower                                     |
| async_tree_none_tg         | 205 ms                                                                     | 220 ms: 1.07x slower                                     |
| async_tree_memoization     | 260 ms                                                                     | 282 ms: 1.08x slower                                     |
| async_tree_none            | 215 ms                                                                     | 234 ms: 1.09x slower                                     |
| async_tree_cpu_io_mixed    | 384 ms                                                                     | 420 ms: 1.09x slower                                     |
| async_tree_memoization_tg  | 252 ms                                                                     | 279 ms: 1.11x slower                                     |
| Geometric mean             | (ref)                                                                      | 1.08x slower                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240518-pythonperf1-amd64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 | bm-20240520-pythonperf1-amd64-zooba-cfg-3.14.0a0-7466cb2 |
|----------------|:--------------------------------------------------------------------------:|:--------------------------------------------------------:|
| pidigits       | 150 ms                                                                     | 151 ms: 1.00x slower                                     |
| nbody          | 69.4 ms                                                                    | 72.4 ms: 1.04x slower                                    |
| float          | 51.2 ms                                                                    | 55.6 ms: 1.08x slower                                    |
| Geometric mean | (ref)                                                                      | 1.04x slower                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240518-pythonperf1-amd64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 | bm-20240520-pythonperf1-amd64-zooba-cfg-3.14.0a0-7466cb2 |
|----------------|:--------------------------------------------------------------------------:|:--------------------------------------------------------:|
| regex_dna      | 119 ms                                                                     | 119 ms: 1.01x slower                                     |
| regex_v8       | 14.8 ms                                                                    | 15.0 ms: 1.02x slower                                    |
| regex_effbot   | 1.58 ms                                                                    | 1.66 ms: 1.05x slower                                    |
| regex_compile  | 77.9 ms                                                                    | 85.5 ms: 1.10x slower                                    |
| Geometric mean | (ref)                                                                      | 1.04x slower                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240518-pythonperf1-amd64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 | bm-20240520-pythonperf1-amd64-zooba-cfg-3.14.0a0-7466cb2 |
|----------------------|:--------------------------------------------------------------------------:|:--------------------------------------------------------:|
| pickle_dict          | 18.2 us                                                                    | 18.7 us: 1.03x slower                                    |
| unpickle_list        | 2.81 us                                                                    | 2.90 us: 1.03x slower                                    |
| unpickle             | 8.56 us                                                                    | 9.08 us: 1.06x slower                                    |
| json_loads           | 13.9 us                                                                    | 14.8 us: 1.06x slower                                    |
| tomli_loads          | 1.36 sec                                                                   | 1.46 sec: 1.08x slower                                   |
| xml_etree_process    | 36.4 ms                                                                    | 39.7 ms: 1.09x slower                                    |
| json_dumps           | 5.57 ms                                                                    | 6.08 ms: 1.09x slower                                    |
| pickle_pure_python   | 176 us                                                                     | 192 us: 1.09x slower                                     |
| unpickle_pure_python | 126 us                                                                     | 137 us: 1.09x slower                                     |
| xml_etree_generate   | 52.9 ms                                                                    | 58.2 ms: 1.10x slower                                    |
| xml_etree_iterparse  | 62.8 ms                                                                    | 70.9 ms: 1.13x slower                                    |
| xml_etree_parse      | 90.5 ms                                                                    | 104 ms: 1.15x slower                                     |
| Geometric mean       | (ref)                                                                      | 1.07x slower                                             |

Benchmark hidden because not significant (2): pickle_list, pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240518-pythonperf1-amd64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 | bm-20240520-pythonperf1-amd64-zooba-cfg-3.14.0a0-7466cb2 |
|------------------------|:--------------------------------------------------------------------------:|:--------------------------------------------------------:|
| python_startup_no_site | 16.4 ms                                                                    | 17.8 ms: 1.09x slower                                    |
| python_startup         | 20.0 ms                                                                    | 21.7 ms: 1.09x slower                                    |
| Geometric mean         | (ref)                                                                      | 1.09x slower                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240518-pythonperf1-amd64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 | bm-20240520-pythonperf1-amd64-zooba-cfg-3.14.0a0-7466cb2 |
|-----------------|:--------------------------------------------------------------------------:|:--------------------------------------------------------:|
| genshi_text     | 14.8 ms                                                                    | 15.3 ms: 1.03x slower                                    |
| genshi_xml      | 31.5 ms                                                                    | 32.8 ms: 1.04x slower                                    |
| django_template | 21.8 ms                                                                    | 23.0 ms: 1.05x slower                                    |
| mako            | 6.53 ms                                                                    | 6.96 ms: 1.07x slower                                    |
| Geometric mean  | (ref)                                                                      | 1.05x slower                                             |

All benchmarks:
===============

| Benchmark                  | bm-20240518-pythonperf1-amd64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 | bm-20240520-pythonperf1-amd64-zooba-cfg-3.14.0a0-7466cb2 |
|----------------------------|:--------------------------------------------------------------------------:|:--------------------------------------------------------:|
| pidigits                   | 150 ms                                                                     | 151 ms: 1.00x slower                                     |
| regex_dna                  | 119 ms                                                                     | 119 ms: 1.01x slower                                     |
| pathlib                    | 79.2 ms                                                                    | 79.8 ms: 1.01x slower                                    |
| meteor_contest             | 73.4 ms                                                                    | 74.3 ms: 1.01x slower                                    |
| regex_v8                   | 14.8 ms                                                                    | 15.0 ms: 1.02x slower                                    |
| go                         | 84.3 ms                                                                    | 85.9 ms: 1.02x slower                                    |
| chaos                      | 38.7 ms                                                                    | 39.5 ms: 1.02x slower                                    |
| pickle_dict                | 18.2 us                                                                    | 18.7 us: 1.03x slower                                    |
| coroutines                 | 12.8 ms                                                                    | 13.2 ms: 1.03x slower                                    |
| unpickle_list              | 2.81 us                                                                    | 2.90 us: 1.03x slower                                    |
| fannkuch                   | 256 ms                                                                     | 265 ms: 1.03x slower                                     |
| raytrace                   | 161 ms                                                                     | 166 ms: 1.03x slower                                     |
| genshi_text                | 14.8 ms                                                                    | 15.3 ms: 1.03x slower                                    |
| 2to3                       | 207 ms                                                                     | 215 ms: 1.04x slower                                     |
| nqueens                    | 57.1 ms                                                                    | 59.4 ms: 1.04x slower                                    |
| genshi_xml                 | 31.5 ms                                                                    | 32.8 ms: 1.04x slower                                    |
| nbody                      | 69.4 ms                                                                    | 72.4 ms: 1.04x slower                                    |
| sqlite_synth               | 1.62 us                                                                    | 1.69 us: 1.05x slower                                    |
| tornado_http               | 82.3 ms                                                                    | 86.1 ms: 1.05x slower                                    |
| regex_effbot               | 1.58 ms                                                                    | 1.66 ms: 1.05x slower                                    |
| sqlglot_parse              | 754 us                                                                     | 792 us: 1.05x slower                                     |
| bench_thread_pool          | 804 us                                                                     | 844 us: 1.05x slower                                     |
| chameleon                  | 4.79 ms                                                                    | 5.03 ms: 1.05x slower                                    |
| sqlglot_transpile          | 963 us                                                                     | 1.01 ms: 1.05x slower                                    |
| django_template            | 21.8 ms                                                                    | 23.0 ms: 1.05x slower                                    |
| async_tree_cpu_io_mixed_tg | 384 ms                                                                     | 405 ms: 1.06x slower                                     |
| coverage                   | 44.5 ms                                                                    | 46.9 ms: 1.06x slower                                    |
| pyflate                    | 286 ms                                                                     | 302 ms: 1.06x slower                                     |
| richards                   | 26.6 ms                                                                    | 28.1 ms: 1.06x slower                                    |
| richards_super             | 29.8 ms                                                                    | 31.5 ms: 1.06x slower                                    |
| logging_format             | 6.08 us                                                                    | 6.44 us: 1.06x slower                                    |
| logging_simple             | 5.67 us                                                                    | 6.01 us: 1.06x slower                                    |
| comprehensions             | 10.4 us                                                                    | 11.1 us: 1.06x slower                                    |
| unpickle                   | 8.56 us                                                                    | 9.08 us: 1.06x slower                                    |
| json_loads                 | 13.9 us                                                                    | 14.8 us: 1.06x slower                                    |
| scimark_monte_carlo        | 41.1 ms                                                                    | 43.8 ms: 1.06x slower                                    |
| mako                       | 6.53 ms                                                                    | 6.96 ms: 1.07x slower                                    |
| thrift                     | 489 us                                                                     | 521 us: 1.07x slower                                     |
| pprint_pformat             | 989 ms                                                                     | 1.05 sec: 1.07x slower                                   |
| json                       | 3.01 ms                                                                    | 3.21 ms: 1.07x slower                                    |
| deepcopy_reduce            | 1.97 us                                                                    | 2.10 us: 1.07x slower                                    |
| pprint_safe_repr           | 485 ms                                                                     | 518 ms: 1.07x slower                                     |
| deltablue                  | 1.94 ms                                                                    | 2.07 ms: 1.07x slower                                    |
| sqlglot_normalize          | 173 ms                                                                     | 184 ms: 1.07x slower                                     |
| async_tree_io              | 578 ms                                                                     | 618 ms: 1.07x slower                                     |
| async_tree_io_tg           | 598 ms                                                                     | 640 ms: 1.07x slower                                     |
| sqlglot_optimize           | 32.8 ms                                                                    | 35.0 ms: 1.07x slower                                    |
| hexiom                     | 3.77 ms                                                                    | 4.04 ms: 1.07x slower                                    |
| bench_mp_pool              | 66.0 ms                                                                    | 70.6 ms: 1.07x slower                                    |
| deepcopy                   | 219 us                                                                     | 235 us: 1.07x slower                                     |
| sympy_integrate            | 12.3 ms                                                                    | 13.2 ms: 1.07x slower                                    |
| async_tree_none_tg         | 205 ms                                                                     | 220 ms: 1.07x slower                                     |
| spectral_norm              | 65.1 ms                                                                    | 70.0 ms: 1.07x slower                                    |
| tomli_loads                | 1.36 sec                                                                   | 1.46 sec: 1.08x slower                                   |
| crypto_pyaes               | 46.5 ms                                                                    | 50.1 ms: 1.08x slower                                    |
| telco                      | 4.68 ms                                                                    | 5.05 ms: 1.08x slower                                    |
| async_tree_memoization     | 260 ms                                                                     | 282 ms: 1.08x slower                                     |
| docutils                   | 1.60 sec                                                                   | 1.74 sec: 1.08x slower                                   |
| logging_silent             | 53.6 ns                                                                    | 58.1 ns: 1.08x slower                                    |
| float                      | 51.2 ms                                                                    | 55.6 ms: 1.08x slower                                    |
| scimark_sor                | 77.3 ms                                                                    | 83.8 ms: 1.08x slower                                    |
| deepcopy_memo              | 23.0 us                                                                    | 24.9 us: 1.09x slower                                    |
| python_startup_no_site     | 16.4 ms                                                                    | 17.8 ms: 1.09x slower                                    |
| python_startup             | 20.0 ms                                                                    | 21.7 ms: 1.09x slower                                    |
| xml_etree_process          | 36.4 ms                                                                    | 39.7 ms: 1.09x slower                                    |
| json_dumps                 | 5.57 ms                                                                    | 6.08 ms: 1.09x slower                                    |
| pickle_pure_python         | 176 us                                                                     | 192 us: 1.09x slower                                     |
| async_tree_none            | 215 ms                                                                     | 234 ms: 1.09x slower                                     |
| unpickle_pure_python       | 126 us                                                                     | 137 us: 1.09x slower                                     |
| async_tree_cpu_io_mixed    | 384 ms                                                                     | 420 ms: 1.09x slower                                     |
| typing_runtime_protocols   | 99.7 us                                                                    | 109 us: 1.09x slower                                     |
| regex_compile              | 77.9 ms                                                                    | 85.5 ms: 1.10x slower                                    |
| sympy_sum                  | 83.9 ms                                                                    | 92.3 ms: 1.10x slower                                    |
| html5lib                   | 35.6 ms                                                                    | 39.1 ms: 1.10x slower                                    |
| xml_etree_generate         | 52.9 ms                                                                    | 58.2 ms: 1.10x slower                                    |
| async_generators           | 228 ms                                                                     | 253 ms: 1.11x slower                                     |
| async_tree_memoization_tg  | 252 ms                                                                     | 279 ms: 1.11x slower                                     |
| sympy_str                  | 162 ms                                                                     | 179 ms: 1.11x slower                                     |
| xml_etree_iterparse        | 62.8 ms                                                                    | 70.9 ms: 1.13x slower                                    |
| sympy_expand               | 270 ms                                                                     | 307 ms: 1.14x slower                                     |
| scimark_lu                 | 55.8 ms                                                                    | 63.9 ms: 1.14x slower                                    |
| xml_etree_parse            | 90.5 ms                                                                    | 104 ms: 1.15x slower                                     |
| scimark_fft                | 181 ms                                                                     | 212 ms: 1.17x slower                                     |
| mdp                        | 1.35 sec                                                                   | 1.61 sec: 1.19x slower                                   |
| create_gc_cycles           | 888 us                                                                     | 1.08 ms: 1.21x slower                                    |
| scimark_sparse_mat_mult    | 2.54 ms                                                                    | 3.14 ms: 1.24x slower                                    |
| gc_traversal               | 1.55 ms                                                                    | 2.80 ms: 1.81x slower                                    |
| Geometric mean             | (ref)                                                                      | 1.07x slower                                             |

Benchmark hidden because not significant (8): pycparser, pickle_list, pickle, flaskblogging, generators, asyncio_tcp, asyncio_tcp_ssl, pylint

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.06x
- 95% likely to have a slowdown of 1.06x
- 99% likely to have a slowdown of 1.05x

# Memory
- memory change: unknown
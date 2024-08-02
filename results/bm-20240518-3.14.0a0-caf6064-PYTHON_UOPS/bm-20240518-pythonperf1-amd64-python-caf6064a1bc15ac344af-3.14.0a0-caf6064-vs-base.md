# Results vs. base

- fork: python
- ref: caf6064a1bc15ac344af
- machine: windows-amd64
- commit hash: caf6064
- commit date: 2024-05-18
- overall geometric mean: 1.09x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20240518-3.14.0a0-caf6064/bm-20240518-pythonperf1-amd64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064.json | results/bm-20240518-3.14.0a0-caf6064-PYTHON_UOPS/bm-20240518-pythonperf1-amd64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064.json |
|----------------|:--------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 207 ms                                                                                                               | 229 ms: 1.11x slower                                                                                                             |
| chameleon      | 4.79 ms                                                                                                              | 5.12 ms: 1.07x slower                                                                                                            |
| docutils       | 1.60 sec                                                                                                             | 1.83 sec: 1.14x slower                                                                                                           |
| html5lib       | 35.6 ms                                                                                                              | 41.5 ms: 1.17x slower                                                                                                            |
| tornado_http   | 82.3 ms                                                                                                              | 87.0 ms: 1.06x slower                                                                                                            |
| Geometric mean | (ref)                                                                                                                | 1.11x slower                                                                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | results/bm-20240518-3.14.0a0-caf6064/bm-20240518-pythonperf1-amd64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064.json | results/bm-20240518-3.14.0a0-caf6064-PYTHON_UOPS/bm-20240518-pythonperf1-amd64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064.json |
|---------------------------|:--------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed   | 384 ms                                                                                                               | 400 ms: 1.04x slower                                                                                                             |
| async_tree_io_tg          | 598 ms                                                                                                               | 628 ms: 1.05x slower                                                                                                             |
| async_tree_none_tg        | 205 ms                                                                                                               | 217 ms: 1.06x slower                                                                                                             |
| async_tree_io             | 578 ms                                                                                                               | 612 ms: 1.06x slower                                                                                                             |
| async_tree_memoization    | 260 ms                                                                                                               | 278 ms: 1.07x slower                                                                                                             |
| async_tree_none           | 215 ms                                                                                                               | 231 ms: 1.08x slower                                                                                                             |
| async_tree_memoization_tg | 252 ms                                                                                                               | 272 ms: 1.08x slower                                                                                                             |
| Geometric mean            | (ref)                                                                                                                | 1.06x slower                                                                                                                     |

Benchmark hidden because not significant (1): async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20240518-3.14.0a0-caf6064/bm-20240518-pythonperf1-amd64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064.json | results/bm-20240518-3.14.0a0-caf6064-PYTHON_UOPS/bm-20240518-pythonperf1-amd64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064.json |
|----------------|:--------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------------:|
| pidigits       | 150 ms                                                                                                               | 151 ms: 1.00x slower                                                                                                             |
| float          | 51.2 ms                                                                                                              | 53.6 ms: 1.05x slower                                                                                                            |
| nbody          | 69.4 ms                                                                                                              | 75.0 ms: 1.08x slower                                                                                                            |
| Geometric mean | (ref)                                                                                                                | 1.04x slower                                                                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20240518-3.14.0a0-caf6064/bm-20240518-pythonperf1-amd64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064.json | results/bm-20240518-3.14.0a0-caf6064-PYTHON_UOPS/bm-20240518-pythonperf1-amd64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064.json |
|----------------|:--------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------------:|
| regex_dna      | 119 ms                                                                                                               | 119 ms: 1.01x slower                                                                                                             |
| regex_v8       | 14.8 ms                                                                                                              | 15.9 ms: 1.08x slower                                                                                                            |
| regex_compile  | 77.9 ms                                                                                                              | 106 ms: 1.36x slower                                                                                                             |
| Geometric mean | (ref)                                                                                                                | 1.10x slower                                                                                                                     |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20240518-3.14.0a0-caf6064/bm-20240518-pythonperf1-amd64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064.json | results/bm-20240518-3.14.0a0-caf6064-PYTHON_UOPS/bm-20240518-pythonperf1-amd64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064.json |
|----------------------|:--------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------------:|
| pickle_list          | 3.23 us                                                                                                              | 2.93 us: 1.10x faster                                                                                                            |
| pickle               | 7.25 us                                                                                                              | 7.11 us: 1.02x faster                                                                                                            |
| pickle_dict          | 18.2 us                                                                                                              | 18.4 us: 1.01x slower                                                                                                            |
| xml_etree_iterparse  | 62.8 ms                                                                                                              | 65.2 ms: 1.04x slower                                                                                                            |
| json_dumps           | 5.57 ms                                                                                                              | 5.81 ms: 1.04x slower                                                                                                            |
| xml_etree_generate   | 52.9 ms                                                                                                              | 56.6 ms: 1.07x slower                                                                                                            |
| tomli_loads          | 1.36 sec                                                                                                             | 1.47 sec: 1.08x slower                                                                                                           |
| xml_etree_process    | 36.4 ms                                                                                                              | 39.5 ms: 1.08x slower                                                                                                            |
| unpickle_pure_python | 126 us                                                                                                               | 155 us: 1.23x slower                                                                                                             |
| pickle_pure_python   | 176 us                                                                                                               | 217 us: 1.23x slower                                                                                                             |
| Geometric mean       | (ref)                                                                                                                | 1.04x slower                                                                                                                     |

Benchmark hidden because not significant (4): xml_etree_parse, json_loads, unpickle_list, unpickle

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup, python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20240518-3.14.0a0-caf6064/bm-20240518-pythonperf1-amd64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064.json | results/bm-20240518-3.14.0a0-caf6064-PYTHON_UOPS/bm-20240518-pythonperf1-amd64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064.json |
|-----------------|:--------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------------:|
| mako            | 6.53 ms                                                                                                              | 7.35 ms: 1.13x slower                                                                                                            |
| django_template | 21.8 ms                                                                                                              | 25.1 ms: 1.15x slower                                                                                                            |
| genshi_text     | 14.8 ms                                                                                                              | 17.4 ms: 1.17x slower                                                                                                            |
| genshi_xml      | 31.5 ms                                                                                                              | 37.6 ms: 1.20x slower                                                                                                            |
| Geometric mean  | (ref)                                                                                                                | 1.16x slower                                                                                                                     |

All benchmarks:
===============

| Benchmark                 | results/bm-20240518-3.14.0a0-caf6064/bm-20240518-pythonperf1-amd64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064.json | results/bm-20240518-3.14.0a0-caf6064-PYTHON_UOPS/bm-20240518-pythonperf1-amd64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064.json |
|---------------------------|:--------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------------:|
| pickle_list               | 3.23 us                                                                                                              | 2.93 us: 1.10x faster                                                                                                            |
| pickle                    | 7.25 us                                                                                                              | 7.11 us: 1.02x faster                                                                                                            |
| generators                | 20.1 ms                                                                                                              | 19.9 ms: 1.01x faster                                                                                                            |
| pidigits                  | 150 ms                                                                                                               | 151 ms: 1.00x slower                                                                                                             |
| regex_dna                 | 119 ms                                                                                                               | 119 ms: 1.01x slower                                                                                                             |
| coverage                  | 44.5 ms                                                                                                              | 44.8 ms: 1.01x slower                                                                                                            |
| gc_traversal              | 1.55 ms                                                                                                              | 1.56 ms: 1.01x slower                                                                                                            |
| pickle_dict               | 18.2 us                                                                                                              | 18.4 us: 1.01x slower                                                                                                            |
| bench_mp_pool             | 66.0 ms                                                                                                              | 67.6 ms: 1.02x slower                                                                                                            |
| create_gc_cycles          | 888 us                                                                                                               | 912 us: 1.03x slower                                                                                                             |
| xml_etree_iterparse       | 62.8 ms                                                                                                              | 65.2 ms: 1.04x slower                                                                                                            |
| mdp                       | 1.35 sec                                                                                                             | 1.40 sec: 1.04x slower                                                                                                           |
| fannkuch                  | 256 ms                                                                                                               | 267 ms: 1.04x slower                                                                                                             |
| async_tree_cpu_io_mixed   | 384 ms                                                                                                               | 400 ms: 1.04x slower                                                                                                             |
| json_dumps                | 5.57 ms                                                                                                              | 5.81 ms: 1.04x slower                                                                                                            |
| bench_thread_pool         | 804 us                                                                                                               | 839 us: 1.04x slower                                                                                                             |
| meteor_contest            | 73.4 ms                                                                                                              | 76.7 ms: 1.04x slower                                                                                                            |
| float                     | 51.2 ms                                                                                                              | 53.6 ms: 1.05x slower                                                                                                            |
| thrift                    | 489 us                                                                                                               | 511 us: 1.05x slower                                                                                                             |
| async_tree_io_tg          | 598 ms                                                                                                               | 628 ms: 1.05x slower                                                                                                             |
| telco                     | 4.68 ms                                                                                                              | 4.91 ms: 1.05x slower                                                                                                            |
| tornado_http              | 82.3 ms                                                                                                              | 87.0 ms: 1.06x slower                                                                                                            |
| crypto_pyaes              | 46.5 ms                                                                                                              | 49.2 ms: 1.06x slower                                                                                                            |
| async_tree_none_tg        | 205 ms                                                                                                               | 217 ms: 1.06x slower                                                                                                             |
| async_tree_io             | 578 ms                                                                                                               | 612 ms: 1.06x slower                                                                                                             |
| richards                  | 26.6 ms                                                                                                              | 28.2 ms: 1.06x slower                                                                                                            |
| chameleon                 | 4.79 ms                                                                                                              | 5.12 ms: 1.07x slower                                                                                                            |
| async_tree_memoization    | 260 ms                                                                                                               | 278 ms: 1.07x slower                                                                                                             |
| xml_etree_generate        | 52.9 ms                                                                                                              | 56.6 ms: 1.07x slower                                                                                                            |
| async_generators          | 228 ms                                                                                                               | 245 ms: 1.07x slower                                                                                                             |
| richards_super            | 29.8 ms                                                                                                              | 32.0 ms: 1.07x slower                                                                                                            |
| pycparser                 | 723 ms                                                                                                               | 777 ms: 1.07x slower                                                                                                             |
| regex_v8                  | 14.8 ms                                                                                                              | 15.9 ms: 1.08x slower                                                                                                            |
| async_tree_none           | 215 ms                                                                                                               | 231 ms: 1.08x slower                                                                                                             |
| scimark_fft               | 181 ms                                                                                                               | 195 ms: 1.08x slower                                                                                                             |
| async_tree_memoization_tg | 252 ms                                                                                                               | 272 ms: 1.08x slower                                                                                                             |
| nbody                     | 69.4 ms                                                                                                              | 75.0 ms: 1.08x slower                                                                                                            |
| tomli_loads               | 1.36 sec                                                                                                             | 1.47 sec: 1.08x slower                                                                                                           |
| xml_etree_process         | 36.4 ms                                                                                                              | 39.5 ms: 1.08x slower                                                                                                            |
| pprint_safe_repr          | 485 ms                                                                                                               | 530 ms: 1.09x slower                                                                                                             |
| deepcopy_reduce           | 1.97 us                                                                                                              | 2.15 us: 1.09x slower                                                                                                            |
| logging_format            | 6.08 us                                                                                                              | 6.67 us: 1.10x slower                                                                                                            |
| pprint_pformat            | 989 ms                                                                                                               | 1.09 sec: 1.10x slower                                                                                                           |
| logging_simple            | 5.67 us                                                                                                              | 6.23 us: 1.10x slower                                                                                                            |
| 2to3                      | 207 ms                                                                                                               | 229 ms: 1.11x slower                                                                                                             |
| chaos                     | 38.7 ms                                                                                                              | 43.2 ms: 1.12x slower                                                                                                            |
| scimark_sor               | 77.3 ms                                                                                                              | 86.3 ms: 1.12x slower                                                                                                            |
| raytrace                  | 161 ms                                                                                                               | 180 ms: 1.12x slower                                                                                                             |
| mako                      | 6.53 ms                                                                                                              | 7.35 ms: 1.13x slower                                                                                                            |
| pylint                    | 206 ms                                                                                                               | 232 ms: 1.13x slower                                                                                                             |
| pyflate                   | 286 ms                                                                                                               | 324 ms: 1.13x slower                                                                                                             |
| deepcopy                  | 219 us                                                                                                               | 249 us: 1.14x slower                                                                                                             |
| docutils                  | 1.60 sec                                                                                                             | 1.83 sec: 1.14x slower                                                                                                           |
| spectral_norm             | 65.1 ms                                                                                                              | 74.5 ms: 1.14x slower                                                                                                            |
| django_template           | 21.8 ms                                                                                                              | 25.1 ms: 1.15x slower                                                                                                            |
| scimark_monte_carlo       | 41.1 ms                                                                                                              | 47.6 ms: 1.16x slower                                                                                                            |
| typing_runtime_protocols  | 99.7 us                                                                                                              | 116 us: 1.16x slower                                                                                                             |
| sqlglot_transpile         | 963 us                                                                                                               | 1.12 ms: 1.16x slower                                                                                                            |
| nqueens                   | 57.1 ms                                                                                                              | 66.4 ms: 1.16x slower                                                                                                            |
| html5lib                  | 35.6 ms                                                                                                              | 41.5 ms: 1.17x slower                                                                                                            |
| sqlglot_parse             | 754 us                                                                                                               | 881 us: 1.17x slower                                                                                                             |
| genshi_text               | 14.8 ms                                                                                                              | 17.4 ms: 1.17x slower                                                                                                            |
| sqlglot_optimize          | 32.8 ms                                                                                                              | 38.6 ms: 1.18x slower                                                                                                            |
| sympy_integrate           | 12.3 ms                                                                                                              | 14.5 ms: 1.18x slower                                                                                                            |
| sympy_sum                 | 83.9 ms                                                                                                              | 99.3 ms: 1.18x slower                                                                                                            |
| scimark_sparse_mat_mult   | 2.54 ms                                                                                                              | 3.01 ms: 1.19x slower                                                                                                            |
| go                        | 84.3 ms                                                                                                              | 100 ms: 1.19x slower                                                                                                             |
| genshi_xml                | 31.5 ms                                                                                                              | 37.6 ms: 1.20x slower                                                                                                            |
| sympy_str                 | 162 ms                                                                                                               | 195 ms: 1.20x slower                                                                                                             |
| deepcopy_memo             | 23.0 us                                                                                                              | 28.0 us: 1.22x slower                                                                                                            |
| unpickle_pure_python      | 126 us                                                                                                               | 155 us: 1.23x slower                                                                                                             |
| pickle_pure_python        | 176 us                                                                                                               | 217 us: 1.23x slower                                                                                                             |
| sympy_expand              | 270 ms                                                                                                               | 337 ms: 1.25x slower                                                                                                             |
| comprehensions            | 10.4 us                                                                                                              | 13.1 us: 1.26x slower                                                                                                            |
| logging_silent            | 53.6 ns                                                                                                              | 68.2 ns: 1.27x slower                                                                                                            |
| deltablue                 | 1.94 ms                                                                                                              | 2.59 ms: 1.34x slower                                                                                                            |
| regex_compile             | 77.9 ms                                                                                                              | 106 ms: 1.36x slower                                                                                                             |
| scimark_lu                | 55.8 ms                                                                                                              | 77.2 ms: 1.38x slower                                                                                                            |
| hexiom                    | 3.77 ms                                                                                                              | 5.23 ms: 1.39x slower                                                                                                            |
| Geometric mean            | (ref)                                                                                                                | 1.09x slower                                                                                                                     |

Benchmark hidden because not significant (15): json, asyncio_tcp, coroutines, xml_etree_parse, json_loads, unpickle_list, python_startup, python_startup_no_site, flaskblogging, regex_effbot, pathlib, unpickle, asyncio_tcp_ssl, sqlite_synth, async_tree_cpu_io_mixed_tg
Ignored benchmarks (1) of results/bm-20240518-3.14.0a0-caf6064/bm-20240518-pythonperf1-amd64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064.json: sqlglot_normalize

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.06x
- 95% likely to have a slowdown of 1.06x
- 99% likely to have a slowdown of 1.05x

# Memory
- memory change: unknown
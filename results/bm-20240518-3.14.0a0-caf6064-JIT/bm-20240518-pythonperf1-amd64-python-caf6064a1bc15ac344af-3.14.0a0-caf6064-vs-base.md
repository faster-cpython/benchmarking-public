# Results vs. base

- fork: python
- ref: caf6064a1bc15ac344af
- machine: windows-amd64
- commit hash: caf6064
- commit date: 2024-05-18
- overall geometric mean: 1.02x slower
- HPT reliability: 99.94%
- HPT 99th percentile: 1.01x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20240518-3.14.0a0-caf6064/bm-20240518-pythonperf1-amd64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064.json | results/bm-20240518-3.14.0a0-caf6064-JIT/bm-20240518-pythonperf1-amd64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064.json |
|----------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 207 ms                                                                                                               | 232 ms: 1.12x slower                                                                                                     |
| chameleon      | 4.79 ms                                                                                                              | 5.11 ms: 1.07x slower                                                                                                    |
| docutils       | 1.60 sec                                                                                                             | 1.76 sec: 1.10x slower                                                                                                   |
| html5lib       | 35.6 ms                                                                                                              | 37.2 ms: 1.05x slower                                                                                                    |
| tornado_http   | 82.3 ms                                                                                                              | 84.9 ms: 1.03x slower                                                                                                    |
| Geometric mean | (ref)                                                                                                                | 1.07x slower                                                                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | results/bm-20240518-3.14.0a0-caf6064/bm-20240518-pythonperf1-amd64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064.json | results/bm-20240518-3.14.0a0-caf6064-JIT/bm-20240518-pythonperf1-amd64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064.json |
|---------------------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| async_tree_io_tg          | 598 ms                                                                                                               | 612 ms: 1.02x slower                                                                                                     |
| async_tree_cpu_io_mixed   | 384 ms                                                                                                               | 394 ms: 1.03x slower                                                                                                     |
| async_tree_none_tg        | 205 ms                                                                                                               | 211 ms: 1.03x slower                                                                                                     |
| async_tree_io             | 578 ms                                                                                                               | 598 ms: 1.03x slower                                                                                                     |
| async_tree_memoization    | 260 ms                                                                                                               | 272 ms: 1.04x slower                                                                                                     |
| async_tree_none           | 215 ms                                                                                                               | 226 ms: 1.05x slower                                                                                                     |
| async_tree_memoization_tg | 252 ms                                                                                                               | 269 ms: 1.07x slower                                                                                                     |
| Geometric mean            | (ref)                                                                                                                | 1.04x slower                                                                                                             |

Benchmark hidden because not significant (1): async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20240518-3.14.0a0-caf6064/bm-20240518-pythonperf1-amd64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064.json | results/bm-20240518-3.14.0a0-caf6064-JIT/bm-20240518-pythonperf1-amd64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064.json |
|----------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| nbody          | 69.4 ms                                                                                                              | 50.5 ms: 1.37x faster                                                                                                    |
| float          | 51.2 ms                                                                                                              | 44.2 ms: 1.16x faster                                                                                                    |
| pidigits       | 150 ms                                                                                                               | 149 ms: 1.01x faster                                                                                                     |
| Geometric mean | (ref)                                                                                                                | 1.17x faster                                                                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20240518-3.14.0a0-caf6064/bm-20240518-pythonperf1-amd64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064.json | results/bm-20240518-3.14.0a0-caf6064-JIT/bm-20240518-pythonperf1-amd64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064.json |
|----------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| regex_v8       | 14.8 ms                                                                                                              | 14.3 ms: 1.03x faster                                                                                                    |
| regex_effbot   | 1.58 ms                                                                                                              | 1.57 ms: 1.01x faster                                                                                                    |
| regex_dna      | 119 ms                                                                                                               | 119 ms: 1.01x slower                                                                                                     |
| regex_compile  | 77.9 ms                                                                                                              | 87.2 ms: 1.12x slower                                                                                                    |
| Geometric mean | (ref)                                                                                                                | 1.02x slower                                                                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20240518-3.14.0a0-caf6064/bm-20240518-pythonperf1-amd64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064.json | results/bm-20240518-3.14.0a0-caf6064-JIT/bm-20240518-pythonperf1-amd64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064.json |
|----------------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| pickle_list          | 3.23 us                                                                                                              | 2.90 us: 1.11x faster                                                                                                    |
| tomli_loads          | 1.36 sec                                                                                                             | 1.23 sec: 1.11x faster                                                                                                   |
| xml_etree_iterparse  | 62.8 ms                                                                                                              | 60.1 ms: 1.04x faster                                                                                                    |
| pickle_dict          | 18.2 us                                                                                                              | 17.5 us: 1.04x faster                                                                                                    |
| xml_etree_generate   | 52.9 ms                                                                                                              | 51.8 ms: 1.02x faster                                                                                                    |
| pickle_pure_python   | 176 us                                                                                                               | 173 us: 1.02x faster                                                                                                     |
| unpickle_pure_python | 126 us                                                                                                               | 125 us: 1.00x faster                                                                                                     |
| xml_etree_parse      | 90.5 ms                                                                                                              | 91.5 ms: 1.01x slower                                                                                                    |
| json_loads           | 13.9 us                                                                                                              | 14.1 us: 1.01x slower                                                                                                    |
| unpickle             | 8.56 us                                                                                                              | 8.69 us: 1.02x slower                                                                                                    |
| pickle               | 7.25 us                                                                                                              | 7.37 us: 1.02x slower                                                                                                    |
| unpickle_list        | 2.81 us                                                                                                              | 2.87 us: 1.02x slower                                                                                                    |
| json_dumps           | 5.57 ms                                                                                                              | 5.75 ms: 1.03x slower                                                                                                    |
| Geometric mean       | (ref)                                                                                                                | 1.02x faster                                                                                                             |

Benchmark hidden because not significant (1): xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | results/bm-20240518-3.14.0a0-caf6064/bm-20240518-pythonperf1-amd64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064.json | results/bm-20240518-3.14.0a0-caf6064-JIT/bm-20240518-pythonperf1-amd64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064.json |
|------------------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| python_startup         | 20.0 ms                                                                                                              | 21.8 ms: 1.09x slower                                                                                                    |
| python_startup_no_site | 16.4 ms                                                                                                              | 18.1 ms: 1.10x slower                                                                                                    |
| Geometric mean         | (ref)                                                                                                                | 1.10x slower                                                                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20240518-3.14.0a0-caf6064/bm-20240518-pythonperf1-amd64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064.json | results/bm-20240518-3.14.0a0-caf6064-JIT/bm-20240518-pythonperf1-amd64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064.json |
|-----------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| mako            | 6.53 ms                                                                                                              | 5.17 ms: 1.26x faster                                                                                                    |
| django_template | 21.8 ms                                                                                                              | 25.6 ms: 1.17x slower                                                                                                    |
| genshi_text     | 14.8 ms                                                                                                              | 17.8 ms: 1.21x slower                                                                                                    |
| genshi_xml      | 31.5 ms                                                                                                              | 44.7 ms: 1.42x slower                                                                                                    |
| Geometric mean  | (ref)                                                                                                                | 1.12x slower                                                                                                             |

All benchmarks:
===============

| Benchmark                 | results/bm-20240518-3.14.0a0-caf6064/bm-20240518-pythonperf1-amd64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064.json | results/bm-20240518-3.14.0a0-caf6064-JIT/bm-20240518-pythonperf1-amd64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064.json |
|---------------------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| spectral_norm             | 65.1 ms                                                                                                              | 45.1 ms: 1.45x faster                                                                                                    |
| nbody                     | 69.4 ms                                                                                                              | 50.5 ms: 1.37x faster                                                                                                    |
| mako                      | 6.53 ms                                                                                                              | 5.17 ms: 1.26x faster                                                                                                    |
| scimark_fft               | 181 ms                                                                                                               | 151 ms: 1.20x faster                                                                                                     |
| scimark_sparse_mat_mult   | 2.54 ms                                                                                                              | 2.17 ms: 1.17x faster                                                                                                    |
| float                     | 51.2 ms                                                                                                              | 44.2 ms: 1.16x faster                                                                                                    |
| fannkuch                  | 256 ms                                                                                                               | 222 ms: 1.16x faster                                                                                                     |
| crypto_pyaes              | 46.5 ms                                                                                                              | 41.0 ms: 1.13x faster                                                                                                    |
| deepcopy_memo             | 23.0 us                                                                                                              | 20.6 us: 1.12x faster                                                                                                    |
| pickle_list               | 3.23 us                                                                                                              | 2.90 us: 1.11x faster                                                                                                    |
| pyflate                   | 286 ms                                                                                                               | 257 ms: 1.11x faster                                                                                                     |
| tomli_loads               | 1.36 sec                                                                                                             | 1.23 sec: 1.11x faster                                                                                                   |
| scimark_monte_carlo       | 41.1 ms                                                                                                              | 38.5 ms: 1.07x faster                                                                                                    |
| pprint_safe_repr          | 485 ms                                                                                                               | 459 ms: 1.06x faster                                                                                                     |
| pprint_pformat            | 989 ms                                                                                                               | 945 ms: 1.05x faster                                                                                                     |
| xml_etree_iterparse       | 62.8 ms                                                                                                              | 60.1 ms: 1.04x faster                                                                                                    |
| telco                     | 4.68 ms                                                                                                              | 4.48 ms: 1.04x faster                                                                                                    |
| sqlite_synth              | 1.62 us                                                                                                              | 1.56 us: 1.04x faster                                                                                                    |
| pickle_dict               | 18.2 us                                                                                                              | 17.5 us: 1.04x faster                                                                                                    |
| json                      | 3.01 ms                                                                                                              | 2.92 ms: 1.03x faster                                                                                                    |
| regex_v8                  | 14.8 ms                                                                                                              | 14.3 ms: 1.03x faster                                                                                                    |
| xml_etree_generate        | 52.9 ms                                                                                                              | 51.8 ms: 1.02x faster                                                                                                    |
| pickle_pure_python        | 176 us                                                                                                               | 173 us: 1.02x faster                                                                                                     |
| comprehensions            | 10.4 us                                                                                                              | 10.3 us: 1.01x faster                                                                                                    |
| pidigits                  | 150 ms                                                                                                               | 149 ms: 1.01x faster                                                                                                     |
| regex_effbot              | 1.58 ms                                                                                                              | 1.57 ms: 1.01x faster                                                                                                    |
| unpickle_pure_python      | 126 us                                                                                                               | 125 us: 1.00x faster                                                                                                     |
| regex_dna                 | 119 ms                                                                                                               | 119 ms: 1.01x slower                                                                                                     |
| xml_etree_parse           | 90.5 ms                                                                                                              | 91.5 ms: 1.01x slower                                                                                                    |
| chaos                     | 38.7 ms                                                                                                              | 39.2 ms: 1.01x slower                                                                                                    |
| json_loads                | 13.9 us                                                                                                              | 14.1 us: 1.01x slower                                                                                                    |
| logging_simple            | 5.67 us                                                                                                              | 5.75 us: 1.01x slower                                                                                                    |
| unpickle                  | 8.56 us                                                                                                              | 8.69 us: 1.02x slower                                                                                                    |
| meteor_contest            | 73.4 ms                                                                                                              | 74.5 ms: 1.02x slower                                                                                                    |
| pickle                    | 7.25 us                                                                                                              | 7.37 us: 1.02x slower                                                                                                    |
| unpickle_list             | 2.81 us                                                                                                              | 2.87 us: 1.02x slower                                                                                                    |
| create_gc_cycles          | 888 us                                                                                                               | 907 us: 1.02x slower                                                                                                     |
| logging_format            | 6.08 us                                                                                                              | 6.21 us: 1.02x slower                                                                                                    |
| async_tree_io_tg          | 598 ms                                                                                                               | 612 ms: 1.02x slower                                                                                                     |
| async_tree_cpu_io_mixed   | 384 ms                                                                                                               | 394 ms: 1.03x slower                                                                                                     |
| coroutines                | 12.8 ms                                                                                                              | 13.2 ms: 1.03x slower                                                                                                    |
| coverage                  | 44.5 ms                                                                                                              | 45.8 ms: 1.03x slower                                                                                                    |
| async_tree_none_tg        | 205 ms                                                                                                               | 211 ms: 1.03x slower                                                                                                     |
| json_dumps                | 5.57 ms                                                                                                              | 5.75 ms: 1.03x slower                                                                                                    |
| tornado_http              | 82.3 ms                                                                                                              | 84.9 ms: 1.03x slower                                                                                                    |
| async_tree_io             | 578 ms                                                                                                               | 598 ms: 1.03x slower                                                                                                     |
| async_tree_memoization    | 260 ms                                                                                                               | 272 ms: 1.04x slower                                                                                                     |
| logging_silent            | 53.6 ns                                                                                                              | 56.0 ns: 1.04x slower                                                                                                    |
| html5lib                  | 35.6 ms                                                                                                              | 37.2 ms: 1.05x slower                                                                                                    |
| bench_thread_pool         | 804 us                                                                                                               | 842 us: 1.05x slower                                                                                                     |
| async_tree_none           | 215 ms                                                                                                               | 226 ms: 1.05x slower                                                                                                     |
| deepcopy_reduce           | 1.97 us                                                                                                              | 2.07 us: 1.05x slower                                                                                                    |
| thrift                    | 489 us                                                                                                               | 516 us: 1.06x slower                                                                                                     |
| sqlglot_parse             | 754 us                                                                                                               | 799 us: 1.06x slower                                                                                                     |
| chameleon                 | 4.79 ms                                                                                                              | 5.11 ms: 1.07x slower                                                                                                    |
| async_tree_memoization_tg | 252 ms                                                                                                               | 269 ms: 1.07x slower                                                                                                     |
| nqueens                   | 57.1 ms                                                                                                              | 61.0 ms: 1.07x slower                                                                                                    |
| scimark_sor               | 77.3 ms                                                                                                              | 82.8 ms: 1.07x slower                                                                                                    |
| sqlglot_transpile         | 963 us                                                                                                               | 1.03 ms: 1.07x slower                                                                                                    |
| generators                | 20.1 ms                                                                                                              | 21.6 ms: 1.07x slower                                                                                                    |
| bench_mp_pool             | 66.0 ms                                                                                                              | 71.3 ms: 1.08x slower                                                                                                    |
| deepcopy                  | 219 us                                                                                                               | 238 us: 1.09x slower                                                                                                     |
| python_startup            | 20.0 ms                                                                                                              | 21.8 ms: 1.09x slower                                                                                                    |
| raytrace                  | 161 ms                                                                                                               | 176 ms: 1.09x slower                                                                                                     |
| sympy_str                 | 162 ms                                                                                                               | 177 ms: 1.10x slower                                                                                                     |
| docutils                  | 1.60 sec                                                                                                             | 1.76 sec: 1.10x slower                                                                                                   |
| mdp                       | 1.35 sec                                                                                                             | 1.48 sec: 1.10x slower                                                                                                   |
| sympy_sum                 | 83.9 ms                                                                                                              | 92.5 ms: 1.10x slower                                                                                                    |
| python_startup_no_site    | 16.4 ms                                                                                                              | 18.1 ms: 1.10x slower                                                                                                    |
| richards                  | 26.6 ms                                                                                                              | 29.5 ms: 1.11x slower                                                                                                    |
| typing_runtime_protocols  | 99.7 us                                                                                                              | 111 us: 1.11x slower                                                                                                     |
| go                        | 84.3 ms                                                                                                              | 93.8 ms: 1.11x slower                                                                                                    |
| richards_super            | 29.8 ms                                                                                                              | 33.3 ms: 1.12x slower                                                                                                    |
| regex_compile             | 77.9 ms                                                                                                              | 87.2 ms: 1.12x slower                                                                                                    |
| sqlglot_optimize          | 32.8 ms                                                                                                              | 36.7 ms: 1.12x slower                                                                                                    |
| 2to3                      | 207 ms                                                                                                               | 232 ms: 1.12x slower                                                                                                     |
| async_generators          | 228 ms                                                                                                               | 257 ms: 1.13x slower                                                                                                     |
| sympy_integrate           | 12.3 ms                                                                                                              | 14.0 ms: 1.14x slower                                                                                                    |
| sympy_expand              | 270 ms                                                                                                               | 309 ms: 1.14x slower                                                                                                     |
| pylint                    | 206 ms                                                                                                               | 236 ms: 1.15x slower                                                                                                     |
| django_template           | 21.8 ms                                                                                                              | 25.6 ms: 1.17x slower                                                                                                    |
| genshi_text               | 14.8 ms                                                                                                              | 17.8 ms: 1.21x slower                                                                                                    |
| deltablue                 | 1.94 ms                                                                                                              | 2.33 ms: 1.21x slower                                                                                                    |
| hexiom                    | 3.77 ms                                                                                                              | 4.65 ms: 1.23x slower                                                                                                    |
| scimark_lu                | 55.8 ms                                                                                                              | 69.9 ms: 1.25x slower                                                                                                    |
| genshi_xml                | 31.5 ms                                                                                                              | 44.7 ms: 1.42x slower                                                                                                    |
| Geometric mean            | (ref)                                                                                                                | 1.02x slower                                                                                                             |

Benchmark hidden because not significant (8): asyncio_tcp_ssl, pathlib, xml_etree_process, flaskblogging, gc_traversal, async_tree_cpu_io_mixed_tg, asyncio_tcp, pycparser
Ignored benchmarks (1) of results/bm-20240518-3.14.0a0-caf6064/bm-20240518-pythonperf1-amd64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064.json: sqlglot_normalize

# HPT report

- Reliability score: 99.94% likely to be slow
- 90% likely to have a slowdown of 1.02x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: unknown
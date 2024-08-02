# Results vs. base

- fork: python
- ref: e418fc3a6e7bade68ab5
- machine: windows-amd64
- commit hash: e418fc3
- commit date: 2024-05-25
- overall geometric mean: 1.02x slower
- HPT reliability: 99.30%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20240525-3.14.0a0-e418fc3/bm-20240525-pythonperf1-amd64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3.json | results/bm-20240525-3.14.0a0-e418fc3-JIT/bm-20240525-pythonperf1-amd64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3.json |
|----------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 210 ms                                                                                                               | 244 ms: 1.16x slower                                                                                                     |
| chameleon      | 4.81 ms                                                                                                              | 5.14 ms: 1.07x slower                                                                                                    |
| docutils       | 1.62 sec                                                                                                             | 1.77 sec: 1.09x slower                                                                                                   |
| html5lib       | 35.2 ms                                                                                                              | 37.5 ms: 1.07x slower                                                                                                    |
| tornado_http   | 81.6 ms                                                                                                              | 85.3 ms: 1.04x slower                                                                                                    |
| Geometric mean | (ref)                                                                                                                | 1.09x slower                                                                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | results/bm-20240525-3.14.0a0-e418fc3/bm-20240525-pythonperf1-amd64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3.json | results/bm-20240525-3.14.0a0-e418fc3-JIT/bm-20240525-pythonperf1-amd64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3.json |
|---------------------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed   | 393 ms                                                                                                               | 401 ms: 1.02x slower                                                                                                     |
| async_tree_io_tg          | 607 ms                                                                                                               | 622 ms: 1.02x slower                                                                                                     |
| async_tree_none_tg        | 204 ms                                                                                                               | 211 ms: 1.04x slower                                                                                                     |
| async_tree_memoization_tg | 259 ms                                                                                                               | 270 ms: 1.04x slower                                                                                                     |
| async_tree_memoization    | 269 ms                                                                                                               | 281 ms: 1.04x slower                                                                                                     |
| Geometric mean            | (ref)                                                                                                                | 1.03x slower                                                                                                             |

Benchmark hidden because not significant (3): async_tree_io, async_tree_none, async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20240525-3.14.0a0-e418fc3/bm-20240525-pythonperf1-amd64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3.json | results/bm-20240525-3.14.0a0-e418fc3-JIT/bm-20240525-pythonperf1-amd64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3.json |
|----------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| nbody          | 68.7 ms                                                                                                              | 51.2 ms: 1.34x faster                                                                                                    |
| float          | 50.5 ms                                                                                                              | 43.4 ms: 1.16x faster                                                                                                    |
| pidigits       | 150 ms                                                                                                               | 150 ms: 1.00x faster                                                                                                     |
| Geometric mean | (ref)                                                                                                                | 1.16x faster                                                                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20240525-3.14.0a0-e418fc3/bm-20240525-pythonperf1-amd64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3.json | results/bm-20240525-3.14.0a0-e418fc3-JIT/bm-20240525-pythonperf1-amd64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3.json |
|----------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| regex_compile  | 76.7 ms                                                                                                              | 87.5 ms: 1.14x slower                                                                                                    |
| Geometric mean | (ref)                                                                                                                | 1.04x slower                                                                                                             |

Benchmark hidden because not significant (3): regex_dna, regex_effbot, regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20240525-3.14.0a0-e418fc3/bm-20240525-pythonperf1-amd64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3.json | results/bm-20240525-3.14.0a0-e418fc3-JIT/bm-20240525-pythonperf1-amd64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3.json |
|----------------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| pickle_list          | 3.26 us                                                                                                              | 2.87 us: 1.14x faster                                                                                                    |
| tomli_loads          | 1.36 sec                                                                                                             | 1.23 sec: 1.11x faster                                                                                                   |
| xml_etree_generate   | 53.7 ms                                                                                                              | 50.9 ms: 1.05x faster                                                                                                    |
| pickle_dict          | 18.3 us                                                                                                              | 17.5 us: 1.04x faster                                                                                                    |
| pickle_pure_python   | 177 us                                                                                                               | 170 us: 1.04x faster                                                                                                     |
| xml_etree_iterparse  | 63.3 ms                                                                                                              | 61.1 ms: 1.04x faster                                                                                                    |
| pickle               | 7.23 us                                                                                                              | 7.08 us: 1.02x faster                                                                                                    |
| xml_etree_process    | 36.6 ms                                                                                                              | 36.0 ms: 1.02x faster                                                                                                    |
| unpickle_pure_python | 126 us                                                                                                               | 125 us: 1.01x faster                                                                                                     |
| xml_etree_parse      | 91.8 ms                                                                                                              | 92.3 ms: 1.01x slower                                                                                                    |
| unpickle_list        | 2.85 us                                                                                                              | 2.92 us: 1.02x slower                                                                                                    |
| unpickle             | 8.73 us                                                                                                              | 8.96 us: 1.03x slower                                                                                                    |
| json_loads           | 13.7 us                                                                                                              | 14.1 us: 1.04x slower                                                                                                    |
| Geometric mean       | (ref)                                                                                                                | 1.03x faster                                                                                                             |

Benchmark hidden because not significant (1): json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | results/bm-20240525-3.14.0a0-e418fc3/bm-20240525-pythonperf1-amd64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3.json | results/bm-20240525-3.14.0a0-e418fc3-JIT/bm-20240525-pythonperf1-amd64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3.json |
|------------------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| python_startup         | 21.0 ms                                                                                                              | 22.8 ms: 1.08x slower                                                                                                    |
| python_startup_no_site | 16.6 ms                                                                                                              | 18.8 ms: 1.14x slower                                                                                                    |
| Geometric mean         | (ref)                                                                                                                | 1.11x slower                                                                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20240525-3.14.0a0-e418fc3/bm-20240525-pythonperf1-amd64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3.json | results/bm-20240525-3.14.0a0-e418fc3-JIT/bm-20240525-pythonperf1-amd64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3.json |
|-----------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| mako            | 6.41 ms                                                                                                              | 4.90 ms: 1.31x faster                                                                                                    |
| django_template | 21.9 ms                                                                                                              | 25.6 ms: 1.17x slower                                                                                                    |
| genshi_text     | 14.6 ms                                                                                                              | 18.2 ms: 1.24x slower                                                                                                    |
| genshi_xml      | 31.5 ms                                                                                                              | 44.8 ms: 1.42x slower                                                                                                    |
| Geometric mean  | (ref)                                                                                                                | 1.12x slower                                                                                                             |

All benchmarks:
===============

| Benchmark                 | results/bm-20240525-3.14.0a0-e418fc3/bm-20240525-pythonperf1-amd64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3.json | results/bm-20240525-3.14.0a0-e418fc3-JIT/bm-20240525-pythonperf1-amd64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3.json |
|---------------------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| spectral_norm             | 64.7 ms                                                                                                              | 46.1 ms: 1.40x faster                                                                                                    |
| nbody                     | 68.7 ms                                                                                                              | 51.2 ms: 1.34x faster                                                                                                    |
| mako                      | 6.41 ms                                                                                                              | 4.90 ms: 1.31x faster                                                                                                    |
| scimark_fft               | 181 ms                                                                                                               | 149 ms: 1.21x faster                                                                                                     |
| scimark_sparse_mat_mult   | 2.51 ms                                                                                                              | 2.14 ms: 1.17x faster                                                                                                    |
| float                     | 50.5 ms                                                                                                              | 43.4 ms: 1.16x faster                                                                                                    |
| pickle_list               | 3.26 us                                                                                                              | 2.87 us: 1.14x faster                                                                                                    |
| fannkuch                  | 249 ms                                                                                                               | 221 ms: 1.12x faster                                                                                                     |
| tomli_loads               | 1.36 sec                                                                                                             | 1.23 sec: 1.11x faster                                                                                                   |
| pyflate                   | 284 ms                                                                                                               | 256 ms: 1.11x faster                                                                                                     |
| crypto_pyaes              | 45.9 ms                                                                                                              | 41.4 ms: 1.11x faster                                                                                                    |
| deepcopy_memo             | 22.5 us                                                                                                              | 20.7 us: 1.09x faster                                                                                                    |
| scimark_monte_carlo       | 41.2 ms                                                                                                              | 38.3 ms: 1.08x faster                                                                                                    |
| pprint_safe_repr          | 492 ms                                                                                                               | 461 ms: 1.07x faster                                                                                                     |
| pprint_pformat            | 997 ms                                                                                                               | 935 ms: 1.07x faster                                                                                                     |
| asyncio_tcp_ssl           | 1.45 sec                                                                                                             | 1.37 sec: 1.06x faster                                                                                                   |
| xml_etree_generate        | 53.7 ms                                                                                                              | 50.9 ms: 1.05x faster                                                                                                    |
| pickle_dict               | 18.3 us                                                                                                              | 17.5 us: 1.04x faster                                                                                                    |
| pickle_pure_python        | 177 us                                                                                                               | 170 us: 1.04x faster                                                                                                     |
| xml_etree_iterparse       | 63.3 ms                                                                                                              | 61.1 ms: 1.04x faster                                                                                                    |
| coverage                  | 46.3 ms                                                                                                              | 45.3 ms: 1.02x faster                                                                                                    |
| pickle                    | 7.23 us                                                                                                              | 7.08 us: 1.02x faster                                                                                                    |
| comprehensions            | 10.5 us                                                                                                              | 10.3 us: 1.02x faster                                                                                                    |
| xml_etree_process         | 36.6 ms                                                                                                              | 36.0 ms: 1.02x faster                                                                                                    |
| logging_format            | 6.26 us                                                                                                              | 6.15 us: 1.02x faster                                                                                                    |
| telco                     | 4.70 ms                                                                                                              | 4.62 ms: 1.02x faster                                                                                                    |
| sqlite_synth              | 1.59 us                                                                                                              | 1.57 us: 1.01x faster                                                                                                    |
| logging_simple            | 5.80 us                                                                                                              | 5.76 us: 1.01x faster                                                                                                    |
| gc_traversal              | 1.57 ms                                                                                                              | 1.56 ms: 1.01x faster                                                                                                    |
| unpickle_pure_python      | 126 us                                                                                                               | 125 us: 1.01x faster                                                                                                     |
| pidigits                  | 150 ms                                                                                                               | 150 ms: 1.00x faster                                                                                                     |
| xml_etree_parse           | 91.8 ms                                                                                                              | 92.3 ms: 1.01x slower                                                                                                    |
| logging_silent            | 54.1 ns                                                                                                              | 54.5 ns: 1.01x slower                                                                                                    |
| json                      | 2.92 ms                                                                                                              | 2.94 ms: 1.01x slower                                                                                                    |
| async_tree_cpu_io_mixed   | 393 ms                                                                                                               | 401 ms: 1.02x slower                                                                                                     |
| coroutines                | 12.8 ms                                                                                                              | 13.1 ms: 1.02x slower                                                                                                    |
| unpickle_list             | 2.85 us                                                                                                              | 2.92 us: 1.02x slower                                                                                                    |
| meteor_contest            | 71.5 ms                                                                                                              | 73.2 ms: 1.02x slower                                                                                                    |
| thrift                    | 501 us                                                                                                               | 513 us: 1.02x slower                                                                                                     |
| async_tree_io_tg          | 607 ms                                                                                                               | 622 ms: 1.02x slower                                                                                                     |
| mdp                       | 1.41 sec                                                                                                             | 1.45 sec: 1.02x slower                                                                                                   |
| unpickle                  | 8.73 us                                                                                                              | 8.96 us: 1.03x slower                                                                                                    |
| bench_thread_pool         | 802 us                                                                                                               | 826 us: 1.03x slower                                                                                                     |
| json_loads                | 13.7 us                                                                                                              | 14.1 us: 1.04x slower                                                                                                    |
| asyncio_tcp               | 470 ms                                                                                                               | 487 ms: 1.04x slower                                                                                                     |
| scimark_sor               | 78.5 ms                                                                                                              | 81.5 ms: 1.04x slower                                                                                                    |
| async_tree_none_tg        | 204 ms                                                                                                               | 211 ms: 1.04x slower                                                                                                     |
| async_tree_memoization_tg | 259 ms                                                                                                               | 270 ms: 1.04x slower                                                                                                     |
| async_tree_memoization    | 269 ms                                                                                                               | 281 ms: 1.04x slower                                                                                                     |
| tornado_http              | 81.6 ms                                                                                                              | 85.3 ms: 1.04x slower                                                                                                    |
| chaos                     | 38.3 ms                                                                                                              | 40.3 ms: 1.05x slower                                                                                                    |
| pycparser                 | 684 ms                                                                                                               | 721 ms: 1.05x slower                                                                                                     |
| sqlglot_parse             | 762 us                                                                                                               | 805 us: 1.06x slower                                                                                                     |
| richards_super            | 30.6 ms                                                                                                              | 32.3 ms: 1.06x slower                                                                                                    |
| richards                  | 27.0 ms                                                                                                              | 28.7 ms: 1.06x slower                                                                                                    |
| html5lib                  | 35.2 ms                                                                                                              | 37.5 ms: 1.07x slower                                                                                                    |
| chameleon                 | 4.81 ms                                                                                                              | 5.14 ms: 1.07x slower                                                                                                    |
| sqlglot_transpile         | 966 us                                                                                                               | 1.04 ms: 1.08x slower                                                                                                    |
| deepcopy_reduce           | 2.00 us                                                                                                              | 2.15 us: 1.08x slower                                                                                                    |
| generators                | 19.7 ms                                                                                                              | 21.2 ms: 1.08x slower                                                                                                    |
| nqueens                   | 57.4 ms                                                                                                              | 62.0 ms: 1.08x slower                                                                                                    |
| python_startup            | 21.0 ms                                                                                                              | 22.8 ms: 1.08x slower                                                                                                    |
| deepcopy                  | 220 us                                                                                                               | 240 us: 1.09x slower                                                                                                     |
| docutils                  | 1.62 sec                                                                                                             | 1.77 sec: 1.09x slower                                                                                                   |
| sympy_sum                 | 83.6 ms                                                                                                              | 92.4 ms: 1.10x slower                                                                                                    |
| sympy_str                 | 160 ms                                                                                                               | 177 ms: 1.11x slower                                                                                                     |
| sqlglot_optimize          | 33.3 ms                                                                                                              | 36.8 ms: 1.11x slower                                                                                                    |
| raytrace                  | 157 ms                                                                                                               | 175 ms: 1.11x slower                                                                                                     |
| bench_mp_pool             | 66.2 ms                                                                                                              | 73.8 ms: 1.11x slower                                                                                                    |
| go                        | 83.5 ms                                                                                                              | 93.7 ms: 1.12x slower                                                                                                    |
| sympy_integrate           | 12.3 ms                                                                                                              | 13.9 ms: 1.13x slower                                                                                                    |
| async_generators          | 223 ms                                                                                                               | 253 ms: 1.13x slower                                                                                                     |
| pylint                    | 208 ms                                                                                                               | 236 ms: 1.13x slower                                                                                                     |
| sympy_expand              | 272 ms                                                                                                               | 309 ms: 1.14x slower                                                                                                     |
| python_startup_no_site    | 16.6 ms                                                                                                              | 18.8 ms: 1.14x slower                                                                                                    |
| regex_compile             | 76.7 ms                                                                                                              | 87.5 ms: 1.14x slower                                                                                                    |
| typing_runtime_protocols  | 99.8 us                                                                                                              | 115 us: 1.16x slower                                                                                                     |
| 2to3                      | 210 ms                                                                                                               | 244 ms: 1.16x slower                                                                                                     |
| scimark_lu                | 58.1 ms                                                                                                              | 67.7 ms: 1.16x slower                                                                                                    |
| django_template           | 21.9 ms                                                                                                              | 25.6 ms: 1.17x slower                                                                                                    |
| hexiom                    | 3.81 ms                                                                                                              | 4.67 ms: 1.23x slower                                                                                                    |
| deltablue                 | 1.90 ms                                                                                                              | 2.35 ms: 1.24x slower                                                                                                    |
| genshi_text               | 14.6 ms                                                                                                              | 18.2 ms: 1.24x slower                                                                                                    |
| genshi_xml                | 31.5 ms                                                                                                              | 44.8 ms: 1.42x slower                                                                                                    |
| Geometric mean            | (ref)                                                                                                                | 1.02x slower                                                                                                             |

Benchmark hidden because not significant (10): create_gc_cycles, json_dumps, flaskblogging, regex_dna, regex_effbot, pathlib, async_tree_io, async_tree_none, async_tree_cpu_io_mixed_tg, regex_v8
Ignored benchmarks (1) of results/bm-20240525-3.14.0a0-e418fc3/bm-20240525-pythonperf1-amd64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3.json: sqlglot_normalize

# HPT report

- Reliability score: 99.30% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown
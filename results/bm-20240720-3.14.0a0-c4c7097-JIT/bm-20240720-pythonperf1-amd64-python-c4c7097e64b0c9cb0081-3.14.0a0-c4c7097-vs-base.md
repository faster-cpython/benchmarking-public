# Results vs. base

- fork: python
- ref: c4c7097e64b0c9cb0081
- machine: windows-amd64
- commit hash: c4c7097
- commit date: 2024-07-20
- overall geometric mean: 1.05x faster
- HPT reliability: 98.18%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20240720-3.14.0a0-c4c7097/bm-20240720-pythonperf1-amd64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097.json | results/bm-20240720-3.14.0a0-c4c7097-JIT/bm-20240720-pythonperf1-amd64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097.json |
|----------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 223 ms                                                                                                               | 235 ms: 1.06x slower                                                                                                     |
| docutils       | 1.68 sec                                                                                                             | 1.79 sec: 1.06x slower                                                                                                   |
| tornado_http   | 91.3 ms                                                                                                              | 93.8 ms: 1.03x slower                                                                                                    |
| Geometric mean | (ref)                                                                                                                | 1.04x slower                                                                                                             |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | results/bm-20240720-3.14.0a0-c4c7097/bm-20240720-pythonperf1-amd64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097.json | results/bm-20240720-3.14.0a0-c4c7097-JIT/bm-20240720-pythonperf1-amd64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097.json |
|----------------------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| asyncio_tcp_ssl            | 1.64 sec                                                                                                             | 1.42 sec: 1.16x faster                                                                                                   |
| async_tree_none            | 216 ms                                                                                                               | 199 ms: 1.09x faster                                                                                                     |
| async_tree_io              | 556 ms                                                                                                               | 521 ms: 1.07x faster                                                                                                     |
| async_tree_none_tg         | 196 ms                                                                                                               | 186 ms: 1.05x faster                                                                                                     |
| async_tree_memoization     | 261 ms                                                                                                               | 251 ms: 1.04x faster                                                                                                     |
| async_tree_io_tg           | 541 ms                                                                                                               | 528 ms: 1.03x faster                                                                                                     |
| async_tree_cpu_io_mixed    | 391 ms                                                                                                               | 382 ms: 1.02x faster                                                                                                     |
| coroutines                 | 13.6 ms                                                                                                              | 13.5 ms: 1.01x faster                                                                                                    |
| async_tree_cpu_io_mixed_tg | 386 ms                                                                                                               | 381 ms: 1.01x faster                                                                                                     |
| async_generators           | 240 ms                                                                                                               | 253 ms: 1.05x slower                                                                                                     |
| Geometric mean             | (ref)                                                                                                                | 1.04x faster                                                                                                             |

Benchmark hidden because not significant (2): asyncio_tcp, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20240720-3.14.0a0-c4c7097/bm-20240720-pythonperf1-amd64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097.json | results/bm-20240720-3.14.0a0-c4c7097-JIT/bm-20240720-pythonperf1-amd64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097.json |
|----------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| nbody          | 77.3 ms                                                                                                              | 50.1 ms: 1.54x faster                                                                                                    |
| float          | 55.4 ms                                                                                                              | 44.2 ms: 1.25x faster                                                                                                    |
| pidigits       | 150 ms                                                                                                               | 150 ms: 1.00x slower                                                                                                     |
| Geometric mean | (ref)                                                                                                                | 1.24x faster                                                                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20240720-3.14.0a0-c4c7097/bm-20240720-pythonperf1-amd64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097.json | results/bm-20240720-3.14.0a0-c4c7097-JIT/bm-20240720-pythonperf1-amd64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097.json |
|----------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| regex_v8       | 16.4 ms                                                                                                              | 14.8 ms: 1.10x faster                                                                                                    |
| regex_dna      | 126 ms                                                                                                               | 122 ms: 1.03x faster                                                                                                     |
| regex_effbot   | 1.62 ms                                                                                                              | 1.61 ms: 1.01x faster                                                                                                    |
| regex_compile  | 86.8 ms                                                                                                              | 87.6 ms: 1.01x slower                                                                                                    |
| Geometric mean | (ref)                                                                                                                | 1.03x faster                                                                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20240720-3.14.0a0-c4c7097/bm-20240720-pythonperf1-amd64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097.json | results/bm-20240720-3.14.0a0-c4c7097-JIT/bm-20240720-pythonperf1-amd64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097.json |
|----------------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| tomli_loads          | 1.51 sec                                                                                                             | 1.23 sec: 1.22x faster                                                                                                   |
| pickle_pure_python   | 199 us                                                                                                               | 176 us: 1.13x faster                                                                                                     |
| xml_etree_generate   | 56.5 ms                                                                                                              | 51.2 ms: 1.10x faster                                                                                                    |
| unpickle_pure_python | 141 us                                                                                                               | 128 us: 1.10x faster                                                                                                     |
| xml_etree_process    | 39.3 ms                                                                                                              | 36.3 ms: 1.08x faster                                                                                                    |
| xml_etree_iterparse  | 64.7 ms                                                                                                              | 62.2 ms: 1.04x faster                                                                                                    |
| json_dumps           | 5.92 ms                                                                                                              | 5.73 ms: 1.03x faster                                                                                                    |
| xml_etree_parse      | 92.8 ms                                                                                                              | 93.8 ms: 1.01x slower                                                                                                    |
| Geometric mean       | (ref)                                                                                                                | 1.08x faster                                                                                                             |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | results/bm-20240720-3.14.0a0-c4c7097/bm-20240720-pythonperf1-amd64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097.json | results/bm-20240720-3.14.0a0-c4c7097-JIT/bm-20240720-pythonperf1-amd64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097.json |
|------------------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| python_startup         | 21.4 ms                                                                                                              | 21.7 ms: 1.01x slower                                                                                                    |
| python_startup_no_site | 17.6 ms                                                                                                              | 18.2 ms: 1.04x slower                                                                                                    |
| Geometric mean         | (ref)                                                                                                                | 1.03x slower                                                                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20240720-3.14.0a0-c4c7097/bm-20240720-pythonperf1-amd64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097.json | results/bm-20240720-3.14.0a0-c4c7097-JIT/bm-20240720-pythonperf1-amd64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097.json |
|-----------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| mako            | 7.11 ms                                                                                                              | 5.26 ms: 1.35x faster                                                                                                    |
| django_template | 23.0 ms                                                                                                              | 25.3 ms: 1.10x slower                                                                                                    |
| genshi_text     | 16.0 ms                                                                                                              | 18.3 ms: 1.14x slower                                                                                                    |
| genshi_xml      | 36.6 ms                                                                                                              | 45.6 ms: 1.25x slower                                                                                                    |
| Geometric mean  | (ref)                                                                                                                | 1.04x slower                                                                                                             |

All benchmarks:
===============

| Benchmark                  | results/bm-20240720-3.14.0a0-c4c7097/bm-20240720-pythonperf1-amd64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097.json | results/bm-20240720-3.14.0a0-c4c7097-JIT/bm-20240720-pythonperf1-amd64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097.json |
|----------------------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| coverage                   | 79.8 ms                                                                                                              | 47.2 ms: 1.69x faster                                                                                                    |
| nbody                      | 77.3 ms                                                                                                              | 50.1 ms: 1.54x faster                                                                                                    |
| spectral_norm              | 69.5 ms                                                                                                              | 46.1 ms: 1.51x faster                                                                                                    |
| mako                       | 7.11 ms                                                                                                              | 5.26 ms: 1.35x faster                                                                                                    |
| scimark_fft                | 198 ms                                                                                                               | 147 ms: 1.34x faster                                                                                                     |
| scimark_sparse_mat_mult    | 2.72 ms                                                                                                              | 2.08 ms: 1.30x faster                                                                                                    |
| fannkuch                   | 280 ms                                                                                                               | 220 ms: 1.27x faster                                                                                                     |
| scimark_monte_carlo        | 47.9 ms                                                                                                              | 37.9 ms: 1.27x faster                                                                                                    |
| deepcopy_memo              | 19.6 us                                                                                                              | 15.6 us: 1.26x faster                                                                                                    |
| float                      | 55.4 ms                                                                                                              | 44.2 ms: 1.25x faster                                                                                                    |
| pyflate                    | 304 ms                                                                                                               | 245 ms: 1.24x faster                                                                                                     |
| crypto_pyaes               | 48.9 ms                                                                                                              | 39.8 ms: 1.23x faster                                                                                                    |
| tomli_loads                | 1.51 sec                                                                                                             | 1.23 sec: 1.22x faster                                                                                                   |
| asyncio_tcp_ssl            | 1.64 sec                                                                                                             | 1.42 sec: 1.16x faster                                                                                                   |
| pprint_safe_repr           | 524 ms                                                                                                               | 461 ms: 1.14x faster                                                                                                     |
| pickle_pure_python         | 199 us                                                                                                               | 176 us: 1.13x faster                                                                                                     |
| pprint_pformat             | 1.07 sec                                                                                                             | 944 ms: 1.13x faster                                                                                                     |
| regex_v8                   | 16.4 ms                                                                                                              | 14.8 ms: 1.10x faster                                                                                                    |
| xml_etree_generate         | 56.5 ms                                                                                                              | 51.2 ms: 1.10x faster                                                                                                    |
| unpickle_pure_python       | 141 us                                                                                                               | 128 us: 1.10x faster                                                                                                     |
| comprehensions             | 11.1 us                                                                                                              | 10.1 us: 1.09x faster                                                                                                    |
| async_tree_none            | 216 ms                                                                                                               | 199 ms: 1.09x faster                                                                                                     |
| xml_etree_process          | 39.3 ms                                                                                                              | 36.3 ms: 1.08x faster                                                                                                    |
| telco                      | 4.81 ms                                                                                                              | 4.45 ms: 1.08x faster                                                                                                    |
| async_tree_io              | 556 ms                                                                                                               | 521 ms: 1.07x faster                                                                                                     |
| logging_silent             | 57.9 ns                                                                                                              | 55.0 ns: 1.05x faster                                                                                                    |
| async_tree_none_tg         | 196 ms                                                                                                               | 186 ms: 1.05x faster                                                                                                     |
| logging_simple             | 5.99 us                                                                                                              | 5.69 us: 1.05x faster                                                                                                    |
| chaos                      | 41.1 ms                                                                                                              | 39.2 ms: 1.05x faster                                                                                                    |
| logging_format             | 6.48 us                                                                                                              | 6.17 us: 1.05x faster                                                                                                    |
| sqlglot_parse              | 847 us                                                                                                               | 808 us: 1.05x faster                                                                                                     |
| meteor_contest             | 73.3 ms                                                                                                              | 70.2 ms: 1.04x faster                                                                                                    |
| xml_etree_iterparse        | 64.7 ms                                                                                                              | 62.2 ms: 1.04x faster                                                                                                    |
| async_tree_memoization     | 261 ms                                                                                                               | 251 ms: 1.04x faster                                                                                                     |
| regex_dna                  | 126 ms                                                                                                               | 122 ms: 1.03x faster                                                                                                     |
| json_dumps                 | 5.92 ms                                                                                                              | 5.73 ms: 1.03x faster                                                                                                    |
| async_tree_io_tg           | 541 ms                                                                                                               | 528 ms: 1.03x faster                                                                                                     |
| async_tree_cpu_io_mixed    | 391 ms                                                                                                               | 382 ms: 1.02x faster                                                                                                     |
| richards_super             | 33.0 ms                                                                                                              | 32.4 ms: 1.02x faster                                                                                                    |
| thrift                     | 514 us                                                                                                               | 505 us: 1.02x faster                                                                                                     |
| deepcopy_reduce            | 1.81 us                                                                                                              | 1.78 us: 1.02x faster                                                                                                    |
| sqlglot_transpile          | 1.05 ms                                                                                                              | 1.03 ms: 1.02x faster                                                                                                    |
| coroutines                 | 13.6 ms                                                                                                              | 13.5 ms: 1.01x faster                                                                                                    |
| async_tree_cpu_io_mixed_tg | 386 ms                                                                                                               | 381 ms: 1.01x faster                                                                                                     |
| nqueens                    | 60.2 ms                                                                                                              | 59.7 ms: 1.01x faster                                                                                                    |
| scimark_sor                | 86.8 ms                                                                                                              | 86.1 ms: 1.01x faster                                                                                                    |
| regex_effbot               | 1.62 ms                                                                                                              | 1.61 ms: 1.01x faster                                                                                                    |
| richards                   | 28.9 ms                                                                                                              | 28.8 ms: 1.01x faster                                                                                                    |
| mdp                        | 1.47 sec                                                                                                             | 1.46 sec: 1.00x faster                                                                                                   |
| pidigits                   | 150 ms                                                                                                               | 150 ms: 1.00x slower                                                                                                     |
| generators                 | 20.9 ms                                                                                                              | 21.1 ms: 1.01x slower                                                                                                    |
| regex_compile              | 86.8 ms                                                                                                              | 87.6 ms: 1.01x slower                                                                                                    |
| xml_etree_parse            | 92.8 ms                                                                                                              | 93.8 ms: 1.01x slower                                                                                                    |
| python_startup             | 21.4 ms                                                                                                              | 21.7 ms: 1.01x slower                                                                                                    |
| go                         | 91.0 ms                                                                                                              | 93.3 ms: 1.02x slower                                                                                                    |
| deepcopy                   | 175 us                                                                                                               | 179 us: 1.03x slower                                                                                                     |
| tornado_http               | 91.3 ms                                                                                                              | 93.8 ms: 1.03x slower                                                                                                    |
| raytrace                   | 169 ms                                                                                                               | 174 ms: 1.03x slower                                                                                                     |
| python_startup_no_site     | 17.6 ms                                                                                                              | 18.2 ms: 1.04x slower                                                                                                    |
| sqlglot_optimize           | 34.2 ms                                                                                                              | 35.5 ms: 1.04x slower                                                                                                    |
| sympy_str                  | 172 ms                                                                                                               | 181 ms: 1.05x slower                                                                                                     |
| sqlglot_normalize          | 180 ms                                                                                                               | 189 ms: 1.05x slower                                                                                                     |
| async_generators           | 240 ms                                                                                                               | 253 ms: 1.05x slower                                                                                                     |
| 2to3                       | 223 ms                                                                                                               | 235 ms: 1.06x slower                                                                                                     |
| bench_mp_pool              | 67.1 ms                                                                                                              | 71.1 ms: 1.06x slower                                                                                                    |
| sympy_expand               | 298 ms                                                                                                               | 316 ms: 1.06x slower                                                                                                     |
| docutils                   | 1.68 sec                                                                                                             | 1.79 sec: 1.06x slower                                                                                                   |
| sympy_sum                  | 89.0 ms                                                                                                              | 94.4 ms: 1.06x slower                                                                                                    |
| deltablue                  | 2.07 ms                                                                                                              | 2.22 ms: 1.07x slower                                                                                                    |
| typing_runtime_protocols   | 105 us                                                                                                               | 113 us: 1.07x slower                                                                                                     |
| django_template            | 23.0 ms                                                                                                              | 25.3 ms: 1.10x slower                                                                                                    |
| sympy_integrate            | 12.8 ms                                                                                                              | 14.1 ms: 1.10x slower                                                                                                    |
| pylint                     | 209 ms                                                                                                               | 232 ms: 1.11x slower                                                                                                     |
| hexiom                     | 4.12 ms                                                                                                              | 4.60 ms: 1.12x slower                                                                                                    |
| scimark_lu                 | 60.3 ms                                                                                                              | 67.7 ms: 1.12x slower                                                                                                    |
| genshi_text                | 16.0 ms                                                                                                              | 18.3 ms: 1.14x slower                                                                                                    |
| genshi_xml                 | 36.6 ms                                                                                                              | 45.6 ms: 1.25x slower                                                                                                    |
| Geometric mean             | (ref)                                                                                                                | 1.05x faster                                                                                                             |

Benchmark hidden because not significant (10): pycparser, asyncio_tcp, html5lib, json, async_tree_memoization_tg, json_loads, create_gc_cycles, pathlib, gc_traversal, bench_thread_pool

# HPT report

- Reliability score: 98.18% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown
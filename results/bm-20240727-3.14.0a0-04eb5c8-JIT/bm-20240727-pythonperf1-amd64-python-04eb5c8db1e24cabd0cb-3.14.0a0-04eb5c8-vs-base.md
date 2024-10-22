# Results vs. base

- fork: python
- ref: 04eb5c8db1e24cabd0cb
- machine: windows-amd64
- commit hash: 04eb5c8
- commit date: 2024-07-27
- overall geometric mean: 1.03x faster
- HPT reliability: 86.69%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20240727-3.14.0a0-04eb5c8/bm-20240727-pythonperf1-amd64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8.json | results/bm-20240727-3.14.0a0-04eb5c8-JIT/bm-20240727-pythonperf1-amd64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8.json |
|----------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 234 ms                                                                                                               | 233 ms: 1.01x faster                                                                                                     |
| docutils       | 1.75 sec                                                                                                             | 1.88 sec: 1.08x slower                                                                                                   |
| html5lib       | 42.0 ms                                                                                                              | 41.6 ms: 1.01x faster                                                                                                    |
| tornado_http   | 93.3 ms                                                                                                              | 96.3 ms: 1.03x slower                                                                                                    |
| Geometric mean | (ref)                                                                                                                | 1.02x slower                                                                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | results/bm-20240727-3.14.0a0-04eb5c8/bm-20240727-pythonperf1-amd64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8.json | results/bm-20240727-3.14.0a0-04eb5c8-JIT/bm-20240727-pythonperf1-amd64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8.json |
|----------------------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| async_tree_io              | 559 ms                                                                                                               | 539 ms: 1.04x faster                                                                                                     |
| async_tree_cpu_io_mixed_tg | 391 ms                                                                                                               | 381 ms: 1.02x faster                                                                                                     |
| coroutines                 | 13.8 ms                                                                                                              | 13.7 ms: 1.01x faster                                                                                                    |
| async_tree_cpu_io_mixed    | 386 ms                                                                                                               | 395 ms: 1.02x slower                                                                                                     |
| async_generators           | 240 ms                                                                                                               | 257 ms: 1.07x slower                                                                                                     |
| Geometric mean             | (ref)                                                                                                                | 1.00x faster                                                                                                             |

Benchmark hidden because not significant (7): asyncio_tcp_ssl, async_tree_io_tg, async_tree_none_tg, async_tree_memoization, async_tree_none, asyncio_tcp, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20240727-3.14.0a0-04eb5c8/bm-20240727-pythonperf1-amd64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8.json | results/bm-20240727-3.14.0a0-04eb5c8-JIT/bm-20240727-pythonperf1-amd64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8.json |
|----------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| nbody          | 83.2 ms                                                                                                              | 51.1 ms: 1.63x faster                                                                                                    |
| float          | 55.9 ms                                                                                                              | 45.0 ms: 1.24x faster                                                                                                    |
| pidigits       | 151 ms                                                                                                               | 152 ms: 1.00x slower                                                                                                     |
| Geometric mean | (ref)                                                                                                                | 1.26x faster                                                                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20240727-3.14.0a0-04eb5c8/bm-20240727-pythonperf1-amd64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8.json | results/bm-20240727-3.14.0a0-04eb5c8-JIT/bm-20240727-pythonperf1-amd64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8.json |
|----------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| regex_v8       | 17.5 ms                                                                                                              | 15.4 ms: 1.13x faster                                                                                                    |
| regex_compile  | 90.4 ms                                                                                                              | 91.7 ms: 1.01x slower                                                                                                    |
| regex_effbot   | 1.58 ms                                                                                                              | 1.63 ms: 1.04x slower                                                                                                    |
| regex_dna      | 119 ms                                                                                                               | 125 ms: 1.05x slower                                                                                                     |
| Geometric mean | (ref)                                                                                                                | 1.01x faster                                                                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20240727-3.14.0a0-04eb5c8/bm-20240727-pythonperf1-amd64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8.json | results/bm-20240727-3.14.0a0-04eb5c8-JIT/bm-20240727-pythonperf1-amd64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8.json |
|----------------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| tomli_loads          | 1.59 sec                                                                                                             | 1.31 sec: 1.22x faster                                                                                                   |
| pickle_pure_python   | 213 us                                                                                                               | 183 us: 1.16x faster                                                                                                     |
| xml_etree_generate   | 58.9 ms                                                                                                              | 52.4 ms: 1.12x faster                                                                                                    |
| unpickle_pure_python | 151 us                                                                                                               | 135 us: 1.12x faster                                                                                                     |
| xml_etree_process    | 41.2 ms                                                                                                              | 38.1 ms: 1.08x faster                                                                                                    |
| xml_etree_iterparse  | 65.9 ms                                                                                                              | 61.5 ms: 1.07x faster                                                                                                    |
| json_dumps           | 6.26 ms                                                                                                              | 6.08 ms: 1.03x faster                                                                                                    |
| json_loads           | 14.4 us                                                                                                              | 14.8 us: 1.03x slower                                                                                                    |
| Geometric mean       | (ref)                                                                                                                | 1.08x faster                                                                                                             |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | results/bm-20240727-3.14.0a0-04eb5c8/bm-20240727-pythonperf1-amd64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8.json | results/bm-20240727-3.14.0a0-04eb5c8-JIT/bm-20240727-pythonperf1-amd64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8.json |
|------------------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| python_startup_no_site | 18.4 ms                                                                                                              | 17.5 ms: 1.05x faster                                                                                                    |
| python_startup         | 22.2 ms                                                                                                              | 21.3 ms: 1.04x faster                                                                                                    |
| Geometric mean         | (ref)                                                                                                                | 1.05x faster                                                                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20240727-3.14.0a0-04eb5c8/bm-20240727-pythonperf1-amd64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8.json | results/bm-20240727-3.14.0a0-04eb5c8-JIT/bm-20240727-pythonperf1-amd64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8.json |
|-----------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| mako            | 7.07 ms                                                                                                              | 5.19 ms: 1.36x faster                                                                                                    |
| django_template | 24.6 ms                                                                                                              | 26.2 ms: 1.07x slower                                                                                                    |
| genshi_text     | 17.3 ms                                                                                                              | 18.9 ms: 1.09x slower                                                                                                    |
| genshi_xml      | 36.9 ms                                                                                                              | 46.7 ms: 1.27x slower                                                                                                    |
| Geometric mean  | (ref)                                                                                                                | 1.02x slower                                                                                                             |

All benchmarks:
===============

| Benchmark                  | results/bm-20240727-3.14.0a0-04eb5c8/bm-20240727-pythonperf1-amd64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8.json | results/bm-20240727-3.14.0a0-04eb5c8-JIT/bm-20240727-pythonperf1-amd64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8.json |
|----------------------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| nbody                      | 83.2 ms                                                                                                              | 51.1 ms: 1.63x faster                                                                                                    |
| spectral_norm              | 70.9 ms                                                                                                              | 46.8 ms: 1.51x faster                                                                                                    |
| scimark_fft                | 206 ms                                                                                                               | 150 ms: 1.38x faster                                                                                                     |
| mako                       | 7.07 ms                                                                                                              | 5.19 ms: 1.36x faster                                                                                                    |
| scimark_sparse_mat_mult    | 2.79 ms                                                                                                              | 2.09 ms: 1.33x faster                                                                                                    |
| scimark_monte_carlo        | 50.9 ms                                                                                                              | 38.2 ms: 1.33x faster                                                                                                    |
| fannkuch                   | 291 ms                                                                                                               | 229 ms: 1.27x faster                                                                                                     |
| deepcopy_memo              | 20.6 us                                                                                                              | 16.3 us: 1.26x faster                                                                                                    |
| pyflate                    | 319 ms                                                                                                               | 256 ms: 1.25x faster                                                                                                     |
| crypto_pyaes               | 50.6 ms                                                                                                              | 40.6 ms: 1.25x faster                                                                                                    |
| float                      | 55.9 ms                                                                                                              | 45.0 ms: 1.24x faster                                                                                                    |
| tomli_loads                | 1.59 sec                                                                                                             | 1.31 sec: 1.22x faster                                                                                                   |
| pprint_safe_repr           | 566 ms                                                                                                               | 478 ms: 1.18x faster                                                                                                     |
| pycparser                  | 834 ms                                                                                                               | 709 ms: 1.18x faster                                                                                                     |
| pprint_pformat             | 1.15 sec                                                                                                             | 987 ms: 1.17x faster                                                                                                     |
| pickle_pure_python         | 213 us                                                                                                               | 183 us: 1.16x faster                                                                                                     |
| comprehensions             | 12.0 us                                                                                                              | 10.5 us: 1.14x faster                                                                                                    |
| regex_v8                   | 17.5 ms                                                                                                              | 15.4 ms: 1.13x faster                                                                                                    |
| xml_etree_generate         | 58.9 ms                                                                                                              | 52.4 ms: 1.12x faster                                                                                                    |
| unpickle_pure_python       | 151 us                                                                                                               | 135 us: 1.12x faster                                                                                                     |
| logging_silent             | 63.7 ns                                                                                                              | 57.3 ns: 1.11x faster                                                                                                    |
| chaos                      | 44.4 ms                                                                                                              | 40.6 ms: 1.09x faster                                                                                                    |
| xml_etree_process          | 41.2 ms                                                                                                              | 38.1 ms: 1.08x faster                                                                                                    |
| xml_etree_iterparse        | 65.9 ms                                                                                                              | 61.5 ms: 1.07x faster                                                                                                    |
| meteor_contest             | 77.0 ms                                                                                                              | 72.2 ms: 1.07x faster                                                                                                    |
| sqlglot_parse              | 886 us                                                                                                               | 835 us: 1.06x faster                                                                                                     |
| python_startup_no_site     | 18.4 ms                                                                                                              | 17.5 ms: 1.05x faster                                                                                                    |
| logging_simple             | 6.43 us                                                                                                              | 6.13 us: 1.05x faster                                                                                                    |
| richards                   | 32.3 ms                                                                                                              | 30.9 ms: 1.04x faster                                                                                                    |
| logging_format             | 6.98 us                                                                                                              | 6.69 us: 1.04x faster                                                                                                    |
| python_startup             | 22.2 ms                                                                                                              | 21.3 ms: 1.04x faster                                                                                                    |
| async_tree_io              | 559 ms                                                                                                               | 539 ms: 1.04x faster                                                                                                     |
| nqueens                    | 64.5 ms                                                                                                              | 62.1 ms: 1.04x faster                                                                                                    |
| richards_super             | 36.4 ms                                                                                                              | 35.1 ms: 1.04x faster                                                                                                    |
| telco                      | 4.89 ms                                                                                                              | 4.72 ms: 1.04x faster                                                                                                    |
| json_dumps                 | 6.26 ms                                                                                                              | 6.08 ms: 1.03x faster                                                                                                    |
| sqlglot_transpile          | 1.11 ms                                                                                                              | 1.08 ms: 1.03x faster                                                                                                    |
| raytrace                   | 197 ms                                                                                                               | 192 ms: 1.03x faster                                                                                                     |
| async_tree_cpu_io_mixed_tg | 391 ms                                                                                                               | 381 ms: 1.02x faster                                                                                                     |
| html5lib                   | 42.0 ms                                                                                                              | 41.6 ms: 1.01x faster                                                                                                    |
| json                       | 3.17 ms                                                                                                              | 3.14 ms: 1.01x faster                                                                                                    |
| coroutines                 | 13.8 ms                                                                                                              | 13.7 ms: 1.01x faster                                                                                                    |
| 2to3                       | 234 ms                                                                                                               | 233 ms: 1.01x faster                                                                                                     |
| dulwich_log                | 42.7 ms                                                                                                              | 42.4 ms: 1.01x faster                                                                                                    |
| pidigits                   | 151 ms                                                                                                               | 152 ms: 1.00x slower                                                                                                     |
| bench_mp_pool              | 72.7 ms                                                                                                              | 73.2 ms: 1.01x slower                                                                                                    |
| thrift                     | 519 us                                                                                                               | 523 us: 1.01x slower                                                                                                     |
| regex_compile              | 90.4 ms                                                                                                              | 91.7 ms: 1.01x slower                                                                                                    |
| async_tree_cpu_io_mixed    | 386 ms                                                                                                               | 395 ms: 1.02x slower                                                                                                     |
| deepcopy                   | 187 us                                                                                                               | 191 us: 1.02x slower                                                                                                     |
| sqlglot_normalize          | 196 ms                                                                                                               | 201 ms: 1.03x slower                                                                                                     |
| gc_traversal               | 1.55 ms                                                                                                              | 1.60 ms: 1.03x slower                                                                                                    |
| sqlglot_optimize           | 36.8 ms                                                                                                              | 37.8 ms: 1.03x slower                                                                                                    |
| mdp                        | 1.51 sec                                                                                                             | 1.55 sec: 1.03x slower                                                                                                   |
| scimark_sor                | 88.0 ms                                                                                                              | 90.5 ms: 1.03x slower                                                                                                    |
| create_gc_cycles           | 908 us                                                                                                               | 935 us: 1.03x slower                                                                                                     |
| json_loads                 | 14.4 us                                                                                                              | 14.8 us: 1.03x slower                                                                                                    |
| coverage                   | 47.0 ms                                                                                                              | 48.4 ms: 1.03x slower                                                                                                    |
| tornado_http               | 93.3 ms                                                                                                              | 96.3 ms: 1.03x slower                                                                                                    |
| regex_effbot               | 1.58 ms                                                                                                              | 1.63 ms: 1.04x slower                                                                                                    |
| deltablue                  | 2.25 ms                                                                                                              | 2.34 ms: 1.04x slower                                                                                                    |
| go                         | 96.8 ms                                                                                                              | 101 ms: 1.04x slower                                                                                                     |
| pathlib                    | 80.9 ms                                                                                                              | 84.7 ms: 1.05x slower                                                                                                    |
| regex_dna                  | 119 ms                                                                                                               | 125 ms: 1.05x slower                                                                                                     |
| typing_runtime_protocols   | 114 us                                                                                                               | 120 us: 1.06x slower                                                                                                     |
| sympy_str                  | 178 ms                                                                                                               | 189 ms: 1.06x slower                                                                                                     |
| django_template            | 24.6 ms                                                                                                              | 26.2 ms: 1.07x slower                                                                                                    |
| generators                 | 20.3 ms                                                                                                              | 21.7 ms: 1.07x slower                                                                                                    |
| hexiom                     | 4.43 ms                                                                                                              | 4.74 ms: 1.07x slower                                                                                                    |
| sympy_expand               | 306 ms                                                                                                               | 329 ms: 1.07x slower                                                                                                     |
| async_generators           | 240 ms                                                                                                               | 257 ms: 1.07x slower                                                                                                     |
| docutils                   | 1.75 sec                                                                                                             | 1.88 sec: 1.08x slower                                                                                                   |
| sympy_sum                  | 90.6 ms                                                                                                              | 98.7 ms: 1.09x slower                                                                                                    |
| genshi_text                | 17.3 ms                                                                                                              | 18.9 ms: 1.09x slower                                                                                                    |
| sympy_integrate            | 13.3 ms                                                                                                              | 14.7 ms: 1.11x slower                                                                                                    |
| pylint                     | 227 ms                                                                                                               | 255 ms: 1.12x slower                                                                                                     |
| scimark_lu                 | 63.2 ms                                                                                                              | 75.9 ms: 1.20x slower                                                                                                    |
| genshi_xml                 | 36.9 ms                                                                                                              | 46.7 ms: 1.27x slower                                                                                                    |
| bench_thread_pool          | 805 us                                                                                                               | 3.06 ms: 3.80x slower                                                                                                    |
| Geometric mean             | (ref)                                                                                                                | 1.03x faster                                                                                                             |

Benchmark hidden because not significant (9): asyncio_tcp_ssl, async_tree_io_tg, async_tree_none_tg, async_tree_memoization, xml_etree_parse, async_tree_none, deepcopy_reduce, asyncio_tcp, async_tree_memoization_tg

# HPT report

- Reliability score: 86.69% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown
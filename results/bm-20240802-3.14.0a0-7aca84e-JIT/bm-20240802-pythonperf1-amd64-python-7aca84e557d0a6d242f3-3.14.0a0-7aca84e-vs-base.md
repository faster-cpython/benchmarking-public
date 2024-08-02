# Results vs. base

- fork: python
- ref: 7aca84e557d0a6d242f3
- machine: windows-amd64
- commit hash: 7aca84e
- commit date: 2024-08-02
- overall geometric mean: 1.08x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20240802-3.14.0a0-7aca84e/bm-20240802-pythonperf1-amd64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e.json | results/bm-20240802-3.14.0a0-7aca84e-JIT/bm-20240802-pythonperf1-amd64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e.json |
|----------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 236 ms                                                                                                               | 242 ms: 1.02x slower                                                                                                     |
| docutils       | 1.79 sec                                                                                                             | 1.85 sec: 1.03x slower                                                                                                   |
| Geometric mean | (ref)                                                                                                                | 1.01x slower                                                                                                             |

Benchmark hidden because not significant (2): html5lib, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | results/bm-20240802-3.14.0a0-7aca84e/bm-20240802-pythonperf1-amd64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e.json | results/bm-20240802-3.14.0a0-7aca84e-JIT/bm-20240802-pythonperf1-amd64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e.json |
|----------------------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| asyncio_tcp_ssl            | 1.67 sec                                                                                                             | 1.51 sec: 1.10x faster                                                                                                   |
| async_tree_io              | 597 ms                                                                                                               | 553 ms: 1.08x faster                                                                                                     |
| async_tree_none_tg         | 203 ms                                                                                                               | 194 ms: 1.05x faster                                                                                                     |
| async_tree_cpu_io_mixed_tg | 396 ms                                                                                                               | 379 ms: 1.04x faster                                                                                                     |
| async_tree_none            | 223 ms                                                                                                               | 214 ms: 1.04x faster                                                                                                     |
| async_tree_io_tg           | 559 ms                                                                                                               | 540 ms: 1.03x faster                                                                                                     |
| coroutines                 | 14.1 ms                                                                                                              | 13.8 ms: 1.03x faster                                                                                                    |
| async_generators           | 252 ms                                                                                                               | 261 ms: 1.04x slower                                                                                                     |
| Geometric mean             | (ref)                                                                                                                | 1.03x faster                                                                                                             |

Benchmark hidden because not significant (4): async_tree_memoization, asyncio_tcp, async_tree_memoization_tg, async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20240802-3.14.0a0-7aca84e/bm-20240802-pythonperf1-amd64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e.json | results/bm-20240802-3.14.0a0-7aca84e-JIT/bm-20240802-pythonperf1-amd64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e.json |
|----------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| nbody          | 85.4 ms                                                                                                              | 50.1 ms: 1.70x faster                                                                                                    |
| float          | 57.0 ms                                                                                                              | 45.0 ms: 1.27x faster                                                                                                    |
| pidigits       | 151 ms                                                                                                               | 150 ms: 1.01x faster                                                                                                     |
| Geometric mean | (ref)                                                                                                                | 1.30x faster                                                                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20240802-3.14.0a0-7aca84e/bm-20240802-pythonperf1-amd64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e.json | results/bm-20240802-3.14.0a0-7aca84e-JIT/bm-20240802-pythonperf1-amd64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e.json |
|----------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| regex_v8       | 16.8 ms                                                                                                              | 14.9 ms: 1.13x faster                                                                                                    |
| regex_compile  | 94.5 ms                                                                                                              | 91.0 ms: 1.04x faster                                                                                                    |
| regex_effbot   | 1.57 ms                                                                                                              | 1.61 ms: 1.03x slower                                                                                                    |
| regex_dna      | 115 ms                                                                                                               | 119 ms: 1.04x slower                                                                                                     |
| Geometric mean | (ref)                                                                                                                | 1.02x faster                                                                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20240802-3.14.0a0-7aca84e/bm-20240802-pythonperf1-amd64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e.json | results/bm-20240802-3.14.0a0-7aca84e-JIT/bm-20240802-pythonperf1-amd64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e.json |
|----------------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| tomli_loads          | 1.62 sec                                                                                                             | 1.26 sec: 1.28x faster                                                                                                   |
| pickle_pure_python   | 221 us                                                                                                               | 182 us: 1.21x faster                                                                                                     |
| xml_etree_process    | 42.1 ms                                                                                                              | 37.6 ms: 1.12x faster                                                                                                    |
| xml_etree_generate   | 58.7 ms                                                                                                              | 52.6 ms: 1.12x faster                                                                                                    |
| unpickle_pure_python | 153 us                                                                                                               | 138 us: 1.11x faster                                                                                                     |
| xml_etree_iterparse  | 66.6 ms                                                                                                              | 61.8 ms: 1.08x faster                                                                                                    |
| json_dumps           | 6.26 ms                                                                                                              | 5.96 ms: 1.05x faster                                                                                                    |
| xml_etree_parse      | 94.8 ms                                                                                                              | 95.5 ms: 1.01x slower                                                                                                    |
| Geometric mean       | (ref)                                                                                                                | 1.10x faster                                                                                                             |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | results/bm-20240802-3.14.0a0-7aca84e/bm-20240802-pythonperf1-amd64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e.json | results/bm-20240802-3.14.0a0-7aca84e-JIT/bm-20240802-pythonperf1-amd64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e.json |
|------------------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| python_startup         | 22.2 ms                                                                                                              | 22.0 ms: 1.01x faster                                                                                                    |
| python_startup_no_site | 17.8 ms                                                                                                              | 18.4 ms: 1.03x slower                                                                                                    |
| Geometric mean         | (ref)                                                                                                                | 1.01x slower                                                                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20240802-3.14.0a0-7aca84e/bm-20240802-pythonperf1-amd64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e.json | results/bm-20240802-3.14.0a0-7aca84e-JIT/bm-20240802-pythonperf1-amd64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e.json |
|-----------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| mako            | 7.06 ms                                                                                                              | 5.05 ms: 1.40x faster                                                                                                    |
| django_template | 26.1 ms                                                                                                              | 25.7 ms: 1.02x faster                                                                                                    |
| genshi_xml      | 37.4 ms                                                                                                              | 40.0 ms: 1.07x slower                                                                                                    |
| Geometric mean  | (ref)                                                                                                                | 1.07x faster                                                                                                             |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark                  | results/bm-20240802-3.14.0a0-7aca84e/bm-20240802-pythonperf1-amd64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e.json | results/bm-20240802-3.14.0a0-7aca84e-JIT/bm-20240802-pythonperf1-amd64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e.json |
|----------------------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| nbody                      | 85.4 ms                                                                                                              | 50.1 ms: 1.70x faster                                                                                                    |
| spectral_norm              | 74.7 ms                                                                                                              | 45.0 ms: 1.66x faster                                                                                                    |
| scimark_sor                | 95.8 ms                                                                                                              | 60.4 ms: 1.59x faster                                                                                                    |
| mako                       | 7.06 ms                                                                                                              | 5.05 ms: 1.40x faster                                                                                                    |
| fannkuch                   | 296 ms                                                                                                               | 214 ms: 1.38x faster                                                                                                     |
| scimark_fft                | 202 ms                                                                                                               | 147 ms: 1.37x faster                                                                                                     |
| pyflate                    | 332 ms                                                                                                               | 251 ms: 1.32x faster                                                                                                     |
| deepcopy_memo              | 20.7 us                                                                                                              | 15.7 us: 1.31x faster                                                                                                    |
| crypto_pyaes               | 52.0 ms                                                                                                              | 40.3 ms: 1.29x faster                                                                                                    |
| scimark_monte_carlo        | 50.4 ms                                                                                                              | 39.2 ms: 1.29x faster                                                                                                    |
| tomli_loads                | 1.62 sec                                                                                                             | 1.26 sec: 1.28x faster                                                                                                   |
| float                      | 57.0 ms                                                                                                              | 45.0 ms: 1.27x faster                                                                                                    |
| scimark_sparse_mat_mult    | 2.62 ms                                                                                                              | 2.10 ms: 1.25x faster                                                                                                    |
| pickle_pure_python         | 221 us                                                                                                               | 182 us: 1.21x faster                                                                                                     |
| scimark_lu                 | 64.8 ms                                                                                                              | 54.0 ms: 1.20x faster                                                                                                    |
| pprint_safe_repr           | 581 ms                                                                                                               | 484 ms: 1.20x faster                                                                                                     |
| pprint_pformat             | 1.18 sec                                                                                                             | 993 ms: 1.19x faster                                                                                                     |
| comprehensions             | 12.5 us                                                                                                              | 10.6 us: 1.18x faster                                                                                                    |
| logging_silent             | 65.5 ns                                                                                                              | 57.2 ns: 1.15x faster                                                                                                    |
| richards                   | 34.7 ms                                                                                                              | 30.4 ms: 1.14x faster                                                                                                    |
| chaos                      | 44.9 ms                                                                                                              | 39.9 ms: 1.13x faster                                                                                                    |
| regex_v8                   | 16.8 ms                                                                                                              | 14.9 ms: 1.13x faster                                                                                                    |
| richards_super             | 39.3 ms                                                                                                              | 35.0 ms: 1.12x faster                                                                                                    |
| xml_etree_process          | 42.1 ms                                                                                                              | 37.6 ms: 1.12x faster                                                                                                    |
| xml_etree_generate         | 58.7 ms                                                                                                              | 52.6 ms: 1.12x faster                                                                                                    |
| telco                      | 5.13 ms                                                                                                              | 4.61 ms: 1.11x faster                                                                                                    |
| unpickle_pure_python       | 153 us                                                                                                               | 138 us: 1.11x faster                                                                                                     |
| asyncio_tcp_ssl            | 1.67 sec                                                                                                             | 1.51 sec: 1.10x faster                                                                                                   |
| logging_simple             | 6.52 us                                                                                                              | 5.94 us: 1.10x faster                                                                                                    |
| logging_format             | 7.01 us                                                                                                              | 6.39 us: 1.10x faster                                                                                                    |
| raytrace                   | 206 ms                                                                                                               | 190 ms: 1.08x faster                                                                                                     |
| async_tree_io              | 597 ms                                                                                                               | 553 ms: 1.08x faster                                                                                                     |
| xml_etree_iterparse        | 66.6 ms                                                                                                              | 61.8 ms: 1.08x faster                                                                                                    |
| sqlglot_parse              | 903 us                                                                                                               | 838 us: 1.08x faster                                                                                                     |
| meteor_contest             | 77.2 ms                                                                                                              | 71.8 ms: 1.07x faster                                                                                                    |
| mdp                        | 1.58 sec                                                                                                             | 1.47 sec: 1.07x faster                                                                                                   |
| deepcopy_reduce            | 1.96 us                                                                                                              | 1.85 us: 1.06x faster                                                                                                    |
| json_dumps                 | 6.26 ms                                                                                                              | 5.96 ms: 1.05x faster                                                                                                    |
| async_tree_none_tg         | 203 ms                                                                                                               | 194 ms: 1.05x faster                                                                                                     |
| sqlglot_normalize          | 203 ms                                                                                                               | 194 ms: 1.05x faster                                                                                                     |
| nqueens                    | 65.5 ms                                                                                                              | 62.7 ms: 1.04x faster                                                                                                    |
| async_tree_cpu_io_mixed_tg | 396 ms                                                                                                               | 379 ms: 1.04x faster                                                                                                     |
| async_tree_none            | 223 ms                                                                                                               | 214 ms: 1.04x faster                                                                                                     |
| regex_compile              | 94.5 ms                                                                                                              | 91.0 ms: 1.04x faster                                                                                                    |
| sqlglot_transpile          | 1.13 ms                                                                                                              | 1.09 ms: 1.03x faster                                                                                                    |
| async_tree_io_tg           | 559 ms                                                                                                               | 540 ms: 1.03x faster                                                                                                     |
| coroutines                 | 14.1 ms                                                                                                              | 13.8 ms: 1.03x faster                                                                                                    |
| dulwich_log                | 44.5 ms                                                                                                              | 43.4 ms: 1.03x faster                                                                                                    |
| sqlglot_optimize           | 37.8 ms                                                                                                              | 36.9 ms: 1.02x faster                                                                                                    |
| django_template            | 26.1 ms                                                                                                              | 25.7 ms: 1.02x faster                                                                                                    |
| deltablue                  | 2.37 ms                                                                                                              | 2.34 ms: 1.01x faster                                                                                                    |
| python_startup             | 22.2 ms                                                                                                              | 22.0 ms: 1.01x faster                                                                                                    |
| pidigits                   | 151 ms                                                                                                               | 150 ms: 1.01x faster                                                                                                     |
| thrift                     | 524 us                                                                                                               | 520 us: 1.01x faster                                                                                                     |
| xml_etree_parse            | 94.8 ms                                                                                                              | 95.5 ms: 1.01x slower                                                                                                    |
| coverage                   | 47.2 ms                                                                                                              | 47.7 ms: 1.01x slower                                                                                                    |
| create_gc_cycles           | 912 us                                                                                                               | 925 us: 1.01x slower                                                                                                     |
| hexiom                     | 4.70 ms                                                                                                              | 4.79 ms: 1.02x slower                                                                                                    |
| 2to3                       | 236 ms                                                                                                               | 242 ms: 1.02x slower                                                                                                     |
| regex_effbot               | 1.57 ms                                                                                                              | 1.61 ms: 1.03x slower                                                                                                    |
| python_startup_no_site     | 17.8 ms                                                                                                              | 18.4 ms: 1.03x slower                                                                                                    |
| docutils                   | 1.79 sec                                                                                                             | 1.85 sec: 1.03x slower                                                                                                   |
| generators                 | 21.8 ms                                                                                                              | 22.5 ms: 1.03x slower                                                                                                    |
| async_generators           | 252 ms                                                                                                               | 261 ms: 1.04x slower                                                                                                     |
| regex_dna                  | 115 ms                                                                                                               | 119 ms: 1.04x slower                                                                                                     |
| sympy_sum                  | 94.0 ms                                                                                                              | 98.4 ms: 1.05x slower                                                                                                    |
| sympy_str                  | 182 ms                                                                                                               | 192 ms: 1.05x slower                                                                                                     |
| bench_mp_pool              | 69.4 ms                                                                                                              | 73.7 ms: 1.06x slower                                                                                                    |
| sympy_expand               | 314 ms                                                                                                               | 334 ms: 1.06x slower                                                                                                     |
| genshi_xml                 | 37.4 ms                                                                                                              | 40.0 ms: 1.07x slower                                                                                                    |
| sympy_integrate            | 13.5 ms                                                                                                              | 14.9 ms: 1.10x slower                                                                                                    |
| Geometric mean             | (ref)                                                                                                                | 1.08x faster                                                                                                             |

Benchmark hidden because not significant (17): async_tree_memoization, pycparser, bench_thread_pool, json, asyncio_tcp, async_tree_memoization_tg, gc_traversal, tornado_http, pathlib, async_tree_cpu_io_mixed, html5lib, json_loads, go, typing_runtime_protocols, genshi_text, deepcopy, pylint

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: unknown
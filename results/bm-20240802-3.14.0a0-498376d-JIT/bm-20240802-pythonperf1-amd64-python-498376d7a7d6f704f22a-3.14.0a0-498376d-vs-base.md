# Results vs. base

- fork: python
- ref: 498376d7a7d6f704f22a
- machine: windows-amd64
- commit hash: 498376d
- commit date: 2024-08-02
- overall geometric mean: 1.10x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20240802-3.14.0a0-498376d/bm-20240802-pythonperf1-amd64-python-498376d7a7d6f704f22a-3.14.0a0-498376d.json | results/bm-20240802-3.14.0a0-498376d-JIT/bm-20240802-pythonperf1-amd64-python-498376d7a7d6f704f22a-3.14.0a0-498376d.json |
|----------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 232 ms                                                                                                               | 240 ms: 1.04x slower                                                                                                     |
| docutils       | 1.79 sec                                                                                                             | 1.84 sec: 1.03x slower                                                                                                   |
| html5lib       | 42.3 ms                                                                                                              | 41.0 ms: 1.03x faster                                                                                                    |
| tornado_http   | 95.3 ms                                                                                                              | 96.1 ms: 1.01x slower                                                                                                    |
| Geometric mean | (ref)                                                                                                                | 1.01x slower                                                                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | results/bm-20240802-3.14.0a0-498376d/bm-20240802-pythonperf1-amd64-python-498376d7a7d6f704f22a-3.14.0a0-498376d.json | results/bm-20240802-3.14.0a0-498376d-JIT/bm-20240802-pythonperf1-amd64-python-498376d7a7d6f704f22a-3.14.0a0-498376d.json |
|----------------------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| asyncio_tcp_ssl            | 1.70 sec                                                                                                             | 1.52 sec: 1.12x faster                                                                                                   |
| async_tree_io              | 599 ms                                                                                                               | 551 ms: 1.09x faster                                                                                                     |
| async_tree_none_tg         | 202 ms                                                                                                               | 189 ms: 1.07x faster                                                                                                     |
| async_tree_none            | 225 ms                                                                                                               | 212 ms: 1.06x faster                                                                                                     |
| async_tree_cpu_io_mixed_tg | 398 ms                                                                                                               | 375 ms: 1.06x faster                                                                                                     |
| async_tree_memoization     | 272 ms                                                                                                               | 259 ms: 1.05x faster                                                                                                     |
| async_tree_io_tg           | 561 ms                                                                                                               | 537 ms: 1.04x faster                                                                                                     |
| coroutines                 | 13.9 ms                                                                                                              | 14.1 ms: 1.01x slower                                                                                                    |
| async_generators           | 249 ms                                                                                                               | 256 ms: 1.03x slower                                                                                                     |
| Geometric mean             | (ref)                                                                                                                | 1.04x faster                                                                                                             |

Benchmark hidden because not significant (3): async_tree_memoization_tg, async_tree_cpu_io_mixed, asyncio_tcp

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20240802-3.14.0a0-498376d/bm-20240802-pythonperf1-amd64-python-498376d7a7d6f704f22a-3.14.0a0-498376d.json | results/bm-20240802-3.14.0a0-498376d-JIT/bm-20240802-pythonperf1-amd64-python-498376d7a7d6f704f22a-3.14.0a0-498376d.json |
|----------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| nbody          | 91.2 ms                                                                                                              | 49.8 ms: 1.83x faster                                                                                                    |
| float          | 55.3 ms                                                                                                              | 44.9 ms: 1.23x faster                                                                                                    |
| pidigits       | 151 ms                                                                                                               | 150 ms: 1.01x faster                                                                                                     |
| Geometric mean | (ref)                                                                                                                | 1.32x faster                                                                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20240802-3.14.0a0-498376d/bm-20240802-pythonperf1-amd64-python-498376d7a7d6f704f22a-3.14.0a0-498376d.json | results/bm-20240802-3.14.0a0-498376d-JIT/bm-20240802-pythonperf1-amd64-python-498376d7a7d6f704f22a-3.14.0a0-498376d.json |
|----------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| regex_v8       | 16.7 ms                                                                                                              | 15.4 ms: 1.09x faster                                                                                                    |
| regex_compile  | 94.2 ms                                                                                                              | 89.4 ms: 1.05x faster                                                                                                    |
| regex_dna      | 125 ms                                                                                                               | 122 ms: 1.03x faster                                                                                                     |
| regex_effbot   | 1.63 ms                                                                                                              | 1.62 ms: 1.01x faster                                                                                                    |
| Geometric mean | (ref)                                                                                                                | 1.04x faster                                                                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20240802-3.14.0a0-498376d/bm-20240802-pythonperf1-amd64-python-498376d7a7d6f704f22a-3.14.0a0-498376d.json | results/bm-20240802-3.14.0a0-498376d-JIT/bm-20240802-pythonperf1-amd64-python-498376d7a7d6f704f22a-3.14.0a0-498376d.json |
|----------------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| tomli_loads          | 1.66 sec                                                                                                             | 1.25 sec: 1.33x faster                                                                                                   |
| pickle_pure_python   | 226 us                                                                                                               | 181 us: 1.25x faster                                                                                                     |
| xml_etree_process    | 42.5 ms                                                                                                              | 37.5 ms: 1.13x faster                                                                                                    |
| xml_etree_generate   | 59.1 ms                                                                                                              | 52.6 ms: 1.12x faster                                                                                                    |
| unpickle_pure_python | 152 us                                                                                                               | 136 us: 1.12x faster                                                                                                     |
| xml_etree_iterparse  | 66.2 ms                                                                                                              | 61.5 ms: 1.08x faster                                                                                                    |
| json_dumps           | 6.26 ms                                                                                                              | 5.99 ms: 1.05x faster                                                                                                    |
| xml_etree_parse      | 95.6 ms                                                                                                              | 92.9 ms: 1.03x faster                                                                                                    |
| json_loads           | 14.1 us                                                                                                              | 14.3 us: 1.01x slower                                                                                                    |
| Geometric mean       | (ref)                                                                                                                | 1.12x faster                                                                                                             |

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup, python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20240802-3.14.0a0-498376d/bm-20240802-pythonperf1-amd64-python-498376d7a7d6f704f22a-3.14.0a0-498376d.json | results/bm-20240802-3.14.0a0-498376d-JIT/bm-20240802-pythonperf1-amd64-python-498376d7a7d6f704f22a-3.14.0a0-498376d.json |
|-----------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| mako            | 7.13 ms                                                                                                              | 4.96 ms: 1.44x faster                                                                                                    |
| django_template | 26.2 ms                                                                                                              | 24.7 ms: 1.06x faster                                                                                                    |
| genshi_text     | 18.0 ms                                                                                                              | 17.9 ms: 1.01x faster                                                                                                    |
| genshi_xml      | 36.9 ms                                                                                                              | 39.0 ms: 1.06x slower                                                                                                    |
| Geometric mean  | (ref)                                                                                                                | 1.10x faster                                                                                                             |

All benchmarks:
===============

| Benchmark                  | results/bm-20240802-3.14.0a0-498376d/bm-20240802-pythonperf1-amd64-python-498376d7a7d6f704f22a-3.14.0a0-498376d.json | results/bm-20240802-3.14.0a0-498376d-JIT/bm-20240802-pythonperf1-amd64-python-498376d7a7d6f704f22a-3.14.0a0-498376d.json |
|----------------------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| nbody                      | 91.2 ms                                                                                                              | 49.8 ms: 1.83x faster                                                                                                    |
| spectral_norm              | 77.3 ms                                                                                                              | 46.1 ms: 1.68x faster                                                                                                    |
| scimark_sor                | 96.2 ms                                                                                                              | 59.9 ms: 1.61x faster                                                                                                    |
| mako                       | 7.13 ms                                                                                                              | 4.96 ms: 1.44x faster                                                                                                    |
| scimark_monte_carlo        | 52.5 ms                                                                                                              | 37.5 ms: 1.40x faster                                                                                                    |
| scimark_fft                | 205 ms                                                                                                               | 148 ms: 1.39x faster                                                                                                     |
| fannkuch                   | 298 ms                                                                                                               | 220 ms: 1.36x faster                                                                                                     |
| scimark_sparse_mat_mult    | 2.78 ms                                                                                                              | 2.07 ms: 1.34x faster                                                                                                    |
| tomli_loads                | 1.66 sec                                                                                                             | 1.25 sec: 1.33x faster                                                                                                   |
| deepcopy_memo              | 21.3 us                                                                                                              | 16.2 us: 1.31x faster                                                                                                    |
| crypto_pyaes               | 51.9 ms                                                                                                              | 39.9 ms: 1.30x faster                                                                                                    |
| pyflate                    | 333 ms                                                                                                               | 257 ms: 1.29x faster                                                                                                     |
| pycparser                  | 928 ms                                                                                                               | 726 ms: 1.28x faster                                                                                                     |
| pickle_pure_python         | 226 us                                                                                                               | 181 us: 1.25x faster                                                                                                     |
| float                      | 55.3 ms                                                                                                              | 44.9 ms: 1.23x faster                                                                                                    |
| comprehensions             | 12.5 us                                                                                                              | 10.2 us: 1.22x faster                                                                                                    |
| pprint_safe_repr           | 573 ms                                                                                                               | 475 ms: 1.21x faster                                                                                                     |
| pprint_pformat             | 1.18 sec                                                                                                             | 983 ms: 1.20x faster                                                                                                     |
| chaos                      | 45.8 ms                                                                                                              | 39.0 ms: 1.17x faster                                                                                                    |
| scimark_lu                 | 65.1 ms                                                                                                              | 55.6 ms: 1.17x faster                                                                                                    |
| logging_silent             | 66.1 ns                                                                                                              | 56.5 ns: 1.17x faster                                                                                                    |
| deepcopy_reduce            | 2.02 us                                                                                                              | 1.78 us: 1.14x faster                                                                                                    |
| xml_etree_process          | 42.5 ms                                                                                                              | 37.5 ms: 1.13x faster                                                                                                    |
| xml_etree_generate         | 59.1 ms                                                                                                              | 52.6 ms: 1.12x faster                                                                                                    |
| unpickle_pure_python       | 152 us                                                                                                               | 136 us: 1.12x faster                                                                                                     |
| richards                   | 34.2 ms                                                                                                              | 30.6 ms: 1.12x faster                                                                                                    |
| asyncio_tcp_ssl            | 1.70 sec                                                                                                             | 1.52 sec: 1.12x faster                                                                                                   |
| richards_super             | 38.5 ms                                                                                                              | 34.5 ms: 1.12x faster                                                                                                    |
| mdp                        | 1.58 sec                                                                                                             | 1.41 sec: 1.11x faster                                                                                                   |
| meteor_contest             | 78.0 ms                                                                                                              | 70.1 ms: 1.11x faster                                                                                                    |
| sqlglot_parse              | 915 us                                                                                                               | 834 us: 1.10x faster                                                                                                     |
| telco                      | 4.97 ms                                                                                                              | 4.54 ms: 1.09x faster                                                                                                    |
| logging_format             | 6.94 us                                                                                                              | 6.36 us: 1.09x faster                                                                                                    |
| logging_simple             | 6.48 us                                                                                                              | 5.95 us: 1.09x faster                                                                                                    |
| async_tree_io              | 599 ms                                                                                                               | 551 ms: 1.09x faster                                                                                                     |
| regex_v8                   | 16.7 ms                                                                                                              | 15.4 ms: 1.09x faster                                                                                                    |
| raytrace                   | 204 ms                                                                                                               | 188 ms: 1.08x faster                                                                                                     |
| nqueens                    | 66.8 ms                                                                                                              | 61.9 ms: 1.08x faster                                                                                                    |
| xml_etree_iterparse        | 66.2 ms                                                                                                              | 61.5 ms: 1.08x faster                                                                                                    |
| async_tree_none_tg         | 202 ms                                                                                                               | 189 ms: 1.07x faster                                                                                                     |
| async_tree_none            | 225 ms                                                                                                               | 212 ms: 1.06x faster                                                                                                     |
| django_template            | 26.2 ms                                                                                                              | 24.7 ms: 1.06x faster                                                                                                    |
| async_tree_cpu_io_mixed_tg | 398 ms                                                                                                               | 375 ms: 1.06x faster                                                                                                     |
| deepcopy                   | 193 us                                                                                                               | 183 us: 1.06x faster                                                                                                     |
| sqlglot_transpile          | 1.14 ms                                                                                                              | 1.08 ms: 1.05x faster                                                                                                    |
| regex_compile              | 94.2 ms                                                                                                              | 89.4 ms: 1.05x faster                                                                                                    |
| async_tree_memoization     | 272 ms                                                                                                               | 259 ms: 1.05x faster                                                                                                     |
| json_dumps                 | 6.26 ms                                                                                                              | 5.99 ms: 1.05x faster                                                                                                    |
| async_tree_io_tg           | 561 ms                                                                                                               | 537 ms: 1.04x faster                                                                                                     |
| sqlglot_normalize          | 202 ms                                                                                                               | 195 ms: 1.04x faster                                                                                                     |
| html5lib                   | 42.3 ms                                                                                                              | 41.0 ms: 1.03x faster                                                                                                    |
| dulwich_log                | 44.4 ms                                                                                                              | 43.1 ms: 1.03x faster                                                                                                    |
| xml_etree_parse            | 95.6 ms                                                                                                              | 92.9 ms: 1.03x faster                                                                                                    |
| regex_dna                  | 125 ms                                                                                                               | 122 ms: 1.03x faster                                                                                                     |
| sqlglot_optimize           | 37.6 ms                                                                                                              | 36.9 ms: 1.02x faster                                                                                                    |
| json                       | 3.07 ms                                                                                                              | 3.00 ms: 1.02x faster                                                                                                    |
| thrift                     | 526 us                                                                                                               | 519 us: 1.01x faster                                                                                                     |
| pidigits                   | 151 ms                                                                                                               | 150 ms: 1.01x faster                                                                                                     |
| regex_effbot               | 1.63 ms                                                                                                              | 1.62 ms: 1.01x faster                                                                                                    |
| coverage                   | 47.6 ms                                                                                                              | 47.1 ms: 1.01x faster                                                                                                    |
| genshi_text                | 18.0 ms                                                                                                              | 17.9 ms: 1.01x faster                                                                                                    |
| generators                 | 20.9 ms                                                                                                              | 20.8 ms: 1.01x faster                                                                                                    |
| hexiom                     | 4.72 ms                                                                                                              | 4.69 ms: 1.01x faster                                                                                                    |
| deltablue                  | 2.35 ms                                                                                                              | 2.36 ms: 1.00x slower                                                                                                    |
| tornado_http               | 95.3 ms                                                                                                              | 96.1 ms: 1.01x slower                                                                                                    |
| json_loads                 | 14.1 us                                                                                                              | 14.3 us: 1.01x slower                                                                                                    |
| coroutines                 | 13.9 ms                                                                                                              | 14.1 ms: 1.01x slower                                                                                                    |
| pathlib                    | 81.0 ms                                                                                                              | 82.1 ms: 1.01x slower                                                                                                    |
| sympy_str                  | 184 ms                                                                                                               | 188 ms: 1.02x slower                                                                                                     |
| docutils                   | 1.79 sec                                                                                                             | 1.84 sec: 1.03x slower                                                                                                   |
| async_generators           | 249 ms                                                                                                               | 256 ms: 1.03x slower                                                                                                     |
| typing_runtime_protocols   | 117 us                                                                                                               | 121 us: 1.03x slower                                                                                                     |
| sympy_sum                  | 94.0 ms                                                                                                              | 97.3 ms: 1.03x slower                                                                                                    |
| 2to3                       | 232 ms                                                                                                               | 240 ms: 1.04x slower                                                                                                     |
| bench_mp_pool              | 69.9 ms                                                                                                              | 73.7 ms: 1.05x slower                                                                                                    |
| genshi_xml                 | 36.9 ms                                                                                                              | 39.0 ms: 1.06x slower                                                                                                    |
| sympy_expand               | 312 ms                                                                                                               | 332 ms: 1.06x slower                                                                                                     |
| sympy_integrate            | 13.6 ms                                                                                                              | 14.7 ms: 1.08x slower                                                                                                    |
| Geometric mean             | (ref)                                                                                                                | 1.10x faster                                                                                                             |

Benchmark hidden because not significant (10): async_tree_memoization_tg, async_tree_cpu_io_mixed, asyncio_tcp, bench_thread_pool, go, python_startup, gc_traversal, create_gc_cycles, python_startup_no_site, pylint

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: unknown
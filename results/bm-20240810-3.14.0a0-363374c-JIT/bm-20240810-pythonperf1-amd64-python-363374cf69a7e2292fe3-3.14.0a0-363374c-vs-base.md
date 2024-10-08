# Results vs. base

- fork: python
- ref: 363374cf69a7e2292fe3
- machine: windows-amd64
- commit hash: 363374c
- commit date: 2024-08-10
- overall geometric mean: 1.07x faster
- HPT reliability: 99.93%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20240810-3.14.0a0-363374c/bm-20240810-pythonperf1-amd64-python-363374cf69a7e2292fe3-3.14.0a0-363374c.json | results/bm-20240810-3.14.0a0-363374c-JIT/bm-20240810-pythonperf1-amd64-python-363374cf69a7e2292fe3-3.14.0a0-363374c.json |
|----------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 233 ms                                                                                                               | 240 ms: 1.03x slower                                                                                                     |
| docutils       | 1.78 sec                                                                                                             | 1.85 sec: 1.04x slower                                                                                                   |
| html5lib       | 42.4 ms                                                                                                              | 42.0 ms: 1.01x faster                                                                                                    |
| tornado_http   | 94.9 ms                                                                                                              | 96.1 ms: 1.01x slower                                                                                                    |
| Geometric mean | (ref)                                                                                                                | 1.02x slower                                                                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | results/bm-20240810-3.14.0a0-363374c/bm-20240810-pythonperf1-amd64-python-363374cf69a7e2292fe3-3.14.0a0-363374c.json | results/bm-20240810-3.14.0a0-363374c-JIT/bm-20240810-pythonperf1-amd64-python-363374cf69a7e2292fe3-3.14.0a0-363374c.json |
|----------------------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| asyncio_tcp_ssl            | 1.55 sec                                                                                                             | 1.39 sec: 1.12x faster                                                                                                   |
| async_tree_cpu_io_mixed_tg | 398 ms                                                                                                               | 381 ms: 1.04x faster                                                                                                     |
| coroutines                 | 14.2 ms                                                                                                              | 13.8 ms: 1.03x faster                                                                                                    |
| asyncio_tcp                | 535 ms                                                                                                               | 550 ms: 1.03x slower                                                                                                     |
| async_generators           | 246 ms                                                                                                               | 260 ms: 1.06x slower                                                                                                     |
| Geometric mean             | (ref)                                                                                                                | 1.01x faster                                                                                                             |

Benchmark hidden because not significant (7): async_tree_none, async_tree_io, async_tree_none_tg, async_tree_memoization, async_tree_io_tg, async_tree_cpu_io_mixed, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20240810-3.14.0a0-363374c/bm-20240810-pythonperf1-amd64-python-363374cf69a7e2292fe3-3.14.0a0-363374c.json | results/bm-20240810-3.14.0a0-363374c-JIT/bm-20240810-pythonperf1-amd64-python-363374cf69a7e2292fe3-3.14.0a0-363374c.json |
|----------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| nbody          | 84.9 ms                                                                                                              | 50.0 ms: 1.70x faster                                                                                                    |
| float          | 55.5 ms                                                                                                              | 44.3 ms: 1.25x faster                                                                                                    |
| pidigits       | 151 ms                                                                                                               | 150 ms: 1.01x faster                                                                                                     |
| Geometric mean | (ref)                                                                                                                | 1.29x faster                                                                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20240810-3.14.0a0-363374c/bm-20240810-pythonperf1-amd64-python-363374cf69a7e2292fe3-3.14.0a0-363374c.json | results/bm-20240810-3.14.0a0-363374c-JIT/bm-20240810-pythonperf1-amd64-python-363374cf69a7e2292fe3-3.14.0a0-363374c.json |
|----------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| regex_compile  | 92.3 ms                                                                                                              | 90.0 ms: 1.03x faster                                                                                                    |
| regex_effbot   | 1.59 ms                                                                                                              | 1.63 ms: 1.03x slower                                                                                                    |
| regex_dna      | 118 ms                                                                                                               | 124 ms: 1.06x slower                                                                                                     |
| Geometric mean | (ref)                                                                                                                | 1.02x slower                                                                                                             |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20240810-3.14.0a0-363374c/bm-20240810-pythonperf1-amd64-python-363374cf69a7e2292fe3-3.14.0a0-363374c.json | results/bm-20240810-3.14.0a0-363374c-JIT/bm-20240810-pythonperf1-amd64-python-363374cf69a7e2292fe3-3.14.0a0-363374c.json |
|----------------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| tomli_loads          | 1.62 sec                                                                                                             | 1.27 sec: 1.27x faster                                                                                                   |
| pickle_pure_python   | 215 us                                                                                                               | 182 us: 1.18x faster                                                                                                     |
| unpickle_pure_python | 153 us                                                                                                               | 134 us: 1.14x faster                                                                                                     |
| xml_etree_iterparse  | 69.7 ms                                                                                                              | 62.2 ms: 1.12x faster                                                                                                    |
| xml_etree_generate   | 59.0 ms                                                                                                              | 52.9 ms: 1.12x faster                                                                                                    |
| xml_etree_process    | 41.7 ms                                                                                                              | 38.0 ms: 1.10x faster                                                                                                    |
| json_dumps           | 6.34 ms                                                                                                              | 5.94 ms: 1.07x faster                                                                                                    |
| json_loads           | 14.3 us                                                                                                              | 14.4 us: 1.01x slower                                                                                                    |
| Geometric mean       | (ref)                                                                                                                | 1.11x faster                                                                                                             |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | results/bm-20240810-3.14.0a0-363374c/bm-20240810-pythonperf1-amd64-python-363374cf69a7e2292fe3-3.14.0a0-363374c.json | results/bm-20240810-3.14.0a0-363374c-JIT/bm-20240810-pythonperf1-amd64-python-363374cf69a7e2292fe3-3.14.0a0-363374c.json |
|------------------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| python_startup         | 21.9 ms                                                                                                              | 22.2 ms: 1.02x slower                                                                                                    |
| python_startup_no_site | 17.7 ms                                                                                                              | 18.4 ms: 1.04x slower                                                                                                    |
| Geometric mean         | (ref)                                                                                                                | 1.03x slower                                                                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20240810-3.14.0a0-363374c/bm-20240810-pythonperf1-amd64-python-363374cf69a7e2292fe3-3.14.0a0-363374c.json | results/bm-20240810-3.14.0a0-363374c-JIT/bm-20240810-pythonperf1-amd64-python-363374cf69a7e2292fe3-3.14.0a0-363374c.json |
|-----------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| mako            | 6.85 ms                                                                                                              | 5.08 ms: 1.35x faster                                                                                                    |
| genshi_text     | 17.7 ms                                                                                                              | 17.5 ms: 1.01x faster                                                                                                    |
| django_template | 24.8 ms                                                                                                              | 25.1 ms: 1.01x slower                                                                                                    |
| genshi_xml      | 36.6 ms                                                                                                              | 38.6 ms: 1.05x slower                                                                                                    |
| Geometric mean  | (ref)                                                                                                                | 1.06x faster                                                                                                             |

All benchmarks:
===============

| Benchmark                  | results/bm-20240810-3.14.0a0-363374c/bm-20240810-pythonperf1-amd64-python-363374cf69a7e2292fe3-3.14.0a0-363374c.json | results/bm-20240810-3.14.0a0-363374c-JIT/bm-20240810-pythonperf1-amd64-python-363374cf69a7e2292fe3-3.14.0a0-363374c.json |
|----------------------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| nbody                      | 84.9 ms                                                                                                              | 50.0 ms: 1.70x faster                                                                                                    |
| spectral_norm              | 73.0 ms                                                                                                              | 46.7 ms: 1.56x faster                                                                                                    |
| scimark_sor                | 93.1 ms                                                                                                              | 61.5 ms: 1.51x faster                                                                                                    |
| fannkuch                   | 297 ms                                                                                                               | 217 ms: 1.37x faster                                                                                                     |
| scimark_fft                | 203 ms                                                                                                               | 149 ms: 1.36x faster                                                                                                     |
| mako                       | 6.85 ms                                                                                                              | 5.08 ms: 1.35x faster                                                                                                    |
| scimark_monte_carlo        | 49.8 ms                                                                                                              | 37.7 ms: 1.32x faster                                                                                                    |
| scimark_sparse_mat_mult    | 2.81 ms                                                                                                              | 2.13 ms: 1.32x faster                                                                                                    |
| pyflate                    | 325 ms                                                                                                               | 248 ms: 1.31x faster                                                                                                     |
| crypto_pyaes               | 52.1 ms                                                                                                              | 40.0 ms: 1.31x faster                                                                                                    |
| deepcopy_memo              | 21.1 us                                                                                                              | 16.3 us: 1.29x faster                                                                                                    |
| tomli_loads                | 1.62 sec                                                                                                             | 1.27 sec: 1.27x faster                                                                                                   |
| float                      | 55.5 ms                                                                                                              | 44.3 ms: 1.25x faster                                                                                                    |
| pprint_safe_repr           | 575 ms                                                                                                               | 475 ms: 1.21x faster                                                                                                     |
| pprint_pformat             | 1.18 sec                                                                                                             | 975 ms: 1.21x faster                                                                                                     |
| comprehensions             | 12.1 us                                                                                                              | 10.2 us: 1.18x faster                                                                                                    |
| pickle_pure_python         | 215 us                                                                                                               | 182 us: 1.18x faster                                                                                                     |
| scimark_lu                 | 64.7 ms                                                                                                              | 55.3 ms: 1.17x faster                                                                                                    |
| logging_silent             | 64.7 ns                                                                                                              | 56.5 ns: 1.15x faster                                                                                                    |
| unpickle_pure_python       | 153 us                                                                                                               | 134 us: 1.14x faster                                                                                                     |
| chaos                      | 44.3 ms                                                                                                              | 39.3 ms: 1.13x faster                                                                                                    |
| xml_etree_iterparse        | 69.7 ms                                                                                                              | 62.2 ms: 1.12x faster                                                                                                    |
| asyncio_tcp_ssl            | 1.55 sec                                                                                                             | 1.39 sec: 1.12x faster                                                                                                   |
| xml_etree_generate         | 59.0 ms                                                                                                              | 52.9 ms: 1.12x faster                                                                                                    |
| xml_etree_process          | 41.7 ms                                                                                                              | 38.0 ms: 1.10x faster                                                                                                    |
| telco                      | 4.99 ms                                                                                                              | 4.59 ms: 1.09x faster                                                                                                    |
| richards                   | 33.7 ms                                                                                                              | 31.1 ms: 1.08x faster                                                                                                    |
| deepcopy_reduce            | 1.96 us                                                                                                              | 1.81 us: 1.08x faster                                                                                                    |
| meteor_contest             | 77.4 ms                                                                                                              | 71.7 ms: 1.08x faster                                                                                                    |
| richards_super             | 37.9 ms                                                                                                              | 35.2 ms: 1.08x faster                                                                                                    |
| json_dumps                 | 6.34 ms                                                                                                              | 5.94 ms: 1.07x faster                                                                                                    |
| logging_format             | 6.88 us                                                                                                              | 6.48 us: 1.06x faster                                                                                                    |
| logging_simple             | 6.37 us                                                                                                              | 6.01 us: 1.06x faster                                                                                                    |
| sqlglot_parse              | 878 us                                                                                                               | 828 us: 1.06x faster                                                                                                     |
| json                       | 3.32 ms                                                                                                              | 3.13 ms: 1.06x faster                                                                                                    |
| mdp                        | 1.53 sec                                                                                                             | 1.44 sec: 1.06x faster                                                                                                   |
| nqueens                    | 65.1 ms                                                                                                              | 61.6 ms: 1.06x faster                                                                                                    |
| async_tree_cpu_io_mixed_tg | 398 ms                                                                                                               | 381 ms: 1.04x faster                                                                                                     |
| deepcopy                   | 191 us                                                                                                               | 184 us: 1.04x faster                                                                                                     |
| sqlglot_normalize          | 198 ms                                                                                                               | 191 ms: 1.04x faster                                                                                                     |
| sqlglot_transpile          | 1.09 ms                                                                                                              | 1.06 ms: 1.03x faster                                                                                                    |
| coroutines                 | 14.2 ms                                                                                                              | 13.8 ms: 1.03x faster                                                                                                    |
| regex_compile              | 92.3 ms                                                                                                              | 90.0 ms: 1.03x faster                                                                                                    |
| thrift                     | 524 us                                                                                                               | 515 us: 1.02x faster                                                                                                     |
| typing_runtime_protocols   | 118 us                                                                                                               | 117 us: 1.01x faster                                                                                                     |
| coverage                   | 47.3 ms                                                                                                              | 46.8 ms: 1.01x faster                                                                                                    |
| genshi_text                | 17.7 ms                                                                                                              | 17.5 ms: 1.01x faster                                                                                                    |
| html5lib                   | 42.4 ms                                                                                                              | 42.0 ms: 1.01x faster                                                                                                    |
| generators                 | 21.4 ms                                                                                                              | 21.2 ms: 1.01x faster                                                                                                    |
| pidigits                   | 151 ms                                                                                                               | 150 ms: 1.01x faster                                                                                                     |
| dulwich_log                | 43.2 ms                                                                                                              | 42.9 ms: 1.01x faster                                                                                                    |
| sqlglot_optimize           | 36.6 ms                                                                                                              | 37.0 ms: 1.01x slower                                                                                                    |
| gc_traversal               | 1.57 ms                                                                                                              | 1.59 ms: 1.01x slower                                                                                                    |
| json_loads                 | 14.3 us                                                                                                              | 14.4 us: 1.01x slower                                                                                                    |
| tornado_http               | 94.9 ms                                                                                                              | 96.1 ms: 1.01x slower                                                                                                    |
| django_template            | 24.8 ms                                                                                                              | 25.1 ms: 1.01x slower                                                                                                    |
| python_startup             | 21.9 ms                                                                                                              | 22.2 ms: 1.02x slower                                                                                                    |
| deltablue                  | 2.29 ms                                                                                                              | 2.34 ms: 1.02x slower                                                                                                    |
| regex_effbot               | 1.59 ms                                                                                                              | 1.63 ms: 1.03x slower                                                                                                    |
| asyncio_tcp                | 535 ms                                                                                                               | 550 ms: 1.03x slower                                                                                                     |
| 2to3                       | 233 ms                                                                                                               | 240 ms: 1.03x slower                                                                                                     |
| hexiom                     | 4.59 ms                                                                                                              | 4.75 ms: 1.03x slower                                                                                                    |
| python_startup_no_site     | 17.7 ms                                                                                                              | 18.4 ms: 1.04x slower                                                                                                    |
| docutils                   | 1.78 sec                                                                                                             | 1.85 sec: 1.04x slower                                                                                                   |
| genshi_xml                 | 36.6 ms                                                                                                              | 38.6 ms: 1.05x slower                                                                                                    |
| bench_mp_pool              | 69.5 ms                                                                                                              | 73.4 ms: 1.06x slower                                                                                                    |
| regex_dna                  | 118 ms                                                                                                               | 124 ms: 1.06x slower                                                                                                     |
| async_generators           | 246 ms                                                                                                               | 260 ms: 1.06x slower                                                                                                     |
| sympy_str                  | 177 ms                                                                                                               | 188 ms: 1.06x slower                                                                                                     |
| sympy_sum                  | 88.9 ms                                                                                                              | 96.9 ms: 1.09x slower                                                                                                    |
| sympy_expand               | 299 ms                                                                                                               | 330 ms: 1.10x slower                                                                                                     |
| sympy_integrate            | 13.3 ms                                                                                                              | 14.7 ms: 1.11x slower                                                                                                    |
| pylint                     | 230 ms                                                                                                               | 255 ms: 1.11x slower                                                                                                     |
| Geometric mean             | (ref)                                                                                                                | 1.07x faster                                                                                                             |

Benchmark hidden because not significant (15): pycparser, async_tree_none, async_tree_io, async_tree_none_tg, async_tree_memoization, async_tree_io_tg, xml_etree_parse, async_tree_cpu_io_mixed, go, raytrace, pathlib, create_gc_cycles, regex_v8, async_tree_memoization_tg, bench_thread_pool

# HPT report

- Reliability score: 99.93% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown
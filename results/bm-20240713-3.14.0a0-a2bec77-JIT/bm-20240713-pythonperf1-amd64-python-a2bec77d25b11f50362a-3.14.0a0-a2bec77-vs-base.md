# Results vs. base

- fork: python
- ref: a2bec77d25b11f50362a
- machine: windows-amd64
- commit hash: a2bec77
- commit date: 2024-07-13
- overall geometric mean: 1.05x faster
- HPT reliability: 98.42%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20240713-3.14.0a0-a2bec77/bm-20240713-pythonperf1-amd64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77.json | results/bm-20240713-3.14.0a0-a2bec77-JIT/bm-20240713-pythonperf1-amd64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77.json |
|----------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 224 ms                                                                                                               | 233 ms: 1.04x slower                                                                                                     |
| docutils       | 1.68 sec                                                                                                             | 1.77 sec: 1.05x slower                                                                                                   |
| html5lib       | 40.3 ms                                                                                                              | 39.9 ms: 1.01x faster                                                                                                    |
| tornado_http   | 81.5 ms                                                                                                              | 84.3 ms: 1.04x slower                                                                                                    |
| Geometric mean | (ref)                                                                                                                | 1.03x slower                                                                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark       | results/bm-20240713-3.14.0a0-a2bec77/bm-20240713-pythonperf1-amd64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77.json | results/bm-20240713-3.14.0a0-a2bec77-JIT/bm-20240713-pythonperf1-amd64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77.json |
|-----------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| async_tree_none | 212 ms                                                                                                               | 205 ms: 1.03x faster                                                                                                     |
| Geometric mean  | (ref)                                                                                                                | 1.02x faster                                                                                                             |

Benchmark hidden because not significant (7): async_tree_none_tg, async_tree_io, async_tree_io_tg, async_tree_memoization, async_tree_memoization_tg, async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20240713-3.14.0a0-a2bec77/bm-20240713-pythonperf1-amd64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77.json | results/bm-20240713-3.14.0a0-a2bec77-JIT/bm-20240713-pythonperf1-amd64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77.json |
|----------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| nbody          | 78.5 ms                                                                                                              | 51.0 ms: 1.54x faster                                                                                                    |
| float          | 56.5 ms                                                                                                              | 45.1 ms: 1.25x faster                                                                                                    |
| pidigits       | 151 ms                                                                                                               | 149 ms: 1.01x faster                                                                                                     |
| Geometric mean | (ref)                                                                                                                | 1.25x faster                                                                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20240713-3.14.0a0-a2bec77/bm-20240713-pythonperf1-amd64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77.json | results/bm-20240713-3.14.0a0-a2bec77-JIT/bm-20240713-pythonperf1-amd64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77.json |
|----------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| regex_compile  | 89.0 ms                                                                                                              | 90.5 ms: 1.02x slower                                                                                                    |
| regex_dna      | 119 ms                                                                                                               | 121 ms: 1.02x slower                                                                                                     |
| regex_v8       | 15.3 ms                                                                                                              | 20.8 ms: 1.36x slower                                                                                                    |
| Geometric mean | (ref)                                                                                                                | 1.09x slower                                                                                                             |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20240713-3.14.0a0-a2bec77/bm-20240713-pythonperf1-amd64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77.json | results/bm-20240713-3.14.0a0-a2bec77-JIT/bm-20240713-pythonperf1-amd64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77.json |
|----------------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| tomli_loads          | 1.57 sec                                                                                                             | 1.25 sec: 1.25x faster                                                                                                   |
| pickle_pure_python   | 204 us                                                                                                               | 173 us: 1.18x faster                                                                                                     |
| unpickle_pure_python | 150 us                                                                                                               | 130 us: 1.15x faster                                                                                                     |
| xml_etree_generate   | 58.0 ms                                                                                                              | 52.8 ms: 1.10x faster                                                                                                    |
| xml_etree_iterparse  | 66.5 ms                                                                                                              | 60.7 ms: 1.10x faster                                                                                                    |
| xml_etree_process    | 40.6 ms                                                                                                              | 37.4 ms: 1.09x faster                                                                                                    |
| json_dumps           | 5.97 ms                                                                                                              | 5.86 ms: 1.02x faster                                                                                                    |
| json_loads           | 14.2 us                                                                                                              | 14.3 us: 1.01x slower                                                                                                    |
| Geometric mean       | (ref)                                                                                                                | 1.10x faster                                                                                                             |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup, python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20240713-3.14.0a0-a2bec77/bm-20240713-pythonperf1-amd64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77.json | results/bm-20240713-3.14.0a0-a2bec77-JIT/bm-20240713-pythonperf1-amd64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77.json |
|-----------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| mako            | 7.37 ms                                                                                                              | 5.16 ms: 1.43x faster                                                                                                    |
| django_template | 23.9 ms                                                                                                              | 25.6 ms: 1.07x slower                                                                                                    |
| genshi_text     | 16.4 ms                                                                                                              | 18.1 ms: 1.10x slower                                                                                                    |
| genshi_xml      | 37.2 ms                                                                                                              | 45.2 ms: 1.21x slower                                                                                                    |
| Geometric mean  | (ref)                                                                                                                | 1.00x slower                                                                                                             |

All benchmarks:
===============

| Benchmark                | results/bm-20240713-3.14.0a0-a2bec77/bm-20240713-pythonperf1-amd64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77.json | results/bm-20240713-3.14.0a0-a2bec77-JIT/bm-20240713-pythonperf1-amd64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77.json |
|--------------------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| spectral_norm            | 72.4 ms                                                                                                              | 45.5 ms: 1.59x faster                                                                                                    |
| nbody                    | 78.5 ms                                                                                                              | 51.0 ms: 1.54x faster                                                                                                    |
| scimark_fft              | 216 ms                                                                                                               | 151 ms: 1.43x faster                                                                                                     |
| mako                     | 7.37 ms                                                                                                              | 5.16 ms: 1.43x faster                                                                                                    |
| scimark_monte_carlo      | 52.0 ms                                                                                                              | 37.6 ms: 1.38x faster                                                                                                    |
| scimark_sparse_mat_mult  | 2.93 ms                                                                                                              | 2.12 ms: 1.38x faster                                                                                                    |
| fannkuch                 | 304 ms                                                                                                               | 221 ms: 1.37x faster                                                                                                     |
| deepcopy_memo            | 20.8 us                                                                                                              | 15.8 us: 1.31x faster                                                                                                    |
| crypto_pyaes             | 52.0 ms                                                                                                              | 40.7 ms: 1.28x faster                                                                                                    |
| float                    | 56.5 ms                                                                                                              | 45.1 ms: 1.25x faster                                                                                                    |
| tomli_loads              | 1.57 sec                                                                                                             | 1.25 sec: 1.25x faster                                                                                                   |
| pyflate                  | 309 ms                                                                                                               | 258 ms: 1.20x faster                                                                                                     |
| pickle_pure_python       | 204 us                                                                                                               | 173 us: 1.18x faster                                                                                                     |
| pprint_safe_repr         | 546 ms                                                                                                               | 464 ms: 1.18x faster                                                                                                     |
| pprint_pformat           | 1.10 sec                                                                                                             | 953 ms: 1.16x faster                                                                                                     |
| unpickle_pure_python     | 150 us                                                                                                               | 130 us: 1.15x faster                                                                                                     |
| chaos                    | 44.0 ms                                                                                                              | 38.8 ms: 1.14x faster                                                                                                    |
| comprehensions           | 11.6 us                                                                                                              | 10.4 us: 1.12x faster                                                                                                    |
| logging_silent           | 63.5 ns                                                                                                              | 56.8 ns: 1.12x faster                                                                                                    |
| xml_etree_generate       | 58.0 ms                                                                                                              | 52.8 ms: 1.10x faster                                                                                                    |
| xml_etree_iterparse      | 66.5 ms                                                                                                              | 60.7 ms: 1.10x faster                                                                                                    |
| sqlglot_parse            | 878 us                                                                                                               | 804 us: 1.09x faster                                                                                                     |
| xml_etree_process        | 40.6 ms                                                                                                              | 37.4 ms: 1.09x faster                                                                                                    |
| asyncio_tcp_ssl          | 1.56 sec                                                                                                             | 1.44 sec: 1.09x faster                                                                                                   |
| telco                    | 4.86 ms                                                                                                              | 4.48 ms: 1.08x faster                                                                                                    |
| logging_simple           | 6.21 us                                                                                                              | 5.74 us: 1.08x faster                                                                                                    |
| mdp                      | 1.53 sec                                                                                                             | 1.42 sec: 1.07x faster                                                                                                   |
| logging_format           | 6.60 us                                                                                                              | 6.19 us: 1.07x faster                                                                                                    |
| sqlglot_transpile        | 1.08 ms                                                                                                              | 1.03 ms: 1.05x faster                                                                                                    |
| nqueens                  | 62.9 ms                                                                                                              | 59.9 ms: 1.05x faster                                                                                                    |
| deepcopy_reduce          | 1.86 us                                                                                                              | 1.79 us: 1.04x faster                                                                                                    |
| async_tree_none          | 212 ms                                                                                                               | 205 ms: 1.03x faster                                                                                                     |
| go                       | 97.0 ms                                                                                                              | 94.2 ms: 1.03x faster                                                                                                    |
| meteor_contest           | 75.7 ms                                                                                                              | 73.6 ms: 1.03x faster                                                                                                    |
| scimark_sor              | 90.7 ms                                                                                                              | 88.9 ms: 1.02x faster                                                                                                    |
| json_dumps               | 5.97 ms                                                                                                              | 5.86 ms: 1.02x faster                                                                                                    |
| richards_super           | 34.6 ms                                                                                                              | 34.0 ms: 1.02x faster                                                                                                    |
| raytrace                 | 181 ms                                                                                                               | 179 ms: 1.01x faster                                                                                                     |
| html5lib                 | 40.3 ms                                                                                                              | 39.9 ms: 1.01x faster                                                                                                    |
| pidigits                 | 151 ms                                                                                                               | 149 ms: 1.01x faster                                                                                                     |
| thrift                   | 522 us                                                                                                               | 519 us: 1.01x faster                                                                                                     |
| json_loads               | 14.2 us                                                                                                              | 14.3 us: 1.01x slower                                                                                                    |
| gc_traversal             | 1.54 ms                                                                                                              | 1.55 ms: 1.01x slower                                                                                                    |
| pathlib                  | 74.1 ms                                                                                                              | 74.6 ms: 1.01x slower                                                                                                    |
| coroutines               | 13.7 ms                                                                                                              | 13.8 ms: 1.01x slower                                                                                                    |
| bench_thread_pool        | 793 us                                                                                                               | 804 us: 1.01x slower                                                                                                     |
| regex_compile            | 89.0 ms                                                                                                              | 90.5 ms: 1.02x slower                                                                                                    |
| deltablue                | 2.21 ms                                                                                                              | 2.25 ms: 1.02x slower                                                                                                    |
| regex_dna                | 119 ms                                                                                                               | 121 ms: 1.02x slower                                                                                                     |
| sqlglot_normalize        | 185 ms                                                                                                               | 190 ms: 1.02x slower                                                                                                     |
| hexiom                   | 4.51 ms                                                                                                              | 4.62 ms: 1.02x slower                                                                                                    |
| sqlglot_optimize         | 34.7 ms                                                                                                              | 35.6 ms: 1.03x slower                                                                                                    |
| tornado_http             | 81.5 ms                                                                                                              | 84.3 ms: 1.04x slower                                                                                                    |
| 2to3                     | 224 ms                                                                                                               | 233 ms: 1.04x slower                                                                                                     |
| json                     | 2.95 ms                                                                                                              | 3.07 ms: 1.04x slower                                                                                                    |
| sympy_str                | 173 ms                                                                                                               | 181 ms: 1.04x slower                                                                                                     |
| sympy_sum                | 88.6 ms                                                                                                              | 92.9 ms: 1.05x slower                                                                                                    |
| docutils                 | 1.68 sec                                                                                                             | 1.77 sec: 1.05x slower                                                                                                   |
| async_generators         | 243 ms                                                                                                               | 257 ms: 1.06x slower                                                                                                     |
| sympy_expand             | 296 ms                                                                                                               | 313 ms: 1.06x slower                                                                                                     |
| generators               | 22.2 ms                                                                                                              | 23.6 ms: 1.06x slower                                                                                                    |
| scimark_lu               | 66.2 ms                                                                                                              | 70.3 ms: 1.06x slower                                                                                                    |
| typing_runtime_protocols | 106 us                                                                                                               | 113 us: 1.06x slower                                                                                                     |
| bench_mp_pool            | 65.2 ms                                                                                                              | 69.6 ms: 1.07x slower                                                                                                    |
| django_template          | 23.9 ms                                                                                                              | 25.6 ms: 1.07x slower                                                                                                    |
| sympy_integrate          | 13.0 ms                                                                                                              | 14.0 ms: 1.08x slower                                                                                                    |
| genshi_text              | 16.4 ms                                                                                                              | 18.1 ms: 1.10x slower                                                                                                    |
| pylint                   | 209 ms                                                                                                               | 231 ms: 1.10x slower                                                                                                     |
| genshi_xml               | 37.2 ms                                                                                                              | 45.2 ms: 1.21x slower                                                                                                    |
| regex_v8                 | 15.3 ms                                                                                                              | 20.8 ms: 1.36x slower                                                                                                    |
| Geometric mean           | (ref)                                                                                                                | 1.05x faster                                                                                                             |

Benchmark hidden because not significant (17): async_tree_none_tg, async_tree_io, asyncio_tcp, async_tree_io_tg, async_tree_memoization, async_tree_memoization_tg, async_tree_cpu_io_mixed_tg, xml_etree_parse, richards, deepcopy, coverage, regex_effbot, python_startup, python_startup_no_site, async_tree_cpu_io_mixed, create_gc_cycles, pycparser

# HPT report

- Reliability score: 98.42% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown
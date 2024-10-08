# Results vs. base

- fork: python
- ref: 34ddb64d088dd7ccc321
- machine: windows-amd64
- commit hash: 34ddb64
- commit date: 2024-08-31
- overall geometric mean: 1.03x faster
- HPT reliability: 60.11%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20240831-3.14.0a0-34ddb64/bm-20240831-pythonperf1-amd64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64.json | results/bm-20240831-3.14.0a0-34ddb64-JIT/bm-20240831-pythonperf1-amd64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64.json |
|----------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 226 ms                                                                                                               | 243 ms: 1.07x slower                                                                                                     |
| docutils       | 1.69 sec                                                                                                             | 1.94 sec: 1.15x slower                                                                                                   |
| html5lib       | 40.7 ms                                                                                                              | 42.8 ms: 1.05x slower                                                                                                    |
| tornado_http   | 93.8 ms                                                                                                              | 99.1 ms: 1.06x slower                                                                                                    |
| Geometric mean | (ref)                                                                                                                | 1.08x slower                                                                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | results/bm-20240831-3.14.0a0-34ddb64/bm-20240831-pythonperf1-amd64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64.json | results/bm-20240831-3.14.0a0-34ddb64-JIT/bm-20240831-pythonperf1-amd64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64.json |
|----------------------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed_tg | 399 ms                                                                                                               | 384 ms: 1.04x faster                                                                                                     |
| async_tree_memoization     | 260 ms                                                                                                               | 251 ms: 1.03x faster                                                                                                     |
| coroutines                 | 14.1 ms                                                                                                              | 13.8 ms: 1.02x faster                                                                                                    |
| asyncio_tcp                | 512 ms                                                                                                               | 530 ms: 1.04x slower                                                                                                     |
| async_generators           | 249 ms                                                                                                               | 261 ms: 1.05x slower                                                                                                     |
| Geometric mean             | (ref)                                                                                                                | 1.00x faster                                                                                                             |

Benchmark hidden because not significant (7): asyncio_tcp_ssl, async_tree_none_tg, async_tree_none, async_tree_io_tg, async_tree_cpu_io_mixed, async_tree_io, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20240831-3.14.0a0-34ddb64/bm-20240831-pythonperf1-amd64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64.json | results/bm-20240831-3.14.0a0-34ddb64-JIT/bm-20240831-pythonperf1-amd64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64.json |
|----------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| nbody          | 83.6 ms                                                                                                              | 50.0 ms: 1.67x faster                                                                                                    |
| float          | 56.2 ms                                                                                                              | 45.3 ms: 1.24x faster                                                                                                    |
| pidigits       | 152 ms                                                                                                               | 149 ms: 1.02x faster                                                                                                     |
| Geometric mean | (ref)                                                                                                                | 1.28x faster                                                                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20240831-3.14.0a0-34ddb64/bm-20240831-pythonperf1-amd64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64.json | results/bm-20240831-3.14.0a0-34ddb64-JIT/bm-20240831-pythonperf1-amd64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64.json |
|----------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| regex_compile  | 91.5 ms                                                                                                              | 95.6 ms: 1.05x slower                                                                                                    |
| regex_effbot   | 1.54 ms                                                                                                              | 1.62 ms: 1.05x slower                                                                                                    |
| regex_dna      | 116 ms                                                                                                               | 124 ms: 1.07x slower                                                                                                     |
| Geometric mean | (ref)                                                                                                                | 1.03x slower                                                                                                             |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20240831-3.14.0a0-34ddb64/bm-20240831-pythonperf1-amd64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64.json | results/bm-20240831-3.14.0a0-34ddb64-JIT/bm-20240831-pythonperf1-amd64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64.json |
|----------------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| tomli_loads          | 1.59 sec                                                                                                             | 1.27 sec: 1.25x faster                                                                                                   |
| xml_etree_generate   | 57.7 ms                                                                                                              | 50.5 ms: 1.14x faster                                                                                                    |
| xml_etree_process    | 40.9 ms                                                                                                              | 35.8 ms: 1.14x faster                                                                                                    |
| json_dumps           | 6.24 ms                                                                                                              | 5.78 ms: 1.08x faster                                                                                                    |
| pickle_pure_python   | 208 us                                                                                                               | 195 us: 1.07x faster                                                                                                     |
| xml_etree_iterparse  | 65.0 ms                                                                                                              | 61.7 ms: 1.05x faster                                                                                                    |
| unpickle_pure_python | 149 us                                                                                                               | 145 us: 1.03x faster                                                                                                     |
| xml_etree_parse      | 95.6 ms                                                                                                              | 94.0 ms: 1.02x faster                                                                                                    |
| json_loads           | 14.4 us                                                                                                              | 14.3 us: 1.00x faster                                                                                                    |
| Geometric mean       | (ref)                                                                                                                | 1.08x faster                                                                                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark              | results/bm-20240831-3.14.0a0-34ddb64/bm-20240831-pythonperf1-amd64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64.json | results/bm-20240831-3.14.0a0-34ddb64-JIT/bm-20240831-pythonperf1-amd64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64.json |
|------------------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| python_startup_no_site | 18.0 ms                                                                                                              | 18.6 ms: 1.03x slower                                                                                                    |
| Geometric mean         | (ref)                                                                                                                | 1.02x slower                                                                                                             |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20240831-3.14.0a0-34ddb64/bm-20240831-pythonperf1-amd64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64.json | results/bm-20240831-3.14.0a0-34ddb64-JIT/bm-20240831-pythonperf1-amd64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64.json |
|-----------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| mako            | 6.87 ms                                                                                                              | 5.26 ms: 1.31x faster                                                                                                    |
| django_template | 24.2 ms                                                                                                              | 26.8 ms: 1.11x slower                                                                                                    |
| genshi_text     | 16.5 ms                                                                                                              | 19.7 ms: 1.19x slower                                                                                                    |
| genshi_xml      | 36.3 ms                                                                                                              | 46.3 ms: 1.28x slower                                                                                                    |
| Geometric mean  | (ref)                                                                                                                | 1.07x slower                                                                                                             |

All benchmarks:
===============

| Benchmark                  | results/bm-20240831-3.14.0a0-34ddb64/bm-20240831-pythonperf1-amd64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64.json | results/bm-20240831-3.14.0a0-34ddb64-JIT/bm-20240831-pythonperf1-amd64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64.json |
|----------------------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| nbody                      | 83.6 ms                                                                                                              | 50.0 ms: 1.67x faster                                                                                                    |
| spectral_norm              | 67.4 ms                                                                                                              | 44.1 ms: 1.53x faster                                                                                                    |
| scimark_sor                | 88.7 ms                                                                                                              | 60.5 ms: 1.46x faster                                                                                                    |
| scimark_fft                | 195 ms                                                                                                               | 149 ms: 1.31x faster                                                                                                     |
| mako                       | 6.87 ms                                                                                                              | 5.26 ms: 1.31x faster                                                                                                    |
| deepcopy_memo              | 19.5 us                                                                                                              | 15.0 us: 1.30x faster                                                                                                    |
| crypto_pyaes               | 47.8 ms                                                                                                              | 38.2 ms: 1.25x faster                                                                                                    |
| tomli_loads                | 1.59 sec                                                                                                             | 1.27 sec: 1.25x faster                                                                                                   |
| float                      | 56.2 ms                                                                                                              | 45.3 ms: 1.24x faster                                                                                                    |
| deltablue                  | 2.25 ms                                                                                                              | 1.82 ms: 1.24x faster                                                                                                    |
| pyflate                    | 322 ms                                                                                                               | 262 ms: 1.23x faster                                                                                                     |
| fannkuch                   | 291 ms                                                                                                               | 239 ms: 1.22x faster                                                                                                     |
| scimark_sparse_mat_mult    | 2.66 ms                                                                                                              | 2.18 ms: 1.22x faster                                                                                                    |
| scimark_lu                 | 62.3 ms                                                                                                              | 54.0 ms: 1.15x faster                                                                                                    |
| xml_etree_generate         | 57.7 ms                                                                                                              | 50.5 ms: 1.14x faster                                                                                                    |
| xml_etree_process          | 40.9 ms                                                                                                              | 35.8 ms: 1.14x faster                                                                                                    |
| scimark_monte_carlo        | 49.1 ms                                                                                                              | 43.5 ms: 1.13x faster                                                                                                    |
| telco                      | 5.09 ms                                                                                                              | 4.58 ms: 1.11x faster                                                                                                    |
| comprehensions             | 11.8 us                                                                                                              | 10.8 us: 1.10x faster                                                                                                    |
| pprint_safe_repr           | 555 ms                                                                                                               | 507 ms: 1.10x faster                                                                                                     |
| logging_silent             | 62.5 ns                                                                                                              | 57.3 ns: 1.09x faster                                                                                                    |
| json_dumps                 | 6.24 ms                                                                                                              | 5.78 ms: 1.08x faster                                                                                                    |
| pickle_pure_python         | 208 us                                                                                                               | 195 us: 1.07x faster                                                                                                     |
| json                       | 3.12 ms                                                                                                              | 2.93 ms: 1.06x faster                                                                                                    |
| nqueens                    | 65.2 ms                                                                                                              | 61.4 ms: 1.06x faster                                                                                                    |
| pprint_pformat             | 1.11 sec                                                                                                             | 1.05 sec: 1.06x faster                                                                                                   |
| xml_etree_iterparse        | 65.0 ms                                                                                                              | 61.7 ms: 1.05x faster                                                                                                    |
| deepcopy_reduce            | 1.90 us                                                                                                              | 1.81 us: 1.05x faster                                                                                                    |
| meteor_contest             | 78.3 ms                                                                                                              | 74.6 ms: 1.05x faster                                                                                                    |
| chaos                      | 42.7 ms                                                                                                              | 40.7 ms: 1.05x faster                                                                                                    |
| async_tree_cpu_io_mixed_tg | 399 ms                                                                                                               | 384 ms: 1.04x faster                                                                                                     |
| coverage                   | 49.3 ms                                                                                                              | 47.6 ms: 1.04x faster                                                                                                    |
| logging_simple             | 6.25 us                                                                                                              | 6.05 us: 1.03x faster                                                                                                    |
| async_tree_memoization     | 260 ms                                                                                                               | 251 ms: 1.03x faster                                                                                                     |
| typing_runtime_protocols   | 115 us                                                                                                               | 111 us: 1.03x faster                                                                                                     |
| unpickle_pure_python       | 149 us                                                                                                               | 145 us: 1.03x faster                                                                                                     |
| deepcopy                   | 186 us                                                                                                               | 183 us: 1.02x faster                                                                                                     |
| coroutines                 | 14.1 ms                                                                                                              | 13.8 ms: 1.02x faster                                                                                                    |
| pidigits                   | 152 ms                                                                                                               | 149 ms: 1.02x faster                                                                                                     |
| xml_etree_parse            | 95.6 ms                                                                                                              | 94.0 ms: 1.02x faster                                                                                                    |
| logging_format             | 6.63 us                                                                                                              | 6.56 us: 1.01x faster                                                                                                    |
| dulwich_log                | 44.4 ms                                                                                                              | 44.0 ms: 1.01x faster                                                                                                    |
| json_loads                 | 14.4 us                                                                                                              | 14.3 us: 1.00x faster                                                                                                    |
| sqlglot_parse              | 891 us                                                                                                               | 901 us: 1.01x slower                                                                                                     |
| mdp                        | 1.43 sec                                                                                                             | 1.46 sec: 1.02x slower                                                                                                   |
| create_gc_cycles           | 917 us                                                                                                               | 933 us: 1.02x slower                                                                                                     |
| gc_traversal               | 1.55 ms                                                                                                              | 1.58 ms: 1.02x slower                                                                                                    |
| python_startup_no_site     | 18.0 ms                                                                                                              | 18.6 ms: 1.03x slower                                                                                                    |
| asyncio_tcp                | 512 ms                                                                                                               | 530 ms: 1.04x slower                                                                                                     |
| regex_compile              | 91.5 ms                                                                                                              | 95.6 ms: 1.05x slower                                                                                                    |
| regex_effbot               | 1.54 ms                                                                                                              | 1.62 ms: 1.05x slower                                                                                                    |
| html5lib                   | 40.7 ms                                                                                                              | 42.8 ms: 1.05x slower                                                                                                    |
| async_generators           | 249 ms                                                                                                               | 261 ms: 1.05x slower                                                                                                     |
| raytrace                   | 188 ms                                                                                                               | 198 ms: 1.05x slower                                                                                                     |
| tornado_http               | 93.8 ms                                                                                                              | 99.1 ms: 1.06x slower                                                                                                    |
| generators                 | 20.6 ms                                                                                                              | 21.7 ms: 1.06x slower                                                                                                    |
| sqlglot_transpile          | 1.11 ms                                                                                                              | 1.17 ms: 1.06x slower                                                                                                    |
| sqlglot_normalize          | 191 ms                                                                                                               | 203 ms: 1.06x slower                                                                                                     |
| regex_dna                  | 116 ms                                                                                                               | 124 ms: 1.07x slower                                                                                                     |
| sympy_expand               | 307 ms                                                                                                               | 329 ms: 1.07x slower                                                                                                     |
| sympy_str                  | 177 ms                                                                                                               | 190 ms: 1.07x slower                                                                                                     |
| 2to3                       | 226 ms                                                                                                               | 243 ms: 1.07x slower                                                                                                     |
| bench_mp_pool              | 68.7 ms                                                                                                              | 74.4 ms: 1.08x slower                                                                                                    |
| richards_super             | 36.2 ms                                                                                                              | 39.3 ms: 1.08x slower                                                                                                    |
| go                         | 84.7 ms                                                                                                              | 92.0 ms: 1.09x slower                                                                                                    |
| sqlglot_optimize           | 36.3 ms                                                                                                              | 40.0 ms: 1.10x slower                                                                                                    |
| sympy_sum                  | 90.1 ms                                                                                                              | 99.3 ms: 1.10x slower                                                                                                    |
| django_template            | 24.2 ms                                                                                                              | 26.8 ms: 1.11x slower                                                                                                    |
| richards                   | 32.4 ms                                                                                                              | 36.0 ms: 1.11x slower                                                                                                    |
| hexiom                     | 4.32 ms                                                                                                              | 4.87 ms: 1.13x slower                                                                                                    |
| sympy_integrate            | 13.1 ms                                                                                                              | 15.0 ms: 1.14x slower                                                                                                    |
| docutils                   | 1.69 sec                                                                                                             | 1.94 sec: 1.15x slower                                                                                                   |
| pylint                     | 228 ms                                                                                                               | 269 ms: 1.18x slower                                                                                                     |
| genshi_text                | 16.5 ms                                                                                                              | 19.7 ms: 1.19x slower                                                                                                    |
| genshi_xml                 | 36.3 ms                                                                                                              | 46.3 ms: 1.28x slower                                                                                                    |
| Geometric mean             | (ref)                                                                                                                | 1.03x faster                                                                                                             |

Benchmark hidden because not significant (13): asyncio_tcp_ssl, regex_v8, async_tree_none_tg, async_tree_none, pycparser, thrift, async_tree_io_tg, bench_thread_pool, pathlib, python_startup, async_tree_cpu_io_mixed, async_tree_io, async_tree_memoization_tg

# HPT report

- Reliability score: 60.11% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown
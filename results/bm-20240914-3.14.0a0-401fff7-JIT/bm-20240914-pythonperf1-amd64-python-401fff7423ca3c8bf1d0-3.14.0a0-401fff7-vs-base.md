# Results vs. base

- fork: python
- ref: 401fff7423ca3c8bf1d0
- machine: windows-amd64
- commit hash: 401fff7
- commit date: 2024-09-14
- overall geometric mean: 1.05x faster
- HPT reliability: 91.18%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20240914-3.14.0a0-401fff7/bm-20240914-pythonperf1-amd64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7.json | results/bm-20240914-3.14.0a0-401fff7-JIT/bm-20240914-pythonperf1-amd64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7.json |
|----------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 225 ms                                                                                                               | 239 ms: 1.06x slower                                                                                                     |
| docutils       | 1.70 sec                                                                                                             | 1.91 sec: 1.13x slower                                                                                                   |
| html5lib       | 40.6 ms                                                                                                              | 42.1 ms: 1.04x slower                                                                                                    |
| tornado_http   | 83.5 ms                                                                                                              | 87.4 ms: 1.05x slower                                                                                                    |
| Geometric mean | (ref)                                                                                                                | 1.07x slower                                                                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | results/bm-20240914-3.14.0a0-401fff7/bm-20240914-pythonperf1-amd64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7.json | results/bm-20240914-3.14.0a0-401fff7-JIT/bm-20240914-pythonperf1-amd64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7.json |
|----------------------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| asyncio_tcp_ssl            | 1.61 sec                                                                                                             | 1.39 sec: 1.16x faster                                                                                                   |
| coroutines                 | 14.4 ms                                                                                                              | 13.8 ms: 1.04x faster                                                                                                    |
| async_tree_none            | 211 ms                                                                                                               | 206 ms: 1.02x faster                                                                                                     |
| async_tree_memoization     | 263 ms                                                                                                               | 258 ms: 1.02x faster                                                                                                     |
| async_tree_cpu_io_mixed_tg | 393 ms                                                                                                               | 397 ms: 1.01x slower                                                                                                     |
| async_tree_cpu_io_mixed    | 386 ms                                                                                                               | 394 ms: 1.02x slower                                                                                                     |
| async_generators           | 243 ms                                                                                                               | 260 ms: 1.07x slower                                                                                                     |
| Geometric mean             | (ref)                                                                                                                | 1.01x faster                                                                                                             |

Benchmark hidden because not significant (5): async_tree_none_tg, async_tree_io_tg, asyncio_tcp, async_tree_io, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20240914-3.14.0a0-401fff7/bm-20240914-pythonperf1-amd64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7.json | results/bm-20240914-3.14.0a0-401fff7-JIT/bm-20240914-pythonperf1-amd64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7.json |
|----------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| nbody          | 83.3 ms                                                                                                              | 49.4 ms: 1.69x faster                                                                                                    |
| float          | 55.9 ms                                                                                                              | 44.5 ms: 1.26x faster                                                                                                    |
| pidigits       | 150 ms                                                                                                               | 149 ms: 1.01x faster                                                                                                     |
| Geometric mean | (ref)                                                                                                                | 1.29x faster                                                                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20240914-3.14.0a0-401fff7/bm-20240914-pythonperf1-amd64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7.json | results/bm-20240914-3.14.0a0-401fff7-JIT/bm-20240914-pythonperf1-amd64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7.json |
|----------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| regex_dna      | 124 ms                                                                                                               | 121 ms: 1.02x faster                                                                                                     |
| regex_v8       | 15.2 ms                                                                                                              | 14.9 ms: 1.02x faster                                                                                                    |
| regex_effbot   | 1.61 ms                                                                                                              | 1.59 ms: 1.01x faster                                                                                                    |
| regex_compile  | 92.3 ms                                                                                                              | 94.2 ms: 1.02x slower                                                                                                    |
| Geometric mean | (ref)                                                                                                                | 1.01x faster                                                                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20240914-3.14.0a0-401fff7/bm-20240914-pythonperf1-amd64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7.json | results/bm-20240914-3.14.0a0-401fff7-JIT/bm-20240914-pythonperf1-amd64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7.json |
|----------------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| tomli_loads          | 1.63 sec                                                                                                             | 1.26 sec: 1.29x faster                                                                                                   |
| xml_etree_generate   | 59.0 ms                                                                                                              | 49.0 ms: 1.20x faster                                                                                                    |
| xml_etree_process    | 41.5 ms                                                                                                              | 34.8 ms: 1.19x faster                                                                                                    |
| pickle_pure_python   | 216 us                                                                                                               | 196 us: 1.10x faster                                                                                                     |
| json_dumps           | 6.23 ms                                                                                                              | 5.73 ms: 1.09x faster                                                                                                    |
| unpickle_pure_python | 157 us                                                                                                               | 145 us: 1.09x faster                                                                                                     |
| xml_etree_iterparse  | 65.2 ms                                                                                                              | 60.7 ms: 1.07x faster                                                                                                    |
| pickle_list          | 2.88 us                                                                                                              | 2.78 us: 1.03x faster                                                                                                    |
| pickle_dict          | 18.5 us                                                                                                              | 17.9 us: 1.03x faster                                                                                                    |
| xml_etree_parse      | 93.2 ms                                                                                                              | 92.4 ms: 1.01x faster                                                                                                    |
| unpickle_list        | 2.77 us                                                                                                              | 2.87 us: 1.03x slower                                                                                                    |
| pickle               | 6.99 us                                                                                                              | 7.38 us: 1.06x slower                                                                                                    |
| Geometric mean       | (ref)                                                                                                                | 1.07x faster                                                                                                             |

Benchmark hidden because not significant (2): json_loads, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark      | results/bm-20240914-3.14.0a0-401fff7/bm-20240914-pythonperf1-amd64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7.json | results/bm-20240914-3.14.0a0-401fff7-JIT/bm-20240914-pythonperf1-amd64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7.json |
|----------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| python_startup | 22.0 ms                                                                                                              | 21.6 ms: 1.02x faster                                                                                                    |
| Geometric mean | (ref)                                                                                                                | 1.01x faster                                                                                                             |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20240914-3.14.0a0-401fff7/bm-20240914-pythonperf1-amd64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7.json | results/bm-20240914-3.14.0a0-401fff7-JIT/bm-20240914-pythonperf1-amd64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7.json |
|-----------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| mako            | 6.82 ms                                                                                                              | 5.26 ms: 1.30x faster                                                                                                    |
| django_template | 26.0 ms                                                                                                              | 26.2 ms: 1.01x slower                                                                                                    |
| genshi_text     | 17.1 ms                                                                                                              | 18.9 ms: 1.10x slower                                                                                                    |
| genshi_xml      | 36.8 ms                                                                                                              | 45.7 ms: 1.24x slower                                                                                                    |
| Geometric mean  | (ref)                                                                                                                | 1.02x slower                                                                                                             |

All benchmarks:
===============

| Benchmark                  | results/bm-20240914-3.14.0a0-401fff7/bm-20240914-pythonperf1-amd64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7.json | results/bm-20240914-3.14.0a0-401fff7-JIT/bm-20240914-pythonperf1-amd64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7.json |
|----------------------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| spectral_norm              | 73.6 ms                                                                                                              | 43.3 ms: 1.70x faster                                                                                                    |
| nbody                      | 83.3 ms                                                                                                              | 49.4 ms: 1.69x faster                                                                                                    |
| scimark_sor                | 93.9 ms                                                                                                              | 60.7 ms: 1.55x faster                                                                                                    |
| deepcopy_memo              | 21.0 us                                                                                                              | 14.8 us: 1.41x faster                                                                                                    |
| scimark_fft                | 206 ms                                                                                                               | 149 ms: 1.38x faster                                                                                                     |
| scimark_sparse_mat_mult    | 2.79 ms                                                                                                              | 2.13 ms: 1.31x faster                                                                                                    |
| mako                       | 6.82 ms                                                                                                              | 5.26 ms: 1.30x faster                                                                                                    |
| tomli_loads                | 1.63 sec                                                                                                             | 1.26 sec: 1.29x faster                                                                                                   |
| deltablue                  | 2.29 ms                                                                                                              | 1.82 ms: 1.26x faster                                                                                                    |
| float                      | 55.9 ms                                                                                                              | 44.5 ms: 1.26x faster                                                                                                    |
| crypto_pyaes               | 47.9 ms                                                                                                              | 38.6 ms: 1.24x faster                                                                                                    |
| pyflate                    | 326 ms                                                                                                               | 265 ms: 1.23x faster                                                                                                     |
| fannkuch                   | 302 ms                                                                                                               | 248 ms: 1.22x faster                                                                                                     |
| xml_etree_generate         | 59.0 ms                                                                                                              | 49.0 ms: 1.20x faster                                                                                                    |
| xml_etree_process          | 41.5 ms                                                                                                              | 34.8 ms: 1.19x faster                                                                                                    |
| scimark_monte_carlo        | 50.2 ms                                                                                                              | 42.7 ms: 1.18x faster                                                                                                    |
| asyncio_tcp_ssl            | 1.61 sec                                                                                                             | 1.39 sec: 1.16x faster                                                                                                   |
| scimark_lu                 | 62.9 ms                                                                                                              | 54.4 ms: 1.16x faster                                                                                                    |
| pycparser                  | 826 ms                                                                                                               | 715 ms: 1.16x faster                                                                                                     |
| comprehensions             | 12.2 us                                                                                                              | 10.7 us: 1.14x faster                                                                                                    |
| logging_silent             | 64.8 ns                                                                                                              | 57.2 ns: 1.13x faster                                                                                                    |
| pickle_pure_python         | 216 us                                                                                                               | 196 us: 1.10x faster                                                                                                     |
| chaos                      | 44.0 ms                                                                                                              | 40.0 ms: 1.10x faster                                                                                                    |
| pprint_pformat             | 1.13 sec                                                                                                             | 1.03 sec: 1.10x faster                                                                                                   |
| pprint_safe_repr           | 551 ms                                                                                                               | 503 ms: 1.10x faster                                                                                                     |
| telco                      | 5.01 ms                                                                                                              | 4.60 ms: 1.09x faster                                                                                                    |
| json_dumps                 | 6.23 ms                                                                                                              | 5.73 ms: 1.09x faster                                                                                                    |
| unpickle_pure_python       | 157 us                                                                                                               | 145 us: 1.09x faster                                                                                                     |
| nqueens                    | 64.5 ms                                                                                                              | 59.6 ms: 1.08x faster                                                                                                    |
| deepcopy_reduce            | 1.93 us                                                                                                              | 1.79 us: 1.08x faster                                                                                                    |
| xml_etree_iterparse        | 65.2 ms                                                                                                              | 60.7 ms: 1.07x faster                                                                                                    |
| logging_format             | 6.90 us                                                                                                              | 6.45 us: 1.07x faster                                                                                                    |
| mdp                        | 1.53 sec                                                                                                             | 1.43 sec: 1.07x faster                                                                                                   |
| logging_simple             | 6.31 us                                                                                                              | 6.06 us: 1.04x faster                                                                                                    |
| meteor_contest             | 78.0 ms                                                                                                              | 74.9 ms: 1.04x faster                                                                                                    |
| deepcopy                   | 188 us                                                                                                               | 181 us: 1.04x faster                                                                                                     |
| coroutines                 | 14.4 ms                                                                                                              | 13.8 ms: 1.04x faster                                                                                                    |
| typing_runtime_protocols   | 115 us                                                                                                               | 111 us: 1.04x faster                                                                                                     |
| pickle_list                | 2.88 us                                                                                                              | 2.78 us: 1.03x faster                                                                                                    |
| pickle_dict                | 18.5 us                                                                                                              | 17.9 us: 1.03x faster                                                                                                    |
| regex_dna                  | 124 ms                                                                                                               | 121 ms: 1.02x faster                                                                                                     |
| async_tree_none            | 211 ms                                                                                                               | 206 ms: 1.02x faster                                                                                                     |
| sqlite_synth               | 1.63 us                                                                                                              | 1.60 us: 1.02x faster                                                                                                    |
| python_startup             | 22.0 ms                                                                                                              | 21.6 ms: 1.02x faster                                                                                                    |
| sqlglot_parse              | 905 us                                                                                                               | 886 us: 1.02x faster                                                                                                     |
| async_tree_memoization     | 263 ms                                                                                                               | 258 ms: 1.02x faster                                                                                                     |
| regex_v8                   | 15.2 ms                                                                                                              | 14.9 ms: 1.02x faster                                                                                                    |
| regex_effbot               | 1.61 ms                                                                                                              | 1.59 ms: 1.01x faster                                                                                                    |
| json                       | 2.98 ms                                                                                                              | 2.95 ms: 1.01x faster                                                                                                    |
| xml_etree_parse            | 93.2 ms                                                                                                              | 92.4 ms: 1.01x faster                                                                                                    |
| pidigits                   | 150 ms                                                                                                               | 149 ms: 1.01x faster                                                                                                     |
| coverage                   | 47.8 ms                                                                                                              | 48.1 ms: 1.01x slower                                                                                                    |
| django_template            | 26.0 ms                                                                                                              | 26.2 ms: 1.01x slower                                                                                                    |
| generators                 | 20.9 ms                                                                                                              | 21.1 ms: 1.01x slower                                                                                                    |
| async_tree_cpu_io_mixed_tg | 393 ms                                                                                                               | 397 ms: 1.01x slower                                                                                                     |
| sqlglot_transpile          | 1.13 ms                                                                                                              | 1.14 ms: 1.02x slower                                                                                                    |
| sqlglot_normalize          | 195 ms                                                                                                               | 199 ms: 1.02x slower                                                                                                     |
| gc_traversal               | 1.52 ms                                                                                                              | 1.55 ms: 1.02x slower                                                                                                    |
| async_tree_cpu_io_mixed    | 386 ms                                                                                                               | 394 ms: 1.02x slower                                                                                                     |
| regex_compile              | 92.3 ms                                                                                                              | 94.2 ms: 1.02x slower                                                                                                    |
| thrift                     | 513 us                                                                                                               | 525 us: 1.02x slower                                                                                                     |
| create_gc_cycles           | 874 us                                                                                                               | 901 us: 1.03x slower                                                                                                     |
| unpickle_list              | 2.77 us                                                                                                              | 2.87 us: 1.03x slower                                                                                                    |
| raytrace                   | 195 ms                                                                                                               | 202 ms: 1.03x slower                                                                                                     |
| html5lib                   | 40.6 ms                                                                                                              | 42.1 ms: 1.04x slower                                                                                                    |
| tornado_http               | 83.5 ms                                                                                                              | 87.4 ms: 1.05x slower                                                                                                    |
| go                         | 87.8 ms                                                                                                              | 92.2 ms: 1.05x slower                                                                                                    |
| pickle                     | 6.99 us                                                                                                              | 7.38 us: 1.06x slower                                                                                                    |
| sympy_str                  | 178 ms                                                                                                               | 189 ms: 1.06x slower                                                                                                     |
| 2to3                       | 225 ms                                                                                                               | 239 ms: 1.06x slower                                                                                                     |
| async_generators           | 243 ms                                                                                                               | 260 ms: 1.07x slower                                                                                                     |
| richards_super             | 36.7 ms                                                                                                              | 39.1 ms: 1.07x slower                                                                                                    |
| hexiom                     | 4.57 ms                                                                                                              | 4.89 ms: 1.07x slower                                                                                                    |
| sympy_expand               | 308 ms                                                                                                               | 330 ms: 1.07x slower                                                                                                     |
| bench_mp_pool              | 66.2 ms                                                                                                              | 71.7 ms: 1.08x slower                                                                                                    |
| sqlglot_optimize           | 36.5 ms                                                                                                              | 39.7 ms: 1.09x slower                                                                                                    |
| sympy_sum                  | 89.7 ms                                                                                                              | 97.9 ms: 1.09x slower                                                                                                    |
| genshi_text                | 17.1 ms                                                                                                              | 18.9 ms: 1.10x slower                                                                                                    |
| richards                   | 32.4 ms                                                                                                              | 36.5 ms: 1.12x slower                                                                                                    |
| sympy_integrate            | 13.2 ms                                                                                                              | 14.8 ms: 1.13x slower                                                                                                    |
| docutils                   | 1.70 sec                                                                                                             | 1.91 sec: 1.13x slower                                                                                                   |
| pylint                     | 225 ms                                                                                                               | 263 ms: 1.17x slower                                                                                                     |
| genshi_xml                 | 36.8 ms                                                                                                              | 45.7 ms: 1.24x slower                                                                                                    |
| unpack_sequence            | 42.2 ns                                                                                                              | 56.9 ns: 1.35x slower                                                                                                    |
| Geometric mean             | (ref)                                                                                                                | 1.05x faster                                                                                                             |

Benchmark hidden because not significant (11): async_tree_none_tg, async_tree_io_tg, asyncio_tcp, bench_thread_pool, json_loads, unpickle, dulwich_log, pathlib, python_startup_no_site, async_tree_io, async_tree_memoization_tg

# HPT report

- Reliability score: 91.18% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown
# Results vs. base

- fork: python
- ref: 04c837d9d8a474777ef9
- machine: windows-amd64
- commit hash: 04c837d
- commit date: 2024-09-28
- overall geometric mean: 1.05x faster
- HPT reliability: 77.44%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20240928-3.14.0a0-04c837d/bm-20240928-pythonperf1-amd64-python-04c837d9d8a474777ef9-3.14.0a0-04c837d.json | results/bm-20240928-3.14.0a0-04c837d-JIT/bm-20240928-pythonperf1-amd64-python-04c837d9d8a474777ef9-3.14.0a0-04c837d.json |
|----------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 227 ms                                                                                                               | 248 ms: 1.09x slower                                                                                                     |
| docutils       | 1.69 sec                                                                                                             | 1.92 sec: 1.13x slower                                                                                                   |
| html5lib       | 40.8 ms                                                                                                              | 42.1 ms: 1.03x slower                                                                                                    |
| tornado_http   | 92.7 ms                                                                                                              | 98.4 ms: 1.06x slower                                                                                                    |
| Geometric mean | (ref)                                                                                                                | 1.08x slower                                                                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | results/bm-20240928-3.14.0a0-04c837d/bm-20240928-pythonperf1-amd64-python-04c837d9d8a474777ef9-3.14.0a0-04c837d.json | results/bm-20240928-3.14.0a0-04c837d-JIT/bm-20240928-pythonperf1-amd64-python-04c837d9d8a474777ef9-3.14.0a0-04c837d.json |
|----------------------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| coroutines                 | 14.9 ms                                                                                                              | 14.0 ms: 1.07x faster                                                                                                    |
| async_tree_none            | 211 ms                                                                                                               | 206 ms: 1.02x faster                                                                                                     |
| async_tree_memoization     | 262 ms                                                                                                               | 259 ms: 1.01x faster                                                                                                     |
| async_tree_cpu_io_mixed_tg | 392 ms                                                                                                               | 397 ms: 1.01x slower                                                                                                     |
| asyncio_tcp                | 526 ms                                                                                                               | 545 ms: 1.04x slower                                                                                                     |
| async_generators           | 246 ms                                                                                                               | 267 ms: 1.08x slower                                                                                                     |
| asyncio_tcp_ssl            | 1.58 sec                                                                                                             | 1.71 sec: 1.09x slower                                                                                                   |
| Geometric mean             | (ref)                                                                                                                | 1.01x slower                                                                                                             |

Benchmark hidden because not significant (5): async_tree_none_tg, async_tree_io_tg, async_tree_io, async_tree_memoization_tg, async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20240928-3.14.0a0-04c837d/bm-20240928-pythonperf1-amd64-python-04c837d9d8a474777ef9-3.14.0a0-04c837d.json | results/bm-20240928-3.14.0a0-04c837d-JIT/bm-20240928-pythonperf1-amd64-python-04c837d9d8a474777ef9-3.14.0a0-04c837d.json |
|----------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| nbody          | 89.4 ms                                                                                                              | 47.9 ms: 1.87x faster                                                                                                    |
| float          | 56.2 ms                                                                                                              | 45.2 ms: 1.24x faster                                                                                                    |
| pidigits       | 151 ms                                                                                                               | 149 ms: 1.01x faster                                                                                                     |
| Geometric mean | (ref)                                                                                                                | 1.33x faster                                                                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20240928-3.14.0a0-04c837d/bm-20240928-pythonperf1-amd64-python-04c837d9d8a474777ef9-3.14.0a0-04c837d.json | results/bm-20240928-3.14.0a0-04c837d-JIT/bm-20240928-pythonperf1-amd64-python-04c837d9d8a474777ef9-3.14.0a0-04c837d.json |
|----------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| regex_v8       | 14.9 ms                                                                                                              | 14.7 ms: 1.02x faster                                                                                                    |
| regex_dna      | 119 ms                                                                                                               | 117 ms: 1.02x faster                                                                                                     |
| regex_compile  | 92.9 ms                                                                                                              | 94.1 ms: 1.01x slower                                                                                                    |
| Geometric mean | (ref)                                                                                                                | 1.01x faster                                                                                                             |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20240928-3.14.0a0-04c837d/bm-20240928-pythonperf1-amd64-python-04c837d9d8a474777ef9-3.14.0a0-04c837d.json | results/bm-20240928-3.14.0a0-04c837d-JIT/bm-20240928-pythonperf1-amd64-python-04c837d9d8a474777ef9-3.14.0a0-04c837d.json |
|----------------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| tomli_loads          | 1.63 sec                                                                                                             | 1.29 sec: 1.27x faster                                                                                                   |
| xml_etree_generate   | 58.4 ms                                                                                                              | 50.0 ms: 1.17x faster                                                                                                    |
| xml_etree_process    | 41.6 ms                                                                                                              | 35.7 ms: 1.17x faster                                                                                                    |
| json_dumps           | 6.43 ms                                                                                                              | 5.72 ms: 1.12x faster                                                                                                    |
| pickle_pure_python   | 221 us                                                                                                               | 201 us: 1.10x faster                                                                                                     |
| unpickle_pure_python | 156 us                                                                                                               | 144 us: 1.08x faster                                                                                                     |
| xml_etree_iterparse  | 66.1 ms                                                                                                              | 61.6 ms: 1.07x faster                                                                                                    |
| pickle_list          | 3.01 us                                                                                                              | 2.82 us: 1.07x faster                                                                                                    |
| pickle_dict          | 18.5 us                                                                                                              | 17.7 us: 1.04x faster                                                                                                    |
| unpickle_list        | 2.86 us                                                                                                              | 2.79 us: 1.02x faster                                                                                                    |
| xml_etree_parse      | 93.6 ms                                                                                                              | 94.6 ms: 1.01x slower                                                                                                    |
| json_loads           | 14.1 us                                                                                                              | 14.3 us: 1.01x slower                                                                                                    |
| pickle               | 7.19 us                                                                                                              | 7.39 us: 1.03x slower                                                                                                    |
| unpickle             | 9.24 us                                                                                                              | 9.77 us: 1.06x slower                                                                                                    |
| Geometric mean       | (ref)                                                                                                                | 1.07x faster                                                                                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark              | results/bm-20240928-3.14.0a0-04c837d/bm-20240928-pythonperf1-amd64-python-04c837d9d8a474777ef9-3.14.0a0-04c837d.json | results/bm-20240928-3.14.0a0-04c837d-JIT/bm-20240928-pythonperf1-amd64-python-04c837d9d8a474777ef9-3.14.0a0-04c837d.json |
|------------------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| python_startup_no_site | 18.0 ms                                                                                                              | 18.4 ms: 1.02x slower                                                                                                    |
| Geometric mean         | (ref)                                                                                                                | 1.01x slower                                                                                                             |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20240928-3.14.0a0-04c837d/bm-20240928-pythonperf1-amd64-python-04c837d9d8a474777ef9-3.14.0a0-04c837d.json | results/bm-20240928-3.14.0a0-04c837d-JIT/bm-20240928-pythonperf1-amd64-python-04c837d9d8a474777ef9-3.14.0a0-04c837d.json |
|-----------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| mako            | 6.88 ms                                                                                                              | 5.10 ms: 1.35x faster                                                                                                    |
| django_template | 25.6 ms                                                                                                              | 26.9 ms: 1.05x slower                                                                                                    |
| genshi_text     | 17.1 ms                                                                                                              | 19.5 ms: 1.14x slower                                                                                                    |
| genshi_xml      | 35.8 ms                                                                                                              | 46.4 ms: 1.30x slower                                                                                                    |
| Geometric mean  | (ref)                                                                                                                | 1.03x slower                                                                                                             |

All benchmarks:
===============

| Benchmark                  | results/bm-20240928-3.14.0a0-04c837d/bm-20240928-pythonperf1-amd64-python-04c837d9d8a474777ef9-3.14.0a0-04c837d.json | results/bm-20240928-3.14.0a0-04c837d-JIT/bm-20240928-pythonperf1-amd64-python-04c837d9d8a474777ef9-3.14.0a0-04c837d.json |
|----------------------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| nbody                      | 89.4 ms                                                                                                              | 47.9 ms: 1.87x faster                                                                                                    |
| spectral_norm              | 69.2 ms                                                                                                              | 44.0 ms: 1.57x faster                                                                                                    |
| scimark_sor                | 95.5 ms                                                                                                              | 61.9 ms: 1.54x faster                                                                                                    |
| deepcopy_memo              | 21.6 us                                                                                                              | 15.0 us: 1.44x faster                                                                                                    |
| json                       | 4.24 ms                                                                                                              | 3.02 ms: 1.40x faster                                                                                                    |
| scimark_fft                | 205 ms                                                                                                               | 146 ms: 1.40x faster                                                                                                     |
| mako                       | 6.88 ms                                                                                                              | 5.10 ms: 1.35x faster                                                                                                    |
| scimark_sparse_mat_mult    | 2.80 ms                                                                                                              | 2.15 ms: 1.30x faster                                                                                                    |
| fannkuch                   | 308 ms                                                                                                               | 239 ms: 1.29x faster                                                                                                     |
| crypto_pyaes               | 49.4 ms                                                                                                              | 38.7 ms: 1.28x faster                                                                                                    |
| tomli_loads                | 1.63 sec                                                                                                             | 1.29 sec: 1.27x faster                                                                                                   |
| pyflate                    | 330 ms                                                                                                               | 261 ms: 1.26x faster                                                                                                     |
| deltablue                  | 2.32 ms                                                                                                              | 1.86 ms: 1.25x faster                                                                                                    |
| float                      | 56.2 ms                                                                                                              | 45.2 ms: 1.24x faster                                                                                                    |
| scimark_lu                 | 68.1 ms                                                                                                              | 55.3 ms: 1.23x faster                                                                                                    |
| scimark_monte_carlo        | 51.6 ms                                                                                                              | 43.4 ms: 1.19x faster                                                                                                    |
| xml_etree_generate         | 58.4 ms                                                                                                              | 50.0 ms: 1.17x faster                                                                                                    |
| xml_etree_process          | 41.6 ms                                                                                                              | 35.7 ms: 1.17x faster                                                                                                    |
| logging_silent             | 65.4 ns                                                                                                              | 57.1 ns: 1.15x faster                                                                                                    |
| comprehensions             | 12.3 us                                                                                                              | 10.7 us: 1.14x faster                                                                                                    |
| telco                      | 4.91 ms                                                                                                              | 4.36 ms: 1.13x faster                                                                                                    |
| json_dumps                 | 6.43 ms                                                                                                              | 5.72 ms: 1.12x faster                                                                                                    |
| chaos                      | 44.7 ms                                                                                                              | 40.3 ms: 1.11x faster                                                                                                    |
| pickle_pure_python         | 221 us                                                                                                               | 201 us: 1.10x faster                                                                                                     |
| pprint_pformat             | 1.15 sec                                                                                                             | 1.04 sec: 1.10x faster                                                                                                   |
| pprint_safe_repr           | 564 ms                                                                                                               | 514 ms: 1.10x faster                                                                                                     |
| unpickle_pure_python       | 156 us                                                                                                               | 144 us: 1.08x faster                                                                                                     |
| xml_etree_iterparse        | 66.1 ms                                                                                                              | 61.6 ms: 1.07x faster                                                                                                    |
| nqueens                    | 65.8 ms                                                                                                              | 61.5 ms: 1.07x faster                                                                                                    |
| coroutines                 | 14.9 ms                                                                                                              | 14.0 ms: 1.07x faster                                                                                                    |
| pickle_list                | 3.01 us                                                                                                              | 2.82 us: 1.07x faster                                                                                                    |
| logging_simple             | 6.47 us                                                                                                              | 6.08 us: 1.06x faster                                                                                                    |
| logging_format             | 6.90 us                                                                                                              | 6.48 us: 1.06x faster                                                                                                    |
| meteor_contest             | 79.9 ms                                                                                                              | 76.1 ms: 1.05x faster                                                                                                    |
| pickle_dict                | 18.5 us                                                                                                              | 17.7 us: 1.04x faster                                                                                                    |
| deepcopy_reduce            | 1.95 us                                                                                                              | 1.88 us: 1.04x faster                                                                                                    |
| thrift                     | 535 us                                                                                                               | 519 us: 1.03x faster                                                                                                     |
| deepcopy                   | 190 us                                                                                                               | 185 us: 1.03x faster                                                                                                     |
| pycparser                  | 735 ms                                                                                                               | 716 ms: 1.03x faster                                                                                                     |
| async_tree_none            | 211 ms                                                                                                               | 206 ms: 1.02x faster                                                                                                     |
| unpickle_list              | 2.86 us                                                                                                              | 2.79 us: 1.02x faster                                                                                                    |
| coverage                   | 47.7 ms                                                                                                              | 46.8 ms: 1.02x faster                                                                                                    |
| regex_v8                   | 14.9 ms                                                                                                              | 14.7 ms: 1.02x faster                                                                                                    |
| regex_dna                  | 119 ms                                                                                                               | 117 ms: 1.02x faster                                                                                                     |
| sqlite_synth               | 1.63 us                                                                                                              | 1.61 us: 1.01x faster                                                                                                    |
| async_tree_memoization     | 262 ms                                                                                                               | 259 ms: 1.01x faster                                                                                                     |
| sqlglot_parse              | 906 us                                                                                                               | 895 us: 1.01x faster                                                                                                     |
| dulwich_log                | 43.9 ms                                                                                                              | 43.4 ms: 1.01x faster                                                                                                    |
| pidigits                   | 151 ms                                                                                                               | 149 ms: 1.01x faster                                                                                                     |
| mdp                        | 1.55 sec                                                                                                             | 1.57 sec: 1.01x slower                                                                                                   |
| xml_etree_parse            | 93.6 ms                                                                                                              | 94.6 ms: 1.01x slower                                                                                                    |
| async_tree_cpu_io_mixed_tg | 392 ms                                                                                                               | 397 ms: 1.01x slower                                                                                                     |
| json_loads                 | 14.1 us                                                                                                              | 14.3 us: 1.01x slower                                                                                                    |
| regex_compile              | 92.9 ms                                                                                                              | 94.1 ms: 1.01x slower                                                                                                    |
| typing_runtime_protocols   | 109 us                                                                                                               | 112 us: 1.02x slower                                                                                                     |
| python_startup_no_site     | 18.0 ms                                                                                                              | 18.4 ms: 1.02x slower                                                                                                    |
| pickle                     | 7.19 us                                                                                                              | 7.39 us: 1.03x slower                                                                                                    |
| html5lib                   | 40.8 ms                                                                                                              | 42.1 ms: 1.03x slower                                                                                                    |
| asyncio_tcp                | 526 ms                                                                                                               | 545 ms: 1.04x slower                                                                                                     |
| sqlglot_transpile          | 1.13 ms                                                                                                              | 1.18 ms: 1.05x slower                                                                                                    |
| django_template            | 25.6 ms                                                                                                              | 26.9 ms: 1.05x slower                                                                                                    |
| sqlglot_normalize          | 195 ms                                                                                                               | 205 ms: 1.05x slower                                                                                                     |
| go                         | 89.7 ms                                                                                                              | 94.1 ms: 1.05x slower                                                                                                    |
| bench_mp_pool              | 69.1 ms                                                                                                              | 72.9 ms: 1.05x slower                                                                                                    |
| unpickle                   | 9.24 us                                                                                                              | 9.77 us: 1.06x slower                                                                                                    |
| tornado_http               | 92.7 ms                                                                                                              | 98.4 ms: 1.06x slower                                                                                                    |
| hexiom                     | 4.70 ms                                                                                                              | 5.03 ms: 1.07x slower                                                                                                    |
| raytrace                   | 196 ms                                                                                                               | 210 ms: 1.07x slower                                                                                                     |
| sympy_expand               | 310 ms                                                                                                               | 334 ms: 1.08x slower                                                                                                     |
| async_generators           | 246 ms                                                                                                               | 267 ms: 1.08x slower                                                                                                     |
| generators                 | 20.6 ms                                                                                                              | 22.3 ms: 1.09x slower                                                                                                    |
| asyncio_tcp_ssl            | 1.58 sec                                                                                                             | 1.71 sec: 1.09x slower                                                                                                   |
| 2to3                       | 227 ms                                                                                                               | 248 ms: 1.09x slower                                                                                                     |
| sympy_str                  | 179 ms                                                                                                               | 195 ms: 1.09x slower                                                                                                     |
| richards_super             | 37.4 ms                                                                                                              | 41.7 ms: 1.12x slower                                                                                                    |
| sympy_sum                  | 90.5 ms                                                                                                              | 102 ms: 1.13x slower                                                                                                     |
| docutils                   | 1.69 sec                                                                                                             | 1.92 sec: 1.13x slower                                                                                                   |
| genshi_text                | 17.1 ms                                                                                                              | 19.5 ms: 1.14x slower                                                                                                    |
| sympy_integrate            | 13.4 ms                                                                                                              | 15.3 ms: 1.14x slower                                                                                                    |
| richards                   | 33.3 ms                                                                                                              | 38.7 ms: 1.16x slower                                                                                                    |
| sqlglot_optimize           | 36.8 ms                                                                                                              | 43.0 ms: 1.17x slower                                                                                                    |
| pylint                     | 225 ms                                                                                                               | 272 ms: 1.21x slower                                                                                                     |
| unpack_sequence            | 45.8 ns                                                                                                              | 56.8 ns: 1.24x slower                                                                                                    |
| genshi_xml                 | 35.8 ms                                                                                                              | 46.4 ms: 1.30x slower                                                                                                    |
| Geometric mean             | (ref)                                                                                                                | 1.05x faster                                                                                                             |

Benchmark hidden because not significant (11): async_tree_none_tg, async_tree_io_tg, create_gc_cycles, gc_traversal, pathlib, regex_effbot, python_startup, bench_thread_pool, async_tree_io, async_tree_memoization_tg, async_tree_cpu_io_mixed

# HPT report

- Reliability score: 77.44% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown
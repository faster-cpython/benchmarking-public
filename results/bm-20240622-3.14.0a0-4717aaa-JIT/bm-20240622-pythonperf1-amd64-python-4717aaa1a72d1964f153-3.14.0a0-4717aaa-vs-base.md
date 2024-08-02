# Results vs. base

- fork: python
- ref: 4717aaa1a72d1964f153
- machine: windows-amd64
- commit hash: 4717aaa
- commit date: 2024-06-22
- overall geometric mean: 1.01x slower
- HPT reliability: 77.31%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20240622-3.14.0a0-4717aaa/bm-20240622-pythonperf1-amd64-python-4717aaa1a72d1964f153-3.14.0a0-4717aaa.json | results/bm-20240622-3.14.0a0-4717aaa-JIT/bm-20240622-pythonperf1-amd64-python-4717aaa1a72d1964f153-3.14.0a0-4717aaa.json |
|----------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 211 ms                                                                                                               | 228 ms: 1.08x slower                                                                                                     |
| docutils       | 1.62 sec                                                                                                             | 1.74 sec: 1.08x slower                                                                                                   |
| html5lib       | 35.0 ms                                                                                                              | 35.7 ms: 1.02x slower                                                                                                    |
| tornado_http   | 79.7 ms                                                                                                              | 82.7 ms: 1.04x slower                                                                                                    |
| Geometric mean | (ref)                                                                                                                | 1.05x slower                                                                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | results/bm-20240622-3.14.0a0-4717aaa/bm-20240622-pythonperf1-amd64-python-4717aaa1a72d1964f153-3.14.0a0-4717aaa.json | results/bm-20240622-3.14.0a0-4717aaa-JIT/bm-20240622-pythonperf1-amd64-python-4717aaa1a72d1964f153-3.14.0a0-4717aaa.json |
|----------------------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed_tg | 380 ms                                                                                                               | 372 ms: 1.02x faster                                                                                                     |
| Geometric mean             | (ref)                                                                                                                | 1.01x faster                                                                                                             |

Benchmark hidden because not significant (7): async_tree_io, async_tree_cpu_io_mixed, async_tree_none_tg, async_tree_none, async_tree_memoization_tg, async_tree_memoization, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20240622-3.14.0a0-4717aaa/bm-20240622-pythonperf1-amd64-python-4717aaa1a72d1964f153-3.14.0a0-4717aaa.json | results/bm-20240622-3.14.0a0-4717aaa-JIT/bm-20240622-pythonperf1-amd64-python-4717aaa1a72d1964f153-3.14.0a0-4717aaa.json |
|----------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| nbody          | 65.8 ms                                                                                                              | 53.6 ms: 1.23x faster                                                                                                    |
| float          | 49.1 ms                                                                                                              | 44.0 ms: 1.12x faster                                                                                                    |
| pidigits       | 149 ms                                                                                                               | 149 ms: 1.00x faster                                                                                                     |
| Geometric mean | (ref)                                                                                                                | 1.11x faster                                                                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20240622-3.14.0a0-4717aaa/bm-20240622-pythonperf1-amd64-python-4717aaa1a72d1964f153-3.14.0a0-4717aaa.json | results/bm-20240622-3.14.0a0-4717aaa-JIT/bm-20240622-pythonperf1-amd64-python-4717aaa1a72d1964f153-3.14.0a0-4717aaa.json |
|----------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| regex_dna      | 124 ms                                                                                                               | 118 ms: 1.06x faster                                                                                                     |
| regex_effbot   | 1.63 ms                                                                                                              | 1.56 ms: 1.04x faster                                                                                                    |
| regex_compile  | 77.2 ms                                                                                                              | 87.2 ms: 1.13x slower                                                                                                    |
| Geometric mean | (ref)                                                                                                                | 1.01x slower                                                                                                             |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20240622-3.14.0a0-4717aaa/bm-20240622-pythonperf1-amd64-python-4717aaa1a72d1964f153-3.14.0a0-4717aaa.json | results/bm-20240622-3.14.0a0-4717aaa-JIT/bm-20240622-pythonperf1-amd64-python-4717aaa1a72d1964f153-3.14.0a0-4717aaa.json |
|----------------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| tomli_loads          | 1.37 sec                                                                                                             | 1.21 sec: 1.14x faster                                                                                                   |
| pickle_pure_python   | 181 us                                                                                                               | 168 us: 1.08x faster                                                                                                     |
| xml_etree_generate   | 53.8 ms                                                                                                              | 51.3 ms: 1.05x faster                                                                                                    |
| xml_etree_iterparse  | 63.2 ms                                                                                                              | 60.9 ms: 1.04x faster                                                                                                    |
| json_dumps           | 5.82 ms                                                                                                              | 5.65 ms: 1.03x faster                                                                                                    |
| pickle_dict          | 18.2 us                                                                                                              | 17.7 us: 1.03x faster                                                                                                    |
| xml_etree_process    | 36.9 ms                                                                                                              | 36.2 ms: 1.02x faster                                                                                                    |
| pickle_list          | 2.92 us                                                                                                              | 2.86 us: 1.02x faster                                                                                                    |
| unpickle_list        | 2.84 us                                                                                                              | 2.80 us: 1.01x faster                                                                                                    |
| unpickle_pure_python | 125 us                                                                                                               | 123 us: 1.01x faster                                                                                                     |
| xml_etree_parse      | 92.0 ms                                                                                                              | 92.6 ms: 1.01x slower                                                                                                    |
| json_loads           | 13.8 us                                                                                                              | 14.0 us: 1.01x slower                                                                                                    |
| pickle               | 7.10 us                                                                                                              | 7.29 us: 1.03x slower                                                                                                    |
| unpickle             | 8.59 us                                                                                                              | 9.00 us: 1.05x slower                                                                                                    |
| Geometric mean       | (ref)                                                                                                                | 1.02x faster                                                                                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark              | results/bm-20240622-3.14.0a0-4717aaa/bm-20240622-pythonperf1-amd64-python-4717aaa1a72d1964f153-3.14.0a0-4717aaa.json | results/bm-20240622-3.14.0a0-4717aaa-JIT/bm-20240622-pythonperf1-amd64-python-4717aaa1a72d1964f153-3.14.0a0-4717aaa.json |
|------------------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| python_startup         | 20.7 ms                                                                                                              | 22.5 ms: 1.09x slower                                                                                                    |
| python_startup_no_site | 16.8 ms                                                                                                              | 18.4 ms: 1.10x slower                                                                                                    |
| Geometric mean         | (ref)                                                                                                                | 1.09x slower                                                                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20240622-3.14.0a0-4717aaa/bm-20240622-pythonperf1-amd64-python-4717aaa1a72d1964f153-3.14.0a0-4717aaa.json | results/bm-20240622-3.14.0a0-4717aaa-JIT/bm-20240622-pythonperf1-amd64-python-4717aaa1a72d1964f153-3.14.0a0-4717aaa.json |
|-----------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| mako            | 6.60 ms                                                                                                              | 5.08 ms: 1.30x faster                                                                                                    |
| django_template | 22.1 ms                                                                                                              | 24.6 ms: 1.11x slower                                                                                                    |
| genshi_text     | 14.7 ms                                                                                                              | 17.2 ms: 1.17x slower                                                                                                    |
| genshi_xml      | 31.8 ms                                                                                                              | 41.8 ms: 1.31x slower                                                                                                    |
| Geometric mean  | (ref)                                                                                                                | 1.07x slower                                                                                                             |

All benchmarks:
===============

| Benchmark                  | results/bm-20240622-3.14.0a0-4717aaa/bm-20240622-pythonperf1-amd64-python-4717aaa1a72d1964f153-3.14.0a0-4717aaa.json | results/bm-20240622-3.14.0a0-4717aaa-JIT/bm-20240622-pythonperf1-amd64-python-4717aaa1a72d1964f153-3.14.0a0-4717aaa.json |
|----------------------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| spectral_norm              | 61.2 ms                                                                                                              | 46.3 ms: 1.32x faster                                                                                                    |
| mako                       | 6.60 ms                                                                                                              | 5.08 ms: 1.30x faster                                                                                                    |
| scimark_sparse_mat_mult    | 2.59 ms                                                                                                              | 2.09 ms: 1.24x faster                                                                                                    |
| nbody                      | 65.8 ms                                                                                                              | 53.6 ms: 1.23x faster                                                                                                    |
| scimark_fft                | 173 ms                                                                                                               | 150 ms: 1.16x faster                                                                                                     |
| tomli_loads                | 1.37 sec                                                                                                             | 1.21 sec: 1.14x faster                                                                                                   |
| float                      | 49.1 ms                                                                                                              | 44.0 ms: 1.12x faster                                                                                                    |
| deepcopy_memo              | 17.1 us                                                                                                              | 15.3 us: 1.11x faster                                                                                                    |
| pyflate                    | 281 ms                                                                                                               | 252 ms: 1.11x faster                                                                                                     |
| crypto_pyaes               | 45.1 ms                                                                                                              | 40.7 ms: 1.11x faster                                                                                                    |
| fannkuch                   | 245 ms                                                                                                               | 222 ms: 1.10x faster                                                                                                     |
| telco                      | 4.93 ms                                                                                                              | 4.48 ms: 1.10x faster                                                                                                    |
| scimark_monte_carlo        | 40.5 ms                                                                                                              | 37.4 ms: 1.08x faster                                                                                                    |
| pickle_pure_python         | 181 us                                                                                                               | 168 us: 1.08x faster                                                                                                     |
| coverage                   | 46.8 ms                                                                                                              | 43.6 ms: 1.07x faster                                                                                                    |
| pprint_safe_repr           | 481 ms                                                                                                               | 450 ms: 1.07x faster                                                                                                     |
| pprint_pformat             | 986 ms                                                                                                               | 924 ms: 1.07x faster                                                                                                     |
| asyncio_tcp_ssl            | 1.57 sec                                                                                                             | 1.48 sec: 1.07x faster                                                                                                   |
| logging_format             | 6.22 us                                                                                                              | 5.87 us: 1.06x faster                                                                                                    |
| regex_dna                  | 124 ms                                                                                                               | 118 ms: 1.06x faster                                                                                                     |
| logging_simple             | 5.78 us                                                                                                              | 5.49 us: 1.05x faster                                                                                                    |
| xml_etree_generate         | 53.8 ms                                                                                                              | 51.3 ms: 1.05x faster                                                                                                    |
| regex_effbot               | 1.63 ms                                                                                                              | 1.56 ms: 1.04x faster                                                                                                    |
| xml_etree_iterparse        | 63.2 ms                                                                                                              | 60.9 ms: 1.04x faster                                                                                                    |
| json_dumps                 | 5.82 ms                                                                                                              | 5.65 ms: 1.03x faster                                                                                                    |
| pickle_dict                | 18.2 us                                                                                                              | 17.7 us: 1.03x faster                                                                                                    |
| generators                 | 20.6 ms                                                                                                              | 20.0 ms: 1.03x faster                                                                                                    |
| sqlite_synth               | 1.61 us                                                                                                              | 1.58 us: 1.02x faster                                                                                                    |
| async_tree_cpu_io_mixed_tg | 380 ms                                                                                                               | 372 ms: 1.02x faster                                                                                                     |
| xml_etree_process          | 36.9 ms                                                                                                              | 36.2 ms: 1.02x faster                                                                                                    |
| pickle_list                | 2.92 us                                                                                                              | 2.86 us: 1.02x faster                                                                                                    |
| unpickle_list              | 2.84 us                                                                                                              | 2.80 us: 1.01x faster                                                                                                    |
| unpickle_pure_python       | 125 us                                                                                                               | 123 us: 1.01x faster                                                                                                     |
| coroutines                 | 12.9 ms                                                                                                              | 12.8 ms: 1.01x faster                                                                                                    |
| mdp                        | 1.38 sec                                                                                                             | 1.37 sec: 1.01x faster                                                                                                   |
| pidigits                   | 149 ms                                                                                                               | 149 ms: 1.00x faster                                                                                                     |
| gc_traversal               | 1.56 ms                                                                                                              | 1.56 ms: 1.00x slower                                                                                                    |
| sqlglot_parse              | 771 us                                                                                                               | 775 us: 1.00x slower                                                                                                     |
| xml_etree_parse            | 92.0 ms                                                                                                              | 92.6 ms: 1.01x slower                                                                                                    |
| chaos                      | 38.2 ms                                                                                                              | 38.5 ms: 1.01x slower                                                                                                    |
| json_loads                 | 13.8 us                                                                                                              | 14.0 us: 1.01x slower                                                                                                    |
| json                       | 2.88 ms                                                                                                              | 2.93 ms: 1.02x slower                                                                                                    |
| html5lib                   | 35.0 ms                                                                                                              | 35.7 ms: 1.02x slower                                                                                                    |
| meteor_contest             | 70.6 ms                                                                                                              | 72.6 ms: 1.03x slower                                                                                                    |
| pickle                     | 7.10 us                                                                                                              | 7.29 us: 1.03x slower                                                                                                    |
| logging_silent             | 53.6 ns                                                                                                              | 55.4 ns: 1.03x slower                                                                                                    |
| bench_thread_pool          | 742 us                                                                                                               | 768 us: 1.04x slower                                                                                                     |
| tornado_http               | 79.7 ms                                                                                                              | 82.7 ms: 1.04x slower                                                                                                    |
| sqlglot_transpile          | 966 us                                                                                                               | 1.01 ms: 1.04x slower                                                                                                    |
| unpickle                   | 8.59 us                                                                                                              | 9.00 us: 1.05x slower                                                                                                    |
| scimark_sor                | 75.4 ms                                                                                                              | 79.3 ms: 1.05x slower                                                                                                    |
| raytrace                   | 159 ms                                                                                                               | 168 ms: 1.05x slower                                                                                                     |
| go                         | 83.6 ms                                                                                                              | 88.0 ms: 1.05x slower                                                                                                    |
| nqueens                    | 55.8 ms                                                                                                              | 59.5 ms: 1.07x slower                                                                                                    |
| deepcopy                   | 164 us                                                                                                               | 175 us: 1.07x slower                                                                                                     |
| async_generators           | 228 ms                                                                                                               | 243 ms: 1.07x slower                                                                                                     |
| sqlglot_normalize          | 176 ms                                                                                                               | 188 ms: 1.07x slower                                                                                                     |
| bench_mp_pool              | 65.3 ms                                                                                                              | 69.9 ms: 1.07x slower                                                                                                    |
| sympy_sum                  | 84.3 ms                                                                                                              | 90.5 ms: 1.07x slower                                                                                                    |
| sqlglot_optimize           | 33.1 ms                                                                                                              | 35.6 ms: 1.08x slower                                                                                                    |
| typing_runtime_protocols   | 102 us                                                                                                               | 110 us: 1.08x slower                                                                                                     |
| docutils                   | 1.62 sec                                                                                                             | 1.74 sec: 1.08x slower                                                                                                   |
| 2to3                       | 211 ms                                                                                                               | 228 ms: 1.08x slower                                                                                                     |
| sympy_str                  | 162 ms                                                                                                               | 175 ms: 1.09x slower                                                                                                     |
| python_startup             | 20.7 ms                                                                                                              | 22.5 ms: 1.09x slower                                                                                                    |
| python_startup_no_site     | 16.8 ms                                                                                                              | 18.4 ms: 1.10x slower                                                                                                    |
| deltablue                  | 1.90 ms                                                                                                              | 2.09 ms: 1.10x slower                                                                                                    |
| pycparser                  | 719 ms                                                                                                               | 796 ms: 1.11x slower                                                                                                     |
| sympy_integrate            | 12.3 ms                                                                                                              | 13.6 ms: 1.11x slower                                                                                                    |
| sympy_expand               | 275 ms                                                                                                               | 305 ms: 1.11x slower                                                                                                     |
| django_template            | 22.1 ms                                                                                                              | 24.6 ms: 1.11x slower                                                                                                    |
| regex_compile              | 77.2 ms                                                                                                              | 87.2 ms: 1.13x slower                                                                                                    |
| pylint                     | 204 ms                                                                                                               | 232 ms: 1.14x slower                                                                                                     |
| richards_super             | 29.4 ms                                                                                                              | 33.8 ms: 1.15x slower                                                                                                    |
| richards                   | 25.9 ms                                                                                                              | 30.2 ms: 1.17x slower                                                                                                    |
| genshi_text                | 14.7 ms                                                                                                              | 17.2 ms: 1.17x slower                                                                                                    |
| hexiom                     | 3.70 ms                                                                                                              | 4.62 ms: 1.25x slower                                                                                                    |
| scimark_lu                 | 53.4 ms                                                                                                              | 68.8 ms: 1.29x slower                                                                                                    |
| genshi_xml                 | 31.8 ms                                                                                                              | 41.8 ms: 1.31x slower                                                                                                    |
| Geometric mean             | (ref)                                                                                                                | 1.01x slower                                                                                                             |

Benchmark hidden because not significant (14): async_tree_io, async_tree_cpu_io_mixed, async_tree_none_tg, async_tree_none, async_tree_memoization_tg, deepcopy_reduce, async_tree_memoization, create_gc_cycles, async_tree_io_tg, pathlib, comprehensions, asyncio_tcp, regex_v8, thrift

# HPT report

- Reliability score: 77.31% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown
# Results vs. 3.13.0b2

- fork: python
- ref: 342e654b8eda24c68da6
- machine: windows-amd64
- commit hash: 342e654
- commit date: 2024-09-20
- overall geometric mean: 1.01x slower
- HPT reliability: 98.40%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240920-pythonperf1-amd64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 207 ms                                                          | 241 ms: 1.17x slower                                                       |
| docutils       | 1.63 sec                                                        | 1.92 sec: 1.18x slower                                                     |
| html5lib       | 35.0 ms                                                         | 41.9 ms: 1.20x slower                                                      |
| tornado_http   | 81.8 ms                                                         | 87.6 ms: 1.07x slower                                                      |
| Geometric mean | (ref)                                                           | 1.15x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240920-pythonperf1-amd64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io_tg           | 605 ms                                                          | 562 ms: 1.08x faster                                                       |
| async_tree_none            | 218 ms                                                          | 206 ms: 1.06x faster                                                       |
| async_tree_cpu_io_mixed_tg | 382 ms                                                          | 397 ms: 1.04x slower                                                       |
| Geometric mean             | (ref)                                                           | 1.02x faster                                                               |

Benchmark hidden because not significant (5): async_tree_none_tg, async_tree_memoization, async_tree_memoization_tg, async_tree_io, async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240920-pythonperf1-amd64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 67.6 ms                                                         | 49.5 ms: 1.37x faster                                                      |
| float          | 49.7 ms                                                         | 44.3 ms: 1.12x faster                                                      |
| pidigits       | 150 ms                                                          | 149 ms: 1.00x faster                                                       |
| Geometric mean | (ref)                                                           | 1.15x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240920-pythonperf1-amd64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_dna      | 119 ms                                                          | 116 ms: 1.03x faster                                                       |
| regex_effbot   | 1.58 ms                                                         | 1.55 ms: 1.02x faster                                                      |
| regex_compile  | 78.0 ms                                                         | 95.0 ms: 1.22x slower                                                      |
| Geometric mean | (ref)                                                           | 1.04x slower                                                               |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240920-pythonperf1-amd64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| xml_etree_generate   | 53.2 ms                                                         | 49.4 ms: 1.08x faster                                                      |
| tomli_loads          | 1.35 sec                                                        | 1.27 sec: 1.06x faster                                                     |
| pickle_list          | 2.90 us                                                         | 2.76 us: 1.05x faster                                                      |
| pickle_dict          | 18.1 us                                                         | 17.6 us: 1.03x faster                                                      |
| xml_etree_process    | 36.4 ms                                                         | 35.4 ms: 1.03x faster                                                      |
| xml_etree_iterparse  | 62.3 ms                                                         | 60.9 ms: 1.02x faster                                                      |
| pickle               | 7.11 us                                                         | 7.19 us: 1.01x slower                                                      |
| json_loads           | 14.2 us                                                         | 14.5 us: 1.02x slower                                                      |
| xml_etree_parse      | 90.9 ms                                                         | 93.5 ms: 1.03x slower                                                      |
| json_dumps           | 5.61 ms                                                         | 5.87 ms: 1.05x slower                                                      |
| unpickle             | 8.40 us                                                         | 8.89 us: 1.06x slower                                                      |
| unpickle_list        | 2.62 us                                                         | 2.83 us: 1.08x slower                                                      |
| pickle_pure_python   | 175 us                                                          | 191 us: 1.09x slower                                                       |
| unpickle_pure_python | 122 us                                                          | 142 us: 1.16x slower                                                       |
| Geometric mean       | (ref)                                                           | 1.02x slower                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240920-pythonperf1-amd64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 20.3 ms                                                         | 22.1 ms: 1.09x slower                                                      |
| python_startup_no_site | 16.2 ms                                                         | 18.3 ms: 1.13x slower                                                      |
| Geometric mean         | (ref)                                                           | 1.11x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240920-pythonperf1-amd64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 6.36 ms                                                         | 5.21 ms: 1.22x faster                                                      |
| django_template | 21.7 ms                                                         | 26.9 ms: 1.24x slower                                                      |
| genshi_text     | 14.4 ms                                                         | 18.8 ms: 1.31x slower                                                      |
| genshi_xml      | 31.6 ms                                                         | 44.1 ms: 1.40x slower                                                      |
| Geometric mean  | (ref)                                                           | 1.17x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240920-pythonperf1-amd64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| thrift                     | 8.11 ms                                                         | 513 us: 15.80x faster                                                      |
| spectral_norm              | 63.7 ms                                                         | 44.1 ms: 1.44x faster                                                      |
| deepcopy_memo              | 22.1 us                                                         | 15.5 us: 1.43x faster                                                      |
| nbody                      | 67.6 ms                                                         | 49.5 ms: 1.37x faster                                                      |
| scimark_sor                | 75.3 ms                                                         | 61.2 ms: 1.23x faster                                                      |
| mako                       | 6.36 ms                                                         | 5.21 ms: 1.22x faster                                                      |
| scimark_sparse_mat_mult    | 2.50 ms                                                         | 2.09 ms: 1.20x faster                                                      |
| deepcopy                   | 220 us                                                          | 184 us: 1.19x faster                                                       |
| crypto_pyaes               | 45.5 ms                                                         | 38.7 ms: 1.18x faster                                                      |
| scimark_fft                | 171 ms                                                          | 150 ms: 1.14x faster                                                       |
| float                      | 49.7 ms                                                         | 44.3 ms: 1.12x faster                                                      |
| json                       | 3.19 ms                                                         | 2.94 ms: 1.08x faster                                                      |
| asyncio_tcp_ssl            | 1.48 sec                                                        | 1.37 sec: 1.08x faster                                                     |
| async_tree_io_tg           | 605 ms                                                          | 562 ms: 1.08x faster                                                       |
| xml_etree_generate         | 53.2 ms                                                         | 49.4 ms: 1.08x faster                                                      |
| pycparser                  | 754 ms                                                          | 709 ms: 1.06x faster                                                       |
| async_tree_none            | 218 ms                                                          | 206 ms: 1.06x faster                                                       |
| tomli_loads                | 1.35 sec                                                        | 1.27 sec: 1.06x faster                                                     |
| deepcopy_reduce            | 1.99 us                                                         | 1.88 us: 1.06x faster                                                      |
| pyflate                    | 279 ms                                                          | 265 ms: 1.05x faster                                                       |
| pickle_list                | 2.90 us                                                         | 2.76 us: 1.05x faster                                                      |
| scimark_lu                 | 56.6 ms                                                         | 54.0 ms: 1.05x faster                                                      |
| deltablue                  | 1.88 ms                                                         | 1.81 ms: 1.04x faster                                                      |
| pickle_dict                | 18.1 us                                                         | 17.6 us: 1.03x faster                                                      |
| xml_etree_process          | 36.4 ms                                                         | 35.4 ms: 1.03x faster                                                      |
| regex_dna                  | 119 ms                                                          | 116 ms: 1.03x faster                                                       |
| fannkuch                   | 243 ms                                                          | 238 ms: 1.02x faster                                                       |
| xml_etree_iterparse        | 62.3 ms                                                         | 60.9 ms: 1.02x faster                                                      |
| regex_effbot               | 1.58 ms                                                         | 1.55 ms: 1.02x faster                                                      |
| gc_traversal               | 1.55 ms                                                         | 1.54 ms: 1.01x faster                                                      |
| pidigits                   | 150 ms                                                          | 149 ms: 1.00x faster                                                       |
| sqlite_synth               | 1.60 us                                                         | 1.60 us: 1.00x slower                                                      |
| pickle                     | 7.11 us                                                         | 7.19 us: 1.01x slower                                                      |
| create_gc_cycles           | 888 us                                                          | 899 us: 1.01x slower                                                       |
| telco                      | 4.67 ms                                                         | 4.73 ms: 1.01x slower                                                      |
| comprehensions             | 10.4 us                                                         | 10.6 us: 1.02x slower                                                      |
| json_loads                 | 14.2 us                                                         | 14.5 us: 1.02x slower                                                      |
| xml_etree_parse            | 90.9 ms                                                         | 93.5 ms: 1.03x slower                                                      |
| async_tree_cpu_io_mixed_tg | 382 ms                                                          | 397 ms: 1.04x slower                                                       |
| chaos                      | 38.4 ms                                                         | 40.0 ms: 1.04x slower                                                      |
| logging_simple             | 5.78 us                                                         | 6.04 us: 1.05x slower                                                      |
| json_dumps                 | 5.61 ms                                                         | 5.87 ms: 1.05x slower                                                      |
| bench_thread_pool          | 768 us                                                          | 803 us: 1.05x slower                                                       |
| logging_format             | 6.22 us                                                         | 6.52 us: 1.05x slower                                                      |
| meteor_contest             | 69.9 ms                                                         | 73.5 ms: 1.05x slower                                                      |
| unpickle                   | 8.40 us                                                         | 8.89 us: 1.06x slower                                                      |
| pprint_safe_repr           | 474 ms                                                          | 503 ms: 1.06x slower                                                       |
| tornado_http               | 81.8 ms                                                         | 87.6 ms: 1.07x slower                                                      |
| logging_silent             | 52.9 ns                                                         | 56.7 ns: 1.07x slower                                                      |
| mdp                        | 1.31 sec                                                        | 1.41 sec: 1.07x slower                                                     |
| pprint_pformat             | 966 ms                                                          | 1.04 sec: 1.08x slower                                                     |
| unpickle_list              | 2.62 us                                                         | 2.83 us: 1.08x slower                                                      |
| pickle_pure_python         | 175 us                                                          | 191 us: 1.09x slower                                                       |
| python_startup             | 20.3 ms                                                         | 22.1 ms: 1.09x slower                                                      |
| coverage                   | 42.1 ms                                                         | 46.1 ms: 1.10x slower                                                      |
| scimark_monte_carlo        | 39.1 ms                                                         | 42.9 ms: 1.10x slower                                                      |
| nqueens                    | 56.7 ms                                                         | 62.4 ms: 1.10x slower                                                      |
| bench_mp_pool              | 64.8 ms                                                         | 71.7 ms: 1.11x slower                                                      |
| go                         | 82.1 ms                                                         | 91.3 ms: 1.11x slower                                                      |
| dulwich_log                | 38.0 ms                                                         | 42.6 ms: 1.12x slower                                                      |
| python_startup_no_site     | 16.2 ms                                                         | 18.3 ms: 1.13x slower                                                      |
| typing_runtime_protocols   | 101 us                                                          | 114 us: 1.13x slower                                                       |
| coroutines                 | 12.8 ms                                                         | 14.6 ms: 1.15x slower                                                      |
| sqlglot_normalize          | 173 ms                                                          | 201 ms: 1.16x slower                                                       |
| sympy_sum                  | 84.4 ms                                                         | 98.3 ms: 1.16x slower                                                      |
| unpickle_pure_python       | 122 us                                                          | 142 us: 1.16x slower                                                       |
| 2to3                       | 207 ms                                                          | 241 ms: 1.17x slower                                                       |
| async_generators           | 223 ms                                                          | 261 ms: 1.17x slower                                                       |
| sqlglot_parse              | 748 us                                                          | 880 us: 1.18x slower                                                       |
| docutils                   | 1.63 sec                                                        | 1.92 sec: 1.18x slower                                                     |
| generators                 | 19.6 ms                                                         | 23.1 ms: 1.18x slower                                                      |
| sympy_str                  | 159 ms                                                          | 188 ms: 1.18x slower                                                       |
| html5lib                   | 35.0 ms                                                         | 41.9 ms: 1.20x slower                                                      |
| sqlglot_transpile          | 955 us                                                          | 1.15 ms: 1.20x slower                                                      |
| sympy_integrate            | 12.2 ms                                                         | 14.8 ms: 1.21x slower                                                      |
| raytrace                   | 162 ms                                                          | 197 ms: 1.22x slower                                                       |
| regex_compile              | 78.0 ms                                                         | 95.0 ms: 1.22x slower                                                      |
| sympy_expand               | 271 ms                                                          | 330 ms: 1.22x slower                                                       |
| sqlglot_optimize           | 32.7 ms                                                         | 40.3 ms: 1.23x slower                                                      |
| django_template            | 21.7 ms                                                         | 26.9 ms: 1.24x slower                                                      |
| richards_super             | 30.2 ms                                                         | 38.6 ms: 1.28x slower                                                      |
| pylint                     | 205 ms                                                          | 264 ms: 1.29x slower                                                       |
| genshi_text                | 14.4 ms                                                         | 18.8 ms: 1.31x slower                                                      |
| hexiom                     | 3.72 ms                                                         | 4.87 ms: 1.31x slower                                                      |
| richards                   | 26.7 ms                                                         | 36.1 ms: 1.35x slower                                                      |
| genshi_xml                 | 31.6 ms                                                         | 44.1 ms: 1.40x slower                                                      |
| Geometric mean             | (ref)                                                           | 1.01x slower                                                               |

Benchmark hidden because not significant (8): async_tree_none_tg, async_tree_memoization, async_tree_memoization_tg, async_tree_io, pathlib, async_tree_cpu_io_mixed, asyncio_tcp, regex_v8
Ignored benchmarks (4) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, flaskblogging, mypy2
Ignored benchmarks (1) of results/bm-20240920-3.14.0a0-342e654-JIT/bm-20240920-pythonperf1-amd64-python-342e654b8eda24c68da6-3.14.0a0-342e654.json: unpack_sequence

# HPT report

- Reliability score: 98.40% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown
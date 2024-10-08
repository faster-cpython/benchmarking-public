# Results vs. 3.13.0b2

- fork: python
- ref: 54dd77fb8c880d7655ff
- machine: windows-amd64
- commit hash: 54dd77f
- commit date: 2024-09-24
- overall geometric mean: 1.02x slower
- HPT reliability: 99.85%
- HPT 99th percentile: 1.01x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240924-pythonperf1-amd64-python-54dd77fb8c880d7655ff-3.14.0a0-54dd77f |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 207 ms                                                          | 243 ms: 1.17x slower                                                       |
| docutils       | 1.63 sec                                                        | 1.93 sec: 1.19x slower                                                     |
| html5lib       | 35.0 ms                                                         | 41.5 ms: 1.19x slower                                                      |
| tornado_http   | 81.8 ms                                                         | 97.3 ms: 1.19x slower                                                      |
| Geometric mean | (ref)                                                           | 1.18x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240924-pythonperf1-amd64-python-54dd77fb8c880d7655ff-3.14.0a0-54dd77f |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io_tg           | 605 ms                                                          | 555 ms: 1.09x faster                                                       |
| async_tree_none            | 218 ms                                                          | 206 ms: 1.06x faster                                                       |
| async_tree_cpu_io_mixed_tg | 382 ms                                                          | 392 ms: 1.03x slower                                                       |
| Geometric mean             | (ref)                                                           | 1.02x faster                                                               |

Benchmark hidden because not significant (5): async_tree_memoization, async_tree_memoization_tg, async_tree_none_tg, async_tree_io, async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240924-pythonperf1-amd64-python-54dd77fb8c880d7655ff-3.14.0a0-54dd77f |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 67.6 ms                                                         | 49.2 ms: 1.37x faster                                                      |
| float          | 49.7 ms                                                         | 44.0 ms: 1.13x faster                                                      |
| pidigits       | 150 ms                                                          | 149 ms: 1.00x faster                                                       |
| Geometric mean | (ref)                                                           | 1.16x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240924-pythonperf1-amd64-python-54dd77fb8c880d7655ff-3.14.0a0-54dd77f |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_effbot   | 1.58 ms                                                         | 1.63 ms: 1.03x slower                                                      |
| regex_dna      | 119 ms                                                          | 123 ms: 1.04x slower                                                       |
| regex_compile  | 78.0 ms                                                         | 96.5 ms: 1.24x slower                                                      |
| Geometric mean | (ref)                                                           | 1.08x slower                                                               |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240924-pythonperf1-amd64-python-54dd77fb8c880d7655ff-3.14.0a0-54dd77f |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| xml_etree_generate   | 53.2 ms                                                         | 49.9 ms: 1.07x faster                                                      |
| tomli_loads          | 1.35 sec                                                        | 1.28 sec: 1.06x faster                                                     |
| xml_etree_process    | 36.4 ms                                                         | 35.0 ms: 1.04x faster                                                      |
| pickle_dict          | 18.1 us                                                         | 17.7 us: 1.02x faster                                                      |
| json_loads           | 14.2 us                                                         | 14.4 us: 1.02x slower                                                      |
| xml_etree_parse      | 90.9 ms                                                         | 92.9 ms: 1.02x slower                                                      |
| pickle               | 7.11 us                                                         | 7.31 us: 1.03x slower                                                      |
| json_dumps           | 5.61 ms                                                         | 5.84 ms: 1.04x slower                                                      |
| unpickle_list        | 2.62 us                                                         | 2.82 us: 1.08x slower                                                      |
| unpickle             | 8.40 us                                                         | 9.16 us: 1.09x slower                                                      |
| pickle_pure_python   | 175 us                                                          | 198 us: 1.13x slower                                                       |
| unpickle_pure_python | 122 us                                                          | 141 us: 1.16x slower                                                       |
| Geometric mean       | (ref)                                                           | 1.02x slower                                                               |

Benchmark hidden because not significant (2): pickle_list, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240924-pythonperf1-amd64-python-54dd77fb8c880d7655ff-3.14.0a0-54dd77f |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 20.3 ms                                                         | 22.5 ms: 1.11x slower                                                      |
| python_startup_no_site | 16.2 ms                                                         | 18.3 ms: 1.13x slower                                                      |
| Geometric mean         | (ref)                                                           | 1.12x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240924-pythonperf1-amd64-python-54dd77fb8c880d7655ff-3.14.0a0-54dd77f |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 6.36 ms                                                         | 4.92 ms: 1.29x faster                                                      |
| django_template | 21.7 ms                                                         | 26.8 ms: 1.24x slower                                                      |
| genshi_text     | 14.4 ms                                                         | 19.2 ms: 1.33x slower                                                      |
| genshi_xml      | 31.6 ms                                                         | 45.5 ms: 1.44x slower                                                      |
| Geometric mean  | (ref)                                                           | 1.16x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240924-pythonperf1-amd64-python-54dd77fb8c880d7655ff-3.14.0a0-54dd77f |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| thrift                     | 8.11 ms                                                         | 518 us: 15.66x faster                                                      |
| spectral_norm              | 63.7 ms                                                         | 43.8 ms: 1.45x faster                                                      |
| deepcopy_memo              | 22.1 us                                                         | 15.5 us: 1.42x faster                                                      |
| nbody                      | 67.6 ms                                                         | 49.2 ms: 1.37x faster                                                      |
| mako                       | 6.36 ms                                                         | 4.92 ms: 1.29x faster                                                      |
| scimark_sor                | 75.3 ms                                                         | 61.1 ms: 1.23x faster                                                      |
| crypto_pyaes               | 45.5 ms                                                         | 38.7 ms: 1.18x faster                                                      |
| deepcopy                   | 220 us                                                          | 188 us: 1.17x faster                                                       |
| scimark_fft                | 171 ms                                                          | 148 ms: 1.15x faster                                                       |
| scimark_sparse_mat_mult    | 2.50 ms                                                         | 2.20 ms: 1.14x faster                                                      |
| float                      | 49.7 ms                                                         | 44.0 ms: 1.13x faster                                                      |
| deepcopy_reduce            | 1.99 us                                                         | 1.80 us: 1.11x faster                                                      |
| async_tree_io_tg           | 605 ms                                                          | 555 ms: 1.09x faster                                                       |
| json                       | 3.19 ms                                                         | 2.93 ms: 1.09x faster                                                      |
| xml_etree_generate         | 53.2 ms                                                         | 49.9 ms: 1.07x faster                                                      |
| async_tree_none            | 218 ms                                                          | 206 ms: 1.06x faster                                                       |
| tomli_loads                | 1.35 sec                                                        | 1.28 sec: 1.06x faster                                                     |
| pyflate                    | 279 ms                                                          | 265 ms: 1.05x faster                                                       |
| xml_etree_process          | 36.4 ms                                                         | 35.0 ms: 1.04x faster                                                      |
| telco                      | 4.67 ms                                                         | 4.56 ms: 1.02x faster                                                      |
| pickle_dict                | 18.1 us                                                         | 17.7 us: 1.02x faster                                                      |
| deltablue                  | 1.88 ms                                                         | 1.84 ms: 1.02x faster                                                      |
| scimark_lu                 | 56.6 ms                                                         | 55.6 ms: 1.02x faster                                                      |
| pidigits                   | 150 ms                                                          | 149 ms: 1.00x faster                                                       |
| json_loads                 | 14.2 us                                                         | 14.4 us: 1.02x slower                                                      |
| xml_etree_parse            | 90.9 ms                                                         | 92.9 ms: 1.02x slower                                                      |
| async_tree_cpu_io_mixed_tg | 382 ms                                                          | 392 ms: 1.03x slower                                                       |
| pickle                     | 7.11 us                                                         | 7.31 us: 1.03x slower                                                      |
| regex_effbot               | 1.58 ms                                                         | 1.63 ms: 1.03x slower                                                      |
| logging_format             | 6.22 us                                                         | 6.41 us: 1.03x slower                                                      |
| comprehensions             | 10.4 us                                                         | 10.7 us: 1.03x slower                                                      |
| logging_simple             | 5.78 us                                                         | 5.97 us: 1.03x slower                                                      |
| regex_dna                  | 119 ms                                                          | 123 ms: 1.04x slower                                                       |
| json_dumps                 | 5.61 ms                                                         | 5.84 ms: 1.04x slower                                                      |
| bench_thread_pool          | 768 us                                                          | 806 us: 1.05x slower                                                       |
| mdp                        | 1.31 sec                                                        | 1.41 sec: 1.08x slower                                                     |
| pathlib                    | 75.9 ms                                                         | 81.6 ms: 1.08x slower                                                      |
| meteor_contest             | 69.9 ms                                                         | 75.2 ms: 1.08x slower                                                      |
| typing_runtime_protocols   | 101 us                                                          | 109 us: 1.08x slower                                                       |
| unpickle_list              | 2.62 us                                                         | 2.82 us: 1.08x slower                                                      |
| chaos                      | 38.4 ms                                                         | 41.7 ms: 1.09x slower                                                      |
| unpickle                   | 8.40 us                                                         | 9.16 us: 1.09x slower                                                      |
| scimark_monte_carlo        | 39.1 ms                                                         | 42.8 ms: 1.09x slower                                                      |
| nqueens                    | 56.7 ms                                                         | 62.2 ms: 1.10x slower                                                      |
| bench_mp_pool              | 64.8 ms                                                         | 71.5 ms: 1.10x slower                                                      |
| coroutines                 | 12.8 ms                                                         | 14.1 ms: 1.11x slower                                                      |
| python_startup             | 20.3 ms                                                         | 22.5 ms: 1.11x slower                                                      |
| logging_silent             | 52.9 ns                                                         | 58.9 ns: 1.11x slower                                                      |
| coverage                   | 42.1 ms                                                         | 47.3 ms: 1.12x slower                                                      |
| python_startup_no_site     | 16.2 ms                                                         | 18.3 ms: 1.13x slower                                                      |
| pickle_pure_python         | 175 us                                                          | 198 us: 1.13x slower                                                       |
| go                         | 82.1 ms                                                         | 93.2 ms: 1.14x slower                                                      |
| pprint_safe_repr           | 474 ms                                                          | 539 ms: 1.14x slower                                                       |
| dulwich_log                | 38.0 ms                                                         | 43.5 ms: 1.14x slower                                                      |
| asyncio_tcp                | 471 ms                                                          | 542 ms: 1.15x slower                                                       |
| unpickle_pure_python       | 122 us                                                          | 141 us: 1.16x slower                                                       |
| pprint_pformat             | 966 ms                                                          | 1.12 sec: 1.16x slower                                                     |
| async_generators           | 223 ms                                                          | 261 ms: 1.17x slower                                                       |
| generators                 | 19.6 ms                                                         | 22.9 ms: 1.17x slower                                                      |
| 2to3                       | 207 ms                                                          | 243 ms: 1.17x slower                                                       |
| sqlglot_normalize          | 173 ms                                                          | 203 ms: 1.18x slower                                                       |
| sympy_sum                  | 84.4 ms                                                         | 99.7 ms: 1.18x slower                                                      |
| html5lib                   | 35.0 ms                                                         | 41.5 ms: 1.19x slower                                                      |
| docutils                   | 1.63 sec                                                        | 1.93 sec: 1.19x slower                                                     |
| tornado_http               | 81.8 ms                                                         | 97.3 ms: 1.19x slower                                                      |
| sqlglot_parse              | 748 us                                                          | 896 us: 1.20x slower                                                       |
| sympy_str                  | 159 ms                                                          | 192 ms: 1.20x slower                                                       |
| sqlglot_transpile          | 955 us                                                          | 1.16 ms: 1.22x slower                                                      |
| sympy_integrate            | 12.2 ms                                                         | 15.0 ms: 1.22x slower                                                      |
| regex_compile              | 78.0 ms                                                         | 96.5 ms: 1.24x slower                                                      |
| django_template            | 21.7 ms                                                         | 26.8 ms: 1.24x slower                                                      |
| sympy_expand               | 271 ms                                                          | 337 ms: 1.24x slower                                                       |
| sqlglot_optimize           | 32.7 ms                                                         | 40.8 ms: 1.25x slower                                                      |
| raytrace                   | 162 ms                                                          | 207 ms: 1.27x slower                                                       |
| richards_super             | 30.2 ms                                                         | 39.3 ms: 1.30x slower                                                      |
| pylint                     | 205 ms                                                          | 268 ms: 1.31x slower                                                       |
| genshi_text                | 14.4 ms                                                         | 19.2 ms: 1.33x slower                                                      |
| hexiom                     | 3.72 ms                                                         | 5.03 ms: 1.35x slower                                                      |
| richards                   | 26.7 ms                                                         | 37.3 ms: 1.40x slower                                                      |
| genshi_xml                 | 31.6 ms                                                         | 45.5 ms: 1.44x slower                                                      |
| Geometric mean             | (ref)                                                           | 1.02x slower                                                               |

Benchmark hidden because not significant (14): pycparser, async_tree_memoization, async_tree_memoization_tg, async_tree_none_tg, pickle_list, xml_etree_iterparse, async_tree_io, sqlite_synth, fannkuch, gc_traversal, async_tree_cpu_io_mixed, create_gc_cycles, regex_v8, asyncio_tcp_ssl
Ignored benchmarks (4) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, flaskblogging, mypy2
Ignored benchmarks (1) of results/bm-20240924-3.14.0a0-54dd77f-JIT/bm-20240924-pythonperf1-amd64-python-54dd77fb8c880d7655ff-3.14.0a0-54dd77f.json: unpack_sequence

# HPT report

- Reliability score: 99.85% likely to be slow
- 90% likely to have a slowdown of 1.03x
- 95% likely to have a slowdown of 1.02x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: unknown
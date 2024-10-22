# Results vs. 3.13.0

- fork: mdboom
- ref: remove_redundant_typ
- machine: windows-amd64
- commit hash: b0f5f3a
- commit date: 2024-09-23
- overall geometric mean: 1.04x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240923-pythonperf1-amd64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 217 ms                                                      | 224 ms: 1.03x slower                                                       |
| docutils       | 1.57 sec                                                    | 1.69 sec: 1.07x slower                                                     |
| html5lib       | 38.6 ms                                                     | 40.1 ms: 1.04x slower                                                      |
| tornado_http   | 92.8 ms                                                     | 84.2 ms: 1.10x faster                                                      |
| Geometric mean | (ref)                                                       | 1.01x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240923-pythonperf1-amd64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| asyncio_tcp                | 654 ms                                                      | 474 ms: 1.38x faster                                                       |
| async_tree_memoization_tg  | 288 ms                                                      | 255 ms: 1.13x faster                                                       |
| async_tree_none            | 223 ms                                                      | 209 ms: 1.07x faster                                                       |
| async_tree_cpu_io_mixed_tg | 375 ms                                                      | 397 ms: 1.06x slower                                                       |
| async_generators           | 223 ms                                                      | 241 ms: 1.08x slower                                                       |
| async_tree_io_tg           | 512 ms                                                      | 560 ms: 1.09x slower                                                       |
| async_tree_io              | 521 ms                                                      | 570 ms: 1.09x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 14.5 ms: 1.16x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.01x faster                                                               |

Benchmark hidden because not significant (4): async_tree_memoization, asyncio_tcp_ssl, async_tree_none_tg, async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240923-pythonperf1-amd64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pidigits       | 148 ms                                                      | 150 ms: 1.01x slower                                                       |
| float          | 48.1 ms                                                     | 55.8 ms: 1.16x slower                                                      |
| nbody          | 64.5 ms                                                     | 81.8 ms: 1.27x slower                                                      |
| Geometric mean | (ref)                                                       | 1.14x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240923-pythonperf1-amd64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_effbot   | 1.62 ms                                                     | 1.55 ms: 1.04x faster                                                      |
| regex_dna      | 114 ms                                                      | 117 ms: 1.02x slower                                                       |
| regex_compile  | 80.1 ms                                                     | 91.4 ms: 1.14x slower                                                      |
| Geometric mean | (ref)                                                       | 1.03x slower                                                               |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240923-pythonperf1-amd64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pickle               | 7.34 us                                                     | 7.31 us: 1.00x faster                                                      |
| xml_etree_parse      | 93.2 ms                                                     | 93.8 ms: 1.01x slower                                                      |
| unpickle_list        | 2.72 us                                                     | 2.77 us: 1.02x slower                                                      |
| json_loads           | 14.3 us                                                     | 14.6 us: 1.02x slower                                                      |
| pickle_dict          | 18.0 us                                                     | 18.5 us: 1.03x slower                                                      |
| xml_etree_iterparse  | 62.3 ms                                                     | 64.6 ms: 1.04x slower                                                      |
| pickle_list          | 2.89 us                                                     | 3.07 us: 1.06x slower                                                      |
| xml_etree_generate   | 53.3 ms                                                     | 57.3 ms: 1.07x slower                                                      |
| json_dumps           | 5.76 ms                                                     | 6.23 ms: 1.08x slower                                                      |
| unpickle             | 8.63 us                                                     | 9.34 us: 1.08x slower                                                      |
| xml_etree_process    | 36.5 ms                                                     | 40.3 ms: 1.10x slower                                                      |
| pickle_pure_python   | 183 us                                                      | 213 us: 1.16x slower                                                       |
| unpickle_pure_python | 127 us                                                      | 149 us: 1.17x slower                                                       |
| tomli_loads          | 1.36 sec                                                    | 1.60 sec: 1.18x slower                                                     |
| Geometric mean       | (ref)                                                       | 1.07x slower                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240923-pythonperf1-amd64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup | 22.2 ms                                                     | 21.9 ms: 1.01x faster                                                      |
| Geometric mean | (ref)                                                       | 1.00x faster                                                               |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240923-pythonperf1-amd64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 6.24 ms                                                     | 6.79 ms: 1.09x slower                                                      |
| genshi_xml      | 32.8 ms                                                     | 37.5 ms: 1.14x slower                                                      |
| genshi_text     | 14.9 ms                                                     | 17.5 ms: 1.18x slower                                                      |
| django_template | 21.8 ms                                                     | 25.7 ms: 1.18x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.15x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240923-pythonperf1-amd64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| thrift                     | 8.68 ms                                                     | 519 us: 16.73x faster                                                      |
| asyncio_tcp                | 654 ms                                                      | 474 ms: 1.38x faster                                                       |
| deepcopy                   | 223 us                                                      | 192 us: 1.17x faster                                                       |
| async_tree_memoization_tg  | 288 ms                                                      | 255 ms: 1.13x faster                                                       |
| tornado_http               | 92.8 ms                                                     | 84.2 ms: 1.10x faster                                                      |
| pathlib                    | 81.2 ms                                                     | 75.6 ms: 1.07x faster                                                      |
| async_tree_none            | 223 ms                                                      | 209 ms: 1.07x faster                                                       |
| bench_mp_pool              | 69.6 ms                                                     | 66.3 ms: 1.05x faster                                                      |
| deepcopy_memo              | 21.8 us                                                     | 20.9 us: 1.05x faster                                                      |
| regex_effbot               | 1.62 ms                                                     | 1.55 ms: 1.04x faster                                                      |
| deepcopy_reduce            | 2.02 us                                                     | 1.96 us: 1.03x faster                                                      |
| bench_thread_pool          | 828 us                                                      | 807 us: 1.03x faster                                                       |
| gc_traversal               | 1.55 ms                                                     | 1.53 ms: 1.02x faster                                                      |
| python_startup             | 22.2 ms                                                     | 21.9 ms: 1.01x faster                                                      |
| coverage                   | 46.7 ms                                                     | 46.3 ms: 1.01x faster                                                      |
| pickle                     | 7.34 us                                                     | 7.31 us: 1.00x faster                                                      |
| xml_etree_parse            | 93.2 ms                                                     | 93.8 ms: 1.01x slower                                                      |
| pidigits                   | 148 ms                                                      | 150 ms: 1.01x slower                                                       |
| unpickle_list              | 2.72 us                                                     | 2.77 us: 1.02x slower                                                      |
| json_loads                 | 14.3 us                                                     | 14.6 us: 1.02x slower                                                      |
| regex_dna                  | 114 ms                                                      | 117 ms: 1.02x slower                                                       |
| go                         | 84.6 ms                                                     | 86.6 ms: 1.02x slower                                                      |
| pickle_dict                | 18.0 us                                                     | 18.5 us: 1.03x slower                                                      |
| sqlite_synth               | 1.60 us                                                     | 1.64 us: 1.03x slower                                                      |
| mdp                        | 1.38 sec                                                    | 1.43 sec: 1.03x slower                                                     |
| 2to3                       | 217 ms                                                      | 224 ms: 1.03x slower                                                       |
| xml_etree_iterparse        | 62.3 ms                                                     | 64.6 ms: 1.04x slower                                                      |
| html5lib                   | 38.6 ms                                                     | 40.1 ms: 1.04x slower                                                      |
| sympy_sum                  | 86.4 ms                                                     | 89.9 ms: 1.04x slower                                                      |
| telco                      | 4.85 ms                                                     | 5.05 ms: 1.04x slower                                                      |
| dulwich_log                | 40.4 ms                                                     | 42.4 ms: 1.05x slower                                                      |
| async_tree_cpu_io_mixed_tg | 375 ms                                                      | 397 ms: 1.06x slower                                                       |
| pickle_list                | 2.89 us                                                     | 3.07 us: 1.06x slower                                                      |
| sympy_str                  | 166 ms                                                      | 177 ms: 1.07x slower                                                       |
| create_gc_cycles           | 829 us                                                      | 883 us: 1.07x slower                                                       |
| sympy_integrate            | 12.3 ms                                                     | 13.1 ms: 1.07x slower                                                      |
| sympy_expand               | 285 ms                                                      | 306 ms: 1.07x slower                                                       |
| docutils                   | 1.57 sec                                                    | 1.69 sec: 1.07x slower                                                     |
| xml_etree_generate         | 53.3 ms                                                     | 57.3 ms: 1.07x slower                                                      |
| meteor_contest             | 72.3 ms                                                     | 77.8 ms: 1.08x slower                                                      |
| async_generators           | 223 ms                                                      | 241 ms: 1.08x slower                                                       |
| json_dumps                 | 5.76 ms                                                     | 6.23 ms: 1.08x slower                                                      |
| unpickle                   | 8.63 us                                                     | 9.34 us: 1.08x slower                                                      |
| mako                       | 6.24 ms                                                     | 6.79 ms: 1.09x slower                                                      |
| generators                 | 19.5 ms                                                     | 21.2 ms: 1.09x slower                                                      |
| async_tree_io_tg           | 512 ms                                                      | 560 ms: 1.09x slower                                                       |
| async_tree_io              | 521 ms                                                      | 570 ms: 1.09x slower                                                       |
| sqlglot_optimize           | 33.1 ms                                                     | 36.3 ms: 1.10x slower                                                      |
| typing_runtime_protocols   | 100 us                                                      | 110 us: 1.10x slower                                                       |
| pprint_safe_repr           | 493 ms                                                      | 543 ms: 1.10x slower                                                       |
| xml_etree_process          | 36.5 ms                                                     | 40.3 ms: 1.10x slower                                                      |
| scimark_sparse_mat_mult    | 2.34 ms                                                     | 2.60 ms: 1.11x slower                                                      |
| pprint_pformat             | 991 ms                                                      | 1.10 sec: 1.11x slower                                                     |
| sqlglot_normalize          | 171 ms                                                      | 191 ms: 1.12x slower                                                       |
| logging_format             | 6.15 us                                                     | 6.91 us: 1.12x slower                                                      |
| crypto_pyaes               | 42.8 ms                                                     | 48.1 ms: 1.12x slower                                                      |
| chaos                      | 37.9 ms                                                     | 42.6 ms: 1.12x slower                                                      |
| logging_simple             | 5.72 us                                                     | 6.46 us: 1.13x slower                                                      |
| scimark_lu                 | 54.0 ms                                                     | 61.3 ms: 1.13x slower                                                      |
| regex_compile              | 80.1 ms                                                     | 91.4 ms: 1.14x slower                                                      |
| genshi_xml                 | 32.8 ms                                                     | 37.5 ms: 1.14x slower                                                      |
| nqueens                    | 55.5 ms                                                     | 63.8 ms: 1.15x slower                                                      |
| coroutines                 | 12.5 ms                                                     | 14.5 ms: 1.16x slower                                                      |
| unpack_sequence            | 40.0 ns                                                     | 46.4 ns: 1.16x slower                                                      |
| float                      | 48.1 ms                                                     | 55.8 ms: 1.16x slower                                                      |
| scimark_fft                | 174 ms                                                      | 203 ms: 1.16x slower                                                       |
| pickle_pure_python         | 183 us                                                      | 213 us: 1.16x slower                                                       |
| spectral_norm              | 59.2 ms                                                     | 69.0 ms: 1.17x slower                                                      |
| sqlglot_transpile          | 952 us                                                      | 1.11 ms: 1.17x slower                                                      |
| pyflate                    | 275 ms                                                      | 322 ms: 1.17x slower                                                       |
| comprehensions             | 10.2 us                                                     | 12.0 us: 1.17x slower                                                      |
| unpickle_pure_python       | 127 us                                                      | 149 us: 1.17x slower                                                       |
| sqlglot_parse              | 761 us                                                      | 895 us: 1.18x slower                                                       |
| tomli_loads                | 1.36 sec                                                    | 1.60 sec: 1.18x slower                                                     |
| genshi_text                | 14.9 ms                                                     | 17.5 ms: 1.18x slower                                                      |
| django_template            | 21.8 ms                                                     | 25.7 ms: 1.18x slower                                                      |
| fannkuch                   | 245 ms                                                      | 293 ms: 1.19x slower                                                       |
| hexiom                     | 3.69 ms                                                     | 4.42 ms: 1.20x slower                                                      |
| richards_super             | 29.3 ms                                                     | 35.6 ms: 1.22x slower                                                      |
| scimark_monte_carlo        | 40.3 ms                                                     | 49.0 ms: 1.22x slower                                                      |
| deltablue                  | 1.86 ms                                                     | 2.27 ms: 1.22x slower                                                      |
| richards                   | 26.0 ms                                                     | 32.0 ms: 1.23x slower                                                      |
| logging_silent             | 51.0 ns                                                     | 63.0 ns: 1.24x slower                                                      |
| raytrace                   | 156 ms                                                      | 194 ms: 1.24x slower                                                       |
| nbody                      | 64.5 ms                                                     | 81.8 ms: 1.27x slower                                                      |
| scimark_sor                | 72.0 ms                                                     | 92.2 ms: 1.28x slower                                                      |
| json                       | 2.98 ms                                                     | 4.39 ms: 1.47x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.04x slower                                                               |

Benchmark hidden because not significant (8): pycparser, async_tree_memoization, asyncio_tcp_ssl, async_tree_none_tg, async_tree_cpu_io_mixed, regex_v8, python_startup_no_site, pylint
Ignored benchmarks (4) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, flaskblogging, mypy2

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.06x
- 95% likely to have a slowdown of 1.06x
- 99% likely to have a slowdown of 1.05x

# Memory
- memory change: unknown
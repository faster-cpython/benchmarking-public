# Results vs. 3.13.0

- fork: python
- ref: 6e06e01881dcffbeef5b
- machine: windows-amd64
- commit hash: 6e06e01
- commit date: 2024-09-12
- overall geometric mean: 1.04x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240912-pythonperf1-amd64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 217 ms                                                      | 224 ms: 1.03x slower                                                       |
| docutils       | 1.57 sec                                                    | 1.70 sec: 1.08x slower                                                     |
| html5lib       | 38.6 ms                                                     | 40.3 ms: 1.04x slower                                                      |
| tornado_http   | 92.8 ms                                                     | 84.4 ms: 1.10x faster                                                      |
| Geometric mean | (ref)                                                       | 1.01x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240912-pythonperf1-amd64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| asyncio_tcp                | 654 ms                                                      | 474 ms: 1.38x faster                                                       |
| asyncio_tcp_ssl            | 1.64 sec                                                    | 1.38 sec: 1.19x faster                                                     |
| async_tree_memoization_tg  | 288 ms                                                      | 252 ms: 1.14x faster                                                       |
| async_tree_none            | 223 ms                                                      | 208 ms: 1.07x faster                                                       |
| async_tree_memoization     | 271 ms                                                      | 262 ms: 1.04x faster                                                       |
| async_tree_cpu_io_mixed    | 387 ms                                                      | 394 ms: 1.02x slower                                                       |
| async_tree_cpu_io_mixed_tg | 375 ms                                                      | 397 ms: 1.06x slower                                                       |
| async_tree_io              | 521 ms                                                      | 570 ms: 1.09x slower                                                       |
| async_tree_io_tg           | 512 ms                                                      | 560 ms: 1.09x slower                                                       |
| async_generators           | 223 ms                                                      | 245 ms: 1.10x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 14.1 ms: 1.13x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.02x faster                                                               |

Benchmark hidden because not significant (1): async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240912-pythonperf1-amd64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pidigits       | 148 ms                                                      | 150 ms: 1.01x slower                                                       |
| float          | 48.1 ms                                                     | 56.1 ms: 1.17x slower                                                      |
| nbody          | 64.5 ms                                                     | 83.7 ms: 1.30x slower                                                      |
| Geometric mean | (ref)                                                       | 1.15x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240912-pythonperf1-amd64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_effbot   | 1.62 ms                                                     | 1.57 ms: 1.03x faster                                                      |
| regex_dna      | 114 ms                                                      | 119 ms: 1.04x slower                                                       |
| regex_compile  | 80.1 ms                                                     | 91.8 ms: 1.15x slower                                                      |
| Geometric mean | (ref)                                                       | 1.04x slower                                                               |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240912-pythonperf1-amd64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pickle               | 7.34 us                                                     | 7.23 us: 1.01x faster                                                      |
| pickle_dict          | 18.0 us                                                     | 18.5 us: 1.02x slower                                                      |
| pickle_list          | 2.89 us                                                     | 3.00 us: 1.04x slower                                                      |
| unpickle_list        | 2.72 us                                                     | 2.83 us: 1.04x slower                                                      |
| xml_etree_iterparse  | 62.3 ms                                                     | 64.9 ms: 1.04x slower                                                      |
| json_dumps           | 5.76 ms                                                     | 6.19 ms: 1.08x slower                                                      |
| xml_etree_generate   | 53.3 ms                                                     | 57.9 ms: 1.09x slower                                                      |
| unpickle             | 8.63 us                                                     | 9.62 us: 1.11x slower                                                      |
| xml_etree_process    | 36.5 ms                                                     | 41.1 ms: 1.12x slower                                                      |
| pickle_pure_python   | 183 us                                                      | 210 us: 1.15x slower                                                       |
| tomli_loads          | 1.36 sec                                                    | 1.58 sec: 1.16x slower                                                     |
| unpickle_pure_python | 127 us                                                      | 151 us: 1.19x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.07x slower                                                               |

Benchmark hidden because not significant (2): xml_etree_parse, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240912-pythonperf1-amd64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 22.2 ms                                                     | 21.7 ms: 1.02x faster                                                      |
| python_startup_no_site | 17.8 ms                                                     | 17.6 ms: 1.01x faster                                                      |
| Geometric mean         | (ref)                                                       | 1.02x faster                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240912-pythonperf1-amd64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_xml      | 32.8 ms                                                     | 36.0 ms: 1.10x slower                                                      |
| mako            | 6.24 ms                                                     | 6.89 ms: 1.10x slower                                                      |
| genshi_text     | 14.9 ms                                                     | 17.1 ms: 1.15x slower                                                      |
| django_template | 21.8 ms                                                     | 26.0 ms: 1.19x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.14x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240912-pythonperf1-amd64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| thrift                     | 8.68 ms                                                     | 523 us: 16.61x faster                                                      |
| asyncio_tcp                | 654 ms                                                      | 474 ms: 1.38x faster                                                       |
| asyncio_tcp_ssl            | 1.64 sec                                                    | 1.38 sec: 1.19x faster                                                     |
| deepcopy                   | 223 us                                                      | 189 us: 1.18x faster                                                       |
| async_tree_memoization_tg  | 288 ms                                                      | 252 ms: 1.14x faster                                                       |
| tornado_http               | 92.8 ms                                                     | 84.4 ms: 1.10x faster                                                      |
| pathlib                    | 81.2 ms                                                     | 75.6 ms: 1.07x faster                                                      |
| async_tree_none            | 223 ms                                                      | 208 ms: 1.07x faster                                                       |
| deepcopy_memo              | 21.8 us                                                     | 20.4 us: 1.07x faster                                                      |
| deepcopy_reduce            | 2.02 us                                                     | 1.93 us: 1.04x faster                                                      |
| async_tree_memoization     | 271 ms                                                      | 262 ms: 1.04x faster                                                       |
| bench_mp_pool              | 69.6 ms                                                     | 67.6 ms: 1.03x faster                                                      |
| regex_effbot               | 1.62 ms                                                     | 1.57 ms: 1.03x faster                                                      |
| bench_thread_pool          | 828 us                                                      | 808 us: 1.02x faster                                                       |
| python_startup             | 22.2 ms                                                     | 21.7 ms: 1.02x faster                                                      |
| gc_traversal               | 1.55 ms                                                     | 1.53 ms: 1.02x faster                                                      |
| pickle                     | 7.34 us                                                     | 7.23 us: 1.01x faster                                                      |
| python_startup_no_site     | 17.8 ms                                                     | 17.6 ms: 1.01x faster                                                      |
| coverage                   | 46.7 ms                                                     | 46.9 ms: 1.00x slower                                                      |
| pidigits                   | 148 ms                                                      | 150 ms: 1.01x slower                                                       |
| go                         | 84.6 ms                                                     | 85.8 ms: 1.01x slower                                                      |
| async_tree_cpu_io_mixed    | 387 ms                                                      | 394 ms: 1.02x slower                                                       |
| pickle_dict                | 18.0 us                                                     | 18.5 us: 1.02x slower                                                      |
| telco                      | 4.85 ms                                                     | 4.97 ms: 1.03x slower                                                      |
| sqlite_synth               | 1.60 us                                                     | 1.64 us: 1.03x slower                                                      |
| 2to3                       | 217 ms                                                      | 224 ms: 1.03x slower                                                       |
| pickle_list                | 2.89 us                                                     | 3.00 us: 1.04x slower                                                      |
| unpickle_list              | 2.72 us                                                     | 2.83 us: 1.04x slower                                                      |
| xml_etree_iterparse        | 62.3 ms                                                     | 64.9 ms: 1.04x slower                                                      |
| sympy_sum                  | 86.4 ms                                                     | 90.0 ms: 1.04x slower                                                      |
| regex_dna                  | 114 ms                                                      | 119 ms: 1.04x slower                                                       |
| html5lib                   | 38.6 ms                                                     | 40.3 ms: 1.04x slower                                                      |
| mdp                        | 1.38 sec                                                    | 1.44 sec: 1.04x slower                                                     |
| json                       | 2.98 ms                                                     | 3.15 ms: 1.06x slower                                                      |
| dulwich_log                | 40.4 ms                                                     | 42.8 ms: 1.06x slower                                                      |
| async_tree_cpu_io_mixed_tg | 375 ms                                                      | 397 ms: 1.06x slower                                                       |
| sympy_str                  | 166 ms                                                      | 177 ms: 1.06x slower                                                       |
| create_gc_cycles           | 829 us                                                      | 883 us: 1.07x slower                                                       |
| unpack_sequence            | 40.0 ns                                                     | 42.7 ns: 1.07x slower                                                      |
| sympy_expand               | 285 ms                                                      | 306 ms: 1.07x slower                                                       |
| sympy_integrate            | 12.3 ms                                                     | 13.2 ms: 1.08x slower                                                      |
| json_dumps                 | 5.76 ms                                                     | 6.19 ms: 1.08x slower                                                      |
| docutils                   | 1.57 sec                                                    | 1.70 sec: 1.08x slower                                                     |
| scimark_lu                 | 54.0 ms                                                     | 58.4 ms: 1.08x slower                                                      |
| xml_etree_generate         | 53.3 ms                                                     | 57.9 ms: 1.09x slower                                                      |
| meteor_contest             | 72.3 ms                                                     | 78.9 ms: 1.09x slower                                                      |
| async_tree_io              | 521 ms                                                      | 570 ms: 1.09x slower                                                       |
| async_tree_io_tg           | 512 ms                                                      | 560 ms: 1.09x slower                                                       |
| sqlglot_optimize           | 33.1 ms                                                     | 36.2 ms: 1.09x slower                                                      |
| genshi_xml                 | 32.8 ms                                                     | 36.0 ms: 1.10x slower                                                      |
| pprint_safe_repr           | 493 ms                                                      | 541 ms: 1.10x slower                                                       |
| async_generators           | 223 ms                                                      | 245 ms: 1.10x slower                                                       |
| generators                 | 19.5 ms                                                     | 21.5 ms: 1.10x slower                                                      |
| mako                       | 6.24 ms                                                     | 6.89 ms: 1.10x slower                                                      |
| unpickle                   | 8.63 us                                                     | 9.62 us: 1.11x slower                                                      |
| crypto_pyaes               | 42.8 ms                                                     | 47.8 ms: 1.12x slower                                                      |
| pprint_pformat             | 991 ms                                                      | 1.11 sec: 1.12x slower                                                     |
| spectral_norm              | 59.2 ms                                                     | 66.4 ms: 1.12x slower                                                      |
| logging_simple             | 5.72 us                                                     | 6.43 us: 1.12x slower                                                      |
| logging_format             | 6.15 us                                                     | 6.91 us: 1.12x slower                                                      |
| scimark_fft                | 174 ms                                                      | 196 ms: 1.12x slower                                                       |
| xml_etree_process          | 36.5 ms                                                     | 41.1 ms: 1.12x slower                                                      |
| typing_runtime_protocols   | 100 us                                                      | 113 us: 1.12x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 14.1 ms: 1.13x slower                                                      |
| sqlglot_normalize          | 171 ms                                                      | 193 ms: 1.13x slower                                                       |
| nqueens                    | 55.5 ms                                                     | 63.1 ms: 1.14x slower                                                      |
| chaos                      | 37.9 ms                                                     | 43.1 ms: 1.14x slower                                                      |
| regex_compile              | 80.1 ms                                                     | 91.8 ms: 1.15x slower                                                      |
| scimark_sparse_mat_mult    | 2.34 ms                                                     | 2.69 ms: 1.15x slower                                                      |
| pickle_pure_python         | 183 us                                                      | 210 us: 1.15x slower                                                       |
| genshi_text                | 14.9 ms                                                     | 17.1 ms: 1.15x slower                                                      |
| tomli_loads                | 1.36 sec                                                    | 1.58 sec: 1.16x slower                                                     |
| pyflate                    | 275 ms                                                      | 320 ms: 1.16x slower                                                       |
| comprehensions             | 10.2 us                                                     | 11.9 us: 1.16x slower                                                      |
| sqlglot_transpile          | 952 us                                                      | 1.11 ms: 1.16x slower                                                      |
| float                      | 48.1 ms                                                     | 56.1 ms: 1.17x slower                                                      |
| sqlglot_parse              | 761 us                                                      | 892 us: 1.17x slower                                                       |
| hexiom                     | 3.69 ms                                                     | 4.37 ms: 1.18x slower                                                      |
| unpickle_pure_python       | 127 us                                                      | 151 us: 1.19x slower                                                       |
| django_template            | 21.8 ms                                                     | 26.0 ms: 1.19x slower                                                      |
| fannkuch                   | 245 ms                                                      | 294 ms: 1.20x slower                                                       |
| scimark_monte_carlo        | 40.3 ms                                                     | 48.7 ms: 1.21x slower                                                      |
| logging_silent             | 51.0 ns                                                     | 62.2 ns: 1.22x slower                                                      |
| deltablue                  | 1.86 ms                                                     | 2.28 ms: 1.22x slower                                                      |
| richards_super             | 29.3 ms                                                     | 35.9 ms: 1.22x slower                                                      |
| richards                   | 26.0 ms                                                     | 31.9 ms: 1.23x slower                                                      |
| raytrace                   | 156 ms                                                      | 195 ms: 1.25x slower                                                       |
| scimark_sor                | 72.0 ms                                                     | 89.9 ms: 1.25x slower                                                      |
| nbody                      | 64.5 ms                                                     | 83.7 ms: 1.30x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.04x slower                                                               |

Benchmark hidden because not significant (6): async_tree_none_tg, regex_v8, xml_etree_parse, json_loads, pycparser, pylint
Ignored benchmarks (4) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, flaskblogging, mypy2

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.06x
- 95% likely to have a slowdown of 1.06x
- 99% likely to have a slowdown of 1.05x

# Memory
- memory change: unknown
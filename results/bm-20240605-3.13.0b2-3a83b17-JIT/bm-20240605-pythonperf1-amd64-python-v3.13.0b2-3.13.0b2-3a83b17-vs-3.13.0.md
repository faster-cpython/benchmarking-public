# Results vs. 3.13.0

- fork: python
- ref: v3.13.0b2
- machine: windows-amd64
- commit hash: 3a83b17
- commit date: 2024-06-05
- overall geometric mean: 1.02x slower
- HPT reliability: 98.57%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| 2to3           | 217 ms                                                      | 229 ms: 1.06x slower                                            |
| chameleon      | 4.72 ms                                                     | 5.00 ms: 1.06x slower                                           |
| docutils       | 1.57 sec                                                    | 1.77 sec: 1.13x slower                                          |
| html5lib       | 38.6 ms                                                     | 37.9 ms: 1.02x faster                                           |
| tornado_http   | 92.8 ms                                                     | 86.1 ms: 1.08x faster                                           |
| Geometric mean | (ref)                                                       | 1.03x slower                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|---------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| asyncio_tcp               | 654 ms                                                      | 479 ms: 1.36x faster                                            |
| asyncio_tcp_ssl           | 1.64 sec                                                    | 1.43 sec: 1.14x faster                                          |
| async_tree_memoization_tg | 288 ms                                                      | 273 ms: 1.06x faster                                            |
| async_tree_none           | 223 ms                                                      | 227 ms: 1.02x slower                                            |
| async_tree_none_tg        | 206 ms                                                      | 215 ms: 1.04x slower                                            |
| coroutines                | 12.5 ms                                                     | 13.2 ms: 1.06x slower                                           |
| async_tree_io             | 521 ms                                                      | 579 ms: 1.11x slower                                            |
| async_generators          | 223 ms                                                      | 252 ms: 1.13x slower                                            |
| async_tree_io_tg          | 512 ms                                                      | 624 ms: 1.22x slower                                            |
| Geometric mean            | (ref)                                                       | 1.01x slower                                                    |

Benchmark hidden because not significant (3): async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| nbody          | 64.5 ms                                                     | 53.1 ms: 1.21x faster                                           |
| float          | 48.1 ms                                                     | 44.3 ms: 1.08x faster                                           |
| pidigits       | 148 ms                                                      | 150 ms: 1.01x slower                                            |
| Geometric mean | (ref)                                                       | 1.09x faster                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| regex_effbot   | 1.62 ms                                                     | 1.55 ms: 1.04x faster                                           |
| regex_dna      | 114 ms                                                      | 116 ms: 1.01x slower                                            |
| regex_compile  | 80.1 ms                                                     | 88.9 ms: 1.11x slower                                           |
| Geometric mean | (ref)                                                       | 1.03x slower                                                    |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| tomli_loads          | 1.36 sec                                                    | 1.24 sec: 1.10x faster                                          |
| pickle_pure_python   | 183 us                                                      | 175 us: 1.05x faster                                            |
| xml_etree_generate   | 53.3 ms                                                     | 51.4 ms: 1.04x faster                                           |
| xml_etree_parse      | 93.2 ms                                                     | 90.3 ms: 1.03x faster                                           |
| pickle_dict          | 18.0 us                                                     | 17.6 us: 1.02x faster                                           |
| xml_etree_iterparse  | 62.3 ms                                                     | 61.2 ms: 1.02x faster                                           |
| json_loads           | 14.3 us                                                     | 14.1 us: 1.02x faster                                           |
| json_dumps           | 5.76 ms                                                     | 5.70 ms: 1.01x faster                                           |
| pickle               | 7.34 us                                                     | 7.27 us: 1.01x faster                                           |
| xml_etree_process    | 36.5 ms                                                     | 36.8 ms: 1.01x slower                                           |
| unpickle             | 8.63 us                                                     | 8.73 us: 1.01x slower                                           |
| unpickle_list        | 2.72 us                                                     | 2.78 us: 1.02x slower                                           |
| unpickle_pure_python | 127 us                                                      | 130 us: 1.03x slower                                            |
| Geometric mean       | (ref)                                                       | 1.02x faster                                                    |

Benchmark hidden because not significant (1): pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| python_startup         | 22.2 ms                                                     | 22.7 ms: 1.02x slower                                           |
| python_startup_no_site | 17.8 ms                                                     | 18.6 ms: 1.05x slower                                           |
| Geometric mean         | (ref)                                                       | 1.04x slower                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| mako            | 6.24 ms                                                     | 5.13 ms: 1.22x faster                                           |
| django_template | 21.8 ms                                                     | 25.4 ms: 1.17x slower                                           |
| genshi_text     | 14.9 ms                                                     | 17.9 ms: 1.21x slower                                           |
| genshi_xml      | 32.8 ms                                                     | 44.2 ms: 1.35x slower                                           |
| Geometric mean  | (ref)                                                       | 1.12x slower                                                    |

All benchmarks:
===============

| Benchmark                 | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|---------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| asyncio_tcp               | 654 ms                                                      | 479 ms: 1.36x faster                                            |
| spectral_norm             | 59.2 ms                                                     | 45.3 ms: 1.31x faster                                           |
| mako                      | 6.24 ms                                                     | 5.13 ms: 1.22x faster                                           |
| nbody                     | 64.5 ms                                                     | 53.1 ms: 1.21x faster                                           |
| scimark_fft               | 174 ms                                                      | 150 ms: 1.16x faster                                            |
| asyncio_tcp_ssl           | 1.64 sec                                                    | 1.43 sec: 1.14x faster                                          |
| fannkuch                  | 245 ms                                                      | 215 ms: 1.14x faster                                            |
| tomli_loads               | 1.36 sec                                                    | 1.24 sec: 1.10x faster                                          |
| telco                     | 4.85 ms                                                     | 4.46 ms: 1.09x faster                                           |
| float                     | 48.1 ms                                                     | 44.3 ms: 1.08x faster                                           |
| tornado_http              | 92.8 ms                                                     | 86.1 ms: 1.08x faster                                           |
| pyflate                   | 275 ms                                                      | 257 ms: 1.07x faster                                            |
| pprint_safe_repr          | 493 ms                                                      | 461 ms: 1.07x faster                                            |
| scimark_monte_carlo       | 40.3 ms                                                     | 37.7 ms: 1.07x faster                                           |
| scimark_sparse_mat_mult   | 2.34 ms                                                     | 2.19 ms: 1.07x faster                                           |
| pathlib                   | 81.2 ms                                                     | 76.3 ms: 1.06x faster                                           |
| async_tree_memoization_tg | 288 ms                                                      | 273 ms: 1.06x faster                                            |
| pprint_pformat            | 991 ms                                                      | 946 ms: 1.05x faster                                            |
| pickle_pure_python        | 183 us                                                      | 175 us: 1.05x faster                                            |
| bench_thread_pool         | 828 us                                                      | 793 us: 1.04x faster                                            |
| deepcopy_memo             | 21.8 us                                                     | 20.9 us: 1.04x faster                                           |
| regex_effbot              | 1.62 ms                                                     | 1.55 ms: 1.04x faster                                           |
| xml_etree_generate        | 53.3 ms                                                     | 51.4 ms: 1.04x faster                                           |
| json                      | 2.98 ms                                                     | 2.88 ms: 1.04x faster                                           |
| crypto_pyaes              | 42.8 ms                                                     | 41.5 ms: 1.03x faster                                           |
| xml_etree_parse           | 93.2 ms                                                     | 90.3 ms: 1.03x faster                                           |
| coverage                  | 46.7 ms                                                     | 45.5 ms: 1.03x faster                                           |
| pickle_dict               | 18.0 us                                                     | 17.6 us: 1.02x faster                                           |
| xml_etree_iterparse       | 62.3 ms                                                     | 61.2 ms: 1.02x faster                                           |
| html5lib                  | 38.6 ms                                                     | 37.9 ms: 1.02x faster                                           |
| json_loads                | 14.3 us                                                     | 14.1 us: 1.02x faster                                           |
| json_dumps                | 5.76 ms                                                     | 5.70 ms: 1.01x faster                                           |
| pickle                    | 7.34 us                                                     | 7.27 us: 1.01x faster                                           |
| dulwich_log               | 40.4 ms                                                     | 40.2 ms: 1.00x faster                                           |
| flaskblogging             | 2.04 sec                                                    | 2.03 sec: 1.00x faster                                          |
| meteor_contest            | 72.3 ms                                                     | 72.0 ms: 1.00x faster                                           |
| xml_etree_process         | 36.5 ms                                                     | 36.8 ms: 1.01x slower                                           |
| pidigits                  | 148 ms                                                      | 150 ms: 1.01x slower                                            |
| regex_dna                 | 114 ms                                                      | 116 ms: 1.01x slower                                            |
| unpickle                  | 8.63 us                                                     | 8.73 us: 1.01x slower                                           |
| comprehensions            | 10.2 us                                                     | 10.4 us: 1.01x slower                                           |
| async_tree_none           | 223 ms                                                      | 227 ms: 1.02x slower                                            |
| unpickle_list             | 2.72 us                                                     | 2.78 us: 1.02x slower                                           |
| python_startup            | 22.2 ms                                                     | 22.7 ms: 1.02x slower                                           |
| aiohttp                   | 932 us                                                      | 954 us: 1.02x slower                                            |
| unpickle_pure_python      | 127 us                                                      | 130 us: 1.03x slower                                            |
| logging_simple            | 5.72 us                                                     | 5.91 us: 1.03x slower                                           |
| chaos                     | 37.9 ms                                                     | 39.2 ms: 1.03x slower                                           |
| bench_mp_pool             | 69.6 ms                                                     | 72.0 ms: 1.03x slower                                           |
| logging_format            | 6.15 us                                                     | 6.42 us: 1.04x slower                                           |
| async_tree_none_tg        | 206 ms                                                      | 215 ms: 1.04x slower                                            |
| python_startup_no_site    | 17.8 ms                                                     | 18.6 ms: 1.05x slower                                           |
| sqlglot_parse             | 761 us                                                      | 801 us: 1.05x slower                                            |
| coroutines                | 12.5 ms                                                     | 13.2 ms: 1.06x slower                                           |
| 2to3                      | 217 ms                                                      | 229 ms: 1.06x slower                                            |
| deepcopy_reduce           | 2.02 us                                                     | 2.13 us: 1.06x slower                                           |
| sqlite_synth              | 1.60 us                                                     | 1.69 us: 1.06x slower                                           |
| chameleon                 | 4.72 ms                                                     | 5.00 ms: 1.06x slower                                           |
| thrift                    | 8.68 ms                                                     | 9.21 ms: 1.06x slower                                           |
| deepcopy                  | 223 us                                                      | 241 us: 1.08x slower                                            |
| logging_silent            | 51.0 ns                                                     | 55.3 ns: 1.09x slower                                           |
| sympy_sum                 | 86.4 ms                                                     | 93.9 ms: 1.09x slower                                           |
| generators                | 19.5 ms                                                     | 21.2 ms: 1.09x slower                                           |
| sympy_str                 | 166 ms                                                      | 181 ms: 1.09x slower                                            |
| mdp                       | 1.38 sec                                                    | 1.51 sec: 1.09x slower                                          |
| sqlglot_transpile         | 952 us                                                      | 1.04 ms: 1.09x slower                                           |
| create_gc_cycles          | 829 us                                                      | 912 us: 1.10x slower                                            |
| nqueens                   | 55.5 ms                                                     | 61.4 ms: 1.11x slower                                           |
| regex_compile             | 80.1 ms                                                     | 88.9 ms: 1.11x slower                                           |
| go                        | 84.6 ms                                                     | 93.8 ms: 1.11x slower                                           |
| async_tree_io             | 521 ms                                                      | 579 ms: 1.11x slower                                            |
| sympy_expand              | 285 ms                                                      | 317 ms: 1.11x slower                                            |
| pylint                    | 211 ms                                                      | 235 ms: 1.12x slower                                            |
| sqlglot_optimize          | 33.1 ms                                                     | 37.0 ms: 1.12x slower                                           |
| typing_runtime_protocols  | 100 us                                                      | 113 us: 1.12x slower                                            |
| docutils                  | 1.57 sec                                                    | 1.77 sec: 1.13x slower                                          |
| raytrace                  | 156 ms                                                      | 176 ms: 1.13x slower                                            |
| async_generators          | 223 ms                                                      | 252 ms: 1.13x slower                                            |
| mypy2                     | 429 ms                                                      | 486 ms: 1.13x slower                                            |
| richards                  | 26.0 ms                                                     | 29.7 ms: 1.14x slower                                           |
| richards_super            | 29.3 ms                                                     | 33.5 ms: 1.14x slower                                           |
| sympy_integrate           | 12.3 ms                                                     | 14.1 ms: 1.15x slower                                           |
| scimark_sor               | 72.0 ms                                                     | 83.5 ms: 1.16x slower                                           |
| django_template           | 21.8 ms                                                     | 25.4 ms: 1.17x slower                                           |
| genshi_text               | 14.9 ms                                                     | 17.9 ms: 1.21x slower                                           |
| async_tree_io_tg          | 512 ms                                                      | 624 ms: 1.22x slower                                            |
| deltablue                 | 1.86 ms                                                     | 2.37 ms: 1.27x slower                                           |
| hexiom                    | 3.69 ms                                                     | 4.72 ms: 1.28x slower                                           |
| scimark_lu                | 54.0 ms                                                     | 69.4 ms: 1.28x slower                                           |
| genshi_xml                | 32.8 ms                                                     | 44.2 ms: 1.35x slower                                           |
| Geometric mean            | (ref)                                                       | 1.02x slower                                                    |

Benchmark hidden because not significant (7): pycparser, pickle_list, gc_traversal, async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, async_tree_memoization, regex_v8
Ignored benchmarks (2) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: sqlglot_normalize, unpack_sequence

# HPT report

- Reliability score: 98.57% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown
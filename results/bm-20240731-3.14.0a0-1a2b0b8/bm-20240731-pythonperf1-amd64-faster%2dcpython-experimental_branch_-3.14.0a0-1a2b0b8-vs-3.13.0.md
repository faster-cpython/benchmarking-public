# Results vs. 3.13.0

- fork: faster-cpython
- ref: experimental_branch_
- machine: windows-amd64
- commit hash: 1a2b0b8
- commit date: 2024-07-31
- overall geometric mean: 1.07x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.07x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240731-pythonperf1-amd64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| 2to3           | 217 ms                                                      | 234 ms: 1.08x slower                                                                 |
| docutils       | 1.57 sec                                                    | 1.75 sec: 1.11x slower                                                               |
| html5lib       | 38.6 ms                                                     | 42.3 ms: 1.09x slower                                                                |
| Geometric mean | (ref)                                                       | 1.07x slower                                                                         |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240731-pythonperf1-amd64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|----------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| asyncio_tcp                | 654 ms                                                      | 539 ms: 1.21x faster                                                                 |
| async_tree_memoization_tg  | 288 ms                                                      | 246 ms: 1.17x faster                                                                 |
| async_tree_none_tg         | 206 ms                                                      | 196 ms: 1.05x faster                                                                 |
| async_tree_cpu_io_mixed_tg | 375 ms                                                      | 390 ms: 1.04x slower                                                                 |
| async_tree_io_tg           | 512 ms                                                      | 543 ms: 1.06x slower                                                                 |
| async_generators           | 223 ms                                                      | 244 ms: 1.09x slower                                                                 |
| async_tree_io              | 521 ms                                                      | 573 ms: 1.10x slower                                                                 |
| asyncio_tcp_ssl            | 1.64 sec                                                    | 1.85 sec: 1.13x slower                                                               |
| coroutines                 | 12.5 ms                                                     | 14.3 ms: 1.14x slower                                                                |
| Geometric mean             | (ref)                                                       | 1.01x slower                                                                         |

Benchmark hidden because not significant (3): async_tree_memoization, async_tree_none, async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240731-pythonperf1-amd64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| pidigits       | 148 ms                                                      | 151 ms: 1.02x slower                                                                 |
| float          | 48.1 ms                                                     | 56.6 ms: 1.18x slower                                                                |
| nbody          | 64.5 ms                                                     | 92.0 ms: 1.43x slower                                                                |
| Geometric mean | (ref)                                                       | 1.20x slower                                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240731-pythonperf1-amd64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| regex_effbot   | 1.62 ms                                                     | 1.59 ms: 1.02x faster                                                                |
| regex_v8       | 14.7 ms                                                     | 14.8 ms: 1.01x slower                                                                |
| regex_dna      | 114 ms                                                      | 120 ms: 1.05x slower                                                                 |
| regex_compile  | 80.1 ms                                                     | 95.0 ms: 1.19x slower                                                                |
| Geometric mean | (ref)                                                       | 1.05x slower                                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240731-pythonperf1-amd64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|----------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| json_loads           | 14.3 us                                                     | 14.5 us: 1.01x slower                                                                |
| xml_etree_parse      | 93.2 ms                                                     | 94.8 ms: 1.02x slower                                                                |
| xml_etree_iterparse  | 62.3 ms                                                     | 66.0 ms: 1.06x slower                                                                |
| xml_etree_generate   | 53.3 ms                                                     | 58.1 ms: 1.09x slower                                                                |
| json_dumps           | 5.76 ms                                                     | 6.43 ms: 1.12x slower                                                                |
| xml_etree_process    | 36.5 ms                                                     | 41.1 ms: 1.12x slower                                                                |
| tomli_loads          | 1.36 sec                                                    | 1.61 sec: 1.18x slower                                                               |
| pickle_pure_python   | 183 us                                                      | 217 us: 1.18x slower                                                                 |
| unpickle_pure_python | 127 us                                                      | 157 us: 1.24x slower                                                                 |
| Geometric mean       | (ref)                                                       | 1.11x slower                                                                         |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240731-pythonperf1-amd64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| python_startup         | 22.2 ms                                                     | 21.7 ms: 1.02x faster                                                                |
| python_startup_no_site | 17.8 ms                                                     | 17.4 ms: 1.02x faster                                                                |
| Geometric mean         | (ref)                                                       | 1.02x faster                                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240731-pythonperf1-amd64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|-----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| genshi_xml      | 32.8 ms                                                     | 36.8 ms: 1.12x slower                                                                |
| django_template | 21.8 ms                                                     | 24.7 ms: 1.14x slower                                                                |
| mako            | 6.24 ms                                                     | 7.25 ms: 1.16x slower                                                                |
| genshi_text     | 14.9 ms                                                     | 17.9 ms: 1.21x slower                                                                |
| Geometric mean  | (ref)                                                       | 1.16x slower                                                                         |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240731-pythonperf1-amd64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|----------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| thrift                     | 8.68 ms                                                     | 525 us: 16.53x faster                                                                |
| asyncio_tcp                | 654 ms                                                      | 539 ms: 1.21x faster                                                                 |
| async_tree_memoization_tg  | 288 ms                                                      | 246 ms: 1.17x faster                                                                 |
| deepcopy                   | 223 us                                                      | 192 us: 1.16x faster                                                                 |
| async_tree_none_tg         | 206 ms                                                      | 196 ms: 1.05x faster                                                                 |
| deepcopy_reduce            | 2.02 us                                                     | 1.95 us: 1.04x faster                                                                |
| deepcopy_memo              | 21.8 us                                                     | 21.1 us: 1.03x faster                                                                |
| python_startup             | 22.2 ms                                                     | 21.7 ms: 1.02x faster                                                                |
| bench_thread_pool          | 828 us                                                      | 808 us: 1.02x faster                                                                 |
| regex_effbot               | 1.62 ms                                                     | 1.59 ms: 1.02x faster                                                                |
| python_startup_no_site     | 17.8 ms                                                     | 17.4 ms: 1.02x faster                                                                |
| pathlib                    | 81.2 ms                                                     | 80.5 ms: 1.01x faster                                                                |
| bench_mp_pool              | 69.6 ms                                                     | 69.1 ms: 1.01x faster                                                                |
| json_loads                 | 14.3 us                                                     | 14.5 us: 1.01x slower                                                                |
| regex_v8                   | 14.7 ms                                                     | 14.8 ms: 1.01x slower                                                                |
| coverage                   | 46.7 ms                                                     | 47.4 ms: 1.01x slower                                                                |
| xml_etree_parse            | 93.2 ms                                                     | 94.8 ms: 1.02x slower                                                                |
| telco                      | 4.85 ms                                                     | 4.93 ms: 1.02x slower                                                                |
| pidigits                   | 148 ms                                                      | 151 ms: 1.02x slower                                                                 |
| async_tree_cpu_io_mixed_tg | 375 ms                                                      | 390 ms: 1.04x slower                                                                 |
| regex_dna                  | 114 ms                                                      | 120 ms: 1.05x slower                                                                 |
| mdp                        | 1.38 sec                                                    | 1.46 sec: 1.06x slower                                                               |
| dulwich_log                | 40.4 ms                                                     | 42.7 ms: 1.06x slower                                                                |
| xml_etree_iterparse        | 62.3 ms                                                     | 66.0 ms: 1.06x slower                                                                |
| async_tree_io_tg           | 512 ms                                                      | 543 ms: 1.06x slower                                                                 |
| json                       | 2.98 ms                                                     | 3.17 ms: 1.06x slower                                                                |
| sympy_sum                  | 86.4 ms                                                     | 92.1 ms: 1.07x slower                                                                |
| create_gc_cycles           | 829 us                                                      | 885 us: 1.07x slower                                                                 |
| 2to3                       | 217 ms                                                      | 234 ms: 1.08x slower                                                                 |
| pylint                     | 211 ms                                                      | 229 ms: 1.09x slower                                                                 |
| sympy_expand               | 285 ms                                                      | 311 ms: 1.09x slower                                                                 |
| xml_etree_generate         | 53.3 ms                                                     | 58.1 ms: 1.09x slower                                                                |
| sympy_str                  | 166 ms                                                      | 181 ms: 1.09x slower                                                                 |
| meteor_contest             | 72.3 ms                                                     | 79.0 ms: 1.09x slower                                                                |
| async_generators           | 223 ms                                                      | 244 ms: 1.09x slower                                                                 |
| html5lib                   | 38.6 ms                                                     | 42.3 ms: 1.09x slower                                                                |
| sqlglot_optimize           | 33.1 ms                                                     | 36.3 ms: 1.10x slower                                                                |
| async_tree_io              | 521 ms                                                      | 573 ms: 1.10x slower                                                                 |
| sympy_integrate            | 12.3 ms                                                     | 13.5 ms: 1.10x slower                                                                |
| typing_runtime_protocols   | 100 us                                                      | 112 us: 1.11x slower                                                                 |
| docutils                   | 1.57 sec                                                    | 1.75 sec: 1.11x slower                                                               |
| logging_simple             | 5.72 us                                                     | 6.39 us: 1.12x slower                                                                |
| json_dumps                 | 5.76 ms                                                     | 6.43 ms: 1.12x slower                                                                |
| logging_format             | 6.15 us                                                     | 6.89 us: 1.12x slower                                                                |
| genshi_xml                 | 32.8 ms                                                     | 36.8 ms: 1.12x slower                                                                |
| xml_etree_process          | 36.5 ms                                                     | 41.1 ms: 1.12x slower                                                                |
| asyncio_tcp_ssl            | 1.64 sec                                                    | 1.85 sec: 1.13x slower                                                               |
| generators                 | 19.5 ms                                                     | 22.0 ms: 1.13x slower                                                                |
| sqlglot_normalize          | 171 ms                                                      | 193 ms: 1.13x slower                                                                 |
| django_template            | 21.8 ms                                                     | 24.7 ms: 1.14x slower                                                                |
| coroutines                 | 12.5 ms                                                     | 14.3 ms: 1.14x slower                                                                |
| pprint_safe_repr           | 493 ms                                                      | 569 ms: 1.15x slower                                                                 |
| mako                       | 6.24 ms                                                     | 7.25 ms: 1.16x slower                                                                |
| pprint_pformat             | 991 ms                                                      | 1.16 sec: 1.17x slower                                                               |
| nqueens                    | 55.5 ms                                                     | 64.9 ms: 1.17x slower                                                                |
| float                      | 48.1 ms                                                     | 56.6 ms: 1.18x slower                                                                |
| go                         | 84.6 ms                                                     | 99.7 ms: 1.18x slower                                                                |
| comprehensions             | 10.2 us                                                     | 12.1 us: 1.18x slower                                                                |
| tomli_loads                | 1.36 sec                                                    | 1.61 sec: 1.18x slower                                                               |
| pickle_pure_python         | 183 us                                                      | 217 us: 1.18x slower                                                                 |
| sqlglot_transpile          | 952 us                                                      | 1.13 ms: 1.18x slower                                                                |
| regex_compile              | 80.1 ms                                                     | 95.0 ms: 1.19x slower                                                                |
| chaos                      | 37.9 ms                                                     | 44.9 ms: 1.19x slower                                                                |
| sqlglot_parse              | 761 us                                                      | 906 us: 1.19x slower                                                                 |
| pyflate                    | 275 ms                                                      | 330 ms: 1.20x slower                                                                 |
| genshi_text                | 14.9 ms                                                     | 17.9 ms: 1.21x slower                                                                |
| crypto_pyaes               | 42.8 ms                                                     | 51.8 ms: 1.21x slower                                                                |
| scimark_lu                 | 54.0 ms                                                     | 65.5 ms: 1.21x slower                                                                |
| scimark_fft                | 174 ms                                                      | 212 ms: 1.22x slower                                                                 |
| fannkuch                   | 245 ms                                                      | 301 ms: 1.23x slower                                                                 |
| scimark_sparse_mat_mult    | 2.34 ms                                                     | 2.88 ms: 1.23x slower                                                                |
| deltablue                  | 1.86 ms                                                     | 2.31 ms: 1.24x slower                                                                |
| unpickle_pure_python       | 127 us                                                      | 157 us: 1.24x slower                                                                 |
| hexiom                     | 3.69 ms                                                     | 4.61 ms: 1.25x slower                                                                |
| raytrace                   | 156 ms                                                      | 196 ms: 1.25x slower                                                                 |
| spectral_norm              | 59.2 ms                                                     | 74.1 ms: 1.25x slower                                                                |
| richards                   | 26.0 ms                                                     | 32.8 ms: 1.26x slower                                                                |
| richards_super             | 29.3 ms                                                     | 37.0 ms: 1.26x slower                                                                |
| logging_silent             | 51.0 ns                                                     | 64.4 ns: 1.26x slower                                                                |
| scimark_monte_carlo        | 40.3 ms                                                     | 51.2 ms: 1.27x slower                                                                |
| scimark_sor                | 72.0 ms                                                     | 96.5 ms: 1.34x slower                                                                |
| nbody                      | 64.5 ms                                                     | 92.0 ms: 1.43x slower                                                                |
| Geometric mean             | (ref)                                                       | 1.07x slower                                                                         |

Benchmark hidden because not significant (6): async_tree_memoization, async_tree_none, pycparser, gc_traversal, async_tree_cpu_io_mixed, tornado_http
Ignored benchmarks (11) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.08x
- 95% likely to have a slowdown of 1.08x
- 99% likely to have a slowdown of 1.07x

# Memory
- memory change: unknown
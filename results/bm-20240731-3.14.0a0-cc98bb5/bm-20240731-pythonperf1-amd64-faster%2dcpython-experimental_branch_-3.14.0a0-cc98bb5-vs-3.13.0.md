# Results vs. 3.13.0

- fork: faster-cpython
- ref: experimental_branch_
- machine: windows-amd64
- commit hash: cc98bb5
- commit date: 2024-07-31
- overall geometric mean: 1.06x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240731-pythonperf1-amd64-faster%2dcpython-experimental_branch_-3.14.0a0-cc98bb5 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| 2to3           | 217 ms                                                      | 230 ms: 1.06x slower                                                                 |
| docutils       | 1.57 sec                                                    | 1.74 sec: 1.11x slower                                                               |
| html5lib       | 38.6 ms                                                     | 41.5 ms: 1.08x slower                                                                |
| Geometric mean | (ref)                                                       | 1.06x slower                                                                         |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240731-pythonperf1-amd64-faster%2dcpython-experimental_branch_-3.14.0a0-cc98bb5 |
|----------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| asyncio_tcp                | 654 ms                                                      | 534 ms: 1.22x faster                                                                 |
| async_tree_memoization_tg  | 288 ms                                                      | 247 ms: 1.17x faster                                                                 |
| async_tree_none_tg         | 206 ms                                                      | 195 ms: 1.05x faster                                                                 |
| async_tree_none            | 223 ms                                                      | 217 ms: 1.03x faster                                                                 |
| async_tree_cpu_io_mixed_tg | 375 ms                                                      | 386 ms: 1.03x slower                                                                 |
| async_tree_io_tg           | 512 ms                                                      | 540 ms: 1.05x slower                                                                 |
| async_generators           | 223 ms                                                      | 243 ms: 1.09x slower                                                                 |
| coroutines                 | 12.5 ms                                                     | 14.0 ms: 1.11x slower                                                                |
| async_tree_io              | 521 ms                                                      | 583 ms: 1.12x slower                                                                 |
| Geometric mean             | (ref)                                                       | 1.01x faster                                                                         |

Benchmark hidden because not significant (3): async_tree_memoization, async_tree_cpu_io_mixed, asyncio_tcp_ssl

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240731-pythonperf1-amd64-faster%2dcpython-experimental_branch_-3.14.0a0-cc98bb5 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| pidigits       | 148 ms                                                      | 151 ms: 1.01x slower                                                                 |
| float          | 48.1 ms                                                     | 55.9 ms: 1.16x slower                                                                |
| nbody          | 64.5 ms                                                     | 85.4 ms: 1.32x slower                                                                |
| Geometric mean | (ref)                                                       | 1.16x slower                                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240731-pythonperf1-amd64-faster%2dcpython-experimental_branch_-3.14.0a0-cc98bb5 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| regex_effbot   | 1.62 ms                                                     | 1.59 ms: 1.01x faster                                                                |
| regex_v8       | 14.7 ms                                                     | 15.5 ms: 1.06x slower                                                                |
| regex_dna      | 114 ms                                                      | 123 ms: 1.08x slower                                                                 |
| regex_compile  | 80.1 ms                                                     | 91.8 ms: 1.15x slower                                                                |
| Geometric mean | (ref)                                                       | 1.06x slower                                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240731-pythonperf1-amd64-faster%2dcpython-experimental_branch_-3.14.0a0-cc98bb5 |
|----------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| xml_etree_iterparse  | 62.3 ms                                                     | 65.6 ms: 1.05x slower                                                                |
| json_dumps           | 5.76 ms                                                     | 6.22 ms: 1.08x slower                                                                |
| xml_etree_generate   | 53.3 ms                                                     | 58.4 ms: 1.09x slower                                                                |
| xml_etree_process    | 36.5 ms                                                     | 41.1 ms: 1.12x slower                                                                |
| tomli_loads          | 1.36 sec                                                    | 1.54 sec: 1.13x slower                                                               |
| pickle_pure_python   | 183 us                                                      | 214 us: 1.17x slower                                                                 |
| unpickle_pure_python | 127 us                                                      | 153 us: 1.20x slower                                                                 |
| Geometric mean       | (ref)                                                       | 1.09x slower                                                                         |

Benchmark hidden because not significant (2): json_loads, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240731-pythonperf1-amd64-faster%2dcpython-experimental_branch_-3.14.0a0-cc98bb5 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| python_startup | 22.2 ms                                                     | 21.5 ms: 1.03x faster                                                                |
| Geometric mean | (ref)                                                       | 1.02x faster                                                                         |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240731-pythonperf1-amd64-faster%2dcpython-experimental_branch_-3.14.0a0-cc98bb5 |
|-----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| genshi_xml      | 32.8 ms                                                     | 36.6 ms: 1.12x slower                                                                |
| mako            | 6.24 ms                                                     | 7.06 ms: 1.13x slower                                                                |
| django_template | 21.8 ms                                                     | 24.8 ms: 1.14x slower                                                                |
| genshi_text     | 14.9 ms                                                     | 17.4 ms: 1.17x slower                                                                |
| Geometric mean  | (ref)                                                       | 1.14x slower                                                                         |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240731-pythonperf1-amd64-faster%2dcpython-experimental_branch_-3.14.0a0-cc98bb5 |
|----------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| thrift                     | 8.68 ms                                                     | 531 us: 16.34x faster                                                                |
| asyncio_tcp                | 654 ms                                                      | 534 ms: 1.22x faster                                                                 |
| deepcopy                   | 223 us                                                      | 189 us: 1.18x faster                                                                 |
| async_tree_memoization_tg  | 288 ms                                                      | 247 ms: 1.17x faster                                                                 |
| async_tree_none_tg         | 206 ms                                                      | 195 ms: 1.05x faster                                                                 |
| deepcopy_memo              | 21.8 us                                                     | 20.9 us: 1.05x faster                                                                |
| deepcopy_reduce            | 2.02 us                                                     | 1.94 us: 1.04x faster                                                                |
| python_startup             | 22.2 ms                                                     | 21.5 ms: 1.03x faster                                                                |
| async_tree_none            | 223 ms                                                      | 217 ms: 1.03x faster                                                                 |
| bench_thread_pool          | 828 us                                                      | 808 us: 1.02x faster                                                                 |
| regex_effbot               | 1.62 ms                                                     | 1.59 ms: 1.01x faster                                                                |
| pathlib                    | 81.2 ms                                                     | 80.6 ms: 1.01x faster                                                                |
| pidigits                   | 148 ms                                                      | 151 ms: 1.01x slower                                                                 |
| async_tree_cpu_io_mixed_tg | 375 ms                                                      | 386 ms: 1.03x slower                                                                 |
| telco                      | 4.85 ms                                                     | 5.05 ms: 1.04x slower                                                                |
| mdp                        | 1.38 sec                                                    | 1.44 sec: 1.04x slower                                                               |
| coverage                   | 46.7 ms                                                     | 48.7 ms: 1.04x slower                                                                |
| xml_etree_iterparse        | 62.3 ms                                                     | 65.6 ms: 1.05x slower                                                                |
| async_tree_io_tg           | 512 ms                                                      | 540 ms: 1.05x slower                                                                 |
| json                       | 2.98 ms                                                     | 3.14 ms: 1.05x slower                                                                |
| regex_v8                   | 14.7 ms                                                     | 15.5 ms: 1.06x slower                                                                |
| sympy_sum                  | 86.4 ms                                                     | 91.4 ms: 1.06x slower                                                                |
| 2to3                       | 217 ms                                                      | 230 ms: 1.06x slower                                                                 |
| dulwich_log                | 40.4 ms                                                     | 43.1 ms: 1.07x slower                                                                |
| meteor_contest             | 72.3 ms                                                     | 77.5 ms: 1.07x slower                                                                |
| regex_dna                  | 114 ms                                                      | 123 ms: 1.08x slower                                                                 |
| html5lib                   | 38.6 ms                                                     | 41.5 ms: 1.08x slower                                                                |
| json_dumps                 | 5.76 ms                                                     | 6.22 ms: 1.08x slower                                                                |
| sympy_expand               | 285 ms                                                      | 309 ms: 1.08x slower                                                                 |
| sympy_str                  | 166 ms                                                      | 180 ms: 1.09x slower                                                                 |
| pylint                     | 211 ms                                                      | 229 ms: 1.09x slower                                                                 |
| create_gc_cycles           | 829 us                                                      | 902 us: 1.09x slower                                                                 |
| async_generators           | 223 ms                                                      | 243 ms: 1.09x slower                                                                 |
| sympy_integrate            | 12.3 ms                                                     | 13.4 ms: 1.09x slower                                                                |
| xml_etree_generate         | 53.3 ms                                                     | 58.4 ms: 1.09x slower                                                                |
| sqlglot_optimize           | 33.1 ms                                                     | 36.3 ms: 1.10x slower                                                                |
| generators                 | 19.5 ms                                                     | 21.5 ms: 1.10x slower                                                                |
| docutils                   | 1.57 sec                                                    | 1.74 sec: 1.11x slower                                                               |
| coroutines                 | 12.5 ms                                                     | 14.0 ms: 1.11x slower                                                                |
| genshi_xml                 | 32.8 ms                                                     | 36.6 ms: 1.12x slower                                                                |
| async_tree_io              | 521 ms                                                      | 583 ms: 1.12x slower                                                                 |
| logging_simple             | 5.72 us                                                     | 6.41 us: 1.12x slower                                                                |
| xml_etree_process          | 36.5 ms                                                     | 41.1 ms: 1.12x slower                                                                |
| tomli_loads                | 1.36 sec                                                    | 1.54 sec: 1.13x slower                                                               |
| mako                       | 6.24 ms                                                     | 7.06 ms: 1.13x slower                                                                |
| logging_format             | 6.15 us                                                     | 6.98 us: 1.13x slower                                                                |
| typing_runtime_protocols   | 100 us                                                      | 114 us: 1.14x slower                                                                 |
| django_template            | 21.8 ms                                                     | 24.8 ms: 1.14x slower                                                                |
| sqlglot_normalize          | 171 ms                                                      | 196 ms: 1.14x slower                                                                 |
| pprint_safe_repr           | 493 ms                                                      | 564 ms: 1.15x slower                                                                 |
| regex_compile              | 80.1 ms                                                     | 91.8 ms: 1.15x slower                                                                |
| pprint_pformat             | 991 ms                                                      | 1.15 sec: 1.16x slower                                                               |
| float                      | 48.1 ms                                                     | 55.9 ms: 1.16x slower                                                                |
| genshi_text                | 14.9 ms                                                     | 17.4 ms: 1.17x slower                                                                |
| pickle_pure_python         | 183 us                                                      | 214 us: 1.17x slower                                                                 |
| sqlglot_transpile          | 952 us                                                      | 1.12 ms: 1.18x slower                                                                |
| sqlglot_parse              | 761 us                                                      | 897 us: 1.18x slower                                                                 |
| go                         | 84.6 ms                                                     | 99.9 ms: 1.18x slower                                                                |
| nqueens                    | 55.5 ms                                                     | 65.7 ms: 1.18x slower                                                                |
| chaos                      | 37.9 ms                                                     | 45.0 ms: 1.19x slower                                                                |
| pyflate                    | 275 ms                                                      | 328 ms: 1.19x slower                                                                 |
| scimark_fft                | 174 ms                                                      | 208 ms: 1.19x slower                                                                 |
| unpickle_pure_python       | 127 us                                                      | 153 us: 1.20x slower                                                                 |
| comprehensions             | 10.2 us                                                     | 12.4 us: 1.21x slower                                                                |
| deltablue                  | 1.86 ms                                                     | 2.26 ms: 1.21x slower                                                                |
| richards                   | 26.0 ms                                                     | 31.5 ms: 1.21x slower                                                                |
| spectral_norm              | 59.2 ms                                                     | 71.8 ms: 1.21x slower                                                                |
| richards_super             | 29.3 ms                                                     | 35.7 ms: 1.22x slower                                                                |
| scimark_lu                 | 54.0 ms                                                     | 65.8 ms: 1.22x slower                                                                |
| crypto_pyaes               | 42.8 ms                                                     | 52.2 ms: 1.22x slower                                                                |
| raytrace                   | 156 ms                                                      | 192 ms: 1.23x slower                                                                 |
| scimark_sparse_mat_mult    | 2.34 ms                                                     | 2.87 ms: 1.23x slower                                                                |
| fannkuch                   | 245 ms                                                      | 302 ms: 1.23x slower                                                                 |
| logging_silent             | 51.0 ns                                                     | 63.6 ns: 1.25x slower                                                                |
| hexiom                     | 3.69 ms                                                     | 4.62 ms: 1.25x slower                                                                |
| scimark_monte_carlo        | 40.3 ms                                                     | 52.7 ms: 1.31x slower                                                                |
| scimark_sor                | 72.0 ms                                                     | 94.3 ms: 1.31x slower                                                                |
| nbody                      | 64.5 ms                                                     | 85.4 ms: 1.32x slower                                                                |
| Geometric mean             | (ref)                                                       | 1.06x slower                                                                         |

Benchmark hidden because not significant (10): async_tree_memoization, async_tree_cpu_io_mixed, bench_mp_pool, pycparser, python_startup_no_site, tornado_http, json_loads, xml_etree_parse, gc_traversal, asyncio_tcp_ssl
Ignored benchmarks (11) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.08x
- 95% likely to have a slowdown of 1.07x
- 99% likely to have a slowdown of 1.06x

# Memory
- memory change: unknown
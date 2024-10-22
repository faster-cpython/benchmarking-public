# Results vs. 3.13.0

- fork: python
- ref: 7aca84e557d0a6d242f3
- machine: windows-amd64
- commit hash: 7aca84e
- commit date: 2024-08-02
- overall geometric mean: 1.00x faster
- HPT reliability: 99.16%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240802-pythonperf1-amd64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 217 ms                                                      | 242 ms: 1.11x slower                                                       |
| docutils       | 1.57 sec                                                    | 1.85 sec: 1.18x slower                                                     |
| html5lib       | 38.6 ms                                                     | 42.1 ms: 1.09x slower                                                      |
| tornado_http   | 92.8 ms                                                     | 95.2 ms: 1.03x slower                                                      |
| Geometric mean | (ref)                                                       | 1.10x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240802-pythonperf1-amd64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|---------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_memoization_tg | 288 ms                                                      | 251 ms: 1.15x faster                                                       |
| asyncio_tcp_ssl           | 1.64 sec                                                    | 1.51 sec: 1.09x faster                                                     |
| async_tree_none_tg        | 206 ms                                                      | 194 ms: 1.06x faster                                                       |
| async_tree_none           | 223 ms                                                      | 214 ms: 1.04x faster                                                       |
| asyncio_tcp               | 654 ms                                                      | 632 ms: 1.03x faster                                                       |
| async_tree_cpu_io_mixed   | 387 ms                                                      | 395 ms: 1.02x slower                                                       |
| async_tree_io_tg          | 512 ms                                                      | 540 ms: 1.05x slower                                                       |
| async_tree_io             | 521 ms                                                      | 553 ms: 1.06x slower                                                       |
| coroutines                | 12.5 ms                                                     | 13.8 ms: 1.10x slower                                                      |
| async_generators          | 223 ms                                                      | 261 ms: 1.17x slower                                                       |
| Geometric mean            | (ref)                                                       | 1.00x slower                                                               |

Benchmark hidden because not significant (2): async_tree_memoization, async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240802-pythonperf1-amd64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 64.5 ms                                                     | 50.1 ms: 1.29x faster                                                      |
| float          | 48.1 ms                                                     | 45.0 ms: 1.07x faster                                                      |
| pidigits       | 148 ms                                                      | 150 ms: 1.01x slower                                                       |
| Geometric mean | (ref)                                                       | 1.11x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240802-pythonperf1-amd64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_v8       | 14.7 ms                                                     | 14.9 ms: 1.02x slower                                                      |
| regex_dna      | 114 ms                                                      | 119 ms: 1.04x slower                                                       |
| regex_compile  | 80.1 ms                                                     | 91.0 ms: 1.14x slower                                                      |
| Geometric mean | (ref)                                                       | 1.05x slower                                                               |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240802-pythonperf1-amd64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| tomli_loads          | 1.36 sec                                                    | 1.26 sec: 1.08x faster                                                     |
| xml_etree_generate   | 53.3 ms                                                     | 52.6 ms: 1.01x faster                                                      |
| xml_etree_iterparse  | 62.3 ms                                                     | 61.8 ms: 1.01x faster                                                      |
| pickle_pure_python   | 183 us                                                      | 182 us: 1.01x faster                                                       |
| xml_etree_parse      | 93.2 ms                                                     | 95.5 ms: 1.02x slower                                                      |
| xml_etree_process    | 36.5 ms                                                     | 37.6 ms: 1.03x slower                                                      |
| json_dumps           | 5.76 ms                                                     | 5.96 ms: 1.03x slower                                                      |
| unpickle_pure_python | 127 us                                                      | 138 us: 1.09x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.01x slower                                                               |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240802-pythonperf1-amd64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 22.2 ms                                                     | 22.0 ms: 1.01x faster                                                      |
| python_startup_no_site | 17.8 ms                                                     | 18.4 ms: 1.04x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.01x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240802-pythonperf1-amd64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 6.24 ms                                                     | 5.05 ms: 1.24x faster                                                      |
| django_template | 21.8 ms                                                     | 25.7 ms: 1.18x slower                                                      |
| genshi_text     | 14.9 ms                                                     | 17.9 ms: 1.21x slower                                                      |
| genshi_xml      | 32.8 ms                                                     | 40.0 ms: 1.22x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.09x slower                                                               |

All benchmarks:
===============

| Benchmark                 | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240802-pythonperf1-amd64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|---------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| thrift                    | 8.68 ms                                                     | 520 us: 16.68x faster                                                      |
| deepcopy_memo             | 21.8 us                                                     | 15.7 us: 1.39x faster                                                      |
| spectral_norm             | 59.2 ms                                                     | 45.0 ms: 1.31x faster                                                      |
| nbody                     | 64.5 ms                                                     | 50.1 ms: 1.29x faster                                                      |
| mako                      | 6.24 ms                                                     | 5.05 ms: 1.24x faster                                                      |
| scimark_sor               | 72.0 ms                                                     | 60.4 ms: 1.19x faster                                                      |
| scimark_fft               | 174 ms                                                      | 147 ms: 1.19x faster                                                       |
| deepcopy                  | 223 us                                                      | 193 us: 1.16x faster                                                       |
| async_tree_memoization_tg | 288 ms                                                      | 251 ms: 1.15x faster                                                       |
| fannkuch                  | 245 ms                                                      | 214 ms: 1.14x faster                                                       |
| scimark_sparse_mat_mult   | 2.34 ms                                                     | 2.10 ms: 1.11x faster                                                      |
| pyflate                   | 275 ms                                                      | 251 ms: 1.10x faster                                                       |
| deepcopy_reduce           | 2.02 us                                                     | 1.85 us: 1.09x faster                                                      |
| asyncio_tcp_ssl           | 1.64 sec                                                    | 1.51 sec: 1.09x faster                                                     |
| tomli_loads               | 1.36 sec                                                    | 1.26 sec: 1.08x faster                                                     |
| float                     | 48.1 ms                                                     | 45.0 ms: 1.07x faster                                                      |
| crypto_pyaes              | 42.8 ms                                                     | 40.3 ms: 1.06x faster                                                      |
| async_tree_none_tg        | 206 ms                                                      | 194 ms: 1.06x faster                                                       |
| telco                     | 4.85 ms                                                     | 4.61 ms: 1.05x faster                                                      |
| async_tree_none           | 223 ms                                                      | 214 ms: 1.04x faster                                                       |
| asyncio_tcp               | 654 ms                                                      | 632 ms: 1.03x faster                                                       |
| pprint_safe_repr          | 493 ms                                                      | 484 ms: 1.02x faster                                                       |
| xml_etree_generate        | 53.3 ms                                                     | 52.6 ms: 1.01x faster                                                      |
| python_startup            | 22.2 ms                                                     | 22.0 ms: 1.01x faster                                                      |
| xml_etree_iterparse       | 62.3 ms                                                     | 61.8 ms: 1.01x faster                                                      |
| meteor_contest            | 72.3 ms                                                     | 71.8 ms: 1.01x faster                                                      |
| pickle_pure_python        | 183 us                                                      | 182 us: 1.01x faster                                                       |
| pidigits                  | 148 ms                                                      | 150 ms: 1.01x slower                                                       |
| gc_traversal              | 1.55 ms                                                     | 1.57 ms: 1.01x slower                                                      |
| regex_v8                  | 14.7 ms                                                     | 14.9 ms: 1.02x slower                                                      |
| async_tree_cpu_io_mixed   | 387 ms                                                      | 395 ms: 1.02x slower                                                       |
| coverage                  | 46.7 ms                                                     | 47.7 ms: 1.02x slower                                                      |
| xml_etree_parse           | 93.2 ms                                                     | 95.5 ms: 1.02x slower                                                      |
| tornado_http              | 92.8 ms                                                     | 95.2 ms: 1.03x slower                                                      |
| xml_etree_process         | 36.5 ms                                                     | 37.6 ms: 1.03x slower                                                      |
| comprehensions            | 10.2 us                                                     | 10.6 us: 1.03x slower                                                      |
| json_dumps                | 5.76 ms                                                     | 5.96 ms: 1.03x slower                                                      |
| python_startup_no_site    | 17.8 ms                                                     | 18.4 ms: 1.04x slower                                                      |
| logging_simple            | 5.72 us                                                     | 5.94 us: 1.04x slower                                                      |
| logging_format            | 6.15 us                                                     | 6.39 us: 1.04x slower                                                      |
| regex_dna                 | 114 ms                                                      | 119 ms: 1.04x slower                                                       |
| chaos                     | 37.9 ms                                                     | 39.9 ms: 1.05x slower                                                      |
| async_tree_io_tg          | 512 ms                                                      | 540 ms: 1.05x slower                                                       |
| bench_mp_pool             | 69.6 ms                                                     | 73.7 ms: 1.06x slower                                                      |
| async_tree_io             | 521 ms                                                      | 553 ms: 1.06x slower                                                       |
| mdp                       | 1.38 sec                                                    | 1.47 sec: 1.06x slower                                                     |
| dulwich_log               | 40.4 ms                                                     | 43.4 ms: 1.07x slower                                                      |
| unpickle_pure_python      | 127 us                                                      | 138 us: 1.09x slower                                                       |
| html5lib                  | 38.6 ms                                                     | 42.1 ms: 1.09x slower                                                      |
| coroutines                | 12.5 ms                                                     | 13.8 ms: 1.10x slower                                                      |
| sqlglot_parse             | 761 us                                                      | 838 us: 1.10x slower                                                       |
| 2to3                      | 217 ms                                                      | 242 ms: 1.11x slower                                                       |
| sqlglot_optimize          | 33.1 ms                                                     | 36.9 ms: 1.12x slower                                                      |
| create_gc_cycles          | 829 us                                                      | 925 us: 1.12x slower                                                       |
| logging_silent            | 51.0 ns                                                     | 57.2 ns: 1.12x slower                                                      |
| nqueens                   | 55.5 ms                                                     | 62.7 ms: 1.13x slower                                                      |
| sqlglot_normalize         | 171 ms                                                      | 194 ms: 1.13x slower                                                       |
| regex_compile             | 80.1 ms                                                     | 91.0 ms: 1.14x slower                                                      |
| sympy_sum                 | 86.4 ms                                                     | 98.4 ms: 1.14x slower                                                      |
| sqlglot_transpile         | 952 us                                                      | 1.09 ms: 1.14x slower                                                      |
| sympy_str                 | 166 ms                                                      | 192 ms: 1.15x slower                                                       |
| generators                | 19.5 ms                                                     | 22.5 ms: 1.16x slower                                                      |
| typing_runtime_protocols  | 100 us                                                      | 116 us: 1.16x slower                                                       |
| async_generators          | 223 ms                                                      | 261 ms: 1.17x slower                                                       |
| richards                  | 26.0 ms                                                     | 30.4 ms: 1.17x slower                                                      |
| sympy_expand              | 285 ms                                                      | 334 ms: 1.17x slower                                                       |
| docutils                  | 1.57 sec                                                    | 1.85 sec: 1.18x slower                                                     |
| pylint                    | 211 ms                                                      | 248 ms: 1.18x slower                                                       |
| django_template           | 21.8 ms                                                     | 25.7 ms: 1.18x slower                                                      |
| richards_super            | 29.3 ms                                                     | 35.0 ms: 1.19x slower                                                      |
| go                        | 84.6 ms                                                     | 102 ms: 1.20x slower                                                       |
| genshi_text               | 14.9 ms                                                     | 17.9 ms: 1.21x slower                                                      |
| sympy_integrate           | 12.3 ms                                                     | 14.9 ms: 1.21x slower                                                      |
| raytrace                  | 156 ms                                                      | 190 ms: 1.22x slower                                                       |
| genshi_xml                | 32.8 ms                                                     | 40.0 ms: 1.22x slower                                                      |
| deltablue                 | 1.86 ms                                                     | 2.34 ms: 1.25x slower                                                      |
| hexiom                    | 3.69 ms                                                     | 4.79 ms: 1.30x slower                                                      |
| Geometric mean            | (ref)                                                       | 1.00x faster                                                               |

Benchmark hidden because not significant (11): async_tree_memoization, scimark_monte_carlo, regex_effbot, json_loads, bench_thread_pool, scimark_lu, pprint_pformat, json, pathlib, async_tree_cpu_io_mixed_tg, pycparser
Ignored benchmarks (11) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 99.16% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown
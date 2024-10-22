# Results vs. 3.13.0

- fork: python
- ref: a9d56e38a08ec198a228
- machine: windows-amd64
- commit hash: a9d56e3
- commit date: 2024-08-01
- overall geometric mean: 1.00x slower
- HPT reliability: 99.62%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240801-pythonperf1-amd64-python-a9d56e38a08ec198a228-3.14.0a0-a9d56e3 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 217 ms                                                      | 240 ms: 1.11x slower                                                       |
| docutils       | 1.57 sec                                                    | 1.85 sec: 1.17x slower                                                     |
| html5lib       | 38.6 ms                                                     | 42.0 ms: 1.09x slower                                                      |
| tornado_http   | 92.8 ms                                                     | 95.5 ms: 1.03x slower                                                      |
| Geometric mean | (ref)                                                       | 1.10x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240801-pythonperf1-amd64-python-a9d56e38a08ec198a228-3.14.0a0-a9d56e3 |
|---------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| asyncio_tcp               | 654 ms                                                      | 555 ms: 1.18x faster                                                       |
| asyncio_tcp_ssl           | 1.64 sec                                                    | 1.42 sec: 1.16x faster                                                     |
| async_tree_memoization_tg | 288 ms                                                      | 250 ms: 1.15x faster                                                       |
| async_tree_none_tg        | 206 ms                                                      | 194 ms: 1.06x faster                                                       |
| async_tree_none           | 223 ms                                                      | 212 ms: 1.05x faster                                                       |
| async_tree_memoization    | 271 ms                                                      | 261 ms: 1.04x faster                                                       |
| async_tree_cpu_io_mixed   | 387 ms                                                      | 393 ms: 1.02x slower                                                       |
| async_tree_io             | 521 ms                                                      | 545 ms: 1.05x slower                                                       |
| async_tree_io_tg          | 512 ms                                                      | 537 ms: 1.05x slower                                                       |
| coroutines                | 12.5 ms                                                     | 13.7 ms: 1.09x slower                                                      |
| async_generators          | 223 ms                                                      | 261 ms: 1.17x slower                                                       |
| Geometric mean            | (ref)                                                       | 1.02x faster                                                               |

Benchmark hidden because not significant (1): async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240801-pythonperf1-amd64-python-a9d56e38a08ec198a228-3.14.0a0-a9d56e3 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 64.5 ms                                                     | 51.5 ms: 1.25x faster                                                      |
| float          | 48.1 ms                                                     | 45.4 ms: 1.06x faster                                                      |
| pidigits       | 148 ms                                                      | 150 ms: 1.01x slower                                                       |
| Geometric mean | (ref)                                                       | 1.09x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240801-pythonperf1-amd64-python-a9d56e38a08ec198a228-3.14.0a0-a9d56e3 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_effbot   | 1.62 ms                                                     | 1.59 ms: 1.01x faster                                                      |
| regex_dna      | 114 ms                                                      | 118 ms: 1.03x slower                                                       |
| regex_compile  | 80.1 ms                                                     | 91.7 ms: 1.14x slower                                                      |
| Geometric mean | (ref)                                                       | 1.04x slower                                                               |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240801-pythonperf1-amd64-python-a9d56e38a08ec198a228-3.14.0a0-a9d56e3 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| tomli_loads          | 1.36 sec                                                    | 1.26 sec: 1.08x faster                                                     |
| xml_etree_generate   | 53.3 ms                                                     | 52.3 ms: 1.02x faster                                                      |
| xml_etree_parse      | 93.2 ms                                                     | 92.5 ms: 1.01x faster                                                      |
| json_loads           | 14.3 us                                                     | 14.6 us: 1.02x slower                                                      |
| xml_etree_process    | 36.5 ms                                                     | 37.8 ms: 1.03x slower                                                      |
| json_dumps           | 5.76 ms                                                     | 5.99 ms: 1.04x slower                                                      |
| unpickle_pure_python | 127 us                                                      | 137 us: 1.08x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.01x slower                                                               |

Benchmark hidden because not significant (2): xml_etree_iterparse, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240801-pythonperf1-amd64-python-a9d56e38a08ec198a228-3.14.0a0-a9d56e3 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup | 22.2 ms                                                     | 22.0 ms: 1.01x faster                                                      |
| Geometric mean | (ref)                                                       | 1.00x faster                                                               |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240801-pythonperf1-amd64-python-a9d56e38a08ec198a228-3.14.0a0-a9d56e3 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 6.24 ms                                                     | 4.97 ms: 1.26x faster                                                      |
| django_template | 21.8 ms                                                     | 25.9 ms: 1.19x slower                                                      |
| genshi_xml      | 32.8 ms                                                     | 40.9 ms: 1.25x slower                                                      |
| genshi_text     | 14.9 ms                                                     | 18.7 ms: 1.26x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.10x slower                                                               |

All benchmarks:
===============

| Benchmark                 | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240801-pythonperf1-amd64-python-a9d56e38a08ec198a228-3.14.0a0-a9d56e3 |
|---------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| thrift                    | 8.68 ms                                                     | 533 us: 16.27x faster                                                      |
| deepcopy_memo             | 21.8 us                                                     | 16.1 us: 1.36x faster                                                      |
| spectral_norm             | 59.2 ms                                                     | 45.8 ms: 1.29x faster                                                      |
| mako                      | 6.24 ms                                                     | 4.97 ms: 1.26x faster                                                      |
| nbody                     | 64.5 ms                                                     | 51.5 ms: 1.25x faster                                                      |
| deepcopy                  | 223 us                                                      | 185 us: 1.21x faster                                                       |
| scimark_fft               | 174 ms                                                      | 147 ms: 1.19x faster                                                       |
| asyncio_tcp               | 654 ms                                                      | 555 ms: 1.18x faster                                                       |
| asyncio_tcp_ssl           | 1.64 sec                                                    | 1.42 sec: 1.16x faster                                                     |
| async_tree_memoization_tg | 288 ms                                                      | 250 ms: 1.15x faster                                                       |
| fannkuch                  | 245 ms                                                      | 215 ms: 1.14x faster                                                       |
| scimark_sparse_mat_mult   | 2.34 ms                                                     | 2.07 ms: 1.13x faster                                                      |
| pyflate                   | 275 ms                                                      | 247 ms: 1.12x faster                                                       |
| deepcopy_reduce           | 2.02 us                                                     | 1.82 us: 1.11x faster                                                      |
| crypto_pyaes              | 42.8 ms                                                     | 39.4 ms: 1.09x faster                                                      |
| tomli_loads               | 1.36 sec                                                    | 1.26 sec: 1.08x faster                                                     |
| telco                     | 4.85 ms                                                     | 4.54 ms: 1.07x faster                                                      |
| async_tree_none_tg        | 206 ms                                                      | 194 ms: 1.06x faster                                                       |
| float                     | 48.1 ms                                                     | 45.4 ms: 1.06x faster                                                      |
| scimark_monte_carlo       | 40.3 ms                                                     | 38.0 ms: 1.06x faster                                                      |
| async_tree_none           | 223 ms                                                      | 212 ms: 1.05x faster                                                       |
| async_tree_memoization    | 271 ms                                                      | 261 ms: 1.04x faster                                                       |
| meteor_contest            | 72.3 ms                                                     | 70.7 ms: 1.02x faster                                                      |
| xml_etree_generate        | 53.3 ms                                                     | 52.3 ms: 1.02x faster                                                      |
| pprint_safe_repr          | 493 ms                                                      | 484 ms: 1.02x faster                                                       |
| regex_effbot              | 1.62 ms                                                     | 1.59 ms: 1.01x faster                                                      |
| python_startup            | 22.2 ms                                                     | 22.0 ms: 1.01x faster                                                      |
| xml_etree_parse           | 93.2 ms                                                     | 92.5 ms: 1.01x faster                                                      |
| pidigits                  | 148 ms                                                      | 150 ms: 1.01x slower                                                       |
| gc_traversal              | 1.55 ms                                                     | 1.58 ms: 1.01x slower                                                      |
| async_tree_cpu_io_mixed   | 387 ms                                                      | 393 ms: 1.02x slower                                                       |
| json_loads                | 14.3 us                                                     | 14.6 us: 1.02x slower                                                      |
| coverage                  | 46.7 ms                                                     | 47.7 ms: 1.02x slower                                                      |
| tornado_http              | 92.8 ms                                                     | 95.5 ms: 1.03x slower                                                      |
| json                      | 2.98 ms                                                     | 3.07 ms: 1.03x slower                                                      |
| regex_dna                 | 114 ms                                                      | 118 ms: 1.03x slower                                                       |
| xml_etree_process         | 36.5 ms                                                     | 37.8 ms: 1.03x slower                                                      |
| json_dumps                | 5.76 ms                                                     | 5.99 ms: 1.04x slower                                                      |
| chaos                     | 37.9 ms                                                     | 39.4 ms: 1.04x slower                                                      |
| async_tree_io             | 521 ms                                                      | 545 ms: 1.05x slower                                                       |
| mdp                       | 1.38 sec                                                    | 1.45 sec: 1.05x slower                                                     |
| async_tree_io_tg          | 512 ms                                                      | 537 ms: 1.05x slower                                                       |
| bench_mp_pool             | 69.6 ms                                                     | 73.0 ms: 1.05x slower                                                      |
| logging_simple            | 5.72 us                                                     | 6.06 us: 1.06x slower                                                      |
| logging_format            | 6.15 us                                                     | 6.53 us: 1.06x slower                                                      |
| dulwich_log               | 40.4 ms                                                     | 43.1 ms: 1.07x slower                                                      |
| unpickle_pure_python      | 127 us                                                      | 137 us: 1.08x slower                                                       |
| html5lib                  | 38.6 ms                                                     | 42.0 ms: 1.09x slower                                                      |
| coroutines                | 12.5 ms                                                     | 13.7 ms: 1.09x slower                                                      |
| create_gc_cycles          | 829 us                                                      | 912 us: 1.10x slower                                                       |
| 2to3                      | 217 ms                                                      | 240 ms: 1.11x slower                                                       |
| sqlglot_parse             | 761 us                                                      | 844 us: 1.11x slower                                                       |
| sqlglot_optimize          | 33.1 ms                                                     | 36.8 ms: 1.11x slower                                                      |
| sympy_sum                 | 86.4 ms                                                     | 96.3 ms: 1.11x slower                                                      |
| nqueens                   | 55.5 ms                                                     | 62.3 ms: 1.12x slower                                                      |
| sqlglot_normalize         | 171 ms                                                      | 192 ms: 1.12x slower                                                       |
| sqlglot_transpile         | 952 us                                                      | 1.08 ms: 1.13x slower                                                      |
| sympy_str                 | 166 ms                                                      | 189 ms: 1.14x slower                                                       |
| regex_compile             | 80.1 ms                                                     | 91.7 ms: 1.14x slower                                                      |
| logging_silent            | 51.0 ns                                                     | 58.7 ns: 1.15x slower                                                      |
| sympy_expand              | 285 ms                                                      | 330 ms: 1.16x slower                                                       |
| async_generators          | 223 ms                                                      | 261 ms: 1.17x slower                                                       |
| typing_runtime_protocols  | 100 us                                                      | 118 us: 1.17x slower                                                       |
| docutils                  | 1.57 sec                                                    | 1.85 sec: 1.17x slower                                                     |
| generators                | 19.5 ms                                                     | 23.0 ms: 1.18x slower                                                      |
| django_template           | 21.8 ms                                                     | 25.9 ms: 1.19x slower                                                      |
| go                        | 84.6 ms                                                     | 101 ms: 1.19x slower                                                       |
| sympy_integrate           | 12.3 ms                                                     | 14.7 ms: 1.20x slower                                                      |
| pylint                    | 211 ms                                                      | 254 ms: 1.20x slower                                                       |
| richards                  | 26.0 ms                                                     | 31.5 ms: 1.21x slower                                                      |
| richards_super            | 29.3 ms                                                     | 35.6 ms: 1.21x slower                                                      |
| raytrace                  | 156 ms                                                      | 192 ms: 1.23x slower                                                       |
| genshi_xml                | 32.8 ms                                                     | 40.9 ms: 1.25x slower                                                      |
| genshi_text               | 14.9 ms                                                     | 18.7 ms: 1.26x slower                                                      |
| deltablue                 | 1.86 ms                                                     | 2.35 ms: 1.26x slower                                                      |
| scimark_sor               | 72.0 ms                                                     | 92.7 ms: 1.29x slower                                                      |
| hexiom                    | 3.69 ms                                                     | 4.83 ms: 1.31x slower                                                      |
| scimark_lu                | 54.0 ms                                                     | 75.2 ms: 1.39x slower                                                      |
| Geometric mean            | (ref)                                                       | 1.00x slower                                                               |

Benchmark hidden because not significant (10): bench_thread_pool, xml_etree_iterparse, pathlib, python_startup_no_site, pickle_pure_python, comprehensions, regex_v8, pprint_pformat, async_tree_cpu_io_mixed_tg, pycparser
Ignored benchmarks (11) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 99.62% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown